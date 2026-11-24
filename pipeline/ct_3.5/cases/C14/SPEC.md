# SPEC: Rates and currencies trend (synthetic test pod)

> Status: REGISTERED 2026-11-24 before the run. One version.

## 0. Header
- Pod: Rates and currencies trend. Type: systematic pod, time-series.
- Data: Synthetic panel `cases/_lib/synth.py` (`make_panel()`, default seed): monthly futures-style excess returns 1970-01..2015-12, 32 markets in 4 classes, markets start at their own first month; carry, valuation and US CPI as documented in the module.

## 1. Claim
Past 3- and 12-month returns predict the sign of the next month's return in bond, note and currency futures.
Grade: moderate.

## 2. Signal (at each month-end t)
1. Markets: all 8 FI and all 8 FX markets of the panel.
2. Score = mean of sign(sum of the last h monthly returns up to t), h = 3 and 12 (each needs all h months).
3. Position = score x 0.10 / vol / sqrt(number of markets with a position); vol = std of the last 36 monthly
   returns up to t (at least 24), annualised.

## 3. Costs
FI 1, FX 2 bp of notional one-way on every change of position. No roll charge.

## 4. Sample
Design window: return months 1975-01..2010-12 (432 months). Data from 1970 may be used for warm-up only. Eras reported: 1975-1992 and 1993-2010. Nothing after 2010-12 is read for results.
Timing: signal and size from data known at the close of month t; position held over month t+1; the trade made at the close of t is charged in month t+1.

## 5. Reported
Headline: net Sharpe over the full design window; mean, vol, worst drawdown; gross; net at twice the costs; eras
(reported, not decisive); costs a year.
