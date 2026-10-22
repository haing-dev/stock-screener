#!/usr/bin/env bash
# ARCHIVED with the v2.9 portal (2026-10-22): only the archived workflows call this.
# Publish after a run:
#  1. commit data/ (company descriptions + the portal's public salt) to the main branch, retrying on conflicts
#  2. force-push the built site (site/, with the encrypted data files) to branch 'site' as a single commit,
#     which Cloudflare Pages deploys. One commit, no history, so the repository doesn't grow every day.
set -euo pipefail
msg="$1"
git config user.name "screener-bot"
git config user.email "screener-bot@users.noreply.github.com"

if [ -d data ]; then git add data; fi
if ! git diff --cached --quiet; then
  git commit -q -m "$msg"
  ok=0
  for i in 1 2 3; do
    if git push -q; then ok=1; break; fi
    git pull --rebase -q || git rebase --abort || true
    sleep 3
  done
  if [ "$ok" != 1 ]; then echo "::error::could not push data/ to the main branch"; exit 1; fi
fi

if [ ! -f archive/portal-v2.9/site/data/meta.bin ]; then
  echo "No portal data was built - nothing to publish."
  exit 0
fi
tmp="$(mktemp -d)"
cp -r archive/portal-v2.9/site/. "$tmp/"
cd "$tmp"
git init -q -b site
git add -A
git -c user.name=screener-bot -c user.email=screener-bot@users.noreply.github.com commit -q -m "$msg"
git push -q -f "https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git" site
echo "Published the portal to branch 'site'."
