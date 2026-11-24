# SPEC: Ranked carry, rates + currencies + commodities (synthetic test pod)

> Status: REGISTERED 2026-11-24 before the run. One version.

## 0. Header
- Pod: Ranked carry (cross-asset). Type: systematic pod, cross-sectional within each class.
- Data: Synthetic panel `cases/_lib/synth.py` (`make_panel()`, default seed): monthly futures-style excess returns 1970-01..2015-12, 32 markets in 4 classes, markets start at their own first month; carry, valuation and US CPI as documented in the module.

## 1. Claim
Within each asset class, markets with higher carry earn more over the next month than markets with lower carry
(compensation for bearing price risk that hedgers pass on). Grade: weak.

## 2. Signal (at each month-end t)
1. Classes FI (8 markets), FX (8), CM (8). Carry = `CARRY` at the close of t.
2. Within a class: rank the markets that have a carry value; subtract the mean rank; scale so the absolute weights
   sum to 1. No position in a class with fewer than 3 markets.
3. Size: weight x 0.06 / vol x sqrt(number of markets in the class); vol = standard deviation of the last 36 monthly
   returns up to t (at least 24), annualised. Classes are summed.

## 3. Costs
One-way cost on every change of position, in bp of notional: EQ 2, FI 1, FX 2, CM 4. The panel's returns are rolled excess returns, so no separate roll charge.

## 4. Sample
Design window: return months 1975-01..2010-12 (432 months). Data from 1970 may be used for warm-up only. Eras reported: 1975-1992 and 1993-2010. Nothing after 2010-12 is read for results.
Timing: signal and size from data known at the close of month t; position held over month t+1; the trade made at the close of t is charged in month t+1.

## 5. Reported
Headline net Sharpe ratio over the design window; mean, volatility, worst drawdown; gross; net at twice the costs;
both eras; costs a year.
