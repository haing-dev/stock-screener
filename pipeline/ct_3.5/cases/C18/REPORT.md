# Result report: Commodity curve carry (synthetic test pod)

Author's report, 2026-11-24. Code: `backtest.py`.

## Headline (all eight markets)
- 432 months, 1975-01..2010-12.
- **Net Sharpe 0.33**; mean 5.11%/yr, volatility 15.25%, worst drawdown -46.4%.
- Gross Sharpe 0.34; costs 0.13%/yr; net at twice the costs 0.33.

## Eras (net)
| Era | Sharpe | Mean | Vol | Worst DD |
|---|---|---|---|---|
| 1975-1992 | 0.05 | 0.95% | 17.48% | -46.4% |
| 1993-2010 | 0.74 | 9.26% | 12.56% | -25.5% |

## Diagnostic split (net)
Energy legs 0.37 (they start 1983-1990); other legs 0.22.

## Reading
Weak positive over the window, but almost all of it comes after 1992 and the first era is flat with the deepest
drawdown. The energy split is diagnostic only. Weak, era-dependent.
