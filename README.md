# PPS Research Archive

A source archive and analysis workspace for **Portland Public Schools (PPS)**, built around the
**2026 rightsizing and school-closure proposals** (Scenario A/B released Oct 6, 2026; board vote scheduled Dec 15, 2026).
It also covers the 2025 bond and seismic retrofits, enrollment, budget, and board deliberations since January 1, 2025.

**Start here:** [`analysis/BRIEFING.md`](analysis/BRIEFING.md), then [`analysis/README.md`](analysis/README.md)
(index of every analysis file, plus "how to answer common questions").

Everything in `sources/` is a copy of something published by PPS or another public body, with its original URL and fetch time
recorded in a manifest. Everything in `analysis/` is derived from `sources/` and cites back to it.

## What's here (as of 2026-10-11)

| Collection | Contents |
|---|---|
| BoardBook (`sources/boardbook/`) | 154 meetings since 2025-01-01: agendas, 1,372 agenda/supplemental attachments, 120 minutes PDFs, 153 public notices; text extracted, plus OCR for 108 scanned PDFs |
| Video transcripts (`sources/youtube/`) | 145 transcripts (~288 hours) with millisecond timestamps: every board and committee meeting video linked from BoardBook, plus Bond Accountability Committee (2023–26), Community Budget Review Committee (2026), rightsizing explainer videos and the Oct 2026 Fox 12 superintendent interview |
| pps.net (`sources/pps_net/`) | ~810 files: Data & Reporting datasets (enrollment, capture rates, class size, PSU forecasts, discipline, graduation), rightsizing pages, the **82 per-school "How could your school be impacted?" PDFs**, regional scenario summaries, budget volumes, Long-Range Facility Plan, Jefferson boundary-process documents, SE Guiding Coalition records (recovered via the Internet Archive) |
| Bond program (`sources/bond/`) | ~184 files from bond.pps.net: 2025 bond, BAC reports and presentations, performance audits, seismic program pages |
| News (`sources/news/`) | 233 article records (metadata, summaries, short quotes; no full text), plus PPS's own "In the News" list |

| Analysis (`analysis/`) | |
|---|---|
| `BRIEFING.md`, `timeline.md` | Closure-decision briefing; master timeline Jan 2023 to Dec 2026 (121 events) |
| `topics/` | Rightsizing, criteria and principles, bond and seismic, budget and enrollment, each with an open-questions file |
| `schools/` + `data/school_impact.csv` | One page per school (82): what Scenario A and B do to it, projections, receiving/sending schools, seismic status, quotes |
| `people/` | 27 profiles of board members and senior staff: positions over time, voting records, key quotes; a stance matrix; `quotes_all.jsonl` (1,443 timestamped, attributed quotes with confidence levels); `positions_timeline.csv` |
| `meetings/` | 106 per-meeting summaries with decisions, votes and a timestamped topic index |
| `data/` | Scenario, school-metric, enrollment, budget, bond-project and seismic tables, each row cited |
| `_verification_report.md` | Independent fact-check: 1,443 of 1,443 quotes verbatim, 156 of 156 votes correct, 25 corrections applied |

## Search

```bash
python3 tools/search.py "Rose City Park" --kind quote                 # what people said
python3 tools/search.py '"school closure" AND savings' --from 2026-01-01
python3 tools/search.py "threshold 360" --kind boardbook               # page-level hits in PDFs, with [BB:doc p.N]
python3 tools/search.py "consolidat*" --kind transcript -n 30          # 60-second transcript windows with YouTube links
python3 tools/search.py --rebuild                                      # after adding files
```
Kinds: `transcript`, `boardbook`, `pps_net`, `bond`, `quote`, `news`, `analysis`. Builds a local SQLite FTS index (`.cache/`, about 8 seconds).

## Citation conventions
- BoardBook: `[BB:<docId> p.<page>]` → `sources/boardbook/meetings/*/attachments/<docId>_*.pdf` (or `minutes_<docId>.pdf`)
- Video: `[YT:<videoId>@H:MM:SS]` → `https://www.youtube.com/watch?v=<videoId>&t=<seconds>s`
- Meeting: `[MTG:<YYYY-MM-DD>/<meetingId>]`; pps.net / bond files: `[PPS:<path under sources/>]`; news: `[NEWS:<id>]`

## Caveats and known gaps
- **Transcripts are YouTube auto-captions:** no speaker labels, and names and numbers are often misheard. Speaker attribution
  in `analysis/` is inferred (chair recognition, roll calls, self-identification), and every quote carries `confidence`.
  Check important quotes against the video at the linked timestamp.
- **No transcript** for the Jan 30, 2026 board retreat (the video has no captions) or the Aug 5, 2025 ethics training (the video doesn't play).
  Executive sessions are closed and have no video.
- **Minutes** for Sept–Oct 2026 meetings weren't posted yet when this was collected. Many 2026 minutes are scanned
  images, so their text is in `.pdf.ocr.txt`. A text search that comes up empty isn't proof a record is missing.
- **Not archived:**
  - The Oregonian (blocked) and most KGW article text; those records are headline-only.
  - 10 dead Google Drive links (BAC Q4 2025 executive summaries).
  - Two large meeting recordings (as video files).
  - The text of board closure policy 6.10.030-P.
- **BoardBook format:** BoardBook serves attachments as PDF, so Office originals aren't available.
- **Split files:** files over GitHub's 100 MB limit are split. See the `*.SPLIT.md` next to each one for sha256 and how to rejoin.

## Collection method and refresh
Pages and files were fetched through a real browser (BoardBook, pps.net, bond.pps.net, Google Drive, the Internet Archive)
and packed into zip batches with per-file manifests: URL, final URL, HTTP status, bytes and fetch time. YouTube captions were
fetched as the full timed caption track (`fmt=json3`). Re-running collection needs the browser helpers in `tools/browser/`.
Processing scripts:
- `tools/parse_boardbook.py`: meeting structure
- `tools/build_attachment_index.py`: attachment index
- `tools/extract_pdf_text.py`: PDF text extraction
- `tools/ocr_pdfs.py`: OCR for scanned PDFs
- `tools/write_transcripts.py`: transcript files
- `tools/split_large.py`: splits files over the size limit
- `tools/search.py`: the search tool above
