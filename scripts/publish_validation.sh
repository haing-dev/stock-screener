#!/usr/bin/env bash
# Commit validation/out (report, statistics, raw lists and returns, audit sheets) to the branch 'validation'.
# Append-only (no force push): each run is one commit, so earlier results stay in the history.
set -euo pipefail
[ -d validation/out ] || { echo "nothing to publish"; exit 0; }
repo="https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"
for attempt in 1 2 3; do
  tmp="$(mktemp -d)"
  if ! git clone -q --depth 1 --branch validation "$repo" "$tmp" 2>/dev/null; then
    git -C "$tmp" init -q -b validation
    git -C "$tmp" remote add origin "$repo"
  fi
  mkdir -p "$tmp/out"
  cp -r validation/out/. "$tmp/out/"
  cp validation/PROTOCOL.md validation/freeze.json validation/CHANGES.md "$tmp/" 2>/dev/null || true
  git -C "$tmp" add -A
  if git -C "$tmp" diff --cached --quiet; then echo "no change"; exit 0; fi
  git -C "$tmp" -c user.name=screener-bot -c user.email=screener-bot@users.noreply.github.com \
    commit -q -m "Validation $(date -u +%Y-%m-%d)"
  if git -C "$tmp" push -q origin validation; then echo "published to branch validation"; exit 0; fi
  sleep $((attempt * 5))
done
echo "::warning::could not publish to branch validation"
