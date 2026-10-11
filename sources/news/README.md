# News coverage index: Portland Public Schools (PPS)

`index.jsonl` holds one record per article, district release or advocacy item. Records were retrieved on two passes: 2026-10-10 (131 records) and 2026-10-11 (102 records, appended below the first set). Both passes used WebSearch and WebFetch; the shell had no web access. Each record's provenance is in its `url` and `retrieved` fields. Per CLAUDE.md rule 8, the index stores metadata, a summary in my own words, short numeric facts and quotes under 25 words. It never stores article text.

- **Records:** 233 (131 from the first pass, 102 from the second)
- **Date range:** 2024-09-12 to 2026-10-09. Two 2024 background items; everything else is 2025-01-01 or later.
- **Access** (field `access`; some second-pass records also carry `access_note`):

| Access | All | 2nd pass | Meaning |
|---|---|---|---|
| `full` | 187 | 63 | Article text was read through WebFetch and summarized. Includes 2 mirrors (newsbeep.com copies of a WW and a KGW story), 3 secondary rewrites (Construction Owners Club ×2 and Hoodline, all relying on The Oregonian or DJC) and 1 advocacy-outlet summary (Heartlander). Each is flagged in `access_note` and the outlet name. |
| `partial` | 2 | 0 | Only part of the page was readable. |
| `search-snippet-only` | 33 | 28 | Headline and URL from WebSearch only, because the page returned an error. Dates are often estimated (see `date_precision`). |
| `listing-only` | 11 | 11 | Known only from PPS's own "In The News" list (`pps_in_the_news_list.json`), and the outlet could not be fetched. |

## Count by outlet (all records)

| Outlet | Records | 2nd pass | Notes |
|---|---|---|---|
| Willamette Week | 85 | +30 | Includes 1 letters page and 1 newsbeep mirror. 9 Sept–Oct 2026 WW pages returned server errors and are `search-snippet-only`: 6 from this pass and 3 from the first. |
| KATU | 28 | +11 | |
| KPTV / FOX 12 | 23 | +8 | Includes the full Armstrong interview of Oct. 5, 2026 (YouTube `vRKUxqyWvYg`, transcript in `sources/youtube/transcripts/`). |
| KGW | 22 | +22 | KGW pages cannot be fetched (client errors, including AMP and Yahoo copies). 1 is `full` via a newsbeep mirror, 18 are `search-snippet-only` with estimated dates, and 3 are `listing-only`. |
| OPB | 21 | +3 | |
| KOIN | 20 | +10 | koin.com now errors. digital-release.koin.com mirrors and Yahoo copies work when they appear in search. |
| The Oregonian/OregonLive | 7 direct | +6 | 1 via a Bend Bulletin reprint (first pass). 6 are `listing-only` from the PPS list. Also see the 3 rewrites below. |
| Axios Portland | 5 | | |
| PPS releases / media.pps.net | 4 | | |
| Portland Mercury | 2 | +1 | |
| Southeast Examiner | 2 | | |
| Portland Tribune | 2 | +2 | Bond results May 2025; scenarios Oct. 2026. |
| K-12 Dive / Facilities Dive | 2 | +1 | |
| Construction Owners Club | 2 | +2 | Rewrites of DJC Oregon and Oregonian stories on the Andersen/Benson dispute. |
| Hoodline | 2 | +2 | One rewrite of an Oregonian story (Procedeo hires ex-board members), and one aggregator item that was not fetched. |
| NW Examiner | 1 | | |
| Portland Monthly | 1 | | |
| Building Design + Construction | 1 | +1 | |
| Daily Tidings (Ashland) | 1 | +1 | |
| Heartlander News (Herzog Foundation) | 1 | +1 | A secondary source with an advocacy mission. Used only because it relays the Oregonian report on the Secretary of State referral and the final audit response. |
| Softwood Lumber Board press release | 1 | +1 | |

## Count by topic (all records; records can carry several topics)

| Topic | Count | | Topic | Count |
|---|---|---|---|---|
| bond | 75 | | seismic | 24 |
| board | 72 | | boundary-changes | 22 |
| budget | 70 | | equity | 22 |
| school-closures | 64 | | high-school-modernization | 21 |
| rightsizing | 56 | | procedeo (new) | 19 |
| enrollment | 36 | | facilities | 15 |
| labor | 34 | | election | 13 |
| layoffs | 31 | | mlc | 13 |
| community-reaction | 29 | | state-funding | 13 |
| jefferson-hs | 26 | | audit (new) | 8 |

Other second-pass tags: `cbse` (Center for Black Student Excellence, 7), `recall`, `state-oversight`, `contractor-dispute`, `litigation`, `ethics`, `governance` and `staffing-cuts`.

## PPS "In The News" list triage

`pps_in_the_news_list.json` is PPS's curated list of 105 items (Jan. 2025–Oct. 2026). `pps_in_the_news_triage.csv` records a decision for each one:

- **already-indexed: 5.** One of these, the KPTV Jefferson groundbreaking, was already indexed under a `kptv.com` URL variant.
- **added: 23.** These cover the rightsizing interview, bond and groundbreakings, Jefferson boundaries, the legislative and budget letter, CBSE, the Aug. 2025 consolidation story, and the bond election.
- **skip: 77.** These are features, arts, sports, awards, academics, celebrity visits and two malformed URLs. Each has a reason.

**Analysis:** PPS's list is weighted toward positive stories. Of the 131 records in this index tagged school-closures, rightsizing, budget or layoffs, PPS's list includes about 4: the Aug. 2025 WW consolidation story, the KGW legislative-letter story, the Aug. 2026 KPTV one-on-one and the Oct. 2026 KPTV interview. It includes none on the Procedeo audit, the layoff grievance or MLC.

## Major storylines

1. **Scenario A/B release (Oct. 5, 2026) and reaction.** Scenario A closes 14 schools: Maplewood, Stephenson, Irvington, Rose City Park, Buckman, Creston, Marysville, Woodmere, Lewis, Beach, James John, Peninsula, Sabin and Sellwood MS. Scenario B spares Stephenson, Rose City Park and Lewis. Both convert seven of 11 K-8s to K-5, close MLC's 9-12 program, move Odyssey from East Sylvan to MLC, and end Sunnyside's focus option. Sellwood students go to Hosford and Brentwood.
   - Six of the 10 schools on both lists are Title I. Per a Mercury correction, all of them except Buckman are majority students of color.
   - Franco's memo: 67% (A) and 57% (B) of schools at threshold, against 26% under the status quo.
   - Armstrong (KPTV, Oct. 5): final recommendation Nov. 17; the board can adopt, amend or defer; closures are "not just about money." The board vote is set for Dec. 15.
   - KGW (via mirror) tallies about $18M already spent on seismic work at closure candidates, plus $50M planned at Rose City Park and Beach.
   - OPB (Oct. 7) covers the Chiefs for Change claims about Armstrong.
   - PAT is now led by Alisha Chavez.
2. **Escalation from 1–12 / 5–10 to 10–20 closures (Mar–Sep 2026).** Spring listening sessions (KATU, Apr. 17–27) recorded Franco saying "not … a money perspective" and Armstrong giving a range of 1–12 closures. Other milestones are listed in the first-pass storylines in `analysis/timeline_from_news.md`.
3. **Budget crisis and layoffs.**
   - 2026-27 draft cuts: 315 positions by level.
   - Jan. 30, 2026 letter to the Legislature, with Wang calling morale "at an all time low".
   - June 2026 layoffs: 82+ notices. PAT's class-action grievance says 77 violate seniority rules. 87 educators were laid off in the end.
   - Engelsman's $13.2M restoration amendment failed 1–6 on June 23.
   - Reserves are at the 5% floor (about $41M).
4. **2025 bond, high school costs and Procedeo (new storyline).**
   - Jan.–Apr. 2025: the Cornerstone audit and the board's cost-cutting framework, which saved only $33–67M in total.
   - Andersen/Benson dispute and cross-lawsuits: Benson cost about $410M against a $269M budget.
   - Procedeo's $149.5K Jefferson study, then its $61.5M program-management contract (Dec. 2, 2025, 5–2, followed by a public apology from Chair Wang). The Office of School Modernization was dismantled, and the Jefferson "shell" acceleration was dropped (Mar. 2026).
   - Procedeo retained ex-board members Hollands and Greene (Oregonian via Hoodline).
   - Sept. 2026: a leaked Sjoberg Evashenk audit (heightened fraud risk, overpayment of more than $700K), a recall petition against Wang by Michael Rosen, a Secretary of State referral to the DOJ (per WW headline and an Oregonian report relayed by Heartlander), and board votes on the audit recommendations. Oct. 2026: PPS disputes the final audit.
5. **Jefferson High.** The May 2025 memo, the Scenario C boundary vote (dual assignment ended unanimously, boundary passed 6–1 with Engelsman voting no) and the accountability provisions. Groundbreaking was May 2026, with move-in August 2029.
6. **Elections.** May 2025: PAT-endorsed candidates won 3 of 4 races, and La Forte beat a PAT-backed 18-year-old by 814 votes. May 2027: 4 seats are open, Splitt is not running, and Wang is undecided.
7. **Enrollment decline, PSU forecasts, MLC and governance.** See `analysis/timeline_from_news.md`.

## Gaps and caveats

- **The Oregonian/OregonLive remains blocked.** WebFetch is blocked for oregonlive.com and for web.archive.org, and archive.ph requires a permission that timed out. No Yahoo or MSN syndication of Oregonian education stories turned up. Oregonian coverage appears here only as `listing-only` records and through rewrites by Construction Owners Club, Hoodline and Heartlander. Key Oregonian stories known only secondhand:
  - the Andersen memo (Jan. 2025)
  - the Benson lawsuits (Sept. 2025)
  - Procedeo's hiring of Hollands and Greene (~May 2026)
  - the Secretary of State referral (Sept. 2026)
- **KGW cannot be fetched** (client error on article, AMP and Yahoo URLs). Headlines exist for about 18 relevant 2025–26 stories, including MLC, furloughs, layoffs, closures and Title I. Their dates are estimates; check `date_precision`. Only one KGW story is `full`, via a newsbeep.com mirror.
- **Willamette Week, Sept–Oct 2026:** many recent WW pages return server errors. That includes the audit story (Sept. 15), the recall petition (Sept. 17), the Secretary of State referral (Sept. 22), the board split (Sept. 30), PPS's response to the auditor (Oct. 2), PPS disputing the audit (Oct. 7), the Oct. 8 Murmurs and the Oct. 11 letters. Those are headline-only.
  - The Oct. 5 scenario story is now readable via a newsbeep mirror (NEWS-20261005-wweek-2). The first-pass snippet record NEWS-20261005-wweek-1 was left unchanged.
  - **Highest-priority verification:** the Secretary of State/DOJ referral (NEWS-20260922-wweek-1). Its content rests on a headline plus a secondary summary.
- **koin.com** now errors. Three Oct. 2026 KOIN stories are headline-only.
- **Still not found:** Street Roots, The Skanner, Hollywood Star and NE Examiner have no 2025–26 PPS closure or budget coverage in the search index. Searches restricted to those domains returned only pre-2024 items.
  - Portland Observer has one Oct. 8, 2026 item that appears to be a reprint of the PPS release. It is not indexed separately.
  - Portland Tribune: 2 items. Its older townnews URLs date from before 2025.
- **Moody's downgrade (Aa2 to Aa3):** still no news coverage found. The Bond Buyer hit was a 2022 Sherwood SD story.
- **Low-quality aggregators seen but not indexed:** karmactive.com (Oct. 7, 2026). It states a vote in "early 2027", which conflicts with every other source, and a "$171.8M cut since 2023-24" figure that is unverified. The K-12 Dive duplicate of the Facilities Dive Sept. 2026 story was also skipped.
- **Quote reliability:** quotes were extracted through the WebFetch summarizer, which was told to copy quoted text exactly. Verify against the original before publishing. Quotes in the KPTV interview record come from the official caption track and carry `[YT:vRKUxqyWvYg@H:MM:SS]` references. "Mykola" in that transcript is a caption artifact for "COLA".
- **Date notes:**
  - Several second-pass records have approximate or estimated dates (`date_precision`).
  - Where the URL date and the byline date differ (UTC vs Pacific), the Pacific/event date is used.
  - A few `id`s use the event date and not the publication date (noted in `date_precision`).
- **Conflicting figures between outlets:**
  - 2026-27 FTE cuts: 315 (KPTV draft), 320, 322, 336.
  - 2026-27 shortfall: $50M vs $56.3M.
  - Mid-year 2025-26 gap: $12M, $14M (KGW headline) and $22.5M.
  - June 23 amendment: $13.1M vs $13.2M.
  - Each is kept as the outlet reported it.

## Related files

- `pps_in_the_news_list.json`: PPS's own list (source; see its `source` and `retrieved` fields).
- `pps_in_the_news_triage.csv`: triage decision for each of the 105 list items (url, date, title, outlet, decision, reason).
- `analysis/timeline_from_news.md`: dated event timeline, with each line citing `[NEWS:<id>]`. The second-pass additions are in a separate section at the end.
- `analysis/people/_quotes_from_news.jsonl`: 264 quotes from PPS board members, the superintendent and staff. 81 were added in the second pass; second-pass rows may carry `context` and `video_ref`.
