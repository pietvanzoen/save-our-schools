#!/usr/bin/env python3
"""Ingest caption records exported by tools/browser/youtube_captions.js (window.__next()).

Each export line looks like:  REC|<videoId>|<base64 of gzip(JSON record)>
Lines may be embedded in any text (saved console output, tool-result dumps). Records are decoded and passed to
tools/write_transcripts.py, which writes sources/youtube/transcripts/<date>_<videoId>.{tsv,txt,meta.json} and rebuilds
sources/youtube/videos_index.csv. Records carrying an `error` (no captions, video didn't load) are still recorded in the index.

Usage:  python3 tools/ingest_transcript_exports.py exports.txt [more files ...]
"""
import base64, gzip, json, re, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAT = re.compile(r"REC\|([A-Za-z0-9_-]{11})\|([A-Za-z0-9+/=]+)")

def main(paths):
    recs = {}
    for p in paths:
        for m in PAT.finditer(Path(p).read_text(errors="ignore")):
            rec = json.loads(gzip.decompress(base64.b64decode(m.group(2))))
            recs[rec["id"]] = rec  # last one wins (re-captures replace earlier ones)
    if not recs:
        print("no REC| lines found"); return
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(list(recs.values()), f)
    subprocess.run([sys.executable, str(ROOT / "tools/write_transcripts.py"), f.name], check=True)
    for r in recs.values():
        print(r["id"], r.get("meetings", ""), r.get("n_lines"), r.get("caption_lang", ""), r.get("error", ""))

if __name__ == "__main__":
    main(sys.argv[1:])
