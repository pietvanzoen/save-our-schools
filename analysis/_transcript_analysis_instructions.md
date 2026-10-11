# Transcript analysis instructions (for meeting-analysis agents)

Read `/home/claude/pps/CLAUDE.md` first; its citation and quoting rules apply.

## Inputs per meeting
- Transcript: `sources/youtube/transcripts/<date>_<videoId>.txt`, one caption line per row: `[H:MM:SS] text`.
  These are YouTube auto-captions: no speaker labels, frequent mis-hearings, especially of names.
  Common caption errors: "director" = board member title (PPS board members are addressed as "Director <Lastname>");
  names get mangled (e.g. "La Forte" → "laforte"/"la Fort", "Engelsman" → "Engleman", "DePass" → "the pass",
  "Brim-Edwards" → "brim Edwards", "Armstrong" → "arm strong"). Use the roster to normalize.
- Meeting metadata: `sources/youtube/transcripts/<date>_<videoId>.meta.json` (lists the BoardBook meeting id(s)).
- Agenda / minutes / attachments: `sources/boardbook/meetings/<date>_<meetingId>_*/` (`meeting.json`, `agenda.md`,
  `minutes_*.pdf.txt` when posted, `attachments/*.pdf.txt`). Minutes record motions, votes and who moved them:
  use them to anchor attribution and outcomes.
- Roster of board members and staff: `analysis/people/_roster_from_web.md` (board composition changed in 2025:
  check dates). Staff often introduce themselves or are introduced by the superintendent or chair.

## Speaker attribution
- The chair recognizes speakers ("Director Sullivan", "Director La Forte, go ahead", "I'll turn it over to Dr. ...").
  Attribute the following passage to that person until another recognition or a clear change of speaker.
- Self-identification ("This is Margaret Calvert, ...") is strong evidence.
- Roll-call votes: the clerk calls names and each member answers. Use these to learn who is present.
- Give every quote `confidence`: high / medium / low, plus `attribution_evidence` (e.g. "recognized by chair at 1:02:10").
  Do not include low-confidence quotes in the summary prose; keep them in the JSONL with confidence low.

## Prioritize
Spend most effort on segments about rightsizing / school closures / consolidation / boundaries / grade configuration /
enrollment balancing / Jefferson enrollment scenarios, the 2025 bond, seismic retrofits, facilities and capacity,
budget deficits and cuts as they relate to school size or closures, enrollment forecasts, and board deliberation and
votes on these. Procedural items (minutes adoption, routine contracts, ceremonial recognitions) get one line in the
summary at most. Public comment: summarize themes, counts and schools mentioned; do not attribute quotes to members
of the public by name (record them as "public commenter (affiliation if stated)").

## Outputs (write ONLY these paths; others are written by other agents)
1. `analysis/meetings/<date>_<videoId>.md`, one per transcript, containing:
   - header: title, date, BoardBook meeting link(s), video URL, duration, attendees (if determinable)
   - **Summary** (5–15 bullets), **Decisions & votes** (with tallies from the minutes if available),
     **Rightsizing / closures** segment notes, **Bond / seismic / facilities** notes, **Budget & enrollment** notes,
     **Public comment themes**, **Notable quotes** (pointing to the JSONL), and a **Topics index** listing
     timestamp ranges per agenda item, e.g. `0:41:10–1:35:00 Rightsizing update (Calvert presentation, board Q&A)`.
   - Every claim timestamped `[YT:<videoId>@H:MM:SS]`, with a link form `https://www.youtube.com/watch?v=<id>&t=<sec>s`
     for the most important moments.
2. `analysis/people/quotes/<your batch id>.jsonl`, one JSON object per quote:
   `{"person": canonical full name, "role": "board member|board chair|superintendent|staff: <title>|student rep",
     "date": "YYYY-MM-DD", "meeting_id": BoardBook id, "video_id", "timestamp": "H:MM:SS", "seconds": int,
     "url": "https://www.youtube.com/watch?v=<id>&t=<sec>s", "quote": verbatim caption text (minimal [bracketed] fixes),
     "paraphrase": one-sentence plain-English meaning, "topics": [rightsizing|closures|boundaries|grade_config|
     enrollment|bond|seismic|facilities|budget|equity|engagement|process|governance|labor|other],
     "stance": what position this expresses (e.g. "supports closing small schools", "wants criteria approved before scenarios"),
     "attribution_evidence": "...", "confidence": "high|medium|low"}`
   Aim for the quotes that best reveal each person's reasoning, priorities, concerns, and positions, especially
   statements that show support, opposition, conditions, or changes of mind. Typically 10–60 quotes per substantive
   meeting; fewer for short committee meetings.
3. `analysis/people/quotes/<your batch id>_notes.md`: your observations on each person's evolving positions within
   your date range, attribution problems, and caption errors you corrected.

Do not run git. Verify every quote string appears in the transcript (allowing only bracketed repairs) before finishing.
Your final reply should be brief: counts of meetings summarized and quotes extracted, plus the 5 most important findings.
