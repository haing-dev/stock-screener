# Recall result of RECIPE_v1 (decisive form) on the investor's own 13F conviction purchases, 2010-2025

Each purchase is evaluated at the quarter-end BEFORE the purchase quarter, on the eligible universe (1,500 largest US stocks, price >= $5, liquid, GICS known). Version a = new position or addition into the five largest weights; version b = to >= 1% of the portfolio; the decisive result averages a and b; fewer than 20 purchases = not measurable. Base rate = pass rate of comparable stocks (same quarter, sector, size third). Lift = recall / base rate. Gate: lift >= 2.0, 90% interval lower end > 1.25, recall >= 25% (plus two baselines not shown to you).

## Result
```
purchases: either 118 (version a 33, b 112); in the eligible universe at t: either 65 (a 15, b 61); in the universe but in a house-excluded industry (A8 2a, not counted): 16; not in the universe: 37
13F filer is firm-wide (Horizon Kinetics; A6): purchases are the firm's, not only this investor's
quarters with a counted purchase: 27; bootstrap: 2000 draws of quarters, seed 20261127
DECISIVE (average of versions a and b)       recall  39.3%  base  28.9%  lift   1.36  90% [  1.04,   1.68]
   NOTE: decisive = one version only (a not measurable: fewer than 20 purchases)
   per version: a: n 15, recall    -  , base    -  , lift    -  ; b: n 61, recall  39.3%, base  28.9%, lift   1.36
lift >= 2.00: NO; interval lower end > 1.25: NO; recall >= 25%: yes
RECALL GATE: FAIL
```

## Share of counted purchases each criterion rejects (rejections overlap; 'of which measure missing' shown)
```
criterion  rejects  of which measure missing  | description
B1          29.0%     5.8%  | FCF margin TTM > 0 or net cash >= 0
B2          48.8%     7.4%  | diluted shares not up over 12 quarters
B3          58.6%     8.3%  | index-fund ownership below the sector median and shares down
B4          33.0%     0.0%  | FY1 analyst count below the sector median (none = 0)
B3|B4       22.2%     0.0%  | one of the two neglect tests
B3g_33      64.4%     0.0%  | B3 below the sector 33rd percentile (full form)
B4g_33      59.5%     0.0%  | B4 below the 33rd percentile (full form)
```
