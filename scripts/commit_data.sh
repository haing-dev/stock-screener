#!/usr/bin/env bash
# Commit data/ (company descriptions) to the main branch, retrying on conflicts.
set -euo pipefail
msg="$1"
git config user.name "screener-bot"
git config user.email "screener-bot@users.noreply.github.com"
git add data
if git diff --cached --quiet; then echo "data/ unchanged"; exit 0; fi
git commit -q -m "$msg"
for i in 1 2 3; do
  if git push -q; then echo "data/ committed"; exit 0; fi
  git pull --rebase -q || git rebase --abort || true
  sleep 3
done
echo "::error::could not push data/ to the main branch"; exit 1
