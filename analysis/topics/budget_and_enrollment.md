# Budget and Enrollment as Drivers of the 2026 Rightsizing (School Closure) Proposals

Synthesis as of 2026-10-10. Scope: PPS enrollment history (10+ years), forecasts and their vintages, under-enrolled
schools, capture/transfers/charters/focus options; the 2025-26 and 2026-27 budgets (deficits, reductions, staffing,
reserves, State School Fund, PERS, local option levy, credit ratings); per-school cost and staffing-formula evidence;
what PPS has (and has not) said about savings from consolidation; and how leadership links budget pressure to school
size and closures.

Sources: BoardBook attachments and minutes only (no pps.net datasets, transcripts or news were in the archive for
this pass; `sources/pps_net/` is empty). Citations follow `CLAUDE.md`. One document (the 2026-27 CBRC report,
[BB:3997238]) has a garbled text layer; figures quoted from it were read from an OCR of the PDF page and are marked
"(OCR)".

Companion files:
- `analysis/data/enrollment_history_and_forecast.csv` (2,005 rows): ACFR Schedule 17 school and level counts
  2015-16 to 2024-25; school-report actuals 2020-21 to 2025-26; two vintages of PPS school-level projections
  (Apr 2025 and Apr 2026); ADMr/ADMw series; PSU/PRC forecasts; grade-level counts; capture rates; charters.
- `analysis/data/budget_figures.csv` (351 rows): budget totals, General Fund service areas, revenues, fund balance,
  reductions, FTE, PERS, ratings, purchased services, per-pupil figures (formula and school-report "heat map").
- `analysis/topics/budget_enrollment_open_questions.md`: inconsistent figures and gaps.
- Related: `analysis/topics/rightsizing.md` (process, scenarios), `analysis/topics/bond_and_seismic.md` (bond,
  S&P downgrade in TSCC context). This file does not repeat their scenario or bond detail.

Labels: plain statements = what a PPS document (or committee report) says; "minutes record" = Board minutes;
**Analysis:** = my arithmetic or inference.

---

## 1. Bottom line

- **Enrollment has fallen about 10% in nine years, almost all of it in elementary grades.** ACFR Schedule 17 shows
  49,075 students in 2015-16 and 44,086 in 2024-25 [BB:3996892 p.146]. The PSU Population Research Center (PRC)
  counted 42,622 K-12 students in fall 2025, "a decrease of 753 students from fall 2024" and "just over 6,000"
  below 2019-20 [BB:14493920 p.15]. The ACFR elementary grouping (K-5 and K-8 buildings) fell from 27,159 to 19,582
  over 2015-16 to 2024-25, while middle and high school totals rose, partly because K-8s were converted to middle
  schools [BB:3996892 p.145-146].
- **The forecast is continued decline, but vintages and units differ.** The ACFR cites a PSU "Middle Series"
  low of 37,057 in 2034-35 [BB:3996892 p.11]. The 2026 rightsizing decks show -12% from 2025-26 to 2035-36
  [BB:3997023 p.6]. The September 2026 deck projects a 3,446-student decrease by 2031-32 [BB:14357211 p.9]. PPS's
  own school-level projections, summed by this archive, show K-5 falling from 14,326 (2025-26) to 13,962 (2028-29)
  and 6-8 from 7,360 to 6,945 [BB:3997161 p.12-177].
- **Under-enrollment is widespread under PPS's thresholds.** In 2025-26, 33 of 45 K-5 schools were below 360
  students and 23 were below 300. 9 of 15 middle schools were below 500 (**Analysis** of [BB:3997161]).
- **A structural deficit has run for four budget cycles.** PPS reports service-level reductions of $171.8M from
  2023-24 to 2026-27 and a projected further $65.2M for 2027-28 [BB:3997181 p.51]. The 2025-26 budget drew General
  Fund reserves down to the 5% policy minimum. The audited ending balance was $44.3M at 6/30/2025, down from
  $105.5M at 6/30/2023 [BB:3996892 p.126]. The 2025-26 budget also used a $23,961,548 transfer from the PERS reserve
  [BB:3990296 p.1].
- **2025-26 went into a mid-year hole.** Staff projected a $22.5M (2.5%) gap [BB:3996968 p.7]. It was closed with
  discretionary controls ($10.5M) and furlough days ($12M) [BB:3997106 p.5]. Without those steps, the January 2026
  report projected a $26.8M spend-down of the beginning balance [BB:3998328 p.3].
- **2026-27 closes a "$50 million" gap ($56.3M against current service level).** The adopted total is
  $2,768,590,878 [BB:3988878 p.1]. The General Fund is $862.1M, down $6.5M [BB:3997160 p.34]. Total FTE falls by 322
  [BB:3997160 p.24], and General Fund FTE falls by 336 (7%) to 4,481 [BB:3997181 p.32, p.35].
- **Revenue is squeezed from three directions:**
  - The local option levy is about $5M below budget because of compression and falling downtown values
    [BB:3993195 p.4] [BB:3988764 p.18].
  - PERS employer cost goes from about 4% to about 23% of payroll [BB:3997181 p.19, p.52].
  - The state's "extended ADMw" cushion lags enrollment decline [BB:3997160 p.22] [BB:3996528 p.16].
- **Credit ratings cite enrollment.** S&P (AA to AA-, 2025) cited "declining fund balances and declining
  enrollment" [BB:3996394 p.7]. Moody's (Aa2 to Aa3, February 2026) did the same [BB:3996891 p.10]; the minutes
  record the BAC chair attributing the Moody's downgrade to a lower fund balance and declining enrollment
  [BB:3990212 p.3].
- **Per-pupil evidence: size does raise costs, but it does not single out the schools proposed for closure.**
  - Under General Fund formula staffing, K-5 costs $10,037.04 per student and HS $8,609.99. Jefferson costs
    $13,638.41 per student against Grant's $8,010.06 [BB:14511742 p.6].
  - In the school-report "heat map," the highest-cost K-5s (Rosa Parks $16,805, Whitman $14,650) are not closing.
    Sellwood MS, which closes in both scenarios, is the second-cheapest middle school per student ($9,552)
    [BB:3997161 p.10-11].
- **No savings estimate exists for consolidation.** No PPS document in the archive estimates savings from
  consolidation, either per school or in total. Staff wrote that "The number of potential layoffs can not be
  determined at this time" [BB:14493920 p.7]. The only unit cost offered is an illustrative "Annual Elementary
  School operating budget" of $4.0 million [BB:3996811 p.8].
- **The Board was told to expect less than it might hope.** The Board-commissioned SEGC equity audit (Green & Hanson)
  warns that districts "often overestimate the savings produced by school closures" [BB:3997427 p.147]. It also
  proposes planning floors of about 450+ (elementary), 600+ (middle) and 650+ (K-8), higher than PPS's thresholds of
  360/500/500 [BB:3997427 p.146].

---

## 2. Enrollment

### 2.1 Ten-year history by level (October 1 counts, ACFR Schedule 17)

ACFR column "2025" = school year 2024-25 (October 2024), confirmed by the transmittal text "Student enrollment as of
October 2024 was 44,086" [BB:3996892 p.10]. Level groupings are by building type, so they shift whenever schools are
reconfigured (K-8s became middle schools at several sites between 2017-18 and 2023-24).

| School year | Elementary (K-5 + K-8 bldgs) | Middle | High | PPS alternative | CBOs | Special services | Charters | Total |
|---|---|---|---|---|---|---|---|---|
| 2015-16 | 27,159 | 5,911 | 11,183 | 1,817 | 964 | 451 | 1,590 | 49,075 |
| 2016-17 | 26,620 | 6,457 | 11,348 | 1,760 | 968 | 451 | 1,585 | 49,189 |
| 2017-18 | 26,627 | 6,449 | 11,768 | 1,659 | 1,035 | 455 | 1,564 | 49,557 |
| 2018-19 | 25,248 | 7,516 | 12,220 | 1,631 | 912 | 529 | 1,494 | 49,550 |
| 2019-20 | 24,988 | 7,579 | 12,425 | 1,632 | 973 | 496 | 1,385 | 49,478 |
| 2020-21 | 23,265 | 7,416 | 12,667 | 1,243 | 872 | 408 | 1,443 | 47,314 |
| 2021-22 | 20,705 | 7,560 | 13,050 | 1,795 | 637 | 455 | 1,295 | 45,497 |
| 2022-23 | 27,805 as printed (20,881 corrected*) | 7,464 | 13,125 | 1,553 | 683 | 456 | 1,294 | 52,380 as printed (45,456 corrected*) |
| 2023-24 | 20,421 | 7,388 | 13,144 | 1,352 | 759 | 376 | 1,331 | 44,771 |
| 2024-25 | 19,582 | 7,356 | 13,138 | 1,554 | 794 | 356 | 1,306 | 44,086 |

Source: [BB:3996892 p.145-146]. *The 2022-23 column is internally inconsistent: Irvington shows 2,514 and Kelly
2,830, and the printed elementary subtotal (27,805) does not equal the sum of its own rows (25,641).
**Analysis:** replacing those two cells with the budget Volume 2 values (228 and 356) gives 20,881 for elementary
and 45,456 overall [BB:3997161 p.88, p.98].

- The ACFR says enrollment fell "from a recent high of 49,557 in the fiscal year 2017-18 to 44,086 in fiscal year
  2024-25" [BB:3996892 p.11].
- **Analysis:** from 2015-16 to 2024-25, elementary-building enrollment fell 7,577 (-27.9%). Middle rose 1,445 and
  high rose 1,955. The total fell 4,989 (-10.2%).
- The one-year elementary drop of 2,560 in 2021-22 coincides with Kellogg MS opening and SE schools shedding grades
  6-8. For example, Arleta went from 485 to 269 and Lent from 476 to 277 [BB:3996892 p.145-146].

### 2.2 2025-26 counts: several "official" totals

| Count | Value | Source |
|---|---|---|
| PRC fall 2025, K-12 | 42,622 | [BB:14493920 p.15] |
| RAA October 2025 total (transfer memo) | 43,479 | [BB:3990672 p.2] |
| "District Total" as of 9/12/2025 (projection 43,529) | 43,887 | [BB:3996602 p.3] |
| "School Total" K-12 as of 9/12/2025 (projection 40,308) | 40,630 | [BB:3996602 p.3] |
| ADMr estimate, 2026-27 budget | 42,467 | [BB:3997160 p.26] |
| Students used for "$1,179 per student" | 42,404 | [BB:3996811 p.8] |
| Sum of 2026-27 Vol 2 school reports (**Analysis**) | 39,647 | [BB:3997161 p.12-177] |

These measure different populations: K-12 only or including PreK, with or without charters and CBOs, headcount or
average daily membership. None of the rightsizing materials reconciles them (see open questions).

**Grade cohorts (9/12/2025):**
- K 2,738; 1st 2,765; 2nd 2,881; 3rd 2,990; 4th 3,155; 5th 3,081.
- 6th 3,220; 7th 3,184; 8th 3,142.
- 9th 3,481; 10th 3,381; 11th 3,264; 12th 3,348.
- Source: [BB:3996602 p.3].
- **Analysis:** the average grade size is about 2,935 in K-5, 3,182 in 6-8 and 3,369 in 9-12. This is the "steep
  decline ... working its way through the system" described in the August 2026 memo [BB:3997426 p.2].

### 2.3 By level, 2021-22 actual through 2028-29 projected (sum of school reports)

**Analysis:** this table sums the per-school enrollment rows in the 2026-27 Proposed Budget Volume 2. Rows are actual
through 2025-26 and PPS projections for 2026-27 to 2028-29 [BB:3997161 p.12-177]. Groupings:
- "K-8" includes ACCESS (1-8) and Odyssey.
- "6-8" includes Harrison Park while it was still a K-8 (2021-22, 2022-23).
- "Alternative" is Alliance and MLC.
- Bridger and Clark have rows only from 2023-24.

| Level | 2021-22 | 2022-23 | 2023-24 | 2024-25 | 2025-26 | 2026-27 proj | 2027-28 proj | 2028-29 proj |
|---|---|---|---|---|---|---|---|---|
| K-5 | 14,794 | 14,863 | 15,202 | 14,683 | 14,326 | 14,091 | 13,899 | 13,962 |
| K-8 | 4,827 | 4,818 | 5,276 | 5,222 | 5,069 | 4,980 | 4,900 | 4,870 |
| 6-8 | 8,089 | 8,039 | 7,388 | 7,356 | 7,360 | 7,289 | 7,237 | 6,945 |
| 9-12 | 13,050 | 13,125 | 13,144 | 13,138 | 12,990 | 12,827 | 12,807 | 12,744 |

**Check (Analysis):** the 2024-25 K-5 + K-8 total less ACCESS (323) equals the ACFR elementary figure (19,582), and
the 9-12 total equals ACFR's 13,138 [BB:3996892 p.146].

### 2.4 Forecasts and their vintages

| Forecast | Value | Vintage / provenance | Source |
|---|---|---|---|
| PSU "Middle Series" district low | 37,057 in 2034-35 | PSU forecast cited in FY2025 ACFR (dated 1/28/2026; vintage not stated) | [BB:3996892 p.11] |
| PSU high school enrollment in ten years | "about 11,000" | PSU forecast of July 2024, as characterized by TSCC | [BB:3996394 p.5] |
| District change 2025-26 to 2035-36 | -12% | Mar-Apr 2026 rightsizing decks (vintage not stated) | [BB:3997023 p.6] [BB:3988980 p.6] |
| Decrease projected in 2031-32 | -3,446 | Sept 1, 2026 deck; PRC forecast "updated on July 24, 2026" is the modeling source | [BB:14357211 p.9] [BB:14493920 p.28] |
| PRC "continued reductions ... through at least 2029-30" | qualitative | as stated by CBRC, May 2026 | [BB:3997238 p.12] (OCR) |
| ADMr 2026-27 | 41,661 (from 42,467) | 2026-27 budget | [BB:3997181 p.15] |
| Extended ADMw 2026-27 (funded count) | 51,390 (from 52,392) | 2026-27 budget | [BB:3997181 p.15] |
| School-level projections | see §2.3 | Apr 2025 and Apr 2026 budget Volume 2 | [BB:3989519] [BB:3997161] |

How PRC forecasts are made: PRC "has calculated district enrollment projections for PPS since 1999." It uses a
"grade progression model" (cohort survival), and PPS uses the middle series [BB:3997160 p.225]. Kindergarten
forecasts use birth data, and school forecasts are reconciled to district totals [BB:3997160 p.226]. PRC "takes into
account new housing developments" [BB:14493920 p.28].

**Recent accuracy (Analysis)** compares the April 2025 school-level projections for 2025-26 with actuals
[BB:3989519] [BB:3997161]:
- K-5: 14,184 projected vs 14,326 actual.
- K-8: 5,083 vs 5,069.
- 6-8: 7,343 vs 7,360.
- 9-12 excluding McDaniel: 11,349 vs 11,361.
- All levels excluding McDaniel: actual was 127 (0.3%) above projection.
- The 9/12/2025 snapshot likewise showed the school total 322 above projection, with kindergarten +130
  [BB:3996602 p.3].
- In fall 2026 the direction reversed. As of 9/11/2026, kindergarten was "running 115 students below the baseline
  projections," and K-12 was "about 700 students below last year's official October counts" [BB:14493920 p.32].
- The April 2026 projections raised the near-term K-5 outlook compared with April 2025:
  - 2026-27: 14,091 vs 13,726.
  - 2027-28: 13,899 vs 13,233.

### 2.5 Under-enrolled schools (2025-26 actual vs PPS thresholds)

Thresholds are K-5 360, K-8 and middle 500, high school 1,100 [BB:14511742 p.10]. PPS derived 360 and 500 "as
guided by the prototype school description in the Quality Education Model," and 1,100 from the Jefferson process
[BB:3997426 p.2].

| Level | Schools | Below threshold, 2025-26 | Below 300 | Below threshold, 2028-29 proj |
|---|---|---|---|---|
| K-5 | 45 | 33 | 23 | 35 |
| K-8 (incl. ACCESS, Odyssey) | 12 | 9 | 2 | 10 |
| 6-8 | 15 | 9 | 0 | 12 |
| 9-12 | 9 | 2 (Benson 1,025; Jefferson 391) | 0 | 1 |

Source: **Analysis** of [BB:3997161 p.12-177].
- **Analysis:** these counts imply 27% of K-5 schools at 360+ and 40% of middle schools at 500+. That is consistent
  with the KPI baseline charts summarized in `rightsizing.md` §2.2. The chart pages are images; their text layer is
  not extractable.
- PPS's own deck gives the 2025-26 K-5 median as 269 [BB:3997004 p.7] [BB:3988980 p.5]. The October 2025
  school-report data give 294 (open question).
- Functional capacity is not what limits size. "There are no current K-5 buildings with a functional capacity below
  360," and the smallest middle-school capacity is Gray at 588 [BB:14493920 p.32].

### 2.6 Capture rates, transfers, charters, focus options

- **Capture:**
  - The resident capture rate rose from 74.4% (fall 2019) to an estimated 76.6% (2025), still 5.6 points below the
    2015 high of 82.2% [BB:14493920 p.15].
  - PPS says it has "only ... In District Capture rate by school," which excludes residents attending charters,
    private schools or homeschool [BB:14493920 p.15].
  - Staff attribute the decline to lower catchment percentages, declining birth rates and fewer families moving in
    [BB:14493920 p.3].
- **Inter-district transfers (net is small):**
  - Standard transfers in 2025-26: 259 approved in and 114 out, net +145 [BB:3989643 p.1].
  - In 2025-26, 1,432 non-residents attended PPS (3.3% of 43,479), up from 1,163 (2.3%) in 2015-16
    [BB:3990672 p.2].
  - Denials for lack of space rose; the top denying schools were Benson (17), Franklin (11), Grant (8) and da Vinci
    (8) [BB:3990672 p.3].
- **Charters (PPS-sponsored), 2025-26 vs 2024-25 enrollment:**
  - Emerson 140 (131).
  - KairosPDX 173 (210).
  - Le Monde 383 (374).
  - Portland Arthur Academy 165 (164).
  - Portland Village School 436 (400).
  - Total 1,297 [BB:3991091 p.1-4].
  - The General Fund pass-through to charters is $19,770,508 in FY26 and $18,977,508 in FY27 [BB:3997181 p.29].
- **Focus options and DLI:**
  - "just under 600 students" are on focus-option or DLI waitlists. Meeting demand would require added sections at
    Winterhaven, Sunnyside, da Vinci and Benson; Spanish DLI demand is unmet [BB:14493920 p.8].
  - The SEGC audit found DLI students leave PPS "at roughly half the rate of non-DLI students" (about 6% vs 11% at
    SEGC schools, 2023-24) [BB:3997427 p.11].
- **Retention after past consolidations:** "district retention remained stable at over 93%" when building retention
  dropped [BB:14493920 p.9]. No numbers on families who left after the Marshall, Edwards or Bridger consolidations
  were provided [BB:14493920 p.9].

---

## 3. Budget

### 3.1 Chronology of the structural deficit

| Year | What PPS reported | Source |
|---|---|---|
| 2022-23 | $30M central cuts; schools $0 | [BB:3988777 p.6] |
| 2023-24 | $10M central cuts | [BB:3988777 p.7] |
| 2024-25 | $30M cuts (schools -$14.2M, central -$15.7M); 204.3 FTE / $29.9M. The Apr 2026 table shows -$40.0M CSL reductions for this year | [BB:3988777 p.8] [BB:3988764 p.4] [BB:3997181 p.51] |
| 2024-25 & 2025-26 | "$105M Deficit Timeline": $72M two-year shortfall plus $32M PERS increase; "$40M of $105M Remaining" | [BB:3988777 p.5] |
| 2025-26 | Reductions of $41.3M / 228 positions (Feb 2025), then $40M / 210 positions (Mar 2025), then $43M total including $3M added central cuts (Apr 2025). CSL reductions later shown as -$43.0M original plus -$22.5M mid-year = -$65.5M | [BB:3988777 p.14] [BB:3996313 p.21] [BB:3990983 p.26] [BB:3997181 p.51] |
| 2026-27 | Estimated at a "Minimum of $32 Million" (Apr 2025); $50M (Oct 2025 onward); $56.3M against CSL in the proposed budget | [BB:3996386 p.8] [BB:3996700 p.8] [BB:3997181 p.51] |
| 2027-28 | Projected -$65.2M; "Reset" to a ~$834.8M ongoing baseline | [BB:3997181 p.50-51] |
| Cumulative | $171.8M of service-level reductions, 2023-24 to 2026-27 | [BB:3997181 p.51] |

The adopted-budget deck adds a separate "Cumulative Reductions: Central Office $67.9M | Schools $43.8M"
[BB:3990695 p.2].

### 3.2 The 2025-26 budget

- **Size:**
  - The adopted total is $2,035,116,552 [BB:3990156 p.1].
  - The General Fund is $868.6M including $41.2M contingency [BB:3991017 p.35].
  - The budgeted beginning balance is $45.0M [BB:3991017 p.27].
  - Expenditures excluding contingency exceeded revenues by $3.8M. PPS described this as "the conclusion of a
    drawdown of reserves, meeting the minimum 5% requirement" [BB:3991017 p.35].
- **Risk posture.** The proposal listed a "minimal General Fund reserve," a draw on the PERS Stabilization Fund,
  spending restrictions and central-office hiring limits. Staff added: "To shield schools from the impacts of
  reductions as much as possible, we are willing to take these risks" [BB:3990983 p.21].
- **Revenue assumptions:**
  - PPS's first-year SSF share is $291.0M of an $11.36B State School Fund [BB:3991017 p.26].
  - Extended ADMw is 52,324 [BB:3991017 p.26].
  - Property tax plus local option revenue is $640.6M [BB:3991017 p.26].
- **School staffing changes:**
  - Upper-grade blends were introduced.
  - Middle and high schools got a minimum class size of 15.
  - The middle school Title I base fell from 2.0 to 1.0.
  - IB supports were removed [BB:3991017 p.41].
  - PPS said "Enrollment decline contributes to about 9% of school-based FTE reductions" [BB:3996313 p.5]. Items
    labeled "Due to Enrollment Decline" total $2.2M and 15 positions [BB:3996313 p.19-20].
- **Approval and adoption votes:**
  - The Budget Committee approved Res 7116 on May 19, 2025. The minutes record "4 yes – 0 no – 1 abstain – 2
    Absent" but list five "Yes" votes [BB:3996425 p.3] [MTG:2025-05-19/689137]. Director Splitt "voiced discomfort
    in voting yes on an inadequate budget" [BB:3996425 p.3].
  - Adoption (Res 7121, June 10, 2025) passed 5-2. Brim-Edwards and Hollands voted no [BB:3996489 p.4]
    [MTG:2025-06-10/689410]. Board comments expressed "concern that continued state underfunding has forced
    difficult trade-offs" [BB:3996489 p.4].
- **PERS reserve:** Res 7325 (June 23, 2026) ratified the one-time transfer of $23,961,548 from the PERS Rate
  Stabilization Reserve Fund. The amount exceeds the limits in the 2011 resolution [BB:3990296 p.1].
- **Mid-year shortfall:**
  - Staff listed the drivers as vacancy savings not materializing ($12M), transportation ($5.5M), maintenance
    including emergency declarations ($6M) and a levy shortfall ($5M), partly offset by about $6M
    [BB:3988764 p.18].
  - The Q2 report projected an ending General Fund balance of $17,684,900 [BB:3998327 p.6].
  - The January report projected $17,476,689 and a "$26.8 million" spend-down [BB:3998328 p.3, p.6].
  - The gap was closed with $10.5M of controls and $12M of furloughs [BB:3997106 p.5].
  - Minutes record staff advising against using reserves because "current reserves represent less than one month
    of payroll" [BB:3997147 p.2].
  - Amendment 2 (Res 7324) moved $10,000,000 out of contingency [BB:3997356 p.1].
  - In September 2026 staff said the year-end result "will be very close" to the 5% target. If below, "we will have
    to adjust the current year resources (beginning fund balance) to match" [BB:14493920 p.17].

### 3.3 The 2026-27 budget

- **Framing:** "A primary driver of the District's structural deficit is sustained enrollment decline." Also: "the
  fixed costs of operating 81 schools and the rising costs of personnel, benefits, and utilities continue to grow"
  [BB:3997160 p.22].
- **General Fund:**
  - $862.1M, -$6.5M [BB:3997181 p.27].
  - Revenue increases: SSF +$19.9M; sale of fixed assets +$2.5M.
  - Revenue decreases: PERS reserve transfer -$23.5M; property taxes -$6.5M; beginning balance -$4.0M
    [BB:3997181 p.27].
  - Revenue assumptions: SSF share $305.4M; property tax $533.6M (+0.4%); local option $103.9M (-4.8%)
    [BB:3997181 p.17].
  - Beginning balance $41.0M [BB:3997181 p.18]; contingency $41.1M [BB:3997160 p.34].
- **Gap-closing by service area (CSL $918,398,076, reductions -$56,286,020)** [BB:3997181 p.29]:
  - Central Office -$13.2M.
  - Schools -$20.5M.
  - Specialized Programs -$14.6M.
  - Transfers/vacancy/contingency -$10.6M.
  - Building Supports +$3.4M.
  - Measured against FY26 adopted, Schools are +1.64% while Central Office is -14.21% [BB:3997181 p.30].
- **Staffing:**
  - Total FTE goes to 5,513, -322 [BB:3997160 p.24]: 142 in building supports and central office, 180 in schools
    and specialized programs ("enrollment-driven staffing adjustments, blended classrooms, and Multilingual Learners
    (MLL) ratio changes") [BB:3997160 p.22].
  - In school cost centers, licensed FTE goes from 2,296 (CSL) to 2,168 [BB:3997181 p.38].
  - Formula changes: counselors at 350:1 with a minimum of 1.0; instructional coaches and interventionists reduced;
    1/2 blends added; middle and high school ratios changed [BB:3997181 p.58-60].
  - Staff later reported that 125 of 717 originally allocated K-5 FTE went to blended classrooms [BB:14493920 p.35].
- **Risks named:**
  - PPS: "No reserves are available to support operational overages" [BB:3997181 p.46].
  - The CBRC said the 1% COLA assumption is "significantly lower than any COLA the district has negotiated"
    [BB:3997238 p.4] (OCR) [BB:3997240 p.9].
- **Adoption:**
  - Budget Committee approval (Res 7308, May 26, 2026) and adoption (Res 7326, June 23, 2026) were both for
    $2,768,590,878 [BB:3990562 p.1] [BB:3988878 p.1].
  - Minutes record Res 7308 passing 7-0 [BB:3998080 p.4] (the minutes label it "7307") and Res 7326 passing
    6-0-1, with Engelsman abstaining [BB:3998082 p.4].
  - Floor amendments filed for June 23 included Director Engelsman's proposal to "reinstate funding ($13,120,000)
    for staffing in schools in student facing positions" [BB:3992230 p.1], plus travel, OIPA and AI-pause
    amendments [BB:3991431 p.1] [BB:3991747 p.1] [BB:3992122 p.1]. Minutes record their outcomes: travel
    (Res 7339) passed 7-0 [BB:3998082 p.4]; OIPA funding (Res 7340) failed 3-4; AI pause (Res 7341) passed 7-0;
    the Engelsman staffing amendment (Res 7342) failed 1-6 [BB:3998082 p.5].

### 3.4 Reserves (General Fund ending balance, audited, $ thousands)

| FY | 2015-16 | 2016-17 | 2017-18 | 2018-19 | 2019-20 | 2020-21 | 2021-22 | 2022-23 | 2023-24 | 2024-25 |
|---|---|---|---|---|---|---|---|---|---|---|
| Balance | 37,835 | 20,104 | 38,282 | 39,887 | 64,474 | 88,691 | 98,804 | 105,497 | 86,078 | 44,323 |

Source: [BB:3996892 p.126-127].
- Board policy sets a 5%-10% reserve goal, "with an expectation that the District will achieve and sustain a 10.00
  percent reserve" [BB:3996892 p.63].
- PPS also spent $121,844,309 of ESSER funds from FY21 to FY24 [BB:3988764 p.16].
- **Analysis:** the 2019-23 build-up coincided with ESSER. The 2023-25 drawdown of about $61M (105.5 to 44.3)
  funded operations that federal relief had supported.

### 3.5 Revenue mechanics that tie money to enrollment

- **State School Fund:**
  - The SSF distributes "on a weighted per-student basis" (ADMw) [BB:3997160 p.39].
  - Formula revenue is about $11,812 per ADMr [BB:3996528 p.15].
  - The SSF is 75.6% of General Fund revenue [BB:3996528 p.9]. The ACFR puts the SSF plus related property taxes at
    about 81% [BB:3996892 p.13].
  - "Extended ADMw" pays on the higher of current or prior year. It "Gives time to adjust staffing levels" and lists
    "School Optimization" among its purposes [BB:3996528 p.16]. Still, "a continuous, multi-year enrollment decline
    ultimately outpaces this statutory buffer" [BB:3997160 p.22].
  - For 2025-26, SSF revenue was "tied to 2024-2025 enrollment" [BB:3998327 p.3].
- **Local option levy:**
  - The rate is $1.99/$1,000 [BB:3990156 p.2]. It provides about 14% of General Fund revenues [BB:3996892 p.13].
  - Revenue was $97.4M in 2019-20 and is projected at $103.9M for 2026-27 [BB:14305424 p.1].
  - Teachers funded fell from "over 916" (2019-20) to 741 (2024-25) and about 686 (2025-26) [BB:3996390 p.1]
    [BB:14305424 p.2].
  - The 2025-26 shortfall of about $5M equals "~ 33 Licensed FTE" [BB:3993195 p.4].
  - Staff linked the shortfall to compression and falling downtown office values. "PPS Local Option Levy has
    experienced three years of decline" [BB:3989745 p.3].
- **PERS:**
  - The employer rate was 4.20% blended plus a 17.39% UAL fringe in 2025-26 [BB:3991017 p.28], and 4.18% + 18.79% =
    22.97% in 2026-27 [BB:3997181 p.19].
  - The 2027-29 advisory rate goes from 4.18% to 20.82% [BB:3997181 p.52].
  - The 2021-23 valuation added 5.33 points, which is "$28 million each year" [BB:3996942 p.10].
  - Expiring side accounts drive the increase [BB:14330795 p.9].
- **Teacher cost:** an average salary of $104,579 plus benefits gives $160,851 per FTE [BB:3997181 p.21]. 82% of
  expenditures are personnel [BB:3997150 p.13].

### 3.6 Credit ratings

- S&P downgraded PPS from AA to AA- before the May 2025 bond vote. PPS told TSCC that "the rationale was largely
  focused on declining fund balances and declining enrollment rather than the amount of new debt" [BB:3996394 p.7].
  Bond-context detail is in `bond_and_seismic.md`.
- Moody's downgraded PPS from Aa2 to Aa3 at the February 2026 sale, and S&P maintained AA- [BB:3996891 p.10]. The
  minutes record the BAC chair saying the downgrade was "due to a lower fund balance and declining enrollment"
  [BB:3990212 p.3].

---

## 4. Per-school cost and efficiency evidence

### 4.1 Staffing formulas embed a small-school premium

- **K-5 (2025-26).** Base school-wide support is 2.75 FTE (principal, 0.75 admin assistant in licensed equivalents,
  1.0 coach) for every K-5 under 550 students. Schools of 550+ get 3.75 or more [BB:3991017 p.206]. Classes are
  formed by sections per grade [BB:3991017 p.204].
- **Middle (2025-26).** Every middle school under 800 gets 4.25 FTE of school-wide support [BB:3991017 p.208]. In
  2026-27 the table is a flat 3.25 for all middle schools [BB:3997160 p.215].
- **High school (2025-26):**
  - Small schools (<1,000) get a 5 FTE base at 24.7:1.
  - Large schools (>1,000) get a 9 FTE base at 27.4:1 [BB:3991017 p.209].
  - A school of 100-600 receives 6.50 FTE of school-wide support in 2026-27 [BB:3997160 p.217].
- **Analysis:** fixed positions are spread over fewer students in small schools. A 200-student K-5 carries the same
  2.75 FTE base as a 500-student K-5, which is 1.4 FTE per 100 students vs 0.55.

### 4.2 PPS's October 2026 per-pupil analysis (General Fund formula staffing only)

- **Averages per student:** K-5 $10,037.04; MS $9,280.79; HS $8,609.99; K-12 $9,484.17. The analysis excludes "SPED,
  MLL, Title I, M98" [BB:14511742 p.6].
- PPS says: "Economies of scale drive costs: Elementary schools cost ~$1,400 more per student than high schools due
  to smaller facility size" [BB:14511742 p.6].
- Jefferson costs $13,638.41 per student vs Grant's $8,010.06, or "+70%" [BB:14511742 p.6].
- **Ten-school sample of "subsidy received"** = projected enrollment x (school $/pupil - $9,484.17)
  [BB:14511742 p.7]:
  - Rosa Parks (161): +$545,049.34.
  - Whitman (196): +$533,103.54.
  - Beach (286): +$479,528.64.
  - Rieke (255): +$325,537.77.
  - Woodstock (351): +$215,057.88.
  - Creston (198): +$194,135.21.
  - Atkinson (358): +$116,668.72.
  - Kelly (412): +$20,523.78.
  - Ainsworth (554): -$142,227.74.
  - Richmond (505): -$637,503.62.
- **Analysis:** of the ten, only Beach and Creston close under either scenario. Rosa Parks and Whitman, the two
  largest "subsidies," are receiving schools. Creston's average class size in the sample is 28.3, the highest of
  the ten.

### 4.3 School-report "dollars per student" (2026-27 budget; General Fund, Title I, Foundation and grants; excludes SPED, ESL, Nutrition)

Source for all figures: [BB:3997161 p.10-11].
- **K-5:** median $11,779 (45 schools); range $8,639 (Alameda) to $16,805 (Rosa Parks).
- **Middle schools (15, excluding MLC):** range $9,113 (West Sylvan) to $13,290 (George).
- **High schools:** range $9,062 (Grant) to $17,438 (Jefferson).

**Closing schools, 2026-27 $/student and rank among 45 K-5s (1 = most expensive):**
- Both scenarios:
  - Woodmere $14,754 (2).
  - Marysville $13,499 (5).
  - James John $13,108 (8).
  - Beach $13,011 (9).
  - Buckman $12,261 (17).
  - Peninsula $12,002 (20).
  - Irvington $11,609 (26).
  - Creston $11,467 (28).
  - Maplewood $11,280 (29).
  - Sabin $10,782 (35).
- Scenario A only: Lewis $11,836 (21); Rose City Park $11,093 (31); Stephenson $10,586 (38).
- Sellwood MS ($9,552) is the second-lowest of 15 middle schools.

**Analysis:**
- Across the 45 K-5s, 2026-27 $/student correlates -0.58 with 2025-26 enrollment and +0.82 with the
  direct-certification share.
- A two-variable least-squares fit gives about -$749 per student for each additional 100 students enrolled, and
  about +$575 for each 10 points of direct certification (R² 0.82).
- Size matters, but much of the per-student variation in this measure reflects poverty-targeted funding. This is a
  crude cross-section, not a causal estimate.

### 4.4 Projected savings from consolidation: what exists and what does not

- No rightsizing document in the archive gives a savings estimate, either per closure or in total (see also
  `rightsizing.md` §1).
  - Asked directly, staff answered: "The number of potential layoffs can not be determined at this time." The most
    affected positions are those "where there is one per building, such as a principal, custodian, possibly a
    school counselor" [BB:14493920 p.7].
  - The same question appears unanswered elsewhere: "how much will we save, per school closed, to close a school?"
    [BB:14493920 p.5].
- **PPS's unit-cost illustrations** (budget framing, not closure savings): the $50M gap equals "$1,179 per student
  (42,404 students)," "312.5 Educator FTEs ($160k each)" or "12.5 Annual Elementary School operating budgets ($4.0
  million each)" [BB:3996811 p.8].
- **Facility-side claims are qualitative:** "With fewer buildings to maintain, crews can address repairs more
  quickly" [BB:14511742 p.9]. The only vacant-building cost given is Smith at "approximately $70,000, including
  insurance costs" per year [BB:14493920 p.23].
- **Analysis (illustrative only, not a PPS figure):**
  - If each K-5 closure eliminated its 2.75-FTE school-wide support base at the $160,851 average teacher cost, the
    saving would be about $442K per school, or $4.9M for 11 closures and $6.2M for 14.
  - Custodial and nutrition FTE (e.g., 2.0 custodial at Abernethy [BB:3997161 p.12]) might add to that.
  - Transportation, receiving-school preparation, retained buildings and any "more than the bare minimum"
    enrichment would reduce it [BB:14493920 p.24].
  - Even at the high end, this is roughly 10% of the projected $65.2M 2027-28 gap [BB:3997181 p.51].

---

## 5. How budget and enrollment arguments are used to justify rightsizing

The framing shifts in four stages, from "enrollment explains part of the budget gap" (early 2025) to "rightsizing is
how we make every school well-resourced within a shrinking budget" (fall 2026).

1. **Budget decks cite buildings explicitly (2025).** Every budget deck from February 2025 on lists "Declining
   Enrollment: We have fewer students and the same number of buildings. Our funding is dependent upon number of
   students" [BB:3988777 p.3] [BB:3990983 p.11] [BB:3997181 p.14].
   - The 2026-27 budget book makes enrollment "A primary driver of the District's structural deficit" and names
     "the fixed costs of operating 81 schools" [BB:3997160 p.22].
   - The state SSF briefing listed "School Optimization" among the reasons extended ADMw gives districts time
     [BB:3996528 p.16].
2. **Oversight bodies press for consolidation (2025-26).**
   - CBRC 2025: "we urge the board to consider more targeted structural reductions—whether to whole programs,
     initiatives, or locations" [BB:3996388 p.2]. Also: "We caution the district against deferring difficult
     decisions about school consolidations" [BB:3996388 p.5].
   - CBRC 2026 urged "additional reductions, in whole or in part, to programs, initiatives and locations"
     [BB:3997238 p.12] (OCR) [BB:3997240 p.15].
   - Rating agencies tied downgrades to fund balance and enrollment [BB:3996394 p.7] [BB:3990212 p.3].
3. **Budget pressure and rightsizing launch together (spring 2026).**
   - The 2025-26 mid-year shortfall (furloughs, "no more fund balance") came in February–March 2026
     [BB:3997016 p.3] [BB:3997147 p.2].
   - Rightsizing was launched in the same period (Res 7296, April 14, 2026; see `rightsizing.md`).
   - The April 2026 engagement decks and the proposed budget use the same line: "As the District faces difficult
     decisions to close the budget gap, it is critical we hear from communities" [BB:3997148 p.5]
     [BB:3997181 p.8].
   - The adopted-budget deck argues that protecting classrooms through enrollment decline has "reached the
     structural limit of this approach" [BB:3990695 p.1].
   - The October 2025 outlook had explicitly assumed "No consolidations or school closures will occur in 2026-27"
     [BB:3996700 p.9]. **Analysis:** this makes 2027-28 (gap -$65.2M) the first budget year closures could affect.
4. **The argument reframes from "savings" to "sufficiency" (summer–fall 2026).** Later materials stress resources
   spread thin rather than dollars saved:
   - "Maintaining more than 80 school sites amid declining enrollment has spread resources increasingly thin"
     [BB:3997426 p.2].
   - "For eight years we have been taking resources from our high schools to subsidize our under enrolled
     elementary, K8 and middle schools" [BB:14430171 p.23].
   - The October 6 per-pupil analysis shows "subsidy received" by small schools and the +70% Jefferson premium
     [BB:14511742 p.6-7].
   - Budget scarcity is also used to rule out the alternative of investing in small schools: "given our looming
     budget deficit, if we do nothing, all schools will continue to experience the types of challenges described"
     [BB:14493920 p.24]. "Because we are still facing an impending budget gap, we are not in a position to consider
     new programming" [BB:14493920 p.24].
   - Enrollment baselines are explicitly the financial base: "These locked spring and summer baseline projections
     form the foundation of our financial and operational modeling as we evaluate the necessary magnitude of
     rightsizing" [BB:14493920 p.32].

**Analysis:** PPS has used the budget argument for rightsizing as a reason (the deficit exists, buildings are a
fixed cost) and as a constraint (no money to fix small schools in place). It has not used it as a quantified promise
(no savings target). The enrollment argument has been quantified (thresholds, KPIs, -3,446 by 2031-32), but its
specific numbers come from vintages that the public documents do not fully reconcile.

---

## 6. Counter-evidence and caveats

- **Savings may be modest and slow:**
  - The Board's own commissioned audit warns that districts "often overestimate the savings produced by school
    closures and underestimate the costs that remain after students leave a building" [BB:3997427 p.147].
  - It notes savings are "often substantial only when closures are paired with personnel reductions"
    [BB:3997427 p.147-148].
  - It calls for a disposition plan and cost estimates before votes [BB:3997427 p.148].
  - PPS's answer to the Board repeats that recommendation [BB:14493920 p.29].
- **Closures cannot fix the macro drivers.** The audit says birth rates, capture, housing costs and state funding
  "cannot be solved by closing buildings" [BB:3997427 p.147].
- **The thresholds are disputed from both sides:**
  - The audit's planning floors (450+/600+/650+) are higher than PPS's thresholds (360/500/500) [BB:3997427 p.146].
  - The audit also says "these numbers should not be used as automatic closure thresholds" [BB:3997427 p.145].
  - Earlier PPS processes used different floors: DBRAC used a K-5 range of 330-720 [BB:3997023 p.12] and SEGC used
    K-5 270+ [BB:3997023 p.13].
- **The cost data do not clearly single out the closing schools:**
  - The highest-cost small schools (Rosa Parks, Whitman, Lee, Boise-Eliot/Humboldt) are not closing.
  - Six of the 13 Scenario-A K-5 closures are below the K-5 median $/student.
  - Sellwood MS (564 students in 2025-26, above the 500 threshold) is among the cheapest middle schools
    [BB:3997161 p.10-11, p.152].
  - Per-student variation tracks poverty funding more than size (Analysis, §4.3).
- **Several closing schools grew from 2021-22 to 2025-26** [BB:3997161]:
  - James John 332 to 365.
  - Marysville 248 to 307.
  - Peninsula 201 to 239.
  - Irvington 248 to 259.
  - Sellwood 553 to 564.
- **The enrollment base is unstable across documents.** Six different 2025-26 totals appear (§2.2). ADMw series
  differ between budget books, and the ACFR 2022-23 column is corrupted (open questions).
- **Projection accuracy is mixed.** The April 2025 projections were slightly low for 2025-26 (+127 actual, +0.3%;
  kindergarten above projection). The April 2026 projections raised near-term K-5. Fall 2026 is running about 200
  below the locked baseline [BB:14493920 p.32].
- **Small schools are not shown to perform worse.** PPS: "there is no data supporting that smaller schools have
  higher test scores. Test scores are better predicted by socio-economic status than school size"
  [BB:14493920 p.27]. Also: "no relationship is noted" between size and scores on its dashboard [BB:14493920 p.4].
- **Other budget levers rival closures in size:**
  - Purchased services rise 61.9% ($269.9M to $437.0M), mostly in capital funds. The General Fund increase is
    $5.8M [BB:3990695 p.10].
  - The CBRC notes the increase is "roughly triple" the budget gap [BB:3997238 p.9] (OCR).
  - The PERS rate jump alone is "$28 million each year" [BB:3996942 p.10].
  - The levy shortfall is about $5M/year [BB:3993195 p.4].
  - **Analysis:** each of these is the same order of magnitude as any plausible closure savings (§4.4).
- **"Central office is lean" vs FTE history.** PPS says central office is 5.8% of the budget, "the low end" of 5-8%
  [BB:3990695 p.5]. The ACFR FTE table shows "Other Staff" rising from 2,048.1 (FY19) to 2,607.5 (FY25) while
  teachers fell from 2,697.3 to 2,665.7 [BB:14493920 p.13] [BB:3996892 p.142-143]. PPS notes SIA and M98 now fund
  many positions [BB:14493920 p.13].
- **The per-pupil headline depends on the denominator.** The CBRC says Volume 2 shows "$11,100 per student reaching
  schools directly" while Volume 1 implies "approximately $26,300 per student" excluding construction and debt
  [BB:3997238 p.3] (OCR). The formula analysis ($9,484.17) excludes all targeted funds [BB:14511742 p.6].
- **Past consolidation evidence is thin.** PPS could not quantify where families went after Marshall, Edwards or
  Bridger. It cites only district-level retention above 93% [BB:14493920 p.9]. The SEGC audit found that one
  whole-school DLI conversion displaced "almost 60%" of students and almost all Black students [BB:3997427 p.11].

---

## 7. Audit and oversight findings relevant to budget and enrollment

- **FY25 ACFR (Talbot, Korvola & Warwick):**
  - Six federal findings and three state findings, attributed by the auditor to "staff turnover" [BB:3988265 p.3-8].
  - State finding 2025-007: General Fund Instruction overspent its appropriation by $4,147K and Special Revenue
    Support Services by $3,584K [BB:3988265 p.8].
  - Finding 2025-008: budget transfers were used instead of a supplemental budget [BB:3988265 p.8].
  - Finding 2025-009: teacher-experience reporting variances affect the SSF formula [BB:3988265 p.8].
  - The CFO notes that more than 50% of the year predated the current finance team [BB:3988265 p.2].
  - The Board accepted the ACFR and corrective action plan by Res 7248 on Feb 10, 2026. The resolution's recital
    refers to the "year ended June 30, 2023" [BB:3989661 p.1]; see open questions.
- **Internal audit (OIPA).**
  - The 2025-26 plan covers ELL compliance, Measure 98, building security and CTE access [BB:3996679 p.1-2].
  - Future topics narrowed to teacher absences, student performance measures and principal supports
    [BB:3997013 p.2].
  - No audit of enrollment forecasting, staffing formulas or closure savings is planned.
- **Hardship Petition Transfer audit.** Implementation status in March 2026 still showed records-retention and
  space-availability controls "Outstanding" or in progress. Standard class-size reporting for transfers "require[s]
  significant time and commitment from other departments" [BB:3997005 p.1-2].
- **CBRC 2026 transparency requests:**
  - Multi-year forecasts.
  - Object-level spending.
  - Per-pupil reconciliation.
  - A feedback loop on its recommendations.
  - Its review window was "nine working days" [BB:3997238 p.2] (OCR) [BB:3997240 p.5-6].

---

## 8. What to watch

- The 2027-28 budget calendar runs alongside the rightsizing decision:
  - Rightsizing vote December 15, 2026, the same date as the Board budget work session setting priorities.
  - Proposed budget April 20, 2027.
  - Adoption June 29, 2027 [BB:14493469 p.1] [BB:14511742 p.45].
- Whether the Superintendent's November recommendation includes a net-savings estimate covering staffing,
  transportation, receiving-school investment and vacant-building costs, as the SEGC audit recommends
  [BB:3997427 p.148].
- The October 1, 2026 count against the locked baseline, which was about 200 below as of 9/11 [BB:14493920 p.32].
- The final 2025-26 General Fund balance against the 5% floor [BB:14493920 p.17].
