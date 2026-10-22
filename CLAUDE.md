# Stock screener: handoff for new sessions

Read this first. User preference: be concise and direct; use only context from the current chat + this repo.

## Hard rules (security)
- Twelve Data key and SEC user agent (name/email) are PRIVATE. Locally they live only in `local_settings.json` (never in repo, outputs, artifacts or chat).
- Online they are GitHub repository secrets: SEC_USER_AGENT, MASSIVE_API_KEY, TWELVEDATA_API_KEY, PORTAL_PASSWORD, CLAUDE_CODE_OAUTH_TOKEN (user's subscription; no ANTHROPIC_API_KEY set).
- Never ask the user to paste keys/tokens into chat. Never drag the PC project folder into GitHub.

## What it is now: Quality Triage (triage/ v1.0.0, built 2026-10-22)
- The 14-screen portal is ARCHIVED (`archive/portal-v2.9/`: its site and workflows; nothing deleted; `qs/` code still used).
- `triage/` = three event-driven US-stock screens in the shape of the biotech crash/slide triage (repo haing-dev/crash-triage):
  Hidden Earnings (month-end close 40%+ below 12-month high), Emerging Compounders and Core Compounders (earnings yield
  enters the cheapest fifth of own last 5 years or of industry peers). Rules, weights, thresholds: `triage/rules.py`
  (pre-registered 2026-10-22; log changes in `triage/CHANGES.md`). Backend requirements (US 10-K filer, history, recent
  report, size, volume, leverage) never enter the score. Calls: weighted cells -> Buy candidate / Watch / Avoid (+ hard
  Avoid; Watch -> Buy on a top performer owner's later 13F). Cells shared by all three: High Conviction Owners, Top
  Performer Owners, Insider Buy/Sell.
- Data: point-in-time panel from the v2.9 backtest code (`qs/backtest.contexts_at`, Massive month-end grid, SEC bulk facts
  filed before each month-end); 13F and insider SEC data sets (`triage/owners.py`); returns open-to-open incl. delistings.
  Outcome: 12-month return vs 10 most similar US stocks + SPY (IWM for Emerging); FF5+UMD calendar-time regression.
- Run: `python -m triage.run auto|monthly|daily|<step>` (workflow `.github/workflows/triage.yml`, weekdays 23:43 UTC;
  monthly pipeline after a month-end). Site -> branch `site` (same Cloudflare Worker, password = PORTAL_PASSWORD).
  Live calls -> branch `triage-record` (append-only ledger.csv). Old site kept on branch `site-archive-v2.9`.
- Massive plan sets the backtest length: free = 2 years of prices (~1 year of results, own-past cheapness mostly N/A);
  Developer = 10 years (run with history_years=10, per_minute=100).
- Local preview: `python tests/triage_smoke.py --demo OUT_DIR` (real SEC samples, invented prices/13F/insiders).
- Tests: `python3 tests/run_tests.py` must print "ALL TESTS PASSED" (includes tests/triage_smoke.py).
- Archived but kept: v2.9 validation of the frozen 14 screens (`validation/PROTOCOL.md`, `qs/validate.py`; workflow archived).

## Deployment
- Repo `haing-dev/stock-screener` (private). Branches: `main` (code), `site` (published triage site, force-pushed), `site-archive-v2.9` (last portal build), `triage-record` (live calls, append-only), `reports`, `research` (transcript store), `history` and `validation` (v2.9 records, no longer updated).
- Cloudflare **Worker** "stock-screener" via Workers Builds on branch `site` (wrangler.jsonc written by `triage/site.py`).
- Workflow: triage.yml only. The old screen/daily/background/report/validate workflows are in `archive/portal-v2.9/workflows/`.
- In the cloud sandbox: blob log downloads are forbidden; `scripts/run_logged.sh` puts the last 60 log lines in check-run annotations (`gh api repos/haing-dev/stock-screener/check-runs/<id>/annotations`).

## Research store (`research` branch)
`git clone -q -b research --single-branch https://github.com/haing-dev/stock-screener research` → read its CLAUDE.md.
253 transcripts + Doc 1/Doc 2 notes, `scripts/search.py` (`--collection`, `--screen`), `scripts/ingest.py <drive folder>`. Source folders on the user's PC: `G:\My Drive\Transcripts\` YouTube Transcripts (general), Healthcare Transcripts, Macro Transcripts (Crypto, Real Estate skipped); screen -> collections map in `collections.json`. New transcripts: ingest + fact-check there FIRST, then update Google Docs / screener.

## Criteria workbook
`docs/criteria/Screener_Criteria.xlsx` (157 rows incl. Tech S-curve: rationale in "investor states that X means Y, because Z; example" format, verified vs all transcripts; verifiability Easy/Partly/No; Valuation + Summary sheets). Rebuild: `python3 docs/criteria/build_criteria.py` (rationale text in `docs/criteria/out_*.json`; recalc formulas after).

## Open items
00. Triage (2026-10-22, NOT pushed): push main, then run Actions > Triage (step monthly) by hand. First run is long (SEC bulk +
   company pass + 13F data sets); it resumes from cache if it times out. Then check the site and cache/tri/out stats.
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
