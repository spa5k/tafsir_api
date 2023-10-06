<h1 align="center">Tafsir API</h1>

<p align="center">
  <img  src="https://raw.githubusercontent.com/spa5k/tafsir_api/main/asset/tafsirapi.png">
</p>
[![](https://data.jsdelivr.com/main/package/gh/spa5k/tafsir_api/badge)](https://www.jsdelivr.com/package/gh/spa5k/tafsir_api)
[![](https://data.jsdelivr.com/main/package/gh/spa5k/tafsir_api/badge/rank)](https://www.jsdelivr.com/package/gh/spa5k/tafsir_api)

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
> Sometimes, v1 don't work in jsDelivr, so you can use `@main` instead of `@v1` in jsDelivr. Prefer Main branch over v1.

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


## Share:

Please Share this repo with your fellow mates and Star this repo by clicking on ⭐ button above ↗️

## Contribution:

We welcome contributions to enhance the API with more Tafsirs and additional features. If you're interested in contributing, please refer to the contribution guidelines for detailed instructions on how to add more Tafsirs.

You can check [https://github.com/spa5k/tafsir_api/blob/main/internal/strategies/quran_strategy.go](https://github.com/spa5k/tafsir_api/blob/main/internal/strategies/quran_strategy.go) for more info on how to add more Tafsirs.

Thank you for being a part of our mission to spread the message of God to the world.