---
source_id: MT117
title: "Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Investor 295"
date: 2024-05-15
channel: "Top Traders Unplugged"
url: 
words: 10817
claims: 54
added_by_crosscheck: 10
corrections: 2
crosscheck: "opus cross-check"
speakers: ["Nick Baltas (co-host, systematic strategist)", "Neils Kostrup Larsen (host, hedge fund manager)"]
tags: [source, layer0]
---
# Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Investor 295

**Speakers:** Nick Baltas (co-host, systematic strategist); Neils Kostrup Larsen (host, hedge fund manager)

**Summary:** May 2024 Systematic Investor episode: Baltas answers listener questions on agnostic risk parity, equal risk allocation across asset classes, ideal trend allocation and volatility regimes, then summarises his FT piece on equity momentum crowding (party and hangover analogy). Conclusion: fixed risk budgets embed return bets; dynamic allocation and vol scaling manage momentum crash risk.

**Approach:** trend following, risk allocation, agnostic risk parity, equity momentum crowding, volatility clustering, replication

**Cross-check completeness estimate of first read:** 0.88 - 45 first-reader claims cover most ideas; missed the 2024 macro sentiment shift, replicator tracking without cocoa, the trend-plus vs trend-minus disagreement, momentum-to-index link and exogenous crash triggers; two speaker errors.

## Argument map

**Episode thesis:** Baltas argues that any fixed risk budget or weighting scheme (60/40, risk parity, equal risk across asset classes, volatility-only scaling) embeds a hidden return forecast and a value bet, so trend portfolios should scale risk by correlation and let budgets follow where trends exist, keep broad coverage without screening out past underperformers (cocoa), and treat relative-value spreads built from small signal differences as fragile and arguably not trend following. He also explains why trend can work without serial correlation (volatility clustering, fundamental disagreement) and, from his Financial Times piece, why crowded equity momentum behaves like a party that ends in a liquidity-driven hangover, with volatility scaling as the prudent way to stay in. The host mostly agrees, preferring pure trend direction and dynamic sizing, and adds that a high trend allocation is mathematically attractive but far above what institutions accept.

### Nick Baltas (Systematic strategist (quant researcher) and co-host of the Systematic Investor series)
Fingerprint: #approach/trend_following #approach/portfolio_construction_stacking #approach/diversification_risk_parity #approach/regime_detection #approach/positioning_crowding #approach/behavioral_sentiment #approach/research_robustness_overfitting #approach/position_sizing_vol_target
_Speaker note: Name as in the ledger and caption ('Nick Bolas' in the raw text). Ledger corrections applied: C15-5 (the cocoa exposure had already been dialled down before the reversal because the vol spike weakened the vol-normalised signal) is Baltas, responding to the host's party analogy; C05-2 (only equities up in early May) is the host's remark, not Baltas's._

**Worldview premises**
- Breadth without performance screening is how trend following earns its keep: cocoa was historically among the largest negative contributors to trend following yet its 2024 rally helped, so markets should not be dropped for past underperformance; the portfolio will be asked why a market is missing either way. _[experience, stated; support: Cocoa as 2024 example; diversification logic.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C01-1|C01-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C01-2|C01-2]])
- In 2024 trends appeared in markets that historically were not the big drivers (cocoa, equities); one cannot forecast which markets will trend, so breadth is the way to capture them. _[empirical, stated; support: 2024 market behaviour.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C02-1|C02-1]])
- Replication can only perform if the strategy it copies performs, and replicating faster programs is harder because of style drift and repositioning; it can capture broad macro trends efficiently with a limited set of markets (10 to 40), though how many are enough is debated. _[theoretical, stated; support: Reasoning; he explicitly disclaims data and a view on being a fan.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C03-1|C03-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C03-2|C03-2]])
- In a mean-variance setup, two 95%-correlated markets with signals 1 and 0.9 lead to long the stronger, short the weaker and a levered tiny spread: an apparently high-Sharpe relative value trade that is fragile if the signal ordering reverses; such concentrated, small-differential positions are arguably no longer trend following. _[theoretical, stated; support: Worked example (NASDAQ versus S&P); technical reasoning.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C06-1|C06-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C06-2|C06-2]])
- CFM's agnostic risk parity allocates equal risk across all principal components of the asset correlation matrix, blending the market component with a small relative-value spread component; scaling by signal strength rather than a binary signal already introduces cross-sectional tilts without forcing shorts. _[theoretical, stated; support: Explanation of CFM's paper (about six to seven years old) using PCA.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C07-1|C07-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C07-2|C07-2]])
- Concentrating on the dominant macro trend component has diminishing value, so diversifying components that need not agree with trend direction (agnostic risk parity spreads, carry, reversion) give a 'trend plus' strategy; but he does not himself favour grossing up a pure relative-value trade and prefers the middle ground or pure direction. _[theoretical, stated; support: Argument and own work enhancing trend with carry or reversion.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C07-X1|C07-X1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C08-1|C08-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C06-R1|C06-R1]])
- Any fixed weighting scheme (60/40, equal risk across asset classes) carries an implied return forecast and a built-in value bet because it sells winners and buys losers to rebalance; inverse-volatility weights across asset classes imply equal expected Sharpe ratios. _[theoretical, stated; support: Black-Litterman style algebra and a 50/50 equity-bond example.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C08-2|C08-2]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C08-3|C08-3]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C10-1|C10-1]])
- Allocating risk dynamically toward where trends exist (e.g. skipping equities in 2022, moving from commodities to the dollar) is more prudent than fixed risk budgets, which force allocation into non-trending markets. _[experience, stated; support: 2022 hindsight examples; he says he would need to define 'better'.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C09-1|C09-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C10-1|C10-1]])
- Scaling positions by volatility alone leaves highly correlated clusters over-represented and loosely correlated markets under-represented; delivering equal risk needs correlations, not just volatility, and translating risk into dollars is the most important step. _[theoretical, stated; support: Four-market example (two highly correlated, two loosely correlated, same volatility).]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C09-2|C09-2]])
- A pure long-term return maximiser would hold close to 100% trend versus a 60/40 portfolio, but institutions face tracking error and career risk against their policy portfolio, so there is no single optimal allocation: it is a utility trade-off between downside improvement, return and tracking error. _[theoretical, stated; support: Mathematical comparison of historical expected returns; qualitative institutional reasoning.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C10-2|C10-2]])
- Trend following works better when investors disagree about fundamental value (post-2020 inflation uncertainty widens views, so price moves carry more information), and worse under consensus valuation where shocks revert. _[theoretical, stated; support: His 2022 Financial Times piece on inflation and trend following.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C11-2|C11-2]])
- Volatility clustering produces return predictability without serial correlation and skewness, which alone supports trend following; so trend should do better in high-volatility regimes for a given asset, but high volatility is not necessary: lower-volatility assets such as bond duration have delivered stronger trend Sharpe, and segregated markets with persistent producer, consumer and speculator imbalances (alternative commodities) can trend without high volatility. _[empirical, stated; support: Academic work from about ten years earlier (not named); the duration and commodity points from his own knowledge.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C11-3|C11-3]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C12-1|C12-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C12-2|C12-2]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C12-3|C12-3]])
- Trend is univariate (an appreciating market continues) whereas momentum is cross-sectional (relative winners keep beating relative losers regardless of sign). _[theoretical, stated; support: Definitions used in his own writing.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C13-1|C13-1]])
- Q1 2024 US equity momentum, driven by AI stocks such as Nvidia, was its best three-month stretch in 20 to 25 years (roughly double the second best), index concentration rose with it and hedge funds held record exposure to the momentum factor, explicitly or implicitly; the same rally lifted equity indices and so fed trend followers' equity gains. _[empirical, stated; support: Hedge fund positioning data and factor returns cited from his FT piece; no figures beyond the ranking.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C13-2|C13-2]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C13-3|C13-3]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C13-X1|C13-X1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C02-2|C02-2]])
- Momentum is anchored in cognitive biases, so the trade is itself a behavioural pattern; traders know the crash risk but stay for fear of missing out and redemption risk. _[behavioural, stated; support: Cited empirical and research results on momentum traders' redemption fear.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C14-3|C14-3]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C14-R1|C14-R1]])
- Timing the end of a crowded equity momentum rally is very hard; the downside can be endogenous (funding liquidity and credit lines exhausted at maximum gross exposure) or exogenous (idiosyncratic shock such as AI hype fading, or value investors buying cheap and shorting expensive stocks). _[theoretical, stated; support: Momentum crash literature; he says he does not predict crashes.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C14-1|C14-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C14-4|C14-4]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C15-X1|C15-X1]])

**Chain: Mean-variance relative value versus pure trend: why small signal differences are fragile**
1. two assets with 95% correlation and signals 1 and 0.9 → optimizer goes long the stronger and short the weaker: it focuses on the smaller eigenvalues (spread) and ignores the market beta move ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C06-1|C06-1]])
2. spread has almost zero risk and a small expected return → gross-up to large leverage, an apparently high-Sharpe relative value trade: risk is tiny relative to the signal differential ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C06-1|C06-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C08-1|C08-1]])
3. the outperformer-underperformer ordering reverses → heavy loss on a concentrated, levered position: the position depends entirely on forecast persistence and on noise ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C06-2|C06-2]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C08-1|C08-1]])
4. middle ground: agnostic risk parity or signal-strength scaling → keep market exposure and add a small spread component without forcing shorts: equal risk across principal components blends market and spread ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C07-1|C07-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C07-2|C07-2]])
- Evidence: PCA-based reasoning and a worked example; no performance data on the CFM approach given.
- Fails when: Pure spread version fails when signals do not persist; he says either extreme is dependent on history repeating.

**Chain: Fixed risk budgets embed return expectations and miss correlation**
1. a fixed weighting scheme (60/40, equal risk by asset class) → implied return forecast and value bet through rebalancing: selling winners and buying losers to restore weights ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C08-2|C08-2]])
2. inverse-volatility weights across asset classes → equal expected Sharpe ratios assumed: weights proportional to 1/volatility ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C08-3|C08-3]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C10-1|C10-1]])
3. volatility-only scaling → correlated clusters over-represented and loosely correlated markets under-represented: equal volatility does not give equal risk contribution when correlations differ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C09-2|C09-2]])
4. dynamic budgets that follow trend strength → capital goes where trends exist; none is forced into non-trending markets: no hard-wired expectation of equal Sharpe ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C09-1|C09-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C10-1|C10-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C09-3|C09-3]])
- Evidence: Algebraic argument and 2022 hindsight examples; no backtest comparing fixed and dynamic budgets.
- Fails when: Not stated; he notes correlations change and complexity can overfit (the listener's concern).

**Chain: Why trend can work: fundamental disagreement and volatility clustering**
1. before 2020, consensus on valuation with subdued disagreement → price deviations from exogenous shocks are faded and revert: everyone agrees the value is 100, so a move to 99 or 101 is a reversion trade ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C11-2|C11-2]])
2. post-2020 inflation uncertainty widens the distribution of views → price moves carry more information and trend following performs: any price move shifts the future distribution of views ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C11-2|C11-2]])
3. volatility clusters → a big move is more likely followed by another in the same direction; skewness appears without serial correlation: serial correlation sits in volatility rather than in returns ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C11-3|C11-3]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C12-1|C12-1]])
4. segregated markets with persistent imbalances between users and speculators → trendy behaviour without needing high volatility: structural imbalances persist ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C12-3|C12-3]])
- Evidence: His 2022 FT article and unnamed academic work; low-volatility duration cited as counterexample.
- Fails when: High volatility is not necessary and not sufficient (the host adds that higher market volatility does not always mean better trend performance).

**Chain: Momentum party and hangover: self-reinforcing crowding and the exit**
1. early crowding into a momentum trade → the trade takes off: needs enough participants at the start, like a party ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C14-2|C14-2]])
2. buying winners raises prices, which attracts more buying (positive feedback) → portfolios and indices concentrate in the leading names; hedge funds hold record momentum exposure: self-fulfilling prophecy; leverage and inflows act as catalysts ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C13-3|C13-3]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C14-2|C14-2]])
3. fear of missing out and redemption risk → momentum traders stay despite knowing the crash risk: asset managers competing for capital are averse to redemptions ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C14-3|C14-3]])
4. funding liquidity and credit lines are exhausted at maximum gross exposure (endogenous) or an idiosyncratic shock arrives (exogenous) → fire sales, short squeezes and a liquidity-driven unwind: everyone exits through a small door ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C14-4|C14-4]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C15-3|C15-3]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C15-X1|C15-X1]])
- Evidence: Momentum-crash literature, hedge fund positioning data, party analogy; he does not predict crashes.
- Fails when: Timing is very hard; the rally continued past mid-Q2; exposure data may hint at a turning point but cannot call it.

**Decision process**
- [universe] Keep breadth in the trend portfolio without screening markets out for past underperformance.. Why: Unpredictable markets sometimes deliver the big trends (cocoa); diversification is the point. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C01-2|C01-2]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C02-1|C02-1]])
- [signal] Scale positions by signal strength rather than using a binary signal, without forcing shorts against the signal direction.. Why: Gives cross-sectional tilts toward the stronger market without pure relative-value concentration. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C07-2|C07-2]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C08-1|C08-1]])
- [sizing] Allocate risk dynamically across asset classes toward where trends exist and scale by volatility and correlation, not volatility only.. Why: Fixed budgets embed equal-Sharpe expectations; volatility-only scaling distorts risk contribution. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C09-1|C09-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C09-2|C09-2]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C10-1|C10-1]])
- [portfolio] Consider adding diversifying components (carry, reversion, agnostic risk parity spreads) to trend as 'trend plus', but avoid a pure grossed-up relative-value spread.. Why: Concentration on the dominant macro component has diminishing value; spread trades are noisy and concentrated. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C07-X1|C07-X1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C08-1|C08-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C06-2|C06-2]])
- [risk] In equity momentum, volatility-scale exposure so participation falls when its volatility rises; be selective by avoiding losers far from recent highs on the short side, or hedge momentum exposure completely.. Why: Stays in the trade while reducing crash risk; low-priced losers rebound most in a crash. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C15-1|C15-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C15-2|C15-2]])
- [risk] Watch gross exposure data as a possible hint of a turning point in a crowded momentum trade.. Why: Funding exhaustion at maximum gross exposure is one route to forced selling; calling it remains very hard. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C15-3|C15-3]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C14-4|C14-4]])
- [execution] Dynamic sizing already cut cocoa exposure before the reversal because a volatility spike weakened the vol-normalised signal even as price kept rising.. Why: Vol normalisation reduces size in blow-off moves. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C15-5|C15-5]])

**Evidence style:** Mathematical and algebraic first-principles reasoning (PCA, implied returns, risk contributions), plus cited academic research (momentum crashes, volatility clustering) and recent market anecdotes (cocoa, AI momentum); no backtests presented on air.

**Views at the time**
- (2024-05-10 (recorded Friday; uploaded 2024-05-15)) Trend programs lost in early May 2024 on a yield reversal, a yen rally on intervention risk, a dip in energy longs and a cocoa reversal; there was no common fundamental cause.. Reasoning: Several unrelated moves reversed in the first few days of May. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C04-2|C04-2]])
- (2024-05-10) Macro sentiment shifted substantially in the first months of 2024 from expected Fed cuts toward higher for longer, no cut or even a hike.. Reasoning: A driver of trend positioning that he monitors. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C02-X1|C02-X1]])
- (2024-05-10) US equity momentum, led by AI stocks, is very strong and raises concern that the trade is overcrowded; it is very hard to time the end, so manage exposure by volatility scaling.. Reasoning: Record hedge fund momentum exposure; concentration; self-reinforcing feedback. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C02-2|C02-2]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C13-2|C13-2]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C13-3|C13-3]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C14-1|C14-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C15-1|C15-1]])
- (2024-05-10) Cocoa's 2024 rally vindicates holding markets that have historically not trended well.. Reasoning: Cocoa was among the largest historical negative contributors before 2024. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C01-1|C01-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C01-2|C01-2]])
- (2024-05-10) A momentum unwind could come from an exogenous shock such as AI enthusiasm fading or from value investors buying cheap and shorting expensive stocks.. Reasoning: Idiosyncratic shocks are even harder to foresee than a funding squeeze. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C15-X1|C15-X1]])

### Neils Kostrup Larsen (Host (Top Traders Unplugged); veteran hedge fund manager running a dynamic-sizing trend program)
Fingerprint: #approach/trend_following #approach/position_sizing_vol_target #approach/manager_selection_allocation #approach/replication_indexing #approach/diversification_risk_parity
_Speaker note: Name as in the ledger (the host, Niels Kaastrup-Larsen). Host questions are context; mapped because he states views on sector behaviour, replication, trend allocation and pure trend. Ledger-corrected: C05-2 (only equities positive in early May; worse than average down month in a great year) is his, and C15-5 is Baltas's, not his._

**Worldview premises**
- Liquid currency and equity index markets have been poor trend sectors over the last 10 to 15 years because of quick corrections, while energies trended better. _[experience, stated; support: From memory of sector performance; hedged ('from memory').]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C02-3|C02-3]])
- High daily correlation is not the same as matching performance: replicators can track closely, underperform and later outperform, so lower fees do not guarantee outperformance; a replicator kept pace with SG CTA in 2024 even though many CTAs profited from cocoa, which the replicator does not trade. _[experience, stated; support: Discussions with the replicator's manager; no analysis done.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C04-1|C04-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C04-X1|C04-X1]])
- Trend managers give every market the same opportunity, risking the same amount only when trend strength is the same, rather than forcing equal risk by sector. _[experience, stated; support: Knowledge of how several trend managers allocate; he cannot speak for everyone.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C09-3|C09-3]])
- Anything that is not pure trend is better called 'trend minus': in the long run trend following should outperform the other components, so adding them may cannibalise rather than enhance; he prefers to focus on direction. _[experience, stated; support: Personal preference as a trend follower 'by heart'.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C08-X1|C08-X1]])
- A 50% S&P 500 and 50% Dunn trend mix historically beat either alone because correlation benefits lift compounding; three large consultants said their analysis implied a trend allocation of 45 to 50%, far above what clients accept. _[empirical, stated; support: Dunn's web-based portfolio tool (monthly tracking) and an earlier podcast with consultants.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C10-3|C10-3]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C11-1|C11-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C10-R1|C10-R1]])
- Higher inflation volatility has created trending opportunities across many markets compared with the stable low-inflation era, but higher market volatility does not always mean better trend performance; trend following is adaptive and should not be put in a box (cocoa was a smooth uptrend before going parabolic; the 2022 bond trends came without panic). _[experience, stated; support: Examples and earlier macro series conversations.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C12-4|C12-4]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C12-R1|C12-R1]])
- Trend followers with dynamic position sizing scale out when a market goes volatile, which naturally reduces exposure to crowded blow-off moves. _[experience, stated; support: Own practice; uses the party analogy to say a trend follower would leave when the party gets crazy.]_ ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C15-4|C15-4]])

**Decision process**
- [signal] Focus on signal direction (pure trend) and let other components bolt on beyond it.. Why: Trend following should outperform non-trend components in the long run. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C08-X1|C08-X1]])
- [sizing] Use dynamic position sizing that scales out when a market goes volatile.. Why: Reduces exposure to crowded blow-off moves. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C15-4|C15-4]])
- [portfolio] Give each market the same opportunity but risk the same amount only when trend strength is the same, rather than forcing equal sector risk.. Why: Avoids forcing risk into non-trending markets. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C09-3|C09-3]])

**Evidence style:** Industry experience, sector memory and anecdotes (Dunn's tool, consultants' views, Twitter replication debate); reports index data; he does not run formal tests on air.

**Views at the time**
- (2024-05-10 (recorded Friday; uploaded 2024-05-15; data as of Wednesday)) Early May 2024 was a soft start with only equities positive for trend programs, a worse-than-average down month in a great year; BTOP50 -2.66% for May and +8.18% YTD, SG CTA -3% (about +8.5% YTD), SG Trend -3.7% (about +10% YTD), short-term traders -0.70% (+2.85% YTD), MSCI World +3.2% (+7.63% YTD), S&P 500 TR +3.58% in May (+9.83% YTD).. Reasoning: Month-to-date recap. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C05-1|C05-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C05-2|C05-2]])
- (2024-05-10) A replication debate will continue as more ETF entrants come; correlation is not performance.. Reasoning: Asks how closely a replicator tracks versus outperforming through fees. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C04-1|C04-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C04-X1|C04-X1]])
- (2024-05-10) Cocoa exposure was reduced before its reversal because the vol spike weakened the signal (agreeing with Baltas).. Reasoning: Vol-normalised signals. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C15-5|C15-5]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C15-4|C15-4]])

### Disagreements
- **'Trend plus' versus pure trend**: Nick Baltas: Diversifying components that need not agree with trend direction (agnostic risk parity spread, carry, reversion) can enhance trend; concentrating on the dominant trend component has diminishing value; but he prefers keeping signal direction and avoids grossed-up spreads. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C07-X1|C07-X1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C08-1|C08-1]]); Neils Kostrup Larsen: Prefers pure trend; anything else is 'trend minus' because trend should outperform in the long run and extra components may cannibalise it. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C08-X1|C08-X1]])
- **How much to allocate to trend following**: Nick Baltas: Mathematically a pure return maximiser holds close to 100% trend, but career and tracking-error constraints mean there is no single optimal allocation. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C10-2|C10-2]]); Neils Kostrup Larsen: Surprised at 100% (suggests something like 70 to 80 might already be unrealistically high); a 50/50 S&P and Dunn mix beat either alone historically; consultants implied 45 to 50%, far above what clients accept. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C10-R1|C10-R1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C10-3|C10-3]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C11-1|C11-1]])
- **Replication as an approach**: Nick Baltas: Replication depends on the underlying strategy performing and is harder for faster programs, but can capture broad macro trends with a limited set of markets; he declines to say whether he is a fan. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C03-1|C03-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C03-2|C03-2]]); Neils Kostrup Larsen: Impressed that a replicator kept pace with the SG CTA index without cocoa, but stresses that high correlation does not equal matching performance and that tracking closeness is what matters if tracking is the aim. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C04-X1|C04-X1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C04-1|C04-1]])
- **Does trend need high volatility?**: Nick Baltas: Volatility clustering supports trend and trend should do better in high-volatility regimes for a given asset, but high volatility is not necessary: bond duration and segregated commodity markets trend without it. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C11-3|C11-3]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C12-2|C12-2]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C12-3|C12-3]]); Neils Kostrup Larsen: Trend following should not be boxed in; inflation volatility is more interesting than market volatility, and higher market volatility does not always bring better performance. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C12-4|C12-4]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C12-R1|C12-R1]])

### Gaps and conflicts
- Baltas says the pure long-run return maximiser would hold close to 100% trend based on higher historical expected return versus 60/40; the host immediately finds this surprising and the claim is not supported with figures, drawdowns or the sample period. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C10-2|C10-2]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C10-R1|C10-R1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C10-3|C10-3]])
- The claim that volatility clustering alone generates trend-like behaviour without serial correlation rests on an unnamed academic paper; the link to the listener's alternative-markets argument is only partly addressed, since Baltas then says high volatility is not necessary. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C11-3|C11-3]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C12-1|C12-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C12-2|C12-2]])
- The statement that fixed weights imply a value bet and risk parity implies equal Sharpe is algebraically true as an implied-views argument but does not show that dynamic budgets perform better; he explicitly declines to define 'better'. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C08-2|C08-2]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C08-3|C08-3]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C09-1|C09-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C10-1|C10-1]])
- Baltas says 2022 hindsight shows equities should have been skipped and commodities swapped for the dollar; this is perfect-foresight reasoning, not a tested dynamic allocation rule. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C09-1|C09-1]])
- The Q1 2024 'best three-month stretch in 20 to 25 years, roughly double the second best' momentum claim has no stated factor definition (long-short construction, universe) and is said to continue past mid-Q2; the crowding evidence (record hedge fund momentum exposure) is asserted from positioning data not shown. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C13-2|C13-2]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C13-3|C13-3]])
- The party analogy lacks a measurable trigger: gross exposure data are said to hint at a turning point but he concedes calling it is very hard, and no threshold is given. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C14-1|C14-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C15-3|C15-3]])
- Baltas' defence of 'not screening out underperformers' (cocoa) relies on one winning example; markets that never trend are also part of the breadth, and the cost of holding them is not discussed. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C01-1|C01-1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C01-2|C01-2]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C02-1|C02-1]])
- Ledger attributions of C05-2 and C15-5 were swapped between the two speakers and are corrected here; both speakers agree on the cocoa de-risking point. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C05-2|C05-2]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C15-5|C15-5]])
- The host's claim that a replicator 'kept pace with SG CTA' is explicitly not backed by analysis, and Baltas declines to evaluate it without data. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C04-X1|C04-X1]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C03-1|C03-1]])
- The signal-direction-versus-strength question (C05-3) is a listener's (Peter's) question read by the host; it is context for Baltas' answer, not a view of either speaker, and its premise (that going slightly short a weak correlated asset reduces volatility) is tested only through Baltas' mean-variance example. ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C05-3|C05-3]], [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C06-1|C06-1]])

### Forward-looking inputs (reader synthesis)
(reader) Inputs the speakers treat as relevant: dispersion of fundamental views (inflation uncertainty widens disagreement and favours trend), volatility clustering and the volatility regime of each asset (high volatility helps but is not required), producer, consumer and speculator imbalances in segregated commodity markets, hedge fund gross exposure and momentum factor exposure (crowding and potential liquidity events), funding liquidity and credit lines, and the shift in Fed expectations (cuts versus higher for longer). Horizons are not specified; momentum timing is explicitly said to be unpredictable. Neither speaker issues price forecasts.

### Reader inferences (not stated by the speakers)
- (reader) Baltas' common theme is that any pre-set allocation is a bet in disguise (equal risk implies equal Sharpe, fixed weights imply value, volatility-only scaling hides correlation), so trend's advantage is letting evidence set the weights.
- (reader) The agnostic-risk-parity discussion shows a boundary for trend following: scaling by signal strength keeps direction, whereas spread trades use direction only as a ranking and bring in an optimiser's fragility.
- (reader) The momentum party analogy and the host's dynamic-sizing reply imply that a trend follower with volatility normalisation is structurally a seller into blow-off phases, which is why trend can be partly insulated from the crash it helps ride.
- (reader) The cocoa example is used twice (breadth defence, vol-normalised de-risking); together they imply that breadth earns the tail and sizing rules protect against its reversal.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | intro; cocoa rally and the case for breadth in trend portfolios |
| C02 | 3 | diversification captures unpredictable trends; macro sentiment shift; AI equity crowding; sector trendiness |
| C03 | 2 | replication debate (Beer vs Pickering): requirements and limits |
| C04 | 2 | correlation vs performance in replication; May 2024 CTA drawdown drivers |
| C05 | 3 | May 2024 index numbers; book guide plug; listener question on agnostic risk parity |
| C06 | 2 | signal direction vs diversification; two extremes (long both vs RV long-short gross up) |
| C07 | 2 | agnostic risk parity blends market PC and RV PC; signal-scaled sizing implies cross-sectional tilt |
| C08 | 3 | trend plus vs trend minus; equal risk across asset classes question and implied return expectations |
| C09 | 3 | dynamic risk allocation across asset classes; vol scaling vs correlation-aware risk allocation; same opportunity not same risk |
| C10 | 3 | forced risk budgets imply return expectations; optimal trend allocation for long-horizon investor |
| C11 | 3 | consultants would pitch 45-50% trend; 50/50 S&P/Dunn; fundamental disagreement regime and volatility clustering |
| C12 | 4 | volatility clustering and trend; producer/consumer/speculator imbalances; trend adapts, inflation volatility as driver |
| C13 | 3 | FT article on equity momentum parties and hangovers; trend vs momentum definitions; record momentum quarter and concentration |
| C14 | 4 | momentum crowding and crash analogy; fear of redemption; endogenous funding crash |
| C15 | 5 | momentum exit liquidity, exogenous shock, ways to manage momentum exposure; trend follower scales out of vol spikes |
| C16 | 0 | outro and plugs (cocoa remark finishes here, recorded under C15) |

## Claims

### C01
- **Nick Baltas** Cocoa was historically one of the largest negative contributors to trend following, yet its 2024 rally helped, which defends holding markets that have never trended well.  #mech/structural_shift _(time-bound view)_
  > one of the largest negative contributors in a trend following strategy that is CA right
  indicator: cocoa trend contribution · asset: commodities · direction: long cocoa in 2024 · horizon: years · conditions: cocoa trends only occasionally; benefit arrives unannounced · testable: yes - per-market contribution history · confidence: high
  ^MT117-C01-1
- **Nick Baltas** Trend portfolios should include markets without screening out past underperformers, because diversification means unpredictable markets sometimes deliver the big trends.  #mech/risk_management
  > we were trying to be agnostic to the underperformer in some respect because at the end of the day you also play the diversification game
  indicator: universe breadth in trend following · asset: multi · direction: hold broad universe · horizon: years · testable: partly - compare screened vs unscreened universes · confidence: high
  ^MT117-C01-2

### C02
- **Nick Baltas** In 2024 trends appeared in markets not historically big drivers (cocoa, equities); one cannot forecast which, so breadth is the way to capture them.  #mech/cycle_persistence _(time-bound view)_
  > persistent Trends not necessarily in a way that we can forecast but certainly by putting them in portfolio we can achieve to to diversify away but also capture those returns
  indicator: trend returns across markets · asset: multi · horizon: months · testable: partly - one-year observation · confidence: high
  ^MT117-C02-1
- **Nick Baltas** AI-stock equity momentum has pushed prices up and raises concern that the trade is overcrowded.  #mech/crowding_positioning _(time-bound view)_
  > this Equity Market rally specific speically on those AI names and this Equity momentum kind of driving prices higher and higher and higher
  indicator: AI equity momentum · asset: equities · direction: long AI equities · horizon: months · conditions: crowding risk · testable: no - opinion on crowding, no measure given · confidence: medium
  ^MT117-C02-2
- **Neils Kostrup Larsen** Liquid currency and equity index markets have been poor trend sectors because of quick corrections, while energies trended better over the last 10 to 15 years.  #mech/cycle_persistence
  > some of the sectors that we would think would be great for Trend because they're liquid like currencies like equities have not necessarily been that great to trade from a trend following perspective
  indicator: sector level trend performance · asset: multi · horizon: years · conditions: quick corrections damage trend following · testable: yes - sector attribution of trend · confidence: medium
  ^MT117-C02-3
- **Nick Baltas** Macro sentiment shifted substantially in the first months of 2024 from expected Fed cuts toward higher for longer, no cut or even a hike, which Baltas monitors as a driver of trend positioning.  #mech/policy_reaction _(added by opus cross-check, time-bound view)_
  > is it here for Longer Now is it going to be no cut and maybe a [L60] hike um is it going to be as is for now I think this shift in um in micro sentiment over the first four or five months of the year has been quite substantial
  indicator: market-implied Fed path (cuts vs hold vs hike) · asset: rates · direction: fewer cuts priced, yields up · horizon: months · testable: partly - track priced Fed path changes Jan-May 2024 vs trend P&L · confidence: medium
  ^MT117-C02-X1

### C03
- **Nick Baltas** A replication product can only perform if the CTA strategy it copies performs, and replicating faster programs is harder because of style drift and repositioning.  #mech/research_method
  > replication is dependent upon its success to replicate by nature but also it's dependent the success of the underlying instrument we're trying to replicate
  indicator: CTA index replication · asset: multi · conditions: faster programs harder to replicate · testable: partly - tracking tests possible · confidence: medium
  ^MT117-C03-1
- **Nick Baltas** Replication can capture broad macro trends efficiently with a limited market set (10 to 40 markets), though how many are enough is debated.  #mech/research_method
  > I see the value of grouping together uh investment profiles and then trying to find a way to achieve that in an efficient manner with a limited set of markets
  indicator: trend replication with limited universe · asset: multi · testable: partly - tracking error vs number of markets · confidence: low
  ^MT117-C03-2

### C04
- **Neils Kostrup Larsen** High daily correlation is not the same as matching performance: replicators can track closely then underperform and later outperform, so lower fees do not guarantee outperformance.  #mech/research_method
  > it is how closely can you actually track the thing you're trying to replicate that to me is quite important
  indicator: correlation vs return tracking of replicator to SG CTA index · asset: multi · testable: yes - compare correlation and cumulative return gap · confidence: medium
  ^MT117-C04-1
- **Nick Baltas** Early May 2024 trend programs lost on a yield reversal, a yen rally on intervention risk, a dip in energy longs and a cocoa reversal, with no common fundamental cause.  #mech/cycle_persistence _(time-bound view)_
  > yields reverted that was one move um the JPY rallied I guess on the uh I guess an intervention risk expectations
  indicator: trend losses in rates, JPY, energy, cocoa · asset: multi · horizon: weeks · conditions: reversals across unrelated markets · testable: partly - trend P&L by sector in May 2024 · confidence: medium
  ^MT117-C04-2
- **Neils Kostrup Larsen** A CTA replicator kept pace with the SG CTA index in 2024 even though many CTAs made money in cocoa, a market the replicator does not trade.  #mech/research_method _(added by opus cross-check, time-bound view)_
  > I'm impressed with Andrew's ability to keep up with the Sugen CTA index in a time where clearly a lot of CT have been making money from Coco which is a market he does not
  indicator: replicator ETF vs SG CTA index tracking 2024 · asset: multi · horizon: months · conditions: single-market outliers not traded by the replicator · testable: yes - compare DBMF-style replicator vs SG CTA index in 2024 · confidence: medium
  ^MT117-C04-X1

### C05
- **Neils Kostrup Larsen** As of mid-May 2024 BTOP50 was down 2.66% for the month and up 8.18% YTD, SG CTA down 3%, and SG Trend down 3.7%, while the S&P 500 total return was up 3.58% in May.  #mech/cycle_persistence _(time-bound view)_
  > the btp 50 is down 2.66% for May still up 8.18 for the year soen CTA index down 3% for May
  indicator: BTOP50, SG CTA, SG Trend, S&P 500 total return · asset: multi · horizon: weeks · testable: yes - published index data · confidence: high
  ^MT117-C05-1
- **Nick Baltas** In early May 2024 only equities were positive in trend programs, so the month was a worse than average down month for trend, though the year stayed strong.  #mech/cycle_persistence _(time-bound view)_
  > the only sector that's up so far this month is is equities and the rest is down
  indicator: trend sector returns · asset: multi · horizon: weeks · testable: yes - sector P&L · confidence: high
  **Correction (cross-check):** wrong speaker: 'the only sector that's up so far this month is equities ... nothing dramatic, it's a great year' is said by Neils Kostrup Larsen; Baltas only said the month could still turn positive → Neils Kostrup Larsen: in early May 2024 only equities were positive for trend programs, making it a worse than average down month, but nothing dramatic in a strong year.
  ^MT117-C05-2
- **Neils Kostrup Larsen** A listener asks whether signal direction should always dominate signal strength in portfolio construction, e.g. long a strong-signal asset and slightly short a correlated weak-signal asset to cut volatility.  #mech/research_method
  > should signal Direction
  indicator: trend signal direction vs signal strength · asset: multi · testable: yes - compare pure trend vs agnostic risk parity · confidence: medium
  ^MT117-C05-3

### C06
- **Nick Baltas** A mean-variance optimizer would long the stronger and short the slightly weaker of two 95%-correlated markets and lever the tiny spread, creating a high-Sharpe-looking relative value trade that is fragile to the signal ordering reversing.  #mech/risk_management
  > I observe two markets very high correlation
  indicator: mean-variance with highly correlated pairs · asset: equities · conditions: breaks if the weaker market outperforms (e.g. NASDAQ vs S&P) · testable: yes - simulate optimizer concentration · confidence: high
  ^MT117-C06-1
- **Nick Baltas** Relative value positions built from small signal differentials depend entirely on forecast persistence, create concentrated positions and are arguably no longer trend following.  #mech/risk_management
  > heavily heavily heavily dependent on those signals playing out exactly as they were observed
  indicator: RV trades levered from trend signal spread · asset: multi · testable: yes - concentration and turnover measurable · confidence: high
  ^MT117-C06-2
- **Nick Baltas** Baltas says he has no strong view for or against CFM's agnostic risk parity paper, only acknowledging its value and the considerations it raises; the real concern is the extreme of grossing up a pure relative-value spread.  #mech/new _(added by map cross-check)_
  > i don't generally have a strong view in favor or against
  indicator: agnostic risk parity · asset: multi · horizon: n/a · testable: no · confidence: high
  ^MT117-C06-R1

### C07
- **Nick Baltas** CFM's agnostic risk parity allocates equal risk across all principal components of the asset correlation matrix, blending the market component (long both) with a small relative value spread component.  #mech/risk_management
  > allocate equal units of risk across all the dimensions of a principal component analysis
  indicator: PCA of correlation matrix; equal risk across eigen-portfolios · asset: multi · direction: hold market exposure plus small RV · testable: yes - PCA risk allocation is implementable · confidence: medium
  ^MT117-C07-1
- **Nick Baltas** Scaling positions by signal strength instead of binary already introduces cross-sectional tilts (more contracts in the stronger of two correlated markets) without forcing shorts.  #mech/research_method
  > to the extent that we move away from a binary signal we're implicitly introducing some sort of crosssectional
  indicator: signal strength scaling · asset: multi · testable: partly - measure cross-sectional share of returns · confidence: medium
  ^MT117-C07-2
- **Nick Baltas** Concentrating on the dominant macro trend component has diminishing value, so adding diversifying components that need not agree with trend direction (agnostic risk parity's spread trades, or carry and reversion signals) gives a 'trend plus' strategy.  #mech/risk_management _(added by opus cross-check)_
  > there is a limit beyond which concentration on the big macro moves brings value from a trend following perspective and maybe we can add to it a diversifying component
  indicator: principal components of trend portfolio; carry and reversion overlays · asset: multi · testable: yes - compare pure trend vs trend plus diversifiers out of sample · confidence: medium
  ^MT117-C07-X1

### C08
- **Nick Baltas** Grossing up the signal differential in a pure relative value trade has too much dependence on noise and concentration, so the middle ground or pure trend direction is preferable.  #mech/risk_management
  > there's too much dependence on noise as well as concentration risk
  asset: multi · testable: partly - judgement · confidence: medium
  ^MT117-C08-1
- **Nick Baltas** Any fixed weighting scheme (e.g. 60/40, equal risk across asset classes) carries an implied return forecast and a built-in value bet because it sells winners and buys losers to rebalance.  #mech/risk_management
  > any waiting scheme we apply between as a class or between markets even if it's not explicit it has an implied expectation of return
  indicator: fixed weights / inverse volatility across asset classes · asset: multi · testable: yes - via Black-Litterman reverse optimisation · confidence: high
  ^MT117-C08-2
- **Nick Baltas** Inverse-volatility weights across asset classes imply equal expected Sharpe ratios across them.  #mech/risk_management
  > doing one over VA in principle between as a classes implicitly suggests that I expect all of them to deliver the same sharp ratio
  indicator: inverse volatility asset class weighting · asset: multi · testable: yes - follows from mean-variance algebra · confidence: high
  ^MT117-C08-3
- **Neils Kostrup Larsen** Larsen disagrees with 'trend plus': adding non-trend components may cannibalize rather than enhance trend, since he expects pure trend to outperform them over the long run; Baltas also prefers keeping signal direction.  #mech/research_method _(added by opus cross-check)_
  > anything that's not pure Trend I I you know I I wonder why do we call it Trend plus why not just call it Trend minus because in the long term Trend following hopefully will outperform
  indicator: pure trend vs trend plus overlays · asset: multi · horizon: years · testable: yes - long-run return of pure trend vs blended trend · confidence: medium
  ^MT117-C08-X1

### C09
- **Nick Baltas** Allocating risk dynamically across asset classes toward where trends exist (e.g. skipping equities in 2022, moving from commodities to the dollar) is more prudent than fixed risk budgets.  #mech/slow_reaction
  > allocating risk where the opportunity lies is prudent
  indicator: dynamic risk allocation across asset classes · asset: multi · horizon: months · testable: partly - compare dynamic vs equal risk budget · confidence: medium
  ^MT117-C09-1
- **Nick Baltas** Scaling positions by volatility alone leaves highly correlated clusters over-represented and loosely correlated markets under-represented; correct risk balance needs correlations, not just volatility.  #mech/risk_management
  > by Dollar allocating equal units because simply they happen to have the same Vault I'm ignoring the fact that they are actually correlated
  indicator: volatility scaling vs correlation-aware risk contribution · asset: multi · direction: downscale dollar exposure of correlated clusters · testable: yes - risk-contribution comparison · confidence: high
  ^MT117-C09-2
- **Neils Kostrup Larsen** Trend managers give every market the same opportunity, risking the same amount only when trend strength is the same, rather than forcing equal risk by sector.  #mech/risk_management
  > giving the same the same opportunity set is not the same as saying they we have the same risk allocation at all times
  indicator: trend-strength-scaled sizing across markets · asset: multi · testable: partly - describes practice · confidence: high
  ^MT117-C09-3

### C10
- **Nick Baltas** Forcing fixed risk budgets (including risk parity) embeds an expectation of equal Sharpe ratios; dynamic budgets avoid that by not forcing allocation into non-trending markets.  #mech/risk_management
  > forcing some risk budgets in itself implies expectation of returns
  indicator: risk parity · asset: multi · testable: yes - via mean-variance equivalence · confidence: high
  ^MT117-C10-1
- **Nick Baltas** Mathematically, a pure long-term return maximiser would hold close to 100% trend versus 60/40, but institutions' tracking error and career risk against the policy portfolio mean there is no single optimal allocation.  #mech/risk_management
  > if you have Trend following and maybe other liquid assets you would do 100% Trend following
  indicator: trend allocation vs 60/40 · asset: multi · horizon: years · conditions: institutional constraints (tracking error, liquidity) · testable: partly - allocation backtest vs policy portfolio · confidence: medium
  ^MT117-C10-2
- **Neils Kostrup Larsen** A 50% S&P 500 and 50% Dunn trend mix historically beat either alone because correlation benefits lift compounding.  #mech/liquidity_flows
  > a simple 50% S&P and 50% done actually outperforms even you know even our own returns
  indicator: 50/50 S&P 500 and Dunn trend fund · asset: multi · horizon: years · testable: yes - portfolio blend backtest · confidence: high
  ^MT117-C10-3
- **Neils Kostrup Larsen** The host is surprised that Baltas says the math implies 100% trend; he would have said maybe 70 or 80 and finds even that unrealistically high, and cites the 50/50 S&P and Dunn mix beating either alone as the reason he would not put his hand on his heart for 100%.  #mech/new _(added by map cross-check)_
  > i was a little bit surprised when you said the if you just look at the math you would take 100% trend
  indicator: trend allocation share · asset: multi · horizon: long term · conditions: historical Dunn and S&P returns · testable: yes - optimise a trend/60-40 mix · confidence: medium
  ^MT117-C10-R1

### C11
- **Neils Kostrup Larsen** Three large consultants said their analysis implied a trend allocation of 45 to 50%, far above what clients accept.  #mech/behavioral
  > they also admitted to saying well if we if we just looked at our analysis we would have to pitch to our clients a much much higher allocation
  asset: multi · testable: no - opinion · confidence: medium
  ^MT117-C11-1
- **Nick Baltas** Trend following works better when investors disagree about fundamental value (post-2020 inflation uncertainty widens views, so price moves carry more information), and worse under consensus valuation where shocks revert.  #mech/cycle_persistence
  > before 2020 part of the reason why Trend following was not necessarily delivering returns in line with history was the you know the increased fundamental certainty and subdued fundamental disagreement
  indicator: fundamental disagreement vs certainty regime · asset: multi · direction: long trend when disagreement high · horizon: years · conditions: high disagreement regimes · testable: partly - dispersion of forecasts as proxy · confidence: medium
  ^MT117-C11-2
- **Nick Baltas** Volatility clustering gives return predictability without serial correlation, so trend following should do better in high-volatility regimes for a given asset.  #mech/cycle_persistence
  > if volatility becomes higher and stays High it is more likely that a big move is followed by another big move in the same direction
  indicator: volatility clustering / high volatility regime · asset: multi · horizon: weeks · conditions: high-volatility periods for the asset · testable: yes - trend Sharpe conditional on vol regime · confidence: medium
  ^MT117-C11-3

### C12
- **Nick Baltas** A price process can look trending with zero serial correlation when volatility clusters and creates skewness, and this alone supports trend following.  #mech/structural_shift
  > it is rather that the volatility itself is serly correla in clusters
  indicator: volatility clustering and return skewness · asset: multi · testable: yes - simulate clustered vol with iid returns · confidence: medium
  ^MT117-C12-1
- **Nick Baltas** High volatility is not a necessary condition for strong trend results: among conventional asset classes lower-volatility assets such as bond duration have historically delivered stronger trend Sharpe ratios.  #mech/structural_shift
  > it's actually the lower volatile assets between them that have historically delivered stronger RS and we're talking about duration here
  indicator: trend Sharpe by asset volatility · asset: rates · horizon: years · testable: yes - cross-asset Sharpe vs vol · confidence: medium
  ^MT117-C12-2
- **Nick Baltas** Segregated markets with persistent producer, consumer and speculator imbalances (alternative commodities) can produce trending behaviour without needing high volatility.  #mech/liquidity_flows
  > alternative markets might have a very more might have a very segregated Marketplace between you know talk about you know some of those alternative commodity markets segregate Market between producers consumers as well as
  indicator: hedger/speculator imbalance in niche commodity markets · asset: commodities · horizon: months · testable: partly - commitments of traders data · confidence: low
  ^MT117-C12-3
- **Neils Kostrup Larsen** Higher inflation volatility has created trending opportunities across many markets compared with the stable low-inflation era, but higher market volatility does not always mean better trend performance.  #mech/cycle_persistence
  > when there is more volatility in inflation that seems to have an impact on trending opportunities in many different
  indicator: inflation volatility · asset: multi · horizon: years · conditions: not necessarily during transitions · testable: yes - trend returns vs inflation volatility · confidence: medium
  ^MT117-C12-4
- **Neils Kostrup Larsen** The host says trend following is adaptive and should not be put in a box: cocoa was a smooth uptrend before going parabolic and the 2022 bond trends were nice downtrends without panic, so volatility is sometimes but not always the driver.  #mech/new _(added by map cross-check)_
  > you shouldn't try to put it in a box
  indicator: trend conditions · asset: multi · horizon: n/a · testable: partly · confidence: high
  ^MT117-C12-R1

### C13
- **Nick Baltas** Trend is univariate (an appreciating market continues), whereas momentum is cross-sectional (relative winners keep beating relative losers regardless of sign).  #mech/research_method
  > trend is about a univariate movement that a market that is appreciating continues whereas momentum is more of a
  indicator: time-series trend vs cross-sectional momentum · asset: equities · testable: yes - definitions · confidence: high
  ^MT117-C13-1
- **Nick Baltas** Q1 2024 US equity momentum, driven by AI stocks such as Nvidia, was its best three-month stretch in 20 to 25 years, roughly double the second best, and index concentration rose with it.  #mech/crowding_positioning _(time-bound view)_
  > it's by far the largest performance that Equity momentum has had at least for the last 20 25 years
  indicator: US equity cross-sectional momentum factor · asset: equities · direction: long equity momentum winners · horizon: months · conditions: crash risk when crowded · testable: yes - factor return data · confidence: high
  ^MT117-C13-2
- **Nick Baltas** Equity momentum is a self-reinforcing positive feedback loop that concentrates portfolios, and hedge funds held record exposure to the momentum factor, explicitly or implicitly.  #mech/crowding_positioning _(time-bound view)_
  > the more it performs the more we want to buy the same names that have been performing and the more we're buying them the higher they go
  indicator: hedge fund exposure to momentum factor · asset: equities · horizon: months · conditions: crash risk grows with crowding · testable: yes - factor exposure data · confidence: high
  ^MT117-C13-3
- **Nick Baltas** Because AI momentum winners make up a large share of indices, the stock momentum rally lifted equity indices and so also fed trend followers' equity index gains, linking CTA returns to equity momentum crowding.  #mech/crowding_positioning _(added by opus cross-check, time-bound view)_
  > part of that has allowed the indices obviously to appreciate substantially because of the amount of concentration they bring to the indices and therefore the index performance has also helped follow us
  indicator: index concentration in momentum stocks; CTA equity sector P&L · asset: equities · direction: long equity indices · horizon: months · conditions: risk if momentum crashes · testable: yes - correlate equity momentum factor with CTA equity sector returns · confidence: medium
  ^MT117-C13-X1

### C14
- **Nick Baltas** Timing the end of a crowded equity momentum rally is very hard, so options are limited to managing exposure.  #mech/risk_management
  > it's very very hard to time that
  indicator: momentum crash timing · asset: equities · testable: no - opinion on difficulty · confidence: high
  ^MT117-C14-1
- **Nick Baltas** Like a party, a momentum trade needs early crowding to take off and catalysts such as leverage keep it going, but once crowded it relies on continued inflows.  #mech/crowding_positioning
  > there is there's an early stage crowding requirement for the trade to uh I guess take off
  indicator: momentum crowding · asset: equities · horizon: months · testable: partly - analogy · confidence: medium
  ^MT117-C14-2
- **Nick Baltas** Momentum traders know the crash risk but stay in because of fear of missing out and redemption risk for asset managers competing for capital.  #mech/behavioral
  > it's actually the fear of a redemption in other words the risk that is associated with a tactical decision to get out of a trade
  indicator: momentum trader behaviour · asset: equities · horizon: months · testable: no - behavioural · confidence: high
  ^MT117-C14-3
- **Nick Baltas** A momentum crash can be endogenous: when funding liquidity and credit lines are exhausted at maximum gross exposure, forced selling begins.  #mech/liquidity_flows
  > something very endogenous like no funding liquidity is not there anymore and credit lines basically say look you've you've you know you you've grossed out your portfolio as much as you could
  indicator: gross exposure and funding liquidity · asset: equities · horizon: weeks · testable: yes - gross exposure data · confidence: medium
  ^MT117-C14-4
- **Nick Baltas** Baltas notes that momentum itself is anchored in cognitive biases and so is a behavioural pattern, which links the late-stage fear of missing out and redemption fear to the persistence and eventual crash of crowded momentum trades.  #mech/new _(added by map cross-check)_
  > momentum in itself is anchored to cognitive biases so it's it's also a behavioral pattern itself
  indicator: momentum factor · asset: equities · horizon: n/a · testable: no · confidence: high
  ^MT117-C14-R1

### C15
- **Nick Baltas** Volatility-scaling equity momentum exposure cuts participation when its volatility rises, a prudent way to stay in the trade while reducing crash risk.  #mech/risk_management
  > by Vol scaling your exposure into Equity momentum you kind of reduce your participation when its own volatility increases
  indicator: equity momentum factor with volatility scaling · asset: equities · direction: reduce exposure when momentum volatility rises · horizon: weeks · conditions: crowded momentum · testable: yes - vol-scaled momentum backtest · confidence: medium
  ^MT117-C15-1
- **Nick Baltas** Within a momentum crash, losing stocks far below their recent highs rebound most, so avoiding them on the short side or hedging them reduces crash losses.  #mech/overshoot
  > those losing stocks that are far away from the recent Highs are the ones that typically rebound more than the rest
  indicator: distance from recent high among losers · asset: equities · direction: avoid shorting far-from-high losers · horizon: months · conditions: momentum crash rebounds · testable: yes - double sort on 52-week-high distance · confidence: medium
  ^MT117-C15-2
- **Nick Baltas** Momentum unwinds are liquidity events: crowded exits cause fire sales and short squeezes, and gross exposure data may hint at a turning point, though calling it is very hard.  #mech/liquidity_flows
  > it's ultimately a liquidity discussion at theend the day right how quickly can we get out
  indicator: hedge fund gross exposure and momentum positioning · asset: equities · horizon: weeks · testable: partly - positioning data observable, timing unreliable · confidence: low
  ^MT117-C15-3
- **Neils Kostrup Larsen** Trend followers with dynamic position sizing scale out when a market goes volatile, which naturally reduces exposure to crowded blow-off moves.  #mech/risk_management
  > if you have dynamic position sizing once the thing gets crazy we're going to be scaling out and leave the party
  indicator: volatility-scaled trend positions · asset: multi · horizon: weeks · testable: yes - position vs vol · confidence: medium
  ^MT117-C15-4
- **Neils Kostrup Larsen** Cocoa positions were already reduced before the reversal because the volatility spike weakened the vol-normalised signal even as price kept rising.  #mech/risk_management _(time-bound view)_
  > cocoa exposure has been dialed down before the downturn came just because the spike up was
  indicator: volatility-normalised trend signal in cocoa · asset: commodities · horizon: weeks · conditions: high-vol spikes in rising market · testable: yes - signal/vol normalisation · confidence: medium
  **Correction (cross-check):** wrong speaker: the cocoa point (exposure dialed down before the reversal because the high-vol spike weakened the signal) is made by Nick Baltas responding to Larsen, who then agrees → Nick Baltas: cocoa exposure was already reduced before the reversal because the volatility spike weakened the vol-normalised signal even as price kept rising.
  ^MT117-C15-5
- **Nick Baltas** A momentum unwind can also be exogenous, from an idiosyncratic shock such as the AI story fading, or from value investors buying cheap and shorting expensive stocks; this is even harder to foresee than an endogenous funding squeeze.  #mech/crowding_positioning _(added by opus cross-check)_
  > another reason can be very exogeneous you can have basically talk about I don't know like a a neighbor calling the police which is maybe relevant to having a very idiosyncratic shock in the market
  indicator: equity momentum factor · asset: equities · direction: momentum factor down · horizon: weeks · conditions: crowded momentum, idiosyncratic shock or value rotation · testable: partly - study momentum crash triggers historically · confidence: low
  ^MT117-C15-X1

