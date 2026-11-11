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

## Macro Compass (macro/ v2.0.0, 2026-10-23)
- One flow: 43 investor-cited indicators (research store + X posts of @AtlasShrug1) -> 3 dials (economy stage,
  inflation hot, market stress) -> state (Expansion/Late/Overheating/Contraction/Stagflation/Recovery + stress overlay)
  -> investor playbook per state (registry.RULES/STRESS) -> history check -> calls on 20 industry ETFs at 6/12 months. Point in time,
  walk-forward odds, ETF backtest from 2006 vs equal weight / momentum / trend / SPY. Details: macro/README.md.
- Workflow `.github/workflows/macro.yml` (weekday schedule PAUSED 2026-11-02 at user request; push to macro/ or dispatch still run). Page: its OWN Cloudflare Worker
  "macro-compass" built from branch `macro-site` (force-pushed; wrangler.jsonc + .assetsignore written by macro/site.py).
  NOT on the stock-screener site (https://stock-screener.haing-penn.workers.dev/ is used for another build - don't touch).
  No password (public, noindex). Branches: `macro-data` (raw downloads, force-pushed),
  `macro-status` (last run log: `git fetch origin macro-status && git show origin/macro-status:status.md`),
  `macro-record` (append-only monthly calls from Oct 2026). Secret FRED_API_KEY (user adds) = first-published data.
- Main action (5.0.0, 2026-10-29, package P1): track-record-weighted warnings (28 core indicators, worst fifth) cut stocks
  100% -> 0% as their share goes 15% -> 35%, only while the Fed is tightening (funds >= 1 pt above 24m low); S&P below
  10m average AND unemployment above 12m average -> 0%. Rest: TLT in a growth-trend cut while stock-bond corr < 0, else
  T-bills. Plus 10% commodities (DBC/AQR index) while the index is up 12m and above its 10m average; sector momentum tilt
  (top/bottom 5 of 20, 1.5x/0.5x) while fully invested. Backtest with 0.2% costs: since 1975 14.5%/yr, worst -18%.
  Page: Analysis = six checks with charts (warning share + 28 indicator boxes, Fed, growth/trend, stock-bond corr,
  commodities, sector momentum); Recommendation = mix chart + momentum sector calls.
  Research: docs/research/hf_macro (audit, 731 transcript hypotheses, packages P1-P4, data wishlist); research data
  snapshot on branch macro-research-data (fetch: step research_fetch). Earlier: docs/research/macro_combos.
- Rules: macro/registry.py (pre-registered; changes -> new VERSION + macro/CHANGES.md).

## Global Macro Book (gm/ v1 gm-1.0.0, 2026-10-30; paper research only)
- Plan + all results: project doc claude/global_macro_book_plan_2026-10-29.md (v5+). Code: gm/panel.py (65-market
  month-end panel from free data on branch macro-data), gm/plumbing.py (vs AQR TSMOM: corr 0.83), gm/signals.py
  (families), gm/book.py (combined book, costs), gm/run.py (monthly run), gm/imf_revisions.py (exploratory).
- Workflow .github/workflows/gm.yml (DISABLED 2026-10-31 at user request until further notice; re-enable: gh api -X PUT repos/haing-dev/stock-screener/actions/workflows/gm.yml/enable) (3rd of each month + push to gm/): branch gm-status (status.md, positions.csv),
  gm-record (append-only ledger.csv; restatements appended with '-restated').
- Research program playbook (2026-11-02): docs/research/PLAYBOOK.md = session types, model routing (Sonnet extract /
  Opus second read + build / Fable judgement), extraction schema, verification thresholds, vault, 2-week schedule.
  Every session: read it + research-branch STATUS.md, do ONE stage, commit, name the next stage.
- Layer 0 DONE 2026-11-04: all 227 Macro Transcripts -> 12,597 claims (quotes script-checked), cross-checked (Opus high 95+5 pilot, Sonnet xhigh 127; list opus_cross_ids.txt). Branch macro-vault (ledger/, raw/, build.py, vault notes); vault copied to G:\...\Obsidian Macro\Macro. Open: calibrate Sonnet-xhigh vs Opus cross-check on ~10 docs; Quant papers DONE 2026-11-05: 15 papers (Quant folder) -> 1,490 claims, all quotes exact, Sonnet + Opus blind read, Opus
  reasoning map per paper (question, thesis, premises, mechanism chain, design rationale, evidence, regimes, gaps, relations);
  spec/tools in macro-vault branch papers/; vault Papers/ (copied to Obsidian). Fable phase NOT started (user controls batches).
- Transcript argument maps (2026-11-06): tier A (103 of 227, by investing value + key investors; transcript_priority.csv)
  DONE with Sonnet high per TRANSCRIPT_MAP_SPEC.md (per speaker: premises, mechanism chains, decision process, evidence,
  dated views, fingerprint tags; disagreements; gaps). macro-vault pipeline/ (docs, maps, spec, queue). Tiers B/C open.
  Tier B (72) DONE 2026-11-06 too (175 of 227 mapped; tier C open). Alias table pipeline/speaker_aliases.json.
- Investor syntheses (2026-11-06): 19 people with >=2 appearances (Sonnet, INVESTOR_SYNTH_SPEC.md) -> vault Investors/;
  Niels (host, 112 appearances) not done (needs 3-part split).
- Fable phase started: F1 = AQR Economic Trend (docs/research/fable/F1_economic_trend.md, Fable max, ~0.23M tokens):
  keep econ 15%; no Holm slot for econ structure; zero-slot diagnostics T1 delay-decay, T2 sign audit by era;
  T3 forecast-based growth/inflation as the one Batch 2 econ challenger. Next: F2 trend, F3 value/carry, F4 rates, F5 method.
- Foundation phase (2026-11-09): 21 units (top funds, practitioners, core papers), one Fable max unit every 4 h via send_later.
  Spec/units/pack builder in macro-vault pipeline/foundation (FOUNDATION_SPEC.md, units.json, build_pack.py). Done: U01 AQR,
  U02 Carver (+31-post blog digest), U03 Kaminski, U04 Baltas, U05 Git, U06 Man AHL, U07 Winton. Notes also in docs/research/fable/foundation/.
- Foundation PAUSED (user runs units one at a time on request; U07 done 2026-11-11, next U08 Eckhardt). Units now run on claude-fable-5-2.
  User rule: no "decisions/routes" for the user; open choices -> variant registry docs/research/fable/foundation/VARIANTS.md
  (dimensions A-H, walk-forward selection on Bloomberg data, one Holm slot for the procedure; register before running).
- WORKFLOW v2.1 (2026-11-11; FINAL DESIGN, awaiting user go per block, nothing executed; Bloomberg files 1-7 now in ...\Bloomberg_UBC_pull_2026-11-04\pulled results): docs/research/WORKFLOW.md = pod shop.
  Systematic + discretionary pods (rule layer + shadow analyst); versions averaged inside a pod (no picking); fixed
  budget Batch A / B1 / B2 -> freeze -> one holdout (verdict only for theses documented before 2011) -> live record;
  Core / Incubator / Shelved by rule; forecast ledger (descriptive); weekly live cycle on free data; agent per step
  (Fable judges small inputs + independent Opus check; Opus builds/tests/rebuilds; Sonnet ops; scripts). It replaces
  the PLAYBOOK routing/schedule, the per-person units U08-U21 and the VARIANTS selection procedure.
  Bloomberg pulled files: stay on the PC (local job runner like the WRDS one, summary statistics only, 2011+ sealed).
- 2026-11-10 status: WORKFLOW block 1 DONE: local job runner on the PC (tools/bbgq; jobs dropped in Documents\WRDS results\local\jobs
  run on the PC, report only; Python 3.15 + numpy/pandas/scipy/openpyxl in local\pylib). Bloomberg inventory (metadata):
  docs/research/bbg/inventory_2026-11-10.md = 2,017 of 2,470 tickers loaded; file 1 complete (490/494); file 5 commodities
  only 246/631 (367 saved while still loading -> user re-pulls file 5 and 8 indexes of file 4). Next: block 2 (reader, data
  check, lock, seal 2011+) on the user's go.
- 2026-11-11 status: WORKFLOW block 2 DONE (provisional): reader tools/bbgq/lib/bbgdata.py (as-of access, 2011+ sealed, 45
  held-back markets), data check, lock v1 = docs/research/bbg/LOCK_v1.json + LOCK_v1_check_2026-11-11.md (lock id f5a4fb7c...).
  FINDING: monthly history is cut off in file 1 (rates futures, curves, returns, yields, bond futures, breakevens, surprise:
  from 2009-06) and file 3 (all sheets: from 2004-04); file 5 mostly still loading; 100 of 260 must-have groups not usable.
  User re-pulls files 1, 3, 5 (+8 EquityIndexes tickers in file 4) -> re-run bbg_build -> lock v2. Usable now: daily files 6, 7
  (from 1990), file 1 DailyCommodities / EquityTR / EquityValuation / Economics, files 2 and 4. Next: block 3 on the user's go
  (engine on the PC, reproduce the book on free data; does not need the re-pull).
- MT228 (2026-11-10): raw X posts of John Galt @AtlasShrug1 (1,359 posts, Jul 2025 - 8 Nov 2026) extracted like a transcript
  with dates: 733 claims (185 rules/tells, 188 dated forecasts), Sonnet single read, quotes script-checked, cross-check
  pending; macro-vault raw/sonnet/MT228.json, brief pipeline/X_EXTRACT_BRIEF.md. Use: forecast ledger (step 2), rule
  layer / Macro Compass indicator candidates (oil +90% y/y, backwardation extremes, breadth divergence, equal- vs
  cap-weight, gold+dollar both down, issuance/IPO supply, news-reaction asymmetry). Not yet tested.
- OBSIDIAN = SINGLE TRACEABLE STORE (user rule 2026-11-09): everything goes into the vault (G:\...\Obsidian Macro\Macro):
  Sources/Papers/Investors/Mechanisms, Fable/Foundation (claim ids linked to quote blocks, code refs linked to GitHub at a
  fixed commit), Method/ (all specs, routing, units, aliases), _data/ (raw JSON bundles + exact Fable input packs). After each
  step run L0 build.py + build_fable.py <commit>, push macro-vault, copy changed files to the PC vault.
- Adoption rule (2026-11-01): docs/research/global_macro/TESTING_PROTOCOL.md (paired bootstrap dSR, Holm, non-inferiority per era);
  run `python -m gm.protocol batch0|batch1|diag`; register each new batch in that file BEFORE running it. Batch 2 = Bloomberg.
- Holdout 2011-2026 has NOT been looked at: never print or inspect it until rules are frozen (then run once).
- 2026-11-01 framework: gm/config.py (BASE = live gm-1.2, CANDIDATE = gm-2.0: hybrid vol + shares trend 45 / carry 25 /
  value 15 / econ 15), gm/trials.py (log every design trial in gm/trials.csv), gm/stats.py, gm/vol.py, gm/daily.py,
  gm/timing.py, gm/bloomberg.py (reads cache/macro/raw/research/bloomberg/Bloomberg_macro_UBC.xlsx; test:
  python3 tests/gm_bloomberg_smoke.py). White paper: Claude Doc "Global Macro Book: White Paper". Holdout criteria:
  SR >= 0.3, worst fall > -25%, corr S&P <= 0.3, 2022 positive.
- Bloomberg EQUITIES workbook (2026-11-04): docs/data_requests/Bloomberg_equities_UBC.xlsx (builder
  build_bloomberg_equities.py; 4,512 US-listed stocks; live formulas (Refresh Workbook); 209 snapshot fields + annual /
  quarterly / monthly history + bulk). Pulled file goes to Documents\Screenerdata\bloomberg (ask access to that folder).
- Bloomberg pull v5 (2026-11-04): 8 numbered workbooks, guide docs/data_requests/BLOOMBERG_PULL_GUIDE.md; files 2-7 from
  build_bloomberg_v5.py (templates + bloomberg_v5_tickers.csv in docs/data_requests/bloomberg_v5/; same block layout as v4).
  Copy on PC: Documents\WRDS results\mscifreedata\Bloomberg_UBC_pull_2026-11-04 (pulled files -> its pulled\ subfolder).
  Next: one reader for all block files (extend gm/bloomberg.py), then register batch 2+ before using.
- Placeholders: Bloomberg commodity workbook docs/data_requests/Bloomberg_macro_UBC.xlsx (commodities + first-release/consensus economics; user at UBC next week; built by build_bloomberg.py);
  equity value/carry; WRDS revisions; econ on first-release data. Manual files: gm/data (RBI); MSCI kept out of git.

## WRDS (tools/wrdsq, 2026-10-29)
- User ttdlisa (UBC) has WRDS; subscription list incl. Compustat Global/NA, CRSP (annual), CRSP Treasuries, LSEG IBES,
  TRACE, Cboe VIX, FRB rates, Fama-French, Global Factor Data, World Indices, Penn World Tables, Dow Jones, 13F.
  No Datastream, OptionMetrics, Markit.
- WRDS policy: no WRDS Data into AI tools. Claude writes jobs; they run on WRDS Cloud via tools/wrdsq; only metadata
  and results come back. Never ask for the WRDS password; it is typed only in the user's PowerShell window.
- User does not code and Windows blocks .bat files: give ONE PowerShell paste line (tools/wrdsq/mkjob.py).
- Triage 10-year backtest on WRDS (2026-10-30): `tools/wrdsq/build_tri.py` copies triage/rules, episodes, score,
  stats (+ qs/btstats ols_nw) unchanged into `tools/wrdsq/lib/tri_wrds.py` with the WRDS adapter
  (`tools/wrdsq/tri_wrds_adapter.py`: CRSP dsf_v2 / Compustat / CCM / s34 13F / FF). Rebuild after any rules change;
  local dry run `python3 tests/tri_wrds_local.py`. Job `tri_bt*`: pull + run, stats only; tri_events exported to the
  user's `Documents\Screenerdata\data` (runner downloads exports; Claude never reads it). Stock-screener jobs, lib and
  reports live in `Documents\Screenerdata\runner\{jobs,lib,results}` (runner v2 serves both that folder and WRDS
  results; status/log stay in WRDS results). Pulls are resumable (one table per year; jobs tri_pull_crsp / tri_pull_rest
  then tri_run*). No insider data on WRDS
  (tr_insiders not permitted) -> insider cell N/A. Entry = close of the day after the scan (live: open).
- Global Macro Book plan: project doc claude/global_macro_book_plan_2026-10-29.md. WRDS-based signals are
  backtested on WRDS Cloud; only statistics return.

## Deployment
- Repo `haing-dev/stock-screener` (private). Branches: `main` (code), `site` (published triage site, force-pushed), `site-archive-v2.9` (last portal build), `triage-record` (live calls, append-only), `triage-status` (last run's log tail + counts, force-pushed), `reports`, `research` (transcript store), `history` and `validation` (v2.9 records, no longer updated).
- Cloudflare **Worker** "stock-screener" via Workers Builds on branch `site` (wrangler.jsonc written by `triage/site.py`).
- Workflows: triage.yml and macro.yml. The old screen/daily/background/report/validate workflows are in `archive/portal-v2.9/workflows/`.
- In the cloud sandbox: blob log downloads are forbidden; `scripts/run_logged.sh` puts the last 60 log lines in check-run annotations (`gh api repos/haing-dev/stock-screener/check-runs/<id>/annotations`).

## Research store (`research` branch)
`git clone -q -b research --single-branch https://github.com/haing-dev/stock-screener research` → read its CLAUDE.md.
397 transcripts (3.5M words; collections general 252, macro 57, healthcare 37, energy 13, consumer 12, banking 11, media 10; all with Doc 1 notes, checked 2026-11-02) + Doc 1/Doc 2 notes, `scripts/search.py` (`--collection`, `--screen`), `scripts/ingest.py <drive folder>`. Source folders on the user's PC: `G:\My Drive\Transcripts\` YouTube Transcripts (general), Healthcare Transcripts, Macro Transcripts (Crypto, Real Estate skipped); screen -> collections map in `collections.json`. New transcripts: ingest + fact-check there FIRST, then update Google Docs / screener.

## Criteria workbook
`docs/criteria/Screener_Criteria.xlsx` (157 rows incl. Tech S-curve: rationale in "investor states that X means Y, because Z; example" format, verified vs all transcripts; verifiability Easy/Partly/No; Valuation + Summary sheets). Rebuild: `python3 docs/criteria/build_criteria.py` (rationale text in `docs/criteria/out_*.json`; recalc formulas after).

## Open items
000. WRDS triage follow-up tests DONE 2026-10-31 (docs/research/triage_wrds/RESULTS.md): no test passed the
   pre-registered bar; calls/red flags only capture the profitability factor (RMW). Rules unchanged. Avoid = useful warning.
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
