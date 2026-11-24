# Result report: Soft-print rule layer (synthetic test pod)

Author's report, 2026-11-24. Code: `backtest.py`.

## Headline
- Window 1975-01..2010-12, 432 months; the rule was on in 227 of them.
- **Net Sharpe -0.09**; mean -1.24%/yr, volatility 14.33%, worst drawdown -82.1%.
- Gross Sharpe -0.07; costs 0.22%/yr; net at twice the costs -0.10.

## Eras (net)
| Era | Sharpe | Mean | Vol | Worst DD |
|---|---|---|---|---|
| 1975-1992 | 0.26 | 3.54% | 13.74% | -24.6% |
| 1993-2010 | -0.41 | -6.01% | 14.81% | -77.3% |

## On months
Mean net return in on months -0.18%; hit rate 50%.

## Reading
No edge over the design window. The positive first era does not survive the second, where the long-bond exposure
in on months lost heavily. The rule fails its registered test as written.
