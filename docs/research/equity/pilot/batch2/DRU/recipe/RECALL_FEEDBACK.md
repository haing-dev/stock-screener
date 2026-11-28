# Recall result of RECIPE_v1 (decisive form) on the investor's own 13F conviction purchases, 2010-2025

Each purchase is evaluated at the quarter-end BEFORE the purchase quarter, on the eligible universe (1,500 largest US stocks, price >= $5, liquid, GICS known). Version a = new position or addition into the five largest weights; version b = to >= 1% of the portfolio; the decisive result averages a and b; fewer than 20 purchases = not measurable. Base rate = pass rate of comparable stocks (same quarter, sector, size third). Lift = recall / base rate. Gate: lift >= 2.0, 90% interval lower end > 1.25, recall >= 25% (plus two baselines not shown to you).

## Result
```
purchases: either 726 (version a 136, b 726); in the eligible universe at t: either 563 (a 109, b 563); in the universe but in a house-excluded industry (A8 2a, not counted): 82; not in the universe: 81
quarters with a counted purchase: 60; bootstrap: 2000 draws of quarters, seed 20261127
DECISIVE (average of versions a and b)       recall  16.5%  base   9.8%  lift   1.69  90% [  1.27,   2.12]
   per version: a: n 109, recall  18.3%, base  10.3%, lift   1.77; b: n 563, recall  14.7%, base   9.2%, lift   1.60
lift >= 2.00: NO; interval lower end > 1.25: yes; recall >= 25%: NO
RECALL GATE: FAIL
```

## Share of counted purchases each criterion rejects (rejections overlap; 'of which measure missing' shown)
```
criterion  rejects  of which measure missing  | description
B1          69.9%     2.1%  | revenue growth 3y (TTM vs 12 quarters before) >= 20%
B2          67.9%     0.2%  | revenue growth 1y >= 20%
B3          28.0%     0.8%  | momentum 6-1 > 0
G           85.5%     2.2%  | branch G: B1 and B2 and B3
B4          54.3%     0.0%  | cyclical sector 10, 15, 20, 25
B5          97.8%     0.0%  | industry EBIT TTM sum < 0 (>= 3 members)
C           97.8%     0.0%  | branch C: B4 and B5
G|C         83.5%     0.0%  | either branch
```
