#!/usr/bin/env python3
"""Import the "Al-Jami' Al-Wajiz" tafsir into static JSON files.

Source: https://github.com/yamanamr/quran-tafsir-jami-wajiz
Author: Dr. Ayman Fathih Al-Amer (الشيخ الدكتور أيمن فاتح آل عامر)
License: CC BY-ND 4.0 — the tafsir wording must never be modified.

Upstream ships three JSON files with one record per ayah. Each record carries
``tafsir_text`` (plain text, the variant this API serves) alongside an HTML
variant that is not used here because the API schema is plain text.

Eight records in surahs 2 and 3 merge the explanation of the following ayah
into the previous record, separated by the author's own
"<next ayah number> - " marker. The import splits those records at the marker
so every ayah keeps its own text without changing any wording.
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from import_qul_sqlite import (
    load_editions,
    load_surahs,
    update_readme,
    write_json,
    write_tafsir,
)

# Stable id outside the QUL resource-id space so future QUL imports cannot
# collide with it.
EDITION = {
    "author_name": "Dr. Ayman Fathih Al-Amer",
    "id": 9001,
    "language_name": "arabic",
    "name": "Tafsir Al-Jami' Al-Wajiz",
    "slug": "ar-tafsir-al-jami-al-wajiz",
    "source": "https://github.com/yamanamr/quran-tafsir-jami-wajiz",
}

SOURCE_FILES = [
    "ayah_tafsir_db_surah_001-020.json",
    "ayah_tafsir_db_surah_021-060.json",
    "ayah_tafsir_db_surah_061-114.json",
]

ARABIC_DIGITS = "٠١٢٣٤٥٦٧٨٩"


def arabic_numeral(number):
    return "".join(ARABIC_DIGITS[int(digit)] for digit in str(number))


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-dir",
        default="tmp/jami-wajiz",
        help="Directory containing the cloned quran-tafsir-jami-wajiz repository",
    )
    parser.add_argument("--ayah-data", default="data/ayah_data.json")
    parser.add_argument("--data-editions", default="data/editions.json")
    parser.add_argument("--tafsir-editions", default="tafsir/editions.json")
    parser.add_argument("--readme", default="README.md")
    parser.add_argument("--output-root", default="tafsir")
    return parser.parse_args()


def load_records(source_dir):
    records = {}
    for name in SOURCE_FILES:
        for row in json.loads((Path(source_dir) / name).read_text()):
            key = (int(row["surah_number"]), int(row["ayah_number"]))
            if key in records:
                raise RuntimeError(f"duplicate record for ayah {key}")
            text = (row["tafsir_text"] or "").strip()
            if not text:
                raise RuntimeError(f"empty tafsir_text for ayah {key}")
            records[key] = text
    return records


def find_split_marker(text, ayah):
    """Locate the author's "<next ayah> - " marker inside a merged record."""
    pattern = re.compile(r"(?<![0-9٠-٩])" + arabic_numeral(ayah) + r"\s*[-–—]")
    matches = list(pattern.finditer(text))
    if not matches:
        return None
    if len(matches) > 1:
        raise RuntimeError(
            f"ambiguous split marker for ayah {ayah}: {len(matches)} candidates"
        )
    return matches[0]


def split_merged_records(records, surah_ayah_counts):
    """Split records that merge the next ayah's explanation into their text."""
    missing = [
        (surah, ayah)
        for surah, ayah_count in surah_ayah_counts.items()
        for ayah in range(1, ayah_count + 1)
        if (surah, ayah) not in records
    ]
    for key in sorted(missing):
        surah, ayah = key
        previous_key = (surah, ayah - 1)
        if previous_key not in records:
            raise RuntimeError(f"ayah {key} missing and has no previous record")
        previous_text = records[previous_key]
        marker = find_split_marker(previous_text, ayah)
        if marker is None:
            raise RuntimeError(f"no split marker for ayah {key} inside {previous_key}")
        records[previous_key] = previous_text[: marker.start()].rstrip()
        records[key] = previous_text[marker.start() :].strip()
        print(f"split merged record {previous_key} -> {key}")

    gaps = [
        (surah, ayah)
        for surah, ayah_count in surah_ayah_counts.items()
        for ayah in range(1, ayah_count + 1)
        if (surah, ayah) not in records
    ]
    if gaps:
        raise RuntimeError(f"unresolved ayahs after splitting: {gaps[:20]}")
    return records


def verify_records(records):
    """Every record must open with the author's own ayah-number marker."""
    broken = []
    for (surah, ayah), text in records.items():
        if not re.match(r"\s*" + arabic_numeral(ayah) + r"\s*[-–—]", text):
            broken.append((surah, ayah))
    if broken:
        raise RuntimeError(f"records without their own ayah marker: {broken[:20]}")


def upsert_edition(existing, edition):
    kept = [item for item in existing if item["slug"] != edition["slug"]]
    kept.append(edition)
    return kept


def main():
    args = parse_args()
    surahs = load_surahs(args.ayah_data)
    surah_ayah_counts = dict(surahs)

    records = load_records(args.source_dir)
    records = split_merged_records(records, surah_ayah_counts)
    verify_records(records)

    texts = {key: records[key] for key in sorted(records)}
    stats = write_tafsir(args.output_root, EDITION["slug"], texts, surahs)

    editions = upsert_edition(load_editions(args.data_editions), EDITION)
    write_json(Path(args.data_editions), editions)
    write_json(Path(args.tafsir_editions), editions)
    update_readme(args.readme, editions)
    print(json.dumps({EDITION["slug"]: stats}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    sys.exit(main())
