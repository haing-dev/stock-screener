---
source_id: MT192
title: "Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.353"
date: 2025-06-27
channel: "Top Traders Unplugged"
url: 
words: 11719
claims: 76
added_by_crosscheck: 9
corrections: 5
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Yoav Git (co-host, systematic trend-following practitioner/researcher; caption spelling 'Yov')", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.353

**Speakers:** Yoav Git (co-host, systematic trend-following practitioner/researcher; caption spelling 'Yov'); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Systematic Investor Ep.353: Niels and Yoav Git review June 2025 CTA performance and discuss four papers (negative correlation 'turbocharging', Quantica equity/trend/gold/bond mixes, SG Trend Indicator and replication, Arthur Seep on trend-following systems). Conclusion: uncorrelated trend with Sharpe similar to 60/40 deserves a large risk share; replication by correlation is meaningless; speed choice matters less than risk-scaling and portfolio diversification.

**Approach:** trend following, CTA, negative correlation, diversification, 60/40, replication, backtesting, time series momentum

**Cross-check completeness estimate of first read:** 0.88 - the first reader caught almost every argument and number in the four papers; misses were minor (G7 remark, Quantica's proxy caveat, recency-bias point, a few history and look-back remarks) and four claims in C05 look misattributed to Niels instead of Yoav.

## Argument map

**Episode thesis:** Across four papers (Galanter on negative correlation, Quantica on equity/trend/gold/bond mixes, SG's trend indicator paper, Arthur Seep on trend-following systems) Yoav Git argues that an asset's value to a portfolio comes from its correlation and capital efficiency, not its standalone Sharpe: trend is zero-correlated to what it trades by construction, has a Sharpe broadly similar to 60/40, and therefore merits a large share of portfolio risk (near 30%) even though the last year or two were poor. He also argues that replication by correlation is meaningless because almost any CTA is 80-90% correlated with the index, so the real question is a manager's added mean return, and that speed choice matters less than risk scaling and portfolio-level diversification. The host adds the allocator's side: committees want long track records and a diversified set of risk mitigators.

### Yoav Git (co-host; systematic trend-following practitioner and researcher (captioned 'Yov', 'Y of Git'))
Fingerprint: #approach/trend_following #approach/diversification_risk_parity #approach/crisis_alpha_convexity #approach/research_robustness_overfitting #approach/portfolio_construction_stacking #approach/replication_indexing #approach/position_sizing_vol_target #approach/behavioral_sentiment
_Speaker note: Recorded around 19 June 2025 (index data as of Wednesday 18 June; US holiday the day before); he was visiting his parents in Israel during the Israel-Iran conflict. Ledger corrections applied: the allocator-justification passage, the list of defensive strategies (option buying, fast trend convexity, trend at the alpha/hedge boundary, quality long-short equity) is his, not the host's; on SG's paper he said the industry has moved slower by checking which speed of the simple indicator correlates with the SG index, not that correlation with slow variants rose over time. Caption: the transcript says 'higher correlation' where lower or negative is meant._

**Worldview premises**
- For a long-term allocation, a strategy with low or negative correlation to the existing portfolio adds risk-adjusted return even with a lower Sharpe, flat or losing, because it lowers overall portfolio volatility; high-volatility negatively correlated strategies are capital efficient, so small allocations hedge meaningfully. _[theoretical, stated; support: Galanter's allocation formula; two-year example where a high-vol manager with about -30% equity correlation beat a multistrat with 12% correlation and stronger returns.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C04-2|C04-2]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C04-3|C04-3]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C05-1|C05-1]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C05-2|C05-2]])
- In real life the hard part for an allocator is justifying a low-Sharpe diversifier to the investment committee even when the maths shows it adds value; the paper does not address that. _[institutional, stated; support: Allocator experience (corrected to him from the ledger).]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C05-3|C05-3]])
- Defensive strategies come in several forms (tail-protect option buying, fast trend with higher convexity like buying options paid for with realised rather than implied volatility, trend at the boundary between alpha and hedge, high-quality long-short equity), each with capacity limits (fast trend programs about 1-2 billion, options). _[empirical, stated; support: Industry knowledge; quality factor traced to Graham and Barra since the 1970s.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C05-4|C05-4]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C05-5|C05-5]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C05-6|C05-6]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C06-1|C06-1]])
- Catastrophe bonds give return streams uncorrelated with 60/40, whereas private equity and private credit are not clearly diversifying because they stay exposed to the same economic factors as long equity. _[theoretical, stated; support: Reasoning from factor exposure; no data.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C06-2|C06-2]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C06-3|C06-3]])
- Trend following is zero correlated to the traded assets by construction because long and short are symmetric, unlike a defensive strategy whose negative correlation may not persist; a tail-protect strategy only works if puts are bought continuously. _[theoretical, stated; support: Construction argument; contrast with option skipping to save money.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C07-1|C07-1]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C07-2|C07-2]])
- Because trend is symmetric and zero correlated it can be overlaid on any long-only exposure (Bitcoin, gold, equities, bonds) and stays additive. _[theoretical, stated; support: Symmetry of long and short positions.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C07-3|C07-3]])
- Bonds were negatively correlated with equities in falling-rate, falling-inflation periods, but the correlation is not stable in inflation; 60/40 had a Sharpe of about 0.76 since 1990 and only about 0.55 since 2000, while CTAs have about 0.5 for 2000-2025, similar and uncorrelated. _[empirical, stated; support: Quoted Sharpe ratios by period; Quantica numbers.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C09-3|C09-3]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C09-4|C09-4]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C09-5|C09-5]])
- Investors judge trend on the last year or two and so miss its structural long-term benefit and zero correlation to 60/40 (recency bias in manager evaluation). _[behavioural, stated; support: Observation of allocators; no survey.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C09-X1|C09-X1]])
- Trend following works at almost all speeds and in commodities, equities and bonds because people buy winners and sell losers; returns come from capturing return autocorrelation and drift; over the last 25 years nearly all speeds and rule types of the three schools (Turtle breakout, European moving average, time-series momentum) made money. _[behavioural, stated; support: Seep's scan of speeds and rule types over 25 years; early crisis-alpha demonstration in 2008.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C13-3|C13-3]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C13-4|C13-4]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C13-5|C13-5]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C12-3|C12-3]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C12-1|C12-1]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C12-2|C12-2]])
- Transparency (the 2011-12 time-series momentum paper, preceded by managers keeping methods secret because a simple rule looks trivial) made trend commonplace and harder to charge for, so many investors are reluctant to pay for it despite its alpha. _[institutional, stated; support: Personal experience at Winton and AHL (anecdote of Anthony Daniels).]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C12-X1|C12-X1]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C13-2|C13-2]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C13-1|C13-1]])
- Almost any CTA is 80-90% correlated with the CTA index, so correlation to a benchmark is not informative for replication and ignores the mean; the relevant question for a manager is the added mean return over a highly correlated, zero-alpha index. _[empirical, stated; support: SG's simple trend indicator is about 80% correlated with the SG CTA index yet returned only 0.43% a year with 16% volatility (Sharpe about 0.03, the host's reading) since 2002; the SG CTA Index has a Sharpe about 0.4 out of sample after costs.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C10-5|C10-5]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C11-1|C11-1]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C11-2|C11-2]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C11-3|C11-3]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C11-5|C11-5]])
- A CTA adds value by raising Sharpe slightly in each market through execution, nonlinear filters, fast/slow switching, cost reduction and risk management. _[experience, stated; support: His working life; no measured decomposition.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C11-4|C11-4]])
- The CTA industry has become slower, and trend constituents decorrelate from the simple SG indicator in high-vol crises (April 2025, Covid, Taper Tantrum) but converge back quickly. _[empirical, stated; support: SG indicator correlations at different speeds, and Commitments of Traders positioning versus trend indicators.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C10-1|C10-1]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C10-2|C10-2]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C10-3|C10-3]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C10-4|C10-4]])
- Volatility estimation and risk scaling was the major innovation in trend following; a 12-month TSMOM equal-weights returns and is optimal for capturing drift unless one has a strong view that autocorrelation varies through the year. _[theoretical, stated; support: Seep's derivation of optimal speed for white noise, AR(1) and fractional ARMA processes.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C15-1|C15-1]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C15-2|C15-2]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C13-6|C13-6]])
- 12-month TSMOM has little positive skew (slightly negative) while its alpha is good. _[empirical, stated; support: Backtest in Seep's paper as he describes it.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C16-2|C16-2]])

**Chain: Why low-Sharpe, negatively correlated assets raise a portfolio's Sharpe**
1. Add a strategy negatively correlated with the existing portfolio, even losing or flat → Overall portfolio volatility falls: Covariance term offsets portfolio variance. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C04-3|C04-3]])
2. Lower volatility with similar mean → Higher risk-adjusted return: Sharpe rises as the denominator falls. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C04-2|C04-2]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C04-3|C04-3]])
3. High volatility of the diversifier → Capital efficiency: small allocations have a meaningful hedging impact: A volatile strategy needs little capital for a given hedge. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C05-1|C05-1]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C05-2|C05-2]])
4. Investors screen on standalone Sharpe → They miss the asset that de-risks the portfolio: The host's restatement of the paper's point. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C06-X1|C06-X1]])
- Evidence: Galanter's formula and a two-year example; the host's 50/50 S&P/Dunn mix near all-time highs with return close to the sum rather than the average.
- Fails when: Negative correlation may not persist (bonds in inflation; defensive strategies may not stay at -30%); allocators need to justify low Sharpe; capacity limits.

**Chain: Why trend deserves about 30% of portfolio risk**
1. Symmetric long/short rules → Trend is zero correlated to the underlying assets by construction: Not a historical accident. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C07-1|C07-1]])
2. 60/40 Sharpe about 0.55-0.76 vs CTA about 0.5 (2000-2025), correlation near zero → Two broadly equivalent, uncorrelated return streams: Efficient frontier is easy to find. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C09-4|C09-4]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C09-5|C09-5]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C14-1|C14-1]])
3. Even a forward Sharpe of 0.7 for 60/40 and 0.3 for CTA → Close to 30% of portfolio risk in trend: Uncorrelated assets are sized by Sharpe relative to each other. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C09-6|C09-6]])
4. Recent poor 1-2 years → Investors underweight trend: Recency bias; structural benefit and zero correlation overlooked. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C09-X1|C09-X1]])
- Evidence: Quantica numbers (Sharpe 0.49 S&P, 0.64 with 40% CTA, 0.72 for one-third each of gold, Treasuries and CTA with 60% equity); Seep's finding of a similar conclusion.
- Fails when: Forward Sharpe of trend falls far below 0.3; the 1990s trend history is a proxy for the SG index; correlation to 60/40 turns positive.

**Chain: Why replication by correlation tells you little**
1. A trivial +1/-1 moving-average crossover (SG trend indicator) → About 80% correlated with the SG CTA index: The industry shares the same underlying trend premium. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C10-5|C10-5]])
2. Picking almost any CTA → 80-90% correlation to the index (unlike 99.99% for SPY vs S&P 500): Correlation range is narrow whatever you pick. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C11-1|C11-1]])
3. Correlation ignores the mean → The simple indicator earned 0.43% a year at 16% vol (Sharpe about 0.03) while the index earned about 0.4 Sharpe: Added mean is what matters; the manager's edge is raising Sharpe slightly per market. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C11-2|C11-2]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C11-3|C11-3]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C11-4|C11-4]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C11-5|C11-5]])
- Evidence: SG indicator live out of sample for 15 years; SG CTA Index Sharpe about 0.4 out of sample after costs (stated by Yoav; the Sharpe of 0.03 is the host's reading from the website).
- Fails when: Manager's added value must be net of costs; a good manager's result is higher but unnamed.

**Chain: How to choose trend speed and combine signals**
1. Trend returns come from autocorrelation and drift → A 12-month TSMOM equal-weights returns and captures drift well: Optimal unless autocorrelation varies through the year. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C13-5|C13-5]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C15-2|C15-2]])
2. Know the underlying process (white noise, AR(1), fractional ARMA) → Optimal speed can be derived: Gives a benchmark though the true process is unknown. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C13-6|C13-6]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C14-4|C14-4]])
3. A signal that currently hedges the rest of the trend book → Tilt risk towards it (e.g. fast momentum in oil because it switches rapidly): Portfolio diversification, not higher standalone alpha. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C15-3|C15-3]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C15-4|C15-4]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C16-1|C16-1]])
- Evidence: Seep's derivations plus his own reasoning; no live test of a speed tilt offered when the host asks.
- Fails when: Autocorrelation structure unknown; tilting could be over-engineered and work only in a backtest (the host's concern).

**Chain: Using known processes to test a backtest for errors and overfit**
1. Run the strategy with a negative lag (look-ahead) → Compare P&L with the theoretically expected Sharpe for a trend system that sees the future: A mismatch signals a bug. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C14-2|C14-2]])
2. Run it on random noise → If some variants make money, the strategy is overfitted: Noise should yield no profit. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C14-3|C14-3]])
3. Simulate known processes → Benchmark for the best achievable performance for a new indicator: Tests new ideas without burning real data. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C14-4|C14-4]])
- Evidence: His own backtesting practice, with Seep's paper as the source of benchmarks.
- Fails when: Real data may not follow the assumed process.

**Decision process**
- [sizing] Put close to 30% of portfolio risk in trend alongside 60/40, based on uncorrelated forward Sharpe of 0.7 versus 0.3.. Why: Zero correlation makes it additive even at a lower Sharpe. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C09-6|C09-6]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C14-1|C14-1]])
- [signal] A beginner can stop at 12-month TSMOM on volatility-adjusted returns; tilt between fast and slow only for portfolio diversification.. Why: TSMOM is near optimal at capturing drift; tilting adds value only when autocorrelation view is strong or a signal hedges the book. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C15-2|C15-2]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C15-3|C15-3]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C13-1|C13-1]])
- [risk] Give more risk to signals or markets that currently hedge the rest of the trend book (negative correlation); many CTAs do not.. Why: Maximises diversification in the portfolio. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C15-4|C15-4]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C16-1|C16-1]])
- [research] Test strategies with negative-lag look-ahead and random-noise runs, and benchmark to simulated known processes.. Why: Detect bugs and overfit. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C14-2|C14-2]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C14-3|C14-3]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C14-4|C14-4]])
- [portfolio] Evaluate a CTA by added mean return over a high-correlation index, not by correlation.. Why: Correlation ignores the mean. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C11-5|C11-5]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C11-4|C11-4]])
- [risk] Estimate volatility and risk-scale positions properly.. Why: The major innovation in trend following. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C15-1|C15-1]])

**Evidence style:** Reads papers closely and restates their mechanisms; uses published Sharpe ratios by period, construction arguments, history of the industry and personal anecdote from Winton/AHL; favours benchmarks and simulation for validation.

**Views at the time**
- (2025-06-19) A program that switches between fast and slow momentum had a better May 2025 than the industry average, though it has been a difficult period for the industry, which is now explaining itself better.. Reasoning: Switching between fast and slow momentum; several good papers (AHL, Seep) appearing. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C04-1|C04-1]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C04-R1|C04-R1]])
- (2025-06-19) Trend is going through a very tough period, but it is wrong to extrapolate the last year or two; its structural benefit and zero correlation to 60/40 remain.. Reasoning: Forward Sharpe of 0.3 for CTA still implies almost 30% of risk in trend. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C09-6|C09-6]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C09-X1|C09-X1]])
- (2025-06-19) Bonds' diversification may not persist because the correlation has been choppy and unstable during inflation.. Reasoning: Bonds were negatively correlated with equities in falling-rate, falling-inflation periods. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C09-3|C09-3]])
- (2025-06-19) With oil switching rapidly, overweight fast momentum in oil to diversify a slow-trend book.. Reasoning: Israel-Iran conflict reversing the longer oil downtrend; diversification, not alpha. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C16-1|C16-1]])

### Niels Kaastrup-Larsen (host, Top Traders Unplugged) (host; CTA industry commentator ('we at Dunn'), runs a daily trend barometer)
Fingerprint: #approach/trend_following #approach/market_internals_leading #approach/manager_selection_allocation #approach/portfolio_construction_stacking #approach/diversification_risk_parity #approach/replication_indexing
_Speaker note: Captions spell his name as 'Neil's Krup Larson'. Four ledger corrections moved the defensive-strategy list to Yoav, but C05-7 (trend non-correlated on average, negatively correlated over rolling 1-3 year windows) and C05-8 (long record of actual data more convincing to a committee than simulations) remain his._

**Worldview premises**
- Trend following is non-correlated to equities on average but can be negatively correlated over rolling 1-3 year windows, as at present. _[empirical, stated; support: His own observation, labelled 'I would imagine'.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C05-7|C05-7]])
- A defensive strategy with a long record of actual data is more convincing to an investment committee than one backed by simulations. _[institutional, stated; support: Allocator experience.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C05-8|C05-8]])
- Investors should screen for assets that de-risk the portfolio (negative correlation at the right time) rather than for standalone Sharpe; his 50/50 S&P 500 and Dunn trend mix is near all-time highs with return close to the sum of the parts. _[experience, stated; support: Dunn's internal monitoring over many years.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C06-X1|C06-X1]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C06-4|C06-4]])
- Diversifying across several liquid risk-mitigating strategies makes sense as regimes change and can be implemented with ETFs; private equity's apparent diversification may be only a lack of pricing. _[theoretical, stated; support: Quantica results; instinct.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C09-1|C09-1]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C09-2|C09-2]])
- The best diversifier to equities changes by period (1990s, 2000-2015, last ten years), though over 1990-2025 bonds were best singly (Sharpe 0.69) and a 60% equity plus one-third each of gold, Treasuries and CTAs gave the best Sharpe (0.72); the bond result was boosted by falling rates through 2021. _[empirical, stated; support: Quantica's quarterly report, read only briefly; trend uses a proxy before the SG Trend Index existed.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C08-1|C08-1]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C08-2|C08-2]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C08-3|C08-3]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C08-4|C08-4]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C08-5|C08-5]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C08-6|C08-6]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C08-X1|C08-X1]])
- Breakout, moving-average and TSMOM managers end up with similar long-run performance; there is no evidence one style is better; one should choose a style one trusts and can hold through bad periods. _[experience, stated; support: Public performance records of managers ('performance reports never lie').]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C16-3|C16-3]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C16-4|C16-4]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C16-X1|C16-X1]])
- Multilateral bodies such as the G7 are losing their ability to move the world, so policy-meeting headlines carry less market-moving weight. _[institutional, stated; support: How little the June 2025 summit registered; no data.]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C02-X1|C02-X1]])
- Many trend managers spread risk across about 20 horizons with equal weights; whether tilting across horizons adds real out-of-sample value remains open. _[experience, stated; support: His reading of the research he has access to (20-day versus 130 or 260-day look-back differ a lot).]_ ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C15-X1|C15-X1]])

**Evidence style:** Industry data (indices, barometer), published studies, Dunn's own monitoring; openly says he and Yoav only skimmed the Quantica report.

**Views at the time**
- (2025-06-19) June 2025: trend returns show high daily volatility and portfolios may be unevenly allocated after April-May position changes; commodity sectors (oil after the Israel-Iran conflict) are reversing the longer downtrend and helping trend, while financial sectors hurt it.. Reasoning: Observation from the models he follows; sector exposure differences. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C03-1|C03-1]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C03-3|C03-3]])
- (2025-06-19) Short-term CTAs did well in April but fell in June, ending on par with trend followers on a vol-adjusted basis.. Reasoning: SG short-term traders index. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C03-2|C03-2]])
- (2025-06-18) Mid-June 2025 numbers: BTOP50 about -3.4%, SG CTA -7.8%, SG Trend -10.8%, short-term traders -4.6% YTD versus MSCI World +5.9% and S&P 500 +2.3% near record highs; trend barometer 48 (neutral, firmer than recent days).. Reasoning: Index data as of Wednesday evening. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C03-4|C03-4]])

### Disagreements
- **Tilting across look-back periods**: Niels Kaastrup-Larsen: Performance differs a lot between a 20-day and a 260-day look-back and many spread risk equally over about 20 horizons; he asks whether a tilt has real-world success or is over-engineered. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C15-X1|C15-X1]]); Yoav Git: A 12-month TSMOM is fine for most; tilt only for portfolio diversification, not standalone alpha. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C15-2|C15-2]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C15-3|C15-3]])
- **How negatively correlated trend is**: Yoav Git: Trend is zero correlated by construction; it is not a hedge whose negative correlation might disappear. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C07-1|C07-1]]); Niels Kaastrup-Larsen: Trend is not really negatively correlated on average but has been negatively correlated over rolling 1-3 year windows, as at present. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C05-7|C05-7]])

### Gaps and conflicts
- The host says he and Yoav only saw the Quantica quarterly report an hour or two earlier and have not read it in detail, so all Quantica Sharpe figures are second-hand and from a skim. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C08-3|C08-3]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C08-4|C08-4]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C08-6|C08-6]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C07-R1|C07-R1]])
- Quantica's trend result for the 1990s uses a proxy because the SG Trend Index does not exist before 2000, so the full-period trend Sharpe depends on a constructed series. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C08-X1|C08-X1]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C08-3|C08-3]])
- The paper's quoted 'higher correlation' is probably a slip for lower or negative correlation. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C04-2|C04-2]])
- The 'almost 30% of risk in trend' figure uses a simple two-asset logic with assumed forward Sharpes of 0.7 and 0.3 and ignores costs, leverage limits and capacity. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C09-6|C09-6]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C06-1|C06-1]])
- SG's simple indicator is shown with a Sharpe of about 0.03 (host) while the CTA index is about 0.4 (Yoav); the comparison mixes cost-free indicator and after-cost index and does not state that the indicator figure is gross. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C11-2|C11-2]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C11-3|C11-3]])
- Statement that trend works at almost all speeds over 25 years is from Seep's paper, said to have been read in an early draft; no figures are given. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C13-3|C13-3]])
- Private equity and private credit are called not diversifying on factor-exposure reasoning; no evidence beyond that. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C06-3|C06-3]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C09-2|C09-2]])
- Whether a speed tilt works out of sample is left unanswered when the host asks; the answer shifts to portfolio diversification. ([[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C15-X1|C15-X1]], [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C15-3|C15-3]])

### Forward-looking inputs (reader synthesis)
(reader) Yoav treats forward Sharpe assumptions for 60/40 (about 0.7) and CTA (about 0.3), and the correlation between them (near zero), as the inputs that fix trend's share of risk; the stability of the stock-bond correlation (falling versus rising inflation) as the input that decides whether bonds keep diversifying; and cross-market signal correlation inside the trend book as the input for speed tilts. The host watches the trend barometer (48, neutral), sector contributions (oil reversing, financials hurting) and short-term versus trend indices. Horizon is multi-year for allocation and weeks for the trend book.

### Reader inferences (not stated by the speakers)
- (reader) Yoav's argument is a portfolio-variance one: size follows correlation and capital efficiency, so a strategy with Sharpe near half of 60/40's can still deserve a third of risk; this contradicts the common screening by standalone Sharpe.
- (reader) His replication point implies that high correlation to a trend index is a weak test of manager quality, and the useful test is net-of-cost added Sharpe relative to a transparent trend benchmark.
- (reader) The two speakers diverge in emphasis: Yoav on mathematical structure (zero correlation by construction, optimal speed), Niels on empirical track records and allocator practicalities.
- (reader) Both agree that the poor 2025 YTD CTA returns are not evidence against the long-run case; both warn against extrapolating the past one or two years in either direction (bonds in 1990-2021, trend in 2024-25).

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | Disclaimer, intro; free bond data sources (MarketWatch yield curves, cbonds) |
| C02 | 0 | nothing actionable: AI site, book, G7, wealth report, lottery |
| C03 | 4 | June 2025 CTA update: volatility, short-term managers, commodities vs financials, index numbers |
| C04 | 3 | May experience of fast/slow switching; paper 1 (negative correlation) premise and examples |
| C05 | 8 | Paper 1 results; allocator constraints; types of defensive strategies |
| C06 | 4 | Capacity of defensive strategies, cat bonds, private equity; 50/50 trend and S&P |
| C07 | 3 | Zero correlation by construction; overlay on long-only assets; start of Quantica paper |
| C08 | 6 | Quantica design and Sharpe results for CTA, gold, bonds and the three-way mix |
| C09 | 6 | Diversifying the diversifiers, bond correlation caveat, 60/40 vs CTA Sharpe, risk share |
| C10 | 5 | SG Trend Indicator paper: industry slowing, decorrelation episodes, replication correlation |
| C11 | 5 | Replication meaning, indicator returns, CTA Sharpe, value of manager alpha; start of Seep paper |
| C12 | 3 | Seep paper history: Turtles, European school, TSMOM; secrecy and 2008 anecdotes |
| C13 | 6 | TSMOM, results across schools, behavioral basis, autocorrelation and drift, optimal speed |
| C14 | 4 | Combination with 60/40 and backtest benchmark methods (lead, noise, simulation) |
| C15 | 4 | Lookback weighting, volatility scaling, TSMOM optimality, diversification tilt |
| C16 | 4 | Fast/slow overallocation for diversification, skew, schools converge, trust in method |
| C17 | 0 | nothing actionable: thanks, show notes, outro |

## Claims

### C01
- **Yoav Git** MarketWatch offers downloadable yield-curve data as a free source for bond history.  #mech/new
  > market watch as a website uh gives you a lot of u yield curves data which is really nice and you can download the CSVs
  indicator: yield curves (MarketWatch) · asset: rates · testable: yes: data availability · confidence: high
  ^MT192-C01-1
- **Yoav Git** The registration-based cbonds website provides bond data including volumes and issuance.  #mech/new
  > the other website which you need to register but it's also very good is seabbond.com.
  indicator: cbonds volumes and issuance · asset: rates · testable: yes: data availability · confidence: medium
  ^MT192-C01-2

### C02
- **Niels Kaastrup-Larsen** Multilateral bodies such as the G7 are losing their ability to move the world, as shown by how little the June 2025 summit registered, in a world dominated by a few individuals, narratives and social media; so policy-meeting headlines carry less market-moving weight.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > these big institutions that we've been used to um where they you know had pretty significant power and people would listen to every single word that came out from these uh meetings.
  asset: multi · testable: no - impressionistic judgement from one summit · confidence: low
  ^MT192-C02-X1

### C03
- **Niels Kaastrup-Larsen** After the April and May position changes, June 2025 trend returns showed high daily volatility and portfolios may be unevenly allocated across sectors.  #mech/crowding_positioning _(time-bound view)_
  > the daily volatility is actually pretty meaningful in the uh in the returns
  indicator: trend portfolio risk allocation · asset: multi · horizon: weeks · conditions: after April/May reversals · testable: partly: needs position data · confidence: low
  ^MT192-C03-1
- **Niels Kaastrup-Larsen** Short-term CTAs did well in April but then fell in June, ending up on par with trend followers on a vol-adjusted basis.  #mech/cycle_persistence _(time-bound view)_
  > while short-term managers did well in April as from memory uh maybe even in May from memory, they're certainly catching up to u the downside uh uh to the trend followers uh in June.
  indicator: SG Short-Term Traders index, SG Trend index · asset: multi · horizon: weeks · testable: yes: index data · confidence: medium
  ^MT192-C03-2
- **Niels Kaastrup-Larsen** In June 2025 commodity sectors, especially oil after the Israel-Iran conflict, were reversing the longer downtrend and helping trend, while financial sectors were hurting it.  #mech/cycle_persistence _(time-bound view)_
  > commodities are doing so much better than financials this month. Uh it's really the financials that are causing a problem.
  indicator: oil, financial futures · asset: commodities · direction: long oil reversal · horizon: weeks · conditions: geopolitical oil shock against prior downtrend · testable: partly: sector P&L attribution · confidence: medium
  ^MT192-C03-3
- **Niels Kaastrup-Larsen** Mid-June 2025 trend indices were down for the year: BTOP50 about -3.4 percent, SG CTA -7.8, SG Trend -10.8, short-term traders -4.6, while MSCI World was +5.9 and the S&P 500 +2.3 percent near record highs; trend barometer 48 (neutral).  #mech/cycle_persistence _(time-bound view)_
  > Sockchen trend up about half a percent uh down 10.8% for the year.
  indicator: BTOP50, SG CTA, SG Trend, SG Short-Term Traders, trend barometer · asset: multi · horizon: months · testable: yes: index data · confidence: high
  ^MT192-C03-4

### C04
- **Yoav Git** A program that switches between fast and slow momentum had a better May 2025 than the industry average.  #mech/cycle_persistence _(time-bound view)_
  > tends to switch between fast and slow momentum. So, um it was having a sort of a much better time.
  indicator: fast/slow momentum switching · asset: multi · horizon: weeks · testable: partly: single-manager anecdote · confidence: low
  ^MT192-C04-1
- **Yoav Git** A paper on adding negative correlation shows that for a long-term allocation an asset with lower Sharpe but low or negative correlation to the existing portfolio can add more risk-adjusted return than a higher-Sharpe asset (transcript says 'higher correlation', probably a slip).  #mech/risk_management
  > sometimes it's better to have a lower sharp and have a higher correlation.
  indicator: correlation, Sharpe ratio · asset: multi · horizon: years · testable: yes: two-asset allocation formula · confidence: medium
  ^MT192-C04-2
- **Yoav Git** A negatively correlated long-term strategy improves the portfolio's risk-adjusted return even if it is flat or loses money, because it lowers overall portfolio volatility.  #mech/risk_management
  > if you have long-term uh strategy with negative correlation, you really want to even if it is losing money, even if it is flat, it will add to your risk adjusted returns
  indicator: negative correlation · asset: multi · direction: add negatively correlated strategy · horizon: years · testable: yes: formula and backtest · confidence: high
  ^MT192-C04-3
- **Yoav Git** Yoav sees the CTA industry as having improved how it explains itself, with several good papers appearing (AHL, Galanter, Seep), after a difficult period for returns.  #mech/new _(added by map cross-check, time-bound view)_
  > I think the industry has upped its game in terms of explaining what it is doing which I think is very nice.
  asset: multi · horizon: 2025 · conditions: difficult performance period for the industry · testable: no · confidence: medium
  ^MT192-C04-R1

### C05
- **Yoav Git** High-volatility negatively correlated strategies are capital efficient: even small allocations make a meaningful hedging impact.  #mech/risk_management
  > of the nice things about high volatility products is that they give you capital efficiency.
  indicator: strategy volatility · asset: multi · direction: small allocation to high-vol hedge · horizon: years · testable: yes · confidence: medium
  ^MT192-C05-1
- **Yoav Git** In the paper's two-year example, a high-vol manager with about -30 percent equity correlation but lower standalone returns added more Sharpe to an equity portfolio than a multistrat with 12 percent correlation and stronger returns.  #mech/risk_management _(time-bound view)_
  > even though it added, you know, less standalone expected returns, it still added quite a bit to your portfolio.
  indicator: correlation to equity portfolio · asset: equities · horizon: years · conditions: recent two years · testable: yes: replicate example · confidence: medium
  ^MT192-C05-2
- **Niels Kaastrup-Larsen** Allocators face a real-world constraint: a low-Sharpe diversifier must be justified to an investment committee even when the maths says it adds value.  #mech/behavioral
  > even if you are a mathematician and you think oh that really adds value to your portfolio you need to justify it to your investment committee.
  asset: multi · horizon: years · testable: no: behavioral · confidence: high
  **Correction (cross-check):** Probable wrong speaker. The speaker who lists the defensive strategies (option buying, fast trend, trend, quality) is Yoav: in C06 Niels asks 'is there anything you have come across' and Yoav answers 'the strategies that I mentioned', and Niels says 'you mentioned that there are other things'. The allocator-justification passage is part of the same unbroken paragraph. → Yoav Git says the real-life difficulty for an allocator is justifying a low-Sharpe diversifier to the investment committee even when the maths shows it adds value, which the paper does not address.
  ^MT192-C05-3
- **Niels Kaastrup-Larsen** Fast trend following is like buying options paid for with realised rather than implied volatility, giving higher convexity as a defensive strategy.  #mech/risk_premium
  > fast trend has got much higher convexity and it's a little bit like buying uh buying options but with with realized volatility rather than implied volatility.
  indicator: fast trend · asset: multi · direction: fast trend as crash hedge · horizon: weeks · testable: yes: convexity of fast trend vs options · confidence: medium
  **Correction (cross-check):** Probable wrong speaker: Yoav, the same speaker who later refers to 'the strategies that I mentioned'. → Yoav Git says fast trend has higher convexity and is like buying options paid for with realised rather than implied volatility.
  ^MT192-C05-4
- **Niels Kaastrup-Larsen** Trend following sits on the boundary between hedge and alpha: zero correlated to underlying markets and with positive expected return.  #mech/risk_premium
  > trend trend following is not only zero correlated to the underlying markets but also has a positive alpha.
  indicator: trend following · asset: multi · horizon: years · testable: yes · confidence: high
  **Correction (cross-check):** Probable wrong speaker: Yoav; Niels's own turn begins at 'Now obviously finding a strategy...' where he says trend is not really negatively correlated. → Yoav Git says trend following crosses the boundary between alpha and hedge: zero correlated to underlying markets with positive alpha.
  ^MT192-C05-5
- **Niels Kaastrup-Larsen** Long-short equity with a high-quality tilt is another defensive strategy with a long history.  #mech/risk_premium
  > long short equity with uh tilt towards high quality stocks
  indicator: quality factor · asset: equities · direction: long high quality, short low quality · horizon: years · testable: yes: factor returns in equity drawdowns · confidence: medium
  **Correction (cross-check):** Probable wrong speaker: Yoav, part of the list of defensive strategies he gives. → Yoav Git lists long-short equity tilted to high-quality stocks as another defensive strategy.
  ^MT192-C05-6
- **Niels Kaastrup-Larsen** Trend following is non-correlated to equities on average but can be negatively correlated over rolling 1 to 3 year windows, as at present.  #mech/cycle_persistence _(time-bound view)_
  > We're non-correlated but we can be negative correlated at times.
  indicator: rolling correlation of trend vs equities · asset: multi · horizon: years · testable: yes: rolling correlations · confidence: medium
  ^MT192-C05-7
- **Niels Kaastrup-Larsen** A defensive strategy with a long record of actual data is more convincing to a committee than one backed by simulations.  #mech/research_method
  > being able to uh essentially provide evidence that's not based and simulations and what have you uh is is should be uh you know uh valued quite highly.
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT192-C05-8

### C06
- **Yoav Git** Fast trend programs run about 1 to 2 billion and face capacity limits because of trading churn; option-based defensive strategies also have capacity limits.  #mech/risk_management
  > there is a capacity because the amount of trading
  indicator: fast trend capacity · asset: multi · testable: partly: needs trading cost data · confidence: medium
  ^MT192-C06-1
- **Yoav Git** Catastrophe bonds give return streams uncorrelated with 60/40.  #mech/risk_premium
  > you know catastrophe bonds in uh in in in my fixed income universe
  indicator: catastrophe bonds · asset: credit · direction: long cat bonds as diversifier · horizon: years · testable: yes: cat bond index · confidence: medium
  ^MT192-C06-2
- **Yoav Git** Private equity and private credit are not clearly diversifying because they remain exposed to the same economic factors as long equity.  #mech/risk_premium
  > I don't think that private equity is a particularly strong diversifier.
  indicator: private equity, private credit · asset: equities · horizon: years · testable: partly: appraisal smoothing hides correlation · confidence: medium
  ^MT192-C06-3
- **Niels Kaastrup-Larsen** A 50/50 mix of the S&P 500 and a Dunn trend program is near all-time highs, with a return close to the sum rather than the average of the two parts.  #mech/risk_management
  > when you blend two things together, you get some kind of average. But in this case, you almost get the sum of the two.
  indicator: 50/50 equities plus trend · asset: multi · direction: combine equity and trend · horizon: years · testable: yes: backtest · confidence: medium
  ^MT192-C06-4
- **Niels Kaastrup-Larsen** When improving an equity portfolio, investors typically screen candidates on standalone Sharpe, but they should look for the asset that de-risks the portfolio, for example one with negative correlation at the right time, even if its own return looks modest.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > They're looking for something with a high sharp because that's what they look for. Uh but what they really should be looking for is something that can truly derisk their portfolio
  indicator: standalone Sharpe vs correlation to existing portfolio · asset: multi · direction: add a de-risking, negatively correlated asset · testable: yes - compare portfolio Sharpe gains when ranking candidates by Sharpe versus by correlation-adjusted contribution · confidence: medium
  ^MT192-C06-X1

### C07
- **Yoav Git** Trend following is zero correlated to the traded assets by construction because long and short are symmetric, unlike a defensive strategy whose negative correlation may not persist.  #mech/risk_management
  > We are by construction sort of zero correlated to the assets that we trade.
  indicator: trend · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT192-C07-1
- **Yoav Git** A tail-protect strategy only works if the puts are bought continuously; skipping them to save money removes protection at the crisis.  #mech/risk_management
  > if you try to save money and you didn't buy the put options exactly when you needed them, then when the crisis comes, you actually don't provide that
  indicator: put option protection · asset: multi · horizon: years · testable: no · confidence: medium
  ^MT192-C07-2
- **Yoav Git** Because trend is symmetric and zero correlated, it can be overlaid on any long-only exposure (Bitcoin, gold, equities, bonds) and stays additive.  #mech/risk_management
  > that gives you the power to sort of strap it on a long only exposure in Bitcoin, in gold, in equities, in bonds
  indicator: trend overlay · asset: multi · direction: long asset plus trend · horizon: years · testable: yes: overlay backtests · confidence: medium
  ^MT192-C07-3
- **Niels Kaastrup-Larsen** The host states that he and Yoav only saw the Quantica quarterly report an hour or two before recording and had not read it in detail, so their summary of its numbers is a first read.  #mech/new _(added by map cross-check)_
  > we only literally uh saw saw this like an hour or two ago
  asset: multi · conditions: Quantica quarterly report just received · testable: no · confidence: high
  ^MT192-C07-R1

### C08
- **Niels Kaastrup-Larsen** Quantica tests trend, gold and Treasuries as equity companions in the best and worst 10 percent of equity periods and in a 60 percent equity plus one-third each mix.  #mech/research_method
  > They look at uh the best uh 10% of equity periods. they look at the worst um uh 10% uh of equity periods
  indicator: best/worst decile equity periods · asset: multi · horizon: years · testable: yes: replicate conditional analysis · confidence: high
  ^MT192-C08-1
- **Niels Kaastrup-Larsen** The best diversifier to equities changes by period (1990s, 2000 to 2015, last 10 years), though consistency appears over the full 1990 to 2025 sample.  #mech/cycle_persistence
  > it's not always going to be the same uh diversifying component that adds the most value to your to your equity portfolio
  indicator: trend, gold, Treasuries · asset: multi · horizon: years · testable: yes: sub-period comparison · confidence: high
  ^MT192-C08-2
- **Niels Kaastrup-Larsen** From 1990 to 2025 a 60/40 equity/CTA mix lifted Sharpe from 0.49 for the S&P 500 to 0.64; gold gave 0.56.  #mech/risk_management
  > If you added instead uh uh to had a 60% equity portfolio and a 40% uh CTA uh allocation, you could increase that to 0.64 uh for your sharp.
  indicator: S&P 500 Sharpe, SG Trend (proxy before index) · asset: multi · direction: add CTA to equity · horizon: years · testable: yes · confidence: high
  ^MT192-C08-3
- **Niels Kaastrup-Larsen** Bonds were the best single diversifier to equities (Sharpe 0.69 for 60/40) over 1990 to 2025.  #mech/risk_premium
  > the best single uh portfolio diversifier uh would have been bonds uh if you had 40% bonds um it would have gone up to 69% uh during that period
  indicator: 60/40 Sharpe · asset: rates · horizon: years · testable: yes · confidence: high
  ^MT192-C08-4
- **Niels Kaastrup-Larsen** Bonds' diversification benefit was boosted by falling interest rates through 2021, so the result may not persist.  #mech/structural_shift
  > for the full part it was in a falling interest rate environment
  indicator: bond returns in falling rates · asset: rates · horizon: years · conditions: falling-rate era to 2021 · testable: yes: split by rate regime · confidence: medium
  ^MT192-C08-5
- **Niels Kaastrup-Larsen** A 60 percent equity portfolio with the 40 percent split equally into gold, Treasuries and CTAs gave the best Sharpe, 0.72.  #mech/risk_management
  > we now just take a third, a third, a third of gold, treasuries, and CTAs. And lo and behold, it actually delivers the best overall portfolio sharp of 72.
  indicator: 60% equities + 13.3% each gold, Treasuries, CTA · asset: multi · direction: diversify the diversifiers · horizon: years · testable: yes · confidence: high
  ^MT192-C08-6
- **Niels Kaastrup-Larsen** Quantica's 1990 to 2025 trend results rely on the SG Trend Index but use a proxy for the 1990s because the index does not exist before then, so the full-period trend Sharpe of 0.64 partly depends on a constructed series.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > Now in terms of trend following they do prefer to use the socken trend index. However it doesn't exist in the 90s. So they are using a proxy for that period.
  indicator: SG Trend Index with pre-history proxy · asset: multi · horizon: years · testable: yes - rerun with alternative trend proxies for the 1990s · confidence: high
  ^MT192-C08-X1

### C09
- **Niels Kaastrup-Larsen** With regimes changing, diversifying across several liquid risk-mitigating strategies makes sense and can be implemented with ETFs.  #mech/risk_management
  > having a diversification across your diversifier, so to speak, um, uh, across your risk mitigating strategies, I think, makes sense.
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT192-C09-1
- **Niels Kaastrup-Larsen** Private equity's apparent diversification may be only lack of pricing, not true diversification.  #mech/risk_premium
  > some people think that private equity is diversifying but to me it's still equities
  indicator: private equity · asset: equities · horizon: years · testable: partly: appraisal smoothing · confidence: medium
  ^MT192-C09-2
- **Yoav Git** Bonds are negatively correlated with equities in falling-rate, falling-inflation periods, but the correlation is not stable during inflation.  #mech/risk_premium
  > during periods of inflation, you have you have issues about that correlation staying negative.
  indicator: stock-bond correlation · asset: rates · horizon: years · conditions: inflation regimes · testable: yes · confidence: high
  ^MT192-C09-3
- **Yoav Git** The 60/40 portfolio had a Sharpe of about 0.76 since 1990 but only about 0.55 since 2000.  #mech/structural_shift
  > look from 2000 onwards in the last 25 years it it only has a sharp of something like uh 0.55
  indicator: 60/40 Sharpe · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT192-C09-4
- **Yoav Git** CTAs have a Sharpe of about 0.5 for 2000 to 2025 despite recent weakness, similar to 60/40 and uncorrelated with it.  #mech/risk_premium
  > you're still looking at sharp between say 2000 and 2025 of around 0.5.
  indicator: CTA Sharpe · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT192-C09-5
- **Yoav Git** Even assuming a forward Sharpe of 0.7 for 60/40 and 0.3 for CTA, uncorrelated assets imply close to 30 percent of portfolio risk in trend.  #mech/risk_management
  > that actually means that you should have like almost you know almost 30% of your risk in trend.
  indicator: risk allocation between 60/40 and trend · asset: multi · direction: about 30% of risk to trend · horizon: years · conditions: zero correlation between the two · testable: yes: mean-variance calculation · confidence: medium
  ^MT192-C09-6
- **Yoav Git** Investors judge trend on the last year or two, a poor stretch, and so miss its structural long-term benefit and zero correlation to a 60/40 portfolio (recency bias in manager evaluation).  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > a lot of people are looking at very recent history.
  indicator: trailing 1 to 2 year trend performance · asset: multi · horizon: years · testable: no - behavioural observation · confidence: medium
  ^MT192-C09-X1

### C10
- **Yoav Git** The SG Trend Indicator is a simple moving-average crossover with +1/-1 positions, live out of sample for 15 years.  #mech/research_method
  > a very simple implementation of a very simple trend, you know, crossover + one minus one uh indicator.
  indicator: SG Trend Indicator · asset: multi · horizon: years · testable: yes: public data · confidence: high
  ^MT192-C10-1
- **Yoav Git** The CTA industry has become slower: the correlation of the simple indicator run at slower speeds with the SG index rose over 15 years.  #mech/structural_shift
  > the industry has shifted a little bit to the slow side.
  indicator: correlation of simple crossover at different speeds vs SG CTA Index · asset: multi · horizon: years · testable: yes · confidence: high
  **Correction (cross-check):** Overstated. The speaker says the industry has shifted to the slow side, measured by the correlation of the simple indicator run at different speeds with the SG index; he does not say the correlation with slow variants rose over the 15 years. → Yoav Git says SG's paper shows the industry has become slower, inferred by checking which speed of the simple +1/-1 indicator correlates most with the SG index.
  ^MT192-C10-2
- **Yoav Git** Commitments of Traders positioning vs trend indicators at different speeds also shows the industry getting slower.  #mech/crowding_positioning
  > we can you know correlate the cot report versus different trend indicators
  indicator: CFTC COT report, trend indicators · asset: multi · horizon: years · testable: yes: public COT data · confidence: medium
  ^MT192-C10-3
- **Yoav Git** Trend constituents decorrelate from the simple indicator during high-vol crises (April 2025, Covid, Taper Tantrum) but converge back quickly.  #mech/cycle_persistence
  > during periods when there's high volatility I suspect April would would have been one covid would have been one taper tantrum would have been one
  indicator: dispersion across CTAs · asset: multi · horizon: weeks · conditions: high volatility episodes · testable: yes · confidence: medium
  ^MT192-C10-4
- **Yoav Git** A trivial trend indicator is about 80 percent correlated with the SG CTA index, so replication papers that reach similar correlations add little.  #mech/research_method
  > without doing anything it is 80% correlated to the soj index
  indicator: SG Trend Indicator vs SG CTA index · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT192-C10-5

### C11
- **Yoav Git** Almost any CTA is 80 to 90 percent correlated with the CTA index, unlike the 99.99 percent between SPY and the S&P 500, so replication correlation is not informative.  #mech/research_method
  > it's very difficult to get above 90% but it's also very difficult to get below 80%.
  indicator: correlation to SG index · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT192-C11-1
- **Niels Kaastrup-Larsen** The simple SG trend indicator returned only 0.43 percent a year with 16 percent volatility (Sharpe about 0.03) since 2002 despite high correlation to the index.  #mech/research_method
  > since October of 2002 so more than 20 years the annualized return is 0.43%.
  indicator: SG Trend Indicator return · asset: multi · horizon: years · testable: yes: public data · confidence: high
  ^MT192-C11-2
- **Yoav Git** The SG CTA Index has a Sharpe of about 0.4 out of sample after costs; good managers do better.  #mech/risk_premium
  > we get a sharp of say4 historically and that's out of sample
  indicator: SG CTA Index Sharpe · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT192-C11-3
- **Yoav Git** A CTA adds value by raising Sharpe in each market slightly through execution, nonlinear filters, fast/slow switching, cost reduction and risk management.  #mech/risk_management
  > can we up the sharp in each of the markets that we trade just a tiny bit be it with better execution be it with some nonlinear filters be it with some some clever switching between fast and slow
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT192-C11-4
- **Yoav Git** Correlation to a benchmark ignores the mean, so the question for a manager is the added mean return over the high-correlation, zero-alpha index.  #mech/research_method
  > correlation is when you remove the mean, right?
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT192-C11-5

### C12
- **Yoav Git** The American Turtle approach opens positions on breakouts and exits with an ATR trailing stop, flipping short on the reverse breakout.  #mech/research_method
  > you open a position when there's a breakout uh you wait you have a trailing stop maybe using average true range which is essentially a volatility measure
  indicator: price breakout, ATR trailing stop · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT192-C12-1
- **Yoav Git** The European school (AHL and descendants) uses continuously adjusted positions from moving-average crossovers with volatility and risk scaling.  #mech/research_method
  > a little bit more continuous change of position. It is based on moving average crossover and some volatility adjustment and risk adjustment
  indicator: moving average crossover with vol scaling · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT192-C12-2
- **Yoav Git** Trend following produced large gains in 2008 while other assets lost, an early demonstration of crisis alpha.  #mech/risk_management _(time-bound view)_
  > We made tons of money while everybody was losing money.
  indicator: trend in 2008 · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT192-C12-3
- **Yoav Git** Before the 2011-12 time-series momentum paper, trend managers kept their methods secret because a simple, explainable rule looks trivial and clients would then refuse to pay fees for it; transparency later made trend commonplace and harder to charge for.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > completely simple completely trivial and they're not going to want to pay for us
  asset: multi · horizon: years · testable: no - industry history recollected by a former Winton/AHL staff member · confidence: medium
  ^MT192-C12-X1

### C13
- **Yoav Git** Time-series momentum (Moskowitz-Ooi-Pedersen) takes the sign of volatility-adjusted past year return.  #mech/research_method
  > let's look at a yearon-year returns adjust by volatility and that's what that's what we're going to do.
  indicator: 12-month volatility-adjusted TSMOM · asset: multi · direction: long if past 12m positive · horizon: years · testable: yes · confidence: high
  ^MT192-C13-1
- **Yoav Git** After the TSMOM paper made trend transparent, many investors are reluctant to pay for it despite its alpha.  #mech/behavioral
  > a lot of people are kind of very reluctant to pay for trend following despite the fact that it's very much one of the few pure alpha strategies.
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT192-C13-2
- **Yoav Git** Over the last 25 years nearly all speeds and rule types of the three trend schools made money.  #mech/cycle_persistence
  > over the last 25 years, it really didn't matter which particular implementation you did.
  indicator: Turtle, European MA crossover, TSMOM at multiple speeds · asset: multi · horizon: years · testable: yes: speed grid · confidence: high
  ^MT192-C13-3
- **Yoav Git** Trend works at almost all speeds and in commodities, equities and bonds because people buy winners and sell losers.  #mech/behavioral
  > trend following is a behavioral um uh sort of phenomenon is prevalent at almost all speeds and all asset classes.
  indicator: trend across assets · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT192-C13-4
- **Yoav Git** Trend returns come from capturing return autocorrelation and drift.  #mech/cycle_persistence
  > how you are able to capture two effects. The first one is uh autocorrelation and the second thing is drift.
  indicator: autocorrelation, drift · asset: multi · horizon: years · testable: yes: decomposition · confidence: medium
  ^MT192-C13-5
- **Yoav Git** The paper derives the optimal trend speed for known processes (white noise, AR(1), fractional ARMA), which gives a benchmark though the true process is unknown.  #mech/research_method
  > if I knew that the underlying process was X I knew what to speed to run but the problem is that we don't know what the problem what X is
  indicator: optimal lookback given process · asset: multi · horizon: years · testable: yes: simulations · confidence: medium
  ^MT192-C13-6

### C14
- **Yoav Git** With similar raw Sharpe and zero correlation, combining trend with 60/40 improves overall and bear-market Sharpe and the efficient frontier is easy to find.  #mech/risk_management
  > the raw sharp of the 6040 and the raw sharp of the um of the trend following strategies are actually ballpark similar and the correlation of course is zero.
  indicator: 60/40 plus trend Sharpe · asset: multi · direction: combine 60/40 and trend · horizon: years · testable: yes · confidence: medium
  ^MT192-C14-1
- **Yoav Git** Test a strategy with a negative lag (look-ahead) and compare its P&L to the theoretically expected Sharpe; a mismatch signals a bug.  #mech/research_method
  > I actually lag it in a negative fashion. I say what happens if the if the strategy knows the data ahead of time, how much money are you expected to make?
  indicator: negative-lag backtest · asset: multi · testable: yes · confidence: high
  ^MT192-C14-2
- **Yoav Git** Run the strategy on random noise; if some variants make money the strategy is overfitted.  #mech/research_method
  > Suppose if I'm feeding it noise, right? If I'm feeding it noise, then I expect it to make no money.
  indicator: noise test · asset: multi · testable: yes · confidence: high
  ^MT192-C14-3
- **Yoav Git** Simulating known processes gives a benchmark for the best achievable performance to judge whether a new trend indicator extracts what it should.  #mech/research_method
  > I can simulate some data I can simulate the processes that we wanted to look at and we and now we understand how much am I expected to make you know with the best possible implementation.
  indicator: simulated-process benchmark · asset: multi · testable: yes · confidence: high
  ^MT192-C14-4

### C15
- **Yoav Git** Volatility estimation and risk scaling was the major innovation in trend following.  #mech/risk_management
  > The fact that we risk manage things properly um is is actually very powerful.
  indicator: volatility estimation, volatility scaling · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT192-C15-1
- **Yoav Git** A 12-month TSMOM equal-weights returns and is optimal for capturing drift unless there is a strong view that autocorrelation varies through the year, so beginners can stop there.  #mech/research_method
  > even if the autocorrelations are zero or the autocorrelations are constant across the year then um then tsmon just the yearon-year returns will be optimal.
  indicator: 12-month TSMOM · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT192-C15-2
- **Yoav Git** Tilt between fast and slow signals for portfolio diversification, not standalone alpha.  #mech/risk_management
  > the reason why you might want to tilt between fast and slow predictors is not necessarily to do with what they do on a standalone basis but what they do in your portfolio in terms of diversification
  indicator: fast vs slow trend signals · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT192-C15-3
- **Yoav Git** Signals that currently hedge the rest of the trend book (negative correlation) deserve more risk, which many CTAs do not do.  #mech/risk_management
  > if I have a trend following signal which is actually negatively correlated to my to the rest of my portfolio, that's wonderful.
  indicator: signal-level correlation to portfolio · asset: multi · direction: overweight diversifying signals · horizon: weeks · testable: yes · confidence: medium
  ^MT192-C15-4
- **Niels Kaastrup-Larsen** Many trend managers diversify across look-back periods by spreading risk over about 20 horizons with equal weights, even though performance differs a lot between a 20-day and a 130 or 260-day look-back; whether a tilt across horizons adds real out-of-sample value remains an open question.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > some managers obviously you can just spread it out and say well I use 20 different look back periods and I weight them equally
  indicator: trend look-back horizons (20, 60, 130, 260 days) · asset: multi · conditions: equal weighting avoids look-back selection; tilting risks over-engineering that works only in backtests · testable: yes - compare equal-weight and tilted look-back blends out of sample · confidence: medium
  ^MT192-C15-X1

### C16
- **Yoav Git** With oil switching rapidly, overweight fast momentum in that market because it diversifies a slow-trend book, not because of higher alpha.  #mech/risk_management _(time-bound view)_
  > you might say, I actually want to overallocate to fast momentum now. Not because I necessarily think that fast momentum is a higher alpha.
  indicator: oil, fast momentum · asset: commodities · direction: overweight fast trend in whipsaw market · horizon: weeks · testable: yes · confidence: low
  ^MT192-C16-1
- **Yoav Git** 12-month TSMOM has little positive skew (slightly negative) while alpha is good.  #mech/risk_premium
  > If you look at the at the at this back test it will have a relatively negative negative uh skew.
  indicator: 12-month TSMOM skew · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT192-C16-2
- **Niels Kaastrup-Larsen** Breakout, moving-average and TSMOM managers end up with similar long-run performance; no evidence that one style is better.  #mech/research_method
  > a lot of them over the very long run uh often get to pretty much the same place.
  indicator: manager track records · asset: multi · horizon: years · testable: yes: compare public records · confidence: medium
  ^MT192-C16-3
- **Niels Kaastrup-Larsen** Choose a trend style you can trust and hold through bad periods, otherwise it will not work for you.  #mech/behavioral
  > you're not able to follow it through thick and thin, um, it certainly won't work for you.
  asset: multi · horizon: years · testable: no · confidence: high
  ^MT192-C16-4
- **Niels Kaastrup-Larsen** Early trend managers of the 1970s used volatility breakout rules, before the price breakout of the Turtles and before moving-average and time-series momentum systems became standard, yet long-run performance records of the different styles converge.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > a lot of the managers from the 70s, including Don, you know, started out using volatility breakout
  indicator: volatility breakout · asset: multi · horizon: years · testable: partly - historical track records exist but are not public for all managers · confidence: medium
  ^MT192-C16-X1

