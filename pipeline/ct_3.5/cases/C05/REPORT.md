# Result report: Directional carry (synthetic test pod)

Author's report, 2026-11-24. Code: `backtest.py`.

## Headline: core carry (currencies + commodities)
- Sample 1975-01..2010-12, 432 months.
- **Net Sharpe 0.53**; mean 5.51%/yr, volatility 10.45%, worst drawdown -34.4%.
- Net at twice the costs 0.51.
- Eras (net): 1975-1992 Sharpe 0.32 (vol 10.92%, worst DD -30.3%); 1993-2010 Sharpe 0.76 (vol 9.94%, worst DD -34.4%).

## By class (net)
| Block | Sharpe | Mean | Vol | Worst DD |
|---|---|---|---|---|
| FX only | 0.45 | 2.96% | 6.57% | -33.0% |
| CM only | 0.34 | 2.56% | 7.63% | -26.4% |
| FI only | -0.23 | -2.41% | 10.43% | -76.6% |

## All three classes
Net Sharpe 0.22 (mean 3.11%, vol 13.82%, worst DD -51.7%); gross 0.24; at twice the costs 0.21; eras 0.26 / 0.20;
costs 0.19%/yr.

## Reading
Carry pays in currencies and commodities in both eras. The bond block's directional sign is almost always long and
mostly measures the bond market's own path, so it is shown separately above.
