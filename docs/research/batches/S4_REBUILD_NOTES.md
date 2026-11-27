# S4 rebuild: spec readings (TESTING_PROTOCOL 7.6 step 6, check S4; WORKFLOW 4.5)

Written 2026-11-27 by the independent rebuilder (Opus 5.5, effort high, a separate agent). Code:
`tools/bbgq/lib/rebuild_s4.py` (rebuild_s4-1.0.0); synthetic self-test `tests/rebuild_s4_selftest.py` (not in
run_tests; the builder decides). Interface followed: `docs/research/batches/S4_INTERFACE.md`.

## 0. What was read and what was not

Read: SPEC_Trend, SPEC_Carry, SPEC_Value (whole files), SPEC_Economic_trend s0-s3 (context only); TESTING_PROTOCOL
7.2, 7.3, 7.4, 7.6; WORKFLOW 4.5; gm/CHANGES.md rule text of gm-2.2.1, X1 outcome (E13), gm-2.1.0 feature version
(E6-E11 and its "closed here" items), gm-1.2.3 (E1-E5), gm-2.0 candidate; the input layer gm/panel.py, gm/daily.py,
gm/seal.py, tools/bbgq/lib/a1_panel.py (data formats only); S4_INTERFACE.md.

Not read, grepped or imported: gm/signals.py, gm/book.py, gm/vol.py, gm/execution.py, gm/config.py,
tools/bbgq/lib/a2_batch.py, diag_a2.py, core_v1.py, their tests, engine_ref*.json, tools/bbgq/results/*,
gm/trials.csv. Disclosure: the gm/CHANGES.md entries read for rule text carry result tables of WHOLE-BOOK statistics
(BASE and CANDIDATE net Sharpe, mean, vol, drawdown), and CLAUDE.md repeats some; they were seen in passing. No
per-part engine figure was seen, nothing was tuned to any number, and no statistic of real data was computed here.

No run on real or free data was made: building the free inputs C, V and vol needs gm/signals.py and gm/vol.py, and
gm/panel.py / gm/daily.py import gm/config.py and gm/signals.py, all of which are off limits. Only synthetic data was
used (self-test).

## 1. What the interface fixes (taken as given, not re-derived)

- `vol` (the A2-final hybrid estimate) is used as given for every w x 0.40 / vol sizing and for the per-market cap.
- `C` already holds the E13 seasonal adjustment for cm_natgas and cm_gasoline; `V` already holds E4's lag 12 for the
  7 non-US equity dividend yields. The rebuild applies neither again.
- `cost` and `em_borrow` give the cost table and the borrow markets; `days` the NYSE calendar.
- Part definitions: `trend` = every class, A2-final single form (mean sign of 1-, 3-, 12-month returns: A2 failed, so
  no 16-version grid); `carry` = FX v2 + CM v1 + CM v2 as ONE part; `value_eq` = Value equities (version 1 only in
  the A2-final book; version 2's equity leg is identical anyway, SPEC_Value s3); plus the two Carry legs alone.

## 2. Readings the rebuild made (each an open point of the written rules; the plain reading, not tuned)

| # | Point | Reading | Source of the rule |
|---|---|---|---|
| N1 | Trend score when one lookback has no value yet (first 12 months of a market) | No score (and so no position) unless all three of the 1-, 3- and 12-month compounded returns exist; the score is their plain mean. Alternative: mean of the signs available. Effect: about one month per market at its start | SPEC_Trend s3 "score = mean over h in (1, 3, 12) of sign(...)"; step 2 "no value if lvl(t-h) is missing" |
| N2 | Compounded level with interior gaps | lvl = cumulative product of (1 + R) with gaps as 0, kept only at months where R exists; lvl(t-h) at a gap month is missing (no sign for that lookback) | SPEC_Trend s3 "gaps as 0 where data exist" |
| N3 | Sign of exactly 0 | 0 (no position contribution) for Trend and Carry v1 | SPEC_Trend s3 step 2, SPEC_Carry s3 |
| N4 | What "lagged" means for the block, part and book scalers | k(t) = target / (36-month realised volatility of the scaled series' own returns up to and including month t, at least 24 months, x sqrt(12)); k(t) multiplies the position decided at month-end t, so the return of month t+1 is r(t+1) x k(t). Volatility: pandas rolling std, ddof 1, NaN months skipped inside the 36-month window. Returns that scalers read = k = 0 panel returns of the held position (CHANGES gm-2.1.0 closed item 2) | SPEC_Trend s5; TESTING_PROTOCOL 7.4 E9; CHANGES gm-2.1.0 closed item 5 ("r_b(t) x k_b(t-1)") |
| N5 | Book scaler input and cap | Book scaler reads the part's scaled return before the book scaler, caps and costs (r_part(t) x k_part(t-1) / n, n = 1); target 0.10; no multiplier cap (the cap of 50 is written for blocks and parts only). Block and part multipliers capped at 50 | SPEC_Trend s5; CHANGES gm-2.1.0 closed item 5 |
| N6 | cs_rank details | Average rank for ties; ranked set = markets of the class with a signal value that month (whether or not they have a vol); weights = demeaned ranks scaled to sum abs = 1, times the count; no weights if fewer than 3 markets or all ranks equal | SPEC_Carry s3 step 5; SPEC_Value s3 step 6 |
| N7 | Missing vol; per-market cap | A market without a vol (or with vol 0) has no position and is not counted in n. The cap 0.10 x 0.10 x 3 / vol is applied after the book scaler; then the 5x gross cap scales every position of the month by 5 / gross when gross > 5 | SPEC_Trend s5 |
| N8 | Cost timing | The cost of the position decided at month-end t (one-way bp x abs change from the previous decision, plus rolls 2 x one-way bp x rolls / 12 x abs position, plus 1%/yr / 12 on short positions of em_borrow markets) is charged in month t+1, the month that holding earns; the first position is a change from 0. Hence the never-traded decision of 2010-12 is not charged (CHANGES gm-1.2.3 closed item 4) | SPEC_Trend s9; S4_INTERFACE s2 "cost"; 7.3 item 2 "Costs are charged as today" |
| N9 | Version average inside a part | Pod position = sum of version positions / number of versions, a missing version as 0; no position where no version has one. Carry FX Core block = p_v2 / 2 (its term of the two-version average); CM block = (p_v1 + p_v2) / 2. The halves wash out in the unit-volatility block scaler except near its multiplier cap | SPEC_Carry s3; CHANGES gm-2.1.0 closed items 3, 5 |
| N10 | Class count n | n = markets of that class with a position that month, counted per version (Carry v1 and v2 separately) | SPEC_Trend s3 step 5; CHANGES gm-2.1.0 closed item 3 |
| N11 | Market sets | Trend: every R column whose id starts with a class prefix of `inputs["classes"]` (so sp_* are never held; cm_aqr_ew falls in CM only, to 2000-12 by its data). Carry FX: the fx_ columns of C; Carry CM: cm_wti, cm_natgas, cm_heatoil, cm_gasoline (SPEC_Carry s4). Value: the 8 equity indexes of SPEC_Value s4, intersected with V's columns (other eq_ columns in V, if any, ignored) | SPEC_Trend s4; SPEC_Carry s4; SPEC_Value s4; gm-2.2.1 |
| N12 | k = 1 return details | As 7.3 item 2 and CHANGES gm-2.1.0 closed item 2: price return of a day = the daily value for bd_/st_ (already a price return), exp(log return) - 1 otherwise; a needed day without a value (or a month without a calendar day, before 1970) -> k = 0 return, flagged; holding cut: where the first NYSE day of the next month lies after the cut or after the calendar, return = R(t) - price return of the first day of t, not flagged. Flags are kept internally (not reported by part_returns) | 7.3 items 2 and 5; CHANGES E6 |
| N13 | Which months a series reports | A net return exists in month t when a non-zero position was held from month-end t-1 (after all scalers, caps); months before that are NaN. A held position whose market has no earned return contributes 0 that month (the cost still counts) | S4_INTERFACE s1 ("NaN in months without a net return") |
| N14 | Sample start | The rebuild runs every month the inputs hold (1960-01 on), so scalers warm up on pre-1975 months; the 1975-01 to 2010-12 window is applied by the job. "Design positions start no earlier than 1975-01" (SPEC_Trend s4) is read as the evaluation window, not as zero positions before 1975 | SPEC_Trend s4, s7; S4_INTERFACE s4 |
| N15 | Seal and cut | Every input is cut at `cut` (monthly: months up to the cut's month; daily and calendar: days up to its close) before use; the output is checked to hold nothing after the cut's month; under k = 1 the decision of the cut month earns nothing | 7.3 item 5; gm/seal.py conventions |

## 3. Ambiguities that may matter for the 15% match (in order of likely size)

1. N4 / N5 scaler conventions (window counted in calendar months with NaNs skipped vs in active months only;
   std ddof; which return the book scaler reads; whether the book multiplier is capped). These set the level of every
   part's volatility and therefore its annualised mean; Sharpe is less sensitive.
2. N8 cost timing (same month vs next month) and whether the roll charge uses the held or the new position.
3. N6 ranked set for cs_rank (markets with a signal vs markets with a signal AND a vol / return).
4. N1 (one month per market) and N13 (months counted).

## 4. Underspecified in the written specs (what is missing)

- The scalers' exact volatility estimator (ddof, how missing months inside the 36-month window count, whether
  "lagged" means returns to t or to t-1) is not written in any spec; only CHANGES gm-2.1.0 closed item 5 pins the
  r_b(t) x k_b(t-1) pairing. Book-scaler input and any book multiplier cap: not written.
- Cost timing (which month a trade's cost is charged in) is not in the specs; only "costs are charged as today"
  (7.3 item 2) and CHANGES gm-1.2.3 closed item 4 imply next-month charging.
- EM equity set for the 5 bp / borrow rule: the specs name "EM_EQ" without listing it (here supplied by the interface
  as `em_borrow`; the bp table also comes from the interface).
- The hybrid volatility model (daily annualisation factor, EWMA adjust convention, how "where daily data exist" is
  decided, staleness) is not fully written in SPEC_Trend s3 step 4; S4 sidesteps this because the interface passes
  `vol` as a shared input. A rebuild of the vol model from the spec alone would need these points fixed.
- The carry and value measures (rate lags, CPI carry-forward, dividend-yield construction) are passed in C and V;
  they were not rebuilt here, so S4 does not test them.
- Trend's CANDIDATE form (the A2-final 1/3/12 mean of signs) is described in SPEC_Trend s3 "Code now" only; its
  rule for a missing lookback is not stated (N1).

## 5. Self-test (synthetic data only, no statistic of real data)

`python3 tests/rebuild_s4_selftest.py` -> 61 checks, "REBUILD_S4 SELFTEST PASSED": interface shape rules of
S4_INTERFACE s3; seal (inputs after 2010-12-31 change nothing; pre-cut inputs give the same output; holding cut of
2010-12); truncation at 1990-06, 1998-06, 2003-11 equal to the full run before the cut month; no look-ahead (changing
month t0 and later leaves positions and returns before t0 unchanged; control shows the change bites); hand cases of
cs_rank, trend score, k = 1 return (log vs price, missing price, flags, holding cut, pre-calendar months), costs,
scaler; signs (Trend, Carry v2, Value); class rules (cm_aqr_ew CM only, sp_* never held, Value's 8 markets); caps;
cost multiple; import rule (numpy and pandas only; no file, network or environment access).
