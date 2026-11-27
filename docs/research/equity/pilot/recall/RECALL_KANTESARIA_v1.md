# Recall test: Dev Kantesaria, recipe v1 (gate G8), 2026-11-27

Job eq_recall_v1 (eq_recall 1.0.3, seal-exempt job 9; spec pilot/RECALL_SPEC_v1.md; full output
eq_recall_v1_report.txt). Labels: **held-out failed**; **recipe covers 7 of 22 buy rules (decisive)**.
Question: at the quarter-end before each of his conviction purchases (2010-2025), would the written recipe have
picked the stock, and how much more often than for a comparable stock?

## Result: RECALL GATE FAIL

| Measure | Value | Bar | Met |
|---|---|---|---|
| Counted purchases (in the eligible universe at t) | 29 (version b); version a 18 = not measurable (< 20) | >= 20 | b only |
| Recall (share of his purchases the recipe passes) | 10.3% (3 of 29) | >= 25% | NO |
| Base rate (same quarter, sector, size third) | 1.2% | | |
| Lift | 8.30 | >= 2.0 | yes |
| 90% interval of lift (2,000 quarter draws, 15 quarters) | 0.00 to 17.57 | lower end > 1.25 | NO |
| Above control baseline (recipe on control purchases: lift 0.56) | yes | | yes |
| Above reference-book baseline (book top fifth on his purchases: lift 0.55) | yes | | yes |

Decisive form = version b alone (flagged: single version). Reported only: strict-missing form recall 6.9%, lift 7.98
[0.00, 18.87]; full form (108 versions averaged) recall 2.0%, lift 13.94 [11.44, 16.91], with 76 version-sets having no
passer in their cells and the interval on 1,315 of 2,000 draws, so not comparable.

Universe: 75,658 eligible stock-quarters at 64 quarter-ends (median 1,189); decisive pass rate 0.2-1.1% of the
universe per year; measure coverage 66-100% (EPS growth lowest). 10-year Treasury: public H.15 (FRED DGS10), 64 of 64
quarter-ends.

## What rejected his purchases (share of counted purchases each criterion rejects)

| Criterion | Rejects | Note |
|---|---|---|
| P2 40%+ below the 12-month high | 100% | he never bought a stock that far down |
| P3 trailed the market over 12 months | 59% | |
| P2 or P3 (the price trigger) | 59% | the largest single cause |
| B2 no loss year in 10 | 28% | |
| B4 steady revenue growth (s.d. below median) | 21% | |
| B5 operating margin up over 3 years | 20% | |
| A5 acquisitions <= 50% of operating cash flow | 20% | |
| B3 revenue and EPS growth above median | 19% | 9 points of it = measure missing |
| P1 FCF yield after share pay above the 10y Treasury | 19% | |
| B6 capex / revenue below median | 15% | |
| B1 10+ years of record | 2% | |
| A1-A4 industry exclusions | 0% | none of his purchases is in an excluded industry |

Rejections overlap; they do not add up.

## Reading
- The recipe does separate his kind of company from others: lift 8.3 on his purchases against 0.56 on the control
  investors' and 0.55 for the reference book. But it catches 3 of 29, and with 15 purchase quarters the interval
  reaches zero.
- The price part is the main miss. The "falling price" trigger (P2 or P3) was the recipe writer's reading of his
  quality-at-a-discount rule; 59% of his purchases came when the stock had NOT trailed the market, and none 40% down.
- Cross table (masked): the recipe gives lift above 2 for four other investors (3.1, 3.6, 6.8 and one control at 2.7);
  roster pooled 0.87, control pooled 0.56. Mask note: his own row (M03, 8.30) is identifiable by its value.

## Next (registered, A10 item 9)
One revision round: the recipe writer sees recall, base rate, lift and the per-criterion rejection shares ONLY (the
"universe rejects" column and the cross table are withheld). One revised recipe, every change citing a quote; both
results logged. Kill criterion after the pilot: 2 of 3 investors must pass.
