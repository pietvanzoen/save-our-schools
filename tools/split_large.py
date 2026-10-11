#!/usr/bin/env python3
"""Split files over GitHub's 100 MB limit. PDFs are split losslessly by page range with qpdf (each part readable);
other files are split into raw byte chunks (rejoin with: cat <name>.part* > <name>). Writes <name>.SPLIT.md with the
original size + sha256, then removes the original. Usage: split_large.py <root> [limit_MB=95]"""
import sys, os, hashlib, subprocess
from pathlib import Path
root = Path(sys.argv[1]); limit = int(sys.argv[2] if len(sys.argv) > 2 else 95) * 1024 * 1024
for f in sorted(root.rglob("*")):
    if not f.is_file() or f.stat().st_size <= limit or ".part" in f.name: continue
    size = f.stat().st_size; sha = hashlib.sha256(f.read_bytes()).hexdigest(); parts = []
    if f.suffix.lower() == ".pdf":
        n = int(subprocess.run(["pdfinfo", str(f)], capture_output=True, text=True).stdout.split("Pages:")[1].split()[0])
        k = size // limit + 1; step = -(-n // k)
        for a in range(1, n + 1, step):
            b = min(n, a + step - 1); out = f.with_name(f"{f.stem}.part{len(parts)+1}_p{a}-{b}.pdf")
            subprocess.run(["qpdf", str(f), "--pages", ".", f"{a}-{b}", "--", str(out)], check=True); parts.append(out.name)
        how = "split losslessly by page range with qpdf; each part is a valid PDF"
    else:
        data = f.read_bytes(); chunk = 90 * 1024 * 1024
        for i in range(0, size, chunk):
            out = f.with_name(f"{f.name}.part{i//chunk+1:02d}"); out.write_bytes(data[i:i+chunk]); parts.append(out.name)
        how = f"split into raw byte chunks; rejoin with: cat {f.name}.part* > {f.name}"
    big = [p for p in parts if (f.parent / p).stat().st_size > 100 * 1024 * 1024]
    f.with_name(f.name + ".SPLIT.md").write_text(
        f"# {f.name} (split for GitHub's 100 MB file limit)\n\nOriginal: {size} bytes, sha256 `{sha}`.\n{how}:\n" +
        "".join(f"- {p}\n" for p in parts) + "\nProvenance (URL, fetch time): see the _manifests/ folder for this source.\n")
    f.unlink(); print("split", f, "->", parts, "OVER LIMIT" if big else "")
