#!/usr/bin/env python3
"""Build a speaker-labeled, lightly corrected transcript from a Substack podcast transcription export.

  python3 tools/substack_transcript.py <raw.json> <speakers.csv> <out.txt> <corrections.csv> "<title>" "<cite path>" "<page url>"

raw.json: Substack's unaligned transcript ({"segments":[{"text","start","end","speaker"}], "language"}).
speakers.csv: speaker_id,label,role,evidence,confidence. Optional override rows use speaker_id "@H:MM:SS" (segment start,
  truncated to the second) to relabel one segment that automatic diarization assigned to the wrong voice.
Words are kept verbatim; only mis-heard names/terms are fixed, shown in [brackets] (RULES below), and every fix is logged.
Consecutive segments from the same speaker less than 2 s apart are joined into one turn.
"""
import csv, json, re, sys
RULES = [  # (rule id, regex, replacement)
    ("chase-miller", r"\b(?:Rochelle|Rachelle),? Chase Miller\b", "[Rashelle Chase-Miller]"),
    ("chase-miller-surname", r"\bChase Miller\b", "[Chase-Miller]"),
    ("rashelle", r"\b(?:Rochelle|Rachelle)\b", "[Rashelle]"),
    ("elinor-jones", r"\bEleanor\b", "[Elinor]"),
    ("sabin", r"\bSaban\b", "[Sabin]"),
    ("kotek", r"\bKotec\b", "[Kotek]"),
    ("drazan", r"\bDrazen\b", "[Drazan]"),
    ("smart-reading", r"\bSmart Reading\b", "[SMART Reading]"),
    ("mcmenamins", r"\bMcMinimans\b", "[McMenamins]"),
    ("board", r"\brun for the sport\b", "run for the [board]"),
    ("besc", r"\b[Pp]rofit [Cc]enter\b", "[BESC]"),
]
def hms(t): t = int(t); return f"{t//3600}:{t%3600//60:02d}:{t%60:02d}"
def main(raw, spk, out, corr, title, cite, page):
    segs = json.load(open(raw))["segments"]
    rows = list(csv.DictReader(open(spk)))
    labels = {r["speaker_id"]: r for r in rows if not r["speaker_id"].startswith("@")}
    over = {r["speaker_id"][1:]: r["label"] for r in rows if r["speaker_id"].startswith("@")}
    bylabel = {r["label"]: sid for sid, r in labels.items()}
    turns = []
    for s in segs:
        sid = s.get("speaker") or "NONE"
        if hms(s["start"]) in over: sid = bylabel[over[hms(s["start"])]]
        txt = re.sub(r"\s+", " ", s["text"]).strip()
        if turns and turns[-1]["sid"] == sid and s["start"] - turns[-1]["end"] < 2.0:
            turns[-1]["text"] += " " + txt; turns[-1]["end"] = s["end"]
        else:
            turns.append({"sid": sid, "start": s["start"], "end": s["end"], "text": txt})
    log = []
    for t in turns:
        for rid, rx, rep in RULES:
            for m in re.finditer(rx, t["text"]):
                log.append((hms(t["start"]), rid, m.group(0).strip(), rep.strip()))
            t["text"] = re.sub(rx, rep, t["text"])
    with open(out, "w") as f:
        f.write(f"# {title}\n# Cite: [AUDIO:{cite}@H:MM:SS] (turn start)\n# Episode page: {page}\n")
        f.write(f"# Source: Substack's automatic transcription with automatic speaker separation ({raw.split('/')[-1]}); audio not archived.\n")
        f.write("# CORRECTED COPY: words are as transcribed; mis-heard names/terms are fixed in [brackets] (log: corrections_*.csv in this folder);\n")
        f.write("# consecutive segments by the same speaker are joined into one turn. Timestamps are turn starts (H:MM:SS into the episode).\n")
        f.write("# Speakers (identification evidence and confidence in speakers_*.csv):\n")
        for sid, r in labels.items(): f.write(f"#   {r['label']}: {r['role']} [{r['confidence']}]\n")
        if over: f.write(f"# Segment relabels (diarization errors): {', '.join(f'{k} -> {v}' for k, v in over.items())}\n")
        f.write("\n")
        for t in turns:
            f.write(f"[{hms(t['start'])}] {labels[t['sid']]['label']}: {t['text']}\n")
    with open(corr, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["file", "timestamp", "rule", "original", "fix"])
        for r in log: w.writerow([out.split("/")[-1], *r])
    print(len(segs), "segments ->", len(turns), "turns;", len(log), "corrections")
if __name__ == "__main__":
    main(*sys.argv[1:8])
