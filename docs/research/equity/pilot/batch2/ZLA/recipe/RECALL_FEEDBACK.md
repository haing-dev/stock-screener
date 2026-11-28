# Recall result of RECIPE_v1 (decisive form) on the investor's own 13F conviction purchases, 2010-2025

Each purchase is evaluated at the quarter-end BEFORE the purchase quarter, on the eligible universe (1,500 largest US stocks, price >= $5, liquid, GICS known). Version a = new position or addition into the five largest weights; version b = to >= 1% of the portfolio; the decisive result averages a and b; fewer than 20 purchases = not measurable. Base rate = pass rate of comparable stocks (same quarter, sector, size third). Lift = recall / base rate. Gate: lift >= 2.0, 90% interval lower end > 1.25, recall >= 25% (plus two baselines not shown to you).

## Result
```
purchases: either 136 (version a 30, b 136); in the eligible universe at t: either 104 (a 28, b 104); in the universe but in a house-excluded industry (A8 2a, not counted): 0; not in the universe: 32
quarters with a counted purchase: 20; bootstrap: 2000 draws of quarters, seed 20261127
DECISIVE (average of versions a and b)       recall   7.4%  base   3.5%  lift   2.12  90% [  0.70,   3.78]
   per version: a: n 28, recall   7.1%, base   3.6%, lift   1.97; b: n 104, recall   7.7%, base   3.4%, lift   2.27
lift >= 2.00: yes; interval lower end > 1.25: NO; recall >= 25%: NO
RECALL GATE: FAIL
```

## Share of counted purchases each criterion rejects (rejections overlap; 'of which measure missing' shown)
```
criterion  rejects  of which measure missing  | description
B1          12.6%     0.0%  | semis, communications equipment, tech hardware (GICS industries)
B3a         41.3%     0.0%  | gross margin TTM >= median of the B1 stocks
B3b         46.2%     0.0%  | gross margin TTM not below a year ago
B4a         21.6%     1.0%  | net debt / EBITDA TTM < 2
B4b          3.4%     0.5%  | FCF margin TTM > 0
P1          59.3%     0.0%  | price / FY2 consensus EPS <= 20
A1           6.5%     0.0%  | software, IT services, internet
B1g          9.8%     0.0%  | B1 plus electronic components (full form)
B3a_3       57.4%     0.0%  | gross margin in the top third (full form)
B4a_1       28.6%     0.0%  | net debt / EBITDA < 1 (full form)
B4a_3       13.7%     0.0%  | net debt / EBITDA < 3 (full form)
P1_15       81.5%     0.0%  | price / FY2 EPS <= 15 (full form)
A2           6.0%     0.0%  | FY2 / FY1 EPS growth >= 0 (full form)
```
