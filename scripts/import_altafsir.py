#!/usr/bin/env python3
"""Import one English tafsir from altafsir.com into tafsir/<slug>.

Example:
    python3 scripts/import_altafsir.py 86 en-asbab-al-nuzul-by-al-wahidi \
        --footer "Asbab Al-Nuzul by Al-Wahidi , trans. Mokrane Guezzou"

Every page is checked before use: the page title must name the requested
tafsir, surah and ayah, and the copyright footer must match. altafsir.com
served other tafsirs' text to the old concurrent Go scraper, so these checks
are what keep the data clean. Fetched pages are cached in tmp/altafsir-<id>.json
so an interrupted run can resume.
"""
import argparse
import html
import json
import re
import shutil
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

URL = ("https://www.altafsir.com/Tafasir.asp?tMadhNo=0&tTafsirNo={t}&tSoraNo={s}"
       "&tAyahNo={a}&tDisplay=yes&Page={p}&UserProfile=0&LanguageId=2")
USER_AGENT = "tafsir-api-import/1.0"


def get(url):
    # urllib fails on this server's responses (IncompleteRead); curl does not.
    err = None
    for attempt in range(5):
        r = subprocess.run(["curl", "-sSL", "--fail", "-m", "90", "-A", USER_AGENT, url], capture_output=True)
        if r.returncode == 0 and b"</html>" in r.stdout[-3000:].lower():
            return r.stdout.decode("cp1256", "replace")
        err = r.stderr.decode() or "truncated body"
        time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"{url}: {err}")


def parse(page, tafsir, surah, ayah):
    title = re.search(r"\((\d+)-(\d+)-(\d+)-(\d+)\)", page)
    if not title or title.groups() != (str(tafsir), "0", str(ayah), str(surah)):
        raise ValueError(f"{surah}:{ayah}: title mismatch {title and title.groups()}")
    i = page.find("TextResultEnglish")
    if i < 0:
        return None
    body = page[i:page.find("</div>", i)].split("</font></font>")[0]
    body = re.sub(r"(?i)<br\s*/?>", "\n", body)
    text = html.unescape(re.sub(r"<[^>]+>", "", body.split(">", 1)[1]))
    text = "\n".join(" ".join(line.split()) for line in text.splitlines())
    footer = re.search(r"class='CopyRight'>(.*?)<", page, re.S)
    pages = {int(p) for t, p, _ in re.findall(r"InnerLink_onchange\((\d+),(\d+),(\d+)\)", page) if t == str(tafsir)}
    return re.sub(r"\n{3,}", "\n\n", text).strip(), footer and footer.group(1).strip(), pages


def fetch_ayah(tafsir, surah, ayah, footer):
    parts, page_no, pages = [], 1, {1}
    while True:
        parsed = parse(get(URL.format(t=tafsir, s=surah, a=ayah, p=page_no)), tafsir, surah, ayah)
        if parsed is None:
            return None
        text, page_footer, found = parsed
        if page_footer != footer:
            raise ValueError(f"{surah}:{ayah} page {page_no}: unexpected footer {page_footer!r}")
        parts.append(text)
        pages |= found
        later = sorted(p for p in pages if p > page_no)
        if not later:
            return "\n\n".join(parts)
        page_no = later[0]


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("tafsir_id", type=int)
    parser.add_argument("slug")
    parser.add_argument("--footer", required=True, help="expected CopyRight footer text")
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()

    counts = {c["surah"]: c["ayah"] for c in json.loads(Path("data/ayah_data.json").read_text())}
    keys = [(s, a) for s in range(1, 115) for a in range(1, counts[s] + 1)]
    cache_path = Path(f"tmp/altafsir-{args.tafsir_id}.json")
    cache_path.parent.mkdir(exist_ok=True)
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    todo = [k for k in keys if f"{k[0]}:{k[1]}" not in cache]
    print(f"{len(todo)} ayahs to fetch")
    with ThreadPoolExecutor(args.workers) as pool:
        results = pool.map(lambda k: (k, fetch_ayah(args.tafsir_id, *k, args.footer)), todo)
        for n, ((surah, ayah), text) in enumerate(results, 1):
            cache[f"{surah}:{ayah}"] = text
            if n % 200 == 0:
                cache_path.write_text(json.dumps(cache, ensure_ascii=False))
                print(n)
    cache_path.write_text(json.dumps(cache, ensure_ascii=False))

    root = Path("tafsir") / args.slug
    shutil.rmtree(root, ignore_errors=True)
    root.mkdir(parents=True)
    total = 0
    for surah in range(1, 115):
        texts = {a: cache[f"{surah}:{a}"] for a in range(1, counts[surah] + 1)}
        if not any(texts.values()):
            continue
        (root / str(surah)).mkdir()
        items = []
        for ayah, text in texts.items():
            if text:
                write_json(root / str(surah) / f"{ayah}.json", {"surah": surah, "ayah": ayah, "text": text})
                items.append({"ayah": ayah, "surah": surah, "text": text})
        empty = [{"surah": surah, "ayah": a} for a, t in texts.items() if not t]
        if empty:
            write_json(root / str(surah) / "empty_ayahs.json", empty)
        write_json(root / f"{surah}.json", {"ayahs": items})
        total += len(items)
    print(f"wrote {total} ayahs to {root}")


if __name__ == "__main__":
    main()
