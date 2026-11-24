# SPEC: Relative value between close substitutes, two versions (synthetic test pod)

> Status: REGISTERED 2026-11-24 before the run. Two versions averaged. Spread pod.

## 0. Header
- Pod: Relative value pairs. Type: systematic spread pod (long one leg, short the other, risk matched).
- Data: Synthetic panel `cases/_lib/synth.py` (`make_panel()`, default seed): monthly futures-style excess returns 1970-01..2015-12, 32 markets in 4 classes, markets start at their own first month; carry, valuation and US CPI as documented in the module.

## 1. Claim
Between two markets that share most of their risk, relative-price gaps fade within months. Grade: weak.

## 2. Signal (per pair a/b, at each month-end t)
Pairs: bd_us10/bd_ca10, bd_de10/bd_uk10, eq_de/eq_fr, fx_aud/fx_nzd, cm_wti/cm_brent, cm_gold/cm_silver,
cm_corn/cm_soy.
1. vol_a, vol_b = std of the last 36 monthly returns up to t (at least 24), annualised.
2. u(t) = r_a(t) / vol_a(t-1) - r_b(t) / vol_b(t-1); level L = running sum of u; su = annualised std of the last 36
   values of u (at least 24).
3. Version 1: gap = u(t). Version 2: gap = L(t) - mean of L over the last 6 months up to t.
4. Each version: z = gap / (su / sqrt 12) clipped to [-2, 2]; units = -z / 2. Pod units = mean of the two versions
   x 0.10 / su x 1 / sqrt(number of pairs live).
5. Leg notionals: a = units / vol_a(t), b = -units / vol_b(t).

## 3. Costs
One-way cost on every change of EACH LEG's notional: EQ 2, FI 1, FX 2, CM 4 bp. No roll charge.

## 4. Sample
Design window: return months 1975-01..2010-12 (432 months). Data from 1970 may be used for warm-up only. Eras reported: 1975-1992 and 1993-2010. Nothing after 2010-12 is read for results.
Timing: signal and size from data known at the close of month t; position held over month t+1; the trade made at the close of t is charged in month t+1.

## 5. Reported
Headline net Sharpe; mean, vol, worst drawdown; gross; net at twice the costs; eras; costs a year.
