#!/usr/bin/env python3
"""Validate the generated tafsir data tree.

Checks performed for every edition:

* each ``<surah>.json`` index matches the per-ayah files (allowing the legacy
  ``{ "ayahs": [...] }`` wrapper and unsorted legacy indexes)
* an ayah never has both a per-ayah file and an ``empty_ayahs.json`` entry
* per-ayah files never contain empty text

Coverage gaps (ayahs without text and without an ``empty_ayahs.json`` entry)
are reported as warnings because several upstream tafsirs comment only on a
subset of the Quran.

Exits with a non-zero status when a hard error is found.
"""

import argparse
import json
import sys
from pathlib import Path

DEFAULT_AYAH_DATA = "data/ayah_data.json"


def load_ayah_counts(path=DEFAULT_AYAH_DATA):
    data = json.loads(Path(path).read_text())
    return {item["surah"]: item["ayah"] for item in data}


def normalize_index(path):
    data = json.loads(path.read_text())
    if isinstance(data, dict):
        if "ayahs" in data and data["ayahs"] is None:
            raise ValueError(f'{path} has "ayahs": null instead of a list')
        data = data.get("ayahs") or []
    if not isinstance(data, list):
        raise ValueError(f"{path} is not a JSON list of ayahs")
    try:
        return sorted(data, key=lambda item: item["ayah"])
    except (KeyError, TypeError):
        raise ValueError(f"{path} contains ayah entries without an ayah number")


def read_ayah_items(surah_dir):
    items = []
    for path in sorted(surah_dir.glob("*.json")):
        if path.name == "empty_ayahs.json":
            continue
        data = json.loads(path.read_text())
        if not isinstance(data, dict):
            raise ValueError(f"{path} is not a JSON object")
        text = data.get("text")
        if not text or not text.strip():
            raise ValueError(f"{path} has empty text")
        items.append({"text": text, "ayah": int(path.stem), "surah": int(surah_dir.name)})
    return sorted(items, key=lambda item: item["ayah"])


def check_edition(edition_dir, ayah_counts, errors, warnings):
    slug = edition_dir.name
    covered = set()
    checkable = set()

    for surah_dir in sorted((p for p in edition_dir.iterdir() if p.is_dir() and p.name.isdigit()), key=lambda p: int(p.name)):
        surah = int(surah_dir.name)
        if surah in ayah_counts:
            checkable |= {(surah, ayah) for ayah in range(1, ayah_counts[surah] + 1)}
        try:
            items = read_ayah_items(surah_dir)
        except ValueError as error:
            errors.append(str(error))
            continue

        empty_entries = []
        empty_path = surah_dir / "empty_ayahs.json"
        if empty_path.exists():
            empty_entries = json.loads(empty_path.read_text())
            if not isinstance(empty_entries, list):
                errors.append(f"{empty_path} is not a JSON list")
                empty_entries = []

        item_ayahs = {item["ayah"] for item in items}
        empty_ayahs = {entry["ayah"] for entry in empty_entries}
        duplicates = item_ayahs & empty_ayahs
        if duplicates:
            errors.append(f"{slug} {surah}: ayahs both written and marked empty: {sorted(duplicates)}")

        index_path = edition_dir / f"{surah}.json"
        if not index_path.exists():
            errors.append(f"{slug} {surah}: missing {index_path.name}")
        else:
            try:
                index_items = normalize_index(index_path)
            except ValueError as error:
                errors.append(str(error))
                index_items = None
            if index_items is not None and index_items != items:
                errors.append(f"{slug} {surah}: {index_path.name} does not match the per-ayah files")

        covered |= {(surah, ayah) for ayah in item_ayahs | empty_ayahs}

    missing = checkable - covered
    if missing:
        warnings.append(f"{slug}: {len(missing)} ayahs have neither text nor an empty_ayahs entry")


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tafsir-root", default="tafsir")
    parser.add_argument("--ayah-data", default=DEFAULT_AYAH_DATA)
    return parser.parse_args()


def main():
    args = parse_args()
    root = Path(args.tafsir_root)
    editions = {path.name: path for path in sorted(root.iterdir()) if path.is_dir()}
    ayah_counts = load_ayah_counts(args.ayah_data)

    errors = []
    warnings = []
    for edition_dir in editions.values():
        check_edition(edition_dir, ayah_counts, errors, warnings)

    for warning in warnings:
        print(f"warning: {warning}")
    for error in errors:
        print(f"error: {error}")
    print(f"checked {len(editions)} editions: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
