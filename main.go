package main

import (
	"encoding/json"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"sync"

	"tafsir_go/internal/strategies"
	"tafsir_go/internal/tafsir"
	internal "tafsir_go/internal/types"
)

const (
	// EditionsJSONFile = "data/test_edition.json"
	EditionsJSONFile = "data/editions.json"
	AyahDataJSONFile = "data/ayah_data.json"
	TafsirDir        = "tafsir"
	EmptyAyahsFile   = "empty_ayahs.json"
	AltafsirWorkers  = 20 // Number of concurrent workers for AltafsirStrategy
	QuranWorkers     = 20 // Number of concurrent workers for QuranStrategy (including after Altafsir)
)

func main() {
	processedAyahs := sync.Map{}
	// Load editions data.
	tafsirData, err := loadTafsirData(EditionsJSONFile)
	if err != nil {
		log.Fatalf("Error loading tafsir data: %v", err)
	}

	var wg sync.WaitGroup

	// Start AltafsirStrategy workers.
	wg.Add(1)
	go func() {
		defer wg.Done()
		fmt.Println("Altafsir Workers started")

		altafsirDone := make(chan struct{}, AltafsirWorkers) // Channel to signal completion of each altafsir worker

		// Start AltafsirStrategy workers concurrently.
		for i := 0; i < AltafsirWorkers; i++ {
			go func(workerNum int) {
				fmt.Printf("Altafsir Worker %d started\n", workerNum)
				processTafsirData(tafsirData, "https://www.altafsir.com/", workerNum, &processedAyahs)
				fmt.Printf("Altafsir Worker %d finished\n", workerNum)
				altafsirDone <- struct{}{} // Signal completion
			}(i)
		}

		// Wait for all AltafsirStrategy workers to finish.
		for i := 0; i < AltafsirWorkers; i++ {
			<-altafsirDone
		}

		fmt.Println("Altafsir Workers are done")
	}()

	// Start QuranStrategy workers concurrently.
	wg.Add(1)
	go func() {
		defer wg.Done()
		fmt.Println("QuranStrategy Workers started")

		quranDone := make(chan struct{}, QuranWorkers) // Channel to signal completion of each quran worker

		// Start QuranStrategy workers concurrently.
		for i := 0; i < QuranWorkers; i++ {
			go func(workerNum int) {
				fmt.Printf("QuranStrategy Worker %d started\n", workerNum)
				processTafsirData(tafsirData, "https://quran.com/", workerNum, &processedAyahs)
				fmt.Printf("QuranStrategy Worker %d finished\n", workerNum)
				quranDone <- struct{}{} // Signal completion
			}(i)
		}

		// Wait for all QuranStrategy workers to finish.
		for i := 0; i < QuranWorkers; i++ {
			<-quranDone
		}

		fmt.Println("QuranStrategy Workers are done")
	}()

	wg.Wait() // Wait for both groups of workers to complete
	fmt.Println("All Workers are done")
}

func processTafsirData(tafsirData []tafsir.Tafsir, source string, workerNum int, processedAyahs *sync.Map) {
	for _, selectedTafsir := range tafsirData {
		if selectedTafsir.Source == source {
			strategy, err := selectStrategy(source)
			if err != nil {
				log.Printf("Worker %d: Error selecting strategy: %v", workerNum, err)
				continue
			}

			// Load ayah data.
			ayahData, err := loadAyahData(AyahDataJSONFile)
			if err != nil {
				log.Printf("Worker %d: Error loading ayah data: %v", workerNum, err)
				continue
			}

			// Process ayahs.
			err = processAyahs(selectedTafsir, strategy, ayahData, processedAyahs)
			if err != nil {
				log.Printf("Worker %d: Error processing ayahs: %v", workerNum, err)
			}
		}
	}
}

func processAyahs(selectedTafsir tafsir.Tafsir, strategy strategies.Strategy, ayahData internal.SurahAyahs, processedAyahs *sync.Map) error {
	for _, surahAyah := range ayahData {
		var emptyAyahs []internal.EmptyAyah

		for i := 1; i <= surahAyah.Ayah; i++ {
			// Generate a unique key for the ayah based on surah and ayah number
			ayahKey := fmt.Sprintf("%d-%d-%d", selectedTafsir.ID, surahAyah.Surah, i)

			// Check if this ayah has already been processed by another worker
			if _, alreadyProcessed := processedAyahs.LoadOrStore(ayahKey, true); alreadyProcessed {
				log.Printf("Ayah %s for Tafsir %s has already been processed", ayahKey, selectedTafsir.Name)
				continue
			}

			if isDuplicateOrEmpty(selectedTafsir.Slug, surahAyah.Surah, i) {
				log.Printf("Duplicate or empty ayah\nSurah: %d\nAyah: %d\n for Tafsir: %s", surahAyah.Surah, i, selectedTafsir.Name)
				continue
			}

			ayah, err := strategy.GetAyah(i, surahAyah.Surah, int(selectedTafsir.ID))
			if err != nil {
				return err
			}
			if ayah == "" {
				println("Empty ayah", i, "of surah", surahAyah.Surah, "for tafsir", selectedTafsir.Name)
				emptyAyahs = append(emptyAyahs, internal.EmptyAyah{Surah: surahAyah.Surah, Ayah: i})
			} else {
				println("Downloaded ayah", i, "of surah", surahAyah.Surah, "for tafsir", selectedTafsir.Name)
				err := saveAyahToFile(selectedTafsir.Slug, surahAyah.Surah, i, ayah)
				if err != nil {
					return err
				}
			}
		}

		err := handleEmptyAyahs(selectedTafsir.Slug, surahAyah.Surah, emptyAyahs)
		if err != nil {
			return err
		}
	}

	return nil
}

func loadTafsirData(filePath string) ([]tafsir.Tafsir, error) {
	editionFile, err := os.ReadFile(filePath)
	if err != nil {
		return nil, err
	}
	var tafsirData []tafsir.Tafsir // Change the type here
	err = json.Unmarshal(editionFile, &tafsirData)
	if err != nil {
		return nil, err
	}
	return tafsirData, nil
}

func selectStrategy(source string) (strategies.Strategy, error) {
	var strategy strategies.Strategy

	switch source {
	case "https://quran.com/":
		strategy = &strategies.QuranStrategy{}
	case "https://www.altafsir.com/":
		strategy = &strategies.AltafsirStrategy{}
	default:
		return nil, fmt.Errorf("Unknown source: %s", source)
	}

	return strategy, nil
}

func loadAyahData(filePath string) (internal.SurahAyahs, error) {
	ayahDataFile, err := os.ReadFile(filePath)
	if err != nil {
		return nil, err
	}
	var ayahData internal.SurahAyahs
	err = json.Unmarshal(ayahDataFile, &ayahData)
	if err != nil {
		return nil, err
	}
	return ayahData, nil
}

func isDuplicateOrEmpty(tafsirSlug string, surah, ayah int) bool {
	// Check if empty_ayahs.json exists and load it
	emptyFilePath := filepath.Join(TafsirDir, tafsirSlug, fmt.Sprintf("%d", surah), EmptyAyahsFile)
	if _, err := os.Stat(emptyFilePath); err == nil {
		emptyJSON, err := os.ReadFile(emptyFilePath)
		if err != nil {
			log.Printf("Error reading empty_ayahs.json: %v", err)
			return false
		}

		var emptyAyahs []internal.EmptyAyah
		err = json.Unmarshal(emptyJSON, &emptyAyahs)
		if err != nil {
			log.Printf("Error unmarshalling empty_ayahs.json: %v", err)
			return false
		}

		// Check if the ayah is in emptyAyahs
		for _, emptyAyah := range emptyAyahs {
			if emptyAyah.Surah == surah && emptyAyah.Ayah == ayah {
				return true
			}
		}
	}

	// Check if the ayah is already downloaded
	filePath := filepath.Join(TafsirDir, tafsirSlug, fmt.Sprintf("%d", surah), fmt.Sprintf("%d.json", ayah))
	if _, err := os.Stat(filePath); err == nil {
		return true
	}

	return false
}

func saveAyahToFile(tafsirSlug string, surah, ayah int, text string) error {
	var ayahData internal.AyahData
	ayahData.Ayah = ayah
	ayahData.Surah = surah
	ayahData.Text = text

	ayahDataJSON, err := json.Marshal(ayahData)
	if err != nil {
		return err
	}

	// Define the directory path where you want to save the JSON files
	saveDir := filepath.Join(TafsirDir, tafsirSlug, fmt.Sprintf("%d", surah))
	if err := os.MkdirAll(saveDir, os.ModePerm); err != nil {
		return err
	}

	// Define the file path
	filePath := filepath.Join(saveDir, fmt.Sprintf("%d.json", ayah))

	// Create and write the JSON file
	file, err := os.Create(filePath)
	if err != nil {
		return err
	}
	defer file.Close()

	_, err = file.Write(ayahDataJSON)
	if err != nil {
		return err
	}

	return nil
}

func handleEmptyAyahs(selectedTafsirSlug string, surah int, emptyAyahs []internal.EmptyAyah) error {
	if len(emptyAyahs) > 0 {
		// Update the empty_ayahs.json file
		emptyFilePath := filepath.Join(TafsirDir, selectedTafsirSlug, fmt.Sprintf("%d", surah), EmptyAyahsFile)
		emptyJSON, err := json.Marshal(emptyAyahs)
		if err != nil {
			return err
		}

		emptyFile, err := os.Create(emptyFilePath)
		if err != nil {
			return err
		}
		defer emptyFile.Close()

		_, err = emptyFile.Write(emptyJSON)
		if err != nil {
			return err
		}
	}

	return nil
}
