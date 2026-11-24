# SPEC: Disinflation rule layer on North American rates (synthetic test pod)

> Status: REGISTERED 2026-11-24 before the run. One version. Rule layer (on/off months).

## 0. Header
- Pod: Disinflation. Type: rule layer, long-only when on, flat when off.
- Data: Synthetic panel `cases/_lib/synth.py` (`make_panel()`, default seed): monthly futures-style excess returns 1970-01..2015-12, 32 markets in 4 classes, markets start at their own first month; carry, valuation and US CPI as documented in the module.

## 1. Claim
When recent US inflation runs below its one-year rate, rates fall and bond and note futures gain over the next
month. Grade: weak.

## 2. Rule (at each month-end t)
1. As-of: the CPI value for reference month m is published in month m+1, so at the close of t the latest known CPI
   is reference month t-1. Every CPI input below is the latest published value.
2. Short-run inflation = 1200 / 3 x log(CPI / CPI three months earlier); one-year inflation = 1200 / 12 x
   log(CPI / CPI twelve months earlier).
3. On when short-run < one-year; off otherwise.
4. When on: long bd_us10, bd_ca10, st_us2, each at 0.10 / vol / sqrt(number of these legs with a vol); vol = std of
   the last 36 monthly returns up to t (at least 24), annualised. Off: flat.

## 3. Costs
FI 1 bp of notional one-way on every change of position. No roll charge.

## 4. Sample
Design window: return months 1975-01..2010-12 (432 months). Data from 1970 may be used for warm-up only. Eras reported: 1975-1992 and 1993-2010. Nothing after 2010-12 is read for results.
Timing: signal and size from data known at the close of month t; position held over month t+1; the trade made at the close of t is charged in month t+1.

## 5. Reported
Headline net Sharpe (off months count as zero); mean, vol, worst drawdown; gross; net at twice the costs; eras;
on-month count, mean, share positive; costs a year.
