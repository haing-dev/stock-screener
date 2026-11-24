# Result report: Disinflation rule layer (synthetic test pod)

Author's report, 2026-11-24. Code: `backtest.py`.

## Headline
- Sample 1975-01..2010-12, 432 months; rule on in 220.
- **Net Sharpe 0.23**; mean 2.63%/yr, volatility 11.41%, worst drawdown -44.0%.
- Gross Sharpe 0.24; costs 0.15%/yr; net at twice the costs 0.22.

## Eras (net)
| Era | Sharpe | Mean | Vol | Worst DD |
|---|---|---|---|---|
| 1975-1992 | 0.41 | 4.40% | 10.71% | -27.7% |
| 1993-2010 | 0.07 | 0.86% | 12.06% | -44.0% |

## On months
Mean net return 0.44% a month; 54% of on months positive.

## Reading
A small positive edge, concentrated in the high-inflation first era and close to zero in the second. Cheap to run.
Weak; a candidate for the rule-layer batch.
