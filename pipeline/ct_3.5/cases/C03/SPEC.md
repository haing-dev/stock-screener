# SPEC: Currency carry, ranked (synthetic test pod)

> Status: REGISTERED 2026-11-24 before the run. One version.

## 0. Header
- Pod: Currency carry (cross-sectional). Type: systematic pod.
- Data: Synthetic panel `cases/_lib/synth.py` (`make_panel()`, default seed): monthly futures-style excess returns 1970-01..2015-12, 32 markets in 4 classes, markets start at their own first month; carry, valuation and US CPI as documented in the module.

## 1. Claim
Currencies with a higher interest-rate gap against the dollar earn more over the next month than those with a lower
gap (a risk premium, paid with losses in unwinds). Grade: weak-moderate.

## 2. Signal (at each month-end t)
1. Markets: fx_eur, fx_jpy, fx_gbp, fx_chf, fx_aud, fx_cad, fx_nzd, fx_sek (fx_eur from 1999-01).
2. Carry = `CARRY` at the close of t. Rank the currencies with a value, subtract the mean rank, scale so the absolute
   weights sum to 1. No position with fewer than 3 currencies.
3. Position = weight x 0.10 / vol; vol = std of the last 36 monthly returns up to t (at least 24), annualised.

## 3. Costs
FX 2 bp of notional one-way on every change of position. No roll charge.

## 4. Sample
Design window: return months 1975-01..2010-12 (432 months). Data from 1970 may be used for warm-up only. Eras reported: 1975-1992 and 1993-2010. Nothing after 2010-12 is read for results.
Timing: signal and size from data known at the close of month t; position held over month t+1; the trade made at the close of t is charged in month t+1.

## 5. Reported
Headline net Sharpe; mean, vol, worst drawdown; gross; net at twice the costs; eras; costs a year; three worst months.
