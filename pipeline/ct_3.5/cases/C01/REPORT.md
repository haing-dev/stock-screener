# Result report: Ranked carry (cross-asset), synthetic test pod

Author's report, 2026-11-24. Code: `backtest.py` (run as is).

## Headline
- Sample 1975-01..2010-12 (410 months).
- **Net Sharpe 0.87**; mean 9.41%/yr, volatility 10.86%, worst drawdown -26.4%.
- Gross Sharpe 0.91 (mean 9.89%); costs 0.48%/yr.
- At twice the registered costs: net Sharpe 0.82.

## Eras (net)
| Era | Sharpe | Mean | Vol | Worst DD |
|---|---|---|---|---|
| 1975-01..1992-12 | 0.61 | 6.71% | 10.92% | -14.6% |
| 1993-01..2010-12 | 1.13 | 12.17% | 10.77% | -26.4% |

## Reading
Positive in both eras, stronger in the second. Costs are small against the gross edge and doubling them changes
little. The result supports carrying the pod into the next stage.
