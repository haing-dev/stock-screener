# SPEC: Bond momentum, cross-sectional 12-1 (synthetic test pod)

> Status: REGISTERED 2026-11-24 before the run. One version.

## 0. Header
- Pod: Bond relative momentum. Type: systematic pod, cross-sectional.
- Data: Synthetic panel `cases/_lib/synth.py` (`make_panel()`, default seed): monthly futures-style excess returns 1970-01..2015-12, 32 markets in 4 classes, markets start at their own first month; carry, valuation and US CPI as documented in the module.

## 1. Claim
Among government bond and note futures, those with the higher past-year return (excluding the latest month) earn
more over the next month. Grade: weak.

## 2. Signal (at each month-end t)
1. Markets: bd_us10, bd_de10, bd_jp10, bd_uk10, bd_ca10, bd_au10, st_us2, st_de2.
2. Momentum = sum of the monthly returns of months t-12 .. t-1 (12 months, the latest month t skipped); all 12 needed.
3. Rank markets with a value, subtract the mean rank, scale so the absolute weights sum to 1; no position with
   fewer than 3 markets.
4. Position = weight x 0.10 / vol x sqrt(number ranked); vol = std of the last 36 monthly returns up to t (at least
   24), annualised.

## 3. Costs
FI 1 bp of notional one-way on every change of position. No roll charge.

## 4. Sample
Design window: return months 1975-01..2010-12 (432 months). Data from 1970 may be used for warm-up only. Eras reported: 1975-1992 and 1993-2010. Nothing after 2010-12 is read for results.
Timing: signal and size from data known at the close of month t; position held over month t+1; the trade made at the close of t is charged in month t+1.

## 5. Reported
Headline net Sharpe; mean, vol, worst drawdown; gross; net at twice the costs; eras; costs a year.
