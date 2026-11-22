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
