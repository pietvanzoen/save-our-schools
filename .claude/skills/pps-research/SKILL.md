---
name: pps-research
description: Answer questions about Portland Public Schools (PPS) 2026 rightsizing / school closures, the 2025 bond and seismic work, enrollment, budget, specific schools, and what board members and staff said, using only this repository's archived sources, and cite every claim back to them. Use whenever working in the timaelliott/save-our-schools repo or asked about PPS closures, schools, board members or meetings.
---

# PPS research archive: answering questions from the repo

This repository already holds the sources: BoardBook agendas, minutes and attachments since Jan 2025; 145 meeting
video transcripts; the pps.net data and rightsizing files; bond and seismic documents; and news metadata. It also
holds a derived analysis layer. **Answer from what is here. Do not browse the web or fetch anything.** If the archive
does not cover something, say so and name the gap. Do not fill it from memory.

Snapshot date: **2026-10-11**. Scenarios A and B were released Oct 5–6, 2026. The superintendent's recommendation and
fiscal impact statement are due Nov 17, and the board vote is Dec 15, 2026. Anything after Oct 11, 2026 is not in the archive.

## 1. Orient

Always read `CLAUDE.md` (repo rules: citations, verbatim quotes, attribution confidence; Claude Code loads it
automatically) and sections 3–5 below.

- **Narrow question** (one school, one person, one meeting): go straight to the matching recipe in section 3.
  For a school, `analysis/schools/<slug>.md` is the right first stop.
- **Broad question, or the first question of a long session:** also read
  - `analysis/BRIEFING.md`: the decision briefing (bottom line, Scenario A vs B, rationale, weak points, stances)
  - `analysis/README.md`: index of every analysis file, with a "how to answer common questions" table
- **When you need them:**
  - `references/data_dictionary.md`: file layouts, CSV/JSONL schemas
  - `references/people_and_captions.md`: roster, roles, caption name variants

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

**Read the context, then cite precisely:**
```bash
python3 tools/window.py zOUH2Jq7Owo 2:23:24          # transcript ±2 min, with links; ">" marks likely speaker changes
python3 tools/window.py zOUH2Jq7Owo 2:23:24 0.5 4    # 0.5 min before, 4 after
python3 tools/doc.py 14505788                        # locate a BoardBook doc id (attachment, minutes_<id>, public_notice_<id>)
python3 tools/doc.py 14505788 2                      # print page 2, the N in [BB:14505788 p.2]
python3 tools/doc.py 14505788 --grep "Rose City"     # matching lines with their page numbers
python3 tools/doc.py school_impact/maplewood 3       # any sources/ PDF by path fragment
```
Transcripts come in two copies with identical lines and timestamps:
- `analysis/transcripts_corrected/<date>_<videoId>.txt`: **read this one.** Obvious caption mis-hearings of names are
  fixed and shown in brackets ("Ricky" → "[Rieke]", "Director the pass" → "Director [DePass]"). Every change is
  logged in `corrections.csv` there. `search.py` and `window.py` use this copy.
- `sources/youtube/transcripts/<date>_<videoId>.txt`: the raw captions, the primary source (`window.py --raw`).

Both copies have one `[H:MM:SS] text` line per caption.
PDF text is `<file>.pdf.txt`, with pages separated by `\f`; `doc.py` prefers the `.ocr.txt` version for scanned PDFs.

**Without a shell (e.g. reading the repo on github.com):** go through the indexes instead.
- Per school: `analysis/schools/<slug>.md`
- Per person: `analysis/people/<slug>.md` and `analysis/board_closure_stance/<slug>.md`
- Per meeting: `analysis/meetings/<date>_<videoId>.md`
- Data: `analysis/data/*.csv`
- Raw sources: `sources/boardbook/meetings_index.csv` and `attachments_index.csv`

## 3. Answer recipes

| Question type | Where to go | Notes |
|---|---|---|
| What happens to school X? Why was it chosen? | `analysis/schools/<slug>.md` → `sources/pps_net/rightsizing/school_impact/<slug>.pdf.txt` (PPS's own "Why is PPS considering this?" text) → `analysis/data/school_impact.csv` | Then search transcripts for the school name **and its caption variants**. The Oct 6, 2026 meeting (`zOUH2Jq7Owo`) has the regional overview (Calvert) from about 2:10 and the school-by-school rationale (Smith) at about 2:23–2:48. |
| What did director/staffer X say about Y? | `--kind quote --person "X"` → `analysis/people/<slug>.md` → `tools/window.py <vid> <timestamp>` to read the context and confirm the speaker | Use only `high` and `medium` quotes. Label medium ones. |
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
  (e.g. "Ricky" → "[Rieke]"). Text copied from the corrected transcript already follows this rule. Keep quotes short
  (1–3 sentences). Never smooth or invent wording. Other caption errors (numbers, unusual words) remain in both copies.
- **Speaker attribution** in transcripts is inferred: captions have no speaker labels. Check who the chair recognized
  just before ("Director Splitt…"), or self-identification. State confidence when it isn't obvious. Don't build
  conclusions on low-confidence attributions.
- **Re-check a stored rating before relying on it.** The `confidence` and `attribution_evidence` in `quotes_all.jsonl`
  are a previous agent's judgment. Before a quote carries weight in your answer, open the window and confirm who is
  speaking. A "thank you, Director X" can end the previous speaker's turn rather than start X's.
- **Members of the public** are described ("a Maplewood parent in public comment"), not named. Board members, staff and
  other public officials speaking in their official capacity (e.g. a state legislator in public comment) are named.
- **Separate three things:** what PPS documents state; what people said; and your own inference, labeled "Analysis:".
- **Be explicit about gaps** (section 6) rather than guessing.
- End with a short **Sources** list of the files you actually read.

## 5. Traps that cause wrong answers

- **Caption name variants.** The corrected transcripts fix the common ones (about 2,800 fixes). Rarer
  variants remain, as do variants in other files (quote batches, notes), so search both spellings. Common ones:
  - Ricky = Rieke; Stevenson = Stephenson; Cresten = Creston; Woodmir = Woodmere; Cwood/Swood = Sellwood
  - Mary'sville = Marysville; Englesman/Engleman = Engelsman; "the pass" = DePass; laforte/la Fort = La Forte
  - "arm strong" = Armstrong; IDW/IdB Wells = Ida B. Wells
  - More in `references/people_and_captions.md`.
- **Numbers in captions are unreliable** (e.g. "1,000" captioned for 1,100). Prefer the BoardBook document for any figure.
- **Board roles changed.** Chase-Miller has been Vice-Chair since Jul 7, 2026 [BB:14305225 p.1]. DePass was Vice-Chair
  before that, and the live pps.net page lagged. The 2025 board turned over in July 2025.
- **Scenario details:** Scenario A closes 14 schools and Scenario B closes 11 (Stephenson, Rose City Park and Lewis stay open in B).
  Use `analysis/data/school_impact.csv` (from the per-school family guides). It supersedes earlier memo-based figures;
  see `analysis/schools/_discrepancies.md`.
- **Forecasts vs. counts.** PSU/PRC forecast tables include the current year as a projection (e.g. Odyssey 2025-26:
  218 forecast vs. 217 actual Oct 1 count). For actual enrollment use the Oct 1 count ([BB:3997157] or the Data &
  Reporting enrollment summaries), and label projections as projections.
- **Space-aligned PDF text** (lottery and enrollment tables) can shift columns. If a number matters, render the page
  (`pdftoppm -f N -l N -png file.pdf out`) and read it, or say the alignment is uncertain. In a lightweight clone the
  PDFs aren't checked out: run `git sparse-checkout add '<path>.pdf'` first. If you can't, say the value is unverified.
- **Scanned PDFs**: use `<file>.pdf.ocr.txt` when it exists (OCR errors are possible). An empty grep is not proof of absence.

## 6. Known gaps (say so; don't guess)

- No transcript for the Jan 30, 2026 board retreat (no captions) or the Aug 5, 2025 ethics training. Executive sessions have no video.
- Sept–Oct 2026 minutes weren't posted at snapshot time.
- No PPS savings or fiscal estimate per closure has been published (due Nov 17).
- No per-scenario equity impact analysis has been published.
- Most KGW text (Oregonian articles are summarized in `sources/news/index.jsonl`, not stored in full), and 10 dead Google Drive links (BAC Q4 2025) are missing.
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
