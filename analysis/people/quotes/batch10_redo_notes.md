# batch10_redo notes: English re-analysis of 10 meetings (captions re-fetched 2026-10-11)

Batch id: `batch10_redo`. Written 2026-10-10/11 from the English ASR caption tracks re-fetched 2026-10-11 into `sources/youtube/transcripts/`.

## Scope

| Date | Video | Meeting (BoardBook id) | Quotes |
|---|---|---|---|
| 2025-09-18 | gVtn7AYmhUU | TLE committee (709744) | 13 |
| 2026-03-05 | ppbt9KnsTbk | Audit committee (735121) | 8 |
| 2026-06-24 | bQb4RGUlfk0 | FIO committee (752646) | 6 |
| 2026-09-01 | kIF9qrrMy6E | Intergovernmental Affairs (763670) | 11 |
| 2026-09-08 | S-pk57P6f_o | TLE committee (765500) | 36 |
| 2026-09-15 | YfANSrxqAMI | Intergovernmental Affairs (766660) | 7 |
| 2026-09-22 | 3N-rsU_g5Yk | Policy committee (767981) | 6 |
| 2026-09-23 | zfvbTie4mpE | FIO committee (768451) | 12 |
| 2026-09-29 | U8Cg5voCxXc | Intergovernmental Affairs (769461) | 5 |
| 2026-10-06 | k0wbO5egtWA | Annual ethics training (770670) | 2 |
| **Total** | | | **106** (73 high, 30 medium, 3 low) |

All 10 `analysis/meetings/<date>_<videoId>.md` files were rewritten from scratch.

## Removal of superseded quotes from earlier batches (task 3)

I removed every line whose parsed `video_id` is one of the 10 ids. All other lines are byte-identical to the originals. I checked this with a diff against a grep-filtered copy of each original. No lines failed to parse.

| File | Lines before | Removed | Lines after | Removed by video |
|---|---|---|---|---|
| batch02.jsonl | 114 | **5** | 109 | gVtn7AYmhUU ×5 |
| batch05.jsonl | 120 | **0** | 120 | none matched (ppbt9KnsTbk had no quotes in this file) |
| batch08.jsonl | 117 | **0** | 117 | none matched (bQb4RGUlfk0 had no quotes in this file) |
| batch09.jsonl | 171 | **11** | 160 | S-pk57P6f_o ×6, kIF9qrrMy6E ×2, zfvbTie4mpE ×2, YfANSrxqAMI ×1 |
| **Total** | | **16** | | |

The earlier batch notes were updated on 2026-10-11 to point to the rewritten meeting files and to `batch10_redo.jsonl`.

## Verification
- Every quote was matched programmatically against the joined English transcript. Matching allowed only [bracketed] spans, and the `>>` speaker-change markers inside a quote were treated as caption artifacts and dropped. For example, the 9/8 Glasgow quote "we have stretched people [>>] incredibly thin" is quoted without the marker.
- Two quotes keep the literal caption tag "[clears throat]", which is in the source text.
- Every `timestamp` is the transcript line on which the quote starts. `seconds` and `url` were recomputed from it, and `date` and `meeting_id` come from the transcript meta.
- Every `[YT:]` timestamp in the 10 meeting files was checked against the transcript line timestamps. One 9-01 file cites the 9-08 video on purpose.

## Attribution notes and caption corrections
- **Name normalizations in captions:**
  - "Virginia Leaffort/LaFore/Lefort/LaPorte" → Virginia La Forte
  - "Michelle Chase Miller"/"Rochelle Chester Miller" → Rashelle Chase-Miller. On 9/23 the introduction "Michelle Chase Miller, uh, vice chair" is garbled. Chase-Miller's presence there is inferred (medium).
  - "Christie Split" → Christy Splitt
  - "Englesman" → Engelsman
  - "Chair Wong" → Eddie Wang
  - "Christina Howard" → Kristina Howard
  - "Emily Glasco/Glazka" → Emily Glasgow
  - "Philipe Hristitch/Pistach/Harage" → Philip (Filip) Hristic. The spelling is uncertain; the JSONL uses "Philip Hristic".
  - "Margaret Calbert/Calbertt" → Margaret Calvert
  - "Deborah Kapori/Capori/KOR" → Deborah Kafoury
  - "Candace Gross" → Candice Grose
  - "Sharon Tancredi/Tunkara" → Sharon Toncray
  - "Presidio/Prescidio" → Procedeo (the RISE program manager firm; the 6/24 minutes say "Procedeo")
  - "PAF" → PCEF
  - "Arita" → Arleta
  - "East Silvin" → East Sylvan
  - "Abernathy" → Abernethy
  - "Ackley/Oakley Green" → Ockley Green
  - "Fabian/Fabien" → Faubion
  - "Grace Ade Air" → Grice Adair
  - "OB/O web" → OEBB
  - "DRA" → DBRAC (Splitt's mishearing; staff say "districtwide boundary review")
- **Staff whose names are uncertain or not in the roster:**
  - Ben Gerwitz, government relations: spelled "Gerwitz/Gerowitz/Gurowitz/Gerwood" in captions.
  - Emily Courtneidge, senior legal counsel: "Courtneidge/Curtinage/Courtney".
  - Janise Hansen, internal auditor. The minutes spell it "Janise".
  - Judy Brennan, Director of Enrollment and Transfer.
  - Liz Large, Contracted Senior Legal Counsel (6/24 minutes). **Analysis:** the "Liz" who introduced the 10/6 ethics training is probably Large (medium). I did not quote her there.
  - The ethics presenter is outside counsel "Mike Porter". He and the OSBA presenters (Stacy Madison, Leslie Rivers) are not quoted in the JSONL.
  - On 9/8 the facilities work-stream lead is captioned "Hannah Whit". **Analysis:** probably Dana White (low).
- **Calvert's title differs by date:** "assistant superintendent for school planning and modernization" (9/18/2025) and "executive director of school planning and modernization" (9/8/2026). The JSONL role uses each meeting's title.
- **9/8 TLE staff turns** are rarely named. My attributions:
  - Calvert (medium): answers on regions, closure history, capacity, fiscal timing and facilities. She is the planning lead, and these answers reference SEGC, Humboldt/Marshall and the threshold sources.
  - Glasgow: quotes are high where she self-references ("Phipe and I...", "I was an elementary principal") and medium otherwise. The "$65 million deficit" line is medium.
  - Hristic (medium): the 54 art positions passage, which Glasgow later credits to "Philipe".
  - The 9/8 questions on facilities layering and the future bond are not clearly attributed (probably Chase-Miller). They are summarized, not quoted.
- **Member attributions made by inference:**
  - 9/18/2025: La Forte's marketing remarks and Chase-Miller's Jefferson-vision question are medium. Splitt's "vibes" remark is low.
  - 3/5/2026: Engelsman's transfer-data question is medium.
  - 9/23: the La Forte surplus-building question is low; "Austin social housing" is low.
  - 6/24: DePass's BAC-alignment comment is medium.

## People: positions and shifts visible in this batch
- **Christy Splitt** (Zone 1):
  - In 2025 she pressed for west-side and catchment-based enrollment outreach [YT:gVtn7AYmhUU@0:50:53].
  - On 9/8/2026 she said she is "supportive of right sizing in general" because split staffing drives educators out [YT:S-pk57P6f_o@0:36:37]. She stayed skeptical of the evidence base and the forecasts: "all models are wrong", whether any schools are already well-resourced, and grounding the 360 threshold in staffing math rather than the QEM [YT:S-pk57P6f_o@0:42:24] [YT:S-pk57P6f_o@0:49:43].
  - As IGA chair she leads on PERS as a PPS-specific crisis [YT:kIF9qrrMy6E@0:48:20] [YT:U8Cg5voCxXc@0:40:51].
  - **Analysis:** conditional support. She is pro-consolidation on staffing grounds and wants better metrics and messaging.
- **Virginia La Forte** (Zone 5; TLE chair 2026-27):
  - Consistently retention- and marketing-minded. In 2025 she called marketing an "easy spend" and urged recruiting before the private-school season [YT:gVtn7AYmhUU@0:50:05]. In 2026 she wants specific program promises (choir/band, counselors, nurses) before the end-of-year rightsizing vote, ahead of private-school recruiting, and a fiscal impact statement [YT:S-pk57P6f_o@0:56:01] [YT:S-pk57P6f_o@1:00:52].
  - She wants "every neighborhood ... left with a school" [YT:S-pk57P6f_o@1:10:55].
  - As 2025-26 FIO chair (6/24) she focused on Grant Bowl lighting and OSAA crowd control.
- **Rashelle Chase-Miller** (Zone 4):
  - Prefers situational, regional solutions over absolutes [YT:S-pk57P6f_o@0:19:36].
  - Keeps Jefferson and Roosevelt commitments in view [YT:S-pk57P6f_o@0:21:53] [YT:S-pk57P6f_o@1:15:31].
  - Relayed the community question "why not just boundaries" [YT:S-pk57P6f_o@0:24:07].
  - On 9/23 (probable) she raised the fate of buildings vacated by "downsizing" [YT:zfvbTie4mpE@0:06:46].
- **Michelle DePass** (Vice-Chair; FIO chair 2026-27):
  - On 9/8 she said rightsizing is "not necessarily for cost savings". She wants the cost analysis delivered with the scenarios, not as a driver [YT:S-pk57P6f_o@1:02:42].
  - She publicly said no list of schools to combine exists [YT:S-pk57P6f_o@1:02:28].
  - On FIO she framed "enrollment capacity and the future PPS footprint" and a refreshed long-range facilities plan as candidate focus areas [YT:zfvbTie4mpE@0:05:56].
- **Stephanie Engelsman** (Zone 6):
  - Asked for an inventory of surplus buildings, how long closed buildings sat, and the disposition process, explicitly "in this right sizing conversation" [YT:zfvbTie4mpE@0:33:27]. This continues her earlier concern (batch09, 8/4) about family loss after SEGC.
  - On IGA she presses on whether PERS stabilization is only temporary [YT:kIF9qrrMy6E@0:29:13].
- **Patte Sullivan** (Zone 3):
  - Budget-focused and skeptical: "Shouldn't we have been able to anticipate this" (PERS) [YT:kIF9qrrMy6E@0:25:54]; "It feels to me like we're at a downturn" [YT:YfANSrxqAMI@0:40:35].
  - Open to using the Education Stability Fund [YT:YfANSrxqAMI@0:36:24].
  - No rightsizing statements in this batch.
- **Eddie Wang** (Chair): in this batch he speaks only on policy design (policy versus administrative directive, a teacher work group). No rightsizing content.
- **Margaret Calvert** (planning lead):
  - Her framing is consistent from 9/2025 ("the third phase is school right-sizing", after Jefferson dual assignment) to 9/2026: "we simply don't have enough students for the number of sites", "no absolutes", and regional scenarios.
  - She says neither enrollment nor facility condition alone will determine outcomes.
  - Fine-grained fiscal impact only comes at the recommendation stage.
- **Michelle Morrison** (CFO): PERS cost cliff in 2027-28, from about 24¢ to 33.5¢ per dollar of eligible payroll [YT:kIF9qrrMy6E@0:27:57]. The PERS reserve was already spent [YT:kIF9qrrMy6E@0:26:23]. "Significant budget challenges" this year and next (3/2026).
- **Superintendent Armstrong** (9/18/2025): she called the Jefferson process "open-ended" [YT:gVtn7AYmhUU@1:23:15]. Calvert gave fall 2027 as the starting-point sunset.
