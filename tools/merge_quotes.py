#!/usr/bin/env python3
"""Verify and merge a new quote batch (analysis/people/quotes/<batch>.jsonl) into analysis/people/quotes_all.jsonl.

Checks for each quote:
  - the video transcript exists, and the quote text appears in it (whitespace/case-insensitive; caption '>>' markers ignored;
    [bracketed] repairs act as wildcards)
  - required fields are present and confidence is high|medium|low
Skips duplicates (same video_id + person + quote). Adds source_batch. Prints a report.

Run it only on NEW batches: older batch files predate corrections applied to quotes_all.jsonl.
Usage:  python3 tools/merge_quotes.py analysis/people/quotes/batch11.jsonl          # dry run (report only)
        python3 tools/merge_quotes.py analysis/people/quotes/batch11.jsonl --write  # append verified quotes
Quotes that fail verification are never merged; fix them in the batch file and re-run.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALL = ROOT / "analysis/people/quotes_all.jsonl"
TR = ROOT / "sources/youtube/transcripts"
REQ = ["person", "role", "date", "video_id", "timestamp", "seconds", "url", "quote", "paraphrase", "topics", "stance", "attribution_evidence", "confidence"]

def norm(s):
    return re.sub(r"\s+", " ", s.replace("\u2019", "'").lower()).strip()

def transcript_text(vid, cache={}):
    if vid not in cache:
        fs = list(TR.glob(f"*_{vid}.txt"))
        cache[vid] = norm(" ".join(re.sub(r"^\[\d+:\d\d:\d\d\] ", "", l).replace(">>", " ") for l in fs[0].read_text().splitlines())) if fs else None
    return cache[vid]

def found(quote, text):
    parts = [re.escape(norm(p)) for p in re.split(r"\[[^\]]*\]", quote)]
    pat = r".{0,40}?".join(p for p in parts if p) or re.escape(norm(quote))
    return re.search(pat, text) is not None

def main(batch, write):
    existing = [json.loads(l) for l in ALL.read_text().splitlines() if l.strip()]
    seen = {(q["video_id"], q["person"], norm(q["quote"])) for q in existing}
    ok, bad, dup = [], [], 0
    for i, l in enumerate(Path(batch).read_text().splitlines(), 1):
        if not l.strip(): continue
        q = json.loads(l)
        miss = [k for k in REQ if k not in q]
        text = transcript_text(q.get("video_id", ""))
        if miss: bad.append((i, f"missing fields {miss}"))
        elif q["confidence"] not in ("high", "medium", "low"): bad.append((i, "bad confidence"))
        elif text is None: bad.append((i, f"no transcript for {q['video_id']}"))
        elif not found(q["quote"], text): bad.append((i, f"quote not found verbatim: {q['quote'][:80]!r}"))
        elif (q["video_id"], q["person"], norm(q["quote"])) in seen: dup += 1
        else:
            q.setdefault("source_batch", Path(batch).stem); ok.append(q); seen.add((q["video_id"], q["person"], norm(q["quote"])))
    print(f"{len(ok)} new verified, {dup} duplicates skipped, {len(bad)} failed")
    for i, why in bad: print(f"  line {i}: {why}")
    if write and ok:
        with ALL.open("a") as f:
            for q in ok: f.write(json.dumps(q, ensure_ascii=False) + "\n")
        print(f"appended {len(ok)} quotes to {ALL.relative_to(ROOT)}")

if __name__ == "__main__":
    main(sys.argv[1], "--write" in sys.argv)
