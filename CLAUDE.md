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
