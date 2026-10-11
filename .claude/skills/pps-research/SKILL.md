---
name: pps-research
description: Answer questions about Portland Public Schools (PPS) 2026 rightsizing / school closures, the 2025 bond and seismic work, enrollment, budget, specific schools, and what board members and staff said, using only this repository's archived sources, and cite every claim back to them. Use whenever working in the timaelliott/pps repo or asked about PPS closures, schools, board members or meetings.
---

# PPS research archive: answering questions from the repo

This repository already holds the sources: BoardBook agendas, minutes and attachments since Jan 2025; 145 meeting
video transcripts; the pps.net data and rightsizing files; bond and seismic documents; and news metadata. It also
holds a derived analysis layer. **Answer from what is here. Do not browse the web or fetch anything.** If the archive
does not cover something, say so and name the gap. Do not fill it from memory.

Snapshot date: **2026-10-11**. Scenarios A and B were released Oct 5–6, 2026. The superintendent's recommendation and
fiscal impact statement are due Nov 17, and the board vote is Dec 15, 2026. Anything after Oct 11, 2026 is not in the archive.

## 1. Orient (read these first, in order)

1. `CLAUDE.md`: repo rules (citations, verbatim quotes, attribution confidence). Claude Code loads it automatically.
2. `analysis/BRIEFING.md`: the decision briefing (bottom line, Scenario A vs B, rationale, weak points, board stances).
3. `analysis/README.md`: the index of every analysis file, with a "how to answer common questions" table.
4. `references/data_dictionary.md` (next to this file): every index, CSV and JSONL schema and what it is good for.
5. `references/people_and_captions.md`: board and staff roster, name variants in auto-captions, and known traps.

## 2. Find things

**With a shell (local clone):** use the full-text search. It builds `.cache/search.sqlite` itself on first run (~10 s, stdlib only).
```bash
python3 tools/search.py "Maplewood" -n 30                            # everything
python3 tools/search.py "Maplewood" --kind transcript                # 60-second caption windows, with [YT:] cite + link
python3 tools/search.py "threshold AND 360" --kind boardbook         # PDF pages, with [BB:doc p.N]
python3 tools/search.py "closure" --kind quote --person "La Forte"   # attributed quotes
python3 tools/search.py '"school deserts"' --from 2026-09-01 --json  # date filter, JSON output
```
Kinds: `transcript`, `boardbook`, `pps_net`, `bond`, `quote`, `news`, `analysis`. FTS5 syntax: `"phrase"`, `AND/OR/NOT`, `prefix*`, `NEAR(a b, 10)`.
The search returns stemmed matches, so also `grep -i` the raw files for exact strings and caption variants (section 5).

**Without a shell (e.g. reading the repo on github.com):** go through the indexes instead.
- Per school: `analysis/schools/<slug>.md`
- Per person: `analysis/people/<slug>.md` and `analysis/board_closure_stance/<slug>.md`
- Per meeting: `analysis/meetings/<date>_<videoId>.md`
- Data: `analysis/data/*.csv`
- Raw sources: `sources/boardbook/meetings_index.csv` and `attachments_index.csv`

## 3. Answer recipes

| Question type | Where to go | Notes |
|---|---|---|
| What happens to school X? Why was it chosen? | `analysis/schools/<slug>.md` → `sources/pps_net/rightsizing/school_impact/<slug>.pdf.txt` (PPS's own "Why is PPS considering this?" text) → `analysis/data/school_impact.csv` | Then search transcripts for the school name **and its caption variants**. The Oct 6, 2026 meeting (`zOUH2Jq7Owo`) has the staff school-by-school rationale at about 2:23–2:48. |
| What did director/staffer X say about Y? | `--kind quote --person "X"` → `analysis/people/<slug>.md` → open the transcript at the timestamp and read ±2 min | Use only `high` and `medium` quotes. Label medium ones. |
| Where does board member X stand on closures? | `analysis/board_closure_stance/<slug>.md` (timeline, contradictions, fixations, weak points) and `README.md` there; scores in `all_scores.csv` | Scores are analytical judgments. Say so. |
| What was decided at meeting M, and the vote? | `analysis/meetings/<date>_<vid>.md` → `sources/boardbook/meetings/<date>_<id>_*/minutes_*.pdf.txt` (or `.ocr.txt`) | Minutes are authoritative for votes. Sept–Oct 2026 minutes were not yet posted. |
| Numbers: enrollment, capacity, budget, seismic, bond | `analysis/data/*.csv` (every row has a source) → the cited PDF page | Cite the source document, not the CSV. Check `analysis/topics/*_open_questions.md` for known conflicting figures. |
| Timeline / "when did X happen" | `analysis/timeline.md` (sourced), `analysis/timeline_from_news.md` (news framing) | |
| Transfers, capture rates, where students come from | `sources/pps_net/data-and-reporting/<year>/` (`school_enrollment_by_neighborhood_of_residence`, `neighborhood_capture_rate_metrics`); lottery history in `sources/pps_net/enrollment/lottery/` | Text columns are space-aligned. Verify column positions against the PDF page image before quoting a number. |
| News coverage | `sources/news/index.jsonl` (summary, key facts, short quotes) | No full article text is stored. Cite `[NEWS:<id>]`. |

## 4. How to write the answer

- **Cite every factual claim** inline, in the repo formats:
  - `[BB:<docId> p.<page>]` for BoardBook PDFs (page = PDF page; in `.txt` files, pages are separated by `\f`)
  - `[YT:<videoId>@H:MM:SS]` for video; also give the link `https://www.youtube.com/watch?v=<id>&t=<seconds>s`
  - `[PPS:<path under sources/>]` for pps.net and bond files
  - `[NEWS:<id>]` for news
  - `[MTG:<date>/<meetingId>]` for a meeting
- **Cite primary sources, not the analysis layer.** `analysis/` files are maps to the sources. Follow their citation
  to the source text, confirm it, and cite the source. When you rely on a judgment made in `analysis/` (a stance score,
  an "Analysis:" paragraph), say it is the archive's analysis.
- **Quotes are verbatim** from the transcript or PDF text. Auto-captions may only be repaired in `[brackets]`
  (e.g. "Ricky" → "[Rieke]"). Keep quotes short (1–3 sentences). Never smooth or invent wording.
- **Speaker attribution** in transcripts is inferred: captions have no speaker labels. Check who the chair recognized
  just before ("Director Splitt…"), or self-identification. State confidence when it isn't obvious. Don't build
  conclusions on low-confidence attributions.
- **Members of the public** are described ("a Maplewood parent in public comment"), not named. Board members and staff are named.
- **Separate three things:** what PPS documents state; what people said; and your own inference, labeled "Analysis:".
- **Be explicit about gaps** (section 6) rather than guessing.
- End with a short **Sources** list of the files you actually read.

## 5. Traps that cause wrong answers

- **Caption name variants.** Search both spellings. Common ones:
  - Ricky = Rieke; Stevenson = Stephenson; Cresten = Creston; Woodmir = Woodmere; Cwood/Swood = Sellwood
  - Mary'sville = Marysville; Englesman/Engleman = Engelsman; "the pass" = DePass; laforte/la Fort = La Forte
  - "arm strong" = Armstrong; IDW/IdB Wells = Ida B. Wells
  - More in `references/people_and_captions.md`.
- **Numbers in captions are unreliable** (e.g. "1,000" captioned for 1,100). Prefer the BoardBook document for any figure.
- **Board roles changed.** Chase-Miller has been Vice-Chair since Jul 7, 2026 [BB:14305225 p.1]. DePass was Vice-Chair
  before that, and the live pps.net page lagged. The 2025 board turned over in July 2025.
- **Ten videos were first captured from Arabic auto-translated captions.** They were re-fetched in English and re-analyzed.
  Prefer `analysis/people/quotes/batch10_redo*` and the `analysis/meetings/` files over the batch notes with CAVEAT headers.
- **Scenario details:** Scenario A closes 14 schools and Scenario B closes 11 (Stephenson, Rose City Park and Lewis stay open in B).
  Use `analysis/data/school_impact.csv` (from the per-school family guides). It supersedes earlier memo-based figures;
  see `analysis/schools/_discrepancies.md`.
- **Space-aligned PDF text** (lottery and enrollment tables) can shift columns. If a number matters, render the page
  (`pdftoppm -f N -l N -png file.pdf out`) and read it, or say the alignment is uncertain.
- **Scanned PDFs**: use `<file>.pdf.ocr.txt` when it exists (OCR errors are possible). An empty grep is not proof of absence.

## 6. Known gaps (say so; don't guess)

- No transcript for the Jan 30, 2026 board retreat (no captions) or the Aug 5, 2025 ethics training. Executive sessions have no video.
- Sept–Oct 2026 minutes weren't posted at snapshot time.
- No PPS savings or fiscal estimate per closure has been published (due Nov 17).
- No per-scenario equity impact analysis has been published.
- Oregonian article text, most KGW text, and 10 dead Google Drive links (BAC Q4 2025) are missing.
- The text of policy 6.10.030-P is missing.
- Hardship-petition transfer counts per school are not published.
- October 2026 community listening sessions are not archived.

## 7. If asked to produce something

- Short answers go in the chat, with citations.
- A shareable page or brief: follow the style of `analysis/schools/maplewood_brief.html` and
  `analysis/board_closure_stance/board_stance.html`. Log anything published in `analysis/_published_pages.md`.
- New derived files go under `analysis/` with citations. Never edit `sources/` (only add new sources plus provenance).
- Refreshing or collecting sources is a different job with different tools: see `RUNBOOK.md`. It needs a browser that
  can reach PPS sites, so don't attempt it while answering questions.
