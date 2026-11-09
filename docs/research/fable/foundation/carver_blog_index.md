# Rob Carver blog digest: index

Source: https://qoppac.blogspot.com/p/systematic-trading-start-here.html (index page fetched fine). 24 posts digested into `carver_blog_digest.json`.

Method note: every page was read through WebFetch, which returns a model-written extract rather than raw HTML. Numbers and the one short quote per post therefore come second-hand and were not checked against the page. Treat the quotes as approximate until verified. B14 has no date on the fetched text; B07's per-rule Sharpes are only in chart images, so none are recorded. B22 has no quote.

## Digested posts

| ID | Post (date) | Why chosen |
|---|---|---|
| B01 | How much risk should we take? (2020-03-05) | Core position-sizing formula, risk target as min of four limits, half-Kelly |
| B02 | How fast should we trade? (2020-04-02) | The cost "speed limit" (one third of pre-cost SR), cost in SR units, max trades formula |
| B03 | Fixed expected vol target? (2020-10-06) | Whether to hold portfolio risk constant or let it follow forecast strength; SR 0.93 vs 0.64 vs 0.87 |
| B04 | Do non-binary forecasts work? (2020-07-03) | Evidence for linear forecast scaling and capping at 20 (average absolute 10) |
| B05 | Forecast linearity and mean-reverting vol (2020-09-01) | Vol estimate blend (current plus 10-year average) and why extreme forecasts overshoot |
| B06 | My trading system, Dec 2021 (2021-12-02) | Full spec: rule families, forecast weights, asset-class weights, IDM 2.5, vol blend 70/30, cost filter |
| B07 | Performance by trading rule, April 2022 (2022-05-11) | Divergent vs convergent rule behaviour and how little diversification the trend variants add |
| B08 | Handcrafting: the method (2018-12-07) | Inverse-vol weights, hierarchical grouping, diversification multiplier, risk targeting |
| B09 | Handcrafting: adjusting for Sharpe Ratios (2019-12-10) | How much to tilt weights toward past performance given SR sampling error |
| B10 | Handcrafting: correlation uncertainty (2020-11-03) | Correlation estimation error (about 4x nominal), weight floor 0.1, lookbacks for correlations |
| B11 | Fit weights by instrument, group, pool, or blend (2021-05-27) | Overfitting control: pooling beats per-instrument fits, equal weights competitive |
| B12 | Dynamic optimisation, Mr Greedy part one (2021-10-01) | Instrument selection and integer positions for small accounts (the author later called its numbers wrong) |
| B13 | Dynamic optimisation, Mr Greedy part two (2021-11-19) | Corrected version: shadow cost 250, tracking-error buffer 1.25%, turnover and costs |
| B14 | An exogenous risk overlay (c. 2020) | Crisis risk cap built from max risk, correlations set to 1, 99th-percentile vol |
| B15 | Skew and expected returns (2019-10-21) | Whether skew predicts returns; demeaning choices; most of the effect comes from vol markets |
| B16 | Trend following and skew (2019-02-28) | Skew of trend rules by speed; skew as a predictor of next-period Sharpe |
| B17 | How much should we get paid for skew? (2025-02-06) | Skew premium is small (about 6bp SR per 5 skew units) once leverage is realistic |
| B18 | Skew and kurtosis as trading rules (2020-01-13) | The only skew/kurtosis rule construction with numbers; small gain (about 7bp SR), single market |
| B19 | Kelly versus classical theory (2018-06-08) | Kelly formulas and SR-uncertainty adjusted leverage table |
| B20 | Portfolio optimisation, leverage, allocation, uncertainty (2023-12-12) | Bootstrapped Kelly leverage by outcome percentile; 60/40 example |
| B21 | Dynamic trend following (2020-12-04) | Vol-scaled positions and dynamic stops: Sharpe vs skew trade-off |
| B22 | Vol targeting: a CAgR race (2022-06-27) | Vol-targeted continuous forecasts beat fixed-size trend rules even on CAGR |
| B23 | Absolute or relative momentum? (2019-03-27) | Asset-allocation momentum with risk targeting; shows that apparent gains partly come from extra risk |
| B24 | Trade momentum differently when vol changes? (2021-03-04) | Vol-regime forecast attenuation, L = 2 - 1.5Q; modest Sharpe gains that shrink with a 3-day lag |

## Topic coverage

Position sizing and risk targets (B01, B03, B14, B19, B20), forecast scaling and capping (B04, B05, B24), vol estimation (B05, B06), combining forecasts and weights (B06, B08, B09, B10, B11), costs and speed limits (B02, B06, B11, B13), trend, carry and other rules (B06, B07, B16, B18, B21, B23), skew (B15, B16, B17, B18), portfolio optimisation and handcrafting (B08, B09, B10), overfitting and pooling (B11, B10), instrument selection and dynamic optimisation (B06, B12, B13), leverage and Kelly (B01, B17, B19, B20, B22), risk management and drawdown behaviour (B14, B21, B22).

Gaps caused by fetch failures: the blog's explicit posts on forecast scalar estimation, instrument diversification multipliers (IDM/FDM) and the cost-versus-momentum-speed studies were all blocked. IDM appears only as the figure 2.5 in B06 and the group multiplier in B08. Forecast scalars are not given anywhere in the digest.

## Fetch failures (skipped, not retried)

Each returned "PROVENANCE_REQUIRED: the permission request for this URL was not answered in time; do not retry". All were skipped as instructed.

1. http://qoppac.blogspot.co.uk/2016/01/correlations-weights-multipliers.html (instrument weights, correlations, IDM)
2. http://qoppac.blogspot.co.uk/2016/01/pysystemtrader-estimated-forecast.html (forecast scalars)
3. http://qoppac.blogspot.co.uk/2016/05/optimising-weights-with-costs.html
4. https://qoppac.blogspot.com/2023/01/scream-if-you-want-to-go-faster.html (instrument cost vs momentum performance)
5. https://qoppac.blogspot.com/2023/02/fast-but-not-furious-do-fast-trading.html
6. https://qoppac.blogspot.com/2025/03/very-slow-mean-reversion-and-some.html
7. https://qoppac.blogspot.com/2018/07/vol-targeting-and-trend-following.html
8. https://qoppac.blogspot.com/2023/02/percentage-or-price-differences-when.html
9. https://qoppac.blogspot.com/2015/11/the-three-kinds-of-overfitting.html
10. https://qoppac.blogspot.com/2021/06/optimising-my-way-out-of-small-fund.html
11. http://qoppac.blogspot.co.uk/2016/05/a-simple-breakout-trading-rule.html
12. http://qoppac.blogspot.co.uk/2017/06/some-more-trading-rules.html
13. https://qoppac.blogspot.com/2025/06/quickies-1-overfitting-and-ewmac.html
14. https://qoppac.blogspot.com/2026/11/optimisation-with-costs-oh-please.html (2026 "gold standard" summary)
15. https://qoppac.blogspot.com/2023/03/i-got-more-than-99-instruments-in-my.html
16. https://qoppac.blogspot.com/2025/10/is-degradation-of-trend-following.html
17. http://qoppac.blogspot.co.uk/2017/02/can-you-eat-geometric-returns.html
18. http://qoppac.blogspot.co.uk/2016/09/systematic-risk-management.html
19. http://qoppac.blogspot.co.uk/2014/11/head-to-head-technical-and-fundamental.html

Not fetched at all, worth a later pass if access is granted: the 2026 portfolio-construction series (fitting and pooling failures, structural breaks, SR pooling), "Optimal trend following allocation with uncertainty and demeaned returns" (2022-11), "Clustering and correlations (trading rules)" (2023-05), "Do less liquid assets trend better" (2025-01), and "Replicating CTA returns" (2024-11).


## Added 2026-11-09 (user-approved fetches)
- B25 2025-10 [Is the degradation of trend following a cohort, instrument or environment effect?](https://qoppac.blogspot.com/2025/10/is-degradation-of-trend-following.html)
- B26 2023-01-05 [Scream if you want to go faster (costs vs optimal momentum speed)](https://qoppac.blogspot.com/2023/01/scream-if-you-want-to-go-faster.html)
- B27 2023-02 [Fast but not furious: smuggling in fast rules via buffering and dynamic optimisation](https://qoppac.blogspot.com/2023/02/fast-but-not-furious-do-fast-trading.html)
- B28 2015-11 [Three kinds of overfitting](https://qoppac.blogspot.com/2015/11/the-three-kinds-of-overfitting.html)
- B29 2026-11-04 [Optimisation with costs (2026 series #11)](https://qoppac.blogspot.com/2026/11/optimisation-with-costs-oh-please.html)
- B30 2025-03 [Very slow mean reversion and trading horizons](https://qoppac.blogspot.com/2025/03/very-slow-mean-reversion-and-some.html)
- B31 2018-07 [Vol targeting and trend following](https://qoppac.blogspot.com/2018/07/vol-targeting-and-trend-following.html)

Note: all blog entries are model-written extracts of the pages (WebFetch), not raw text; quotes are unverified.
