# Odyssey's move from East Sylvan to MLC: how many Southwest students would return to neighborhood schools

Compiled 2026-10-22.

Data:
- [`data/odyssey_move_sw_estimate.csv`](../data/odyssey_move_sw_estimate.csv): per neighborhood.
- [`data/school_drive_distances_odyssey.csv`](../data/school_drive_distances_odyssey.csv): drive distances for 61 schools.

**Bottom line (Analysis).**
- About 123 Odyssey students live in Southwest neighborhoods whose drive gets longer under the move. These are Bridlemile, Hayhurst, Maplewood, Rieke and Forest Park (K-5), plus Gray and West Sylvan (6-8).
- The drive roughly doubles for Hayhurst (3.8 → 7.5 mi) and Maplewood (4.0 → 7.8 mi).
- **Neighborhood schools.** A distance model puts the number of SW elementary students who would shift back to neighborhood schools at about 17 (range 7–33), net of small gains for Markham and Capitol Hill.
- **Hayhurst.** If Maplewood closes, about 11 (5–23) of these would land at Hayhurst.
- **What PPS assumes.** PPS projects Odyssey's enrollment as flat after the move (220 → 224), which implies no families leave because of it [PPS:pps_net/rightsizing/school_impact/odyssey.pdf p.4](https://drive.google.com/open?id=1cUaUTKyIFWmWzTghepiA3Ib6rEdVJIx0&usp=drive_copy).

## What PPS proposes
- Odyssey K-8 "would move to the Metropolitan Learning Center (MLC) school. The East Sylvan building would close." [PPS:pps_net/rightsizing/school_impact/odyssey.pdf p.3](https://drive.google.com/open?id=1cUaUTKyIFWmWzTghepiA3Ib6rEdVJIx0&usp=drive_copy)
- Timing: fall 2027 or fall 2028 [PPS:pps_net/rightsizing/school_impact/odyssey.pdf p.3](https://drive.google.com/open?id=1cUaUTKyIFWmWzTghepiA3Ib6rEdVJIx0&usp=drive_copy).
- East Sylvan is at 1849 SW 58th Ave and MLC is at 2033 NW Glisan St (PPS budget school pages).

## Where Odyssey students live
In October 2025, 217 students attended Odyssey [PPS:pps_net/data-and-reporting/2025-26/distribution_charters_focus_options.pdf p.12](https://www.pps.net/fs/resource-manager/view/d52c1154-4c1d-4291-babf-3ce04902b791#page=12):
- K-5, by home neighborhood: Hayhurst 26, Bridlemile 24, Markham 24, Maplewood 18, Rieke 13, Capitol Hill 6, Chapman 6, Forest Park 6.
- 6-8, by home neighborhood: Jackson 35, Gray 19, West Sylvan 17.

The October 2024 figures are similar [PPS:pps_net/data-and-reporting/2024-25/distribution_charters_focus_options.pdf p.11](https://www.pps.net/fs/resource-manager/view/238a092d-f746-4241-9e84-b043ad665f3b#page=11).

## How Odyssey's draw falls with distance
Share of resident PPS students attending Odyssey, by drive distance from the neighborhood school to East Sylvan. This covers elementary and K-8 neighborhoods, with Oct 2024 and Oct 2025 pooled. Residents come from [PPS:pps_net/data-and-reporting/2025-26/neighborhood_capture_rate_metrics.pdf p.1](https://www.pps.net/fs/resource-manager/view/d65fc69c-e9b5-4c13-8199-545d12deb541#page=1) and the 2024-25 edition.

| Drive to East Sylvan | Neighborhoods | Odyssey students | Resident students | Share |
|---|---|---|---|---|
| under 3.5 mi | 2 | 50 | 1,798 | 2.8% |
| 3.5–4.5 mi | 3 | 97 | 1,999 | 4.9% |
| 4.5–6 mi | 5 | 49 | 3,370 | 1.5% |
| 6–8 mi | 12 | 4 | 9,016 | 0.04% |
| 8–11 mi | 24 | 74 | 18,474 | 0.4% |
| 11+ mi | 6 | 1 | 3,975 | 0.03% |

Analysis:
- Districtwide, the share drops sharply beyond about 6 miles. Hayhurst and Maplewood move from about 4 miles to about 7.5–7.8 miles.
- Much of this pattern is east side versus west side, though, not distance as such.
- Within the west side, the relationship is weak. Markham, about 9.4 mi away by the I-5 route, sends 24 students. Ainsworth, about 3 mi away, sends 2.

## Method (Analysis)
- **Drive distances.** These come from the OSRM routing service on OpenStreetMap, run 2026-10-22. They go from each neighborhood school's address (a proxy for the neighborhood) to each site.
- **Times are free-flow.** Peak-hour trips into NW Portland via US-26 and I-405 will take longer.
- **Model.** A negative-binomial regression of Odyssey students on log drive distance, with log residents as offset, fitted to all 2024 and 2025 neighborhoods.
- **Elasticity range used:**

  | Case | Elasticity | Model behind it |
  |---|---|---|
  | Low | −0.23 | west-side neighborhoods only (not significant) |
  | Central | −0.65 (SE 0.25) | all neighborhoods, with a west-side indicator |
  | High | −1.87 | all neighborhoods, no indicator (overstates, because it mixes in the east/west difference) |

- **Projection.** Each neighborhood's expected Odyssey count after the move is today's count × (MLC distance / East Sylvan distance)^elasticity.
- **Where leavers go.** Leavers return to their neighborhood school at the rate that neighborhood's other PPS students attend it, which is 75–91%. The rest are assumed to go elsewhere, including other options or leaving PPS.
- **Not modeled:**
  - current Odyssey families who stay through 8th grade, which spreads the change over several years;
  - backfilling of Odyssey seats by NW and inner-city families, for whom MLC is closer. This is consistent with PPS's flat projection.

## Results (central, with low–high range)

| Neighborhood | Odyssey (Oct 2025) | Drive to East Sylvan → MLC | Leave Odyssey | Back to neighborhood school |
|---|---|---|---|---|
| Hayhurst (K-5) | 26 | 3.8 → 7.5 mi (10 → 17 min) | 9 (4–19) | 7 (3–15) |
| Maplewood (K-5) | 18 | 4.0 → 7.8 mi (11 → 16 min) | 6 (3–13) | 6 (2–11) |
| Bridlemile (K-5) | 24 | 2.9 → 4.1 mi (8 → 14 min) | 5 (2–11) | 4 (2–10) |
| Rieke (K-5) | 13 | 5.1 → 6.3 mi | 2 (1–4) | 1.5 (0.5–4) |
| Forest Park (K-5) | 6 | 4.2 → 6.3 mi | 1 (0.5–3) | 1 (0.5–3) |
| Markham (K-5) | 24 | 9.4 → 7.9 mi | −3 (gain) | −2 |
| Capitol Hill (K-5) | 6 | 8.2 → 6.7 mi | −1 (gain) | −1 |
| West Sylvan (6-8) | 17 | 1.7 → 5.3 mi | 9 (4–15) | 8 (3–13) |
| Gray (6-8) | 19 | 4.7 → 6.7 mi | 4 (2–9) | 3 (1–8) |
| Jackson (6-8) | 35 | 9.7 → 8.2 mi | −4 (gain) | −4 |

**If Maplewood closes,** its returning students split between Hayhurst (70%) and Rieke (30%). That puts about 11 (5–23) at Hayhurst. None of this is in Hayhurst's projection of 472 for 2027-28 [PPS:pps_net/rightsizing/school_impact/hayhurst.pdf p.4](https://drive.google.com/open?id=1BwsMTqcVksEx0je_XtPcti9pgFLBE_TP&usp=drive_copy).

## Alternative used in the Maplewood email: half of families leave when the drive doubles (Analysis)
This scenario sets the elasticity so that 50% of Hayhurst and Maplewood Odyssey families leave: (7.5/3.8 ≈ 7.8/4.0 ≈ 1.95)^b = 0.5, which gives b ≈ −1.03. The same b is then applied to every neighborhood.

| Neighborhood | Leave Odyssey | Back to neighborhood school |
|---|---|---|
| Hayhurst | 13.1 | 10.5 |
| Maplewood | 8.9 | 7.8 |
| Bridlemile | 7.2 | 6.3 |
| Rieke | 2.5 | 2.2 |
| Forest Park | 2.0 | 1.8 |
| Markham / Capitol Hill / Stephenson (closer) | −6.3 | −4.7 |
| **SW K-5, net** | | **≈ 24** |
| Gray + West Sylvan (6-8) | 17.5 | 15.1 |

**Hayhurst, if Maplewood closes:** 10.5 + 70% × 7.8 ≈ **16**.
