# Stock screener: handoff for new sessions

Read this first. User preference: be concise and direct; use only context from the current chat + this repo.

## Hard rules (security)
- Twelve Data key and SEC user agent (name/email) are PRIVATE. Locally they live only in `local_settings.json` (never in repo, outputs, artifacts or chat).
- Online they are GitHub repository secrets: SEC_USER_AGENT, MASSIVE_API_KEY, TWELVEDATA_API_KEY, PORTAL_PASSWORD, CLAUDE_CODE_OAUTH_TOKEN (user's subscription; no ANTHROPIC_API_KEY set).
- Never ask the user to paste keys/tokens into chat. Never drag the PC project folder into GitHub.

## What it is (v2.5.0)
- Python screener over SEC XBRL companyfacts + submissions; prices from Massive (ex-Polygon, free plan 5 req/min: grouped daily, unadjusted month-end history in `hist_raw`, adjusted `hist`, split list from /v3/reference/splits); Twelve Data = backup + FX.
- 13 screens in `qs/screens.py`: first batch Core, Emerging, Special, Fortress, HC Commercial, HC Clinical, Cyclicals; second batch (strict) Owners, Hard Assets, Asset-Floor, Trough Cash, Hidden Earnings, Red Flags (avoid list). Thresholds in `config.json`.
- Gate statuses PASS/FAIL/NO DATA/N/A; company classes PASS/CHECK/NEAR/PRICE/ONE/FAIL. HARD_GATES = defining rules; VALUATION_GATES = E12,C8,O11,R10,T8,X9. `site/app.js` statusOf mirrors the Python logic. Site shows two lists: Pass (PASS) and Near misses (CHECK+NEAR+PRICE+ONE, each with its reason).
- Core (Oct 2026): G2 recent report applied but hidden (`Gate.hidden`, all screens); G4 <= 2 loss years; G9 no operating loss in a downturn FY (2008-09, 2015-16, 2020, 2022; `metrics.DOWNTURNS`) while sales fell, only downturns inside SEC data; G10 3y revenue CAGR >= 0 (sole failure = near miss). Quality warnings removed from every screen. Rationales on the site = `screens.RATIONALE` / `PURPOSE` (no investor names; attributions stay in the criteria workbook).
- Portal: AES-GCM encrypted data (PBKDF2 from PORTAL_PASSWORD). Same table columns on every screen (`portal.TABLE_METRICS`). Company page (#screen/TICKER): about, valuation vs 10 closest peers + own 3y/10y average multiples (`qs/history.py`, info only, listed companies), Excel 3-statement model built in the browser (`site/vendor/exceljs.min.js`, `buildModel` in app.js) from `state.models` (`metrics.model_years`, 10 FYs, shares restated to today's basis) exported as `model_XX.bin` shards.
- Price history (`history.update`, screen + daily runs, budgets in config `portal`): 52-week range from Massive weekly high/low files (`cache/prices/massive/weeks`, backfilled ~100-200 days/run, shown once >= 240 days); month-end prices from Twelve Data (`cache/prices/monthly_history.json.gz`, 1 credit/company, listed + peers, refetch after 180 days or a split).
- `extract.SUBSET_VERSION` 7 (v2.5) -> next screen run re-downloads all SEC facts (6 added statement-model concepts, `model: True`, annual only).
- Metric audit (Oct 2026, v2.5): ROIC uncapped (floor -500%); capital-light years (invested capital <= 2% of revenue or negative, with profit) = n/m and count as above any >= floor (`_median_nm`, `<metric>_nm` notes; Gate PASS with note). Revenue growth uses a like-for-like chain from same-filing ratios (`CompanyData.revenue_ratios`, restatements/disposals); `revenue_cagr_raw` kept. Agg "max" for capex/R&D/D&A/other debt; extra capex, securities, lease, commercial-paper tags; EV/net debt subtract long-term investments; missing capex/SBC = None (not 0); 3y ratios need all 3 years. Known limits: derived revenue (e.g. NVS) gets no chain; annual EBIT keeps interest income; no debt tags = debt-free.
- Thesis update from 98 new transcripts (v2.5): G7/H7/O7 cash conversion = (FCF - stock pay)/net income (MSFT now near miss on G7); Emerging E3/E12 use EBIT / EV-EBIT when D&A >= 50% of EBITDA (`_capital_heavy`); Asset-Floor tangible-book route needs tangible book/share not down over 3 yrs; Red Flags W4 + 6 signals (profits above cash 2y, negative OCF, restructuring >= 4 of 5 yrs, acquisitions > OCF 3y, inventory days 5y high, heavy capex with negative FCF).
- Local preview: `python tests/demo_portal.py OUT_DIR` (real samples, invented prices).
- Tests: `python3 tests/run_tests.py` must print "ALL TESTS PASSED".

## Deployment
- Repo `haing-dev/stock-screener` (private). Branches: `main` (code), `site` (published site, force-pushed by workflow), `reports` (check_report.md), `research` (transcript store, see below).
- Cloudflare **Worker** "stock-screener" via Workers Builds on branch `site` (site/wrangler.jsonc, static assets). Pages wasn't available.
- Workflows: screen.yml (cron 17 9 1,16 * *, ~1h15m), daily.yml (15 9 * * 2-6, prices), report.yml (manual check report).
- In the cloud sandbox: blob log downloads are forbidden; `scripts/run_logged.sh` puts the last 60 log lines in check-run annotations (`gh api repos/haing-dev/stock-screener/check-runs/<id>/annotations`).

## Research store (`research` branch)
`git clone -q -b research --single-branch https://github.com/haing-dev/stock-screener research` → read its CLAUDE.md.
211 transcripts + Doc 1/Doc 2 notes, `scripts/search.py` (`--collection`, `--screen`), `scripts/ingest.py <drive folder>`. Source folders on the user's PC: `G:\My Drive\Transcripts\` YouTube Transcripts (general), Healthcare Transcripts, Macro Transcripts (Crypto, Real Estate skipped); screen -> collections map in `collections.json`. New transcripts: ingest + fact-check there FIRST, then update Google Docs / screener.

## Criteria workbook
`docs/criteria/Screener_Criteria.xlsx` (157 criteria: rationale in "investor states that X means Y, because Z; example" format, verified vs all transcripts; verifiability Easy/Partly/No; Valuation + Summary sheets). Rebuild: `python3 docs/criteria/build_criteria.py` (rationale text in `docs/criteria/out_*.json`; recalc formulas after).

## Open items
1. After v2.5: run the Screen workflow by hand (SUBSET 7 re-download; new metrics/red-flag signals, statement models, peers only exist after a screen run). 52-week ranges appear after ~2-3 runs (backfill); peer/own-history multiples fill over ~3-5 runs (Twelve Data 800 credits/day).
2. Unverifiable criteria list + strategies: `Unverifiable` sheet in `docs/criteria/Screener_Criteria.xlsx`. Thesis notes not implemented (Oct 2026): Core 'second-best business' (high ROIC, no reinvestment) fails G6; ROIC floor for Emerging; 10% FCF yield T8 may favour weaker E&Ps; H4/H5 exclude new launchers.
3. Offered, not yet decided: cut 'check manually' cases with (a) ADR market caps from Massive reference data, (b) Owner-Operators fallback when no cover-page share count near the float date, (c) partnership equity tags (PartnersCapital, MembersEquity).
4. Valuation: no 'cheap enough' rule in Core/Fortress/HC Commercial by design; company page shows peers/own history as information.
5. `gh` token in the sandbox was invalid on 2026-10-07/08 (git push still worked); workflows can't be triggered from the sandbox. Google Drive connector didn't find the transcripts folder; use the device bridge (stage files) instead.
6. Offered, not built: top institutional holders column from SEC 13F data sets (not by scraping hedgefollow).
