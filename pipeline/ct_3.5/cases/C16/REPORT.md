# Result report: Bond carry, two versions (synthetic test pod)

Author's report, 2026-11-24. Code: `backtest.py`.

## Headline
- Window 1975-01..2010-12, 432 months.
- **Net Sharpe -0.15**; mean -0.99%/yr, volatility 6.66%, worst drawdown -54.9%.
- Gross Sharpe -0.13; costs 0.12%/yr; net at twice the costs -0.17.

## Eras (net)
| Era | Sharpe | Mean | Vol | Worst DD |
|---|---|---|---|---|
| 1975-1992 | 0.03 | 0.17% | 6.28% | -16.4% |
| 1993-2010 | -0.31 | -2.16% | 7.02% | -52.4% |

## Versions (net, diagnostic only)
Directional -0.23; ranked 0.20.

## Reading
The registered pod fails. The ranked version alone is positive, but the pod is the average by registration and the
version split is reported only; it is not a reason to switch versions after seeing results.
