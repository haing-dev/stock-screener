# S4 rebuild: spec readings (TESTING_PROTOCOL 7.6 step 6, check S4; WORKFLOW 4.5)

Written 2026-11-27 by the independent rebuilder (Opus 5.5, effort high, a separate agent). Code:
`tools/bbgq/lib/rebuild_s4.py`. Synthetic self-test: `tests/rebuild_s4_selftest.py` (not in run_tests; the builder
decides that). Interface followed: `docs/research/batches/S4_INTERFACE.md` **v2** (raw inputs).

- **1.0.0**: built on interface v1. Not accepted: the independent check found M1, and interface v2 widened S4.
- **1.1.0** (this file):
  - M1 fixed: only Trend's score is clipped (N16).
  - The carry measure, the value measure and the hybrid volatility are now derived from the spec text (N17-N23).
  - The registered gap rule of SPEC_Trend s3 is followed (N2, N24).

## 0. What was read and what was not

**Read:**
- SPEC_Trend, SPEC_Carry and SPEC_Value, whole files, including SPEC_Trend s3's amendment of 2026-11-27.
- SPEC_Economic_trend s0-s3, for context only.
- TESTING_PROTOCOL 7.2, 7.3, 7.4 and 7.6; WORKFLOW 4.5.
- gm/CHANGES.md rule text of: gm-2.2.1, X1 outcome (E13), the gm-2.1.0 feature version (E6-E11 and its "closed here"
  items), gm-1.2.3 (E1-E5) and the gm-2.0 candidate.
- The input layer, for data formats only: gm/panel.py, gm/daily.py, gm/seal.py, tools/bbgq/lib/a1_panel.py.
- S4_INTERFACE v1 and v2.

**Not read, grepped or imported:**
- gm/signals.py, gm/book.py, gm/vol.py, gm/execution.py, gm/config.py.
- tools/bbgq/lib/a2_batch.py, diag_a2.py and core_v1.py, and their tests.
- engine_ref*.json, tools/bbgq/results/*, gm/trials.csv.

**Disclosure:** the gm/CHANGES.md entries read for rule text contain result tables of WHOLE-BOOK statistics (BASE and
CANDIDATE net Sharpe, mean, vol, drawdown), and CLAUDE.md repeats some of them. I saw them in passing. I saw no
per-part engine figure, tuned nothing to any number, and computed no statistic of real data.

**Runs:** none on real or free data. Building the free raw inputs needs gm/panel.py and gm/daily.py, which import
gm/config.py and gm/signals.py, both off limits. Only synthetic data was used (the self-test).

## 1. What interface v2 fixes (taken as given)

- **Raw inputs:**
  - R (A1 panel excess returns) and D (daily: log returns, price returns for bd_/st_).
  - days (NYSE calendar).
  - rate3m (percent a year, unlagged monthly averages) and fx_rate_country.
  - eia (contracts 1 and 2 at month-end).
  - Ken French returns with and without dividends; SPY total and ^GSPC price returns.
  - cost, em_borrow and classes.
- **Part definitions:**
  - `trend`: every class, in the A2-final single form (the mean sign of the 1-, 3- and 12-month returns). A2 failed,
    so there is no 16-version grid.
  - `carry`: FX v2, CM v1 and CM v2 as ONE part.
  - `value_eq`: Value equities (version 1; version 2's equity leg is identical).
  - The two Carry legs alone, reported only.
- **Bloomberg switches are off** (E1): nothing to apply.

## 2. Readings the rebuild made (each an open point of the written rules; the plain reading, not tuned)

| # | Point | Reading | Source of the rule |
|---|---|---|---|
| N1 | Trend score when a lookback has no value yet (first 12 months of a market) | No score unless all three of the 1-, 3- and 12-month compounded returns exist; the score is their plain mean. Alternative: the mean of the signs available. Effect: about one month per market at its start | SPEC_Trend s3 "score = mean over h in (1, 3, 12) of sign(...)"; step 2 "no value if lvl(t-h) is missing" |
| N2 | Level at interior gap months (REGISTERED since 1.0.0) | 1.1.0 follows the SPEC_Trend s3 amendment of 2026-11-27 (S4_INTERFACE v2 s2a item 7). lvl = cumulative product of (1 + R) with a gap month adding 0. It exists from the market's first return onward, so lvl(t) = lvl(t-1) at a gap and the score is computed there like any other month. 1.0.0 had made lvl missing at gap months. The amendment was written with sight of the engine, so S4 does not test this point | SPEC_Trend s3 amendment; CHANGES "Core book v1" |
| N3 | Sign of exactly 0 | 0 for Trend and Carry v1 | SPEC_Trend s3 step 2; SPEC_Carry s3 |
| N4 | What "lagged" means for the block, part and book scalers | k(t) = target / (36-month realised vol of the scaled series' own returns up to and including month t, at least 24 months, x sqrt(12)). k(t) multiplies the position decided at month-end t, so month t+1 earns r(t+1) x k(t). Vol = pandas rolling std, ddof 1, NaN months skipped inside the 36-month window. The returns the scalers read are the k = 0 panel returns of the held position | SPEC_Trend s5; TESTING_PROTOCOL 7.4 E9; CHANGES gm-2.1.0 closed items 2 and 5 ("r_b(t) x k_b(t-1)") |
| N5 | Book scaler input and cap | The book scaler reads the part's scaled return before the book scaler, caps and costs: r_part(t) x k_part(t-1) / n, with n = 1. Target 0.10, no multiplier cap. Block and part multipliers are capped at 50 | SPEC_Trend s5; CHANGES gm-2.1.0 closed item 5 |
| N6 | cs_rank details | Ties take the average rank. The ranked set is the class's markets with a measure value that month, whether or not they have a vol. Weights = demeaned ranks scaled to sum abs = 1, times the count. No weights if fewer than 3 markets or all ranks are equal | SPEC_Carry s3 step 5; SPEC_Value s3 step 6 |
| N7 | Missing vol; per-market cap | A market without a vol (or with vol 0) has no position. The cap 0.10 x 0.10 x 3 / vol is applied after the book scaler. Then the 5x gross cap scales every position of the month by 5 / gross when gross > 5 | SPEC_Trend s5 |
| N8 | Cost timing | The cost of the position decided at month-end t is charged in month t+1, the month that holding earns. It is: one-way bp x abs change from the previous decision, plus rolls 2 x one-way bp x rolls / 12 x abs new position, plus 1%/yr / 12 on short positions of em_borrow markets. The first position is a change from 0. So the never-traded decision of 2010-12 is never charged | SPEC_Trend s9; interface s2 "cost"; 7.3 item 2; CHANGES gm-1.2.3 closed item 4 |
| N9 | Version average inside a part | Pod position = sum of version positions / number of versions, a missing version counting as 0; no position where no version has one. The Carry FX Core block is p_v2 / 2 (its term of the two-version average); the CM block is (p_v1 + p_v2) / 2. The halves wash out in the unit-vol block scaler, except near its multiplier cap | SPEC_Carry s3; CHANGES gm-2.1.0 closed items 3 and 5 |
| N10 | Class count n | n = markets of the class with a position that month, counted per version | SPEC_Trend s3 step 5; CHANGES gm-2.1.0 closed item 3 |
| N11 | Market sets | Trend: every R column whose id starts with a class prefix (sp_* are never held; cm_aqr_ew falls in CM only). Carry FX: the markets of fx_rate_country. Carry CM: cm_wti, cm_natgas, cm_heatoil, cm_gasoline. Value: the 8 indexes of SPEC_Value s4. A measure counts only for a market that is a column of R | SPEC_Trend s4; SPEC_Carry s4; SPEC_Value s4; gm-2.2.1 (interface v2 s2a item 6) |
| N12 | k = 1 return details | A day's price return = D's value for bd_/st_ (already a price return), exp(log return) - 1 otherwise. A needed day without a value, or a month without a calendar day (before the calendar starts), earns the k = 0 return and is flagged. Holding cut: where the first NYSE day of the next month lies after the cut or after the calendar, the return is R(t) - price return of the first day of t, not flagged | 7.3 items 2 and 5; CHANGES E6 |
| N13 | Which months a series reports | Month t has a net return when a non-zero position was held from month-end t-1 (after all scalers and caps); months before that are NaN. A held market with no earned return contributes 0 that month, but its cost still counts | Interface s1 |
| N14 | Sample start | The rebuild runs every month the inputs hold (1960-01 on), so scalers warm up before 1975; the job applies the 1975-01..2010-12 window. "Design positions start no earlier than 1975-01" (SPEC_Trend s4) is read as the evaluation window | SPEC_Trend s4, s7; interface s4 |
| N15 | Seal and cut | Every raw input is cut at `cut` BEFORE any measure is computed: monthly frames up to the cut's month; daily frames and the calendar up to its close. The output is checked to hold nothing after the cut's month. Under k = 1 the decision of the cut month earns nothing | 7.3 item 5; gm/seal.py conventions |
| N16 | (M1, fixed in 1.1.0) Clipping | Only Trend's score is clipped to [-1, 1] (SPEC_Trend s3 lines 49 and 62). Carry v1 signs and the cs_rank weights of Carry v2 (FX and energy) and Value equities enter as p = w x 0.40 / vol with no clip (SPEC_Carry s3 lines 50-52; SPEC_Value s3 line 58). A rank weight can reach about 1.5 (3 markets) to almost 2 (many markets). 1.0.0 clipped them, which shrank the extreme ranks | as stated |
| N17 | Currency carry | C_fx(t) = (rate3m[local](t-1) - rate3m["US"](t-1)) / 100, decimal a year. "Lagged 1 month" = the rates of month t-1 at month-end t. Missing if either rate is missing. No further carry-forward beyond the loader's 12 months | SPEC_Carry s3 step 2; interface v2 s2a item 1 |
| N18 | Energy carry | C(t) = 12 x (F1(t) / F2(t) - 1), with F1, F2 = contracts 1 and 2 at month-end t. Missing where F1 is missing or F2 is not positive | SPEC_Carry s3 step 3; interface v2 s2a item 2 |
| N19 | E13 (natgas, gasoline only) | d(t) = C(t) - mean(C over the 12 month-ends up to and including t), all 12 present. Adjusted C(t) = C(t) - mean of d over all EARLIER same-calendar month-ends that have a d (strictly before t, at least 5 values). Missing where C or that mean is missing. A missing d in an earlier year is skipped, not counted. Both Carry versions read the adjusted value | SPEC_Carry s3; CHANGES "X1 outcome" closed item 3; interface v2 s2a item 3 |
| N20 | Equity dividend yield | Seven countries: the 12-month sum of (French with - without dividends), all 12 months needed; the value used at t is the sum ending at t-12 (E4), with no carry-forward and NO clip (the spec writes the clip for the US only). US: the 12-month sum of (SPY total - ^GSPC price), all 12 needed, clipped to [0, 0.10], at t with no lag. SPY's first return is 1993-02, so the first US value is 1994-01; SPEC_Value s4 says "US 1993-12", the one-month difference follows from "all 12 needed" | SPEC_Value s3 item 1; 7.4 E4; CHANGES gm-1.2.3 closed item 3; interface v2 s2a item 4 |
| N21 | Daily annualisation | Daily variance x 252 (trading days a year). The spec says only "annualised". D's rows are about 261 weekdays a year; using 261 would raise the daily fast estimate by 1.8% | SPEC_Trend s3 step 4; interface v2 s2a item 5 |
| N22 | "Where free daily data exist" and sampling | The daily fast estimate is used at month-end t when the market is a column of D and its EWMA has at least 40 daily values up to the month's last calendar day; else the monthly EWMA. It is read at the last D row at or before that day. A market whose daily values stop keeps its last estimate (pandas carries it), with no staleness rule | SPEC_Trend s3 step 4; interface v2 s2 "D", s2a item 5 |
| N23 | EWMA conventions | EWMA of SQUARED returns, no mean removed, pandas ewm(halflife, min_periods) with adjust=True and ignore_na=False. Half-lives run on each input's own time axis: D's rows for "35 days", R's months for "6 months". min_periods counts values present (40 days, 12 months). Slow = rolling 120-month std (ddof 1, demeaned), at least 36 values. m36 = rolling 36-month std, at least 12. hybrid = max(0.7 fast + 0.3 slow, 0.75 slow) where both exist; fast alone until slow exists; m36 where neither exists. D's bond/note values are used as given (price returns) | SPEC_Trend s3 step 4; interface v2 s2a item 5 |
| N24 | Gap rule after a market's LAST return | Read literally ("lvl is missing only before the market's first return"), the level also continues flat after a series ends. This matters for cm_aqr_ew after 2000-12: for up to 11 months the 12-month sign stays non-zero (score +-1/3), then the score is 0 for good. Where vol still exists (the carried EWMA, the 120-month slow), it holds a small Trend position in 2001 earning 0 (costs only), then a 0 position | SPEC_Trend s3 amendment |
| N25 | Zero positions in the class count | A position of exactly 0 (score 0 with a vol) is "a position" and counts in n. Together with N24 this adds cm_aqr_ew to the CM count after 2001. The unit-vol block scaler mostly removes the effect | SPEC_Trend s3 step 5 "count of markets in its class with a p_v" |

## 3. Ambiguities that may matter for the 15% match (largest first)

1. **N23 and N21, the vol model's conventions.** These set every position size and every cap, so they move both Sharpe
   and mean, mainly through the per-market cap and through what share of the mixture is fast versus slow. The
   open points are:
   - the time axis of the EWMAs (rows versus days with a value: ignore_na);
   - adjust=True versus a recursive EWMA (it matters early in a series);
   - the daily annualisation (252 versus 261);
   - no demeaning in the EWMAs versus a demeaned slow std;
   - staleness of a stopped daily series (N22).
2. **N4 and N5, the scaler conventions.** These are:
   - how missing months count inside the 36-month window;
   - ddof;
   - which return the book scaler reads;
   - whether the book multiplier is capped.

   They set each part's realised volatility level, so mostly the annualised MEAN; Sharpe is less sensitive.
3. **N8, cost timing and the roll base.**
4. **N16 (fixed) and N6, the rank details.** Not clipping matters most for the 3-market energy rank and the 8-market
   equity rank. Ranked-set membership (signal versus signal plus vol) matters only at market starts.
5. **N20, the dividend-yield details** (no clip outside the US; the US start in 1994-01), and **N17, the rate lag**.
   The job's raw check (interface v2 s3 item 0) shows that the raw inputs reproduce the engine's measures. It does not
   check this rebuild's formulas.
6. **N1 and N24/N25**: about one month per market at the start, and cm_aqr_ew in 2001.

## 4. Underspecified in the written specs (what is missing)

- **The hybrid vol model (SPEC_Trend s3 step 4)** does not state:
  - the daily annualisation factor;
  - the EWMA form (adjusted or recursive; on a calendar of rows or of values);
  - whether squared returns are demeaned;
  - how "where free daily data exist" is decided month by month (and what happens to a series that stops);
  - whether the slow standard deviation is ddof 1.

  It is buildable only by taking the plain readings N21-N23.
- **The scalers:** no spec writes the estimator details (missing months inside the window, ddof, whether "lagged"
  means returns to t or to t-1). Only CHANGES gm-2.1.0 closed item 5 pins the r_b(t) x k_b(t-1) pairing. The
  book-scaler input and any book multiplier cap are not written.
- **Cost timing** (the month a trade's cost is charged in) is not in the specs. It is implied only by "costs are
  charged as today" (7.3 item 2) and CHANGES gm-1.2.3 closed item 4.
- **EM_EQ** (5 bp, borrow) is named but not listed in the specs. The interface supplies em_borrow and the bp table.
- **The gap rule (N2/N24)** is registered for interior gaps, but whether it also runs past a market's last return is
  not said. "Missing only before the first return", read literally, says it does.
- **Trend's A2-final form** (the mean of the 1/3/12 signs) is described only in SPEC_Trend s3 "Code now". Its rule for
  a missing lookback is not stated (N1).

## 5. Self-test (synthetic data only, no statistic of real data)

`python3 tests/rebuild_s4_selftest.py` runs 85 checks and prints "REBUILD_S4 SELFTEST PASSED". It covers:

- **Interface shape rules** (s1, s3).
- **Seal:**
  - raw inputs after 2010-12-31, monthly and daily, change nothing;
  - pre-cut inputs give the same output;
  - the 2010-12 holding cut;
  - truncation at 1990-06, 1998-06 and 2003-11 equals the full run before the cut month.
- **No look-ahead:** changing every raw monthly input from t0, and D after t0's first day, leaves positions, returns
  and the derived carry, value and vol measures before t0 unchanged. Controls show that the change bites.
- **M1:** rank weights of 1.5 survive in hand cases and in the build; Trend's sizing clips.
- **Hand cases:**
  - currency carry lag; energy carry and its missing rules;
  - E13 (removes a pure calendar pattern, first value 5 years and 12 months in, point in time, natgas only);
  - dividend yield (E4 lag 12, missing-month handling, US clip at 0.10 and at 0, no US lag);
  - hybrid vol (daily fast, monthly fallback, the blend with slow, start dates, point in time);
  - the gap rule (a flat level at a gap; missing only before the first return; scores after the gap; cm_aqr_ew after
    2000-12);
  - cs_rank, trend score, the k = 1 return (log versus price, missing price, flags, holding cut, pre-calendar months),
    costs and the scaler.
- **Signs:** Trend, Carry v2, Value.
- **Class rules:** cm_aqr_ew in CM only, sp_* never held, Value's 8 markets.
- **Caps; cost multiple.**
- **Import rule:** numpy and pandas only; no file, network or environment access.
