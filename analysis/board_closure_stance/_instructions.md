# Board member closure-stance analysis: instructions (one agent per member)

Read `/home/claude/pps/CLAUDE.md` first. Its citation and quoting rules apply strictly.

## Goal
For ONE board member, build a dated timeline of everything they have said or done that bears on **school
closures / consolidation / rightsizing** (Jan 2025 → Oct 2026). Call out contradictions and shifts, score
their lean on each dated point, identify the themes they fixate on, and identify the weak points in those
positions.

## Sources (search them all)
- `analysis/people/<slug>.md`: existing profile, a starting point only; verify against sources
- `analysis/people/quotes_all.jsonl`: filter `person`; use confidence high/medium only (mark medium in output)
- `analysis/people/_quotes_from_news.jsonl` and `sources/news/index.jsonl`: interviews, op-eds, campaign statements
- Transcripts: `sources/youtube/transcripts/*.txt`. Search for the member's name (caption variants are listed
  in `analysis/people/quotes/*_notes.md`) and read ±3 minutes around hits to find statements the quote files missed,
  especially in 2026 rightsizing meetings (3/10, 3/12, 3/31, 4/14, 4/22, 4/28, 5/12, 5/26, 6/23, 8/4, 9/1, 9/8, 9/15, 10/6)
- Votes: `sources/boardbook/meetings/*/minutes_*.pdf.txt` and `.pdf.ocr.txt`, and `analysis/meetings/*.md`.
  Key votes: Res 7296 (4/14/26) + La Forte amendment + "will→may" amendment; Res 7307 (5/26/26); MLC 9-12 decision (Feb 2026);
  seismic Res 7109/7110; Jefferson 7228/7229; budgets
- `python3 tools/search.py "<name>" --kind quote|transcript|news`

## Lean score (one per dated data point)
Question: "If the Dec 15, 2026 vote were held on that date, how likely is this member to vote to ADOPT a closure
package (Scenario A, B, or an amended version that still closes schools) vs. vote AGAINST / to DEFER / for no closures?"
- **+2** strongly for adopting closures at scale (explicitly supports closing/consolidating; urges speed/scale)
- **+1** leans for (supports in principle; conditions are ones staff can plausibly meet)
- **0** genuinely undecided / conditions that cut both ways / mixed signals
- **−1** leans against (conditions unlikely to be met; prefers smaller/slower; process objections)
- **−2** strongly against / wants deferral / "no closures"
Each point gets: `date, score, confidence (high/medium/low), type (quote|vote|news|action), citation, one-line rationale`.
Score what the statement implies **at that time**, not hindsight. Votes are strong evidence; procedural
objections aren't automatically opposition. Also give an overall **trajectory** and a **current (Oct 2026) score with range**.

## Outputs (write ONLY these two files for your member)
1. `analysis/board_closure_stance/<slug>.md`:
   - Header: name, zone, role(s), tenure; the bottom line (current score, range, one sentence)
   - **Timeline**: chronological table: date | what they said/did (short verbatim quote with `[YT:id@H:MM:SS]` link, or vote) | score | note.
     Include every substantive closure-related point (typically 15–40).
   - **Contradictions & shifts**: each with the earlier statement vs the later one (both quoted and cited), and whether it's a
     true reversal, a refinement, or a position conditioned on new information
   - **Fixations / recurring themes**: the 3–6 things they return to most, with how many times and representative quotes
   - **Weak points**: for each theme, the tension, inconsistency, or factual problem in the position, checked against
     PPS documents/data in this repo (cite `[BB:]`/`[PPS:]`), labeled "Analysis:"; be fair and specific, not snarky
   - **What would move them**: the evidence or conditions their own words suggest would change their vote
   - **Watch items before 12/15**: specific upcoming moments (e.g. Nov 17 fiscal statement) and what to listen for
2. `analysis/board_closure_stance/<slug>_scores.csv` with columns:
   `member,date,score,confidence,type,citation,quote_or_action,rationale`

Rules: verbatim quotes only (verify each against the transcript), at most 2 sentences per quote; label inferences "Analysis:";
no low-confidence attributions in the timeline (you may list them separately as "unconfirmed"). Do not run git.
Final reply: current score with range, trajectory in one line, top 3 fixations, top 3 weak points.
