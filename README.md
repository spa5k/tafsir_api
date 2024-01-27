<h1 align="center">Tafsir API</h1>

<p align="center">
  <img  src="https://raw.githubusercontent.com/spa5k/tafsir_api/main/asset/tafsirapi.png">
</p>

[![](https://data.jsdelivr.com/v1/package/gh/spa5k/tafsir_api/badge)](https://www.jsdelivr.com/package/gh/spa5k/tafsir_api)
[![](https://data.jsdelivr.com/v1/package/gh/spa5k/tafsir_api/badge/rank)](https://www.jsdelivr.com/package/gh/spa5k/tafsir_api)

<p align="center">
  <img src="https://raw.githubusercontent.com/spa5k/tafsir_api/main/asset/bismilllah.jpg">
</p>

**In the name of Allah, the Entirely Merciful, the Especially Merciful, who has guided me to do this work**

Welcome to the Tafsir API repository, a comprehensive collection of Quran Tafsirs presented in a REST architectural style. This API is designed to facilitate the development of websites and applications, with the primary aim of spreading the word of God to people around the world.

## Features

- **Free & Lightning-Fast**: Our API provides free access to Quran Tafsirs with blazing-fast response times.
- **No Rate Limits**: There are no rate limits imposed on API usage, ensuring unrestricted access to the content.
- **Multilingual Support**: The API offers Tafsirs in various languages.
- **25+ Tafsirs**: Access over 25 different Tafsirs to explore Quranic interpretations. (Currently 27)

## URL Structure:

- `https://cdn.jsdelivr.net/gh/spa5k/tafsir_api@{apiVersion}/{endpoint}`

> Versioning - By default, it uses main branch, which you can use as `@main` or `@v1` etc. You can also use commit hash as versioning.

### Base URLs -

1. JS Delivr: `https://cdn.jsdelivr.net/gh/spa5k/tafsir_api@main/tafsir`
2. Git Hack: `https://rawcdn.githack.com/spa5k/tafsir_api/bf42646e16973c59a0789b7a3ad065ff6ad6b0bf/tafsir`
3. Staticaly: `https://cdn.statically.io/gh/spa5k/tafsir_api/main/tafsir`
4. Github: `https://raw.githubusercontent.com/spa5k/tafsir_api/main/tafsir`
5. Gitloaf: `https://gitloaf.com/cdn/spa5k/tafsir_api/main/tafsir`

## Endpoints:

- /editions
  > Description: List all available editions.

  > [https://cdn.jsdelivr.net/gh/spa5k/tafsir_api@main/tafsir/editions.json](https://cdn.jsdelivr.net/gh/spa5k/tafsir_api@main/tafsir/editions.json)

- /editions/{editionSlug}/{surahNumber}
  > Description: Fetch specific edition's Surahs with their Ayahs.

  > Example URL: [https://cdn.jsdelivr.net/gh/spa5k/tafsir_api@main/tafsir/en-al-jalalayn/1.json](https://cdn.jsdelivr.net/gh/spa5k/tafsir_api@main/tafsir/en-al-jalalayn/1.json)

- /editions/{editionSlug}/{surahNumber}/{ayahNumber}
  > Description: Fetch a specific edition's Surahs with their Ayahs.

  > Example URL: [https://cdn.jsdelivr.net/gh/spa5k/tafsir_api@main/tafsir/en-al-jalalayn/1/1.json](https://cdn.jsdelivr.net/gh/spa5k/tafsir_api@main/tafsir/en-al-jalalayn/1/1.json)

- /editions/{editionSlug}/{surahNumber}/empty_ayahs.json
  > Description: Fetch the specific edition's Surahs that contain empty Ayahs.

  > Example URL: [https://cdn.jsdelivr.net/gh/spa5k/tafsir_api@main/tafsir/en-al-qushairi-tafsir/2/empty_ayahs.json](https://cdn.jsdelivr.net/gh/spa5k/tafsir_api@main/tafsir/en-al-qushairi-tafsir/2/empty_ayahs.json)

## Editions:

| Author Name                            | ID  | Language Name | Name                                    | Slug                                | Source                    |
| -------------------------------------- | --- | ------------- | --------------------------------------- | ----------------------------------- | ------------------------- |
| Saddi                                  | 91  | arabic        | Tafseer Al Saddi                        | ar-tafseer-al-saddi                 | https://quran.com/        |
| Hafiz Ibn Kathir                       | 14  | arabic        | Tafsir Ibn Kathir                       | ar-tafsir-ibn-kathir                | https://quran.com/        |
| Baghawy                                | 94  | arabic        | Tafseer Al-Baghawi                      | ar-tafsir-al-baghawi                | https://quran.com/        |
| Tanweer                                | 92  | arabic        | Tafseer Tanwir al-Miqbas                | ar-tafseer-tanwir-al-miqbas         | https://quran.com/        |
| Waseet                                 | 93  | arabic        | Tafsir Al Wasit                         | ar-tafsir-al-wasit                  | https://quran.com/        |
| Tabari                                 | 15  | arabic        | Tafsir al-Tabari                        | ar-tafsir-al-tabari                 | https://quran.com/        |
| Al Muyassar                            | 16  | arabic        | Tafsir Muyassar                         | ar-tafsir-muyassar                  | https://quran.com/        |
| AbdulRahman Bin Hasan Al-Alshaikh      | 381 | bengali       | Tafsir Fathul Majid                     | bn-tafisr-fathul-majid              | https://quran.com/        |
| Tawheed Publication                    | 164 | bengali       | Tafseer ibn Kathir                      | bn-tafseer-ibn-e-kaseer             | https://quran.com/        |
| Bayaan Foundation                      | 165 | bengali       | Tafsir Ahsanul Bayaan                   | bn-tafsir-ahsanul-bayaan            | https://quran.com/        |
| King Fahd Quran Printing Complex       | 166 | bengali       | Tafsir Abu Bakr Zakaria                 | bn-tafsir-abu-bakr-zakaria          | https://quran.com/        |
| Hafiz Ibn Kathir                       | 169 | english       | Tafsir Ibn Kathir (abridged)            | en-tafisr-ibn-kathir                | https://quran.com/        |
| Maulana Wahid Uddin Khan               | 817 | english       | Tazkirul Quran(Maulana Wahiduddin Khan) | en-tazkirul-quran                   | https://quran.com/        |
| Kashf Al-Asrar Tafsir                  | 109 | english       | Kashf Al-Asrar Tafsir                   | en-kashf-al-asrar-tafsir            | https://www.altafsir.com/ |
| Al Qushairi Tafsir                     | 108 | english       | Al Qushairi Tafsir                      | en-al-qushairi-tafsir               | https://www.altafsir.com/ |
| Kashani Tafsir                         | 107 | english       | Kashani Tafsir                          | en-kashani-tafsir                   | https://www.altafsir.com/ |
| Tafsir al-Tustari                      | 93  | english       | Tafsir al-Tustari                       | en-tafsir-al-tustari                | https://www.altafsir.com/ |
| Asbab Al-Nuzul by Al-Wahidi            | 86  | english       | Asbab Al-Nuzul by Al-Wahidi             | en-asbab-al-nuzul-by-al-wahidi      | https://www.altafsir.com/ |
| Tanwîr al-Miqbâs min Tafsîr Ibn ‘Abbâs | 73  | english       | Tanwîr al-Miqbâs min Tafsîr Ibn ‘Abbâs  | en-tafsir-ibn-abbas                 | https://www.altafsir.com/ |
| Al-Jalalayn                            | 74  | english       | Al-Jalalayn                             | en-al-jalalayn                      | https://www.altafsir.com/ |
| Mufti Muhammad Shafi                   | 168 | english       | Maarif-ul-Quran                         | en-tafsir-maarif-ul-quran           | https://quran.com/        |
| Qurtubi                                | 90  | arabic        | Tafseer Al Qurtubi                      | ar-tafseer-al-qurtubi               | https://quran.com/        |
| Rebar Kurdish Tafsir                   | 804 | Kurdish       | Rebar Kurdish Tafsir                    | kurd-tafsir-rebar                   | https://quran.com/        |
| Saddi                                  | 170 | russian       | Tafseer Al Saddi                        | ru-tafseer-al-saddi                 | https://quran.com/        |
| Sayyid Ibrahim Qutb                    | 157 | urdu          | Fi Zilal al-Quran                       | ur-tafsir-fe-zalul-quran-syed-qatab | https://quran.com/        |
| Hafiz Ibn Kathir                       | 160 | urdu          | Tafsir Ibn Kathir                       | ur-tafseer-ibn-e-kaseer             | https://quran.com/        |
| Dr. Israr Ahmad                        | 159 | urdu          | Tafsir Bayan ul Quran                   | ur-tafsir-bayan-ul-quran            | https://quran.com/        |
| Maulana Wahid Uddin Khan               | 818 | urdu          | Tazkirul Quran(Maulana Wahiduddin Khan) | ur-tazkirul-quran                   | https://quran.com/        |

## Share:

Please Share this repo with your fellow mates and Star this repo by clicking on ⭐ button above ↗️

## Contribution:

We welcome contributions to enhance the API with more Tafsirs and additional features. If you're interested in contributing, please refer to the contribution guidelines for detailed instructions on how to add more Tafsirs.

You can check [https://github.com/spa5k/tafsir_api/blob/main/internal/strategies/quran_strategy.go](https://github.com/spa5k/tafsir_api/blob/main/internal/strategies/quran_strategy.go) for more info on how to add more Tafsirs.

Thank you for being a part of our mission to spread the message of God to the world.


### Other Similar Projects:
- [Hadith API](https://github.com/fawazahmed0/hadith-api#readme)
- [Tafsir API](https://github.com/spa5k/tafsir_api#readme)
