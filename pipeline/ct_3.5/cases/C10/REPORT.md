# Result report: Curve reversion (synthetic test pod)

Author's report, 2026-11-24. Code: `backtest.py`.

## Headline
- 432 months, 1975-01..2010-12.
- **Net Sharpe 0.41**; mean 1.64%/yr, volatility 3.96%, worst drawdown -11.6%.
- Gross Sharpe 0.45; costs (trades and rolls) 0.13%/yr.
- Net at twice the costs: Sharpe 0.38.

## Eras (net)
| Era | Sharpe | Mean | Vol | Worst DD |
|---|---|---|---|---|
| 1975-1992 | 0.40 | 1.37% | 3.38% | -3.8% |
| 1993-2010 | 0.42 | 1.90% | 4.48% | -11.6% |

## Reading
A steady, modest edge in both eras, only the US curve before 1991. Costs, including quarterly rolls on the large
2-year notional, take little of it. Candidate for the spread batch.
