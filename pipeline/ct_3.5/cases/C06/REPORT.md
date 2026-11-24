# Result report: Pair reversion (synthetic test pod)

Author's report, 2026-11-24. Code: `backtest.py`.

## Headline
- 432 months, 1975-01..2010-12.
- **Net Sharpe 0.89**; mean 4.60%/yr, volatility 5.20%, worst drawdown -7.1%.
- Gross Sharpe 1.09; costs 1.12%/yr.
- Net at twice the costs: Sharpe 0.67.

## Eras (net)
| Era | Sharpe | Mean | Vol | Worst DD |
|---|---|---|---|---|
| 1975-01..1992-12 | 0.87 | 5.03% | 5.78% | -5.7% |
| 1993-01..2010-12 | 0.92 | 4.17% | 4.55% | -6.3% |

## Reading
Strong and even across eras. Costs are material for a spread pod (about a fifth of the gross return) and the result
still holds at double costs, though with a clear cut. The low volatility reflects the 1/sqrt(pairs) sizing.
