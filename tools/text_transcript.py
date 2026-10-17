#!/usr/bin/env python3
"""Build a speaker-labeled, lightly corrected transcript from a plain-text radio transcript (no audio, no timestamps).

  python3 tools/text_transcript.py <raw.txt> <speakers.csv> <out.txt> <corrections.csv> "<title>" "<cite base>" "<source page>"

Raw format: a speaker-label line ("OPB", "Dr. Kimberlee Armstrong", ...) followed by that speaker's text line(s);
blank lines separate blocks. speakers.csv: raw_label,label,role,evidence,confidence.
Each turn is written as "[L<n>] <label>: <text>", where n is the line number in the RAW file where the turn's text
starts; cite as [AUDIO:<cite base>@L<n>]. Words are kept verbatim; only mis-heard names/terms are fixed, shown in
[brackets] (RULES below), and every fix is logged to corrections.csv.
"""
import csv, re, sys
RULES = [  # (rule id, regex, replacement)
    ("armstrong-first-name", r"\bKimberly\b", "[Kimberlee]"),
    ("sellwood", r"\b(?:Sailwood|Selwood)\b", "[Sellwood]"),
    ("pps", r"\bTPS\b", "[PPS]"),
    ("kiddos", r"\bKittles\b", "[Kiddos]"),
    ("state-school-fund", r"\bstate school fun\b", "state school [fund]"),
    ("rightsize-url", r"\bpps\. net forward slash right size\b", "pps[.net/rightsize]"),
]
def main(raw, spk, out, corr, title, cite, page):
    lines = open(raw, encoding="utf-8").read().splitlines()
    sp = {r["raw_label"]: r for r in csv.DictReader(open(spk))}
    turns, cur, i = [], None, 0
    while i < len(lines):
        s = lines[i].strip()
        if s in sp:
            cur = {"label": sp[s]["label"], "line": None, "text": []}; turns.append(cur)
        elif s and cur is not None:
            if cur["line"] is None: cur["line"] = i + 1
            cur["text"].append(s)
        i += 1
    log = []
    for t in turns:
        t["text"] = " ".join(t["text"])
        for rid, rx, rep in RULES:
            for m in re.finditer(rx, t["text"]): log.append((f"L{t['line']}", rid, m.group(0), rep))
            t["text"] = re.sub(rx, rep, t["text"])
    with open(out, "w") as f:
        f.write(f"# {title}\n# Audio: none archived (transcript only)\n# Cite: {cite}\n# Program page: {page}\n")
        f.write(f"# Source: plain-text transcript ({raw.split('/')[-1]}), supplied by the repository owner; origin and accuracy not verified against audio.\n")
        f.write("# CORRECTED COPY: words are as transcribed; mis-heard names/terms are fixed in [brackets] (log: corrections_*.csv in this folder).\n")
        f.write("# No timestamps exist: [L<n>] is the line in the raw transcript where the turn starts; cite as [AUDIO:<cite>@L<n>].\n")
        f.write("# Speakers (identification evidence and confidence in speakers_*.csv). Listeners are members of the public and are described,\n")
        f.write("# not named; names spoken on air are left as transcribed.\n")
        for r in sp.values(): f.write(f"#   {r['label']}: {r['role']} [{r['confidence']}]\n")
        f.write("\n")
        for t in turns: f.write(f"[L{t['line']}] {t['label']}: {t['text']}\n")
    with open(corr, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["file", "line", "rule", "original", "fix"])
        for r in log: w.writerow([out.split("/")[-1], *r])
    print(len(turns), "turns;", len(log), "corrections")
if __name__ == "__main__":
    main(*sys.argv[1:8])
