# Stock screener: handoff for new sessions

Read this first. User preference: be concise and direct; use only context from the current chat + this repo.
From 2026-10-22 Claude handles GitHub and Cloudflare (push, runs, deploys); the user only chats for adjustments.
Control without a gh token: commit to `triage/` or `triage/settings.json` (step, history_years, per_minute) -> the
Triage workflow runs; read results with `git fetch origin triage-status && git show origin/triage-status:status.md`.

## Hard rules (security)
- Twelve Data key and SEC user agent (name/email) are PRIVATE. Locally they live only in `local_settings.json` (never in repo, outputs, artifacts or chat).
- Online they are GitHub repository secrets: SEC_USER_AGENT, MASSIVE_API_KEY, TWELVEDATA_API_KEY, PORTAL_PASSWORD, CLAUDE_CODE_OAUTH_TOKEN (user's subscription; no ANTHROPIC_API_KEY set).
- Never ask the user to paste keys/tokens into chat. Never drag the PC project folder into GitHub.

## What it is now: Quality Triage (triage/ v1.0.0, built 2026-10-22)
- The 14-screen portal is ARCHIVED (`archive/portal-v2.9/`: its site and workflows; nothing deleted; `qs/` code still used).
- `triage/` = three event-driven US-stock screens in the shape of the biotech crash/slide triage (repo haing-dev/crash-triage):
  Scans twice a month (15th and month-end). Hidden Earnings (close 40%+ below 12-month high), Emerging Compounders and
  Core Compounders (earnings yield enters the cheapest fifth of own last 5 years or of industry peers). Rules, weights, thresholds: `triage/rules.py`
  (pre-registered 2026-10-22; log changes in `triage/CHANGES.md`). Backend requirements (US 10-K filer, history, recent
  report, size, volume, leverage) never enter the score. Calls: weighted cells -> Buy candidate / Watch / Avoid (+ hard
  Avoid; Watch -> Buy on a top performer owner's later 13F). Cells shared by all three: High Conviction Owners, Top
  Performer Owners, Insider Buy/Sell.
- Data: point-in-time panel from the v2.9 backtest code (`qs/backtest.contexts_at`, Massive month-end grid, SEC bulk facts
  filed before each month-end); 13F and insider SEC data sets (`triage/owners.py`); returns open-to-open incl. delistings.
  Outcome: 12-month return vs 10 most similar US stocks + SPY (IWM for Emerging); FF5+UMD calendar-time regression.
- Run: `python -m triage.run auto|monthly|daily|<step>` (workflow `.github/workflows/triage.yml`, weekdays 23:43 UTC and on
  push to triage/; full scan once a scan date has settled 3 days, else daily mark + rebuild). Site -> branch `site` (same Cloudflare Worker, password = PORTAL_PASSWORD).
  Live calls -> branch `triage-record` (append-only ledger.csv). Old site kept on branch `site-archive-v2.9`.
- Massive plan sets the backtest length: free = 2 years of prices, a rolling window back from today (~1 year of
  results, own-past cheapness mostly N/A); Starter $29/mo 5 years, Developer $79/mo 10 years (set history_years and
  per_minute=100 in triage/settings.json). User chose 2 years (free) for now.
- Local preview: `python tests/triage_smoke.py --demo OUT_DIR` (real SEC samples, invented prices/13F/insiders).
- Tests: `python3 tests/run_tests.py` must print "ALL TESTS PASSED" (includes tests/triage_smoke.py).
- Archived but kept: v2.9 validation of the frozen 14 screens (`validation/PROTOCOL.md`, `qs/validate.py`; workflow archived).

## Macro Compass (macro/ v1.0.0, built 2026-10-23)
- Stage of the US cycle (Expansion / Late cycle / Contraction / Recovery) + 20 industry ETFs at risk / in favour at
  6 and 12 months, from 38 investor-cited indicators (research store + X posts of @AtlasShrug1). Point in time,
  walk-forward odds, ETF backtest from 2006 vs equal weight / momentum / trend / SPY. Details: macro/README.md.
- Workflow `.github/workflows/macro.yml` (weekdays 22:17 UTC; push to macro/). Page: its OWN Cloudflare Worker
  "macro-compass" built from branch `macro-site` (force-pushed; wrangler.jsonc + .assetsignore written by macro/site.py).
  NOT on the stock-screener site (https://stock-screener.haing-penn.workers.dev/ is used for another build - don't touch).
  No password (public, noindex). Branches: `macro-data` (raw downloads, force-pushed),
  `macro-status` (last run log: `git fetch origin macro-status && git show origin/macro-status:status.md`),
  `macro-record` (append-only monthly calls from Oct 2026). Secret FRED_API_KEY (user adds) = first-published data.
- Rules: macro/registry.py (pre-registered; changes -> new VERSION + macro/CHANGES.md).

## Deployment
- Repo `haing-dev/stock-screener` (private). Branches: `main` (code), `site` (published triage site, force-pushed), `site-archive-v2.9` (last portal build), `triage-record` (live calls, append-only), `triage-status` (last run's log tail + counts, force-pushed), `reports`, `research` (transcript store), `history` and `validation` (v2.9 records, no longer updated).
- Cloudflare **Worker** "stock-screener" via Workers Builds on branch `site` (wrangler.jsonc written by `triage/site.py`).
- Workflows: triage.yml and macro.yml. The old screen/daily/background/report/validate workflows are in `archive/portal-v2.9/workflows/`.
- In the cloud sandbox: blob log downloads are forbidden; `scripts/run_logged.sh` puts the last 60 log lines in check-run annotations (`gh api repos/haing-dev/stock-screener/check-runs/<id>/annotations`).

## Research store (`research` branch)
`git clone -q -b research --single-branch https://github.com/haing-dev/stock-screener research` → read its CLAUDE.md.
253 transcripts + Doc 1/Doc 2 notes, `scripts/search.py` (`--collection`, `--screen`), `scripts/ingest.py <drive folder>`. Source folders on the user's PC: `G:\My Drive\Transcripts\` YouTube Transcripts (general), Healthcare Transcripts, Macro Transcripts (Crypto, Real Estate skipped); screen -> collections map in `collections.json`. New transcripts: ingest + fact-check there FIRST, then update Google Docs / screener.

## Criteria workbook
`docs/criteria/Screener_Criteria.xlsx` (157 rows incl. Tech S-curve: rationale in "investor states that X means Y, because Z; example" format, verified vs all transcripts; verifiability Easy/Partly/No; Valuation + Summary sheets). Rebuild: `python3 docs/criteria/build_criteria.py` (rationale text in `docs/criteria/out_*.json`; recalc formulas after).

## Open items
00. Triage pushed 2026-10-22; the push starts the first full scan (long: SEC bulk + company pass + 13F data sets; resumes
   from cache after a timeout; the daily cron continues it). Check branch triage-status, then the site. Tag
   prereg-2026-10-20 could not be pushed (proxy drops tag pushes).
0. (Paused: portal archived 2026-10-22.) Validation (v2.9, built 2026-10-20, NOT yet pushed or run): push `main` + tag `prereg-2026-10-20`, then run Validate by hand.
   With the free Massive plan (2 years) every verdict is 'too little history'; 10 years needs the Developer plan
   (run with history_years=10, per_minute=100). After the first run: send `validation/out/audit_reconciliation.csv`,
   `audit_gates.csv` and `audit_stars.csv` to a third-party reviewer. Re-implementation of Fortress from the written rules:
   Jaccard 0.58 (fails 0.9) - rules underspecified (F13 pp vs %, F2 basis, F5, F10, F9, F7); publish exact definitions, re-run.
1. (Paused: portal archived.) After v2.7: run the Screen workflow by hand (SUBSET 8 bulk refresh; the Tech screen, 13F buyers/sellers and insider trades appear after the screen + background runs). Add the free OPENFIGI_API_KEY secret to speed 13F mapping. Background costs ~40 min/day of Actions until histories/ranges are filled, then a few minutes.
2. Unverifiable criteria list + strategies: `Unverifiable` sheet in the criteria workbook. Thesis notes not implemented: Core 'second-best business' fails G6; ROIC floor for Emerging; 10% FCF yield T8 may favour weaker E&Ps.
3. Offered, not yet decided: (a) ADR market caps from Massive reference data, (b) Owner-Operators fallback without a cover-page share count near the float date, (c) partnership equity tags.
4. Valuation: no 'cheap enough' rule in Core/Fortress/HC Commercial by design.
5. `gh` token in the sandbox was invalid on 2026-10-07/08 (git push works); workflows can't be triggered from the sandbox. Transcripts: use the device bridge, not the Drive connector.
6. Congress trades: needs a Quiver Quant API key as a secret (not built). 21st.dev MCP is connected in chat (design work).
