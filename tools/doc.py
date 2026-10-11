#!/usr/bin/env python3
"""Find a source document by BoardBook document id (or a path fragment) and print a page of its text, for citing.

Usage:  python3 tools/doc.py 14505788            # list matching files, page count, meeting
        python3 tools/doc.py 14505788 2          # print page 2 (the N in [BB:14505788 p.2])
        python3 tools/doc.py school_impact/maplewood 3
        python3 tools/doc.py 14505788 2 --grep "Rose City"   # only lines matching, with page number
Matches attachments (<id>_*.pdf), supplementals, minutes_<id>.pdf and public_notice_<id>.pdf under sources/boardbook,
or any .pdf.txt under sources/ whose path contains the fragment. Uses the .pdf.ocr.txt version when it exists
(scanned PDFs). Pages are the form-feed-separated chunks of the text file, which equal the PDF page numbers.
If the PDF itself is needed (e.g. to render a page image) and this is a lightweight clone, fetch it with:
    git sparse-checkout add '<path>.pdf'   then   pdftoppm -f N -l N -png <path>.pdf /tmp/page
"""
import re, signal, sys
signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # quiet when piped to head
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def find(key):
    if key.isdigit():
        pats = [f"**/{key}_*.pdf.txt", f"**/minutes_{key}.pdf.txt", f"**/public_notice_{key}.pdf.txt"]
        hits = [p for pat in pats for p in (ROOT / "sources/boardbook").glob(pat)]
    else:
        hits = [p for p in (ROOT / "sources").rglob("*.pdf.txt") if key.lower() in str(p).lower()]
    return sorted(set(hits))

def text_of(p):
    ocr = Path(str(p)[:-4] + ".ocr.txt")
    return (ocr if ocr.exists() else p).read_text(errors="ignore"), ocr.exists()

def main():
    args = [a for a in sys.argv[1:]]
    grep = None
    if "--grep" in args:
        i = args.index("--grep"); grep = args[i + 1]; del args[i:i + 2]
    key = args[0]; page = int(args[1]) if len(args) > 1 else None
    hits = find(key)
    if not hits: sys.exit(f"no .pdf.txt matching {key!r}")
    for p in hits:
        txt, ocr = text_of(p)
        pages = txt.split("\f")
        if pages and not pages[-1].strip(): pages = pages[:-1]
        print(f"# {p.relative_to(ROOT)}  ({len(pages)} pages{', OCR text' if ocr else ''})")
        rng = [page] if page else (range(1, len(pages) + 1) if grep else [])
        for n in rng:
            if n < 1 or n > len(pages): print(f"  page {n} out of range"); continue
            body = pages[n - 1]
            if grep:
                for l in body.splitlines():
                    if re.search(grep, l, re.I): print(f"p.{n}: {l.strip()}")
            else:
                print(f"--- page {n} ---\n{body}")

if __name__ == "__main__":
    main()
