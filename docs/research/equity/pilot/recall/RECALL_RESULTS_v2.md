# Recall test, eight recipes (eq_recall 1.1.1, job eq_recall_v2), 2026-11-28

Full output: eq_recall_v2_report.txt (the runner cut it at 60,000 characters inside the Li Lu block, so Li Lu and the
summary table were not seen; rerun of the same computation in two steps = eq_recall 1.1.2, job eq_recall_v2b, A13 item
23: every recipe seen in v2 is identical line for line in v2b; report eq_recall_v2b_report.txt). kantesaria_v1 reproduces eq_recall_v1 exactly (recall 10.3%, lift 8.30, 90% [0.00, 17.57]).

Gate (RECALL_SPEC_v1): lift >= 2.0, 90% interval lower end > 1.25, recall >= 25%, lift above the control baseline and
above the reference-book baseline. Decisive form = average of the two purchase versions (a: into the top five; b: to
>= 1% of the portfolio); a version with fewer than 20 purchases is not measurable.

| Recipe | Purchases (a / b) | Recall | Base | Lift | 90% interval | Control lift | Ref-book lift | Gate | Labels |
|---|---|---|---|---|---|---|---|---|---|
| kantesaria_v1 | 18 (n.m.) / 29 | 10.3% | 1.2% | 8.30 | 0.00-17.57 | 0.56 | 0.55 | FAIL | held-out failed; 7 of 22 buy rules |
| kantesaria_v2 | 18 (n.m.) / 29 | 37.9% | 5.9% | 6.41 | 4.19-8.91 | 1.01 | 0.55 | **PASS** | **revision after seeing v1, same 29 purchases: not independent**; held-out failed |
| druckenmiller_v1 | 109 / 563 | 16.5% | 9.8% | 1.69 | 1.27-2.12 | 1.51 | 1.13 | FAIL | thin; held-out failed; equity longs only; no price rule; 3 of 11 buy rules |
| stahl_v1 | 15 (n.m.) / 61 | 39.3% | 28.9% | 1.36 | 1.04-1.68 | 0.97 | 0.96 | FAIL | thin; held-out failed; 13F firm-wide (Horizon Kinetics); no price rule; 3 of 6, stand-ins |
| hohn_v1 | 54 / 80 | 15.9% | 7.1% | 2.24 | 1.42-3.17 | 1.14 | 1.26 | FAIL (recall) | thin; 5 of 14 buy rules |
| zlatev_v1 | 28 / 104 | 7.4% | 3.5% | 2.12 | 0.70-3.78 | 0.07 | 1.84 | FAIL | thin; longs only tested; 3 of 5 |
| pilecki_v1 | 8 (n.m.) / 43 | 18.6% | 9.8% | 1.89 | 0.95-3.09 | 1.24 | 1.29 | FAIL | thin; financials only; decisive minus B4 |
| nygren_v1 | 23 / 61 | 31.0% | 14.9% | 2.05 | 1.54-2.54 | 1.44 | 1.16 | **PASS** | thin; 13F firm-wide (Harris Associates); r = 10y Treasury |
| lilu_v1 | 9 (n.m.) / 14 (n.m.) | - | - | - | - | 3.20 | - | NOT MEASURABLE (fewer than 20 purchases) | thin; own set (all industries) |
| sosin_v1 | not measured (not in eq_conv_panel) | | | | | | | | |

n.m. = not measurable (fewer than 20). Ref-book lift = the reference book's top fifth on this investor's purchases.

## Largest rejectors of each investor's purchases (decisive criteria first)
- Druckenmiller: neither branch fits 84% of his purchases; the cyclical-trough branch C rejects 98%, the growth branch G 86%.
- Stahl: few index owners (B3) 59%, shares not falling (B2) 49%; base rate 29%, so the screen passes a lot of everything.
- Hohn: the ten-year 15% return-on-capital barrier (B1) 62%; stable margins (B2) 55%.
- Zlatev: price / FY2 EPS <= 20 (P1) 59%; gross margin not falling (B3b) 46%.
- Pilecki: ROE above the group median (B1) 59%; cheapest 30% on value (P1) 42%.
- Nygren: price below 70% of the seven-year value (P4) 61%.

## Reading
- Two passes: Kantesaria v2 (not independent: built after seeing v1 on the same purchases) and Nygren/Fitch (thin
  material; the 13F is Harris Associates as a firm, so the purchases are not only theirs).
- Most recipes pick their investor's purchases 1.4-2.2 times more often than comparable stocks, but also pick the
  control investors' purchases more often than chance (control lifts 1.0-1.5): part of what they capture is "what
  professional investors buy" rather than this investor.
- Zlatev's recipe separates sharply from the controls (0.07) but misses 93% of his purchases.

## Kill criterion (A10 item 9; pilot set registered in A13 item 23 before any revision result)
Pilot = the three investors with full material: Kantesaria, Druckenmiller, Stahl. Today: Kantesaria passes only
after his revision (flagged); Druckenmiller and Stahl fail and each has one revision round left. Rule: if fewer than 2
of 3 pass after their revision rounds, no more recipes; investor work turns analyst-led.

## Li Lu (from eq_recall_v2b)
Only 14 of his conviction purchases fall in the eligible universe (17 in all; version a 9, version b 14): fewer than
20, so the recall test cannot measure his recipe and no revision round applies. The recipe on the control investors'
purchases gives lift 3.20 [1.86, 4.93]: it picks a narrow kind of stock that some professional investors buy, but his
own record is too small to tell whether it is his.
