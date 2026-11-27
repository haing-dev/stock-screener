# Global Macro Book: rule changes and trial log

Every rule change gets a new VERSION in gm/run.py and a line here. Every variant tested on the design period
(1990-2010; extra check 1975-89) is logged so the deflated Sharpe can count the trials. The holdout (2011-2026) is run
once, after the rules are frozen, by gm/holdout.py.

## data: card inputs (FRED / ALFRED first release, macro-data branch) (registered 2026-11-27, BEFORE first use): 7.4 E15
Registered data entry (no rule change; no statistic of any card rule has been computed on these files; the builder
read only file metadata: first / last dates, row counts, the fetch mode in the branch manifests, and the size of month-
to-month jumps in the first-release levels for item 5). It is the "card inputs (FRED / ALFRED)" entry that "Pre-B
diagnostics" item 4 asks for; with it the pre-B job gm_diag_preb_v1 (not yet run) is extended in place (diag_preb
1.1.0, "Pre-B diagnostics" addendum below), not replaced by a v2.
1. Source: branch origin/macro-data, commit 264d0a2cc2f74d02264b30a52d5e8f0950db9cca ("macro data 2026-11-01T01:08Z"),
   written by the Macro Compass fetch (macro/fetch.py for the root files: registry.FRED, FRED API with the user's key,
   "first release" = ALFRED output_type 4 where registry.FRED has fr=True; macro/fetch_research.py for research/:
   public FRED csv = latest values, and research/<id>_FR.csv = ALFRED first release). Files (raw bytes as in the commit):
   | File | Mode (branch manifest "how") | sha256 | Serves |
   |---|---|---|---|
   | GS1.csv | api | 3ab25da1ce76f092ada31ea7ea83c89b98c7facbb7523049d5c504564c4ee7df | card 3 R3 (measure 2) |
   | GS2.csv | api | c92b08197af1084e93f09a06bd0fd5620e2a9eacb2f9e1956bd71fe250063dc9 | card 1 R2, card 3 R2 / R3, card 4 R5 |
   | GS5.csv | api | 4097a254739c4a69ae6b564f063ec1800986d40c56b3b5647264fd481ecb89b7 | card 1 R2 warning (a) |
   | GS10.csv | api | 14101ef859fbbacf0f0be00bc7a7ad70eea56b640a7a33b41a19982519639c60 | card 1 R1 / R2 / R3, card 2 R1 / R2, card 3 R2, card 4 R5 |
   | FEDFUNDS.csv | api | 1febfbfd22ef4d1e354d412ab224009f9df4214fd880e60e3b1d3d6f22798573 | card 1 R1-R4, card 3 R1 gate / R3, C3-D2, card 4 R5 v2 |
   | BAA.csv | api | a19a4e7230f5dbf42ad2b056b7b13a8cee53307f1ae893fb073d829a6e0f8f1c | card 1 R2 warning (b), R3 |
   | TWEXMMTH.csv | api | a5c1ea123197ae46207e489052debaf4cc1309d734a356eeff3900717dc7d33e | card 1 R1 dollar (to its last month) |
   | DTWEXBGS.csv | api (daily) | d1c0528a9e337567a70a576a2721829446551d1d6e00a1e7d6197723dfb1e33d | card 1 R1 dollar (after TWEXMMTH) |
   | WTISPLC.csv | api | 0f917359164123db1598402e455c1694e8c639fe58b9cc8e66ba03bcc3d5f4ef | card 1 R1 oil |
   | VIXCLS.csv | api (daily) | 1c4696be0611e16d07d696bced9182b5dada3fc0e0850ea7b63bb25941efaaf4 | C4-D1 |
   | M2SL.csv | first release | 871ca3301a05ad1b462fb26edc408a8eeeb9d14a6e6f3b9a564c0825a80074bf | card 1 R2 warning (c), first published |
   | PCEPILFE.csv | first release | 2580087dc66e991d6e4275d7602ebd3bd8c96963eb87d157ceb9bca4e0590a18 | card 3 R3, first published |
   | research/CPILFESL_FR.csv | first release | 32f8c0ab27789d3cafac39644cfd239ca62846cb67c440eaf50fb02b7edc75a8 | CPILFESL first published (cards 1, 2, 4, 5) |
   | research/UNRATE_FR.csv | first release | 32a5962ede84fe0a42e7b1dac474dc91ba326432881878d7470a3777328295b0 | UNRATE first published (card 2 R2) |
   | research/CPILFESL.csv | latest | 90d152a56c2be24e3a595308feff963d22c8431dda24cc9f948c12c420a19a50 | CPILFESL in months without a first vintage (flagged) |
   | research/UNRATE.csv | latest | 65fb73bccaa4086aaaf3d19fbae5802daa62401ea3383322c1c5046468757c45 | UNRATE in months without a first vintage (flagged) |
   | research/M2SL.csv | latest | c745c8995d819bbee56d32156cd1e3c514db199df23606886ad7aef0cc0b4a9d | M2SL in months without a first vintage (flagged) |
   | research/PCEPILFE.csv | latest | cdf87be0d6669f8346c08b853b3b78bf669f84f9a6f028208b24587a641271f3 | PCEPILFE in months without a first vintage (flagged) |
   | manifest.json (root) | - | 2d0213bd625eb5b71d8aa8249971b225b002d32e3410defff22cdb1fb4025561 | provenance only: the "how" of every root file |
   TB3MS and the OECD IR3TIB01 rates stay on the free inputs (they are engine inputs already); not in this lock.
2. Which file serves which input, and why:
   - Rates, spreads, the dollar, oil, VIX (lag-0 / market or unrevised series): the ROOT files. They are the Macro Compass
     live fetch (macro/fetch.py, registry.FRED): the same series, from the same fetch code, serve history and live
     (item 7). research/ copies of GS1, GS2, GS5, GS10, FEDFUNDS exist but come from another fetch path; not used.
   - First published (the specs: card 1 s3 step 2 "each month's first-published value from ALFRED where a vintage
     exists"; card 2 s3 "CPILFESL and UNRATE as first published where vintages exist, else latest, flagged"; card 3 s3
     "PCEPILFE as first published where vintages exist, else latest, flagged"; card 4 s3 R5 and card 5 s3 R1 step 4
     "first published ... as card 1"): CPILFESL and UNRATE from research/*_FR.csv (the named first-release files);
     M2SL and PCEPILFE from the ROOT files, whose branch manifest records how = "first release" (macro/fetch.py with
     fr=True and the FRED key: ALFRED output_type 4). So first vintages of M2SL and PCEPILFE DO exist on the branch
     (the coordinator's note listed them as missing; corrected here from the manifest). Check (builder, metadata):
     the root CPILFESL.csv and UNRATE.csv hold the same dates and values as their _FR files (the root files are not
     used). First-vintage coverage: CPILFESL from 1996-12, UNRATE from 1960-03, M2SL from 1980-01, PCEPILFE from 2000-07.
   - Months without a first vintage (before those starts): the research/ latest file of the same series, each such
     month flagged, as every spec writes ("Months with no vintage use the latest value and carry a flag; the share of
     flagged months is reported", card 1 s3 step 2; cards 2-5 "else latest, flagged"). No row stays blocked for want of
     a vintage.
3. Cut and seal: the reader (tools/bbgq/lib/card_inputs.py) drops every observation dated after 2010-12-31 before it
   computes anything; its outputs are checked by gm/seal.py like every design input. The zip holds the raw files
   whole (so their hashes are the source's); no function returns a later value.
4. As-of (release lag, the specs' own wording; "A lag of 1 means the last value used at t is month t-1", card 1 s3 step
   1): FEDFUNDS 0, GS1 0, GS2 0, GS5 0, GS10 0, BAA 0, TWEXMMTH 0, DTWEXBGS 0 (card 1 s3 step 1; card 3 s3 R2 / R3
   "Lags 0"; card 4 s8 "FRED, lag 1 / 0"); WTISPLC 1, CPILFESL 1, M2SL 1 (card 1 s3 step 1); UNRATE 1 (card 2 s3);
   PCEPILFE 2 (card 3 s3 R3 step 2); VIXCLS 0 (card 4 s8 "FRED, lag 0"; C4-D1 reads the month's average). Daily series
   (DTWEXBGS, VIXCLS) enter as the mean of the month's daily values (card 1 s3 R1 step 1: "monthly average of daily
   values, the same averaging as TWEXMMTH"; C4-D1: "the month's average VIXCLS"). The monthly averages of lag-0 series
   carry 7.3 item 4's registered one-day tolerance; nothing else is shifted.
5. First-published changes (card 1 s3 step 2: "a change (12-month growth) is computed from two first-published
   values"): a change over months m - k .. m uses the two first-release values when both exist and are comparable, else
   the latest values of both months, flagged. Comparable: no first-release level break inside m - k + 1 .. m, a break
   being a month whose first-release month-to-month change differs from the latest series' change of the same month by
   more than 2 percentage points (an index rebase or a unit change moves the level by the base ratio, 6-8% for the two
   PCEPILFE rebases inside the design years and about 1000x for a unit switch; one month's revision moves it by far
   less). Reason: two first-published values from vintages with different base years are not a change of the series
   (the Macro Compass reader corrects the unit case the same way, macro/engine.py _unit_breaks). The reader prints the
   break months found (metadata) and every report prints the flagged share per input. Levels used as levels (UNRATE
   against its own prior 240 values) use the first-release value where it exists, else latest, flagged.
6. Lock: docs/research/card_inputs/LOCK_CARD_v1.json (commit, seal date, the file table of item 1), lock id =
   sha256(json.dumps({"source": "origin/macro-data", "commit": ..., "seal_date": "2010-12-31", "files": {path:
   sha256}}, sort_keys=True)) = 6c154f7d736cefd141fac2252a71536811e7440724d8e3cb4d4eacfecb8e3110. Packaging: a
   separate small zip work\free\gm_card_inputs.zip built from git at that commit (tools/bbgq/build_card_inputs.py),
   checked file by file against the lock by the reader; the free inputs zip, its digest, engine_ref.json and the k = 0
   reproduction are untouched (the card inputs are not engine inputs).
7. Live: the same FRED series by the same fetch (macro/fetch.py, FRED API; first release where registry.FRED has fr
   = True), same lags; registered as a live source for the card rule layers under 7.10 item 1 ("Free public data
   qualify"). The live cycle needs no LSEG or Bloomberg input for these rows.
8. Inputs still not available: none of the rows of "Pre-B diagnostics" item 4 needs anything beyond this entry, the
   free inputs and LOCK_LSEG_v5.
Code (2026-11-27; this entry 12e108c before the code 049ab75): reader tools/bbgq/lib/card_inputs.py 1.0.0 (sha256
4091f84bcbb11f43061bcc0330520a4a5580cb775895148a38849c0fbcab7b80), builder tools/bbgq/build_card_inputs.py (from git at
264d0a2, deterministic zip, sha256 4f84b01d07ad59da05ad7e8ca4e78b31b1ed687941c6852da804c685be1b068d), lock
docs/research/card_inputs/LOCK_CARD_v1.json (lock id 6c154f7d...); build_engine ships the zip as
work\free\gm_card_inputs.zip and lib\card_inputs.py. Metadata facts printed by the builder (no value): first vintages
CPILFESL 1996-12, UNRATE 1960-03, M2SL 1980-01, PCEPILFE 2000-07; first-release breaks by item 5: PCEPILFE 2003-11 and
2009-06 (the two rebases), M2SL 1983-01 and 1996-01 (first-release level shifts against the revised series); CPILFESL
none; UNRATE is used as a level only (no break rule); the root CPILFESL.csv and UNRATE.csv equal their _FR files up to
2010-12-31. The free inputs zip, engine_ref.json and the k = 0 reproduction are unchanged.

## Pre-B diagnostics (registered 2026-11-27, BEFORE the diagnostics code and run): TESTING_PROTOCOL 7.6 step 7, 7.5 order item 3
Registered run entry (no rule, weight, threshold, gate, cost or market change; no gm/ code change; no statistic of any
diagnostic below has been computed on real data, cloud or PC). The A1 panel (Bloomberg values) and the LSEG store exist
only on the PC, so every diagnostic is computed by one PC job (tools/bbgq/jobs/gm_diag_preb_v1.py, library
tools/bbgq/lib/diag_preb.py). The builder has read the reports the job pins (gm_a2_v1, gm_diag_v1, gm_core_v1); no
choice below reads a result: each is closed from the registered text, with the reason given.
1. The registered text. 7.6 step 7: "The pre-B diagnostics of 7.5 order item 3." 7.5 order item 3: "After Core book v1
   (7.6 step 6), before B2 is run: R1 (needs daily dollar contracts 1-8 locked), C1-D1, C1-D2, C2-D1, C2-D2, C3-D1,
   C3-D2, C4-D1, C4-D2, C5-D1, C5-D2, F0." 7.5: "No diagnostic adopts anything or uses a Holm slot (charter s5). Each
   is logged as a design-data run (7.8)"; "Every diagnostic reads positions, signals or its registered outcome only;
   none reads a sealed day after its fix." Gates: the 7.5 table rows R1, F0, C1-D1 .. C5-D2 with their 3.4 fixes, the
   paragraph on the "already held" thresholds, and the specs' section 13 (SPEC_Strip_reversion, SPEC_Card1-5).
   Consequences: 7.6 step 9 (B2 = Strip reversion "only if R1 passes and daily settlements of dollar contracts 1-8 are
   locked (else dropped unbuilt, logged); Curve carry if moved; and every card rule that survives its gates").
2. Book and data. "The registered systematic book" (7.5: "the four existing pods in their final Batch A form at the
   CANDIDATE shares, all parts (Core and Incubator), sign of its net position per market (book.run "pos")") = the
   A2-final book A1_INCUMBENT gm-2.0.4-candidate-x1 (config 77374d7bef), engine gm-2.2.1, no grid, on the A1 panel
   e7f98d4439fccf91f3451bc4b9e78079e3bc2cc2452931363b28520460b6cb43, every loader cut at 2010-12-31; its positions are
   book.run's "pos" (identical at k = 0 and k = 1, "Diagnostics after A2" item 2), checked as run against the A2 report
   (diag_a2.as_run) before any diagnostic line. Free inputs: the shipped zip (TB3MS, the OECD IR3TIB01 3-month rates,
   ^GSPC daily closes, panel.fx_usd_value). LSEG: LOCK_LSEG_v5 90322681b9f989cc24393ae7de4fe24bf5af2f32074ffa6400b1cbed09c4074c
   (data entry "LSEG registered as a source for history"), lsegdata-1.0.0, lseg_rules-1.1.0, design part only, as of
   2010-12-31; its item 4 names the inputs read here: "Strip reversion strips", "card 3 R4 forward EPS", "card 5 R1
   fronts" (and SPEC_Card5 s8 lists "for D2 also cocoa, LME cash, grains" as LSEG). Volatility of every card position:
   the engine hybrid estimate with the CANDIDATE vol config (the card specs s5), on the A1 panel and the free daily
   returns; no volatility, no position.
3. The empty Core book (CORE BOOK V1 RUN: "CORE BOOK V1 EMPTY"). How each diagnostic reads:
   - C3-D1 (the only row that names the "Core book"): 7.5 fix "'Core book' read as the registered systematic book
     (below), because the question is content, not trading status (Core book v1 exists by then but holds Core parts
     only)"; and "Core or Incubator is a trading status, not a content question". So C3-D1 compares with the registered
     systematic book of item 2, which an empty Core book v1 does not change.
   - C1-D2: "> 80% of held months same sign as the registered systematic book": the same reference, unchanged.
   - C5-D1 and C4-D2 name Trend: ">= 75% of held months with the 12-month Trend versions long" (C5-D1), "R5 overlap
     with card 3 R2 and Trend" (C4-D2). Trend is a pod of the registered systematic book (Incubator since Core book v1);
     the reference is content, so the empty Core book changes nothing.
   - R1, C1-D1, C2-D1, C2-D2, C3-D2, C4-D1, C5-D2, F0 name no book. F0's pass reads "judged in B2", where B tests "read
     alpha against a zero book (the pod's own mean)" (7.6 step 6): a B2 matter, not this step's.
4. What runs now and what is blocked (inputs checked against the free inputs (docs/research/batches/
   META_first_dates_2026-11-27.txt), the A1 panel and LOCK_LSEG_v5; "blocked" = an input not in any registered source):
   | Id | Runs | Inputs | Blocked by |
   |---|---|---|---|
   | R1 | yes, PC | LSEG ED quarterly contracts, daily (deliveries 1982-2012, L14), NYSE days | - |
   | C1-D1 | R5 only | R5: panel.fx_usd_value | R1-R4: FEDFUNDS, GS2, GS5, GS10, BAA, TWEXMMTH / DTWEXBGS, WTISPLC, CPILFESL, M2SL (ALFRED) not in the free inputs |
   | C1-D2 | R5 legs only | R5 + the book | R1-R4 legs: as C1-D1 |
   | C2-D1 | yes, PC | TB3MS, IR3TIB01 JP / DE then EZ / GB / CA, panel bonds and indexes | - |
   | C2-D2 | no | - | card 2 R1, R2 (GS10, CPILFESL, UNRATE) and card 1 R4's state (CPILFESL, FEDFUNDS) |
   | C3-D1 | R4 only | LSEG S&P 500 forward EPS, ^GSPC month-end, TB3MS, the book | R1 (FEDFUNDS gate versions), R2 (GS2, GS10), R3 (FEDFUNDS, GS1, GS2, PCEPILFE) |
   | C3-D2 | no | - | FEDFUNDS |
   | C4-D1 | no | - | VIXCLS |
   | C4-D2 | no | - | card 4 R5 (CPILFESL, FEDFUNDS, GS2, GS10), card 3 R2 (GS2, GS10) |
   | C5-D1 | yes, PC | LSEG HG c1, CL c1 (monthly), the A1 panel (Trend 12-month versions, volatility) | - |
   | C5-D2 | yes, PC | LSEG c1 of HG, CL, W, C, S; LCC c1, LME cash (reported line) | - |
   | F0 | card 1 R5, card 3 R4, card 4 R1-R4, card 5 R1 | as their rows / ^GSPC daily | card 1 R1-R4, card 2 R1-R2, card 3 R1-R3, card 4 R5: as above |
   No input needs a new LSEG pull. The blocked rows need ONE registered data entry before their run: "card inputs (FRED /
   ALFRED)" = GS1, GS2, GS5, GS10, FEDFUNDS, BAA, TWEXMMTH, DTWEXBGS, WTISPLC, VIXCLS, UNRATE and the
   ALFRED first vintages of CPILFESL, M2SL, PCEPILFE, UNRATE (A1 entry item 8 already lists them as "card inputs,
   fetched before B2"), fetched once, cut at 2010-12-31, locked (file hashes) apart from the free inputs zip, with the
   metadata listing of 7.6 step 2; then a job gm_diag_preb_v2 (its own dated entry) runs the blocked rows with the
   rule signals of their specs. The rows that run now are not re-run then. B2 cannot start before the blocked rows run
   (7.5: each card rule is "judged in B2" only after its gates).
   R1's precondition "daily dollar contracts 1-8 locked" (7.5, 7.6 step 9): met by LOCK_LSEG_v5 (contract-level
   Datastream daily, identity in the code; IDENTITY_STATUS item 11: "Eurodollar 1990-2010 all eight quarterly contracts
   priced on 5,475 of 5,480 trading days"); the 7.11 blocker ("contracts 3, 5, 6, 7 not pulled, monthly start dates of
   5-8 unknown") is closed by the L14 pulls and the lock. The job re-counts this coverage before R1 (printed, no gate).
5. Closed here (the simplest reading of the registered text; none chosen from results):
   R1 a. Contracts: catalog rows of the LSEG store with per D, status ok, no duplicate_of, function DS, code
      "<ED" + H / M / U / Z + year digit + "^" + decade digit + ">" (lsegdata RIC_RE; decade digit >= 5 -> 19xx, as
      lseg_contract_v3); serial months are not used (spec s3 step 1); one source (Datastream daily), so no strip mixes
      settlement conventions. Settlement on a day = an observation dated that day (no carry-forward).
      b. Last trading day: lseg_rules.dates("ED", y, m) (registered rule, matches the observed last priced day).
      c. Trading days = NYSE days (gm.execution.nyse_days on the free ^GSPC closes, cut at 2010-12-31; 7.3 item 6).
      Decision day d of month m = its last NYSE day; next trading day d1 = the next NYSE day; month-end of the normal =
      the last NYSE day of each month from 1981-12.
      d. Holding end h(d) = the first US business day of month m + 2 by lsegdata's US holiday calendar (calendar
      arithmetic: for d = 2010-11-30 it lies in January 2011, and no 2011 price or NYSE date is read). The strip
      depends on h only through "last trading day after h", and every ED last trading day falls on or after the 13th of
      its month, so any day in the first week of month m + 2 gives the same strip.
      e. Strip at d: contracts 1-8 = the first eight quarterly ED contracts by delivery whose last trading day is after
      h(d). A month-end d is in R1 only if all eight have a settlement on d and on d1 (spec s3 step 1; d1 is where the
      second gap is read).
      f. r_k = (100 - settlement) x 100 bp; y_n = mean of r_1..r_n; K_n = 2 y_n - y_(n-1) - y_(n+1), n = 2..7.
      g. Normal of K_n at d: the mean of K_n over the earlier month-ends e < d (from 1981-12) whose contract n (on e's
      own strip, h(e)) expires in the same calendar month as contract n at d, using e only where contracts 1..n+1 each
      have a settlement on e's last NYSE day (7.5 fix: "replaced by the last trading day's settlement, else left out of
      the normal"); "screened or not" (spec s3 step 5): no stale screen inside the normal. It exists at d if the
      measure's first month-end value (any group) is at least 60 calendar months before d and the group has at least
      one earlier value. G(d) = K_n(d) - normal; G(d1) = K_n on d1's settlements of d's strip - the same normal.
      h. Stale screen at d: each contract 1..n+1 (every contract with a non-zero weight in K_n) must have changed on at
      least 15 of the 20 NYSE days before d (d excluded); a change on day t = settlements on t and on the NYSE day before
      t that differ (a missing settlement is no change). A triple-month with a failing contract is left out of
      numerator and denominator (7.5 fix) and counted.
      i. Cost of K_n = 2 x 0.5 x (2n + 4) / (n (n + 1)) bp. A triple-month qualifies when |G(d)| > cost, |G(d1)| >
      cost and sign G(d) = sign G(d1).
      j. Month-ends: from the later of 1990-01 and the spec s7 start (the first month-end at which the strip exists and
      every measure of at least one version, S_2..S_8 or K_2..K_7, has its normal by g; S_n = y_n - y_(n-1) on contracts
      1..n, grouped by contract n) to 2010-11 (7.5 fix); a triple-month enters where its normal exists ("where a normal
      exists", spec s13).
      k. Gate (7.5): qualifying / eligible >= 0.5 -> R1 PASS: Strip reversion enters B2 with both versions; else
      dropped unbuilt and logged. Printed: eligible and qualifying counts and the share, by n; left out by reason (no
      normal, strip missing on d or d1, stale); the first normal month per measure; NYSE days 1990-2010 with all eight
      contracts priced. No return is computed.
   F0 a. Held month: monthly rules: a decision month t (position decided at month-end t, held over t + 1) from the
      rule's start (its spec s7) to 2010-11 (7.3 item 5: "the decision at month-end 2010-12 is never traded"); card 4's
      daily date rules: a design month 1975-01..2010-12 with at least one NYSE day whose return the averaged rule earns
      with a non-zero position (held days: entry < day <= exit; a window running into 2011 ends at the last NYSE day of
      2010, SPEC_Card4 s7).
      b. Averaged rule position = the mean over the rule's registered versions, an off version counting 0; non-zero =
      not exactly 0 (versions that share one volatility are summed as integer directions, so a cancellation is exact).
      c. Episodes: a new episode starts at a held month whose previous held month is 12 or more months earlier (month
      index difference >= 12). d. Judgeable = at least 48 held months and at least 3 episodes; else "not judgeable"
      (analyst watch condition).
      e. Entry versions (card 1 E1 / E3), sizing versions (card 3 max(vol, expanding median), card 5 50% cap) and C4-D1's
      half-size version multiply a position by a positive factor over the same months (E3 holds one third or full, of the
      same sign, from the same first month): they change neither sign nor held months, so positions for every count here
      are built from the versions without them.
      f. Card 5 R1's real-ceiling versions need CPILFESL (blocked), but a ceiling version holds a subset of its
      non-ceiling twin's months (runs start only at trigger months; the ceiling only ends a run early) and every R1
      position is long; so the averaged rule's non-zero months are those of the four non-ceiling versions (H 24 / 36 x
      crude out / in). F0 and C5-D1 for card 5 R1 use them on this reading of the rule text.
      g. Known from the rule text before any data: card 4 R1 form A holds every year from late October or mid-December
      to mid-January (gaps of 10 or 11 months), R2 holds a window before every monthly expiry and R4 one around every
      month end; so under F0 c each has one episode whatever the data and is "not judgeable" when F0 is computed. This
      entry changes nothing about it (7 intro: a change needs a numbered sub-section 7.12, dated and committed before the
      run it affects); the job computes F0 as registered.
   C1-D1 / C1-D2 / F0 card 1 R5 a. m_i(t) = 100 x (v_i(t) / v_i(t - 6) - 1), v = panel.fx_usd_value at month-end, for
      the universe EUR, JPY, GBP, AUD, CAD (spec s3 R5 step 1); trigger of currency i at t (version G): at least three
      universe currencies have m(t), and m_i(t) <= their median - G, G = 15 or 10.
      b. A currency's legs are held at t when it triggered in t - 12 .. t (the 12-month tail, "to 12 months after the last
      one", inclusive); stock leg = its index (both versions), bond leg = its 10-year bond (version "stocks and bond");
      a leg holds a position only where its market has a volatility at t.
      c. C1-D1: condition months = months with a trigger of any universe currency at G = 10 (which contains every G =
      15 trigger: "any version"); tail months not counted (spec s13); episodes as F0 c; gate: fewer than 6 -> analyst
      watch condition (and 7.5: "kept with F0 (both must hold)").
      d. C1-D2: a leg = one leg of the rule text (R5: the stock-index leg, the bond leg), counted over the market-months
      in which the averaged rule holds that leg (any version, tails included) pooled across its markets; same sign = the
      book's pos of that market at t has the leg's sign (a zero or missing book position is not the same sign); gate:
      share > 0.80 -> the leg is dropped.
   C2-D1 a. Countries and rates as SPEC_Card2 s13: US TB3MS; JP IR3TIB01JPM156N; DE IR3TIB01DEM156N, then
      IR3TIB01EZM156N where DE has no value; GB IR3TIB01GBM156N; CA IR3TIB01CAM156N (the named series only: no call-rate
      fill for Japan); stock index and 10-year bond = panel monthly excess returns of eq_us_spx / bd_us_10y,
      eq_jp_nikkei / bd_jp_10y, eq_de_dax / bd_de_10y, eq_gb_ftse / bd_gb_10y, eq_ca_tsx / bd_ca_10y; design months
      1975-01..2010-12.
      b. Worst fifth: the months in which the stock index's return is at or below its 20th percentile (numpy linear)
      over its design months with a return. Short rate = the rate of the same month (the state the month was in); low =
      below 1.0, other = 1.0 or above; a month needs the bond return and the rate.
      c. Pooled over the five countries (Japan also reported apart; Japan alone may make up the pooled count, spec s13).
      Gate: at least 30 pooled low-rate months, the other mean above 0 and the low-rate mean below half of it -> PASS:
      floor versions (TB3MS at least 1.0) on card 1 R1 and R2 (+16, +32 with entry) and a stop line in card 2; else no
      change.
   C3-D1 card 3 R4 a. E(t) = 100 x EPS(t) / X(t), EPS = LSEG DS:@:USSP500|A12FE at month-end t (delay 0, lag 0, spec s3
      R4 step 3), X(t) = the last ^GSPC daily close of month t; on while E(t) - TB3MS(t) < B, B = 1.0 or 0.0; short
      eq_us_spx; decision months from the first EPS month to 2010-11.
      b. Share of held months (any version) in which the book's eq_us_spx pos is negative. Gate: >= 0.80 -> R4 dropped
      before B2; 0.50 to 0.80 kept and flagged. The spec's reported lines (cards 1 and 2 in shared markets; R1 against
      Economic trend's monetary theme; R3 against Carry's directional bonds) need blocked rules: not printed.
   C5-D1 / C5-D2 / F0 card 5 R1 a. P = the LSEG continuous front c1 month-end close as served (HP:HGc1|CLOSE copper,
      HP:CLc1|CLOSE WTI; monthly; spec s3 R1 step 1). Trigger at t: P(t) above every earlier month-end P of the series,
      with at least 120 earlier values. Long from a trigger month to H months after the last trigger month (inclusive),
      H = 24 or 36; copper always, WTI in the crude versions; a position only where the market has a volatility on the
      A1 panel.
      b. C5-D1: over R1's held market-months (any version), the share in which the 12-month Trend versions (config
      TREND_GRID with h = 12: sign and graded, hybrid and 36-month volatility; book._trend_version on the A1 panel; each
      version's position sign where it and its volatility exist, a missing version counting 0) are long by average sign
      (mean of the four signs > 0). Gate: >= 0.75 -> R1 not registered. This row names its own reference ("12-month
      Trend versions"), so the book's net sign is not used for the gate; it is printed beside as a reported line. The
      R2 part is not computed (R2 held back).
      c. C5-D2: a break = a trigger month (a) with no trigger in the 12 months before it, up to 2008-12; higher = P(t + 24)
      > P(t). Slow class = copper (the markets R1 can trade; crude reported apart); grains = W, C, S c1 pooled. Gate:
      slow share at least 0.15 above the grains share and at least 10 breaks in each class; fewer breaks = not passed
      -> R1 dropped unbuilt. Reported line: London cocoa (HP:LCCc1|CLOSE) and the LME cash prices (DS:LCPCASH, LAHCASH,
      LZZCASH, LNICASH, LEDCASH, LTICASH) pooled.
6. What each outcome triggers (an "outcomes" paragraph under this entry after the run; nothing is adopted here): R1 ->
   Strip reversion in B2 or dropped; C1-D1 -> card 1 R5 stays or becomes an analyst watch condition; C1-D2 -> each R5
   leg stays or is dropped; C2-D1 -> floor versions and a card 2 stop line, or no change; C3-D1 -> card 3 R4 kept,
   flagged or dropped; C5-D1 / C5-D2 -> card 5 R1 registered and built, or not; F0 -> each computed rule "judged in B2"
   or "not judgeable". Spec edits are text changes after the run, each citing this entry.
7. Printing (tools/bbgq/README.md export whitelist): shares, means and gaps only over at least 60 months; a smaller
   group prints its count and the sign of its value; gates PASS / FAIL; counts, months and ids. C5-D2's break shares
   are printed as counts only when a class has fewer than 60 breaks. No LSEG or Bloomberg value is printed.
8. Trial count (7.8 item 1, family "diag"): one gm/trials.csv row per diagnostic run: R1, C1-D1, C1-D2, C2-D1, C3-D1,
   C5-D1, C5-D2, F0 (8 rows, no Sharpe columns; hash = config hash of the id, diag_preb version, book hash, A1 panel id
   and LSEG lock id), written by the coordinator from the job's TRIAL ROW lines; the blocked rows get none.
9. Job (tools/bbgq/jobs/gm_diag_preb_v1.py on the PC; the gm_core_v1 pattern): STOP before any Bloomberg or LSEG value
   is read unless the gm .py files equal engine_ref.json's code block; sha256(lib\engine_ref.json) = cebd4932...c955e39;
   config.ENGINE_VERSION gm-2.2.1 and the four config hashes; the lib files (diag_preb, diag_a2, a2_batch, a1_panel,
   gm_engine, bbg_panel, bbgdata, lsegdata, lseg_rules) have the sha256 registered in the job; the book / pod rows of
   lib\gm\trials.csv have the digest f200d02ce574f002753c0d9ad54ae7a082c8e7f3d2ad120a14905fcf498e268a, N = 41 (40 + the
   Core book v1 row); results\gm_a2_v1.txt gives the A2 facts; results\gm_diag_v1.txt has the A3-empty summary;
   results\gm_core_v1.txt has "CORE V1 JOB DONE" and "CORE BOOK V1 EMPTY"; the Bloomberg store is LOCK_v2; the LSEG
   store's lock id is LOCK_LSEG_v5; the free inputs match the reference; the free arm matches engine_ref.json. Then it
   rebuilds the A1 panel, asserts extension-only and the registered id, compares it with the saved file when present
   (STOP on a difference), writes nothing, checks the A2-final book as run, and prints the diagnostics and the TRIAL
   ROW lines.
10. Cloud: no diagnostic statistic is computed on the free, A1 or LSEG data. Cloud work = the code, tests on synthetic
   panels and a mock LSEG store (tests/diag_preb_smoke.py in tests/run_tests.py), the engine gates (k = 0 reproduction
   24 of 24, truncation 8 of 8; gm/ is unchanged, so engine_ref.json is unchanged).
Correction found while coding (2026-11-27, BEFORE any run; from the rule text, no data; item 5 F0 g is not rewritten):
item 5 F0 g is wrong for card 4 R1. Its six versions are averaged, and on a day inside one entry's window form A (+1),
form B (+1 above last year's close, else 0) and form C (+1 above, -1 below) sum to 3 above the bar and to 1 + 0 - 1 = 0
below it: the averaged R1 rule is flat in every year whose close before both entries is below the previous year's
close. So R1's held months and episodes depend on the data, as for any state rule; the job computes them. What stays
true from the rule text: card 4 R2 (every version long before every monthly expiry) has one episode on any data; R4
holds around every month end unless both versions' month-to-date signs cancel or are exactly zero, so it has one
episode unless that happens in 11 months running. F0 is computed as registered for all four.
Correction 2 found while coding (2026-11-27, BEFORE any run; no data read): item 5 C5-D2's "Reported line: London cocoa
(HP:LCCc1|CLOSE) and the LME cash prices" is NOT computed. Those instruments are held back: tools/lseg/lseg_untouched.csv
(part of LOCK_LSEG_v5's config) lists LCC and CC futures ("alternative commodity not in the book") and the LME cash / 3m
prices, and lsegdata hides them unless Panel(allow_untouched=True), which no registered entry grants for a design run
(the A1 rule likewise excludes held-back markets). The job opens the LSEG store with allow_untouched=False and prints
the line as "not computed (held-back instruments)". The gate (copper against wheat, corn, soybeans) is unchanged; no
gate input is held back (HG, CL, W, C, S, ED, the S&P 500 forward EPS are not on the list).
Code and cloud gates (2026-11-27; entry 6497db6 and corrections bd6e3f5 before the code fd760ae; no diagnostic
statistic computed in the cloud): tools/bbgq/lib/diag_preb.py 1.0.0 (sha256
072b3dbe075353cc2ad6a3b2a95e0c50e97221ec05a8fddcf20b813493d11c77), PC job tools/bbgq/jobs/gm_diag_preb_v1.py (sha256
in docs/research/batches/PREB_BUILD_2026-11-27.md), tests/diag_preb_smoke.py (52 checks, in tests/run_tests.py),
build_engine ships diag_preb, the job and the LSEG reader files (lsegdata 0d1b500d... = LOCK_LSEG_v5's code hash,
lseg_rules 56869991..., the config CSVs = the lock's config hashes). gm/ unchanged, so engine_ref.json is unchanged.
Gates: k = 0 reproduction 24 of 24, difference 0 (tools/bbgq/results/engine_repro_cloud_2026-11-27g_gm-2.2.1.txt);
truncation PASS at all 8 cut dates, 21 k = 0 and 37 feature stages (results/engine_trunc_cloud_2026-11-27g_gm-2.2.1.txt);
run_tests ALL TESTS PASSED (results/run_tests_gm_2026-11-27i_gm-2.2.1.txt). Test-only fix in the same round: the
diag_a2 and core_v1 smoke tests read the trial log as shipped to their jobs (tests/data/trials_core_v1_shipped.csv,
book / pod digest 676b7b0f..., N 40), because the Core book v1 row appended at c69083e broke their record pin (6
failures in run_tests before the fix; no job or lib changed). Closed while coding (no rule change): the job opens the
LSEG store with allow_untouched=False after reading its lock id from the manifest; card 4's day windows that run past
2010-12-31 are laid on US business days by lsegdata's calendar and cut there; a C5-D2 break without a 24-month value
counts as not higher (counted and printed). NOT RUN: queue in PREB_BUILD_2026-11-27.md.
Addendum 1.1.0 (registered 2026-11-27, after the data entry "card inputs" and BEFORE the diag_preb 1.1.0 code; the
job has not run, so it is extended in place, as the coordinator asked; items above stand where not named here; nothing
chosen from a result):
A1. Scope: with the card inputs locked, every row of item 4 runs: C1-D1, C1-D2 and F0 for card 1 R1-R5; C2-D2 and F0
   for card 2 R1, R2; C3-D1, C3-D2 and F0 for card 3 R1-R4; C4-D1, C4-D2 and F0 for card 4 R1-R5; R1, C2-D1, C5-D1,
   C5-D2 and F0 card 5 R1 as before. The BLOCKED lines go. Trial rows (item 8): 12 (R1, C1-D1, C1-D2, C2-D1, C2-D2,
   C3-D1, C3-D2, C4-D1, C4-D2, C5-D1, C5-D2, F0). The job also pins card_inputs.py and checks work\free\
   gm_card_inputs.zip file by file against LOCK_CARD_v1 (id 6c154f7d...) before reading a value; every report prints
   each first-published input's flagged share (data entry item 2).
A2. Order and F0 basis: each card's own gates first (C3-D2 before C3-D1; C2-D2's version prune; C1-D2's leg drop), then
   F0 on the rule as it would enter B2 (versions left out, legs dropped and a dropped gate removed); a rule that a gate
   removes (C1-D1 watch condition, C3-D1 dropped, C4-D2 not registered, C5-D1 / C5-D2) still gets its F0 line, marked
   with that gate. Versions that only add a condition to a rule whose versions all hold the same sign per market
   (C2-D1's floor versions on card 1 R1, R2) or only scale a position by a positive factor (card 1 E3, card 4 C4-D1
   half size, card 5 50% cap) change neither sign nor held months and are not built. Card 3's sizing version is built
   (card 3 R1's versions hold opposite signs in one market, so magnitudes decide the averaged sign).
A3. Card 1 (SPEC_Card1 s3; closed here where the spec is silent): the dollar's L-month change is taken in TWEXMMTH when
   both ends have a TWEXMMTH value, else in DTWEXBGS (monthly mean); WTISPLC lag 1 compares t-1 with t-1-L; R2
   warning (c) compares the 12-month growth of M2SL at t with the same growth at t-24, each by data entry item 5;
   R3's spread percentiles are numpy linear over the expanding window from the first month both BAA and GS10 exist,
   the S&P level is the last ^GSPC daily close of the month, gold's level is the cumulated A1-panel cm_gold excess
   return (book.trend_signal's construction); R4's core inflation c(t) is CPILFESL's 12-month change by data entry
   item 5 at lag 1, state on while c > H and FEDFUNDS(t) < c(t); R4-B's basket = the spec's 16 panel commodities with
   a volatility at t, each 1/n of the leg. C1-D2 legs: R1, R2 the 2-year and 10-year legs; R3 the 10-year and S&P legs;
   R4 the 2-year and 10-year legs (both actions) and the S&P and basket legs (action B); R5 as item 5. Starts: R2 at
   GS2's first month; the others 1975-01.
A4. Card 2 (SPEC_Card2 s3, s13): R1 y(t) = GS10(t) - c(t) (c as A3); bar b = at or below the numpy-linear 33.3rd
   percentile of y from its first month to t, once 120 values exist; hedge gate = Pearson correlation of the 12 panel
   excess returns t-11..t of eq_us_spx and bd_us_10y above 0 (all 12 present). R2 d(t) = GS10(t) - GS10(t-12); on when
   d >= X and the ^GSPC 12-month % change (month-end closes) >= -10 x d; labour gate = UNRATE at t (lag 1, first
   published else latest) at or below the lowest of its 240 prior lagged values (all present). C2-D2 per version over
   decision months 1975-01..2010-11: on-months = condition months; left out if fewer than 24 on-months, fewer than 3
   episodes, or more than 2/3 of on-months in card 1 R4's state at H 4.5.
A5. Card 3 (SPEC_Card3 s3, s5, s13): R1 reads the named FRED / OECD series only, each currency from its own start (7.11:
   "R1 runs on FRED alone, each currency from its own start"; the LSEG entry names only a deposit-rate cross-check), all
   at lag 1; equal changes: shape A flat, shape B ties go to the first in the order US, JP, CH, EZ, GB, CA, SE; a leg's
   notional is fixed at the first month of a run with the same sign and role (A: the currency; B: long leg, short leg,
   basket) and kept for the run; the sizing version uses max(vol, expanding median of vol). R2's pair: 10-year notional
   = 2-year notional x D2 / D10 at that month's GS2, GS10 (par, semiannual), the pair's volatility from its own monthly
   return R2y(t) - h(t-1) R10y(t). R3 as the spec (PCEPILFE change at lag 2 by data entry item 5). C3-D2: design months
   1975-01..2010-12 with FEDFUNDS's 12-month range (t-11..t) below 0.50; C3-D1 then on the averaged rule (any version),
   market-months pooled over the rule's markets, sign equal to the book's pos.
A6. Card 4 (SPEC_Card4 s3, s13): R5 c(t) as A3; v1 on while c(t) < c(t-6), v2 also FEDFUNDS(t) <= FEDFUNDS(t-6) - 0.25;
   pair as A5; start GS2's first month. C4-D2 per R5 version: share of on-months with card 3 R2 on (either version), and
   share with Trend long bd_us_2y and short or flat bd_us_10y, Trend = the A2-final book's single Trend form (A2 FAIL:
   one version, so "the average of Trend's registered versions" is that form's score, book.trend_signal on the A1 panel),
   long = score > 0; gate: either share >= 0.80 in both versions. C4-D1: month-ends 1990-01..2010-06 (7.5 fix); up-month
   = ^GSPC month-end close above its close 6 months earlier; state on = the month's mean VIXCLS above that of 6 months
   earlier; outcome = the largest fall of ^GSPC daily closes from the last close of t to the last close of t + 6, over
   sqrt(252) x the standard deviation (ddof 1) of daily returns in months t-2..t; gate = median(state-on up-months) /
   median(other up-months) >= 1.25 over 1990-01..2010-06, 1990-01..1999-12 and 2000-01..2010-06; printed as the two
   counts and yes / no per window (the ratio over >= 60 months each).
Code 1.1.0 and cloud gates (2026-11-27; addendum 6146c2c before the code 049ab75; NOT RUN; no diagnostic statistic
computed in the cloud): tools/bbgq/lib/diag_preb.py 1.1.0 (sha256 5273944bcb9811ccba83510da3359996e28def8eb8b89a4408ed3efad855c64e),
job tools/bbgq/jobs/gm_diag_preb_v1.py extended in place (sha256 in PREB_BUILD_2026-11-27.md: pins card_inputs.py,
checks gm_card_inputs.zip against LOCK_CARD_v1 before any value), tests/diag_preb_smoke.py 71 checks. Gates: k = 0
reproduction 24 of 24, difference 0 (tools/bbgq/results/engine_repro_cloud_2026-11-27h_gm-2.2.1.txt); truncation PASS
at all 8 cut dates, 21 k = 0 and 37 feature stages (results/engine_trunc_cloud_2026-11-27h_gm-2.2.1.txt); run_tests ALL
TESTS PASSED (results/run_tests_gm_2026-11-27j_gm-2.2.1.txt). Closed while coding (no rule change): a market the panel
lacks holds no position; card 3 R1's euro rate is the DE-then-EZ series of C2-D1 and the dollar's is TB3MS; card 3's
reported lines (spec s13) are not printed in this version (they are no gate). Trial rows: 12.

## Core book v1 (registered 2026-11-27, BEFORE the Core book v1 code and run): TESTING_PROTOCOL 7.6 step 6
Registered run entry (no rule, weight, threshold, gate, cost or market change; no gm/ code change; no statistic of S1-S4,
of any Incubator test or of Core book v1 has been computed on real data, cloud or PC). The A1 panel holds Bloomberg
values and exists only on the PC, so every statistic is computed by one PC job (tools/bbgq/jobs/gm_core_v1.py, library
tools/bbgq/lib/core_v1.py). The builder has read the A2 and diagnostics reports (repo files the job pins); no choice
below reads them: each is closed from the registered text, with the reason given.
1. The registered text. 7.6 step 6: "Core book v1. For each Core part of an existing pod (7.2: Trend; Carry currencies
   v2 + energy; Value equities), on the final Batch A design run (k = 1, 1975-01 to 2010-12): S1 placebo passes (7.7 T3);
   S2 its net mean return at twice the costs is above 0; S3 tail test 5 on the Core book with and without the part
   (both rescaled as 7.7 T4); S4 an independent rebuild from the spec alone matches within 15% (WORKFLOW 4.5: design net
   Sharpe and annualised mean each within 15% relative). Departure from WORKFLOW s5 ("Decisive, all four"): test 1 is not
   decisive for these parts. Reported, not decisive: leave-one-out alpha of the part on the other Core parts with its
   bootstrap p. ... A part that passes S1-S4, with a free live source for every input, is Core. Core book v1 = the Core
   parts at equal risk as defined in 7.4 E9, 10% target, the engine's caps. Every other part of an existing pod
   (Economic trend; Carry currencies v1 and bonds; Value bonds and currencies) and any Core part that fails S1-S4 takes
   the Incubator rule (7.7) against Core book v1: pass = Incubator (shadow), fail = Shelved. If no Core part passes, Core
   book v1 is empty: B tests read alpha against a zero book (the pod's own mean), and there is no holdout run (BASE
   continues, labelled "no Core book")." 7.7 T3, T4, Window, Held size, Incubator (quoted in gm-2.1.0 item 5 and 7.7);
   test 5 (section 2): "Maximum drawdown and worst month on the window (both books at the same vol target) | max fall not
   worse by more than 2 points and worst month not worse by more than 1 point"; 7.8 item 1: family "book" = "a change
   that could alter the book: A2, A3, Core book v1".
2. Book and data (closed by "A3: empty" item 2): the final Batch A book = the A2-final book A1_INCUMBENT
   gm-2.0.4-candidate-x1 (config 77374d7bef), engine gm-2.2.1, A1 PANEL ID e7f98d4439fccf91f3451bc4b9e78079e3bc2cc2452931363b28520460b6cb43,
   design months 1975-01..2010-12, every loader cut at 2010-12-31 and the holding cut of 7.3 item 5. Timing k = 1 for
   every decisive line (gm.execution.run_k1); k = 0 and the one-month delay are reported for Core book v1 only (7.3
   item 1).
3. Parts and masks (7.2 item 5; 7.4 E9; gm-2.1.0 closed item 5; gm/config.py CORE_PARTS and SHADOW_PARTS, unchanged):
   Core candidates (three parts): trend = [(trend, *, *)]; carry = [(carry, FX, 2), (carry, CM, 1), (carry, CM, 2)];
   value = [(value, EQ, *)]. Shadow parts (three): econ = [(econ, *, *)]; carry shadow = [(carry, FX, 1), (carry, FI,
   *)]; value shadow = [(value, FI, *), (value, FX, *)]. Readings: Carry's CM leg is energy only (the four EIA markets
   cm_wti, cm_natgas, cm_heatoil, cm_gasoline are the only CM markets with a carry value on free data, SPEC_Carry s3 and
   s4; E13 adjusts natgas and gasoline); Carry is always split into v1 (sign) and v2 (rank) for masks (gm-2.1.0 closed
   item 5), so "currencies v2" exists without a grid; the A2-final book has no grid (A2 FAIL), so Trend and Value hold
   one version each and "Value equities (both versions)" is version 1 as held (v2's equity leg is "equities as v1",
   SPEC_Value s3). "Carry currencies v2 + energy" is ONE part, as 7.6 step 6 lists it and CORE_PARTS holds it (n = 3);
   its two legs alone are reported only.
4. Closed here (simplest reading of the registered text; none from results):
   a. A part's test return ("Held size", 7.7: "its block at the book's 10% target with the engine's caps") = the part
      alone as a one-part equal-risk book of E9 (its masked blocks, block scalers, part scaler, the 10% book scaler, the
      per-market and gross caps, costs at cost multiple 1), at k = 1. Window (7.7): the months 1975-01..2010-12 with a
      net return of the part alone; fewer than 120 = "insufficient data": not tested, not Core, status "insufficient
      data" (7.7 Window: "not tested").
   b. S1 = 7.7 T3 on the part alone: 1,000 date maps (gm.stats.placebo_perms: the window's months in 12-month blocks
      from its first month, the last part-block kept, numpy default_rng(20261101)); for each, the score / rank arrays of
      all markets moved jointly inside the window (gm.book.placebo_net_fn, runner gm.execution.run_k1 with the NYSE
      days, the part's mask; only the part's components enter a one-part book), re-sized with each month's own
      volatility, scalers and caps, same costs; Sharpe on the window; p = share of placebos with net Sharpe >= the
      part's (gm.stats.placebo_runs); pass p < 0.05.
   c. S2 = the mean monthly net return of the part alone at cost multiple 2 over its window > 0 (point estimate).
   d. S3: "the Core book" = the candidate Core book of item 3 (all three Core candidates at equal risk, E9, n = 3);
      "without the part" = the equal-risk E9 book of the other two candidates (n = 2). All three parts are judged on S1-S4
      side by side against this one candidate book, not in sequence (no order exists in the registered text, and an
      order would be a choice). "Both rescaled as 7.7 T4": each book as run, because its own book scaler is T4's
      convention (10% target, trailing 36-month realised volatility, lagged one month; gm-2.1.0 closed item 6: "the
      Core book is taken as run (its own book scaler is the same convention)"). Test 5 = gm.stats.tail_test(without,
      with) on their common months in 1975-01..2010-12: the book with the part has a maximum fall not worse by more
      than 2 points and a worst month not worse by more than 1 point.
   e. S4: the rebuild is tools/bbgq/lib/rebuild_s4.py, written by a separate agent from the specs and the registered
      texts alone, to the interface docs/research/batches/S4_INTERFACE.md (written before this entry; the builder of
      core_v1 does not read that file). Decisive keys trend, carry, value_eq (the three parts of item 3); carry_fx_v2 and
      carry_energy reported. Engine figure = item 4a's series. Statistic over 1975-01..2010-12, each series over its
      own months with a net return (A2's convention): annualised net Sharpe (gm.stats.sharpe) and annualised mean (12 x
      monthly mean). Pass = |rebuild - engine| / |engine| <= 0.15 for both. The rebuild's sha256 is registered in the
      job (REBUILD_SHA) by a dated line under this entry before the job is queued; the job STOPs (before any statistic)
      if the file is missing or differs, if its source imports gm, gm_engine, a1_panel, a2_batch, diag_a2, core_v1,
      bbgdata or bbg_panel, if it raises, or if an output breaks the interface's section 3 (a broken rebuild is not a
      failed part).
   f. "A free live source for every input": live runs read the free panel (A1 rule, 7.6 step 2: a Bloomberg series
      "may only extend a market's free history backwards ... (live runs on the free source, rule 7)"), so the inputs a
      live run of a part reads are the free panel's. Check per part: every market the part alone holds at the last
      design decision (month-end 2010-12, non-zero position) has, on the FREE panel, a monthly return at 2010-12 and,
      for carry and value, its measure at 2010-12 (free C or V); and the A1 extension-only check passed (already a STOP
      condition). Pass = no held market lacks one. The markets and any missing input are printed (ids only). Recorded
      with it, not changing the check: the GB and euro-area 3-month rates end 2026-01 and are carried 12 months; 7.10
      item 2 requires a registered free replacement before 2027-01 (else fx_gbp, fx_eur, bd_gb_10y, st_gb_5y, bd_de_10y,
      st_de_2y lose their excess return live); the specs' rule 7 lines (SPEC_Trend s8, SPEC_Carry s8, SPEC_Value s8:
      "every input has a free live source") govern sources (7.1 item 2); MSCI country indexes are a manual free
      download (gm/panel.py:203).
   g. Verdict of a Core candidate: Core = S1, S2, S3 and S4 pass and item 4f passes. Core book v1 = the parts that are
      Core, at equal risk (E9 with n = their number), 10% target, the engine's caps and costs, k = 1; if all three are
      Core it is the candidate book of item 4d.
   h. Leave-one-out alpha (reported, never decisive): gm.stats.alpha_boot(part alone, the item 4d "without" book) on
      their common window months (10,000 resamples, mean block 6, seed 20261101): alpha x 12 (%/yr) and p.
   i. Incubator rule (7.7: "not Core, and alpha of T1 above 0 at single costs (point estimate), T3 and T4 pass") for
      the three shadow parts and for every Core candidate that is not Core, against Core book v1: T1 = alpha_boot(part
      alone, Core book v1 net) on common window months, alpha > 0 decides, raw p reported (outside any Holm count: no
      Holm here); T3 = item 4b (a failed Core candidate reuses its S1 result); T4 = gm.stats.t4_tail(Core book v1 net,
      part net) (Core book v1 + the part at lambda 0.5, rescaled to 10%, against Core book v1 alone). Pass = Incubator
      (shadow), fail = Shelved; fewer than 120 common months = "insufficient data". T2 (alpha at twice the costs) is
      printed, not decisive (it is not in the Incubator rule). F0 does not apply (parts, not rule layers).
   j. Empty branch: no Core candidate is Core -> "CORE BOOK V1 EMPTY". Then T1 reads alpha against a zero book (the
      part's own mean; gm.stats.alpha_boot with a zero series: beta 0, alpha = mean), as the registered text says for B
      tests; T4 is printed "not applicable" and does not block (test 5 compares two books "at the same vol target", and a
      zero book has no volatility to rescale; the registered text names only the alpha adaptation); the job prints that
      there is no holdout run and that BASE continues labelled "no Core book".
   k. Reported for Core book v1 (7.7 reported list, the lines that apply to a book; 7.3 item 2; 7.8): at k = 1, k = 0
      and the one-month delay, cost multiples 1 and 2: months, net Sharpe, mean, volatility, maximum drawdown, skew,
      Lo-adjusted Sharpe for 1975-2010, 1975-89 and 1990-2010; the k = 1 flagged share 1975-2010 and by year; P4 with
      the S&P 500 alone (M1 outcome), 1978-01..2010-12; the selection inflation of 7.8 item 2 from the book / pod rows
      of the trial log as shipped (printed beside, never subtracted); the tuned-knob counts of 7.8 item 4 as
      registered. Each part alone (Core candidates and shadow parts): net Sharpe and mean, 1975-2010 and eras.
5. Printing: Sharpe ratios, means, alphas, p-values, shares and drawdowns only over at least 60 months; a group with
   fewer months is printed as its count and sign; worst-month levels are not printed (test 5 is printed as its two
   margins in points and pass / fail; maximum drawdown levels are printed); gates as PASS / FAIL; ids and counts.
6. Trial count (7.8 item 1): ONE gm/trials.csv row, family "book", for Core book v1 at k = 1 on the A1 panel (config
   hash = cfg_hash of A1_INCUMBENT with the key "core_parts" = the sorted list of Core parts; sr_9010, t_9010,
   maxdd_9010, sr_7589, turnover as gm/trials.py; note: panel id, LOCK_v2, engine, parent 77374d7bef, the verdict of
   every part), written by the coordinator from the job's TRIAL ROW line. If Core book v1 is empty the row has no
   Sharpe columns (as a diag row). S1-S4, the placebos, the Incubator tests and the part-alone runs are report lines of
   this one trial, not trials (none can be adopted into the book except through this row).
7. Job (tools/bbgq/jobs/gm_core_v1.py on the PC; the gm_diag_v1 pattern): STOP before any Bloomberg value is read
   unless the gm .py files equal engine_ref.json's code block; sha256(lib\engine_ref.json) = cebd4932e8643f14c541258abe68809a4e3c119f0c384beaa3d656b44c955e39;
   config.ENGINE_VERSION = gm-2.2.1 and the config hashes BASE f1d682c384, CANDIDATE 438a092b53, A1_INCUMBENT
   77374d7bef, A2_CHALLENGER 1faa343535; core_v1.py, diag_a2.py, a2_batch.py, a1_panel.py, gm_engine.py, bbg_panel.py,
   bbgdata.py have the sha256 registered in the job, and rebuild_s4.py REBUILD_SHA (item 4e); the book / pod rows of
   lib\gm\trials.csv have the digest 676b7b0f157cc6cc3e14f4e82754d5ad4c80bc61e3e9e5aa7c26596c6403e5ed, N = 40;
   local\results\gm_a2_v1.txt gives the A2 facts as in "Diagnostics after A2" item 9; local\results\gm_diag_v1.txt has
   "DIAG JOB DONE" and a DIAG SUMMARY line with "D1: candidate half blocked", "D2: closed" and "D3: closed" (A3 empty);
   the store's lock id is LOCK_v2; the free inputs match the reference; the free arm matches engine_ref.json. Then it
   rebuilds the A1 panel, asserts extension-only and the registered id, compares the rebuild with
   work\a1\a1_panel_e7f98d4439fc.pkl when present (STOP on any difference) and writes nothing to work\ (beyond the free
   inputs manifest refresh noted at the diagnostics, W3). It runs and validates the rebuild before any statistic is
   printed, then checks the A2-final book as run against the A2 report (diag_a2.as_run, STOP on a difference), then
   prints S1-S4, the live-source check, the verdicts, Core book v1, the Incubator tests, the reported lines and the
   TRIAL ROW.
8. Cloud: no statistic of S1-S4, of an Incubator test or of Core book v1 is computed on the free or the A1 panel. Cloud
   work = the code, mock-store and synthetic-panel tests (tests/core_v1_smoke.py in tests/run_tests.py, with the stub
   rebuild tests/data/rebuild_s4_stub.py), the engine gates (k = 0 reproduction 24 of 24, truncation 8 of 8; gm/ is
   unchanged, so engine_ref.json is unchanged) and identity plumbing on the free panel that prints differences, ids and
   PASS / FAIL only (the Core and shadow masks partition each pod's components; the identity date map reproduces the
   part-alone series exactly; the interface inputs build with the documented keys and shapes).
9. After the run (an "outcomes" paragraph under this entry): the verdict of each part; Core book v1's parts and config
   hash (the B1 / B2 test-1 book, 7.1 F9, and the book of step 11); each shadow part's status (Incubator or Shelved).
   Nothing in the specs, the register or 7.x changes from this run except those status words.

Code and cloud gates (2026-11-27; entry 28f14a6 before the code 9aa8527; no statistic of S1-S4, of an Incubator test or
of Core book v1 computed in the cloud): tools/bbgq/lib/core_v1.py 1.0.0 (sha256
817380e8e9e7ed49f4f2a4ec2495b3e4ec154c186104dd99b07eab06738f1423), PC job tools/bbgq/jobs/gm_core_v1.py (sha256 in
docs/research/batches/CORE_V1_BUILD_2026-11-27.md; it changes once REBUILD_SHA is set), stub tests/data/rebuild_s4_stub.py
(tests only), tests/core_v1_smoke.py (70 checks, in tests/run_tests.py), cloud script tools/bbgq/core_plumbing.py. gm/
unchanged, so engine_ref.json is unchanged. Gates: k = 0 reproduction 24 of 24, difference 0
(tools/bbgq/results/engine_repro_cloud_2026-11-27f_gm-2.2.1.txt); truncation PASS at all 8 cut dates, 21 k = 0 and 37
feature stages (results/engine_trunc_cloud_2026-11-27f_gm-2.2.1.txt); run_tests ALL TESTS PASSED
(results/run_tests_gm_2026-11-27g_gm-2.2.1.txt); free-panel identities PASS (results/core_plumbing_cloud_2026-11-27.txt:
masks partition each pod, identity date map = each part alone, interface inputs as documented, live check runs).
Closed while coding (no rule change): the job runs the rebuild on the interface inputs (A1 panel, cut at 2010-12-31)
and validates it before the as-run check and any statistic; the S3 "without" books and the candidate Core book are run
once and reused by S3 and the leave-one-out alpha; a candidate with fewer than 120 window months is "insufficient data"
and is not sent to the Incubator rule (7.7 Window: "not tested").
S4 rebuild: written by the separate agent and committed by it (1204233, rebuild_s4 1.0.0, sha256
3febdce707c9706d43d189c64f0700705a3b5b1bd2ee912e8fe430be1dac8ebf as committed; the core_v1 builder neither read nor
edited it). REBUILD_SHA is NOT set: item 4e's dated registration line is the coordinator's after accepting the
rebuild. NOT RUN: queue in docs/research/batches/CORE_V1_BUILD_2026-11-27.md.

Corrections after the independent check (CHECK_CORE, APPROVED WITH CORRECTIONS, 2026-11-27; registered BEFORE the
core_v1-1.1.0 code and BEFORE any run; the items above are not rewritten; none chosen from a result; the coordinator's
decision on M2 is option A):
- M2 (S4 scope = the full spec, option A). TESTING_PROTOCOL 7.6 step 6 asks for "an independent rebuild from the spec
  alone" (WORKFLOW 4.5: "of each Core pod from its written spec alone"). Interface v1 handed the rebuild the engine's
  carry measure C, value measure V and volatility estimate, which narrowed the registered test. That narrowing is
  WITHDRAWN (so no 7.12 sub-section is needed): S4 also rebuilds the carry measure (SPEC_Carry s3 steps 2-3 and the X1 /
  E13 text), the value measure (SPEC_Value s3 item 1 with E4) and the hybrid volatility model (SPEC_Trend s3 step 4)
  from the spec text. The rebuild receives RAW month-end and daily inputs only, before any engine signal or volatility
  code: docs/research/batches/S4_INTERFACE.md version 2 (v1 kept in the file's git history, commit 28f14a6). Item 4e is
  amended accordingly; its decisive keys, statistic and 15% band are unchanged. The job checks, before any statistic,
  that the raw inputs reproduce the engine's measures exactly (carry of the currencies and energy markets, the equity
  dividend yields; a packaging check, max abs difference and missing pattern, nothing else printed) and STOPs if not,
  or if A1 admitted a dividend-yield extension (interface v2 has no form for one; none was admitted).
- M1 (the rank weights must not be clipped): fixed by the separate rebuild agent in rebuild_s4 (1.0.1 or later), from
  the spec text, together with interface v2. The core_v1 builder does not touch rebuild_s4.py.
- M3: REBUILD_SHA is set only after the corrected rebuild (M1 and interface v2) is accepted, by the dated item-4e line
  under this entry in the same commit; rebuild_s4 1.0.0 (3febdce7...) is not registered.
- Item 4e REGISTERED (2026-11-27, coordinator, before the Core book v1 run): rebuild_s4 1.1.0 (commit 4a5d5b6, written
  by the separate rebuild agent from the specs alone; readings N1-N25 in docs/research/batches/S4_REBUILD_NOTES.md)
  ACCEPTED after the independent re-check (CHECK_CORE 'Re-check': APPROVED; synthetic self-test 85/85; core_plumbing
  --rebuild PASS, no statistic). REBUILD_SHA = 4f191fea1dfac0ae4f67ddd3974c92dd79969f6fa5414ef107de70d5315ed17d.
  Re-check note R1: two readings in S4_INTERFACE v2 were written by the core_v1 builder with sight of the engine,
  like N2: "the 12-month sums need all 12 months (US too)" and "the model uses D's values as given" (bond and note
  price returns as the daily vol input); S4 does not test these two points independently (effect tiny).
- S1 / N2 gap rule, a dated clarification of SPEC_Trend s3 (2026-11-27, mirrored there as an amendment): "Gap rule (N2),
  clarifying "gaps as 0 where data exist" and step 2's "no value if lvl(t-h) is missing": the level lvl of a market
  exists at every month-end from its first month with a monthly excess return onward, including later months without
  a return (interior gaps); a gap month adds a return of 0, so lvl(t) = lvl(t-1) there, and the score at and after a gap
  month is computed from that level like any other month; lvl is missing only before the market's first return." It
  states the rule as the engine's registered design implements it (for the record only: gm/book.py:71 trend_signal,
  `lvl = (1 + X.fillna(0)).cumprod().where(X.notna().cummax())`, and book.py:165 _trend_version, sign shape). It was
  written with sight of the engine code, so S4 does not test this one point independently. No engine behaviour
  changes.
- C1: every Core candidate that is not Core goes to the Incubator rule, including one with "insufficient data"; such a
  part prints "insufficient data" there (its common months with Core book v1 are also fewer than 120), the same outcome
  as before, now as item 4i writes it.
- C2: the k = 1 flagged share by year (item 4k) is coverage metadata, not a return statistic; it is printed by year as
  item 4k registers, outside item 5's 60-month rule (which governs return statistics).
- C4: the job sets sys.dont_write_bytecode, so importing the lib modules writes no __pycache__ (nothing is written to
  lib\ or work\).
- Not applied here (can wait, CHECK_CORE): C3 (the import scan reads import statements; the sha pin covers the rest),
  C5 (agent and run ids go into the notes of later steps), C6 (the rebuild notes' check count, the rebuild agent's
  file), C7 (Core book v1's two test-5 margins against the candidate book, for the outcomes paragraph), C8 (stated).
Code 1.1.0 (2026-11-27, commit 57cc241; corrections e18bc33 before it): tools/bbgq/lib/core_v1.py 1.1.0 (sha256
ee01320501fd1ec1f1fcc8b89dca91000e7644f728ed67cbb9e4ac674b04549e; replaces 1.0.0 817380e8...), job gm_core_v1.py
(sha256 80ff15f25f2ce1a6de33057208b66dc608b03a9cd0feb2f9df23e9a20127220d with REBUILD_SHA unset), stub 0.0.2,
tests/core_v1_smoke.py 75 checks. Gates: run_tests ALL TESTS PASSED (tools/bbgq/results/run_tests_gm_2026-11-27h_gm-2.2.1.txt);
free-panel identities PASS (results/core_plumbing_cloud_2026-11-27b.txt: the raw inputs reproduce the engine's
currency carry, energy carry before E13 and equity value with E4 exactly, difference 0); gm/ unchanged, so the k = 0
reproduction (24 of 24) and truncation (8 of 8) results stand. Closed while coding (no rule change): the raw check
compares on the design grid with tolerance 1e-12 and the missing pattern; the A1 block-2 contract extension is applied
to the raw EIA contracts by the same steps as a1_panel.build (its result is what the raw check compares). NOT RUN.

CORE BOOK V1 RUN (2026-11-27, PC job gm_core_v1, 4476 s; report tools/bbgq/results/gm_core_v1.txt; every pin, raw check,
A1 panel id and as-run check PASS): CORE BOOK V1 EMPTY. Per candidate (k = 1, 1975-2010, net):
- trend: S1 PASS (placebo share 0.000), S2 PASS (10.37 %/yr at 2x costs), S3 FAIL (with vs without: max fall 12.1 pts
  BETTER, -21.2% vs -33.3%, but worst month 1.2 pts worse > the 1-pt margin), S4 PASS (rebuild Sharpe 1.21 vs 1.19,
  relative 0.016 / 0.005, corr 0.99), live PASS -> NOT CORE.
- carry (FX v2 + energy): S1 PASS, S2 PASS (5.19), S3 FAIL (max fall 4.0 pts worse, worst month 3.3 pts worse), S4 PASS
  (0.008 / 0.012, corr 1.00), live PASS -> NOT CORE.
- value (EQ): S1 FAIL (placebo share 0.462), S2 FAIL (-0.13), S3 FAIL, S4 FAIL (relative 2.36: both Sharpes ~0, 0.01 vs
  -0.01; corr 1.00), live PASS -> NOT CORE.
The S3 'with' book is the equal-risk book of all three candidates (closed choice: judged together, the checker found it
faithful to the text, which gives no order); value, which fails S1/S2/S4, is in every 'with' book. This reading was
registered before the run and is not changed after it.
Consequences, as registered (7.6 step 6): B tests read alpha against a zero book (the pod's own mean); there is NO
holdout run; BASE continues, labelled "no Core book". Incubator rule (against the empty book; T4 not applicable):
INCUBATOR trend, carry, econ, carry_shadow (FX v1 + bonds), value_shadow (bonds + currencies, T1 raw p 0.26 -> PASS by the
registered 'alpha > 0' reading); SHELVED value (EQ; T3 placebo share 0.462). S4 note: the independent rebuild matched
the engine within 2% on trend and carry and within 5% on the reported legs, so the existing book's rules are
reproducible from the specs. Trial row (book, core_parts []) appended.
## A3: empty (registered 2026-11-27, after the diagnostics run and BEFORE Core book v1): TESTING_PROTOCOL 7.6 step 5
Record entry (no rule, weight, threshold, cost, market or code change; nothing is run; no trial row).
1. The registered text. 7.6 step 5: "Batch A3, items opened by diagnostics only (charter s5; register B9): breadth (D1,
   alternative commodities and T10 strip markets that qualify), no-trade buffer (D2), faster book scaler (D3). Each is
   tested alone against the A2-final book by 7.7 H1-H4 with its own target decisive (H4). An item whose preconditions
   (locked history with the 2011+ seal; a registered live source for T09/T10 markets) are not met when A3 starts is not
   run; it may be registered with B1 or B2 before that batch starts, else it waits for the live path (WORKFLOW s6)."
   REGISTRATION_3.4 part (c) item 5: "Before A3, one entry per opened item: the D2 buffer, the D3 scaler, the D1 breadth
   markets (with E12 for any T10 strip market)".
2. What the diagnostics opened (the "DIAGNOSTICS RUN" paragraph of "Diagnostics after A2", job gm_diag_v1, report
   tools/bbgq/results/gm_diag_v1.txt): D2 closed -> no no-trade buffer item; D3 closed -> no faster book scaler item; D1
   candidate half not run (blocked, that entry's item 6a) -> no breadth item. So no A3 item is opened and no part (c)
   item 5 entry exists. A3 is empty: nothing is tested, no Holm or hygiene slot is used, no gm/trials.csv row is written,
   and the A2-final book (A1_INCUMBENT gm-2.0.4-candidate-x1, config 77374d7bef, engine gm-2.2.1, A1 panel e7f98d44...)
   is the final Batch A book that 7.6 step 6 reads ("on the final Batch A design run").
3. The D1 breadth item is not run because its preconditions are unmet when A3 starts (7.6 step 5, quoted above):
   T09 (alternative commodities): no registered data entry names a T09 series, E1 keeps the Bloomberg alternative
   columns off, and no T09 market has a registered live source; T10 (strip markets other than the dollar): 7.5 D1's
   extension admits a strip "only with eight contracts locked and a registered live source", LSEG lock v5 has
   eight-contract strips only for ED (the dollar, excluded) and FEI (euro, 1999-2010), and LSEG LIVE_START is not set
   (data entry "LSEG registered as a source for history" item 6), so no T10 market has a registered live source.
4. How it may come back (the registered text, nothing added): "it may be registered with B1 or B2 before that batch
   starts, else it waits for the live path (WORKFLOW s6)". Read exactly, a breadth market can return only if, before
   B1 (or B2) starts, in this order: (a) its preconditions are met (T09: a data entry naming the series, a locked history
   with the 2011+ seal and a registered live source; T10: eight contracts locked with the seal, a registered live source,
   i.e. LSEG LIVE_START set by its own data entry, and E12 coded for that market under its own entry); (b) D1's candidate
   half runs for it as registered in "Diagnostics after A2" item 6a and 7.5 D1 (zero slot, design months, gate "both
   averaged shares < 1/2, >= 120 months before 2011, costed at 8 bp"), logged as a "diag" row; (c) a market that passes
   the gate gets its own entry (REGISTRATION_3.4 part (c) item 5) registered with B1 or B2 before that batch starts,
   tested by 7.6 step 5's rule (alone against the A2-final book, 7.7 H1-H4, H4 = breadth target "lower first-factor share
   of Trend's variance", baseline 0.20 from the D1 structural half). Because Trend is a Core part, that entry must also
   say, before its run, how an admitted market enters Core book v1. If (a)-(c) are not all done before B2 starts, the
   item waits for the live path. Nothing here opens, schedules or prefers any of this; B1 / B2 do not wait for it.
5. Trial count: none (no run). The book / pod rows of gm/trials.csv are unchanged (digest 676b7b0f..., 40 rows).

## Diagnostics after A2 (registered 2026-11-27, BEFORE the diagnostics code and run): TESTING_PROTOCOL 7.6 step 4, 7.5 order item 2
Registered run entry (no rule, weight, threshold, gate, cost or market changes; no gm/ code change; no statistic of any
diagnostic below has been computed on real data, cloud or PC). The A1 panel holds Bloomberg values and exists only on
the PC, so every diagnostic is computed by one PC job (tools/bbgq/jobs/gm_diag_v1.py, library tools/bbgq/lib/diag_a2.py).
1. The registered text. 7.6 step 4: "The diagnostic pass of 7.5 order item 2 on the A2-final book." 7.5 order item 2:
   "After A2: D1 (its candidate half only where a locked history exists), D2, D3, D4, D5, D6, X2, M1, S1." 7.5: "No
   diagnostic adopts anything or uses a Holm slot (charter s5). Each is logged as a design-data run (7.8)"; "Every
   diagnostic reads positions, signals or its registered outcome only; none reads a sealed day after its fix." Gates:
   the 7.5 table (rows D1-D6, X2, M1, S1, with the 3.4 fixes: D1 extension to T10, D3 state months end at 2009-12, D4 one
   shared bad-state set and one crisis table, D5 overlap printed, X2 90% interval reported, M1 gate kept, S1 five-state
   table, Fung-Hsieh part only with a locked factor file), CHARTER_1.2 s5 (computations), THESIS_1.3_xs s5 (X2),
   THESIS_1.3_method s7 (M1). A2 entry item 5: the specs' falsifier lines other than the splits A2 reported "are read on
   the A2-final book ... with the 7.5 order item 2 diagnostics, family 'diag'; X2 and D4 supply their inputs".
2. Book (closed by the A2 RUN paragraph: "A2-final book = the incumbent, unchanged"): A1_INCUMBENT
   gm-2.0.4-candidate-x1, config 77374d7bef, old code path, no grid, CANDIDATE shares 45 / 15 / 25 / 15, engine
   gm-2.2.1, A1 PANEL ID e7f98d4439fccf91f3451bc4b9e78079e3bc2cc2452931363b28520460b6cb43, design months 1975-01..2010-12,
   every loader cut at 2010-12-31 and the holding cut of 7.3 item 5. Timing: every return a diagnostic reads is the
   k = 1 return (7.3 item 1, decisive timing; gm.execution.run_k1); positions are book.run's (identical at k = 0 and
   k = 1). Only D5, whose subject is timing, also prints the k = 0 path beside.
3. In this pass: D1 structural half, D2, D3, D4, D5, D6, X2, M1, S1 (equity-state part) and the falsifier lines of
   SPEC_Trend, SPEC_Carry, SPEC_Value and SPEC_Economic_trend s10. Not in this pass: X1 (done, order item 1); R1,
   C1-D1, C1-D2, C2-D1, C2-D2, C3-D1, C3-D2, C4-D1, C4-D2, C5-D1, C5-D2, F0 (order item 3: after Core book v1, before B2;
   their registered cuts stay: R1 month-ends to 2010-11, C4-D1 last state month 2010-06, C5-D2 breaks to 2008-12);
   blocked parts in item 6.
4. Closed here (the simplest reading of the registered text; none chosen from results):
   D1 a. Trend profit and loss of market m in month t at equal risk = clip(score(t-1), -1, 1) x 0.40 / vol(t-1) x R1(t)
      (book.py trend_signal and the line w x 0.40 / vol), score = book.trend_signal of the A2-final config (sign,
      1 / 3 / 12 months), vol = gm.vol.estimate (hybrid), R1 = the k = 1 return; before costs, class division and scalers.
      b. Markets: the book's Trend class-block markets except cm_aqr_ew (7.1 item 3: "61 markets ... plus cm_aqr_ew"),
      i.e. the 61 distinct markets.
      c. Windows: every trailing 60-month window ending 1979-12 .. 2010-12 (373 windows inside 1975-01..2010-12); in each,
      the markets with a P&L in all 60 months and non-zero variance; a window needs at least 3 markets.
      d. Principal components = eigen-decomposition of the window's correlation matrix (equal risk: each stream
      standardised); first-factor share = largest eigenvalue / number of markets; loading = eigenvector x
      sqrt(eigenvalue) (the market's correlation with the factor), signed so the loadings sum to >= 0; class mean
      loading = mean over the class's markets in the window. Each averaged over windows with equal weight (a class over
      the windows in which it has a market).
      e. Pod Sharpe over mean market Sharpe: per window, the Sharpe of the Trend pod alone (one-part equal-risk book of
      gm-2.1.0 E9, mask (trend, *, *), k = 1) BEFORE costs (its gross return, since the market streams are before costs)
      over the mean of the window's market Sharpe ratios; windows where that mean is <= 0 or the pod lacks a month are
      skipped and counted; averaged over the rest.
      f. This half has no gate (the registered gate is on candidates); reported only. Candidate half: item 6.
   D2 a. The book's positions are rebuilt from their intermediates (unscaled family-class positions p, volatility vol,
      block scalers k, book scaler s, per-market caps, gross cap; book.py run / _finish, old path); the rebuild must
      equal book.run's "pos" (max absolute difference <= 1e-12, printed; if not, D2 prints FAIL and is not gated).
      b. "Volatilities and all scalers held at last month's values": the position at t is built from the scores at t
      (q = p x vol = w x 0.40 / n, the volatility-free part of each family-class term) with vol(t-1), k(t-1) and s(t-1);
      the per-market cap, a function of vol, from vol(t-1); the gross cap is applied to the result (caps are rules,
      not scalers). "Scores held" (reported): q(t-1) with vol(t), k(t), s(t) and the caps at t.
      c. Turnover = sum over markets of |position(t) - actual position(t-1)| (book.py turnover). Market-months in which a
      held input is missing (a market's first month with a volatility, a block scaler's warm-up, the book scaler's
      warm-up) are left out of both the numerator and the denominator.
      d. Gate statistic per era (trade months 1975-89, 1990-2010): 1 - (turnover with volatilities and scalers held) /
      (actual turnover), sums over the era's market-months. Reported: the scores-held share = (turnover with scores
      held) / (actual turnover).
      e. Cost drag per market (reported): mean yearly cost in basis points of capital (trades x one-way cost + roll
      charge + EM borrow, book.py at cost multiple 1) over the design months with a position.
   D3 a. r = the A2-final book's net k = 1 return; forward volatility FV(t) = standard deviation (ddof 1) of r over
      t+1..t+12 x sqrt(12), all 12 months present; state months from the first month with a state and an FV to 2009-12
      (7.5 fix), so no forward window passes 2010-12.
      b. Split (a), named state = trailing 12-month Pearson correlation of eq_us_spx and bd_us_10y monthly excess
      returns (A1 panel, months t-11..t, all 12 present) above 0 (the premise MT194-C16-3, "positive correlation which
      means ... you have more risk on", CHARTER_1.2_check table D3); other = the rest.
      c. Split (b), named state = mean over Trend's book markets with a score at t of |trend score| (book.py:72,
      score as D1) at or above its 90th percentile over the state months (numpy linear); other = the rest.
      d. Difference = mean FV in the named state - mean FV in the other state months. One-sided 90% lower bound =
      difference - 90th percentile of (bootstrap difference - difference); stationary bootstrap of the state months
      (state and FV resampled together, gm.stats._stationary_idx), mean block 12, 10,000 resamples, seed 20261101.
      Per split: open if difference >= 0.02 and bound > 0. Either split open -> the A3 faster book scaler item.
   D4 a. State at month-end t, S&P base: compounded excess-return index of eq_us_spx (A1 panel R); fall = 1 - index(t) /
      max(index over t-23..t); age = months since that maximum. Reported beside: the same states on the four-market
      average of protocol.py:200 (equal-weight mean of the monthly returns of eq_us_spx, eq_eu_stoxx50, eq_jp_nikkei,
      eq_gb_ftse that exist that month).
      b. Five states (also S1's "five-state equity table"): fall < 5% (no age split); 5% <= fall <= 15% with age <= 2
      ("young") and age > 2; fall > 15% with age <= 2 and age > 2.
      c. Return of a pod in month t = its family contribution at k = 1 before costs (held family position x k = 1
      return, a2_batch.contrib_fam, the A2 convention); mean per state; a state with fewer than 6 months is reported,
      not used (it cannot open a gate).
      d. Gates (S&P base): Trend's mean < 0 in the 5-15% young state and > 0 in the two > 15% states pooled -> SPEC_Trend
      s10 line "young, shallow equity fall"; Carry's summed contribution < 0 in both the "1998 LTCM" (1998-08..10) and
      the "2008 Lehman" (2008-09..12) windows -> SPEC_Carry s11 stop state "funding break".
      e. Crisis table (one shared bad-state set, 7.5 fix): bad months = the six config.py STRESS_WINDOWS that end by
      2010-12 together with the months whose eq_us_spx return is at or below its 20th percentile over 1975-01..2010-12
      (numpy linear); per pod and per Carry leg (FX, FI, CM): mean contribution in bad and in other months; per stress
      window and pod: the summed contribution.
      f. S1: the five-state table for all four pods on both bases; reported only.
   D5 a. Economic trend alone = one-part equal-risk book (E9, mask (econ, *, *)), net, at k = 1, with config key
      delay_months d = 0, 1, 3, 6, 12 (book.py _finish: positions earn 1 + d months after the decision); each Sharpe over
      its own months in 1975-01..2010-12 (A2's convention). Gate as written: Sharpe(d = 3) < 0.5 x Sharpe(d = 0) ->
      claim "slow reaction" (falsifier "no fading with delay"); else "a lasting macro state". Reported beside: the same
      five on the k = 0 path, and the caution of charter JP8 (at 3 months' delay 9 of the 12 months of the 12-month
      inputs overlap).
   D6 a. Per calendar year 1975-2010 and market of D1: the year's annualised Sharpe of D1's P&L and of the market's
      k = 1 return R1 (12 monthly values each, both with non-zero variance; else that market-year is out).
      b. Year level: y = mean over markets of the trend Sharpe, x = mean over markets of |market Sharpe|; years with at
      least 3 markets.
      c. Per era (1975-89, 1990-2010) least squares of y on x with intercept; Newey-West slope standard error, 2 lags,
      Bartlett weights (as gm.stats.nw_alpha_t); z = (slope 1990-2010 - slope 1975-89) / sqrt(se1^2 + se2^2) (eras
      independent). Gate: |z| < 2 -> "trend return per unit of market move, against the design slope" registered as
      Trend's breakdown check (SPEC_Trend s11); else dropped.
   X2 a. Legs EQ, FI, FX of Value as held in the A2-final book (fam_pos value; the book has version 1 only, so the
      averaged position is version 1's).
      b. Income of market m in month t = held position(t-1) x C_m(t-1) / 12, C = gm.signals.carry_values of the A1 panel,
      raw (equities: 12-month dividend yield at lag 0 minus the local 3-month rate; bonds: yield minus 3-month rate;
      currencies: rate gap to the dollar; E13 touches only natgas and gasoline); total = held position(t-1) x R1(t);
      price = total - income; over market-months with a position, a carry value and a return; the covered share of the
      leg's gross position is printed.
      c. Gate per leg: mean over the months with a covered position of the monthly summed price part <= 0 -> the
      register entry "paid by income" for that leg. Reported: mean income, price and total (%/yr) and the 90% interval of
      the price part's mean (stationary bootstrap of the monthly price part, mean block 6, 10,000 resamples, seed
      20261101, 5th and 95th percentiles).
   M1 a. r = the A2-final book's net k = 1 return; m1 = eq_us_spx, m2 = bd_us_10y monthly excess returns of the A1 panel
      (the P4 form of the A2 report); b(t) by least squares with intercept over all common months 1975-01..t-1, first
      value in month 37 (1978-01); one-market w = a2_batch.p4; two-market w = r - b1 m1 - b2 m2 with joint slopes.
      b. Sharpe of r, w (S&P) and w (both) over 1978-01..1989-12 and 1990-01..2010-12 (1978-2010 reported). Gate as
      written: in either era Sharpe(w both) <= Sharpe(w S&P) - 0.05 -> P4 uses both markets; else the S&P alone.
   Falsifier lines (A2 item 5; specs s10), each printed "holds" or "does not hold", reported only:
      Trend (1) pod alone net Sharpe <= 0 in both eras; (2) the two > 15% S&P states pooled: mean Trend contribution
      <= 0 (D4). Trend's carry / price split and class-average / relative split: already read on this same book by
      gm_a2_v1 (CARRYPRICE and SPLIT lines, incumbent); not recomputed.
      Carry (1) pod alone and each leg alone (one-part books with masks (carry, FX / FI / CM, *)) net Sharpe <= 0 in both
      eras; (2) FX: the leg's mean contribution in the bad months (D4 e) not below its mean in the other months; (3) CM:
      "high-carry positions" = the long side (version 1 is long where carry > 0, version 2 long the upper half of the
      rank): mean monthly contribution of the CM market-months held long <= 0; (4) FI standing long: on the FI leg alone,
      its mean net return <= the mean net return of a constant position in each bond equal to the leg's mean position in
      it over the months it holds it (same months; cost = the roll charge of the constant position, which never trades);
      (5) per leg (FX, FI, CM) the split of X2 b with income = carry / 12 at the prior month end: holds for a leg whose
      income part <= 0 or whose price part > its income part.
      Value (1) pod alone net Sharpe <= 0 in both eras; (2) = X2; (3) Value against Trend's relative part: read at A2
      (VALUE lines, incumbent); not recomputed.
      Economic trend (1) pod alone (= D5 d = 0) net Sharpe <= 0 in both eras; (3) theme split: the econ score E is the
      mean of the theme parts present (gm.signals.econ_versions, at least 2 present), so theme t's part of the held
      position = held Economic trend position x (theme score_t / number of themes present) / E, exact; market-months
      with E = 0 hold nothing; the check sum of parts = held position is printed; contribution per theme at k = 1 before
      costs by era; holds if the inflation part's mean <= 0 in both eras while the sum of the other three is > 0 in both.
      Theme scores = gm.signals.econ_theme_scores of the A1 panel, computed on the PC under the 2010-12-31 cut.
      Loss-event lines (P3): text only, nothing computed.
5. Printing (tools/bbgq/README.md export whitelist): Sharpe ratios, means, slopes, correlations and shares only over
   at least 60 months; a state, window or group with fewer months is printed with its month count and the sign of its
   value only, never the value; gates as pass / fail; counts and ids. Gates are evaluated on full precision on the PC.
6. Blocked (not run; listed by the job):
   a. D1 candidate half. T09 (alternative commodities): no registered data entry names a T09 series (the LSEG data
      entry item 4 lists the LSEG inputs it serves, and T09 is not among them; the A1 entry item 4 lists "every
      non-panel commodity" as not a candidate; E1 keeps the Bloomberg alternative columns off), and no T09 market has a
      registered live source. T10 (strip markets): LSEG lock v5 identifies eight-contract strips for ED (the dollar,
      which T10 excludes) and FEI (euro, 1999-2010) only; 7.5 D1's extension admits a strip "only with eight contracts
      locked and a registered live source", and LSEG LIVE_START is not set (LSEG data entry item 6), so no candidate can
      be admitted whatever its statistics; E12's return form is coded only for an admitted market. Consequence: this
      pass opens no A3 breadth item; 7.6 step 5 applies (an item whose preconditions are not met when A3 starts is not
      run; it may be registered with B1 or B2 before that batch starts, else it waits for the live path).
   b. S1's Fung-Hsieh part: the factor file is not obtained and locked (7.11).
7. What each outcome triggers (recorded after the run as an "outcomes" paragraph under this entry; nothing is adopted
   here): D2 open -> the A3 no-trade buffer item; D3 open (either split) -> the A3 faster book scaler item; each opened A3
   item gets its own entry before A3 (REGISTRATION_3.4 part (c) item 5); D4 -> the SPEC_Trend s10 line and the
   SPEC_Carry s11 stop state, or neither; D5 -> SPEC_Economic_trend's claim wording; D6 -> Trend's breakdown check line
   or none; X2 -> a "paid by income" entry per leg in the thesis register, or none; M1 -> P4's form in every later
   report; S1 and the falsifier lines are reported only. Spec and register edits are text changes made after the run,
   each citing this entry.
8. Trial count (7.8 item 1, family "diag"): one gm/trials.csv row per diagnostic run: D1, D2, D3, D4, S1, D5, D6, X2,
   M1 and one row for the falsifier lines = 10 rows, no Sharpe columns (as the X1 row), hash = config hash of the
   diagnostic's id, diag_a2 version, book hash and panel id; written by the coordinator from the job's TRIAL ROW
   lines. Family "diag" rows do not enter the selection-inflation count (book and pod rows only, 7.8 item 2).
9. Job (tools/bbgq/jobs/gm_diag_v1.py on the PC; the A2 pattern): STOP before any Bloomberg value is read unless the gm
   .py files equal engine_ref.json's code block; sha256(lib\engine_ref.json) = cebd4932e8643f14c541258abe68809a4e3c119f0c384beaa3d656b44c955e39;
   config.ENGINE_VERSION = gm-2.2.1 and the config hashes BASE f1d682c384, CANDIDATE 438a092b53, A1_INCUMBENT
   77374d7bef, A2_CHALLENGER 1faa343535; diag_a2.py, a2_batch.py, a1_panel.py, gm_engine.py, bbg_panel.py, bbgdata.py
   have the sha256 registered in the job; the book / pod rows of lib\gm\trials.csv (item 10, C7) have the registered
   digest; local\results\gm_a2_v1.txt has "A2 JOB DONE", the registered A1 PANEL ID PASS line, "A2 VERDICT FAIL" and
   "A2-final book = gm-2.0.4-candidate-x1 (77374d7bef)"; the store's lock id is LOCK_v2; the free inputs match the
   reference; the free arm matches engine_ref.json. Then it rebuilds the A1 panel, asserts extension-only and the
   registered id, compares the rebuild with work\a1\a1_panel_e7f98d4439fc.pkl when present (STOP on any difference) and
   writes nothing. As-run check against the A2 report before any diagnostic line (STOP on a difference): the A2-final
   book's net Sharpe 1975-2010 at k = 1 / k = 0 / one-month delay (3 decimals: 1.439 / 1.481 / 1.064, tolerance
   5e-4), each pod alone at k = 1 1975-2010 (2 decimals, tolerance 5e-3) and the P4 book / specific line (2 decimals),
   all read from gm_a2_v1.txt.
10. A2 check items applied here (CHECK_A2 "can wait"):
   C1 stale text corrected: tools/bbgq/README.md A2 lines (gm-2.2.1, a2_batch 1.1.0 for the run, hashes 77374d7bef /
      1faa343535, gm_a1_v2 named as the A1 rerun whose report gm_a2_v1 reads), tests/run_tests.py label, build_engine.py
      docstring.
   C4 a2_batch-1.1.1: the SPLIT check line prints PASS only if max(maxdiff_parts, maxdiff_held) < 1e-9 (a reported line;
      the verdict never read it). The A2 run used a2_batch-1.1.0 (sha256 87b24d8f558da20f6b5403d67006629b87edf45cea2d7e36cfa71605b014797b),
      whose line read maxdiff_parts alone; its printed maxdiff_held values (1.1e-15, 1.8e-15) pass the 1.1.1 criterion.
      gm_a2_v1.py keeps the 1.1.0 hash (it is the record of that run; a frozen copy tests/data/a2_batch_1.1.0.py serves
      its smoke test). Future jobs pin 1.1.1.
   C6 the diag job compares the rebuilt A1 panel with the saved file before anything else and never writes it; any
      later job that writes the A1 panel prints that comparison before writing.
   C2 pins of item 9 (engine_ref.json sha256, ENGINE_VERSION, the four config hashes).
   C7 the job pins only what it relies on in the trial log: the sha256 of the sorted lines "trial|family|hash|sr_9010"
      (raw CSV text) of the rows with family book or pod = 676b7b0f157cc6cc3e14f4e82754d5ad4c80bc61e3e9e5aa7c26596c6403e5ed,
      N = 40 (39 + the A2 challenger 1faa343535, 1.526); appended diag, data or fix rows do not change it. A2 item 4l is
      not amended (A2 has run).
11. Cloud: no diagnostic statistic is computed on the free or the A1 panel. Cloud work = the code, synthetic-data and
   mock-store tests (tests/diag_a2_smoke.py in tests/run_tests.py), the engine gates (k = 0 reproduction 24 of 24,
   truncation 8 of 8; gm/ is unchanged, so engine_ref.json is unchanged) and identity plumbing on the free panel that
   prints differences only (D2 rebuild = book.run positions; X2 income + price = total; theme parts sum to the held
   Economic trend position).

Code and cloud gates (2026-11-27; entry 3fdd3f9 before the code 3fd5d1b; no diagnostic statistic computed in the
cloud): tools/bbgq/lib/diag_a2.py 1.0.0 (sha256 b811df2b4a9ad009668856bb0a2fdd84cc03334aa5d4213e473e4165a99e9caa), PC job
tools/bbgq/jobs/gm_diag_v1.py (8d50d30e651bd702640ec3df90879ba6bf01641d016b9295afb7c5ce774c9c9a), a2_batch-1.1.1
(35339f673f351f43315ad3c7010ba733b6fb8990a6a41feb1ef20de324de58c6), cloud script tools/bbgq/diag_plumbing.py, test
tests/diag_a2_smoke.py (48 checks, in tests/run_tests.py). gm/ unchanged, so engine_ref.json is unchanged. Gates: k = 0
reproduction 24 of 24, difference 0 (tools/bbgq/results/engine_repro_cloud_2026-11-27e_gm-2.2.1.txt); truncation PASS at
all 8 cut dates, 21 k = 0 and 37 feature stages (results/engine_trunc_cloud_2026-11-27e_gm-2.2.1.txt); run_tests ALL
TESTS PASSED (results/run_tests_gm_2026-11-27e_gm-2.2.1.txt; a2_batch_smoke 44 checks with the frozen 1.1.0 copy for the
gm_a2_v1 job); free-panel identities PASS (results/diag_plumbing_cloud_2026-11-27.txt: D2 rebuild = book.run positions
difference 0; income + price = total 6.9e-18; theme parts = held Economic trend position 2.2e-16 and theme scores
reproduce E exactly; 62 Trend book markets, 61 without cm_aqr_ew). Closed while coding (no rule change): a D2 market-month
counts in the scores-held share under the same exclusion as in item 4 D2 c; the cost drag's per-market costs must sum to
the book's cost (printed check); the A2 facts parser reads only the incumbent's BOOK (costs x1, 1975-2010), POD and P4
lines of gm_a2_v1.txt. NOT RUN: queue in docs/research/batches/DIAG_A2_BUILD_2026-11-27.md.
Corrections after the independent check (CHECK_DIAG, APPROVED WITH CORRECTIONS; registered 2026-11-27 BEFORE the
diag_a2-1.0.1 code and BEFORE any run; the items above are not rewritten; none chosen from a result):
- M1 (item 5, printing): a D3 split whose named state or other group has fewer than 60 months prints its difference and
  its one-sided 90% bound as sign only (with the other group's mean printed, the difference would give the small
  group's mean); the gate still uses full precision.
- M2 (item 4 D2 a): if the rebuild fails, the gate line reads "D2 GATE | not gated (rebuild FAIL) | no A3 buffer item
  decision" and the recorded outcome is "not gated (rebuild FAIL)", never "closed".
- W1 (item 4 D2 d, closed while coding): the decision month 2010-12 is left out of D2's trade months (its trade is never
  made: holding cut of 7.3 item 5), so the eras are trade months 1975-01..1989-12 and 1990-01..2010-11.
- W2 (item 4 D2 e, closed while coding): the cost drag charges a decision month's cost in the next month, as book.py
  charges it against the net return (tc.shift(1)); means over the months 1975-01..2010-12 whose held position (the one
  decided the month before) is non-zero, so the 2010-12 decision's cost falls outside the window.
- W5: diag_a2.rebuild refuses a panel with alternative-commodity columns (their 30% cap depends on vol(t), which the
  held forms of item 4 D2 b assume away); E1 keeps them off today.
- W6: D3 prints how many bootstrap resamples held no state month or no other month (left out of the bound).
- W7 (item 4 M1 b): each M1 era's three Sharpe ratios are over the common months of the book return and both specific
  returns, and that count is printed.
Left for the outcomes paragraph (CHECK_DIAG can-wait, unchanged): W3 the job and the build note say "nothing is written
to work\", but the free-input check refreshes work\free\inputs_manifest.json (free-data metadata; nothing derived from
Bloomberg is written); W4 diag_plumbing computes the D2 shares on the free panel in memory without printing them; W8
the lib modules are imported before their sha256 check (the A2 pattern); W9 the trial-row config also hashes timing and
window; W10 D3 split (b) reads Trend's book markets including cm_aqr_ew, D1 excludes it.
Code 1.0.1 (2026-11-27, commit aa96955; corrections 5510e4e before it): tools/bbgq/lib/diag_a2.py 1.0.1 (sha256 3264a5381c13b124d2566d02f263e21905f4e901680c1af7c2134f0bd558be1b;
replaces 1.0.0 b811df2b... in the paragraph above), job tools/bbgq/jobs/gm_diag_v1.py (sha256 15b42eef009ee9e9181eae22791a558a87472f2bfd544a37704881267a890054;
replaces 8d50d30e...), a2_batch-1.1.1 unchanged; smoke cases for M1, M2, W1, W2, W5, W6, W7 (tests/diag_a2_smoke.py 55
checks). Gates rerun: run_tests ALL TESTS PASSED (tools/bbgq/results/run_tests_gm_2026-11-27f_gm-2.2.1.txt); free-panel
identities PASS (results/diag_plumbing_cloud_2026-11-27b.txt); gm/ unchanged, so the k = 0 reproduction (24 of 24) and
truncation (8 of 8) results of the paragraph above stand. NOT RUN: queue and hashes in
docs/research/batches/DIAG_A2_BUILD_2026-11-27.md.

DIAGNOSTICS RUN (2026-11-27, PC job gm_diag_v1, report tools/bbgq/results/gm_diag_v1.txt; every hash, pin, A1 panel id and
as-run check PASS; check CHECK_DIAG APPROVED WITH CORRECTIONS, must-fix applied in 1.0.1 before the run). OUTCOMES:
D2 CLOSED (non-signal share 0.038 / 0.031, rebuild exact) -> no-trade buffer item dropped. D3 CLOSED -> faster book
scaler item dropped. D4 CLOSED for Trend and Carry -> no SPEC_Trend line, no Carry stop state. D6 CLOSED (z -2.01). X2:
price part > 0 in EQ, FI, FX -> no "paid by income" entry. M1: P4 uses the S&P 500 alone. D5 YES: Economic trend
alone 0.53 at no delay, 0.23 at 3 months (< half) -> spec wording "slow reaction" (falsifier: no fading). D1
structural: first factor 0.20 of variance, Trend pod / mean market Sharpe 2.86 (baseline for H4). D1 candidate half
and S1 Fung-Hsieh part BLOCKED (entry item 6). Every falsifier line: does not hold (T1, T2, C1-C5, V1, E1, E3). So this
pass opens NO A3 item (7.6 step 5). Ten diag trial rows appended.
## gm-2.2.1 fix: cm_aqr_ew a Trend market in CM only (registered 2026-11-27, BEFORE the code change; found while building A2)
Registered fix of the existing engine (TESTING_PROTOCOL 7.4: a found defect gets a registered engine version, as C1-C4,
gm-1.2.2 and E1-E5). Found while coding A2 (gm/CHANGES.md "A2" item 13, commit d0ecdc7), BEFORE any A2 statistic was
computed anywhere (the A2 job has not run on the PC; the cloud computed positions only). Decision by the coordinator
(2026-11-27): fix now, before A2 runs; not a decision for the user.
1. Defect. gm/book.py family_positions (lines 127-128, old path) and family_positions_v (257-258, version path) build a
   class block's market list as
   `[k for k in X.columns if k.startswith(pre) and k in R and k != "cm_aqr_ew" or (k == "cm_aqr_ew" and f in ("trend",) and k in X.columns)]`.
   `and` binds tighter than `or`, so the second clause holds in EVERY class: cm_aqr_ew (AQR Commodities for the Long
   Run, equal weight, to 2000-12, gm/panel.py:550) is a Trend market in all four class blocks (EQ 19, FI 15, FX 14, CM
   17 columns on the free panel), where SPEC_Trend s4 lists it in CM only ("CM (16 + 1) ... cm_aqr_ew 1970-01 to
   2000-12") and book.py's own comment says "trend only". Its Trend position entered the EQ, FI and FX blocks too (and
   the count n of each), so the class blocks before 2001 were not what the spec says. No other family is affected (the
   second clause needs f = trend); gm/signals.py:476 has the same shape but its `or` is the intended reading.
2. Fix (the spec's reading, nothing else): cm_aqr_ew is in a class block only when the class is CM and the family is
   Trend: `(k.startswith(pre) and k in R and k != "cm_aqr_ew") or (k == "cm_aqr_ew" and c == "CM" and f == "trend" and
   k in X.columns)`, in both places. No other rule, weight, threshold, cost, market or date changes.
3. Scope: every config alike (BASE, CANDIDATE, A1_INCUMBENT, A2_CHALLENGER, and every parts / Core / shadow / tranche /
   placebo path, which all read these two functions). Version names (the convention of every number-changing fix,
   gm-1.2.2 and gm-1.2.3): engine gm-2.2.1 (config.ENGINE_VERSION); BASE gm-1.2.3 -> gm-1.2.4 (gm/run.py VERSION too);
   CANDIDATE gm-2.0.3-candidate -> gm-2.0.4-candidate; A1_INCUMBENT -> gm-2.0.4-candidate-x1; A2_CHALLENGER ->
   gm-2.2.1-a2-challenger. The config hashes change with the names (each printed in the result paragraph); the
   hashes 465b5ecd4f / a5b83bdf45 of the A2 entry are superseded by them (the A2 entry's rules are unchanged).
4. Consequences, stated before the code:
   a. Design numbers move for BASE and CANDIDATE (Trend before 2001). Gate (7.4 "Gate for E1-E5", a fix): truncation
      test at 8 dates; tests pass; design statistics before / after reported once (BASE and CANDIDATE, 1975-2010 and
      1990-2010, net Sharpe, mean, volatility, worst drawdown; free data, cloud, as for E4); one gm/trials.csv row per
      config, family "fix". New reference tools/bbgq/engine_ref.json made by tools/bbgq/engine_ref.py (the old file kept
      as engine_ref_gm-2.2.0.json); then the k = 0 reproduction 24 of 24 against the NEW reference.
   b. A1 is rerun as PC job tools/bbgq/jobs/gm_a1_v2.py: identical to gm_a1_v1 apart from its name and the registered
      sha256 of the engine files (gm code checked against the new engine_ref.json, whose free arm is the new
      reference). Same A1 rule, same LOCK_v2, same candidates and a1_panel-1.1.0 (unchanged): the A1 panel id is
      computed from the a1_panel version, LOCK_v2, the free-inputs digest, the blocks and the admitted list only, so it
      stays e7f98d4439fccf91f3451bc4b9e78079e3bc2cc2452931363b28520460b6cb43 unless the admission changes (the
      admission reads the free panel return, the EIA contracts and the dividend yields, none of which this fix touches;
      if gm_a1_v2 printed another id, that is a finding and A2 stops). The A1 report numbers change (the book changes);
      gm_a1_v2's TRIAL ROW (family "data") is logged as the A1 row of gm-2.2.1, the gm_a1_v1 row stays as history.
   c. A2 (amending its entry item 7, registered here before the job change): the incumbent's as-run values are no
      longer the hard-coded A1-report numbers; gm_a2_v1 reads them from local\results\gm_a1_v2.txt, the three lines
      "all blocks (A1 panel) | k1 / k0 / d1 | 1975-2010 | ..." (net Sharpe, 3 decimals), and STOPS if that file is
      missing, has no "A1 JOB DONE", lacks one of the three lines, or names another A1 PANEL ID than the registered
      one. The trial log hash of A2 item 4l changes (the two "fix" rows; book / pod rows unchanged, so N 39 and the
      inflation 0.26 stay). Queue: gm_repro_v7 -> gm_a1_v2 -> gm_a2_v1.
5. Test (registered with the fix): a smoke check that every class block's columns carry that class's prefix, except
   cm_aqr_ew, which may appear only in the CM block of Trend (both code paths, BASE and the A2 challenger).
6. Live paper ledger: untouched (workflow disabled); the next live run restates under gm-1.2.4. Holdout not run.
Code (2026-11-27, commit 0dadb20; entry afdcadc before it): gm/book.py both class lists as item 2; gm/config.py names and
ENGINE_VERSION gm-2.2.1; gm/run.py VERSION gm-1.2.4; tests/gm_class_smoke.py (in tests/run_tests.py; it FAILS on the old
code: cm_aqr_ew in trend/EQ, FI, FX, and passes on the fix). Config hashes: BASE f1d682c384 (was 7651ea6ebc), CANDIDATE
438a092b53 (a9466df18b), A1_INCUMBENT 77374d7bef (465b5ecd4f), A2_CHALLENGER 1faa343535 (a5b83bdf45).
Result (2026-11-27, free data, design months only; inputs = the repo cache, the same 239 files as the gm-2.2.0
reference): new reference tools/bbgq/engine_ref.json made by tools/bbgq/engine_ref.py at gm commit 0dadb20 (sha256
cebd4932e8643f14c541258abe68809a4e3c119f0c384beaa3d656b44c955e39; old file kept as engine_ref_gm-2.2.0.json); k = 0
reproduction against it 24 of 24, difference 0 (tools/bbgq/results/engine_repro_cloud_2026-11-27d_gm-2.2.1.txt);
truncation test PASS at all 8 cut dates, 21 k = 0 stages and 37 feature stages, 0 failing end-to-end or alone
(results/engine_trunc_cloud_2026-11-27d_gm-2.2.1.txt); tests/run_tests.py ALL TESTS PASSED
(results/run_tests_gm_2026-11-27d_gm-2.2.1.txt); bbgq_engine_smoke OK; a1_panel, gm_bloomberg, gm_x1, gm_feature, gm_seal,
gm_class and a2_batch smokes passed. On the free panel the Trend class blocks now hold EQ 18, FI 14, FX 13, CM 17 columns
(positions only). Design statistics, net of costs, before (gm-2.2.0 reference) -> after (gm-2.2.1), reported once:
| Config | Period | Sharpe | Mean %/yr | Vol %/yr | Worst drawdown % |
|---|---|---|---|---|---|
| BASE gm-1.2.3 -> gm-1.2.4 | 1975-2010 | 1.226 -> 1.220 | 12.46 -> 12.65 | 10.17 -> 10.37 | -21.0 -> -22.4 |
| BASE gm-1.2.3 -> gm-1.2.4 | 1990-2010 | 1.469 -> 1.474 | 14.47 -> 14.52 | 9.86 -> 9.85 | -12.3 -> -12.4 |
| CANDIDATE gm-2.0.3 -> gm-2.0.4 | 1975-2010 | 1.461 -> 1.464 | 14.38 -> 14.97 | 9.84 -> 10.22 | -16.8 -> -17.6 |
| CANDIDATE gm-2.0.3 -> gm-2.0.4 | 1990-2010 | 1.620 -> 1.631 | 16.38 -> 16.65 | 10.11 -> 10.21 | -16.8 -> -17.6 |
Trial log: two rows, family "fix" (fix gm-2.2.1 gm-1.2.4, fix gm-2.2.1 gm-2.0.4-candidate; one per config, not a
selection trial); book / pod rows unchanged (N 39, selection inflation 0.26). gm/trials.csv sha256 now
2b80e2f9b255b05e839f6a6edcafa844aa67c161423d4966d99a141e4e178a36 (a2_batch TRIALS_SHA). Jobs: tools/bbgq/jobs/gm_a1_v2.py
(= gm_a1_v1 + name + REF_SHA check of the new engine_ref.json); gm_a2_v1.py reads the as-run values from
local\results\gm_a1_v2.txt (a2_batch-1.1.0 as_run_from_a1; the hard-coded AS_RUN is removed). No A1 or A2 statistic was
computed in the cloud. The PC is not yet redeployed (queue: docs/research/batches/A2_BUILD_2026-11-27.md).

## A2: Batch A2, version grids, hygiene H1-H4 (registered 2026-11-27, BEFORE the A2 code and the A2 run): TESTING_PROTOCOL 7.6 step 3, 7.7
Registered batch entry (no rule, weight, threshold or cost changes; no gm/ code changes; no statistic of the A2
challenger, of any grid version or of any A2 report line has been computed on real data, cloud or PC). Nothing has to
be built between A1 and A2: REGISTRATION_3.4 part (c) entries 1-4 are done (gm-1.2.3, gm-2.1.0, data entry A1 with its
panel id, X1 outcome / E13); entry 5 is due before A3, entry 6 before B1 / B2; the E3 metadata listing ran 2026-11-24;
the diagnostics of 7.5 order item 2 run AFTER A2 on the A2-final book (step 4). The A1 panel holds Bloomberg values, so
every A2 statistic is computed by one PC job (tools/bbgq/jobs/gm_a2_v1.py, library tools/bbgq/lib/a2_batch.py).
1. The registered text, word for word. 7.6 step 3: "Batch A2, grids (hygiene, 7.7 H1-H4). Challenger = CANDIDATE with
   Trend 16 versions, Economic trend 2, Carry 2, Value 2 (version counts: SPEC_Trend s6, SPEC_Economic_trend s6,
   SPEC_Carry s6, SPEC_Value s6; Carry's two versions reproduce today's half-and-half exactly, so A2 tests averaging,
   not a new Carry rule). Incumbent = CANDIDATE gm-2.0.3, k = 1, A1 data. Value version 2's bond leg is already seen
   (batch-1 V1, protocol_batch1.md; SPEC_Value s12): it is counted as a seen leg (7.8). Reported with A2: Sharpe by
   version, by tranche (weekly check), by class and era; Trend's split into class-average and relative parts (register
   B12, T12); Trend's carry and price parts; Value next to Trend. If A2 fails, the incumbent stays without averaging; no
   cell of a grid is picked." 7.7: "Hygiene items (A2, A3): H1 one-sided 95% lower bound of dSR (paired stationary
   bootstrap of section 2, pooled design window) > -0.10; H2 dSR at twice the costs, reported; H3 tail test 5 between
   the two books; H4 (A3 only) ... Pass = H1, H3 and, in A3, H4. No Holm across hygiene items (a margin test, not an
   adoption claim; error at the margin measured 0.06-0.09, power s3.7)." 7.1 F9: "A2 and A3: incumbent = CANDIDATE
   gm-2.0.3 (7.4) as run at k = 1 on the A1 data; the 0.23 is printed beside the result, not subtracted." 7.1 F2: eras
   "Reported, not decisive, for pods, rule layers and hygiene items"; F4: "'improves its own target' decisive only for
   items with a written target (A3), reported for A1 and A2"; F5: "Hygiene: dSR at twice the costs reported". 7.3 item 1:
   "Decisive timing is k = 1 ... Reported beside it: k = 0 ... and the one-period (one-month) delay of WORKFLOW s5."
2. Arms (closed by the A1 and X1 entries, which say every later run uses A1_INCUMBENT and the A1 panel): incumbent =
   A1_INCUMBENT (gm-2.0.3-candidate-x1, config hash 465b5ecd4f = CANDIDATE a9466df18b + E13) as run, on the old code path
   (no grid); challenger = A2_CHALLENGER (gm-2.2.0-a2-challenger, config hash a5b83bdf45 = A1_INCUMBENT + config key
   "grid" = Trend 16 (config.TREND_GRID), Economic trend tanh / sign, Carry dir / cs, Value 1 / 2), version path of
   gm-2.1.0 E7. Both on the A1 panel, A1 PANEL ID e7f98d4439fccf91f3451bc4b9e78079e3bc2cc2452931363b28520460b6cb43
   (rebuilt on the PC by a1_panel-1.1.0 from LOCK_v2 and the free inputs, its id checked; the saved panel file, if
   present, must equal the rebuild), engine gm-2.2.0, CANDIDATE shares 45 / 15 / 25 / 15 (7.1 F8), the same costs,
   design months only (every loader cut at 2010-12-31, holding cut of 7.3 item 5).
3. Decisive (the verdict): at k = 1, on the pooled design window = the months 1975-01 .. 2010-12 in which both books
   have a net return (gm.stats.noninferiority, gm-2.1.0 E10): H1 = the one-sided 95% lower bound of dSR (challenger
   minus incumbent net Sharpe) from gm.stats.paired_sr_test (10,000 resamples, mean block 6, seed 20261101) > -0.10
   (identical books pass); H3 = gm.stats.tail_test (challenger's maximum fall not worse by more than 2 points, worst
   month not worse by more than 1 point). PASS = H1 and H3: the A2-final book is the A2 challenger (grids averaged).
   FAIL: the A2-final book is A1_INCUMBENT, without averaging; no cell of any grid is picked. H2 (dSR with every cost
   doubled, both books at cost multiple 2) is printed, not decisive. H4 does not apply (A2 has no written target).
   No Holm. The selection inflation of 7.8 item 2 is printed beside, never subtracted.
4. Reported (not decisive), the 7.6 step 3 list plus the lines 7.3, 7.7 and 7.8 require on every book result:
   a. each book at k = 1, k = 0 and the one-month delay (config key delay_months = 1 on the k = 0 path, as the A1
      report), each at single and double costs: months, net Sharpe, mean, volatility, maximum drawdown, skew, Lo-adjusted
      Sharpe (gm.stats.lo_sharpe), for 1975-2010, 1975-89 and 1990-2010; H1 / H2 / H3 at k = 0 and the one-month delay
      beside (reported); per era (1975-89, 1990-2010) dSR with its lower bound and standard error (7.1 F2);
   b. by version: each challenger version of each pod as a complete pod alone = a one-part equal-risk book of gm-2.1.0
      E9 (parts = {version: [(pod, "*", v)]}: class blocks, part scaler, 10% book scaler, caps, costs) at k = 1;
      net Sharpe 1975-2010 and by era; share of versions with net Sharpe > 0 (1975-2010) per pod and over all 22; each
      pod alone (mask (pod, "*", "*")) for both books, and the incumbent's Carry versions 1 and 2;
   c. by class and era: family x class contributions at k = 1 (held family positions x k = 1 returns, before costs:
      a1_panel.contrib_k1, the A1 report's convention), family totals and class totals, both books, 1975-2010 and eras;
   d. by tranche (weekly check, 7.3 item 6, 1990-01 .. 2010-12 only): gm.execution.tranches for both books; net Sharpe
      of each tranche j = 0..3 and of the tranche form; dSR of the tranche form with its lower bound (reported);
      coverage = share of gross position held in market-months flagged for lack of daily data, per tranche;
   e. Trend's split (SPEC_Trend s14, closed there): per version and class, the score w (clipped to [-1, 1]) is split
      into its class mean over the markets of the class with a position that month and w minus that mean; each part x
      0.40 / vol_v / n_v / V gives a class-average and a relative position; summed over versions; each is scaled to the
      book by the same factor that turns Trend's unscaled class position into its held family position (block scaler x
      family share x book scaler x cap shrink, book.run), so the two parts add up to Trend's contribution exactly;
      return = held part x k = 1 return, before costs; Sharpe 1975-2010, by era and by class; both books;
   f. Trend's carry and price parts (SPEC_Trend s10): carry part = held Trend position x carry / 12 at the prior month
      end (the Carry pod's carry values, gm.signals.carry_values of the A1 panel, bonds and currencies only); price part =
      Trend's bond and currency contribution minus the carry part; k = 1, before costs; Sharpe and mean, 1975-2010 and
      eras; both books;
   g. Value next to Trend (SPEC_Value s14 "A2 reads version 2 with Trend's old and new grids"): correlation of Value's
      and Trend's contributions (k = 1, before costs), Newey-West (6 lags) t of Value's intercept on Trend's
      contribution (gm.stats.nw_alpha_t), correlation of Value with Trend's relative part (SPEC_Value s10, 1.3b (iii));
      for incumbent Value v1 / incumbent Trend, challenger Value v1 + v2 / incumbent Trend (old grid) and challenger
      Value / challenger Trend (new grid); 1975-2010;
   h. Economic trend next to Trend (SPEC_Trend s14, SPEC_Economic_trend s14 "A2 report"): Pearson correlation of the two
      pods' held equity positions, pooled over equity market-months 1975-2010 where both are non-zero; both books;
   i. k = 1 flagged share (7.3 item 2): share of gross position in flagged market-months, 1975-2010 and by year, both
      books;
   j. P4 (7.7): w = r - b x m, m = the A1 panel's eq_us_spx monthly excess return, b by least squares with intercept
      over all months from 1975-01 to the month before, first value in month 37 (1978-01); annualised Sharpe of w beside
      r, 1978-01 .. 2010-12, both books at k = 1. S&P alone: M1 (which may add the US 10-year) runs after A2 (7.5 order
      item 2), so until it has run the line uses its "S&P alone" form;
   k. fragility (7.7): the largest loss of the pooled k = 1 dSR when one calendar year (its months dropped from both
      return series), one market or one asset class (removed from the A1 panel, both books re-run) is removed, and
      which; flagged when one calendar year gives more than 40% of the summed monthly net-return difference (challenger
      minus incumbent), if that sum is positive;
   l. trial count and selection inflation (7.8 item 2): rows of gm/trials.csv with family "book" or "pod" and a 1990-2010
      Sharpe, by the stats_audit method of gm/audit.py s2: N rows, z = (1 - g) x Phi^-1(1 - 1/N) + g x Phi^-1(1 - 1/(N e)),
      g = 0.5772156649, inflation = z x sd(ddof 1). On the trial log shipped with this entry (gm/trials.csv sha256
      dd10359e3c1cec49640f3df054df8c2da28baf81ec887d2db258c72b2ea81198; 39 book rows, 0 pod rows): N = 39, mean 1.481,
      sd 0.118, z 2.18, inflation 0.26 (computed now from the logged rows only; 32 variants gave 0.23 in stats_audit,
      which left out the batch rows); the job recomputes it from the shipped file and stops if the file differs;
   m. tuned-knob counts (7.8 item 4), as registered: Trend 4, Economic trend 3, Carry 3, Value 3 + 1 seen leg (Value
      version 2's bond leg, 7.8 item 3), book level 3 (pod share vector, no risk scaler, no scenario limit).
5. Not reported at A2 (closed here, with the reason): untouched markets (the held-back markets are sealed and not in
   the A1 panel; WORKFLOW 0.4 "untouched markets named and sealed"); the specs' falsifier lines other than the splits
   named in 7.6 step 3 (they are read on the A2-final book, which exists only after the A2 verdict, with the 7.5 order
   item 2 diagnostics, family "diag"; X2 and D4 supply their inputs); the combined-book lambda line (pods only); the
   martingale test and the deflated Sharpe (dropped, 7.1). Worst-month levels are not printed (export whitelist names
   drawdowns, not single months): H3 is printed as its two margins (challenger minus incumbent, points) and pass / fail.
6. Trial count (7.8 item 1, family "book": "a change that could alter the book: A2"): one gm/trials.csv row for the
   challenger at k = 1 on the A1 panel (columns as gm/trials.py; note: panel id, LOCK_v2, engine, parent A1_INCUMBENT
   465b5ecd4f, verdict and the H1 bound), written by the coordinator from the job's TRIAL ROW line. The incumbent's run
   is the A1 row already logged (same config hash, same panel): not logged again. The by-version, pod-alone, tranche
   and fragility runs are report lines of this one trial, not trials (none can be adopted).
7. Job (tools/bbgq/jobs/gm_a2_v1.py on the PC; the A1 pattern): stops (prints STOP, reads no Bloomberg value) unless
   the gm .py files equal engine_ref.json's code block; a2_batch.py, a1_panel.py, gm_engine.py, bbg_panel.py and
   bbgdata.py have the sha256 registered in the job; lib\gm\trials.csv has the sha256 of item 4l; the store's lock id is
   LOCK_v2 d85a46cb2853646b24796f294f3ccab1d1507188c402e978fd59f5196ea41fc9; the free inputs match the reference; the
   free arm matches engine_ref.json (E, C, V signal sums 1e-6, market months exact). Then it rebuilds the A1 panel
   (a1_panel evaluate + build, all blocks), asserts extension-only and the registered A1 PANEL ID, compares the rebuild
   with work\a1\a1_panel_e7f98d4439fc.pkl when that file exists (stop on any difference), and checks the incumbent as
   run against the A1 report (net Sharpe 1975-2010 at 3 decimals: k = 1 1.439, k = 0 1.480, one-month delay 1.052;
   stop on a difference). Prints summary statistics over at least 60 months only, pass / fail, ids; exception text as
   type and code frames, numbers scrubbed. Writes nothing to work\ (A2 saves no panel).
8. Cloud: no A2 statistic is computed on the free or the A1 panel. Cloud work = the code, synthetic-data tests (mock
   stores, synthetic panels with known answers: tests/a2_batch_smoke.py in tests/run_tests.py), the gates of the engine
   (k = 0 reproduction 24 of 24, truncation 8 of 8; gm/ is unchanged, so engine_ref.json is unchanged), and
   positions-only plumbing on free data (the Trend split parts add up to the Trend held positions; no return).
Amended by "gm-2.2.1 fix" (registered above, before its code): engine gm-2.2.1, arm hashes 77374d7bef (incumbent) and
1faa343535 (challenger) replace 465b5ecd4f / a5b83bdf45; item 7's as-run values are read from gm_a1_v2's report
(gm-2.2.1 item 4c), not the gm_a1_v1 numbers; item 4l's trial-log hash is 2b80e2f9...e178a36 (N 39 and 0.26
unchanged); item 13 is fixed by gm-2.2.1. Every other item stands.
Closed while coding (2026-11-27, before any A2 run; simplest reading, none from results):
9. Carry / price (item 4f): both parts and the total are taken over the bond and currency market-months that have a
   held Trend position and a carry value, so total = carry + price exactly; the covered share of Trend's FX + FI gross
   position is printed. The incumbent's Carry versions and pod-alone runs use the version path (gm-2.1.0 E9), which
   reproduces the old path's Carry (gm-2.1.0 result item 2).
10. Weekly coverage (item 4d): tranche 0's flag is the k = 1 flag (no daily price on a first trading day), tranches 1-3
    the no-daily-data flag of gm.execution.tranches.
11. Fragility (item 4k): markets tried = every column of the A1 panel (cm_aqr_ew included); a class = the columns with
    its prefix (gm.signals.CLASSES); the loss is of the dSR point estimate (no bootstrap); "largest loss" = full dSR
    minus the smallest dSR after a removal.
12. As-run check (item 7): equality at 3 decimals of the three registered values (tolerance 5e-4).
13. Code fact found while coding, NOT changed (any change needs its own registered fix entry and a new reference):
    book.py family_positions (lines 127-128) and the version path family_positions_v (257-258) build a class's market
    list as `k.startswith(pre) and k in R and k != "cm_aqr_ew" or (k == "cm_aqr_ew" and f in ("trend",) ...)`; by
    Python precedence the second clause holds in every class, so cm_aqr_ew (to 2000-12) sits in all four Trend class
    blocks (EQ 19, FI 15, FX 14, CM 17 columns on the free panel), not only in CM as SPEC_Trend s4 lists it ("CM (16 +
    1)"). It is the same in both A2 arms, in BASE and CANDIDATE and in engine_ref.json; a2_batch's Trend split
    replicates it (its parts add to the held position). Not fixed here: A2 is built on the registered engine gm-2.2.0.

A2 RUN (2026-11-27, PC job gm_a2_v1, report tools/bbgq/results/gm_a2_v1.txt; every hash, lock, A1 panel id and
as-run check PASS; check CHECK_A2 APPROVED WITH CORRECTIONS, none before the run): A2 VERDICT FAIL. Decisive (k = 1,
1975-2010, 432 months): dSR -0.104, lb95 -0.165 (H1 margin -0.10: FAIL), H3 PASS (max fall -0.1 pt, worst month -0.1 pt).
Incumbent gm-2.0.4-candidate-x1 (77374d7bef) net SR 1.439 vs challenger gm-2.2.1-a2-challenger (1faa343535) 1.335. Same
sign at k = 0 (-0.113) and at the one-month delay (-0.079, H3 FAIL there); both eras negative (1975-89 -0.140, 1990-2010
-0.071). 21 of 22 versions alone have net SR > 0 (Value v2 does not). A2-final book = the incumbent, unchanged: no
averaging, no grid cell picked (7.6 step 3). Fragility (C5 of the check): market and class removals keep the signals as
built, so Economic trend themes that read a removed market still see it. Trial rows appended after the run: the A1
rerun gm_a1_v2 (its job's 'when' is the run time; the earlier A1 row's 'when' 2026-11-27 23:55 was a PC-local stamp
written later than its commit, kept as written, C3) and the A2 challenger.

## data: A1 data rule (registered 2026-11-27, BEFORE the A1 code and the A1 run): TESTING_PROTOCOL 7.6 step 2, 7.4 E15
Entry 3 of docs/research/registration/REGISTRATION_3.4.md part (c): "Data entry A1 (before the A1 run): the
extension-only rule of 7.6 step 2 with LOCK_v2 id d85a46cb2853646b24796f294f3ccab1d1507188c402e978fd59f5196ea41fc9; the
A1 panel id recorded after the run." Registered data entry (no rule change; no statistic of any A1 path has been
computed; Bloomberg values stay on the user's PC, rule 7).
1. The rule, word for word (TESTING_PROTOCOL 7.6 step 2): "Rule for each Bloomberg series (LOCK_v2, lock id
   d85a46cb2853646b24796f294f3ccab1d1507188c402e978fd59f5196ea41fc9): it may only extend a market's free history
   backwards, never replace an overlapping free month (live runs on the free source, rule 7); it must be the same
   instrument (same index family or contract root) with status ok in LOCK_v2 (not a copy, not cut); and its monthly
   returns must correlate at least 0.95 with the free series over the overlap months up to 2010-12 (just below the
   lowest agreement our own bond returns showed against CRSP, 0.965, gm/CHANGES.md gm-2.0). A series failing a
   condition is not used and is listed. The A1 panel (its id recorded) is the panel of every later run, B2 included
   (CHECK_3.2_C s4 item 1); cm_aqr_ew is not a stand-in for card 1 R4-B's basket."
2. Lock: LOCK_v2, lock id d85a46cb2853646b24796f294f3ccab1d1507188c402e978fd59f5196ea41fc9 (docs/research/bbg/LOCK_v2.json;
   store on the PC in local\work\bbg, read only through tools/bbgq/lib/bbgdata.py 1.2.0 and bbg_panel 1.0.0). The A1
   job stops before reading any value if the store's lock id differs.
3. The A1 panel id is recorded after the run (appended to this entry and, at the freeze, in the 7.9 item 1 record).
4. Candidate series (registered here, from the specs' own A1 lines and the engine's Bloomberg map with E1 off and E2
   applied; nothing chosen from data):
   Block 1, commodity returns (SPEC_Trend s16 "Bloomberg only as the registered A1 data swap of the same series";
   gm-1.2.3 closed here item 1: "The Bloomberg excess-return indexes of the 16 panel commodities ... are the A1 data
   swap (7.6 A1, E15)"): for each of the 16 panel commodities, the excess-return indexes of gm/bloomberg.py COMMOD_ER
   (S&P GSCI, then BCOM), sheet Returns, field PX_LAST. Instrument: the index rolls the futures root whose front
   contract or ETF the free series holds (same contract root). Market history extended: the panel return R.
   Block 2, energy carry inputs (SPEC_Carry s3 "Allowed at A1: Bloomberg or LSEG contracts 1 and 2 of the same four
   markets as a data swap of the same formula"): the generic contracts 1 and 2 of CL, NG, HO, XB (gm/bloomberg.py
   CURVE_ROOT; cm_wti, cm_natgas, cm_heatoil, cm_gasoline), field PX_LAST, any sheet of LOCK_v2 (the primary series
   id). Instrument: same contract root and position as the EIA NYMEX contract 1 / 2. History extended: the EIA
   contract-n month-end price, used by the Carry signal 12 x (F1 / F2 - 1) only (the panel return keeps its free
   sources; block 1 is the return route).
   Block 3, Value's equity dividend yield (SPEC_Value s3 "Allowed at A1: the same 12-month dividend yield from Bloomberg
   or LSEG as a data swap"; 7.4 E2: "every remaining mapping (a local index to the MSCI index of the same country) is
   used only if the A1 rule of 7.6 step 2 admits the series"): EQY_DVD_YLD_12M of the gm/bloomberg.py EQ_INDEX MSCI
   index of the market's country, sheet EquityValuation. History extended: the market's 12-month dividend yield
   before the lag of E4 (both Value versions read it).
   Report line R (TESTING_PROTOCOL 7.1 F7: "bond futures against yield-built returns = an A1 report line"): the 1st
   generic bond futures of sheet BondFutures (TU, FV, TY, US, DU, RX, G, JB, CN, YM, XM) against the yield-built bond
   returns of the same market: overlap months and correlation of monthly returns up to 2010-12. Reported only, never
   used (a bond future is not the same instrument as the par bond the free series prices).
   Not candidates: no registered spec reads them and the engine has no Bloomberg route for them (a new route would be
   its own data entry): EquityTR total-return indexes, generic government yields and 3-month rates, FX spot and
   forwards (U07-T4's block 4 would replace overlapping months), first-release economics (U07-T4 block 3; overlapping
   months cannot be replaced, and register T37 dropped first-release growth), every non-panel commodity (E1 keeps
   the alternative commodities off), curve points beyond contract 2 (E1 curve carry off), valuation fields other than
   the dividend yield (E1 composite off).
5. How each condition is applied (closed here, the simplest reading):
   a. "status ok in LOCK_v2 (not a copy, not cut)": the (ticker, field) has a primary series id in the lock's catalog
      (status ok; a copy block has no series id), its file name has no _CUT tag, and it is not a held-back (untouched)
      market (invisible in the design panel). The catalog status of a failing row is listed.
   b. "same instrument": by the candidate map of item 4 (contract root and position; index family; for block 3 the
      same-country MSCI index named by E2).
   c. "only extend a market's free history backwards, never replace an overlapping free month": the extension fills
      only months strictly before the free series' first month with a value; interior gaps of the free series are not
      filled; a market or input with no free history at all has nothing to extend (and no overlap), so it fails.
   d. "monthly returns must correlate at least 0.95 with the free series over the overlap months up to 2010-12":
      Pearson correlation over the months where both have a monthly return, up to 2010-12; at least 24 overlap months
      (gm's C4 convention for a Bloomberg series), else the series fails ("too few overlap months"). Monthly return:
      block 1 the index's month-on-month change as gm/bloomberg.py commodity_return serves it (the engine's own route,
      with its C4 gate of more than 24 levels up to each month) against the panel return; block 2 the month-end price
      change of contract n against EIA contract n; block 3 (a yield, no return) the monthly change of the yield
      against the monthly change of the free 12-month dividend yield (lag-0 form). Correlation values are printed only
      over at least 60 months (export whitelist); with fewer the pass / fail is printed.
   e. As of: every Bloomberg series is read through bbg_panel.Source(asof="2010-12-31") (bbgdata as-of guard; market
      data carry a one-day live delay, so their last usable month-end is 2010-11); the sealed tables are never opened;
      every free input is cut at 2010-12-31 (gm_engine.Cut); outputs are checked by gm/seal.py.
   f. Which admitted series fills a month: block 1 month by month the first index in the registered preference order
      (config.BBG_ER_PREFERENCE: GSCI, then BCOM; gm-1.2.1 C4) that is admitted and has a return; block 2 contract n
      from its admitted Bloomberg series; carry recomputed where the free carry has no value and both (extended)
      contracts exist; block 3 the admitted yield / 100, lagged as E4 (12 months for the 7 non-US markets, 0 for the US).
6. Report (7.6 step 2, "report, no adoption test ... differences explained"): A1_INCUMBENT (CANDIDATE gm-2.0.3 + E13,
   gm/CHANGES.md "X1 outcome") at k = 1 on the A1 data against the same config at k = 1 on free data, one block at a
   time (free + block b alone, for each block with an admitted series), then all blocks together (= the A1 panel);
   design window 1975-01 .. 2010-12; eras 1975-89 and 1990-2010 and the whole window. Per arm: net Sharpe, mean,
   volatility, worst drawdown; difference to the free arm and dSR with its one-sided 95% lower bound (gm.stats
   paired_sr_test, section 2 bootstrap); Sharpe of each family x class block (unit-volatility blocks); market-months
   added by market; share of k = 1 market-months flagged; k = 0 beside (7.3 item 1). The A1 panel is the panel of
   every later run whatever the sign (U07-T4: "a correction enters the incumbent whatever its sign").
7. Trial count (7.8 item 1, family "data"): one gm/trials.csv row for A1 (the all-blocks arm, k = 1), written by the
   coordinator from the job's TRIAL ROW line, with the config hash, engine version, LOCK_v2 id and the A1 panel id.
8. Metadata listing (7.6 step 2, "A metadata job at each lock (free inputs, LOCK_v2, any LSEG lock) lists the first
   date of every series a spec reads"): free inputs and LSEG lock v5 now, from file metadata only
   (tools/bbgq/meta_first_dates.py -> docs/research/batches/META_first_dates_2026-11-27.txt and
   META_lseg_v5_2026-11-27.csv); 13 named series are not in the free inputs (GS1, GS2, GS5, GS10, FEDFUNDS, BAA,
   TWEXMMTH, DTWEXBGS, WALCL and the ALFRED first vintages of CPILFESL, M2SL, PCEPILFE, UNRATE: card inputs, fetched
   before B2). LOCK_v2: the first design date, status and design count of every candidate series and report-line
   series, printed by the A1 job on the PC.
9. Writes: the A1 panel values only to local\work\a1 on the PC (never to the repo or chat); the job prints metadata
   and the registered summary statistics only (tools/bbgq/README.md export whitelist).
Code (2026-11-27, commit 854b724; entry 56729b0 before it): tools/bbgq/lib/a1_panel.py 1.0.0 (candidates, Store over
bbg_panel.Source, free_inputs under gm_engine.Cut, evaluate, build, assert_extension_only, report, trial_row,
save_panel), PC job tools/bbgq/jobs/gm_a1_v1.py, packaged by tools/bbgq/build_engine.py; tests on mock bbgdata stores
and synthetic free inputs (tests/a1_panel_smoke.py, in tests/run_tests.py: extension only, correlation gate, copy /
cut / held back / missing, seal, panel id, no raw value printed, the job in the PC layout stops on a non-LOCK_v2
store before reading a value). Closed while coding: a series that passes every condition but has no month before the
free start is "rejected: nothing to extend" (it is not used); the job stops (prints STOP, reads no value) if the gm
code differs from engine_ref.json, the lock id is not LOCK_v2 or the free inputs differ; when no series is admitted
the report has the free arm only and the A1 panel equals the free panel. NOT RUN: the A1 report needs the Bloomberg
store on the PC (queue: docs/research/batches/A1_BUILD_2026-11-27.md). A1 panel id: to be recorded here after the run.
Corrections after the independent check (docs: CHECK_A1, APPROVED WITH CORRECTIONS; registered 2026-11-27 BEFORE their
code and BEFORE any A1 run; appended, the items above are not rewritten):
- Item 5b, correction ("same instrument" decided per series, not by one template; a registered table in
  a1_panel.py NOT_SAME / NOT_SAME_BEFORE; a listed series stays in the output as REJECTED with the reason):
  | Market | Series | Decision | Reason |
  |---|---|---|---|
  | cm_copper | SPGSICP Index | rejected | S&P GSCI copper rolls LME copper (GSCI contract IC); the free series is COMEX HG (HG=F, CPER) |
  | cm_copper | BCOMHG Index | candidate | BCOM copper rolls COMEX HG, the free series' contract |
  | cm_gasoline | SPGSRBP Index, BCOMRB Index | months before 2006-01 not the same instrument | before 2006 both rolled NYMEX HU (unleaded), not RBOB (RB); the LSEG entry treats gasoline before 2006 as another contract identity (HU). Every month they could add lies before the free start (2000-12), so neither can extend anything |
  | cm_gasoline | XB1 Comdty, XB2 Comdty (block 2) | months before 2006-01 not the same instrument | same reason, applied to the generic RBOB contracts for consistency (closed here; EIA rb starts 2005-10, so this changes nothing in practice) |
  | cm_brent | SPGSBRP Index, BCOMCO Index | candidate (same instrument) | both roll ICE Brent futures (CO); the free series (BNO ETF, NYMEX BZ=F, stooq co.f) holds or settles on the same ICE Brent futures, so it is the same reference contract |
  | eq_us_spx | MXUS Index (dividend yield) | rejected | MSCI USA is not the S&P 500, whose dividend yield the free series is (SPY minus ^GSPC) |
  | eq_de_dax, eq_gb_ftse, eq_fr_cac, eq_jp_nikkei, eq_ca_tsx, eq_au_asx, eq_hk_hsi | MSCI country index (dividend yield) | rejected | the free yield is the Ken French country 'Mkt' portfolio (value-weighted, with minus without dividends; gm/panel.py french_country_usd, gm/signals.py equity_dy); neither the repo, its source notes (macro/fetch_research.py) nor the file header states that this portfolio is an MSCI index, so the same index family is not established and the series are rejected (checked 2026-11-27) |
  Every other block-1 and block-2 candidate: the index or generic contract on the same exchange contract as the free
  series (per-market instrument text in a1_panel.py INSTRUMENT). Block-3 candidates for the 10 equity markets with
  no free dividend yield stay rejected for "no free history to extend". Consequence: block 3 admits nothing.
- Item 4, "Not candidates", addition (LSEG): the source of A1 is LOCK_v2. TESTING_PROTOCOL 7.6 step 2 writes the rule
  "for each Bloomberg series (LOCK_v2, lock id d85a46cb...)", REGISTRATION_3.4 part (c) item 3 registers "the
  extension-only rule of 7.6 step 2 with LOCK_v2 id ...", and 7.4 E15 names "the A1 data rule (7.6 A1) and the LOCK_v2
  reader path; later, the LSEG source (7.10 item 3) ... as data entries" as separate items; LSEG was not a registered
  source when A1 was registered. So LSEG series (LOCK_LSEG_v5), including LSEG contracts 1-2 and dividend yields that
  SPEC_Carry s3 and SPEC_Value s3 allow "from Bloomberg or LSEG", are not A1 candidates. No later run adds an LSEG
  backward extension to the existing pods' A1 panel (it would be a data change made with sight of A1); the A1-style
  exception in the LSEG data entry's item 4 applies only to the inputs that entry names (Curve carry legs, Strip
  reversion strips, T10 strip markets if admitted, card 3 R4, card 5 R1, card 3 R1 cross-check): LSEG enters only
  where its own registered data entry names it, i.e. the new pods and markets.
- Item 6, addition (report lines of TESTING_PROTOCOL 7.3 items 1-2): beside k = 1 and k = 0, the one-month delay
  (config key delay_months = 1, book.py) for every arm and era; the k = 1 flagged share by year 1975-2010 per arm;
  the family x class block table from the k = 1 books (decisive timing) as well as the k = 0 books, each labelled.
- Job hardening (no rule change): the job stops (prints STOP, reads no Bloomberg value) unless a1_panel.py,
  gm_engine.py, bbg_panel.py and bbgdata.py have the sha256 registered in the job (the values in A1_BUILD); it asserts
  the Store's lock id = LOCK_v2; before the Bloomberg candidates it compares the free arm with engine_ref.json
  (per-market sums of |signal| for E, C, V within the reproduction tolerance 1e-6, market months exact) and stops on a
  difference; exception messages are printed with the type and code frames only, numbers with 3 or more decimals
  replaced by <num>. The trial row's note names its parent (CANDIDATE a9466df18b; A1_INCUMBENT 465b5ecd4f).
  Code: c61e6dd (a1_panel 1.1.0 sha256 eb9ef3f7...22ebb5; job gm_a1_v1.py 8955c4e6...14e54ed), smoke cases added
  (well-correlated SPGSICP rejected, BCOMHG admitted, HU months unused, MXUS and MSCI-vs-French rejected, free-arm check,
  scrub, report lines). Reruns: k = 0 reproduction 24/24 difference 0, truncation PASS 8/8 (21 + 37 stages), run_tests
  ALL TESTS PASSED, smoke tests passed, free arm vs engine_ref difference 0 (cloud). gm/ unchanged in this round.
A1 RUN (2026-11-27, PC job gm_a1_v1, report tools/bbgq/results/gm_a1_v1.txt; every hash, lock and free-arm check PASS):
A1 PANEL ID e7f98d4439fccf91f3451bc4b9e78079e3bc2cc2452931363b28520460b6cb43 (LOCK_v2 d85a46cb2853646b, free inputs
378d65b09c23d234, a1_panel-1.1.0). Admitted 4 of 54 candidates; panel changed by 3: corn return 1971-12..2000-07
(SPGSCNP, corr 0.958), gold return 1980-01..2000-08 (SPGSGCP, 0.996), WTI contract 2 1984-11..12 (CL2). NG1 admitted
but adds nothing (NG2 is a first-pull copy). Most first-pull commodity indexes are copies (unusable); copper rejected
(SPGSICP = LME). Block 3 admits nothing. Report (CANDIDATE-x1, net, 1975-2010, k = 1): free SR 1.427, A1 panel 1.439
(dSR +0.012, lb95 -0.028); k = 0 1.469 -> 1.480; one-month delay 1.043 -> 1.052. k = 1 flagged share 0.21 (free) /
0.23 (A1). A1 is a data step, not a test (7.6): the A1 panel is the panel of every later design run from here on.

## X1 outcome (registered 2026-11-27, after the X1 run and BEFORE the E13 code and A1's design run): E13 for natgas, gasoline
Entry 4 of docs/research/registration/REGISTRATION_3.4.md part (c): "X1 outcome (after X1, before A1's design run): for
each energy market whose gate opens, E13 seasonal adjustment; if none opens, an entry saying so." TESTING_PROTOCOL 7.5
row X1 (order of running item 1: "X1 (signals only), before the A1 design run"); 7.4 row E13 "X1 seasonal adjustment of
a market's energy carry, coded only if X1's gate opens for that market (SPEC_Carry s3)".
Run: gm/diag_x1.py (diag_x1-1.0.0), free data (repo cache = the gm-1.2.3 reference inputs), every loader cut at
2010-12-31; output docs/research/batches/X1_2026-11-27.txt. SIGNALS ONLY: no return, no Sharpe, no month after 2010-12.
Signal = the Carry pod's input for each energy market, gm.signals.carry_values = 12 x (F1 / F2 - 1) from the EIA NYMEX
contracts 1 and 2 at month end (the input of both Carry versions: v1 its sign, v2 its rank in class). Window: design
month-ends 1975-01 .. 2010-12 from the first month the signal exists. Gate (registered, 1.3b s5, SPEC_Carry s13): share
of the signal's variance explained by its 12 calendar-month means >= 0.25.
| Market | Signal months | Smallest calendar-month count | Share | Gate |
|---|---|---|---|---|
| cm_wti | 1985-01..2010-12, 312 | 26 | 0.012 | closed |
| cm_natgas | 1994-01..2010-12, 204 | 17 | 0.403 | OPEN |
| cm_heatoil | 1994-02..2010-12, 203 | 16 | 0.178 | closed |
| cm_gasoline | 2005-10..2010-12, 63 | 5 | 0.564 | OPEN |
Rule from now on (E13, registered text of SPEC_Carry s3): for cm_natgas and cm_gasoline, "that market's carry in both
versions becomes carry minus the mean, over all earlier same-calendar month-ends (at least five; no signal before), of
(carry minus its trailing 12-month mean, the 12 month-ends up to and including that month-end)." cm_wti and cm_heatoil:
no change.
Where it applies: E13 sits in the 7.4 feature group (gate: "BASE and CANDIDATE at k = 0 reproduce the fix version's
reference exactly"), so it is a registered config key, "x1_seasonal" = (cm_natgas, cm_gasoline) (gm/config.py
X1_MARKETS), held by A1_INCUMBENT = CANDIDATE + the key (name gm-2.0.3-candidate-x1) and by the A2 challenger (built on
A1_INCUMBENT). BASE (the live paper book, 7.1 item 6) and CANDIDATE (the gm-2.0.3 reference) do not hold it and are
unchanged at k = 0. Both arms of the A1 report (7.6 step 2, CANDIDATE on A1 data against CANDIDATE on free data) and
every later run of the programme (A2 incumbent and challenger, Core book v1, B batches) use A1_INCUMBENT. Engine
version gm-2.2.0 (gm/config.py ENGINE_VERSION).
Closed here (details the registered text leaves open; simplest reading, none chosen from results):
1. The share is the plain (unadjusted) share, 1 - SS_within / SS_total over the window's months, i.e. the R^2 of a
   regression on 12 calendar-month dummies. The "five" of the spec's knob line ("X1 gate 0.25, five months") belongs to
   the adjustment (at least five earlier same-calendar values); the gate statistic is also computed only when every
   calendar month has at least 5 observations (else 'insufficient', gate closed). All four markets meet it (gasoline
   exactly 5).
2. Window from the first month the signal exists (cm_gasoline: EIA contract 2 from 2005-10) to 2010-12; months
   without a signal inside it are skipped, not filled.
3. E13: the trailing 12-month mean needs all 12 month-ends present; "earlier" = strictly before t (s(t) reads only
   months before t, so the rule is point in time); no adjusted value (missing, no position) where the carry or the
   seasonal mean is missing.
4. Consequences (signal facts, stated before the code from the rule itself; confirmed below): an adjusted value needs
   12 months for the first d plus five earlier same-calendar values of d, so cm_natgas's adjusted carry starts about
   six years after its raw start (1994-01) and cm_gasoline's (raw start 2005-10) lies after 2010-12: in design runs
   cm_gasoline holds no Carry position and the CM class has fewer markets with carry (version 2 needs 3).
5. Trial count: X1 is one gm/trials.csv row, family "diag" (7.5: "Each is logged as a design-data run (7.8)"), with
   no Sharpe (signals only).
Code and result (2026-11-27; X1 run and entry c5e8b60, E13 code d8253b2; no performance statistic computed): gm/signals.py
x1_adjust / x1_seasonal (SPEC_Carry s3 formula; synthetic test tests/gm_x1_smoke.py: equals the formula by hand, point
in time, removes a pure calendar pattern, only the keyed markets change); gm/book.py applies it in both the old and the
version path when the config holds "x1_seasonal"; gm/config.py X1_MARKETS, A1_INCUMBENT (config hash 465b5ecd4f, name
gm-2.0.3-candidate-x1), A2 challenger now built on A1_INCUMBENT (name gm-2.2.0-a2-challenger); ENGINE_VERSION gm-2.2.0.
Signal facts (signals only, design months): cm_natgas adjusted carry from 1999-12 (133 months; raw from 1994-01);
cm_gasoline none before 2011 (raw from 2005-10), as item 4 says. Gates: k = 0 reproduction of the reference 24 of 24,
difference 0 (tools/bbgq/results/engine_repro_cloud_2026-11-27_gm-2.2.0.txt; BASE 7651ea6ebc and CANDIDATE a9466df18b
unchanged); truncation test PASS at all 8 cut dates, 21 k = 0 stages and 37 feature stages including the E13 stages
(adjusted carry, A1_INCUMBENT positions and k = 1 book) (results/engine_trunc_cloud_2026-11-27_gm-2.2.0.txt);
tests/run_tests.py ALL TESTS PASSED (results/run_tests_gm_2026-11-27_gm-2.2.0.txt), tests/gm_bloomberg_smoke.py PASSED, tests/bbgq_engine_smoke.py OK. Reference: engine_ref.json numbers unchanged, code block rehashed (old file
engine_ref_gm-2.1.0.json).

## data: LSEG registered as a source for history (registered 2026-11-27, BEFORE first use): TESTING_PROTOCOL 7.10 item 3
Registered data entry (no rule change; no performance statistic of any LSEG-sourced path has been computed). LSEG
Workspace / Datastream workbooks L1a-L16f saved on the user's PC become a registered HISTORY source. Steps of 7.10 item 3:
(1) reader with as-of access: lsegdata-1.0.0 (tools/lseg/lsegdata.py, sha256 0d1b500d...16198de) + config CSVs (hashes
in the lock); (2) data check and contract identity: jobs lseg_check_v3, lseg_ident_v1-v4, lseg_contract_v3 (reports in
tools/bbgq/results), status docs/research/lseg/IDENTITY_STATUS.md; (3) lock: docs/research/lseg/LOCK_LSEG_v5.json, lock
id 90322681b9f989cc24393ae7de4fe24bf5af2f32074ffa6400b1cbed09c4074c (job lseg_build_v5, 2026-11-26), 2011+ sealed;
(4) weekly refresh job: lseg_weekly_v1 (continuous series; see item 6 for contracts); (5) licence statement:
docs/research/lseg/LICENCE_STATEMENT.md (user, 2026-11-24).
1. History and seal: observations dated <= 2010-12-31 are the design part; later ones are sealed (holdout key or live
   flag only; every attempt logged). As-of: an observation is known at its date plus the delay of lseg_live_sources.csv
   (market closes and settlements 0 days; economic series 45 / 60 / 90 days).
2. Contract identity (closed here: LSEG returns no contract calendar on this licence, L11; the calendar is not pulled):
   a. Contract-level prices carry their identity in their code. Pulled for the roots that need contracts beyond position
      2: CL, LCO, RB, SI, HG, PL, C, W, S, SB, CT, LC (monthly month-end settlements, Datastream "<RIC>" form; Brent in
      the HistoricalPricing form) and the strips ED (1982-2012), FEI (1999-2012), daily. Check (lseg_contract_v3):
      continuous c1/c2 month-ends match one contract whose delivery agrees with LSEG's TR.ExpiryDate identity in 99-100%
      of matched months (sugar 95%). Design deliveries only (to 2012); contracts delivering 2013 and later are pulled in
      the same forms after the freeze, for the holdout and live record.
   b. Positions 1-2 of every HistoricalPricing root: identified per month-end by the TR.ExpiryDate dated series of c1 /
      c2 (L11/L12), except platinum (no series).
   c. Continuous positions of NG, HO, GC, KC (not pulled as contracts): lseg_rules-1.1.0 (tools/lseg/lseg_rules.py,
      sha256 56869991...cc42da9) LISTING models, fitted by lseg_ident_v4 on design evidence (agreement 100 / 99.5 /
      100 / 100% at every observed depth); a contract is held through its expiry day; expiry = observed TR.ExpiryDate
      where shown, else the exchange rule. The fit is an identity fact read from prices and expiry dates, not a
      performance choice; no return was computed.
   d. Not identified (hold nothing where a spec needs identity, SPEC_Curve_carry s3, 7.6 step 8): short sterling and
      Euroswiss strips (no expired-contract codes on LSEG), gasoline before 2006 (HU), copper before 1988, cotton and
      cattle contracts of the 1970s (L16f probe: none in either form), Euribor before 1999 (did not exist).
3. Coverage facts (data availability, not results): Curve carry design months with both legs priced (front >= 3 months
   out and the same month a year later): HG 100% (from 1988-07), CT 96%, SB 86%, CL 80%, C 79%, SI 78%, RB 76%, S 64%,
   W 40%, LCO 37%, PL 19%, LC 13% (the far leg is mostly not yet listed); strips: all eight quarterly contracts priced
   on 5,475 of 5,480 Eurodollar days 1990-2010 and 3,149 of 3,149 Euribor days 1999-2010.
4. Scope: LSEG serves the inputs the specs list as LSEG (Curve carry legs, Strip reversion strips, T10 strip markets if
   admitted, card 3 R4 forward EPS, card 5 R1 fronts, card 3 R1 deposit-rate cross-check). It never replaces a free-data
   series the engine already uses, except by the A1-style rule of 7.6 step 2 (same instrument, extend backwards only,
   overlap correlation >= 0.95 up to 2010-12), applied per series and listed in the run that uses it.
5. Excluded series: lseg_exclusions.csv (wrong series CEDCS00, LSSCS00, MBACS00, LESCS00, GSPTTOT; Moody's after 2019).
6. Live (not yet open): LIVE_START is set in a later data entry, after the weekly file adds the current contract codes of
   every LSEG-sourced leg (lseg_weekly v2) and its first ingest; until then no LSEG-sourced pod runs live.
Usage: not separately measured (done in the coordinator session, no subagent).

## gm-2.1.0 feature version (registered 2026-11-24, BEFORE the code): E6-E11, E14
Feature version (no change to BASE or CANDIDATE at k = 0). Registered in docs/research/global_macro/TESTING_PROTOCOL.md
section 7.4 rows E6-E11 and E14 with 7.3 items 1-3, 5, 6 and 7.7 (step 3.4, 2026-11-23); this is entry 2 of
docs/research/registration/REGISTRATION_3.4.md part (c). The fix version gm-1.2.3 (E1-E5, entry 1) is done (afca6b2,
d68c0d6, c27d9d2). Each item below is the registered text (quoted where possible); none is chosen from results, and none
is revisited after them. Not in this version: E12, E13, E15, the LSEG source, the pod builds (Curve carry, Strip
reversion, the card rule-layer engine of part (c) item 6), and every diagnostic run (7.5).
1. E6 "k = 1 return form of 7.3 item 2 with flags" (7.3 item 1: decisive timing is k = 1). 7.3 item 1: "a position
   decided at the close of month-end t is traded at the close of the first trading day after t and held to the close of
   the first trading day after month-end t+1. Reported beside it: k = 0 (the engine's same-close form, book.py run,
   timing.py k = 0) and the one-period (one-month) delay of WORKFLOW s5." 7.3 item 2: "k = 1 return of market m for the
   holding decided at t: the panel's monthly excess return of month t+1, plus the price return of m on the first trading
   day of month t+2, minus the price return of m on the first trading day of month t+1 (carry and dividends accrue
   monthly, as timing.py assumes). It applies where a daily price of m exists on both days. Where it does not, the k = 0
   monthly return is used and the market-month is flagged; the result sheet reports, by year, the share of gross position
   flagged. Costs are charged as today."
2. E7 "Version-grid machinery: each version computed as a complete pod, pod position = equal-weight mean of version
   positions at the unscaled stage, a missing version counted as 0 (SPEC_Trend s3 step 6); Trend 16, Economic trend sign
   shape, Carry versions 1/2 as separate signals, Value version 2". Grids as the approved specs fix them (section 6 of
   each): Trend v1-v4 lookback 1/3/6/12 months, sign, hybrid volatility; v5-v8 the same with m36; v9-v12 graded (cap 2),
   hybrid; v13-v16 graded, m36 (SPEC_Trend s3 steps 1-6). Economic trend v1 f(z) = tanh(z / 2) (today), v2 f(z) =
   sign(z) (SPEC_Economic_trend s3 step 8). Carry v1 directional w = sign(carry), v2 cross-asset w = rank in class
   (SPEC_Carry s3; "this reproduces today's half-and-half exactly"). Value v1 as coded; v2 bonds yield(t) - yield(t-60
   month-ends), currencies minus the deviation of q(t) = ln USD value(t) + cumulative (local CPI yoy - US CPI yoy) / 100
   / 12 from its expanding mean (at least 60 months of q), equities as v1 (SPEC_Value s3). Each version: position = w x
   0.40 / vol, divided by the count of markets in the class with a position that month; Trend versions use their own
   volatility (vol_v), every other pod the CANDIDATE hybrid estimate. 7.6 step 3 defines the A2 challenger ("CANDIDATE
   with Trend 16 versions, Economic trend 2, Carry 2, Value 2"): its config is written here; it is not run.
3. E8 "Weekly tranche engine of 7.3 item 6" (registration part (c): "NYSE calendar, offsets 0/5/10/15, k = 1 trades,
   cut"). 7.3 item 6: "tranche j = 0, 1, 2, 3 decides on trading day 5 x j after the month's last trading day. Trading
   days = days the New York Stock Exchange is open; a market without a price that day uses its last price ... Each
   tranche holds a quarter of the pod from the close of the trading day after its decision day (k = 1) to the same point
   after its next decision day. Decisions dated after 2010-12-31 do not exist (tranches 1-3 of month-end 2010-12 decide
   in January 2011); holdings of tranches 1-3 decided in December 2010 end at the 2010-12-31 close. Monthly design runs
   use tranche 0 only. The tranche form runs only in the weekly-implementation check (1990-2010, reported). In it, a
   market without daily data holds its tranche-0 position all month and is flagged ... coverage is reported." Card 4
   R1-R4 and Curve carry have no tranches (registered exceptions).
4. E9 "Component masks (pod x class x version) so that the Core book holds only Core parts and the shadow book the
   rest; Core book at equal risk: each Core part's summed scaled-block return is rescaled to unit volatility (trailing
   36-month realised volatility, lagged one month, as the block scaler) and weighted 1/n before the book scaler (book.py
   family weights alone give a 4-block part up to about twice the risk of a 1-block part)". Core parts (7.2 item 5, 7.6
   step 6): Trend (all classes and versions); Carry currencies version 2 plus energy versions 1 and 2; Value equities
   (both versions). Shadow: Economic trend; Carry currencies version 1 and bonds (both versions); Value bonds and
   currencies (both versions). "Core book v1 = the Core parts at equal risk as defined in 7.4 E9, 10% target, the
   engine's caps."
5. E10 "Test code: alpha bootstrap (7.7 T1) in gm/stats.py; placebo engine (7.7 T3) for monthly signals, rule states
   and date rules; non-inferiority decision for hygiene (7.7 H1-H4)". T1: "Intercept of the least-squares regression of
   the pod's monthly net return on the Core book's monthly net return over the window. One-sided p for H0 alpha <= 0
   from the centred stationary bootstrap: whole months, mean block 6, 10,000 resamples, seed 20261101, the regression
   re-fitted in every resample; p = share of resamples with (alpha_b - alpha_hat) >= alpha_hat"; Holm-adjusted p < 0.025
   over the Core-eligible systematic pods. T2: alpha of T1 with every cost doubled > 0. T3: "1,000 placebos, seed
   20261101. Monthly pods and state rules: the score array (before division by volatility) of all markets moved jointly
   in 12-month blocks in random order (blocks aligned to the window's first month, the last part-block kept), then
   re-sized with each month's own volatility, scalers and caps, same costs. Card 4 R1-R4: each window moved to a random
   start in the same calendar year (R1, R3) or month (R2, R4), same length in trading days, gates re-read at the new
   dates"; pass: "share of placebos with net Sharpe >= the pod's < 0.05". T4: test 5 on the combined book (Core book +
   pod at lambda 0.5, rescaled to 10% by its trailing 36-month realised volatility, lagged one month) against the Core
   book alone. H1 "one-sided 95% lower bound of dSR (paired stationary bootstrap of section 2, pooled design window) >
   -0.10; H2 dSR at twice the costs, reported; H3 tail test 5 between the two books; H4 (A3 only) the item's own target,
   point estimate ... Pass = H1, H3 and, in A3, H4."
6. E11 "Spread pods: joint caps (a currency's whole Strip contract vector multiplied by the smallest ratio cap_j /
   abs(x_j); Curve carry's two legs share one cap from the front leg's hybrid volatility); per-instrument gross weight
   (3-month contracts at 0.25/1.9 of notional)". Why (7.4): "book.py clips each column alone, which breaks level
   neutrality (SPEC_Strip_reversion s5; SPEC_Curve_carry s5; CHECK_3.2_B s4)". Machinery only: no spread pod is built.
7. E14 "Daily S&P excess return for card 4 (spec s3: ^GSPC daily price return + the panel's monthly carry part spread
   over trading days)". SPEC_Card4 s3: "e(d) = ^GSPC price return of day d + c(m) / N(m), where c(m) = panel eq_us_spx
   monthly excess return minus the ^GSPC monthly price return ... and N(m) = trading days in m. So a rule held all month
   earns exactly the panel's monthly excess return."
8. E5 in every new path (part (c) item 2: "E5's seal and holding cut are built into each new path in this entry"):
   7.3 item 5, every holding of the k = 1, tranche and daily paths ends at the close of 2010-12-31 at the latest; no
   price or statistic dated after 2010-12-31 is read; "under k = 1 the decision at month-end 2010-12 is never traded; the
   holding decided at month-end 2010-11 ends at the 2010-12-31 close (the move to 2011-01-03 is not read)"; card 4
   windows that would run into 2011 end at the last trading day of 2010. Each new path's output passes gm/seal.py
   check_output.
Version names: the engine version is gm-2.1.0 (gm/config.py ENGINE_VERSION). BASE stays gm-1.2.3 and CANDIDATE
gm-2.0.3-candidate (nothing changes at k = 0; gm/run.py VERSION stays the BASE name gm-1.2.3). The A2 challenger config
is named gm-2.1.0-a2-challenger. No rule, weight, threshold or cost of BASE or CANDIDATE changes.
Gate (7.4 "Gate for E6-E14", part (c) item 2): BASE and CANDIDATE at k = 0 reproduce the gm-1.2.3 reference
(tools/bbgq/engine_ref.json) exactly, 24 of 24 items, difference 0; the truncation test passes at all 8 cut dates,
including the k = 1, tranche and daily paths (and the grid, Core and shadow positions) cut at each date; tests pass
(tests/run_tests.py with a new synthetic-data test of every item). NO PERFORMANCE STATISTIC OF ANY NEW PATH IS COMPUTED
IN THIS VERSION: no return, Sharpe, drawdown, hit rate, alpha, p-value or placebo result of any k = 1 form, version,
grid, tranche, Core or shadow book or pod, on real data, in any period. On real data only the k = 0 reproduction and
the truncation test (positions, signals and value differences across cut dates) are run. Every test of the new
statistics runs on synthetic data with known answers. No gm/trials.csv row (nothing is a trial). The live paper ledger
and the holdout are untouched.
Closed here, before the code (details the registered text leaves open; simplest reading consistent with the specs):
1. NYSE calendar (E6, E8, E14): the NYSE open days are the dates of the daily ^GSPC closes in the free daily file
   (gm/daily.py EQ_DAILY, from 1970-01-02), the engine's only record of NYSE days; it includes the special closures
   (e.g. 2001-09-11 to 09-14). "Month-end" = the month's last NYSE day; "first trading day" = its first NYSE day.
2. E6 price return of m on a day = gm/daily.py build()'s daily return of m on that day turned into a price return
   (bonds and notes: -duration x yield change, already a price return; every other market: exp(log return) - 1); a day
   without a value (no price, or removed by daily.py's 25% filter) has no price, so the market-month is flagged and
   earns the k = 0 return. Positions, signals, scalers, caps and costs are the same under k = 0 and k = 1: only the
   return a holding earns changes (the block and book scalers keep reading the k = 0 returns, which are known at the
   decision close; the k = 1 return of the last holding is not). Cost timing as today (the same cost series, same
   lag). Holding cut: where the first trading day of t+2 lies after the seal (or after the last day of a truncated run),
   the holding ends at the close of month-end t+1: return = R(t+1) - price return of the first trading day of t+1, not
   flagged. Months whose first trading day is missing from the calendar (before 1970) are flagged.
3. E7 configs: a config key "grid" ({pod: versions}); absent = today's single form, so BASE and CANDIDATE are unchanged.
   A missing version adds 0; a market-month where no version has a position holds no position (missing, as today), so
   block starts are unchanged. Each version counts its own markets with a position (n_v). The alternative-commodity
   30% cap (inactive while E1 is off) applies to the averaged pod. Trend vol_v: "hybrid" = CANDIDATE's vol parameters,
   "m36" = vol.py m36; the per-market cap uses the config's engine volatility (SPEC_Trend s5: CANDIDATE hybrid). Economic
   trend sign shape: f is applied where tanh(z / 2) is applied today (FX: to local minus US theme; commodities: to the
   four-country mean); both shapes come from one pass over the themes. Value v2 currencies: CPI as v1 (carried at most
   18 months, lagged 1 month); the cumulative inflation gap starts at the first month both CPIs exist and a month
   without a gap adds nothing; q is missing where the USD value is missing; the expanding mean is over all q values up
   to and including t. Carry: v1 = sign of carry through the "dir" form, v2 = cs_rank; whenever components or a grid are
   used, Carry is computed as these two versions (equal to the half-and-half form; checked on synthetic data, and on
   real positions in the result commit).
4. E8: decision day d_j(t) = the (5j)-th NYSE day after month-end t (j = 0: month-end t); the holding runs from the
   close of the NYSE day after d_j(t) to the same point after d_j(t+1). Tranche j's decision panel X_j(t) = R(t) - pr(m,
   month-end t-1 -> d_j(t-1)) + pr(m, month-end t -> d_j(t)) and its earned return Y_j(t+1) = R(t+1) - pr(month-end t ->
   d_j(t)+1 day) + pr(month-end t+1 -> d_j(t+1)+1 day), where pr(a -> b) = the ratio of m's last daily price at or before
   b to its last daily price at or before a, minus 1 ("uses its last price"); carry accrues monthly, as for k = 1.
   Tranche 0 is exactly the E6 monthly k = 1 path (its flags included), so the monthly design run is tranche 0. Price
   trend, cross-sectional momentum and every volatility estimate of tranche j read X_j and the daily EWMA at d_j(t)
   (the last daily value at or before it); Economic trend, Carry and Value use their month-end t values (all published
   by d_j(t)). A market has daily data for label t if its first daily price is at or before month-end t-1 (decided by
   the past only, so the rule is truncation-safe); a market without daily data uses R(t) in X_j, earns tranche 0's k = 1
   return and holds tranche 0's final position (overwritten after the caps), flagged. Each tranche is a full book run
   with its own costs; the tranche form's return = one quarter of the sum of the four tranche returns (a tranche without
   a return that month adds 0). Decision days after the seal do not exist (no position); holding ends are capped at the
   seal close.
5. E9: a component = (pod, class, version), versions numbered as the grids (a config without a grid has one version per
   pod, except Carry, always split into v1 and v2 for masks). Component position = its term p_v / V in the pod average,
   so the Core and shadow components partition the pod. Masked block = the sum of a class's masked components, scaled
   by the block scaler (36 months, at least 24, lagged, multiplier capped at 50). Part return = the sum over its blocks
   of the scaled block position's return r_b(t) x k_b(t-1) (book.py's blocks table records r_b(t) x k_b(t); the part
   scaler needs the return of the position it scales); part scaler = the block scaler's convention (36 months, at least
   24, lagged one month, capped at 50); weight 1/n with n = the number of parts in the book (3 for the Core book),
   constant. Then the book scaler, the per-market cap, the gross cap and costs exactly as book.run; family shares are not
   used. Shadow book: the same construction over the shadow parts (Economic trend; Carry shadow; Value shadow). BASE's
   cross-sectional momentum is not a component.
6. E10: the bootstrap index matrix is gm.stats._stationary_idx(T, 10000, 6, 20261101) (the registered section 2
   bootstrap); p = (number of resamples with alpha_b - alpha_hat >= alpha_hat) / 10,000, as registered ("share"); the
   count is returned too (tools/power used (count + 1) / 10,001, as paired_sr_test does; the test checks the counts
   agree). A zero Core book (7.6 step 6: "alpha against a zero book (the pod's own mean)"): beta 0, alpha = mean. The
   window is the common months of the two series. Placebo: the window's months are cut into 12-month blocks from its
   first month (the last part-block kept), the blocks are put in random order by numpy default_rng(20261101).permutation,
   drawn in sequence, 1,000 placebos; the permuted array is every version's score or rank weight (before x 0.40 / vol),
   rows inside the window only, all markets jointly; p = (placebos with net Sharpe >= the pod's) / 1,000 on the window;
   pass p < 0.05. Date rules: each window's entry is redrawn uniformly among the NYSE days of its calendar year (R1, R3)
   or month (R2, R4), length kept in trading days, cut at the seal close; the caller re-reads the gates. H1-H3: H1 = the
   lb95 of gm.stats.paired_sr_test on the common pooled window > -0.10; H3 = check 5 of gm.protocol.decide (max fall not
   more than 2 points worse, worst month not more than 1 point worse); identical books pass. T4: the combined book is
   rescaled; the Core book is taken as run (its own book scaler is the same convention); common months.
7. E11: config key "cap_groups" = list of {"members": [...], "cap_from": None or a member}; a group's ratio = min(1,
   min over members with a position of cap_j / abs(x_j)), cap_j = the per-market cap of j (or of cap_from for every
   member); all members are multiplied by it; columns outside a group clip as today; no group = today. Gross weight:
   config.STRIP_GROSS_WEIGHT = 0.25 / 1.9 through the existing "gross_weights" config key.
8. E14: price return of day d = ratio of consecutive ^GSPC closes minus 1; c(m) = panel eq_us_spx(m) minus the SUM of
   the daily price returns of m (the reading that makes "a rule held all month earns exactly the panel's monthly
   excess return" true); N(m) = number of ^GSPC days in m; no value in a month without a panel return or without daily
   closes; no day after 2010-12-31.
9. Truncation horizons for the new stages: positions and signals compare months <= T; a k = 1 or tranche return or a
   tranche position whose holding or decision day falls after T in the full run is cut at T in the cut run (the holding
   cut rule), so these compare months <= T - 1 (all months at T = 2010-12-31, the seal); daily e(d) compares days <= T.
Closed while coding (before any real-data run of a new path; simplest reading, none from results):
10. E9 active months of an equal-risk book: months with a scaled part return r_P(t) x k_P(t), the convention of
    book.py's blocks table (r x k) for the old book. Found on synthetic data: counting months from the first scaled
    BLOCK return let the book scaler read about 24 warm-up months of exact zeros (while the part scalers warm up), so
    its 36-month volatility was 0 and the first positions were infinite (then clipped to every market's cap).
11. E8 labels before the calendar's first month (before 1970) or whose month-end lacks a neighbour: X = R, the market
    earns tranche 0's return and holds tranche 0's position, flagged (as "no daily data"). Tranches 1-3 of a label whose
    decision day lies after the seal hold no position (their positions are missing at 2010-12).
12. E7 the version path builds the components of the four pods even where a config's family share is 0 (a parts book
    can hold them); the ordinary book still drops a family with share 0 (BASE xsmom 5%, CANDIDATE xsmom 0). Trend
    version "m36" = gm/vol.py m36 whatever the config's own model; "hybrid" = CANDIDATE's vol parameters (equal to the
    config's estimate when the config uses them, then reused).
13. E10 the placebo runner (gm/book.py placebo_net_fn) runs the pod itself on the same version path with the identity
    map, so pod and placebos share one code path; a date map covers the months from the window's first month to the
    last design month.
14. Code layout: gm/execution.py (calendar, E6, E8, E14), gm/book.py (E7 version path family_positions_v, E9
    mask_components and the parts book, E11 cap_positions; run() keeps today's code path when no new option is used),
    gm/stats.py (E10), gm/signals.py (econ_versions, value_v2), gm/vol.py (daily volatility sampled at a given day),
    gm/config.py (grids, A2_CHALLENGER, CORE_PARTS, SHADOW_PARTS, STRIP_GROSS_WEIGHT, test constants,
    ENGINE_VERSION). Engine runner tools/bbgq/lib/gm_engine.py 1.2.0 (feature paths and their truncation stages);
    tools/bbgq/engine_repro_cloud.py (k = 0 reproduction in the cloud, PASS / FAIL and differences only);
    tools/bbgq/engine_ref.py --rehash (rewrites the reference's code block only after a 24 of 24, difference 0 run).

Result (2026-11-24/25, free data, design months only; code commit 9efa371; inputs = the repo cache, the same files as
the gm-1.2.3 reference). No performance statistic of any new path was computed, printed or logged; on real data only
the two gate runs below were made.
1. k = 0 reproduction (tools/bbgq/engine_repro_cloud.py -> tools/bbgq/results/engine_repro_cloud_2026-11-24_gm-2.1.0.txt):
   BASE and CANDIDATE reproduce the gm-1.2.3 reference 24 of 24 items, largest difference 0.0 (statistics, per-year
   book returns, positions, volatility, family positions, signals, market months). REPRODUCTION PASS.
2. Truncation test (tools/bbgq/engine_trunc.py --features -> tools/bbgq/results/engine_trunc_cloud_2026-11-24_gm-2.1.0.txt):
   PASS at all 8 cut dates (1980-06 ... 2010-12): the 21 k = 0 stages (BASE, CANDIDATE) 0 differing cells end-to-end
   and alone; the 34 feature stages (NYSE days; Economic trend sign shape and Value v2 signals; k = 1 returns and flags;
   k = 1 book returns of BASE, CANDIDATE and the A2 challenger; the challenger's positions, volatility and family
   positions; positions, part returns and k = 1 returns of the equal-risk Core and shadow books; panel, holding
   returns, positions and flags of tranches 1-3 and the tranche form; card 4 daily excess return) 0 differing cells
   end-to-end and alone, every input cut at the loader. Control: for the stages compared up to T - 1, month T itself
   differs between the full and the cut run (the holding cut bites; e.g. 1998-06: 38 k = 1 return cells, 44-65 cells
   per tranche panel / holding return / position), except the tranche flags, which depend only on when daily data
   start. Positions only, real data: Carry v1 + v2 averaged equals the half-and-half family position of CANDIDATE
   (largest difference 1.4e-14, no missing-pattern mismatch), as SPEC_Carry states.
3. Tests: tests/run_tests.py ALL TESTS PASSED (420 checks; tests/gm_feature_smoke.py adds 67 synthetic-data checks:
   tools/bbgq/results/run_tests_gm_2026-11-24_gm-2.1.0.txt); tests/gm_bloomberg_smoke.py PASSED;
   tests/bbgq_engine_smoke.py BBGQ ENGINE SMOKE OK (packaged engine reproduces the reference 24 of 24, truncation at
   1995-12 PASS, Bloomberg adapter on mocks, output whitelist clean).
4. Reference: every number of tools/bbgq/engine_ref.json is unchanged (made 2026-11-24 by gm-1.2.3); only its code
   block (gm file hashes, gm commit 9efa371, engine helper gm_engine-1.2.0) was rewritten by engine_ref.py --rehash
   after a 24 of 24, difference-0 run; the previous file is kept as engine_ref_gm-1.2.3.json.
5. Version strings: gm/config.py ENGINE_VERSION = gm-2.1.0; BASE name gm-1.2.3 and CANDIDATE gm-2.0.3-candidate
   unchanged (config hashes 7651ea6ebc / a9466df18b, as in the reference); gm/run.py VERSION stays gm-1.2.3 (the BASE
   name, nothing changes at k = 0); tools/bbgq/lib/gm_engine.py VERSION gm_engine-1.2.0. No gm/trials.csv row.
Not built here (as registered): E12, E13, E15, the LSEG source, the Curve carry and Strip reversion pods (E11 is the
cap machinery only), the card rule-layer engine (rule states, entry versions, netting; E10's mover and move_rows are
its placebo tools), every diagnostic of 7.5. The PC engine is not redeployed in this version (the packaged copy is
built and checked by tests/bbgq_engine_smoke.py; a PC run of gm_repro with the new lib is the next PC step).

## gm-1.2.3 and gm-2.0.3 candidate (registered 2026-11-24, BEFORE the code change): E1-E5
Fix version (may change design numbers). Registered in docs/research/global_macro/TESTING_PROTOCOL.md section 7.4 rows
E1-E5 and 7.3 item 5 (step 3.4, 2026-11-23); this is entry 1 of docs/research/registration/REGISTRATION_3.4.md part (c).
Each item is the registered text; none is chosen from results, and none is revisited after them.
1. E1 gm/config.py (flags), read by gm/signals.py and gm/panel.py: Bloomberg switches OFF by default, by registered
   config flags: Value's Bloomberg equity composite; Carry's farthest-contract commodity curve carry; the alternative
   commodity columns (until charter D1 admits a market through A3); Bloomberg growth surprise. Why: different measures
   on different markets, switched on by which tickers load (register D4-D6, D16); a Bloomberg-only input cannot run
   live (rule 7). With no Bloomberg file present (the cloud and free-data case) E1 alone changes no number; this is
   shown before the other items are coded.
2. E2 gm/bloomberg.py EQ_INDEX: remove the mappings eq_eu_stoxx50 -> "MXEM Index", eq_us_ndx -> MSCI USA, eq_us_r2k ->
   MSCI USA; every remaining mapping (a local index to the MSCI index of the same country) is used only if the A1 rule
   of 7.6 step 2 admits the series. Why: code defect (NOTES_3.1_agent_A item 3; CHECK_3.2_A s4 item 12). Inactive on
   free data.
3. E3 gm/signals.py: CPI as-of rule: a country whose OECD CPI series is quarterly enters a quarter's value at the end
   of the month after the quarter ends; oecd_sdmx raises an error instead of returning an empty table when the csv
   cannot be parsed; a metadata job lists, per country, monthly or quarterly and the first date (metadata only, design
   rows only). Why: look-ahead (SPEC_Economic_trend s3; CHECK_3.2_A s4 item 7: a parse error silently moves every
   country to FRED). Found while reading the code before this entry: the current parser reads a quarterly period
   "YYYY-Qn" as the FIRST month of the quarter (pandas), so a quarterly value would enter before its quarter ends.
4. E4 gm/signals.py, Value, the 7 non-US equity markets (Germany, UK, France, Japan, Canada, Australia, Hong Kong; Ken
   French country files): the trailing 12-month dividend yield used at month t is the one ending at t-12 (design and
   live alike); US (SPY) unchanged. Why: the live Ken French file can be up to 12 months stale (ffill limit 12) while
   the design run used month t (CHECK_3.2_A s4 item 5); using the bound means live is never staler than the backtest.
   Reported: the lag-0 form, kept as a flag (default = the registered lag-12 form).
5. E5 seal and holding cut (7.3 item 5): every holding period of every pod, tranche, rule and diagnostic ends at the
   close of 2010-12-31 at the latest. No price, settlement or statistic dated after 2010-12-31 is read, printed or used
   before the holdout. Under k = 1 the decision at month-end 2010-12 is never traded; the holding decided at month-end
   2010-11 ends at the 2010-12-31 close (the move to 2011-01-03 is not read). Why: sealed days were reachable through
   k = 1, tranches and forward windows (checks A item 9, C item 3; register D15). This entry covers the paths that exist
   now: the monthly k = 0 book (gm/book.py), the existing trade-delay diagnostic (gm/timing.py) and the engine runner
   (tools/bbgq/lib/gm_engine.py); the k = 1, tranche and daily paths are built in entry 2 with the cut built in. A guard
   and a test fail if any design output has a date after 2010-12 or uses an input dated later. The live run
   (gm/run.py) and the one-shot holdout run (gm/holdout.py) are not design runs and say so explicitly.
VERSION gm-1.2.3 in gm/run.py; config names gm-1.2.3 (BASE) and gm-2.0.3-candidate (CANDIDATE). No other rule, weight,
threshold or cost changes.
Gate: the truncation test passes at all 8 cut dates for BASE and CANDIDATE on free data; tests pass
(tests/run_tests.py, tests/bbgq_engine_smoke.py, tests/gm_bloomberg_smoke.py); the current reference (gm-1.2.2) is
reproduced 24/24 before the change. Reported once: design-period statistics before and after (net Sharpe, mean, vol,
worst drawdown; BASE and CANDIDATE; 1975-2010 and 1990-2010). Logged in gm/trials.csv as family "fix" (one row per
config, not a selection trial). New reference tools/bbgq/engine_ref.json (old one kept as engine_ref_gm-1.2.2.json).
Live paper ledgers: untouched (workflow disabled); the next live run restates under the new version name. Holdout not
run. The PC engine is redeployed when PC jobs that import pandas run again (7.4 precondition).

Result (2026-11-24, free data, design months only; inputs = the repo cache, the same 239 files as the gm-1.2.2
reference, which the cloud reproduced 24/24 before the change; code commit d68c0d6): truncation test PASS at all 8 cut dates
(1980-06 ... 2010-12), every stage (21 of 21), BASE and CANDIDATE, 0 differing market-months
(tools/bbgq/results/engine_trunc_cloud_2026-11-24_gm-1.2.3.txt). Which item moves numbers (engine fingerprint, 24
items, vs the gm-1.2.2 reference): E1 + E2 + E3 with E4 at lag 0, unsealed engine 24/24 identical (E1 alone changes no
number on free data, nor do E2 and E3); the same sealed (E5) 24/24 identical; gm-1.2.3 sealed vs unsealed 24/24
identical. Only E4 changes numbers: Value's signal for the 7 non-US equity markets and everything that follows from
it (other signals, volatility estimates and market months identical). So the reported lag-0 form of E4 has exactly
the gm-1.2.2 statistics (the "old" column). Net of costs, old -> new:
| Config | Period | Sharpe | Mean %/yr | Vol %/yr | Worst drawdown % |
|---|---|---|---|---|---|
| BASE gm-1.2.2 -> gm-1.2.3 | 1975-2010 | 1.222 -> 1.226 | 12.34 -> 12.46 | 10.10 -> 10.17 | -19.9 -> -21.0 |
| BASE gm-1.2.2 -> gm-1.2.3 | 1990-2010 | 1.452 -> 1.469 | 14.27 -> 14.47 | 9.83 -> 9.86 | -12.5 -> -12.3 |
| CANDIDATE gm-2.0.2 -> gm-2.0.3 | 1975-2010 | 1.456 -> 1.461 | 14.27 -> 14.38 | 9.81 -> 9.84 | -16.9 -> -16.8 |
| CANDIDATE gm-2.0.2 -> gm-2.0.3 | 1990-2010 | 1.608 -> 1.620 | 16.23 -> 16.38 | 10.09 -> 10.11 | -16.9 -> -16.8 |
E3 metadata (tools/bbgq/cpi_freq_meta.py -> tools/bbgq/results/cpi_freq_meta_2026-11-24.txt): the cached
oecd_cpi_yoy.csv holds monthly rows only (19 countries, 0 quarterly; macro/fetch_research.py requests frequency M), so
the quarterly as-of rule is built and tested on synthetic rows but INACTIVE on this file; it acts if quarterly rows ever
arrive. Australia has OECD rows only after 2010-12 and New Zealand none, and neither has a FRED fallback file, so
neither has CPI in design months (unchanged; a new CPI source would be a data entry). Every other country: OECD monthly
from 1990-01, FRED monthly before.
Closed here (details the registered text leaves open; simplest reading, not chosen from results):
1. E1: the four switches are module-level registered constants (gm/config.py BBG_SWITCHES), not keys of the BASE /
   CANDIDATE dicts, because the panel and the signals are shared by both configs. Growth surprise off = an empty series
   (the theme is unused anyway: ECON_THEMES has no growth and GROWTH_SOURCE stays 'off'). The Bloomberg excess-return
   indexes of the 16 panel commodities are not an E1 switch: they are the A1 data swap (7.6 A1, E15).
2. E3: a quarterly value sits on the quarter's last month and is carried two more months; with the callers' existing
   one-month publication lag (Economic trend lag 1, Value shift 1) it enters at the end of the month after the quarter
   ends and stays until the next quarter enters. Where a country has both, its monthly value wins month by month. A
   period that is neither YYYY-MM nor YYYY-Qn, or any read error, raises OECDParseError; a MISSING file still gives an
   empty table (the registered text names the parse error only). The metadata listing counts rows up to 2010-12 only
   and shows a first date only if it is in the design period; it also lists the FRED fallback's spacing.
3. E4: the lag-12 value at t is exactly the 12-month sum ending at t-12, with no carry-forward (the old 12-month
   carry-forward stays only in the lag-0 form), so a file that does not reach t-12 gives no value. Only Value changes:
   equity carry (not in the book) keeps the lag-0 form; the Bloomberg-composite path (switched off) ranks the same
   lagged yield. Flag: gm/config.py VALUE_DY_LAG (12); value_values(dy_lag=0) gives the reported form.
4. E5: a design run is every run except gm/run.py (live) and gm/holdout.py (the one-shot holdout), which pass
   seal=None; gm.book.run seals by default (inputs after 2010-12-31 are dropped, not masked; outputs end at 2010-12 and
   are checked by gm/seal.py check_output). Under k = 0 the decision at month-end 2010-12 is computed but earns
   nothing, and its trading cost (charged in 2011-01) is not charged. The engine runner (gm_engine 1.1.0) cuts every
   loader at 2010-12-31 in a design run and stops if an input dated later reached the engine; the truncation test's
   full run is therefore sealed and its 2010-12-31 cut passes by construction (the unsealed comparison above, 24/24,
   stands in for that cut's old meaning). gm/timing.py (delay diagnostic, an existing path): days after 2010-12-31 are
   dropped and a delayed holding ends at the 2010-12-31 close at the latest; this changes only that diagnostic's
   2010-12 month for delays k > 0 (it used to read k days of January 2011).
5. gm/trials.csv rows: from the sealed engine books with gm.stats.summary, as for the gm-1.2.2 rows.
Tests: tests/run_tests.py ALL TESTS PASSED (incl. the new tests/gm_seal_smoke.py);
tests/gm_bloomberg_smoke.py PASSED; tests/bbgq_engine_smoke.py OK (packaged engine reproduces the new reference
24/24, truncation at 1995-12 PASS, curve carry only with its switch on). Logged in gm/trials.csv as family "fix" (two rows). Reference: tools/bbgq/engine_ref.json (old
one kept as engine_ref_gm-1.2.2.json). Not built here (registered for entry 2): the k = 1, tranche and daily paths and
their cut. PC engine not redeployed (pandas blocked on the PC).

## gm-1.2.2 and gm-2.0.2 candidate (registered 2026-11-22, BEFORE the code change): doubled US 2-year market removed
Found by code reading in the systematic charter (docs/research/fable/CHARTER_1.2.md section 9 item 2; confirmed by its
independent Opus check): `st_us_2y` and `bd_us_2y` are the same series (the 2-year par note priced from DGS2, less the
same US 3-month rate) wherever DGS2 exists, in monthly returns, daily volatility and every signal; `bd_us_2y` also
carries any stooq months before DGS2. So the book has 61 distinct markets, not 62, and the US 2-year note holds 2/15 of
the fixed-income block instead of 1/14 and can reach twice the per-market cap. The charter fixed the remedy before any
number: drop `st_us_2y` (the subset), keep `bd_us_2y`; registered as a design change before the run.
1. D1 gm/panel.py: "st_us_2y" leaves SHORT (the other short-end notes stay).
2. D1 gm/signals.py: "st_us_2y" leaves BD.
3. gm/variants.py, archived batch-1 variant S1 (US 3-month rate market): its signs are taken from `bd_us_2y` (the same
   series), so S1 is unchanged wherever it can be rebuilt.
No other rule, weight, threshold or cost changes. Which id goes is set by the data (the superset stays), not by results,
and is not revisited after them. Batch A1 (data swap) therefore stays a pure data swap.
Gate: the truncation test passes at all 8 cut dates for BASE and CANDIDATE on free data; tests pass; the PC engine is
redeployed and reproduces the new reference. Reported once: design-period statistics before and after (1975-2010,
1990-2010), as for C1-C4. Logged in gm/trials.csv as family "fix" (one row per config, not a selection trial). Live
paper ledger: untouched (workflow disabled); the next live run restates under the new version name. Holdout not run.
Texts that still say 62 markets (TESTING_PROTOCOL.md) are corrected at registration step 3.4.

Result (2026-11-22, free data, design months only; inputs = the PC's gm_free_inputs.zip, the same 239 files as the
gm-1.2.1 reference, which the cloud first reproduced 24/24 before the change): truncation test PASS at all 8 cut dates
(1980-06 ... 2010-12), every stage, BASE and CANDIDATE (tools/bbgq/results/engine_trunc_cloud_2026-11-22_gm-1.2.2.txt).
Net of costs, old -> new:
| Config | Period | Sharpe | Mean %/yr | Vol %/yr | Worst drawdown % |
|---|---|---|---|---|---|
| BASE gm-1.2.1 -> gm-1.2.2 | 1975-2010 | 1.236 -> 1.222 | 12.49 -> 12.34 | 10.11 -> 10.10 | -20.5 -> -19.9 |
| BASE gm-1.2.1 -> gm-1.2.2 | 1990-2010 | 1.474 -> 1.452 | 14.41 -> 14.27 | 9.77 -> 9.83 | -12.3 -> -12.5 |
| CANDIDATE gm-2.0.1 -> gm-2.0.2 | 1975-2010 | 1.464 -> 1.456 | 14.33 -> 14.27 | 9.78 -> 9.81 | -16.8 -> -16.9 |
| CANDIDATE gm-2.0.1 -> gm-2.0.2 | 1990-2010 | 1.629 -> 1.608 | 16.34 -> 16.23 | 10.03 -> 10.09 | -16.8 -> -16.9 |
Logged in gm/trials.csv as family "fix" (two rows). Reference: tools/bbgq/engine_ref.json (old one kept as
engine_ref_gm-1.2.1.json).

## gm-1.2.1 and gm-2.0.1 candidate (registered 2026-11-11, BEFORE the code change): input-layer look-ahead removed
Found by the block 3 truncation test (docs/research/bbg/BLOCK3_engine_2026-11-11.md; 8 cut dates 1980-2010, loader-level
cuts, stricter than the gm-1.2.0 audit). Signals, volatility, positions and book code are clean; four places in the
input layer read the whole sample. The fixes below are the point-in-time form of each existing rule. They were fixed
here before any number was produced and are not to be tuned after the results.
1. C1 gm/panel.py, pre-total-return dividend proxy: the yield added in month t is the mean gap between total-return
   and price-index returns over overlap months up to t only, used when more than 60 such months exist (same
   threshold), otherwise the registered constant per market. (Before total-return data exist this is the constant.)
2. C2 gm/panel.py, local-rate stand-in for equity excess returns: `gap = rl.isna() & (GRID >= 1990-01) &
   rl.notna().cummax()` (the stand-in is used only after the local rate has first appeared, decided month by month).
3. C3 gm/daily.py: the whole-sample "more than 500 days" gate is dropped (the volatility estimate already needs its
   own minimum of observations).
4. C4 Bloomberg paths (gm/panel.py commodity_return, gm/signals.py carry_values and growth_surprise, gm/bloomberg.py
   index choice): "more than 24 / 36 observations" is counted on observations up to each month; a choice between two
   series is a fixed preference order written in gm/config.py, not a comparison of sample lengths. Inactive on free data.
Gate: the truncation test passes at all 8 cut dates for BASE and CANDIDATE on free data (and the Bloomberg-input cut
on mock data). Reported once: design-period statistics before and after (1975-2010, 1990-2010). Logged in
gm/trials.csv as one fix run per config (not a selection trial). Live paper ledger: untouched; the next live run
restates under the new version name. Holdout not run.

Result (2026-11-12, gm-1.2.1 / gm-2.0.1-candidate, free data, design months only): truncation test PASS at all 8 cut
dates (1980-06 ... 2010-12), every stage (panel, daily, the four signal families, volatility, family positions,
positions, book returns) for BASE and CANDIDATE, 0 differing market-months; with Bloomberg inputs from mock workbooks
(245 tickers through the adapter) PASS at 1984-12, 1995-12 and 2007-06. Only C1 changes design numbers: 631 equity
market-months in 8 markets (eq_us_ndx 170, eq_us_r2k 152, eq_fr_cac 106, eq_br_ibov 45, eq_cn 41, eq_kr_kospi 41,
eq_in 41, eq_tw 35; 1985-02 to 2000-12), largest monthly return change 0.33 percentage points (eq_cn); C2 and C3, run
alone, change no design number; C4 is inactive on free data. Net of costs, old -> new:
| Config | Period | Sharpe | Mean %/yr | Vol %/yr | Worst drawdown % |
|---|---|---|---|---|---|
| BASE gm-1.2.0 -> gm-1.2.1 | 1975-2010 | 1.235 -> 1.236 | 12.48 -> 12.49 | 10.10 -> 10.11 | -20.5 -> -20.5 |
| BASE gm-1.2.0 -> gm-1.2.1 | 1990-2010 | 1.475 -> 1.474 | 14.40 -> 14.41 | 9.77 -> 9.77 | -12.3 -> -12.3 |
| CANDIDATE gm-2.0 -> gm-2.0.1 | 1975-2010 | 1.464 -> 1.464 | 14.32 -> 14.33 | 9.78 -> 9.78 | -16.8 -> -16.8 |
| CANDIDATE gm-2.0 -> gm-2.0.1 | 1990-2010 | 1.630 -> 1.629 | 16.34 -> 16.34 | 10.03 -> 10.03 | -16.8 -> -16.8 |
C4 preference order (gm/config.py BBG_ER_PREFERENCE): S&P GSCI before BCOM, decided by the ticker's index family only.
Logged in gm/trials.csv as family "fix" (two rows, not counted as book trials). Reference: tools/bbgq/engine_ref.json
(old one kept as engine_ref_gm-1.2.0.json).

## gm-2.0 candidate (2026-11-01, NOT frozen: waits for the Bloomberg data)
Framework rebuilt to be config-driven and statistics-driven: gm/config.py (every rule), gm/vol.py, gm/daily.py,
gm/timing.py, gm/stats.py (decade table, bootstrap, deflated Sharpe, marginal alpha), gm/trials.py (every trial
logged to gm/trials.csv with its config hash), gm/bloomberg.py (adapter; synthetic smoke test passes).
Decision rule fixed before the tests: adopt a component only if it raises net Sharpe in BOTH 1990-2010 and 1975-89.
| Trial (logged) | SR 1990-2010 | SR 1975-89 | Verdict |
|---|---|---|---|
| gm-1.2 base | 1.48 | 0.93 | reference |
| continuous vol-normalised trend | 1.43 | 0.76 | rejected |
| hybrid volatility (daily EWMA 35d + 10y, floor) | 1.58 | 1.06 | ADOPTED |
| cluster weights within class | 1.48 | 0.94 | rejected (no gain, deeper drawdown) |
| trend on spot moves only | 1.39 | 0.92 | rejected (carry inside trend helps) |
| scenario limit 3% | 1.32 | 0.93 | rejected as a rule; diagnostic |
| family shares 45/25/15/15 (trend/carry/value/econ) | 1.56 | 1.09 | ADOPTED |
| hybrid + shares = candidate | 1.63 | 1.22 | candidate |
| candidate with slow trend 6/12 / 12 | 1.43 / 1.40 | 1.03 / 1.10 | rejected |
| candidate + scenario limit 5% / 3% | 1.56 / 1.41 | 1.22 / 1.20 | rejected (drawdown/vol 1.55 vs 1.68 only) |
| risk theme credit-only (removes trend overlap) | 1.57 | 1.20 | rejected |
Trade timing (daily, price moves only, 1990-2010): 1/3/12 trend Sharpe 0.95 at k=0, 0.85 at 1 day late, 0.64 at 5,
0.61 at 10; slow 6/12 0.57 / 0.52 / 0.42 / 0.42. The fast blend beats the slow one at every delay. Rule: trade on the
first trading day after month end.
Candidate statistics 1990-2010: net SR 1.63, bootstrap 90% interval 1.26-2.02, deflated-Sharpe probability ~1.00
with 32 logged book trials (expected best of unskilled trials 0.21); every family adds (marginal alpha t: carry 4.9,
trend 3.3, value 3.1, econ 2.8); family correlations -0.16 to 0.26.
WRDS (statistics only): our yield-built US bond returns vs CRSP Treasury indexes: corr 0.985 (2y), 0.989 (5y),
0.965 (10y), 0.990 (30y); tracking error 0.6-2.1%/yr. Daily-vol study on 20 MSCI country indexes 1990-2010: daily
EWMA R2 0.46 vs 0.07 for the 36-month estimate (QLIKE 0.29 vs 0.60); blend keeps vol-scaled returns at 1.05 x target.
Holdout pass criteria changed BEFORE any holdout run (user decision 2026-11-01): net SR >= 0.3, worst fall > -25%,
corr S&P <= 0.3, 2022 positive.

## gm-1.2.0 (2026-10-31): independent look-ahead audit fixes
Audit by a separate agent (truncation test: rebuilding with data cut at 1998-06, 2003-11, 2008-09, 2010-12 gives
identical signals and positions up to each cut, apart from item 1). Verdict: no material look-ahead. Fixes:
1. Pre-ETF dividend proxy estimated on design data only (overlap up to 2010-12), not the full sample.
2. Excess returns subtract the 3m rate known at the start of the month (rate3m.shift(1)), for equities, bonds,
   notes and FX.
3. Monetary theme lags the OECD 3m-rate fallback by one month.
4. The |r| >= 60% filter was outcome-based; replaced by an explicit BAD_POINTS list plus a warning. The only large
   moves left are real (RBOB 2020-03, WTI roll 2020-05). The KRW spikes 2015-17 came from Yahoo, so FX now uses Fed
   H.10 daily first.
5. Yahoo files in cache/macro/raw are now read too, so the US equity uses SPY (1993+) and the US dividend yield exists.
6. book.main reports positions at the last complete month.
Known and documented (not fixed): hand-picked surviving universe; EM FX limited to MXN/BRL/KRW/ZAR (no TRY, RUB, THB,
IDR, ARS), which flatters carry; families dropped after design-period results; latest-vintage CPI and BIS data.
Design 1990-2010 net SR 1.47 (2x costs 1.36), maxDD -12%; 1975-89 net SR 0.93.

## gm-1.1.0 (2026-10-31)
- Econ trend: growth theme (OECD CLI, latest vintage, heavily revised) left out until first-release vintages exist.
  Themes now inflation (CPI, rarely revised), trade (BIS FX), monetary (yields), risk appetite (markets, credit spread).
  Design net effect: econ family SR 0.71 -> 0.60.
- Equity value: dividend yield (Ken French country market with minus without dividends, 1975+; US from SPY minus
  S&P 500 price, 1993+) replaces the 5-year reversal (which failed: -0.46). Design SR 0.28, corr with AQR equity-index
  value 0.51. Emerging-market equities have no value signal yet.
- Equity carry (dividend yield minus 3m rate, half directional / half cross-sectional): design SR 0.02; left out.
- Book design 1990-2010: net SR 1.55, maxDD -13%; 1975-89 net SR 0.95.

## gm-1.0.0 (2026-10-30)
- First combined book. Families: trend 30, econ 30, carry 20, value 15 (FX PPP + bond real yield), xs-momentum 5.
- Design 1990-2010 net SR 1.50; 1975-89 0.96.

## Trial log (design-period variants, all seen)
1. Price trend 1/3/12 blend and 12-month only (plumbing vs AQR).
2. Econ: five themes (v1); four themes without growth (v1.1); each theme alone (diagnostic, 5 runs).
3. Carry: half/half (chosen), directional only, cross-sectional only; equity carry half/half.
4. Value: 5-year reversal + real yield + PPP (v1); equity dividend yield (v1.1).
5. Cross-sectional momentum 12-1; value + momentum 50/50 pairing.
6. Risk scaler: credit-spread jump, cross-asset correlation jump, drawdown brake (none adopted).
7. IMF WEO forecast revisions: cross-sectional and directional, equities and bonds (exploratory, not adopted).
8. Family ablations of the book (diagnostic, 5 runs).
9. Trend lookbacks (2026-10-31, after reading Solovis "Momentum vs trend following": 6/12 months explain CTA returns
   best): 1/3/12 (kept), 3/6/12, 6/12, 12. Design 1990-2010 book net SR 1.48 / 1.35 / 1.28 / 1.27. With positions
   applied one month late, gross SR is 1.10-1.16 for every variant: the extra Sharpe of 1/3/12 is the fast part,
   which needs trading within days of month end. Rule unchanged; noted as an execution dependency.
10. Point-in-time growth theme (2026-10-31): industrial-production growth change and unemployment change as first
    published (Dallas Fed vintages 1962-98, OECD revisions editions 1999+; plus CLI editions from 2001). Design
    1990-2010, growth theme alone: PIT 0.29 vs revised CLI 0.42 (commodities 0.05 vs 0.68: the revised CLI's commodity
    result was mostly hindsight). Econ with PIT growth 0.64 vs 0.59 without; 1975-89 0.24 vs 0.37. Book net SR
    1990-2010 1.47 either way; 1975-89 0.84 vs 0.93. Not adopted (GROWTH_PIT stays False).
Total: about 37 variants before the trial log; 32 book-level trials in gm/trials.csv since (2026-11-01).

## 2026-11-01: statistical adoption protocol (docs/research/global_macro/TESTING_PROTOCOL.md)
Replaces "raise net Sharpe in both eras" with a pre-registered test: paired stationary bootstrap of the Sharpe
difference (Holm across each batch, p < 0.05), dSR >= 0.05, non-inferiority per era (95% lower bound > -0.10;
eras without new data identical), dSR > 0 at 2x costs, tail checks. Code gm/protocol.py, gm/variants.py, gm/stats.py.
- Batch 0 (re-test of gm-2.0 adoptions): hybrid vol dSR +0.12 (Holm p 0.004) PASS; family shares 45/25/15/15
  dSR +0.11 (p 0.037) PASS. gm-2.0 candidate unchanged.
- Batch 1 (free data): all rejected. Econ theme x class blocks -0.01; US 3m short-rate market -0.02; bond value
  composite +0.00; FX value skip 12m +0.01 (p 0.17); bond carry per duration +0.00.
- Diagnostics (protocol_diagnostics.md): trend family SR 1.22 vs AQR TSMOM 1.34 (corr 0.66) on 1990-2010, so the
  trend leg is not inflated; book Lo-adjusted SR 1.49 / 1.32; no single market or 2008 drives the result
  (1.35-1.48 with any top market removed; 1.44 without 2008). 1987 loss came from trend long equities (-6.4%) and
  short bonds (-2.1%).

## 2026-11-02: statistical audit (gm/audit.py -> docs/research/global_macro/stats_audit_2026-11-02.md)
- Bootstrap: gm-2.0 1975-2010 SR 1.46, 90% interval 1.17-1.79, stable for mean blocks 3-24 months; batch-0 p-values
  stable across block lengths.
- Selection inflation among 32 logged variants (sd 0.11): about 0.23 Sharpe (0.28-0.31 if 100-300 variants).
  Deflated Sharpe is 1.000 at every trial count, so it is uninformative here and is no longer cited as evidence.
- CSCV over 20 rebuildable variants: PBO 0.04 (in-sample winner 1.50 -> 1.45 out of sample).
- Holdout power (block bootstrap, 189 months): pass-all probability 0.04 if true SR 0, 0.22 at 0.3, 0.41 at 0.5,
  0.66 at 0.8; the -25% max-fall criterion is the binding one (61% at SR 0.5).
- EM currencies and equities removed before 2000: 1990-2010 SR 1.63 -> 1.51; 1975-2010 1.46 -> 1.43.
- Trial log fix: batch rows had the pooled 1975-2010 SR in the 1990-2010 column and signal-only challengers
  shared the incumbent's hash; corrected (era columns recomputed, fingerprint includes the challenger name).
