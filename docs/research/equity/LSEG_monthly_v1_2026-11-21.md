# LSEG monthly files: what came back (2026-11-21)

Three workbooks (`G:\My Drive\Screener project\LSEG\03_monthly`), read with the streaming reader
`tools/equity/lseg/read_monthly.py` into one panel (`panel_monthly_v1.csv.gz`, on the PC and in the session scratch only).
Counts and data checks only; no portfolio or signal return was computed.

| Check | Result |
|---|---|
| Blocks | 25 of 25 returned; no copied series between lines |
| Lines with data | 5,436 of 5,537 (2009-12 .. 2026-10); 633,193 line-months |
| Filled | close 98.7%, shares 99.1%, company value 99.7%, volume 99.9%, one-month total return 99.0% |
| Security value (close x shares) vs company value | median ratio 1.000; within 5% for 78% of rows (the rest: companies with several share classes) |
| Total return vs price change | aligned month by month (correlation 0.988 same month, about 0 one month off); within 2 points in 89% of months (dividends, splits on unadjusted prices) |
| Extreme months (total return above +200% or below -100%) | 1,421, mostly below $5 or real price moves (71% with a price change above 100%); 243 among lines worth $1bn+ |
| 1,500th line by security value, price >= $5 | $0.84bn (2009-12), $1.22bn (2012-12), $1.76bn (2015-12 and 2018-12), $3.55bn (2021-12), $2.51bn (2024-12), $2.48bn (2025-10) |
| Volume | monthly TR.Volume is the volume of the LAST DAY of the month, not the month's total (Crocs 2024: 3-8% of the summed daily volume; some months 0) |

Consequence for R3 (addendum A7): the $2m liquidity screen uses the median of the last three month-end daily dollar
volumes (zeros treated as missing), a stand-in until daily volume is pulled. Among the 1,500 largest it rarely binds.
