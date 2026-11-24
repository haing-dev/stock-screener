# Result report: Equity index relative momentum (synthetic test pod)

Author's report, 2026-11-24. Code: `backtest.py` (6-month window, 1-month gap).

## Headline
- 432 months, 1975-01 to 2010-12.
- **Net Sharpe 0.43**; mean 4.05%/yr, volatility 9.48%, worst drawdown -28.2%.
- Gross Sharpe 0.45; costs 0.23%/yr; net at twice the costs 0.40.

## Eras (net)
| Era | Sharpe | Mean | Vol | Worst DD |
|---|---|---|---|---|
| 1975-1992 | 0.44 | 3.99% | 9.09% | -28.2% |
| 1993-2010 | 0.42 | 4.11% | 9.88% | -17.8% |

## Reading
Positive and remarkably even across eras, with modest costs. A clean candidate for the cross-sectional batch.
