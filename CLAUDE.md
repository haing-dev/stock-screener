# Stock screener: handoff for new sessions

Read this first. User preference: be concise and direct; use only context from the current chat + this repo.

## Hard rules (security)
- Twelve Data key and SEC user agent (name/email) are PRIVATE. Locally they live only in `local_settings.json` (never in repo, outputs, artifacts or chat).
- Online they are GitHub repository secrets: SEC_USER_AGENT, MASSIVE_API_KEY, TWELVEDATA_API_KEY, PORTAL_PASSWORD, CLAUDE_CODE_OAUTH_TOKEN (user's subscription; no ANTHROPIC_API_KEY set).
- Never ask the user to paste keys/tokens into chat. Never drag the PC project folder into GitHub.

## What it is (v2.9.0)
- Python screener over SEC XBRL + submissions; prices from Massive (free plan, 5 req/min), Twelve Data = backup + 10-year history; Cloudflare-hosted encrypted portal. Details and design notes: `docs/HANDOFF.md` (read the relevant section only).
- 14 screens in `qs/screens.py` (site text in `qs/screen_text.py`, theses in `qs/thesis.py`, thresholds in `config.json`). `site/app.js` statusOf mirrors the Python classes. VALUATION_GATES = E12,C8,O11,R10,T8,X9,B7,A16. Pass* = no verified miss, some rules unverifiable (asterisk + hover note); `screens.DEFINING_GATES` unverifiable, no financials yet, or Red Flags -> CHECK (near miss).
- Daily SEC sync (`qs/secsync.py`) + bulk files; workflows screen / daily / background (see HANDOFF).
- Local preview: `python tests/demo_portal.py OUT_DIR` (real samples, invented prices and invented 13F holders).
- Tests: `python3 tests/run_tests.py` must print "ALL TESTS PASSED".
- Validation (v2.9, see `validation/PROTOCOL.md`, HANDOFF): screens FROZEN at v2.8.0 on 2026-10-20 (`validation/freeze.json`,
  `python -m qs.freeze --check`). A rule change must be logged in `validation/CHANGES.md` and is tested as a variant only.
  Point-in-time backtest + stats + audits: `python screener.py validate all` (workflow validate.yml, monthly) -> branch
  `validation`. Forward record: every Screen/Daily run appends its lists to branch `history` (never force-pushed).

## Deployment
- Repo `haing-dev/stock-screener` (private). Branches: `main` (code), `site` (published site, force-pushed by workflow), `reports` (check_report.md), `research` (transcript store, see below), `history` (forward record of published lists, append-only), `validation` (validation results, append-only).
- Cloudflare **Worker** "stock-screener" via Workers Builds on branch `site` (site/wrangler.jsonc, static assets). Pages wasn't available.
- Workflows: screen.yml (cron 17 9 1,16 * *), daily.yml (15 9 * * 2-6, prices), background.yml (40 10 * * *, slow fills + descriptions), report.yml (manual check report), validate.yml (41 11 3 * *, validation; inputs history_years / per_minute for the Massive plan).
- In the cloud sandbox: blob log downloads are forbidden; `scripts/run_logged.sh` puts the last 60 log lines in check-run annotations (`gh api repos/haing-dev/stock-screener/check-runs/<id>/annotations`).

## Research store (`research` branch)
`git clone -q -b research --single-branch https://github.com/haing-dev/stock-screener research` → read its CLAUDE.md.
253 transcripts + Doc 1/Doc 2 notes, `scripts/search.py` (`--collection`, `--screen`), `scripts/ingest.py <drive folder>`. Source folders on the user's PC: `G:\My Drive\Transcripts\` YouTube Transcripts (general), Healthcare Transcripts, Macro Transcripts (Crypto, Real Estate skipped); screen -> collections map in `collections.json`. New transcripts: ingest + fact-check there FIRST, then update Google Docs / screener.

## Criteria workbook
`docs/criteria/Screener_Criteria.xlsx` (157 rows incl. Tech S-curve: rationale in "investor states that X means Y, because Z; example" format, verified vs all transcripts; verifiability Easy/Partly/No; Valuation + Summary sheets). Rebuild: `python3 docs/criteria/build_criteria.py` (rationale text in `docs/criteria/out_*.json`; recalc formulas after).

## Open items
0. Validation (v2.9, built 2026-10-20, NOT yet pushed or run): push `main` + tag `prereg-2026-10-20`, then run Validate by hand.
   With the free Massive plan (2 years) every verdict is 'too little history'; 10 years needs the Developer plan
   (run with history_years=10, per_minute=100). After the first run: send `validation/out/audit_reconciliation.csv`,
   `audit_gates.csv` and `audit_stars.csv` to a third-party reviewer; finish `validation/reimplementation.md` explanations.
1. After v2.7: run the Screen workflow by hand (SUBSET 8 bulk refresh; the Tech screen, 13F buyers/sellers and insider trades appear after the screen + background runs). Add the free OPENFIGI_API_KEY secret to speed 13F mapping. Background costs ~40 min/day of Actions until histories/ranges are filled, then a few minutes.
2. Unverifiable criteria list + strategies: `Unverifiable` sheet in the criteria workbook. Thesis notes not implemented: Core 'second-best business' fails G6; ROIC floor for Emerging; 10% FCF yield T8 may favour weaker E&Ps.
3. Offered, not yet decided: (a) ADR market caps from Massive reference data, (b) Owner-Operators fallback without a cover-page share count near the float date, (c) partnership equity tags.
4. Valuation: no 'cheap enough' rule in Core/Fortress/HC Commercial by design.
5. `gh` token in the sandbox was invalid on 2026-10-07/08 (git push works); workflows can't be triggered from the sandbox. Transcripts: use the device bridge, not the Drive connector.
6. Congress trades: needs a Quiver Quant API key as a secret (not built). 21st.dev MCP is connected in chat (design work).
