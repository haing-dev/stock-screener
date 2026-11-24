# SPEC: Curve reversion, 2-year against 10-year (synthetic test pod)

> Status: REGISTERED 2026-11-24 before the run. One version. Spread pod.

## 0. Header
- Pod: Curve reversion. Type: systematic spread pod on two curves (US: st_us2 / bd_us10; DE: st_de2 / bd_de10).
- Data: Synthetic panel `cases/_lib/synth.py` (`make_panel()`, default seed): monthly futures-style excess returns 1970-01..2015-12, 32 markets in 4 classes, markets start at their own first month; carry, valuation and US CPI as documented in the module.

## 1. Claim
Bends between the 2-year and 10-year points fade within months (maturity-bound demand moves one point; it is
arbitraged back). Grade: weak.

## 2. Signal (per curve, at each month-end t)
1. vol_s, vol_l = std of the last 36 monthly returns up to t (at least 24), annualised, for the 2-year (s) and the
   10-year (l) leg.
2. u(t) = r_s(t) / vol_s(t-1) - r_l(t) / vol_l(t-1); level L = running sum of u; su = std of the last 36 values of
   u (at least 24).
3. gap = L(t) - mean of L(t-2..t); z = gap / su clipped to [-2, 2]; k = -z / 2 x 0.10 / (su x sqrt 12).
4. Notionals: 2-year = k / vol_s(t), 10-year = -k / vol_l(t); both x 1 / sqrt(number of curves live at t).

## 3. Costs (registered for this pod: the 2-year leg runs a large notional)
- FI 1 bp of notional one-way on every change of each leg's notional.
- Rolls: each leg is rolled 4 times a year; each roll is a round trip (2 x one-way) on the notional held,
  charged monthly as |notional| x 2 x 4 / 12 x 1 bp.

## 4. Sample
Design window: return months 1975-01..2010-12 (432 months). Data from 1970 may be used for warm-up only. Eras reported: 1975-1992 and 1993-2010. Nothing after 2010-12 is read for results.
Timing: signal and size from data known at the close of month t; position held over month t+1; the trade made at the close of t is charged in month t+1.

## 5. Reported
Headline net Sharpe; mean, vol, worst drawdown; gross; net at twice the costs; eras; costs a year (trades + rolls).
