#!/usr/bin/env bash
# Append the run's list snapshot(s) in history_out/ to the branch 'history' (append-only: never force-pushed, so
# every published list keeps its date in git). Creates the branch on first use. Retries on concurrent pushes.
set -euo pipefail
shopt -s nullglob
files=(history_out/*.json.gz)
if [ ${#files[@]} -eq 0 ]; then echo "no list snapshot to append"; exit 0; fi
repo="https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"
for attempt in 1 2 3 4 5; do
  tmp="$(mktemp -d)"
  if git clone -q --depth 1 --branch history "$repo" "$tmp" 2>/dev/null; then
    :
  else
    git -C "$tmp" init -q -b history
    git -C "$tmp" remote add origin "$repo"
    printf '%s\n' "# Forward record" "" \
      "Append-only log of every list the screener published (validation/PROTOCOL.md section 7)." \
      "One file per run: lists/YYYY/<date>_<kind>.json.gz. Never rewritten." > "$tmp/README.md"
  fi
  for f in "${files[@]}"; do
    y="$(basename "$f" | cut -c1-4)"
    mkdir -p "$tmp/lists/$y"
    cp "$f" "$tmp/lists/$y/"
  done
  git -C "$tmp" add -A
  if git -C "$tmp" diff --cached --quiet; then echo "lists already recorded"; exit 0; fi
  git -C "$tmp" -c user.name=screener-bot -c user.email=screener-bot@users.noreply.github.com \
    commit -q -m "Lists $(basename "${files[0]}" .json.gz)"
  if git -C "$tmp" push -q origin history; then echo "lists appended to branch history"; exit 0; fi
  echo "push rejected (attempt $attempt) - retrying"
  sleep $((attempt * 5))
done
echo "::warning::could not append the lists to branch history"
exit 0
