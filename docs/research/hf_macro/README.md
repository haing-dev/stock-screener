# Macro Compass: hedge-fund-style research round (2026-10-29, research only, live rule unchanged)

Inputs: all 61 files in `Processed Transcripts/Macro Transcripts` read in full by 7 parallel readers -> 1,062 testable rules
(`transcript_rules/batch1-7.md`: rule, speaker, quote, testable logic, data, conflicts, data requests). Galt's raw X posts
were not available (only the rules already in macro/registry.py). Data: ~370 free series (Yahoo ETFs/indexes/futures,
FRED, AQR long-history data sets, Shiller, World Bank pink sheet, CBOE, CFTC, AAII, NY Fed), fetched by
`python -m macro.run research_fetch` (macro/fetch_research.py) into branch macro-data/research. Panel: `rpanel.py`;
lab: `lab.py`, `base.py`. Costs 0.10% per 100% traded; T-bill cash; month-end decisions applied next month.

## Results (CAGR / worst fall / Sharpe)
| | 1966-74 (untouched) | 1975-2000 | 2001-2026 | 1975-2026 |
|---|---|---|---|---|
| S&P 500 | -0.6% / -47% | 15.9% / -30% / 0.62 | 9.0% / -51% / 0.53 | 12.4% / -51% / 0.58 |
| Live 4.1 | 7.6% / -15% | 16.8% / -15% / 0.74 | 11.5% / -20% / 0.81 | 14.1% / -20% / 0.77 |
| Candidate 5.0 | 10.5% / -15% | 19.2% / -15% / 0.97 | 13.2% / -18% / 1.03 | 16.2% / -18% / 0.99 |

Candidate 5.0 = live 4.1 plus:
1. Dollar/oil/rates squeeze score >= 80 -> 0% stocks (Druckenmiller/Hyman).
2. Melt-up with a rate spike (S&P 12m > +25% and 10y +1.5 pts in 12m) -> 0% stocks (Trennert; 1987-type).
3. Inflation sleeve: 10% gold while CPI > 3% and gold above its 10m average; 10% commodities (DBC) while CPI > 3% and
   commodities above their 10m average.
4. Sector momentum tilt (top/bottom 5 of 20 sectors, 1.5x/0.5x) while 100% in stocks.
5. Long Treasuries in a growth-trend cut only if also 10y >= Fed funds (Druckenmiller); else T-bills.
Checks: every decade better than live; neighbours stable (squeeze 75-90, melt-up 20-30% / 1-2 pts, CPI 2.5-4, sleeve
5-20%); shuffled-timing placebo 0/300; bootstrap Sharpe gain <= 0 in 0/2000; at 0.3% costs 15.5%/yr; grid of 300
layer combinations CSCV PBO 0.08. Weak spot: 2015-2026 11.7% vs S&P 13.6%; 2025-04..2026-10 +20% vs +40%.
Today (Oct 2026, data to 10-23): squeeze 82 (oil +70% in 12m, 10y +0.9) -> 0% stocks, 10% commodities, rest T-bills.

## Tested and rejected (did not beat live in both halves)
- Non-stock share: own trend-following sleeve (ETF-built; AQR TSMOM factor looks unrealistically strong before 2000 and
  weak after 2011), gold/commodities/2y instead of bills, half trend. Always-on 10-30% trend or gold: lower return.
- Exposure signals: leading industries (homebuilders+transports+retail), no-Fed-put, real policy rate, hike >= 300bp,
  oil shock, curve re-steepening, earnings yield - bills < 1, narrow leadership, policy uncertainty top 10%, Baa spread
  jump, sell-in-May, (midterm seasonal small +, not adopted).
- Location: US vs ex-US momentum, dollar-trend ex-US/EM, country momentum top 3/5 (great 1997-2011, poor 2012-2026),
  EM rebound, importers on oil spikes. Small positives: China cycle (Korea exports + copper) -> Korea/Taiwan/China;
  commodity boom -> exporters (need MSCI history to confirm).
- Hedges: protective puts (CBOE PPUT, -3%/yr), daily crash cap (worst -16% but -0.5%/yr), AAII sentiment.

## Data requested from the user
MSCI country/region gross USD monthly (Korea, Brazil, China, India, Taiwan, Mexico, Japan, Germany, UK, EM, EAFE,
ACWI ex-US) from inception; Galt's raw X posts; ISM PMI / new orders history.
