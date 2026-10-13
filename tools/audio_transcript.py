#!/usr/bin/env python3
"""Build a speaker-labeled, lightly corrected transcript from a vendor diarization JSON export.

  python3 tools/audio_transcript.py <raw.json> <speakers.csv> <out.txt> <corrections.csv> "<title>" "<audio path>" "<source page>"

speakers.csv: speaker_id,label,role,evidence,confidence  (label is what appears in the transcript)
Words are kept verbatim; only mis-heard names/terms are fixed, shown in [brackets] (rules in RULES below), and every
fix is logged to corrections.csv. Consecutive segments from the same speaker less than 2 s apart are joined into one turn.
"""
import csv, json, re, sys
RULES = [  # (rule id, regex, replacement)
    ("wang", r"\bWong\b", "[Wang]"),
    ("pps", r"\bPBS (?=proposals)", "[PPS] "),
    ("dbrac", r"\bDBRAQ\b", "[DBRAC]"),
    ("resj", r"\bresj\b", "[RESJ]"),
    ("opb-staff-fass", r"\bAmalia Fast\b", "[Malya Fass]"),
    ("opb-staff-dicarlo", r"\bJeremy DiCarlo\b", "[Gemma DiCarlo]"),
    ("opb-staff-sadiq", r"\bShiraz Siddique\b", "[Sheraz Sadiq]"),
]
def hms(t): t = int(t); return f"{t//3600}:{t%3600//60:02d}:{t%60:02d}"
def main(raw, spk, out, corr, title, audio, page):
    segs = json.load(open(raw))["segments"]
    labels = {r["speaker_id"]: r for r in csv.DictReader(open(spk))}
    turns = []
    for s in segs:
        sid = s["speaker"]["id"]; txt = re.sub(r"\s+", " ", s["text"]).strip()
        if turns and turns[-1]["sid"] == sid and s["start_time"] - turns[-1]["end"] < 2.0:
            turns[-1]["text"] += " " + txt; turns[-1]["end"] = s["end_time"]
        else:
            turns.append({"sid": sid, "start": s["start_time"], "end": s["end_time"], "text": txt})
    log = []
    for t in turns:
        for rid, rx, rep in RULES:
            for m in re.finditer(rx, t["text"]):
                log.append((hms(t["start"]), rid, m.group(0).strip(), rep.strip()))
            t["text"] = re.sub(rx, rep, t["text"])
    with open(out, "w") as f:
        f.write(f"# {title}\n# Audio: {audio}\n# Program page: {page}\n")
        f.write(f"# Source: vendor speech-to-text export with automatic speaker separation ({raw.split('/')[-1]}), supplied by the repository owner 2026-10-13.\n")
        f.write("# CORRECTED COPY: words are as transcribed; mis-heard names/terms are fixed in [brackets] (log: corrections_*.csv in this folder);\n")
        f.write("# consecutive segments by the same speaker are joined into one turn. Timestamps are turn starts (H:MM:SS into the audio).\n")
        f.write("# Speakers (identification evidence and confidence in speakers.csv). Callers are members of the public and are described, not named;\n")
        f.write("# the host says callers' first names on air, and those spoken words are left as transcribed.\n")
        for sid, r in labels.items(): f.write(f"#   {r['label']}: {r['role']} [{r['confidence']}]\n")
        f.write("\n")
        for t in turns:
            f.write(f"[{hms(t['start'])}] {labels[t['sid']]['label']}: {t['text']}\n")
    with open(corr, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["file", "timestamp", "rule", "original", "fix"])
        for r in log: w.writerow([out.split("/")[-1], *r])
    print(len(segs), "segments ->", len(turns), "turns;", len(log), "corrections")
if __name__ == "__main__":
    main(*sys.argv[1:8])
