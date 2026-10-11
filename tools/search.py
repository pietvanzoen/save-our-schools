#!/usr/bin/env python3
"""Full-text search over the PPS archive (sources + analysis) using SQLite FTS5.

  python3 tools/search.py "school closure" [--kind transcript|boardbook|pps_net|bond|news|analysis|quote]
                                         [--from 2026-01-01] [--to 2026-12-31] [--person "La Forte"] [-n 20]
  python3 tools/search.py --rebuild        # (re)build the index (done automatically on first use)

Index is stored at .cache/search.sqlite (not committed). Units indexed:
- transcript: ~60-second windows of each YouTube transcript, with a timestamped YouTube link
- boardbook / pps_net / bond: one row per PDF page (from .pdf.txt, or .pdf.ocr.txt when present), plus .md/.html text
- quote: each line of analysis/people/quotes_all.jsonl (person, date, link)
- news: each record of sources/news/index.jsonl (summary + facts + short quotes)
- analysis: each Markdown section of analysis/**.md
FTS5 query syntax applies: "exact phrase", AND/OR/NOT, prefix*, NEAR(a b, 10).
"""
import argparse, json, re, sqlite3, sys, html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / ".cache" / "search.sqlite"

def hms(sec):
    sec = int(sec); return f"{sec//3600}:{sec%3600//60:02d}:{sec%60:02d}"

def rows():
    # transcripts
    for tsv in sorted((ROOT / "sources/youtube/transcripts").glob("*.tsv")):
        vid = tsv.stem.split("_", 1)[1]; date = tsv.name[:10]
        meta = json.loads(tsv.with_suffix(".meta.json").read_text())
        title = (meta.get("meta") or {}).get("title", "")
        # caption text comes from the corrected copy (name fixes in [brackets]) when it exists; it aligns 1:1 with the TSV rows
        corr = ROOT / "analysis/transcripts_corrected" / (tsv.stem + ".txt")
        ctext = [re.sub(r"^\[\d+:\d\d:\d\d\] ?", "", l) for l in corr.read_text().splitlines() if re.match(r"^\[\d+:\d\d:\d\d\]", l)] if corr.exists() else None
        rows_tsv = [l.split("\t", 2) for l in tsv.read_text().splitlines()[1:]]
        if ctext is not None and len(ctext) != len(rows_tsv): ctext = None
        win, start = [], None
        for i, parts in enumerate(rows_tsv):
            if len(parts) < 3: continue
            ms = int(parts[0]); start = ms if start is None else start
            win.append(ctext[i] if ctext is not None else parts[2])
            if ms - start >= 60000:
                yield ("transcript", date, title, f"https://www.youtube.com/watch?v={vid}&t={start//1000}s",
                       f"[YT:{vid}@{hms(start/1000)}]", " ".join(win), "")
                win, start = [], None
        if win:
            yield ("transcript", date, title, f"https://www.youtube.com/watch?v={vid}&t={start//1000}s", f"[YT:{vid}@{hms(start/1000)}]", " ".join(win), "")
    # PDFs (page level)
    for kind, base in [("boardbook", "sources/boardbook"), ("pps_net", "sources/pps_net"), ("bond", "sources/bond")]:
        for txt in sorted((ROOT / base).rglob("*.pdf.txt")):
            ocr = Path(str(txt)[:-4] + ".ocr.txt")
            src = ocr if ocr.exists() else txt
            rel = str(txt.relative_to(ROOT))[:-4]
            date = (re.search(r"(20\d\d-\d\d-\d\d)", rel) or [None, ""])[1] if kind == "boardbook" else ""
            m = re.search(r"/(?:attachments|supplemental)/(\d+)_", rel) or re.search(r"/(?:minutes|public_notice)_(\d+)\.pdf", rel)
            ref = f"[BB:{m.group(1)}" if (kind == "boardbook" and m) else f"[PPS:{rel}"
            for i, page in enumerate(src.read_text(errors="ignore").split("\f"), 1):
                if len(page.strip()) > 30:
                    yield (kind, date, Path(rel).name, rel, f"{ref} p.{i}]", re.sub(r"\s+", " ", page), "")
        for f in sorted((ROOT / base).rglob("*.html")):
            t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", f.read_text(errors="ignore"), flags=re.S)
            t = html.unescape(re.sub(r"<[^>]+>", " ", t)); t = re.sub(r"\s+", " ", t)
            if len(t) > 50: yield (kind, "", f.name, str(f.relative_to(ROOT)), f"[PPS:{f.relative_to(ROOT)}]", t[:200000], "")
    # quotes
    qa = ROOT / "analysis/people/quotes_all.jsonl"
    if qa.exists():
        for l in qa.read_text().splitlines():
            if not l.strip(): continue
            q = json.loads(l)
            yield ("quote", q.get("date", ""), f"{q.get('person')} ({q.get('role','')})", q.get("url", ""),
                   f"[YT:{q.get('video_id')}@{q.get('timestamp')}] conf={q.get('confidence')}",
                   f"{q.get('quote','')} || {q.get('paraphrase','')} || {q.get('stance','')} || {' '.join(q.get('topics',[]))}", q.get("person", ""))
    # news
    ni = ROOT / "sources/news/index.jsonl"
    if ni.exists():
        for l in ni.read_text().splitlines():
            if not l.strip(): continue
            n = json.loads(l)
            body = " ".join([n.get("summary", ""), " ".join(n.get("key_facts", [])), " ".join(q.get("quote", "") for q in n.get("short_quotes", []))])
            yield ("news", n.get("date", ""), f"{n.get('outlet')}: {n.get('title')}", n.get("url", ""), f"[NEWS:{n.get('id')}]", body,
                   " ".join(p.get("name", "") for p in n.get("people_quoted", [])))
    # analysis markdown, split by heading
    for md in sorted((ROOT / "analysis").rglob("*.md")):
        rel = str(md.relative_to(ROOT)); date = (re.search(r"(20\d\d-\d\d-\d\d)", md.name) or [None, ""])[1]
        for sec in re.split(r"\n(?=#{1,3} )", md.read_text(errors="ignore")):
            if len(sec.strip()) > 30:
                head = sec.strip().split("\n", 1)[0][:120]
                yield ("analysis", date, f"{rel} — {head}", rel, rel, sec, "")

def build():
    DB.parent.mkdir(exist_ok=True)
    if DB.exists(): DB.unlink()
    con = sqlite3.connect(DB)
    con.execute("CREATE VIRTUAL TABLE docs USING fts5(kind UNINDEXED, date UNINDEXED, title, link UNINDEXED, cite UNINDEXED, body, person, tokenize='porter unicode61')")
    n = 0
    for r in rows():
        con.execute("INSERT INTO docs VALUES (?,?,?,?,?,?,?)", r); n += 1
    con.commit(); con.close(); print(f"indexed {n} units -> {DB}", file=sys.stderr)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="?"); ap.add_argument("--rebuild", action="store_true")
    ap.add_argument("--kind"); ap.add_argument("--from", dest="dfrom"); ap.add_argument("--to", dest="dto")
    ap.add_argument("--person"); ap.add_argument("-n", type=int, default=20); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.rebuild or not DB.exists(): build()
    if not a.query: return
    con = sqlite3.connect(DB)
    sql = "SELECT kind,date,title,link,cite,snippet(docs,5,'**','**',' … ',40) FROM docs WHERE docs MATCH ?"
    args = [a.query if not a.person else f"({a.query}) AND person:\"{a.person}\""]
    if a.kind: sql += " AND kind=?"; args.append(a.kind)
    if a.dfrom: sql += " AND date>=?"; args.append(a.dfrom)
    if a.dto: sql += " AND date<=?"; args.append(a.dto)
    sql += " ORDER BY rank LIMIT ?"; args.append(a.n)
    res = con.execute(sql, args).fetchall()
    if a.json:
        print(json.dumps([dict(zip(["kind", "date", "title", "link", "cite", "snippet"], r)) for r in res], indent=1)); return
    for k, d, t, l, c, s in res:
        print(f"[{k}] {d} {t}\n   {c}  {l}\n   {s}\n")

if __name__ == "__main__":
    main()
