#!/bin/bash
# Commit and push new/changed BoardBook meeting folders in chunks of <= ~350MB, so no single push is too large
# for GitHub. Run from anywhere: tools/push_chunks.sh   (optional: COMMIT_TRAILER="Co-Authored-By: ..." env var)
# Files over 100MB must be split first: python3 tools/split_large.py sources/ 95
cd "$(dirname "$0")/.." || exit 1
limit=$((350*1024*1024)); acc=0; batch=()
flush(){ [ ${#batch[@]} -eq 0 ] && return
  git add -- "${batch[@]}"
  git commit -qm "BoardBook: ${batch[0]##*/meetings/} .. ${batch[-1]##*/meetings/}${COMMIT_TRAILER:+

$COMMIT_TRAILER}"
  git push -q origin main 2>&1 | grep -v -e 'expected .acknowledgments' -e 'push negotiation failed'
  echo "pushed ${#batch[@]} folders $((acc/1024/1024))MB"; batch=(); acc=0; }
for d in sources/boardbook/meetings/*/; do
  d=${d%/}
  [ -z "$(git status --porcelain -- "$d")" ] && continue
  s=$(git status --porcelain -uall -- "$d" | awk '{print $2}' | xargs -d '\n' du -cb 2>/dev/null | tail -1 | cut -f1)
  if [ $((acc+s)) -gt $limit ]; then flush; fi
  batch+=("$d"); acc=$((acc+s))
done
flush
