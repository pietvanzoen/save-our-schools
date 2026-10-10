# Working conventions for this repository (for Claude agents)

Purpose: source archive + analysis of Portland Public Schools (PPS), focused on the **2026 rightsizing /
school-closure proposals**. Supporting topics: 2025 bond & seismic retrofits, enrollment, budget, facilities,
and how board members and senior staff think and change positions over time. Routine procedural business
(contract approvals, minutes adoption, ceremonial items) can be noted briefly or skipped.

## Rules
1. `sources/` is primary material. Never edit files there except to ADD new source files plus their
   provenance (URL + fetch date in a manifest or front matter). Do not paraphrase into sources/.
2. `analysis/` is derived. Every factual claim carries a citation:
   - BoardBook doc: `[BB:<docId> p.<page>]` (page = PDF page; text files separate pages with \f)
   - Video: `[YT:<videoId>@H:MM:SS]` (timestamp from the transcript line)
   - Meeting: `[MTG:<YYYY-MM-DD>/<meetingId>]`
   - pps.net / bond.pps.net files: `[PPS:<path under sources/>]` or full URL
   - News: `[NEWS:<id from sources/news/index.jsonl>]`
3. Quotes must be verbatim from the source text. Transcripts are auto-captions: fix nothing inside the
   quote except obvious caption artifacts, and mark any repair with [brackets]. Keep each quote short and
   relevant (1–3 sentences). Never invent or "smooth" a quote.
4. Speaker attribution for transcript quotes must state evidence and confidence:
   `confidence: high` (named by chair/self-identified immediately before, or unambiguous role),
   `medium` (strong contextual inference), `low` (guess; avoid using low-confidence quotes in syntheses).
5. Distinguish clearly between what PPS documents state, what people said, and your own inference
   (label inference as "Analysis:").
6. Do NOT run git commit/push. The controller commits. Write only to the paths your task assigns you.
7. Prefer structured outputs (CSV/JSONL) alongside readable Markdown so things can be searched and joined.
8. News articles are copyrighted: store metadata, a summary in your own words, and at most short quotes
   (< 25 words each) with attribution; never full article text.

## Key indexes
- `sources/boardbook/meetings_index.csv`: every meeting since 2025-01-01
- `sources/boardbook/attachments_index.csv`: every agenda/supplemental attachment with tags and local paths
- `sources/boardbook/meetings/<date>_<id>_<slug>/meeting.json`: agenda items + attachments per meeting
- `sources/youtube/transcripts/`: per-video transcripts (when present)
- PDF text: `<file>.pdf.txt` next to each PDF (pages separated by form feed \f)
