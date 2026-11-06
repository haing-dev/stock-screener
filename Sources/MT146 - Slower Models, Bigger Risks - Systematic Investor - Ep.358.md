---
source_id: MT146
title: "Slower Models, Bigger Risks - Systematic Investor - Ep.358"
date: 2025-07-31
channel: "Top Traders Unplugged"
url: 
words: 13704
claims: 67
added_by_crosscheck: 21
corrections: 3
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Niels Kaastrup-Larsen (host, Top Traders Unplugged)", "Andrew Beer (DBi, replication)", "Tom Roble (author, trend speed paper)"]
tags: [source, layer0]
---
# Slower Models, Bigger Risks - Systematic Investor - Ep.358

**Speakers:** Niels Kaastrup-Larsen (host, Top Traders Unplugged); Andrew Beer (DBi, replication); Tom Roble (author, trend speed paper)

**Summary:** Systematic Investor panel on CTA trend-following speed (CTAs drifted to longer models, with short-term used in stress), replication versus single managers, and the cost of complexity. Beer argues implicit costs (3-5x explicit) and extra esoteric markets add little; Roble defends diversification across markets.

**Approach:** trend following, CTA replication, implementation costs, portfolio construction

**Cross-check completeness estimate of first read:** 0.72 - first reader captured the main theses (speed shift, replication versus single manager, implicit costs, breadth debate) in about 48 of roughly 67 ideas; missed supporting methods (multi-era calibration, PCA checks, reference-price gaming), several counter-arguments by Roble and Niels, allocator-incentive points, and misattributed the closing remarks to the host

## Argument map

**Episode thesis:** Tom Roble's paper finds that CTAs have drifted to slower trend models (the 'speed factor'), that a blend of fast and slow looks like a painful medium-term model, and that even a homogeneous-looking CTA group shows huge dispersion. Andrew Beer uses this to argue that broad top-down replication captures the industry beta more reliably than any single manager and that the 'complexity crisis' (hundreds of esoteric markets) is not paid for once implicit trading costs are counted; Roble defends marginal diversification and Niels Kaastrup-Larsen sides with 'show it in the data'.

### Tom Roble (Guest; author of the paper on CTA trend speed, builds a paper-traded CTA replicator against the SG Trend index; allocator-side research)
Fingerprint: #approach/trend_following #approach/manager_selection_allocation #approach/portfolio_construction_stacking #approach/costs_execution #approach/regime_detection #approach/diversification_risk_parity #approach/research_robustness_overfitting
_Speaker note: Name spelled 'Roble' in captions; role is inferred from the discussion (meets CTAs and multistrats, wrote the paper), not stated._

**Worldview premises**
- CTAs are not one model but a toolbox: they have drifted to longer-term trend models because those performed better, yet keep short-term models they deploy adaptively in stress. _[empirical, stated; support: Correlation heat map of the replicator versus SG Trend over time frames; manager meetings; Q1 2025 evidence that over half of short-term traders were positive while trend was down double digits]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C04-1|C04-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C04-2|C04-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C04-3|C04-3]])
- A blend of long and short trend looks like medium-term, and medium-term can be the worst place: it lacks long-term trend benefits and short-term stress gains. _[empirical, stated; support: Heat maps of returns by speed]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C07-1|C07-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C06-X2|C06-X2]])
- Trend followers using the same techniques produce widely different results because speed, risk allocation, markets, stops and risk-cutting all differ; drawdown shape matters. _[empirical, stated; support: Exhibit 1 dispersion chart for SG CTA index managers]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C05-1|C05-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C05-2|C05-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C07-3|C07-3]])
- Diversification is the only free lunch: single-market trend IR is only 0.3-0.5, so adding uncorrelated markets raises portfolio Sharpe; excluding a market is itself a bet that the chosen markets will do better net of cost. _[theoretical, stated; support: Portfolio theory; success of Man Evolution, Systematica, etc.]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C13-3|C13-3]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C14-1|C14-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C17-2|C17-2]])
- CTAs weigh transaction costs and slippage before adding a market and have become implementation experts, so costly markets are added only if net marginal benefit is positive. _[institutional, stated; support: Manager meetings; futures moving from exotic to mainstream]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C13-X2|C13-X2]])
- Trends have many causes, including inefficiency in thinly traded alternative markets, not only information digestion. _[theoretical, stated; support: Argument only]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C18-2|C18-2]])
- Institutional allocators hold CTAs to diversify equity risk and want risk-mitigating portfolios, not 'crisis alpha' per se. _[institutional, stated; support: Allocator conversations]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C14-X1|C14-X1]])
- Manager outperformance can come from one or two markets, which reverses (cocoa, coffee 2024 then a harder 2025). _[empirical, stated; support: Example of Mulvaney]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C09-3|C09-3]])

**Chain: Why the replicator was too fast and what it implies for CTA speed**
1. Replicator built to maximise correlation with SG Trend (20/120 crossover) → Occasional short-term dislocations in correlation: Model was a medium-term model ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C03-3|C03-3]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C03-4|C03-4]])
2. Slower crossover tested → Higher correlation in dislocations: CTAs drifted to longer horizons where performance was better ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C04-1|C04-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C04-2|C04-2]])
3. Industry mixes long and short models → Blend looks medium-term and is painful as a stand-alone: Neither long-term benefits nor short-term stress gains ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C07-1|C07-1]])
- Evidence: Heat maps of correlation and return by trend speed; Q1 2025 short-term index constituents.
- Fails when: Short-term models only win briefly (host: long-run longer-term models work better).

**Chain: Breadth of markets and net diversification benefit**
1. Single-market trend IR is low (0.3-0.5) → Add many uncorrelated markets: Diversification is the only free lunch ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C13-3|C13-3]])
2. Not adding a market → Implicit assumption that chosen markets will beat it net of cost: Reverse assumption is dangerous ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C14-1|C14-1]])
3. Moving from 15/50 to 150 markets → Material extra diversification (150 to 151 is not): Track records of alternative-market CTAs ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C17-2|C17-2]])
- Evidence: Man Evolution, Systematica records; concedes they are now working poorly.
- Fails when: Edges decay as capital arrives (Beer) and costs exceed incremental return.

**Decision process**
- [research] Build a transparent bottom-up CTA replicator, optimise for correlation to the SG Trend index (not for performance), and review correlation by horizon with heat maps.. Why: Attribute trend performance and monitor drift in industry speed ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C03-3|C03-3]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C03-4|C03-4]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C04-2|C04-2]])
- [portfolio] Allocators typically start with one CTA, then add several CTAs or non-trend quant strategies to diversify single-manager risk.. Why: Dispersion between managers ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C07-3|C07-3]])
- [universe] Add a market when its marginal diversification outweighs its cost and it is not highly correlated with what is traded.. Why: Diversification benefit versus transaction costs ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C13-3|C13-3]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C13-X2|C13-X2]])

**Evidence style:** Empirical replication and heat maps on SG indices, manager meetings, portfolio theory, and named track records; relies on industry data rather than backtests of own strategy.

**Views at the time**
- (2025-07-31) Macro managers see a very opportunity-rich environment; CTAs benefit if trends emerge across markets in 2H 2025.. Reasoning: Stubborn inflation, relatively high rates, geopolitical dislocations ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C03-2|C03-2]])
- (2025-07-31) Multistrat talent war continues and emerging managers are now typically anchored by large multistrat tickets.. Reasoning: Multistrats see talent as alpha and use SMAs and seeds ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C01-1|C01-1]])
- (2025-07-31) Short-term CTAs showed adaptability in the Q1 2025 tariff shock, when longer-term CTAs were down double digits.. Reasoning: More than half of the short-term traders index constituents were positive ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C04-3|C04-3]])

### Andrew Beer (Guest; runs DBi, a top-down managed futures replication manager (weekly rebalance, about 10 core positions))
Fingerprint: #approach/replication_indexing #approach/costs_execution #approach/trend_following #approach/manager_selection_allocation #approach/research_robustness_overfitting #approach/portfolio_construction_stacking #approach/diversification_risk_parity
_Speaker note: Ledger corrections applied: the cocoa/'no market inherently trends better' remark and the portfolio-Sharpe closing remark (webinar yesterday) are attributed to Beer, not the host._

**Worldview premises**
- Managed futures performance at industry level is driven by a few major themes in the largest, most liquid markets; alpha is detecting information changes early, so the best implementation is in liquid instruments. _[theoretical, stated; support: 2015 bottom-up and top-down analysis; his own replication results]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C09-1|C09-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C09-2|C09-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C17-1|C17-1]])
- Bottom-up replicators calibrated at one date drift as the industry evolves, so top-down adaptive replication keeps correlation in the 80s-90s. _[empirical, stated; support: Redoing the model-selection exercise as of 2012, 2009, 2006 gave different answers; Mount Lucas index example]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C06-1|C06-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C06-2|C06-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C06-X1|C06-X1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C05-3|C05-3]])
- Bottom-up CTA models add model risk through the many parameters, so inferences from them are noisy; single-manager risk is large and breaks allocator capital-market assumptions. _[empirical, stated; support: 30-point gap between best and worst funds in H1 2025; manager-specific choices on equities and FX]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C07-2|C07-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C08-1|C08-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C08-X1|C08-X1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C08-X2|C08-X2]])
- Replicating a pool of funds reduces single-manager risk (correlations about 90% versus mid-80s for single managers) and is the cheapest way to hold the industry beta. _[empirical, stated; support: Own long-term correlations; 9 years above the index]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C08-2|C08-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C10-1|C10-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C11-2|C11-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C09-R1|C09-R1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C10-R1|C10-R1]])
- Implicit trading costs (market impact) are much larger than commonly believed: all-in about 200bp for a typical CTA, implicit costs about 3-5 times explicit, and complexity adds more. _[empirical, stated; support: BestEx analysis of every trade since 2019; UCITS reporting rules (TransTrend paper) allow zero reported costs]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C13-1|C13-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C15-2|C15-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C16-2|C16-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C16-X1|C16-X1]])
- A complexity crisis: firms add non-core markets as a badge of honour and as a response to cheap replication and QIS products, and the extra markets do not cover their costs. _[empirical, stated; support: Hypothetical market 193 versus market 14 arithmetic (illustrative); simple managed futures ETFs beat complex funds in 2025]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C13-2|C13-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C13-X1|C13-X1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C15-1|C15-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C19-1|C19-1]])
- Esoteric-market edges decay as capital arrives (power markets 2004 to 2007), so past excess returns may no longer justify costs. _[experience, stated; support: Own experience founding a commodity firm]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C17-3|C17-3]])
- Incentives drive the push to complexity and the lack of allocator scrutiny. _[behavioural, stated; support: Anecdote of lost mandates; talking to people who declined to do it]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C18-1|C18-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C15-X2|C15-X2]])
- Trend following delivers when other strategies do not; Sharpe is a portfolio measure, and trend raises the Sharpe of stock-bond portfolios with the most diversification per unit. _[theoretical, stated; support: Portfolio argument]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C19-3|C19-3]])
- No market inherently trends better; it depends on the time frame (cocoa went from worst to a top market in three years). _[empirical, stated; support: Cocoa anecdote; remark by a large alternative-market manager]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C19-2|C19-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C17-X2|C17-X2]])

**Chain: Why more markets can lower net returns**
1. Low-cost replication and QIS products compete → Firms add non-core markets as a differentiator: Business incentive, marketing ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C13-X1|C13-X1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C15-X1|C15-X1]])
2. More markets traded at scale → Higher implicit costs (3-5 times explicit costs): Ripple effects of large trades ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C15-2|C15-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C13-2|C13-2]])
3. Costs exceed incremental return → Simple replication does better after fees: Complex strategies should beat simple ones but have not in 2025 ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C15-1|C15-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C19-1|C19-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C20-1|C20-1]])
- Evidence: Illustrative cost arithmetic (hypothetical 400bp vs 1000bp), 2025 ETFs versus mutual funds and hedge funds, absence of evidence from managers.
- Fails when: Edge persists in new markets, costs are lower than assumed, or the underperformance is 2025 luck.

**Chain: Why top-down replication stays correlated**
1. Industry mix of speeds changes over time → Bottom-up fixed-parameter replicators decorrelate: Calibration is date-specific ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C06-X1|C06-X1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C06-1|C06-1]])
2. Top-down method fitted to the industry returns with constant adaptation → Correlations stay in the 80s-90s and misses self-correct in weeks: Self-adaptive process ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C06-2|C06-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C11-2|C11-2]])
- Evidence: Own correlation history; PCA checks against bottom-up models.
- Fails when: Assets for the major themes are unavailable or the industry becomes fully short-term; correlation breaks down in volatile markets.

**Decision process**
- [signal] Top-down replication of the industry using about 10 core positions, rebalanced weekly; the pre-implementation-cost return is the target.. Why: Capture industry beta in the most liquid instruments at low cost ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C05-3|C05-3]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C09-R1|C09-R1]])
- [universe] Trade only about 10 of the most liquid futures; consider reading signals from ~150 markets and implementing in ~15 liquid positions.. Why: Implicit costs dominate when the underlying signal Sharpe is low ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C17-X1|C17-X1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C17-1|C17-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C15-2|C15-2]])
- [execution] Benchmark every trade against arrival price with an algorithmic execution firm.. Why: Nickels and dimes matter on a low-Sharpe signal ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C15-2|C15-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C17-1|C17-1]])
- [research] Monitor tracking by running many bottom-up trend models and applying the same PCA to confirm the replicator picks up the main themes.. Why: Check coverage of themes while accepting divergence ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C10-X1|C10-X1]])
- [portfolio] Allocators should use an investable replication-based index to build capital-market assumptions and benchmark managers; the replicator then has no tracking error to it.. Why: Hedge fund indices are net of fees and not investable ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C10-2|C10-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C11-X1|C11-X1]])
- [other] Allocators should ask managers to state implicit costs next to headline fees and justify extra markets; talk to smart people who chose not to do the strategy.. Why: Allocators lack incentive to ask hard questions ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C19-X1|C19-X1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C18-1|C18-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C15-X2|C15-X2]])

**Evidence style:** Replication correlations, his own cost analysis (BestEx), industry statistics from 2025, anecdote and incentive reasoning; uses rhetorical hypotheticals (market 193) and admits 2025 evidence could be luck.

**Views at the time**
- (2025-07-31) Complex alternative-market CTAs and funds with many markets have underperformed simple replication and ETFs in 2025; the space is in a 'complexity crisis'.. Reasoning: Implicit costs of about 3-5 times explicit costs and 400bp-type incremental costs ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C13-2|C13-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C15-1|C15-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C19-1|C19-1]])
- (2025-07-31) Another long winter may come; if so cost efficiency will matter most, though fewer big trends may also be a cause.. Reasoning: The late-2010s winter may have partly reflected industry costs ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C20-1|C20-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C20-X1|C20-X1]])
- (2025-07-31) Trend following remains the best diversifier of stock-bond portfolios.. Reasoning: Delivers when other strategies do not ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C19-3|C19-3]])

### Niels Kaastrup-Larsen (Host; CTA manager, argues for evidence over narrative)
Fingerprint: #approach/trend_following #approach/replication_indexing #approach/research_robustness_overfitting #approach/costs_execution #approach/manager_selection_allocation
_Speaker note: Ledger corrections removed two claims from the host (C19-2, C19-3) and gave them to Beer; the host's own views are in the opening commentary and the challenges._

**Worldview premises**
- Evidence, not narrative: ultra-diversified 300-500 market portfolios have not beaten 70-100 liquid-market portfolios over 10-year or rolling 5-year windows, and managers show only backtests. _[empirical, stated; support: Observation of returns; no manager has produced evidence]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C14-2|C14-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C15-X1|C15-X1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C18-X1|C18-X1]])
- A replicator should be judged against the real index, not an index built from its own model. _[theoretical, stated; support: Argument; calls own-model benchmark 'cheating' though good marketing]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C11-1|C11-1]])
- Execution should aim at the price used in the backtest (we trade what we test); slippage against a chosen reference price is partly random. _[experience, stated; support: Own practice]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C16-1|C16-1]])
- Trend following is not as poor as claimed over the long run, and weak starts have precedents. _[empirical, stated; support: SG Trend 10-year rolling return stats; Aspect Capital paper]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C12-1|C12-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C12-X1|C12-X1]])
- Short-term models beat longer-term ones only briefly; the middle may be the weak spot. _[empirical, stated; support: Index data and Roble's heat maps]_ ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C06-X2|C06-X2]])

**Decision process**
- [execution] Fill at the same reference price (open or close) as the backtest; do not obsess over intraday slippage.. Why: We trade what we test and test what we trade ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C16-1|C16-1]])

**Evidence style:** Index return data and rolling statistics, personal track-record experience, and challenges to guests' claims (marketing versus data).

**Views at the time**
- (2025-07-31) Trend barometer at 52 (strong) fits a decent July for CTAs; CTA indices still down YTD (SG CTA -6.64%, SG Trend -8.92%, short-term -4.23%).. Reasoning: Metals and equities strong; daily CTA gains ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C02-2|C02-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C03-1|C03-1]])
- (2025-07-31) Chinese outbound investment is rising while the West turns protectionist; copycat Bitcoin 'yield' companies look like a late-cycle product.. Reasoning: Divergent trade regimes; paying twice the price for leveraged Bitcoin exposure ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C02-1|C02-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C02-X1|C02-X1]])

### Disagreements
- **Are more (esoteric) markets worth it for a trend follower?**: Tom Roble: Diversification is the only free lunch; moving from 15-50 to 150 markets adds material diversification; CTAs weigh costs before adding markets ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C13-3|C13-3]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C17-2|C17-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C13-X2|C13-X2]]); Andrew Beer: Implicit costs of 3-5 times explicit costs mean extra markets do not pay; complexity crisis ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C13-2|C13-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C15-2|C15-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C19-1|C19-1]]); Niels Kaastrup-Larsen: The data over 10 years does not show benefits from 300-500 markets; the claim is partly marketing ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C14-2|C14-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C15-X1|C15-X1]])
- **Tracking error benchmark for a replicator**: Andrew Beer: Hedge fund indices are net of fees and not investable; benchmark against a replication-based index with no tracking error ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C10-2|C10-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C11-X1|C11-X1]]); Niels Kaastrup-Larsen: Tracking error must be measured against the CTA index, not a self-built model ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C11-1|C11-1]])
- **Does execution slippage versus a reference price matter?**: Andrew Beer: Implicit costs are large and should be measured honestly; reported figures can be gamed ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C15-2|C15-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C16-2|C16-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C16-X1|C16-X1]]); Niels Kaastrup-Larsen: Slippage versus a chosen reference price is random; target the backtest price and expect little annual slippage from good managers ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C16-1|C16-1]])
- **Is replication a way to get the beta or a self-referential benchmark?**: Andrew Beer: Replication gives broad industry exposure with lower single-manager risk, correlation about 90% ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C08-2|C08-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C10-1|C10-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C11-2|C11-2]]); Tom Roble: Bottom-up replicators like his own are useful for attribution but there is large dispersion among managers ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C05-1|C05-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C07-3|C07-3]])
- **Source of trends in alternative markets**: Tom Roble: Thin-market inefficiencies can create persistent trends ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C18-2|C18-2]]); Andrew Beer: Quants find no statistical evidence that alternative markets trend more; no market inherently trends better ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C18-1|C18-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C19-2|C19-2]])

### Gaps and conflicts
- Beer's 400bp / 1000bp / 600bp numbers are a hypothetical rhetorical question, not measured estimates (ledger correction applied). ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C13-2|C13-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C17-3|C17-3]])
- Speaker attribution of the closing remarks (cocoa worst-to-best, trend Sharpe at portfolio level) is corrected to Beer by the ledger; captions are ambiguous. ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C19-2|C19-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C19-3|C19-3]])
- Beer's own replication is compared with a SocGen index built from the same model, which the host calls circular; no independent tracking-error figure is given. ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C10-2|C10-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C11-1|C11-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C11-2|C11-2]])
- The 2025 evidence (simple ETFs beating complex funds) is a single short episode, admitted as possibly luck. ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C15-1|C15-1]])
- Host's claim that no manager has shown evidence for ultra-diversification conflicts with Roble's cited track records of Man Evolution and Systematica, which Beer says are now working badly. ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C14-2|C14-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C17-2|C17-2]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C17-3|C17-3]])
- Reported 10-year rolling index statistics were calculated by the host on air and flagged as possibly wrong. ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C12-1|C12-1]])
- Replicator correlation stays 'in the 80s-90s' but reference to the true industry benchmark (pre- or post-cost) is mixed, so correlation numbers are not strictly comparable between single managers and replicators. ([[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C06-1|C06-1]], [[MT146 - Slower Models, Bigger Risks - Systematic Investor - Ep.358#^MT146-C08-2|C08-2]])

### Forward-looking inputs (reader synthesis)
(reader) Roble: stubborn inflation, high rates and geopolitical dislocation as inputs for a rich trend/macro environment in 2H 2025; short-term model performance as an indicator of stress regimes. Beer: implicit-cost drag and the mix of trend speeds in the industry; whether complex funds beat replication over the next 3 to 5 years. Host: trend barometer reading and SG Trend 10-year rolling returns. No quantitative forecast is given; horizons are 3 to 5 years for the breadth debate.

### Reader inferences (not stated by the speakers)
- (reader) Roble and Beer agree on the empirical drift to longer-term trend but draw different conclusions: Roble that CTAs adaptively keep short-term tools, Beer that the answer is not to fit a speed at all.
- (reader) The cost-versus-breadth debate cannot be settled without disclosed net-of-implicit-cost returns by market bucket; neither side supplies them.
- (reader) Beer's business interest (replication fund) aligns with his complexity-crisis thesis; Roble's allocator-advisory role aligns with the multi-manager framing; each speaker's evidence should be read with that in mind.
- (reader) The warning against the medium-term speed is consistent with the finding that CTAs mix speeds, but no out-of-sample test of a pure long-term versus medium-term model is shown.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro, multistrat talent war |
| C02 | 2 | fee reduction anecdote, China, bitcoin yield companies, CTA performance numbers |
| C03 | 4 | markets data, macro environment, paper origins, 20/120 model |
| C04 | 3 | speed factor, longer models, short-term CTAs in Q1 2025 |
| C05 | 3 | dispersion, drawdown shape, replication speed |
| C06 | 2 | bottom-up vs top-down replication, medium-term models |
| C07 | 3 | medium-term painful, model risk, dispersion |
| C08 | 2 | dispersion drivers, manager choice, single-manager risk |
| C09 | 3 | replication correlation, major themes, Mulvaney |
| C10 | 2 | beta, allocator structure, tracking error |
| C11 | 2 | replication index, tracking error debate |
| C12 | 1 | trend 10-year rolling returns, implicit costs introduction |
| C13 | 3 | implicit costs, complexity crisis, diversification |
| C14 | 2 | adding markets assumption, no evidence in data |
| C15 | 2 | storytelling, simple ETFs, explicit vs implicit costs |
| C16 | 2 | slippage reference price, UCITS cost reporting, signal efficiency |
| C17 | 3 | 150 vs 15 markets, decay of alt-market edge |
| C18 | 2 | incentives, complex products |
| C19 | 3 | costs vs fees, markets trend, portfolio value of trend |
| C20 | 1 | long winter, wrap-up and sign-off (little content) |

## Claims

### C01
- **Tom Roble** Multistrat hedge funds compete for talent via external SMAs and seeding, so large launches are spinouts or multistrat-anchored and an emerging manager now usually starts with a large multistrat ticket.  #mech/structural_shift
  > the largest launches really are almost spinouts in in single managers the largest launches are almost spinouts or multistrat seeds where they are providing capital early stage to to talented individuals
  indicator: hedge fund launches · asset: other · horizon: years · conditions: multistrat talent war · testable: no - industry observation · confidence: medium
  ^MT146-C01-1

### C02
- **Niels Kaastrup-Larsen** While the West turns protectionist, China is increasing outbound investment, a divergent trade/investment regime.  #mech/structural_shift _(time-bound view)_
  > China seems to be going completely in the other direction. They they you know, they're doing more investments this year, I think, abroad than than ever before.
  indicator: China outbound investment · asset: multi · horizon: years · conditions: 2025 tariffs · testable: partly - FDI data · confidence: low
  ^MT146-C02-1
- **Niels Kaastrup-Larsen** His trend barometer reading of 52 (strong) fits a decent July for CTAs, with Btop50 up 1.08% on the day and -2.21% YTD, SG CTA index -6.64% YTD, SG Trend -8.92% YTD and the short-term traders index -4.23% YTD.  #mech/cycle_persistence _(time-bound view)_
  > my own trend barometer finished at 52 two yesterday which is strong.
  indicator: trend barometer, BTOP50, SG CTA, SG Trend, SG Short-Term Traders · asset: multi · direction: CTA performance data points · horizon: days · conditions: July 2025 · testable: yes - index numbers · confidence: high
  ^MT146-C02-2
- **Niels Kaastrup-Larsen** July 2025 observation: copycat Bitcoin 'yield' companies modelled on MicroStrategy sell leveraged Bitcoin exposure at about twice the price of simply holding Bitcoin, yet attract strong demand, which he views sceptically as a late-cycle product.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check, time-bound view)_
  > these Bitcoin quote unquote yield companies that are setting up where they, you know, kind of tried to replicate what what Strategy or Micro Strategy has done
  indicator: Bitcoin treasury company premium to NAV · asset: other · horizon: months · testable: partly - premium to NAV is observable · confidence: low
  ^MT146-C02-X1

### C03
- **Niels Kaastrup-Larsen** Market data points as of late July 2025: MSCI World +12.2% YTD, bonds +3.5% YTD, S&P 500 almost +9% YTD, with metals and equities strong.  #mech/new _(time-bound view)_
  > Msei World up 2.3% as of last night, up 12.2% for the year. The S&P US aggregate bond index down 42 basis points and up three and a half% roughly for the year.
  indicator: MSCI World, S&P 500, US aggregate bonds · asset: multi · horizon: months · conditions: July 2025 · testable: yes - index data · confidence: high
  ^MT146-C03-1
- **Tom Roble** Discretionary macro managers see an opportunity-rich environment because inflation is stubborn, rates are high and geopolitical dislocations are large; CTAs benefit if trends emerge across markets.  #mech/cycle_persistence _(time-bound view)_
  > they think this is one of the most opportunity rich environments for macro trading because of the variety of um themes that are available
  asset: multi · direction: macro and trend opportunity · horizon: months · conditions: 2H 2025 · testable: no - manager sentiment · confidence: medium
  ^MT146-C03-2
- **Tom Roble** They built a paper-traded CTA replicator from the bottom up (market selection plus a moving average crossover model) to attribute trend-following performance.  #mech/research_method
  > we built our own CTA from the bottom up. Um and part of that process is the selection of markets. But the other big part is is the model that you choose.
  indicator: 20/120-day moving average crossover vs SG Trend index · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT146-C03-3
- **Tom Roble** A 20/120-day moving average crossover gave a robust correlation to the SG Trend index, chosen to maximise correlation rather than performance.  #mech/research_method
  > the model set that we chose was a 2120, so a 20-day short fast moving average and 120 days slow moving average
  indicator: 20/120-day MA crossover · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT146-C03-4

### C04
- **Tom Roble** The 20/120 model was too fast: moving to a slower crossover immediately raised correlation to the CTA index during dislocations.  #mech/slow_reaction
  > our model appeared to be a little bit too fast
  indicator: slow moving average length · asset: multi · direction: slower trend models track CTAs better · horizon: months · conditions: recent years · testable: yes · confidence: high
  ^MT146-C04-1
- **Tom Roble** A correlation heat map shows CTAs drifted from medium-term to longer-term models over 15 years because longer horizons performed better (the 'speed factor').  #mech/structural_shift
  > there's been a pronounced shift to them drifting or moving to be employing what appears to be longerterm models
  indicator: correlation of trend indicator at different speeds vs SG Trend · asset: multi · direction: longer-term models outperform · horizon: years · testable: yes - heat map · confidence: high
  ^MT146-C04-2
- **Tom Roble** CTAs run a mix of models and allocate risk adaptively, using short-term models in stress; in Q1 2025 more than half of the short-term traders index constituents were positive while the trend index was down double digits.  #mech/crowding_positioning _(time-bound view)_
  > trend followers have adapted and evolved their model sets but they retain the ability to deploy risk in these shorter term models maybe during a period of um of dislocation or uh market stress
  indicator: SG Short Term Traders Index vs SG Trend · asset: multi · direction: short-term CTAs outperformed in Q1 2025 · horizon: months · conditions: tariff shock · testable: yes · confidence: medium
  ^MT146-C04-3

### C05
- **Tom Roble** Trend followers using the same techniques have large performance dispersion because of model speed, risk allocation, markets, stops and risk-cutting, so drawdown shape matters.  #mech/risk_management
  > the way you think about correlations and risk can really have a very important impact on the returns that you deliver
  indicator: dispersion across SG CTA managers · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT146-C05-1
- **Tom Roble** Drawdown shape matters for risk management; Man Group research finds V-shaped recoveries have become more common after fast risk cutting, but may not persist.  #mech/risk_management
  > man Group have written some really interesting research on on V-shaped recoveries um which seem to have become more prevalent
  indicator: drawdown recovery shape · asset: multi · horizon: months · testable: partly · confidence: low
  ^MT146-C05-2
- **Andrew Beer** DBi's replication rebalances weekly with about 10 core positions, a short horizon bet on accuracy, while the underlying driver it captures is long-term trend.  #mech/research_method
  > we rebalance our portfolios once a week. It's a very short-term bet, right?
  indicator: weekly replication portfolio · asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT146-C05-3

### C06
- **Andrew Beer** Bottom-up CTA replicators calibrated at one time lose correlation as the industry evolves, with widening dispersion; top-down replication stays adaptive with correlations in the 80s-90s.  #mech/research_method
  > the problem with the bottom-up indices is that they're done at a particular moment in time and the industry does evolve and change
  indicator: bottom-up vs top-down replication correlation · asset: multi · horizon: years · testable: yes - rolling correlation · confidence: high
  ^MT146-C06-1
- **Andrew Beer** Replication should not bet on a specific trend speed because the optimal one changes with time; a self-adaptive method is needed.  #mech/research_method
  > we don't want to make a long-term bet on whether people are going to be more on short-term, long-term, medium-term
  indicator: trend speed · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT146-C06-2
- **Andrew Beer** Test of bottom-up trend-model calibration: repeating the model-selection analysis as of 2012, 2009 and 2006 gives different answers about the best speed, so a bottom-up index fitted at one date drifts as the industry evolves (the Mount Lucas managed futures index worked in one period but diverged badly over longer periods).  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > what if we done the same analysis in 2012? What about 2009? What about 2006? Would we have reached the same conclusion?
  indicator: trend model speed chosen by calibration date; Mount Lucas index · asset: multi · horizon: years · conditions: when the industry's model mix shifts over time · testable: yes - rerun calibration at multiple start dates · confidence: high
  ^MT146-C06-X1
- **Niels Kaastrup-Larsen** Short-term trend models beat the trend index only briefly in 2025 and over the long run work less well than long-term models; the medium-term, often assumed to be a happy medium, may actually be the weak spot.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > the the numbers are the numbers and in the long term short term doesn't work as well uh as as longterm
  indicator: short-term traders index versus SG Trend index · asset: multi · direction: favour long-term trend models · horizon: years · conditions: outside short bursts of dislocation · testable: yes - speed-by-speed performance is measurable · confidence: medium
  ^MT146-C06-X2

### C07
- **Tom Roble** A blend of long and short trend looks like medium-term, which can be painful because it lacks long-term benefits and short-term stress gains: the middle is neither one nor the other.  #mech/research_method
  > the danger you fall into is that looks like on average the blend of long and short-term looks like medium-term and medium-term isn't maybe what you were trying to achieve
  indicator: medium-term trend model returns · asset: multi · direction: medium-term underperforms · horizon: years · testable: yes - heat map · confidence: medium
  ^MT146-C07-1
- **Andrew Beer** Building bottom-up CTA models adds model risk from the many parameters, so inferences from them carry large noise.  #mech/research_method
  > And what you end up with is instead of single manager risk, you have model
  indicator: model parameter choices · asset: multi · testable: yes · confidence: high
  ^MT146-C07-2
- **Tom Roble** Even among the 20 SG CTA index managers dispersion is large in almost every year, so allocators diversify across several CTAs.  #mech/risk_management
  > There's a huge amount of performance dispersion in almost every single year.
  indicator: SG CTA index dispersion · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT146-C07-3

### C08
- **Andrew Beer** There was a 30-point gap between best and worst funds in H1 2025, driven for example by avoiding equities (good in 2022) or currencies (good this year).  #mech/risk_management _(time-bound view)_
  > not an accident that there are 30 there's a 30 point difference between the best funds and the worst funds this year
  indicator: fund return dispersion · asset: multi · horizon: months · conditions: 2025 · testable: yes · confidence: medium
  ^MT146-C08-1
- **Andrew Beer** Replicating a pool of funds reduces single-manager risk, with correlations around 90% versus mid-80s for individual managers.  #mech/risk_management
  > we're by targeting a large pool of funds, right? Whether it's the stock CTA index, whether it's the um a pool of mutual funds, a pool of usage funds, etc.
  indicator: replication correlation · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT146-C08-2
- **Andrew Beer** Allocators plug SG CTA index data into capital market assumptions and value predictability, so a single manager 20 points off the index breaks the portfolio analysis; this single-manager risk is why they either diversify across managers, use a multi-manager platform, or use broad replication.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > which is the industry standard and use that plugged it into all sorts of capital market assumptions. So that whole analysis doesn't work if you then pick one guy who's 20 points off everybody else over the next two years
  indicator: SG CTA index as asset-class assumption · asset: multi · horizon: years · conditions: allocators building a defined managed-futures category · testable: partly - tracking dispersion versus the index is measurable · confidence: high
  ^MT146-C08-X1
- **Andrew Beer** Behavioural bias in a multi-manager CTA line-up: allocators spotlight the manager who is doing well rather than the one lagging, which hides dispersion costs.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > If one of your guys is not doing well, but another guy is doing well, you spend a lot of time shining a light on the guy who's doing well
  asset: multi · conditions: multiple CTA managers with divergent results · testable: no - anecdotal · confidence: medium
  ^MT146-C08-X2

### C09
- **Andrew Beer** At industry level performance is driven by major themes (e.g. inflation) in the largest, most liquid markets, so trades in heating oil or small markets matter little.  #mech/structural_shift
  > the only thing that matters in this space are major themes and at an industry at an industry level
  indicator: major market themes · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT146-C09-1
- **Andrew Beer** The alpha in managed futures is detecting information changes early, best implemented in the largest liquid instruments.  #mech/slow_reaction
  > the alpha generation in this space is detecting changes in information early so you can put on contrarian trades that typical allocators are not capitalizing on
  asset: multi · testable: partly · confidence: medium
  ^MT146-C09-2
- **Tom Roble** Manager outperformance often comes from one or two markets (e.g. Mulvaney in cocoa and coffee in 2024), which fell back in 2025, so concentrated-market bets are volatile.  #mech/crowding_positioning _(time-bound view)_
  > some of the best managers in recent years it's been down to one or two markets right that they got right
  indicator: soft commodities trend · asset: commodities · direction: outsized gains followed by tougher year · horizon: years · testable: no - anecdote · confidence: medium
  ^MT146-C09-3
- **Andrew Beer** Because the replication targets pre-implementation-cost returns while reported CTA indices and mutual funds are net of fees and costs, the replicator's measured tracking error to them is higher by construction.  #mech/new _(added by map cross-check)_
  > will actually increase our tracking error relative to the reported ind indices or reported mutual funds
  indicator: tracking error versus SG CTA index · asset: managed futures · direction: none · conditions: Replication aimed at pre-cost returns · testable: yes - compare gross and net returns to indices · confidence: medium
  ^MT146-C09-R1

### C10
- **Andrew Beer** Broad-based, low-cost beta exposure is useful for allocators who cannot do multi-manager due diligence, whereas pension allocators prefer picking four managers.  #mech/research_method
  > buying something that that that gives you broad-based industry exposure as efficiently as you can is really valuable
  asset: multi · testable: no - industry structure · confidence: medium
  ^MT146-C10-1
- **Andrew Beer** Comparing a replication product to a hedge fund index is apples to oranges since the index is net of fees but not investable; a replication-based index has no tracking error to its own product.  #mech/research_method
  > you're comparing something that is um you know has a completely different fee structure, completely different level of implementation cost relative
  indicator: tracking error vs benchmark · asset: multi · testable: yes · confidence: high
  ^MT146-C10-2
- **Andrew Beer** Replication monitoring: run many bottom-up trend models and apply the same PCA to them to confirm that the top-down replication is picking up the main themes, accepting periods of divergence.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > We have lots of bottom-up models that we run where we can essentially do the same kind of PCA analysis on those models to determine whether we're picking up on the major themes
  indicator: PCA of replication positions versus bottom-up models · asset: multi · testable: yes - PCA loading comparison · confidence: high
  ^MT146-C10-X1
- **Andrew Beer** An allocator picking a handful of managers is trying to reconstruct the industry beta, ideally plus about 100bp from manager selection skill.  #mech/new _(added by map cross-check)_
  > ideally it's the index returns plus 100 basis points because you're good at picking those four
  indicator: manager selection alpha · asset: managed futures · direction: none · conditions: Allocators selecting four managers from the SG CTA index · testable: partly · confidence: medium
  ^MT146-C10-R1

### C11
- **Niels Kaastrup-Larsen** Tracking error of a replicator should be measured against the SG CTA index and not against an index built from its own model.  #mech/research_method
  > if you're saying you're going to replicate the CTA index well then the tracking error must be calculated from the CTA index and not from your own model
  indicator: tracking error · asset: multi · testable: yes · confidence: medium
  ^MT146-C11-1
- **Andrew Beer** DBi's replication model self-corrects within weeks if it misses a market theme or an inflection point and has beaten the index 9 years running.  #mech/slow_reaction
  > it's self- adaptive so if we're missing something over you know a week or two weeks or copper is flying and everybody's making a bit of money on copper the the model itself is self- adaptive
  indicator: replication vs SG CTA index · asset: multi · horizon: weeks · testable: yes · confidence: medium
  ^MT146-C11-2
- **Andrew Beer** Benchmark choice follows the user's job: a pension head of CTA allocations uses hedge fund data, whereas a wealth manager wanting efficient exposure should build capital market assumptions and benchmark managers on an investable replication-based index, to which the replicator has no tracking error.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > someone has given me a hedge fund hammer and I'm going to look for hedge fund nails all day long
  indicator: SG replication-based CTA index versus SG CTA index · asset: multi · conditions: wealth managers versus institutional allocators · testable: no - argument about incentives · confidence: medium
  ^MT146-C11-X1

### C12
- **Niels Kaastrup-Larsen** SG Trend index 10-year rolling returns: max 180%, min +1%, average 60%, now 96%, so trend is not as poor over the long run as commonly claimed.  #mech/cycle_persistence
  > the highest 10-year rolling return of the index uh since inception is 180%. The lowest is actually a positive 1%. Um and the average is 60%. And the current 10-year returns uh is 96%.
  indicator: SG Trend index 10-year rolling return · asset: multi · horizon: years · testable: yes - published index · confidence: high
  ^MT146-C12-1
- **Niels Kaastrup-Larsen** Aspect Capital's paper documents the difficult periods across 25 years of the SG Trend index, evidence that the weak 2025 start is not unprecedented and will not be the last such period.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > aspect capital also had done a paper recently where they provide a lot of details to some of the tricky periods uh throughout those 25 years
  indicator: SG Trend index drawdown history (Aspect paper) · asset: multi · horizon: years · testable: yes - index history is public · confidence: medium
  ^MT146-C12-X1

### C13
- **Andrew Beer** Implicit trading costs (market impact) are far larger than assumed; the all-in implementation cost of a typical CTA is about 200bp, probably more.  #mech/risk_management
  > we've used a round number of maybe 200 basis points of all-in costs across the industry as as as the implementation costs associated with a typical um CTA
  indicator: implementation cost · asset: multi · direction: costs reduce net returns · horizon: years · testable: partly · confidence: medium
  ^MT146-C13-1
- **Andrew Beer** Adding esoteric markets can add about 400bp of implicit costs, so a CTA must expect much higher trending in market 193 versus market 14 to net positive; he calls this a complexity crisis.  #mech/risk_management
  > do you really think market 193 trends so much more than market 14
  indicator: number of markets traded · asset: multi · direction: simple CTAs do better · horizon: years · testable: partly - compare net returns of simple vs complex funds · confidence: medium
  **Correction (cross-check):** Numbers are illustrative, not estimates: Beer poses 400bp of incremental implicit cost and 1000bp of extra return (net 600bp) as a hypothetical rhetorical question about market 193 versus market 14. → Hypothetically, if adding a marginal esoteric market costs about 400bp in implicit trading costs, would it really trend enough to add 1000bp (net 600bp)? Beer calls the resulting overcomplexity a complexity crisis.
  ^MT146-C13-2
- **Tom Roble** A single market trend strategy has an IR of 0.3-0.5, but diversification is the only free lunch, so adding markets raises portfolio Sharpe if not highly correlated.  #mech/research_method
  > a single market with a trend following strategy has an information ratio of maybe.5 point 4.3 maybe even lower
  indicator: single-market trend Sharpe · asset: multi · direction: add uncorrelated markets · horizon: years · testable: yes · confidence: medium
  ^MT146-C13-3
- **Andrew Beer** Complexity is partly a business response to cheap replication and QIS products: firms add non-core markets as a badge of honour, which raises implementation cost without clear evidence of benefit.  #mech/new _(added by sonnet-xhigh cross-check)_
  > one of the ways that a lot of firms have responded to threats of lowerc cost products like what we do like the QIS products has I think to introduce more and more complexity into their portfolios
  indicator: number of markets traded; implementation cost · asset: multi · horizon: years · conditions: when low-cost competitors appear · testable: partly - market count versus net performance is measurable · confidence: medium
  ^MT146-C13-X1
- **Tom Roble** Counter-argument: CTAs weigh transaction costs and slippage before adding a market, have become implementation experts over 10-15 years, and futures have moved from exotic to mainstream, so costly markets would not be added unless they raise the risk-adjusted return.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > if the transaction costs are too high, I don't believe a CTA would be adding that market to their CTA portfolio
  indicator: transaction cost versus marginal Sharpe of a new market · asset: multi · direction: add markets only when net marginal benefit is positive · horizon: years · conditions: costs are measured honestly · testable: yes - net marginal benefit per added market · confidence: medium
  ^MT146-C13-X2

### C14
- **Tom Roble** Excluding a market assumes the chosen markets will beat it on a cost-adjusted basis; institutional allocators want diversification of equity risk and alternative markets like commodities may help in stress.  #mech/risk_management
  > If you aren't adding that market, it isn't just a decision that you're not adding it. It is an assumption that you're making.
  indicator: market universe · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT146-C14-1
- **Niels Kaastrup-Larsen** Over 10-year and rolling 5-year returns, ultra-diversified 300-500 market portfolios have not beaten 70-100 liquid-market portfolios, and no manager has shown evidence apart from backtests.  #mech/research_method
  > I don't see these uh ultra diversified um portfolios doing better than those who focus on say 70 odd 100 odd markets of the most liquid um and wellestablished futures
  indicator: number of markets traded vs returns · asset: multi · direction: no benefit from more markets · horizon: years · testable: yes - fund return comparison · confidence: high
  ^MT146-C14-2
- **Tom Roble** Institutions diversify equity risk and want risk-mitigating portfolios rather than crisis alpha per se, so the CTA role is to diversify the primary risk asset (equity) across regimes.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > I don't like the term crisis alpha. I know it's a term that get gets used a lot but I think they aren't necessarily looking for crisis alpha but they are looking for the ability to build risk mitigating portfolios
  indicator: CTA return in equity drawdowns · asset: multi · direction: hold CTAs to diversify equity risk · horizon: years · conditions: allocator portfolios dominated by equity risk · testable: yes - conditional correlation and drawdown behaviour · confidence: medium
  ^MT146-C14-X1

### C15
- **Andrew Beer** In 2025 simple managed futures ETFs beat complex mutual funds and hedge funds, perhaps luck but not isolated.  #mech/cycle_persistence _(time-bound view)_
  > the simple managed futures ETFs in the US that are derided for their simplicity are doing meaningfully better than the more complicated mutual funds and doing meaningfully better than hedge funds this year
  indicator: managed futures ETFs vs mutual funds vs hedge funds · asset: multi · direction: simple outperform complex · horizon: months · conditions: 2025 · testable: yes · confidence: medium
  ^MT146-C15-1
- **Andrew Beer** Implicit costs are roughly 3-5 times explicit costs for large players; he benchmarks every trade against arrival price (BestEx).  #mech/risk_management
  > whatever your explicit costs are, it's probably three to five times that when you're getting into implicit costs as you get into as you become a scale player in the space
  indicator: implicit vs explicit costs · asset: multi · conditions: at scale · testable: yes · confidence: medium
  ^MT146-C15-2
- **Niels Kaastrup-Larsen** Trading hundreds of markets is partly marketing: managers are asked how they differ from competitors and market count is an easy answer even though the data does not show a benefit.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > that's the first question we get as a managers. How are you different from all your competitors? So you have to come up with something
  indicator: number of markets traded · asset: multi · horizon: years · conditions: competitive manager selection · testable: partly - claim about motive is untestable, outcome is testable · confidence: medium
  ^MT146-C15-X1
- **Andrew Beer** Allocators have little incentive to question implicit costs and market-count claims because they like the story; examples of it backfiring now prompt soul-searching about what was predictable.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > allocators have not had a strong incentive to ask these questions because they like the story and when people like the story they don't ask hard questions about it
  asset: multi · testable: no - narrative · confidence: medium
  ^MT146-C15-X2

### C16
- **Niels Kaastrup-Larsen** Execution should target the same price (open or close) used in the backtest; slippage versus a chosen reference price is partly random.  #mech/research_method
  > we trade what we test and we test what we trade
  indicator: backtest fill price · asset: multi · testable: yes · confidence: medium
  ^MT146-C16-1
- **Andrew Beer** UCITS rules allow some large CTAs to report zero implementation costs, which is wrong (true cost 80-250bp), per a TransTrend paper.  #mech/risk_management
  > large CTAs out there that in their regulatory filings on their usage funds are showing zero implementation costs
  indicator: reported implementation costs · asset: multi · testable: yes · confidence: high
  ^MT146-C16-2
- **Andrew Beer** Slippage and implementation-cost measures depend on the reference price chosen, so a manager can pick a settlement price that flatters results; reported cost figures need scrutiny.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > you can also pick your settlement price, you can do whatever in a way that that that gains the system in your favor
  indicator: slippage versus reference price · asset: multi · conditions: when costs are self-reported · testable: yes - audit against arrival price · confidence: medium
  ^MT146-C16-X1

### C17
- **Andrew Beer** Trend following has a naturally low Sharpe, so implementation efficiency (trade in liquid instruments) matters greatly.  #mech/risk_management
  > in a space where you have a naturally low sharp ratio for the underlying signal, it's getting that as efficiently as you possibly can where you know nickels and dimes matter
  indicator: trend signal Sharpe · asset: multi · horizon: years · testable: partly · confidence: high
  ^MT146-C17-1
- **Tom Roble** Marginal diversification from 15-50 to 150 markets is material even if 150 to 151 is not; alternative-market CTAs like Man Evolution and Systematica built strong records.  #mech/research_method
  > moving from 15 or 50 to 150 does provide much more marginal diversification
  indicator: number of markets · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT146-C17-2
- **Andrew Beer** Esoteric-market edges decay as more capital enters, as in power markets 2004-07, so the question is whether 1000bp excess return is still worth 500bp of cost in 2025.  #mech/crowding_positioning _(time-bound view)_
  > they worked incredibly well for a period of time and and a lot of them are working terribly right now
  indicator: alternative-market CTA returns · asset: multi · direction: excess return decays · horizon: years · conditions: as more managers enter · testable: partly · confidence: medium
  ^MT146-C17-3
- **Andrew Beer** Design idea: read signals from a broad set (about 150 markets) but implement them through about 15 liquid positions to cut implementation cost while keeping the information.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > maybe you should look at 150 markets and then synthesize that down to 15 liquid positions and implement it at at a much lower cost
  indicator: 150 markets of signal condensed into 15 liquid positions · asset: multi · conditions: when implicit costs dominate · testable: yes - tracking error and cost saving can be backtested · confidence: medium
  ^MT146-C17-X1
- **Andrew Beer** Periods when trends occur cannot be predicted, which is why the breadth-versus-cost trade-off turns on the predictability of trends and should be settled by evidence.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > we'd all agree that it's impossible to predict periods where trends will occur
  asset: multi · testable: no - premise · confidence: high
  ^MT146-C17-X2

### C18
- **Andrew Beer** To judge a space, ask smart people who chose not to do it; quants say alternative markets do not trend more, but incentives (winning mandates) push complexity.  #mech/research_method
  > talk to really smart people who decided not to do it
  asset: multi · testable: no - heuristic · confidence: medium
  ^MT146-C18-1
- **Tom Roble** Trends can come from inefficiency in thin alternative markets as well as from information digestion, so such markets may sustain trends.  #mech/slow_reaction
  > It's not simply a structural price drift as the market digests information. And it can be an inefficiency in for example a a an alternative market which is more thinly traded
  indicator: thinly traded markets · asset: multi · horizon: years · testable: partly · confidence: low
  ^MT146-C18-2
- **Niels Kaastrup-Larsen** Settle the breadth debate with 10-40 years of actual returns rather than narratives; managers in alternative markets may still be worth holding because they are different, not necessarily better.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > let's look at, you know, 10, 15, 20, 30, 40 years of actual returns and and then people can decide what actually has stood out as being both better, more robust, more consistent
  indicator: long-run returns of alt-market CTAs versus liquid-market CTAs · asset: multi · horizon: years · testable: yes - long-run returns comparison · confidence: high
  ^MT146-C18-X1

### C19
- **Andrew Beer** Managers pushed into complexity; five years on they should beat simple replication but have not, implying costs or fees exceed the benefit; multistrats at least are open about 1200bp fee loads for a 2 Sharpe.  #mech/risk_management
  > you're starting with a lower sharp and you've had a push toward more expensive things
  indicator: fund Sharpe vs cost · asset: multi · direction: simple beats complex · horizon: years · testable: partly · confidence: medium
  ^MT146-C19-1
- **Niels Kaastrup-Larsen** No market inherently trends better, e.g. cocoa went from worst to best within three years.  #mech/structural_shift
  > I think we all agree that it's very difficult to say that a market trends better. It just depends on the time frame.
  indicator: cocoa trend · asset: commodities · horizon: years · testable: partly · confidence: medium
  **Correction (cross-check):** Speaker most likely wrong: the 'two final thoughts' passage (alternative markets do not trend better; cocoa worst to best in three years) is the same speaker as the webinar remark, Andrew Beer, not the host; the anecdote about a large alt-market manager is told to Tom, who replies that it could have been said. → Andrew Beer: no market inherently trends better, which depends on the time frame (cocoa went from the worst market three years ago to a top one), echoing a large alt-market manager's remark at a SocGen conference.
  ^MT146-C19-2
- **Niels Kaastrup-Larsen** Sharpe should be judged at portfolio level; trend following raises the Sharpe of stock-bond portfolios, giving the most diversification per unit.  #mech/risk_premium
  > when trend delivers, it is usually when all the other strategies don't. And that has huge value in a portfolio.
  indicator: portfolio Sharpe with trend · asset: multi · direction: trend diversifies stocks and bonds · horizon: years · testable: yes · confidence: high
  **Correction (cross-check):** Wrong speaker: the passage ends 'I basically said all that on the webinar yesterday' (the webinar was Beer's, per C02) and runs straight into Beer's C20 remarks ('we made specific choices'), so it is Andrew Beer, not the host. → Andrew Beer: trend following delivers when other strategies do not, Sharpe is a portfolio measure rather than a single-strategy one, and trend improves the Sharpe of stock-bond portfolios, giving the most diversification per unit.
  ^MT146-C19-3
- **Andrew Beer** Allocators should demand that a manager state implicit trading costs next to the headline fee (for example 1.5% all-in plus about 400bp of costs) and justify why the extra markets are still worth it.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > be aware that we're only charging you, you know, we're charging you a one and a half% all-in fee or something, but be aware there's 400 basis points more of costs, but we still think it's worth it
  indicator: implicit trading cost disclosure · asset: multi · testable: partly - disclosure standards, cost estimates testable · confidence: medium
  ^MT146-C19-X1

### C20
- **Andrew Beer** The late-2010s 'long winter' may be partly due to industry costs, and another may come, when cost efficiency matters most.  #mech/risk_management
  > if you go through a period like the long winter in the late 2010s then how much of that was due to the cost structure of the industry
  indicator: trend returns vs costs · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT146-C20-1
- **Andrew Beer** Alternative explanation for trend 'winters': there may simply be fewer big trends to participate in, so cost efficiency and structure may not be the whole story.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check)_
  > No one cares about them in 2022. And maybe these winters are just a function of the fact that there
  indicator: frequency of big trends · asset: multi · horizon: years · testable: partly - trend frequency versus returns · confidence: low
  ^MT146-C20-X1

