---
source_id: MT073
title: "How Alpha Hides in Plain Sight - Systematic Investor - Ep.362"
date: 2025-08-28
channel: "Top Traders Unplugged"
url: 
words: 12306
claims: 75
added_by_crosscheck: 5
corrections: 1
crosscheck: "opus cross-check"
speakers: ["Alan Dunne (host, sitting in for Niels, allocator/researcher)", "Yoav Git (guest co-host, quant CTA researcher, Cambridge)"]
tags: [source, layer0]
---
# How Alpha Hides in Plain Sight - Systematic Investor - Ep.362

**Speakers:** Alan Dunne (host, sitting in for Niels, allocator/researcher); Yoav Git (guest co-host, quant CTA researcher, Cambridge)

**Summary:** Systematic Investor ep. 362 (Aug 2025): Yoav Git discusses a futures-curve (spread) trend paper, COT-based evidence that trend is not at capacity, the Bank of England FX derivatives paper, and his blog on how CTAs fit with long-term capital-market-assumption allocators (Vanguard 30/70). Main conclusions: trade spreads only after dislocations create risk, speculator positioning shows no trend crowding, and long-horizon allocators are mean-reverting so systematic strategies complement them.

**Approach:** trend following, futures curve and spread trading, market structure, COT positioning, FX derivatives, asset allocation, capital market assumptions

**Cross-check completeness estimate of first read:** 0.95 - first reader covered nearly every idea (72 claims); only a cost figure, the CLS data source and the van Hemert FX-hedging reference were missed; one numeric misstatement on the Vanguard cut.

## Argument map

**Episode thesis:** Yoav Git argues that trend followers should treat futures-curve spreads as transient, dislocation-driven risk factors to be traded with breakout rules only once their volatility has jumped (never at constant risk, which is the LTCM trap), and that the speculator-positioning data show no sign that trend is crowded or at capacity. His blog reverses his own first premise: long-horizon capital-market-assumption allocators (Vanguard's cut to about 30% equities) are mean-reverting, trading the opposite side of trend at a ten-year horizon, so systematic strategies at a three-month horizon are independent alpha for them and can modulate tactical changes.

### Yoav Git (guest co-host; quant CTA researcher based in Cambridge (first-time stand-up comedian that weekend))
Fingerprint: #approach/trend_following #approach/relative_value_arbitrage #approach/positioning_crowding #approach/commodity_fundamentals #approach/regime_detection #approach/research_robustness_overfitting #approach/portfolio_construction_stacking #approach/liquidity_flows
_Speaker note: Recorded Friday 22 August 2025 (Jackson Hole day; index data as of the day before). Ledger correction applied to the Vanguard detail: Vanguard cut its ten-year US equity return assumption by about half a percentage point after a 10-11% June rally, not by half the rally itself. Captions garble names ('Yol', 'Yo', and the spread paper's authors 'Maritz at Takahi Capital'), so author and firm names are not relied on._

**Worldview premises**
- A commodity is not one object: contracts for different delivery months (old crop vs new crop) differ in supply, demand, financial conditions and regulation, so points on the curve can be traded separately. _[institutional, stated; support: Corn crop-year and copper tariff examples from the paper.]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C03-5|C03-5]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C04-1|C04-1]])
- The front of the commodity curve is more volatile and driven by macro news and speculators (new participants crowd into the liquid front contract), while long-dated prices follow long-term supply and demand and are held by slower hedgers and producers. _[empirical, stated; support: Volume versus open interest and Commitments of Traders for copper.]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C04-2|C04-2]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C04-3|C04-3]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C09-1|C09-1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C09-2|C09-2]])
- Spreads show strong, violent breakouts and reversals, so a breakout rule fits them; a breakout signals a fundamental event. _[empirical, stated; support: Paper's finding; examples of tariffs, crop shocks, refinery outages.]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C04-4|C04-4]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C06-3|C06-3]])
- Spread convergence follows the cost of carry (interest, storage, convenience yield) and is slow; dislocations arise when the two contracts are not substitutable (a supply shock to one crop year), which creates a short-lived trend. _[theoretical, stated; support: Economic reasoning on fungibility; corn drought example.]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C05-5|C05-5]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C05-6|C05-6]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C06-1|C06-1]])
- Spread volatility is residual volatility after 90-98% correlation between legs, so it is tiny and itself volatile; targeting constant risk needs huge leverage (50x) and wipes you out in a dislocation (left-skewed), as LTCM's on/off-the-run trade did. _[theoretical, stated; support: LTCM analogy; leg correlation arithmetic.]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C05-1|C05-1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C06-4|C06-4]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C06-5|C06-5]])
- Transient risk factors (spreads, crack spreads, currency basis) are uncorrelated to the rest of the portfolio and so add diversification when traded only while their volatility is sufficient. _[theoretical, stated; support: Argument by examples; no portfolio test given.]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C05-3|C05-3]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C06-2|C06-2]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C07-2|C07-2]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C07-3|C07-3]])
- Relative-value trades are value-based rather than trend-based, so making money from spreads is harder than from outrights; in bond principal components the top factors (about 70% of risk) trend well, middle ones still trend but smaller, and the lowest (pure RV) factors are strongly mean-reverting. _[empirical, stated; support: PCA of bond markets as he describes it (own observation, no numbers shown).]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C07-4|C07-4]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C07-5|C07-5]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C08-1|C08-1]])
- Spreads cost more per unit of risk because both legs trade, while slow outright trend costs only about 0.02-0.03 of Sharpe and is the dominant source of trend returns, so fast spread trend may be uneconomic. _[empirical, stated; support: Cost arithmetic; his own cost benchmarks.]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C08-4|C08-4]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C08-X1|C08-X1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C08-3|C08-3]])
- The claim that trend is at capacity is not supported: industry AUM understates trend capital (QIS, multistrat pods), but regressing speculators' COT positions on trend signals shows loading on fast trend declined since the early 2000s while slow trend loading did not rise; speculators cut positions when volatility rises. _[empirical, stated; support: Own COT regression (descriptive, not predictive), consistent with CTAs migrating to slow trend.]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C09-4|C09-4]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C09-5|C09-5]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C10-1|C10-1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C10-2|C10-2]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C10-3|C10-3]])
- Judge trend over long periods, not one to six months; it is painful like going down the stairs and up the elevator, and its fundamental reasons (zero correlation plus dynamic adaptation) are unchanged by a weak period; investors hold off after poor starts regardless of the manager. _[experience, stated; support: Client conversations and the long historical record (not quoted).]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C02-5|C02-5]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C03-1|C03-1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C03-3|C03-3]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C03-4|C03-4]])
- Describe data structure first before building predictive strategies; understand data before applying machine learning, and avoid overcomplicated models. _[experience, stated; support: The Bank of England paper as an example; the 'virtue of complexity' paper as contrast.]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C11-2|C11-2]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C11-3|C11-3]])
- FX players sit in different habitats along the curve (market makers within a week, hedge funds and asset managers 1-3 months around IMM dates, corporates 2-3 year swaps); UK corporates are structurally long sterling/short dollar and dealers hold the opposite, with US corporates the unseen mirror. _[institutional, stated; support: Non-anonymised regulator data of about 100 million London FX derivative transactions 2015-2020; he concedes the dealer net-position reading may be misleading and needs checking.]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C11-1|C11-1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C12-1|C12-1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C13-1|C13-1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C10-4|C10-4]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C11-X1|C11-X1]])
- Post-GFC dealers cannot hold large risk on their books, so risk passes to corporates and others in bonds, credit and FX; FX derivatives are star-shaped with the top five dealers and five market makers dominating, more than 20 years ago, unlike the spot market with non-bank market makers. _[institutional, stated; support: Paper's structure and his EBS memory; implication unclear to him.]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C13-2|C13-2]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C13-3|C13-3]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C14-1|C14-1]])
- Long-horizon allocators derive the equity/bond split from ten-year capital-market assumptions and a correlation matrix, and their models are mean-reverting: after equities rise they cut expected return and underweight equities, taking the opposite side of trend; an allocator estimates equity beta of managers' P&L but cannot fit CTA positioning because CTAs change exposure too often. _[institutional, stated; support: Conversation with an allocator; Vanguard's July 2025 revision (30% equity, 70% bonds).]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C14-3|C14-3]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C14-4|C14-4]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C15-1|C15-1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C15-2|C15-2]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C15-3|C15-3]])
- Valuation-based long-horizon models (Shiller PE, ten-year views) are useful only for very long horizons, not tactically; selling equities after the June rally would have done poorly (S&P from about 6.2k to 6.4k), and allocators dislike models that have been underweight equities for years. _[empirical, stated; support: S&P move since the end of June; allocator remark.]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C16-1|C16-1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C16-2|C16-2]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C16-3|C16-3]])
- Active traders (CTAs, multistrats, macro funds) operate at a three-month horizon invisible to ten-year allocators, which is why they are uncorrelated to them; treat CTA alpha as independent of the CMA allocation, using positioning only to modulate small tactical changes. _[theoretical, stated; support: Time-horizon and habitat reasoning; he calls it an experimental thought and does not expect consultants to adopt it.]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C17-2|C17-2]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C17-3|C17-3]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C16-R1|C16-R1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C18-X1|C18-X1]])

**Chain: Why spreads should be traded only after a dislocation and with breakouts**
1. Legs 90-98% correlated → Spread volatility is residual and tiny (about 2% of leg vol): Most leg volatility is common. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C06-4|C06-4]])
2. Targeting constant risk on a tiny, itself volatile spread → Needs huge leverage (about 50x), and a dislocation wipes you out (left skew, the LTCM trap): Volatility jumps when contracts stop being substitutable. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C05-1|C05-1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C06-5|C06-5]])
3. Structural break (tariff, refinery outage, crop shock) → Spread volatility rises to about 10% of leg vol and a real fundamental divergence creates a short-lived trend: Contracts become non-fungible; transient risk factor. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C07-1|C07-1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C06-1|C06-1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C06-2|C06-2]])
4. Volatility sufficient → Start trading with dynamic sizing and a breakout signal; exit when volatility fades: A break signals a fundamental event; risk management is key. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C05-2|C05-2]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C06-3|C06-3]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C07-3|C07-3]])
- Evidence: Paper's copper tariff example and his arithmetic; no backtest quoted in the discussion.
- Fails when: Fast spread trend becomes uneconomic after costs (both legs trade); the trigger depends on unpredictable events.

**Chain: Why the trend-capacity argument fails in the data**
1. Industry AUM said to be constant while the market grew → Man's argument that trend is a small part of the market: Ignores trend run inside QIS and multistrat pods. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C09-4|C09-4]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C09-5|C09-5]])
2. Regress speculators' COT positions on trend signals → A high beta would signal crowded trend: Descriptive test of loading. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C10-1|C10-1]])
3. Observed loading → Fast-trend loading fell since the early 2000s, slow-trend loading did not rise, speculators cut positions when volatility rises: CTAs migrated to slow trend and risk-target on volatility. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C10-2|C10-2]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C10-3|C10-3]])
- Evidence: COT regression (his own, not shown in detail).
- Fails when: COT shows only reportable positions and speculator groups; he calls the test descriptive rather than predictive.

**Chain: Why long-horizon allocators are the other side of trend**
1. Ten-year capital market assumptions and correlation matrix set the strategic split → Allocation is the key decision: Derived from expected equity and bond returns. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C15-1|C15-1]])
2. Equities rally (June 2025 +10-11%) → The model lowers expected equity return (Vanguard cut about 0.5 point) and underweights equities (30/70): Mean-reverting models. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C15-2|C15-2]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C15-3|C15-3]])
3. Allocators take the opposite side to trend → Trend can phase the long-term allocation tactically (delay deallocating while trend is strong): Trend is fast; the CMA is slow. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C16-4|C16-4]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C16-5|C16-5]])
4. Different time horizons (ten-year vs three-month) → CTA positioning is invisible to the allocator and alpha is independent: Habitat argument; allocators should stick to their numbers. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C17-2|C17-2]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C17-3|C17-3]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C17-R1|C17-R1]])
- Evidence: Vanguard July 2025 revision; a conversation with one allocator; the S&P rose after June, showing the cost of selling.
- Fails when: He admits his original premise (allocators' delta to equity assumptions is positive, adding to equities) was wrong.

**Chain: Choosing which contract to trade with curve information**
1. Curve spreads show the back cheap and the front dear → If momentum says buy, buy the back: The back is supply/demand driven; the front is macro driven. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C08-5|C08-5]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C04-2|C04-2]])
2. Fast spread trend is uneconomic → Use spread information to select the contract rather than trade the spread: Incremental benefit at low cost. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C08-4|C08-4]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C08-5|C08-5]])
- Evidence: His suspicion of what the researchers do; no numbers.
- Fails when: The benefit is smaller than full spread trading.

**Decision process**
- [universe] Include transient risk factors (calendar spreads, crack spreads, currency basis) only while their volatility is sufficient, and exit when it fades.. Why: Diversification without the leverage trap. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C05-2|C05-2]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C07-3|C07-3]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C07-2|C07-2]])
- [sizing] Do not use constant risk allocation for spreads (unlike outright markets, about 2% per market); size dynamically after a dislocation lifts volatility.. Why: Spread volatility is itself volatile. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C04-5|C04-5]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C05-1|C05-1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C05-2|C05-2]])
- [signal] Use breakout rules on spreads; trade spread trend faster than outright trend but not too fast because of costs.. Why: Breakouts mark fundamental events; costs bite. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C06-3|C06-3]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C08-3|C08-3]])
- [signal] In a PCA-based bond trend system remove the smallest factors and overweight the middle ones.. Why: Lowest factors mean-revert; middle ones still trend. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C08-1|C08-1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C08-2|C08-2]])
- [research] Test crowding by regressing speculators' COT positions on trend signals.. Why: A high beta would indicate crowding. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C10-1|C10-1]])
- [portfolio] Embed systematic strategies in the allocator's optimisation so the allocation adjusts automatically as assumptions change; use trend to phase out of equities.. Why: Covers a wider set of assumption outcomes. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C16-4|C16-4]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C16-5|C16-5]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C18-1|C18-1]])

**Evidence style:** Reads a paper for its mechanism, adds his own risk-management and capacity commentary, uses Commitments of Traders regressions and cost arithmetic; anecdote from allocators; freely admits a wrong premise in his own blog.

**Views at the time**
- (2025-08-22) Trend in fixed income has been difficult in 2025 because US yields oscillate indeterminately, while Japan's 10-year yield has climbed steadily from zero in 2022 to an all-time high, helping trend; at least one other market (name garbled in captions) shows yields falling significantly.. Reasoning: Yield behaviour by market; trend needs persistence. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C02-1|C02-1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C02-2|C02-2]])
- (2025-08-22) CTA allocators remain hesitant after about six months of poor performance; the long-run case is unchanged.. Reasoning: General malaise whatever the manager; client conversations. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C02-5|C02-5]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C03-1|C03-1]])
- (2025-08-22) Selling equities after the June rally would have done poorly; long-horizon valuation views are not for tactical use.. Reasoning: S&P rose from about 6.2k to 6.4k since end-June. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C16-2|C16-2]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C16-3|C16-3]])
- (2025-08-22) Copper has become more speculative at the front of the curve, with CTAs and multistrats now trading it.. Reasoning: Volume versus open interest and COT. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C09-1|C09-1]])

### Alan Dunne (host, sitting in for Niels Kaastrup-Larsen) (host; allocator/researcher; asks clarifying questions and adds headlines)
Fingerprint: #approach/trend_following #approach/macro_fundamental_topdown #approach/fiscal_dominance #approach/manager_selection_allocation #approach/portfolio_construction_stacking
_Speaker note: Captioned 'Alan Dunn'. Mostly questions; views listed are those he states himself._

**Worldview premises**
- Fiscal dominance (monetary policy bending to fiscal needs at high debt) is becoming a market theme alongside rising Japanese yields, though not fully reached. _[theoretical, stated; support: FT story and record Japanese yields.]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C02-3|C02-3]])
- Where many risk-averse hedgers exist, speculators can earn a risk premium. _[theoretical, stated; support: Textbook reasoning; no data.]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C09-3|C09-3]])
- Most managers trade spreads for mean reversion/carry, not breakout trend. _[experience, stated; support: Industry knowledge.]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C05-4|C05-4]])
- Mean-variance frameworks were designed for assets, not strategies that trade the same assets, so allocating to CTAs raises a conceptual problem; a CTA allocation adds or removes equity exposure with the equity trend, a favourable portfolio effect. _[theoretical, stated; support: Reasoning about allocation frameworks.]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C17-1|C17-1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C16-6|C16-6]])
- Hedge fund net FX exposures fluctuate widely and dealers hold the opposite of hedgers. _[empirical, stated; support: Paper's net exposure chart; Yoav says the dealer reading is partly misleading.]_ ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C12-2|C12-2]])

**Evidence style:** Headlines, index data and conceptual allocator framing; defers to the guest on research.

**Views at the time**
- (2025-08-22) BlackRock recommended raising hedge fund allocations by 5%, reflecting a more volatile macro environment, while Vanguard recommends a bond-heavy 70/30 style allocation; CTA allocators remain hesitant.. Reasoning: FT reports; the volatile macro case for hedge funds also applies to CTAs. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C02-4|C02-4]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C14-2|C14-2]])
- (2025-08-21) SG Trend Index down about 8.5% YTD and SG CTA nearly 7% (to the previous day); August up (Trend +1.67%, CTA about +0.5%); fixed-income trends in Japan and Europe helping, FX and equities rangy.. Reasoning: Index data. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C03-2|C03-2]])

### Disagreements
- **How managers trade spreads**: Alan Dunne: Most managers trade spreads for mean reversion or carry, not breakout trend. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C05-4|C05-4]]); Yoav Git: Carry convergence is slow and traditional, but dislocations from non-substitutable contracts create short trends best traded by breakout after volatility rises. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C05-5|C05-5]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C05-6|C05-6]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C05-2|C05-2]])
- **How CTAs fit into a capital-market-assumption allocation**: Alan Dunne: Mean-variance was built for assets, and CTAs trade those assets, which creates a conceptual problem; asks whether the CTA allocation should be higher given the extra tactical role. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C17-1|C17-1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C16-6|C16-6]]); Yoav Git: Horizon difference resolves it: treat CTA alpha as independent of the ten-year allocation and use positioning only to modulate small tactical changes. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C17-2|C17-2]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C17-3|C17-3]])

### Gaps and conflicts
- Yoav's blog premise (long-term allocators add to equities when they have risen, i.e. their delta is positive) was wrong, and he says so; the revised claim is that they mean-revert and trade opposite to trend. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C15-2|C15-2]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C16-R1|C16-R1]])
- The Vanguard numbers are muddled in the transcript: the ledger correction says a cut of about 0.5 point from about 4.5%, but the speaker also says 'we're left with three and a half percent'; the 30/70 allocation figure is given without the model's inputs. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C15-3|C15-3]])
- The dealer net-position reading from the BoE paper is flagged by Yoav himself as partly misleading (missing the US side) and he says it needs checking. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C12-2|C12-2]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C13-1|C13-1]])
- The authors and paper titles are garbled by captions; the spread paper's findings are reported second-hand with no tests quoted (no Sharpe, no backtest for spread breakout). ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C04-4|C04-4]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C07-1|C07-1]])
- The COT crowding regression is described without results beyond the direction of loadings; speculator categories in COT do not isolate trend followers. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C10-1|C10-1]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C10-3|C10-3]])
- The statement that PCA factors cover about 70% of risk in the top quartile and that the lowest are mean-reverting comes from his own work without numbers; the first 25% is also described loosely as 'about 70% of risk'. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C07-5|C07-5]], [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C08-1|C08-1]])
- The explanation that trend underperformed in 2025 is not given; Yoav declines to discuss and only argues against the capacity cause. ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C10-3|C10-3]])

### Forward-looking inputs (reader synthesis)
(reader) For the trend book the speakers watch persistence of yield moves by market (Japan, Europe versus choppy US), volatility jumps in spreads after policy or supply shocks (tariffs, refinery outages, crop shocks) as the trigger for spread trades, and COT loading of speculators on trend signals for crowding. For allocators the horizon is ten years for capital-market assumptions versus three months for active traders; Vanguard-style mean-reverting models change equity weights after rallies, which is the opposite side of trend.

### Reader inferences (not stated by the speakers)
- (reader) Yoav's spread logic is a volatility-regime rule: the signal is not the spread's level but its volatility jumping from about 2% to about 10% of leg volatility, so the trade is sized by the new volatility and switched off when it fades.
- (reader) His capacity argument depends on loading of speculators' positions rather than AUM, so a rise in slow-trend loading would be the observable that refutes his view.
- (reader) Both speakers frame long-horizon allocators as natural counterparties to trend, so periods when CMA models cut equities after a rally while trend is long are the structural source of the opposite-side positioning.
- (reader) His admission of a wrong premise shows how he treats own errors: keep the principle (systematic strategies belong inside the optimisation) while discarding the mechanism that was falsified.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | nothing actionable: intro, holidays, comedy gig |
| C02 | 5 | fixed income trend difficulty, Japan yields, fiscal dominance, BlackRock hedge funds, CTA malaise |
| C03 | 5 | CTA performance, patience, trend as zero correlation; paper on curve trading intro |
| C04 | 5 | copper tariff dislocation, front vs back of curve, spread breakouts, static vs spread risk |
| C05 | 6 | sizing spreads, waiting for dislocation, trend vs carry/mean reversion in spreads |
| C06 | 5 | supply shocks and crack spreads, breakouts, residual volatility, LTCM analogy |
| C07 | 5 | risk-managed spread trading, currency basis, PCA factors of rates |
| C08 | 5 | mean-reverting PCA factors, speed, costs, using curves to select contracts |
| C09 | 5 | speculation in copper front curve, COT, trend capacity argument |
| C10 | 4 | COT loading on trend, no capacity evidence; FX market size |
| C11 | 3 | FX topography paper data, descriptive research approach |
| C12 | 2 | habitats of FX players along the curve, exposures |
| C13 | 3 | dealer risk, UK corporate hedging, concentration of dealers |
| C14 | 4 | spot vs derivative structure; Vanguard 70/30; allocator process and CTA exclusion |
| C15 | 3 | capital market assumptions, mean-reverting long-term allocators, Vanguard cut |
| C16 | 6 | allocator view, trend as tactical phasing, systematic strategies in optimisation |
| C17 | 3 | time horizons of CMA vs active traders, alpha as independent play |
| C18 | 1 | embedding systematic strategies like FX hedging and CTA; sign-off |

## Claims

### C02
- **Yoav Git** Trend following in fixed income has been difficult in 2025 because US yields oscillate indeterminately, while Japan shows a persistent climb and other markets show opposite drifts.  #mech/slow_reaction _(time-bound view)_
  > it has been a very difficult uh period for trend in fixed income
  indicator: trend signals in bond futures · asset: rates · horizon: months · conditions: range-bound US yields · testable: yes · confidence: high
  ^MT073-C02-1
- **Yoav Git** Japan's 10-year yield rose steadily from zero in 2022 to an all-time high in August 2025, a persistent trend benefiting trend followers.  #mech/slow_reaction _(time-bound view)_
  > they've started a long climb back in 2022 from zero now sitting at an all-time high last night
  indicator: Japan 10-year yield · asset: rates · direction: higher JGB yields · horizon: years · testable: yes · confidence: high
  ^MT073-C02-2
- **Alan Dunne** Fiscal dominance (monetary policy bending to fiscal needs at high debt) is becoming a market theme alongside rising Japanese yields.  #mech/fiscal_debt _(time-bound view)_
  > the idea that monetary policy will um kind of have to adapt to the fiscal stance you know when debt levels get so great
  indicator: long-end yields · asset: rates · direction: higher yields · horizon: years · conditions: high debt levels · testable: partly · confidence: medium
  ^MT073-C02-3
- **Alan Dunne** BlackRock recommended raising hedge fund allocations by 5%, reflecting a more volatile macro environment, though CTA allocators remain hesitant after poor H1 returns.  #mech/crowding_positioning _(time-bound view)_
  > recommending that investors increase their allocations to hedge funds by 5%
  indicator: hedge fund allocation · asset: multi · horizon: months · testable: no - recommendation · confidence: medium
  ^MT073-C02-4
- **Yoav Git** Investors hold off allocating to CTAs after six months of poor performance regardless of manager, even though the case for CTAs persists.  #mech/behavioral _(time-bound view)_
  > I think there is a general malaise in the CTA industry. Investors are waiting to see what's happening.
  indicator: CTA investor sentiment · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT073-C02-5

### C03
- **Yoav Git** The long-run reasons to hold CTAs are unchanged by a weak period.  #mech/risk_premium
  > alltime performance of CTAs, the reasons why they should invest in CTAs is that actually hasn't gone away at all
  asset: multi · horizon: years · testable: partly · confidence: high
  ^MT073-C03-1
- **Alan Dunne** As of late August 2025 the SG Trend index was down about 8.5% YTD and the SG CTA index nearly 7% down, with fixed income trends in Japan and Europe helping and FX/equities rangy.  #mech/slow_reaction _(time-bound view)_
  > year to date the trend index down 8 and a half% and the sock CTA index down just under 7%
  indicator: SG Trend index, SG CTA index · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT073-C03-2
- **Yoav Git** Judge trend following over long periods, not one to six months; it is painful like going down the stairs and up the elevator.  #mech/risk_management
  > it will be a mistake to look at at you know, one month performance, two months per even six month performance
  asset: multi · horizon: years · testable: partly · confidence: high
  ^MT073-C03-3
- **Yoav Git** Trend following offers zero correlation to the rest of a portfolio plus dynamic adaptation, a fundamental reason to hold it.  #mech/risk_premium
  > you're buying that that uh beautiful zero correlation to the um to the rest of the rest of your portfolio while you have a dynamic adjustment to market conditions
  indicator: correlation of trend to portfolio · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT073-C03-4
- **Yoav Git** A commodity is not one object: contracts for different delivery months (old crop vs new crop) differ by supply, demand, regulation, so curve points can be traded separately.  #mech/structural_shift
  > you can buy corn for delivery at different months and the different months may behave differently right
  indicator: futures curve by delivery month · asset: commodities · horizon: months · testable: yes · confidence: high
  ^MT073-C03-5

### C04
- **Yoav Git** Policy shocks such as copper tariffs create dislocations between adjacent contract spreads because one contract falls before and one after the tariff.  #mech/policy_reaction _(time-bound view)_
  > if I look at the difference between two deliveries two contracts Suddenly sometimes you get a dislocation uh and they behave differently
  indicator: copper calendar spread · asset: commodities · horizon: weeks · conditions: tariff announcements · testable: yes · confidence: high
  ^MT073-C04-1
- **Yoav Git** The front of the commodity curve is more volatile and driven by macro news, while long-dated prices follow long-term supply and demand.  #mech/structural_shift
  > the front of the curve is generally the one which is more volatile in the commodity business world and it is the one which is more affected by macronuse flow
  indicator: front vs deferred volatility · asset: commodities · testable: yes · confidence: high
  ^MT073-C04-2
- **Yoav Git** New participants crowd into the liquid front contract, increasing volume there.  #mech/crowding_positioning
  > when other players come onto the markets they tend to congregate where the the liquidity is and the front of the curve is where the liquidity is
  indicator: front-month volume · asset: commodities · horizon: years · testable: yes · confidence: high
  ^MT073-C04-3
- **Yoav Git** Calendar spreads show strong breakouts and reversals, and breakouts are violent, so a breakout rule fits spread trading.  #mech/slow_reaction
  > spreads exhibit strong breakouts and reversals and I like I like the what they say about breakouts because the um when spreads actually break do break out it's actually quite violent
  indicator: spread breakout · asset: commodities · direction: trade spread breakouts · horizon: days · testable: yes · confidence: medium
  ^MT073-C04-4
- **Yoav Git** Traditional CTAs hold roughly constant risk allocations per outright market, but this cannot be done for spreads.  #mech/risk_management
  > they allocate to each of the individual markets and that allocation is relatively static over time
  indicator: static risk allocation · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT073-C04-5

### C05
- **Yoav Git** Spread volatility is itself volatile, so targeting constant risk needs huge leverage and wipes you out in a dislocation (left-skewed).  #mech/risk_management
  > if you try to make this spread provide you with that risk you will have to leverage your position to such an extent that when a dislocation does happen you will be out of business
  indicator: spread volatility · asset: commodities · horizon: days · conditions: quiet spread regimes · testable: yes · confidence: high
  ^MT073-C05-1
- **Yoav Git** Only start trading a spread after a dislocation lifts its volatility to a minimum level, then size it dynamically.  #mech/risk_management
  > you have to wait until actually a dislocation happens you can't get into the trade first
  indicator: spread volatility threshold · asset: commodities · horizon: weeks · conditions: after a dislocation · testable: yes · confidence: high
  ^MT073-C05-2
- **Yoav Git** Allocating risk to transient risk factors (such as spreads) adds diversification because they are uncorrelated to the rest of the portfolio.  #mech/risk_premium
  > being able to allocate meaningful risk to risk factors that um rise and they are transient by nature is something which I think is quite important
  indicator: transient spread risk factors · asset: multi · horizon: weeks · testable: partly · confidence: medium
  ^MT073-C05-3
- **Alan Dunne** Most managers trade spreads for mean reversion/carry, not breakout trend.  #mech/research_method
  > a lot of managers trade spreads more from I suppose for the spread to revert to more mean reversion
  indicator: calendar spreads · asset: commodities · testable: yes · confidence: high
  ^MT073-C05-4
- **Yoav Git** Spread convergence follows cost of carry (interest, storage, convenience yield) and is slow, while dislocations arise when contracts are not substitutable.  #mech/risk_premium
  > the play for the convergence of these two things is is normally the carriage rate and it's a kind of a nice and slow process.
  indicator: cost of carry · asset: commodities · horizon: months · conditions: contracts fungible · testable: yes · confidence: high
  ^MT073-C05-5
- **Yoav Git** If two contracts are fungible they converge; a supply shock to one crop year breaks that and produces divergence.  #mech/structural_shift
  > if the two objects are funible then you will expect them to converge.
  indicator: spread convergence · asset: commodities · horizon: months · testable: yes · confidence: medium
  ^MT073-C05-6

### C06
- **Yoav Git** A real fundamental divergence (next crop shock) drives a short-lived trend in the spread.  #mech/slow_reaction
  > Okay. So then what you have is you have a real reason for that divergence between those spreads and that will create a a trend.
  indicator: corn old/new crop spread · asset: commodities · horizon: weeks · conditions: supply shock · testable: yes · confidence: high
  ^MT073-C06-1
- **Yoav Git** Refinery outages make crack spreads trend, a transient and diversifying risk factor unrelated to long-term oil.  #mech/structural_shift
  > unscheduled stoppage in those refineries, right? So suddenly suddenly what you have is you have uh that spread will start trending
  indicator: crack spread · asset: commodities · horizon: weeks · conditions: storms, outages · testable: yes · confidence: high
  ^MT073-C06-2
- **Yoav Git** Use breakout signals on spreads because a break signals a fundamental event.  #mech/slow_reaction
  > they use breakout rather than using sort of a smooth trading because you actually are looking for a breakout as an indication of something something fundamental happening there
  indicator: spread breakout signal · asset: commodities · horizon: days · testable: yes · confidence: medium
  ^MT073-C06-3
- **Yoav Git** Spread volatility is residual volatility after 90-98% correlation between legs, so it is tiny and needs 50x leverage to matter.  #mech/risk_management
  > But what they're looking for is like the residual volatility, the the difference in movement between the two.
  indicator: spread residual volatility · asset: commodities · testable: yes · confidence: high
  ^MT073-C06-4
- **Yoav Git** Leveraging a 2% residual-vol spread is the LTCM trap (on/off the run Treasuries); trade only when the spread becomes volatile.  #mech/risk_management
  > LTCM bumped up the risk profile by you know 50x 100x and then of course when those spreads we refuse to converge
  indicator: spread leverage · asset: rates · testable: yes · confidence: high
  ^MT073-C06-5

### C07
- **Yoav Git** After a structural break (tariff, refinery), spread volatility rises from about 2% to about 10% of leg vol, making it tradeable without much leverage.  #mech/risk_management
  > becomes 10% of the volatility and now it's interesting it's a it's actually a valid risk factor that you can trade with not too much leverage
  indicator: spread volatility share · asset: commodities · horizon: weeks · conditions: after a break · testable: yes · confidence: high
  ^MT073-C07-1
- **Yoav Git** Currency basis moves can trend when transient funding pressure arises (e.g., bond issuance in USD), so they are another transient factor to trade with strict risk rules.  #mech/liquidity_flows
  > a currency basis is the difference between uh funding funding in local currency versus the US
  indicator: cross-currency basis · asset: fx · horizon: weeks · conditions: funding pressure · testable: yes · confidence: medium
  ^MT073-C07-2
- **Yoav Git** Trade transient factors only while their volatility is sufficient, exit when it fades.  #mech/risk_management
  > the ability to say I'm going to wait until there is a sufficient risk to start trading it um and then I'm going to get out of this when when there isn't enough volatility
  indicator: volatility gating · asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT073-C07-3
- **Yoav Git** Making money from spreads is harder than from outrights because relative value is value-based rather than trend-based.  #mech/slow_reaction
  > relative value trades are called relative value because uh it's value rather than trend. So making money out of spreads is more difficult.
  asset: multi · testable: partly · confidence: medium
  ^MT073-C07-4
- **Yoav Git** In bond markets the top principal components trend very well and cover about 70% of risk, the middle ones still trend but smaller.  #mech/slow_reaction
  > maybe the first 25% of of PCA factors trend very well sort of then then we have like a 50% of the remaining uh PCA factors and they do trend
  indicator: PCA factors of bond markets · asset: rates · direction: trade top and middle PCA factors · testable: yes · confidence: medium
  ^MT073-C07-5

### C08
- **Yoav Git** The lowest PCA factors (pure RV trades) are strongly mean-reverting, not trending.  #mech/slow_reaction
  > they tend to actually move in the opposite direction. So they will tend to be uh actually very strongly mean reverting.
  indicator: bottom PCA factors · asset: rates · direction: avoid trend on bottom factors · testable: yes · confidence: medium
  ^MT073-C08-1
- **Yoav Git** Remove the smallest factors and overweight middle factors in a PCA-based trend system.  #mech/research_method
  > Or maybe you want to upweight the middle factors because although they are they are they they trend less
  indicator: PCA factor weighting · asset: rates · testable: yes · confidence: medium
  ^MT073-C08-2
- **Yoav Git** Spread trend should be traded faster than outright trend but not too fast because costs bite.  #mech/risk_management
  > fast but not as fast as you think
  indicator: spread trend speed · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT073-C08-3
- **Yoav Git** Spreads cost more per unit of risk since both legs trade, so fast spread trend may be uneconomic.  #mech/risk_management
  > the notional amount that I trade is higher and therefore my trading cost will be higher. So like per turnover the spread will be more expensive than trading outright.
  indicator: spread transaction cost · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT073-C08-4
- **Yoav Git** Use curve spreads to choose which contract to trade: if momentum wants to buy and the back is cheap, buy the back (supply/demand driven) rather than the front (macro driven).  #mech/risk_management
  > the back of the curve looks cheap while the front of the curve looks dear. If you if momentum wants to buy something then maybe you should buy the back.
  indicator: curve shape for contract selection · asset: commodities · direction: buy deferred contracts · horizon: weeks · testable: yes · confidence: medium
  ^MT073-C08-5
- **Yoav Git** Trading costs for slow outright trend are small, roughly 0.02-0.03 of Sharpe ratio, and slow trend is the dominant source of trend returns, which sets the cost benchmark that spread trading must beat.  #mech/research_method _(added by opus cross-check)_
  > if I'm trading the outright there's going to be a certain cost in sharper basis stuff. So maybe three two or three basis points of sharp okay so 002 of sharp
  indicator: transaction cost in Sharpe-ratio units · asset: commodities · horizon: months · conditions: slow outright trend vs faster spread trend · testable: yes - gross vs net Sharpe by speed and instrument · confidence: medium
  ^MT073-C08-X1

### C09
- **Yoav Git** Copper has become more speculative (CTAs, multistrats) at the front of the curve, seen in volume vs open interest and COT.  #mech/crowding_positioning
  > these days everybody is trading copper and as a result the copper has become sort of more speculative in nature right
  indicator: volume/open interest, COT in copper · asset: commodities · horizon: years · testable: yes · confidence: high
  ^MT073-C09-1
- **Yoav Git** Hedgers and producers dominate further out the curve, trade slowly, and give open interest with less volume, so contract dynamics differ along the curve.  #mech/liquidity_flows
  > they tend to trade more slowly so there's less volume there is more open interest
  indicator: stock vs flow along curve · asset: commodities · testable: yes · confidence: high
  ^MT073-C09-2
- **Alan Dunne** Where many risk-averse hedgers exist, speculators can earn a risk premium.  #mech/risk_premium
  > But if there's a lot of hedggers in a market, then there and they're risk averse, then in theory there's a there is a premium a risk.
  indicator: hedger/speculator mix · asset: commodities · testable: yes · confidence: medium
  ^MT073-C09-3
- **Yoav Git** Clients argue trend underperformed because too much money is in trend; Man's AUM argument says industry AUM is constant.  #mech/crowding_positioning
  > some an argument which comes up quite often is to say oh uh trend is at capacity.
  indicator: trend industry AUM · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT073-C09-4
- **Yoav Git** Industry AUM understates trend capital since QIS and multistrat pods also run trend.  #mech/crowding_positioning
  > Um the problem with this argument is that there is tons of trend being done at other places where you don't see it.
  indicator: hidden trend assets · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT073-C09-5

### C10
- **Yoav Git** Test crowding by regressing speculators' COT positions on trend signals; high beta would signal crowded trend.  #mech/research_method
  > if the industry was overly trend reliant then what you would see is you would see a good correlation yeah a beta between the speculators positioning in the cult report to your signal
  indicator: COT speculator positioning vs trend signal · asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT073-C10-1
- **Yoav Git** Speculators cut positions when volatility rises, a dominant effect now (volatility-based risk targeting).  #mech/risk_management
  > the speculators have become very sensitive to volatility. So the loading on changes in volatility i.e. if volatility goes up the it goes the speculators uh proportion goes down.
  indicator: speculator positioning vs volatility · asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT073-C10-2
- **Yoav Git** Loading on fast trend declined since the early 2000s while CTAs migrated to slow trend; slow trend loading did not rise, so the capacity argument is not supported.  #mech/crowding_positioning
  > What we don't see is we don't see like suddenly a huge rise or in fact any rise whatsoever in terms of the loading on on slow trend or mid-frequency trend in the data.
  indicator: COT loading on trend by speed · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT073-C10-3
- **Yoav Git** The FX market trades about 7.5 trillion daily (BIS 2022), dwarfing equities and including corporates, asset managers and funds.  #mech/liquidity_flows
  > the amount of daily trading in FX is something like 7.5 trillion
  indicator: BIS triennial survey · asset: fx · testable: yes · confidence: high
  ^MT073-C10-4

### C11
- **Yoav Git** A Bank of England-led paper (Topography of the FX derivative market) uses regulator-level non-anonymized London FX derivative data for 2015-2020.  #mech/research_method
  > They have 100 million transactions, millions of transactions in the London FX markets from 2015 to 2020. And it's non anonymized.
  indicator: London FX derivatives transaction data · asset: fx · testable: yes · confidence: high
  ^MT073-C11-1
- **Yoav Git** Describe data structure first before building predictive strategies; avoid overcomplicated models.  #mech/research_method
  > a lot of quans again rush into here's a trading strategy. Sit back just just look at the data. Let it tell you a story.
  asset: multi · testable: partly · confidence: high
  ^MT073-C11-2
- **Yoav Git** Understand the data before using machine learning on it.  #mech/research_method
  > it behooves us as corns rather than just shoving it into a machine to really understand what's going on
  asset: multi · testable: partly · confidence: high
  ^MT073-C11-3
- **Yoav Git** Few data sets show FX positioning; CLS, a major FX settlement provider, offers heavily anonymized flow data, which the regulator-level Bank of England data far exceeds in granularity.  #mech/research_method _(added by opus cross-check)_
  > there's uh CLS is one of the biggest providers they do settlement FX settlements and they offer some data which is very anonymized
  indicator: CLS FX settlement flow data · asset: fx · testable: partly - data availability statement · confidence: high
  ^MT073-C11-X1

### C12
- **Yoav Git** FX market makers hold risk in contracts up to one week; hedge funds and asset managers trade 1-3 months (IMM dates); corporates hold 2-3 year swaps, each in their own habitat along the curve.  #mech/liquidity_flows
  > most of it is up to one one week uh expiry right and and that's the most liquid part
  indicator: FX derivative maturity by participant · asset: fx · testable: yes · confidence: high
  ^MT073-C12-1
- **Alan Dunne** Hedge fund net FX exposures fluctuate widely, while dealers hold the opposite of hedgers.  #mech/crowding_positioning
  > the hedge funds uh specs their net exposures to the dollar euro and sterling fluctuate a lot
  indicator: net FX exposures by segment · asset: fx · horizon: weeks · testable: yes · confidence: medium
  ^MT073-C12-2

### C13
- **Yoav Git** UK corporates are structurally long sterling/short dollar from hedging, and dealers hold the opposite; US corporates are the unseen mirror position.  #mech/liquidity_flows
  > there's a structural short dollar for UK corporates right because they have they hedge their dollars back to the UK
  indicator: UK corporate FX hedging · asset: fx · horizon: years · testable: yes · confidence: medium
  ^MT073-C13-1
- **Yoav Git** Post-GFC dealers cannot hold large risk on their books, so risk is passed through to corporates and others in bonds, credit and FX.  #mech/liquidity_flows
  > the amount of risk which is available on the market that you are you are able to hold is actually not not not that great
  indicator: dealer risk capacity · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT073-C13-2
- **Yoav Git** The FX derivative market is star-shaped: the top five dealers and five market makers dominate, much more than 20 years ago.  #mech/structural_shift
  > the top five dealer and the top five market makers really dominate the everything
  indicator: dealer concentration · asset: fx · horizon: years · testable: yes · confidence: high
  ^MT073-C13-3

### C14
- **Yoav Git** FX spot is structured differently, with non-bank market makers, while derivatives are concentrated in few counterparties which may be a cause for concern.  #mech/structural_shift
  > the emergence of players like the the non-bank um market makers so like the XTX and the J Street
  indicator: FX spot vs derivative structure · asset: fx · testable: partly · confidence: medium
  ^MT073-C14-1
- **Alan Dunne** Vanguard recommends a 70/30 style allocation (bond-heavy, 30% equity per Yoav) despite BlackRock's hedge fund call.  #mech/behavioral _(time-bound view)_
  > Vanguard kind of going against the tide a little bit by suggesting they're suggesting 7030 is the optimal for the next decades
  indicator: Vanguard time-varying asset allocation model · asset: multi · horizon: years · testable: no · confidence: medium
  ^MT073-C14-2
- **Yoav Git** An allocator estimates the equity beta of each manager's P&L to track hidden equity exposure.  #mech/risk_management
  > we actually do try to figure out the the beta let's say the equity beta on each of the uh data sets and we fit the the P&L of each of uh the people that we allocate to
  indicator: manager P&L equity beta · asset: equities · horizon: months · testable: yes · confidence: medium
  ^MT073-C14-3
- **Yoav Git** Allocators cannot fit CTA positioning from P&L because CTAs change exposure too often, showing CTAs' lack of persistent correlation.  #mech/risk_management
  > we exclude you guys, we exclude CTAs because you guys change, you change your mind too too often
  indicator: CTA equity beta · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT073-C14-4

### C15
- **Yoav Git** The strategic equity-bond split, derived from 10-year capital market assumptions and a correlation matrix, is the allocator's key decision.  #mech/research_method
  > that's actually probably one of the most important decisions that you have to make about you know what's the proportion between equities and bonds
  indicator: capital market assumptions · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT073-C15-1
- **Yoav Git** Long-horizon CMA-based allocators are mean-reverting: after equities rise they cut expected return and underweight equity, taking the opposite side of trend.  #mech/behavioral
  > most most of these models are mean reverting by nature i.e. If equities go up, they will actually underweight equity.
  indicator: CMA-based allocation · asset: equities · direction: sell equities after rallies · horizon: months · testable: yes · confidence: high
  ^MT073-C15-2
- **Yoav Git** Vanguard cut its 10-year equity return forecast by half the June 2025 rally (10-11%), leading to a 30% equity / 70% bond allocation.  #mech/behavioral _(time-bound view)_
  > they only cut 50% of it. So we we they cut the expect long-term expectation to to equity by half a percent based on actually very short-term change in equities.
  indicator: Vanguard 10-year equity return forecast · asset: equities · direction: less equity · horizon: years · testable: yes · confidence: high
  **Correction (cross-check):** Wrong number: Vanguard cut its 10-year equity return expectation by about half a percentage point (about half of the roughly 1%/yr implied by the 10-11% June rally, from about 4.5%), not by half the rally itself. → After the 10-11% June 2025 equity rally Vanguard cut its 10-year US equity return assumption by about 0.5 percentage point (from roughly 4.5%), half the rally's per-year effect, and moved to about 30% equities / 70% bonds.
  ^MT073-C15-3

### C16
- **Yoav Git** Allocators dislike valuation-based models that have been underweight equity for years.  #mech/behavioral
  > we kind of don't like them because they they have been negative equity for years
  indicator: valuation-based long-term models · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT073-C16-1
- **Yoav Git** Selling equities after the June rally would have done poorly, as the S&P rose from 6.2k to 6.4k.  #mech/slow_reaction _(time-bound view)_
  > equity has been has been uh has been rising quite happily regardless of what Vanguard is saying
  indicator: S&P 500 · asset: equities · horizon: weeks · testable: yes · confidence: medium
  ^MT073-C16-2
- **Yoav Git** Long-horizon valuation metrics (Shiller PE, 10-year views) are only useful for very long horizons, not for tactical use.  #mech/research_method
  > all of these very long-term 10-year horizon things um uh all of these are uh maybe make sense if you're investing for 100 years
  indicator: Shiller PE · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT073-C16-3
- **Yoav Git** Trend can phase in or out a long-term allocation tactically, e.g. delay deallocating from equities while trend is strong.  #mech/slow_reaction
  > the role of trend not necessarily as a long-term but as a tactical as a long-term right but as a tactical way of you phasing in that long-term view
  indicator: trend as allocation overlay · asset: equities · horizon: months · testable: yes · confidence: medium
  ^MT073-C16-4
- **Yoav Git** Including systematic strategies in the optimization automatically adjusts the allocation as assumptions change.  #mech/risk_management
  > you will be able to create an optimal allocation over a much wider set of parameters
  indicator: systematic strategies in allocation · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT073-C16-5
- **Alan Dunne** A CTA allocation adds or removes equity exposure with the equity trend (long in bull, short in bear), a favorable portfolio effect.  #mech/slow_reaction
  > CTAs will modulate your overall equity exposure. So, if you have 50% equities and you have 20% CTA, you're going to pick up some more equity exposure in your CTA allocation
  indicator: CTA equity exposure · asset: equities · horizon: months · testable: yes · confidence: medium
  ^MT073-C16-6
- **Yoav Git** Yoav concedes that his blog's premise, that long-term allocators add to equities when equities have gone up, was wrong; their models are mean-reverting, though his principle of embedding systematic strategies in the allocation still holds.  #mech/new _(added by map cross-check)_
  > the premise that I had in my mind that the the delta of uh long-term allocators is positive is completely false.
  indicator: change in capital-market assumptions after rally · asset: equity · direction: mean-reverting · horizon: ten-year CMA horizon · conditions: long-horizon CMA-based allocators such as Vanguard · testable: partly - allocator model revisions · confidence: high
  ^MT073-C16-R1

### C17
- **Alan Dunne** Mean-variance frameworks were designed for assets, not for strategies that trade those same assets, creating a conceptual problem.  #mech/research_method
  > now we got the we're adding strategies such as CTA which are trading some of the assets that you're diversifying
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT073-C17-1
- **Yoav Git** Active traders operate at a three-month horizon, invisible to 10-year allocators, which is why they are uncorrelated and long-term allocators should not worry about their positioning.  #mech/risk_premium
  > they are playing in a different time horizon than you they're playing at the three-month horizon
  indicator: time horizon · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT073-C17-2
- **Yoav Git** Treat CTA/systematic alpha as independent of the CMA allocation, using its positioning only to modulate small tactical changes.  #mech/risk_management
  > in terms of alpha, you just think of it as almost an independent play
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT073-C17-3
- **Yoav Git** For long-term allocations built on capital-market assumptions, Yoav's advice is to stick with the numbers and ignore three-month noise, leaving tactical adjustment to systematic strategies on a different horizon.  #mech/new _(added by map cross-check)_
  > stick with those numbers have those allocations go and play golf right you know allocate for equity long-term
  asset: multi · horizon: ten years versus three months · conditions: investors using CMA-based strategic allocation · testable: no · confidence: medium
  ^MT073-C17-R1

### C18
- **Yoav Git** Allocators already embed systematic strategies such as FX hedging and could embed trend as another tool.  #mech/risk_management
  > some systematic strategies like FX hedging are part of the way that you embed are embedded into your process
  indicator: systematic FX hedge · asset: fx · horizon: years · testable: partly · confidence: medium
  ^MT073-C18-1
- **Yoav Git** An allocator with structural foreign-currency exposure (e.g. an Australian investor holding USD assets) should hedge it with a systematic rule; a van Hemert paper studies the best ways to hedge FX exposure, a simple model for embedding systematic strategies such as trend into allocation.  #mech/risk_management _(added by opus cross-check)_
  > there's a great paper by van Hemtt um about the best ways to hedge FX exposure
  indicator: systematic FX hedge ratio rules · asset: fx · horizon: months · conditions: investors with structural FX exposure · testable: yes - compare hedging rules historically · confidence: medium
  ^MT073-C18-X1

