---
source_id: MT079
title: "If Trend Following was an Olympic Sport - Systematic Investor 306"
date: 2024-08-01
channel: "Top Traders Unplugged"
url: 
words: 11358
claims: 60
added_by_crosscheck: 9
corrections: 0
crosscheck: "opus cross-check"
speakers: ["Mark rinsky (guest, Systematic Investor co-host, rules-based investor)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# If Trend Following was an Olympic Sport - Systematic Investor 306

**Speakers:** Mark rinsky (guest, Systematic Investor co-host, rules-based investor); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Weekly trend-following chat (July 2024): Treasury bill issuance as offset to QT, trend giveback and calm-regime risk, market add/drop rules, how to read backtests and build systems, stock-bond correlation, GIC/JPM paper placing trend following as loss mitigation, caution on LLM/ML, and law of small numbers.

**Approach:** trend following, CTA portfolio construction, backtesting, macro liquidity

**Cross-check completeness estimate of first read:** 0.89 - main ideas all caught; missed QT/coupon net-supply detail, short-term index numbers and some market-selection nuances (add criterion, vol-removal rule, commodity boards).

## Argument map

**Episode thesis:** Mark (captioned 'Mark rinsky') argues that systematic trend following should be run and judged as a full system (signals, diversified portfolio construction, risk management), where market selection, realistic backtests and humility about models matter more than clever new techniques, and that when valuation and macro arguments cut both ways one should follow price trends. He adds a macro thread (heavy Treasury bill issuance acting as de facto QE that offsets Fed tightening) and cites the GIC/JPMorgan hedge-fund framework as an unintended case for trend following as loss mitigation. The host reports a three-month giveback for trend followers in July 2024 and agrees that drawdowns are entry points, that markets should not be dropped for past losses (cocoa) and that volatility floors guard against suppressed volatility.

### Mark rinsky (caption spelling; Systematic Investor co-host) (Rules-based investor / trend-following practitioner and manager evaluator, co-host of the Systematic Investor series)
Fingerprint: #approach/trend_following #approach/research_robustness_overfitting #approach/diversification_risk_parity #approach/liquidity_flows #approach/policy_reaction_central_banks #approach/manager_selection_allocation #approach/behavioral_sentiment
_Speaker note: Name is as captioned in the transcript and ledger. Listener questions (Philip) are read by Niels and are not Mark's views. The ledger's speaker label is used for Mark throughout; no speaker confusion found between the two voices._

**Worldview premises**
- Heavy Treasury bill issuance relative to coupons acts as de facto quantitative easing: bills are near-money and usable as collateral, fewer coupons make risky long-duration supply scarcer and lower long-term rates, offsetting the Fed's tightening. _[institutional, stated; support: Cites a Hudson Bay Capital paper on activist Treasury issuance and describes the size of the issuance difference as 'staggering'; no figures given on air.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C02-1|C02-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C02-2|C02-2]])
- The 2016 money market fund rules raised structural demand for short-term instruments, giving Treasury room to issue more bills; Treasury's rule of thumb is about 15% bills, but actual issuance has been much higher. _[institutional, stated; support: Regulatory history and Treasury practice recalled from memory.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C02-3|C02-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C03-1|C03-1]])
- Net duration supply (Fed QT runoff plus coupon issuance) is what matters; Fed balance-sheet runoff adds coupon supply each month and a Treasury cut in coupon issuance offsets it. _[theoretical, stated; support: Supply-and-demand reasoning along the yield curve.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C03-X1|C03-X1]])
- The cost of crisis alpha and low correlation is poor performance in calm, sideways markets with lower rate and inflation volatility, and investors forget the crisis benefit when they rebalance on recent results. _[behavioural, stated; support: Practitioner experience with investor behaviour.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C04-1|C04-1]])
- Past losses are not a reason to drop a market: it may be a diversifier whose future is unknown, and one-sided-market assumptions fail (short-term interest rates went below zero after he had judged them one-sided). _[experience, stated; support: Personal anecdotes: an argument with a large trend follower about a five-year losing market; his own wrong forecast on the zero bound.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C05-1|C05-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C05-2|C05-2]])
- Markets with central-bank intervention (managed FX) that punish speculators justify lower exposure; the best markets are two-sided with hedgers and speculators, with retail participation, because markets of only professional traders are harder to make money in. _[experience, stated; support: Market-review criteria used at his earlier firm; no data.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C05-3|C05-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C05-4|C05-4]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-1|C06-1]])
- Illiquidity brings jump risk, so a market falling below minimum volume or open interest should be dropped, and brand-new markets avoided; screening should go into adding markets carefully because removal is hard to decide well. _[experience, stated; support: Market-review practice.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-2|C06-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-X1|C06-X1]])
- A market review should look at how a market earned or lost money (one trade or many, choppiness), not just whether it made money. _[experience, stated; support: Practice description.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-3|C06-3]])
- Commodity markets whose prices governments can manage (like cocoa) look like poor trend markets, yet can still produce explosive trends after a supply dislocation; an index excluding cocoa (Credit Suisse managed futures) underperformed CTAs that held it; few markets are dropped except for liquidity. _[empirical, stated; support: Index comparison from memory; no figures.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C07-1|C07-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C07-X1|C07-X1]])
- Volatility targeting raises size when volatility is artificially low (Swiss franc peg), which was the worst action when the peg broke. _[empirical, stated; support: Swiss franc peg episode.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C07-2|C07-2]])
- Backtests are valuable not for performance or Sharpe ('I've never seen a bad backtest') but for what they reveal about the manager's care in research, assumptions and treatment of transaction costs; investors' Sharpe thresholds conflict, so the research process matters more than the numbers. _[experience, stated; support: His paper 'I've never seen a bad backtest'; anecdote of two Manhattan investors with opposite Sharpe thresholds (reject below 2 versus reject above 1.25).]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C07-3|C07-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C08-1|C08-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C08-4|C08-4]])
- Anyone can build a good model; what matters is applying it across many markets, building portfolios and a full system, and moving from the backtest (laboratory) to a factory with realistic inputs, outputs, timing, costs and execution. _[experience, stated; support: Scientist versus engineer analogy.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C08-2|C08-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C08-3|C08-3]])
- A systematic manager should be evaluated on return generation, portfolio construction and risk management; regression or model-based signals risk parameter instability so simple rules are preferred; diversification is the one free lunch. _[theoretical, stated; support: Manager evaluation experience; Markowitz-style free lunch idea.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C09-1|C09-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C09-2|C09-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C09-3|C09-3]])
- Risk management belongs inside the model's entry and exit rules, with a stop loss as a fail-safe protecting investor principal. _[experience, stated; support: Mike Tyson 'punched in the nose' quote.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C09-4|C09-4]])
- When stock-bond correlation turns positive, 60/40 volatility rises and bonds lose their diversification role, so risk must be monitored via the off-diagonal correlation terms and the stock-versus-bond choice becomes one of relative valuation. _[theoretical, stated; support: Covariance-matrix reasoning.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C10-2|C10-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C11-1|C11-1]])
- In the GIC/JPMorgan framework trend following meets all three criteria (low equity correlation, drawdown mitigation, positive alpha after beta); managed futures ranked second for alpha after beta behind global macro; trend following is not an equity substitute. _[empirical, stated; support: His reading of the GIC/JPM paper; he stresses the paper was not written as a case for trend following.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C11-2|C11-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C11-3|C11-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C12-1|C12-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C12-2|C12-2]])
- Being wedded to one macro model produces false alarms (post-GFC QE did not cause rampant inflation) and doomsday forecasts are often wrong (Covid fell sharply but recovered faster than expected); prices should be the null hypothesis, and one should not chase data releases such as PCE because the price reaction to them is what drives positions. _[experience, stated; support: Book 'Stocks, Crisis and False Alarms' (as relayed), QE and Covid examples.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C13-1|C13-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C13-2|C13-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C13-3|C13-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C14-1|C14-1]])
- Large language models add little to time-series forecasting, and machine learning does well in expansions but poorly in recessions because training data have few recessions, so model building is harder than expected. _[empirical, stated; support: Two papers he cites from his blog; no details given.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C14-2|C14-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C14-3|C14-3]])
- Prices are public and discounted almost immediately, so models and new techniques are valuable only if they turn the same public data into private insight others do not have; new techniques should be adopted gradually, not as an on/off switch. _[theoretical, stated; support: Information-theory and efficient-markets reasoning.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C15-2|C15-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C15-3|C15-3]])
- The law of small numbers (gambler's fallacy and hot hand) affects trend and quant models that decide on limited data; knowing the distribution implies mean reversion, not knowing it implies following the hot hand. _[behavioural, stated; support: Behavioural finance literature (basketball and coin examples).]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C16-1|C16-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C16-2|C16-2]])

**Chain: Treasury bill issuance offsets Fed quantitative tightening**
1. Fed QT adds coupon (duration) supply each month → tighter financial conditions: more duration for the market to absorb ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C03-X1|C03-X1]])
2. Treasury issues more bills and fewer coupons than its 15% rule of thumb → scarcer coupons (prices up, long rates down) and more near-money: bills are collateral-eligible, near-money; coupons are risky long-duration assets with limited demand ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C02-1|C02-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C02-2|C02-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C03-1|C03-1]])
3. structural demand for short instruments after the 2016 money market fund rules → Treasury can issue bills without strain: regulation shifted demand to short instruments ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C02-3|C02-3]])
4. offsetting Treasury policy → strong US growth, slow disinflation and easy financial conditions despite Fed tightening: it answers 'why is the US economy doing so well' and 'why did disinflation take so long' ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C02-1|C02-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C03-X1|C03-X1]])
- Evidence: Hudson Bay Capital paper as relayed; no numbers on air; he says he wants to explore it further.
- Fails when: Not stated; the argument is presented as a plausible explanation, not tested.

**Chain: Calm markets make crisis alpha look bad and investors abandon it**
1. falling rate and inflation volatility; sideways markets → trend following performs poorly: low correlation to risk assets means it lags when everything calm is up ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C04-1|C04-1]])
2. recent poor results next to strong alternatives → investors forget the benefit in selloffs and rebalance away: rebalancing decisions weigh the last three months or the year to date ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C04-1|C04-1]])
- Evidence: Practitioner experience; the host adds the 2010s analogy (decade to 2019 when central banks controlled everything).
- Fails when: Not stated; the host adds that drawdowns are entry points because few investors hold trend.

**Chain: Stocks versus bonds: when both look compelling, rising correlation and the case for following prices**
1. stocks look overvalued while the rate outlook (cuts, slower growth, lower inflation) also supports bonds → compelling reasons exist for both stocks and bonds: valuation says sell stocks, rates say hold both ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C10-1|C10-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C10-R1|C10-R1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C10-R2|C10-R2]])
2. both assets driven by the same rate story → they can become correlated and portfolio risk rises: 60/40 volatility depends on the off-diagonal covariance terms ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C10-2|C10-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C10-3|C10-3]])
3. positive stock-bond correlation → bonds no longer diversify, and the choice becomes relative valuation: bonds were held at lower return because they diversified ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C10-2|C10-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C11-1|C11-1]])
4. valuation question unanswerable → follow price trends and let the market disclose what to do: trend following does not need to resolve the competing narratives ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C10-1|C10-1]])
- Evidence: Blog-post reasoning; the host notes the one-year rolling stock-bond correlation is at a multi-year high.
- Fails when: Not stated.

**Chain: Volatility targeting into artificially low volatility**
1. volatility artificially suppressed (Swiss franc peg, short rates at zero) → volatility-targeted size rises: lower volatility means more size per unit of risk budget ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C07-2|C07-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-4|C06-4]])
2. peg break or volatility spike → oversized positions lose heavily: worst possible exposure at the worst time ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C07-2|C07-2]])
3. safeguard: volatility floors and multiple lookbacks → size capped despite low measured volatility: experienced managers do not trust a year or two of low volatility ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-4|C06-4]])
- Evidence: Swiss franc 2015 and short-rate episodes; the safeguard is stated as the host's practice.
- Fails when: Not stated.

**Chain: Machine learning and new techniques: why public data and few recessions limit value**
1. prices and macro data are public → discounted into prices almost immediately: efficient markets ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C15-2|C15-2]])
2. a model must turn public data into private insight → new techniques help only if they give an insight others lack: everyone starts from the same data (cocoa prices example) ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C15-2|C15-2]])
3. ML trained mostly on expansions → poor performance in recessions: training data include few recession periods ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C14-3|C14-3]])
4. gradual adoption → avoid binary switch from old to new models: model building is harder than expected and LLMs add little to time series ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C15-3|C15-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C14-2|C14-2]])
- Evidence: Two cited papers; information-theory framing.
- Fails when: Not stated.

**Decision process**
- [universe] Add markets carefully, favouring two-sided markets with hedgers, some retail participation, established history and sufficient volume/open interest; avoid brand-new markets and markets with heavy central-bank intervention (lower exposure).. Why: Removing markets later is hard to decide well; one-sided or purely professional markets are harder to profit in. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C05-4|C05-4]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-1|C06-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-2|C06-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-X1|C06-X1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C05-3|C05-3]])
- [universe] Drop a market when volume or open interest falls below a threshold (jump risk), but not because it lost money for years; when reviewing, check how it earned or lost (one trade or many, choppiness).. Why: A losing market may be a diversifier; the future is unknown; cocoa shows explosive returns can follow years of losses. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C05-1|C05-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-2|C06-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-3|C06-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C07-1|C07-1]])
- [research] Use backtests to probe the manager's assumptions, cost treatment and realism, and move from lab to factory (inputs, outputs, timing, costs, execution), not to judge by Sharpe.. Why: Every backtest looks good; carefulness is what is informative. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C07-3|C07-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C08-1|C08-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C08-3|C08-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C08-4|C08-4]])
- [signal] Prefer simple rules over regression or model-based signals.. Why: Parameter instability risk. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C09-2|C09-2]])
- [portfolio] Build the portfolio for diversification across many markets and treat it as the one free lunch.. Why: Applying a model across many markets and combining them is where the system value lies. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C09-3|C09-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C08-2|C08-2]])
- [risk] Build risk management into entry and exit rules and keep a stop loss as a fail-safe protecting investor principal.. Why: Plans fail when you are 'punched in the nose'. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C09-4|C09-4]])
- [signal] Where stock and bond valuation or macro arguments conflict, follow price trends; use prices as the null hypothesis and depart only if needed.. Why: Macro models give false alarms; the price reaction to data matters, not the data. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C10-1|C10-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C13-3|C13-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C14-1|C14-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C13-1|C13-1]])
- [risk] Monitor stock-bond correlation (off-diagonal covariance terms) in a 60/40 portfolio.. Why: Positive correlation raises portfolio volatility and removes bond diversification. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C10-2|C10-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C11-1|C11-1]])
- [research] Check sample size and distribution to avoid the law of small numbers in trend or quant models.. Why: Decisions are made on limited data; extrapolation and mean reversion are both mis-specified without the distribution. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C16-1|C16-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C16-2|C16-2]])
- [other] Classify strategies by equity correlation, drawdown mitigation versus equities and alpha after beta.. Why: Tells loss mitigation from equity substitutes; trend following meets all three. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C11-2|C11-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C11-3|C11-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C12-2|C12-2]])

**Evidence style:** Practitioner anecdote and manager-evaluation experience, plus citation of papers (Hudson Bay, GIC/JPMorgan, LLM time-series and ML across the cycle papers, a book on macro false alarms); argues from first principles on information and diversification; offers few numbers himself.

**Views at the time**
- (2024-07-26) US growth has been strong and disinflation slow because Treasury bill issuance offsets Fed tightening (a plausible explanation he wants to explore).. Reasoning: Hudson Bay paper relayed; more near-money and fewer coupons. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C02-1|C02-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C03-X1|C03-X1]])
- (2024-07-26) US stocks look overvalued (mega-cap stocks well extended) while the Fed may cut as early as September, so there are compelling arguments for both stocks and bonds and prices should be followed.. Reasoning: Cannot resolve the valuation question; trend following lets the market decide. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C10-R1|C10-R1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C10-R2|C10-R2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C10-1|C10-1]])
- (2024-07-26) Trend following's recent three-month weakness does not mean much on its own ('three months don't make a year'); calm rate and inflation volatility is the cost of crisis alpha.. Reasoning: Low rate and inflation volatility with sideways markets hurts trend; investors forget the crisis benefit. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C04-1|C04-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C04-R1|C04-R1]])
- (2024-07-26) The GIC/JPMorgan framework is one of the best explanations for holding trend following, even though the paper was agnostic.. Reasoning: Trend meets all three criteria (low correlation, drawdown mitigation, alpha). ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C12-2|C12-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C12-1|C12-1]])
- (2024-07-26) LLMs and machine learning deserve caution for systematic modelling.. Reasoning: Two papers: no gain from LLMs in time series; ML poor in recessions. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C14-2|C14-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C14-3|C14-3]])

### Niels Kaastrup-Larsen (Host (Top Traders Unplugged); veteran hedge fund manager and trend-following allocator/commentator)
Fingerprint: #approach/trend_following #approach/position_sizing_vol_target #approach/manager_selection_allocation #approach/regime_detection #approach/market_internals_leading
_Speaker note: Host questions are context. Mapped because he states views on trend-following regimes, market removal and volatility floors. The listener question from Philip (C05-X1, C05-X2) is read by him and is not his view._

**Worldview premises**
- Trend followers gave back performance for three months through July 2024, which strains investor conversations but opens entry points because too few investors hold trend following (and those who do hold too little). _[experience, stated; support: Industry observation; his optimist case.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C03-2|C03-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C03-4|C03-4]])
- If macro calms again (inflation and rates controlled by central banks), trend followers may struggle as in the decade to 2019. _[empirical, stated; support: Historical analogy; he says he is not sure 'we're there yet'.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C03-3|C03-3]])
- July 2024 was a transition period with reversals across currencies (yen strength), equities, metals, energy and bonds; the Trend Barometer at 36 signals a weak environment and a negative month for trend followers. _[empirical, stated; support: His own barometer and sector observations.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C04-2|C04-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C04-3|C04-3]])
- Volatility floors and multiple lookbacks are needed so that suppressed volatility (Swiss franc, short rates) does not lead to oversized positions; large managers look at volatility over several time frames. _[experience, stated; support: Practitioner knowledge of large managers.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-4|C06-4]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C05-X2|C05-X2]])
- Removing markets for past losses is dangerous: cocoa was unprofitable for trend followers for 15 to 20 years before January 2023 and then extremely profitable in 2023 to 2024; a market that makes little money but pays when others lose still adds diversification value. _[empirical, stated; support: Cocoa episode.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-5|C06-5]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-6|C06-6]])
- A trend follower should add a market only if its diversification value exceeds its transaction costs and the opportunity cost of displacing other markets (listener Philip's framing, adopted as a trade-off). _[theoretical, stated; support: Read from a listener's email; the hosts discuss rather than endorse it as their own rule.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C05-X1|C05-X1]])
- The one-year rolling stock-bond correlation is at a multi-year high, exposing portfolios to higher risk than they may think. _[empirical, stated; support: Observed data; no figure given.]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C10-3|C10-3]])
- Every technology wave in 30 years was predicted to hurt trend following and it has not; experience is hard to backtest. _[experience, stated; support: Three decades of industry experience; hedged ('one should never say never').]_ ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C15-1|C15-1]])

**Decision process**
- [sizing] Use volatility floors and multiple volatility lookbacks so that suppressed volatility does not inflate position size.. Why: Swiss franc and short-rate volatility collapses show the danger. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-4|C06-4]])
- [universe] Remove markets mainly for liquidity concerns, not past losses; keep markets that diversify even if they earn little.. Why: Cocoa after 15 to 20 years of losses; value of paying when others lose. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-5|C06-5]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-6|C06-6]])
- [other] Track the Trend Barometer and index returns (BTOP50, SG CTA, SG Trend, short-term traders) to gauge the trend environment.. Why: A barometer of 36 means a weak month for the industry. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C04-3|C04-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C04-4|C04-4]])

**Evidence style:** Industry experience and data reporting (index returns, Trend Barometer); historical anecdotes (cocoa, Swiss franc); he mostly asks questions and relays listener input.

**Views at the time**
- (2024-07-26) Trend followers are in a transition period with a negative July: currencies hit by yen strength, reversals in equities, metals, energy and bonds; BTOP50 -1.48% (+5.47% YTD), SG CTA -2.19% (+4.91% YTD), SG Trend -2.21% (+6.28% YTD), MSCI World ~+10% YTD, S&P 500 ~+14% YTD.. Reasoning: Month-to-date data as of Wednesday night; Trend Barometer 36. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C04-2|C04-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C04-3|C04-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C04-4|C04-4]])
- (2024-07-26) The SG Short-Term Traders index fell 1.17% in July and is slightly negative YTD (-0.12%), lagging trend indices (+5 to 6% YTD).. Reasoning: Data recap. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C04-X1|C04-X1]])
- (2024-07-26) The drawdown creates entry points, but calm macro could bring a struggle like the decade to 2019.. Reasoning: Too few investors hold trend following; inflation concerns are fading and rates are subdued. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C03-2|C03-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C03-3|C03-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C03-4|C03-4]])
- (2024-07-26) The one-year rolling stock-bond correlation is at a multi-year high, so 60/40 holders are exposed to more risk.. Reasoning: Both stocks and bonds rose until recently, which masked the correlation. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C10-3|C10-3]])

### Disagreements
- **Removing markets from a trend portfolio**: Mark rinsky (caption spelling; Systematic Investor co-host): Run regular reviews with explicit drop criteria (falling volume or open interest, loss of two-sidedness, choppiness) but never drop for past losses alone; invest the effort in adding markets carefully. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C05-1|C05-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-2|C06-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-3|C06-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-X1|C06-X1]]); Niels Kaastrup-Larsen: Liquidity is the clear reason to drop; volatility issues are better handled with volatility floors and multiple lookbacks than by removal; the bigger risk is removing markets for losses (cocoa). ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-4|C06-4]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-5|C06-5]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C05-X2|C05-X2]])
- **Cocoa: poor trend market in principle, or underrated diversifier?**: Mark rinsky (caption spelling; Systematic Investor co-host): Government-managed pricing and choppiness give several reasons not to trade cocoa, yet a supply dislocation produced explosive returns, so exclusion would have hurt. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C07-1|C07-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C07-X1|C07-X1]]); Niels Kaastrup-Larsen: Cocoa was unprofitable for 15 to 20 years then extremely profitable; this is the example of why not to remove markets for losses; it made some managers' profits. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-5|C06-5]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-6|C06-6]])

### Gaps and conflicts
- The Hudson Bay bill-issuance argument is relayed from a paper with no numbers, no estimate of the QE-equivalent size, and no test of the claim that it explains US growth and slow disinflation; Mark says he wants to explore it more. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C02-1|C02-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C02-2|C02-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C03-1|C03-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C03-X1|C03-X1]])
- Mark's conclusion that trend following meets all three GIC/JPM criteria rests on the paper's strategy-level 'managed futures' category; he himself notes managed futures is not the same as trend following, yet applies the result to trend following. The paper's authors did not draw this conclusion. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C11-2|C11-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C12-1|C12-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C12-2|C12-2]])
- Mark uses 'prices as the null hypothesis' and 'follow prices' after saying that valuation and macro arguments for stocks and bonds are both compelling; the claim that trend following resolves the conflict is argued, not shown, and ignores the cost of whipsaws he himself describes in calm regimes. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C10-1|C10-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C13-3|C13-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C04-1|C04-1]])
- The market-review criteria (retail share, two-sidedness) are unquantified and some conflict with the 'don't drop for losses' rule; the cocoa case is both a reason to exclude (managed prices) and a poster child for inclusion. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C05-4|C05-4]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C06-1|C06-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C07-1|C07-1]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C07-X1|C07-X1]])
- Claims about papers on LLMs in time series and ML in recessions are second-hand and the first paper's test is described as 'very specific'; the extrapolation to a general caution is Mark's. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C14-2|C14-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C14-3|C14-3]])
- The host says he is not sure trend followers are in a calm-macro regime yet, while also saying inflation concerns have eased and rates are subdued; the PCE number released during recording was higher than expected, which neither speaker connects to the thesis. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C03-3|C03-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C14-1|C14-1]])
- Stock-bond correlation risk is raised by both speakers but no threshold or response rule is given beyond 'follow trends' or 'think about valuation'. ([[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C10-2|C10-2]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C10-3|C10-3]], [[MT079 - If Trend Following was an Olympic Sport - Systematic Investor 306#^MT079-C11-1|C11-1]])

### Forward-looking inputs (reader synthesis)
(reader) Inputs the speakers treat as relevant: the mix of Treasury bill and coupon issuance versus Fed QT runoff (net duration supply) for financial conditions; rate and inflation volatility (calm hurts trend); the one-year rolling stock-bond correlation (portfolio risk and the case for trend); volume and open interest by market (jump risk); and the price reaction to data rather than data themselves. Horizon is not stated precisely: a few months for trend giveback and entry points, and a multi-year regime view for calm versus volatile macro. Neither speaker makes a price forecast.

### Reader inferences (not stated by the speakers)
- (reader) Mark's view of trend following is mainly structural: it earns its place through diversification and crisis behaviour, so the cost is regime-dependent (calm periods) and the right response to drawdowns is to look at the process, not the recent returns.
- (reader) The cocoa case plays two roles: for Mark it shows exclusion risk despite good reasons to dislike the market; for Niels it shows removal for past losses is dangerous. Both lead to 'keep broad coverage, drop for liquidity'.
- (reader) The T-bill argument implies that Fed policy alone understates financial-condition easing; a trend follower reading rates would see the effect in curve moves, not in the policy rate, consistent with 'let prices speak'.
- (reader) The backtest-as-diligence argument shifts the investor's question from 'how good are the numbers' to 'how were they produced', which links to the law-of-small-numbers advice on sample size.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, Olympic analogy; nothing actionable |
| C02 | 3 | Treasury bill issuance offsets Fed (Hudson Bay paper) |
| C03 | 4 | issuance rule of thumb, trend giveback, calm regimes |
| C04 | 4 | cost of crisis alpha, July 2024 trend performance |
| C05 | 4 | when to add/remove markets |
| C06 | 6 | market selection criteria, vol floors, cocoa |
| C07 | 3 | cocoa, vol targeting in pegs, backtest value |
| C08 | 4 | backtest to system/factory, Sharpe anecdote |
| C09 | 4 | three components of a system, simple rules, risk management |
| C10 | 3 | stocks vs bonds, correlation risk |
| C11 | 3 | GIC/JPM hedge fund framework |
| C12 | 2 | trend following fits the framework |
| C13 | 3 | Stocks Crisis and False Alarms; prices as null |
| C14 | 3 | price action vs data; LLM and ML caveats |
| C15 | 3 | tech revolutions, public to private information |
| C16 | 2 | law of small numbers; outro |
| C17 | 0 | outro and sponsor; nothing actionable |

## Claims

### C02
- **Mark rinsky** Heavy Treasury bill issuance relative to coupons acts as de facto QE that offsets Fed tightening, which helps explain strong US growth, slow disinflation and easy financial conditions.  #mech/policy_reaction _(time-bound view)_
  > the activist treasury issuance of more more bills than coupons has had an impact of providing quantitative uh easing that's offset what the FED has been doing
  indicator: bill vs coupon issuance share (Hudson Bay paper) · asset: rates · direction: easier financial conditions, lower long yields · horizon: months · conditions: while Treasury skews issuance to bills · testable: yes: Treasury issuance composition is public · confidence: medium
  ^MT079-C02-1
- **Mark rinsky** Bills are near-money and usable as collateral, so more bills adds money-like assets, while fewer coupons makes risky long-duration supply scarcer and lowers long-term rates.  #mech/liquidity_flows
  > so if you issue more uh bills it's as if you're issuing more money
  indicator: bill share of issuance; coupon supply · asset: rates · direction: long yields down when coupon supply falls · horizon: months · testable: partly: transmission channel hard to isolate · confidence: medium
  ^MT079-C02-2
- **Mark rinsky** The 2016 money market fund rules raised structural demand for short-term instruments, so Treasury has room to issue more bills.  #mech/structural_shift
  > there's a greater demand for treasury bills because of the way we've changed the regulations on U money market funds that came around in 2016
  indicator: money market fund assets · asset: rates · horizon: years · testable: yes · confidence: medium
  ^MT079-C02-3

### C03
- **Mark rinsky** Treasury's rule of thumb is about 15% bills, but actual issuance has been much higher, shifting supply versus demand along the curve.  #mech/policy_reaction _(time-bound view)_
  > we'll do about 15% in bills and the rest in coupons they've done numbers that are much higher on the on the bill side
  indicator: bills as % of issuance · asset: rates · horizon: months · testable: yes · confidence: medium
  ^MT079-C03-1
- **Niels Kaastrup-Larsen** Trend followers gave back performance for three months through July 2024, which strains investor conversations but may open entry points.  #mech/cycle_persistence _(time-bound view)_
  > somewhat Relentless giveback of performance that Trend followers have experienced in the past three months and actually it continued in July
  indicator: CTA performance · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT079-C03-2
- **Niels Kaastrup-Larsen** If macro calms again (inflation and rates controlled), trend followers may struggle as in the decade to 2019.  #mech/policy_reaction _(time-bound view)_
  > might have a bit of a struggle like they had in the uh the 10 years uh leading into 2019 where everything was well controlled by central banks
  indicator: inflation, rate volatility · asset: multi · horizon: years · conditions: calm central-bank-controlled macro · testable: partly: regime comparison is loose · confidence: low
  ^MT079-C03-3
- **Niels Kaastrup-Larsen** Drawdowns in trend following offer entry points because too few investors hold it.  #mech/behavioral _(time-bound view)_
  > it also opens up for some great entry points because still around you know in terms of investors there are still way too few who have exposure to Trend filling
  asset: multi · direction: allocate to trend following after drawdown · horizon: years · testable: partly · confidence: medium
  ^MT079-C03-4
- **Mark rinsky** Fed quantitative tightening adds coupon (duration) supply to the market each month, and Treasury cutting coupon issuance offsets that supply, so net duration supply (QT runoff plus coupon issuance) is what drives long rates and financial conditions.  #mech/liquidity_flows _(added by opus cross-check)_
  > if the treasury doesn't issue coupon bonds then in some sense it's it's actually sort of offsetting the pressures that have been put in from the from the FED
  indicator: Fed QT coupon runoff vs Treasury coupon issuance (net duration supply) · asset: rates · direction: less net coupon supply -> lower long yields, easier conditions · horizon: months · conditions: QT ongoing · testable: yes - net duration supply vs term premium · confidence: medium
  ^MT079-C03-X1

### C04
- **Mark rinsky** The cost of crisis alpha and low correlation is poor performance in calm, sideways markets with lower rate and inflation volatility, and investors forget the crisis benefits when rebalancing.  #mech/risk_premium
  > the cost with that of having low correlation is the fact that when there is calm periods in the market such as when uh where we have interest rates have volatility has come down
  indicator: trend following vs volatility regime · asset: multi · direction: trend following weak in calm markets · horizon: months · conditions: low rate/inflation vol, sideways markets · testable: yes: performance by vol regime testable · confidence: high
  ^MT079-C04-1
- **Niels Kaastrup-Larsen** In July 2024 trend followers suffered reversals across currencies (yen strength), equities, metals, energy and bonds, a transition period.  #mech/cycle_persistence _(time-bound view)_
  > currencies have been uh as far as I can tell has been hit pretty hard not least from the the strength the new found strength of the Japanese uh Yen
  indicator: USDJPY and cross-asset reversals · asset: multi · horizon: weeks · conditions: trend reversals · testable: yes · confidence: medium
  ^MT079-C04-2
- **Niels Kaastrup-Larsen** A Trend barometer of 36 indicates a weak environment and negative month for trend followers.  #mech/cycle_persistence _(time-bound view)_
  > my own Trend barometer closed yesterday at 36 that's weak it's not super weak but it is weak
  indicator: Trend barometer (Niels' own) · asset: multi · horizon: weeks · testable: yes: barometer defined by host · confidence: medium
  ^MT079-C04-3
- **Niels Kaastrup-Larsen** In July 2024 trend indices were down about 1.5-2.2% for the month and up about 5-6% YTD; MSCI World up about 10% YTD and the bond index slightly down.  #mech/cycle_persistence _(time-bound view)_
  > St gen CTA index down 2.19% in July up 4.91% uh for the year
  indicator: BTOP50, SG CTA, SG Trend, SG Short-term Traders; MSCI World; S&P Global Developed Sovereign Bond · asset: multi · horizon: months · testable: yes: public index data · confidence: high
  ^MT079-C04-4
- **Niels Kaastrup-Larsen** In July 2024 the SG Short-Term Traders index fell 1.17% and was slightly negative year to date (-0.12%), lagging the trend indices (+5-6% YTD), while the S&P 500 was up about 14% YTD.  #mech/cycle_persistence _(added by opus cross-check, time-bound view)_
  > the short-term Traders index also a negative territory in July down 1.17% but also down for the year down uh 12 basis points
  indicator: SG Short-Term Traders index, S&P 500 · asset: multi · direction: short-term CTAs lag trend CTAs in 2024 · horizon: months · testable: yes - public index numbers · confidence: high
  ^MT079-C04-X1
- **Mark rinsky** Mark cautions that a three-month stretch of weak trend-following returns is not a year; short-run weakness should not be over-read.  #mech/new _(added by map cross-check, time-bound view)_
  > three months don't make a year
  indicator: trend-following returns over three months · asset: multi · horizon: months · conditions: July 2024 · testable: no · confidence: high
  ^MT079-C04-R1

### C05
- **Mark rinsky** Do not drop a market from a trend portfolio just because it lost money for years: it may be a diversifier whose future is unknown.  #mech/research_method
  > if let's say a a market has been trading poorly over the last few years that doesn't mean it's going to trade poorly going forward
  indicator: market-level past performance · asset: multi · horizon: years · testable: yes: removal rules can be backtested · confidence: high
  ^MT079-C05-1
- **Mark rinsky** Dropping short-term interest rate markets near the zero bound would have been wrong because rates went negative; one-sided-market assumptions fail.  #mech/research_method
  > rates are never going to go below zero so therefore uh and if we're getting close to the zero bound let's of course drop that market
  indicator: short-term interest rate futures near zero bound · asset: rates · horizon: years · testable: yes · confidence: high
  ^MT079-C05-2
- **Mark rinsky** Central-bank-intervention markets (managed FX) that punish speculators justify lower exposure.  #mech/policy_reaction
  > central banks actually intervene because they want to punish speculators
  indicator: managed currencies · asset: fx · direction: reduce exposure · horizon: years · conditions: central bank not profit-maximizing · testable: partly · confidence: medium
  ^MT079-C05-3
- **Mark rinsky** Market selection criteria: two-sided markets with hedgers and speculators; markets with only speculators are a problem.  #mech/research_method
  > you want to have two-sided markets where you have hedgers and both speculators if it's pure speculative then that could be a a problem
  indicator: hedger participation · asset: multi · testable: partly: hedger share via COT data · confidence: medium
  ^MT079-C05-4
- **Philip (listener question, read by Niels Kaastrup-Larsen)** A trend follower should add a market only if its diversification value exceeds its transaction costs and the opportunity cost of displacing other markets, so market selection is a trade-off rather than an obvious choice.  #mech/research_method _(added by opus cross-check)_
  > does it add enough value relative to transaction cost and opportunity cost of not holding uh other assets anymore so usually not an obvious choice only tradeoffs
  indicator: marginal portfolio value vs transaction cost · asset: multi · horizon: years · testable: yes - marginal contribution net of costs · confidence: medium
  ^MT079-C05-X1
- **Philip (listener question, read by Niels Kaastrup-Larsen)** Some trend followers drop a market when its volatility falls too low (e.g. a soft currency peg); the hosts later prefer volatility floors to removal.  #mech/risk_management _(added by opus cross-check)_
  > some will argue that if V is too low then the asset is out
  indicator: market volatility threshold · asset: multi · direction: remove or cap exposure in very low-vol markets · horizon: months · conditions: soft pegs, managed markets · testable: yes - compare removal rule vs volatility floor · confidence: low
  ^MT079-C05-X2

### C06
- **Mark rinsky** Markets with only professional traders (little retail) are harder to make money in.  #mech/crowding_positioning
  > all professional Traders it's going to be harder to make money
  indicator: participant mix · asset: multi · testable: partly · confidence: medium
  ^MT079-C06-1
- **Mark rinsky** Drop markets when volume or open interest fall below minimums, because illiquidity brings jump risk; avoid brand-new markets.  #mech/risk_management
  > the volume starts to fall below a certain threshold or open interest Falls I'd want to drop it out because uh because then then you could get more likely a jump risk which could work against you
  indicator: volume and open interest minimums · asset: multi · testable: yes: thresholds testable · confidence: high
  ^MT079-C06-2
- **Mark rinsky** When reviewing a market, check how it earned (one trade or many, choppiness) rather than whether it made money.  #mech/research_method
  > not so much if it makes money or loses money but how it makes the money and lose the money is it all coming with a single trade
  indicator: trade-level P&L concentration · asset: multi · testable: yes · confidence: medium
  ^MT079-C06-3
- **Niels Kaastrup-Larsen** Use volatility floors and multiple lookbacks so that suppressed volatility (Swiss franc, short rates) does not lead to oversized positions.  #mech/risk_management
  > there you have to have some safeguards some volatility flaws that you know doesn't prevent you is the word I'm looking for here prevents you from sizing up and and getting really badly hurt
  indicator: volatility floor; multi-horizon volatility · asset: multi · conditions: pegged or administered markets · testable: yes: vol-floor effect can be backtested · confidence: high
  ^MT079-C06-4
- **Niels Kaastrup-Larsen** Cocoa was unprofitable for trend followers for 15-20 years and then turned extremely profitable in 2023-24, so removing markets for past losses is dangerous.  #mech/research_method _(time-bound view)_
  > Coco literally was not profitable as far as I can tell for the last 15 or 20 years prior to the beginning of January 2023
  indicator: cocoa trend returns · asset: commodities · horizon: years · testable: yes · confidence: high
  ^MT079-C06-5
- **Niels Kaastrup-Larsen** A market that makes little money but pays when others lose still adds diversification value.  #mech/risk_management
  > there's nothing wrong with having a market that doesn't really make money for you if it makes money when a lot of other things is not making money for you in your portfolio
  indicator: market-level diversification · asset: multi · horizon: years · testable: yes: marginal contribution testable · confidence: medium
  ^MT079-C06-6
- **Mark rinsky** Because removing a market later is hard to decide well, the screening effort should go into adding markets carefully in the first place.  #mech/research_method _(added by opus cross-check)_
  > you want to be very careful in adding markets so that then you don't have to be posed with the problem of whether you should drop it in uh later on
  asset: multi · horizon: years · testable: no - process advice · confidence: medium
  ^MT079-C06-X1

### C07
- **Mark rinsky** An index excluding cocoa (Credit Suisse managed futures index) underperformed CTAs that held cocoa; few markets are dropped except for liquidity.  #mech/research_method _(time-bound view)_
  > it underperformed relative to a lot of ctas who did have Coco
  indicator: cocoa in CTA portfolios · asset: commodities · horizon: months · testable: yes · confidence: high
  ^MT079-C07-1
- **Mark rinsky** Volatility targeting increases size when volatility is artificially low (Swiss franc peg), which was the worst action when the peg broke.  #mech/risk_management
  > I will increase my exposure in those markets that have low volatility and then if let's say there is a spike in volatility I could be on a wrong wrong-sided on that market
  indicator: realised volatility in pegged markets · asset: fx · horizon: days · conditions: pegged or manipulated markets · testable: yes · confidence: high
  ^MT079-C07-2
- **Mark rinsky** Backtests are valuable not for performance or Sharpe (all look good) but for insight into the manager's care in research and treatment of transaction costs and realism.  #mech/research_method
  > I've never seen a bad back test in terms of performance and sharp
  indicator: backtest assumptions · asset: multi · testable: partly · confidence: high
  ^MT079-C07-3
- **Mark rinsky** Commodities whose prices government commodity boards can manage (like cocoa) look like poor trend markets, yet such markets can still produce explosive trends after a supply dislocation, so managed pricing alone is not a reason to exclude them.  #mech/policy_reaction _(added by opus cross-check)_
  > you have you know governments that have uh commodity boards that actually can manipulate price so so there's a whole set of reasons for why you wouldn't want to trade Coco
  indicator: government commodity boards / managed pricing · asset: commodities · horizon: years · conditions: supply shock can override managed pricing · testable: partly - trend returns in board-managed commodities · confidence: medium
  ^MT079-C07-X1

### C08
- **Mark rinsky** Due diligence should ask about backtest assumptions and costs to judge the manager's rigour.  #mech/research_method
  > you get insight into the manager in terms of how careful he is with his uh with his research how careful he is at being able to account for all of the realism in the market
  asset: multi · testable: partly · confidence: high
  ^MT079-C08-1
- **Mark rinsky** Anyone can build a good model; what matters is applying it across many markets, building portfolios and a full system.  #mech/research_method
  > how does someone build a system not a model and there's a difference between the two I can always come up with a good model
  asset: multi · testable: no · confidence: high
  ^MT079-C08-2
- **Mark rinsky** Move from backtest (laboratory) to factory: inputs, outputs, timing, costs, and execution must be realistic.  #mech/research_method
  > you have to take off your scientist hat you have to put on the hat of an engineer and then you have to say I am building a factory
  asset: multi · testable: partly · confidence: high
  ^MT079-C08-3
- **Mark rinsky** Investors' Sharpe thresholds conflict (one rejects below 2, another above 1.25), so research process matters more than the numbers.  #mech/research_method
  > I would say it's the process of how you do your research which is more important than the actual numbers you generate
  indicator: backtest Sharpe ratio · asset: multi · testable: no · confidence: medium
  ^MT079-C08-4

### C09
- **Mark rinsky** Evaluate systematic managers by return generation, portfolio construction and risk management.  #mech/research_method
  > any portfolio you build has to be related to three components one what is the process for return generation two what is the portfolio construction and what is the risk management
  asset: multi · testable: partly · confidence: high
  ^MT079-C09-1
- **Mark rinsky** Regression or model-based signals risk parameter instability, so simple rules are preferred.  #mech/research_method
  > if it's more regression based or it's model based then there's a potential for parameter un uh instability in some sense you you actually like simple rules
  indicator: signal complexity · asset: multi · testable: yes: parameter stability testable · confidence: high
  ^MT079-C09-2
- **Mark rinsky** Portfolio construction (diversification) is the one free lunch available.  #mech/risk_management
  > that's where you're getting the only free lunch available in finance which is diversification
  indicator: diversification · asset: multi · testable: yes · confidence: high
  ^MT079-C09-3
- **Mark rinsky** Risk management belongs in the model's entry and exit rules, with a stop loss as a fail-safe protecting investor principal.  #mech/risk_management
  > a good model should incorporate uh risk management in the portfolio construction and decision rules that you determine when to get long but then you also have a uh determination of when to exit
  indicator: stop loss · asset: multi · testable: yes · confidence: high
  ^MT079-C09-4

### C10
- **Mark rinsky** When valuation and the rate outlook give compelling reasons for both stocks and bonds, follow price trends instead.  #mech/slow_reaction _(time-bound view)_
  > perhaps the best way to approach it is to look at this from a trend following perspective and let the prices themselves tell you what you should do
  indicator: price trend · asset: multi · direction: follow trend in stocks and bonds · horizon: months · conditions: when fundamental case is ambiguous · testable: yes · confidence: medium
  ^MT079-C10-1
- **Mark rinsky** If stock-bond correlation turns positive, 60/40 volatility rises and bonds lose their diversification role, so risk should be monitored via the off-diagonal covariance terms.  #mech/risk_management
  > if correlations change on you and if correlation especially if you have the classic 6040 portfolio it turns positive is is that you're really going to get a lot more volatility in your overall portfolio
  indicator: stock-bond correlation · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT079-C10-2
- **Niels Kaastrup-Larsen** The one-year rolling stock-bond correlation was at a multi-year high in mid-2024, exposing portfolios to higher risk.  #mech/structural_shift _(time-bound view)_
  > the one-year rolling correlation is actually at the highest it's been in a very very long time
  indicator: one-year rolling stock-bond correlation · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT079-C10-3
- **Mark rinsky** Mark says that in mid-2024 stocks appear overvalued on P/E, with the mega-cap technology names well extended, which raises the question of whether to cut equities in the second half.  #mech/new _(added by map cross-check, time-bound view)_
  > we're seeing an environment where stocks seem to be overvalued
  indicator: P/E ratio; mega-cap concentration · asset: equities · direction: bearish · horizon: second half of 2024 · conditions: July 2024 · testable: no - qualitative view · confidence: medium
  ^MT079-C10-R1
- **Mark rinsky** Mark relays the market expectation that the Fed may cut rates as early as September 2024; lower rates, slower growth and lower inflation support both holding equities and holding bonds, so there are compelling reasons for both.  #mech/new _(added by map cross-check, time-bound view)_
  > the FED is actually going to be lowering rates you know possibly as early as September
  indicator: expected Fed cuts · asset: multi · horizon: months · conditions: July 2024 · testable: no · confidence: medium
  ^MT079-C10-R2

### C11
- **Mark rinsky** When stock-bond correlation is positive, bonds are no longer diversifiers and the choice becomes relative valuation.  #mech/risk_premium
  > to really start to think about valuation because uh then it's a relative return situation not a diversification question
  indicator: relative valuation of stocks vs bonds · asset: multi · conditions: positive correlation · testable: partly · confidence: medium
  ^MT079-C11-1
- **Mark rinsky** GIC/JPMorgan paper classifies hedge fund strategies into loss mitigation, equity diversifiers, equity complements and equity substitutes.  #mech/research_method
  > there's loss mitigation strategies equity diversifiers and we'll call Equity complements and Equity substitutes
  indicator: hedge fund strategy buckets · asset: multi · testable: yes · confidence: high
  ^MT079-C11-2
- **Mark rinsky** Classify strategies by equity correlation, drawdown mitigation relative to equities, and alpha after beta.  #mech/research_method
  > one you want to look at what's the correlation with equities
  indicator: correlation to equities, relative drawdown, alpha · asset: multi · testable: yes · confidence: high
  ^MT079-C11-3

### C12
- **Mark rinsky** In the GIC/JPM framework managed futures ranked second for alpha after beta and global macro first.  #mech/structural_shift
  > lo and behold bage Futures is probably number two number one was uh was a global ma Global macro
  indicator: alpha after beta by strategy · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT079-C12-1
- **Mark rinsky** Trend following meets all three criteria (low equity correlation, drawdown mitigation, positive alpha); not an equity substitute.  #mech/structural_shift
  > if you look at what is the strategy that seems to fit within that it's probably Trend following on all three of those counts
  indicator: trend following · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT079-C12-2

### C13
- **Mark rinsky** Being wedded to one model produces false alarms, e.g. post-GFC QE did not cause rampant inflation; entertain alternatives.  #mech/research_method
  > we often use judgment that's you know wedded in a specific model or school of thought
  asset: multi · horizon: years · testable: no · confidence: high
  ^MT079-C13-1
- **Mark rinsky** Doomsday macro forecasts are often wrong; Covid saw a sharp drop but a fast recovery, better than expected.  #mech/behavioral
  > we have a lot of of of macroeconomists or are doomsday or is is they they they make their bones by uh by suggesting that the world is going to come to an end
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT079-C13-2
- **Mark rinsky** Use prices as the null hypothesis and let prices speak before departing.  #mech/research_method
  > prices are Primal and use prices as your sort of your null hypothesis
  indicator: price · asset: multi · testable: no · confidence: high
  ^MT079-C13-3

### C14
- **Mark rinsky** Don't chase data releases such as PCE; the price reaction to the data is what drives positions.  #mech/slow_reaction
  > what's the price action that you see in markets in the next couple of days and that's going to be what the real driver
  indicator: price reaction to macro data · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT079-C14-1
- **Mark rinsky** A paper found LLMs add little to time series forecasting, so model building is harder than expected.  #mech/research_method _(time-bound view)_
  > they looked at llm large language model uh models and they tied it to time series
  indicator: LLM time-series forecasts · asset: multi · testable: yes · confidence: medium
  ^MT079-C14-2
- **Mark rinsky** Machine learning performs well in expansions but poorly in recessions because training data has few recession periods.  #mech/research_method
  > she learning does pretty well during up parts of the business cycle but then when you hit the down uh the downdraft when you hit a recession
  indicator: ML performance across business cycle · asset: multi · conditions: recessions · testable: yes · confidence: medium
  ^MT079-C14-3

### C15
- **Niels Kaastrup-Larsen** Every technology wave in 30 years was predicted to hurt trend following, and it has not.  #mech/structural_shift
  > people were quick to to kind of state that this would have a negative impact on Trend following
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT079-C15-1
- **Mark rinsky** Prices are public and discounted rapidly, so models and new techniques are valuable only if they turn the same public data into private insight others do not have.  #mech/research_method
  > the purpose of building models is to take public information which could be past prices or macro data and then we want to turn it into private information
  asset: multi · testable: no · confidence: high
  ^MT079-C15-2
- **Mark rinsky** Adopting new techniques should be gradual, not a binary switch from old to new models.  #mech/research_method
  > the answer is not going to be digital like like we just need to switch and it's an onoff switch that we should go from one set of models to a new set of models
  asset: multi · testable: no · confidence: medium
  ^MT079-C15-3

### C16
- **Mark rinsky** Law of small numbers: extrapolating from small samples, which affects trend and quant models that decide on limited data, so check sample size and distribution.  #mech/behavioral
  > we often extrapolate from a small sample on what we might think what will happen in the in the future as opposed to using a very large sample
  indicator: sample size in model decisions · asset: multi · testable: yes · confidence: high
  ^MT079-C16-1
- **Mark rinsky** Gambler's fallacy and hot hand: knowing the distribution implies mean reversion, not knowing it implies following the hot hand.  #mech/behavioral
  > if you know the distribution then you probably you're always going to be a uh a mean reverter if you don't know the distribution then you might sort of follow the hot hand
  asset: multi · testable: partly · confidence: medium
  ^MT079-C16-2

