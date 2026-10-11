#!/usr/bin/env python3
"""OCR scanned pages of PDFs whose text layer is missing.
For each <file>.pdf.txt where >=30% of pages have <40 chars, writes <file>.pdf.ocr.txt:
the text-layer page where it exists, otherwise tesseract OCR of that page (300 dpi). Pages separated by \f.
A header line notes which pages were OCRed. OCR text may contain recognition errors; cite the PDF page."""
import subprocess, sys, tempfile, os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
ROOT = Path(__file__).resolve().parents[1]

def ocr_page(pdf, n, tmp):
    base = os.path.join(tmp, f"p{n}")
    subprocess.run(["pdftoppm", "-r", "300", "-f", str(n), "-l", str(n), "-gray", "-png", str(pdf), base], check=True, capture_output=True)
    png = [f for f in os.listdir(tmp) if f.startswith(f"p{n}") and f.endswith(".png")][0]
    out = subprocess.run(["tesseract", os.path.join(tmp, png), "-", "--psm", "3"], capture_output=True, text=True).stdout
    os.remove(os.path.join(tmp, png)); return out

def process(txt):
    pdf = Path(str(txt)[:-4]); out = Path(str(pdf) + ".ocr.txt")
    if out.exists(): return "skip"
    pages = txt.read_text(errors="ignore").split("\f")
    if pages and not pages[-1].strip(): pages = pages[:-1]
    done = []
    with tempfile.TemporaryDirectory() as tmp:
        res = []
        for i, p in enumerate(pages, 1):
            if len(p.strip()) < 40:
                try: res.append(ocr_page(pdf, i, tmp)); done.append(i)
                except Exception as e: res.append(f"[OCR failed: {e}]")
            else: res.append(p)
    out.write_text(f"[OCR supplement of {pdf.name}: pages {done} were OCRed with tesseract 5; other pages are the PDF text layer]\n" + "\f".join(res) + "\f")
    return f"ok {len(done)}"

if __name__ == "__main__":
    lst = [ROOT / l.split("\t")[0] for l in Path(sys.argv[1]).read_text().splitlines() if l.strip()]
    with ThreadPoolExecutor(int(sys.argv[2]) if len(sys.argv) > 2 else 6) as ex:
        for t, r in zip(lst, ex.map(process, lst)): print(r, t.relative_to(ROOT), flush=True)
