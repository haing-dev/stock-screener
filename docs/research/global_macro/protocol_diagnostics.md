# Diagnostics for the gm-2.0 candidate (design periods only)

- 1975..1989: SR 1.22, Lo-adjusted SR 1.32, skew -0.65, first-order autocorrelation 0.09
  Sortino 2.07, worst month -14.7%, compound growth 11.6%/yr, rolling 36m vol min/median/max 4.9/10.3/13.3%
- 1990..2010: SR 1.63, Lo-adjusted SR 1.49, skew 0.26, first-order autocorrelation 0.12
  Sortino 3.54, worst month -9.8%, compound growth 17.1%/yr, rolling 36m vol min/median/max 6.1/9.5/14.2%

Sharpe 1975-2010 (net) with a top-contributing market removed (positions zeroed, costs kept):
- full book: 1.46; without 2008: 1.44
- without fx_krw (contributed 42% of capital in total): 1.35
- without st_jp_2y (contributed 35% of capital in total): 1.37
- without cm_wti (contributed 28% of capital in total): 1.40
- without bd_us_30y (contributed 28% of capital in total): 1.48
- without cm_aqr_ew (contributed 25% of capital in total): 1.46

Trend family (unit-vol blocks, equal class weight, gross) vs AQR TSMOM factor, 1990-2010 (252 months): our SR 1.22, AQR SR 1.34, correlation 0.66
- smile 1975..1989 (book return by world-equity quintile, %/yr): {1: -1.0, 2: 7.5, 3: 18.0, 4: 8.8, 5: 24.2}
- smile 1990..2010 (book return by world-equity quintile, %/yr): {1: 18.1, 2: 9.5, 3: 14.7, 4: 25.0, 5: 14.4}

1987 crash (Oct-Nov), gross contribution by family x class (percent of capital):
- trend: {'EQ': -6.38, 'FI': -2.06, 'FX': 0.71, 'CM': 1.18}
- econ: {'EQ': -1.58, 'FI': -1.71, 'FX': -1.04, 'CM': -0.39}
- carry: {'EQ': 0.0, 'FI': 0.92, 'FX': -0.05, 'CM': -0.29}
- value: {'EQ': -0.71, 'FI': -0.02, 'FX': -1.04, 'CM': 0.0}
