# Result report: Relative value pairs, two versions (synthetic test pod)

Author's report, 2026-11-24. Code: `backtest.py`.

## Headline
- 432 months, 1975-01 to 2010-12.
- **Net Sharpe 1.09**; mean 6.78%/yr, volatility 6.21%, worst drawdown -9.8%.
- Gross Sharpe 1.12; costs 0.17%/yr.
- Net at twice the costs: Sharpe 1.07.

## Eras (net)
| Era | Sharpe | Mean | Vol | Worst DD |
|---|---|---|---|---|
| 1975-1992 | 1.09 | 7.23% | 6.62% | -5.6% |
| 1993-2010 | 1.09 | 6.33% | 5.79% | -9.8% |

## Reading
Strong, identical in both eras, and robust to doubling costs. Averaging the fast and the 6-month versions gives a
smooth return stream. Recommended for the next stage.
