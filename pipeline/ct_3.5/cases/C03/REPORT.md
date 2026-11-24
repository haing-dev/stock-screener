# Result report: Currency carry, ranked (synthetic test pod)

Author's report, 2026-11-24. Code: `backtest.py`.

## Headline
- 432 months, 1975-01..2010-12.
- **Net Sharpe 0.56**; mean 2.65%/yr, volatility 4.76%, worst drawdown -14.5%.
- Gross Sharpe 0.58; costs 0.10%/yr; net at twice the costs 0.53.

## Eras (net)
| Era | Sharpe | Mean | Vol | Worst DD |
|---|---|---|---|---|
| 1975-01..1992-12 | 0.63 | 3.13% | 4.94% | -11.5% |
| 1993-01..2010-12 | 0.47 | 2.16% | 4.58% | -14.5% |

## Tail
Worst months: 2009-01 -8.8%, 1992-09 -6.8%, 1998-10 -4.9%.

## Reading
Positive in both eras, insensitive to costs. Volatility is low at this sizing; the book-level scaler handles that.
