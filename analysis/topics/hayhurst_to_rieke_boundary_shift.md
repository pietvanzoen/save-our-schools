# Hayhurst → Rieke boundary shift: housing units and K-5 students

Compiled 2026-10-22. Question: how many homes are in the part of Hayhurst's neighborhood that Scenarios A and B move to
Rieke (including Stephens Creek Crossing), and how many K-5 students does that area send to Hayhurst today?

**Bottom line (Analysis):** about **585–655 dwelling units** (≈285 single-family, ≈300–370 multifamily, including the
122-unit Stephens Creek Crossing). That housing holds an estimated **70–120 K-5 public-school children**, of whom roughly
**50–90 attend Hayhurst today** (central estimate ≈65). Stephens Creek Crossing alone accounts for about 28–44 of the
children. PPS's own projections independently imply the moved area contributes **at least ~36, and plausibly 50–80**,
students to Rieke in 2027-28. PPS has not published a count for this area.

Files: `analysis/data/hayhurst_to_rieke_shift_parcels.csv` (one row per parcel),
`analysis/data/hayhurst_to_rieke_shift_k5_estimate.csv` (the yield arithmetic),
`analysis/data/hayhurst_to_rieke_shift_area.geojson` (study polygon). Rebuild with `python3 tools/hayhurst_rieke_shift.py`
(add `--fetch` to re-pull the parcel data).

## 1. What PPS proposes

- Hayhurst "would welcome 70% of the school boundary from the closing Maplewood K-5 school. A portion of Hayhurst's
  current boundary would shift to Rieke." [PPS:pps_net/rightsizing/school_impact/hayhurst.pdf p.3]
- Rieke "receives a portion of the Hayhurst boundary to create a logical, connected boundary between Rieke and
  Hayhurst." [PPS:pps_net/rightsizing/school_impact/rieke.pdf p.3]
- Same in both scenarios. Students continue to Robert Gray MS and Ida B. Wells HS, so the middle/high pathway does not
  change for this area [PPS:pps_net/rightsizing/school_impact/rieke.pdf p.3].

**The area.** On the status-quo map, Hayhurst's neighborhood has a southeast "panhandle" bounded by SW Vermont St /
SW Capitol Hwy (north), SW 25th Ave (east), SW Capitol Hwy (west) and SW Troy St (south); on the Scenario A/B map that
panhandle is gone from Hayhurst and Rieke's line moves west to Capitol Hwy
[PPS:pps_net/rightsizing/school_impact/hayhurst.pdf p.4] [PPS:pps_net/rightsizing/school_impact/rieke.pdf p.4].
Rieke's further extension west of Capitol Hwy toward SW 35th Ave is the 30% of Maplewood, not Hayhurst
(Analysis: read from the same two maps). Between SW 25th and about SW 29th, Capitol Hwy runs on the Vermont alignment,
so the north edge is one street.

## 2. Housing units

Source: Multnomah County assessor taxlots and City of Portland (BDS) address points, pulled from Portland Maps on
2026-10-22 for the study polygon (`sources/gis/portlandmaps/hayhurst_rieke_shift/`, query in `_manifest.json`).
A parcel counts if an interior point falls inside the polygon; 337 parcels do.

| Type | Parcels | Units (low–high) | Notes |
|---|---|---|---|
| Detached single-family | 252 | 265 | 13 have a second unit (ADU or duplex, assessor UNITS = 2) |
| Attached (row/townhouse) | 20 | 20 | |
| 2–4 unit plexes | 15 | 47 | Mostly on SW Capitol Hwy and SW Troy St |
| Market-rate apartments | 7 | 110–179 | Dwell Apartments, 6810 SW 26th (53); 6630–6640 SW Capitol Hwy (18–54); 6808 SW Capitol Hwy (11); 2724 SW Custer (11–22); Troy St and Canby Ct buildings (17–39) |
| Condominiums | 2 | ~15 | Multnomah Heights (~8), Miles Street (~7); counted from address points |
| Units over shops / mixed use | 3 | 5 | Capitol Hwy |
| **Stephens Creek Crossing** | 2 | **122** | Home Forward public housing, 6715 SW 26th Ave |
| **Total** | | **≈584–653** | |

Ranges are where the assessor's UNITS field disagrees with building size and address points (each case is explained
in the `note` column of the parcel CSV). The other 36 parcels are churches, offices, shops, a day-care center, city
property or vacant lots.

**Stephens Creek Crossing.** Home Forward's page lists 122 one- to four-bedroom flats and townhomes built in 2013, with
a unit table of 19 one-bedroom, 21 two-bedroom, 79 three-bedroom and 5 four-bedroom units (124 in the table vs 122 in
the text), most of them subsidized public housing; it lists Hayhurst as the K-5 school
(`sources/housing/homeforward/stephens-creek-crossing.html`). The assessor shows 150 + 47 = 197 units on its two
parcels, which does not fit the building area, so 122 is used. It replaced the 60-unit Hillsdale Terrace, which PSU's
forecasts identified in 2009–2010 as Hayhurst-area public housing
[PPS:pps_net/data-archives/2010-11/psu_prc_enrollment_forecast_2010-11.pdf p.39].

## 3. K-5 students: bottom-up estimate

Yields are from PSU's 2026-27 forecast: average PPS students age 5–17 per unit by housing type (Table 2.6)
[PPS:pps_net/data-and-reporting/2026-27/psu_prc_enrollment_forecast_2026-27_to_2035-36.pdf p.16] and K-5 students per
regulated affordable 2+ bedroom unit (Table 4.1)
[PPS:pps_net/data-and-reporting/2026-27/psu_prc_enrollment_forecast_2026-27_to_2035-36.pdf p.25]. K-5 is taken as 6 of
the 13 single-year ages in Table 2.6.

| Component | Units | K-5 per unit | K-5 children |
|---|---|---|---|
| Single-family (detached + attached) | 272 | 0.12–0.21 | 33–57 |
| Second units on house lots | 13 | ~0.02 | ~0 |
| Market-rate multifamily | 177–246 | 0.05–0.08 | 9–20 |
| Stephens Creek Crossing | 122 | 0.23–0.37 | 28–44 |
| **Total K-5 public-school residents** | | | **69–122** |
| **Attending Hayhurst (×74%)** | | | **51–90** |

- Single-family high end = PSU's 0.45 × 6/13. The low end is **Analysis:** a judgment discount for an established
  neighborhood with older households; PSU does not publish it.
- Market-rate multifamily uses PSU's 1-bedroom (0.04) and 2-bedroom (0.26) yields, assuming mostly small units
  (**Analysis**).
- Stephens Creek low = Table 4.1's 0.265 K-5 per 2+ BR unit (5+ years old) × 105 units; high = Table 2.6 affordable
  yields by bedroom count × K-5 share (0.265/0.516 from Table 4.1).
- Capture: 262 of the 354 PPS elementary students living in the Hayhurst neighborhood attended Hayhurst in Oct 2025
  (74%); 60 (17%) attended PPS alternative/focus programs
  [PPS:pps_net/data-and-reporting/2025-26/neighborhood_capture_rate_metrics.pdf p.1]. **Analysis:** applying the
  Hayhurst-wide rate to this area is an assumption; capture at Stephens Creek could differ.

For scale: Hayhurst enrolled 290 in Oct 2025 [BB:3997157 p.1], so the shift area is roughly a fifth to three tenths of
the school.

## 4. Cross-check: what PPS's own projections imply

PPS's 2027-28 projections [PPS:pps_net/rightsizing/school_impact/hayhurst.pdf p.4]
[PPS:pps_net/rightsizing/school_impact/rieke.pdf p.4] [PPS:pps_net/rightsizing/school_impact/maplewood.pdf p.4]:

| School | Status quo | Scenario A/B | Change | Poverty SQ → A/B |
|---|---|---|---|---|
| Rieke | 252 | 348 | +96 (Maplewood share + Hayhurst area) | 15.2% → 24.0% |
| Hayhurst | 274 | 472 | +198 (Maplewood share − Hayhurst area) | 26.2% → 15.5% |
| Maplewood | 278 | closed | | 19.5% |

**Analysis:**
- The two gains sum to 294, close to Maplewood's 278 (the difference is plausibly students returning from focus
  options), so the arithmetic is internally consistent.
- Rieke's poverty count rises from about 38 to about 84 students (+45 of the 96 added). Maplewood movers, at the
  implied ~16% poverty rate, cannot supply that. If H is the number of Hayhurst-area students moved, their poverty rate
  is (45.2 − 0.158 × (96 − H)) / H, which stays at or below 100% only if **H ≥ ~36**. At a 55–75% poverty rate, which
  is plausible for an area with public housing, H ≈ 50–80. The same calculation on the "underserved racial groups"
  column gives H ≥ ~29.
- It follows that Rieke receives only about 16–60 Maplewood students, so "30% of Maplewood" must refer to share of
  area, not share of students.
- The bottom-up estimate (51–90 at Hayhurst) and the projection-implied range (≥36, likely 50–80) come from
  independent data and agree.

## 5. Caveats and open questions

- PPS has published no student count for the Hayhurst → Rieke area; a records request for the 2027-28 projection by
  attendance-area piece (and current residents by grade) would replace these estimates.
- Assessor unit counts are unreliable for several older apartment buildings (ranges in §2).
- PSU yields are tri-county averages (Table 2.6 is from buildings under five years old); this area's older housing
  could differ.
- Not counted: any new construction after the Oct 22, 2026 pull. Director Splitt's comments on a large housing
  development missing from Hayhurst's numbers [YT:zOUH2Jq7Owo@3:47:40] do not appear to concern this area: the
  largest vacant parcel inside it is about 0.65 acres (**Analysis**, from the parcel CSV).

Sources outside `pps_net/`: Portland Maps ArcGIS REST, `Public/Taxlots/MapServer/0` and `Public/BDS_Address/MapServer/0`
(https://www.portlandmaps.com/arcgis/rest/services/Public); Home Forward, https://www.homeforward.org/stephens-creek-crossing/.
