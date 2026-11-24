# Result report: Short-horizon rates trend (synthetic test pod)

Author's report, 2026-11-24. Code: `backtest.py` (2-month look-back).

## Headline
- Period 1975-01..2010-12, 432 months.
- **Net Sharpe 0.34**; mean 3.67%/yr, volatility 10.76%, worst drawdown -33.7%.
- Gross Sharpe 0.37; costs 0.32%/yr; net at twice the costs 0.31.

## Eras (net)
| Era | Sharpe | Mean | Vol | Worst DD |
|---|---|---|---|---|
| 1975-1992 | 0.21 | 2.34% | 11.09% | -33.7% |
| 1993-2010 | 0.48 | 4.99% | 10.44% | -21.1% |

## Reading
Positive in both eras and robust to doubling costs. A useful fast complement to the 12-month trend pods.
