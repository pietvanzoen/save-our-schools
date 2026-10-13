# Staffing workbook: "Board Request as of 9/22" (Sept 2026)

This is a PPS staff spreadsheet of 2026-27 enrollment and staffing. It appears to be the "large spreadsheet" staff gave the
Board in answer to a 9/21/26 rightsizing question in the Oct 1, 2026 Q&A tracker [BB:14493920 p.35]. The repository owner
supplied it on 2026-10-13 as an Excel export of a Google Sheets copy. Provenance details and a checksum are in `_manifest.json`.

| # | Tab | What it holds |
|---|---|---|
| 00 | School Detail wo ESL or SPED or M98 or T1 *(hidden)* | Every school (K-5, K-8, MS, HS): Title I, direct-certification and underserved shares, **student count for staffing** for 2025-26 and 2026-27, and FTE under three staffing runs (2025-26; "26-27 Enrollment Only Dec30"; "26-27 Reduction Simulation 2"), with changes |
| 01 | **26-27 As of 9/23 Counts** | K-8 grades at 58 elementary, K-8 and program schools (grades 6-8 at K-8s only): one row per school × program/co-located × grade, giving unit (blend), blend applied, initial sections, **Enrollment Count** (the Sept 2026 actual) and **Projected Enrollment** (the spring staffing projection) |
| 02 | 6-8 Course Loads 26-27 | Middle-grade sections by school and course with students per period (no names) |
| 03 | School detail for ISR | 2026-27 staffing count and FTE by role (homeroom, PE, arts, counselor, librarian, ...) per school |
| 04–10 | Resolve, Sheet12, M98, ELD, SPED, ELD Summary, Title 1 Gen Fund Analysis *(mostly hidden)* | Kindergarten EA analysis, SPED/HIT models, Measure 98 staffing, ELD staffing (with fall ELD counts), SPED allocations, Title I analysis |
| 11 | Readme *(hidden)* | A link to a Google Doc (not archived) |

`tabs/` holds a CSV dump of each tab. In the Counts tab, "Enrollment Count" is the September count and "Projected
Enrollment" equals the "Total Student Count for Staffing" used to allocate staff in the spring: the two match school by
school in the ISR tab (e.g. Maplewood 300).

Cite as `[PPS:staffing/2026-09-22_board-request/board_request_as_of_2026-09-22.xlsx#<tab>!R<row>]`.
Per-school and per-grade tables: `analysis/data/enrollment_2026-27_sept_by_school.csv` and `..._by_grade.csv`
(`python3 tools/staffing_workbook_2026.py` rebuilds them).
