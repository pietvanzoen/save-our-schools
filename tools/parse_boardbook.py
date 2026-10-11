#!/usr/bin/env python3
"""Parse downloaded BoardBook meeting pages into structured JSON + markdown text.

Input:  sources/boardbook/meetings/<YYYY-MM-DD>_<meetingid>_<slug>/{agenda,minutes,public_notice,supplementals}.html
        sources/boardbook/boardbook_index_2025_2026.json (meeting list scraped from the org page)
Output: sources/boardbook/meetings/<dir>/meeting.json, agenda.md, minutes.md
        sources/boardbook/meetings_index.csv / .json
"""
import json, re, csv, html, sys
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
BB = ROOT / "sources" / "boardbook"
ORG = "https://meetings.boardbook.org"

def clean(t):
    return re.sub(r"\s+", " ", html.unescape(t or "")).strip()

def text_md(soup):
    main = soup.find("main") or soup
    for s in main(["script", "style", "noscript"]):
        s.decompose()
    lines = [clean(x) for x in main.get_text("\n").split("\n")]
    out, prev = [], None
    for l in lines:
        if l and l != prev:
            out.append(l)
        prev = l
    return "\n".join(out)

def parse_agenda(path):
    soup = BeautifulSoup(path.read_text(errors="ignore"), "html.parser")
    items = []
    for tr in soup.select("tr.agenda-item-information"):
        fc = tr.select_one(".form-check")
        title = clean(fc.get_text(" ")) if fc else ""
        depth = 0
        pad = tr.select_one("div[style*=padding-left]")
        if pad:
            m = re.search(r"padding-left:\s*([\d.]+)em", pad["style"])
            depth = int(float(m.group(1)) / 2) if m else 0
        atts = []
        for a in tr.select("a[data-documentid]"):
            atts.append({"document_id": a["data-documentid"], "name": clean(a.get_text()),
                         "viewer_url": f"{ORG}/Documents/FileViewerOrPublic/915?file={a['data-documentid']}",
                         "download_url": f"{ORG}/Documents/DownloadPDF/{a['data-documentid']}?org=915"})
        # item description / notes text (exclude attachments block)
        desc_el = tr.select_one(".agenda-item-description, .description, .item-description")
        desc = clean(desc_el.get_text(" ")) if desc_el else ""
        items.append({"agenda_item_id": tr.get("data-agendaitemid"), "title": title, "depth": depth,
                      "description": desc, "attachments": atts})
    return items, text_md(soup)

def generic_files(path):
    soup = BeautifulSoup(path.read_text(errors="ignore"), "html.parser")
    files = []
    for a in soup.select("a[href]"):
        m = re.search(r"file=(\d+)", a["href"]) or re.search(r"/Documents/\w+/(\d+)", a["href"])
        if m:
            files.append({"document_id": m.group(1), "name": clean(a.get_text()) or m.group(1),
                          "download_url": f"{ORG}/Documents/DownloadPDF/{m.group(1)}?org=915"})
    return files, text_md(soup)

def main():
    idx = json.loads((BB / "boardbook_index_2025_2026.json").read_text())
    by_id = {m["id"]: m for m in idx["meetings"]}
    rows = []
    for d in sorted((BB / "meetings").iterdir()):
        date, mid, slug = d.name.split("_", 2)
        m = by_id.get(mid, {})
        rec = {"meeting_id": mid, "date": date, "slug": slug, "heading": m.get("head"),
               "meeting_type": m.get("type"), "location": m.get("loc"),
               "cancelled": (m.get("head") or "").startswith("Cancelled"),
               "videos": [v if v.startswith("http") else "https:" + v for v in m.get("vids", [])],
               "agenda_url": f"{ORG}/Public/Agenda/915?meeting={mid}",
               "minutes_url": f"{ORG}/Public/Minutes/915?meeting={mid}" if (d / "minutes.html").exists() else None,
               "supplementals_url": f"{ORG}/Meeting/Supplementals/915?meeting={mid}" if (d / "supplementals.html").exists() else None,
               "folder": str(d.relative_to(ROOT))}
        items, agenda_md = parse_agenda(d / "agenda.html")
        rec["agenda_items"] = items
        (d / "agenda.md").write_text(f"# Agenda: {rec['heading']}\n\nSource: {rec['agenda_url']}\n\n{agenda_md}\n")
        for name in ["minutes", "supplementals", "public_notice"]:
            p = d / f"{name}.html"
            if p.exists():
                files, md = generic_files(p)
                rec[f"{name}_files"] = files
                dm = re.search(r'id="NewDocumentViewerDocumentID" value="(\d+)"', p.read_text(errors="ignore"))
                if dm:  # minutes / notices are PDFs shown in BoardBook's viewer
                    rec[f"{name}_document_id"] = dm.group(1)
                    rec[f"{name}_pdf"] = str((d / f"{name}_{dm.group(1)}.pdf").relative_to(ROOT))
                    rec[f"{name}_download_url"] = f"{ORG}/Documents/DownloadPDF/{dm.group(1)}?org=915"
                (d / f"{name}.md").write_text(f"# {name.replace('_',' ').title()}: {rec['heading']}\n\nSource: {rec.get(name+'_url') or ''}\n\n{md}\n")
        (d / "meeting.json").write_text(json.dumps(rec, indent=1))
        n_att = sum(len(i["attachments"]) for i in items)
        rows.append({k: rec[k] for k in ["date", "meeting_id", "heading", "meeting_type", "location", "cancelled", "agenda_url", "minutes_url", "folder"]}
                    | {"videos": " ".join(rec["videos"]), "n_agenda_items": len(items), "n_attachments": n_att,
                       "n_supplemental_files": len(rec.get("supplementals_files", []))})
    with open(BB / "meetings_index.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print(len(rows), "meetings;", sum(r["n_attachments"] for r in rows), "agenda attachments;",
          sum(r["n_supplemental_files"] for r in rows), "supplemental files")

if __name__ == "__main__":
    main()
