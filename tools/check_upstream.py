#!/usr/bin/env python3
"""Check whether documents we archived are still available upstream; log any that disappeared.

Run from a machine that can reach meetings.boardbook.org and drive.google.com (the cloud sandbox usually can't):

  python3 tools/check_upstream.py [--since 2026-08-01] [--log]

Checks every BoardBook document in sources/boardbook/attachments_index.csv dated on/after --since (plus minutes,
public notices and supplementals on disk) and every Google Drive file id in sources/pps_net manifests.
Prints the ones that no longer download. With --log, appends new disappearances to sources/_removed_upstream.csv
(our archived copy stays where it is; never delete it).
"""
import argparse, csv, datetime, glob, json, re, urllib.request, urllib.error, pathlib
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parents[1]


def probe(kind, i):
    u = (f"https://meetings.boardbook.org/Documents/DownloadPDF/{i}?org=915" if kind == "BoardBook"
         else f"https://drive.usercontent.google.com/download?id={i}&export=download&confirm=t")
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0", "Range": "bytes=0-1023"}), timeout=25)
        b = r.read(64); ct = r.headers.get("Content-Type", "")
        ok = b[:5] == b"%PDF-" if kind == "BoardBook" else "html" not in ct
        return kind, i, r.status, ok
    except urllib.error.HTTPError as e:
        return kind, i, e.code, False
    except Exception as e:
        return kind, i, str(e)[:40], None  # network problem: unknown, not "gone"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--since", default="2026-08-01"); ap.add_argument("--log", action="store_true")
    a = ap.parse_args()
    bb = {r["document_id"]: r["pdf"] for r in csv.DictReader(open(ROOT / "sources/boardbook/attachments_index.csv")) if r["date"] >= a.since}
    for f in glob.glob(str(ROOT / "sources/boardbook/meetings/*/*.pdf")) + glob.glob(str(ROOT / "sources/boardbook/meetings/*/supplemental/*.pdf")):
        if pathlib.Path(f).parent.name[:10] >= a.since or pathlib.Path(f).parent.parent.name[:10] >= a.since:
            m = re.search(r"(?:minutes|public_notice)_(\d+)\.pdf$|supplemental/(\d+)_", f)
            if m: bb.setdefault(m.group(1) or m.group(2), str(pathlib.Path(f).relative_to(ROOT)))
    drive = set()
    for f in glob.glob(str(ROOT / "sources/pps_net/_manifests/*.json")) + [str(ROOT / "sources/pps_net/_download_manifest.jsonl")]:
        drive |= set(re.findall(r"drive\.google\.com/file/d/([\w-]{20,})", open(f).read()))
    jobs = [("BoardBook", i) for i in bb] + [("Drive", i) for i in sorted(drive)]
    with ThreadPoolExecutor(6) as ex:
        res = list(ex.map(lambda j: probe(*j), jobs))
    gone = [r for r in res if r[3] is False]
    print(f"checked {len(bb)} BoardBook docs and {len(drive)} Drive files; {len(gone)} not available; "
          f"{sum(1 for r in res if r[3] is None)} could not be checked")
    known = set()
    log = ROOT / "sources/_removed_upstream.csv"
    if log.exists():
        known = {r["document_id_or_url"] for r in csv.DictReader(open(log))}
    new = [g for g in gone if g[1] not in known and not any(g[1][:12] in k for k in known)]
    for g in gone:
        print("GONE", g[0], g[1], g[2], "(already logged)" if g not in new else "")
    if a.log and new:
        with open(log, "a", newline="") as fh:
            w = csv.writer(fh)
            for kind, i, code, _ in new:
                w.writerow([datetime.date.today().isoformat(), kind, i, "", "", bb.get(i, ""), f"HTTP {code} on check"])


if __name__ == "__main__":
    main()
