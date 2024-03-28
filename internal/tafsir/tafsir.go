package tafsir

import "encoding/json"

// Tafsir represents your data structure for Tafsir elements.
// type Tafsir []Element
func (r *Tafsir) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

type Tafsir struct {
	AuthorName   string `json:"author_name"`
	ID           int64  `json:"id"`
	LanguageName string `json:"language_name"`
	Name         string `json:"name"`
	Slug         string `json:"slug"`
	Source       string `json:"source"`
}
