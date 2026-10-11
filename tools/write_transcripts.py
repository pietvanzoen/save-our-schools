#!/usr/bin/env python3
"""Write captured YouTube caption records (JSON list from the browser capture job) into
sources/youtube/transcripts/<date>_<videoId>.{tsv,txt,meta.json} and rebuild sources/youtube/videos_index.csv.

TSV columns: start_ms, duration_ms, text  (YouTube json3 caption events; ASR = auto-generated)
TXT: one line per caption event: [H:MM:SS] text   (for reading/grepping)"""
import json, sys, csv
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sources/youtube/transcripts"

def hms(ms):
    s = int(ms) // 1000
    return f"{s//3600}:{s%3600//60:02d}:{s%60:02d}"

def write(rec):
    vid = rec["id"]
    meetings = rec.get("meetings", "")
    date = meetings.split("|")[0] if meetings else (rec.get("meta", {}).get("publishDate", "")[:10] or "unknown")
    base = OUT / f"{date}_{vid}"
    meta = {k: v for k, v in rec.items() if k != "tsv"}
    meta["url"] = f"https://www.youtube.com/watch?v={vid}"
    meta["boardbook_meetings"] = [m.split("|") for m in meetings.split(";")] if meetings else []
    base.with_suffix(".meta.json").write_text(json.dumps(meta, indent=1))
    if rec.get("tsv"):
        base.with_suffix(".tsv").write_text("start_ms\tduration_ms\ttext\n" + rec["tsv"] + "\n")
        lines = []
        for l in rec["tsv"].split("\n"):
            a, b, t = l.split("\t", 2)
            lines.append(f"[{hms(a)}] {t}")
        title = rec.get("meta", {}).get("title", "")
        hdr = (f"# {title}\n# Video: https://www.youtube.com/watch?v={vid}\n# Source: YouTube captions "
               f"({rec.get('caption_kind','?')}, {rec.get('caption_lang','?')}), fetched {rec.get('fetched_at','')}\n"
               f"# BoardBook meeting(s): {meetings}\n# Link to a moment: https://www.youtube.com/watch?v={vid}&t=<seconds>s\n\n")
        base.with_suffix(".txt").write_text(hdr + "\n".join(lines) + "\n")
    return vid

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    n = 0
    for f in sys.argv[1:]:
        for rec in json.load(open(f)):
            write(rec); n += 1
    rows = []
    for m in sorted(OUT.glob("*.meta.json")):
        d = json.loads(m.read_text()); md = d.get("meta", {})
        rows.append({"date": m.name[:10], "video_id": d["id"], "title": md.get("title"), "length_s": md.get("lengthSeconds"),
                     "caption_kind": d.get("caption_kind"), "n_lines": d.get("n_lines"), "error": d.get("error", ""),
                     "boardbook_meetings": d.get("meetings"), "url": d["url"],
                     "transcript": str(m.with_name(m.name.replace(".meta.json", ".txt")).relative_to(ROOT)) if d.get("n_lines") else ""})
    with open(ROOT / "sources/youtube/videos_index.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print("wrote", n, "records;", len(rows), "videos indexed;", sum(1 for r in rows if r["n_lines"]), "with transcripts")
