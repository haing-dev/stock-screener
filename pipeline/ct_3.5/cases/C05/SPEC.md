# SPEC: Directional carry, bonds + currencies + commodities (synthetic test pod)

> Status: REGISTERED 2026-11-24 before the run. One version.

## 0. Header
- Pod: Directional carry. Type: systematic pod, time-series (sign of own carry).
- Data: Synthetic panel `cases/_lib/synth.py` (`make_panel()`, default seed): monthly futures-style excess returns 1970-01..2015-12, 32 markets in 4 classes, markets start at their own first month; carry, valuation and US CPI as documented in the module.

## 1. Claim
A market with positive carry earns more over the next month than one with negative carry, in bonds, currencies and
commodities alike. Grade: weak.

## 2. Signal (at each month-end t)
1. Markets: all 8 FI, all 8 FX and all 8 CM markets of the panel.
2. Weight = sign(`CARRY` at the close of t).
3. Position = weight x 0.05 / vol / sqrt(number of markets in the class with a position); vol = std of the last 36
   monthly returns up to t (at least 24), annualised. The three class blocks are summed.

## 3. Costs
One-way cost on every change of position, in bp of notional: EQ 2, FI 1, FX 2, CM 4. The panel's returns are rolled excess returns, so no separate roll charge.

## 4. Sample
Design window: return months 1975-01..2010-12 (432 months). Data from 1970 may be used for warm-up only. Eras reported: 1975-1992 and 1993-2010. Nothing after 2010-12 is read for results.
Timing: signal and size from data known at the close of month t; position held over month t+1; the trade made at the close of t is charged in month t+1.

## 5. Reported
Headline: net Sharpe of the pod (all three classes) over the design window; mean, vol, worst drawdown; gross; net
at twice the costs; eras; costs a year. Per-class results reported as diagnostics.
