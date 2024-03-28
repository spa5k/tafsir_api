package strategies

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

type QuranStrategy struct{}

type QuranCOMAyah struct {
	Tafsir QuranCOMTafsir `json:"tafsir"`
}

type QuranCOMTafsir struct {
	ResourceID   int64  `json:"resource_id"`
	ResourceName string `json:"resource_name"`
	LanguageID   int64  `json:"language_id"`
	Slug         string `json:"slug"`
	Text         string `json:"text"`
}

func (q *QuranStrategy) GetAyah(ayahNumber int, surahNumber int, tafsirNumber int) (string, error) {
	quranUrl := "https://api.quran.com/api/v4"
	ayahUrl := fmt.Sprintf("%s/tafsir/%d/by_ayah/%d:%d", quranUrl, tafsirNumber, surahNumber, ayahNumber)

	// Make an HTTP GET request to fetch the ayah text
	response, err := http.Get(ayahUrl)
	if err != nil {
		return "", err
	}
	defer func(Body io.ReadCloser) {
		err := Body.Close()
		if err != nil {
			panic(err)
		}
	}(response.Body)

	// Check if the response status code is not OK (200)
	if response.StatusCode != http.StatusOK {
		return "", fmt.Errorf("HTTP request failed with status code: %d", response.StatusCode)
	}

	// Read the response body
	body, err := io.ReadAll(response.Body)
	if err != nil {
		return "", err
	}

	// Parse the response JSON
	var quranCOMAyah QuranCOMAyah
	if err := json.Unmarshal(body, &quranCOMAyah); err != nil {
		return "", err
	}

	// Extract and return the ayah text
	ayahText := quranCOMAyah.Tafsir.Text
	return ayahText, nil
}

// Name returns the name of this strategy.
func (q *QuranStrategy) Name() string {
	return "quran"
}
