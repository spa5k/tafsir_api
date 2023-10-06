package internal

type SurahAyahs []SurahAyah

type SurahAyah struct {
	Surah int `json:"surah"`
	Ayah  int `json:"ayah"`
}

type QueueData struct {
	Surah  int    `json:"surah"`
	Ayah   int    `json:"ayah"`
	Source string `json:"source"`
}

type AyahData struct {
	Surah int    `json:"surah"`
	Ayah  int    `json:"ayah"`
	Text  string `json:"text"`
}

type EmptyAyah struct {
	Surah int `json:"surah"`
	Ayah  int `json:"ayah"`
}
