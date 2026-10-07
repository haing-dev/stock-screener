# Stock screener: handoff for new sessions

Read this first. User preference: be concise and direct; use only context from the current chat + this repo.

## Hard rules (security)
- Twelve Data key and SEC user agent (name/email) are PRIVATE. Locally they live only in `local_settings.json` (never in repo, outputs, artifacts or chat).
- Online they are GitHub repository secrets: SEC_USER_AGENT, MASSIVE_API_KEY, TWELVEDATA_API_KEY, PORTAL_PASSWORD, CLAUDE_CODE_OAUTH_TOKEN (user's subscription; no ANTHROPIC_API_KEY set).
- Never ask the user to paste keys/tokens into chat. Never drag the PC project folder into GitHub.

## What it is (v2.3.0)
- Python screener over SEC XBRL companyfacts + submissions; prices from Massive (ex-Polygon, free plan 5 req/min: grouped daily, unadjusted month-end history in `hist_raw`, adjusted `hist`, split list from /v3/reference/splits); Twelve Data = backup + FX.
- 13 screens in `qs/screens.py`: first batch Core, Emerging, Special, Fortress, HC Commercial, HC Clinical, Cyclicals; second batch (strict) Owners, Hard Assets, Asset-Floor, Trough Cash, Hidden Earnings, Red Flags (avoid list). Thresholds in `config.json`.
- Gate statuses PASS/FAIL/NO DATA/N/A; company classes PASS/CHECK/NEAR/PRICE/ONE/FAIL. HARD_GATES = defining rules; VALUATION_GATES = E12,C8,O11,R10,T8,X9. `site/app.js` statusOf mirrors the Python logic.
- Portal: AES-GCM encrypted data (PBKDF2 from PORTAL_PASSWORD); peer medians by SIC 4->3->2 digit (min 6), display only.
- Tests: `python -m tests...` see README; must print "ALL TESTS PASSED".

## Deployment
- Repo `haing-dev/stock-screener` (private). Branches: `main` (code), `site` (published site, force-pushed by workflow), `reports` (check_report.md), `research` (transcript store, see below).
- Cloudflare **Worker** "stock-screener" via Workers Builds on branch `site` (site/wrangler.jsonc, static assets). Pages wasn't available.
- Workflows: screen.yml (cron 17 9 1,16 * *, ~1h15m), daily.yml (15 9 * * 2-6, prices), report.yml (manual check report).
- In the cloud sandbox: blob log downloads are forbidden; `scripts/run_logged.sh` puts the last 60 log lines in check-run annotations (`gh api repos/haing-dev/stock-screener/check-runs/<id>/annotations`).

## Research store (`research` branch)
`git clone -q -b research --single-branch https://github.com/haing-dev/stock-screener research` → read its CLAUDE.md.
113 transcripts + Doc 1/Doc 2 notes, `scripts/search.py`, `scripts/ingest.py`. New transcripts: ingest + fact-check there FIRST, then update Google Docs / screener.

## Criteria workbook
`docs/criteria/Screener_Criteria.xlsx` (157 criteria: rationale in "investor states that X means Y, because Z; example" format, verified vs all transcripts; verifiability Easy/Partly/No; Valuation + Summary sheets). Rebuild: `python3 docs/criteria/build_criteria.py` (rationale text in `docs/criteria/out_*.json`; recalc formulas after).

## Open items
1. Gate `insight` strings in `qs/screens.py` still carry some attributions the transcripts don't support (e.g. Kantesaria/Gaonkar on FCF conversion G7, Haley "mid-cycle ROIC>=10%" C4, Haley "generally <20x" E12, Druckenmiller on dilution E8). Align them with `docs/criteria/out_*.json`.
2. Offered, not yet decided: cut ~200 'check manually' cases with (a) ADR market caps from Massive reference data, (b) Owner-Operators fallback when no cover-page share count near the float date (adjusted close x current shares), (c) partnership equity tags (PartnersCapital, MembersEquity).
3. Valuation gap: no peer-relative or own-history 'cheap enough' rule; Core/Fortress/HC Commercial are price-blind. Options: EV/EBIT <= industry median (data exists), FCF-yield hurdle, own multiple percentile (needs multi-year prices).
4. `gh` token in the sandbox was invalid on 2026-10-07 (git push still worked). Google Drive connector didn't find the transcripts folder.
