#!/usr/bin/env python3
"""Extract text from every PDF under sources/ into a sibling .txt (same name + .txt).
Uses poppler's pdftotext -layout. Pages are separated by form feeds (\f) so page numbers can be recovered.
Idempotent: skips PDFs whose .txt is newer than the PDF."""
import subprocess, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
ROOT = Path(__file__).resolve().parents[1]

def one(pdf):
    txt = pdf.with_suffix(pdf.suffix + ".txt")
    if txt.exists() and txt.stat().st_mtime >= pdf.stat().st_mtime:
        return "skip"
    r = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", str(pdf), str(txt)], capture_output=True, text=True, timeout=600)
    if r.returncode != 0:
        txt.write_text(f"[pdftotext failed: {r.stderr.strip()[:300]}]\n")
        return "fail"
    if txt.stat().st_size < 50:
        return "empty"   # probably scanned image PDF; needs OCR
    return "ok"

if __name__ == "__main__":
    base = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "sources")
    pdfs = sorted(base.rglob("*.pdf"))
    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(one, pdfs))
    from collections import Counter
    print(Counter(res))
    empties = [str(p.relative_to(ROOT)) for p, r in zip(pdfs, res) if r == "empty"]
    (ROOT / "sources" / "_needs_ocr.txt").write_text("\n".join(empties) + "\n")
