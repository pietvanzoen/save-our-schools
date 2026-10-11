#!/usr/bin/env python3
"""Build corrected copies of the meeting transcripts, fixing obvious auto-caption mis-hearings of names.

The raw captions in sources/youtube/transcripts/ are primary sources and are never edited. This script writes
analysis/transcripts_corrected/<date>_<videoId>.txt with the same lines and timestamps, where each correction is
shown in [brackets], e.g. "Maplewood drops to 247 students, [Rieke] to 311". The brackets follow the repo's quoting
rule (CLAUDE.md rule 3: caption repairs are bracketed), so text quoted from the corrected copy is a valid quote, and
tools/merge_quotes.py still verifies it against the raw captions (brackets act as wildcards).

Every change is logged in analysis/transcripts_corrected/corrections.csv (video, timestamp, rule, original, fix).

Rules are deliberately conservative:
  - "any" rules fix spellings that only ever mean one PPS name (e.g. Englesman -> Engelsman, Cresten -> Creston).
  - "title" rules fix common words only right after a title (e.g. "Director Split" -> Director [Splitt],
    "Vice Chair the pass" -> Vice Chair [DePass], "Chair Wong" -> Chair [Wang]).
  - Real people or places with similar names are excluded (e.g. Brian Stevenson, Cheryl Pitman, the Albina district,
    the Lents neighborhood, Paul Hogland).
Add a rule by appending to RULES and re-running. Usage:  python3 tools/caption_fixes.py [--stats]
"""
import csv, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "sources/youtube/transcripts"
OUT = ROOT / "analysis/transcripts_corrected"

TITLE = (r"(?:vice[\s-]+chair|co-?chair|chair(?:woman|person)?|directors?|board\s+members?|dr\.?|doctor|"
         r"superintendent|student\s+rep(?:resentative)?|representative|commissioner|thank\s+you,?)")
BOARD = r"(?:vice[\s-]+chair|chair(?:woman|person)?|directors?|board\s+members?|thank\s+you,?)"
W = r"\s+"  # word gap (may cross a caption line break)

# (rule_id, scope, regex for the misheard text, canonical replacement)
RULES = [
    # ---- board members ----
    ("wang", "board", r"wong", "Wang"),
    ("wang-eddie", "any", r"(?<=eddie\s)wong|(?<=edward\s)wong", "Wang"),
    ("depass", "board", r"(?:of" + W + r")?(?:the|to|de)" + W + r"pass|pass|deass|dass|deas|dpass|defass|deepass|depasu", "DePass"),
    ("depass-any", "any", r"deass|defass|deepass|depasu", "DePass"),
    ("depass-michelle", "any", r"(?<=michelle\s)(?:the|to)" + W + r"pass", "DePass"),
    ("splitt", "board", r"split|slit|splits|splitz|splint", "Splitt"),
    ("splitt-christy", "any", r"(?<=christy\s)split|(?<=chrisy\s)split|(?<=christie\s)split|(?<=chrissy\s)split", "Splitt"),
    ("engelsman", "any", r"englesman|anglesman|inglesman|ingelsman|englesmen|danglesman|zanglesman", "Engelsman"),
    ("engelsman-title", "board", r"engles|engleson|englesmith|engelman|engleman|angelman|englishman", "Engelsman"),
    ("laforte", "any", r"lefort|laforte|lafort|leaffort|leffort|lafourte|leaport", "La Forte"),
    ("laforte-title", "board", r"lefor|leford|laporte|lafore|laforge|laforest|lafonte|la" + W + r"fort|le" + W + r"fort|la" + W + r"porte", "La Forte"),
    ("sullivan", "board", r"suvan|svin|suvin|stullivan|solivan|sulliv", "Sullivan"),
    ("sullivan-any", "any", r"stullivan|solivan", "Sullivan"),
    ("greene", "board", r"green", "Greene"),
    ("hollands", "board", r"holland|hollin|holl|hogland(?=\s+(?:and|moves|seconds))", "Hollands"),
    ("brim-edwards", "any", r"bram" + W + r"edwards|brenwards|medwards", "Brim-Edwards"),
    ("brim-edwards-title", "board", r"bram|bim", "Brim-Edwards"),
    ("ritorto", "any", r"retorto|rtorto|rturto|rtortoro|rorto|rtrto", "Ritorto"),
    ("ritorto-title", "title", r"rtor|rto|torto|rotoro|roro|rito", "Ritorto"),
    ("sandell", "any", r"(?<=rose\s)sand(?:al|el|all|elle)", "Sandell"),
    ("sandell-title", "title", r"sand(?:al|el|all|elle)", "Sandell"),
    # ---- staff ----
    ("armstrong", "any", r"arm" + W + r"strong(?=\W)|arshong|armstron(?=\W)|armstong", "Armstrong"),
    ("armstrong-title", "title", r"arshaw|armshaw", "Armstrong"),
    ("calvert", "any", r"calbertt|calbert", "Calvert"),
    ("calvert-margaret", "any", r"(?<=margaret\s)(?:calver|caler|carler|halver)(?=\W)", "Calvert"),
    ("kafoury", "any", r"kafuri|kafori|capori|kapori|capfori", "Kafoury"),
    ("glasgow", "any", r"glascow|glasow|(?<=emily\s)glasco|(?<=dr\.\s)glasco|(?<=dr\s)glasco", "Glasgow"),
    ("hristic", "any", r"histich|hristitch|rristic|tristitch|histiche", "Hristić"),
    ("procedeo", "any", r"procedio|proedo", "Procedeo"),
    ("zavitkovski", "any", r"zavikovski|zavikosski", "Zavitkovski"),
    ("dan-jung", "any", r"(?<=dan\s)young(?=\W)", "Jung"),
    # ---- schools and places ----
    ("rieke", "any", r"ricky(?!\s+wrote)", "Rieke"),
    ("stephenson", "any", r"(?<!brian\s)(?<!bryan\s)stevenson|stephvenson", "Stephenson"),
    ("creston", "any", r"crestston|cresten", "Creston"),
    ("creston-crescent", "any", r"(?-i:Crescent)", "Creston"),
    ("woodmere", "any", r"woodmir|woodmre", "Woodmere"),
    ("sellwood", "any", r"cellwood|swood|cwood|selwood|sailwood", "Sellwood"),
    ("marysville", "any", r"mary'sville|maryville|marville|mary'svilles", "Marysville"),
    ("abernethy", "any", r"abernathy", "Abernethy"),
    ("mt-tabor", "any", r"(?<=mount\s)taber|(?<=mt\.\s)taber|(?<=mt\s)taber", "Tabor"),
    ("ockley", "any", r"(?:oley|olay|aley|auckley|ackley|kley)(?=\s+green)", "Ockley"),
    ("woodlawn", "any", r"woodlon|woodline", "Woodlawn"),
    ("duniway", "any", r"dunaway|dunway|dunaways", "Duniway"),
    ("atkinson", "any", r"atinson", "Atkinson"),
    ("rigler", "any", r"wrigler|wriggler|wiggler|regler", "Rigler"),
    ("glencoe", "any", r"gleno|glenco(?=\W)", "Glencoe"),
    ("beaumont", "any", r"bumont|bulmont", "Beaumont"),
    ("llewellyn", "any", r"luwellyn|llewellen|lellan", "Llewellyn"),
    ("humboldt", "any", r"humbult|humbold(?=\W)", "Humboldt"),
    ("ainsworth", "any", r"ainssworth|aworth", "Ainsworth"),
    ("sitton", "any", r"sitin|sitten|sittin", "Sitton"),
    ("polytechnic", "any", r"polytenic", "Polytechnic"),
    ("lincoln", "any", r"linkoln|lincol(?=\W)", "Lincoln"),
    ("arleta", "any", r"arita|alita(?=\s+(?:elementary|annex|facility))", "Arleta"),
    ("bridlemile", "any", r"bridal" + W + r"mile|solid" + W + r"mle", "Bridlemile"),
    ("boise-eliot", "any", r"bois(?:e|ey)" + W + r"elliott?|boisey", "Boise-Eliot"),
    ("ida-b-wells", "any", r"(?:idw|iw|idb|ida" + W + r"b\.?)" + W + r"wells", "Ida B. Wells"),
    ("west-sylvan", "any", r"(?<=west\s)silvin|(?<=east\s)silvin", "Sylvan"),
    ("faubion", "any", r"fabian|fabien|fation", "Faubion"),
    ("hosford", "any", r"hoffsford|husford", "Hosford"),
    ("hayhurst", "any", r"palhurst|hayhust", "Hayhurst"),
    ("roosevelt", "any", r"rosevelt|roselt|rose" + W + r"correct", "Roosevelt"),
    ("terwilliger", "any", r"turilliger", "Terwilliger"),
    ("markham", "any", r"markhamm", "Markham"),
    ("alameda", "any", r"alama(?=\W)|alamas", "Alameda"),
    ("astor", "any", r"(?-i:Aster)(?=\W)", "Astor"),
    ("segc", "any", r"southeast" + W + r"guiden" + W + r"coalition", "Southeast Guiding Coalition"),
    ("albina-vision", "any", r"(?:alpine|albino)" + W + r"vision" + W + r"trust", "Albina Vision Trust"),
]

def compile_rules():
    out = []
    for rid, scope, pat, canon in RULES:
        core = rf"(?P<fix>{pat})(?P<poss>'s)?\b"
        if scope in ("title", "board"):
            rx = re.compile(rf"\b(?P<pre>{TITLE if scope == 'title' else BOARD}\s+)" + core, re.I)
        else:
            rx = re.compile(rf"\b" + core, re.I)
        out.append((rid, rx, canon))
    return out

def fix_text(text, rules, log):
    for rid, rx, canon in rules:
        def rep(m):
            orig = m.group("fix")
            norm = lambda s: re.sub(r"[\s.\-']", "", s.lower())
            if norm(orig) == norm(canon): return m.group(0)
            log.append((rid, orig, canon, m.start("fix")))
            nl = "\n" if "\n" in orig else ""
            return (m.groupdict().get("pre") or "") + f"[{canon}]" + nl + (m.group("poss") or "")
        text = rx.sub(rep, text)
    return text

def main():
    rules = compile_rules(); OUT.mkdir(parents=True, exist_ok=True)
    stats, rows = Counter(), []
    for f in sorted(SRC.glob("*.txt")):
        lines = f.read_text().splitlines()
        stamps = [re.match(r"(\[\d+:\d\d:\d\d\]) ?(.*)", l) for l in lines]
        # only caption lines are corrected; header lines ("# ...") are blanked during matching and restored after
        texts = [m.group(2) if m else "" for m in stamps]
        joined = "\n".join(texts)
        # line start offsets, to map a match back to its caption line (offsets shift as fixes apply; recompute per rule)
        log = []
        for rid, rx, canon in rules:
            starts = [0]
            for t in joined.split("\n")[:-1]: starts.append(starts[-1] + len(t) + 1)
            sub = []
            joined = fix_text(joined, [(rid, rx, canon)], sub)
            for (r, orig, c, pos) in sub:
                ln = max(i for i, s in enumerate(starts) if s <= pos)
                ts = stamps[ln].group(1).strip("[]") if stamps[ln] else ""
                rows.append({"video_id": f.stem.split("_", 1)[1], "file": f.name, "timestamp": ts, "rule": r,
                             "original": orig.replace("\n", " "), "fix": c})
                stats[r] += 1
        new = joined.split("\n")
        assert len(new) == len(lines), f.name
        out = [(m.group(1) + " " + t) if m else lines[i] for i, (m, t) in enumerate(zip(stamps, new))]
        for i, l in enumerate(out):
            if l.startswith("# Source: YouTube captions"):
                out[i] = l + f" | CORRECTED COPY: caption name fixes shown in [brackets] by tools/caption_fixes.py; raw text: sources/youtube/transcripts/{f.name}"
        (OUT / f.name).write_text("\n".join(out) + "\n")
    with (OUT / "corrections.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["video_id", "file", "timestamp", "rule", "original", "fix"])
        w.writeheader(); w.writerows(rows)
    print(f"{len(rows)} corrections in {len({r['file'] for r in rows})} transcripts -> {OUT.relative_to(ROOT)}")
    if "--stats" in sys.argv:
        for r, n in stats.most_common(): print(f"  {n:5d}  {r}")

if __name__ == "__main__":
    main()
