# Batch 12 notes: media appearances, Oct 6–17, 2026 (OPB Think Out Loud plus TV clips)

Scope: 2 OPB Think Out Loud broadcasts (summaries in `analysis/meetings/2026-10-13_kdPfX6KH05c.md` and
`analysis/meetings/2026-10-16_D3dVt33To7g.md`) and 6 short TV news clips.

`batch12.jsonl` holds 73 quotes:

| Person | Quotes | Breakdown |
|---|---|---|
| Eddie Wang | 31 | all OPB |
| Kimberlee Armstrong | 35 | 28 OPB, 5 KPTV, 2 KOIN |
| Christine Drazan | 4 | |
| Tina Kotek | 2 | both letter text read on air |
| Stephanie Engelsman | 1 | |

- All quotes are verbatim from the YouTube caption transcripts. `merge_quotes.py` dry run: "73 new verified, 0 duplicates skipped, 0 failed".
- Media quotes carry `meeting_id: ""` and a `source` field (OPB Think Out Loud / KGW / KATU / KOIN / KPTV).
- Members of the public are never named and are not in the JSONL.

## TV clips

### 2026-10-06 KPTV (FOX 12): "Interview with PPS Superintendent Dr. Kimberlee Armstrong on school closures" (IF_vv3wXgAE, 3:58)
- Armstrong explained rightsizing with a fair-budget analogy: the same budget goes further with three people than six [YT:IF_vv3wXgAE@0:00:38].
- Asked whether she has the board votes, she said only "I'm confident that they're ready to engage in conversation about sustainability" [YT:IF_vv3wXgAE@0:01:09].
- She has no layoff number yet, and pointed to the state school fund "set by the governor" [YT:IF_vv3wXgAE@0:01:44]. She defended her raise as set in her 2024 contract, below market, with her COLA capped at her request [YT:IF_vv3wXgAE@0:02:35].
- On whether input is "performative": "we actually expect it to lead to changes" [YT:IF_vv3wXgAE@0:03:40].
- Reporter's paraphrase (not a quote): "Armstrong says it's also very possible that the board will decide to pause the plan" [YT:IF_vv3wXgAE@0:03:46].
- Reporter's claims, not checked here: spending per student is up about 23% inflation-adjusted over 10 years, and central-office staffing was cut 14% [YT:IF_vv3wXgAE@0:02:02] [YT:IF_vv3wXgAE@0:02:11].

### 2026-10-12 KGW: "PPS parents urge Gov. Kotek, Sen. Drazan to intervene…" (u0XKcIye1HI, 2:09)
- A letter from 300+ parents asks state leaders to step in. An Irvington-area letter organizer and a parent of three (not named here) are featured [YT:u0XKcIye1HI@0:00:05].
- Sen. Christine Drazan: "The district needs to listen to those families, and they also need to slow their roll. This is not inevitable." [YT:u0XKcIye1HI@0:00:32]. Closures are "unlikely to help them balance the budget at a level that makes it worth all the chaos" [YT:u0XKcIye1HI@0:00:57].
- Gov. Kotek was not interviewed. The reporter says she pointed to the bipartisan district-accountability law she signed last year, and that both candidates are open to rethinking the enrollment-based funding formula [YT:u0XKcIye1HI@0:01:30]. The closing soundbite ("what Portland Public Schools needs right now is stability") is attributed to Drazan with confidence medium [YT:u0XKcIye1HI@0:01:44].
- The reporter states a board vote date of December 15: A closes 14, B 11, C "basically do nothing" [YT:u0XKcIye1HI@0:01:56].

### 2026-10-14 KGW: "Kotek weighs in on Portland school closures as backlash reaches governor's office" (16XtQjqVzr8, 2:33)
- Kotek's letter to Superintendent Armstrong and Board Chair Wang urges PPS to slow down. In the reporter's paraphrase, the district "must take the necessary time for families to understand and adequately weigh in before decisions are made" [YT:16XtQjqVzr8@0:01:09].
- Director Stephanie Engelsman told KGW the district is "not releasing more data until mid-November, leaving the board just 1 month to decide" (reporter paraphrase), and wants the board to put the plans on hold in December. Her quote: "We could pause, get data, come back with a situation that does not look like spaghetti on a map" [YT:16XtQjqVzr8@0:01:34] [YT:16XtQjqVzr8@0:01:51].
- The Drazan "slow their roll" soundbite is reused from the Oct 12 clip [YT:16XtQjqVzr8@0:01:01]. It is not duplicated in the JSONL.
- The reporter notes that tapping the $1.2B Education Stability Fund needs a 3/5 legislative vote or a governor-declared emergency [YT:16XtQjqVzr8@0:02:19].

### 2026-10-14 KATU: "Kotek, Drazan push for transparency as Portland and Salem-Keizer weigh school closures" (MH2_R4kO4AQ, 5:16)
- The reporter read Kotek's letter. It cites "shock and disappointment" and "confusion about the decision-making timeline and why schools were identified for change or closure", and says "Confusion about the process is not something we should accept." [YT:MH2_R4kO4AQ@0:01:02] [YT:MH2_R4kO4AQ@0:01:20].
- KATU asked Kotek's office whether she wants the timeline changed. Her team did not answer and referred back to the letter [YT:MH2_R4kO4AQ@0:01:51].
- A PPS spokesperson statement says "we've already held 50 sessions" [YT:MH2_R4kO4AQ@0:01:36]. Board Chair Wang did not return KATU's call [YT:MH2_R4kO4AQ@0:00:48].
- Drazan: "there's a difference between having a community engagement session and providing the kind of data and information that would help inform those sessions" [YT:MH2_R4kO4AQ@0:03:04]. Per the reporter, she says enrollment can be fixed by improving student outcomes [YT:MH2_R4kO4AQ@0:03:16]. Reporter: six of the proposed closures are Title I schools [YT:MH2_R4kO4AQ@0:04:42].

### 2026-10-15 KATU: "Irvington parents join call for PPS to slow school closure process" (jQnBqmnQ4Uo, 2:41)
- The superintendent met Irvington Elementary parents at the school that day. They want more time and clearer answers on what receiving schools gain [YT:jQnBqmnQ4Uo@0:00:24] [YT:jQnBqmnQ4Uo@0:01:13].
- No official was quoted on camera. The PPS statement (reporter paraphrase) says moving fast is important "to protect student services that could be lost due to declining enrollment". It also says listening sessions began in March, though families learned of the proposals this month [YT:jQnBqmnQ4Uo@0:01:53] [YT:jQnBqmnQ4Uo@0:02:03].

### 2026-10-17 KOIN: "PPS superintendent urged to slow down decision on possible school closures" (NadLYOURLtg, 3:15)
- At the Grant High community meeting, an audience member asked when PPS will take the governor's (and, per the questioner, the state treasurer's) slow-down message seriously [YT:NadLYOURLtg@0:01:58]. Armstrong: "I don't think she said pause, but I heard the slow down, take the time to consider feedback. That's absolutely what we're doing." [YT:NadLYOURLtg@0:02:11] (confidence high: the reporter says "Superintendent Armstrong asked about this today" immediately before).
- An unidentified district speaker defended the "tradeoffs" toward "a better resource school" [YT:NadLYOURLtg@0:00:59]. It is kept in the JSONL as Armstrong with confidence low: the voice is not named.
- Reporter: she will recommend one of two plans next month, closing 13 or 10 elementary schools plus Sellwood MS; the board decides in December [YT:NadLYOURLtg@0:01:30] [YT:NadLYOURLtg@0:02:59]. A Rose City Park Vietnamese DLI family raised equity concerns [YT:NadLYOURLtg@0:02:38].

## How Wang's positions compare with earlier ones

Sources: `analysis/people/eddie-wang.md`, `analysis/board_closure_stance/eddie-wang.md`.

1. **No change on the core stance (+2).** On Oct 13 he again argued against delay: "the longer we wait, the more severe the fix will have to be" and "no more road left to kick the can" [YT:kdPfX6KH05c@0:31:00] [YT:kdPfX6KH05c@0:31:23]. That matches "sooner the better" (Mar 10) and "picking up the can that we've kicked down the road" (Jul 7). The SEGC "do it once" fixation recurs, with his signing of the SEGC opposition letter [YT:kdPfX6KH05c@0:07:36]. So does the equity frame (zip code decides band access; almost 70% of underserved students in unsustainable schools) [YT:kdPfX6KH05c@0:08:33] [YT:kdPfX6KH05c@0:15:48].
2. **New: he concedes the board lacks data.** "Uh, not not all of it. No." [YT:kdPfX6KH05c@0:14:42]. Analysis: this is the first time in the archive that he publicly says the board lacks requested impact data. Engelsman's KGW comment the next day, that data won't come until mid-November [YT:16XtQjqVzr8@0:01:41], gives the timing.
3. **The money framing is still in tension.**
   - He says rightsizing is "reducing the expense of the district so that we can get to a point where we no longer have to worry about budget cuts" [YT:kdPfX6KH05c@0:19:07], and cites a ~$500K subsidy per small school [YT:kdPfX6KH05c@0:20:46].
   - In the same answer: "we're not um closing schools to save on the budget" [YT:kdPfX6KH05c@0:20:08].
   - This repeats the Sept 1 pattern: "cuts are need to happen, period" and "one less admin team" alongside the district's "not cost-saving" line.
4. **Closure scale.**
   - Sept 1: "if it means this and to get there means 20 closures, I'm fine" [YT:5RMfvT-sAPU@2:24:37].
   - Oct 13: he credits the district with cutting from 20 to 14 for transition-support reasons [YT:kdPfX6KH05c@0:48:45].
   - Analysis: he now endorses the smaller number without saying whether he prefers A (14) or B (11). He says he does not know how much the final option will change [YT:kdPfX6KH05c@0:29:48]. His timeline (the 20 figure came "before" the Green report) does not fit the archive: WW's "up to 20" ran Aug 26 [NEWS:NEWS-20260826-wweek-1], after the audit was presented Aug 4 [MTG:2026-08-04/758088].
5. **Focus options.** "deserves a robust discussion" and "needs to be deeply explored" on Sunnyside [YT:kdPfX6KH05c@0:44:09] [YT:kdPfX6KH05c@0:44:29]. This is consistent with his Apr 28 shift toward a non-closure approach to focus options. He did not defend the Sunnyside K-8 change as such.
6. **Surplus property.** "public assets need to stay public assets" and "strongly against" sale [YT:kdPfX6KH05c@0:22:45] [YT:kdPfX6KH05c@0:22:50]. "PPS has a very strong policy for protecting public assets" [YT:kdPfX6KH05c@0:22:40] closely echoes the Oct 6 board-meeting remark by an unidentified director ("a relatively strong policy") [YT:zOUH2Jq7Owo@4:26:38]. Analysis: this makes Wang the likely speaker on Oct 6, but the Oct 6 attribution should stay unconfirmed until the speaker is identified there.
7. **Governance signal.** He said he speaks "for myself, not for the full board" [YT:kdPfX6KH05c@0:22:21]. He did not return KATU's call about Kotek's letter on Oct 14 [YT:MH2_R4kO4AQ@0:00:48]. No public reaction from Wang to the Kotek letter is archived.

## How Armstrong's positions compare with earlier ones

Source: `analysis/people/kimberlee-armstrong.md`.

1. **First public preference: Scenario B.** "I'm I'm definitely leaning into scenario B" [YT:D3dVt33To7g@0:21:06]. Before this she presented A/B/C without a preference. On Oct 6 she said staff "isn't to come here and persuade", and that the board could accept, amend or "defer this work to a later time" [YT:zOUH2Jq7Owo@3:11:14] [YT:zOUH2Jq7Owo@3:11:30]. Analysis:
   - B is the smaller option (11 closures).
   - Her spring range was 5–12 and "as low as one, two, or or three" [YT:h_0YMlJnXPk@0:59:10]. On Sept 1 she said board members had told her 5–12 was too low [YT:5RMfvT-sAPU@2:11:46].
   - Leaning to B moves back toward her original range and away from what she described as the board's appetite.
2. **Harder line on pausing.**
   - Oct 6 (KPTV): input is expected "to lead to changes" [YT:IF_vv3wXgAE@0:03:40]. The reporter paraphrases her as saying a board pause is "very possible" [YT:IF_vv3wXgAE@0:03:46].
   - Oct 16: "what are we waiting for? And to go slower to do what?" [YT:D3dVt33To7g@0:02:23]; C "just delays the inevitable" [YT:D3dVt33To7g@0:21:46].
   - Oct 17 (KOIN): Kotek's letter "I don't think she said pause" [YT:NadLYOURLtg@0:02:11].
   - Analysis: after the governor's letter, she treats "slow down" as satisfied by the ongoing engagement window, not by any change to the December timeline.
3. **Phasing offered, but limited so far.** "There will be some things that are phased in" [YT:D3dVt33To7g@0:03:52]. Her only examples (Sellwood MS and Marysville in June 2028) were already in the published family guides [PPS:pps_net/rightsizing/school_impact/sellwood.pdf p.3] [PPS:pps_net/rightsizing/school_impact/marysville.pdf p.3]. Watch the Nov 4 themes report and the early-November recommendation for any new phasing.
4. **New commitments:**
   - a staffing plan with the recommendation [YT:D3dVt33To7g@0:09:09];
   - all closure funds reinvested in schools [YT:D3dVt33To7g@0:10:44];
   - publishing the opt-out loss modeling [YT:D3dVt33To7g@0:13:43].

   Analysis: the staffing plan answers the SEGC audit's receiving-school questions and Engelsman's data requests. But she ties definitive resource levels to the state school fund and "after the election on November 3rd" [YT:D3dVt33To7g@0:13:05], and repeats the "set by the governor" line from KPTV [YT:IF_vv3wXgAE@0:01:44].
5. **Unchanged:**
   - closures "not ... to save money" and not to reduce the $65M deficit [YT:D3dVt33To7g@0:11:12], consistent with April's "not a cost-saving strategy";
   - full trust in PSU forecasts [YT:D3dVt33To7g@0:05:57];
   - the system-over-site framing [YT:D3dVt33To7g@0:20:06].
6. **Wang vs Armstrong.** Both reject delay and frame the current phase as feedback-driven tweaking. Wang would not pick A or B (Oct 13); Armstrong picked B three days later. Their capture-rate figures differ: Wang says ~87% → 71% → ~73% [YT:kdPfX6KH05c@0:04:22]; Armstrong says "mid-80s" → "mid-70s", "has not gone back up" [YT:D3dVt33To7g@0:14:13] [YT:D3dVt33To7g@0:14:34].

## Attribution problems

- **KGW u0XKcIye1HI@0:01:44** ("what Portland Public Schools needs right now is stability"): the reporter does not name the speaker. It follows a sentence about both Kotek and Drazan, but Kotek "was not available for an interview", so it is Drazan with confidence medium.
- **KOIN NadLYOURLtg@0:00:59** ("These are tradeoffs…"): a district voice at the Grant meeting, not named. Armstrong with confidence low; do not use in syntheses.
- **Kotek quotes are letter text read by reporters, not speech.** The letter itself is not in `sources/correspondence/`, which holds only the Grayber letter. Recommend archiving the Kotek letter (and any state treasurer letter mentioned at KOIN @0:01:58) with provenance.
- **OPB:** all attributions are high. They come from the vendor and plain-text speaker labels plus the host naming the guest. The YouTube captions have no labels.

## Caption errors noticed (not corrected in quotes unless bracketed)

- **OPB Oct 13:**
  - "organ problem" = Oregon problem (0:04:45);
  - "DI" = DLI (0:34:04 onward; bracketed once in a quote);
  - "Salwood" = Sellwood (0:26:53; bracketed in the quote);
  - "DRA" = DBRAC (0:31:15);
  - "RSJ" = RESJ (0:36:03);
  - "PBS proposals" = PPS (0:33:27);
  - "reenter" = recenter (0:18:29);
  - "size from district office" = sighs (0:19:16);
  - "Green" at 0:47:31 is a rating ("Green"), not Dr. Green. Dr. Terrance Green is referenced at 0:47:56.
- **OPB Oct 16:**
  - "Kimberly" = Kimberlee;
  - "well resource" = well-resourced (bracketed once).
- **KATU clips:**
  - "K2"/"K12" = KATU;
  - the reporter's name is garbled as "Sunnivie Drazan" and "Thumby Varma" (= Tanvi Verma, as she signs off);
  - the MH2_R4kO4AQ opening "New on KGW News, we're on your side" is a KATU clip ("On Your Side" is KATU's slogan; "KGW" is likely a caption error).
- **KOIN:** "board share" = board chair (0:01:51).
