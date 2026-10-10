#!/usr/bin/env bash
# Keep only the newest GitHub Actions cache entry for each key prefix given (each run saves a new entry; old copies
# would otherwise fill the 10 GB cache limit and push out the SEC data). Needs GH_TOKEN with actions: write.
set -uo pipefail
for prefix in "$@"; do
  ids="$(gh cache list --key "$prefix" --sort created_at --order desc --limit 100 --json id --jq '.[1:][].id' 2>/dev/null || true)"
  n=0
  for id in $ids; do gh cache delete "$id" >/dev/null 2>&1 && n=$((n+1)); done
  echo "cache $prefix: $n older copies deleted"
done
exit 0
