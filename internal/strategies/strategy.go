package strategies

type Strategy interface {
	GetAyah(ayahNumber int, surahNumber int, tafsirNumber int) (string, error)
	Name() string
}
