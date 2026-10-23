# The 2016 West Side boundary and program changes: the justification, and whether PSU forecasts were cited

Sources: [`sources/pps_net/boundaries_2016/`](../../sources/pps_net/boundaries_2016/) (Board packets and resolutions) and [`dbrac/`](../../sources/pps_net/boundaries_2016/dbrac/) (D-BRAC and Superintendent materials, 2015–16). Both sets were recovered from the Internet Archive; provenance is in each folder's `_manifest.json`. Each citation links to the archived PDF; go to the page shown.

## What was decided
- Res. 5256 was adopted April 19, 2016 as amended and corrected as Res. 5266 on May 17, 2016 [PPS:pps_net/boundaries_2016/2016-04-19_meeting_overview.pdf p.2](../../sources/pps_net/boundaries_2016/2016-04-19_meeting_overview.pdf) [PPS:pps_net/boundaries_2016/2016-05-17_board_packet.pdf p.1](../../sources/pps_net/boundaries_2016/2016-05-17_board_packet.pdf). It:
  - moved Chapman kindergarten to Ramona;
  - moved Odyssey out of Hayhurst to East Sylvan;
  - moved parts of Maplewood and Rieke into Hayhurst and part of Maplewood into Rieke;
  - moved part of Capitol Hill into Stephenson;
  - changed middle-school feeders (Maplewood to Jackson).
  - It also told staff to "Prepare to re-open Smith School as a K-5 school, with a projected launch of fall, 2019" [PPS:pps_net/boundaries_2016/2016-05-17_board_packet.pdf p.21](../../sources/pps_net/boundaries_2016/2016-05-17_board_packet.pdf). (See [2005_closures.md](2005_closures.md): Smith was closed in 2005.)

## How many students Maplewood lost, and where they went

Data: [`data/2016_west_reassignment_flows.csv`](../data/2016_west_reassignment_flows.csv).

**PPS's count: 48 out, none in.** The Superintendent's West Side KPI tables list Maplewood at "# Neighborhood Reassigned Out" 48 and "# Neighborhood Reassigned In" 0 [PPS:pps_net/boundaries_2016/dbrac/Quadrant_KPIs_SuptRecommendationsWest.pdf p.3](../../sources/pps_net/boundaries_2016/dbrac/Quadrant_KPIs_SuptRecommendationsWest.pdf). The tables for Director Kohnstamm's scenario, the version the board adopted, show the same 48 and 0 [PPS:pps_net/boundaries_2016/dbrac/Dir._Kohnstamm_Scenario.pdf p.4](../../sources/pps_net/boundaries_2016/dbrac/Dir._Kohnstamm_Scenario.pdf).
- **What the count measures.** PPS's note says the columns "represent the number of students reassigned in or out of the neighborhood (not the number of students currently enrolled at the school) if fully implemented 2015-16" [PPS:pps_net/boundaries_2016/dbrac/Quadrant_KPIs_SuptRecommendationsWest.pdf p.3](../../sources/pps_net/boundaries_2016/dbrac/Quadrant_KPIs_SuptRecommendationsWest.pdf).
  - So 48 is the number of students living in the moved areas, measured against 2015-16.
  - It is not the number of enrolled students forced to switch. Current students could stay, and their younger siblings had a transfer path.
- **Effect on Maplewood's projections.** Same tables, p.2 [PPS:pps_net/boundaries_2016/dbrac/Quadrant_KPIs_SuptRecommendationsWest.pdf p.2](../../sources/pps_net/boundaries_2016/dbrac/Quadrant_KPIs_SuptRecommendationsWest.pdf):
  - **2015-16:** 359 under the old boundary, 325 under the new one.
  - **2020 forecast:** 404 under the old boundary, 378 under the new one.

**The split between Hayhurst and Rieke (Analysis).** PPS does not publish it, but the reassignment table balances: 541 students out and 541 in [PPS:pps_net/boundaries_2016/dbrac/Quadrant_KPIs_SuptRecommendationsWest.pdf p.3](../../sources/pps_net/boundaries_2016/dbrac/Quadrant_KPIs_SuptRecommendationsWest.pdf). Matching each school's outflow to an inflow:

| Flow | Students | How it is matched |
|---|---|---|
| Chapman → Ainsworth, Bridlemile, Forest Park | 158 = 97 + 44 + 17 | Chapman's 158 out equals those three schools' combined inflow |
| Capitol Hill → Stephenson | 63 | Equal out and in; the resolution moves part of Capitol Hill to Stephenson |
| West Sylvan → Gray | 7 | Middle-school flow |
| Hayhurst (Odyssey) → East Sylvan | 222 | "For Hayhurst and East Sylvan, the number reassigned in/out includes focus option program enrollment" |
| **Maplewood → Rieke** | **≈14** | Rieke's 14 in. Maplewood is the only remaining source that sends students to Rieke |
| Rieke → Hayhurst | 19 | |
| Bridlemile → Hayhurst | 24 | The recommendation moves "a small area south of Beaverton-Hillsdale Highway" from Bridlemile to Hayhurst |
| **Maplewood → Hayhurst** | **≈34** | Hayhurst's 77 in, minus 19 from Rieke and 24 from Bridlemile; also 48 − 14 |

- **What PPS's text supports.** The Superintendent's March 29 recommendation names portions of "Bridlemile, Capitol Hill, Maplewood and Rieke" going to Hayhurst and "a portion of the Maplewood attendance area" going to Rieke [PPS:pps_net/boundaries_2016/dbrac/3-29-16-Super-Final-Recommendations-March-29-16.pdf p.21](../../sources/pps_net/boundaries_2016/dbrac/3-29-16-Super-Final-Recommendations-March-29-16.pdf).
  - Capitol Hill is named among the areas going to Hayhurst. But its 63 students out exactly equal Stephenson's 63 in, so the table counts no Capitol Hill students going to Hayhurst. Analysis: that piece was probably small or had no resident students in 2015-16.
  - The matching assumes the flows the documents describe and no others. For example, it assumes no Rieke students moved to Stephenson.
- **Caveat: Custer Park.**
  - That March recommendation also said "Custer Park would be added to the Hayhurst boundary" (same page).
  - Board members then asked staff to model moving a small part of Maplewood near Custer Park to Rieke instead: "Rieke was selected instead of Hayhurst, because the area is less than one mile to Rieke" [PPS:pps_net/boundaries_2016/dbrac/Directors_scenarios_memo_4.15.16.final.pdf p.3](../../sources/pps_net/boundaries_2016/dbrac/Directors_scenarios_memo_4.15.16.final.pdf). That is the adopted "south of SW Caldew St. and east of SW 25th Ave" area.
  - The memo's 2020 table leaves Maplewood unchanged (404 in both columns) and shows Rieke falling from 392 to 387 (same page). So it cannot be used to size the Custer Park piece.
  - The split of the 48 may therefore have moved a few students from the Hayhurst side to the Rieke side. The total stays 48 in both the March and April tables.
- **Land area (Analysis).** Comparing 2013-14 attendance areas (NCES School Attendance Boundary Survey) with 2025-26 areas (City of Portland School Boundaries layer):
  - about **73 acres** moved from Maplewood to Hayhurst;
  - about **22 acres** moved from Maplewood to Rieke;
  - Hayhurst also gained 32 acres from Rieke and 19 from Bridlemile.
  - Source: the "SW Portland Boundary Overlay" map built Oct 13, 2026 (https://claude.ai/artifact/Szm7RriX6DisJVycLzPet3). The boundary data is not yet archived in this repo.
- **What happened next.** Maplewood enrolled 384 in fall 2016, above both projections [BB:3996892 p.145](../../sources/boardbook/meetings/2026-02-05_730080_audit-committee-meeting/attachments/3996892_FY25_PPS_FINAL_ACFR_1.28.26.pdf).

## The justification: growth and overcrowding
- The resolution's recitals open with "seven straight years of student enrollment growth." They describe a rise in schools with insufficient classroom space alongside schools too small to offer the core program [PPS:pps_net/boundaries_2016/2016-05-17_board_packet.pdf p.19](../../sources/pps_net/boundaries_2016/2016-05-17_board_packet.pdf).
- The named West Side needs were:
  - relief for Chapman and a plan for "future expected residential growth" there;
  - a plan for overcrowding at Hayhurst (neighborhood program plus Odyssey) that would not leave the neighborhood program under-enrolled;
  - relief for Lincoln HS;
  - "Enrollment relief for Capitol Hill and Maplewood schools that would allow both schools to avoid overcrowding for several years" [PPS:pps_net/boundaries_2016/2016-05-17_board_packet.pdf p.19](../../sources/pps_net/boundaries_2016/2016-05-17_board_packet.pdf).
- D-BRAC's February 2016 report framed the moment the same way. It noted "seven years of enrollment increases" and that "demographers are forecasting another 5,000 students in PPS schools in next decade" [PPS:pps_net/boundaries_2016/dbrac/DBRAC-Report-with-Recommendations-FEB-2016-WEB.pdf p.5](../../sources/pps_net/boundaries_2016/dbrac/DBRAC-Report-with-Recommendations-FEB-2016-WEB.pdf). It described Hayhurst and Odyssey as "bursting at the seams as young families snatched up still relatively affordable homes" [PPS:pps_net/boundaries_2016/dbrac/DBRAC-Report-with-Recommendations-FEB-2016-WEB.pdf p.22](../../sources/pps_net/boundaries_2016/dbrac/DBRAC-Report-with-Recommendations-FEB-2016-WEB.pdf).
- At the Jan 19, 2016 Wilson-cluster D-BRAC meeting, staff said December data "forecast even more crowding at Westside schools, including Chapman and Capitol Hill" [PPS:pps_net/boundaries_2016/dbrac/011916-DBRAC-Wilson.pdf p.2](../../sources/pps_net/boundaries_2016/dbrac/011916-DBRAC-Wilson.pdf).

## Were PSU forecasts cited?
- **The resolution itself: no.** Res. 5256/5266 does not name PSU or quote a forecast number. Its recitals rest on recent growth, overcrowding and the community process [PPS:pps_net/boundaries_2016/2016-05-17_board_packet.pdf p.19](../../sources/pps_net/boundaries_2016/2016-05-17_board_packet.pdf).
- **The staff analysis behind it: yes, explicitly.**
  - The Superintendent's West Side KPI tables give a "Forecast 2020" for every school. They state that the 2020-21 estimates "are based on current K-5 school boundaries and the latest population estimates from the Population Research Center @ PSU" [PPS:pps_net/boundaries_2016/dbrac/Quadrant_KPIs_SuptRecommendationsWest.pdf p.2](../../sources/pps_net/boundaries_2016/dbrac/Quadrant_KPIs_SuptRecommendationsWest.pdf).
  - Staff told D-BRAC that "Enrollment forecasts developed in 2014 based on 2013 data are the baseline for scenario modeling" [PPS:pps_net/boundaries_2016/dbrac/Enrollment_balancing_DBRAC_10.8.15-FINAL.pdf p.26](../../sources/pps_net/boundaries_2016/dbrac/Enrollment_balancing_DBRAC_10.8.15-FINAL.pdf). Analysis: that is PSU's 2014-15 edition, built on October 2013 enrollment.
  - PSU's Charles Rynerson briefed D-BRAC on forecasting methods [PPS:pps_net/boundaries_2016/dbrac/DBRAC-Rynerson.Forecasting_Overview.pdf p.1](../../sources/pps_net/boundaries_2016/dbrac/DBRAC-Rynerson.Forecasting_Overview.pdf) (scanned; OCR text). The D-BRAC report lists the PSU Population Research Center among its expert presenters [PPS:pps_net/boundaries_2016/dbrac/DBRAC-Report-with-Recommendations-FEB-2016-WEB.pdf p.7](../../sources/pps_net/boundaries_2016/dbrac/DBRAC-Report-with-Recommendations-FEB-2016-WEB.pdf).

## What the 2016 forecast said about Maplewood, and what happened
From the Superintendent's West Side tables, with figures as printed [PPS:pps_net/boundaries_2016/dbrac/Quadrant_KPIs_SuptRecommendationsWest.pdf p.2](../../sources/pps_net/boundaries_2016/dbrac/Quadrant_KPIs_SuptRecommendationsWest.pdf) [PPS:pps_net/boundaries_2016/dbrac/Quadrant_KPIs_SuptRecommendationsWest.pdf p.3](../../sources/pps_net/boundaries_2016/dbrac/Quadrant_KPIs_SuptRecommendationsWest.pdf):

| | 2015-16 actual | 2020 forecast, no change | 2020 forecast, Superintendent's plan |
|---|---|---|---|
| Maplewood enrollment | 359 | 404 | 378 |
| Maplewood utilization | 99.5% | 112.8% | 106.5% |
| Capitol Hill enrollment | 437 | 494 | 455 |
| Capitol Hill utilization | 102.0% | 114.1% | 106.1% |

- The table note adds: "Future overcrowding at Capitol Hill and Maplewood will be addressed with the re-opening of Smith School, potentially by the 2019-20 school year" [PPS:pps_net/boundaries_2016/dbrac/Quadrant_KPIs_SuptRecommendationsWest.pdf p.3](../../sources/pps_net/boundaries_2016/dbrac/Quadrant_KPIs_SuptRecommendationsWest.pdf).
- Actual October counts were Maplewood 374 (2019-20), 347 (2020-21) and 291 (2021-22), and Capitol Hill 416, 346 and 324 [BB:3996892 p.145](../../sources/boardbook/meetings/2026-02-05_730080_audit-committee-meeting/attachments/3996892_FY25_PPS_FINAL_ACFR_1.28.26.pdf).
- Analysis: Maplewood's 2020 forecast under the adopted plan (378) was close to its actual 2019-20 count (374), but both schools then fell sharply. The overcrowding that justified shrinking Maplewood's zone and planning to reopen Smith never arrived. Smith was not reopened and is still vacant.
- Analysis: the logic ran the opposite way from 2026. In 2016 a growth forecast was the reason to shrink Maplewood's boundary. In 2026 a decline forecast is the reason to close it. Both rest on PSU-based projections five years out.
