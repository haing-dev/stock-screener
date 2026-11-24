# SPEC: Bond carry, two versions averaged (synthetic test pod)

> Status: REGISTERED 2026-11-24 before the run. Two versions, equal weight.

## 0. Header
- Pod: Bond carry. Type: systematic pod.
- Data: Synthetic panel `cases/_lib/synth.py` (`make_panel()`, default seed): monthly futures-style excess returns 1970-01..2015-12, 32 markets in 4 classes, markets start at their own first month; carry, valuation and US CPI as documented in the module.

## 1. Claim
Bond and note futures with higher carry (yield minus the 3-month rate) earn more over the next month. Pattern, no
established mechanism. Grade: weak.

## 2. Signal (at each month-end t)
1. Markets: bd_us10, bd_de10, bd_jp10, bd_uk10, bd_ca10, bd_au10, st_us2, st_de2. Carry = `CARRY` at the close of t.
2. Version 1 (directional): w = sign(carry).
3. Version 2 (ranked): ranks of carry minus their mean, scaled so the absolute weights sum to the number of markets
   with carry; no position when fewer than 3 markets have carry.
4. Each version: position = w x 0.06 / vol / sqrt(number of markets with a vol); vol = std of the last 36 monthly
   returns up to t (at least 24), annualised. Pod = mean of the two versions (a missing one counts as 0).

## 3. Costs
FI 1 bp of notional one-way on every change of the POD's position (versions net before trading). No roll charge.

## 4. Sample
Design window: return months 1975-01..2010-12 (432 months). Data from 1970 may be used for warm-up only. Eras reported: 1975-1992 and 1993-2010. Nothing after 2010-12 is read for results.
Timing: signal and size from data known at the close of month t; position held over month t+1; the trade made at the close of t is charged in month t+1.

## 5. Reported
Headline net Sharpe of the pod; mean, vol, worst drawdown; gross; net at twice the costs; eras; each version alone
(diagnostic); costs a year.
