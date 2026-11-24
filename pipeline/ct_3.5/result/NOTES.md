# Planter notes, step 3.5 checker test (2026-11-24)

Do not show to checkers. Key: KEY.json. Assignment: ASSIGN.json. Working files (calibration scripts, fixed
variants of every defective case, saved outputs): planter/work/ (fix/Cxx_fixed.py = the case with only the defect
removed; out_Cxx.txt = the case output the report was written from).

## Generator
cases/_lib/synth.py, make_panel(seed=20261124), deterministic, runs in < 0.1 s. 32 markets (EQ 8, FI 8 incl. two
2-year notes, FX 8, CM 8), monthly 1970-01..2015-12, late starts (fx_eur 1999, cm_natgas 1990-04, cm_brent 1988-07,
cm_wti 1983-04, st_de2 1991, eq_kr 1990, ...). Returns = drift + vol regime x (class factor + idiosyncratic), t(4)
and t(5) tails, dated shocks (1987-10, 2008-10, 1994 bonds, ...). Drift = persistent trend state (stronger before
1993), carry known at the previous close, value mean reversion to an unknown anchor, bond/equity reaction to the
CPI print of the previous reference month (published during the month), FX carry unwinds on fixed dates. Ten pairs
share most of their risk with a fast mean-reverting spread (8 cross-market + two 2y/10y curves). CARRY, VALUE are
observed at the close of t; MACRO us_cpi is indexed by reference month with a one-month publication lag
(documented in the docstring). The generator itself uses whole-sample normalisation of its own vol regime; that is
part of the synthetic world, not a strategy input.

## Case ids
Built under internal keys k01..k20, mapped to C01..C20 by random.Random(3520261124).shuffle:
k01 C13, k02 C03, k03 C07, k04 C02, k05 C06, k06 C11, k07 C18, k08 C17, k09 C16, k10 C04 (clean);
k11 C08, k12 C12 (look-ahead), k13 C19, k14 C01 (sample), k15 C09, k16 C10 (costs), k17 C14, k18 C05
(period-selection), k19 C20, k20 C15 (tuned-knob).

## How each defect was built (one change each; the fixed variant differs by that line only)
- C08 look-ahead: rule reads np.log(cpi) instead of the latest published value (cpi.shift(1)). Spec 2.1 states the
  lag. The synthetic bonds react in month t+1 to the reference-month-t print, so the error is a direct peek.
  0.23 -> -0.18 (sign change).
- C12 look-ahead: "standardise" uses each market's full-sample mean and sd (1970-2015) instead of the registered
  expanding as-of z-score. 0.74 -> 0.20. Clean twin C07 (different classes, expanding mean, min 60).
- C19 sample: R.dropna(how="any") on the 8 commodities silently starts the run in 1990-04; the code prints the
  configured window labels, not the months used; report repeats "1975-01..2010-12". Tell: era 1975-1992 vol 3.21%.
  0.94 -> 0.39.
- C01 sample: months where any panel market moves > 6 trailing sds are removed from the result ("usable_months",
  22 months incl. unwinds/crashes). Code and report say 410 months; spec registers 432. 0.87 -> 0.62. (A start-date
  move was tried first, best plausible shift gave only +0.10, so the month filter was used instead.)
- C09 costs: cost on the change of the pair's risk units times (bp_a + bp_b) instead of each leg's notional change
  (units / vol). 1.09 -> 0.92; costs 0.17 -> 1.29 %/yr. Clean twin C06 charges each leg correctly.
- C10 costs: ONE_WAY = 1.0e-5 where the spec registers 1 bp (trades and quarterly rolls on the large 2-year leg).
  0.41 -> 0.11; at 2x costs 0.38 -> -0.21. (An "entries only" bug was tried first: effect 0.08, too small.)
- C14 period-selection: code prints the full window and both eras honestly; the report's headline is the
  1993-2010 era (0.71) with an argument that the early era is less relevant; registered headline 0.43.
- C05 period-selection (market subset): code prints the registered FI+FX+CM pod and, as a diagnostic, FX+CM; the
  report leads with "core carry (currencies + commodities)" 0.53; registered headline 0.22.
- C15 tuned-knob: spec leaves window and gap to the code; (6, 1) is the best of a window 1-12 x gap 0-2 grid
  (grid median 0.15; gap 0 -> 0.11, gap 2 -> 0.24). Report silent. Clean twin of the family: C04 (bonds, 12-1
  registered).
- C20 tuned-knob: spec leaves LOOK to the code; LOOK = 2 is the best of 1-12 (median 0.095; 1 -> 0.10, 3 -> 0.24,
  12 -> 0.01). Report silent.
Each effect was measured by running the fixed variant (planter/work/fix) or the grid scripts (work/grid15.py,
work/grid20.py). All are >= 0.15 Sharpe against the registered/neutral value.

## How the clean cases were verified (line by line)
For each of C02, C03, C04, C06, C07, C11, C13, C16, C17, C18 I checked:
1. Timing: every signal, vol and count uses data up to the close of t (rolling/expanding/ewm windows that include t;
   CPI shifted one month in C02); positions are shifted one month before multiplying returns (or pos[t-1] @ R[t] in
   the numpy cases); no shift(-1), no full-sample mean/sd/rank anywhere in a signal or size.
2. Costs: one-way bp per class on |change of notional| (C06: each leg; C16: pod position after averaging, as its
   spec says), charged in the month after the trade; the class table matches the spec (C18 natgas 6 bp registered);
   net = gross - costs and the 2x-cost line doubles only costs.
3. Sample: result series sliced to 1975-01..2010-12 on return months; each prints 432 months; eras 1975-1992 and
   1993-2010; no rows dropped (markets before their start get zero position, not dropped rows).
4. Knobs: every number in the code (lookbacks, vol windows and minimums, clip, risk, thresholds, min markets) is
   written in the spec; no value was chosen by looking at results (values set before running: 12, 36/24, 20%,
   1/3/12, half-life 6 etc.; C11 MARKET_RISK lowered 0.10 -> 0.06 and C05/C01 risk scalars changed only to bring
   volatility near 10-15%, which does not change any Sharpe ratio; spec states the final value).
5. Report: headline = registered full window; every number checked by script against the code output
   (work/out_Cxx.txt); interpretive sentences that the output does not support were removed (C03 tail sentence,
   C17 episodes).
Clean cases deliberately include features a checker might wrongly flag: weak or negative results (C02, C07, C16,
C17), era instability reported honestly (C04, C13, C18), diagnostic subsets reported below the registered headline
(C07, C16, C18), cross-class costs that matter (C06 1.12%/yr), registered roll costs only where the spec says so.

## Known limits
- Twins share a family (C02/C08 CPI rules, C07/C12 value, C06/C09 pairs, C04/C15 cross-sectional momentum);
  ASSIGN.json puts each twin with a different checker. Each checker gets exactly one defect of each type.
- C09's effect (0.17) is the smallest; it is clearest in the cost line (0.17 vs 1.29 %/yr) and at 2x costs.
- Tuned-knob cases can only be shown by the spec gap plus sensitivity; the "after" figure is the grid median.
