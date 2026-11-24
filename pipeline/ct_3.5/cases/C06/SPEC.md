# SPEC: Pair reversion between close substitutes (synthetic test pod)

> Status: REGISTERED 2026-11-24 before the run. One version. Spread pod.

## 0. Header
- Pod: Pair reversion. Type: systematic spread pod (long one leg, short the other, risk matched).
- Data: Synthetic panel `cases/_lib/synth.py` (`make_panel()`, default seed): monthly futures-style excess returns 1970-01..2015-12, 32 markets in 4 classes, markets start at their own first month; carry, valuation and US CPI as documented in the module.

## 1. Claim
Between two markets that share most of their risk, a short-lived gap in their relative price fades within months
(local supply and demand moves the relative price; arbitrage capital closes it). Grade: weak.

## 2. Signal (per pair a/b, at each month-end t)
Pairs: bd_us10/bd_ca10, bd_de10/bd_uk10, eq_de/eq_fr, fx_aud/fx_nzd, cm_wti/cm_brent, cm_gold/cm_silver,
cm_corn/cm_soy, fx_chf/fx_sek.
1. vol_a, vol_b = std of the last 36 monthly returns up to t (at least 24), annualised.
2. Unit spread return u(t) = r_a(t) / vol_a(t-1) - r_b(t) / vol_b(t-1); level L = running sum of u.
3. gap(t) = L(t) - mean of L(t-2), L(t-1), L(t); s(t) = std of the last 36 values of u up to t (at least 24).
4. z = gap / s, clipped to [-2, 2]. Spread units k = -z / 2 x 0.10 / (s x sqrt 12).
5. Positions: a = k / vol_a(t), b = -k / vol_b(t); both multiplied by 1 / sqrt(number of pairs live at t).

## 3. Costs
One-way cost on every change of EACH LEG's notional: EQ 2, FI 1, FX 2, CM 4 bp. No roll charge.

## 4. Sample
Design window: return months 1975-01..2010-12 (432 months). Data from 1970 may be used for warm-up only. Eras reported: 1975-1992 and 1993-2010. Nothing after 2010-12 is read for results.
Timing: signal and size from data known at the close of month t; position held over month t+1; the trade made at the close of t is charged in month t+1.

## 5. Reported
Headline net Sharpe; mean, vol, worst drawdown; gross; net at twice the costs; eras; costs a year.
