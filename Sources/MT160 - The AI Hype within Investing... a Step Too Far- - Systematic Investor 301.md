---
source_id: MT160
title: "The AI Hype within Investing... a Step Too Far- - Systematic Investor 301"
date: 2024-06-25
channel: "Top Traders Unplugged"
url: 
words: 12855
claims: 62
added_by_crosscheck: 28
corrections: 1
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Rob Carver (systematic trader, author)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# The AI Hype within Investing... a Step Too Far- - Systematic Investor 301

**Speakers:** Rob Carver (systematic trader, author); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Systematic Investor 301: Rob Carver and Niels Kaastrup-Larsen on trend following vs tail hedging, VIX carry across the roll, why a systematic trader makes no election adjustments, and why LLMs in trading invite overfitting. Also fees and vol-adjusted fee comparison.

**Approach:** trend following, tail hedging, volatility carry, systematic research method

**Cross-check completeness estimate of first read:** 0.72 - the first reader caught the main arguments (tail hedging, trend vs puts, VIX carry at roll, elections, LLM overfitting, fees) but missed supporting data (index returns, positioning), the fee hurdle and two-tier points, UK fiscal comments and several caveats from Niels.

## Argument map

**Episode thesis:** Rob Carver argues that tail protection and trend following do different jobs: puts are persistently overpriced insurance that only pays for leveraged investors (it lets them lever up safely and raise geometric return), whereas trend following is a positive-expected-return, low-correlation allocation for unleveraged investors and must not be used as an excuse to add leverage. He also argues that a systematic trader should make no event-driven adjustments for elections, because profit needs three hard predictions (outcome, implications, market reaction), and that off-the-shelf LLMs applied to financial data are an overfitting machine whose in-sample gains and out-of-sample losses cannot be seen. Niels adds that trend following is better described as a non-correlated return than as crisis alpha, and that AI in models raises transparency and liability problems; the two split mildly on competing on low fees, and agree that fees should be judged net and volatility-adjusted.

### Rob Carver (Systematic futures trader and author (Advanced Futures Trading Strategies), part-time lecturer, former options trader and AHL researcher; co-host of the Systematic Investor series)
Fingerprint: #approach/trend_following #approach/carry #approach/volatility_options #approach/position_sizing_vol_target #approach/research_robustness_overfitting #approach/short_term_systematic #approach/crisis_alpha_convexity #approach/costs_execution
_Speaker note: Captions do not label speakers; attribution follows content (first-person trading book and teaching experience = Carver, relayed listener questions and index numbers = Niels). Correction applied to MT160-C02-2: the chips-commoditization remarks are Carver's; the 'who would have talked about Nvidia 2-3 years ago, shows how unpredictable things are' remark is Niels's (added as MT160-C02-R1)._

**Worldview premises**
- Trend-following returns have a weak mean-reversion effect: after a modest drawdown is a better time to add allocation than at a high watermark, but judgement timing is too hard, so timing is left to the model. _[empirical, stated; support: Own experience: he added allocation near a high, and the return fell from about +16% YTD in late April to about +7.8% by late June.]_ ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C02-1|C02-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C02-X1|C02-X1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C03-X1|C03-X1]])
- Buying options is a long-run losing strategy because of the variance (insurance) premium, and downside puts are overpriced even more than other options because everyone wants crash protection and nobody hedges a 20% up day; wide bid-offer spreads on far out-of-the-money options add to the cost. Selling vol is dangerous too, around event risk. _[empirical, stated; support: Experience as a junior options trader (a colleague bled theta and was sacked; Carver himself was short vol into payrolls); no data cited.]_ ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C05-1|C05-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C06-1|C06-1]])
- Equities (especially single stocks) and strategies such as emerging-market FX carry are negatively skewed: sharp losses are possible, with no matching upside tail. _[empirical, stated; support: 1987: a 25% down day in the S&P 500 but never a 25% up day.]_ ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C05-3|C05-3]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C05-X2|C05-X2]])
- Geometric (compound) return is the ultimate performance measure, so an asset that lowers raw return but raises Sharpe can raise geometric return once leverage is allowed. _[theoretical, stated; support: Portfolio-optimisation logic; he writes about it often.]_ ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C05-2|C05-2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C05-X1|C05-X1]])
- Whether tail protection is worth buying depends on leverage: an unleveraged long-horizon investor has no margin-call risk, so protection only reduces return. _[theoretical, stated; support: Reasoning from the endowment case; no data.]_ ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C06-2|C06-2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C08-X1|C08-X1]])
- Trend following is a positive-expected-return strategy with low correlation to traditional markets, so a 10-30% slice improves both Sharpe and geometric return of a long-only portfolio without leverage; it is not guaranteed protection in a crisis. _[empirical, stated; support: Historic data referred to (numbers 'we talked about before'), no figures given in this episode.]_ ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C07-3|C07-3]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C07-4|C07-4]])
- Costs are known with precision and returns are known only with high uncertainty, so with no other information the cheaper manager wins; allocators say they are tough on fees but pay high fees to managers with great net records (Renaissance). _[behavioural, stated; support: Own experience on both sides of the allocator relationship plus Ted Seides's blog post.]_ ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C17-1|C17-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C17-X1|C17-X1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C17-X2|C17-X2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C18-X1|C18-X1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C18-X3|C18-X3]])
- Political risk reaches prices through the equity risk premium (drastic change raises required returns) and, because equity is a call option on enterprise value, volatility is not always bad; a foregone election with similar platforms creates little uncertainty. _[theoretical, stated; support: Economics training; examples are the UK 2024 and US 2024 elections.]_ ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C11-1|C11-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C11-X2|C11-X2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C11-X3|C11-X3]])
- Fiscal credibility shocks hit markets hard (Truss), while the UK debate wrongly treats deficit spending as bad; a counter-cyclical stance since 2010 would have left the UK better off. _[theoretical, stated; support: Political and economic opinion; the Truss episode as illustration.]_ ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C10-X1|C10-X1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C11-X1|C11-X1]])
- Off-the-shelf LLMs are an overfitting trap for financial data: the user cannot see the fitting process, parameter uncertainty or in-sample/out-of-sample split, although non-linear patterns may exist (Renaissance, using specialist AI hires). _[empirical, stated; support: His own pattern-fitting experiment (NDA-covered, not published) and a student assignment where an LLM answer got zero.]_ ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C15-1|C15-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C15-2|C15-2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C14-2|C14-2]])
- Chip businesses (memory first, then CPUs and phone chips) have become commoditized with thin margins, so Nvidia's position as the most valuable company is an unusual outcome and its stock is highly rated. _[empirical, stated; support: General industry knowledge; no numbers.]_ ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C02-2|C02-2]])

**Chain: Why a negative-return, negatively correlated hedge can raise geometric return (leveraged investors)**
1. Leveraged long position in a negatively skewed asset (S&P at 4x) → Risk of a gap drawdown too fast to de-risk, losing all capital: Negative tail (1987), leverage amplifies, vol-targeting cannot act inside a day ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C05-3|C05-3]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C05-X3|C05-X3]])
2. Buy far out-of-the-money puts → Hard floor on the loss, but the puts lose money persistently: Downside vol is overpriced; wide spreads on far-OTM options ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C06-1|C06-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C05-1|C05-1]])
3. Protected book has a higher Sharpe ratio even though raw return is lower → Investor can apply more leverage: The negatively correlated asset cuts portfolio variance more than it cuts return ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C05-2|C05-2]])
4. More leverage on the Sharpe-improved book → Higher geometric return than the unhedged unlevered position: Geometric return is the ultimate measure ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C05-X1|C05-X1]])
- Evidence: Theoretical argument and a thought example; no backtest. Spitznagel's version is relayed by the listener question, not tested here.
- Fails when: Protection costs far more than about 2% a year (30% is 'a different story'), the manager buys puts only selectively so the hedge is missing when needed, or the investor is unleveraged and long-horizon.

**Chain: Trend following versus tail protection: different jobs for different investors**
1. Add 10-30% trend following to a long-only unlevered portfolio → Higher Sharpe and higher geometric return without extra leverage: Positive expected return and low correlation to markets ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C07-3|C07-3]])
2. Add a big trend slice to an already levered risk-parity portfolio → Measured risk falls, so the investor levers up further: Lower measured volatility invites more leverage ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C07-4|C07-4]])
3. A crisis in which trend also loses (the wrong kind of crisis) → All assets fall together under large leverage: Trend gives no guaranteed protection, unlike a put ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C07-4|C07-4]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C08-1|C08-1]])
4. Match tool to investor → Leveraged investors buy tail protection; unleveraged investors buy trend: Put payoff is guaranteed in a crash; trend's value is positive expected return ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C08-X1|C08-X1]])
- Evidence: Reasoning from historic portfolio-blend results (not shown) and the McCauley-type 'first responder / second responder' framing relayed by Niels.
- Fails when: Trend is used as an excuse to lever up; the crisis is fast or has no trend (trend may miss the initial phase).

**Chain: VIX carry across the roll and why it is a low-priority detail**
1. VIX futures curve in contango (spot 13.4, then 15, 16.5, nearly 19 in October) → A short-VIX carry signal (futures expected to roll down): Expected volatility is on average higher than realised volatility ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C08-2|C08-2]])
2. US election on 5 November → November/December futures price below October, so the curve has a kink: Event risk is concentrated in October ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C09-1|C09-1]])
3. Roll from October to November contract → Contract-level carry flips from negative (short) to modestly positive: Slope changes after the roll ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C09-1|C09-1]])
4. Trend and momentum computed on one back-adjusted continuous series → No forecast jump at roll: Per-contract calculation changes the view for no real reason ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C09-2|C09-2]])
5. EMA-smoothed carry → The carry signal drifts rather than jumping, so the roll effect is immaterial: Smoothing absorbs the change; seasonal markets like crude and gas are the exception ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C10-1|C10-1]])
- Evidence: Live look at the VIX curve on the day; his own system design; no test of the alternative.
- Fails when: Strong seasonality (crude, gas) makes the carry at different contracts differ materially.

**Chain: Why a systematic trader makes no election adjustments**
1. Election, referendum or payrolls approaches → Temptation to override the system: The more it plays on the mind, the harder it is not to act ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C12-X2|C12-X2]])
2. To profit one must predict the outcome → Easy in the UK or Russia (foregone), very hard in the US (knife-edge): A foregone conclusion earns no P&L ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C11-X2|C11-X2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C11-2|C11-2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C13-1|C13-1]])
3. Then predict the implications → Relatively easy (manifestos, bank research): Plenty of published analysis ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C12-1|C12-1]])
4. Then predict the market reaction → The hardest step, and not linked to whether the outcome is 'good': Brexit moved euro-dollar unexpectedly ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C13-1|C13-1]])
5. Needing to beat everyone on all three → Correct system adjustment is nil; express any political view via a betting site: Keeps the view separate from the systematic book ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C12-1|C12-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C13-X1|C13-X1]])
- Evidence: Experience around Brexit; his own small bets on UK and US elections.
- Fails when: Not stated.

**Chain: Why LLMs in trading invite overfitting**
1. Wide access to LLMs by users who do not understand them → They are used as consumers to find predictive patterns in financial data: They look like magic and produce plausible output ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C14-2|C14-2]])
2. No visible fitting process, parameter uncertainty or in/out-of-sample split → Overfitting without the user knowing: Unlike transparent fitting there is no diagnostic ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C15-1|C15-1]])
3. Pattern-fitting experiment: pattern length 1 to 10 periods (up to 1,024 patterns) → In-sample curve becomes a straight line while out-of-sample gets worse: More patterns means more fitted noise; one-lag trend following stays stable in and out of sample ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C15-3|C15-3]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C15-R1|C15-R1]])
4. Genuine non-linear structure may exist → Only specialist, rigorous AI efforts (Renaissance) plausibly capture it: Hard-to-detect patterns need special techniques, not generic tools ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C15-2|C15-2]])
- Evidence: His own experiment (NDA-covered, cannot be shown), plus a student assignment and observations that AI pivots have not rewarded shareholders.
- Fails when: Specialist teams with rigorous statistical control (implied Renaissance).

**Decision process**
- [sizing] Volatility-targeted trend book; when trends weaken or reverse, forecasts and positions shrink, so risk automatically runs at just under 10% annualised, about half the long-term target.. Why: Positions follow the signals; no discretionary override. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C03-1|C03-1]])
- [portfolio] Mid-2024 book: long equity indices (MIB, AEX, Nikkei, Nasdaq, S&P), long yen and euro, long cattle, short bonds and short VIX; cocoa closed by the trend reversal.. Why: It is whatever the signals say; a short VIX is carry, and it acts as a pro-risk-on position. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C03-X2|C03-X2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C03-2|C03-2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C03-3|C03-3]])
- [signal] Carry from the futures curve: a steep VIX contango gives a short VIX signal (roll-down).. Why: Implied volatility exceeds realised volatility on average. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C08-2|C08-2]])
- [signal] Trend and momentum on one back-adjusted continuous price series, not on individual contracts; carry forecast EMA-smoothed.. Why: Avoids forecast changes at roll; the individual-contract refinement adds complexity for almost no difference to positions. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C09-2|C09-2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C10-1|C10-1]])
- [risk] No adjustment for elections, referendums or payrolls; if he thinks he can call an election, he bets on a betting site instead.. Why: Profit requires out-predicting everyone on outcome, implications and market reaction. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C12-1|C12-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C13-1|C13-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C13-X1|C13-X1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C12-X2|C12-X2]])
- [risk] Hold a 10-30% allocation to trend in a long-only portfolio; do not lever up because trend reduced measured risk; buy tail protection only if leveraged and at a cost of about 2% a year, not 30%.. Why: Leverage plus an unprotected crisis is the failure mode. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C07-3|C07-3]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C07-4|C07-4]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C07-1|C07-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C08-X1|C08-X1]])
- [research] Test pattern models with an explicit in-sample/out-of-sample split and increasing complexity to see overfitting; avoid black-box LLM fitting.. Why: Overfit models look perfect in sample and lose out of sample. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C15-1|C15-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C15-3|C15-3]])
- [research] Leave allocation timing to the model rather than judging a high watermark or a drawdown.. Why: His own timing error shows judgement timing is hard. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C03-X1|C03-X1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C02-1|C02-1]])
- [other] Compare managers' fees after adjusting for volatility target (2-and-20 at 25% vol is about 1-and-10 at half the vol), and judge on net return.. Why: CTAs with high vol targets look cheap against low-vol long/short funds. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C18-1|C18-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C17-1|C17-1]])

**Evidence style:** Mixes first-principles portfolio theory (Sharpe, leverage, geometric return), personal trading anecdotes (options desk, Brexit, own allocation timing) and one small self-run experiment he cannot show; no published backtests or tables cited in the episode.

**Views at the time**
- (late June 2024 (upload 2024-06-25)) Own book is net long equities and pro-risk-on with risk at about half target; short VIX, long yen/euro, short bonds.. Reasoning: Signals after a weak spring for trend; short VIX also from curve carry. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C03-1|C03-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C03-X2|C03-X2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C03-2|C03-2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C08-2|C08-2]])
- (late June 2024) VIX is elevated for October because of the knife-edge US election; markets price a Trump win as the riskier outcome.. Reasoning: Futures kink at November and the VIX chart show where fear sits. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C09-1|C09-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C11-2|C11-2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C12-X1|C12-X1]])
- (late June 2024) UK election is trading-wise boring: Labour win expected, little policy difference for markets.. Reasoning: Both parties compete for fiscal prudence after the Truss episode. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C11-X2|C11-X2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C11-X1|C11-X1]])
- (late June 2024) AI hype is fading outside Nvidia; non-Nvidia AI pivots have underperformed.. Reasoning: Share prices of AI pivots and growing scepticism on his Twitter feed. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C14-1|C14-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C14-X1|C14-X1]])
- (late June 2024) Nvidia's rise to the world's most valuable company is surprising in a commoditized chip industry, and the stock is highly rated.. Reasoning: Commoditization of memory, CPU and phone chips. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C02-2|C02-2]])
- (late June 2024) Trend allocation: his own trend exposure was +16% YTD at the April high and about +7.8% by late June after he added at the high.. Reasoning: Weak mean reversion in trend returns; added at a high watermark and regretted it. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C02-X1|C02-X1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C02-1|C02-1]])
- (late June 2024) Fee structure heads to two tiers: new funds charge less than established managers with track records.. Reasoning: Costs known, returns unknown; raising fees later is awkward with seed investors. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C18-X1|C18-X1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C17-1|C17-1]])

### Niels Kaastrup-Larsen (Host of Top Traders Unplugged; veteran CTA/hedge fund manager)
Fingerprint: #approach/trend_following #approach/crisis_alpha_convexity #approach/diversification_risk_parity #approach/manager_selection_allocation #approach/costs_execution #approach/regime_detection
_Speaker note: Host questions are context; Niels's own positions are mapped where he states a view (trend is not 'crisis alpha', fees, AI liability, policy continuity). Index numbers and listener questions are read out by him._

**Worldview premises**
- Trend following should be described as a non-correlated return strategy, not crisis alpha, because every crisis is different and trend's response cannot be known in advance; blending a non-correlated positive-return strategy with equities and bonds is theoretically good. _[experience, stated; support: Long industry experience; no data.]_ ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C08-1|C08-1]])
- Option strategies are first responders in a sudden crisis and trend following the second responder in a prolonged one; trend may miss the early phase. _[theoretical, stated; support: A paper (recalled as McCauley's) discussed earlier on the show.]_ ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C07-2|C07-2]])
- A 50% drawdown happens less than once a decade, so paying 2% a year for protection compounds into a large drag. _[empirical, stated; support: Rough frequency, no data.]_ ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C07-X1|C07-X1]])
- AI inside trading models needs supervision and transparency; liability is unresolved; trend rules are valuable because the output is known. _[institutional, stated; support: Reasoning; Tesla analogy raised in conversation.]_ ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C16-1|C16-1]])
- Fees: CTA fees have already fallen to reasonable levels over 35 years; chasing the lowest fee is not the right thing because strategies cost money to run and net returns matter. _[experience, stated; support: 35 years in the CTA industry.]_ ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C18-X2|C18-X2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C13-X3|C13-X3]])
- Election rhetoric overstates the policy change: many Trump-era policies were maintained under Biden. _[empirical, stated; support: Observation, no detail.]_ ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C13-X2|C13-X2]])

**Chain: Why puts and trend complement each other in a crisis**
1. Sudden equity crash → Puts pay first: Convex payoff on a gap move ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C07-2|C07-2]])
2. Prolonged bear market → Trend following catches up and profits: Trends build over time; the initial phase is random ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C07-2|C07-2]])
3. Every crisis differs → Trend should be sold as a non-correlated return, not as crisis alpha: No guarantee of how it reacts ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C08-1|C08-1]])
- Evidence: Relayed academic framing, plus a listener question; no data.
- Fails when: A crisis where trend is positioned the wrong way (agrees with Carver's caution).

**Decision process**
- [research] Track a trend barometer (25, near the weakest level normally seen) and CTA/trend indices (BTOP50, SG CTA, Trend Index, Short Term Traders) against equity indices as a monthly check.. Why: Shows how trend followers are doing against equities. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C04-1|C04-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C04-X1|C04-X1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C03-X3|C03-X3]])
- [other] Judge fees on net returns, not on the lowest headline fee.. Why: Strategies cost money to run. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C18-X2|C18-X2]])

**Evidence style:** Experience-driven and index-reporting; relays academic papers and listener questions rather than testing claims.

**Views at the time**
- (late June 2024 (about 10 days left in the month)) June 2024 was a difficult month for trend followers after a strong Q1: fixed income whipsawed by inflation data and rate-cut hopes, metals hard, equities up strongly; trend barometer 25, indices down 2 to 4% in June but still positive YTD against MSCI +11.6% and S&P +15.5%.. Reasoning: Trend indices lagged a strong equity rally; Europe's equities lagged the US after European elections. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C04-1|C04-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C04-X1|C04-X1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C03-X3|C03-X3]])
- (late June 2024) Nvidia's rise shows how unpredictable leadership is.. Reasoning: Nobody talked about it that way 2 to 3 years ago. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C02-R1|C02-R1]])

### Disagreements
- **Competing on low fees versus charging for track record**: Rob Carver: Between two new managers with no track record the cheaper wins, so a two-tier market forms; new funds charge less; fees should be compared after vol adjustment, on which CTAs look cheap. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C17-1|C17-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C18-X1|C18-X1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C18-1|C18-1]]); Niels Kaastrup-Larsen: He is not in the camp that wins attention with super-low fees; fees have already come down to reasonable levels and net return is what matters. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C18-X2|C18-X2]])
- **How much policy change an election produces**: Rob Carver: Markets (VIX) price a Trump win as a more dangerous outcome because nobody expects technocrats to restrain him. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C12-X1|C12-X1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C11-2|C11-2]]); Niels Kaastrup-Larsen: Many policies were kept under Biden, so you never know what you get from an election. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C13-X2|C13-X2]])
- **How to frame trend following against tail protection (a difference of emphasis)**: Rob Carver: Trend and puts should not share a 'protection' bucket; trend suits unleveraged investors, puts suit leveraged ones, and trend must not justify more leverage. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C08-X1|C08-X1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C07-4|C07-4]]); Niels Kaastrup-Larsen: Puts respond first in a crisis and trend later; trend is a non-correlated return and not crisis alpha; the cost of annual protection builds up over a decade. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C07-2|C07-2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C08-1|C08-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C07-X1|C07-X1]])

### Gaps and conflicts
- The transcript says the far out-of-the-money put 'is going to be cheap because it's extremely likely it will happen', which reads as a caption or speech slip (it should be unlikely); the argument that follows is about overpricing. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C06-1|C06-1]])
- The headline claim that trend adds Sharpe and geometric return at 10-30% is stated from earlier discussion with no numbers or sample in this episode. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C07-3|C07-3]])
- The 2%-versus-30% cost threshold for tail protection is an illustration, not computed; there is no estimate of actual put-programme cost or payoff. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C07-1|C07-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C07-X1|C07-X1]])
- The pattern-fitting experiment is under NDA and no figures are given; the result is credible but unverifiable here. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C15-3|C15-3]])
- The AI pivot underperformance is anecdotal (no names or returns), and the 'Twitter feed' scepticism is weak evidence. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C14-1|C14-1]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C14-X1|C14-X1]])
- The Spitznagel claim and the monetisation rule are relayed by a listener, and Carver says he is in the bottom percentile of people who know tail hedging; his answer is theoretical and experience-based. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C04-2|C04-2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C04-X2|C04-X2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C05-1|C05-1]])
- Carver says UK 'pro-cyclical' fiscal stance would have been better while arguing for deficit spending, which is counter-cyclical; the wording looks like a slip. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C10-X1|C10-X1]])
- Speaker attribution on the Nvidia unpredictability remark was mixed in the first-read claim; fixed by correction and a new claim. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C02-2|C02-2]], [[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C02-R1|C02-R1]])
- Equity as 'a call option on enterprise value' so that volatility could be good is mentioned briefly and not developed into a trading implication. ([[MT160 - The AI Hype within Investing... a Step Too Far- - Systematic Investor 301#^MT160-C11-1|C11-1]])

### Forward-looking inputs (reader synthesis)
(reader) Carver's forward-looking inputs are the system's own forecasts (trend, carry) and, for event risk, the VIX futures term structure, where the election kink in November/December futures shows how much fear is priced into October. He names no leading indicators for returns: he says explicitly not to trade elections, and he reads AI-pivot stock performance and social-media scepticism only as sentiment evidence. Niels's inputs are the trend barometer and CTA indices (weak but near the bottom of their normal range) and rate-cut expectations driving fixed income. Horizons are short (months for the roll and election) to years (the fee and AI themes).

### Reader inferences (not stated by the speakers)
- (reader) The leverage rule is the central design idea: the same position can be sensible or dangerous depending on leverage, so a robust portfolio rule should ask whether the investor is leveraged before choosing between convexity (puts) and positive-carry diversifiers (trend).
- (reader) The pattern-fitting experiment is a general overfitting yardstick: any strategy family whose number of candidate rules grows exponentially should be judged on out-of-sample decline, not in-sample fit.
- (reader) Carver's refusal to adjust for events is consistent with a vol-targeted system where the volatility estimate already responds to event moves after they happen; the VIX term structure is the only place the event is priced into a signal (through carry).
- (reader) His mean-reversion remark on trend returns (add after a drawdown) implies a possible allocator-level overlay, but he says it is too hard to time and he did it wrong; it is not a rule he applies.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | sponsor intro and football banter |
| C02 | 2 | Nvidia commoditized chips; trend allocation timing and weak mean reversion |
| C03 | 3 | portfolio P&L, positioning and risk at half target |
| C04 | 2 | trend barometer, CTA index numbers, put-buying listener question |
| C05 | 3 | options trading experience; theory of negatively correlated hedge |
| C06 | 3 | overpriced downside vol; leveraged vs unleveraged tail hedging |
| C07 | 4 | tail hedge cost; trend vs puts; leverage danger |
| C08 | 2 | tail protection vs trend use cases; crisis alpha; roll carry question |
| C09 | 2 | VIX curve carry and election kink; back-adjusted series |
| C10 | 1 | roll carry immaterial; UK election politics |
| C11 | 2 | political risk through equity risk premium; US election |
| C12 | 1 | no system adjustments; three steps of political trading |
| C13 | 1 | market reaction difficulty, Brexit; AI hype intro |
| C14 | 2 | AI hype skepticism and LLM limits |
| C15 | 3 | Renaissance, LLM overfitting, pattern experiment |
| C16 | 1 | overfitting result, AI liability, fees intro |
| C17 | 1 | allocators and incentive fees; costs known returns unknown |
| C18 | 1 | two-tier fee system; vol-adjusted fees |
| C19 | 0 | nothing actionable: wrap-up and sponsor read |

## Claims

### C02
- **Rob Carver** Trend-following returns show weak mean reversion, so adding allocation after a modest drawdown is better timing than adding at a high watermark.  #mech/cycle_persistence
  > There is a sort of weak mean reversion effects in trend-following returns.
  indicator: trend-following strategy equity curve · asset: multi · direction: add trend allocation after a modest drawdown · horizon: months · conditions: weak effect only; market timing is hard · testable: partly - test allocation timing on trend index returns · confidence: medium
  ^MT160-C02-1
- **Rob Carver** Chip businesses (memory, CPUs, smartphone chips) have become commoditized with thin margins, so Nvidia's position is unusual and its highly rated stock reflects unpredictable shifts in leadership.  #mech/structural_shift
  > the thing about chips is is is one of those businesses that that has gradually got more commoditized over time.
  asset: equities · horizon: years · testable: no - qualitative · confidence: low
  **Correction (cross-check):** Mixes two speakers and overstates the margin point: Carver said memory chips are microscopic-margin, while CPU margins are 'better' but still commoditized; the remark on unpredictability of who would be talked about (Nvidia 2-3 years ago) is Niels's, not Carver's. → Carver: memory chips are heavily commoditized with microscopic margins, CPUs and smartphone chips are less so but also commoditized; Nvidia is the surprise. Niels adds that Nvidia's rise shows how unpredictable leadership is.
  ^MT160-C02-2
- **Rob Carver** Carver's own trend allocation went from +16% year-to-date at the late-April high to about +7.8% by late June right after he added allocation at the high, in line with trend indices: an anecdote of buying a trend fund at its high watermark.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > in in late April, I actually reached a high watermark of about um which would have So, the year-to-date figure would have been 16%
  indicator: trend-following P&L YTD · asset: multi · horizon: months · conditions: Single anecdote, in line with CTA indices. · testable: partly - fits the weak mean-reversion claim only anecdotally · confidence: high
  ^MT160-C02-X1
- **Niels Kaastrup-Larsen** Niels says Nvidia's rise to the world's most valuable company shows how unpredictable market leadership is: hardly anyone talked about it that way two or three years earlier.  #mech/new _(added by map cross-check, time-bound view)_
  > who would have who would have talked about Nvidia in this way at least uh 2 or 3 years ago.
  asset: equities · horizon: years · testable: no - anecdote · confidence: medium
  ^MT160-C02-R1

### C03
- **Rob Carver** After trends reversed or weakened, a volatility-targeted trend system automatically runs at about half its long-term risk target because forecasts and positions shrink.  #mech/risk_management _(time-bound view)_
  > Um my risk is running at just under 10% annualized standard deviations. That's about just under half of my kind of long-term target.
  indicator: portfolio volatility vs target · asset: multi · direction: lower exposure after trend weakness · horizon: months · conditions: after drawdown with weak trends · testable: yes - compare realized risk to target · confidence: high
  ^MT160-C03-1
- **Rob Carver** A short VIX position is effectively risk-on (long equities) because VIX falls when investors think equities are getting less risky, so the book is net long equity beta.  #mech/risk_premium _(time-bound view)_
  > my biggest short position actually is VIX. So, that's very much a pro risk-on um position
  indicator: VIX futures position · asset: other · direction: short VIX with long equity indices · horizon: weeks · conditions: when equity trends are up · testable: yes - correlation of positions with equities · confidence: medium
  ^MT160-C03-2
- **Rob Carver** Mid-2024 P&L: FX (yen, euro, Swiss franc), Asian equities (Taiwan, Nikkei) and cocoa were profitable while energies (gas) and metals (gold, platinum) lost money.  #mech/slow_reaction _(time-bound view)_
  > the markets that have done well have been uh interest in the effects, particularly yen
  indicator: sector P&L of a trend portfolio · asset: multi · direction: long FX and Asian equities; losses in energy and metals · horizon: months · testable: yes - sector P&L data · confidence: high
  ^MT160-C03-3
- **Rob Carver** Even a systematic trader who made an allocation timing mistake concludes that timing is too hard to do by judgement and should be left to the model.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > market timing is very difficult, as we as we always say, which is why we leave it to to our models to do that.
  asset: multi · testable: no - methodological stance · confidence: high
  ^MT160-C03-X1
- **Rob Carver** Carver's mid-2024 positioning: long equity indices (MIB, AEX, Nikkei, Nasdaq, S&P), yen and euro, cattle, short bonds and short VIX; cocoa was closed by the trend reversal. This is a positive-beta, pro-equity book with the roll (carry) position pointing the same way.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > I'm long MIB, which is the Italian stock index.
  indicator: positions by market · asset: multi · direction: long equities, FX, cattle; short bonds, VIX · horizon: months · conditions: Derived from trend and carry signals at the time. · testable: no - description of current positions · confidence: high
  ^MT160-C03-X2
- **Niels Kaastrup-Larsen** After a very strong Q1, trend followers had a difficult spring: fixed income was whipsawed by inflation data and hopes of rate cuts (Europe cutting, the Fed holding out), and metals were hard; Europe's equities lagged the US after the European elections.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > I think fixed income has probably been one of the more challenging sectors so far as far as I can tell.
  indicator: fixed income trend P&L; inflation data; Fed path · asset: rates · horizon: months · testable: partly - sector P&L by month is observable · confidence: medium
  ^MT160-C03-X3

### C04
- **Niels Kaastrup-Larsen** A trend barometer at 25 is close to the weakest level normally seen, in line with trend-follower performance in June 2024 (BTOP50 -2.79%, SG CTA -3%, Trend Index -3.57%) while equities rose.  #mech/cycle_persistence _(time-bound view)_
  > My own trend barometer is super weak. So in line with performance numbers it's 25
  indicator: trend barometer · asset: multi · horizon: months · conditions: after strong Q1, difficult Q2 for trend followers; fixed income and metals challenging · testable: yes - index data · confidence: medium
  ^MT160-C04-1
- **Niels Kaastrup-Larsen** Spitznagel's claim: a 2% allocation to far out-of-the-money puts and 98% to the S&P can beat the S&P on geometric return despite a negative expected return on the puts.  #mech/risk_premium
  > a portfolio with a 2% allocation to insurance and a 98% allocation to S&P 500 can theoretically achieve a higher geometric return
  indicator: systematic deep OTM put buying plus monetization · asset: equities · direction: long OTM puts, long S&P · horizon: years · conditions: requires a monetization rule when a crash occurs · testable: yes - backtest the put overlay · confidence: medium
  ^MT160-C04-2
- **Niels Kaastrup-Larsen** In June 2024 the CTA and trend indices were down 2 to 4% (SG CTA about -3%, Trend Index -3.57%, Short Term Traders -1.93%) while year-to-date they were +0.8% to +7.7% against MSCI +11.6% and S&P 500 +15.5%, so trend followers lagged a strong equity rally.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > Beta 50 down 2.79 for the month of June, up 6.41 uh, for the year.
  indicator: BTOP50, SG CTA, Trend Index, Short Term Traders Index, MSCI, S&P 500 YTD · asset: multi · direction: trend lags equities in a narrow rally · horizon: months · testable: yes - public index data · confidence: high
  ^MT160-C04-X1
- **Niels Kaastrup-Larsen** The Spitznagel result requires two pieces: a permanent systematic programme of far out-of-the-money puts (the crash date is unknowable) and an explicit rule to monetise the puts when volatility spikes (listener question relayed by Niels).  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > it would appear to be dependent upon a systematic program of buying far out of the money put options because you don't know in advance when the fast equity crash will occur, and then a monetization strategy
  indicator: far-OTM put programme; monetisation rule · asset: equities · horizon: years · conditions: Without the monetisation rule the payoff is not captured. · testable: yes - backtestable on option data · confidence: medium
  ^MT160-C04-X2

### C05
- **Rob Carver** Buying options is a long-run losing strategy because of the variance (insurance) premium, while selling volatility is dangerous in different ways around events.  #mech/risk_premium
  > buying optionality is is in the long run a long losing strategy because we because of the variance premium because of the insurance premium if you like.
  indicator: variance premium · asset: other · direction: short volatility earns premium; long optionality loses · horizon: years · testable: yes - implied vs realised volatility · confidence: high
  ^MT160-C05-1
- **Rob Carver** Adding a negative-return asset that is negatively correlated with the portfolio raises the Sharpe ratio, which allows more leverage and hence a higher geometric return.  #mech/risk_management
  > it's actually possible to improve the expected um either sharp ratio geometric return both can be improved by adding an asset to your portfolio that has a negative return but is negatively cause a negatively correlated
  indicator: portfolio Sharpe and geometric return · asset: multi · direction: add hedge then lever up · conditions: hedge must be strongly negatively correlated · testable: yes - portfolio optimisation test · confidence: high
  ^MT160-C05-2
- **Rob Carver** Equities are negatively skewed in the tails (1987 -25% day, no +25% day), so strategies with negative skew justify tail protection when leveraged.  #mech/risk_premium
  > there was once a 25% down day in the S&P 500 in 1987. There has never been a 25% up day.
  indicator: S&P 500 return skew · asset: equities · testable: yes - tail distribution · confidence: high
  ^MT160-C05-3
- **Rob Carver** Geometric (compound) return is the right ultimate performance measure, which is why a Sharpe-improving but return-reducing asset can still help once leverage is allowed.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > geometric return is is all the the kind of ultimate I write about it a lot but it's the ultimate performance measure it's what everything comes back to essentially.
  indicator: geometric return · asset: multi · testable: yes - standard result · confidence: high
  ^MT160-C05-X1
- **Rob Carver** Negatively skewed strategies include FX carry (especially emerging-market carry) and long stock holdings, particularly individual stocks, which are prone to sudden sharp losses.  #mech/risk_premium _(added by sonnet-xhigh cross-check)_
  > typical negatively skewed trading strategy. And then that could be something like FX carry, an extreme emerging market FX carry, but it could also just be buying stocks
  indicator: FX carry; single stocks · asset: multi · direction: carry and long-equity returns have sharp left tails · testable: yes - skewness measurable · confidence: high
  ^MT160-C05-X2
- **Rob Carver** For a leveraged book the danger is a gap drawdown too fast to de-risk, which vol-targeting cannot prevent and only an option or similar hard floor does; this is the case for tail protection.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > the drawdown being so fast that I can't de-risk my portfolio, and I'll basically lose all my money.
  asset: equities · horizon: days · conditions: Needs high leverage, e.g. 4x S&P. · testable: partly - gap risk is measurable · confidence: high
  ^MT160-C05-X3

### C06
- **Rob Carver** Out-of-the-money downside puts are systematically overpriced because investors hedge crashes, not rallies, and bid-offer spreads on far-OTM options are wide, so put buying persistently loses money.  #mech/risk_premium
  > people overprice volatility, but they overprice downside volatility even more
  indicator: OTM put implied vol skew · asset: other · direction: short downside vol earns premium · horizon: years · testable: yes - skew versus realized · confidence: high
  ^MT160-C06-1
- **Rob Carver** Unleveraged long-horizon investors (e.g. endowments) face no margin-call risk, so tail protection only reduces their return; it makes sense only for leveraged investors.  #mech/risk_management
  > I'm a bit skeptical as to why you need to buy tail protection, to be honest, because you're you're only going to see the costs and not the benefits
  asset: multi · direction: avoid tail hedge when unleveraged · horizon: years · conditions: investor has long horizon and no leverage · testable: partly - compare returns with and without hedge · confidence: high
  ^MT160-C06-2
- **Rob Carver** A tail-risk fund that buys puts only selectively (when cheap) may leave the investor unprotected at the moment of need, so claims of free insurance are suspect.  #mech/risk_management
  > any tail-risk manager that tells you they're going to give you their insurance policy for free, I'd be a bit skeptical.
  asset: other · testable: partly - fund track records in crisis · confidence: medium
  ^MT160-C06-3

### C07
- **Rob Carver** Paying about 2% per year for tail protection can be reasonable for a leveraged book because protection allows higher leverage; at 30% cost it does not.  #mech/risk_management
  > if it's going to cost you 2% of your portfolio to defend yourself against a you know, a 50% drawdown, that seems to me to me quite reasonable
  indicator: cost of tail hedge · asset: multi · direction: modest tail hedge for leveraged portfolios · horizon: years · conditions: hedge cost small relative to leverage gain · testable: yes - cost-benefit calculation · confidence: medium
  ^MT160-C07-1
- **Niels Kaastrup-Larsen** Option strategies respond to a sudden crisis first while trend following helps in prolonged drawdowns but may not help in the initial phase.  #mech/cycle_persistence
  > option strategies as kind of first responders in a crisis and then trend following was like the second responder
  indicator: options vs trend following crisis response · asset: multi · direction: long puts early; trend later · horizon: months · conditions: trend works in prolonged bear markets, random in fast crashes · testable: yes - compare strategy returns in crisis phases · confidence: medium
  ^MT160-C07-2
- **Rob Carver** Adding 10-30% trend following to a long-only portfolio raises Sharpe and geometric return without extra leverage because it has positive expected return and low correlation to markets.  #mech/risk_premium
  > If you add um trend following to a uh long only portfolio, you can improve your geometric return
  indicator: trend following allocation share in a traditional portfolio · asset: multi · direction: long trend following diversifier · horizon: years · conditions: uncorrelated; no extra leverage · testable: yes - blend backtest · confidence: high
  ^MT160-C07-3
- **Rob Carver** Adding trend following to a levered risk-parity portfolio lowers measured risk, tempting investors to lever up; in a crisis where trend also loses, all assets fall together with large leverage.  #mech/risk_management
  > you add a big slug of trend following say 30%. Um it's quite plausible that your your risk is going to fall
  indicator: portfolio leverage after trend allocation · asset: multi · conditions: when trend does the wrong thing in a crisis · testable: partly - scenario analysis · confidence: high
  ^MT160-C07-4
- **Niels Kaastrup-Larsen** A 50% drawdown happens less than once per decade, so paying 2% a year for protection accumulates to a large drag over ten years and the benefit must be compared with that.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > if you're paying 2% every year for 10 years, you know, it becomes meaningful.
  indicator: annual cost of tail protection · asset: equities · horizon: years · testable: yes - cost-benefit backtest · confidence: medium
  ^MT160-C07-X1

### C08
- **Niels Kaastrup-Larsen** Trend following should be seen as a non-correlated return strategy rather than crisis alpha because each crisis differs and trend response is not guaranteed.  #mech/cycle_persistence
  > it's dangerous to describe trend following as a crisis alpha strategy because no crisis is the same
  asset: multi · testable: partly - crisis-by-crisis trend performance · confidence: high
  ^MT160-C08-1
- **Rob Carver** VIX futures curve in contango (spot 13.4, then 15, 16.5, just under 19 in October) predicts roll-down, which is the carry signal behind a short-VIX position and reflects the gap between expected and realised vol.  #mech/risk_premium _(time-bound view)_
  > the spot VIX is about 13.4.
  indicator: VIX futures term structure carry · asset: other · direction: short VIX futures · horizon: months · conditions: curve upward sloping · testable: yes - carry backtest · confidence: high
  ^MT160-C08-2
- **Rob Carver** Match the tool to the investor: leveraged investors should buy tail protection (guaranteed payoff in a crash), unleveraged investors should buy trend following (positive expected return); trend must not be used to justify extra leverage.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > Leveraged investors should buy tail protection but should be wary of buying trend following if they're going to then use that as an excuse to apply even more leverage.
  asset: multi · testable: partly - argument, not test · confidence: high
  ^MT160-C08-X1

### C09
- **Rob Carver** VIX futures for November and December price below October because of the US election on 5 November, so event risk shows up as a kink in the term structure that changes carry signals when rolling.  #mech/policy_reaction _(time-bound view)_
  > November expiry and actually the December expiry as well, they're actually lower than October.
  indicator: VIX futures curve around US election · asset: other · horizon: weeks · conditions: around event dates · testable: yes - futures prices · confidence: high
  ^MT160-C09-1
- **Rob Carver** Computing trend and momentum on a single back-adjusted continuous price series avoids a forecast change at roll, whereas per-contract calculation changes positions at roll for no real reason.  #mech/research_method
  > I think it's more common to do what I do, which is form a single back adjusted price series of continuous contract
  indicator: back-adjusted continuous contract series · asset: multi · testable: yes - compare signal turnover · confidence: high
  ^MT160-C09-2

### C10
- **Rob Carver** Using carry of the held contract at roll versus a smoothed continuous series is an immaterial approximation; the EMA smoothing of carry absorbs the change, though seasonal markets like crude and gas are more affected.  #mech/research_method
  > Do I really care? Um, implementing what Lewis suggested would make my system a lot more complex
  indicator: roll carry smoothed with EMA · asset: commodities · conditions: stronger seasonality in crude and natural gas · testable: yes - test roll-carry handling · confidence: high
  ^MT160-C10-1
- **Rob Carver** Carver believes UK policy dialogue ignores that government deficit spending can be beneficial, and that a more counter-cyclical (he says pro-cyclical) fiscal stance since 2010 would have left the UK better off.  #mech/fiscal_debt _(added by sonnet-xhigh cross-check)_
  > the fact that that often governments spending more than they earn can be a good thing for example.
  indicator: UK fiscal stance · asset: multi · horizon: years · conditions: Opinion, no evidence given. · testable: no - opinion · confidence: medium
  ^MT160-C10-X1

### C11
- **Rob Carver** Political risk affects markets through the equity risk premium (drastic change raises required returns), and equity is a call option on enterprise value so volatility can even help.  #mech/risk_premium
  > there are essentially um two things that that that kind of can affect markets in terms of political risk. One is the effect it has on, you know, what we would call the the equity risk premium
  indicator: equity risk premium around elections · asset: equities · horizon: weeks · conditions: if change is drastic · testable: partly - event studies · confidence: medium
  ^MT160-C11-1
- **Rob Carver** The 2024 US election was finely balanced, and markets (VIX in October) priced a Trump win as the riskier outcome.  #mech/policy_reaction _(time-bound view)_
  > this thing's on a knife edge, it could go either way.
  indicator: VIX around the US election · asset: equities · direction: VIX higher into election · horizon: months · testable: partly - VIX term structure · confidence: medium
  ^MT160-C11-2
- **Rob Carver** Liz Truss's badly communicated economic plan nearly broke the UK financial system overnight, which is why both UK parties compete to look fiscally prudent: fiscal credibility shocks hit markets hard.  #mech/fiscal_debt _(added by sonnet-xhigh cross-check, time-bound view)_
  > nearly caused the entire UK financial system to disintegrate overnight, which is quite impressive.
  indicator: UK gilt market · asset: rates · direction: gilt yields up, sterling down on fiscal credibility loss · horizon: days · testable: partly - event study · confidence: high
  ^MT160-C11-X1
- **Rob Carver** A foregone election with near-identical platforms (UK 2024) creates little market uncertainty, unlike a close election with very different candidates.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > generally think that the Labour Party and the Conservative There's not going to be that much difference as far as the markets are concerned, at least initially.
  indicator: UK election; implied volatility · asset: equities · horizon: weeks · conditions: Holds when policy convergence is credible. · testable: partly - election event studies · confidence: medium
  ^MT160-C11-X2
- **Rob Carver** In the US system the popular vote does not decide the winner (2016), so even a lead in national polls leaves the presidency near 50/50.  #mech/research_method _(added by sonnet-xhigh cross-check, time-bound view)_
  > the US has a sort of system where you can lose the popular vote or do very badly in the popular vote and still become president
  indicator: polls; Electoral College · asset: equities · horizon: weeks · testable: partly - historical polls vs outcomes · confidence: high
  ^MT160-C11-X3

### C12
- **Rob Carver** A systematic trader should make no system adjustment for elections, referendums or payrolls, because trading political macro requires predicting the outcome, its implications and the market reaction better than everyone else.  #mech/risk_management
  > and the correct answer is nil. Nothing. Nothing.
  asset: multi · testable: partly - compare rule-based vs discretionary overrides · confidence: high
  ^MT160-C12-1
- **Rob Carver** In 2016 markets assumed Trump would be moderated by technocrats; by 2024 nobody believes it, so a Trump win is priced as a higher policy-risk outcome and the October VIX is bid up.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > I think everyone believes that that that, you know, if if the the crazy guy does get in, he's going to do crazy things.
  indicator: VIX October futures · asset: equities · direction: VIX up around the election · horizon: months · conditions: Rob's reading of consensus, not a measured quantity. · testable: partly - VIX term structure observable · confidence: medium
  ^MT160-C12-X1
- **Rob Carver** Staying engaged with political news is a behavioural trap: the more it plays on the mind, the harder it is to resist overriding the system, so the rule is to hold the position of 'do nothing'.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > it's all very well to be interested in this and read the news, but it doesn't mean I should actually do anything
  asset: multi · testable: no - discipline rule · confidence: high
  ^MT160-C12-X2

### C13
- **Rob Carver** Political event trading needs three steps (outcome, implications, market reaction), and the last is hardest because reactions are unpredictable (Brexit moved euro-dollar unexpectedly) and consensus outcomes are already priced.  #mech/behavioral
  > it's no good predicting a foregone conclusion. No one's going to give you any any kind of P&L for that.
  indicator: market reaction to political results · asset: fx · horizon: days · testable: no - qualitative · confidence: high
  ^MT160-C13-1
- **Rob Carver** If you believe you can forecast an election, express that on a betting site rather than by overriding the trading system, keeping the view separate from the systematic book.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > I think if you if you are you do think you can predict political outcomes, then, um, there are websites certainly in the UK where you can bet directly on the political outcome.
  asset: multi · horizon: weeks · conditions: Legality varies by country. · testable: no - practical suggestion · confidence: medium
  ^MT160-C13-X1
- **Niels Kaastrup-Larsen** Niels's caveat to Rob: many Trump-era policies were kept under Biden, so campaign rhetoric overstates the policy change an election produces.  #mech/policy_reaction _(added by sonnet-xhigh cross-check)_
  > actually, for the record, a lot of policies have been maintained actually under Biden, so, uh, you know, you never know what you get, uh, with these elections
  asset: multi · horizon: years · testable: partly - continuity of policy can be measured · confidence: medium
  ^MT160-C13-X2
- **Niels Kaastrup-Larsen** A BCG report puts global asset-management assets at $120 trillion in 2023 yet the industry faces fee compression, rising costs and passive competition.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > They talked about how it reached $120 trillion in 2023.
  indicator: global AUM · asset: multi · direction: fees down · horizon: years · testable: yes - public data · confidence: medium
  ^MT160-C13-X3

### C14
- **Rob Carver** Companies that pivoted to AI (other than Nvidia) have not done well, suggesting AI hype is not translating into returns.  #mech/behavioral _(time-bound view)_
  > if we look at the the share prices of of not of Nvidia, but if you look at other companies that have done a very strong pivot to AI, um they're not doing so well
  indicator: share prices of AI-pivot companies · asset: equities · horizon: months · testable: partly - basket of AI-pivot companies · confidence: low
  ^MT160-C14-1
- **Rob Carver** General large language models give meaningless platitudes on real data analysis tasks, so they are poor tools for evaluating strategy returns.  #mech/research_method
  > this assignment, which for what it's worth, involves analyzing some some returns data from a strategy and comparing it to a couple of benchmarks, is is kind of AI-proof.
  asset: other · testable: partly · confidence: medium
  ^MT160-C14-2
- **Rob Carver** Carver reads rising AI scepticism on social media, alongside weak share prices of non-Nvidia AI pivots, as a sign that the hype is fading.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > I am starting to see a bit of kind of, um, you know, skepticism creeping to my Twitter feed about AI
  indicator: social-media sentiment on AI · asset: equities · horizon: months · conditions: Anecdotal sentiment reading. · testable: partly - sentiment indices exist · confidence: low
  ^MT160-C14-X1

### C15
- **Rob Carver** Using off-the-shelf LLMs to find predictive patterns in financial data carries high overfitting risk and gives no statistical uncertainty or in-sample/out-of-sample discipline, unlike transparent fitting.  #mech/research_method
  > it's very unlikely that that you'll you'll get that kind of rigor using the LLM.
  indicator: LLM-derived signals · asset: multi · conditions: user does not understand the technology · testable: partly - test out-of-sample · confidence: high
  ^MT160-C15-1
- **Rob Carver** Non-linear patterns in financial data may exist that classical statistics miss (Renaissance hires AI specialists), but that is very different from applying generic LLM tools.  #mech/structural_shift
  > Renaissance Technologies. The I mean, you know, nobody knows what they do, but it's probably that cuz they aren't doing what
  indicator: non-linear pattern detection · asset: multi · conditions: requires deep expertise · testable: no - proprietary · confidence: low
  ^MT160-C15-2
- **Rob Carver** In an experiment fitting up/down sequence patterns, as pattern length rises from 1 to 10 periods (up to 1,024 patterns) in-sample returns improve until the equity curve is a straight line while out-of-sample performance deteriorates; simple one-lag trend following stays similar in and out of sample.  #mech/research_method
  > Get up to 10, and you're you've got
  indicator: pattern-length complexity vs in/out-of-sample performance · asset: multi · conditions: number of patterns grows exponentially · testable: yes - replicable experiment · confidence: high
  ^MT160-C15-3
- **Rob Carver** Carver says a one-lag up/down trend model performs similarly in and out of sample and does reasonably well, and that simple trend models tend to do well; complexity is what breaks out-of-sample performance.  #mech/new _(added by map cross-check)_
  > it's a simple trend following model, and as we both know, Neils, simple trend following models tend to do pretty well.
  indicator: in-sample versus out-of-sample performance · asset: multi · conditions: simple models with few parameters · testable: yes - his own experiment · confidence: medium
  ^MT160-C15-R1

### C16
- **Niels Kaastrup-Larsen** AI used in trading models without supervision and transparency raises liability and explainability issues, unlike transparent trend rules where the output is known.  #mech/risk_management
  > what about the liability? What about the liability of a firm using AI in its models
  asset: multi · testable: no - governance point · confidence: medium
  ^MT160-C16-1

### C17
- **Rob Carver** Since costs are known and returns are not, between two new managers choose the cheaper one, while established managers with great net returns (Renaissance) keep high fees.  #mech/research_method
  > I always say that costs are known and returns are unknown.
  indicator: manager fees · asset: multi · direction: prefer lower-fee new managers · horizon: years · conditions: absent other information on performance · testable: partly - fees vs net return · confidence: high
  ^MT160-C17-1
- **Rob Carver** Many managers charge incentive fees without a hurdle, i.e. on total return including cash interest instead of only excess over the risk-free rate, which matters most when rates are high.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > a lot of the people you're allocating to are still charging quite, you know, hefty incentive fees and incentive fees that don't have a hurdle, right?
  indicator: incentive fee hurdle vs risk-free rate · asset: multi · conditions: Material when short rates are high (50bp vs 500bp). · testable: yes - fee arithmetic · confidence: high
  ^MT160-C17-X1
- **Rob Carver** Ted Seides's point: allocators say they push hard on fees but keep investing in high-fee managers, so there is no real negotiation; investors really care about net performance (Renaissance), not the fee level.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > you guys are talking a big game, but actually when you look at who you're investing in
  asset: multi · testable: partly - allocator behaviour can be studied · confidence: medium
  ^MT160-C17-X2

### C18
- **Rob Carver** Compare fees after adjusting for volatility target: 2-and-20 on a 25% vol CTA equals 1-and-10 on half the vol, so CTAs look cheap relative to low-vol long/short funds.  #mech/research_method
  > you should always look at fees adjusting for volatility
  indicator: fee per unit of volatility · asset: multi · conditions: comparing high-vol CTAs with low-vol equity funds · testable: yes - calculation · confidence: high
  ^MT160-C18-1
- **Rob Carver** Fee structure becomes two-tier: new funds charge less, established funds with track records keep high fees, and raising fees later is awkward for seed investors.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > we were kind of going to end up with is a two-tier system where anyone, um, who's starting a who's starting a fund in the last few years is is going to have much lower fees
  asset: multi · horizon: years · testable: no - industry observation · confidence: medium
  ^MT160-C18-X1
- **Niels Kaastrup-Larsen** Niels disagrees with competing on the lowest fees: CTA fees have already fallen over 35 years to reasonable levels, strategies cost money to run, and net returns are what matter.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > I'm not in that camp. I don't believe that uh, to be uh, the right thing to do for our industry
  indicator: CTA fee levels · asset: multi · horizon: years · testable: no - opinion · confidence: high
  ^MT160-C18-X2
- **Rob Carver** Legacy fund fees were very high because they were launched in the early 1990s when interest rates were higher and trail fees to advisers were part of the model; the fee margin has come down since.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > fees on some of the legacy funds we had were just you know, eye-popping
  indicator: fee levels · asset: multi · direction: fees down · horizon: years · testable: no - historical anecdote · confidence: high
  ^MT160-C18-X3

