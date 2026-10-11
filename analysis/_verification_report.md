# Verification report: independent fact-check of the PPS analysis

Verifier: an independent agent that did not write any of the analysis. Date: 2026-10-11.
Scratch work (scripts, OCR output, rendered slides) is outside the repo. Nothing under `sources/` was modified.

## 1. Method

| Area | What was checked | How |
|---|---|---|
| 1. Rightsizing scenarios | `analysis/topics/rightsizing.md`, `analysis/data/rightsizing_scenarios.csv` | Every school listed as closing, consolidating, converting (K-8 to K-5, MLC to K-8), receiving a program or changing boundary, under A and B, was compared with the scenario memo [BB:14509719], districtwide summary [BB:14505788], Oct 6 deck [BB:14511742] and the four regional summaries [BB:14505790]–[BB:14505793]. The CSV's boundary-change sets were compared programmatically with the printed lists (38 for A, 34 for B). Its 2025-26 enrollment, capacity, utilization and Title I values were checked against the April 20 table [BB:3997157] for all 82 schools. The deck's feeder slides (pp. 32 and 39) were rendered and read visually. All 137 quoted passages in rightsizing.md were matched against the cited page text, allowing for column-interleaved text layers. About 40 further figures (KPIs, ranges, DLI seats, Jefferson projections, per-pupil costs) were checked on their cited pages. Per-school impact PDFs are **not** in the archive: `sources/pps_net/rightsizing/school_impact/` holds only `_index.json` (Drive links). |
| 2. Board members | `analysis/people/README.md` stance matrix and the 7 current-member profiles | (a) Every one of the 1,443 quotes in `quotes_all.jsonl` was checked verbatim against the transcript TSV within ±180 s of its timestamp. (b) All 446 quote+YT-citation pairs in README and the 7 profiles were checked verbatim, and each was traced to the jsonl record for the same person, with matching confidence and *(medium)* flags. (c) Attribution was reviewed by hand for 72 quotes, at least 8 per member (Wang 12, DePass 8, Chase-Miller 12, Sullivan 9, Splitt 12, La Forte 10, Engelsman 9). Each review read the transcript about 2–7 minutes before the quote for chair recognition, self-identification and turn changes, and checked any stated evidence. (d) An automated scan of all 1,443 quotes looked for passages the speaker was quoting from someone else (quotation marks in the caption text); 8 were flagged and read. (e) Voting tables: 156 member-vote entries (142 minutes-sourced, 14 video-sourced) were checked against roll calls in the minutes (`minutes_*.pdf.txt` / `.ocr.txt`) or video. |
| 3. Bond and budget | `bond_and_seismic.md`, `budget_and_enrollment.md` | 15 key-figure groups (46 values) in the bond file and 20 groups (35 values) in the budget file were checked on the cited [BB:] pages. Image-only tables were rendered (BAC memo p.6). Three CBRC quotes in a garbled text layer were checked with a fresh OCR of the PDF pages. All quoted passages in both files were located. The "33 of 45 K-5 below 360 / 23 below 300 / 9 of 15 MS below 500" analysis was recomputed. |
| 4. Random quotes | 40 records drawn at random (seed 2026) from `quotes_all.jsonl`, across 2025-01 to 2026-10 | Verbatim check, plus a manual attribution-plausibility review of the transcript context. |
| 5. News timeline | `analysis/timeline_from_news.md` | 15 entries were checked against `sources/news/index.jsonl` and, where possible, BoardBook minutes or video. |

## 2. Results by area

| Area | Sample | Pass | Rate | Notes |
|---|---|---|---|---|
| 1a. Closure / merge / conversion assignments (A and B) | 25 closures + 16 grade reconfigurations + 25 program moves + 72 boundary-list entries | all | 100% | Every school, receiving school, percentage split (70/30, 50/50) and program move matches the memo, regional summaries and deck. |
| 1b. CSV structured checks | 164 A/B rows; 82 enrollment/capacity/Title I/utilization rows | all | 100% | The boundary-change sets equal the printed 38 and 34 lists exactly. |
| 1c. Key numbers (thresholds 360/500/1,100; 67/57/26%; 80/73/48%; 27%/24% movers; counts 14/11, 38/34, 13/12, 8/8; 11/17 and 12/15; regional tables) | ~170 cells | all | 100% | The "65 as printed" Scenario B figure is correctly flagged as a source anomaly. |
| 1d. Quotes in rightsizing.md | 137 | 137 located | 100% | 7 were on the adjacent page (usually both pages are cited). |
| 1e. Narrative claims of absence ("not in the archive") | 4 checked | 1 | 25% | The 7307 tally and the 7342 outcome are in the archived minutes; the MLC reversal is reported by news. See §3. |
| 2a. Verbatim, all jsonl quotes | 1,443 | 1,443 | 100% | 1,442 were within ±5 s. One was 148 s off only because a "[clears throat]" tag is in the caption text itself. |
| 2b. Verbatim, profile/README quote-cites | 446 | 446 | 100% | 5 "nomatch" hits were resolution titles or a news quote paired with a nearby YT cite, not transcript quotes. |
| 2c. README matrix → jsonl person/confidence chain | all matrix cites | all | 100% | |
| 2d. Manual attribution, board members | 72 | 69 | 95.8% | 1 relayed quote presented as her own words (Engelsman); 2 confidence over-ratings (Splitt). A third Splitt record in the same turn was also downgraded. |
| 2e. Voting tables vs minutes/video | 156 member-votes | 156 | 100% | One systematic page-citation error: Res. 7229 is cited to p.3, but the roll call is on p.4. |
| 3a. Bond figures | 15 groups / 46 values | all | 100% | Missing context on one figure (Procedeo savings typo); one imprecise citation. |
| 3b. Budget/enrollment figures | 20 groups / 35 values | all | 100% | The narrative wrongly says the May 26 / June 23 minutes are absent. |
| 4. Random 40 quotes | 40 | verbatim 40; attribution 39 | 100% / 97.5% | One high→medium downgrade (Splitt, Apr 28). |
| 5. News timeline entries | 15 | 13 consistent; 1 news-only and contradicted in effect by later primary docs; 1 unverifiable | 87% | See §3. |

**Overall:** quote fidelity is excellent (100% verbatim on 1,443 + 446 checks). Votes are accurate. The scenario detail is accurate down to the school level. The main defects are (a) several "not in the archive" statements that predate the minutes being added, or rest on empty text layers, and (b) a small number of attribution and framing problems.

## 3. Discrepancies found

| # | File | Claim | What the source actually says | Citation | Severity | Status |
|---|---|---|---|---|---|---|
| 1 | people/stephanie-engelsman.md (also quotes_all.jsonl, positions_timeline.csv, meetings/2026-04-27_2bSmBVuoajw.md) | "the goal is to end up with great schools, not less of what we have now" is presented as Engelsman's own statement and a heading of her Apr–May stance | She is quoting a parent from the Benson listening session: "the other comment that really resonated was, 'Why that first comment was important is the goal is to end up with great schools, not less…'". She endorses it, but the words are not hers. | [YT:2bSmBVuoajw@0:15:54] [YT:2bSmBVuoajw@0:16:00] | major | fixed (reframed; jsonl high→medium) |
| 2 | topics/budget_and_enrollment.md §3.3 | "Minutes for these meetings [May 26, June 23] are not in the archive, so the votes are unknown"; amendment outcomes "not in the archive" | The minutes are archived (readable in the OCR files). Res 7308 7-0; Res 7326 6-0-1 (Engelsman abstain); 7339 travel 7-0; 7340 OIPA failed 3-4; 7341 AI pause 7-0; 7342 Engelsman staffing failed 1-6 | [BB:3998080 p.4] [BB:3998082 p.4] [BB:3998082 p.5] | major | fixed |
| 3 | topics/budget_enrollment_open_questions.md #6 | Same as #2 | Same as #2 | same | major | fixed |
| 4 | topics/rightsizing.md §7 | Engelsman $13.12M amendment: "Its outcome is not in the archive" | Res 7342 failed 1-6; only Engelsman voted yes | [BB:3998082 p.5] | major | fixed |
| 5 | topics/rightsizing.md §3.1 table and §3.3 | Res 7307 "on agenda for vote; adoption stated by later PPS memo"; "The vote tally is not in the archive" | Passed 7-0 | [BB:3998080 p.3] | major | fixed |
| 6 | topics/rightsizing_open_questions.md §30 | Minutes for Apr 28, May 12, May 26, Jul 7, Aug 4 "are not attached as text in the archive" | Minutes 3998078, 3998079, 3998080, 3998081 (Jun 9), 3998082 (Jun 23), 14305225, 14440686 are all present. Only Sept 1 and Sept 15 are missing. | `sources/boardbook/meetings/*/minutes_*.txt` | major | fixed |
| 7 | topics/rightsizing_criteria_and_principles.md §0 table | "Res. 7307 (adopted per later memo)" | adopted 7-0 | [BB:3998080 p.3] | minor | fixed |
| 8 | quotes_all.jsonl / christy-splitt.md (2026-05-12 4:51:42 and 4:52:28) | Attributed to Splitt at **high** ("not re-named") | The speaker is unnamed. At 4:51:24 the chair said "let's start from director Chase Miller". The content (her own earlier "compact boundaries" and "fragmentation" asks, made at 4:17–4:20 after she was recognized) points to Splitt, so this is an inference. | [YT:OLAZDzvg3RM@4:51:24] [YT:OLAZDzvg3RM@4:17:48] | major (calibration) | downgraded to medium |
| 9 | quotes_all.jsonl / christy-splitt.md (2026-04-28 4:59:36) | high | The speaker is unnamed in the window. Attribution rests on biographical cues ("radical cander has gotten me nowhere in Oregon politics"). | [YT:j9PzUvPpSVA@4:58:15] | minor (calibration) | downgraded to medium |
| 10 | topics/bond_and_seismic.md §4.2 | Procedeo "Total Realized Savings" $20,839,680 | Packet slide says $20,839,680. On the record, Franco said the slide had a typo: "The number is actually 19,839,680" | [BB:14383796 p.34] [YT:uAf7l-ChjFo@1:49:53] | minor | note added |
| 11 | topics/bond_and_seismic.md §4.1; bond_seismic_open_questions.md #2 | Res 7331 BAC charter vote "not in archive minutes" | passed 7-0 | [BB:3998082 p.3] | minor | fixed |
| 12 | topics/rightsizing.md §5 | MLC 9-12 closure "(announced Feb 2026) now folded into both scenarios" | News reports PPS reversed the February plan around Feb 27, 2026. No BoardBook or transcript record of the reversal was found. The Oct docs re-propose the closure, so this is a reversal followed by a re-proposal, not a continuous plan. | [NEWS:NEWS-20260227-wweek-1] [BB:14505788 p.2] | minor | note added |
| 13 | people/*.md voting tables (8 files), README, 2 text lines | Res 7229 (6-1, Engelsman no) cited [BB:3998053 p.3] | The 7229 roll call is on p.4. p.3 has 7228 and the start of the 7229 item. | [BB:3998053 p.4] | minor | fixed |
| 14 | topics/bond_and_seismic.md §1 | Jefferson revised plan "$466,007,500" cited to [BB:3993106 p.3] | That page says "$466m total project cost". The exact figure appears in later bond updates. | [BB:3996975 p.20] | minor | not changed (value correct) |
| 15 | quotes_all.jsonl attribution_evidence (several) | Evidence timestamps for recognitions | Occasionally off by 20–35 s, e.g. "Director Split is always hard to follow" is listed at 3:51:05 but occurs at 3:51:35; "Director Chase Miller's amendment" is listed at 4:38:46 but occurs at 4:39:04. The attributions themselves hold. | [YT:zOUH2Jq7Owo@3:51:35] [YT:yinJ7KK-Bqc@4:39:04] | minor | not changed |
| 16 | timeline_from_news.md 2025-01-13/14 | Splitt appointed 4–2 in the final round | News and video agree (DePass, Sullivan, Brim-Edwards, Wang for Splitt). The minutes are internally garbled: their "Round 3" roll call still lists votes for the eliminated candidate Wirz. | [YT:xNoisoONrkA@2:14:41] [BB:3997971 p.3] | info (source defect) | none needed |
| 17 | timeline_from_news.md 2026-10-07 | KATU: bond work at Rose City Park ~$40M, Beach ~$10M, etc. | Not verifiable from primary docs. The Holmes ROM construction-only estimates (2023 $) are different measures, e.g. Rose City Park complete retrofit $21.1M. | [BB:3991109 p.12] | info | none needed |
| 18 | topics/rightsizing.md §3.2 | April 14 La Forte amendment: minutes say "passed 4-3" but the roll call shows 3-4 | Confirmed in both the draft and adopted minutes. The analysis already flags this correctly. | [BB:3997322 p.4] [BB:3998077 p.4] | info (source defect) | none needed |
| 19 | topics/budget_and_enrollment.md header; bond_and_seismic.md header | "no video transcripts, pps.net or news were in the archive for this pass" | Stale: the archive now has 320 transcript files, news and pps.net pages. Some "unknown" items may now be answerable from them. | — | minor | not changed |
| 20 | (archive) | — | Text-layer defects: the July 7 minutes p.1 leadership vote is in the PDF but missing from `.pdf.txt`; the CBRC report [BB:3997238] text layer is garbled (3 quotes were verified via fresh OCR); May 26 and June 23 minutes are readable only in `.ocr.txt`. Absence claims based on text search are unreliable for these documents. | — | info | none needed |

## 4. Corrections applied

All edits are in `analysis/` only. "Old → New" is abbreviated where long; the full strings are in the files.

| # | File | Old → New | Citation |
|---|---|---|---|
| C1 | people/christy-splitt.md, eddie-wang.md, ian-ritorto.md, michelle-depass.md, patte-sullivan.md, rashelle-chase-miller.md, stephanie-engelsman.md, virginia-la-forte.md (voting tables, Res. 7229 row) | `[BB:3998053 p.3] [YT:BJMsF-90V6U@2:12:05]` → `[BB:3998053 p.4] [YT:BJMsF-90V6U@2:12:05]` | [BB:3998053 p.4] |
| C2 | people/README.md | "lone 7229 no [BB:3998053 p.3]" → "… [BB:3998053 p.4]" | [BB:3998053 p.4] |
| C3 | people/stephanie-engelsman.md §Enrollment | "Only board member to vote no on Res. 7229 … [BB:3998053 p.3]" → "… p.4" | [BB:3998053 p.4] |
| C4 | people/michelle-depass.md | "(7228, 7229) [BB:3998053 p.3]" → "[BB:3998053 p.3–4]" | [BB:3998053 p.3–4] |
| C5 | people/stephanie-engelsman.md (Apr–May narrative) | Bare quote "the goal is to end up with great schools…" → "On April 27 she relayed, approvingly, a parent's comment from the Benson listening session: '…' (the words are the parent's, quoted by Engelsman) … *(medium)*" | [YT:2bSmBVuoajw@0:16:00] |
| C6 | people/stephanie-engelsman.md (key quotes list) | "— 'the goal is…'" → "— (relaying a parent's comment) 'the goal is…' *(medium)*"; context line "supports rightsizing only if it yields better-resourced schools" → "relays a parent's comment that rightsizing should yield better-resourced schools" | same |
| C7 | meetings/2026-04-27_2bSmBVuoajw.md | "Engelsman: 'great schools, not less…'" → "Engelsman: relayed a parent's comment from the Benson session, '…'" | same |
| C8 | people/quotes_all.jsonl (Engelsman 2026-04-27 0:16:00) | confidence high → **medium**; paraphrase rewritten to say she relays a parent's comment; verifier note appended to attribution_evidence | same |
| C9 | people/quotes_all.jsonl (Splitt 2026-05-12 4:51:42; 4:52:28) | confidence high → **medium**; verifier note appended (chair had just called on Chase-Miller; speaker not named) | [YT:OLAZDzvg3RM@4:51:24] |
| C10 | people/quotes_all.jsonl (Splitt 2026-04-28 4:59:36) | confidence high → **medium**; verifier note appended | [YT:j9PzUvPpSVA@4:58:15] |
| C11 | people/positions_timeline.csv (4 rows above) | confidence high → medium; Engelsman stance → "relays parent comment: rightsizing should yield better-resourced schools" | as above |
| C12 | people/christy-splitt.md | Header "(119 high, 34 medium, 4 low" → "(116 high, 37 medium, 4 low"; added *(medium)* flags at the 3 places citing 4:51:42, 4:52:28 and 4:59:36 | jsonl recount |
| C13 | people/stephanie-engelsman.md | Header "(92 high, 21 medium" → "(91 high, 22 medium" | jsonl recount |
| C14 | topics/rightsizing.md §3.1 table | "Res. 7307 … on agenda for vote; adoption stated by later PPS memo" → "Res. 7307 … adopted 7-0", adding [BB:3998080 p.3] | [BB:3998080 p.3] |
| C15 | topics/rightsizing.md §3.3 | "The vote tally is not in the archive." → "The May 26 minutes record that 7307 passed 7-0 [BB:3998080 p.3] (text layer is in the OCR file)." | [BB:3998080 p.3] |
| C16 | topics/rightsizing.md §7 | "Its outcome is not in the archive." → "The minutes record that it (Res. 7342) failed 1-6, with only Engelsman voting yes [BB:3998082 p.5]." | [BB:3998082 p.5] |
| C17 | topics/rightsizing.md §5 table (Oct 5 MLC row) | Added: "News reported that PPS reversed the February closure plan around Feb 27, 2026 [NEWS:NEWS-20260227-wweek-1]; no BoardBook record of that reversal is in the archive" | [NEWS:NEWS-20260227-wweek-1] |
| C18 | topics/rightsizing_criteria_and_principles.md | "Res. 7307 (adopted per later memo)" → "Res. 7307 (adopted 7-0 [BB:3998080 p.3])" | [BB:3998080 p.3] |
| C19 | topics/rightsizing_open_questions.md §30 | Minutes-missing bullet rewritten: Apr 28–Aug 4 minutes are present (OCR for some); 7307 passed 7-0; only Sept 1 and Sept 15 minutes are missing | file listing; [BB:3998080 p.3] |
| C20 | topics/budget_and_enrollment.md §3.3 | "Minutes for these meetings are not in the archive, so the votes are unknown" → Res 7308 7-0 [BB:3998080 p.4] (minutes label it "7307"); Res 7326 6-0-1, Engelsman abstaining [BB:3998082 p.4] | [BB:3998080 p.4] [BB:3998082 p.4] |
| C21 | topics/budget_and_enrollment.md §3.3 | "Their outcomes are not in the archive." → travel 7339 7-0; OIPA 7340 failed 3-4; AI pause 7341 7-0; Engelsman 7342 failed 1-6 | [BB:3998082 p.4–5] |
| C22 | topics/budget_enrollment_open_questions.md #6 | "…not in the archive. Vote tallies … are unknown" → tallies listed; question marked closed | [BB:3998080 p.4] [BB:3998082 p.4–5] |
| C23 | topics/bond_and_seismic.md §4.1 | "(vote not in archive minutes)" → "passed 7-0 [BB:3998082 p.3]" | [BB:3998082 p.3] |
| C24 | topics/bond_seismic_open_questions.md #2 | Removed Res 7331 from the "No vote tallies found" list | [BB:3998082 p.3] |
| C25 | topics/bond_and_seismic.md §4.2 | Appended: "At the Sept 15 meeting Franco said the packet slide had a typo and 'The number is actually 19,839,680' [YT:uAf7l-ChjFo@1:49:53]." | [YT:uAf7l-ChjFo@1:49:53] |

Total: 25 corrections, made as 43 individual text replacements. Of these, 4 are quote-confidence downgrades in `quotes_all.jsonl`, mirrored in `positions_timeline.csv`. No quotes were deleted. The input batch files under `analysis/people/quotes/` were not edited, so they still carry the old confidence values for those 4 records.

## 5. Items checked and found correct (selected)

- School lists. Closing in both scenarios: Beach, Buckman, Creston, Irvington, James John, Maplewood, Marysville, Peninsula, Sabin, Sellwood MS, Woodmere. Closing only under A: Lewis, Rose City Park, Stephenson. The seven K-8→K-5 conversions and MLC→K-8 also match [BB:14505788 p.2] [BB:14509719 p.2–4].
- Receiving schools and splits: Maplewood 70/30 to Hayhurst/Rieke; Stephenson 70/30 to Markham/Capitol Hill; Buckman 50/50 to Abernethy/Sunnyside; Sellwood split to Hosford/Brentwood by Llewellyn vs Duniway areas. The deck feeder slides (Skyline "no longer feeds" Lincoln; Atkinson "no longer feeds" Harrison Park; Mt. Tabor split Grant/greyed Cleveland) were confirmed visually [BB:14511742 p.32] [BB:14511742 p.39].
- The closing schools' 2025-26 enrollment sums (4,258 A / 3,301 B) and capacity removed (7,623 / 6,096) recompute exactly. Six Title I schools close in both scenarios, matching KATU's 1,709 students (892 + 817).
- April 14 Res. 7296 sub-votes, final 5-2, and the 4-3/3-4 contradiction were confirmed in both the draft [BB:3997322] and adopted [BB:3998077] minutes. Res. 7307 7-0 [BB:3998080 p.3]. 7228 7-0 and 7229 6-1 [BB:3998053]. Bond-auditor Rec. 34 4-3 (Splitt, Sullivan, Engelsman, La Forte yes) [YT:SPwXuNlwP_U@2:43:54]. Superintendent contract 5-2 voice vote [YT:5RMfvT-sAPU@3:32:31]; the no votes are inferred and consistent with [NEWS:NEWS-20260902-wweek-1].
- Attributions explicitly confirmed by later staff summaries: DePass "9.5" / "go big", Splitt "scalpel", La Forte "similar to … go big", Chase-Miller "in between … Yes" [YT:5RMfvT-sAPU@2:48:47–2:51:24]. Oct 6 speaker order (Engelsman named, Sullivan named, Wang, then Chase-Miller, Splitt and La Forte by order and content) is plausible as rated.
- Thresholds: 360 / 500 (K-8 and MS) / 1,100, from the QEM prototype and the Jefferson process [BB:3997426 p.2] [BB:14511742 p.10].

## 6. The five most serious issues

1. **Relayed quote presented as a member's own words** (Engelsman, Apr 27). Her "great schools, not less of what we have now" was a parent's comment she quoted. It anchored a section heading of her profile. Fixed and downgraded.
2. **False "minutes not in archive / votes unknown" statements on the 2026-27 budget** (budget_and_enrollment.md and its open questions). The May 26 and June 23 minutes are archived, with full roll calls (7308 7-0; 7326 6-0-1 with Engelsman abstaining; 7340 3-4; 7342 1-6; 7339 and 7341 7-0). Fixed.
3. **The same error in the rightsizing files**: "7307 tally unknown", "Engelsman amendment outcome unknown", and an open-question entry listing five archived minutes as missing. Fixed. Root cause: empty or garbled text layers. These minutes are readable only in `.ocr.txt`, and the July 7 leadership vote is visible only in the PDF image.
4. **Over-confident attribution of Splitt's May 12 "I might vote no" turn.** The chair had just called on Chase-Miller, and the speaker is identified only by content. Two records were downgraded to medium (plus one Apr 28 record), and the profile flags were updated. The likely attribution is still Splitt.
5. **Uncorrected bond figure and an omitted reversal.** Procedeo's "realized savings" was reported from a packet slide that staff corrected on the record ($20.84M → $19.84M). The MLC 9-12 closure is described as continuous, although news reports PPS reversed it on ~Feb 27 before re-proposing it in October. Notes added to both.

Also worth knowing: the Res. 7229 page citation was wrong in 8 profiles (fixed); the per-school impact PDFs are not archived; and two topic-file headers say transcripts and news were absent, which is no longer true.
