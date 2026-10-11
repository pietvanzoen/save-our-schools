# News coverage index: Portland Public Schools (PPS)

`index.jsonl` holds one record per article, district release or advocacy item. All records were retrieved 2026-10-10 using WebSearch and WebFetch; the shell had no web access. Provenance for each record is in its `url` and `retrieved` fields. Per CLAUDE.md rule 8, the index stores metadata, a summary written in my own words, short numeric facts and quotes under 25 words. It never stores article text.

- **Records:** 131
- **Date range:** 2024-09-12 to 2026-10-07. Two 2024 background items; everything else is 2025-01-01 or later.
- **Access:** 124 `full`, 2 `partial`, 5 `search-snippet-only`

## Count by outlet

| Outlet | Records |
|---|---|
| Willamette Week | 55 |
| OPB (incl. *Think Out Loud* and *First Look* newsletter) | 18 |
| KATU | 17 |
| KPTV / FOX 12 | 15 |
| KOIN (incl. 3 Yahoo-syndicated copies) | 10 |
| Axios Portland | 5 |
| PPS releases / media.pps.net | 4 |
| Southeast Examiner | 2 |
| Portland Mercury | 1 |
| The Oregonian/OregonLive (via The Bulletin reprint) | 1 |
| NW Examiner | 1 |
| Portland Monthly | 1 |
| K-12 Dive / Facilities Dive | 1 |

## Count by topic

Records can carry several topics.

| Topic | Count |
|---|---|
| budget | 47 |
| school-closures | 37 |
| board | 35 |
| rightsizing | 34 |
| bond | 30 |
| enrollment | 29 |
| labor | 22 |
| seismic | 21 |
| layoffs | 18 |
| community-reaction | 14 |
| jefferson-hs | 13 |
| boundary-changes | 12 |
| equity | 11 |
| state-funding | 9 |
| midyear-deficit | 7 |
| advocacy | 7 |
| mlc | 6 |
| psu-forecast | 6 |
| grade-reconfiguration | 5 |
| election | 5 |
| furloughs | 5 |
| superintendent-contract | 4 |

## Major storylines

1. **Scenario A/B release (Oct. 5, 2026) and reaction.** Scenario A closes 14 schools: Maplewood, Stephenson, Irvington, Rose City Park, Buckman, Creston, Marysville, Woodmere, Lewis, Beach, James John, Peninsula, Sabin and Sellwood MS. Scenario B spares Stephenson, Rose City Park and Lewis. Both convert seven K-8s to K-5. Coverage spans OPB, KATU, KPTV, Axios, WW and PPS. The Oct. 6 board meeting drew hundreds of protesters. Board member Engelsman called the plan "mayhem", and Rep. Thuy Tran said PPS had broken a promise on Rose City Park. The vote is set for Dec. 15. Strong follow-up angles:
   - KATU on Title I equity: the same six Title I schools close under both scenarios.
   - KATU on bond money spent at closure candidates (Woodmere, Marysville, Rose City Park, Beach).
   - KATU on why closures yield limited savings.
2. **Escalation from 5–10 to 10–20 closures (Mar–Sep 2026).** The arc runs from the Feb. 2025 first mention, to March 2026 (5–10 closures), April listening sessions, the April 14 launch vote and the May 26 guiding principles, the Aug. 26 jump to 10–20, and the Sept. 1 work session where the staff model called for 15 elementary and 3 middle school closures. WW published a stance-by-stance board roundup on Sept. 3.
3. **Budget crisis.**
   - 2025-26: about $40M cut and 200+ positions; adopted 5–2.
   - 2026-27 mid-year hole: $22.5M, closed with furloughs and a shortened school year.
   - 2026-27 budget: $2.77B, a $56.3M gap and 320–336 FTE cut, including 87 educator layoffs.
   - 2027-28: a $65.2M structural gap is projected, with a preliminary reduction plan in Jan. 2027.
   - Running threads: state funding and the Education Stability Fund, PERS (employer rate rising from about 4% to about 20%), and reserves held at the 5% floor.
4. **2025 bond (Measure 26-259, $1.83B) and seismic.** The bond passed May 20, 2025 with about 58–59%. The seismic resolution (Res. 7109) passed 7–0 before the vote. The fight over the prioritization formula ran from 35% to 90% weight on risk. Nine schools were selected, with full retrofits at Beverly Cleary and Rose City Park. Jefferson ($466M) and Cleveland (~$450M) broke ground in May–June 2026. **Analysis:** several URM and bond-work schools later appear on the closure lists, a tension KATU (Oct. 7) and Rep. Tran both raise.
5. **Jefferson High enrollment.** Dual assignment ended Jan. 13, 2026 (Scenario C: Sabin to Jefferson, Irvington to Grant). The coverage includes a race and class framing (WW, Dec. 10, 2025) and the programming build-out.
6. **Enrollment decline and PSU forecasts.** Enrollment was 42,622 in 2025-26 and is projected at 36,763 by 2035-36. Kindergarten rose in fall 2025 for the first time since 2012-13. High school enrollment peaked in 2022-23. Multnomah County is projected to lose 17,474 school-age children.
7. **Metropolitan Learning Center.** PPS announced the end of MLC's high school in February 2026, reversed it within weeks, and the October scenarios propose it again. The episode raised a dispute over the 2003 school-closure policy.
8. **Governance and labor.**
   - May 2025 board election: Chase-Miller unseated Greene; La Forte and Engelsman joined.
   - Armstrong's contract extension passed 5–2 in Sept. 2026.
   - PAT opposition and bargaining begin Jan. 2027, and four board seats are up in spring 2027.
   - Southeast Guiding Coalition evaluation: high staff turnover at merged schools.

## Gaps and caveats

- **The Oregonian/OregonLive is blocked** for WebFetch and does not appear in this search index. Only one Oregonian story (Jan. 2025) was found, through a Bend Bulletin reprint. Expect significant missing Oregonian coverage, especially for Oct. 2026.
- **KGW**: no 2025–26 KGW articles on these topics turned up in search, and KGW search pages failed to load. KGW coverage almost certainly exists but is not indexed here.
- **Willamette Week, Oct. 2026**: the Oct. 5 scenario story, the Oct. 6 protest-movement story and the Sept. 19 Title I story returned server errors on every fetch. They are indexed as `search-snippet-only`, with no summary content.
- **Not found (no indexable coverage):** Portland Tribune/Pamplin (2025–26), Street Roots, Oregon Capital Chronicle (PPS-specific), The Skanner, Portland Observer, Hollywood Star (robots-blocked), NE Examiner.
- **Moody's credit downgrade:** board documents record a downgrade from Aa2 to Aa3, with S&P holding at AA- (`sources/boardbook/meetings/2026-02-10_730093_regular-meeting/attachments/3996891_*.pdf.txt`), but **no news coverage was found**.
- **Thin areas:**
  - Southeast enrollment balancing has only two items (the SEGC evaluation and Bridger Creative Science).
  - Grade reconfiguration (K-8 to K-5, middle school model) is mentioned in release-day stories but has no dedicated coverage yet.
  - School-specific "save our school" sites and PTA posts were not found by search. Coalitions named in news coverage are Save PDX Schools, Right-Sizing the Right Way, the Title I Coalition and Safe Structures PPS, but their own sites were not indexed.
- **Quote reliability:** quotes were extracted through the WebFetch summarizer, which was told to copy text inside quotation marks exactly. The summarizer could still introduce small errors, so verify a quote against the original article before publishing it. Fragmentary quotes are reproduced exactly as reported.
- **Date notes:**
  - Two KOIN items (Yahoo copies) have approximate dates, flagged in `date_precision`.
  - Where the URL date and the byline date differ (UTC vs Pacific), the Pacific/event date is used.
- **Conflicting figures between outlets:** the 2026-27 FTE cut appears as 320, 322 and 336, and the 2026-27 shortfall as $50M and $56.3M. These are kept as each outlet reported them.

## Related files

- `analysis/timeline_from_news.md`: dated event timeline, with each line citing `[NEWS:<id>]`.
- `analysis/people/_quotes_from_news.jsonl`: 183 quotes from PPS board members, the superintendent and staff.
