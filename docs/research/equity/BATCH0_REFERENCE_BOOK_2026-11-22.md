# Batch 0: reference book v1 on WRDS (2026-11-22)

Run T001 (`TRIAL_LOG.md`), registered in `V04_REGISTRATION.md` A8 before any return was computed. Code eq_ref 1.0.2
(e5a7ee9c...), job `eq_ref_v1c` (the first two runs stopped before any return: a key bug, then a stale copy of the
code on the runner; both logged). Report: `eq_ref_v1c_report.txt`. Batch 0 is plumbing: **no verdict, nothing is
adopted or changed because of these numbers** (reference book v1 stays as registered; any change = v2).

## Plumbing checks
| Check | Result |
|---|---|
| Universe | 1,500 largest US-incorporated lines each month; 1,433-1,494 pass price and liquidity; 210-329 excluded (banks, insurers, real estate, biotech); 12-28 without a GICS sector; 1,097-1,194 ranked |
| Coverage (share of non-excluded members with the measure) | earnings yield 98-99%, book to price 99-100%, momentum 94-99%, ROE 88-96%, accruals 93-99%, Piotroski 89-98%, revisions 96-99% |
| GICS | history (comp.co_hgic), not today's codes |
| Measures behave like the published factors | correlation of the inside-sector spread with the matching Fama-French factor: momentum / UMD 0.86, book to price / HML 0.70, ROE / RMW 0.57, earnings yield / HML 0.46, revisions / UMD 0.39 |
| Book mechanics | 133-167 names (median 150), fully invested, turnover 3.75x a year both sides, costs 0.56% a year, no position above 5% of median daily dollar volume at $10m |
| Share-basis check for revisions | CRSP price factor falls over time in CIZ (AAPL 2020 split: 0.25), handled |

## Published-form spreads 2010-2025 (top minus bottom tenth inside the sector, gross, per month)
Momentum +0.68% (t 2.65), revisions +0.57% (t 3.43), Piotroski 8-9 minus 0-1 +1.92% (t 1.98; 179 months, some months
have no stock at 0-1 or 8-9), ROE +0.21% (t 0.76), accruals +0.09% (t 0.59), earnings yield +0.08% (t 0.26), book to
price **-0.28% (t -1.52)**: the only sign opposite to the paper, in line with the weak value years 2010-2020 (its
correlation with HML is 0.70, so the measure is built right). Book score spread +0.68% (t 2.78).

## Reference book v1, long book under R4, 2010-2025 (reported, no verdict)
| Series | Return a year | Vol | Worst fall |
|---|---|---|---|
| Book, net of costs | 13.3% | 18.3% | -29.8% |
| Sector-matched universe | 12.2% | 17.8% | -28.8% |
| Book net minus sector-matched | +1.0% (NW t 1.24, IR 0.37) | 2.8% | -16.9% |
| Book gross minus sector-matched | +1.6% (t 1.91) | 2.8% | -14.4% |

Eras (net minus sector-matched): 2010-14 +0.5% a year (t 0.5), 2015-19 -1.8% (t -1.8), 2020-25 +3.9% (t 2.7).
Calendar years: worst 2020 -7.1 points (stress year M4), 2019 -4.7, 2016 -4.4; best 2024 +11.9, 2025 +7.2, 2021 +5.1.

## Findings to carry
1. The plumbing works end to end on WRDS data; coverage is high from 2009 on (the LSEG first-reported data are thinner
   before about 2015: about 60% of Q2 companies have the account measures in 2010, rising to 90%+ from 2022; see
   `LSEG_measures_check_2026-11-22.md`). The LSEG run of the same engine is the registered primary and is compared
   with this one when the stage-B files exist.
2. The cap of 2.5% per stock is applied at formation (A8 b); drift lets one stock reach 2.99% of the book. Reported;
   whether R4 means a hard cap at every review is a question for the second implementation, not a change now.
3. The book's edge over its sector-matched universe is small and uneven (negative 2015-19). Every pod is measured
   against this book (R5), so the bar for "added return" is this series, not the market.
4. Still open before Batch A: the second implementation by a separate agent (plan step 5) must reproduce these
   numbers from the written spec; the LSEG run; the daily engine (next-day close, R4).
