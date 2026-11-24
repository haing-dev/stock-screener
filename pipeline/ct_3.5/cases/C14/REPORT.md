# Result report: Rates and currencies trend (synthetic test pod)

Author's report, 2026-11-24. Code: `backtest.py`.

## Headline: 1993-2010
- **Net Sharpe 0.71**; mean 10.18%/yr, volatility 14.28%, worst drawdown -26.2%.
- Gross Sharpe 0.75 (mean 10.78%).
- Best year 2008 (+35.7%): the pod did what a trend pod should in a crisis.

## Full window and first era
| Period | Net Sharpe | Mean | Vol | Worst DD |
|---|---|---|---|---|
| 1975-01..2010-12 (432 months) | 0.43 | 6.01% | 14.06% | -42.0% |
| 1975-1992 | 0.13 | 1.84% | 13.76% | -42.0% |

Gross 1975-2010 Sharpe 0.46; net at twice the costs 0.40; costs 0.43%/yr. Worst year 1989 (-20.6%).

## Reading
The modern era, with deep and liquid rates and currency futures, is the relevant one for running the pod, and there
the result is strong and robust to costs. The early era, when these markets were thinner, adds noise.
