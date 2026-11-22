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
- Re-pull set (2026-11-11, user pulls Fri 13 Nov): docs/data_requests/bloomberg_repull_2026-11-13/R1..R7 (builder
  build_bloomberg_repull.py; 1,283 series; sheets named '<file digit> <sheet>'; Check sheet with live STATUS and a
  'should start by' month per series). Copy on the PC: ...\Bloomberg_UBC_pull_2026-11-04\repull_2026-11-13; pulled files go to
  'pulled results'. AFTER the pull: run jobs bbg_build_v2 + bbg_check_v2 (reader bbgdata-1.2.0 merges R files: an ok re-pull
  replaces the first-pull block unless it is shorter; _CUT twins never win) -> lock v2 (docs/research/bbg/LOCK_v2.json).
  CUT-OFF EXPLAINED (bbg_diag_v1/v2 in tools/bbgq/results): the late blocks are COPIES of one series (file 1: 355 blocks =
  the 209 numbers of JYBSV1 Curncy; file 3: 481 blocks with one set of 271 numbers), cause not proven (add-in glitch
  suspected). The Check sheet flags copies ("WRONG NUMBERS", columns J/K); the reader gives them status `copy` (unusable).
- 2026-11-11 status: WORKFLOW block 3 DONE (gate: reproduction PASS, truncation FAIL with 3 causes). Note
  docs/research/bbg/BLOCK3_engine_2026-11-11.md. Engine on the PC: tools/bbgq/build_engine.py -> engine_pkg/ (git-ignored;
  gm/ unchanged -> local\lib\gm, free inputs zip -> local\work\free), reference tools/bbgq/engine_ref.json (design period),
  jobs gm_repro_v1 (PC: 24/24 PASS, diff 0), gm_trunc_v1 (PC = cloud), gm_bbg_map_v1, adapter lib/bbg_panel.py (mocks only).
  Look-ahead found in the INPUT layer (rules clean; 2010-12 cut passes): C1 panel.py dividend mean up to 2010, C2 panel.py
  local-rate stand-in start, C3 daily.py >500-day gate, C4 >24/>36-month gates on Bloomberg series. NOT fixed: they need ONE
  new registered engine version (gm/CHANGES.md, new reference) before Batch A; C2 fix = `& rl.notna().cummax()`.
  Usage: Opus builder ~566k tokens, Opus checker ~317k. Next: lock v2 after the Friday pull; block 4/5 on the user's go.
- 2026-11-12 ENGINE gm-1.2.1 (BASE, live) / gm-2.0.1-candidate: look-ahead fixes C1-C4 registered in gm/CHANGES.md BEFORE the
  code change, implemented by Opus (81fe176). Truncation test PASSES at all 8 cut dates (free data; mock Bloomberg inputs too).
  Design numbers barely move (BASE 1975-2010 SR 1.235 -> 1.236; CANDIDATE 1.464 -> 1.464; only C1 changes numbers: 631 early
  equity market-months). New reference tools/bbgq/engine_ref.json (old: engine_ref_gm-1.2.0.json); PC redeployed, reproduction
  24/24 PASS. Open risk (not registered): commodity_carry's "farthest contract" depends on which tickers have data.
- 2026-11-12 FABLE AUDIT (WORKFLOW 1.1) PASS: docs/research/fable/AUDIT_1.1_2026-11-12.md. 12 of 12 planted errors caught, 0
  carried, 0 false alarms (Eckhardt pack); Carver re-derivation: substance 6 agree / 4 partly / 0 disagree, but the ORIGINAL
  U02 note has 4 real errors (T4 "with a mechanism" vs B24 "No mechanism was established"; costs "within 1-2 bp" graded strong
  on summary text only; buffer test read from wrong columns). So notes U01-U07 = sound logic, UNVERIFIED numbers. Brief v2
  rules appended to FOUNDATION_SPEC.md (quotes = ground truth; summary-only numbers cannot support grades/tests; "Pack
  problems" section; Opus checks test premises before registration). Exact inputs/outputs/keys: macro-vault pipeline/audit_1.1.
  Usage: Fable ~0.91M tokens (two runs; quote-checking makes units ~2-4x longer), Opus prep+scoring ~0.32M.
- FABLE SCHEDULE (user 2026-11-11): ONE Fable max unit per day via send_later. Day 1 = 1.1 audit (done). Next, in order: 1.2
  systematic charter (then Opus check vs claims and code), 1.3 thesis notes (rates/curve QP06-07-12; value/momentum/carry
  QP15-08; testing method QP13), 1.4 playbook cards x5 (Druckenmiller+Bessent; Bridgewater; Graham+Elliott; Karsan; Andurand).
  Every unit: brief v2 rules, private work folder per agent, report tokens, store exact input in the vault.
- 2026-11-12 FORECAST LEDGER (WORKFLOW block 5, steps 2.1-2.3) DONE: tools/fcast (pull, validate, merge, agree, score,
  scorecard; tests/fcast_smoke.py), docs/research/forecasts (FORECAST_SPEC v1, CODING_AGREEMENT, SCORING_RULES v1 frozen
  before outcomes, SCORECARD_2026-11-12), data on macro-vault pipeline/forecasts (ledger.csv 2,102 rows from 1,815 views;
  outcomes.csv; scored_frozen.csv). Sonnet coded, Opus blind-recoded 20% (is-forecast 94%, variable 90%, direction 92%,
  resolvable 80%, confidence 55% = unusable). 329 resolved, 227 open. Direction calls ~ base rate (+1 pp, n=113); macro calls
  +26 pp over base rate (n=47). Descriptive only, never weights. 27 rule gaps listed (macro levels ignored; WEO has no
  actuals); cache stale (ends 2026-10-23/30). Re-run score.py + scorecard.py after a data refresh to resolve open rows.
  Lesson: give each parallel agent a PRIVATE scratch folder (coders overwrote each other's helper scripts).
- LSEG WORKSPACE (2026-11-12): the user has LSEG Workspace + Datastream in Excel on her OWN PC (usable any day). Probe v1
  (tools/bbgq/results/lseg_probe_v1.txt): 57 of 69 test formulas return data. Works WITH dates: RHistory (BID.Timestamp;
  BID.Close; FX from 1990+), RDP.Data TR fields (.SPX, yields; not futures or FX), DSGRID (Datastream: S&P from 1950, MSCI,
  benchmark bonds from ~1980, economics, GSCI, continuous futures; monthly dates = the day of the START date, so use a
  month-end start). RDP.HistoricalPricing returns values WITHOUT dates (futures c1..c12, yields, forwards, vols all have
  data; needs SOURCE:RFV); .SPX/.VIX "no permission" there; EDc1 (Eurodollar) not retrievable; =ECI economic codes need other
  fields. Pull set v1: docs/data_requests/build_lseg_pull.py -> lseg_pull_2026-11-12/ L1a FX spot+forwards, L1b FX vol+SOFR
  swaps, L2a Datastream benchmark bonds (yield + return index), L2b Workspace yields, L3 equity markets/indexes (377 series)
  + P2 probe (203 formulas: how to date futures, 67 futures roots, curve depth, GSCI/BCOM/MSCI codes, short rates, swaps,
  economics with polls). PC copy: Documents\WRDS results\lseg\pull_2026-11-12. Reader: tools/bbgq/jobs/lseg_read_v1.py
  (metadata only; env LSEG_DIR). The user attaches saved files to the chat herself; read them ONLY through the reader (no
  values printed, never commit the files). NEXT: read P2 -> build the futures-curve, commodity-index and economics files;
  then an LSEG reader into the engine, registered as a SECOND source (cross-check + live weekly data); Bloomberg stays the
  registered backtest source. Daily Fable units run at 22:00 Vancouver time (user 2026-11-12; Vancouver = UTC-7).
  PC runner stalls overnight (last check 23:14); one-line fix given (allow start on battery), not confirmed applied.
- LSEG PROBE 2 (2026-11-12, tools/bbgq/results/lseg_probe_v2.txt; 167 of 203 return data). DATED FUTURES: RDP.HistoricalPricing
  with display "SORT:ASC TSREPEAT:NO CH:Fd RH:Timestamp" (also RHistory ".Timestamp;.Close", DSGRID "<RIC>", RDP.Data
  TR.SETTLEMENTPRICE). 58 of 67 futures roots work (all commodities except lumber and LME; all bond and equity-index futures;
  SRA, FF, FEI, SON3, YBA); curves: CL to c36, LCO/NG to c24, metals c12, grains c9. NOT available: Eurodollar, short
  sterling, BAX, Euroswiss (ended contracts), LME, US breakeven code, MSCI valuation ratios and ICAP swaps in Datastream
  (access denied), economic releases with consensus/first release (=ECI history has no poll field). Available: Datastream
  S&P GSCI total/excess-return indexes by commodity (GS<code>TOT / GS<code>EXR), BCOM TR (DJUBSTR), MSCI total-return
  indexes, 3m deposit rates (EC<ccy>3M from 1975), national economics (<CC>CONPRCF etc.), Citi surprise indexes
  (USCESIR, .CESIxxx from 2003), USD swaps, cross-currency basis, TIPS yields. Datastream monthly with a month-end start
  date returns the last weekday of each month. Pull set 2: build_lseg_pull2.py -> L4a energy curves, L4b metals/agri
  curves, L5 financial futures, L6 commodity indexes/MSCI/surprise, L7 short rates/swaps/economics (555 formulas;
  helpers lseg_pull_helpers.py). 11 files to pull in total (L1a-L7); none read back yet except the two probes.
  Bloomberg re-pull priority given to the user: R1 (Eurodollar/short-rate futures, breakevens, surprise, first release),
  R5 (swaps, credit), then R2-R4 (commodity cross-check, fundamentals), R6, R7 (LSEG covers FX).
- LSEG PULL READ BACK (2026-11-12, tools/bbgq/results/lseg_pull_2026-11-12_read.txt; reader now reports dates of rows that
  hold numbers + a copy check): 913 of 932 blocks have data, 0 still loading, 0 copied blocks (3 legit duplicates). History:
  FX spot from 1975, forwards from 1982 (median 1996), FX vol from 1995; Datastream benchmark bonds (yield + return index)
  from 1979-12; equity markets (price, return, P/E, yield) from 1973; commodity curves from 1973 (grains/softs/metals), WTI
  1983 (c24 from 1995, c36 from 2006), Brent 1988, natural gas 1990; bond futures from 1977 (TY 1982, Bund 1990, JGB 1987);
  GSCI by commodity from 1970-87; 3m deposit rates from 1975; economics for 18 countries. FAILED (19): Norway 2y, 30y
  benchmarks for CH/SE/NO/NZ, VIX (no licence in any function), GSCI platinum code, 9 economics pattern guesses; 8 economics
  series are discontinued codes. GAPS LSEG CANNOT FILL (need Bloomberg or free data): Eurodollar / short sterling / BAX /
  Euroswiss futures (LSEG rate futures: Euribor 1994, Fed funds 2000, SOFR/SONIA 2018), swap rates before 2011, economic
  surprise by release + first release + consensus (Citi surprise only from 2003), non-US breakevens (US TIPS from 1997),
  credit spreads, commodity fundamentals, forward EPS and MSCI valuation (denied), LME metals, EM NDF forwards before
  ~2010, VIX (free source). Files were read via the bridge with the metadata reader because the PC runner is stalled.
  PROPOSED NEXT (not done): LSEG reader + lock with the 2011+ seal (like bbgdata), register LSEG in the data plan as the
  source for the families it covers (same source in backtest and live), Bloomberg for the gaps and as cross-check.
- 2026-11-12 (later) USER RULE: Bloomberg needs a campus visit; anything LSEG can supply should come from LSEG (refreshable
  daily on her PC). Done: (1) LSEG set 3 = build_lseg_pull3.py -> L8_fixes_and_alternatives (181 formulas: failed codes +
  guessed LSEG alternatives for ended rate futures via Datastream, swaps by Workspace codes, inflation-linked yields, LME via
  Datastream, 13 other commodities, extra bond futures, FX option quotes, Fed series, forward EPS guesses), L9a/L9b DAILY
  from 1990 (46 commodity c1/c2; 73 rates, equity futures, FX, yields). Not pulled yet. (2) SLIM BLOOMBERG VISIT SET =
  build_bloomberg_slim.py -> docs/data_requests/bloomberg_visit_2026-11-13/ (PC: ...\Bloomberg_UBC_pull_2026-11-04\
  visit_2026-11-13): R8 rates only on Bloomberg (149: ED / short sterling / BA / Euroyen / Euroswiss futures, extra bond
  futures, breakevens, CTA benchmarks, swaps), R9 (108: credit, commodity fundamentals, 8 equity indexes, NDF forwards),
  R10 cross-check sample (47), R11 other commodity curves (205, lowest priority) = 509 series; replaces R1-R7 (1,283).
  One R number per file (the reader keeps one workbook per number). If L8 shows an LSEG alternative works, drop that part
  of R8/R9 before the visit. (3) RUNNER: schedule repair script Documents\WRDS results\fix_runner.ps1 (repo:
  tools/wrdsq/runner/fix_runner.ps1): daily trigger repeating every 10 min, allowed on battery, start when available;
  writes local\task_fix_report.txt (before/after). Needs ONE paste by the user:
  powershell -ExecutionPolicy Bypass -File "C:\Users\admin\Documents\WRDS results\fix_runner.ps1"
  Computer use cannot type into terminals, so this cannot be done remotely. Job lseg_read_v1.py is queued in local\jobs.
- 2026-11-12 (evening) L8/L9 READ BACK + RUNNER FIXED. Runner: the user pasted fix_runner.ps1; cause was the task's battery
  settings (no start on battery, stop on battery, no catch-up; 74 missed runs); now a daily trigger repeating every 10 min.
  LSEG files are read ON THE PC by job lseg_read_v1b (report tools/bbgq/results/lseg_pull_2026-11-12_read_v1c.txt, which replaced v1b: then 14
  files, 1,343 of 1,435 blocks with data, no unexplained copies). L8: 144 of 181 work. NOW ON LSEG: Eurodollar (Datastream
  "<EDc1>" style, 1981-12 to 2023), Canada BA "<BAXc1>" 1989, Euroswiss "<FESc1>" 1991, Euroyen JEYc1 1989, short sterling
  "<FSSc1>" only from 1999-06; swaps USD/EUR/GBP/JPY/CHF from 1987-89 (codes USDAM3L10Y=, EURAB6E.., GBPSB6L.., JPYSB6L..,
  CHFAB6L..), AUD (AUDQM3AB..), SEK (SEKAB3S..), NZD (NZDSM3NB..); EUR OIS EUREON1Y= 1999; US and UK inflation swaps 2007
  (USCPIZ10Y=, GBRPIZ10Y=); US TIPS 5/10/30y; LME cash + 3 months via Datastream from 1970 (LCPCASH, LCP3MTH; LAH, LZZ, LNI,
  LED, LTI); oats, rice, TTF, robusta, white sugar, canola, palm oil, milling wheat, iron ore, uranium, EU carbon, rubber
  (c1-c3); ultra 10y, short BTP, Bono, Canada 2y/5y, Korea 3y futures; gold/silver/platinum/palladium spot; DEM/FRF/ITL;
  risk reversals from 2010; 11 more equity indexes; S&P 500 12m forward EPS (@:USSP500, A12FE) from 1985.
  WRONG SERIES, do not use: L8 Datastream guesses CEDCS00, LSSCS00, MBACS00, LESCS00 (other contracts) and GSPTTOT (petroleum,
  not platinum). Dead after 2019: Datastream Moody's Aaa/Baa. STILL FAILED on LSEG: CAD and NOK swaps, USD OIS, euro inflation
  swap, non-US inflation-linked yields (UK only from 2010), Korea 10y, class III milk, SG CTA / BTOP50 (no permission),
  Baltic Dry (denied), Norway 3y, Argentina / Chile indexes. L9a/L9b daily from 1990: 119 of 119 with data.
  NEW: L10 (build_lseg_pull4.py, 144 formulas, not pulled yet): full strips of the ended rate futures (monthly + daily),
  remaining swap tenors, last guesses for the failures. BLOOMBERG VISIT SET v2 (build_bloomberg_slim.py, 265 series, was
  509): R8 (48: short sterling L1-L12, Korea 10y / Swiss bond / JGB mini futures, 7 non-US breakevens, 6 CTA benchmarks, 20
  swaps LSEG lacks), R9 (95: credit 47, commodity fundamentals 15, NDF forwards 33), R10 cross-check (75), R11 (47: lumber,
  milk, London cocoa, Newcastle coal, rapeseed, NBP gas; lowest priority). PC folders updated. Vault not yet updated with
  the LSEG notes. NEXT: read L10 -> LSEG reader + lock with the 2011+ seal -> register LSEG as source (still proposed).
- 2026-11-12 (night) L10 READ BACK (job lseg_read_v1c; report tools/bbgq/results/lseg_pull_2026-11-12_read_v1c.txt: 15 files,
  1,455 of 1,579 blocks with data). L10: 112 of 144. WORKS: Eurodollar c1-c12 (c1-c4 1981-12, c9-c12 1987-06; daily from
  1989-12), Euroswiss c1-c8 (1991; c5+ 1996-98), Euroyen JEYc1-c6 (1989; c7-c8 not found), short sterling c1 1999-06 and
  c2-c8 only 2002-03, Canada BA ONLY c1 and c9-c12 ("<BAXc2>".."<BAXc8>" invalid in Datastream); swap tenors 1/3/7y
  (GBP 1y only 2016), CHF/AUD/SEK/NZD 5y; NOK swaps NOKAB6O2Y= (1995); USD OIS USD2YOIS= (2001; 10y 2011); GBP SONIA OIS
  GBP2YOIS= (2007); JPY OIS JPY2YOIS= (2005); EUR OIS 5/10y (2005); US/UK inflation swaps 1-30y (2007); Korea 10y 10TBc1
  (2008); Swiss bond CONFc1 (1992); London cocoa LCCc (1974), Newcastle coal NCFMc (2008), rapeseed COMc (1994), NBP gas
  NGLNMc (1997), class III milk DCSc (1998), TTF c12/c13. Guessed Workspace codes return no series name: they are cross-checked
  against Bloomberg in R10 before use. FAILED: CAD swaps (3 guesses), euro and Japan inflation swaps, lumber LBRc, JGB mini,
  AUD 30y, GSCI platinum, Baltic Dry (denied); Rotterdam coal ATWc returned numbers without dates (unusable as is).
  BLOOMBERG VISIT SET v3 (237 series): R8 (45: short sterling L1-L12, Canada BA2-BA8, JGB mini, 7 non-US breakevens, 6 CTA
  benchmarks, 12 swaps: CAD 2/5/10, euro inflation 1/2/5/10 + 5y5y, yen inflation 10, 2 swaption vols, FRA-OIS), R9 (95,
  unchanged), R10 cross-check (85, now incl. the guessed LSEG codes), R11 (12: lumber only, optional). PC folder updated.
- 2026-11-13 SYSTEMATIC CHARTER (WORKFLOW 1.2) DONE, PASS WITH CORRECTIONS: docs/research/fable/CHARTER_1.2.md (Fable max, one
  run, ~0.67M tokens; the 24 corrections of the Opus check are applied in the text) + CHARTER_1.2_check.md (Opus high, ~0.36M;
  verified against the verbatim quotes and code; read Eckhardt MT020 and Fung-Hsieh QP09). Exact inputs, briefs, original
  Fable text: macro-vault pipeline/charter_1.2. CONTENT: pods = Trend, Economic trend, Carry, Value (existing book) + Curve
  carry (new, B1; far vs near commodity contract; rests on one seller's unshown claims, no live source registered). The notes
  give NO thesis for Carry or Value (step 1.3 must) and do not establish why trends exist (4 rival mechanisms). Version
  grids (averaged, equal weight): Trend 16 (lookback 1/3/6/12 x sign/graded x hybrid/36-month vol), Economic trend 2, Carry
  2, Value 1, Curve carry 2; all in four weekly tranches. ONE diagnostic pass D1-D6 (zero slots, design months) replaces the
  34 queued tests: D1 breadth (gates alternative commodities), D2 non-signal turnover (gates a no-trade buffer), D3 book risk
  by state (gates a faster book scaler), D4 crisis profile, D5 econ delay decay, D6 trend return per unit of market move.
  Nothing registered or run (registration = step 3.4). FINDINGS: (a) bd_us_2y and st_us_2y are the SAME series (61 distinct
  markets, US 2y double weight); removal needs a registered engine version before any run, effect unknown; (b) numbers: 11
  of 19 source numbers are in the quote, 6 summary only (U01 Sharpe figures are chart reads); (c) Fung-Hsieh: trend pays
  like lookback straddles (skew, weak mean) so Sharpe / linear alpha alone can reward a rule that lost its shape; trend
  funds earned in the 1987 and 1990 crashes while our engine lost in 1987 from long equities; (d) Eckhardt's firm does not
  resize with volatility and rates alternative markets worse in practice; (e) rule 5: no note dates a thesis before 2011;
  Economic trend's sources are 2017 and 2023 (Incubator unless step 1.5 finds an earlier source). 9 open judgement points
  are listed in section 11 with the step that closes each (1.5, 3.1-3.2, 3.4); none is a decision for the user.
  NEXT Fable unit: 1.3 thesis note rates and curve (QP06, QP07, QP12), daily 22:00 Vancouver.
- 2026-11-13 BLOOMBERG VISIT BLOCKED: every BDH/BDP on the campus terminal returns "#N/A Review" (data-download capacity limit), even
  =BDP("SPX Index","PX_LAST") in a blank sheet. Likely cause: the 4 Nov pull (~2,500 macro series + 4,500-stock workbook) used
  the terminal's or the login's allowance. R8-R11 (237 series) not pulled; retry on another terminal or after the limit
  resets. Nothing in the engine depends on them now (LSEG covers most).
- 2026-11-13 (later) BLOOMBERG VISIT PULLED after all (limit cleared): files R8 (v2, 48 series), R9, R10, R11 saved in
  Documents\WRDS results\lseg\pull_2026-11-12\bloomber 13 Nov 2026 (NOT in 'pulled results'; point BBG reader there or copy).
  Check job bbg_visit_check_v1 (tools/bbgq/results/bbg_visit_check_v1.txt, metadata only): 230 of 265 with data, 0 copies,
  0 late starts. Short sterling L1-L5 from 1988; L6-L12 no data. Failed tickers: SG CTA/Trend, HFRI x2, BTOP50, Italy and
  Canada breakevens, 7 credit guesses, 7 commodity-fundamental guesses (EIA free instead). CAD swaps only from 2009-09.
  R12_canada_bax_swaps.xlsx (BA2-BA8 + CAD swap BGN/CMPN guesses, 13 series) given to the user to pull before leaving.
- 2026-11-14 R12 pulled: 13 of 13 with data (job bbg_visit_check_v2): BA2-BA8 from 1990-91; CAD swaps CMPN source from 1989-04
  (tickers 'CDSW2 CMPN Curncy' etc.; BGN only 2009). Job bbg_visit_merge_v1 (tools/bbgq/jobs) QUEUED on the PC: copies R8-R12
  from the lseg\...\bloomber 13 Nov 2026 folder into 'pulled results', then runs the bbg_build_v2 + bbg_check_v2 code (lock
  v2). RAN 2026-11-13 22:10 PC time (report tools/bbgq/results/bbg_visit_merge_v1.txt): all 5 R files used, 315 series
  re-pulled, 273 replaced a failed or copied first-pull block, 6 added, 0 re-pulled copies; LOCK v2 id d85a46cb2853...ea41fc9
  (on the PC in local\work; docs/research/bbg/LOCK_v2.json NOT yet written in the repo). First-pull copies that were not
  re-pulled stay unusable in Bloomberg (e.g. 125 curve blocks, 28 bond futures): LSEG covers those families.
- 2026-11-14 THESIS NOTE 1.3a RATES AND CURVE DONE, PASS WITH CORRECTIONS: docs/research/fable/THESIS_1.3_rates.md (Fable max,
  ~0.65M tokens; 20 corrections of the Opus check applied) + THESIS_1.3_rates_check.md (Opus high, ~0.28M; 36 of 38 numbers in
  quote, 0 contradicted). Inputs/briefs/original: macro-vault pipeline/thesis_1.3_rates. RESULT: one new pod, Strip reversion
  (fade local bends between neighbouring short-rate futures contracts, QP06 rules 2-B and 3-B; 2 versions averaged), grade
  WEAK, Batch B2 behind every stronger candidate and only if zero-slot diagnostic R1 passes (are local bends on the dollar
  strip bigger than trading cost and still there a day later, 1990-2010; at least half of triple-months, else dropped
  unbuilt). Needs daily prices for dollar contracts 1-8 (LSEG L10 has daily only for Eurodollar c1, c2, c4, c8: a small
  extra pull). NOT specced: QP06 Treasury-bill form, whole-curve level/slope/curvature reversion (the engine's three built
  spreads stay untraded), QP07 model as a signal, QP12 commodity forecast. Short-rate futures (U01-T4) = markets added to
  Trend / Economic trend / Carry through charter gate D1 (euro, sterling, yen if live; not the dollar; live source needed).
  Spread gate (U05-T5) = two fixed rules inside Strip reversion. Evidence: QP06 on ESTIMATED Treasury yields 1973-2000, before
  costs, fading after the late 1980s; no test of the local rule on traded prices; QP07 puts such bends in the component it
  expects to last (C10-4). 9 open judgement points in section 10 with closing steps. Rule 5: QP06 = J. Fixed Income 2006
  (checker's knowledge). NEXT Fable unit: 1.3b value / momentum / carry (QP15, QP08): must supply the Carry and Value theses.
  SCRATCH FOLDER WAS CLEARED during the pause (L0 build tree lost; vault_wt re-cloned from branch macro-vault). Single vault
  notes are now built with vault_wt/build_note.py (same linkify as build_fable.py); a full rebuild needs L0 recreated.
- 2026-11-14 THESIS NOTE 1.3b VALUE / MOMENTUM / CARRY DONE, PASS WITH CORRECTIONS (run on the user's word, same day):
  docs/research/fable/THESIS_1.3_xs.md (Fable max, ~0.63M tokens; 22 corrections applied) + THESIS_1.3_xs_check.md (Opus
  high, ~0.27M; 27 of 34 numbers in quote, 0 contradicted). Inputs: macro-vault pipeline/thesis_1.3_xs. RESULT: CARRY thesis
  supplied for currencies and commodities (asserted risk premium / hedgers), NOT for bonds (pattern, no mechanism); grade
  weak; stays in both forms (directional + cross-asset), 2 versions unchanged; equities stay out. VALUE thesis supplied with
  a reservation, grade WEAK after the check (only per-class figure in a quote = bonds, which fails; nobody establishes who
  pays; QP15 itself says the cross-asset pattern is hard to fit to behavioural theories); cross-asset form only; 1 -> 2
  versions (second anchor for bonds and currencies). CROSS-SECTIONAL MOMENTUM = neither a pod nor a Trend version (what is
  left of Trend once each class's average position is removed); Trend registered directional only. Two zero-slot
  diagnostics: X1 (is energy carry a calendar pattern; gate 0.25 of signal variance -> seasonal adjustment), X2 (is Value
  paid by prices coming back or by income). Limits: both papers before costs, both author groups sell the strategies,
  QP08's sample runs 52 months into the sealed years. Rule 5: neither paper dated before 2011 in the pack; checker's
  knowledge: Asness-Liew-Stevens 1997, Fama 1984, Fama-Bliss 1987 (step 1.5). 9 open judgement points in section 10.
  PC vault copy done. NEXT Fable unit: 1.3c testing method (QP13),
  2026-11-15 22:00 Vancouver (trigger trig_01JvgC3A3rV5N9JuQFvvVYjh, prompt updated to 1.3c).
- 2026-11-15 THESIS NOTE 1.3c TESTING METHOD DONE, PASS WITH CORRECTIONS (scheduled unit, 22:00 Vancouver):
  docs/research/fable/THESIS_1.3_method.md (Fable max, ~0.46M tokens; 22 corrections of the Opus check applied) +
  THESIS_1.3_method_check.md (Opus high, ~0.24M; 87 numbers checked, none summary-only, 1 arithmetic slip corrected).
  Inputs/briefs/original: macro-vault pipeline/thesis_1.3_method (pack = QP13 claims AND the slide text itself, because
  slide quotes are fragments; TESTING_PROTOCOL; WORKFLOW 1-6; digest; design-era book facts from the repo result files).
  RESULT: QP13 (Stine's 45 teaching slides, 2009) establishes one thing: the martingale test of alpha (Foster, Stine,
  Young 2008) keeps false alarms at 1 in 20 even against a fund with steady gains and a hidden total loss. The rest is
  asserted or shown on dice and four hand-picked assets. NO new decisive test. Four protocol items for step 3.4:
  P1 correct two citations in TESTING_PROTOCOL (Stine 2009 backs the worry behind the tail test, not its fall statistic;
  the Newey-West alpha t is not a "Foster-Stine" test); P2 test 1 for a NEW POD = regression alpha on the Core book
  with a p-value from the registered whole-month bootstrap, Holm at 0.025 per batch (Sharpe difference at the held size
  reported only); P3 scope paragraph: error rates do not cover a loss rarer than the window, for pods and challengers
  (+ one computed row in the power table: a zero-mean pod with a hidden loss is adopted >= 0.37 x as often as a
  Sharpe-0.4 pod at 432 months; "loss not seen" flag in pod specs, no effect on verdicts); P4 reported line: Sharpe of
  the book after taking out its S&P 500 exposure (expanding-window slope, from month 37). One zero-slot diagnostic M1
  (S&P alone or S&P + US 10-year in P4; gate 0.05 Sharpe in either era). MARTINGALE TEST DROPPED as decisive and as a
  reported line: as held, a typical path clears the bar of 20 only at a Sharpe gap of ~0.84 (registered minimum 0.05);
  for the whole book the volatility convention sets the verdict (candidate compounds to ~143 over 1975-2010: p 0.007,
  0.22 after 32 variants, 0.021 at a 15% target). Sizing: the 10% target is cautious (growth-best only at a true Sharpe
  of 0.10); a fifth independent pod at equal risk helps only if its Sharpe exceeds 0.236 x the book's.
  TO RECONCILE AT 3.4 (pack problems): WORKFLOW vs TESTING_PROTOCOL disagree on the error level per batch (2.5% vs 5%),
  the decisive sets (era test), the form of test 1 (alpha vs Sharpe difference), hygiene ("does not hurt" vs
  superiority) and "double costs" for a pod; WORKFLOW still reports the deflated Sharpe the audit calls uninformative;
  5.1 equal risk vs the candidate's family shares 45/25/15/15. 10 open judgement points in section 13 with closing
  steps (3.1-3.4); none is a decision for the user. Settled from the code: gm/panel.py holds futures-style EXCESS
  returns, so the book's return is in excess of cash.
  NEXT Fable unit: 1.4 first playbook card (policy and liquidity: Druckenmiller, Bessent; Sonnet builds the pack, Fable
  writes the card), MOVED to 2026-11-17 22:00 Vancouver (trigger trig_01Nd4vmLiA5Mc6cGt2nwnGGf; user paused 16 Nov).
  USER RULE 2026-11-16: Fable units run at effort HIGH, not max, from unit 1.4 on (max uses too much); prompt updated.
  NEW TOOL tools/vault/make_sync_job.py: builds ONE PC-runner job that carries vault notes inside itself and writes them
  into the Obsidian vault (the device shell is not available in every session; the bridge writes single files only).
  How: generate the job, send the file, write it to Documents\WRDS results\local\jobs through the bridge, read
  local\results\<job>.txt after the runner's next pass (every 10 minutes). Vault branch macro-vault 011f178.
  PC VAULT COPY DONE 2026-11-15 22:30 PC time (job vault_sync_20261115a: 24 files written = the two 1.3c notes,
  _data/thesis_1.3_method, Method/00 Method.md and the Method notes that were pending: equity design v0.2, biotech
  desk v0.1, equity plan v0.3 with its two checks, transcript library inventory).
- 2026-11-17 PLAYBOOK CARD 1.4 (1 of 5) POLICY AND LIQUIDITY (Druckenmiller, Bessent) DONE, PASS WITH CORRECTIONS:
  docs/research/fable/CARD_1.4_policy_liquidity.md (Fable at effort HIGH, ~0.34M tokens; 45 corrections of the Opus check
  applied) + CARD_1.4_policy_liquidity_check.md (Opus high, ~0.22M as reported; cut once by the usage limit, resumed).
  Inputs: macro-vault pipeline/card_1.4_policy (pack built BY SCRIPT from the ledger: 590 claims, 11 recordings
  2018-2026, forecast rows, digest, data sheet of live series; no Sonnet agent needed). RESULT: playbook = find where
  policy is out of step with the economy, wait for a cheap one-sided bet, size big, cut fast. Part can be coded: six
  rules R1 Squeeze (oil, dollar, rates all up -> long US 2y/10y), R2 Tightening into warnings, R3 Easing into strength,
  R4 Behind on inflation, R5 After the fall (currency collapse -> long that stock index), R6 Gold that ignores yields
  (HELD BACK: its only quote points to a pullback, not a rise); 28 versions to register (56 with two entry versions),
  all averaged; 10 weekly analyst questions; 11 open forecasts; 2 zero-slot diagnostics. NOT codable: liquidity itself,
  peg breaks, policy personnel, conviction sizing (where the recalled profits came from). ALL six rules are hindsight
  under rule 5 (nothing recorded before 2018). Ledger record: Druckenmiller 4 of 16 forecasts right, three recession
  calls missed. Check findings: the 1999 long behind R3 ended in his largest recalled loss; his 2021 front-end short on
  money growth was missing; the R1/R2 inflation gate was built knowing 2022 (now a version). 10 open judgement points
  with closing steps (1.5, 2.2-2.3, 3.1-3.2); none is a decision for the user. Pack problems: MT085 repeats MT151 (one
  statement scored twice with opposite results), 10 claim ids cited by the forecast ledger are missing from the claims,
  Bessent's Le Pen forecast window has closed but shows open.
  FABLE DAILY UNIT PAUSED (user 2026-11-18) until she says resume: NO next unit is scheduled. Next in order when
  resumed: 1.4 second card (regime and debt cycle, Bridgewater), Fable at effort high, same procedure as this unit
  (brief templates in pipeline/card_1.4_policy).
  Vault branch 4c10eb7; PC vault copy DONE (job vault_sync_20261117a ran, no errors).
- 2026-11-21 PLAYBOOK CARD 1.4 (2 of 5) REGIME AND DEBT CYCLE (Bridgewater) DONE, PASS WITH CORRECTIONS (run on the
  user's word; daily schedule stays PAUSED): docs/research/fable/CARD_1.4_regime_debt_cycle.md (Fable high, ~0.26M tokens;
  29 corrections of the Opus check applied) + _check.md (Opus high, ~0.21M). Inputs: macro-vault pipeline/card_1.4_bridgewater
  (pack by script: 183 claims of Dalio, Prince, Jensen, Karniol-Tambour, Yechiely (former), 6 recordings 2022-2025).
  RESULT: playbook = follow how debt, deficits and policy feed spending, profits and bond demand; work out what prices
  assume; spread risk. Little is codable: 2 rules, 8 versions: R1 Not paid to hold (Dalio: real 10y yield below a bar ->
  short US 10y; may overlap card 1 R4 in 1975-81), R2 Rates-only repricing (Karniol-Tambour: 10y up >= 1.0/1.5 pt in 12m
  and S&P not yet down 10x that -> short S&P; her 2022 live call scored wrong at 12m). Both hindsight-flagged, Incubator
  at best. The codable growth/inflation idea = our existing Economic trend pod. 10 analyst questions, 7 open forecasts,
  2 diagnostics. Ledger: 5 of 11 resolved rows right after two disputed. Check: the no-override rule rests on Prince,
  not Jensen (Jensen says systemizing a new shock was the error); a chain misread a quote; Dalio's debt-dynamic quote
  (1930-45) had been missed. 9 open judgement points (3.1-3.4, 2.2-2.3); none is a decision for the user.
  NEXT when resumed: card 3 (macro relative value and risk: Graham, Elliott), Fable high, templates in
  pipeline/card_1.4_bridgewater.
  Vault branch dce020b; PC vault copy QUEUED (job vault_sync_20261121a in local\jobs).
- 2026-11-21 PLAYBOOK CARD 1.4 (3 of 5) MACRO RELATIVE VALUE AND RISK (Graham Capital, Elliott) DONE, PASS WITH
  CORRECTIONS (user's word; schedule stays PAUSED): docs/research/fable/CARD_1.4_relative_value_risk.md (Fable high,
  ~0.32M tokens; 41 corrections of the Opus check applied) + _check.md. Inputs: macro-vault pipeline/card_1.4_graham_elliott
  (361 claims, 11 recordings 2022-2025: Tropin, Calderini, 2022 Graham panel, Chris Jones; Paul Singer). RESULT: playbook =
  liquid rates/FX/index/commodity trades on central banks vs market pricing; many small different bets; size by
  volatility; shrink before events; keep capital intact (Singer). "Relative value" is thin (one definition, one curve
  trade, one worked case). 4 rules, 16 versions (32 with sizing), all hindsight: R1 Hawkish currency (rank currencies by
  12m change in 3m rates), R2 Steepener (2s10s below 1.0), R3 Cuts priced too early (likely = Carry; D1 decides), R4 No
  alternative (S&P forward earnings yield minus T-bill low -> short S&P; both live uses wrong). 3 registered pod process
  rules + 1 sizing version. Ledger: 15 of 40 (rates 10 of 17, mostly 2022; Graham stocks 0 of 5). Check: risk officer
  McCann says crowded times have HIGHER PM information ratios (contradicts the card's stop condition); Tropin says
  rules decay; Graham's quant side is trend/value/carry = our pods. 8 open judgement points (2.2-2.3, 3.1-3.2).
  NEXT when resumed: card 4 (flows and volatility: Karsan), Fable high, templates in pipeline/card_1.4_graham_elliott.
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

## Equity pod shop (DESIGN ONLY: plan v0.3 + annex v0.2, 2026-11-15; nothing built or run)
- USER DIRECTION 2026-11-19 (remember): use a list of about 30 top investors, each with transcripts and 13F holding
  history with conviction (largest weights), to build a book of strategies (like the earlier screeners), find stocks
  from them, build paper portfolios and backtest historically and forward to see which strategies consistently
  outperform. Purpose: an agentic workflow of independent, unbiased pods: investors' logic -> WRDS/LSEG company data
  standardised into one like-for-like tracker (candidates at attractive valuation, plus the roster's latest 13F buys)
  -> paper portfolios with backtests; scientific, data-driven, cross-checked between steps.
  PROPOSAL v0.1 = docs/research/equity/EQUITY_BUILD_STRUCTURE_PROPOSAL_v0.1.md (project doc
  claude/equity_build_structure_proposal_v0.1.md): five desks + referee on top of plan v0.3, five changes (roster
  rule v2, conviction holdings, tracker live early, owner panel + registered follow pod, valuation as version).
  SUGGESTION ONLY, nothing built or run; next on the user's go: plan v0.4 (with review M1-M6).
  USER FEEDBACK 2026-11-20 (proposal section 11): (a) records and tests may use 2010-2026, not much further back
  (funds did not exist, markets differ) -> roster on the long record too: 15 library investors in the top quarter
  on 2011-25 pass the material bar (+9 leaderboard = 24, +6 with one document); a like-for-like 2010-2025 weighted
  ranking needs one more eq_hf run (60 quarters), not run; tests: US 2010-2025 main period with three same-period
  checks (non-US, control-investor pods, source holdings left out). (b) LICENCE: user states WRDS and LSEG data may
  be used freely if not published; site with password; non-commercial -> LSEG figures may reach agents and the
  password site. WRDS AI-tools term still open (asked the user); until answered WRDS rows stay on WRDS.
  SECOND FEEDBACK 2026-11-20: WRDS or LSEG both fine, LSEG PREFERRED (faster) -> LSEG first for company data;
  managers' portfolios from SEC 13F / WRDS (not on LSEG). Roster may grow to 30 BUT each investor must allow a screen
  on consistently calculable measures (qualitative investors are out). First read:
  hf_leaderboard/ROSTER_SCREENABILITY_2026-11-20.md (+csv): 21 pass record + screenability (A: Greenblatt, T. Smith,
  Kantesaria, Hohn, Greenberg, Zlatev, Pilecki; B: Nygren/Fitch, Stahl, Dorsey, C. Davis, Shaposhnik, Sacerdote,
  Einhorn, Druckenmiller, Kantor, Robotti, F. Martin; borderline Gerstner, Bloomstran, Li Lu); 16 judgement-led set
  aside (Vinall, Russo, Begg, McLennan, Ruffer, Tropin, Shaver, Paulson ...); 9 places open. Nothing built or run.
- PLAN v0.4 + REGISTRATION (2026-11-20, user's go for steps 1-2; nothing built or run; no independent check yet):
  docs/research/equity/EQUITY_POD_SHOP_PLAN_v0.4.md (project doc claude/equity_pod_shop_plan_v0.4_2026-11-20.md) +
  V04_REGISTRATION.md (R1 roster rule v2: record rank_share >= 0.60 on 2011-25 or leaderboard top 50, material,
  screenability measured >= half of criteria computable; 21 on the roster, 9 open, control 10; R2 conviction purchase
  = new position / addition into the five largest weights OR >= 1% of the portfolio, both averaged; R3 main test
  period US 2010-01..2025-12, eras 2010-14 / 2015-19 / 2020-25, universe 1,500 largest, side check 2001-09 on WRDS,
  outside-US and 2026 months sealed until the freeze; R4 portfolio rule; R5 five tests (M1 era rule, M6 placebo of
  1,000) + same-period checks A outside US, B control pods, C source holdings left out; best class on history =
  "Passed on history", Core only by the live rule; LONG-ONLY against reference book + sector-matched universe is
  decisive, long/short reported; R6 8 slots; R7 reference book v1 from pre-2011 sources). SEAL_LOG has the v0.4 entry.
  Build order = plan section 10 (9 steps, user paces). Data: LSEG first (PC), WRDS 13F + cross-check.
  FIELD DICTIONARY v0.1 (draft): docs/research/equity/FIELD_DICTIONARY_v0.1.md + field_dictionary_v0.1.csv (67
  measures) + field_dictionary_raw_v0.1.csv (52 account items with TR.F names; source of names: kaxanuk loader map).
  LSEG TEST FILE 2: docs/data_requests/build_lseg_equity_probe2.py (imports the v1 builder) ->
  lseg_equity_probe2_2026-11-20/LSEG_equity_probe_v2.xlsx (184 formulas: field names, forms, universe incl. dead
  2010-25, estimates, prices, short/owners, sizes); PC copy Documents\WRDS results\lseg\equity_probe2_2026-11-20;
  reader job tools/bbgq/jobs/lseg_eq_probe_v2.py (NOT queued: put it in local\jobs AFTER the user has refreshed and
  saved). NEXT: read it back -> dictionary v1.0 + LSEG file plan (step 3); WRDS conviction job (step 4).
  TEST FILE 2 READ BACK 2026-11-20 (docs/research/equity/LSEG_equity_probe2_2026-11-20.md; report
  tools/bbgq/results/lseg_eq_probe_v2.txt; the user attached the saved file, read in the cloud with the reader):
  48 of 52 account items have a working TR.F name as first reported (net income TR.F.NetIncAfterTax, capex
  TR.F.CAPEXNetCF, FCF TR.F.FOCF); quarterly Orig vs Rsdt differ; S&P 500 x 8 fields x 18 years and ~100,000-row
  monthly blocks work in one formula; dead companies work by ISIN; estimates, returns, past market cap, holders,
  insiders work. MAIN RISK: the Workspace screen misses most dead companies (70 of 1,930 large 2010 companies marked
  retired) -> universe must come from Datastream DEADUS1-7 + FAMER lists, checked against CRSP delisting counts.
  Open: short-interest history (SHORTINT fails for code lists), no GICS on a past date, ownership totals, 4 items
  to retest on a second company. Reader runs out of memory on 500-column Datastream grids (skip the Limits sheet or
  cap columns). USER RULE 2026-11-20: every file for the user goes to a dedicated subfolder of
  G:\My Drive\Screener project (folder connected), not Downloads / WRDS results.
  NEXT: universe file (dead + research lists) + CRSP count check; dictionary v1.0; then the data files (step 3).
  UNIVERSE FILE 1 READ BACK 2026-11-20 (docs/research/equity/LSEG_universe_v1_2026-11-20.md; builder
  docs/data_requests/build_lseg_universe.py; file on the PC G:\My Drive\Screener project\LSEG\01_universe): DEADUS1-10 +
  FAMERA-Z = 33,234 US common shares; main-exchange set alive 3,882 (2010) to 4,463 (2024). EXMNEM is the LAST exchange
  (failed companies show OTC -> keep OTC, filter by monthly price/size/volume). 3 of 11 known dead companies missing
  (Twitter, Time Warner, Whole Foods) -> add SEC 13(f) securities lists (CUSIP->ISIN) + CRSP count-only check on WRDS.
  Retests: 51 of 52 raw items named (goodwill open); short interest history = TR.ShortInterest Frq=M from 2010;
  ownership = TR.CategoryOwnershipPct / Datastream NOSHST etc.
  WRDS UNIVERSE CHECK 2026-11-21 (seal-exempt job 4 `universe_check`, module tools/equity/wrds/eq_univ.py 1.1.0; the
  LSEG identifier input lives only on the PC runner lib, not in the repo; V04_REGISTRATION A1-A2; reports
  docs/research/equity/eq_univ_check_v1/_v2_report.txt): rule 99% NOT met. US-incorporated top 1,500 (>= $5): 94.7%
  (2010) -> 99.8% (2025) with CUSIP + ticker + name keys. CAUSE: Datastream dead lists are ALPHABETICAL and DEADUS1-10
  stop at S -> universe file 2 (build_lseg_universe2.py, G:\My Drive\Screener project\LSEG\01_universe\
  LSEG_universe_v2.xlsx, DEADUS11-16 + Datastream retests) given to the user. Non-US-incorporated: 74-89% found; the
  missing are foreign primary listings (Canadian banks etc.) -> proposed rule "primary listing in the US" (addendum due).
  AFTER the user saves file 2: add its rows to the input, rerun as eq_univ_check_v3 (input change only, log it).
  Quiver vs Quantgress (2026-11-20): advised not to buy Quiver now; Quantgress free API covers Congress trades (history
  start unknown; user to create a key as a GitHub secret if wanted). Quiver connector: account has no subscription.
  2026-11-21: UNIVERSE CHECK v3 PASSES (US-incorporated top 1,500 >= $5: 99.3-100% every year with CUSIP + ticker + name;
  file 2 added DEADUS11-12 = T-Z; DEADUS13+ do not exist). USER: US companies only, RBC / ASML must NOT be in ->
  candidates = Datastream EQ lines with GEOGN 'UNITED STATES', primary line (ISINID P), alive 2010-2025: 26,932 (25,620
  with ISIN); list on the PC only (G:\My Drive\Screener project\LSEG\01_universe\universe_candidates_v1.csv; scratch
  recs.pkl lost if scratch is cleared -> rebuild from the two universe workbooks). STAGE A0 SIZE FILE given to the user:
  docs/data_requests/build_lseg_size.py CANDIDATES.csv OUT -> G:\...\LSEG\02_size\LSEG_size_v1.xlsx (78 blocks:
  year-end market cap 2009-2025 by ISIN, 1,000 companies per block, 3 sheets; Excel caps a text argument at 255 chars).
  NEXT after it is saved: select companies that could be in the 1,500 largest -> stage A monthly files (price, market
  value, volume, total return) + stage B account/estimate files (field_dictionary_raw_v1.0.csv: 51 of 52 names
  confirmed; goodwill open). CONVICTION JOB eq_conv_v1 queued (seal-exempt job 5, tools/equity/wrds/eq_conv.py, R2 + A4):
  20 investors with 13F ids; name search for Greenblatt (Gotham), Pilecki (Gator), Nygren/Fitch (Harris), Stahl (Horizon
  Kinetics), Davis (Davis Selected), Shaposhnik, Carlisle, Van Den Berg, Elfenbein -> ids into v2. Control overlap:
  Einhorn + Shaposhnik are in control AND roster (control = 8 until 2 replacements are drawn).
  2026-11-21 (later): SIZE FILE READ (A5): TR.CompanyMarketCap is company-level (repeats on share classes / preferred /
  depositary lines) -> drop non-common names, group by TR.CommonName, keep companies in the top 2,500 at any year-end ->
  5,065 companies / 5,537 lines (G:\...\LSEG\02_size\selected_lines_v1.csv, PC only). MONTHLY FILES (stage A) given:
  docs/data_requests/build_lseg_monthly.py SELECTED.csv OUT -> G:\...\LSEG\03_monthly\LSEG_monthly_part1-3_v1.xlsx
  (close, shares, company value, volume, 1-month total return 2009-12..2026-10; 250 lines per block; part 1 has a
  volume check block). The probe reader runs out of memory on big sheets -> write a streaming reader before reading
  them. eq_conv_v1 BUG (mod(yyyymm,3)) -> counts void; eq_conv_v2 queued with ids for Greenblatt, Pilecki, Harris,
  Stahl, Davis, Van Den Berg. eq_conv_v2 DONE (A6; report docs/research/equity/eq_conv_v2_report.txt): 26 of 29 with 13F,
  65 quarters, panel eq_conv_panel on WRDS; Greenblatt's Gotham 13F = quant book (910 names) -> not used for thresholds;
  firm-wide filers flagged.
  2026-11-21 MONTHLY FILES READ (docs/research/equity/LSEG_monthly_v1_2026-11-21.md; streaming reader
  tools/equity/lseg/read_monthly.py -> panel_monthly_v1.csv.gz on the PC in LSEG\03_monthly): 5,436 lines, 99% filled,
  returns aligned; monthly TR.Volume = LAST DAY's volume -> liquidity stand-in (A7). STAGE B FILES GIVEN (A7):
  docs/data_requests/build_lseg_company_data.py COMPANIES.csv OUT -> G:\...\LSEG\04_accounts (Q1-Q6 quarterly first-reported,
  A1 annual), 05_estimates (E1-E3 monthly consensus), 06_sector_short (S1 short interest, S2 GICS + actual EPS); company
  list G:\...\LSEG\02_size\companies_v1.csv (one primary line per company). NEXT: read stage B (streaming reader for
  accounts), build the measures (field dictionary v1.0) + lock; then the engine / reference book (step 5).
  2026-11-21/22 STAGE B LOADING: only LSEG_accounts_Q2_v1.xlsx (companies 851-1700) loaded and saved (04_accounts,
  47.6 MB); Workspace/Excel stalled on everything else (likely LSEG throttle + add-in hang; Excel crashed once). User
  REVOKED PC CONTROL (2026-11-21): no computer use; she refreshes herself. Fresh set = G:\...\LSEG\07_stageB_v3\
  01..12 (builder build_lseg_company_data.py v3 = ~20 blocks per file, quarterly 851-1700 skipped; file 12 =
  build_lseg_unadjusted.py, close as traded). Older v1/v2 files obsolete except Q2_v1. Reader for all stage-B files:
  tools/equity/lseg/read_stage_b.py OUT_DIR FILES (-> <kind>_<group>.csv.gz, columns = formula field names).
  FINDINGS (LSEG_measures_check_2026-11-22.md): quarterly CFO is one quarter (not YTD); MONTHLY CLOSE IS SPLIT-ADJUSTED
  while shares are as reported (close x shares wrong before splits; TR.CompanyMarketCap right; file 12 fixes price
  floor/line value); panel_monthly has repeated line-months (keep latest date); first-reported values thin in 2010
  (~2/3 of quarter rows filled, >90% from 2022). Adapter tools/equity/lseg/lseg_adapter.py feeds LSEG data into the
  same formulas as the WRDS engine.
  STEP 5 STARTED 2026-11-22: engine + reference book v1 on WRDS = tools/equity/wrds/eq_ref.py 1.0.1 (code c8705b6f...;
  seal-exempt job 6 reference_book; smoke test tests/eq_ref_smoke.py). Registered BEFORE any return: A8 in
  V04_REGISTRATION.md (spec choices a-f, Batch 0 contents, WRDS-form differences), FIELD_DICTIONARY_v1.0.md part 1
  (7 book measures + universe, LSEG and WRDS forms), TRIAL_LOG.md (NEW; T001 = Batch 0), SEAL_LOG entry. Queued on the
  PC WRDS runner: eq_ref_pull_v1 (ref_* data sets); THEN queue tools/wrdsq/jobs/eq_ref_v1.json (Batch 0 report) once
  the pull prints ALL PULLS COMPLETE (run() refuses if pulls are incomplete). Still open: second implementation by a
  separate agent; LSEG run of the same engine after stage B; daily engine.
  BATCH 0 DONE 2026-11-22 (eq_ref 1.0.2 e5a7ee9c, job eq_ref_v1c; v1 = gvkey key bug, v1b = stale code copy on the runner,
  both stopped before returns, logged): docs/research/equity/BATCH0_REFERENCE_BOOK_2026-11-22.md + eq_ref_v1c_report.txt.
  Plumbing passes (coverage 88-100%, ~1,100-1,190 ranked, GICS history, measures correlate with FF factors: mom/UMD 0.86,
  bp/HML 0.70, roe/RMW 0.57). Spreads 2010-25: mom +0.68%/mo, rev +0.57, Piotroski +1.92, book +0.68; bp -0.28 (only
  wrong sign). Book net 13.3%/yr vs sector-matched 12.2% (+1.0%/yr, t 1.24; eras +0.5 / -1.8 / +3.9; 2020 -7.1 pts). Cap
  2.5% only at formation (drift to 2.99%). No verdict. LESSON: after writing a runner lib file, READ IT BACK (stage) and
  compare before queuing (outputs copies can be stale). NEXT: second implementation (separate agent, from the written
  spec) before Batch A; LSEG run after the stage-B files.
  LSEG PIECES v4 (2026-11-22, user request): G:\...\LSEG\08_pieces_v4 = 56 small files (~0.5-0.7M values each; builder
  docs/data_requests/build_lseg_pieces.py COMPANIES.csv SELECTED_LINES.csv OUT; README.md + README_order.csv in the
  folder): P01-P18 FIRST (reference book: GICS, close as traded, 17 quarterly book items for companies 1-850 and
  1701-5065, FY1 EPS by month), B01-B38 later (other quarterly items, annual, other consensus, short interest, actual
  EPS). Old v1/v2/v3 templates DELETED on the PC (local job delete_old_lseg_templates_20261122: 34 files; folders
  05_estimates, 06_sector_short, 07_stageB_v3 removed; 04_accounts keeps only LSEG_accounts_Q2_v1.xlsx).
  read_stage_b.py / lseg_adapter.py accept the v4 groups (Q_C*, Q_R* merged with combine_first).
  SAY-DO TABLES (A9, descriptive, no return) DONE 2026-11-22: eq_ref 1.1.0 saydo() (c6021bb1), job eq_saydo_v1;
  docs/research/equity/saydo/SAYDO_2026-11-22.md + SAYDO_TABLE_2026-11-22.csv (masked ids) + eq_saydo_v1_report.txt.
  4,573 conviction purchases, 76% of roster purchases inside the test universe. Roster ~ control on average (large,
  profitable, low book to price; only gross margin differs > 0.05); investors differ widely (earnings yield 0.22-0.92);
  tilts on valuation / size / sales growth / momentum are stable odd vs even years (corr 0.79-0.92), Piotroski and
  revisions are not (0.37); high ROE is common to all incl. control. Mask is weak vs eq_conv_v2 counts -> writer
  packs must drop the count line. USER ASKED 2026-11-21 how fidelity to the investors is ensured and what a top
  investor would improve; answer given (deep read not started = step 6; proposed additions: primary writing, recall
  test of recipes on own purchases, held-out document, rule/example tags, sells and sizing, fewer investors deeper,
  concentrated long-hold version, business-outcome tests, tracker early, kill criterion): NOT registered, awaiting
  her choice.
- PLAN v0.3 (2026-11-15) = docs/research/equity/EQUITY_POD_SHOP_PLAN_v0.3.md (project doc
  claude/equity_pod_shop_plan_v0.3_2026-11-15.md): evaluation of the user's workflow idea (rank investors on 5-year
  returns to pick transcripts; technique transcripts as foundation; agentic pipeline transcript -> strategy -> portfolio ->
  backtest; judge on stocks they bought) + our own plan. v0.2 stays in force as the annex; where they differ v0.3 wins
  (its section 11 lists the amendments). Checked twice by separate Opus agents, corrections applied:
  EQUITY_POD_SHOP_PLAN_v0.3_check.md (5 must-fix / 17 should / 14 notes; ~236k tokens) and ..._recheck.md (0 / 9 / 10;
  ~212k). Three rules added after the re-check are unchecked (plan section 13) and go to the Stage 0 review.
  NEW LIBRARY (built by DocProcessor on the PC): G:\My Drive\Transcripts\Processed Transcripts = 2,257 documents, 17.0M
  words (AI CEO Interviews 883, General 695, Healthcare 431, Macro 214, Banking 24, Media 10); each has .txt with [Lnnn]
  anchors, .note.md with machine-checked quotes, _catalog.md; _system/manifest.json, search.db, search.py. General: 327
  documents with an investor present, ~240 names (191 appear once, 48 twice or more), 647 of 695 dated 2022+. Counts:
  docs/research/equity/library_inventory_2026-11-15.md (tools/equity/library_stats.py reads only the manifest). Raw
  folders not yet processed: Tech&AI, Energy, Consumer & Retail, Automotive & Industrial, AI Transformation, Real Estate,
  Crypto. The research branch (397 transcripts) is the older store.
  CONTENT: (1) INVESTOR SCORECARD on WRDS: 13F copy portfolios for ALL filers, windows 2011-15 / 2016-20 / 2021-25 /
  2011-25 only (never before 2011), style-adjusted, record grades A/B/C/F/N, persistence check -> tier A = 40 investors
  (30 by record, max 8 per style, + 10 with the most explicit criteria), 10 random control, tier B, foundation list
  (40-60 technique documents). The ranking orders the reading only; never proof. (2) HOLDINGS MODULE: sector ranks of
  purchases at the end of the quarter BEFORE, say-do table, revealed thresholds (odd years set, even years check), no
  later returns. (3) FOUNDATION TRACK -> methods register (definition / version / check / analyst question / dropped;
  never its own test slot). (4) ONE YARDSTICK: v0.2 test sheet; 8 registered slots (B1/B2) + "Incubator pass" (one
  design-era run for every other family, best outcome Incubator, fail = Shelved); investor families can NOT be Core on
  history (theses stated after 2010 by people picked on post-2010 returns): design era -> untouched regions ->
  holdouts reported by region -> promotion on the live record (joins the book, never labelled Core). (5) DATA: history
  on WRDS, live + second source on LSEG (needs an equity probe workbook of ~150 formulas, one refresh on the PC: dead
  companies, first-reported values, past consensus, holders, short interest), Bloomberg no role. Gate G8 amended: the
  scorecard and the holdings job are "registered descriptive jobs" that may read US 2011+, each run logged.
  NEXT (on the user's go): STAGE 0 = independent review of v0.2, E0.1 inventory/typing, E1.2 WRDS table check, E1.1 LSEG
  probe (side by side); then seal log -> register tier rule + "follow the best managers" signal -> E0.4 scorecard ->
  E0.5 tiers (= the investor league table and reading order). Then Stage 1 (engine, Batch 0, reference book live on
  paper, 16-document pilot). Vault: Method notes on macro-vault (61e384e); PC vault copy done 2026-11-15 (job
  vault_sync_20261115a, see the 1.3c entry).
- STAGE 0 DONE 2026-11-18 (user's go 2026-11-17): v0.2 reviewed (EQUITY_POD_SHOP_DESIGN_v0.2_review.md: 7 gating fixes
  applied to plan v0.3; Part 2 = 6 must / 15 should / 10 notes for the next plan version, due before the Stage 1 engine);
  E0.1 inventory of 635 General documents (docs/research/equity/inventory/: inventory.csv, investors.csv 241 names,
  agreement.md; Sonnet coders + Opus blind recode); E1.2 WRDS tables (no wrdssec/mfl: 13F = tfn.s34 first versions;
  CRSP stock months end 2025-12 = SEAL END; delisting returns inside msf_v2 mthret); E1.1 LSEG equity probe
  (LSEG_equity_probe_2026-11-18.md: first-reported vs restated accounts from 1983, consensus from 1990, holders from
  ~1999, insiders from 1998, no StarMine history, no manager portfolios); matching + frozen file
  (inventory/frozen_investors.csv: grades A 36, B 4, F 13, C 37, N 151); SEAL: reader tools/equity/wrds/eq_reader.py,
  checker tools/equity/seal_check.py, exempt list tools/equity/seal_exempt.json, lock e680ca33, SEAL_LOG.md; REGISTERED
  STAGE0_REGISTRATION.md at commit 184b5d0; scorecard code tools/equity/wrds/eq_scorecard.py (three independent reads +
  hidden-error test, SCORECARD_CODE_CHECK.md, scorecard_check/); pulls eq_sc_pull_v1/v1b (73 data sets, eq_sc_* kept on
  WRDS for a logged bug-fix rerun; job eq_sc_cleanup_v1 deletes them once the result is accepted); RUN eq_scorecard_v1
  once (the opening of the seal). RESULTS: docs/research/equity/SCORECARD_RESULTS_2026-11-18.md (project doc
  claude/equity_scorecard_results_2026-11-18.md) + scorecard_check/league_table_2026-11-18.csv. Records do NOT persist
  (rank corr +0.14 / -0.05 for 13F, +0.12 / -0.00 funds); only 2 library investors have 2021-25 t > 2. Tiers: A by
  record 30, A explicit 10, control 10, foundation 50 docs. NEXT (user's go): Stage 1 (plan v0.4 with the review's
  Part 2, engine, Batch 0, reference book on paper, 16-document pilot drawn from tier A).
- HF LEADERBOARD 2026-11-19 (user request): top 50 US + UK/Europe hedge funds >= $1bn by 5-year 13F top-20 return
  2021-2025, HedgeFollow method (verified: weights = PREVIOUS quarter-end 13F; 46/54 quarters match the site).
  docs/research/equity/hf_leaderboard/ (LEADERBOARD_2026-11-19.md, top50 CSV, Q3 2026 activity, reports); job eq_hf
  (third seal-exempt job; HF_LEADERBOARD_REGISTRATION.md; data sets eq_hf_* on WRDS). 42 of 50 have no transcript.
  FOUNDATION RANKING 2026-11-20 (hf_leaderboard/FOUNDATION_RANKING_2026-11-20.md + csv; project doc
  claude/hf_foundation_ranking_2026-11-20.md): user added 19 interviews (Processed\General Transcripts 2) + 18 articles
  (.md in raw General Transcripts, not processed). Return rank gated by process material: CORE Zlatev (Analog Century),
  Druckenmiller, Kantor (Encompass); WITH LIMITS Ruffer, Tropin/Graham, Shaver (Electron), Einhorn, Greenberg, Paulson;
  41 parked (29 with nothing, incl. #1 Gendell, #2 Harnisch). Sosin/CAS: 4 interviews but not in the WRDS universe.
- ANNEX docs/research/equity/EQUITY_POD_SHOP_DESIGN_v0.2.md (project doc claude/equity_pod_shop_design_v0.2_2026-11-15.md;
  replaces v0.1 of 2026-11-14, which was long-only): the macro pod-shop method applied to stocks as a LONG/SHORT book,
  market- and sector-neutral, slow (monthly signals, holdings of months to years, no intraday data; user 2026-11-15: no
  high frequency, long/short, statistical, logic verified by data). Four parts: (1) REFERENCE BOOK = plain long/short
  portfolio of published signals with a mechanism (value, momentum, quality, expectations; ranked inside the sector, no
  fitted weights): the benchmark every pod must add to, the plumbing test, the first live record (Stage 1) and the honest
  null; (2) investor pods = strategy families found bottom-up in the stock-picker transcripts (claims with quotes ->
  fingerprint cards -> strategy map -> charter -> spec), joined only for what they add to the reference book; (3) short
  and avoid rules (short where borrowable, else Exclusion); (4) analyst layer judged on a live forecast record (quarterly
  results vs consensus, scenarios, kill criteria; checkpoint 200 resolved). Chain tested link by link: rule -> selection
  -> business outcome -> surprise vs expectations -> price. Risk: own simple risk model, written risk charter (gross
  <= 200%, net market sensitivity within 0.1, sector net within 5%, long <= 2.5%, short <= 1.5%, target risk 8%; all
  proposals), shortable set (1,000 largest US, ownership floor, short-interest cap), flat borrow fee tested at double,
  netting across pods, crowding report, monthly attribution. Five decisive tests (adds to the reference book after all
  costs; not worse in any era incl. 2001-10; double costs; placebo; tail). Samples and seal as in v0.1 (design US
  1975-2010, untouched regions, holdout 2011+, live). Budget: Batch 0, Batch A (hygiene on the reference book), B1/B2
  (<= 4 pods each, Holm 2.5%). Banks, insurers, real estate and biotech stay out of generic pods. Section 2 of the file
  = the critique of v0.1 (14 points). SELF-REVIEW ONLY: the independent Opus review of v0.2 as a whole is still due
  (now part of Stage 0 of plan v0.3; order of work = plan v0.3 section 10).
  Steps are numbered E0-E7 to avoid clashing with macro steps.
- BIOTECH DESK (design v0.1, 2026-11-15; nothing built): docs/research/equity/BIOTECH_DESK_DESIGN_v0.1.md (project doc
  claude/biotech_desk_design_v0.1_2026-11-15.md) = sector desk on top of haing-dev/crash-triage + the 37 healthcare
  transcripts (26 investor talks by ten people, Kolchinsky 9 and Wong 6; notes only, no quote-level claims yet). Long book
  of 25-50 small positions + biotech-index hedge + exclusion list + small tested short sleeve + ODDS LEDGER (probability
  forecasts on pivotal results and FDA decisions, Brier-scored vs base rates, every event in the universe). Candidate
  pods P1 Aftermath (the triage), P2 Asset floor, P3 Run-up, P4 Odds, P5 Launch drift, P6 Specialist footprint, P7
  Financing reset; exclusions E1-E8; sizing by loss-if-wrong (<= 0.5% of capital per position scenario, <= 3% per 30
  days; proposals). History can reject a pod, only the live record promotes one (career overlap, no untouched regions).
  Event database + calendar as known built from SEC 8-Ks, ClinicalTrials.gov version histories, FDA letters (openFDA);
  hindsight rule for model-read history (quote-anchored fields only, masked re-read test). Steps B0-B6.
  DESCRIPTIVE RE-RUN of the public crash-triage backtest (docs/research/equity/biotech_checks/2026-11-15; the 2020-26
  sample is SPENT: the rules were chosen on it; 12-month return minus XBI): crash Avoid -59 points (n=490, every year),
  crash Watch -35, crash Buy candidates +15 (n=150, t 1.7, median below XBI, +7 without the 3 best; the top-performer
  subset of 23 carries it), slide Buy +1 (n=1,168), slide Avoid -28. So the warnings work; the Buy side is unproven and
  cannot be proven live (about 410 resolved calls needed, about 30 a year). A code comment in crash-triage
  pipeline/fit.py records an earlier WRDS test 1998-2023 of the top-performer pick (train 1998-2019); its report is in
  neither repo: step B0.1 finds it (PC results folders) before any year is called clean.
  Vault: both designs are Method notes on branch macro-vault (197c515); PC vault copy done 2026-11-15 (job
  vault_sync_20261115a, see the 1.3c entry).

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
