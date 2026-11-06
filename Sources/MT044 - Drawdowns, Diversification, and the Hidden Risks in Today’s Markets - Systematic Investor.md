---
source_id: MT044
title: "Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor - Ep. 354"
date: 2025-07-06
channel: "Top Traders Unplugged"
url: 
words: 14597
claims: 69
added_by_crosscheck: 8
corrections: 2
crosscheck: "opus cross-check"
speakers: ["Niels Kaastrup-Larsen (host, Top Traders Unplugged)", "Rob Carver (independent systematic trader and author)"]
tags: [source, layer0]
---
# Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor - Ep. 354

**Speakers:** Niels Kaastrup-Larsen (host, Top Traders Unplugged); Rob Carver (independent systematic trader and author)

**Summary:** Top Traders Unplugged Ep.354 (late June 2025): Rob Carver on his largest live drawdown, factor and PCA views of trend, Kelly sizing and skew, blending discretionary forecasts, and Ilmanen's paper on bond contrarian vs equity extrapolation. Conclusions: size by Sharpe-consistent vol, trend works where consensus mean-reversion expectations fail, trend timing is too weak to exploit.

**Approach:** trend following, position sizing, Kelly, risk premia, drawdown, behavioral

**Cross-check completeness estimate of first read:** 0.94 - first reader captured essentially all of Carver's methods and numbers; missed Black-Litterman, the luck caveat on manager dispersion, analyst optimism bias and the risk-premium argument, plus two small attribution/emphasis errors.

## Argument map

**Episode thesis:** Rob Carver argues that trend following earns most of its return (about 70%) from trending asset-class indices and the rest from relative trends, that position sizing should follow Kelly logic tempered by Sharpe uncertainty (so no static, concentration-prone sizing), and that trend works best in bonds because forecasters expect rates to mean-revert while equity analysts extrapolate. He also argues that no hidden edge exists beyond marginal gains and error avoidance, and that neither market timing ('missing the best days') nor timing the trend strategy itself holds up. Niels adds the June 2025 drawdown context, shipping-data macro signals, and the case for staying invested through flat spells.

### Rob Carver (Guest co-host; independent systematic futures trader (ex-AHL) and author)
Fingerprint: #approach/trend_following #approach/position_sizing_vol_target #approach/kelly_or_conviction_sizing #approach/behavioral_sentiment #approach/research_robustness_overfitting #approach/replication_indexing #approach/costs_execution #approach/diversification_risk_parity
_Speaker note: Captions render the AQR author as 'Auntie Ilmanan', 'Anthony'; and Rob as the speaker throughout the Q&A. The ledger correction on MT044-C11-2 (the 90% volatility to implied Sharpe 0.9 inference is Rob's, only the 90% volatility remark is Niels's) is applied. A conference speaker's name appears only as 'side'/'s' and is not mapped._

**Worldview premises**
- Trend following is positively skewed at the right time frequency; in Sharpe units a good year is about +2 and a bad year about -1, so a drawdown is best read as a multiple of annual volatility. _[experience, stated; support: Own rule of thumb from live and backtest results (current drawdown -1.3 Sharpe units in 2025; long-run Sharpe 0.5-1).]_ ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C04-2|C04-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C04-3|C04-3]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C03-3|C03-3]])
- Trend works where consensus expects mean reversion and is wrong; mean reversion works where consensus expects trends and is wrong. _[behavioural, stated; support: Ilmanen (AQR) paper on how bond investors are contrarian while equity investors extrapolate.]_ ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C16-1|C16-1]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C17-1|C17-1]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C17-2|C17-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C17-X1|C17-X1]])
- Under Gaussian returns, known Sharpe and unlimited leverage, CAGR is maximised by setting annualised volatility equal to the Sharpe ratio (Kelly); because the Sharpe is uncertain and skew matters, practical targets sit well below it. _[theoretical, stated; support: Pure maths ('you can't argue with it'); his own target is under half of Kelly.]_ ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C09-1|C09-1]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C09-2|C09-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C09-3|C09-3]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C11-3|C11-3]])
- Positive skew raises the optimal volatility target by less than people think, so it cannot easily be converted into higher returns. _[theoretical, stated; support: His blog analysis (not shown).]_ ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C09-4|C09-4]])
- A higher Sharpe gives a higher CAGR with leverage unless the Sharpe gain costs too much positive skew; fixed-stop, static sizing adds skew but loses too much Sharpe. _[empirical, stated; support: Own research, consistent with Saratini and Quantica studies.]_ ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C10-2|C10-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C10-3|C10-3]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C10-1|C10-1]])
- Letting winners run is partly anecdotal bias; at portfolio level it concentrates risk so a reversal causes big losses. _[behavioural, stated; support: Cocoa anecdote; the unnamed trend manager's 2025 loss.]_ ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C10-4|C10-4]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C11-1|C11-1]])
- Only the buy-or-not decision can be discretionary; sizing, holding period, stops and portfolio optimisation should be systematic, and systematic volatility forecasts are hard to beat. _[experience, stated; support: Own judgment and Marshall Wace's practice of feeding forecasts into an optimiser; he doubts his own discretionary skill.]_ ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C12-3|C12-3]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C12-4|C12-4]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C12-R3|C12-R3]])
- There is no big undiscovered secret; manager differences come from marginal gains (beta cleaning, execution, cost-aware optimisation) and avoiding errors, and outcome differences are largely luck. _[experience, stated; support: Years in the industry; cycling 'marginal gains' analogy.]_ ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C14-2|C14-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C14-3|C14-3]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C14-4|C14-4]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C14-X1|C14-X1]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C14-1|C14-1]])
- Capital adequacy rules can cause crises (Basel 2 contributed to 2008), so loosening bank rules or treating crypto as bank assets is risky. _[institutional, stated; support: Personal theory; no data.]_ ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C02-2|C02-2]])
- Timing the market by missing days is absurd; avoiding the worst days beats missing the best days only because equity returns are negatively skewed, and random day-missing raises dispersion; the honest case for equities is the risk premium. _[empirical, stated; support: Asness paper and his simulations.]_ ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C19-1|C19-1]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C19-2|C19-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C19-3|C19-3]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C20-X1|C20-X1]])
- Timing the trend-following strategy itself would need meaningful autocorrelation of annual returns; measured on gross returns it is weak and fades at longer horizons. _[empirical, stated; support: His own gross-return test, plus the Winton paper.]_ ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C20-2|C20-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C21-1|C21-1]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C21-2|C21-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C21-3|C21-3]])
- OTC liquidity can vanish suddenly, and IP leakage between CTAs is minor (staff moves bring a fresh perspective). _[experience, stated; support: His fixed-income experience in 2009; industry knowledge.]_ ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C15-1|C15-1]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C15-2|C15-2]])

**Chain: Trend the asset-class index, then add relative trends**
1. Cap-weighted indices are 'America plus noise' → Build an index weighted equally by volatility (US about 10% rather than 70%): Gives a usable asset-class factor where market cap has no meaning (copper) ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C05-3|C05-3]])
2. Trend signal on the index → Apply that signal to every instrument in the class: Equivalent to trading a metals or equity factor (all long or all short) ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C06-1|C06-1]])
3. Index trend leaves a residual → Add market-neutral residual momentum versus the vol-normalised index over six months: Residual trends at about one-month holding periods but mean-reverts at very short and very long horizons ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C07-1|C07-1]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C07-2|C07-2]])
4. Index plus residual → Results almost identical to plain trend following; about 70% of profit from the index and 30% from relative trends: Decomposition of performance ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C07-3|C07-3]])
5. Index trend explains most profit → A limited-capital investor can trade the main instrument per class (S&P, 5-10y bond, gold) for about 70% of performance: Main instrument carries the factor ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C08-1|C08-1]])
- Evidence: His last book's tests; PCA exercise in crypto (70% Bitcoin) and the equity PCA matching cap weights; metals would likely show two factors (precious and industrial).
- Fails when: Factor structure is unclear outside equities and crypto; a PCA of trend returns (replication) differs from a PCA of markets.

**Chain: Extensions from removing principal components**
1. Remove further components beyond the first → A mean-reverting residual may remain: Less intuitive components may be tradeable ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C08-2|C08-2]])
2. PCA across the whole futures universe → Use it as a trading strategy, not only a risk tool: Novel use he plans to write about ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C08-3|C08-3]])
- Evidence: Untested idea.
- Fails when: Not stated.

**Chain: Kelly sizing to a conservative volatility target**
1. Maximise CAGR → Run annualised volatility equal to the Sharpe ratio (50% vol at Sharpe 0.5): Kelly under Gaussian returns, known Sharpe, infinite leverage ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C09-1|C09-1]])
2. Sharpe is uncertain and returns are skewed → Negative skew needs a lower target, positive skew a higher one but only slightly: Skew changes the optimum less than people assume ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C09-3|C09-3]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C09-4|C09-4]])
3. Uncertain Sharpe → Target well below Kelly (his is under half; most CTAs run lower): Nobody can forecast near-term Sharpe well enough to double the risk target ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C09-2|C09-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C11-3|C11-3]])
- Evidence: Theory plus his own estimate of a 0.5-1 Sharpe.
- Fails when: Assumptions break: non-Gaussian returns, unknown Sharpe, limited leverage.

**Chain: Why static, let-it-ride sizing loses at portfolio level**
1. Static sizing and fixed stops → Extra positive skew: Hanging on to winners with one entry and one stop ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C10-3|C10-3]])
2. Winners grow without trimming → Higher dispersion and concentration: Single-market anecdotes (cocoa) hide portfolio-level concentration ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C10-4|C10-4]])
3. Concentration → Portfolio volatility far above target at peaks, so losses are large when the position reverses: Over-risked relative to the Sharpe actually expected; one manager's volatility reached about 90% ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C11-1|C11-1]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C11-2|C11-2]])
4. 90% volatility under Kelly → Implies expected Sharpe of 0.9 or more, about twice a realistic 0.5: Rob's inference ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C11-2|C11-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C11-3|C11-3]])
- Evidence: Saratini and Quantica studies agree: sharpe loss outweighs skew gain; one named-by-implication manager's 2025 loss.
- Fails when: Some investors can size the fund down; for them the risk may be appropriate.

**Chain: Consensus extrapolation explains where trend works**
1. Forecasters assume rates return to normal (4% expected 2009-2020, down from 6% in 1999) → Rates actually persist: Forecasts always mean-revert, reality does not ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C17-1|C17-1]])
2. Equity analysts extrapolate good and bad times → Momentum is already priced in or overpriced: Emotional extrapolation; separate level optimism bias ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C17-2|C17-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C17-X1|C17-X1]])
3. Expectations differ by asset → Trend works better in bonds than in equity indices, which suffer V-shaped reversals: Bond mean-reversion expectations are wrong; equity momentum is priced ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C18-1|C18-1]])
4. Other contributors → Bond carry, secular decline in rates and rising equity valuations give momentum a tailwind, stronger in bonds: Long-run trends ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C18-2|C18-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C18-3|C18-3]])
- Evidence: Ilmanen's forecast 'whisker' charts and analyst EPS data; trend performance by asset class.
- Fails when: He admits other explanations (carry, secular drift) may do the work; unclear which dominates.

**Chain: Timing the strategy: why it fails**
1. Wish to avoid weak years → Needs meaningful autocorrelation of annual returns: Positive would mean add after good years, negative the reverse ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C20-2|C20-2]])
2. Performance fees → Net returns look more negatively autocorrelated: Fees are paid only when doing well ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C21-1|C21-1]])
3. Gross returns → Weak positive annual autocorrelation that vanishes at longer horizons, too weak to exploit after costs: Strategy timing is as hard as market timing ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C21-2|C21-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C21-3|C21-3]])
- Evidence: His own test on gross momentum returns; Winton paper.
- Fails when: Not stated.

**Decision process**
- [signal] Convert every signal to a forecast on a -20 to +20 scale (10 = average bullish); trend signal on a volatility-equal-weighted asset-class index applied to all instruments, plus residual (relative) momentum over six months.. Why: A single numeric scale lets signals, including discretionary ones, be combined and tested. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C11-4|C11-4]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C06-1|C06-1]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C07-1|C07-1]])
- [sizing] Reduce position size when volatility rises during a trade and scale position with forecast strength (continuous, not discrete pyramiding); target volatility under half of Kelly.. Why: Backtests and the Saratini and Quantica studies favour both adjustments, with forecast scaling having the larger effect; protects against concentration. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C10-R2|C10-R2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C10-1|C10-1]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C09-2|C09-2]])
- [portfolio] Weighted average of systematic and discretionary forecasts (e.g. 50/50 or 70/30), with the weight set by testing the discretionary forecasts as a backtest; Black-Litterman is the heavier alternative.. Why: Simple 'semi-automatic' blending that is verifiable. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C12-1|C12-1]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C12-2|C12-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C11-X1|C11-X1]])
- [risk] Avoid discretionary views on volatility; keep sizing, holding period, stops and optimisation systematic.. Why: Systematic volatility forecasts are hard to beat. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C12-3|C12-3]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C12-4|C12-4]])
- [portfolio] Cost-aware portfolio optimisation across many illiquid markets; avoid trading too fast and over-concentrating.. Why: Separates profitable from less profitable managers; his own past mistakes. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C14-3|C14-3]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C14-4|C14-4]])
- [research] Use simulations (random day-missing) and gross-return autocorrelation tests; test discretionary forecasts like a backtest.. Why: Extrapolates beyond one historical path and removes fee bias. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C19-3|C19-3]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C21-1|C21-1]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C12-2|C12-2]])
- [other] Express P&L as an annualised Sharpe ratio to judge a drawdown against long-run expectations.. Why: Intuitive multiple-of-volatility scale. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C04-2|C04-2]])

**Evidence style:** Own backtests (since 1970) and live results, simulations, and published papers (Asness, Ilmanen, Saratini, Quantica, Winton, Black-Litterman); first-principles maths for Kelly; caveats of anecdotal bias; admits uncertainty and avoids naming managers.

**Views at the time**
- (2025-06 (end of June)) Current live drawdown is his largest and on a par with the worst backtest drawdowns since 1970, about a one-in-10 to one-in-20 year event; year-to-date about -5.5% (-1.3 Sharpe units), though June was up a couple of percent.. Reasoning: Weak trend environment after April 2025 reversals. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C03-3|C03-3]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C04-2|C04-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C04-R5|C04-R5]])
- (2025-06 (end of June)) System takes low risk: longish equities, a little short bonds, energy net flat (short gas, long crude); no start-of-trend signals.. Reasoning: Trend signals are weak across markets. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C03-4|C03-4]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C04-1|C04-1]])
- (2025-06 (end of June)) Concerned about the Fed's capital-rule rollback and the idea of letting Bitcoin and stablecoins sit on bank balance sheets.. Reasoning: Capital rules contributed to past crises. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C02-2|C02-2]])
- (2025-06 (end of June)) Bond trend following should remain stronger than equity trend following.. Reasoning: Consensus expects mean reversion in rates but rates persist; equity momentum is priced in. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C17-1|C17-1]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C18-1|C18-1]])

### Niels Kaastrup-Larsen (Host (Top Traders Unplugged); trend-following manager)
Fingerprint: #approach/trend_following #approach/manager_selection_allocation #approach/nowcasting_data #approach/policy_reaction_central_banks #approach/behavioral_sentiment #approach/crisis_alpha_convexity
_Speaker note: Argues positions on macro signals (shipping data, bank rules), trend-industry performance and staying invested. The Sharpe-0.9 implication in ledger MT044-C11-2 is Rob's, per the ledger correction._

**Worldview premises**
- The Fed's plan to roll back a capital rule that limits bank Treasury holdings raises bank demand for Treasuries but sets up the risk of another bank crisis. _[institutional, stated; support: Bloomberg story and commentary; ironic echo of 2008.]_ ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C02-1|C02-1]])
- Container and box shipping data have been a strong predictor of the US economy in recent years, and a sharp turn lower signals weakening demand. _[empirical, stated; support: Bank of America box survey (11% expecting falling prices in March vs 61% by June); inbound container volume up 10-11% in March-April then down 6.9% in May, read as tariff front-loading.]_ ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C02-3|C02-3]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C02-4|C02-4]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C03-1|C03-1]])
- A one-standard-deviation drawdown for trend is small compared with equity bear markets of about four standard deviations. _[empirical, stated; support: S&P falls of 50-60% in the last 25 years.]_ ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C04-4|C04-4]])
- A strategy that delivers uncorrelated returns in the long run is worth holding through flat spells, and trend followers' best returns often follow their worst. _[experience, stated; support: RG Niederhoffer-related paper from the previous episode; memory of past rebounds.]_ ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C05-1|C05-1]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C20-1|C20-1]])
- News-driven reversals hurt even short-term CTAs in June 2025 after they led trend followers in April, despite trading at about one third of trend followers' volatility. _[empirical, stated; support: Index prints: short-term traders index down 3% in June.]_ ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C05-2|C05-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C03-2|C03-2]])
- Investors can size a high-volatility manager to their own risk appetite, and diversifying across approaches is sensible. _[experience, stated; support: Standard allocator advice; said diplomatically about the 90%-volatility manager.]_ ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C11-R4|C11-R4]])

**Chain: Tariff front-loading to a demand air pocket**
1. Tariff announcements → Importers front-load, so inbound container volume jumps 10-11% in March-April: Pull-forward before a specific date ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C03-1|C03-1]])
2. Front-loading ends → Volume falls 6.9% in May and box price expectations collapse (61% expect falls): Demand pulled forward and weakening ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C02-4|C02-4]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C03-1|C03-1]])
3. Shipping data lead the economy → Signal of a weakening US economy: Strong recent predictive record ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C02-3|C02-3]])
- Evidence: Bank of America box survey and Container Volume Observer data, via OddLots; no statistics on predictive power shown.
- Fails when: Not stated; the tariff pull-forward may distort the signal (implied).

**Decision process**
- [other] Monitors a trend barometer (43, weak but not a disaster) and the SG and BTOP index prints for context.. Why: Frames the trend-industry environment. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C03-2|C03-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C05-2|C05-2]])
- [portfolio] Stay invested in trend through weak spells rather than time entry.. Why: Best returns often follow the worst, and uncorrelated long-run returns justify holding. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C20-1|C20-1]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C05-1|C05-1]])

**Evidence style:** Index data, podcast and newsletter reading (OddLots, Money Stuff, Bloomberg), anecdotes from client conversations, papers by other guests.

**Views at the time**
- (2025-06 (end of June)) June 2025 was choppy for trend (one step forward, one back); oil's spike after the Iran strike and collapse days later whipsawed trend followers; trend barometer at 43.. Reasoning: News-driven reversals. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C03-2|C03-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C05-2|C05-2]])
- (2025-06 (end of June)) US demand is weakening (shipping and box-price data) after tariff front-loading.. Reasoning: Container volumes and survey expectations turned sharply lower. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C02-4|C02-4]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C03-1|C03-1]])
- (2025-06 (end of June)) Fed capital-rule rollback is a setup for a future bank crisis.. Reasoning: Looser rules echo pre-2008. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C02-1|C02-1]])

### Disagreements
- **Is a rebound after bad trend years a usable pattern?**: Niels Kaastrup-Larsen: Best returns often follow the worst, so stay invested and hope for a 2025 rebound. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C20-1|C20-1]]); Rob Carver: Gross annual autocorrelation is only weakly positive and disappears at longer horizons, so neither adding after good years nor after bad years is exploitable. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C21-2|C21-2]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C21-3|C21-3]])
- **Risk of static (unadjusted) sizing at a high-volatility manager**: Rob Carver: Static sizing lets concentration push risk far above target and implies an over-optimistic Sharpe of about 0.9 or more. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C11-1|C11-1]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C11-2|C11-2]]); Niels Kaastrup-Larsen: Investors can size the fund to fit their appetite; the right answer depends on the investor. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C11-R4|C11-R4]])

### Gaps and conflicts
- Ledger fix applied: Saratini and Quantica find both vol-adjusting and forecast scaling help, with forecast scaling (pyramiding) the bigger effect; the original ledger text said differences were small. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C10-1|C10-1]])
- Ledger fix applied: Niels says only that the manager's volatility reached about 90%; the Kelly inference of an expected Sharpe of 0.9 or more (about twice 0.5) is Rob's. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C11-2|C11-2]])
- The long-run Sharpe of 0.5-1 and the 'one-in-10 to one-in-20 year' drawdown label are self-estimates with no data shown. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C03-3|C03-3]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C04-2|C04-2]])
- The 70/30 split between index and relative trends comes from Rob's own book and is not independently reproduced; the equity PCA statement is a guess ('would probably'). ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C07-3|C07-3]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C06-2|C06-2]])
- He says trend works in bonds because investors expect mean reversion, but also lists carry and secular rate declines as explanations and says he does not know which dominates; the behavioural story is not separated from the tailwind story. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C18-1|C18-1]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C18-2|C18-2]])
- Box and container data are claimed to have a strong predictive record, but only a newsletter source and survey readings are given. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C02-3|C02-3]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C02-4|C02-4]])
- Rob says positive skew raises the Kelly target only modestly but also says a Sharpe loss from static sizing outweighs skew; neither is quantified in the episode. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C09-4|C09-4]], [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C10-3|C10-3]])
- Rob calls the IP-leakage risk minor while acknowledging that less systematic and higher-frequency strategies depend more on secrets. ([[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C15-2|C15-2]])

### Forward-looking inputs (reader synthesis)
(reader) Inputs the speakers treat as informative: strength of trend signals across asset classes (currently weak, so low risk); trend of the volatility-equal-weighted asset-class index as the main driver of trend returns; consensus forecasts for rates and equity earnings as contrarian input (forecasters assume mean reversion, so persistence favours bond trend); realised portfolio concentration and volatility relative to target; Bank of America box survey and container volumes as demand nowcasts; bank capital rules as a financial-stability risk. Horizon is months for trend and years for the Sharpe and Kelly arguments.

### Reader inferences (not stated by the speakers)
- (reader) Rob's 70/30 finding implies most trend-following alpha is a factor-timing bet at the asset-class level, which is why replicators and a few-factor view are plausible; his stated caution is that PCA of trend returns differs from PCA of markets.
- (reader) His Kelly and concentration arguments together imply that skew-seeking sizing is a bet on an unusually high Sharpe, so sizing choices are really Sharpe-confidence choices.
- (reader) The consensus-extrapolation story gives a testable prediction: trend should be weaker where forecasters extrapolate (equity indices) and stronger where they assume mean reversion (rates, possibly gold), which matches the post-2000 asset-class record he cites.
- (reader) Niels's reading of shipping data as a demand warning and Rob's low-risk positioning point in the same direction (no strong trend, weakening activity) but are not connected by either speaker.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, weather, Asness podcast recommendation; nothing actionable |
| C02 | 4 | Fed bank capital rule, Basel 2, Bitcoin on bank balance sheets, container and box survey indicator |
| C03 | 4 | container volume reversal, June trend weakness, oil whipsaw, drawdown vs history, low system risk |
| C04 | 4 | positions, Sharpe-unit view of drawdown, skew rule of thumb, equity perspective |
| C05 | 3 | short-term index in June, factor decomposition question, asset-class index construction |
| C06 | 3 | trending an asset class index, PCA of crypto and equities, metals factors |
| C07 | 3 | residual relative momentum, 70/30 split of index vs residual |
| C08 | 4 | limited capital implication, mean-reverting residual, whole-universe PCA, replication argument |
| C09 | 4 | Kelly criterion, practical vol targets, skew and Kelly |
| C10 | 4 | position sizing papers, Sharpe vs skew, concentration and anecdotal bias |
| C11 | 4 | concentration risk, 90% vol manager, forecast scale, semi-systematic question |
| C12 | 4 | blending discretionary forecasts, volatility forecasts, systematic versus discretionary roles |
| C13 | 0 | industry sameness, AHL history and hiring; nothing actionable |
| C14 | 4 | Renaissance hiring, marginal gains, portfolio optimisation, mistakes |
| C15 | 2 | liquidity vanishing, IP contamination and staff moves |
| C16 | 1 | Ilmanen paper intro and expectation formation logic |
| C17 | 2 | bond yield forecasts always mean revert, equity analysts extrapolate |
| C18 | 3 | trend by asset class, carry and secular trends, who is on the other side, Asness best days |
| C19 | 3 | best/worst days argument, trend versus day timing, simulations |
| C20 | 2 | timing trend following, autocorrelation needed |
| C21 | 3 | autocorrelation evidence, fees bias, conclusion on timing; outro |

## Claims

### C02
- **Niels Kaastrup-Larsen** The Fed plans to roll back a bank capital rule that limited Treasury holdings, which raises bank demand for Treasuries but sets up risk of another bank crisis.  #mech/policy_reaction _(time-bound view)_
  > they plan to roll back an important capital rule that gives banks um that they have had to comply with to limit their ability to hold more treasuries
  indicator: bank capital rule on Treasury holdings · asset: rates · direction: Treasury demand up, bank risk up · horizon: years · testable: partly - rule change observable · confidence: medium
  ^MT044-C02-1
- **Rob Carver** Capital adequacy rules can cause crises (Basel 2 contributed to 2008), so loosening or treating Bitcoin and stablecoins as bank assets is a risk Rob is concerned about.  #mech/policy_reaction _(time-bound view)_
  > the the Basel 2 um banking um capital adequacy rules were partly responsible for the last financial crisis
  asset: credit · horizon: years · testable: no - theory · confidence: medium
  ^MT044-C02-2
- **Niels Kaastrup-Larsen** Container and box shipping data (Bank of America box survey) has been a strong predictor of the US economy in recent years.  #mech/slow_reaction
  > containers and boxes. You know, how much is being shipped uh in and out of the US
  indicator: BofA box survey; container volumes · asset: multi · horizon: months · testable: yes - compare with GDP · confidence: low
  ^MT044-C02-3
- **Niels Kaastrup-Larsen** Box price expectations fell sharply: in March 11% of respondents said prices were more likely to fall; by June 61%, signalling weakening demand.  #mech/slow_reaction _(time-bound view)_
  > Okay now we're 3 months later now 61% believe they're going to fall more likely than rise
  indicator: BofA box price survey · asset: multi · direction: Economy weaker · horizon: months · testable: yes - survey data · confidence: medium
  ^MT044-C02-4

### C03
- **Niels Kaastrup-Larsen** US inbound container volume rose about 10-11% in March-April (front-loading before tariffs) then fell 6.9% in May.  #mech/overshoot _(time-bound view)_
  > a 6.9% decrease in inbound US volume last month. Um which is um a big reversal from the 11% and almost 10% increase we saw in March and April
  indicator: US inbound container volume · asset: multi · direction: Imports down after pull-forward · horizon: months · conditions: after tariff deadlines · testable: yes - Container Volume Observer data · confidence: high
  ^MT044-C03-1
- **Niels Kaastrup-Larsen** June 2025 trend returns were choppy (one step forward, one back); the oil surge after the Iran strike and collapse days later whipsawed trend followers; trend barometer at 43.  #mech/overshoot _(time-bound view)_
  > the big surge initially after the uh strike on Iran and then the collapse uh only a few days ago
  indicator: oil price; trend barometer · asset: commodities · direction: Trend losses on reversal · horizon: weeks · conditions: news-driven reversals · testable: yes · confidence: high
  ^MT044-C03-2
- **Rob Carver** Rob's current drawdown is his largest live and about equal to his worst backtest drawdowns since 1970, a one-in-10 to one-in-20 year event.  #mech/research_method _(time-bound view)_
  > this the current draw down is the largest I've seen in live trading, and it's it's kind of on a par with the biggest draw downs in my back test, which go back to 1970
  indicator: drawdown vs backtest · asset: multi · horizon: years · testable: yes - drawdown distribution · confidence: high
  ^MT044-C03-3
- **Rob Carver** Rob's trend signals were weak in mid-2025 (long equities, a little short bonds, flat energies), so the system took low risk instead of piling on positions.  #mech/risk_management _(time-bound view)_
  > my own system disagrees with that and is saying, well, actually still pretty low risk to be honest
  indicator: trend forecast strength · asset: multi · horizon: weeks · conditions: weak signals · testable: yes · confidence: high
  ^MT044-C03-4

### C04
- **Rob Carver** Rob's energy position is net flat (short gas, long crude), with no big risk coming on.  #mech/risk_management _(time-bound view)_
  > I'm short gas but I'm long crude so um you know I'm kind of I could have sort of hedge position in energies effectively
  asset: commodities · direction: Short natural gas, long crude · horizon: weeks · testable: no - snapshot · confidence: medium
  ^MT044-C04-1
- **Rob Carver** Expressing P&L as an annualised Sharpe ratio gives intuition for drawdowns: Rob is at -1.3 Sharpe units for 2025 against a long-run Sharpe of 0.5-1.  #mech/research_method
  > convert your P&L into an annualized sharp ratio
  indicator: annualised Sharpe of performance · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT044-C04-2
- **Rob Carver** Trend following is positively skewed at the right time frequency: a good year is about +2 Sharpe units, a bad year about -1.  #mech/cycle_persistence
  > in a good year I'll make two sharp duration units. bad lose one
  indicator: annual return in Sharpe units · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT044-C04-3
- **Niels Kaastrup-Larsen** A one standard deviation drawdown for trend is small compared with equity bear markets of about four standard deviations.  #mech/risk_management
  > when the S&P 500 is down 50 or 60% in which what we've seen in the last 25 years, that's like four four standard deviation of the annualized volatility
  indicator: drawdown in standard deviation units · asset: equities · horizon: years · testable: yes · confidence: high
  ^MT044-C04-4
- **Rob Carver** Rob's system is still down about 5.5% for calendar 2025 at the end of June, a couple of percent better than the low.  #mech/new _(added by map cross-check, time-bound view)_
  > I'm still down sort of 5 and a half%
  indicator: own YTD return · asset: multi-asset futures · direction: n/a · horizon: year to date · conditions: after April 2025 reversals and a weak 2024 · testable: no · confidence: high
  ^MT044-C04-R5

### C05
- **Niels Kaastrup-Larsen** A strategy can be worth holding through a flat spell if it delivers uncorrelated returns in the long run.  #mech/risk_management
  > even strategies that don't make money for a while might still be a good strategy to have in your portfolio
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT044-C05-1
- **Niels Kaastrup-Larsen** Short-term CTAs were hit in June 2025 by news-driven reversals after doing well in April, despite trading at one third of trend followers' volatility.  #mech/overshoot _(time-bound view)_
  > short-term traders index is down 3% in June and now it's down 5 1/2% in uh for the year
  indicator: short-term traders index vs trend index · asset: multi · horizon: weeks · conditions: news-driven markets · testable: yes - index data · confidence: medium
  ^MT044-C05-2
- **Rob Carver** Rob builds an asset-class index equally weighted by volatility (US weight about 10% not 70% as in a cap-weighted index) to act as a factor.  #mech/research_method
  > I kind of normalize everything by volatility and then equally weight
  indicator: volatility-normalised equal-weight asset class index · asset: multi · testable: yes · confidence: high
  ^MT044-C05-3

### C06
- **Rob Carver** Trend signal on the asset-class index is applied to every instrument, equivalent to trading a metals or equity factor (all long or all short).  #mech/slow_reaction
  > what I then do is say, well, I'm going to trend follow that index
  indicator: asset class index trend · asset: multi · direction: Long all metals when index up · horizon: months · testable: yes - testable with backtest · confidence: high
  ^MT044-C06-1
- **Rob Carver** PCA of crypto shows 70% weight on Bitcoin; in equities PCA and cap weights give similar index; other asset classes are less clear.  #mech/research_method
  > 70% of the weight was coming from Bitcoin. So basically you know crypto you can think of as Bitcoin plus noise effectively
  indicator: first principal component · asset: other · testable: yes · confidence: high
  ^MT044-C06-2
- **Rob Carver** Metals have two drivers: precious metals as a risk-off factor and industrial metals tied to growth, so a PCA would likely give two factors.  #mech/research_method
  > precious metals like gold, silver, platinum that act as kind of riskoff assets like you know Swiss exchange rates and US treasuries
  indicator: gold, silver, platinum vs copper · asset: commodities · direction: Precious up on risk-off; industrials up on growth · testable: yes · confidence: medium
  ^MT044-C06-3

### C07
- **Rob Carver** After trading the index, add a market-neutral residual momentum: long assets beating the vol-normalised index over six months, short underperformers.  #mech/slow_reaction
  > we'd have a relative value strategy on top of that where we'd go long gold and short silver and then add everything up at the end
  indicator: vol-normalised outperformance vs asset class index · asset: multi · direction: Long outperformers, short underperformers · horizon: months · testable: yes · confidence: high
  ^MT044-C07-1
- **Rob Carver** Residual momentum trends at about one-month holding periods but mean-reverts at very short and very long horizons.  #mech/cycle_persistence
  > In the very long run, it mean reverts and in the very short term, it mean reverts
  indicator: residual return vs index · asset: multi · horizon: weeks · conditions: about 1 month horizon · testable: yes · confidence: medium
  ^MT044-C07-2
- **Rob Carver** Index plus residual trend gives results almost identical to plain trend following; about 70% of profit comes from trending the asset-class index and 30% from relative trends.  #mech/research_method
  > you find that the splits about 7030
  indicator: index vs residual attribution · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT044-C07-3

### C08
- **Rob Carver** A limited-capital investor can trade only the main instrument per asset class (S&P, 5-10 year bond, gold or metals) and get about 70% of the performance.  #mech/research_method
  > if you just trade that, you know, you're probably going to be getting about 70% of the performance as if you traded everything on top
  asset: multi · horizon: years · conditions: limited capital · testable: partly · confidence: medium
  ^MT044-C08-1
- **Rob Carver** Removing more principal components could leave a mean-reverting residual that supports a mean-reversion strategy.  #mech/research_method
  > once you start factoring those out as well, you will get to the point potentially where you've got a mean reverting residual, which means you can create a mean reversing strategy
  indicator: residual after removing principal components · asset: multi · testable: yes - proposed · confidence: low
  ^MT044-C08-2
- **Rob Carver** A PCA across the whole futures universe could be used as a trading strategy, not just a risk tool.  #mech/research_method
  > you can run a PCA entire futures universe. So actually equities, bonds, everything together
  indicator: PCA of futures returns · asset: multi · testable: yes - proposed · confidence: low
  ^MT044-C08-3
- **Rob Carver** The replication argument says a few factors explain CTA performance, so those can be traded alone; Rob notes this is PCA of trend returns not of markets.  #mech/research_method
  > if there's only a few factors driving everything well we just need to trade those factors we don't need the other hundred or so instruments
  indicator: PCA of trend system returns · asset: multi · testable: yes · confidence: medium
  ^MT044-C08-4

### C09
- **Rob Carver** Full Kelly says run annualised volatility equal to Sharpe ratio to maximise CAGR, assuming Gaussian returns, known Sharpe and infinite leverage; at Sharpe 0.5 that is 50% vol.  #mech/risk_management
  > you should run your your um system um at a standard deviation equal to SH ratio
  indicator: volatility target = Sharpe · asset: multi · horizon: years · conditions: Gaussian returns, known Sharpe, unlimited leverage · testable: yes - math · confidence: high
  ^MT044-C09-1
- **Rob Carver** Practical volatility targets (Rob's is under half of Kelly) are well below full Kelly because the Sharpe is uncertain.  #mech/risk_management
  > most CTAs, hedge funds are running an even lower vault than I am as well
  asset: multi · testable: yes · confidence: high
  ^MT044-C09-2
- **Rob Carver** Negative skew requires a lower Kelly-type volatility target and positive skew a higher one.  #mech/risk_management
  > If you've got negatively skewed returns, you need to run at a lower volt target. And if you've got positively skewed returns, you should run at a higher volt target
  indicator: return skew · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT044-C09-3
- **Rob Carver** Positive skew raises the optimal volatility target by less than people think, so it cannot be converted into higher returns easily.  #mech/risk_management
  > it doesn't actually improve um increase your standard deviation as much as you think it your standard deviation target as much as you think it does
  indicator: skew · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT044-C09-4

### C10
- **Rob Carver** Position sizing studies (Saratini and Quantica) find that both volatility-adjusting positions during a trade and scaling with forecast strength help in a long backtest, with small differences.  #mech/risk_management
  > if if volatility increases then I you know reduce my position size throughout the life of a trade
  indicator: volatility-adjusted sizing; forecast-scaled sizing · asset: multi · horizon: years · testable: yes · confidence: high
  **Correction (cross-check):** Says differences are small between both sizing adjustments; Carver says the differences are not massive but that pyramiding (scaling position with forecast strength) has a much bigger effect than volatility adjustment. → Position sizing studies (Saratini and Quantica) find that both volatility-adjusting positions during a trade and scaling with forecast strength help over a long backtest; differences are not large, but scaling with forecast strength (pyramiding) has the bigger effect.
  ^MT044-C10-1
- **Rob Carver** Higher Sharpe gives higher CAGR with leverage unless it costs too much positive skew.  #mech/risk_management
  > as a rule of thumb if you can get a higher sharp you can get a higher CAGR assuming you've got leverage um unless you give up too much positive skew in the process of doing it
  indicator: Sharpe, skew · asset: multi · horizon: years · conditions: needs leverage · testable: yes · confidence: high
  ^MT044-C10-2
- **Rob Carver** Fixed-stop sizing that ignores changing volatility adds positive skew but loses too much Sharpe, giving lower CAGR.  #mech/risk_management
  > that does give you extra positive skew but you you lose too much in sharp ratio
  indicator: fixed stop-loss sizing · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT044-C10-3
- **Rob Carver** Letting winners run (cocoa anecdote) is anecdotal bias; at the portfolio level it increases dispersion and concentration, so a reversal causes big losses.  #mech/behavioral
  > at a portfolio level um you know all that's going to do is increase the dispersion of your trades
  indicator: position concentration · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT044-C10-4
- **Rob Carver** Rob's own system reduces position size during a trade when volatility rises, and also scales with forecast strength, unlike some managers.  #mech/new _(added by map cross-check)_
  > if if volatility increases then I you know reduce my position size throughout the life of a trade
  indicator: realised volatility during a trade; forecast strength · asset: multi-asset futures · direction: neutral · horizon: life of a trade · conditions: volatility rises after entry · testable: yes: compare dynamic vs static sizing backtests · confidence: high
  ^MT044-C10-R2

### C11
- **Rob Carver** Concentration lifts portfolio volatility above the intended target, so the manager is over-risked at peaks.  #mech/risk_management
  > allow your portfolio to become too concentrated in one place then the standard deviation is going to be a lot higher
  indicator: portfolio volatility vs target · asset: multi · testable: yes · confidence: high
  ^MT044-C11-1
- **Niels Kaastrup-Larsen** A well-known trend manager with static sizing reached about 90% volatility, which implies a belief in a Sharpe of 0.9 or more, about twice a realistic 0.5.  #mech/risk_management _(time-bound view)_
  > the volatility of that product or that fund uh reached something like 90% at times because of the static position sizing
  indicator: fund volatility · asset: multi · horizon: years · testable: yes · confidence: high
  **Correction (cross-check):** Attributes the Sharpe implication to Niels; Niels only says the fund's volatility reached about 90% because of static sizing. The inference that 90% vol implies an expected Sharpe of 0.9 (about twice a realistic 0.5) is Carver's, from Kelly sizing. → Niels: a well-known trend manager using static position sizing saw fund volatility reach about 90% at times. Carver: under Kelly sizing that implies an expected Sharpe of 0.9 or more, about twice a realistic 0.5.
  ^MT044-C11-2
- **Rob Carver** Nobody can forecast near-term Sharpe accurately enough to justify doubling the risk target.  #mech/risk_management
  > if you think your risk is now 90% that implies you think your current expected sharp 0.9
  asset: multi · testable: yes · confidence: medium
  ^MT044-C11-3
- **Rob Carver** Rob scales every signal into a forecast from -20 to +20 (10 = average bullish) so systematic and discretionary views can be combined.  #mech/research_method
  > essentially the way my system works is I convert everything into a forecast and a forecast is just a number and it's a scaled number
  indicator: scaled forecast · asset: multi · testable: yes · confidence: high
  ^MT044-C11-4
- **Rob Carver** Black-Litterman is the classic framework for blending discretionary return views into a systematic (e.g. market-cap) portfolio; Carver's simpler alternative is a weighted average of scaled forecasts.  #mech/research_method _(added by opus cross-check)_
  > there was seminal paper written by Black Litterman in the early '9s, I think, where they they basically took the kind of standard portfolio construction technology
  asset: multi · testable: yes - blended portfolios can be backtested against pure systematic · confidence: high
  ^MT044-C11-X1
- **Niels Kaastrup-Larsen (host)** Niels says investors in a very high-volatility trend fund can size their own allocation to suit their risk appetite, which he always suggests.  #mech/new _(added by map cross-check)_
  > people can can size it appropriately as we would always suggest
  indicator: fund volatility (about 90% at times) · asset: multi-asset futures · direction: n/a · horizon: n/a · conditions: investor can scale the allocation · testable: no · confidence: medium
  ^MT044-C11-R4

### C12
- **Rob Carver** Discretionary forecasts on the same scale can be blended with systematic ones using weights (50/50, 70/30), which Rob calls semi-automatic trading.  #mech/research_method
  > use some kind of weighted average of, you know, what what those discretionary forecasts are combined with your more systematic forecasts
  indicator: blended forecast · asset: multi · testable: yes · confidence: high
  ^MT044-C12-1
- **Rob Carver** A numeric forecast can be tested like a backtest, so the weight on discretionary views can be based on evidence.  #mech/research_method
  > because the forecast is a number, you can actually then independently verify how good that forecast is in exactly the same way you could verify a back test
  asset: multi · conditions: less history than for systematic · testable: yes · confidence: high
  ^MT044-C12-2
- **Rob Carver** Do not apply discretionary views to volatility forecasts because systematic forecasts are hard to beat.  #mech/research_method
  > systematic methods of forecasting volatility are extremely good and I don't I think it's tough to beat that
  indicator: volatility forecast · asset: multi · testable: yes · confidence: medium
  ^MT044-C12-3
- **Rob Carver** Only the buy-or-not decision may be discretionary; sizing, holding period, stops and portfolio optimisation should be systematic, as done by Marshall Wace feeding forecasts into an optimiser.  #mech/research_method
  > setting stop-loss limits for your stop losses and and and things like you know optimizing a portfolio for the the most diversification those things should all be done scientifically I believe using systematic methods
  asset: multi · testable: partly · confidence: high
  ^MT044-C12-4
- **Rob Carver** Rob doubts his own discretionary skill for buy-or-not decisions, citing that he sold all his equities around April 14 (2025), which he treats as a mistake.  #mech/new _(added by map cross-check, time-bound view)_
  > I'm the guy that sold all my equities and on April the 14th or whenever it was
  indicator: own discretionary timing · asset: equities · direction: n/a · horizon: weeks · conditions: April 2025 tariff selloff and rebound · testable: no: personal anecdote · confidence: medium
  ^MT044-C12-R3

### C14
- **Rob Carver** Renaissance hires pure mathematicians without finance experience to see the data with fresh eyes, while others hire from the same schools.  #mech/behavioral
  > hiring people from you know mainly pure mathematics backgrounds with with no finance experience because they want to look at the data with fresh eyes
  asset: other · horizon: years · testable: no · confidence: medium
  ^MT044-C14-1
- **Rob Carver** Skilled managers differ in small details such as beta cleaning; there is no big undiscovered secret, only marginal gains in execution and data cleaning.  #mech/research_method
  > you could give the same data and the same books to a bunch of people and ask them to do to create you know a trading strategy um and they'd all do it in slightly different ways
  asset: multi · horizon: years · testable: no · confidence: high
  ^MT044-C14-2
- **Rob Carver** Cost-aware portfolio optimisation across many illiquid markets separates the profitable from less profitable managers.  #mech/risk_management
  > things like sort of optimizing portfolios to try and make the best use of this vast variety of of markets we've
  indicator: portfolio optimisation with costs · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT044-C14-3
- **Rob Carver** Rob's mistakes were trading too quickly and over-concentrating, and he stresses avoiding errors.  #mech/risk_management
  > trading too quickly you know overconentrating individual markets
  asset: multi · testable: no · confidence: medium
  ^MT044-C14-4
- **Rob Carver** Return differences between CTAs are largely luck, so it is hard to tell skilled from unskilled managers from outcomes; post-mortems should ask whether a loss came from bad luck or a bad decision such as overweighting an illiquid market.  #mech/research_method _(added by opus cross-check)_
  > If you look at the profitable managers and the less profitable managers, because there's a lot of luck, right? See, they may it's not necessarily whether they're good or bad. I think you can it's hard to tell.
  indicator: manager return dispersion · asset: multi · horizon: years · testable: partly - skill vs luck tests on manager track records need long histories · confidence: medium
  ^MT044-C14-X1

### C15
- **Rob Carver** Liquidity in OTC markets can vanish suddenly (fixed income agencies in 2009).  #mech/liquidity_flows
  > market capacity can vanish like that right and it did in 2009
  asset: rates · horizon: days · conditions: OTC markets · testable: no · confidence: high
  ^MT044-C15-1
- **Rob Carver** IP leakage between CTAs is minor; staff moves bring a fresh perspective, though less systematic and higher frequency strategies rely more on secrets.  #mech/behavioral
  > I can't imagine you know someone leaving say a big CTA going to the big CTA and taking some big big secret with them
  asset: multi · testable: no · confidence: medium
  ^MT044-C15-2

### C16
- **Rob Carver** Trend following works where consensus expects mean reversion and is wrong, and mean reversion works where consensus expects trends and is wrong.  #mech/behavioral
  > Then that obviously is a fantastic place to do trend following
  indicator: consensus forecasts of mean reversion · asset: multi · horizon: years · testable: yes - compare forecast errors with trend returns · confidence: high
  ^MT044-C16-1

### C17
- **Rob Carver** Forecasts always assume rates return to normal (4% expected from 2009 to 2020, falling from 6% in 1999), but rates persist, which favours bond trend.  #mech/slow_reaction
  > people think that interest rates are going to uh mean revert and they don't they don't mean revert they persist for long periods of time
  indicator: yield forecast whiskers · asset: rates · direction: Rate trends persist · horizon: years · testable: yes - Ilmanen paper · confidence: high
  ^MT044-C17-1
- **Rob Carver** Equity analysts extrapolate, so momentum is already priced in and even overpriced.  #mech/behavioral
  > They think if times are good, they're going to continue getting good. If times are bad, they're going to continue getting bad
  indicator: analyst EPS growth expectations · asset: equities · horizon: years · testable: yes - EPS forecast data · confidence: high
  ^MT044-C17-2
- **Rob Carver** Equity analysts' EPS forecasts carry a systematic optimism bias from institutional incentives, which shrank somewhat after post-tech-bubble reforms; this level bias is separate from their extrapolation bias.  #mech/behavioral _(added by opus cross-check)_
  > analysts generally are overoptimistic and there are institutional biases as to why that might be the case
  indicator: analyst EPS growth forecasts vs realised · asset: equities · direction: forecasts above outcomes · horizon: years · conditions: bias smaller after the early-2000s reforms · testable: yes - IBES forecast errors over time · confidence: medium
  ^MT044-C17-X1

### C18
- **Rob Carver** Trend works better in bonds than equity indices because investors expect mean reversion in bonds and extrapolate in equities, and equity trend suffers V-shaped reversals.  #mech/behavioral
  > trend falling in bonds has done very well indeed trend following in equities has done much less well in equity indices
  indicator: trend performance by asset class · asset: multi · direction: Bond trend > equity trend · horizon: years · conditions: index futures, not single stocks · testable: yes · confidence: high
  ^MT044-C18-1
- **Rob Carver** Bond carry and secular decline in rates, plus rising equity valuations, give a tailwind to momentum that is stronger in bonds.  #mech/structural_shift
  > carry tends to be higher in bonds and u that means that you will earn carry which creates a secular upward trend in bond prices
  indicator: carry; secular rate trend · asset: rates · horizon: years · testable: partly · confidence: medium
  ^MT044-C18-2
- **Rob Carver** Ask who is on the other side of a risk premium trade (Ilmanen): knowing the counterparty helps judge whether a factor persists.  #mech/research_method
  > where you know where does the money come from, right?
  asset: multi · testable: no · confidence: medium
  ^MT044-C18-3

### C19
- **Rob Carver** Avoiding the worst days beats missing the best days because equity returns are negatively skewed, so Asness's critique of the 'missing the best days' argument holds.  #mech/research_method
  > equity returns are also negatively skewed and the worst days are much worse than the best days are good
  indicator: worst vs best daily returns · asset: equities · horizon: years · testable: yes · confidence: high
  ^MT044-C19-1
- **Rob Carver** Trend-based exposure changes are different from forecasting one-day moves; nobody sits out single days.  #mech/research_method
  > over the last 3 months the market has been trending down therefore I think I should no longer be owning the market
  asset: equities · testable: partly · confidence: medium
  ^MT044-C19-2
- **Rob Carver** Simulations of randomly missing days raise dispersion of returns, reinforcing the case against day-timing; costs and taxes add to the damage.  #mech/research_method
  > increase the dispersion of your returns over time and that's what his statistical work shows
  asset: equities · horizon: years · testable: yes - simulation · confidence: high
  ^MT044-C19-3

### C20
- **Niels Kaastrup-Larsen** Trend followers' best returns often follow their worst, so stay invested and hope for a rebound in 2025.  #mech/cycle_persistence _(time-bound view)_
  > some of the best returns actually comes after your worst returns uh period
  asset: multi · horizon: years · testable: yes - conditional return study · confidence: low
  ^MT044-C20-1
- **Rob Carver** Timing entry into trend following needs autocorrelation of strategy returns: positive would mean add after good years, negative the reverse.  #mech/research_method
  > If trend following had had a good year and there was a positive autocorrelation between annual returns and trend following then you should if there's been a good year you should invest more
  indicator: autocorrelation of annual trend returns · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT044-C20-2
- **Rob Carver** The honest case for long-only equities is the long-run risk premium (higher risk, higher return), not the 'missing the best days' argument, which is marketing.  #mech/risk_premium _(added by opus cross-check)_
  > I'm happy with the thesis that if you have increased risk you'll get higher returns equities are quite risky therefore if you're investing for the long term buy
  asset: equities · direction: long equities over long horizons · horizon: years · conditions: long holding period; cannot time the market · testable: yes - long-run equity premium data · confidence: high
  ^MT044-C20-X1

### C21
- **Rob Carver** Performance fees bias net returns toward negative autocorrelation, so autocorrelation tests should use gross returns.  #mech/research_method
  > performance fees actually make your returns more negatively autocorrelated um because you only take performance fees out of um when you're doing well
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT044-C21-1
- **Rob Carver** Gross momentum returns show weak positive annual autocorrelation that disappears at longer horizons.  #mech/cycle_persistence
  > for momentum specifically if I looked at um say annual returns I did find there was a bit of weak pos positive autocorrelation
  indicator: annual momentum return autocorrelation · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT044-C21-2
- **Rob Carver** The autocorrelation effects are too weak to time trend following; strategy timing is as hard as market timing.  #mech/research_method
  > you would really be crazy to try and use them in any kind of momentum market timing strategy because they would definitely get eaten up by fee fees or costs
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT044-C21-3

