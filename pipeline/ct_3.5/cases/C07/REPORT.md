# Result report: Cross-asset value (synthetic test pod)

Author's report, 2026-11-24. Code: `backtest.py`.

## Headline
- 432 months, 1975-01..2010-12.
- **Net Sharpe 0.10**; mean 1.51%/yr, volatility 14.64%, worst drawdown -75.7%.
- Gross Sharpe 0.11; costs 0.13%/yr; net at twice the costs 0.09.

## Eras (net)
| Era | Sharpe | Mean | Vol | Worst DD |
|---|---|---|---|---|
| 1975-1992 | 0.47 | 6.69% | 14.25% | -38.3% |
| 1993-2010 | -0.25 | -3.68% | 14.91% | -75.7% |

## By class (net)
EQ 0.18, FX 0.07, CM -0.07.

## Reading
Essentially no edge over the window. The first era is positive; the second loses, with a long drawdown. With an
expanding-history anchor the early years rest on short histories, which the registered rule accepts. Fails.
