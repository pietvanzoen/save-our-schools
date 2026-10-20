# RUNBOOK: refreshing and rebuilding the archive

**Answering questions from the archive needs none of this.** Use `.claude/skills/pps-research/SKILL.md`.
This runbook is for collecting new source material (new meetings, transcripts, documents) and updating the analysis.

## 0. What you need

| Need | Why |
|---|---|
| A real browser that can reach meetings.boardbook.org, www.pps.net, bond.pps.net, youtube.com, drive.google.com and web.archive.org | Cloud sandboxes usually can't reach these sites. Collection runs as JavaScript in a browser tab (DevTools console, or a browser-automation tool's "run JavaScript"). |
| Chrome download settings: a fixed download folder, "Ask where to save each file" **off**, and "Automatic downloads" allowed for each site above | The collectors save zip batches without a dialog per file |
| A foreground tab for YouTube work | Background tabs throttle timers and captures stall |
| Python 3 with `beautifulsoup4`; `poppler-utils` (pdftotext, pdftoppm); `tesseract-ocr`; `qpdf`; `git` | Processing scripts in `tools/` |
| Push access to github.com/timaelliott/save-our-schools | Commits |

GitHub rejects files over 100 MB. Run `python3 tools/split_large.py sources/ 95` before committing new big files. It
splits by page with qpdf for PDFs and in byte chunks otherwise, and writes a `*.SPLIT.md` with sha256 and rejoin steps.

## 1. Routine refresh after new meetings (most common)

Do this after each board meeting, and once a month to pick up newly posted minutes.

### 1a. BoardBook (agendas, attachments, minutes)
1. Open https://meetings.boardbook.org/Public/Organization/915 and paste `tools/browser/zipdl.js`, then `tools/browser/boardbook_crawl.js`, into the console.
2. Build the index:
   ```js
   const idx = await __bbIndex('2025-01-01'); __bbSaveIndex(idx);
   ```
3. Decide which meetings to fetch: any meeting id not yet in `sources/boardbook/meetings_index.csv`, plus recent meetings
   whose `minutes_url` was empty (their minutes may have been posted since). Then:
   ```js
   await __bbFetch(idx, {only:['<id>','<id>']}); __bbstat
   ```
4. Unzip into `sources/`, keeping provenance:
   ```bash
   cd sources && for z in ~/Downloads/bb_*.zip ~/Downloads/boardbook_index.zip; do unzip -o "$z"; done
   mv _manifest_*.json boardbook/_manifests/
   ```
   Re-fetching a meeting overwrites its HTML pages. That's intended (minutes get added), and nothing else in the folder is touched.
5. Process the files:
   ```bash
   python3 tools/parse_boardbook.py                 # meeting.json, agenda.md, minutes.md, meetings_index.csv
   python3 tools/extract_pdf_text.py sources/boardbook
   python3 tools/ocr_pdfs.py sources/boardbook      # OCR for scanned PDFs (writes .pdf.ocr.txt)
   python3 tools/build_attachment_index.py
   ```

**Without a browser (Python, any machine that can reach BoardBook):** `tools/boardbook_crawl.py` does the same as the
JS crawler. It writes the files and a per-meeting manifest under an output folder that mirrors `sources/`:
```bash
python3 tools/boardbook_crawl.py OUT --index sources/boardbook/boardbook_index_2025_2026.json --only <id> <id>
```
Bring it in with `python3 tools/safe_copy.py OUT` (never plain `cp`). Changed files are moved to `_prior/` first and
logged in `sources/_versions_log.csv`. Then run `python3 tools/check_upstream.py --log` on the same machine. It records
documents PPS has deleted in `sources/_removed_upstream.csv`, and `build_attachment_index.py` keeps those archived copies
indexed with the tag `unlisted_upstream`. PPS deleted the Oct 20, 2026 Board question tracker a day after posting it.
Older note on copying `OUT/boardbook/meetings/*`: Copy the new index over the old one, keeping any
extra keys the old one had (`supp`, `minutesFiles`). Save each manifest as `_manifest_bb_<id>_<date>.json` so earlier
manifests aren't overwritten. Then run step 5. The 2026-10-18 refresh ran this from the owner's computer, because the
cloud sandbox cannot reach BoardBook.

### 1b. Meeting video transcripts
1. Find new videos: the `vids` in the index, compared with `sources/youtube/videos_index.csv`.
2. On any youtube.com page, in a foreground tab, paste `tools/browser/youtube_captions.js` and run:
   ```js
   __queue([["<videoId>","<YYYY-MM-DD>|<boardbookMeetingId>"], ...]);   // check progress with __q
   await __next()   // repeat until 'NONE'; save every returned REC| line into a text file
   ```
   Records are stored in IndexedDB as they finish, so a reload loses nothing. Re-paste the script and keep calling `__next()`.
3. Ingest the records:
   ```bash
   python3 tools/ingest_transcript_exports.py exports.txt
   ```
   This writes the transcript `.txt/.tsv/.meta.json` files and rebuilds `videos_index.csv`.
   Alternative used on 2026-10-18: run `yt-dlp --skip-download --write-info-json` for each video. Download the
   `automatic_captions['en-orig']` json3 URL from the info JSON, then build the same record (`tsv` lines of
   `tStartMs\tdDurationMs\ttext`, `meta`, `meetings`, `caption_kind`, `fetch_method`) and pass a JSON list to
   `tools/write_transcripts.py`. YouTube returns 429 if you go fast, so pause a few seconds between videos.
4. Check that the first lines are English. The script forces `lang=en`, but verify anyway.

### 1c. Corrected transcripts and search
```bash
python3 tools/caption_fixes.py --stats    # regenerates analysis/transcripts_corrected/ (name fixes in [brackets])
python3 tools/search.py --rebuild
```
If a new transcript shows a new mis-hearing of a name (check `--stats` and skim the new files), add a rule to
`RULES` in `tools/caption_fixes.py` and re-run. Rules must be unambiguous. Use the title-only scope for words that are
also ordinary English ("split", "pass", "green").

### 1d. Update the analysis (per new meeting)
1. **Meeting summary and quotes.** Follow `analysis/_transcript_analysis_instructions.md`. Use the next batch id
   (e.g. `batch11`). This writes `analysis/meetings/<date>_<vid>.md`, `analysis/people/quotes/batch11.jsonl` and `batch11_notes.md`.
2. **Merge quotes:**
   ```bash
   python3 tools/merge_quotes.py analysis/people/quotes/batch11.jsonl          # dry run
   python3 tools/merge_quotes.py analysis/people/quotes/batch11.jsonl --write  # append verified quotes
   ```
   Every quote must be found verbatim in its transcript. Fix failures in the batch file, never in the transcript.
3. **Downstream files:**
   - Add rows to `analysis/people/positions_timeline.csv` and a dated entry in each affected `analysis/people/<slug>.md`.
   - For each director, add dated points to `analysis/board_closure_stance/<slug>.md` and `<slug>_scores.csv` following
     `analysis/board_closure_stance/_instructions.md`, then rebuild `all_scores.csv`:
     `head -1 x_scores.csv > all_scores.csv; tail -qn +2 *_scores.csv >> all_scores.csv`
   - Update `analysis/timeline.md`, the affected `analysis/schools/<slug>.md`, `analysis/topics/*`, and `analysis/BRIEFING.md` if the picture changed.
4. **Verify.** Have someone (or a separate agent that didn't write it) spot-check new claims against sources, as
   `analysis/_verification_report.md` did. Then republish any pages listed in `analysis/_published_pages.md` that depend on the changes.

### 1e. Commit
```bash
tools/push_chunks.sh          # commits and pushes new BoardBook folders in <=350 MB chunks
git add sources/youtube analysis tools && git commit -m "Refresh: <meetings>" && git push
```

## 2. Other sources

### pps.net and bond.pps.net files
- `sources/pps_net/_download_manifest.jsonl` lists every known URL (`url, title, found_on, section, kind, topic, school_year, priority, save_as`).
  Add new pages or files there first.
- On a page of the same site, paste `tools/browser/zipdl.js` and run:
  ```js
  await __runBatch('https://raw.githubusercontent.com/timaelliott/save-our-schools/main/sources/pps_net/_download_manifest.jsonl', ['www.pps.net','resources.finalsite.net'], 0, 60, 'ppsnet_00.zip');
  __bstat
  ```
  Repeat with `start` advanced by 60. Use `['bond.pps.net']` on bond.pps.net. Fetches use default credentials:
  `credentials:'include'` breaks the cross-origin redirect to finalsite.
- Unzip into `sources/` and move `_manifest_*.json` into the matching `_manifests/` folder. Then run
  `python3 tools/extract_pdf_text.py sources/pps_net` (or `sources/bond`).

### Google Drive files (linked from bond.pps.net)
Drive blocks `fetch` (CORS). From a drive.google.com tab, create one hidden iframe per file with
`src = https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t`. Each iframe triggers a normal
download. Google Docs and Slides export via `https://docs.google.com/document/d/<ID>/export?format=pdf` (or
`/presentation/d/<ID>/export/pdf`). Record id → title → URL in `sources/pps_net/_manifests/_google_files_manifest.json`.

### Dead pages (Internet Archive)
From a web.archive.org tab, query `https://archive.org/wayback/available?url=<url>`, then fetch the raw snapshot
`https://web.archive.org/web/<timestamp>id_/<url>` (the `id_` suffix returns the original bytes) and zip it with
`__zipdl3`. Record the snapshot URL as the source in `_manifest_wayback_retry.json`.

### News
News articles are added by hand to `sources/news/index.jsonl`:
- Each record holds metadata, a summary in your own words, `key_facts`, and at most short quotes (under 25 words, attributed).
- Never store full article text.
- The Oregonian blocks automated fetching. Read it only in a logged-in subscriber browser, one page at a time with ~35 s between pages, and stop at any "Access is temporarily restricted" page or CAPTCHA (a fast crawl triggers a block). Then merge with `python3 tools/merge_news.py records.json --write` (keeps existing ids, checks quote length).

## 3. Full rebuild from scratch
Run section 1 with `__bbFetch(idx)` (all meetings) and the full video list. Then run section 2 for pps.net, bond, Drive and
Wayback, using the manifests already in the repo. Then process the files and re-run analysis agents per
`analysis/_transcript_analysis_instructions.md` and `analysis/board_closure_stance/_instructions.md`. Expect hundreds of
zip batches (about 4 GB). The original run is described in `README.md` under "Collection method".

## 4. Lessons from the first build
- **BoardBook minutes and notice pages are viewer shells.** The PDF id is in `NewDocumentViewerDocumentID`.
- **Pick the English caption track explicitly.** YouTube's `captionTracks[0]` can be an auto-translated language.
- **Export transcripts as they finish**, never all at once at the end. A page reload once wiped in-memory results.
- **Keep each tool output under ~300k characters.** Browser-automation tools truncate larger results, so export one record per call.
- **Large zips are a problem.** A 446 MB zip exceeded one transfer limit; fetch big files individually.
- **Data & Reporting PDFs have space-aligned columns.** Check column positions against the rendered page before quoting a number.
- **If browser downloads stop arriving** (Chrome reports a saved zip but nothing lands in the folder), don't hand-copy page HTML. As a stopgap:
  - extract PDF text in the page with pdf.js and save it as `<id>_<name>.pdf.txt`;
  - rebuild a reduced `agenda.html` holding only the agenda rows;
  - log both as TEXT ONLY / REDUCED in a `_manifests/_manifest_refresh_<date>.json`.

  Fetch the real files on the next refresh. The 2026-10-12 refresh did this for meetings 771664 and 771676.
- **OregonLive pages carry a reCAPTCHA notice** in a poll footer, so a bare `/captcha/` test gives a false alarm. Test for "Access is temporarily restricted", or check whether the article body is missing.
