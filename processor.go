package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
)

const (
	baseDir        = "tafsir"
	emptyAyahsFile = "empty_ayahs.json"
	filePermission = 0o644
)

func main() {
	processTafsirDirectories()
}

func processTafsirDirectories() {
	tafsirDirs, err := getSubdirectories(baseDir)
	if err != nil {
		log.Fatalf("Error listing subdirectories in %s: %v\n", baseDir, err)
	}

	for _, tafsirDir := range tafsirDirs {
		fmt.Printf("Processing Tafsir subdirectory: %s\n", tafsirDir)
		processSurahDirectories(tafsirDir)
	}
}

func processSurahDirectories(tafsirDir string) {
	surahDirs, err := getSubdirectories(tafsirDir)
	if err != nil {
		log.Printf("Error listing Surah subdirectories in %s: %v\n", tafsirDir, err)
		return
	}

	for _, surahDir := range surahDirs {
		fmt.Printf("Processing Surah subdirectory: %s\n", surahDir)
		ayahs, err := processJSONFiles(surahDir)
		if err != nil {
			log.Printf("Error processing Surah subdirectory %s: %v\n", surahDir, err)
			continue
		}

		emptyAyahs, err := readEmptyAyahs(filepath.Join(surahDir, emptyAyahsFile))
		if err != nil {
			log.Printf("Warning: Empty Ayahs file not found for Surah %s\n", surahDir)
		}

		saveCombinedJSON(tafsirDir, surahDir, ayahs, emptyAyahs)
	}
}

func processJSONFiles(surahDir string) ([]map[string]interface{}, error) {
	var ayahs []map[string]interface{}

	processFile := func(path string, info os.FileInfo, err error) error {
		if err != nil {
			log.Printf("Error processing file: %v\n", err)
			return err
		}

		if filepath.Ext(path) == ".json" && filepath.Base(path) != emptyAyahsFile {
			fmt.Printf("Processing JSON file: %s\n", path)
			data, err := ioutil.ReadFile(path)
			if err != nil {
				log.Printf("Error reading JSON file: %v\n", err)
				return err
			}

			var jsonData map[string]interface{}
			if err := json.Unmarshal(data, &jsonData); err != nil {
				log.Printf("Error unmarshaling JSON data: %v\n", err)
				return err
			}

			ayahs = append(ayahs, jsonData)
		}
		return nil
	}

	if err := filepath.Walk(surahDir, processFile); err != nil {
		log.Printf("Error walking directory %s: %v\n", surahDir, err)
		return nil, err
	}

	return ayahs, nil
}

func readEmptyAyahs(filePath string) ([]map[string]interface{}, error) {
	data, err := ioutil.ReadFile(filePath)
	if err != nil {
		return nil, err
	}

	var emptyAyahs []map[string]interface{}
	if err := json.Unmarshal(data, &emptyAyahs); err != nil {
		return nil, err
	}

	return emptyAyahs, nil
}

func saveCombinedJSON(tafsirDir string, surahDir string, ayahs []map[string]interface{}, emptyAyahs []map[string]interface{}) {
	outputFile := filepath.Join(tafsirDir, filepath.Base(surahDir)+".json")

	data := map[string]interface{}{"ayahs": ayahs}
	if len(emptyAyahs) > 0 {
		data["empty_ayahs"] = emptyAyahs
	}

	combinedJSON, err := json.Marshal(data)
	if err != nil {
		log.Printf("Error marshaling JSON data: %v\n", err)
		return
	}

	if err := ioutil.WriteFile(outputFile, combinedJSON, filePermission); err != nil {
		log.Printf("Error writing combined JSON data to %s: %v\n", outputFile, err)
		return
	}

	fmt.Printf("Combined JSON data saved to %s for Surah %s\n", outputFile, filepath.Base(surahDir))
}

func getSubdirectories(dir string) ([]string, error) {
	var subdirs []string
	entries, err := ioutil.ReadDir(dir)
	if err != nil {
		return nil, err
	}
	for _, entry := range entries {
		if entry.IsDir() {
			subdir := filepath.Join(dir, entry.Name())
			subdirs = append(subdirs, subdir)
		}
	}
	return subdirs, nil
}
