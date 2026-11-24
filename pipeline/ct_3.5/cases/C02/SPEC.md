# SPEC: Soft-print rule layer on government bonds (synthetic test pod)

> Status: REGISTERED 2026-11-24 before the run. One version. Rule layer (on/off months).

## 0. Header
- Pod: Soft print. Type: rule layer, long-only when on, flat when off.
- Data: Synthetic panel `cases/_lib/synth.py` (`make_panel()`, default seed): monthly futures-style excess returns 1970-01..2015-12, 32 markets in 4 classes, markets start at their own first month; carry, valuation and US CPI as documented in the module.

## 1. Claim
A US consumer-price print that comes in soft relative to the recent run of prints is followed by better bond
returns over the next month (inflation news is persistent and bonds price it slowly). Grade: weak.

## 2. Rule (at each month-end t)
1. As-of: the CPI value for reference month m is published in month m+1; at the close of t the latest known
   reference month is t-1.
2. m = 1200 x log change of the latest published CPI over the month before it (annualised monthly inflation).
3. On when m is below the average of the 12 published monthly changes before it; off otherwise (and off until that
   average exists).
4. When on: long each of bd_us10, bd_de10, bd_jp10, bd_uk10, bd_ca10, bd_au10 at 0.10 / vol / sqrt(number of these
   markets with a vol), vol = std of the last 36 monthly returns up to t (at least 24), annualised. Off: flat.

## 3. Costs
FI 1 bp of notional one-way on every change of position. No roll charge (rolled excess returns).

## 4. Sample
Design window: return months 1975-01..2010-12 (432 months). Data from 1970 may be used for warm-up only. Eras reported: 1975-1992 and 1993-2010. Nothing after 2010-12 is read for results.
Timing: signal and size from data known at the close of month t; position held over month t+1; the trade made at the close of t is charged in month t+1.

## 5. Reported
Headline net Sharpe (all months, off months count as zero); mean, vol, worst drawdown; gross; net at twice the
costs; eras; on-month count, on-month mean and hit rate; costs a year.
