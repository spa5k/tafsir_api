#!/usr/bin/env python3
import argparse
import html
import json
import re
import shutil
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path


BLOCK_TAG_RE = re.compile(r"</?(?:p|div|br|li|ul|ol|h[1-6])[^>]*>", re.IGNORECASE)
TAG_RE = re.compile(r"<[^>]+>")
SPACE_RE = re.compile(r"[ \t\r\f\v]+")
NEWLINE_RE = re.compile(r"\n{3,}")


def parse_args():
    parser = argparse.ArgumentParser(description="Import QUL tafsir SQLite databases into static JSON files.")
    parser.add_argument("--manifest", default="tmp/qul-cache/sqlite_manifest.tsv")
    parser.add_argument("--db-root", default="tmp/qul-sqlite-dbs")
    parser.add_argument("--ayah-data", default="data/ayah_data.json")
    parser.add_argument("--data-editions", default="data/editions.json")
    parser.add_argument("--tafsir-editions", default="tafsir/editions.json")
    parser.add_argument("--readme", default="README.md")
    parser.add_argument("--output-root", default="tafsir")
    return parser.parse_args()


def clean_text(value):
    value = value or ""
    value = BLOCK_TAG_RE.sub("\n", value)
    value = TAG_RE.sub("", value)
    value = html.unescape(value)
    value = "\n".join(SPACE_RE.sub(" ", line).strip() for line in value.splitlines())
    value = NEWLINE_RE.sub("\n\n", value)
    return value.strip()


def parse_key(key):
    surah, ayah = key.split(":", 1)
    return int(surah), int(ayah)


def expand_keys(row, surah_ayah_counts):
    ayah_key, _group_key, from_ayah, to_ayah, ayah_keys, _text = row
    if ayah_keys:
        return [parse_key(key.strip()) for key in ayah_keys.split(",") if key.strip()]
    if from_ayah and to_ayah:
        return expand_range(parse_key(from_ayah), parse_key(to_ayah), surah_ayah_counts)
    return [parse_key(ayah_key)]


def expand_range(start, end, surah_ayah_counts):
    """Expand a from/to pair, crossing surah boundaries when needed."""
    start_surah, start_ayah = start
    end_surah, end_ayah = end
    if start_surah == end_surah:
        return [(start_surah, ayah) for ayah in range(start_ayah, end_ayah + 1)]

    keys = []
    for surah in range(start_surah, end_surah + 1):
        first = start_ayah if surah == start_surah else 1
        last = end_ayah if surah == end_surah else surah_ayah_counts.get(surah, 0)
        keys.extend((surah, ayah) for ayah in range(first, last + 1))
    return keys


def load_manifest(path, db_root):
    rows = []
    for line in Path(path).read_text().splitlines():
        if not line.strip():
            continue
        resource_id, _hash, title, tags, source, _url = line.split("\t")
        resource_dir = next(Path(db_root).glob(f"{resource_id}-*"))
        db_files = [path for path in resource_dir.rglob("*.db") if path.is_file()]
        if len(db_files) != 1:
            raise RuntimeError(f"expected one database for resource {resource_id}, found {len(db_files)}")
        rows.append(
            {
                "id": int(resource_id),
                "name": title,
                "tags": [tag for tag in tags.split(",") if tag],
                "source": source,
                "db_path": db_files[0],
                "base_slug": db_files[0].stem,
            }
        )

    slug_counts = Counter(row["base_slug"] for row in rows)
    seen = Counter()
    for row in rows:
        base_slug = row["base_slug"]
        if slug_counts[base_slug] == 1:
            row["slug"] = base_slug
            continue
        seen[base_slug] += 1
        row["slug"] = f"{base_slug}-{row['id']}"
    return rows


def infer_language(tags):
    for tag in tags:
        normalized = tag.strip()
        if normalized.lower() == "tafsir" or normalized.lower().startswith("tafsir "):
            continue
        return normalized.lower()
    return "unknown"


def slugify(value):
    value = html.unescape(value).lower()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def generated_slug(resource):
    language = infer_language(resource["tags"])
    language_prefixes = {
        "arabic": "ar",
        "bengali": "bn",
        "english": "en",
        "russian": "ru",
        "urdu": "ur",
    }
    prefix = language_prefixes.get(language, slugify(language))
    name = slugify(resource["name"])
    if "tafsir" not in name and "mokhtasar" not in name:
        name = f"tafsir-{name}"
    return f"{prefix}-{name}"


def resolve_slugs(resources, existing):
    existing_by_id = {
        edition["id"]: edition
        for edition in existing
        if str(edition.get("source", "")).startswith("https://qul.tarteel.ai/")
    }
    existing_slugs = {edition["slug"] for edition in existing}
    base_counts = Counter(resource["base_slug"] for resource in resources)
    used = set()

    for resource in resources:
        if resource["id"] in existing_by_id:
            slug = existing_by_id[resource["id"]]["slug"]
        elif resource["base_slug"] in existing_slugs and base_counts[resource["base_slug"]] == 1:
            slug = resource["base_slug"]
        elif base_counts[resource["base_slug"]] == 1 and resource["base_slug"] != "abridged-explanation-of-the-quran":
            slug = resource["base_slug"]
        else:
            slug = generated_slug(resource)

        if slug in used:
            slug = f"{slug}-{resource['id']}"
        used.add(slug)
        resource["slug"] = slug


def load_surahs(path):
    surahs = json.loads(Path(path).read_text())
    return [(item["surah"], item["ayah"]) for item in surahs]


def import_database(db_path, surah_ayah_counts):
    con = sqlite3.connect(str(db_path))
    rows = con.execute(
        "select ayah_key, group_ayah_key, from_ayah, to_ayah, ayah_keys, text from tafsir"
    ).fetchall()
    con.close()

    by_key = defaultdict(list)
    group_texts = {}
    members = []
    for row in rows:
        ayah_key, group_ayah_key, _from_ayah, _to_ayah, _ayah_keys, raw_text = row
        text = clean_text(raw_text)
        if not text:
            # QUL exports text-less member rows that point at the row holding
            # the text (``group_ayah_key``); resolve them below instead of
            # dropping the ayah.
            members.append((ayah_key, group_ayah_key))
            continue

        group_texts[ayah_key] = text
        for key in expand_keys(row, surah_ayah_counts):
            if text not in by_key[key]:
                by_key[key].append(text)

    for ayah_key, group_ayah_key in members:
        text = group_texts.get(group_ayah_key)
        if not text:
            continue
        try:
            key = parse_key(ayah_key)
        except ValueError:
            continue
        if text not in by_key[key]:
            by_key[key].append(text)

    return {key: "\n\n".join(parts) for key, parts in by_key.items()}


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def write_tafsir(output_root, slug, texts, surahs):
    out_dir = Path(output_root) / slug
    if out_dir.exists():
        shutil.rmtree(out_dir)
    empty_by_surah = defaultdict(list)

    for surah, ayah_count in surahs:
        surah_ayahs = []
        for ayah in range(1, ayah_count + 1):
            text = texts.get((surah, ayah), "")
            if text:
                item = {"text": text, "ayah": ayah, "surah": surah}
                write_json(out_dir / str(surah) / f"{ayah}.json", item)
                surah_ayahs.append(item)
            else:
                empty_by_surah[surah].append({"surah": surah, "ayah": ayah})
        write_json(out_dir / f"{surah}.json", surah_ayahs)

    for surah, empty_ayahs in empty_by_surah.items():
        write_json(out_dir / str(surah) / "empty_ayahs.json", empty_ayahs)

    return {
        "ayah_files": len(texts),
        "surah_files": len(surahs),
        "empty_ayahs": sum(len(items) for items in empty_by_surah.values()),
    }


def load_editions(path):
    return json.loads(Path(path).read_text())


def upsert_editions(existing, resources):
    by_slug = {edition["slug"]: edition for edition in existing}
    ordered = [edition for edition in existing if edition["slug"] not in {resource["slug"] for resource in resources}]
    for resource in resources:
        previous = by_slug.get(resource["slug"], {})
        ordered.append(
            {
                "author_name": previous.get("author_name") or resource["name"],
                "id": resource["id"],
                "language_name": previous.get("language_name") or infer_language(resource["tags"]),
                "name": resource["name"],
                "slug": resource["slug"],
                "source": resource["source"],
            }
        )
    return ordered


def update_readme(path, editions):
    readme = Path(path)
    text = readme.read_text()
    text = re.sub(
        r"\*\*\d+ Tafsirs\*\*: Access \d+ different Tafsirs",
        f"**{len(editions)} Tafsirs**: Access {len(editions)} different Tafsirs",
        text,
    )
    header = (
        "| #  | Author Name | ID  | Language Name | Name | Slug | Source |\n"
        "| -- | ----------- | --- | ------------- | ---- | ---- | ------ |"
    )
    rows = [header]
    for index, edition in enumerate(editions, 1):
        rows.append(
            f"| {index} | {edition['author_name']} | {edition['id']} | {edition['language_name']} | "
            f"{edition['name']} | {edition['slug']} | {edition['source']} |"
        )
    table = "\n".join(rows)
    text = re.sub(r"## Editions:\n\n.*?\n\n## Share:", f"## Editions:\n\n{table}\n\n## Share:", text, flags=re.S)
    readme.write_text(text)


def main():
    args = parse_args()
    surahs = load_surahs(args.ayah_data)
    surah_ayah_counts = dict(surahs)
    resources = load_manifest(args.manifest, args.db_root)
    existing_editions = load_editions(args.data_editions)
    resolve_slugs(resources, existing_editions)

    stats = {}
    for resource in resources:
        print(f"import {resource['id']} {resource['slug']}")
        texts = import_database(resource["db_path"], surah_ayah_counts)
        stats[resource["slug"]] = write_tafsir(args.output_root, resource["slug"], texts, surahs)

    editions = upsert_editions(existing_editions, resources)
    write_json(Path(args.data_editions), editions)
    write_json(Path(args.tafsir_editions), editions)
    update_readme(args.readme, editions)
    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
