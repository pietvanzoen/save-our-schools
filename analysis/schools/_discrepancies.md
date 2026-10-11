# Discrepancies: per-school PDFs vs earlier rightsizing analysis

Compares the 82 PPS per-school family guides (`sources/pps_net/rightsizing/school_impact/*.pdf`, fetched 2026-10-11) with `analysis/data/rightsizing_scenarios.csv` and `analysis/topics/rightsizing.md` (as of 2026-10-10).
Part 1 lists conflicts, ambiguities and superseded statements. Part 2 logs every change made to `rightsizing_scenarios.csv`. The CSV was corrected only where a per-school PDF is unambiguous. Each changed row's `source` column now ends with "; per-school PDF [PPS:...]". The topic file was not edited.

Citations: `[PPS:pps_net/rightsizing/school_impact/<file> p.N]`, where p.3 is the school proposal page and p.4 is the enrollment/programs/maps page. Pages 1–2 are a shared glossary.

## Part 1: Conflicts, ambiguities and superseded statements

### D01. Rigler: neighborhood boundary
Schools: [rigler](rigler.md), [scott](scott.md)

The Rigler PDF text says "Rigler’s non-DLI neighborhood boundary would shift to Scott K-5" and calls Rigler "a focused regional Spanish DLI K-5 school" [PPS:pps_net/rightsizing/school_impact/rigler.pdf p.3]. But the same PDF's measures table keeps "K-5 neighborhood/language immersion" with type of change "Programs joining", and projected enrollment rises from 321 to 505 (2031-32), roughly the size of the incoming Scott DLI program [PPS:pps_net/rightsizing/school_impact/rigler.pdf p.4]. The Scott PDF does not mention receiving any Rigler area, and Scott's Scenario B projection falls to 301 [PPS:pps_net/rightsizing/school_impact/scott.pdf p.4]. The CSV row ("receive program") was left unchanged.

**Resolution:** Not applied (ambiguous). Check against the NE boundary maps [BB:14505794]–[BB:14505805] or ask PPS.

### D02. Marysville: where students go
Schools: [marysville](marysville.md), [arleta](arleta.md), [kelly](kelly.md)

The Marysville PDF splits the area: "The pre-SEGC neighborhood K-5 school boundary would move to Arleta K-5, the pre-SEGC Lent neighborhood non-DLI boundary would move to Kelly" [PPS:pps_net/rightsizing/school_impact/marysville.pdf p.3], and the Kelly PDF agrees [PPS:pps_net/rightsizing/school_impact/kelly.pdf p.3]. The Arleta PDF says Arleta "would welcome the entire neighborhood school area and student body from Marysville" [PPS:pps_net/rightsizing/school_impact/arleta.pdf p.3].

**Resolution:** CSV updated to the split (C19), because two PDFs and the Oct 6 deck [BB:14511742 p.43] agree. The Arleta wording is logged here.

### D03. Markham in Scenario B: K-2 Intensive Skills Classroom
Schools: [markham](markham.md), [maplewood](maplewood.md)

Maplewood closes in both scenarios and its "K-2 Intensive Skills Classroom would move to Markham K-5" [PPS:pps_net/rightsizing/school_impact/maplewood.pdf p.3]. The Markham PDF's measures table nevertheless says "No changes proposed" for Option B [PPS:pps_net/rightsizing/school_impact/markham.pdf p.4].

**Resolution:** CSV Markham B left as "no change"; school_impact.csv records the ISC move for B as a special-education change.

### D04. Woodstock in Scenario B: Lewis CB classrooms
Schools: [woodstock](woodstock.md), [lewis](lewis.md)

The Woodstock PDF (labeled Options A and B) says "The Communication Behavior Classrooms currently located at Lewis Elementary School will be relocated to Woodstock" [PPS:pps_net/rightsizing/school_impact/woodstock.pdf p.3]. Lewis closes only in Scenario A [PPS:pps_net/rightsizing/school_impact/lewis.pdf p.3].

**Resolution:** Applied to Woodstock A only (C35). Whether the move also happens under B is unclear.

### D05. Robert Gray: size goal
Schools: [gray](gray.md)

The Gray narrative says receiving Maplewood "brings Gray above 500 students" [PPS:pps_net/rightsizing/school_impact/gray.pdf p.3]. Its own table shows 481 / 518 / 551 / 508 / 490 for 2027-28 to 2031-32, with "Meets school size goal? No" [PPS:pps_net/rightsizing/school_impact/gray.pdf p.4].

**Resolution:** PDF internal inconsistency: true only for 2028-29 to 2030-31. No CSV change.

### D06. Vernon: seismic scope
Schools: [vernon](vernon.md)

The Vernon PDF says "Vernon received a full seismic retrofit in Summer 2026" [PPS:pps_net/rightsizing/school_impact/vernon.pdf p.3]. `analysis/data/seismic_facilities.csv` records a "Targeted retrofit: Bldg A2 east gym wall (URM)", Summer 2026, citing [BB:3990267 p.17].

**Resolution:** Not changed (seismic CSV outside this task). The bond documents describe a targeted scope, so the family guide's "full" is probably loose wording.

### D07. Capacity figures
Schools: [marysville](marysville.md), [whitman](whitman.md)

The PDFs give Marysville's "space of 410" [PPS:pps_net/rightsizing/school_impact/marysville.pdf p.3] and say Whitman "has room for 416 students" [PPS:pps_net/rightsizing/school_impact/whitman.pdf p.3]. The April 20 table used in the CSV gives functional capacity 459 (Marysville) and 442 (Whitman) [BB:3997157 p.1]. Other capacities stated in PDFs match the table: Abernethy 441, Arleta 653, Boise-Eliot/Humboldt 632, MLK Jr. 618, Maplewood 465.

**Resolution:** Not changed. The two sources may use different capacity definitions.

### D08. Title I: expected vs 2025-26
Schools: [arleta](arleta.md), [atkinson](atkinson.md), [roosevelt](roosevelt.md)

The CSV marks Arleta, Atkinson and Roosevelt HS as Title I in 2025-26. Each PDF shows the "expected designation" as "No" even with no changes [PPS:pps_net/rightsizing/school_impact/arleta.pdf p.4] [PPS:pps_net/rightsizing/school_impact/atkinson.pdf p.4] [PPS:pps_net/rightsizing/school_impact/roosevelt.pdf p.4].

**Resolution:** Not changed. The two describe different years (current vs projected designation).

### D09. Sunnyside: size goal label
Schools: [sunnyside](sunnyside.md)

The Sunnyside snapshot lists the size goal as "More than 360 students (general district goal)" while the school is currently K-8 (goal 500) [PPS:pps_net/rightsizing/school_impact/sunnyside.pdf p.3]. Its status-quo projection of 475 is marked "No".

**Resolution:** PDF internal inconsistency; no change.

### D10. MLC enrollment includes Odyssey
Schools: [metropolitan-learning-center](metropolitan-learning-center.md), [odyssey](odyssey.md)

The MLC Scenario A/B projection (386 → 341) is labelled "Enrollment shows Odyssey and MLC for facility purposes" [PPS:pps_net/rightsizing/school_impact/metropolitan_learning_center.pdf p.4]. Odyssey's own PDF shows 220 → 224 for both scenarios [PPS:pps_net/rightsizing/school_impact/odyssey.pdf p.4].

**Resolution:** In school_impact.csv the MLC A/B rows carry the combined figure and a note. Do not add MLC and Odyssey together.

### D11. Rose City Park Option A prints zeros
Schools: [rose-city-park](rose-city-park.md)

The Rose City Park enrollment table prints "0" for every year under Option A rather than "School would close" [PPS:pps_net/rightsizing/school_impact/rose_city_park.pdf p.4].

**Resolution:** Recorded as 0 with a note.

### D12. Lewis Option B "74.2" lacks a % sign
Schools: [lewis](lewis.md)

Students living within 1 mile, Option B, is printed as "74.2" [PPS:pps_net/rightsizing/school_impact/lewis.pdf p.4].

**Resolution:** Recorded as printed.

### D13. Typos in the PDFs
Schools: [irvington](irvington.md), [faubion](faubion.md), [peninsula](peninsula.md)

Irvington: "Middle grade (6th-8th) students would from move Tubman to Beaumont" [PPS:pps_net/rightsizing/school_impact/irvington.pdf p.3]. Faubion: "Faubitoo large" [PPS:pps_net/rightsizing/school_impact/faubion.pdf p.3]. Peninsula: "updated an building" [PPS:pps_net/rightsizing/school_impact/peninsula.pdf p.3].

**Resolution:** Kept verbatim in the page quotes.

### D14. Document versions
Schools: [ockley-green](ockley-green.md), [scott](scott.md), [sunnyside](sunnyside.md)

Three PDFs carry a footer "Version 1.12 10082026" (Ockley Green, Scott, Sunnyside) [PPS:pps_net/rightsizing/school_impact/ockley_green.pdf p.4] [PPS:pps_net/rightsizing/school_impact/scott.pdf p.4] [PPS:pps_net/rightsizing/school_impact/sunnyside.pdf p.4]. The others carry no version stamp.

**Resolution:** Analysis: these three were probably revised on 10/08/2026, after the 10/05 release. Re-fetch periodically.

### D15. Harrison Park region
Schools: [harrison-park](harrison-park.md)

The CSV places Harrison Park MS in "Grant/McDaniel (NE)", because it appeared on the Grant/McDaniel feeder slide. The PDFs tie its changes to SE schools (Lent, Kelly, Atkinson, Bridger) and the deck shows it as a split feeder to Franklin, Cleveland and McDaniel [BB:14511742 p.39].

**Resolution:** Region left as is (the PDFs do not assign regions). Analysis: grouping it with Cleveland/Franklin (SE) would match the PDFs better.

### D16. Thresholds stated at the Oct 6 meeting

The meeting notes record Franco giving the high-school threshold as "1,000 (HS)" [YT:zOUH2Jq7Owo@1:37:33] (analysis/meetings/2026-10-06_zOUH2Jq7Owo.md). Every PDF says "More than 1,100" for high schools [PPS:pps_net/rightsizing/school_impact/abernethy.pdf p.2].

**Resolution:** The documents consistently use 1,100. Re-check the caption.

### D17. Clark size after DLI leaves
Schools: [clark](clark.md)

The Oct 6 meeting notes record Engelsman saying Clark falls "to about 214 non-DLI students" (analysis/meetings/2026-10-06_zOUH2Jq7Owo.md). The Clark PDF projects 276 (2027-28) to 272 (2031-32) under A and B [PPS:pps_net/rightsizing/school_impact/clark.pdf p.4].

**Resolution:** Unreconciled. Engelsman may have used current non-DLI counts.

### D18. rightsizing.md §1 / §4.4: "per-school projections not published"

rightsizing.md says per-school projected 2031-32 enrollments under each scenario are "not in the released documents", and §4.4 says PPS has not published per-school projections. The per-school PDFs now give 2027-28 to 2031-32 projections for status quo, A and B. Of the closing schools that are currently above threshold: James John is projected at 352 by 2031-32, below 360, and its closure is attributed to "structural building limits and multi-story accessibility challenges" [PPS:pps_net/rightsizing/school_impact/james_john.pdf p.3] [PPS:pps_net/rightsizing/school_impact/james_john.pdf p.4]. Rose City Park stays above threshold (370) and closes for building condition ("Severe building conditions were the primary reason") [PPS:pps_net/rightsizing/school_impact/rose_city_park.pdf p.3] [PPS:pps_net/rightsizing/school_impact/rose_city_park.pdf p.4]. Sellwood falls to 350 by 2031-32 and closes for building systems ("entire mechanical system replacement") [PPS:pps_net/rightsizing/school_impact/sellwood.pdf p.3] [PPS:pps_net/rightsizing/school_impact/sellwood.pdf p.4].

**Resolution:** Topic file not edited (outside this task). Superseded statements are flagged here.

### D19. rightsizing.md §4.2: Scenario B "65 remaining open"

The district summary prints 65 schools/programs remaining under B [BB:14505788 p.2]. In the per-school PDFs, 68 schools/programs still have an open-school column under A and 71 under B, i.e. 82 − 14 and 82 − 11 (school_impact.csv).

**Resolution:** Supports the analysis in rightsizing.md that 65 is a misprint; 71 is consistent with the PDFs.

### D20. District KPIs recomputed from the PDFs

Using each PDF's "Meets school size goal?" and 2031-32 projections: status quo 21 of 82 schools meet the goal (26%) with 48% of students; A 45 of 68 (66%), 79% of students; B 41 of 71 (58%), 74% of students. The district summary reports 26%/48%, 67%/80% and 57%/73% [BB:14505788 p.1].

**Resolution:** Analysis: within about one point. The small gaps are probably rounding or the treatment of programs such as ACCESS and Odyssey.

### D21. Implementation timing not in rightsizing.md / CSV
Schools: [marysville](marysville.md), [sellwood](sellwood.md), [metropolitan-learning-center](metropolitan-learning-center.md), [odyssey](odyssey.md), [beverly-cleary](beverly-cleary.md), [irvington](irvington.md), [arleta](arleta.md), [brentwood](brentwood.md), [hosford](hosford.md)

The PDFs show phased timing. Marysville is open in 2027-28 and closed from 2028-29 ("Delaying full implementation") [PPS:pps_net/rightsizing/school_impact/marysville.pdf p.3] [PPS:pps_net/rightsizing/school_impact/marysville.pdf p.4]. Sellwood closes "in 2028" (523 students projected in 2027-28) [PPS:pps_net/rightsizing/school_impact/sellwood.pdf p.3]. MLC 9-12 students move Fall 2027 [PPS:pps_net/rightsizing/school_impact/metropolitan_learning_center.pdf p.3]. Odyssey moves in fall 2027 or fall 2028 [PPS:pps_net/rightsizing/school_impact/odyssey.pdf p.3]. Beverly Cleary 6-8 moves to Beaumont in Fall 2027, with seismic work finishing summer 2028 and Irvington as a possible swing site [PPS:pps_net/rightsizing/school_impact/beverly_cleary.pdf p.3] [PPS:pps_net/rightsizing/school_impact/irvington.pdf p.3]. Arleta, Brentwood and Hosford projections jump in 2028-29 [PPS:pps_net/rightsizing/school_impact/arleta.pdf p.4] [PPS:pps_net/rightsizing/school_impact/brentwood.pdf p.4] [PPS:pps_net/rightsizing/school_impact/hosford.pdf p.4].

**Resolution:** CSV action_detail updated (C19–C21, C29–C32). rightsizing.md lists only "implementation start 2027-28"; flagged here.

### D22. Spanish DLI hubs
Schools: [kellogg](kellogg.md), [west-sylvan](west-sylvan.md), [ainsworth](ainsworth.md)

rightsizing.md §6.3 lists Spanish DLI consolidation at "Chávez, George, Lent, Rigler and Roseway Heights". The Kellogg PDF adds "All Spanish Immersion in the southeast remains at Kellogg" [PPS:pps_net/rightsizing/school_impact/kellogg.pdf p.3]. Ainsworth (K-5) [PPS:pps_net/rightsizing/school_impact/ainsworth.pdf p.3] and West Sylvan (MS) [PPS:pps_net/rightsizing/school_impact/west_sylvan.pdf p.3] keep the West-side Spanish DLI.

**Resolution:** Topic list is incomplete for middle grades and the West side; not edited.

### D23. Mt. Tabor high-school feeder
Schools: [mt-tabor](mt-tabor.md), [laurelhurst](laurelhurst.md)

rightsizing.md §4.3 reads the deck as making Mt. Tabor a split feeder to Grant and Cleveland. The Laurelhurst and Mt. Tabor PDFs speak only of a path "directly" to Grant HS [PPS:pps_net/rightsizing/school_impact/laurelhurst.pdf p.3] [PPS:pps_net/rightsizing/school_impact/mt_tabor.pdf p.3].

**Resolution:** Not contradictory, but the PDFs do not confirm the Cleveland split. Check the 6-8 boundary maps.

### D24. Kelly middle-school pathway
Schools: [kelly](kelly.md), [brentwood](brentwood.md), [harrison-park](harrison-park.md)

The CSV/deck note "Kelly is a boundary feeder to Harrison Park" [BB:14511742 p.39]. The PDFs make clear this is a change: Kelly neighborhood middle schoolers "would shift to Harrison Park" from Brentwood, while Russian DLI students stay on the Brentwood path [PPS:pps_net/rightsizing/school_impact/kelly.pdf p.3] [PPS:pps_net/rightsizing/school_impact/brentwood.pdf p.3].

**Resolution:** CSV updated (C10, C11).

### D25. Facts the PDFs add that are not in rightsizing.md
Schools: [buckman](buckman.md), [creston](creston.md), [astor](astor.md), [faubion](faubion.md), [jefferson](jefferson.md), [sunnyside](sunnyside.md), [bridger-creative-science](bridger-creative-science.md), [harriet-tubman](harriet-tubman.md), [george](george.md), [hayhurst](hayhurst.md), [rieke](rieke.md), [skyline](skyline.md), [lincoln](lincoln.md), [roosevelt](roosevelt.md)

The PDFs add these specifics. Buckman's Arts focus program closes and the split line is Burnside/Hawthorne [PPS:pps_net/rightsizing/school_impact/buckman.pdf p.3]. The Creston Annex preschool stays open. The Bybee Lake Shelter area moves from Faubion to Astor and from Jefferson to Roosevelt. Sunnyside's high-school path moves from Franklin to Cleveland, and the Sunnyside area moves to Cleveland HS. A small Vestal section moves from Franklin to McDaniel. Current Bridger 6th/7th graders may return to their neighborhood middle school. Current Irvington-area students may stay at Tubman through 8th grade. Peninsula-area middle graders move from Ockley Green to George. Part of the Hayhurst boundary moves to Rieke. Sibling preference applies at Jackson and Gray. Special-education classroom moves are listed school by school (SES, CB, ISC, DHH).

**Resolution:** CSV updated where unambiguous (C01–C39).

### D26. Transportation and cost

No per-school PDF contains a cost, savings or transportation number. Transportation appears only as something to be evaluated in "site walk-throughs to evaluate programmatic readiness, space, transportation, and ADA accessibility" (e.g. [PPS:pps_net/rightsizing/school_impact/glencoe.pdf p.3]), plus qualitative claims about shorter trips for Skyline/Lincoln/Roosevelt [PPS:pps_net/rightsizing/school_impact/skyline.pdf p.3] [PPS:pps_net/rightsizing/school_impact/roosevelt.pdf p.3] and for Llewellyn/Duniway [PPS:pps_net/rightsizing/school_impact/llewellyn.pdf p.3].

**Resolution:** Consistent with rightsizing.md §4.6 (no cost or ride-time estimates).

## Part 2: Corrections applied to `analysis/data/rightsizing_scenarios.csv`

39 corrections, 71 rows (A and B rows counted separately). "before" is the value before this pass.

### C01. Kellogg MS (A and B)
CSV said "Listed among boundary changes; specifics not described"; PDF gives the specifics. Evidence: [PPS:pps_net/rightsizing/school_impact/kellogg.pdf p.3]

- `proposed_action`: before: "boundary change" → after: "receive students; boundary change"
- `action_detail`: before: "Listed among boundary changes; specifics not described" → after: "Per-school PDF: boundary expands to take Atkinson and Creston neighborhood students; Lent neighborhood students shift from Kellogg to Harrison Park MS; "All Spanish Immersion in the southeast remains at Kellogg"; all Kellogg-boundary students feed Franklin HS"
- `receiving_schools`: before: "" → after: "Harrison Park MS (Lent area)"
- `sending_schools`: before: "" → after: "Atkinson (neighborhood area); Creston (neighborhood area)"

### C02. Cleveland HS (A and B)
CSV said "specifics not described"; PDF gives the specifics. Evidence: [PPS:pps_net/rightsizing/school_impact/cleveland.pdf p.3] [PPS:pps_net/rightsizing/school_impact/franklin.pdf p.3] [PPS:pps_net/rightsizing/school_impact/sunnyside.pdf p.3]

- `action_detail`: before: "Listed among boundary changes; specifics not described" → after: "Per-school PDF: boundary expands to include the Sunnyside school area; remaining sections of Woodmere and Whitman move to Franklin; current Cleveland/Franklin students may stay through graduation"
- `receiving_schools`: before: "" → after: "Franklin HS (remaining Woodmere/Whitman sections)"
- `sending_schools`: before: "" → after: "Franklin HS (Sunnyside area)"

### C03. Franklin HS (A and B)
CSV said "specifics not described"; PDF gives the specifics. Evidence: [PPS:pps_net/rightsizing/school_impact/franklin.pdf p.3]

- `action_detail`: before: "Listed among boundary changes; specifics not described" → after: "Per-school PDF: boundary adjusts to welcome the expanded Whitman area (former Whitman and Woodmere boundaries); full Sunnyside boundary shifts to Cleveland; a small section of the Vestal boundary moves to McDaniel; current students may stay through graduation, with sibling preferences"
- `receiving_schools`: before: "" → after: "Cleveland HS (Sunnyside area); McDaniel HS (small Vestal section)"
- `sending_schools`: before: "" → after: "Cleveland HS (remaining Whitman/Woodmere sections)"

### C04. McDaniel HS (A and B)
CSV said "specifics not described in memo"; PDF gives the specifics. Evidence: [PPS:pps_net/rightsizing/school_impact/mcdaniel.pdf p.3]

- `action_detail`: before: "Listed among attendance boundary changes; specifics not described in memo" → after: "Per-school PDF: receives a small portion of the Vestal boundary (shifting from Franklin)"
- `sending_schools`: before: "" → after: "Franklin HS (small section of Vestal boundary)"

### C05. Jefferson HS (A and B)
CSV said "specifics not described in memo"; PDF gives the specifics. Evidence: [PPS:pps_net/rightsizing/school_impact/jefferson.pdf p.3]

- `action_detail`: before: "Listed among attendance boundary changes; specifics not described in memo" → after: "Per-school PDF: minor boundary adjustment shifting the Bybee Lake Shelter area to Roosevelt HS (matching the shelter area's move from Faubion to Astor K-8)"
- `receiving_schools`: before: "" → after: "Roosevelt HS (Bybee Lake Shelter area)"

### C06. Roosevelt HS (A and B)
Adds the Bybee Lake Shelter area named in the Jefferson PDF. Evidence: [PPS:pps_net/rightsizing/school_impact/roosevelt.pdf p.3] [PPS:pps_net/rightsizing/school_impact/jefferson.pdf p.3]

- `action_detail`: before: "Listed among boundary changes; gains Skyline K-8 high school assignment from Lincoln" → after: "Listed among boundary changes; gains Skyline K-8 high school assignment from Lincoln; Per-school PDF also: Jefferson PDF shifts the Bybee Lake Shelter area to Roosevelt"
- `sending_schools`: before: "Skyline (HS assignment)" → after: "Skyline (HS assignment, from Lincoln); Jefferson HS (Bybee Lake Shelter area)"

### C07. Astor (A and B)
CSV said "specific change not described in memo"; PDF gives the specifics. Evidence: [PPS:pps_net/rightsizing/school_impact/astor.pdf p.3] [PPS:pps_net/rightsizing/school_impact/faubion.pdf p.3]

- `action_detail`: before: "Listed among attendance boundary changes; specific change not described in memo" → after: "Per-school PDF: stays K-8; boundary expands slightly to include students living near the Bybee Lake Shelter area (moved from Faubion); stays K-8 because nearby middle schools lack room"
- `sending_schools`: before: "" → after: "Faubion (Bybee Lake Shelter area)"

### C08. Faubion (A and B)
Adds the Bybee Lake Shelter boundary change behind Faubion's "boundary change" label. Evidence: [PPS:pps_net/rightsizing/school_impact/faubion.pdf p.3]

- `action_detail`: before: "Becomes K-5; grades 6-8 to Ockley Green MS" → after: "Becomes K-5; grades 6-8 to Ockley Green MS; Per-school PDF: Bybee Lake Shelter school area moves from Faubion to Astor"
- `receiving_schools`: before: "Ockley Green MS (6-8)" → after: "Ockley Green MS (6-8); Astor (Bybee Lake Shelter area)"

### C09. Harrison Park MS (A and B)
CSV named only Bridger 6-8; PDFs add Lent and Kelly areas in and Atkinson area out. Evidence: [PPS:pps_net/rightsizing/school_impact/harrison_park.pdf p.3] [PPS:pps_net/rightsizing/school_impact/bridger_creative_science.pdf p.3] [PPS:pps_net/rightsizing/school_impact/kellogg.pdf p.3] [PPS:pps_net/rightsizing/school_impact/brentwood.pdf p.3]

- `action_detail`: before: "Receives Bridger Creative Science grades 6-8; listed among Grant/McDaniel boundary changes; Deck feeder slide: split feeder to Franklin, Cleveland and McDaniel" → after: "Per-school PDF: boundary expands to welcome elementary graduates from the Lent and Kelly school areas; Atkinson neighborhood students shift to Kellogg; keeps Mandarin DLI. Bridger PDF: current Bridger 6th/7th graders reassigned to Harrison Park or may return to their neighborhood MS. Deck feeder slide: split feeder to Franklin, Cleveland and McDaniel"
- `receiving_schools`: before: "" → after: "Kellogg MS (Atkinson area)"
- `sending_schools`: before: "Bridger Creative Science (6-8)" → after: "Bridger Creative Science (6-8); Kellogg MS (Lent area); Brentwood MS (Kelly area)"

### C10. Kelly (A and B)
CSV had only the deck's Lent non-DLI area; PDFs add Pre-K, CB classrooms and the MS pathway shift. Evidence: [PPS:pps_net/rightsizing/school_impact/kelly.pdf p.3] [PPS:pps_net/rightsizing/school_impact/marysville.pdf p.3] [PPS:pps_net/rightsizing/school_impact/woodmere.pdf p.3] [PPS:pps_net/rightsizing/school_impact/brentwood.pdf p.3]

- `proposed_action`: before: "boundary change" → after: "receive students; program move; boundary change"
- `action_detail`: before: "Listed among boundary changes; deck shows Lent non-DLI students attending Marysville moving to Kelly; Deck feeder slide: Kelly is a boundary feeder to Harrison Park MS" → after: "Per-school PDF: welcomes Lent neighborhood students previously assigned to Marysville; Communication Behavior classrooms from Woodmere and the PPS Pre-K from Marysville move to Kelly; neighborhood middle schoolers shift to Harrison Park MS (from Brentwood); Russian DLI students continue to Brentwood"
- `receiving_schools`: before: "" → after: "Harrison Park MS (neighborhood 6-8 pathway)"
- `sending_schools`: before: "Lent non-DLI area (per deck)" → after: "Lent non-DLI area (via Marysville); Marysville (PPS Pre-K); Woodmere (CB classrooms)"

### C11. Lane MS (renamed Brentwood MS) (A and B)
Adds the Kelly-area loss to Harrison Park. Evidence: [PPS:pps_net/rightsizing/school_impact/brentwood.pdf p.3]

- `action_detail`: before: "Brentwood MS receives Sellwood students from Duniway and Lewis areas" → after: "Brentwood MS receives Sellwood students from Duniway and Lewis areas; Per-school PDF: Kelly neighborhood middle schoolers shift to Harrison Park; Russian DLI stays; Duniway/Lewis students continue to Cleveland HS while Whitman/Woodmere students go to Franklin HS"
- `receiving_schools`: before: "" → after: "Harrison Park MS (Kelly neighborhood area)"

### C12. Harriet Tubman MS (A and B)
Adds the Irvington-area loss and ISC move. Evidence: [PPS:pps_net/rightsizing/school_impact/harriet_tubman.pdf p.3] [PPS:pps_net/rightsizing/school_impact/beverly_cleary.pdf p.3]

- `action_detail`: before: "Receives Vernon grades 6-8" → after: "Receives Vernon grades 6-8; Per-school PDF: middle graders in the current Irvington area move to Beaumont (current Irvington-area students may stay through 8th grade); 6-8 Intensive Skills Classroom from Beverly Cleary relocates to Tubman"
- `receiving_schools`: before: "" → after: "Beaumont MS (Irvington area)"

### C13. George MS (A and B)
Adds the Peninsula-area boundary change. Evidence: [PPS:pps_net/rightsizing/school_impact/george.pdf p.3] [PPS:pps_net/rightsizing/school_impact/ockley_green.pdf p.3]

- `action_detail`: before: "Receives César Chávez grades 6-8 and Ockley Green MS Spanish immersion" → after: "Receives César Chávez grades 6-8 and Ockley Green MS Spanish immersion; Per-school PDF: also welcomes neighborhood middle graders from the Peninsula area (shifting from Ockley Green); Peninsula-area students already at Ockley Green may stay"
- `sending_schools`: before: "César Chávez (6-8); Ockley Green MS (Spanish DLI)" → after: "César Chávez (6-8); Ockley Green MS (Spanish DLI); Ockley Green MS (Peninsula area)"

### C14. Ockley Green MS (A and B)
Adds the Peninsula-area boundary change. Evidence: [PPS:pps_net/rightsizing/school_impact/ockley_green.pdf p.3]

- `action_detail`: before: "Receives Faubion 6-8; Ockley Green Spanish immersion moves to George" → after: "Receives Faubion 6-8; Ockley Green Spanish immersion moves to George; Per-school PDF: former Peninsula area shifts to George MS; all Ockley Green students go to Jefferson HS (split pathway removed)"
- `receiving_schools`: before: "George MS (Spanish DLI)" → after: "George MS (Spanish DLI); George MS (Peninsula area)"

### C15. Peninsula (A and B)
Adds the middle-school reassignment. Evidence: [PPS:pps_net/rightsizing/school_impact/peninsula.pdf p.3] [PPS:pps_net/rightsizing/school_impact/george.pdf p.3]

- `action_detail`: before: "Consolidates into Rosa Parks" → after: "Consolidates into Rosa Parks; Per-school PDFs (George, Ockley Green): Peninsula middle-grade area shifts from Ockley Green to George MS"
- `receiving_schools`: before: "Rosa Parks" → after: "Rosa Parks (K-5, 100%); George MS (6-8 area)"

### C16. Hayhurst (A and B)
Adds the Hayhurst-to-Rieke boundary adjustment. Evidence: [PPS:pps_net/rightsizing/school_impact/hayhurst.pdf p.3] [PPS:pps_net/rightsizing/school_impact/rieke.pdf p.3]

- `action_detail`: before: "Receives ~70% of Maplewood area" → after: "Receives ~70% of Maplewood area; Per-school PDF: a portion of Hayhurst's current boundary shifts to Rieke"
- `receiving_schools`: before: "" → after: "Rieke (portion of Hayhurst boundary)"

### C17. Rieke (A and B)
Adds the Hayhurst-to-Rieke boundary adjustment. Evidence: [PPS:pps_net/rightsizing/school_impact/rieke.pdf p.3]

- `action_detail`: before: "Receives ~30% of Maplewood area" → after: "Receives ~30% of Maplewood area; Per-school PDF: also receives a portion of the Hayhurst boundary; continues to Robert Gray MS and Ida B. Wells HS"
- `sending_schools`: before: "Maplewood (30%)" → after: "Maplewood (30%); Hayhurst (portion of boundary)"

### C18. Sunnyside Environmental (A and B)
Adds the high-school pathway change. Evidence: [PPS:pps_net/rightsizing/school_impact/sunnyside.pdf p.3] [PPS:pps_net/rightsizing/school_impact/cleveland.pdf p.3] [PPS:pps_net/rightsizing/school_impact/franklin.pdf p.3]

- `action_detail`: before: "Becomes K-5 neighborhood school; environmental focus option discontinued (no new lottery transfers; existing lottery students may stay through grade 5); receives ~50% of Buckman; grades 6-8 to Hosford" → after: "Becomes K-5 neighborhood school; environmental focus option discontinued (no new lottery transfers; existing lottery students may stay through grade 5); receives ~50% of Buckman; grades 6-8 to Hosford; Per-school PDF: high school path changes from Franklin to Cleveland; Buckman SES classrooms relocate to Sunnyside"
- `receiving_schools`: before: "Hosford MS (6-8)" → after: "Hosford MS (6-8); Cleveland HS (HS path, instead of Franklin)"

### C19. Marysville (A and B)
CSV said "Consolidates into Arleta" with no timing; PDFs give the split and a 2028-29 closure (Arleta PDF wording "entire ... student body" conflicts; see D02). Evidence: [PPS:pps_net/rightsizing/school_impact/marysville.pdf p.3] [PPS:pps_net/rightsizing/school_impact/kelly.pdf p.3] [PPS:pps_net/rightsizing/school_impact/arleta.pdf p.3]

- `proposed_action`: before: "close" → after: "close; program move"
- `action_detail`: before: "Consolidates into Arleta" → after: "Per-school PDF: closes as a K-5 school after 2027-28 (projection shows 300 students in 2027-28 and "School would close" from 2028-29; "Delaying full implementation" so SEGC-impacted students are not moved twice). Pre-SEGC Marysville boundary to Arleta; pre-SEGC Lent non-DLI boundary to Kelly; PPS Pre-K to Kelly"
- `receiving_schools`: before: "Arleta" → after: "Arleta (pre-SEGC Marysville boundary); Kelly (pre-SEGC Lent non-DLI boundary; PPS Pre-K)"

### C20. Arleta (A and B)
Adds timing. Evidence: [PPS:pps_net/rightsizing/school_impact/arleta.pdf p.3]

- `action_detail`: before: "Receives Marysville" → after: "Receives Marysville; Per-school PDF: projection shows the merge in 2028-29 (224 in 2027-28; 536 in 2028-29); new HVAC in Summer 2027"

### C21. Sellwood MS (A and B)
Adds timing. Evidence: [PPS:pps_net/rightsizing/school_impact/sellwood.pdf p.3] [PPS:pps_net/rightsizing/school_impact/hosford.pdf p.3] [PPS:pps_net/rightsizing/school_impact/llewellyn.pdf p.3]

- `action_detail`: before: "Students go to Hosford (Llewellyn area) or Brentwood (Duniway and Lewis areas)" → after: "Students go to Hosford (Llewellyn area) or Brentwood (Duniway and Lewis areas); Per-school PDF: closes as a school building in 2028 (projection shows 523 students in 2027-28, closed from 2028-29); reason: entire mechanical system replacement needed"

### C22. Duniway (Scenario A)
CSV described the Llewellyn shift as "southern boundary, per deck"; PDF defines it as the area west of McLoughlin Blvd. Evidence: [PPS:pps_net/rightsizing/school_impact/duniway.pdf p.3] [PPS:pps_net/rightsizing/school_impact/llewellyn.pdf p.3]

- `action_detail`: before: "Receives Lewis; deck shows southern Duniway boundary change involving Llewellyn" → after: "Receives Lewis neighborhood students; per-school PDF: Duniway's boundary area west of McLoughlin Blvd moves to Llewellyn (Scenario A only); all Duniway students go to Brentwood MS then Cleveland HS"
- `receiving_schools`: before: "Llewellyn (southern boundary, per deck)" → after: "Llewellyn (area west of McLoughlin Blvd)"

### C23. Llewellyn (Scenario A)
Same as C22. Evidence: [PPS:pps_net/rightsizing/school_impact/llewellyn.pdf p.3]

- `action_detail`: before: "Listed among Scenario A boundary changes; Llewellyn-area Sellwood students to Hosford" → after: "Per-school PDF: boundary expands to welcome students from Duniway living west of McLoughlin Blvd; students go to Hosford MS instead of Sellwood"
- `sending_schools`: before: "Duniway (southern boundary, per deck)" → after: "Duniway (area west of McLoughlin Blvd)"

### C24. Capitol Hill (Scenario A)
Adds special-education program move. Evidence: [PPS:pps_net/rightsizing/school_impact/capitol_hill.pdf p.3] [PPS:pps_net/rightsizing/school_impact/stephenson.pdf p.3]

- `action_detail`: before: "Receives ~30% of Stephenson area" → after: "Receives ~30% of Stephenson area; Per-school PDF: Stephenson's Communication Behavior classroom moves to Capitol Hill; targeted seismic bond work Summer 2027 and Summer 2028"

### C25. Stephenson (Scenario A)
Adds special-education program move. Evidence: [PPS:pps_net/rightsizing/school_impact/stephenson.pdf p.3]

- `action_detail`: before: "Consolidates into Markham (70%) and Capitol Hill (30%)" → after: "Consolidates into Markham (70%) and Capitol Hill (30%); Per-school PDF: Communication Behavior classroom moves to Capitol Hill"

### C26. Buckman (A and B)
CSV only noted Buckman was listed as an arts focus option; PDF states the arts program closes. Evidence: [PPS:pps_net/rightsizing/school_impact/buckman.pdf p.3]

- `proposed_action`: before: "close" → after: "close; program discontinued"
- `action_detail`: before: "Consolidates into Abernethy (50%) and Sunnyside (50%); Buckman is listed as a focus-option school (arts) in June 2026 materials" → after: "Consolidates into Abernethy (north of Hawthorne and south of Burnside) and Sunnyside (north of Burnside); per-school PDF: "The Arts special-focus choice program would close"; SES classrooms move to Sunnyside"

### C27. Creston (A and B)
Adds preschool annex and pathway. Evidence: [PPS:pps_net/rightsizing/school_impact/creston.pdf p.3]

- `action_detail`: before: "Neighborhood K-5 students to Atkinson; Creston Deaf and Hard of Hearing program to Glencoe" → after: "Neighborhood K-5 students to Atkinson; Creston Deaf and Hard of Hearing program to Glencoe; Per-school PDF: the Creston Annex preschool building would stay open as a preschool center; new boundary goes Atkinson -> Kellogg MS -> Franklin HS"

### C28. Bridger Creative Science (A and B)
Adds choice for current 6th/7th graders. Evidence: [PPS:pps_net/rightsizing/school_impact/bridger_creative_science.pdf p.3]

- `action_detail`: before: "Becomes K-5 (neighborhood/focus); grades 6-8 to Harrison Park MS" → after: "Becomes K-5 (neighborhood/focus); grades 6-8 to Harrison Park MS; Per-school PDF: keeps neighborhood area and Creative Science choice program; current 6th and 7th graders reassigned to Harrison Park MS or may return to their neighborhood middle school"

### C29. Beverly Cleary (A and B)
Adds timing and swing-site plan. Evidence: [PPS:pps_net/rightsizing/school_impact/beverly_cleary.pdf p.3] [PPS:pps_net/rightsizing/school_impact/beaumont.pdf p.3] [PPS:pps_net/rightsizing/school_impact/irvington.pdf p.3]

- `action_detail`: before: "Becomes K-5; receives Irvington K-5; grades 6-8 to Beaumont MS (memo cites Beverly Cleary seismic work)" → after: "Becomes K-5; receives Irvington K-5; grades 6-8 to Beaumont MS (memo cites Beverly Cleary seismic work); Per-school PDF: 6-8 moves to Beaumont in Fall 2027; seismic upgrades completed summer 2028; Irvington site evaluated as a 2027-28 swing site; 6-8 Intensive Skills Classroom relocates to Harriet Tubman"

### C30. Irvington (A and B)
Adds swing-site plan. Evidence: [PPS:pps_net/rightsizing/school_impact/irvington.pdf p.3]

- `action_detail`: before: "Consolidates into Beverly Cleary for K-5; Irvington middle school area assigned to Beaumont" → after: "Consolidates into Beverly Cleary for K-5; Irvington middle school area assigned to Beaumont; Per-school PDF: Irvington building considered as a temporary swing site for Beverly Cleary K-5 during its summer 2027 seismic upgrades; Irvington middle graders move from Tubman to Beaumont"

### C31. Metropolitan Learning Center (MLC) (A and B)
Adds timing. Evidence: [PPS:pps_net/rightsizing/school_impact/metropolitan_learning_center.pdf p.3]

- `action_detail`: before: "MLC becomes K-8; MLC 9-12 high school program closes (students to neighborhood HS; not counted as a closure); Odyssey relocates to MLC site" → after: "MLC becomes K-8; MLC 9-12 high school program closes (students to neighborhood HS; not counted as a closure); Odyssey relocates to MLC site; Per-school PDF: high schoolers move in Fall 2027; Odyssey moves when site preparation at MLC is complete"

### C32. Odyssey (A and B)
Adds timing. Evidence: [PPS:pps_net/rightsizing/school_impact/odyssey.pdf p.3]

- `action_detail`: before: "Odyssey relocates to MLC site; East Sylvan building left vacant for repurposing process" → after: "Odyssey relocates to MLC site; East Sylvan building left vacant for repurposing process; Per-school PDF: "The East Sylvan building would close"; move in fall 2027 or fall 2028 depending on building preparation at MLC"

### C33. Woodmere (A and B)
Adds special-education program move. Evidence: [PPS:pps_net/rightsizing/school_impact/woodmere.pdf p.3] [PPS:pps_net/rightsizing/school_impact/whitman.pdf p.3] [PPS:pps_net/rightsizing/school_impact/kelly.pdf p.3]

- `action_detail`: before: "Consolidates into Whitman" → after: "Consolidates into Whitman; Per-school PDF: Communication Behavior classrooms move to Kelly; combined Whitman boundary goes to Brentwood MS then Franklin HS"

### C34. Lewis (Scenario A)
Adds special-education program move. Evidence: [PPS:pps_net/rightsizing/school_impact/lewis.pdf p.3] [PPS:pps_net/rightsizing/school_impact/woodstock.pdf p.3]

- `action_detail`: before: "Consolidates into Duniway" → after: "Consolidates into Duniway; Per-school PDF: Communication Behavior classroom moves to Woodstock; students go to Brentwood MS then Cleveland HS"

### C35. Woodstock (Scenario A)
Adds special-education program move (A only; see D04 for B). Evidence: [PPS:pps_net/rightsizing/school_impact/woodstock.pdf p.3] [PPS:pps_net/rightsizing/school_impact/lewis.pdf p.3]

- `action_detail`: before: "Receives Clark Chinese (Mandarin) immersion" → after: "Receives Clark Chinese (Mandarin) immersion; Per-school PDF: Communication Behavior classrooms from Lewis (closing in A) relocate to Woodstock"

### C36. Maplewood (A and B)
Adds special-education program move. Evidence: [PPS:pps_net/rightsizing/school_impact/maplewood.pdf p.3] [PPS:pps_net/rightsizing/school_impact/markham.pdf p.3]

- `action_detail`: before: "Consolidates into Hayhurst (70%) and Rieke (30%); Maplewood middle school area shifts from Jackson MS to Robert Gray MS" → after: "Consolidates into Hayhurst (70%) and Rieke (30%); Maplewood middle school area shifts from Jackson MS to Robert Gray MS; Per-school PDF: K-2 Intensive Skills Classroom moves to Markham to rejoin the 3-5 classroom"

### C37. Markham (Scenario A)
Adds special-education program move (B ambiguous; see D03). Evidence: [PPS:pps_net/rightsizing/school_impact/markham.pdf p.3]

- `action_detail`: before: "Receives ~70% of Stephenson area" → after: "Receives ~70% of Stephenson area; Per-school PDF: also receives the K-2 Intensive Skills Classroom from Maplewood"

### C38. Sabin (A and B)
Adds special-education program move. Evidence: [PPS:pps_net/rightsizing/school_impact/sabin.pdf p.3] [PPS:pps_net/rightsizing/school_impact/vernon.pdf p.3] [PPS:pps_net/rightsizing/school_impact/dr_martin_luther_king_jr.pdf p.3]

- `action_detail`: before: "Consolidates into Dr. Martin Luther King Jr." → after: "Consolidates into Dr. Martin Luther King Jr.; Per-school PDF: Sabin SES students go to a K-5 SES classroom at Vernon or MLK Jr."

### C39. Atkinson (A and B)
Adds pathway. Evidence: [PPS:pps_net/rightsizing/school_impact/atkinson.pdf p.3]

- `action_detail`: before: "Receives Creston neighborhood K-5; Atkinson Spanish immersion moves to Lent; Deck feeder slide: Atkinson marked "No longer feeds to" Harrison Park MS" → after: "Receives Creston neighborhood K-5; Atkinson Spanish immersion moves to Lent; Deck feeder slide: Atkinson marked "No longer feeds to" Harrison Park MS; Per-school PDF: all students in the new Atkinson boundary go to Kellogg MS and Franklin HS"
