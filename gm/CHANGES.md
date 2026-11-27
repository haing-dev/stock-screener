# Global Macro Book: rule changes and trial log

Every rule change gets a new VERSION in gm/run.py and a line here. Every variant tested on the design period
(1990-2010; extra check 1975-89) is logged so the deflated Sharpe can count the trials. The holdout (2011-2026) is run
once, after the rules are frozen, by gm/holdout.py.

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
