# SPEC: Cross-asset value: equities, currencies, commodities (synthetic test pod)

> Status: REGISTERED 2026-11-24 before the run. One version.

## 0. Header
- Pod: Value. Type: systematic pod, time-series value against each market's own history.
- Data: Synthetic panel `cases/_lib/synth.py` (`make_panel()`, default seed): monthly futures-style excess returns 1970-01..2015-12, 32 markets in 4 classes, markets start at their own first month; carry, valuation and US CPI as documented in the module.

## 1. Claim
A market that is cheap against its own valuation history earns more over the next month (prices drift back toward
value). Grade: weak.

## 2. Signal (at each month-end t)
1. Markets: all EQ, FX and CM markets of the panel (8 each). Valuation level = `VALUE` at the close of t (higher =
   cheaper).
2. Score = (V(t) - mean of V over the market's history up to and including t) / std of V over the same history;
   at least 60 months of history. Clip to [-2, 2], divide by 2.
3. Position = score x 0.10 / vol / sqrt(number of markets in the class with a position); vol = std of the last 36
   monthly returns up to t (at least 24), annualised. Class blocks summed.

## 3. Costs
EQ 2, FX 2, CM 4 bp of notional one-way on every change of position. No roll charge.

## 4. Sample
Design window: return months 1975-01..2010-12 (432 months). Data from 1970 may be used for warm-up only. Eras reported: 1975-1992 and 1993-2010. Nothing after 2010-12 is read for results.
Timing: signal and size from data known at the close of month t; position held over month t+1; the trade made at the close of t is charged in month t+1.

## 5. Reported
Headline net Sharpe; mean, vol, worst drawdown; gross; net at twice the costs; eras; each class alone; costs a year.
