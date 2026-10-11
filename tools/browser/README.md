# Browser collectors

These scripts run inside a real browser tab: the DevTools console, or a browser-automation tool's "run JavaScript".
They run on the site being collected, so requests are same-origin and use the browser's normal network access.
Results download as store-only zip batches. Each zip contains `_manifest_<name>.json` with the URL, final URL, HTTP
status, content type, bytes and fetch time of every file. See `../../RUNBOOK.md` for the full procedure.

| File | Run on | Provides |
|---|---|---|
| `zipdl.js` | any site being collected | `__zipdl3(items, zipName)` zips `{url, save_as}` items and fixes file extensions by content type. `__runBatch(manifestUrl, hosts, start, count, zipName)` downloads a slice of `sources/pps_net/_download_manifest.jsonl`. |
| `boardbook_crawl.js` (load `zipdl.js` first) | meetings.boardbook.org | `__bbIndex(since)` builds the meeting list with videos and agenda attachments. `__bbSaveIndex(idx)` saves it. `__bbFetch(idx, {only})` downloads agenda, minutes, notice and supplementals pages plus every attachment and minutes PDF, one zip per meeting. |
| `youtube_captions.js` | youtube.com (foreground tab) | `__queue([[videoId, "date\|meetingId"], ...])` captures the full English caption track for each video into IndexedDB. `__next()` exports one record at a time as `REC\|id\|base64gzip` for `tools/ingest_transcript_exports.py`. |
