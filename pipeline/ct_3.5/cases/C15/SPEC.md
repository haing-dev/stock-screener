# SPEC: Equity index relative momentum (synthetic test pod)

> Status: REGISTERED 2026-11-24 before the run. One version.

## 0. Header
- Pod: Equity relative momentum. Type: systematic pod, cross-sectional.
- Data: Synthetic panel `cases/_lib/synth.py` (`make_panel()`, default seed): monthly futures-style excess returns 1970-01..2015-12, 32 markets in 4 classes, markets start at their own first month; carry, valuation and US CPI as documented in the module.

## 1. Claim
Among equity index futures, those with the higher recent past return earn more over the next month than those with
the lower (slow diffusion of country news). Grade: weak.

## 2. Signal (at each month-end t)
1. Markets: eq_us, eq_jp, eq_de, eq_uk, eq_fr, eq_au, eq_hk, eq_kr.
2. Momentum = sum of the monthly returns over the momentum window, ending a short gap before t (window and gap as
   set in `backtest.py`: WINDOW_MONTHS, GAP).
3. Rank indexes with a value and a vol, subtract the mean rank, scale so the absolute weights sum to 1; no position
   with fewer than 3.
4. Position = weight x 0.10 / vol x sqrt(number ranked); vol = std of the last 36 monthly returns up to t (at least
   24), annualised.

## 3. Costs
EQ 2 bp of notional one-way on every change of position. No roll charge.

## 4. Sample
Design window: return months 1975-01..2010-12 (432 months). Data from 1970 may be used for warm-up only. Eras reported: 1975-1992 and 1993-2010. Nothing after 2010-12 is read for results.
Timing: signal and size from data known at the close of month t; position held over month t+1; the trade made at the close of t is charged in month t+1.

## 5. Reported
Headline net Sharpe; mean, vol, worst drawdown; gross; net at twice the costs; eras; costs a year.
