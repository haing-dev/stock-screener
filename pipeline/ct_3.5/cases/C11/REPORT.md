# Result report: Trend, three horizons (synthetic test pod)

Author's report, 2026-11-24. Code: `backtest.py`.

## Headline
- 432 months, 1975-01..2010-12.
- **Net Sharpe 0.66**; mean 10.20%/yr, volatility 15.42%, worst drawdown -47.9%.
- Gross Sharpe 0.72; costs 0.93%/yr; turnover 55.4x notional a year.
- Net at twice the costs: Sharpe 0.60.

## Eras (net)
| Era | Sharpe | Mean | Vol | Worst DD |
|---|---|---|---|---|
| 1975-1992 | 0.45 | 6.69% | 14.85% | -47.9% |
| 1993-2010 | 0.86 | 13.71% | 15.94% | -38.2% |

## Reading
Positive in both eras, stronger in the second. The 1-month horizon raises turnover, so costs are visible but do not
change the conclusion.
