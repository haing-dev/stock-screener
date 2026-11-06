---
source_id: MT137
title: "Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor - Ep.375"
date: 2025-11-27
channel: "Top Traders Unplugged"
url: 
words: 14490
claims: 64
added_by_crosscheck: 11
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Rob Carver (systematic futures trader, author of Systematic Trading, ex-AHL)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor - Ep.375

**Speakers:** Rob Carver (systematic futures trader, author of Systematic Trading, ex-AHL); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Systematic Investor weekly (Nov 2025) with Rob Carver answering listener questions on backtest robustness, rebalancing, intraday vs end-of-day execution, position sizing and skew, sentiment indicators, ATR; then CalPERS' adoption of the total portfolio approach. Carver: trend following is a risk premium, backtests must avoid multiple-testing and use rolling selection, dynamic vol targeting beats fixed sizing, trade slow. TPA is promising but vague; could benefit trend following.

**Approach:** trend following, backtesting methodology, position sizing / volatility targeting, execution and costs, total portfolio approach, skew

**Cross-check completeness estimate of first read:** 0.88 - first reader covered all 21 chunks including every listener question and the TPA discussion with accurate numbers; missed minor caveats (Monte Carlo/OOS limits, Lo autocorrelation point, no-stop-loss method, UK DB bond demand) and some Renaissance context.

## Argument map

**Episode thesis:** Carver argues trend following is a risk premium rather than an edge (anyone can do it, so the pay is compensation for discomfort), and that a systematic trader survives by keeping costs low, leverage moderate and avoiding overfitting: build backtests as rolling, past-only selection across many strategies, size positions by dynamic volatility targeting (the skew gained from not scaling does not repay the Sharpe lost), and trade slowly. On the total portfolio approach adopted by CalPERS he is hopeful but sceptical: judging a CTA by its contribution to the whole portfolio should help diversifiers, but the approach has no formal definition.

### Rob Carver (independent systematic futures trader, author of Systematic Trading, ex-AHL (Man Group))
Fingerprint: #approach/trend_following #approach/position_sizing_vol_target #approach/research_robustness_overfitting #approach/costs_execution #approach/portfolio_construction_stacking #approach/behavioral_sentiment #approach/diversification_risk_parity
_Speaker note: Captions have no labels but host questions are read in a distinct style and Carver's answers are first-person about his own system, blog and AHL experience. The ledger correction moves the Bitcoin halving remark (C05) to Carver; the host's joke about being 'hot' follows. In C16 Carver cannot recall the author of an execution paper (probably AQR, he says)._

**Worldview premises**
- Trend following is a risk premium, not an edge: if anyone with capital and a spreadsheet can do it, the profit must be compensation for taking risks others find uncomfortable. The two main explanations are psychological biases and delayed reaction to information. _[theoretical, stated; support: first-principles argument; a recent Cliff Asness podcast making the same point]_ ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C01-1|C01-1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C01-2|C01-2]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C10-1|C10-1]])
- Trend following works across many asset classes with long holding periods; it is not designed for single asset classes or fast speeds. Trend efficacy falls below holding periods of about one or two weeks to a month, and below about one hour mean reversion appears. _[experience, stated; support: his experience of how trend systems perform by holding period; no data shown]_ ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C09-4|C09-4]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C10-1|C10-1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C09-3|C09-3]])
- Three things kill systematic traders: excessive costs, excessive leverage and overfitting. His advice has not changed in 10-20 years; backtesting principles are not new scientific discoveries. _[experience, stated; support: about 20 years in the CTA industry; 11.5 years running his own automated platform]_ ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C11-1|C11-1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C10-R1|C10-R1]])
- A backtest has two jobs, finding future strategies and estimating past performance. Selecting the best in-sample strategies destroys the second job because the result is selected on the same data; and picking the top few from many (multiple testing) selects luck. _[theoretical, stated; support: statistical argument: 10 of 1,000 flat strategies will look amazing by chance]_ ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C06-4|C06-4]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C07-2|C07-2]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C07-X1|C07-X1]])
- Dynamic volatility sizing beats fixed sizing for geometric return: positive skew improves CAGR but hurts Sharpe, and the skew gained from not volatility-scaling does not compensate for the Sharpe lost. A high-Sharpe, less skewed system with a bit more leverage can beat the CAGR of high-skew, high-vol CTAs. _[theoretical, stated; support: theoretical result on his blog (not empirical) that assumes leverage can be adjusted]_ ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C12-1|C12-1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C13-1|C13-1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C13-2|C13-2]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C13-3|C13-3]])
- Upside and downside volatility are the same risk for sizing: returns are close to a coin flip, so a large position after a big rise is a coin flip away from becoming a large loss. _[theoretical, stated; support: reasoning; he says the question about asymmetric volatility is the one he has no real answer for]_ ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C14-3|C14-3]])
- Third-party sentiment indicators and sell-side models are typically fitted in-sample and should be built in-house; skew, option ratios and the VIX level are valid sentiment proxies even though he does not use them. _[experience, stated; support: AHL experience of sell-side vendors; digging into construction]_ ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C15-2|C15-2]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C15-3|C15-3]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C15-1|C15-1]])
- Strategic asset allocation is a top-down box structure that ignores correlation across boxes; a total portfolio approach evaluates additions holistically, which should favour diversifying strategies and help CTAs that fit neither the hedge-fund nor the tail-protection box. _[institutional, stated; support: his work with allocators and multi-manager groups at Man Group; a made-up Danish equities example]_ ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C18-1|C18-1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C19-1|C19-1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C19-2|C19-2]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C20-1|C20-1]])
- Capacity-limited alpha stays inside: Renaissance's closed Medallion fund returns differ massively from its outside funds, possibly because good ideas are kept inside or have limited capacity. _[experience, stated; support: public returns of Renaissance's outside funds, including a CTA-type fund that underperformed]_ ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C02-2|C02-2]])

**Chain: Honest backtesting by rolling selection**
1. start with many strategies and no information → equal weight them (performance is flat if half are bad): no past evidence to prefer any ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C07-1|C07-1]])
2. past performance accrues → shift weights toward strategies that look good, keep most others: a few years of data cannot prove 10 strategies are best ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C06-5|C06-5]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C07-3|C07-3]])
3. the rolling process → an honest historic result and a final mix of strategies to trade: uses only past data at each point ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C06-5|C06-5]])
- Evidence: Methodological argument, AHL's annual refit practice, his own refit about every three years.
- Fails when: Very short time frames, where there is enough data to separate strategies; Monte Carlo and holdout tests help but do not fix selection of a tiny subset on too little data.

**Chain: Why not to skip volatility scaling for skew**
1. no vol scaling: position held at full size after a jump (cocoa) → outsized positive outlier return and positive skew: position size does not shrink as volatility rises ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C13-1|C13-1]])
2. more variable risk → lower Sharpe: Sharpe calculations penalise risk that moves around ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C13-1|C13-1]])
3. skew versus Sharpe trade-off for a given CAGR → the skew gained does not pay for the Sharpe lost, so CAGR is lower than with dynamic sizing: theoretical result ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C13-2|C13-2]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C13-3|C13-3]])
- Evidence: Blog article; theory, not data; positive-skew CTAs with high vol can still outperform high-Sharpe systems unless leverage is added.
- Fails when: Leverage cannot be adjusted; objective is not geometric return.

**Chain: Rebalancing and churn**
1. daily rebalancing to a noisy volatility estimate → buying and selling on alternate days: volatility jiggles around ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C14-1|C14-1]])
2. extra trades → trading costs exceed the benefit: tracking the optimal position matters less than costs ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C13-4|C13-4]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C14-1|C14-1]])
3. buffering or smoothing (EWMA vol, moving average of target) → frequent rebalancing without extra cost: trades only when far from optimum ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C14-2|C14-2]])
- Evidence: Standard practice and his blog tests.
- Fails when: Not stated; depends on costs.

**Chain: Total portfolio approach and CTAs**
1. SAA: boxes for asset classes, hedge funds, CTAs → correlations across boxes are ignored: each sleeve judged on its own ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C18-1|C18-1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C19-1|C19-1]])
2. TPA judges each addition by its effect on the whole portfolio → diversifiers with positive Sharpe look better: CTAs fit neither the hedge-fund nor the tail-protection box ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C19-2|C19-2]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C20-1|C20-1]])
3. large quant-heavy allocators (ADIA) adopt it with formal papers → could be a game-changer for trend allocations: would define the approach ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C20-2|C20-2]])
- Evidence: Reasoning from SAA mechanics; CalPERS adoption (read by host).
- Fails when: It may be an excuse to add private assets; the approach is vague.

**Decision process**
- [research] Match backtest data frequency to holding period: tick data only for fast strategies, none for monthly holding; test a one-day execution delay and expect no material change for slow systems.. Why: a slow strategy insensitive to a one-day delay need not trade at the close ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C06-1|C06-1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C06-2|C06-2]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C09-1|C09-1]])
- [research] Do not build on 3-5 years of data for a monthly-holding system; include trading costs from the start and drop any strategy that does not make money before slippage.. Why: insufficient data for calibration; costs belong in the design ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C06-3|C06-3]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C07-4|C07-4]])
- [research] Refit strategy weights about annually for monthly-holding systems (AHL did); personally about every three years, usually when other changes are made.. Why: an extra year adds under 2% to 55 years of data ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C08-1|C08-1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C08-2|C08-2]])
- [sizing] Continuous dynamic position sizing on volatility, trend strength and possibly account size; no stop losses and no ATR, with risk handled by standard-deviation sizing.. Why: better geometric return than fixed sizing, theory ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C12-2|C12-2]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C16-X2|C16-X2]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C13-2|C13-2]])
- [execution] Trade through the day after the previous close (not at the close); institutional size should spread trades through the day; run the dynamic optimiser through the day only with care about reacting to intraday bounces.. Why: performance lies between trading at the previous and next close; reduces market impact ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C09-1|C09-1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C09-2|C09-2]])
- [execution] Buffering or smoothing instead of daily rebalancing.. Why: avoids churn on noisy volatility estimates ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C14-1|C14-1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C14-2|C14-2]])
- [signal] Skew signal: buy assets with heavy negative historic skew, which tend to be underpriced because people dislike them.. Why: a form of buying negative sentiment; he uses no other sentiment indicators ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C15-1|C15-1]])
- [research] Use monthly, weekly or daily data to estimate Sharpe and volatility; use daily data for ATR/volatility estimates, weekly systems can be tested on weekly data.. Why: annual returns hide autocorrelation that biases annualised Sharpe and volatility; more frequent data gives more accurate volatility ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C16-X1|C16-X1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C16-3|C16-3]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C16-1|C16-1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C16-2|C16-2]])
- [execution] Idea in his back book: execute slow signals the next day only if price has moved in your favour (buy only after a dip), combining slow trend with short-term mean reversion for cheaper execution.. Why: better fills from a fast mean-reversion element without extra trades; untested for delays over one day ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C16-4|C16-4]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C17-X1|C17-X1]])

**Evidence style:** First principles and statistics (multiple testing, skew-Sharpe theory, autocorrelation), his own long backtests (data from 1970) and blog articles, and AHL practice; explicit about what is theory versus empirical and about what he has not tested.

**Views at the time**
- (2025-11-20) His own risk sizing is below average, consistent with a neutral trend barometer; he is up about 5% for the year, in a drawdown of just over 10% (about 3% below mid-October), with the largest short in Bitcoin and net long equities (short DAX, long Italy).. Reasoning: the system, not his opinion, drives positions; trends have become more volatile since September-October ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C04-3|C04-3]])
- (2025-11-20) The Bitcoin halving cycle has only about four observations, too few for a statistically significant model.. Reasoning: small sample ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C05-1|C05-1]])
- (2025-11-20) CalPERS' move to a total portfolio approach could help trend following, but he suspects it is partly an excuse to add more private assets; he calls it hopeful but vague.. Reasoning: holistic evaluation favours diversifiers; no formal definition; management-consultant language ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C17-2|C17-2]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C19-2|C19-2]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C19-3|C19-3]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C19-R1|C19-R1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C20-2|C20-2]])
- (2025-11-20) UK defined-benefit pension funds' large bond holdings have supported long-dated UK bonds and distort the yield curve.. Reasoning: obligations to retirees put investment risk on the manager ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C18-X1|C18-X1]])

### Niels Kaastrup-Larsen (host, Top Traders Unplugged; CTA background)
Fingerprint: #approach/trend_following #approach/regime_detection #approach/manager_selection_allocation #approach/behavioral_sentiment #approach/replication_indexing #approach/costs_execution
_Speaker note: Host. He reads listener questions and states views on 2025 CTA performance, ETFs, trend decay and total portfolio approach. The ledger correction reassigns the Bitcoin halving remark to Carver._

**Worldview premises**
- Apparent decay in trend following mainly reflects poor market environments over the last 20 years, which research teams cannot overcome, not a broken strategy; success needs commitment to the rules and comfort with a strategy that is unpredictable day to day but predictable in the long run. _[experience, stated; support: career observation; no data]_ ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C11-X1|C11-X1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C11-X2|C11-X2]])
- Trend systems have evolved without changing core rules: more differentiation of speeds between entry and exit signals, and better risk management and use of volatility. _[experience, stated; support: what his firm does]_ ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C11-2|C11-2]])
- In 2025 differences between CTAs, ETFs and replicators came from exposure (how much equity, fixed income) and market universe rather than model type, so conclusions about which approach is better are dangerous; a fund with a low-equity-correlation mandate should not be judged against the S&P 500. _[empirical, stated; support: performance comparison and a Renaissance product mandate]_ ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C04-1|C04-1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C03-X2|C03-X2]])
- Allocators chase past performance with too short a horizon (a Midwestern pension added CTAs after 2022 and was disappointed), and cheaper ETFs drew inflows after outperforming in 2025. _[behavioural, stated; support: a trade press article on a pension fund; ETF flows]_ ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C03-2|C03-2]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C03-1|C03-1]])
- Even elite quant funds suffer outlier months, so a single large monthly loss reported by a journalist (Renaissance equity funds) is a selected number; the Renaissance outside equity fund lost 19% in 2022 and returned only 3.7% since inception. _[empirical, stated; support: fund returns recalled from an article]_ ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C02-1|C02-1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C03-X1|C03-X1]])
- CalPERS' move to a total portfolio approach (from July 2026, reference portfolio 75% equities/25% bonds) makes trend following more interesting because each component will be judged by its contribution to the portfolio. _[institutional, stated; support: the board vote and quoted statements]_ ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C17-1|C17-1]])

**Chain: Why 2025 comparisons across trend products mislead**
1. equity and fixed income exposure differs across products → return differences in 2025: equities were the challenge in November while metals, softs and small currencies paid ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C04-1|C04-1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C04-2|C04-2]])
2. market universe differences → differences across CTAs, ETFs and replicators: which markets are traded matters more than model type ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C04-1|C04-1]])
- Evidence: November and year-to-date index numbers.
- Fails when: Not stated.

**Decision process**
- [other] Trend barometer (48 in November 2025, neutral) used as a gauge of trend conditions.. Why: indicates how supportive the environment is for trend ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C04-3|C04-3]])

**Evidence style:** Anecdote, news articles and index data; moderates guest claims with balance points.

**Views at the time**
- (2025-11-20) November 2025 trend profits were in precious metals, softs, some oil products and small currencies (NZD, MXN), while equities were the challenge.. Reasoning: sector attribution from his barometer and performance ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C04-2|C04-2]])
- (2025-11-20) Late November 2025: SG CTA -2.2% YTD, SG Trend -1.18%, short-term traders -5.16%, versus MSCI World +16.86% and S&P 500 +14.2%.. Reasoning: index data read out ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C05-2|C05-2]])
- (2025-11-20) A 7% loss this year for the Renaissance outside equity fund is not an outlier; CTAs' 2025 looks less bad next to it.. Reasoning: its 2022 loss and low since-inception return ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C02-1|C02-1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C03-X1|C03-X1]])

### Disagreements
- **How much has trend following changed in 20 years?**: Rob Carver: His advice and principles have not changed in 10-20 years. ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C10-R1|C10-R1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C11-1|C11-1]]); Niels Kaastrup-Larsen: Entry rules are unchanged but risk management, volatility use and speed differentiation between entry and exit have evolved. ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C11-2|C11-2]])
- **Is the total portfolio approach good news for trend following?**: Niels Kaastrup-Larsen: Very interesting for trend, since each component is judged by its contribution to the portfolio. ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C17-1|C17-1]]); Rob Carver: Holistic thinking should help diversifiers, but he is sceptical: vague, management-consultant language and maybe an excuse for more private assets; a formal definition from big quant allocators would be a game-changer. ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C17-2|C17-2]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C19-2|C19-2]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C19-3|C19-3]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C20-2|C20-2]])

### Gaps and conflicts
- Carver's static-versus-dynamic result is theoretical and he stresses it is not an empirical result; his claim that extra leverage on a high-Sharpe system beats high-skew CTAs rests on that theory and on being able to lever without limit. ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C13-2|C13-2]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C13-3|C13-3]])
- The rolling selection backtest is described as the gold standard but not demonstrated; costs of implementing it with many strategies and the choice of weighting scheme are not discussed. ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C06-5|C06-5]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C07-1|C07-1]])
- Skew as sentiment: the ledger correction notes Carver only says one could argue it; his rule buys heavy negative skew, which he says tends to be underpriced, without evidence given. ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C15-1|C15-1]])
- Carver cannot answer the asymmetric-volatility question empirically and offers only a coin-flip argument for treating upside and downside volatility alike. ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C14-3|C14-3]])
- The execute-only-after-a-favourable-move idea is untested and may lose trend capture if fills are delayed by more than one day. ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C16-4|C16-4]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C17-X1|C17-X1]])
- The Renaissance comparison mixes outside funds with the closed Medallion fund; the explanations (capacity, ideas kept inside) are guesses. ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C02-2|C02-2]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C03-X1|C03-X1]])
- The host's view that decay reflects environment and not strategy is offered without a test; Carver's risk premium argument is compatible with either. ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C11-X1|C11-X1]])
- Carver reports a heated disagreement with people on X who claim a moving-average crossover is an edge, but the counter-arguments are not presented, so his edge-versus-risk-premium view is one-sided in this episode. ([[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C01-1|C01-1]], [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C01-2|C01-2]])

### Forward-looking inputs (reader synthesis)
(reader) Observable inputs the speakers treat as leading performance: the trend barometer and the size of market moves for trend returns; the volatility estimate used for sizing (with EWMA smoothing); market universe and equity or fixed income exposure for product differences; correlations for fixed-vol-target systems; formal publications by large quant allocators (ADIA) for the total portfolio approach. Horizons: monthly holding period and annual or multi-year refits for the strategy; July 2026 for CalPERS' switch.

### Reader inferences (not stated by the speakers)
- Carver's advice on backtests implies that published CTA-style backtests that select a small share of many candidates on a few years of data overstate expected performance.
- His risk premium framing, plus the claim that trend efficacy falls below about a month, suggests lower-speed signals carry the premium and costs eat the faster ones; it is consistent with the host's view that short lookbacks are poor.
- If the TPA is adopted and judged holistically, a CTA's correlation to an allocator's other holdings (not only its stand-alone Sharpe) becomes the selling point; this favours CTAs with low equity beta.
- Carver's theory result on skew versus Sharpe implies that, for a given CAGR target, an allocator choosing between a high-skew CTA and a high-Sharpe CTA should consider the leverage they can apply.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | intro; trend following as edge vs risk premium |
| C02 | 2 | why trend makes money; Renaissance public funds October losses |
| C03 | 2 | CTOL article on ETFs vs CTAs; Renaissance details |
| C04 | 3 | AI bubble aside; trend barometer 48; 2025 performance by market universe; Carver's book and risk |
| C05 | 2 | Bitcoin halving data points; Nov 2025 index performance; listener question on robustness framework |
| C06 | 5 | holding period vs data frequency; backtest purposes; rolling strategy selection |
| C07 | 4 | rolling selection, multiple testing, costs from start |
| C08 | 2 | refit frequency; intraday vs end-of-day question starts |
| C09 | 4 | execution timing, spreading trades, intraday trend limits; single asset class |
| C10 | 1 | trend needs diversification and longer holding; advice for new systematic traders |
| C11 | 2 | three killers of systematic traders; industry evolution; position sizing question start |
| C12 | 2 | static vs dynamic sizing definitions; Sharpe vs geometric return objective |
| C13 | 4 | skew vs Sharpe trade-off, fixed vs dynamic vol; rebalancing frequency |
| C14 | 3 | buffering and smoothing; asymmetric volatility; sentiment question |
| C15 | 3 | skew as sentiment; third-party indicators; ATR question |
| C16 | 4 | autocorrelation and sqrt-time scaling; ATR data frequency; stops; combining slow momentum with execution filter |
| C17 | 2 | execution filter caveat; CalPERS TPA vote and reference portfolio |
| C18 | 1 | how SAA works (efficient frontier, sleeves) |
| C19 | 3 | SAA boxes ignore correlation; TPA holistic; vagueness |
| C20 | 2 | CTAs lack a box; TPA game-changer if large quant allocators follow; ChatGPT summary |
| C21 | 0 | nothing actionable: ChatGPT joke, outro and sponsor reads |

## Claims

### C01
- **Rob Carver** Trend following is a risk premium rather than an edge: anyone with capital and a simple system can do it, so profits compensate for risks others find uncomfortable.  #mech/risk_premium
  > my my personal belief is if anyone can do it then you haven't got an edge
  asset: multi · direction: long trend following as risk premium · horizon: years · testable: partly - definitional · confidence: high
  ^MT137-C01-1
- **Rob Carver** The two main explanations for why trend following earns money are psychological biases and delayed reactions to information.  #mech/slow_reaction
  > So, we can talk about psychological biases but we can talk about you know, delayed reactions to information.
  asset: multi · testable: partly · confidence: medium
  ^MT137-C01-2

### C02
- **Niels Kaastrup-Larsen** Renaissance public funds (Institutional Equity -14% in Oct 2025, Diversified Alpha -15%) show that even elite quant funds suffer outlier months, making CTAs' 2025 look less bad.  #mech/crowding_positioning _(time-bound view)_
  > the Renaissance Institutional Equity Fund was down 14% in October um and down 8.3% so far this this year
  asset: equities · horizon: months · conditions: Oct 2025 · testable: yes - fund returns · confidence: medium
  ^MT137-C02-1
- **Rob Carver** Renaissance's closed Medallion fund returns differ massively from its outside funds, possibly because alpha has limited capacity or good ideas are kept inside, and its outside CTA-type fund underperformed.  #mech/structural_shift
  > there's always been a big disparity between um the Medallion Fund, which has been closed forever, you know.
  asset: multi · horizon: years · conditions: capacity-limited strategies · testable: no - Medallion data not public · confidence: low
  ^MT137-C02-2

### C03
- **Niels Kaastrup-Larsen** Cheaper, more transparent managed futures ETFs outperformed many established CTA funds in 2025 and attracted inflows.  #mech/risk_management _(time-bound view)_
  > A newer category of managed futures exchange-traded funds has outperformed better uh has performed better, sorry, than many established CTA funds.
  asset: multi · horizon: months · conditions: 2025 · testable: yes - fund returns · confidence: medium
  ^MT137-C03-1
- **Niels Kaastrup-Larsen** A Midwestern pension that allocated to CTAs in 2023 after the great 2022 became frustrated: chasing past performance with too short a horizon leads to disappointment.  #mech/behavioral
  > they obviously added it in 2023 after the exceptional year in 2022
  asset: multi · horizon: years · testable: no - anecdote · confidence: medium
  ^MT137-C03-2
- **Niels Kaastrup-Larsen** The Renaissance International/Institutional Equity fund (equity-market-neutral style) lost 19% in 2022 and has returned only 3.7% since inception, so a -7% year in 2025 is not an outlier and the headline October loss is a journalist's selected number.  #mech/research_method _(added by sonnet-xhigh cross-check, time-bound view)_
  > its worst year so far, I believe, in the past in 2022, they were down 19%
  indicator: Renaissance Institutional Equity fund returns · asset: equities · horizon: years · conditions: outside-investor Renaissance products differ sharply from the closed Medallion fund · testable: yes - fund returns are public · confidence: medium
  ^MT137-C03-X1
- **Niels Kaastrup-Larsen** A fund with a mandate for low equity correlation should not be expected to rise just because the S&P 500 rises, so its 2025 shortfall must be judged against its mandate rather than the equity index.  #mech/research_method _(added by sonnet-xhigh cross-check, time-bound view)_
  > at least one of these funds actually had a mandate to be not very correlated with equity
  indicator: fund correlation to equities · asset: equities · conditions: benchmark must match fund mandate · testable: yes - correlation and beta can be measured · confidence: medium
  ^MT137-C03-X2

### C04
- **Niels Kaastrup-Larsen** In 2025, differences between CTAs, ETFs and replicators were driven by exposure (how much equity, fixed income) and market universe, more than model type, so conclusions about which approach is better are dangerous.  #mech/risk_management _(time-bound view)_
  > market universe this year is really having a huge impact on on returns
  asset: multi · horizon: months · conditions: 2025 · testable: yes - attribution by market · confidence: medium
  ^MT137-C04-1
- **Niels Kaastrup-Larsen** In November 2025 trend profits were in precious metals, softs, some oil products and small currencies (NZD, MXN) while equities were the challenge.  #mech/slow_reaction _(time-bound view)_
  > It's still you know okay to be long in in precious precious metals
  asset: commodities · direction: long precious metals, softs · horizon: weeks · conditions: Nov 2025 · testable: yes · confidence: medium
  ^MT137-C04-2
- **Rob Carver** Carver's dynamic risk sizing was below average, consistent with a neutral trend barometer (48); he was in a drawdown of just over 10% with biggest short in Bitcoin and net long equities.  #mech/risk_management _(time-bound view)_
  > my my risk sizing is probably in line with your trend barometer
  indicator: trend barometer · asset: multi · horizon: weeks · conditions: Nov 2025 · testable: partly · confidence: medium
  ^MT137-C04-3

### C05
- **Niels Kaastrup-Larsen** Only about four Bitcoin halvings exist, too few observations for a statistically meaningful halving-cycle model.  #mech/research_method
  > that's not really enough data points for a statistically significant model
  indicator: Bitcoin halving cycle · asset: other · horizon: years · testable: yes - sample size · confidence: high
  **Correction (cross-check):** Speaker is likely Carver, not the host: Carver says there have been 'like four, something' halvings and the sentence that this is 'not really enough data points for a statistically significant model' runs straight into 'you should know better than to even ask me that question, Neils', i.e. the quant answering the host. → Carver (as a quant) says Bitcoin has had only about four halvings, too few data points for a statistically significant halving-cycle model.
  ^MT137-C05-1
- **Niels Kaastrup-Larsen** As of late Nov 2025 SG CTA index -2.2% YTD, SG Trend -1.18%, short-term traders -5.16%, vs MSCI World +16.86% and S&P 500 +14.2%.  #mech/slow_reaction _(time-bound view)_
  > CTA Societe Generale CTA index down 69 basis points for the month, down 2.2% for the year.
  indicator: SG CTA, SG Trend, SG Short-Term Traders indices · asset: multi · horizon: months · conditions: 2025 · testable: yes - index data · confidence: high
  ^MT137-C05-2

### C06
- **Rob Carver** Backtest data frequency should match holding period: fast strategies need tick data, monthly-holding trend systems need none.  #mech/research_method
  > if your holding period is more analogous to mine, which is about, say, an average of a month, um then you don't need to go near tick data.
  asset: multi · conditions: depends on holding period · testable: yes · confidence: high
  ^MT137-C06-1
- **Rob Carver** A slow strategy should be insensitive to a one-day execution delay; if it is not, there is a problem. This also removes the need to trade at the close.  #mech/research_method
  > even delaying your trades by a day, which is what I test in my backtester, shouldn't change your results that much.
  indicator: one-day fill delay test · asset: multi · horizon: days · conditions: for holding periods of about a month · testable: yes · confidence: high
  ^MT137-C06-2
- **Rob Carver** With monthly holding periods, 3-5 years of build data is too short for calibration and yields non-robust results.  #mech/research_method
  > 3 to 5 years probably for me is an insufficient amount of time um to to do sort of the calibration testing of strategies.
  asset: multi · horizon: years · conditions: slow strategies · testable: yes - statistical power · confidence: high
  ^MT137-C06-3
- **Rob Carver** A backtest has two aims, finding future strategies and estimating past performance; selecting the best in-sample strategies destroys the second because performance is selected on the same data.  #mech/research_method
  > they also tell you how well you would have performed in the past
  asset: multi · testable: yes · confidence: high
  ^MT137-C06-4
- **Rob Carver** Gold-standard backtest: start with many strategies, roll forward and reweight using only past performance, which gives an honest historic result and a final strategy mix.  #mech/research_method
  > you start with say a thousand strategies and you basically do a rolling process where you you subselect from those strategies depending on the performance you've only seen in the past.
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT137-C06-5

### C07
- **Rob Carver** In a rolling selection backtest, begin with all strategies equal weighted (flat performance if half are bad) and shift weight to good ones as evidence accrues.  #mech/research_method
  > you've got no information, so you just include all the strategies backtest including ones that are beep as well as ones that are good.
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT137-C07-1
- **Rob Carver** Multiple testing: picking the top 1% of a thousand strategies selects luck, since flat strategies will produce 10 amazing ones by chance; choosing too few on insufficient data is the main flaw.  #mech/research_method
  > just by luck 10 of them are going to be amazing
  asset: multi · horizon: years · conditions: unless trading very short time frames · testable: yes · confidence: high
  ^MT137-C07-2
- **Rob Carver** With statistically robust weighting, the best strategies get higher weights but others stay, since a few years of data cannot prove 10 strategies are best.  #mech/research_method
  > Yes, your 10 superstars would would have a higher weight than the others, but they by no means would they be filling the entire portfolio up.
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT137-C07-3
- **Rob Carver** Include trading costs in the backtest from the beginning; strategies that do not make money before slippage should not be considered.  #mech/research_method
  > Trading costs should be in there from the very start.
  asset: multi · testable: yes · confidence: high
  ^MT137-C07-4
- **Rob Carver** Monte Carlo permutation and out-of-sample holdout tests weed out crazy strategies but do not fix the central flaw of selecting a tiny subset of strategies on too little data (multiple testing).  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > But you know, doing things like Monte Carlo testing, doing things like holding out out of sample, that's all good.
  asset: multi · horizon: years · conditions: fails when the selected set is a small share of many candidates and the sample is short · testable: yes - multiple-testing corrections can be applied · confidence: high
  ^MT137-C07-X1

### C08
- **Rob Carver** With monthly holding, reoptimise strategy weights about annually (AHL used an annual refit); more frequent adds nothing.  #mech/research_method
  > then I think it's probably appropriate to do this re-optimization of weights to strategies about every year, say.
  asset: multi · horizon: years · conditions: slow strategies · testable: yes · confidence: high
  ^MT137-C08-1
- **Rob Carver** With 55 years of data an extra year adds under 2%, so Carver refits weights about every three years, typically only when other changes are made.  #mech/research_method
  > I've refitted my my weights on average about every 3 years.
  asset: multi · horizon: years · conditions: long histories, slow trading · testable: yes · confidence: medium
  ^MT137-C08-2

### C09
- **Rob Carver** Trading during the day after the previous close gives performance between trading at the previous close and at the next close, so if backtests at both are close results are robust.  #mech/research_method
  > You're going to be somewhere between those two.
  asset: multi · horizon: days · conditions: slow strategies · testable: yes · confidence: high
  ^MT137-C09-1
- **Rob Carver** Institutional-size slow trend systems should spread execution through the day to cut impact, and can run dynamic optimisation continuously to smooth trades, though reacting to big intraday moves can lose if prices bounce back.  #mech/risk_management
  > You want to spread your trades throughout the day and try and reduce your market impact as much as possible.
  asset: multi · horizon: days · conditions: institutional size · testable: partly · confidence: high
  ^MT137-C09-2
- **Rob Carver** Intraday trend trading has higher costs because more trades are needed and passive limit orders do not work when catching a short trend.  #mech/risk_management
  > it's harder to to do your trades with sort of passive limit orders
  asset: multi · horizon: days · conditions: intraday trend · testable: yes · confidence: high
  ^MT137-C09-3
- **Rob Carver** Trend efficacy declines for holding periods below roughly a month or two weeks, and below about one hour mean reversion appears.  #mech/cycle_persistence
  > they tend to start to decline for holding periods shorter than about a month or a couple of weeks, depending on the asset class.
  indicator: holding period · asset: multi · horizon: days · conditions: shorter than 1 month; sub-hour is mean reversion · testable: yes · confidence: high
  ^MT137-C09-4

### C10
- **Rob Carver** Trend following is designed to work across many asset classes with long holding periods, not on single asset classes or at fast speeds; the discomfort is what earns the premium.  #mech/risk_premium
  > It's really the diversification and and the longer holding period and all that stuff that makes it a little bit difficult, makes it a little bit uncomfortable, that makes it work.
  asset: multi · horizon: years · conditions: needs diversification and slow speed · testable: partly · confidence: high
  ^MT137-C10-1
- **Rob Carver** Carver says his advice to a new systematic trader would be much the same as 10 or 20 years ago; the principles (including backtesting) have not changed, apart from adding crypto as an asset class.  #mech/research_method _(added by map cross-check)_
  > I'm actually struggling to think how my advice would have changed from 10 or even 20 years ago
  indicator: systematic trading principles · asset: multi · horizon: years · testable: no - experience · confidence: medium
  ^MT137-C10-R1

### C11
- **Rob Carver** Three things kill systematic traders: excessive costs, excessive leverage and overfitting.  #mech/risk_management
  > are spending too much in costs, but you know, taking too much leverage, and over fitting the trading systems.
  asset: multi · testable: partly · confidence: high
  ^MT137-C11-1
- **Niels Kaastrup-Larsen** Trend systems can differentiate speeds between entry and exit signals, and risk management and use of volatility have evolved, without changing the core rules.  #mech/research_method
  > you can design your systems to react differently from entries to exits.
  asset: multi · testable: yes · confidence: medium
  ^MT137-C11-2
- **Niels Kaastrup-Larsen** Apparent decay in trend following mainly reflects bad market environments of the last 20 years (which research teams cannot overcome) rather than a broken strategy, so recent weakness is weak evidence that the edge is gone.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check)_
  > that's why people sometimes write that oh, this strategy doesn't work as well anymore. I'm not so sure that's true.
  indicator: trend following long-run performance · asset: multi · horizon: years · conditions: regime dependent: poor trending environments · testable: partly - needs long-sample regime analysis · confidence: medium
  ^MT137-C11-X1
- **Niels Kaastrup-Larsen** Trend following is unpredictable day to day but predictable in the long run, so success depends on committing to the rules and being comfortable with that, which is the discipline needed to earn the premium.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > feeling completely comfortable with a a strategy that um is unpredictable in some ways, uh yet it's very predictable in the long run
  asset: multi · horizon: years · testable: no - behavioural commitment · confidence: high
  ^MT137-C11-X2

### C12
- **Rob Carver** Choosing between static and dynamic sizing depends on objective: positive skew improves geometric return but hurts Sharpe, negative skew the opposite.  #mech/risk_management
  > things that have positive skew um may not have as good a sharp ratio, but may produce you a better geometric return.
  indicator: skew; Sharpe; geometric return · asset: multi · testable: yes · confidence: high
  ^MT137-C12-1
- **Rob Carver** Continuous trading re-evaluates positions on volatility, trend strength and possibly account size, and fixed-vol-target systems are also affected by correlations.  #mech/risk_management
  > you you constantly evaluate your positions according to things like volatility, strength of your trends
  asset: multi · direction: reduce size as vol or losses rise · horizon: days · testable: partly · confidence: medium
  ^MT137-C12-2

### C13
- **Rob Carver** Without volatility scaling a sudden jump (cocoa) is held at full size, giving outsized positive outlier returns and positive skew but lower Sharpe.  #mech/risk_management
  > if you're not changing your position according to volatility, that leap in price which of course also increases volatility, you'd keep your you'd keep your position the same size
  indicator: position size vs volatility · asset: commodities · horizon: days · testable: yes · confidence: high
  ^MT137-C13-1
- **Rob Carver** Theory shows that the skew gained from not scaling position size to volatility does not compensate for the Sharpe lost, giving lower CAGR than dynamic vol sizing.  #mech/risk_management
  > it's not worth doing fixed vol position sizing because the the additional skew you get does not pay you for the loss in sharp, which is substantial.
  indicator: skew vs Sharpe trade-off · asset: multi · direction: use dynamic volatility targeting · horizon: years · conditions: theory rather than empirical; assumes leverage can be adjusted · testable: yes · confidence: high
  ^MT137-C13-2
- **Rob Carver** A high-Sharpe, less skewed system with a bit more leverage can beat the geometric return of high-skew, high-vol CTAs.  #mech/risk_management
  > if I apply just a little bit of extra leverage to my system, I could very easily beat their geometric returns
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT137-C13-3
- **Rob Carver** Rebalancing frequency trades off tracking the optimal position against trading costs.  #mech/risk_management
  > you're trying to trade off two things. The benefits you'd get from having your position close to what your optimal position should be and the cost of trading to get there.
  asset: multi · testable: yes · confidence: high
  ^MT137-C13-4

### C14
- **Rob Carver** Daily rebalancing to a noisy volatility estimate creates churn and extra trading costs that exceed the benefit.  #mech/risk_management
  > If I was to to rebalance, say, every day without fail, then some days I'll be buying, some days I'll be selling.
  asset: multi · direction: slow the rebalancing · horizon: days · testable: yes · confidence: high
  ^MT137-C14-1
- **Rob Carver** Buffering (trade only if far from optimum) or smoothing (moving average of target position, EWMA vol) allows frequent rebalancing without extra cost.  #mech/risk_management
  > there is an a solution to this conundrum, and that's to use um either buffering or smoothing.
  asset: multi · horizon: days · testable: yes · confidence: high
  ^MT137-C14-2
- **Rob Carver** Volatility should be treated symmetrically for sizing: upside risk equals downside risk and a coin flip away from big gains turning into big losses.  #mech/risk_management
  > I'd say you should treat both kinds of volatility the same.
  asset: multi · testable: partly · confidence: medium
  ^MT137-C14-3

### C15
- **Rob Carver** Carver's skew signal buys assets with heavy negative historic skew, which is underpriced because investors dislike it; a skew signal is a sentiment proxy.  #mech/risk_premium
  > something with that's got very heavy negative skew would tend to be underpriced because people don't like it
  indicator: historic skew · asset: multi · direction: long assets with negative skew · horizon: months · testable: yes · confidence: medium
  **Correction (cross-check):** Overstated certainty: Carver says 'you could argue' a skew signal is a sentiment indicator; he does not use sentiment data and notes his skew rule simply buys assets with heavy negative skew that people dislike. → Carver's skew signal looks at historic skew and buys assets with heavy negative skew, which tend to be underpriced because people dislike them; one could call this buying negative sentiment, but he does not use sentiment indicators.
  ^MT137-C15-1
- **Rob Carver** Third-party sentiment indicators or models offered by sell-side are typically in-sample fitted, so be wary and build in-house.  #mech/research_method
  > essentially it's massively in-sample fitted and therefore of course it looks very good.
  asset: multi · testable: yes · confidence: high
  ^MT137-C15-2
- **Rob Carver** Skew, option ratios and VIX level are valid sentiment proxies for predicting prices though Carver does not use them.  #mech/behavioral
  > sort of various options ratios as well you can use.
  indicator: VIX; options ratios; skew · asset: multi · testable: yes · confidence: low
  ^MT137-C15-3

### C16
- **Rob Carver** Volatility scaling by sqrt(time) holds only with zero autocorrelation; negative autocorrelation makes daily vol exceed annualised vol, positive the opposite.  #mech/research_method
  > So, in this that that simple example where you've got very strong negative auto correlation, the daily standard deviation is much higher than the annual standard deviation.
  indicator: autocorrelation · asset: multi · testable: yes · confidence: high
  ^MT137-C16-1
- **Rob Carver** Weekly ATR should be about sqrt(5) times daily ATR under zero autocorrelation.  #mech/research_method
  > there should be a sort of multiple of around square root of five between those two values in theory.
  indicator: ATR · asset: multi · horizon: weeks · testable: yes · confidence: medium
  ^MT137-C16-2
- **Rob Carver** More frequent data gives more accurate volatility estimates, though backtests can run weekly for weekly systems.  #mech/research_method
  > I would use daily daily daily price changes to calculate my ATRs
  indicator: volatility estimation · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT137-C16-3
- **Rob Carver** Cheap execution idea: slow momentum signals executed the next day only if price has moved in your favour (buy only after dip) combines slow trend with short-term mean reversion.  #mech/research_method
  > only only execute those that have moved in your favor.
  indicator: previous close vs next day price · asset: multi · direction: buy after dips, sell after rallies for slow signals · horizon: days · conditions: needs test that delay beyond one day does not hurt · testable: partly - not tested · confidence: low
  ^MT137-C16-4
- **Rob Carver** Following Andrew Lo's work on hedge fund Sharpe ratios, performance and risk should be estimated from monthly, weekly or daily data because annual returns hide autocorrelation that biases annualised Sharpe and volatility.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > annual returns hide a lot of a lot of fun auto correlation properties
  indicator: Sharpe ratio under autocorrelation · asset: multi · testable: yes - compare annualised Sharpe from high-frequency versus annual data · confidence: high
  ^MT137-C16-X1
- **Rob Carver** Carver's system uses no stop losses and no ATR; it sizes by standard deviation of returns and handles risk through position sizing instead.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > I don't use stop losses when I'm trading and I don't use ATRs either
  indicator: stop-loss; ATR versus standard deviation · asset: multi · testable: yes - stop versus no-stop backtest · confidence: high
  ^MT137-C16-X2

### C17
- **Niels Kaastrup-Larsen** CalPERS board adopted the total portfolio approach (from July 2026) replacing SAA, with a reference portfolio of 75% equities/25% bonds.  #mech/structural_shift _(time-bound view)_
  > they voted in favor of adopting the total portfolio approach TPA which is going to replace their existing strategic asset allocation the SAA model.
  asset: multi · horizon: years · conditions: Nov 2025 · testable: no - event · confidence: high
  ^MT137-C17-1
- **Rob Carver** Carver cynically suggests TPA may be an excuse to add more private assets rather than diversifiers.  #mech/behavioral _(time-bound view)_
  > whether this is just going to be an easy an excuse to jam more private equity.
  asset: multi · horizon: years · testable: no · confidence: low
  ^MT137-C17-2
- **Rob Carver** The execute-only-on-favourable-move idea delays some trades by more than one day, and it is untested whether the missed trend capture offsets the execution saving; a one-day delay is harmless, longer ones need testing.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > whether delaying by um sort of potentially more than one day because you're waiting for the price to breach a nice level whether that's that's an an issue or not
  indicator: delayed execution of slow momentum signals · asset: multi · horizon: days · conditions: depends on how long fills are delayed relative to holding period · testable: yes - delay-sensitivity backtest · confidence: medium
  ^MT137-C17-X1

### C18
- **Rob Carver** SAA is top-down: set return, risk and correlation expectations, build the efficient frontier, choose the max Sharpe or minimum risk meeting hurdle, then fill sleeves (hedge funds, private credit, CTAs) as boxes.  #mech/structural_shift
  > it's a very kind of structured top-down process, basically.
  asset: multi · horizon: years · testable: no - description · confidence: high
  ^MT137-C18-1
- **Rob Carver** UK defined-benefit pension funds, with obligations to retirees and investment risk on the manager, hold large bond allocations, which has supported long-dated UK bonds and distorts the yield curve.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > that's been particularly good for long-dated UK bonds, actually. Um, that does weird things to the yield curve
  indicator: UK DB pension demand for long-dated gilts · asset: rates · direction: long-dated UK bond prices supported, curve distorted · horizon: years · testable: partly - liability-driven demand and curve shape can be examined · confidence: medium
  ^MT137-C18-X1

### C19
- **Rob Carver** SAA box structure ignores correlations across boxes, e.g. a CTA correlated to Danish equities added to a Danish-equity-heavy portfolio.  #mech/risk_management
  > I happen to put into one of my boxes something that's highly correlated to something in another box, that does not enter into the decision process.
  indicator: cross-box correlation · asset: multi · testable: yes · confidence: high
  ^MT137-C19-1
- **Rob Carver** TPA evaluates additions holistically (add CTA, dial down equities, or replace), which should favour diversifying strategies.  #mech/structural_shift
  > we look at the thing as a whole
  asset: multi · direction: more allocation to diversifiers if adopted · horizon: years · testable: partly · confidence: medium
  ^MT137-C19-2
- **Rob Carver** TPA lacks formal definition; a quant formulation would be Markowitz optimisation with utility and constraints.  #mech/research_method
  > a quant would say something like maximize uh utility function where you input the correlation the standard deviation and the expected vector of mean returns plus your constraints
  asset: multi · testable: no · confidence: medium
  ^MT137-C19-3
- **Rob Carver** Carver finds the total portfolio approach vague and apparently invented by management consultants, with charts and phrases, and lacking a quant definition.  #mech/research_method _(added by map cross-check)_
  > it does seem to be something that's been invented by some management consultants and it's very vague
  indicator: total portfolio approach definition · asset: multi · horizon: n/a · testable: no - qualitative · confidence: medium
  ^MT137-C19-R1

### C20
- **Rob Carver** CTAs do not fit in the hedge fund box or the tail-protection box because their correlation is different, they have no crisis guarantee but a positive Sharpe, so portfolio-level assessment helps them.  #mech/risk_management
  > unlike proper tail protection funds, we can't guarantee that we'll make you money in in a in a down market.
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT137-C20-1
- **Rob Carver** If large quant-heavy allocators like ADIA adopt TPA with formal publications, it could be a game-changer for trend following allocations.  #mech/structural_shift _(time-bound view)_
  > if they start doing it, then then I think that will really will be a game-changer
  asset: multi · horizon: years · conditions: if big allocators follow · testable: no - prediction · confidence: low
  ^MT137-C20-2

