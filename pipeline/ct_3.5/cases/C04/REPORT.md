# Result report: Bond relative momentum 12-1 (synthetic test pod)

Author's report, 2026-11-24. Code: `backtest.py`.

## Headline
- Window 1975-01..2010-12, 432 months, 8 markets.
- **Net Sharpe 0.32**; mean 3.34%/yr, volatility 10.45%, worst drawdown -49.2%.
- Gross Sharpe 0.35; costs 0.30%/yr; net at twice the costs 0.29.

## Eras (net)
| Era | Sharpe | Mean | Vol | Worst DD |
|---|---|---|---|---|
| 1975-1992 | -0.02 | -0.18% | 11.11% | -49.2% |
| 1993-2010 | 0.71 | 6.86% | 9.67% | -19.4% |

## Reading
Modest positive result over the full window, earned entirely in the second era; the first era is flat with a deep
drawdown. Not stable across eras; treat as weak.
