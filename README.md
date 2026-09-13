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
- **122 Tafsirs**: Access 122 different Tafsirs to explore Quranic interpretations.

## URL Structure:

- `https://cdn.jsdelivr.net/gh/spa5k/tafsir_api@{apiVersion}/{endpoint}`

> Versioning - By default, it uses main branch, which you can use as `@main` or `@v1` etc. You can also use commit hash as versioning.

### Base URLs -

1. JS Delivr: `https://cdn.jsdelivr.net/gh/spa5k/tafsir_api@main/tafsir`
2. Git Hack: `https://rawcdn.githack.com/spa5k/tafsir_api/bf42646e16973c59a0789b7a3ad065ff6ad6b0bf/tafsir`
3. Staticaly: `https://cdn.statically.io/gh/spa5k/tafsir_api/main/tafsir`
4. Github: `https://raw.githubusercontent.com/spa5k/tafsir_api/main/tafsir`
5. Gitloaf: `https://gitloaf.com/cdn/spa5k/tafsir_api/main/tafsir`

### Self-hosting (recommended)

You can and should download `data` and `tafsir` folders and host it yourself (instead of depending only on public CDNs).

Required folders to host:

- `data/**`
- `tafsir/**`

Quick start:

```bash
git clone --depth 1 https://github.com/spa5k/tafsir_api.git
cd tafsir_api
```

Then upload/serve the `data/` folder from your own static hosting (Nginx, Cloudflare R2, S3, Vercel static, etc.).

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

| #   | Author Name                                                     | ID  | Language Name | Name                                                            | Slug                                   | Source                                      |
| --- | --------------------------------------------------------------- | --- | ------------- | --------------------------------------------------------------- | -------------------------------------- | ------------------------------------------- |
| 1   | AbdulRahman Bin Hasan Al-Alshaikh                               | 381 | bengali       | Tafsir Fathul Majid                                             | bn-tafisr-fathul-majid                 | https://quran.com/                          |
| 2   | Tanweer                                                         | 92  | arabic        | Tafseer Tanwir al-Miqbas                                        | ar-tafseer-tanwir-al-miqbas            | https://quran.com/                          |
| 3   | Sayyid Ibrahim Qutb                                             | 157 | urdu          | Fi Zilal al-Quran                                               | ur-tafsir-fe-zalul-quran-syed-qatab    | https://quran.com/                          |
| 4   | Hafiz Ibn Kathir                                                | 160 | urdu          | Tafsir Ibn Kathir                                               | ur-tafseer-ibn-e-kaseer                | https://quran.com/                          |
| 5   | Dr. Israr Ahmad                                                 | 159 | urdu          | Tafsir Bayan ul Quran                                           | ur-tafsir-bayan-ul-quran               | https://quran.com/                          |
| 6   | Maulana Wahid Uddin Khan                                        | 818 | urdu          | Tazkirul Quran(Maulana Wahiduddin Khan)                         | ur-tazkirul-quran                      | https://quran.com/                          |
| 7   | Maulana Wahid Uddin Khan                                        | 817 | english       | Tazkirul Quran(Maulana Wahiduddin Khan)                         | en-tazkirul-quran                      | https://quran.com/                          |
| 8   | Kashf Al-Asrar Tafsir                                           | 109 | english       | Kashf Al-Asrar Tafsir                                           | en-kashf-al-asrar-tafsir               | https://www.altafsir.com/                   |
| 9   | Al Qushairi Tafsir                                              | 108 | english       | Al Qushairi Tafsir                                              | en-al-qushairi-tafsir                  | https://www.altafsir.com/                   |
| 10  | Kashani Tafsir                                                  | 107 | english       | Kashani Tafsir                                                  | en-kashani-tafsir                      | https://www.altafsir.com/                   |
| 11  | Tafsir al-Tustari                                               | 93  | english       | Tafsir al-Tustari                                               | en-tafsir-al-tustari                   | https://www.altafsir.com/                   |
| 12  | Asbab Al-Nuzul by Al-Wahidi                                     | 86  | english       | Asbab Al-Nuzul by Al-Wahidi                                     | en-asbab-al-nuzul-by-al-wahidi         | https://www.altafsir.com/                   |
| 13  | Tanwîr al-Miqbâs min Tafsîr Ibn ‘Abbâs                          | 73  | english       | Tanwîr al-Miqbâs min Tafsîr Ibn ‘Abbâs                          | en-tafsir-ibn-abbas                    | https://www.altafsir.com/                   |
| 14  | Al-Jalalayn                                                     | 74  | english       | Al-Jalalayn                                                     | en-al-jalalayn                         | https://www.altafsir.com/                   |
| 15  | Sinhalese Mokhtasar                                             | 453 | sinhala       | Sinhalese Mokhtasar                                             | sinhalese-mokhtasar                    | https://qul.tarteel.ai/resources/tafsir/453 |
| 16  | Tafsir Center for Quranic Studies                               | 266 | english       | English Al-Mukhtasar                                            | en-tafsir-al-mukhtasar                 | https://qul.tarteel.ai/resources/tafsir/266 |
| 17  | Tafsir As-Saadi                                                 | 283 | albanian      | Tafsir As-Saadi                                                 | sq-saadi                               | https://qul.tarteel.ai/resources/tafsir/283 |
| 18  | Japanese Abridged Explanation of the Quran                      | 265 | japanese      | Japanese Abridged Explanation of the Quran                      | japanese-mokhtasar                     | https://qul.tarteel.ai/resources/tafsir/265 |
| 19  | Russian Al-Mukhtasar                                            | 262 | russian       | Russian Al-Mukhtasar                                            | russian-mokhtasar                      | https://qul.tarteel.ai/resources/tafsir/262 |
| 20  | Bengali Abridged Explanation of the Quran                       | 267 | bengali       | Bengali Abridged Explanation of the Quran                       | bengali-mokhtasar                      | https://qul.tarteel.ai/resources/tafsir/267 |
| 21  | Filipino (Tagalog) Al-Mukhtasar in interpreting the Noble Quran | 254 | tagalog       | Filipino (Tagalog) Al-Mukhtasar in interpreting the Noble Quran | tagalog-mokhtasar                      | https://qul.tarteel.ai/resources/tafsir/254 |
| 22  | Tafsir Ibne Kathir                                              | 307 | russian       | Tafsir Ibne Kathir                                              | ru-tafsir-ibne-kahtir                  | https://qul.tarteel.ai/resources/tafsir/307 |
| 23  | Chinese Abridged Explanation of the Quran                       | 264 | chinese       | Chinese Abridged Explanation of the Quran                       | chinese-mokhtasar                      | https://qul.tarteel.ai/resources/tafsir/264 |
| 24  | Tafsir Ibne Kathir                                              | 306 | turkish       | Tafsir Ibne Kathir                                              | tr-tafsir-ibne-kathir                  | https://qul.tarteel.ai/resources/tafsir/306 |
| 25  | Asseraj fi Bayan Gharib AlQuran                                 | 250 | arabic        | Asseraj fi Bayan Gharib AlQuran                                 | asseraj-fi-bayan-gharib-alquran        | https://qul.tarteel.ai/resources/tafsir/250 |
| 26  | Assamese Abridged Explanation of the Quran                      | 255 | assamese      | Assamese Abridged Explanation of the Quran                      | assamese-mokhtasar                     | https://qul.tarteel.ai/resources/tafsir/255 |
| 27  | Tafsir Center for Quranic Studies                               | 251 | arabic        | Arabic Al-Mukhtasar in interpreting the Noble Quran             | ar-tafsir-al-mukhtasar                 | https://qul.tarteel.ai/resources/tafsir/251 |
| 28  | Italian Al-Mukhtasar in interpreting the Noble Quran            | 253 | italian       | Italian Al-Mukhtasar in interpreting the Noble Quran            | italian-mokhtasar                      | https://qul.tarteel.ai/resources/tafsir/253 |
| 29  | Tafsir As-Saadi                                                 | 310 | russian       | Tafsir As-Saadi                                                 | tafsir-as-saadi-russian                | https://qul.tarteel.ai/resources/tafsir/310 |
| 30  | Bosnian Abridged Explanation of the Quran                       | 252 | bosnian       | Bosnian Abridged Explanation of the Quran                       | bosnian-mokhtasar                      | https://qul.tarteel.ai/resources/tafsir/252 |
| 31  | Malayalam Abridged Explanation of the Quran                     | 256 | malayalam     | Malayalam Abridged Explanation of the Quran                     | malayalam-mokhtasar                    | https://qul.tarteel.ai/resources/tafsir/256 |
| 32  | Turkish Al-Mukhtasar in Interpreting the Noble Quran            | 258 | turkish       | Turkish Al-Mukhtasar in Interpreting the Noble Quran            | turkish-mokhtasar                      | https://qul.tarteel.ai/resources/tafsir/258 |
| 33  | Khmer Abridged Explanation of the Quran                         | 257 | central khmer | Khmer Abridged Explanation of the Quran                         | khmer-mokhtasar                        | https://qul.tarteel.ai/resources/tafsir/257 |
| 34  | French Abridged Explanation of the Quran                        | 259 | french        | French Abridged Explanation of the Quran                        | french-mokhtasar                       | https://qul.tarteel.ai/resources/tafsir/259 |
| 35  | Vietnamese Al-Mukhtasar in interpreting the Noble Quran         | 261 | vietnamese    | Vietnamese Al-Mukhtasar in interpreting the Noble Quran         | vietnamese-mokhtasar                   | https://qul.tarteel.ai/resources/tafsir/261 |
| 36  | Persian Al-Mukhtasar in interpreting the Noble Quran            | 263 | persian       | Persian Al-Mukhtasar in interpreting the Noble Quran            | persian-mokhtasar                      | https://qul.tarteel.ai/resources/tafsir/263 |
| 37  | Tafsir As-Saadi                                                 | 308 | arabic        | Tafsir As-Saadi                                                 | ar-tafsir-as-saadi                     | https://qul.tarteel.ai/resources/tafsir/308 |
| 38  | Indoniesua Al-Mukhtasar in Interpreting the Noble Quran         | 260 | indonesian    | Indoniesua Al-Mukhtasar in Interpreting the Noble Quran         | indonesian-mokhtasar                   | https://qul.tarteel.ai/resources/tafsir/260 |
| 39  | Iraab Al-Muyassar                                               | 504 | arabic        | Iraab Al-Muyassar                                               | al-i-rab-al-muyassar                   | https://qul.tarteel.ai/resources/tafsir/504 |
| 40  | Tafsir As-Saadi - Urdu                                          | 309 | urdu          | Tafsir As-Saadi - Urdu                                          | ur-tafsir-as-saadi-urdu                | https://qul.tarteel.ai/resources/tafsir/309 |
| 41  | Tafsir As-Saadi - Indonesian                                    | 503 | indonesian    | Tafsir As-Saadi - Indonesian                                    | id-tafsir-as-saadi                     | https://qul.tarteel.ai/resources/tafsir/503 |
| 42  | Tafsir Ibn Abi Zamanin                                          | 499 | arabic        | Tafsir Ibn Abi Zamanin                                          | tafsir-ibn-abi-zamanin                 | https://qul.tarteel.ai/resources/tafsir/499 |
| 43  | Abu Bakr Jabir Al-Jazairi                                       | 507 | arabic        | Abu Bakr Jabir Al-Jazairi                                       | abu-bakr-jabir-al-jazairi              | https://qul.tarteel.ai/resources/tafsir/507 |
| 44  | I'rab Al Quran li Al Darwish                                    | 506 | arabic        | I'rab Al Quran li Al Darwish                                    | i-rab-al-quran-li-al-darwish           | https://qul.tarteel.ai/resources/tafsir/506 |
| 45  | Nazam Al-Durar Al-Biqa'i                                        | 498 | arabic        | Nazam Al-Durar Al-Biqa'i                                        | nazam-al-durar-al-biqa-i               | https://qul.tarteel.ai/resources/tafsir/498 |
| 46  | Tafsir al-Tahrir wa al-Tanwir                                   | 25  | arabic        | Tafsir al-Tahrir wa al-Tanwir                                   | ar-tafseer-tahrir-al-tanwir            | https://qul.tarteel.ai/resources/tafsir/25  |
| 47  | Hafiz Ibn Kathir                                                | 35  | english       | Tafsir Ibn Kathir                                               | en-tafisr-ibn-kathir                   | https://qul.tarteel.ai/resources/tafsir/35  |
| 48  | Saddi                                                           | 24  | arabic        | Tafseer Al Saadi - Arabic                                       | ar-tafseer-al-saddi                    | https://qul.tarteel.ai/resources/tafsir/24  |
| 49  | Saddi                                                           | 36  | russian       | Tafseer Al Saadi - Russian                                      | ru-tafseer-al-saddi                    | https://qul.tarteel.ai/resources/tafsir/36  |
| 50  | Hafiz Ibn Kathir                                                | 22  | arabic        | Tafsir Ibn Kathir                                               | ar-tafsir-ibn-kathir                   | https://qul.tarteel.ai/resources/tafsir/22  |
| 51  | Qurtubi                                                         | 23  | arabic        | Tafseer Al Qurtubi                                              | ar-tafseer-al-qurtubi                  | https://qul.tarteel.ai/resources/tafsir/23  |
| 52  | Baghawy                                                         | 27  | arabic        | Tafseer Al-Baghawi                                              | ar-tafsir-al-baghawi                   | https://qul.tarteel.ai/resources/tafsir/27  |
| 53  | Tafsir Ibn Kathir                                               | 30  | urdu          | Tafsir Ibn Kathir                                               | tafseer-ibn-e-kaseer-urdu              | https://qul.tarteel.ai/resources/tafsir/30  |
| 54  | Fi Zilal al-Quran                                               | 28  | urdu          | Fi Zilal al-Quran                                               | tafsir-fe-zalul-quran-syed-qatab       | https://qul.tarteel.ai/resources/tafsir/28  |
| 55  | Tawheed Publication                                             | 31  | bengali       | Tafseer ibn Kathir                                              | bn-tafseer-ibn-e-kaseer                | https://qul.tarteel.ai/resources/tafsir/31  |
| 56  | Tafsir Bayan ul Quran                                           | 29  | urdu          | Tafsir Bayan ul Quran                                           | tafsir-bayan-ul-quran                  | https://qul.tarteel.ai/resources/tafsir/29  |
| 57  | Waseet                                                          | 26  | arabic        | Tafsir Al Wasit                                                 | ar-tafsir-al-wasit                     | https://qul.tarteel.ai/resources/tafsir/26  |
| 58  | Mufti Muhammad Shafi                                            | 34  | english       | Maarif-ul-Quran                                                 | en-tafsir-maarif-ul-quran              | https://qul.tarteel.ai/resources/tafsir/34  |
| 59  | المیسر                                                          | 38  | arabic        | Tafsir Muyassar                                                 | ar-tafsir-muyassar                     | https://qul.tarteel.ai/resources/tafsir/38  |
| 60  | Tafsir Jalalayn                                                 | 41  | indonesian    | Tafsir Jalalayn                                                 | in-tafsir-jalalayn                     | https://qul.tarteel.ai/resources/tafsir/41  |
| 61  | Bayaan Foundation                                               | 32  | bengali       | Tafsir Ahsanul Bayaan                                           | bn-tafsir-ahsanul-bayaan               | https://qul.tarteel.ai/resources/tafsir/32  |
| 62  | Tafsir Fathul Majid                                             | 39  | bengali       | Tafsir Fathul Majid                                             | tafisr-fathul-majid-bn                 | https://qul.tarteel.ai/resources/tafsir/39  |
| 63  | King Fahd Quran Printing Complex                                | 33  | bengali       | Tafsir Abu Bakr Zakaria                                         | bn-tafsir-abu-bakr-zakaria             | https://qul.tarteel.ai/resources/tafsir/33  |
| 64  | Tazkirul Quran(Maulana Wahiduddin Khan)                         | 42  | english       | Tazkirul Quran(Maulana Wahiduddin Khan)                         | tazkirul-quran-en                      | https://qul.tarteel.ai/resources/tafsir/42  |
| 65  | Tazkirul Quran(Maulana Wahiduddin Khan)                         | 43  | urdu          | Tazkirul Quran(Maulana Wahiduddin Khan)                         | tazkiru-quran-ur                       | https://qul.tarteel.ai/resources/tafsir/43  |
| 66  | Rebar Kurdish Tafsir                                            | 40  | Kurdish       | Rebar Kurdish Tafsir                                            | kurd-tafsir-rebar                      | https://qul.tarteel.ai/resources/tafsir/40  |
| 67  | Al-Muharrar Al-Wajiz Ibn Atiyyah                                | 509 | arabic        | Al-Muharrar Al-Wajiz Ibn Atiyyah                                | al-muharrar-al-wajiz-ibn-atiyyah       | https://qul.tarteel.ai/resources/tafsir/509 |
| 68  | Tabari                                                          | 37  | arabic        | Tafsir al-Tabari                                                | ar-tafsir-al-tabari                    | https://qul.tarteel.ai/resources/tafsir/37  |
| 69  | Al-Basit                                                        | 511 | arabic        | Al-Basit                                                        | al-basit                               | https://qul.tarteel.ai/resources/tafsir/511 |
| 70  | Alrab Al-Quran li-Da'as                                         | 515 | arabic        | Alrab Al-Quran li-Da'as                                         | alrab-al-quran-li-da-as                | https://qul.tarteel.ai/resources/tafsir/515 |
| 71  | Tafsir Al-Nasafi                                                | 514 | arabic        | Tafsir Al-Nasafi                                                | tafsir-al-nasafi                       | https://qul.tarteel.ai/resources/tafsir/514 |
| 72  | Al-Muyassar fi Al-Gharib                                        | 519 | arabic        | Al-Muyassar fi Al-Gharib                                        | al-muyassar-fi-al-gharib               | https://qul.tarteel.ai/resources/tafsir/519 |
| 73  | Al Lubab fi Ulum Al Kitab                                       | 516 | arabic        | Al Lubab fi Ulum Al Kitab                                       | al-lubab-fi-ulum-al-kitab              | https://qul.tarteel.ai/resources/tafsir/516 |
| 74  | Jalal al-Din al-Mahalli and Jalal al-Din al-Suyuti              | 523 | arabic        | Tafsir Jalalayn                                                 | ar-tafsir-al-jalalayn                  | https://qul.tarteel.ai/resources/tafsir/523 |
| 75  | Tafsir Al-Baydawi                                               | 518 | arabic        | Tafsir Al-Baydawi                                               | tafsir-al-baydawi                      | https://qul.tarteel.ai/resources/tafsir/518 |
| 76  | Al Jadwal fi I'rab Al Quran                                     | 520 | arabic        | Al Jadwal fi I'rab Al Quran                                     | al-jadwal-fi-i-rab-al-quran            | https://qul.tarteel.ai/resources/tafsir/520 |
| 77  | Tafsir Al-Razi                                                  | 488 | arabic        | Tafsir Al-Razi                                                  | tafsir-al-razi                         | https://qul.tarteel.ai/resources/tafsir/488 |
| 78  | Tafsir Al Jalalayn - English                                    | 573 | english       | Tafsir Al Jalalayn - English                                    | tafsir-al-jalalayn                     | https://qul.tarteel.ai/resources/tafsir/573 |
| 79  | Tafsir Ibn Juzay                                                | 491 | arabic        | Tafsir Ibn Juzay                                                | tafsir-ibn-juzay                       | https://qul.tarteel.ai/resources/tafsir/491 |
| 80  | Tafsir As-Saadi - Persian                                       | 485 | persian       | Tafsir As-Saadi - Persian                                       | fr-tafsir-as-saadi                     | https://qul.tarteel.ai/resources/tafsir/485 |
| 81  | Tafsir As-Saadi - Turkish                                       | 484 | turkish       | Tafsir As-Saadi - Turkish                                       | turkish-tafsir-as-saadi-turkish        | https://qul.tarteel.ai/resources/tafsir/484 |
| 82  | Mawsoo'at Al-Tafsir Al-Ma'thoor                                 | 492 | arabic        | Mawsoo'at Al-Tafsir Al-Ma'thoor                                 | mawsoo-at-al-tafsir-al-ma-thoor        | https://qul.tarteel.ai/resources/tafsir/492 |
| 83  | Tahlil Kalimat al-Qur'an                                        | 487 | arabic        | Tahlil Kalimat al-Qur'an                                        | tahlil-kalimat-al-qur-an               | https://qul.tarteel.ai/resources/tafsir/487 |
| 84  | Tafsir Ibn Uthaymeen                                            | 486 | arabic        | Tafsir Ibn Uthaymeen                                            | tafsir-ibn-uthaymeen                   | https://qul.tarteel.ai/resources/tafsir/486 |
| 85  | Tafsir Makhi                                                    | 490 | arabic        | Tafsir Makhi                                                    | tafsir-makhi                           | https://qul.tarteel.ai/resources/tafsir/490 |
| 86  | Thai Mokhtasar                                                  | 541 | thai          | Thai Mokhtasar                                                  | thai-mokhtasar                         | https://qul.tarteel.ai/resources/tafsir/541 |
| 87  | Mahasin Al-Ta'wil Al-Qasimi                                     | 524 | arabic        | Mahasin Al-Ta'wil Al-Qasimi                                     | mahasin-al-ta-wil-al-qasimi            | https://qul.tarteel.ai/resources/tafsir/524 |
| 88  | Telugu Mokhtasar                                                | 540 | telugu        | Telugu Mokhtasar                                                | telugu-mokhtasar                       | https://qul.tarteel.ai/resources/tafsir/540 |
| 89  | Uyghur Mokhtasar                                                | 539 | uighur        | Uyghur Mokhtasar                                                | uyghur-mokhtasar                       | https://qul.tarteel.ai/resources/tafsir/539 |
| 90  | Pashto Mokhtasar                                                | 533 | pashto        | Pashto Mokhtasar                                                | pashto-mokhtasar                       | https://qul.tarteel.ai/resources/tafsir/533 |
| 91  | Tafsir Al-Sam'ani                                               | 529 | arabic        | Tafsir Al-Sam'ani                                               | tafsir-al-sam-ani                      | https://qul.tarteel.ai/resources/tafsir/529 |
| 92  | Azeri Mokhtasar                                                 | 537 | azeri         | Azeri Mokhtasar                                                 | azeri-mokhtasar                        | https://qul.tarteel.ai/resources/tafsir/537 |
| 93  | Fulani Mokhtasar                                                | 534 | fulah         | Fulani Mokhtasar                                                | fulani-mokhtasar                       | https://qul.tarteel.ai/resources/tafsir/534 |
| 94  | Al-Bahr Al-Muhit                                                | 526 | arabic        | Al-Bahr Al-Muhit                                                | al-bahr-al-muhit                       | https://qul.tarteel.ai/resources/tafsir/526 |
| 95  | Tafsir Al-Tha'alibi                                             | 528 | arabic        | Tafsir Al-Tha'alibi                                             | ar-tafsir-al-tha-alibi                 | https://qul.tarteel.ai/resources/tafsir/528 |
| 96  | Uzbek Mokhtasar                                                 | 538 | uzbek         | Uzbek Mokhtasar                                                 | uzbek-mokhtasar                        | https://qul.tarteel.ai/resources/tafsir/538 |
| 97  | Tafsir Al-Tha'alibi                                             | 527 | arabic        | Tafsir Al-Tha'alibi                                             | ar-tafsir-al-tha-alibi-527             | https://qul.tarteel.ai/resources/tafsir/527 |
| 98  | Adwa' Al-Bayan                                                  | 525 | arabic        | Adwa' Al-Bayan                                                  | adwa-al-bayan                          | https://qul.tarteel.ai/resources/tafsir/525 |
| 99  | Ayah Dependency Graphs                                          | 563 | arabic        | Ayah Dependency Graphs                                          | ayah-dependency-graphs                 | https://qul.tarteel.ai/resources/tafsir/563 |
| 100 | Serbian Mokhtasar                                               | 543 | serbian       | Serbian Mokhtasar                                               | serbian-mokhtasar                      | https://qul.tarteel.ai/resources/tafsir/543 |
| 101 | Kurdish Mokhtasar                                               | 542 | kurdish       | Kurdish Mokhtasar                                               | kurdish-mokhtasar                      | https://qul.tarteel.ai/resources/tafsir/542 |
| 102 | Al-Wajiz Wahidi                                                 | 489 | arabic        | Al-Wajiz Wahidi                                                 | al-wajiz-wahidi                        | https://qul.tarteel.ai/resources/tafsir/489 |
| 103 | Tamil Mokhtasar                                                 | 554 | tamil         | Tamil Mokhtasar                                                 | tamil-mokhtasar                        | https://qul.tarteel.ai/resources/tafsir/554 |
| 104 | Fath Al-Qadir Al-Shawkani                                       | 494 | arabic        | Fath Al-Qadir Al-Shawkani                                       | fath-al-qadir-al-shawkani              | https://qul.tarteel.ai/resources/tafsir/494 |
| 105 | Al Nashr li Ibn Al Jazari                                       | 522 | arabic        | Al Nashr li Ibn Al Jazari                                       | al-nashr-li-ibn-al-jazari              | https://qul.tarteel.ai/resources/tafsir/522 |
| 106 | Kyrgyz Mokhtasar                                                | 536 | kyrgyz        | Kyrgyz Mokhtasar                                                | kyrgyz-mokhtasar                       | https://qul.tarteel.ai/resources/tafsir/536 |
| 107 | Al Qira'at Al Mawsoo'ah Al Qur'aniyyah                          | 521 | arabic        | Al Qira'at Al Mawsoo'ah Al Qur'aniyyah                          | al-qira-at-al-mawsoo-ah-al-qur-aniyyah | https://qul.tarteel.ai/resources/tafsir/521 |
| 108 | Spanish Abridged Explanation of the Quran                       | 268 | spanish       | Spanish Abridged Explanation of the Quran                       | spanish-mokhtasar                      | https://qul.tarteel.ai/resources/tafsir/268 |
| 109 | Tafsir Ibn Al-Jawzi                                             | 496 | arabic        | Tafsir Ibn Al-Jawzi                                             | tafsir-ibn-al-jawzi                    | https://qul.tarteel.ai/resources/tafsir/496 |
| 110 | Tafsir Ibn Al-Qayyim                                            | 500 | arabic        | Tafsir Ibn Al-Qayyim                                            | tafsir-ibn-al-qayyim                   | https://qul.tarteel.ai/resources/tafsir/500 |
| 111 | Hindi Mokhtasar                                                 | 535 | hindi         | Hindi Mokhtasar                                                 | hindi-mokhtasar                        | https://qul.tarteel.ai/resources/tafsir/535 |
| 112 | Al-Durr Al-Manthur                                              | 493 | arabic        | Al-Durr Al-Manthur                                              | al-durr-al-manthur                     | https://qul.tarteel.ai/resources/tafsir/493 |
| 113 | Jamia Al-Bayan AlIji                                            | 508 | arabic        | Jamia Al-Bayan AlIji                                            | jamia-al-bayan-aliji                   | https://qul.tarteel.ai/resources/tafsir/508 |
| 114 | Tafsir Al-Samarqandi                                            | 513 | arabic        | Tafsir Al-Samarqandi                                            | tafsir-al-samarqandi                   | https://qul.tarteel.ai/resources/tafsir/513 |
| 115 | Tafsir Ibn Abi Hatim                                            | 502 | arabic        | Tafsir Ibn Abi Hatim                                            | tafsir-ibn-abi-hatim                   | https://qul.tarteel.ai/resources/tafsir/502 |
| 116 | Tafsir Al-Alusi                                                 | 501 | arabic        | Tafsir Al-Alusi                                                 | tafsir-al-alusi                        | https://qul.tarteel.ai/resources/tafsir/501 |
| 117 | Al Dur Al Masun Lil Samin Al Halabi                             | 505 | arabic        | Al Dur Al Masun Lil Samin Al Halabi                             | al-dur-al-masun-lil-samin-al-halabi    | https://qul.tarteel.ai/resources/tafsir/505 |
| 118 | Tadabbur wa 'Amal                                               | 517 | arabic        | Tadabbur wa 'Amal                                               | tadabbur-wa-amal                       | https://qul.tarteel.ai/resources/tafsir/517 |
| 119 | Fath Al-Bayan li Al-Qanuji                                      | 495 | arabic        | Fath Al-Bayan li Al-Qanuji                                      | fath-al-bayan-li-al-qanuji             | https://qul.tarteel.ai/resources/tafsir/495 |
| 120 | Tafsir Abi Al-Suaood                                            | 497 | arabic        | Tafsir Abi Al-Suaood                                            | tafsir-abi-al-su-ood                   | https://qul.tarteel.ai/resources/tafsir/497 |
| 121 | Tafsir Al-Mawardi                                               | 512 | arabic        | Tafsir Al-Mawardi                                               | tafsir-al-mawardi                      | https://qul.tarteel.ai/resources/tafsir/512 |
| 122 | Al-Kashshaf Al-Zamakhshari                                      | 510 | arabic        | Al-Kashshaf Al-Zamakhshari                                      | al-kashshaf-al-zamakhshari             | https://qul.tarteel.ai/resources/tafsir/510 |

## Share:

Please Share this repo with your fellow mates and Star this repo by clicking on ⭐ button above ↗️

## Contribution:

We welcome contributions to enhance the API with more Tafsirs and additional features. If you're interested in contributing, please refer to the contribution guidelines for detailed instructions on how to add more Tafsirs.

You can check [https://github.com/spa5k/tafsir_api/blob/main/internal/strategies/quran_strategy.go](https://github.com/spa5k/tafsir_api/blob/main/internal/strategies/quran_strategy.go) for more info on how to add more Tafsirs.

### Data generation

Most editions are generated from [QUL](https://qul.tarteel.ai/resources) SQLite exports:

1. `scripts/import_qul_sqlite.py` regenerates `tafsir/**` and `data/editions.json` from the downloaded databases.
2. `scripts/check_tafsir_data.py` validates the generated tree (indexes match the per-ayah files, no empty text, no stale `empty_ayahs` entries).

Thank you for being a part of our mission to spread the message of God to the world.

### Other Similar Projects:

- [Hadith API](https://github.com/fawazahmed0/hadith-api#readme)
- [Quran API](https://github.com/fawazahmed0/quran-api#readme)

## Notes

Some tafsirs, such as Fi Zilal al-Qur'an by Sayyid Qutb, were removed due to reports of problematic aqeedah by some users [#25](https://github.com/spa5k/tafsir_api/issues/25)
