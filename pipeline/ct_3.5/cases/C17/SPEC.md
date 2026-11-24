# SPEC: After-the-fall rule layer on equity indexes (synthetic test pod)

> Status: REGISTERED 2026-11-24 before the run. One version. Rule layer (on/off by market).

## 0. Header
- Pod: After the fall. Type: rule layer, long-only per market when on, flat when off.
- Data: Synthetic panel `cases/_lib/synth.py` (`make_panel()`, default seed): monthly futures-style excess returns 1970-01..2015-12, 32 markets in 4 classes, markets start at their own first month; carry, valuation and US CPI as documented in the module.

## 1. Claim
After an equity index has fallen far from its recent high, forced selling has run its course and the next month's
return is better than average. Grade: weak (anecdote-based).

## 2. Rule (per market, at each month-end t)
1. Markets: eq_us, eq_jp, eq_de, eq_uk, eq_fr, eq_au, eq_hk, eq_kr.
2. Level = cumulative product of (1 + monthly excess return) up to t. High = maximum level over the last 12 month-ends
   up to t (all 12 needed).
3. On when level / high - 1 <= -0.20 (a fall of 20% or more). Off otherwise.
4. When on: long at 0.10 / vol / sqrt(number of these indexes with a vol); vol = std of the last 36 monthly returns
   up to t (at least 24), annualised.

## 3. Costs
EQ 2 bp of notional one-way on every change of position. No roll charge.

## 4. Sample
Design window: return months 1975-01..2010-12 (432 months). Data from 1970 may be used for warm-up only. Eras reported: 1975-1992 and 1993-2010. Nothing after 2010-12 is read for results.
Timing: signal and size from data known at the close of month t; position held over month t+1; the trade made at the close of t is charged in month t+1.

## 5. Reported
Headline net Sharpe (all months); mean, vol, worst drawdown; gross; net at twice the costs; eras; months with any
market on and market-months on; net Sharpe in on months; costs a year.
