# PPS Research Archive

A source archive and analysis workspace for **Portland Public Schools (PPS)**, built around the
**2026 rightsizing / school-closure proposals**, with supporting context on the 2025 bond, seismic
retrofits, enrollment, budget, and the board's deliberations since **January 1, 2025**.

Every file in `sources/` is a copy of something published by PPS or another public body, with its
original URL recorded. Everything in `analysis/` is derived from `sources/` and cites back to it.

## Layout

```
sources/                      # primary material, as published (do not edit)
  boardbook/
    meetings_index.csv        # one row per meeting since 2025-01-01 (date, type, video, links, counts)
    meetings/<date>_<meetingId>_<slug>/
      meeting.json            # structured: agenda items, attachments (with BoardBook document ids + URLs), videos
      agenda.html|.md         # agenda as published / as text
      minutes.html|.md        # minutes (when posted)
      public_notice.*, supplementals.*
      attachments/<docId>_<name>.pdf (+ .pdf.txt extracted text)
      supplemental/<docId>_<name>.pdf
    _manifests/               # per-download-batch manifests: url, HTTP status, bytes, fetch time
  youtube/                    # board meeting video transcripts (YouTube auto-captions) + video metadata
  pps_net/                    # pps.net pages, datasets, reports (data & reporting, rightsizing, budget)
  bond/                       # bond.pps.net program material (2025 bond, seismic)
  news/                       # news coverage index: outlet, date, URL, summary, short quotes (not full text)
analysis/
  people/                     # one file per board member / staff member: roles, quotes w/ timestamps, positions over time
  topics/                     # rightsizing, bond & seismic, enrollment, budget ... syntheses with citations
  meetings/                   # per-meeting summaries (what was discussed, decided, who said what)
  data/                       # derived tables (enrollment by school, capacity, scenarios ...) with provenance
  timeline.md                 # dated timeline of decisions and events
tools/                        # scripts that build indexes / extract text / search
```

## Citation conventions

- BoardBook documents: `[BB:<docId>]` → `sources/boardbook/meetings/*/attachments/<docId>_*.pdf`
- Video moments: `[YT:<videoId>@H:MM:SS]` → `https://www.youtube.com/watch?v=<videoId>&t=<seconds>s`
- Meetings: `[MTG:<YYYY-MM-DD>/<meetingId>]`
- pps.net files: `[PPS:<relative path under sources/pps_net>]`

## Caveats

- Transcripts are YouTube **auto-generated captions**: no speaker labels, and names and numbers are often
  misheard. Speaker attribution in `analysis/` is inferred from context (chair recognition, roll call,
  self-identification) and every quote carries a confidence level. Verify important quotes against the video.
- BoardBook serves every attachment as PDF (Office originals are converted by BoardBook).
- Some PDFs are scanned images with no text layer; see `sources/_needs_ocr.txt`.
