# SPEC: Trend, three horizons, EWMA risk (synthetic test pod)

> Status: REGISTERED 2026-11-24 before the run. One version.

## 0. Header
- Pod: Trend (multi-horizon). Type: systematic pod, time-series.
- Data: Synthetic panel `cases/_lib/synth.py` (`make_panel()`, default seed): monthly futures-style excess returns 1970-01..2015-12, 32 markets in 4 classes, markets start at their own first month; carry, valuation and US CPI as documented in the module.

## 1. Claim
Past returns over 1, 3 and 12 months predict the sign of the next month's return in futures markets (slow
reaction to news; hedging and risk-limit flows). Grade: moderate.

## 2. Signal (at each month-end t)
1. Markets: all 32 markets of the panel.
2. Score = mean of sign(sum of the last h monthly returns up to t) for h = 1, 3, 12 (each needs all h months).
3. Risk: vol = sqrt(exponentially weighted mean of squared monthly returns up to t, half-life 6 months, at least
   12 observations) x sqrt 12.
4. Position = score x 0.06 / vol / sqrt(number of markets in the class with a position); classes summed.

## 3. Costs
One-way cost on every change of position, in bp of notional: EQ 2, FI 1, FX 2, CM 4. The panel's returns are rolled excess returns, so no separate roll charge.

## 4. Sample
Design window: return months 1975-01..2010-12 (432 months). Data from 1970 may be used for warm-up only. Eras reported: 1975-1992 and 1993-2010. Nothing after 2010-12 is read for results.
Timing: signal and size from data known at the close of month t; position held over month t+1; the trade made at the close of t is charged in month t+1.

## 5. Reported
Headline net Sharpe; mean, vol, worst drawdown; gross; net at twice the costs; eras; costs and turnover a year.
