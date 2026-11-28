# Recall result of RECIPE_v1 (decisive form) on the investor's own 13F conviction purchases, 2010-2025

Each purchase is evaluated at the quarter-end BEFORE the purchase quarter, on the eligible universe (1,500 largest US stocks, price >= $5, liquid, GICS known). Version a = new position or addition into the five largest weights; version b = to >= 1% of the portfolio; the decisive result averages a and b; fewer than 20 purchases = not measurable. Base rate = pass rate of comparable stocks (same quarter, sector, size third). Lift = recall / base rate. Gate: lift >= 2.0, 90% interval lower end > 1.25, recall >= 25% (plus two baselines not shown to you).

## Result
```
purchases: either 107 (version a 68, b 102); in the eligible universe at t: either 85 (a 54, b 80); in the universe but in a house-excluded industry (A8 2a, not counted): 1; not in the universe: 21
quarters with a counted purchase: 44; bootstrap: 2000 draws of quarters, seed 20261127
DECISIVE (average of versions a and b)       recall  15.9%  base   7.1%  lift   2.24  90% [  1.42,   3.17]
   per version: a: n 54, recall  13.0%, base   7.0%, lift   1.85; b: n 80, recall  18.8%, base   7.2%, lift   2.62
lift >= 2.00: yes; interval lower end > 1.25: yes; recall >= 25%: NO
RECALL GATE: FAIL
```

## Share of counted purchases each criterion rejects (rejections overlap; 'of which measure missing' shown)
```
criterion  rejects  of which measure missing  | description
A1          34.4%     0.0%  | consumer discretionary (sector 25)
A2           0.0%     0.0%  | banks, autos, retail, insurance, energy, materials, tobacco, asset managers
B1          62.1%     9.6%  | Q01 > 15% in 10 of the last 10 fiscal years (S04*)
B1i        100.0%     9.6%  | airports / toll roads with no loss year in 10
B1|B1i      62.1%     9.6%  | barrier route
B2          54.7%     9.6%  | operating-margin s.d. 10y in the stable half of the sector
P1          12.4%     1.6%  | FCF yield TTM minus the 10y Treasury >= 0
B4          35.7%     0.0%  | revenue-growth s.d. 10y in the stable half of the sector (full form)
A3           0.0%     0.0%  | airlines, wireless, media (full form)
P1g_1       25.8%     0.0%  | FCF yield gap >= 1 point (full form)
P1g_2       45.4%     0.0%  | FCF yield gap >= 2 points (full form)
```
