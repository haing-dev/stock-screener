# Result report: Trend, 12-month sign (synthetic test pod)

Author's report, 2026-11-24. Code: `backtest.py`.

## Headline
- Window 1975-01..2010-12, 432 months.
- **Net Sharpe 0.38**; mean 5.75%/yr, volatility 15.22%, worst drawdown -57.8%.
- Gross Sharpe 0.39; costs 0.25%/yr; turnover 14.5x notional a year.
- Net at twice the costs: Sharpe 0.36.

## Eras (net)
| Era | Sharpe | Mean | Vol | Worst DD |
|---|---|---|---|---|
| 1975-1992 | -0.00 | -0.08% | 16.83% | -57.8% |
| 1993-2010 | 0.87 | 11.59% | 13.25% | -30.7% |

## Reading
The full-window result is positive but rests on the second era; the first era is flat with a deep drawdown. Era
instability is the main caveat.
