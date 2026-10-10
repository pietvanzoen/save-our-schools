#!/usr/bin/env python3
"""Build sources/boardbook/attachments_index.csv: one row per attachment with meeting, agenda item,
local paths, page count, text size and topic tags (keyword-based, for triage only)."""
import json, csv, re, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
BB = ROOT / "sources/boardbook"
TAGS = {
 "rightsizing": r"rightsiz|right-siz|school closure|consolidat|closure|merge|boundar|enrollment balanc|scenario|grade configuration|middle school transition|K-?8|feeder",
 "enrollment": r"enrollment|forecast|capture rate|PSU|population research|transfer|demograph",
 "bond_seismic": r"\bbond\b|seismic|modernization|FIOC|facilities improvement|capital|construction|Benson|Lincoln|Jefferson HS|Cleveland HS|Ida B\.? Wells|master plan|PTMP|BAC",
 "budget": r"budget|deficit|revenue|expenditure|fund balance|PERS|SSF|state school fund|levy|cuts|reduction|staffing",
 "facilities": r"facilit|capacity|utilization|square f|building condition|FCI|portable",
 "equity": r"equity|Black student|CBSE|title I|focus option|dual language|special education|SPED|ELL|immersion",
 "labor": r"PAT|union|bargain|collective|strike|PFSP",
 "governance": r"policy|superintendent evaluation|board goals|ethics|minutes|retreat|self-evaluation",
}
rows = []
for mj in sorted(BB.glob("meetings/*/meeting.json")):
    m = json.loads(mj.read_text()); d = mj.parent
    def add(att, item_title, kind):
        hits = list((d / ("attachments" if kind == "agenda" else "supplemental")).glob(f"{att['document_id']}_*.pdf"))
        pdf = hits[0] if hits else None
        pages, tchars = "", ""
        if pdf:
            info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
            mm = re.search(r"Pages:\s+(\d+)", info); pages = mm.group(1) if mm else ""
            t = pdf.with_suffix(".pdf.txt"); tchars = t.stat().st_size if t.exists() else ""
        blob = f"{item_title} {att['name']}"
        if pdf and pdf.with_suffix('.pdf.txt').exists():
            blob += " " + pdf.with_suffix('.pdf.txt').read_text(errors='ignore')[:4000]
        tags = [k for k, rx in TAGS.items() if re.search(rx, blob, re.I)]
        rows.append({"date": m["date"], "meeting_id": m["meeting_id"], "meeting": m["heading"], "kind": kind,
                     "agenda_item": item_title, "document_id": att["document_id"], "name": att["name"],
                     "pages": pages, "text_bytes": tchars, "tags": ";".join(tags),
                     "pdf": str(pdf.relative_to(ROOT)) if pdf else "", "url": att["download_url"]})
    for it in m["agenda_items"]:
        for a in it["attachments"]:
            add(a, it["title"], "agenda")
    for a in m.get("supplementals_files", []):
        add(a, "(supplemental resources)", "supplemental")
with open(BB / "attachments_index.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(len(rows), "rows;", sum(1 for r in rows if r["pdf"]), "with local pdf")
