# OPB audio

Broadcast audio added to the archive by the repository owner. Provenance and checksums are in `_manifest.json`.

| File | Program | Air date | Length | Guest (per OPB page) |
|---|---|---|---|---|
| `2026-10-13_think-out-loud_pps-closures_eddie-wang.mp3` | Think Out Loud: "Many PPS families asking for a pause in school closures process" ([OPB page](https://www.opb.org/article/2026/10/13/think-out-loud-portland-public-schools-pps-closures/)) | 2026-10-13 | 50:51 | Eddie Wang, PPS Board chair, plus listener calls |
| *(no audio; transcript only)* `2026-10-16_think-out-loud_pps-closures_kimberlee-armstrong.transcript.txt` | Think Out Loud: "Portland Public Schools Superintendent answers questions about proposed school closures" ([OPB page](https://www.opb.org/article/2026/10/16/portland-public-schools-superintendent-answers-questions-about-proposed-school-closures/)) | 2026-10-16 | about 15 min (not stated) | Kimberlee Armstrong, PPS Superintendent, plus two listener voicemails and an emailed question |

## Transcripts

- Raw export (primary transcript, never edit): `2026-10-13_think-out-loud_pps-closures_eddie-wang.transcript.json`
  (machine speech-to-text with automatic speaker separation, supplied by the repository owner; 208 segments with word timestamps).
- Corrected, speaker-labeled copy: `analysis/audio_transcripts/2026-10-13_opb-think-out-loud_eddie-wang.txt`, built by
  `python3 tools/audio_transcript.py` (see the script header). Speaker identification with evidence and confidence:
  `analysis/audio_transcripts/speakers_2026-10-13_opb-think-out-loud.csv`; every correction: `corrections_2026-10-13_opb-think-out-loud.csv`.
- Cite as `[AUDIO:opb/2026-10-13_think-out-loud_pps-closures_eddie-wang@H:MM:SS]` (turn start). `tools/search.py` indexes the corrected copy.

### Oct 16, 2026 (Kimberlee Armstrong): transcript only

- Raw transcript (primary, never edit): `2026-10-16_think-out-loud_pps-closures_kimberlee-armstrong.transcript.txt`. Plain text, speaker-labeled, no timestamps;
  supplied by the repository owner 2026-10-16. Its producer isn't stated and no audio is archived, so it can't be checked against the broadcast.
- Corrected, speaker-labeled copy: `analysis/audio_transcripts/2026-10-16_opb-think-out-loud_kimberlee-armstrong.txt`, built by `python3 tools/text_transcript.py`.
- Cite as `[AUDIO:opb/2026-10-16_think-out-loud_pps-closures_kimberlee-armstrong@L<n>]`, where n is the raw-transcript line where the turn starts (the `[L<n>]` prefix in the corrected copy).

As with YouTube captions, the words are machine transcription: check the audio before quoting anything that matters,
especially numbers. Callers are members of the public: describe them, don't name them.
