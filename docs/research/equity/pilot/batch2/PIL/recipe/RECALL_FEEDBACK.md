# Recall result of RECIPE_v1 (decisive form) on the investor's own 13F conviction purchases, 2010-2025

Each purchase is evaluated at the quarter-end BEFORE the purchase quarter, on the eligible universe (1,500 largest US stocks, price >= $5, liquid, GICS known). Version a = new position or addition into the five largest weights; version b = to >= 1% of the portfolio; the decisive result averages a and b; fewer than 20 purchases = not measurable. Base rate = pass rate of comparable stocks (same quarter, sector, size third). Lift = recall / base rate. Gate: lift >= 2.0, 90% interval lower end > 1.25, recall >= 25% (plus two baselines not shown to you).

## Result
```
purchases: either 83 (version a 17, b 82); in the eligible universe at t: either 44 (a 8, b 43); in the universe but in a house-excluded industry (A8 2a, not counted): 0; not in the universe: 39
quarters with a counted purchase: 21; bootstrap: 2000 draws of quarters, seed 20261127
DECISIVE (average of versions a and b)       recall  18.6%  base   9.8%  lift   1.89  90% [  0.95,   3.09]
   NOTE: decisive = one version only (a not measurable: fewer than 20 purchases)
   per version: a: n 8, recall    -  , base    -  , lift    -  ; b: n 43, recall  18.6%, base   9.8%, lift   1.89
lift >= 2.00: NO; interval lower end > 1.25: NO; recall >= 25%: NO
RECALL GATE: FAIL
```

## Share of counted purchases each criterion rejects (rejections overlap; 'of which measure missing' shown)
```
criterion  rejects  of which measure missing  | description
A1           2.3%     0.0%  | financials (GICS 2023 groups 4010, 4020, 4030)
B1          59.2%     2.3%  | ROE TTM above the comparison-group median
B2           2.3%     1.2%  | tangible book per share + dividends up over 12 quarters (banks, insurers)
B3          19.8%     1.2%  | momentum 6-1 > 0
P1          42.0%     0.0%  | value score in the cheapest 30% of the comparison group
A2          15.1%     2.3%  | a new 12-month low (excluded)
B1_33       33.9%     0.0%  | ROE rank > 1/3 (full form)
```
