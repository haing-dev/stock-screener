---
source_id: MT009
title: "AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419"
date: 2026-09-29
channel: "Top Traders Unplugged"
url: 
words: 11744
claims: 60
added_by_crosscheck: 6
corrections: 2
crosscheck: "opus cross-check"
speakers: ["Nick Palus [caption spelling] (guest, quantitative strategies researcher, Goldman Sachs)", "Alan Dunne (guest host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419

**Speakers:** Nick Palus [caption spelling] (guest, quantitative strategies researcher, Goldman Sachs); Alan Dunne (guest host, Top Traders Unplugged)

**Summary:** Top Traders Unplugged Ep.419 (Sept 2026): record 2026 trend-following gains from short bonds, a Goldman chart of 45% negative-beta S&P stocks, and a review of an Alpha Architect VIX-dependent look-back paper that finds no edge over a static 10-month window. Second half reviews Andrew Ang's multi-agent AI asset allocation paper, its look-ahead, reproducibility and monoculture issues.

**Approach:** trend following, volatility scaling, AI agents, portfolio construction, backtest bias

**Cross-check completeness estimate of first read:** 0.90 - thorough first read; missed the front-end interpretation of the yield rise, the consensus-forecast miss, the cross-sectional vs time-series caveat, the trend-timing verdict and the vintage-model fix; one wrong direction (signal strength) and one wrong speaker

## Argument map

**Episode thesis:** Recorded about 24 September 2026 (upload 29 Sep), with Alan Dunne guest-hosting for Niels. Nick Palus argues that markets are hard to read and predict (even the current state), so trend following should be treated as a continuous, volatility-scaled exposure that earns its place in portfolios by being short bonds in a rate sell-off (September 2026: about 80% of gains from fixed-income shorts, SG CTA/Trend about +15.25% YTD), not as something to be conditioned with VIX triggers: an Alpha Architect test finds no real edge over a static 10-month window. Dunne adds that analysts wrongly assume linear fundamentals-to-price links in complex adaptive markets. In the second half they review Andrew Ang's agentic-AI asset allocation architecture, and Palus concludes the idea has value (many portfolio methods, auditability, relaxing human bandwidth) but is undermined for research by look-ahead bias, non-reproducibility and monoculture risk, and that trend followers need no macro agent because the trend signal is itself an implicit regime indicator.

### Nick Palus (Guest; quantitative strategies researcher at Goldman Sachs (index/QIS side: 'designing index products', 'portfolio design'))
Fingerprint: #approach/trend_following #approach/position_sizing_vol_target #approach/regime_detection #approach/research_robustness_overfitting #approach/portfolio_construction_stacking #approach/replication_indexing #approach/diversification_risk_parity #approach/market_internals_leading
_Speaker note: Caption spelling 'Nick Palus' kept (ledger spelling); the name is unverified. He speaks for himself ('we', 'managers we allocate to') but an index/QIS employer is implied only through his remarks about designing index products. Corrections applied: MT009-C04-4 is 'signals strengthened', not 'stayed flat'; MT009-C16-1 (binding constraint is finite human decision bandwidth) is Nick reading Ang's opening, not Alan._

**Worldview premises**
- Even identifying the current market state is difficult, never mind predicting it; consensus forecasts are unreliable (analysts expected central-bank easing in Jan-Feb 2026, yet yields hit multi-year, in places decade, highs by September). _[experience, stated; support: Recalled quote he cannot place; the Jan-Feb 2026 versus September 2026 yield contrast.]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C03-1|C03-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C03-X1|C03-X1]])
- Trend following's value in a multi-asset portfolio is that it deploys the opposite exposure to the core: in a rate sell-off the trend sleeve is short bonds and offsets the long bond core of a 60/40. _[theoretical, stated; support: September 2026 experience: rates were the strongest contributor and about 80% of the month's gains across managers came from fixed-income shorts including the 2-year.]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C03-2|C03-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C03-4|C03-4]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C03-5|C03-5]])
- Contribution to trend returns rotates across sectors over time, which is why diversification across contributors matters: rates did not trend until Q2 2026, currencies lacked trendiness, and 2022 was a rates, dollar and commodity (inflation/geopolitics) year. _[empirical, stated; support: Own allocations' YTD attribution; 2026 is the third best trend year in 15 (with 2014 and 2022).]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C04-1|C04-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C04-2|C04-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C05-1|C05-1]])
- A smooth, low-vol yield rise earns more trend P&L than a choppy one, and when bond volatility stays contained while yields move a lot, volatility-scaled signals strengthen. _[theoretical, stated; support: Observed signal strength in September 2026 (correction applied to the ledger direction).]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C04-4|C04-4]])
- Triggers (e.g., VIX bands for look-back switching) are statistically fragile: they rarely activate, so a handful of episodes drives results; a continuous function has more power and is preferable. _[theoretical, stated; support: Alpha Architect test: high-VIX periods in the nine-year extension were only about three months; no benefit versus a 10-month static window outside 2020-2021; November 2020 vaccine month drove the apparent edge.]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C06-1|C06-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C06-3|C06-3]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-1|C07-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-2|C07-2]])
- The Alpha Architect design is long-only, equal-notional, monthly rebalanced top-1 or top-2 of five ETFs (relative momentum with no volatility scaling), so it does not transfer directly to directional time-series trend following. _[empirical, stated; support: Reading the note's methodology; the note itself discloses small samples.]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C05-3|C05-3]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C06-2|C06-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C06-X1|C06-X1]])
- Volatility belongs in trend portfolios through continuous signal scaling and risk budgeting, not through VIX switching; volatility and correlation spiking together change the capital needed for a vol target, so design should use asset volatilities and the correlation structure rather than the VIX. _[theoretical, stated; support: Own research philosophy ('we scale our signals by volatility'); no data quoted.]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-4|C07-4]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-5|C07-5]])
- Timing trend following with volatility-based regime classification is very hard and unproven; in trendless periods do not over-parameterise the trend model, add complementary strategies that benefit from those regimes. _[experience, stated; support: His 'mantra' of long-term viability; he says he cannot show statistically that regime timing is worth pursuing.]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C08-X1|C08-X1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C08-1|C08-1]])
- Faster models help at turning points, but the open question is whether speed can be deployed dynamically in time to cut exposure; claims of timing indicators must be judged on false positives. _[theoretical, stated; support: Example: picking 3 of 33 turning points tells nothing without the false-positive count.]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C08-3|C08-3]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C09-1|C09-1]])
- Short-lived V-shaped reversals, about one a year for four years (Liberation Day, March 2026), hurt unconstrained trend followers even though recent results were good. _[experience, stated; support: Recollection of the last four years; unclear whether linked to economic or political regime.]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C09-2|C09-2]])
- Equity breadth is deteriorating: about 45% of S&P 500 stocks have negative 3-month beta to the index (just under 20% at the dot-com peak), because AI stocks form a mini-index within a cap-weighted index; this clustering creates dispersion opportunities. _[empirical, stated; support: Goldman Sachs chart (Christian Mulman, caption spelling) reported in the FT; the paper offers little explanation beyond concentration.]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C01-1|C01-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C01-2|C01-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C02-1|C02-1]])
- Agentic AI changes the human into supervisor and fiduciary, and the binding constraint in asset management is the finite bandwidth of human decision makers, which agents relax. _[theoretical, stated; support: Ang's paper (opening paragraph); CIO covering 10-15 departments, analyst covering 10-20 stocks, committees meeting monthly or quarterly.]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C10-1|C10-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C16-1|C16-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C12-2|C12-2]])
- Institutions value trend following because it deploys exposure faster than investment boards can decide, which is a structural advantage in inflation or shock regimes. _[experience, stated; support: A client's explanation of why they held trend in the 2022 inflation regime.]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C16-2|C16-2]])
- LLM-based research suffers from look-ahead bias (knowledge in parameters even if inputs are date-restricted), data-mining through agent votes, non-reproducibility of outputs, and monoculture risk when agents share one model. _[theoretical, stated; support: Disclaimers in Ang's paper plus his own elaboration; no empirical test shown.]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C14-1|C14-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C14-2|C14-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C14-3|C14-3]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C13-4|C13-4]])
- A trend signal is itself an implicit regime indicator and a past-return/volatility-scaled forecast, so a trend follower needs no macro agent and its asset-class forecasts are not comparable to capital-market-assumption forecasts; only the portfolio-construction step (one or two methods today) could benefit from the multi-method agent approach. _[theoretical, stated; support: Mapping the Ang workflow to a trend model step by step.]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C15-1|C15-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C15-2|C15-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C15-3|C15-3]])

**Chain: Global short-end repricing to trend profits to portfolio diversification**
1. Short-end yields reprice sharply from mid-August 2026 (2-year up at least 75bp, globally) → Trend followers, short fixed income, profit in rates (80% of the month's gains): Trend followers were short; rates were the strongest contributor. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C02-2|C02-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C03-2|C03-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C03-4|C03-4]])
2. Yields break out of a 3.5-5% 10-year range after nearly four years of whipsaw → Trend signals strengthen because the move is large relative to contained bond volatility: Vol-scaled signals respond to move size relative to volatility; smooth moves raise P&L. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C04-3|C04-3]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C04-4|C04-4]])
3. Investor swaps part of 60/40 into trend → Net short bonds in the sell-off, offsetting core long bonds: The sleeve takes the opposite exposure to the core. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C03-5|C03-5]])
- Evidence: SG Trend and SG CTA about +3.7% for September to the 23rd and +15.25% YTD; share of attribution from allocated managers.
- Fails when: V-shaped reversals (one a year for four years) and trendless periods (rates did not trend until Q2 2026).

**Chain: Why VIX-conditioned look-backs show no robust edge**
1. Rule: faster window in high VIX, slower in low VIX → Results depend on a few activation periods: High-VIX months in the extension amount to about three months; monthly rebalancing and parameter sensitivity. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C06-1|C06-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C05-2|C05-2]])
2. Long-only equal-notional top-1/top-2 design with no vol scaling → Risk differs hugely across S&P and Treasuries, and relative-momentum results are not time-series trend results: Design choices contaminate comparison. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C06-2|C06-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C06-X1|C06-X1]])
3. Apparent edge in top-1 selection → Traced to November 2020 (vaccine month) and to the 2020-2021 period; after costs, top-two shows no difference: A single month drives the result. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C06-3|C06-3]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-1|C07-1]])
4. Alternative: scale signals continuously by volatility → More statistical power, no triggers: Trigger rules rarely activate. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-2|C07-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-4|C07-4]])
- Evidence: Alpha Architect extension of a 2017 study with nine new years across five ETFs.
- Fails when: He concedes the study has small samples (disclosed) and that short-term momentum is stronger in high realised volatility (Dunne's point), so a faster response can matter if it can be deployed in time.

**Chain: Unclear macro regime to more diversified allocation (reading of the Ang March 2026 example)**
1. Macro agent finds late cycle with stagflation risk (March 2026) with low-confidence regime identification → CIO agent favours cap-weight, vol-target, equal-weight and inverse-variance portfolios that use no return forecasts: Nick's interpretation: when the regime is hard to identify, capital-market assumptions look 'fluffy' and the allocation tilts toward risk-based and heuristic methods. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C12-3|C12-3]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C13-2|C13-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C13-3|C13-3]])
2. Risk-based and heuristic weighting → Final allocation of 44% equities versus a 60/40 benchmark: It is a blend of weighting schemes; the mechanism is not obvious from the paper. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C13-1|C13-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C12-1|C12-1]])
- Evidence: Ang paper example; his own gut interpretation, explicitly labelled as such.
- Fails when: Not tested; he says it is 'my gut feeling' and the paper does not explain the CIO's decision.

**Chain: Why agentic backtests cannot be trusted at face value**
1. A model trained today estimates yesterday → Knowledge of the future is baked into parameters: Look-ahead survives input date restrictions. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C14-1|C14-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C13-4|C13-4]])
2. Agents vote for the better backtest → Data-mining inside the process: Voting rewards the better-looking history. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C14-1|C14-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C11-3|C11-3]])
3. Same prompt gives different answers → No reproducible backtest to represent the methodology: LLM outputs are stochastic. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C14-2|C14-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C17-1|C17-1]])
4. All agents on one LLM → Correlated errors (monoculture): Shared model shares mistakes. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C14-3|C14-3]])
- Evidence: Disclaimers in the Ang paper and his elaboration; Dunne notes vintage-restricted models may be too weak to run the analysis.
- Fails when: Date-vintage models become strong enough to run the analysis (Dunne's fix).

**Decision process**
- [signal] Scale trend signals continuously by volatility (more volatile means weaker signal) rather than switching windows with triggers.. Why: Statistical power; triggers rarely activate. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-4|C07-4]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-2|C07-2]])
- [sizing] Volatility targeting at portfolio level uses both volatility and correlation, not the VIX; each asset has its own volatility.. Why: Correlation spikes change the dollar amount needed for a target. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-5|C07-5]])
- [research] Demand the false-positive count for any timing indicator before accepting it.. Why: Hitting 3 of 33 turning points is not evidence. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C09-1|C09-1]])
- [portfolio] In trendless regimes do not add parameters to the trend model; add complementary strategies that benefit from those regimes.. Why: Long-term viability of the allocation. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C08-1|C08-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C08-X1|C08-X1]])
- [portfolio] When the macro regime is unclear, diversify more and rely less on return-based capital-market assumptions.. Why: Regime estimate may be wrong and loss follows. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C13-2|C13-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C13-3|C13-3]])
- [portfolio] Run about 20 portfolio-construction methods rather than one or two, using agents for scale (heuristic, return-based, risk-based, non-traditional), with an adversarial diversifier that builds the principal component of the others and takes the opposite stance.. Why: Ang design; he sees value for the portfolio-construction step of a trend portfolio. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C10-4|C10-4]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C11-1|C11-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C11-2|C11-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C15-3|C15-3]])
- [research] Agent scoring: 60% peer votes, 40% historical backtest measures (Sharpe, drawdown); human sets the policy statement and receives a CIO board memo with audit trail.. Why: Ang's governable delegation design. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C11-3|C11-3]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C12-2|C12-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C10-1|C10-1]])
- [research] Macro agent classifies regime (expansion, late cycle, recession, recovery) with a confidence measure; asset-class agents give expected return, volatility, confidence and a memo for about 18 assets.. Why: Ang's pipeline; confidence is meant to capture regime-identification risk. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C10-2|C10-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C10-3|C10-3]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C09-3|C09-3]])
- [other] Index-product design faces a higher bar for AI use than coding or backtesting platforms, though auditable natural-language debate helps.. Why: Index products must be rules-based and defensible. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C17-1|C17-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C09-3|C09-3]])

**Evidence style:** Reads papers closely and points to design caveats (long-only, equal notional, small sample), asks for false positives, and prefers stating limits of what can be shown statistically ('I cannot prove'); leans on his managers' attribution data and client anecdotes; gives interpretations labelled as gut feeling.

**Views at the time**
- (2026-09-23/24) September 2026 is a strong trend month driven by short bond positions; 2026 is the third-best trend year in 15; equities flat to slightly negative, commodities mixed.. Reasoning: Managers' attribution: rates doubled their share, commodities and equities second and third. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C03-2|C03-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C03-4|C03-4]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C04-1|C04-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C05-1|C05-1]])
- (2026-09) US equity breadth and correlation have deteriorated (45% negative-beta stocks), implying dispersion rather than index-level moves.. Reasoning: AI mini-index inside the cap-weighted S&P. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C01-1|C01-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C01-2|C01-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C02-1|C02-1]])
- (2026-09) No strong view on why yields are rising; the Jan-Feb 2026 consensus of easing was wrong, and geopolitical tension complicates inflation causality.. Reasoning: Cannot identify the state, let alone predict. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C03-X1|C03-X1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C03-1|C03-1]])
- (2026-09) V-shaped reversals are now recurring, and the latest (March 2026) was less contagious than Liberation Day.. Reasoning: One reversal a year over four years. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C09-2|C09-2]])
- (2026-09) Not changing his trend model on the back of the VIX-look-back note; the benefit of agent-based allocation is real but the research reliability problem is unsolved.. Reasoning: Triggers are statistically weak; LLM backtests are biased and non-reproducible. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-2|C07-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C14-2|C14-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C14-1|C14-1]])

### Alan Dunne (Guest host (sitting in for Niels Kaastrup-Larsen); macro and CTA analyst, hosts an allocator series)
Fingerprint: #approach/macro_fundamental_topdown #approach/positioning_crowding #approach/policy_reaction_central_banks #approach/regime_detection #approach/trend_following #approach/research_robustness_overfitting #approach/behavioral_sentiment
_Speaker note: Ledger spelling 'Alan Dunne' kept (transcript 'Alan Dunn'). He mostly asks questions but states clear views on yields and market complexity, so he is mapped. Dunne's relay of paper content is attributed to the papers._

**Worldview premises**
- Analysts wrongly assume linear and proportionate links from fundamentals to prices; markets are complex adaptive systems where the same change has large or small effects depending on positioning, barriers and hedges. _[theoretical, stated; support: Observation of the heated analyst debate over why yields rose (growth, fiscal, term premium, AI capex, debasement); no data.]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C02-3|C02-3]])
- The September 2026 yield rise was led by a global short-end repricing, which points to higher expected policy rates (stronger growth or a prolonged Iran conflict), not only to the fiscal or debasement concerns that would hit the long end. _[empirical, stated; support: 2-year yields up at least 75bp since mid-August, globally.]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C02-2|C02-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C02-X1|C02-X1]])
- Growth expectations have flipped: the market priced a recession three times since 2022, with the 10-year in a 3.5-5% range since October 2022 whipsawing trend followers, and now the move is accelerating on a stronger growth scenario. _[empirical, stated; support: Yield history recalled.]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C04-3|C04-3]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C04-R1|C04-R1]])
- Some managers trade faster when market volatility is high and slower when low, and short-term momentum is stronger when realised volatility is higher. _[empirical, stated; support: Industry knowledge of manager practice; no data.]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-3|C07-3]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C08-2|C08-2]])
- LLM backtests suffer from look-ahead; restricting to model vintages available at each date helps but older models may be too weak, so results have largely to be taken at face value. _[theoretical, stated; support: Ang paper discussion.]_ ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C13-4|C13-4]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C14-X1|C14-X1]])

**Chain: What the global short-end repricing signals**
1. 2-year yields rise at least 75bp since mid-August worldwide → Market expects higher policy rates on average: A short-end move is a policy-rate expectation move. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C02-2|C02-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C02-X1|C02-X1]])
2. Higher expected policy rates → Stronger growth or a longer Iran conflict, rather than only fiscal or debasement fears: Fiscal credibility worries would show at the long end. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C02-X1|C02-X1]])
3. Analysts seek a single linear cause → They miss that positioning, barriers and hedges amplify or damp the same news: Complex adaptive system. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C02-3|C02-3]])
- Evidence: Yield moves; the range-bound 10-year before the breakout.
- Fails when: Not stated.

**Decision process**
- [research] Check what a paper tests (assets, rebalancing, window) before generalising; asks how a result is robust to design choices and after costs.. Why: Design choices drive results. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C05-2|C05-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-1|C07-1]])
- [signal] Cites that some managers model faster trading in high-volatility regimes and slower in low, and asks whether Palus has looked at it.. Why: Industry practice. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-3|C07-3]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C08-2|C08-2]])

**Evidence style:** Asks probing questions, uses market narrative and statistics from the index data (SG Trend, SG CTA), and highlights the gaps between analyst narratives and market dynamics.

**Views at the time**
- (2026-09-24) SG Trend and SG CTA are each about +3.7% for September to the 23rd and about +15.25% YTD; likely understated by one good day.. Reasoning: Index data to the 23rd. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C03-3|C03-3]])
- (2026-09) The rise in yields reflects a global short-end repricing toward higher policy rates (stronger growth or prolonged Iran conflict), and the market has flipped from recession pricing to growth.. Reasoning: 2-year up 75bp+ since mid-August. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C02-2|C02-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C02-X1|C02-X1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C04-R1|C04-R1]])
- (2026-03 (example run) read in 2026-09) The March 2026 Ang run found late-cycle conditions with stagflation risk, which reflected the energy markets then.. Reasoning: Dunne links the macro agent's output to energy-market conditions. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C12-3|C12-3]])
- (2026-03 (example run) read in 2026-09) The final recommendation was 44% equities against a 60/40 benchmark.. Reasoning: From the paper; he asks what drove the tilt. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C13-1|C13-1]])

### Disagreements
- **Whether volatility conditioning belongs in trend following**: Alan Dunne: Notes that some managers trade faster in high volatility and slower in low, and that short-term momentum is stronger when realised volatility is higher. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-3|C07-3]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C08-2|C08-2]]); Nick Palus: Uses volatility only as continuous signal scaling and risk budgeting; regime timing is unproven, and deploying speed dynamically in time is the open question. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-4|C07-4]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C08-X1|C08-X1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C08-3|C08-3]])
- **How to explain the rise in yields**: Alan Dunne: Analysts disagree heatedly; he thinks the global short-end repricing implies higher expected policy rates, and that linear causal stories ignore positioning and complexity. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C02-3|C02-3]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C02-X1|C02-X1]]); Nick Palus: No strong view; the episode shows how unreliable consensus forecasts are and how hard it is to read the current state. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C03-1|C03-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C03-X1|C03-X1]])
- **How far agentic backtests can be trusted**: Nick Palus: Look-ahead bias, in-process data mining, non-reproducibility and monoculture risk undermine representative backtests, though the architecture still has value. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C14-1|C14-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C14-2|C14-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C14-3|C14-3]]); Alan Dunne: Proposes restricting to older model vintages but concedes they may be too weak, so results must be taken at face value. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C14-X1|C14-X1]])

### Gaps and conflicts
- The 44% equity allocation is attributed by Palus to risk-based and heuristic weighting under an unclear regime, but he says it is his gut feeling and the paper does not show what drove the CIO agent's tilt; this is an interpretation, not a finding. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C13-1|C13-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C13-2|C13-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C13-3|C13-3]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C12-1|C12-1]])
- Palus argues triggers lack statistical power yet reports an apparent edge for one condition that traces to a single month; he does not test continuous scaling versus triggers himself. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-1|C07-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-2|C07-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-4|C07-4]])
- The Alpha Architect note is long-only relative momentum, so using it to discuss directional trend following is a category mismatch (Palus flags this himself). ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C06-X1|C06-X1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C06-2|C06-2]])
- Dunne's contention that analysts assume linear causality is a general complaint without examples tied to specific analysts; the short-end inference (growth or Iran) is a hypothesis. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C02-3|C02-3]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C02-X1|C02-X1]])
- Goldman's negative-beta chart is accompanied by little explanation in the paper; the proposed 'AI mini-index' mechanism and the dispersion/long-correlation implications are unsupported by data in the discussion. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C01-2|C01-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C02-1|C02-1]])
- Claim that agents use a debate/audit trail to be auditable conflicts with the stochastic nature of outputs: auditable reading of a debate does not make it reproducible. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C17-1|C17-1]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C14-2|C14-2]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C12-2|C12-2]])
- Palus's claim that adding trend to a 60/40 helps in rate sell-offs rests on one month of data (and 2022); it does not address periods when bonds and trend lose together. ([[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C03-5|C03-5]], [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C05-1|C05-1]])

### Forward-looking inputs (reader synthesis)
(reader) Palus gives few forward-looking inputs: he says he cannot read or predict the state of the market. Inputs he treats as informative are volatility-scaled trend signal strength (bond move larger than bond volatility), the volatility and correlation structure (for vol targeting), and the macro regime confidence (for diversification). Dunne's input is the short-end of the yield curve as a gauge of expected policy rates, and positioning/barriers/hedges as amplifiers of fundamental news. Horizons are days to months; none are explicit.

### Reader inferences (not stated by the speakers)
- (reader) Palus's stance is epistemic humility: because the current state is hard to identify, he prefers continuous, rules-based exposures and more diversification over discrete regime calls, which also explains why he is sceptical of both VIX triggers and macro agents for trend.
- (reader) His trend-following defence is structural (opposite exposure to the core, speed versus slow boards), not a claim of predictive skill.
- (reader) The two halves are connected by the same theme: where a process adds discretionary or parameter freedom (triggers, agent voting), statistical validation weakens.
- (reader) Dunne's complex-adaptive-system framing implies that forward price effects depend on positioning, which he does not quantify here.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | intro; Goldman chart of negative-beta S&P 500 stocks, AI mini-index |
| C02 | 3 | dispersion, yield debate, linear vs complex market reaction |
| C03 | 5 | point-in-time uncertainty, September 2026 CTA performance, rates and 60/40 |
| C04 | 4 | rate contribution, yield range history, bond signal strength |
| C05 | 3 | equity/commodity months, rate story, Alpha Architect VIX-lookback paper setup |
| C06 | 3 | paper design details and results |
| C07 | 5 | costs, trigger power, vol scaling approach |
| C08 | 3 | regime classification, complementary strategies, speed at turning points |
| C09 | 3 | false positives, V-shapes, intro to Ang agentic AI paper |
| C10 | 4 | agent pipeline: macro agent, asset-class agents, portfolio agents |
| C11 | 3 | portfolio method menu, researcher and adversarial agents, voting and scoring |
| C12 | 3 | CIO agent, five design principles, March 2026 results |
| C13 | 4 | 44% equity allocation, diversify under unclear regime, LLM backtest bias |
| C14 | 3 | look-ahead, non-determinism, monoculture risk |
| C15 | 3 | mapping the agent workflow to trend following |
| C16 | 2 | multiple objectives, human bandwidth, AI-run products |
| C17 | 1 | auditability and outro, disclaimer |

## Claims

### C01
- **Nick Palus (caption spelling)** About 45% of S&P 500 stocks have a negative 3-month beta to the index versus just under 20% at the dot-com peak (Goldman Sachs chart).  #mech/crowding_positioning _(time-bound view)_
  > about half of the stocks in S&P 500 have a negative beta to the index
  indicator: share of S&P 500 stocks with negative 3m beta · asset: equities · horizon: months · conditions: Cap-weighted index with narrow leadership · testable: yes - computable from stock returns · confidence: high
  ^MT009-C01-1
- **Nick Palus (caption spelling)** AI-stock dominance forms a mini-index within the S&P 500 and the rest decouple, which is clustering and concentration.  #mech/crowding_positioning _(time-bound view)_
  > The AI dominance um is effectively building its own kind of mini index within the index and all the rest are becoming less correlated to it
  indicator: S&P 500 concentration · asset: equities · horizon: months · testable: yes · confidence: medium
  ^MT009-C01-2

### C02
- **Nick Palus (caption spelling)** Equity decoupling creates dispersion opportunities and some argue for long-correlation positions.  #mech/crowding_positioning _(time-bound view)_
  > this decoupling in the equity space is creating opportunities for dispersion some people talk about you know going long correlation
  indicator: dispersion / implied correlation · asset: equities · direction: long correlation · horizon: months · testable: partly · confidence: low
  ^MT009-C02-1
- **Alan Dunne** Short-end yields repriced sharply from mid-August 2026 (2-year up at least 75bp), with a global move.  #mech/policy_reaction _(time-bound view)_
  > the 2-year yield has gone up um I know 75 bips or maybe a percent at least 75 pips I would say since the middle of August
  indicator: 2-year yield · asset: rates · horizon: weeks · testable: yes · confidence: high
  ^MT009-C02-2
- **Alan Dunne** Analysts wrongly assume linear cause and effect: the same fundamental change can have a large or small price effect depending on positioning, barriers and hedges, so markets are complex adaptive systems.  #mech/crowding_positioning
  > this kind of tendency amongst analysts to view the fundamentals and then the market reaction as as being very much linear
  indicator: positioning · asset: multi · testable: partly · confidence: medium
  ^MT009-C02-3
- **Alan Dunne** Because the September 2026 yield rise was led by a global short-end repricing, it points to higher expected policy rates from stronger growth or a prolonged Iran conflict, not only to fiscal or debasement concerns that would hit the long end.  #mech/policy_reaction _(added by opus cross-check, time-bound view)_
  > it's as if everybody now has taken a much more bullish view on global growth or else sees you know the conflict in Iran um staying on much longer
  indicator: 2-year yields globally vs long-end yields · asset: rates · direction: short-end yields up · horizon: months · conditions: front-end-led sell-off · testable: partly - decompose curve moves into front-end vs term premium · confidence: low
  ^MT009-C02-X1

### C03
- **Nick Palus (caption spelling)** Even identifying the current market state is difficult, never mind predicting it.  #mech/research_method
  > it is a struggle to understand point in time what is actually happening in the market let alone predicting the markets
  asset: multi · testable: no · confidence: medium
  ^MT009-C03-1
- **Nick Palus (caption spelling)** In September 2026 rates were the strongest trend-following contributor, most programmes short fixed income.  #mech/cycle_persistence _(time-bound view)_
  > rates have been the strongest contributor to trend following strategies
  indicator: trend following sector contribution · asset: rates · direction: short bonds · horizon: weeks · testable: yes · confidence: high
  ^MT009-C03-2
- **Alan Dunne** September 2026 to the 23rd: SG Trend and SG CTA each about +3.7%, and about +15.25% year to date.  #mech/cycle_persistence _(time-bound view)_
  > sochen trend up about 3.7% and sochen CTA index up about 3.7% as well
  indicator: SG Trend, SG CTA · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT009-C03-3
- **Nick Palus (caption spelling)** About 80% of the month's gains across managers came from fixed income shorts, including the long end and 2-year futures.  #mech/cycle_persistence _(time-bound view)_
  > I'd say 80 80% of the cases concentrated in fixed income short positions and at the long end as well
  indicator: trend P&L attribution · asset: rates · direction: short bonds · horizon: weeks · testable: yes · confidence: high
  ^MT009-C03-4
- **Nick Palus (caption spelling)** Adding trend following to a 60/40 portfolio offsets the long bond core with a short bond position in a rate sell-off.  #mech/risk_management
  > if you've got a 60 uh 40 portfolio and you've taken out some of the allocation and added it to trend following that that trend following exposure now is short bonds
  indicator: 60/40 plus trend following · asset: multi · direction: trend is short bonds when yields rise · horizon: months · conditions: Rising-yield regimes · testable: yes · confidence: high
  ^MT009-C03-5
- **Nick Palus** In January-February 2026 the analyst consensus expected central-bank easing and normalisation, yet by September yields reached multi-year (in places decade) highs, showing how unreliable consensus rate forecasts are.  #mech/slow_reaction _(added by opus cross-check, time-bound view)_
  > 6 months back, um analysts were projecting um rate cuts.
  indicator: analyst rate forecasts vs realised yields · asset: rates · horizon: months · testable: yes - consensus forecast errors · confidence: medium
  ^MT009-C03-X1

### C04
- **Nick Palus (caption spelling)** Rates, commodities and equities were equal contributors at the start of the month, but rates doubled their share in September.  #mech/cycle_persistence _(time-bound view)_
  > precisely because rates have doubled their contribution
  indicator: trend sector contribution · asset: rates · horizon: weeks · testable: yes · confidence: high
  ^MT009-C04-1
- **Nick Palus (caption spelling)** Rates did not trend until Q2 2026 and currencies lack trendiness, showing diversification across contributors over time.  #mech/cycle_persistence _(time-bound view)_
  > we hadn't seen actually rates kind of trending
  indicator: trend contribution by asset class · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT009-C04-2
- **Alan Dunne** The US 10-year yield stayed in a 3.5% to 5% range from October 2022, whipsawing trend followers, and then broke out.  #mech/cycle_persistence _(time-bound view)_
  > it had been a three and a half to 5% range since uh you know October 2022
  indicator: US 10-year yield · asset: rates · horizon: years · conditions: Range-bound yields hurt trend followers · testable: yes · confidence: high
  ^MT009-C04-3
- **Nick Palus (caption spelling)** Bond vol stayed contained, so a vol-scaled signal did not strengthen despite the large yield move; smooth moves raise P&L.  #mech/cycle_persistence _(time-bound view)_
  > no strengthening of those of those um of those signals which attest to the point that the the move has been greater than the volatility at which it comes along
  indicator: vol-scaled trend signals · asset: rates · horizon: weeks · conditions: Low-vol trending moves · testable: yes · confidence: medium
  **Correction (cross-check):** Wrong direction: Nick says the volatility-scaled signals did NOT stay flat; they strengthened, because the yield move was larger than the (contained) bond volatility it came with ('no strengthening' is a caption error for 'now strengthening'). → Bond volatility stayed contained while yields rose sharply, so volatility-scaled trend signals strengthened (move larger than its volatility), and a smooth, low-vol move gives larger P&L than a choppy one.
  ^MT009-C04-4
- **Alan Dunne** Since 2022 the market priced a recession about three times, and has now flipped to a much more positive growth scenario, which is accelerating the yield move.  #mech/new _(added by map cross-check, time-bound view)_
  > the market had priced in a recession probably three times since uh 2022 and now has flipped back towards a much more positive economic growth scenario
  indicator: growth expectations implied by yields · asset: rates · horizon: since 2022 · testable: partly - market pricing history · confidence: medium
  ^MT009-C04-R1

### C05
- **Nick Palus (caption spelling)** 2026 and 2022 were strong trend years, 2022 driven by rates, the dollar and commodities (inflation and geopolitics); this is the third best year in 15.  #mech/cycle_persistence _(time-bound view)_
  > 2022, I guess, was a rate story, but it was also a dollar story as well.
  indicator: trend following annual returns · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT009-C05-1
- **Alan Dunne** Alpha Architect note tests faster look-backs in high VIX and slower in low VIX against a static window on five ETFs.  #mech/research_method
  > whether you can enhance a trend system or a momentum model uh by looking at the volatility um environment
  indicator: VIX-dependent lookback window · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT009-C05-2
- **Nick Palus (caption spelling)** The test picks the top one or two of S&P, US ex-S&P, international equities, global IG bonds and T-bills by momentum.  #mech/slow_reaction
  > Either the best or the two best assets out of the five based on their momentum
  indicator: relative momentum, five ETFs · asset: multi · direction: long the top 1-2 by momentum · horizon: months · testable: yes · confidence: high
  ^MT009-C05-3

### C06
- **Nick Palus (caption spelling)** VIX-triggered look-back switches are fragile: high-VIX periods in the nine-year extension amounted to only about three months.  #mech/research_method
  > as soon as you use kind of VIX triggers, everything becomes very parameterized and quite you know sensitive to to the choices you're making
  indicator: VIX triggers · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT009-C06-1
- **Nick Palus (caption spelling)** The design uses equal notional with no volatility scaling, so risk differs hugely between S&P and Treasuries.  #mech/risk_management
  > but $100 in S&P is not uh is much more risky than $100 in treasuries right
  indicator: equal notional vs vol-scaled · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT009-C06-2
- **Nick Palus (caption spelling)** The paper finds no significant benefit from VIX-conditioned look-backs versus a 10-month static window, outside a 2020-2021 period.  #mech/research_method
  > what they find broadly speaking is no significant value above and beyond a 10-month static look back
  indicator: 10-month static vs VIX-dependent lookback · asset: multi · horizon: months · testable: yes - paper result · confidence: high
  ^MT009-C06-3
- **Nick Palus** The Alpha Architect test is long-only relative (cross-sectional) momentum with monthly rebalancing, so its results do not transfer directly to directional time-series trend following, which takes long or short positions on each asset's own trend.  #mech/research_method _(added by opus cross-check)_
  > a certain extent more of a cross-sectional momentum strategy because if you're picking the best, it is not clear that this is a long or a short position.
  indicator: cross-sectional vs time-series momentum · asset: multi · horizon: months · testable: yes - rerun with time-series signals · confidence: medium
  ^MT009-C06-X1

### C07
- **Nick Palus (caption spelling)** After costs, top-two selection shows no difference between dynamic and fixed windows; an apparent edge came from November 2020 (vaccine month).  #mech/research_method
  > when they use the top two there is no significant difference at all versus using the same two but coming from a kind of fixed window
  asset: multi · horizon: months · testable: yes · confidence: high
  ^MT009-C07-1
- **Nick Palus (caption spelling)** Trigger-based rules have low statistical power since they rarely activate; prefer a continuous function.  #mech/research_method
  > Um and triggers themselves um by nature lend themselves to very low statistical power because you need the trigger to be activated
  indicator: trigger rules · asset: multi · testable: yes · confidence: high
  ^MT009-C07-2
- **Alan Dunne** Some managers trade faster when market volatility is high and slower when it is low.  #mech/slow_reaction
  > this idea of trading faster when market vol is higher and slower um when it's
  indicator: volatility-dependent lookback · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT009-C07-3
- **Nick Palus (caption spelling)** Scale trend signals continuously by volatility (more volatile means weaker signal), instead of switching windows with triggers.  #mech/risk_management
  > But instead of us utilizing a different kind of window depending on volatility, we scale our signals by volatility.
  indicator: vol-scaled trend signal · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT009-C07-4
- **Nick Palus (caption spelling)** Volatility and correlation spikes together change the capital required for a vol target, so portfolio design should use both rather than the VIX.  #mech/risk_management
  > not only do you have volatility spikes, but you have correlation spiking, which also has implications on how much dollar is required for a specific volatility target
  indicator: asset volatility and correlation structure · asset: multi · horizon: days · conditions: Coordinated moves · testable: yes · confidence: medium
  ^MT009-C07-5

### C08
- **Nick Palus (caption spelling)** Do not over-parameterise trend following in trendless periods; add complementary strategies that benefit from those regimes.  #mech/risk_management
  > If they do not exist, I'm not going to try to recreate them with a more complicated structure.
  asset: multi · horizon: years · conditions: Trendless markets · testable: partly · confidence: high
  ^MT009-C08-1
- **Alan Dunne** Short-term momentum is stronger when realised volatility is higher.  #mech/slow_reaction
  > short-term managers and short-term momentum, they do tend to be tend to be stronger when you get higher probably higher realized volatility
  indicator: short-term momentum, realised volatility · asset: multi · horizon: weeks · conditions: High realised volatility · testable: yes · confidence: medium
  ^MT009-C08-2
- **Nick Palus (caption spelling)** Faster models help at turning points, but dynamically deploying speed in time to cut exposure is the open question.  #mech/research_method
  > can I deploy that speed dynamically and will it be fast enough to to cut to cut my exposures
  asset: multi · horizon: weeks · testable: partly · confidence: medium
  ^MT009-C08-3
- **Nick Palus** Using volatility to classify regimes where trend reversals are more likely, and so to time trend following, is very hard and he cannot show statistically that it is worth doing.  #mech/research_method _(added by opus cross-check)_
  > I wouldn't necessarily argue that I can I can prove statistically at least using data um that this is um that this is a pursuit worth pursuing
  indicator: volatility-based regime classification for timing trend · asset: multi · testable: yes - out-of-sample trend timing tests · confidence: medium
  ^MT009-C08-X1

### C09
- **Nick Palus (caption spelling)** A timing indicator must be judged on false positives; calling 3 of 33 turning points tells nothing without them.  #mech/research_method
  > tell me your false positives and then we're going to have a conversation
  asset: multi · testable: yes · confidence: high
  ^MT009-C09-1
- **Nick Palus (caption spelling)** One V-shaped reversal a year for four years (Liberation Day, March 2026) hurts unconstrained trend followers, though recent results were good.  #mech/cycle_persistence _(time-bound view)_
  > these are all the vshapes that we have seen basically one per year for the last four years
  indicator: V-shaped drawdown episodes · asset: multi · horizon: years · conditions: V-shaped sell-offs and rebounds · testable: yes · confidence: medium
  ^MT009-C09-2
- **Nick Palus (caption spelling)** Andrew Ang's Old Bridge paper sets out an agentic AI architecture for institutional asset allocation.  #mech/new _(time-bound view)_
  > it basically talks about agentic architecture for asset management
  asset: multi · testable: partly · confidence: medium
  ^MT009-C09-3

### C10
- **Nick Palus (caption spelling)** Agentic AI turns the human into supervisor and fiduciary, with a policy statement defining risk, return and allowed assets.  #mech/new
  > that human in the loop becomes more of a supervisor more of a kind of the fiduciary
  asset: multi · testable: no · confidence: medium
  ^MT009-C10-1
- **Nick Palus (caption spelling)** The macro agent classifies the economic regime (expansion, late cycle, recession, recovery) with a confidence measure for regime identification risk.  #mech/new
  > it's not about identifying a regime, but it's also about producing a an assessment of the identification risk of that regime
  indicator: regime classification confidence · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT009-C10-2
- **Nick Palus (caption spelling)** Asset-class agents give an expected return, volatility, confidence and a memo for each of about 18 assets.  #mech/new
  > come up with an expected return of the asset class of a volatility estimate and some confidence around that
  indicator: capital market assumptions · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT009-C10-3
- **Nick Palus (caption spelling)** Run about 20 portfolio construction methods instead of one or two, using agents for scale.  #mech/new
  > why don't you actually allow the scale that agents can give you to run 20 portfolios
  indicator: portfolio construction methods · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT009-C10-4

### C11
- **Nick Palus (caption spelling)** The method set spans heuristics (equal weight, cap weight, inverse vol), return-based (mean-variance, Black-Litterman), risk-based (risk parity, max diversification, minimum variance) and non-traditional (CVaR, drawdown constraints).  #mech/risk_management
  > some are more risk based the risk parity max diversification minimum v some are as they call them non-traditional like a civar optimization
  indicator: portfolio construction menu · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT009-C11-1
- **Nick Palus (caption spelling)** An adversarial diversifier agent builds the principal component of the other portfolios and takes the opposite stance to find unseen correlation pockets.  #mech/risk_management
  > So this is now an agent that observes the rest and effectively builds a principal component of the rest and tries to do opposite stuff.
  indicator: principal component of portfolios · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT009-C11-2
- **Nick Palus (caption spelling)** Agents are scored 60/40 from peer votes and historical backtest measures (Sharpe, drawdown).  #mech/new
  > those two combined on a 60/40 kind of scaling basis give you the composite score of all the agents
  indicator: peer votes + backtest score · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT009-C11-3

### C12
- **Nick Palus (caption spelling)** In the March 2026 run the CIO agent picked different schemes from the agents' votes, driven by macro uncertainty.  #mech/new _(time-bound view)_
  > So the most popular allocation scheme um in their example is not the most popular in the selection of the CIO
  asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT009-C12-1
- **Nick Palus (caption spelling)** The paper's design: debate and peer review, natural-language audit trail, composable expertise and governable delegation, with human supervision.  #mech/new
  > there's an element of supervision rather than replacement
  asset: multi · testable: no · confidence: medium
  ^MT009-C12-2
- **Alan Dunne** The March 2026 macro agent found late-cycle conditions with stagflation risk.  #mech/new _(time-bound view)_
  > from a macro perspective they concluded it was late cycle with uh some stagflationary risks
  asset: multi · horizon: months · testable: no · confidence: medium
  ^MT009-C12-3

### C13
- **Alan Dunne** The final recommendation was 44% equities against a 60/40 benchmark.  #mech/new _(time-bound view)_
  > they came out at 44% equities
  asset: equities · direction: underweight equities · horizon: months · conditions: Late-cycle, mixed macro signals · testable: no · confidence: medium
  ^MT009-C13-1
- **Nick Palus (caption spelling)** When the macro regime is unclear, diversify more and rely less on return-based capital market assumptions.  #mech/risk_management
  > should we instead be more prone to diversify at the times that we cannot tell how the macro outcome uh is clear
  indicator: regime classification clarity · asset: multi · direction: more diversified · horizon: months · conditions: Unclear macro regime · testable: partly · confidence: medium
  ^MT009-C13-2
- **Nick Palus (caption spelling)** The CIO favoured cap-weight, vol-target, equal-weight and inverse-variance portfolios that use no return forecasts.  #mech/risk_management
  > I should then rather tilt my allocation towards risk oriented and more huristic allocation frameworks rather than trusting the data as much
  indicator: heuristic allocations · asset: multi · horizon: months · conditions: Unclear regime · testable: partly · confidence: low
  ^MT009-C13-3
- **Alan Dunne** LLM backtests suffer from look-ahead knowledge.  #mech/research_method
  > they all currently incorporate information now that they wouldn't have had back running it in real time
  asset: multi · testable: yes · confidence: high
  ^MT009-C13-4

### C14
- **Nick Palus (caption spelling)** Look-ahead bias in LLM research (knowledge in model parameters), plus data-mining as agents vote for the better-performing backtest.  #mech/research_method
  > you're using a model that was built today perhaps to build estimates for yesterday
  asset: multi · testable: yes · confidence: high
  ^MT009-C14-1
- **Nick Palus (caption spelling)** LLM outputs are non-reproducible, which blocks building a representative backtest.  #mech/research_method
  > LLMA models are not deterministic and even with the same model with the same prompt you might end up having a different answer
  asset: multi · testable: yes · confidence: high
  ^MT009-C14-2
- **Nick Palus (caption spelling)** Monoculture risk: agents sharing one LLM share correlated errors.  #mech/crowding_positioning
  > So if all agents follow the same model from one of the big kind of genai kind of companies, you might find yourself being exposed to some correlation in the in the model.
  asset: multi · testable: partly · confidence: medium
  ^MT009-C14-3
- **Alan Dunne** One fix for LLM look-ahead bias is to restrict backtests to model vintages available at each date, but older models may be too weak to run the analysis, so agentic allocation results must largely be taken at face value.  #mech/research_method _(added by opus cross-check)_
  > maybe those ones weren't even computationally strong enough at that time to run these types of analysis
  indicator: point-in-time LLM model vintages · asset: multi · testable: partly - only forward or vintage-model tests · confidence: medium
  ^MT009-C14-X1

### C15
- **Nick Palus (caption spelling)** In a trend model the 'asset class agent' is past return scaled by volatility; confidence is volatility, so trend and capital-market-assumption forecasts are not comparable.  #mech/slow_reaction
  > we say the expected return is our past return maybe scaled by some measure of all or whatever
  indicator: past return vol-scaled · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT009-C15-1
- **Nick Palus (caption spelling)** A trend signal is itself an implicit regime indicator; trend followers need no macro agent.  #mech/slow_reaction
  > the fact that I observe a rise in in in my price is nothing more than an indicator of the regime
  asset: multi · horizon: months · testable: no · confidence: medium
  ^MT009-C15-2
- **Nick Palus (caption spelling)** Trend portfolio construction uses one or two methods, so the multi-method agent approach could add value there.  #mech/risk_management
  > the fourth which is portfolio construction this is the place that typically we go for one or two and that's about it
  indicator: portfolio construction · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT009-C15-3

### C16
- **Alan Dunne** The binding constraint in asset management is human decision bandwidth, which agentic AI relaxes.  #mech/structural_shift
  > it is the finite bandwidth of human decision makers
  asset: multi · testable: no · confidence: medium
  **Correction (cross-check):** Wrong speaker: Nick reads this from the opening of the Ang paper; Alan only raised multiple objectives. → Nick (citing the paper): the binding constraint in asset management is the finite bandwidth of human decision makers, not data or model sophistication, which agentic AI relaxes.
  ^MT009-C16-1
- **Nick Palus (caption spelling)** Institutions value trend following because it deploys exposure faster than investment boards decide.  #mech/slow_reaction
  > we like trend following because it can be opportunistic and deploy the exposures faster than our ability to bring together the investment board
  asset: multi · horizon: months · conditions: Slow institutional decisions · testable: partly · confidence: medium
  ^MT009-C16-2

### C17
- **Nick Palus (caption spelling)** Agents debating in natural language are auditable but stochastic.  #mech/new
  > all becoming much more auditable and tractable. M but that in itself is stochastic.
  asset: multi · testable: no · confidence: medium
  ^MT009-C17-1

