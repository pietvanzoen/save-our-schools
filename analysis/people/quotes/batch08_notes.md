# Batch 08 notes: 2026-05-26 → 2026-07-07

This batch covers 9 transcripts and 9 meeting files:
- 05-26 special meeting and budget committee
- 05-27 FIO
- 06-09 regular meeting
- 06-11 TLE
- 06-15 Policy Committee
- 06-23 TSCC hearing
- 06-23 special meeting (budget adoption)
- 06-24 FIO
- 07-07 regular meeting

Quotes are in `batch08.jsonl`: 117 in total (77 high, 37 medium, 3 low confidence). Every quote string was checked programmatically against the raw transcript, with tolerance only for bracketed repairs. Timestamps and seconds are taken from the transcript line where each quote begins.

## Attribution method and problems

- **Seat-order rounds, May–June 2026.**
  - In "go-around" rounds the chair names only the first (and sometimes the last) speaker. Two named anchors fix the cyclic dais order at the 5/26 meeting:
    - "start with Director Sullivan … end with Chase Miller" (rightsizing round)
    - "start with Director Lefort … Vice Chair Depass … Director Englesman" (budget round)
  - The order this gives is **Sullivan → La Forte → DePass → Wang → Engelsman → Splitt → Ritorto → (Sandell) → Chase-Miller**.
  - Named cross-references confirm it independently:
    - Ritorto: "agree with Director LaForte about Access Academy"
    - Chase-Miller: "appreciate Director Splitt's comments"
    - Another director: "similar to Director Englesman" (bond permits)
    - Wang: "Director Englesman" (AI pause)
  - The same order holds in every 6/23 round (travel, OIPA, AI, the $13M amendment and reserves). For example, the reserves round started at "student representative Retorto" and ran Chase-Miller → Sullivan → La Forte → DePass → Wang → Engelsman → Splitt.
  - Quotes that rest only on seat order are marked `medium`. Other batches found a *different* dais order in March 2026 (batch06 notes), so do not carry this order to other dates without re-checking.
- **6/24 FIO (bQb4RGUlfk0):** analyzed from English captions in `batch10_redo` (see `analysis/meetings/2026-06-24_bQb4RGUlfk0.md`).
- **Committee chair discrepancies** (resolved from video):
  - The 6/15 Policy minutes call Chase-Miller "Committee Chair" but say "Committee Chair DePass called the meeting to order". On video, DePass introduces herself as policy committee chair and says Chase-Miller "chairs the teaching and learning" committee.
  - At 6/11 TLE, La Forte was "standing in for committee chair" Chase-Miller.
  - La Forte chaired FIO on 5/27 and 6/24.
  - For 2026-27, BoardBook lists DePass as FIO chair and Engelsman as Policy chair. That listing is in the archived meeting-list page `sources/boardbook/meetings/2026-06-23_751802_*/minutes.md`.
- **Caption name errors corrected (all normalized in the JSONL):**
  - Engelsman: Englesman, Anglesman, Anglesmith, Inklesmith, Ingelsman, Egleston, Engleson, Director Angle
  - La Forte: Lefort, LaForge, LaFrance, LaPorte, Leaffort, "Dart."
  - Splitt: Split, Slate, Smith, Space
  - Sullivan: Solvang, Svin
  - Wang: Wong, Wung, Won
  - Chase-Miller: "Michelle Chase Miller", "Chase Billowith"
  - DePass: Depast, "the pass", "to pass"
  - Ritorto: Retorto, Retardo, RTO, Torto
  - Sandell: Sandal
  - Other names:
    - Toncray: Tonkray, Tonrey
    - Emily Glasgow: Glasco, Blascal; spelling per BoardBook
    - Jenny Withycombe: Wikcom, Wetzel-Cohen
    - Brandon Coonrod: Conrad, Comrade
    - Rose Sandell: Rose Sandal
    - Grace Adair: Gryair, Graceadair, Grice-Adair in minutes
    - Presidio: Prescidio
- **Minutes discrepancies with video:**
  - 5/26 minutes label the PAT agreement vote "Resolution 7299" and the Budget Committee vote "Resolution 7307". They also say the motion to send contracting rules back to Policy "failed"; on video the chair announces it passed 7–0.
  - 6/23: on video Ritorto votes "No" on the OIPA amendment; the minutes record "Yes (unofficial)".
  - 7/07 minutes list Ritorto and all seven directors in attendance, but the votes record Engelsman absent. The video shows new student rep Rose Sandell.
- **Minutes text extraction.** Most minutes PDFs (3998080/81/82/97/99/3998100/3998101) have only page 1 as text; the remaining pages are images. I OCR'd them in scratch with tesseract, without editing `sources/`. Citations use PDF page numbers. **Suggestion:** add OCR text files for these minutes to `sources/` with provenance, so later agents can grep them.
- **Low-confidence items** are in the JSONL but not used in the summaries:
  - Calvert's "anytime there's an and" (5/26)
  - the CFO's property-sale remarks at TSCC (6/23 eD_6WvmchGw) and at the 6/23 special meeting
  - The 7/07 Morrison $2.5M property statement is high confidence and confirms the 6/23 one.

## People: positions and evolution within this window

**Kimberlee Armstrong (Superintendent)**
- **Deficit framing:**
  - The structural deficit is over $160M and only about 60% has been addressed (6/9).
  - 82 layoffs, later cited as 87 by PAT. This is the first layoff of more than about 5 people in a decade.
  - The 2027-28 cut of about $65M is meant to be "the stabilizing reduction". Her goal is to end recurring reductions "within the next 2 years" (6/23).
- **Rightsizing:**
  - She explicitly ties stabilization to "boundary adjustments or program moves and school closures" (6/23).
  - Fall 2026 decisions cannot involve "a conversation with every impacted human"; some will be "decide and then mitigate later" (6/9).
- **Rebutting "chop from the top":**
  - Central leadership is down 14% since 2018-19.
  - All central admin costs less than $5M.
  - Any found money would go to the deficit, not to restoring positions (6/23, 7/07).
- **Next cuts.** She lists likely next-year cuts: non-mandatory transport, "holding firm on class-size minimums or grade minimums", middle-school athletics, custodial (7/07).

**Jon Franco (Sr. Chief of Operations)**
- Operational lead on rightsizing alongside Calvert.
- At TSCC (6/23) he gave the clearest staff savings estimate: closing a site saves "roughly a 15 to 20% savings in operational costs". He insisted rightsizing is "not … for the purpose of cost savings" but for "consistency of student experience".
- Early closure savings would fund transitions, a lesson from SEGC.
- Modeling is in-house in four work groups.
- Cited a $65M 2027-28 deficit (6/9).
- Champions the ACCESS hub model as "sustainable practice" (5/26).

**Margaret Calvert (Asst. Superintendent)**
- Presented the Reso 7307 revisions and the timeline: scenarios in late summer, recommendation in mid-November, vote in December, implementation in fall 2027.
- Added a cohort-cohesion assessment (5/26).
- At TLE (6/11) she flagged the clustering of focus options in SE Portland and their physical location as a rightsizing lever.

**Michelle Morrison (CFO)**
- PERS is the main remaining structural gap. The PERS reserve is now exhausted (6/23 TSCC).
- Drawing reserves would turn the $65M gap into $78M and threaten the credit rating (6/23).
- **Disclosed that the adopted budget assumes one real-property sale (~$2.5M, one-time),** and that more property could be "liquidated" as enrollment declines (7/07).

**Eddie Wang (Chair; re-elected 7/07, 6–0)**
- **Rightsizing:** walkability as a top priority "means … we don't do anything" (5/26). He favors a riskier 2026-27 budget and a "safer lower baseline" *after consolidations* (5/26). This is consistent with treating consolidation as the route to stability.
- **Budget:** a strong defender of the board's record of protecting classrooms ($30M, then $48M, mostly central cuts). "we kept kicking the can down the road … hoping … Salem would change something" (6/23, 7/07). Opposed the reserve draw and the $13M amendment.
- **Governance:** clashed with La Forte over OIPA funding (6/23). Wants BAC independence protected (6/9). Abstained on postponing the waste-sensor contract (7/07).

**Stephanie Engelsman**
- **Rightsizing:** wants earlier, granular notice to communities and the Policy 6.10.030 closure fiscal report, including transport costs. Highlights harm to the SE Guiding Coalition fifth-grader cohort (5/26).
- **ACCESS:** floated a second ACCESS site (5/26). Insisted that neighborhood kids keep priority for after-school programs (6/9).
- **Budget:**
  - Sponsored the failed $13.12M school-staffing restoration (1–6).
  - Argued cuts could cost ~1,822 students' worth of state funding.
  - Was the only abstention on budget adoption (6/23).
  - Ran for chair, then withdrew the day of the 7/07 vote while absent.
- **Oversight:** bond permit slippage (5/26); contract amendments between 100% and 124.99% (6/15); AI and data privacy, including the Amira contract collecting migrant and foster status (6/15, 6/23).
- **Likely Cleveland neighbor** who campaigned for the 2025 bond (6/23, medium).

**Virginia La Forte**
- Strongest ACCESS advocate. Wants "expanding not shrinking" ACCESS within rightsizing (5/26).
- **Bond oversight hawk as FIO chair:**
  - Objects that bond consultant "pools" bypass board approval of contracts over $150K (5/27).
  - Says Jefferson problems "cost us tens of millions" (6/9).
  - Wants annual visibility into multi-year "not to exceed" contracts (7/07).
- **6/23 amendments:** the travel freeze (passed), OIPA protection (failed 3–4) and the GenAI pause (passed 7–0).
- Wants board goals beyond test scores ("feel loved and cared for").

**Christy Splitt**
- Accepts rightsizing trade-offs if explained ("exceptions to the rule … fewer kids have a walkable route … so that they can have a full-time librarian", 5/26).
- Recalled the board's ambivalence about the 2025 bond and backs a stronger BAC (6/9).
- **Layoffs:** personally affected (her daughter's teacher). Wants a briefing on the seniority process (6/9).
- On the $13M: "don't know where we could cut another $13 million" (6/23).
- **Signals she will leave the board:** "I'll be gone" (6/9) and "I will never have the experience of being in leadership" (7/07, medium). She asked for more frequent leadership rotation.

**Rashelle Chase-Miller (Vice-Chair from 7/07)**
- **Equity voice on rightsizing:** prioritizing walkability risks "disadvantaging some communities over other communities" and burdening historically bused families (5/26).
- Sees rightsizing as the path to a "sustainable baseline" (5/26, medium).
- **On the $13M amendment** she was the pivotal pragmatist:
  - she asked for a path to the money;
  - she proposed a limited reserve draw (4%) paired with property sales to rebuild reserves (failed 2–4–1);
  - she voted no on the full amendment.

**Michelle DePass (Vice-Chair until 7/07)**
- Asked when facility retrofits for converted or merged schools would be scheduled (5/26, medium).
- **Draws on her bond-construction background:**
  - objected to the BAC "planning and execution" language (6/9);
  - explained why multi-year contracts lock in prices (7/07).
- Resisted last-minute amendments and invoked "sense of urgency" as a white-supremacy-culture characteristic (6/15, 6/23).
- "We've already said yes to everything" (6/23). Suggested revisiting MLC programming.

**Patte Sullivan**
- Endorsed Reso 7307 as written (5/26).
- Supported the expanded BAC charter (6/9).
- As Audit Committee chair she objected to a public debate over cutting an auditor position (6/23).
- Opposed reserve draws as fiscally irresponsible (6/23).

**Ian Ritorto (student rep through June)**
- Wants a 10–15-year moratorium on further boundary changes after rightsizing. Criticized Jefferson Rising for departing from community feedback without explanation (5/26).
- Backed ACCESS expansion.
- Skeptical of the $13M amendment ("charcuterie board of stinky cheese").

**Rose Sandell** became student rep in July 2026. Her first meeting was 7/07.

## Rightsizing timeline facts recorded in this batch
- **5/26:** Reso 7307 (guiding principles and work plan) adopted 7–0. Late June/July: framework and metrics. Late Aug–early Oct: scenario engagement. Mid-Nov: superintendent recommendation. December: vote. Fall 2027: implementation.
- **6/11 TLE:** educational options inventory. Lottery seats are now 32% of K enrollment, up from 14%.
- **6/23 TSCC:** Franco's 15–20% per-site savings estimate.
- **6/23 and 7/07:** a property sale is already budgeted (~$2.5M). Future sales are tied to enrollment decline.
- **7/07:** PAT's new president expects "difficult conversations about what right sizing might look like".

## Facts the controller may want saved to memory
- None about the user. **Process note for future runs:** this scratchpad is shared across batch agents, so each agent should work in its own subfolder.
