#!/usr/bin/env python3
"""Print a window of a meeting transcript around a timestamp, to read context and check who is speaking.

Usage:  python3 tools/window.py <videoId> <H:MM:SS> [minutes_before] [minutes_after] [--raw]
Reads the corrected copy (analysis/transcripts_corrected/, caption name fixes in [brackets]) when it exists;
--raw shows the original captions from sources/youtube/transcripts/.
        python3 tools/window.py zOUH2Jq7Owo 2:23:24          # default 2 min before, 2 min after
        python3 tools/window.py zOUH2Jq7Owo 2:23:24 0.5 4
Each output line is "[H:MM:SS] caption text  <youtube link>" (the link is printed every ~30 s).
Lines containing "Director", "Chair", "thank you", or a self-introduction are marked with ">" because they often
signal a change of speaker.
"""
import re, signal, sys
signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # quiet when piped to head
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def secs(t):
    parts = [int(x) for x in t.split(":")]
    while len(parts) < 3: parts.insert(0, 0)
    return parts[0] * 3600 + parts[1] * 60 + parts[2]

def main():
    args = [a for a in sys.argv[1:] if a != "--raw"]
    vid, ts = args[0], args[1]
    before = float(args[2]) if len(args) > 2 else 2
    after = float(args[3]) if len(args) > 3 else 2
    raw = "--raw" in sys.argv
    files = [] if raw else list((ROOT / "analysis/transcripts_corrected").glob(f"*_{vid}.txt"))
    files = files or list((ROOT / "sources/youtube/transcripts").glob(f"*_{vid}.txt"))
    if not files: sys.exit(f"no transcript for {vid} (see sources/youtube/videos_index.csv)")
    t0, lo, hi = secs(ts), secs(ts) - before * 60, secs(ts) + after * 60
    print(f"# {files[0].relative_to(ROOT)}  window {ts} -{before}m/+{after}m")
    last_link = -999
    for line in files[0].read_text().splitlines():
        m = re.match(r"\[(\d+:\d\d:\d\d)\] (.*)", line)
        if not m: continue
        s = secs(m.group(1))
        if s < lo or s > hi: continue
        mark = ">" if re.search(r"\bdirector\b|\bchair\b|thank you|my name is|\bI'm \w+ \w+,", m.group(2), re.I) else " "
        link = ""
        if s - last_link >= 30:
            link = f"  https://www.youtube.com/watch?v={vid}&t={s}s"; last_link = s
        print(f"{mark}[{m.group(1)}] {m.group(2)}{link}")

if __name__ == "__main__":
    main()
