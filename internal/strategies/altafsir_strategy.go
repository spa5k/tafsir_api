package strategies

import (
	"fmt"
	"io"
	"net/http"
	"strings"

	"github.com/PuerkitoBio/goquery"
)

// AltafsirStrategy downloads and formats data from altafsir.com.
type AltafsirStrategy struct{}

func (q *AltafsirStrategy) GetAyah(ayahNumber int, surahNumber int, tafsirNumber int) (string, error) {
	pageNumber := 1
	url := fmt.Sprintf("https://www.altafsir.com/Tafasir.asp?tMadhNo=0&tTafsirNo=%d&tSoraNo=%d&tAyahNo=%d&tDisplay=yes&Page=%d&UserProfile=0&LanguageId=2", tafsirNumber, surahNumber, ayahNumber, pageNumber)
	ayahText := downloadAndGetText(url)

	return ayahText, nil
}

func downloadAndGetText(url string) string {
	response, err := http.Get(url)
	if err != nil {
		fmt.Println("Error while downloading", url, "-", err)
		return ""
	}
	defer func(Body io.ReadCloser) {
		err := Body.Close()
		if err != nil {
			panic(err)
		}
	}(response.Body)

	// Check if the response status code is not OK (200)
	if response.StatusCode != http.StatusOK {
		// just log the error and return empty
		fmt.Println("Error while downloading", url, "-", response.StatusCode)
		return ""
	}

	// Parse the HTML content using goquery
	doc, err := goquery.NewDocumentFromReader(response.Body)
	if err != nil {
		panic(err)
	}

	// Find the element containing the Ayah text
	ayahText := ""
	doc.Find(".TextResultEnglish > font:nth-child(1)").Each(func(index int, element *goquery.Selection) {
		ayahText += strings.TrimSpace(element.Text())
	})
	if ayahText == "" {
		fmt.Println("Could not find ayah text", url)
	}
	return ayahText
}

// Name returns the name of this strategy.
func (q *AltafsirStrategy) Name() string {
	return "quran"
}
