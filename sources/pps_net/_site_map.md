# pps.net / bond.pps.net / media.pps.net: site map for the PPS archive

Crawled 2026-10-10 with WebFetch. The shell cannot reach pps.net, so nothing here has been downloaded yet. The download list is `_download_manifest.jsonl` in this folder: 937 unique URLs, each with `found_on`, `topic`, `priority` and a suggested `save_as`. Many entries also carry `notes` with download hints (Drive direct-download URL, Google Docs export URL, legacy-URL warning, and so on).

How these notes were written: facts below are what the pages said when fetched, as summarized by the fetch tool. They have not been checked against the files. **Analysis:** marks my own inference.

General download notes:
- `https://www.pps.net/fs/resource-manager/view/<uuid>` is Finalsite's document link. It redirects to the actual file on `resources.finalsite.net`. The manifest guesses `.pdf` for most; keep whatever extension the server actually returns.
- Many rightsizing, Jefferson, BAC and CBRC files are on Google Drive. The `notes` field gives a `uc?export=download&id=` URL. Fetching the Drive viewer pages with WebFetch shows only "Loading…", so a real browser is needed.
- **All BoardBook numeric docIds** linked from the Rightsizing Presentations page are **already in `sources/boardbook`**: 14430171, 14357211, 3997425–3997428, 3997273, 3997282, 3997246, 3990244, 3990653, 3988980, 3990455, 3991313 and 3997004. I verified this against `attachments_index.csv`, so the manifest does not repeat them.
- BoardBook links that use a GUID (`?file=<guid>`) instead of a docId *are* in the manifest. Examples are the Jefferson resolutions and memo, and the Holmes seismic assessment. They may duplicate archived docIds, so check before downloading.
- Pages with `/cms/lib/OR01913224/Centricity/...` URLs come from the pre-Finalsite site. I found them by web search, and they may now return 404.

---

## 1. Rightsizing ("Rightsize. Right Support. Right for Students.")

- `https://www.pps.net/rightsizing` is the short link to `/about/portland-public-schools-information/rightsize/rightsize`, the landing page. The site-wide banner on every PPS page links there.
- **Subpages** under `/about/portland-public-schools-information/rightsize/`:
  - `rightsize`: the landing page. It holds dated messages from April 13, April 19, April 22, May 7 and September 2026, plus the engagement calendar.
  - `videos`: 6 explainer videos (page published 2026-09-29).
  - `frequently-asked-questions`
  - `rightsizing-presentations`
  - `segc-documents`
  - `timeline`
  - `calendar`
  - `scenarios`: created 2026-10-02, published 2026-10-08.
  - `how-could-your-school-be-impacted`
  - `feeder-patterns`
- **fs/pages aliases** for the same subpages: 49325 (videos), 49329 (scenarios), 46269 (presentations), 46802 (SEGC), 46268 (FAQ), 49328 (feeder patterns), 46257 (calendar), 49336 (school information, which resolves to how-could-your-school-be-impacted), and **46267, a "Maps" page** that is not in the navigation and showed only a banner.
- **Scenarios page.** It links one overview PDF, "View the Scenarios". That file is on Google Drive under the name *"District wide scenarios 10.04.26 (2).pdf"*. The page also links four regional PDFs: Cleveland-Franklin, Grant-McDaniel, Jefferson-Roosevelt and Wells-Lincoln. It says school-specific information exists "for all 81 PPS schools". However, **the per-school links are not in the HTML**: neither the main content of how-could-your-school-be-impacted nor fs/pages/49336 has them. **Analysis:** they are probably behind a JS widget or image map. The controller should open the page in a real browser and capture every per-school document. **This is the biggest gap.**
- **Scenario survey.** `https://www.pps.net/rightsize-scenario-survey` redirects (302) to a Google Form titled "Rightsize. Right Support. Right for Students. Scenario Feedback". There are Spanish, Vietnamese, Chinese, Russian and Somali versions; their URLs are in the WebFetch result but are not in the manifest. The page states no deadline.
- **May 2026 feedback poll.** It closed May 15 at 11:59 PM and ran on Slido in 5 languages. The English version is `/rightsize/English`, which failed to fetch.
- **Timeline page (verbatim phases):**
  - Exploration: Fall 2025 – Winter 2026
  - Plan + Initiate: Winter 2025-26
  - Engage + Develop: Spring Summer 2026
  - Study + Recommend: Fall 2026
  - Decide + Commit: Late Fall 2026 (Nov – Dec)
  - Implement: Winter – Fall 2027
- **FAQ facts:**
  - The Superintendent presents draft plans in early fall 2026 and a formal recommendation in November. The Board votes in December.
  - Changes begin in fall 2027. Implementation must start no later than 2027-28 and finish within 3 years.
  - The Board adopted four guiding principles on May 26, 2026 (Resolution 7307).
  - PPS cites a 30% drop in Portland births over a decade.
  - The page gives no closure count, no savings figure and no numeric thresholds.
  - It links the PAT furlough MOU (4 unpaid days in 2025-26).
- **Engagement calendar on the landing and calendar pages:**
  - Board Community Connections: 9/19 Faubion, 9/30 Ida B. Wells, 10/9 Roosevelt, 10/17 McDaniel, 10/27 Lincoln, 10/28 virtual, 10/29 Cleveland at Marshall, 11/14 Franklin, 12/3 Grant.
  - Board Public Listening Sessions: 11/18 Harriet Tubman MS, 11/19 Franklin, 12/1 Lincoln.
  - Community Voice sessions for Native, Multilingual, Latino/a/e and Black/African American families: Sept 22–24 and Oct 19–26.
  - School Board meeting on Oct 6, 2026.
- **Presentations page.** It lists, with BoardBook agenda and YouTube links, the meetings of:
  - 2026: 3/10, 3/12, 3/31, 4/14, 4/28, 5/12, 5/26, 6/11, 8/4, 9/1, 9/8, 9/15.
  - The **9/8 TLE presentation is a Google Slides deck** ("09.08.26_TLE_Well-Resourced-Schools_Rightsizing"), not a BoardBook file. It is in the manifest as priority 1.
  - The page also links outside reference documents that are already in BoardBook: the Denver DSTI annual report and the Oregon PTA consolidation guidance (both 3/31).
- **SEGC documents:** the Equity Audit Evaluation of the Southeast Enrollment & Program Balancing Initiative, and its School-by-School Analysis. Both are on Drive and duplicate BoardBook 3997427 and 3997428.
- **Contacts named:**
  - Dr. Kimberlee Armstrong (Superintendent)
  - Dr. Jon Franco (Sr. Chief of Operations), on the April 13 letter
  - Margaret Calvert (Assistant Superintendent, School Planning and Modernization), on the May 7 letter
  - Email: Rightsizing@pps.net
- **media.pps.net Rumors & Facts** contains the rightsizing statements most useful for analysis. PPS states that:
  - Rightsizing savings won't balance the implementation-year budget.
  - Bond projects are not an indicator of rightsizing status.
  - Head Start, Columbia Regional and MECP seats are excluded from utilization (Creston is the example given).
  - It projects a **$65M gap in 2027-28**.
- **Press release, 2026-10-05:** "PPS Sends Rightsizing Scenarios to the Board".

## 2. Data & Reporting (Data Strategy & Insights)

Base path: `/departments/dataaccountability/data-and-accountability/data-strategy-and-insights/`

- `data-and-reporting` has 52 dataset links:
  - **2026-27:** only the PSU PRC Enrollment Forecast (2026-27 to 2035-36). The "Enrollment & School Profile" and "Discipline" headings have no items yet. **Analysis:** the October 2026 counts are not yet posted.
  - **2025-26:** 22 datasets (enrollment summary, 10-year history, capture rates, enrollment by neighborhood of residence, class size, DLI tracks, the PSU forecast 2025-26 to 2034-35, discipline).
  - **2024-25:** 24 datasets.
  - Graduation dashboard files covering 2009–2026.
- **Discrepancy:** the 2025-26 PSU forecast has *two different* uuids. The Data & Reporting page uses `e54facfd…`; the archive's "2025-26 Report" uses `5c948f4e…`. Both are in the manifest; compare them.
- `archives` (= fs/pages/46482): about 250 links in 15 categories, mostly 2006-07 through 2023-24. They cover PSU enrollment projections back to 2008-09, enrollment profiles, 10-year history summary and detail, capture rates and residence-area enrollment (2019-20 to 2023-24), class size, ADM/ADA, TAG/SpEd, FRL, discipline, restraint/seclusion and old program evaluations.
  - Quirks: several "Report" companion links all point to the 2024-25 forecast uuid. A few uuids repeat across years (class size 2014-15/2015-16; ADA 2008-09/2009-10; discipline 2007-08 is the same file in two categories).
- `enrollment-and-systems-planning` is **passkey-gated**: it shows a login prompt only and was published 2026-09-09. Nothing could be retrieved.
- `research-and-evaluation` links the Panorama "Successful Schools Survey" dashboard. Research reports are "Coming Soon!". Contact: Dr. Anna Kushner, Evaluator III.
- `our-academic-journey` shows 2024-25 results as images. Its enrollment graph shows decline from 48,780 toward a projected 43,375.

## 3. Budget

- `/about/2026-27-budget-process/2026-27-budget-process`:
  - Shortfall of $50M for 2026-27.
  - Prior cuts: $30M (2022-23); $10M plus a hiring freeze (2023-24); $15M (2024-25); $40M (2025-26).
  - The Proposed Budget was released 2026-04-28. About $3.5M was restored after more than 300 people gave input.
  - Documents:
    - Proposed Budget Vol 1 PDF
    - Proposed Budget Vol 2 PDF (updated 2026-05-06)
    - 2026-27 Budget Development Preliminary Report (Drive)
- **2026-27 FAQ:** about 322 FTE may be affected. The Board vote was set for June 23 (2026). Rightsizing is separate from the budget process.
- **2025-26 FAQ:**
  - About 183 FTE reduced: about $23M school-based and about $20M central.
  - $24M PERS Stabilization Reserve used as a one-year fix.
  - Links the 2025-26 Proposed Budget Vol 1 and Vol 2 (School Reports).
  - No closures were planned for 2025-26.
- **Budget calendar page** (URL slug still says 2025-26): it shows no events.
- **CBRC page (fs/pages/20903):** 9 members (term ends listed); 2026 meeting materials (Feb 4 to Jul 9); the "2026-27 CBRC Proposed Budget Review"; "Budget Principles Adopted by the Board"; and an archived-materials page.
- **Legacy Centricity budget PDFs found by search:** 2025-26 Adopted Budget, 2024-25 Adopted Vol 1, the 2025-26 budget calendar and the 2025-26 CBRC report of April 24, 2025.
- **Not found:** a 2026-27 *Adopted* Budget link on Finalsite pages. **Gap:** the controller should search for it, or check BoardBook for June 2026.

## 4. Bond (bond.pps.net) and seismic

- **bond.pps.net home:**
  - Over 1,100 projects since 2012. Modernizations in progress: Jefferson, Cleveland and Ida B. Wells, with HS openings in Fall 2029.
  - Jefferson construction runs in phases from 2026. Its athletic fields are due February 2027.
  - Ida B. Wells groundbreaking is Nov 13. Cleveland "Claim a Brick" was Sept 26.
- **`/about`:**
  - 2025 bond: new Cleveland and Ida B. Wells, completion of the Jefferson rebuild, seismic work at **8–10 schools at greatest risk**, a reserve fund, repairs, curriculum and tech, athletics and arts.
  - The page states no dollar amount. RISE says **$1.83B**.
  - Prior bonds: 2012 ($482M), 2017 ($790M), 2020 ($1.2B).
- **`ppsbondhub.com`** (2025 Bond Reporting & Vendor Hub, run by PROCEDEO). It links:
  - **Program Summary Schedule (2026-09-02)**
  - **Bond Financials as of 07.01.26**
  - Both are priority 1. The hub also shows bid status, including Grice-Adair CMGC with a tentative board date of 11/4/26.
- **`/seismic-improvements`** (the main seismic page, also reached as `/seismic-improvements/seismic-retrofits-2020-bond`):
  - **2025-bond seismic projects:**
    - Vernon (targeted, summer–fall 2026)
    - Winterhaven (targeted, summer 2026–spring 2027)
    - Starting summer 2027: Ainsworth (targeted, partly SRGP); **Beverly Cleary-Fernwood** (full; swing site TBD); Capitol Hill, Kelly and Richmond (targeted)
    - Starting summer 2028: **Rose City Park** (full; swing site TBD); **Beach** (targeted). The Beach text is internally inconsistent about dates.
  - **Selection method:** Resolution 7109 (May 6, 2025) and Holmes Engineering scoring, weighted 90% seismic risk, 5% facility condition and 5% enrollment, with an equity adjustment for CSI/TSI schools.
  - Lists of completed full and targeted/roof-level retrofits.
  - Links the **"Seismic and Seismic Risk Assessment"** (Holmes) as a BoardBook GUID file `f8bb4ec8-…`.
- **Analysis:** two schools on the 2025-bond seismic list also appear in rightsizing Scenario A closures: Rose City Park (full retrofit 2028–29) and Beach (targeted 2028–29). Beach closes in both scenarios and Rose City Park only in A [per `analysis/topics/rightsizing.md`]. Rumors & Facts says bond projects are "not an indicator" of rightsizing status.
- **"Seismic Risk Reduction Plan":** no public document with this title was found on pps.net or bond.pps.net. The term comes from **Resolution 7109** (BoardBook 3988254), which directs the Superintendent to develop one. The closest public documents are the Holmes assessment (BoardBook f8bb4ec8) and the staff memo "2025 Bond Seismic Update" of 2025-09-09 (BoardBook 3990341, already archived). **Gap.**
- **RISE seismic-assessments page** (the legacy Facilities & Asset Management URL redirects there):
  - History: 1995 bond ($47M, 53 schools); 2001 policy; 2002 Pierson study; 2006 DOGAMI; 2009 KPFF; 2012 EPR ratings.
  - Documents: the 2012 Expected Seismic Performance ratings (2 files), the "Facilities Seismic Assessment Document", and a Google Doc listing the City's URM-list school buildings.
- **BAC page:**
  - Members: Greg DiLoreto (Chair), Chris Dunning, Cara Turano, Norm Dowty, Travis George, Ryan Kinsella, Jonathan Truit.
  - Full materials for every meeting from Dec 18, 2024 to Jul 29, 2026, including presentations, status reports, minutes, the PMP v8, HS project management plans, the Year 6 audit and draft charters.
  - Earlier material: 2023–2024 presentations, and BAC Reports #1–#36 (2013–2022) plus #46 (the proposed 2025 bond).
  - **BAC Reports #37–#45 are not listed on the page.** Gap or never posted.
- **External bond performance audits** (`/board/.../external-bond-performance-audits`): audits for 2014–2026 and implementation status reports. "Year 7 & 8" (2026) is posted, with its status ETA February 2027.
- **Office of School Modernization** and **bond history** URLs redirect (302) to RISE and to the PPS Overview page.

## 5. Facilities (RISE and Facilities & Asset Management)

- **RISE** (`/departments/rise`):
  - Staff: Sarah Norman (Exec Dir), Joanna Evenson and TJ Hopkins (Sr Directors), Chris Lueneburg (Comms Dir).
  - PROCEDEO is owner's representative for the "$1.83B bond program budget".
- **Long-Range Facility Plan:** the 2021 LRFP, accepted December 2021, in Vol 1 and Vol 2 plus 5 translations. Contact: Dana White.
- **Building & Asset Condition** (2018 AECOM FCA):
  - 94 sites and 8.1M sq ft; about 7,000 deficiencies.
  - District FCI 0.15 ("Poor"); 62 of 94 sites rated Poor or Critical.
  - Deficiencies estimated at **$614,073,845** (2020 dollars).
  - "Recommendations: Forthcoming."
  - The page refers to "Building Condition Documents" appendices with FCI scores, but **no link exists**. Gap: the per-school FCA/FCI data was not found.
- **Historic Building Assessment (2009):** 1 report plus 98 per-school files. Files for schools named in the rightsizing scenarios are priority 2.
- **Ed Specs:** Education Facilities Vision, plus Comprehensive HS (rev. 2017), MS, K-8 and K-5. These likely contain program-capacity targets and were not read.
- **PPS Maps & Facility Data:**
  - 2026-27 district maps (S/M/L), a focus option/DLI/charter map, and the school board zones map 2022–2032.
  - ArcGIS School Finder (interactive boundary lookup).
  - Employee-only maps.
- **Facilities & Asset Management staff:** Frank Leavitt (Sr Dir Operations), Tim Carman (Dir Facilities Ops), and others.
- **Not found:** any capacity/utilization study page. **Analysis:** utilization figures appear only in the BoardBook rightsizing decks.

## 6. Enrollment & Transfer; Jefferson; SE balancing

- **Jefferson Is Rising** (`/about/portland-public-schools-information/jefferson-is-rising`, alias fs/pages/37708):
  - On **Jan 13, 2026** the Board approved Scenario C.
  - Jefferson dual assignment ends after 2026-27.
  - New Jefferson/Grant/McDaniel/Roosevelt boundaries take effect fall 2027.
  - Under Scenario C, Irvington moves to Grant, and Peninsula plus Beach Spanish Immersion move to Roosevelt.
  - The page has about 45 linked files: Enrollment Scenarios A, B and C plus a summary, methodology, the 11/14/2025 slides, actual and estimated enrollment by year and school, transit analysis, feeder demographics, translations, the Fall Engagement Summary, Board Policy 4.10.045-P, and others. All are in the manifest.
- **Enrollment & Transfer:** Prior Transfer Data (lottery results 2007-08 to 2026-27; 45 files), School Progression Patterns (4 images, 2022), and Policy 4.10.020-P.
- **SE Enrollment & Program Balancing (SEGC, 2020–22):** no current Finalsite page was found; only legacy Centricity PDFs turned up in search. The 2026 equity audit of SEGC is on the rightsizing SEGC page.

## 7. Board

- **Board main page and Board Members:** zones, roles and terms. See `analysis/people/_roster_from_web.md`.
- **Committees for 2026-27:**
  - TLE: chair La Forte; members Splitt and Chase-Miller.
  - FIO: DePass, Chase-Miller and Engelsman.
  - Policy: chair Engelsman; members Sullivan and La Forte.
  - Audit: chair Sullivan; members DePass and La Forte, plus 2 community members.
- **Board Priorities:**
  - 2022–2027 Board Goals (adopted June 2022)
  - Board/Superintendent Operating Protocols (May 2021)
  - Ethics statement
  - Board Leadership Election Process (February 2023)
- The 2026-27 adopted meeting schedule, the Historical List of Board Members and zone maps are also in the manifest.

## 8. Leadership

- **Superintendent's Leadership Team page:** 10 chiefs and 6 advisors.
- **Leadership Org Chart page:**
  - **Proposed 2026-27 chart** (v2026-05-04, effective July 2026)
  - 2025-26 chart (effective July 1, 2025)
  - Org charts for 2018-19 through 2024-25
- The superintendent page links the monthly "Progress Report" newsletters (ParentSquare/Smore). These are not in the manifest; the URLs are in the WebFetch result if needed.

## 9. media.pps.net

- **Press Releases** (9 PDFs; undated on the page): Rightsizing scenarios (2026-10-05), PAT agreement (5/26/26), HS boundary vote (Jan 2026), One North purchase, OSAS gains, Official Bond Statements, and others.
- **"PPS In The News"** shows only the 10 latest items (Aug 10 – Oct 6, 2026). "Load More" has no URL, so **older coverage was not enumerated**.
- **Rumors & Facts:** see §1.
- `https://www.pps.net/news` failed to fetch, so PPS district news posts since 2025-01-01 were **not enumerated**. **Gap.**

## 10. Related external coverage (for `sources/news/`; not in the download manifest)

Found during search. Store metadata only, per CLAUDE.md:
- OPB, 2026-10-05: https://opb.org/article/2026/10/05/portland-public-schools-closures-rightsizing/
- OPB, 2026-10-06: https://opb.org/article/2026/10/06/portland-public-schools-closure-proposals-rightsizing
- OPB, 2026-09-02: https://opb.org/article/2026/09/02/portland-public-schools-rightsizing-close-schools-standardize-education
- OPB, 2026-04-23: https://www.opb.org/article/2026/04/23/portland-public-schools-closing-schools/
- KPTV, 2026-10-07: https://www.kptv.com/2026/10/07/its-betrayal-parents-push-back-against-potential-pps-school-closures-board-meeting/
- KPTV, 2026-09-02: https://www.kptv.com/2026/09/02/portland-public-schools-board-weighs-plan-close-up-20-schools/
- KATU: https://katu.com/news/project-education/pps-is-closing-schools-but-may-not-see-a-big-budget-payoff-heres-why-rightsizing-consolidation-educationbudget-shortfall-deficit-education-students-teachers-parents
- KATU: https://katu.com/news/local/portland-public-schools-board-superintendent-kimberlee-armstrong-has-sobering-conversation-about-school-closure-priorities-declining-enrollment
- WWeek, 2026-04-15, utilization metric: https://www.wweek.com/news/schools/2026/04/15/pps-introduces-another-metric-to-inform-school-closures/
- WWeek seismic series:
  - 2025-05-02: https://www.wweek.com/news/schools/2025/05/02/pps-school-board-members-draft-resolution-to-prioritize-seismic-safety-in-the-bond/
  - 2025-09-10: https://www.wweek.com/news/schools/2025/09/10/portland-public-schools-mulls-seismic-retrofits-amid-plan-for-consolidations
  - 2025-10-10: https://www.wweek.com/news/schools/2025/10/10/ppss-preliminary-seismic-upgrade-plans-leave-some-advocates-shaken/
  - 2025-11-13: https://www.wweek.com/news/schools/2025/11/13/updated-pps-seismic-formula-prioritizes-risk/
  - 2026-01-22: https://www.wweek.com/news/schools/2026/01/22/pps-moves-forward-on-seismic-retrofits-despite-pushback/
- WWeek Jefferson coverage: 2025-06-06, 2025-09-20, 2025-11-17 and 2025-12-10 (URLs under `wweek.com/news/schools/`); OPB 2025-10-30.
- 2025 bond passage: OPB 2025-05-20 (https://www.opb.org/article/2025/05/20/oregon-may-2025-special-election-results-voting-ballot-school-bond/) and WWeek 2025-05-20.
- Board election, May 2025: https://www.wweek.com/news/schools/2025/05/20/splitt-chase-miller-la-forte-and-engelsman-lead-portland-school-board-races/
- A KATU-hosted copy of the SEGC Equity Audit report: https://katu.com/resources/pdf/55ebca04-2231-4d30-a4c1-421b467ff162-File_SEGCEquityAuditEvaluationReport.pdf

## 11. Could not retrieve / gaps (summary)

1. **Per-school "How could your school be impacted?" documents for 81 schools.** No links appear in the HTML, so a real browser is needed.
2. The **Scenario Drive PDFs** (overview plus 4 regions) were not readable via WebFetch.
3. `enrollment-and-systems-planning` is passkey-gated.
4. `/rightsize/English` (poll), `https://www.pps.net/page/954` and `https://www.pps.net/news` all returned fetch errors.
5. No FCA "Building Condition Documents" or FCI appendix links; no capacity/utilization study; no public "Seismic Risk Reduction Plan" document.
6. No 2026-27 Adopted Budget link; the budget calendar page is empty.
7. BAC Reports #37–#45 are missing from the BAC archive listing.
8. Older media.pps.net coverage ("Load More") and pps.net news posts were not enumerated.
9. The Google Slides deck from 9/8/2026 needs a real browser or export to confirm it is public.
