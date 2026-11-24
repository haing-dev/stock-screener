# Result report: After-the-fall rule layer (synthetic test pod)

Author's report, 2026-11-24. Code: `backtest.py`.

## Headline
- 432 months, 1975-01..2010-12; rule on (any market) in 154 months, 424 market-months.
- **Net Sharpe 0.03**; mean 0.31%/yr, volatility 10.47%, worst drawdown -32.2%.
- Gross Sharpe 0.03; costs 0.02%/yr; net at twice the costs 0.03.

## Eras (net)
| Era | Sharpe | Mean | Vol | Worst DD |
|---|---|---|---|---|
| 1975-1992 | 0.04 | 0.42% | 11.76% | -30.4% |
| 1993-2010 | 0.02 | 0.20% | 9.02% | -28.0% |

## On months
Net Sharpe 0.05 over the 154 months with a position (mean 0.87%/yr, vol 17.57%).

## Reading
No edge at the registered 20% fall. With 154 on-months there is enough to judge; the rule fails as written.
