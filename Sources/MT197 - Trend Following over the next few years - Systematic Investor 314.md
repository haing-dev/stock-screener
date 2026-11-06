---
source_id: MT197
title: "Trend Following over the next few years - Systematic Investor 314"
date: 2024-09-27
channel: "Top Traders Unplugged"
url: 
words: 11878
claims: 59
added_by_crosscheck: 13
corrections: 1
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Mark Rzepczynski (host/guest, systematic researcher; caption 'Mark rinsky')", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Trend Following over the next few years - Systematic Investor 314

**Speakers:** Mark Rzepczynski (host/guest, systematic researcher; caption 'Mark rinsky'); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Mark and Niels discuss September 2024 trend-following results, the Fed 50bp cut, post-event behaviour and the KUU framework. Topics: algo aversion, explaining models, market connectedness, adaptive markets, bear-market memory and CTA index replication. Main idea: systematic managers respond to prices after events and stay diversified instead of forecasting.

**Approach:** trend following, carry, macro, manager selection

**Cross-check completeness estimate of first read:** 0.80 - the first reader caught the main frameworks (post-event behaviour, KUU, connectedness, adaptive markets, replicators); missed secondary ideas on Jackson Hole and central bank narratives, passive vs active under KUU, discretionary vs systematic investor bar, spillover decomposition and the 20% correction point.

## Argument map

**Episode thesis:** Mark and Niels argue that systematic investors should not forecast events such as the Fed's surprising 50bp cut but act on post-event price behaviour, and handle the unknown and unknowable with true diversification (about 100 markets, long/short), following models rather than overriding them. They add that algo aversion, poor manager explanations, bear-market amnesia and replicator/index risk shape how trend following is bought and sold, and that connectedness across markets may be exploitable.

### Mark Rzepczynski (Systematic/quant researcher and macro-minded guest co-host (caption 'Mark rinsky'))
Fingerprint: #approach/trend_following #approach/policy_reaction_central_banks #approach/behavioral_sentiment #approach/regime_detection #approach/research_robustness_overfitting #approach/replication_indexing #approach/manager_selection_allocation #approach/diversification_risk_parity
_Speaker note: Caption spells the name 'Mark rinsky'; identified from the ledger header. Turns alternate with Niels and are clear from question/answer structure; one passage (C03 carry-ties-to-society) was misattributed in the ledger and is corrected to Niels._

**Worldview premises**
- Replication, already done for hedge fund and managed futures strategies, is now being tried for private equity, raising many quant and replication problems. _[experience, stated; support: Colleague's (Randy Cohen) research project.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C01-1|C01-1]])
- Trend and carry are uncorrelated and can be blended: carry earns in risk-on, trend in risk-off; the size of carry is highly uncertain and the word covers different things (short-term active carry vs long-term mega carry). _[empirical, stated; support: Industry practice (CTAs blend trend with carry); size estimates from hundreds of billions to trillions.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C03-2|C03-2]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C03-3|C03-3]])
- Systematic managers should not forecast central-bank decisions; what matters is post-event behaviour, i.e. how prices and portfolios adjust after the action. _[theoretical, stated; support: Practitioner stance; notes the sample of past 50bp-cut episodes is too small to study.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C04-4|C04-4]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C05-1|C05-1]])
- Separate three layers of any market event: what I think they should have done, how the market perceives it, and what prices then tell me; only the third drives the trade (continuation, reversal or mean reversion). _[behavioural, stated; support: Personal discipline; no data.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C05-2|C05-2]])
- Uncertainty comes in three kinds (KUU): known (countable), unknown (cannot be handicapped, avoid) and unknowable (diversify and follow prices). _[theoretical, stated; support: Framework attributed to a Wharton group; applied by examples (US election = unknown but resolving; million-job revision = unknowable).]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C07-1|C07-1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C07-2|C07-2]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C07-3|C07-3]])
- Long-only is not enough diversification when stock-bond correlation is positive; long/short across as many asset classes as possible handles unknown and unknowable best. _[empirical, stated; support: Argued from current correlation regime; no numbers.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C08-1|C08-1]])
- Investors suffer algo aversion: they react more slowly to the same information when it comes from an AI/algorithm than from a human, and forgive human managers' excuses but not models. _[behavioural, stated; support: Cites a recent FT-reported study, his own blog from ten years earlier (weather-forecast tests) and meeting experience.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C08-2|C08-2]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C09-2|C09-2]])
- Following the model beats overriding it in a one-off situation, especially in trend following. _[experience, stated; support: Experience; override mechanism exists but should rarely be used.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C10-1|C10-1]])
- Managers explain themselves poorly and investors ask poor questions; the right answer states why and when a model should win or lose, not 'when there are trends' (a tautology). _[experience, stated; support: Observation from manager meetings.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C10-3|C10-3]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C10-X1|C10-X1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C11-X2|C11-X2]])
- Attribution (why money was made, under which conditions) is more informative than contribution (how much per market). _[theoretical, stated; support: None beyond argument.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C12-1|C12-1]])
- Markets form a network: connectedness (clusters, common traders, similar events) drives dynamic correlations and contagion, so diversification should also be designed around network structure. _[theoretical, stated; support: Own current research with Vienna collaborators; no results shown.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C12-2|C12-2]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C14-1|C14-1]])
- Market efficiency is dynamic (adaptive markets hypothesis): it varies by liquidity, valuation difficulty, hedger/speculator mix, participants and cycle, so trends can exist. _[theoretical, stated; support: Andy Lo's AMH; contrasts with Asness's 'social media makes markets less efficient'.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C14-2|C14-2]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C14-3|C14-3]])
- Central bankers lack skin in the game, unlike traders who lose clients when wrong, so their actions can be rash and their memory of bear markets is short. _[experience, stated; support: Taleb-style argument; anecdote of Wall Street careers with no bear market.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C06-1|C06-1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C15-1|C15-1]])
- Modest equity bear markets are over-feared by policymakers: a 20% fall would only give back about 18 months of returns. _[empirical, stated; support: Rough valuation arithmetic, no figures shown.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C15-X1|C15-X1]])
- Most managers underperform their benchmarks, so a median-replication product is not a benchmark and suits only low-cost investors with no manager skill; a diversified selection of CTAs can beat the SG index. _[empirical, stated; support: General industry observation; SG index built from largest managers by AUM, rebalanced yearly.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C16-1|C16-1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C17-2|C17-2]])

**Chain: Fed 50bp cut to portfolio decisions**
1. Fed cut of unexpected size and maximum pre-event uncertainty → Market adjustment across dollar, bonds, equities, oil: Investors adjust portfolios after the event and effects spread to secondary markets ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C04-1|C04-1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C05-1|C05-1]])
2. Post-event price reaction (dollar no new low, long bonds fell) → Information about market perception, not policy intent: Opposite of the usual response suggests long-end investors did not want bonds ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C04-2|C04-2]])
3. Market price reaction → Trade: continuation, reversal or mean reversion: Third layer of the three-way separation ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C05-2|C05-2]])
- Evidence: Single episode (Sept 2024); past 50bp cuts have too few observations.
- Fails when: Small sample; reaction unclear, cuts that signal real stress may behave differently.

**Chain: Connectedness to spillover trading**
1. Clusters, common traders and similar events (connectedness) → Dynamic correlations: Network design of markets ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C12-2|C12-2]])
2. Dynamic correlations → Contagion and delayed spillovers: A Fed move reaches equities and bonds first, then dollar, then oil and commodities after a short delay ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C13-1|C13-1]])
3. Spillover direction (variance decomposition of shocks) → Cross-trend portfolio construction and risk: Causality direction would show where risk and opportunity arise ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C13-X1|C13-X1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C14-1|C14-1]])
- Evidence: Older variance-decomposition literature; not tested by him on air.
- Fails when: Reaction patterns reliable mostly within a sector (Niels's objection).

**Chain: Why trend followers can exist: adaptive efficiency**
1. Efficiency varying with liquidity, valuation difficulty, hedger/speculator mix, participants, cycle → Periods and markets of lower efficiency: Evolutionary view of markets ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C14-2|C14-2]])
2. Lower-efficiency periods → Trends: Trend followers 'really believe' in AMH ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C14-2|C14-2]])
- Evidence: Lo's AMH; Niels recalls Lo saying markets are efficient but not all the time.
- Fails when: Not specified.

**Chain: Bear-market memory to policy reaction**
1. Cohort never lived through a large bear market → Collective belief that policy will always support markets: Poor market memory ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C15-1|C15-1]])
2. That belief → Policy over-reacts to modest declines (e.g. call for a 75bp cut after the August carry unwind): A 20% bear market would only take back about a year and a half of returns ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C15-X1|C15-X1]])
3. Long-history backtests → Systematic managers already have a sell/short plan for equity falls: Models do not depend on lived experience ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C15-2|C15-2]])
- Evidence: Anecdotal (New Yorker cartoon) plus valuation arithmetic.
- Fails when: Passive flows could amplify a sustained fall (Niels).

**Decision process**
- [research] Study past events by what happened after them, not by forecasting the event; accept small samples are a limit.. Why: Systematic managers use post-event behaviour. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C04-4|C04-4]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C05-1|C05-1]])
- [signal] Act on the market's price reaction, not on own opinion of what the central bank should have done.. Why: Third layer of the three-way separation. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C05-2|C05-2]])
- [portfolio] Diversify across dollar, oil, equities, fixed income and long/short to exploit secondary effects without forecasting them.. Why: Handles the unknown and unknowable. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C05-1|C05-1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C07-1|C07-1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C08-1|C08-1]])
- [risk] Increase positions only on the knowable (trend, information edge); stay diversified for the unknown and unknowable.. Why: KUU framework. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C07-1|C07-1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C07-3|C07-3]])
- [execution] Follow the model; keep an override mechanism but expect that overriding in a one-off event usually does worse.. Why: Discipline and keeping backtests meaningful. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C10-1|C10-1]])
- [research] Explain models via attribution and via exogenous, non-price conditions that are necessary or sufficient for trend returns.. Why: Avoids the 'works when there are trends' tautology. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C10-3|C10-3]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C10-X1|C10-X1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C12-1|C12-1]])
- [portfolio] Add cross-correlations and cross-trends from network and variance-decomposition analysis to portfolio construction.. Why: Use connectedness offensively. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C13-1|C13-1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C13-X1|C13-X1]])
- [portfolio] Hold a diversified portfolio of selected CTAs rather than the SG index.. Why: Index is largest-by-AUM, reconstituted yearly, popularity-driven. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C16-1|C16-1]])

**Evidence style:** Reasons from a few cases and first principles (frameworks such as KUU, AMH, network theory, behavioural studies); few numbers of his own, relies on cited academic work and market anecdotes.

**Views at the time**
- (2024-09-27) Macro trends (growth path, rate direction) will drive trend-following performance through the rest of 2024 and early 2025.. Reasoning: Slow growth/no growth question and the direction of interest rates. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C02-3|C02-3]])
- (2024-09-27) The Fed's 50bp cut was odd: maximum uncertainty the day before, bonds sold off, dollar made no new low, nowcast growth about 3%, inflation above target.. Reasoning: Contradicts forward guidance and strong data; labour weakness exists but no recession precipice. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C04-1|C04-1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C04-2|C04-2]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C04-3|C04-3]])
- (2024-09-27) Volatility will rise around the US election date as uncertainty resolves.. Reasoning: Outcome unknown but resolvable. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C07-2|C07-2]])
- (2024-09-27) A sustained equity fall may come for which many participants have no experience.. Reasoning: Collective memory gap and policy dependence. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C15-1|C15-1]])

### Niels Kaastrup-Larsen (Host, Top Traders Unplugged; CTA industry insider)
Fingerprint: #approach/trend_following #approach/carry #approach/policy_reaction_central_banks #approach/behavioral_sentiment #approach/replication_indexing #approach/manager_selection_allocation #approach/research_robustness_overfitting #approach/diversification_risk_parity
_Speaker note: Host of the series; main speaker alongside Mark. The C03 passage on carry feeding through society and on the Fed fostering carry is his._

**Worldview premises**
- Financial engineering can create the perception of liquidity for inherently illiquid assets, which is a risk. _[theoretical, stated; support: General caution, not specific to the project.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C01-2|C01-2]])
- Trend followers react to events only through price data; the new move enters the sample at once but takes time to change the signal. _[institutional, stated; support: How rules-based systems are built.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C05-X1|C05-X1]])
- Prices are the real voting machine; systems do not need to speculate about what the Fed will do. _[theoretical, stated; support: Industry practice.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C05-R1|C05-R1]])
- Carry runs through society and finance, and most investors prefer nothing to happen while earning a little each day, which makes selling trend following hard. _[behavioural, stated; support: Observation from selling trend following.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C03-4|C03-4]])
- Decades of central-bank policy and forward guidance fostered the carry regime. _[empirical, stated; support: Narrative.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C03-5|C03-5]])
- Central bank narratives are self-serving: they ignore the effect of their own extreme policies on inflation, credit tightening with the return of stability and blame exogenous shocks. _[experience, stated; support: Quotes David Dredge's report on Jackson Hole and Bailey (Covid/Ukraine mentioned about 50 times).]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C06-X1|C06-X1]])
- Systematic funds are blamed for losses while discretionary losses are excused as unforeseeable. _[behavioural, stated; support: Own feeling, 'no way of proving this'.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C09-1|C09-1]])
- True diversification (about 100 markets, not 100 stocks) helps against the unknown and unknowable for active and passive alike. _[theoretical, stated; support: Argued in reply to KUU.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C07-4|C07-4]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C07-X1|C07-X1]])
- Rules-based approaches avoid anchoring and follow unprecedented moves (10-year yields below 2%, negative rates), while discretionary managers can anticipate (e.g. regime breaks) if good; combining both might be best. _[behavioural, stated; support: Historical example.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C11-1|C11-1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C11-X1|C11-X1]])
- Detailed parameter questions (20 vs 30 day volatility) do not help investors understand future performance; manager claims on speed and market count need evidence. _[experience, stated; support: Due-diligence experience.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C11-2|C11-2]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C12-X1|C12-X1]])
- Reaction patterns across markets are reliable only within a sector; trend following's strength is not needing to know how things play out. _[experience, stated; support: Judgement; unsure even for gold or oil.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C13-2|C13-2]])
- Markets are efficient but not all the time, so big moves called trends are expected. _[theoretical, stated; support: Reports Andrew Lo's answer in an interview.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C14-R1|C14-R1]])
- Trend turning points show volatility spikes that make trend followers cut risk; passive flows could amplify a sustained fall. _[empirical, stated; support: Experience, no data.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C15-3|C15-3]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C15-4|C15-4]])
- A CTA replicator or investable index is a giant backtest with its own manager risk, not risk-free like a stock index; investors should look for managers that strive to beat the index. _[institutional, stated; support: Cites Transtrend and Michael Green's 'Why bother being better'.]_ ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C16-2|C16-2]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C16-X1|C16-X1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C17-1|C17-1]])

**Chain: Policy pivot and carry unwind**
1. Decades of forward guidance and central-bank policy → Carry regime: Reduced uncertainty rewarded carry ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C03-5|C03-5]])
2. Yen reversal and carry unwind in August 2024 → Losses for trend followers: Reversal against carry-linked positions ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C03-1|C03-1]])
- Evidence: Single month; stated without numbers.
- Fails when: Not specified.

**Chain: Cut size to market read**
1. Equities at all-time highs with low volatility → 50bp cut looks rash: Markets showed no problem ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C06-2|C06-2]])
2. August Jackson Hole signals (Powell pivot to employment) → Cut was foreshadowed in direction: Size was the surprise ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C05-X2|C05-X2]])
- Evidence: David Dredge's report and own market observation.
- Fails when: Not specified.

**Chain: Why rules beat anchoring**
1. Past ranges (yields cannot go below 2%) → Human anchoring: Expectations tied to history ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C11-1|C11-1]])
2. Rules without expectations → Follow the move as long as it lasts: Capture records and extremes ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C11-1|C11-1]])
- Evidence: Example: Treasury 10-year below 2%, negative European rates.
- Fails when: Discretionary anticipation can add value (regime breaks).

**Decision process**
- [execution] Let the models run even if monitoring continues; overriding destroys the usefulness of the backtest.. Why: March 2020 overrides questionable. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C10-2|C10-2]])
- [portfolio] Hold roughly 100 markets for real diversification.. Why: Helps with unknown and unknowable. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C07-4|C07-4]])
- [research] Support claims on trend speed and market count with evidence, not assertion.. Why: Investors' untested beliefs. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C12-X1|C12-X1]])
- [risk] Cut risk when volatility rises around trend turning points.. Why: Typical systematic risk response. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C15-3|C15-3]])
- [research] Do not over-engineer spillover models outside sectors.. Why: Few sectors with high-confidence reaction patterns. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C13-2|C13-2]])
- [portfolio] Treat CTA index replicators as products with manager risk and seek managers who differ from the index.. Why: Replicators are small firms, models can break. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C16-2|C16-2]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C16-X1|C16-X1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C17-1|C17-1]])

**Evidence style:** Track-record and industry observation; quotes other commentators (Dredge, Lo, Green, Transtrend) rather than testing ideas himself.

**Views at the time**
- (2024-09-26) Trend-follower gains in late Sept 2024 came from fixed income and precious metals; sugar and grain counter-trend rallies hurt, coffee helped; trend barometer 45.. Reasoning: Position/price notes; BTOP50 +1.18% Sept, SG CTA +1%, SG Trend +1.42%. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C02-1|C02-1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C02-2|C02-2]])
- (2024-09-27) The Fed's 50bp cut with equities at highs is nearly unprecedented.. Reasoning: Low volatility and uncertainty did not call for a large cut. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C06-2|C06-2]])
- (2024-09-27) Policy pivot was telegraphed by Jackson Hole.. Reasoning: Powell's speech pointed to the employment mandate. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C05-X2|C05-X2]])

### Disagreements
- **Do central-bank reaction patterns and cross-market spillovers support systematic trading?**: Mark Rzepczynski: Spillovers and connectedness can be exploited via cross-correlations and cross-trends. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C13-1|C13-1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C13-X1|C13-X1]]); Niels Kaastrup-Larsen: Reaction patterns are reliable only within a sector; trend following's strength is not needing to know how things play out. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C13-2|C13-2]])
- **What KUU implies for passive vs active**: Mark Rzepczynski: The more is unknown or unknowable, the more sensible passive indexing becomes. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C07-X1|C07-X1]]); Niels Kaastrup-Larsen: The real lesson is true diversification (about 100 markets), which works for both active and passive. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C07-4|C07-4]])
- **Systematic vs discretionary**: Niels Kaastrup-Larsen: Discretionary managers can anticipate regime breaks and a combination might be better; humans are excused more lightly than models. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C11-X1|C11-X1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C09-1|C09-1]]); Mark Rzepczynski: Investors forgive human excuses and distrust models; following the model usually beats overriding. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C09-2|C09-2]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C10-1|C10-1]])

### Gaps and conflicts
- Mark's pivot claim that the 50bp cut signals a major policy reversal is asserted without data; small sample of past 50bp cuts. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C04-1|C04-1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C04-4|C04-4]])
- Network/spillover ideas are described but no results or tests are given; Niels doubts confidence outside sectors. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C12-2|C12-2]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C13-1|C13-1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C13-2|C13-2]])
- Algo-aversion evidence is cited second-hand (FT article, old blog) with no figures. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C08-2|C08-2]])
- Index and replicator claims (SG index beatable, most managers underperform) have no supporting numbers. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C16-1|C16-1]], [[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C17-2|C17-2]])
- Ledger C03-4 was attributed to Mark but the passage is Niels replying; mapped to Niels. ([[MT197 - Trend Following over the next few years - Systematic Investor 314#^MT197-C03-4|C03-4]])

### Forward-looking inputs (reader synthesis)
Observable inputs: macro growth path and rate direction (growth nowcasts, Atlanta Fed GDPNow), post-event price reactions of dollar, long bonds, equities, oil, volatility spikes at turning points, stock-bond correlation, and passive flows; horizon: rest of 2024 to H1 2025 for trend performance, longer for diversification.

### Reader inferences (not stated by the speakers)
- Both speakers' stance is a 'follow prices, don't forecast' epistemology; their disagreements are about how much structure (network spillovers) can be added without becoming a forecast.
- The Fed-cut discussion works as a case study: Mark reads the muted/inverted price reaction as the signal, which a trend follower would only trade as the new data shift the signal.
- Mark's three-layer separation and KUU together imply sizing up only where a measurable edge exists.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | intro; private equity replication |
| C02 | 3 | Waymo aside; trend update, index numbers, macro trends |
| C03 | 5 | carry unwind, trend-carry blend, carry size, Fed and carry |
| C04 | 4 | Fed 50bp cut, uncertainty, bond reaction, post-event behaviour |
| C05 | 2 | post-event approach, three-way separation, Jackson Hole commentary (no extra claim) |
| C06 | 2 | central bank skin in game, cut at all-time highs |
| C07 | 4 | KUU framework, election volatility, diversification |
| C08 | 2 | long-short diversification, algo anxiety study |
| C09 | 2 | blame on systems vs humans, trust in models |
| C10 | 3 | overrides, explaining models, attribution |
| C11 | 2 | investor questions, anchoring, rule-based advantage |
| C12 | 2 | attribution, three Cs connectedness |
| C13 | 2 | market connectedness and spillover exploitation |
| C14 | 3 | clusters, adaptive markets |
| C15 | 4 | bear market memory, turning points, passive flows |
| C16 | 2 | SG index, replicators |
| C17 | 2 | replicator manager risk, median vs benchmark; outro |
| C18 | 0 | outro; nothing actionable |

## Claims

### C01
- **Mark Rzepczynski** Replication, already done for hedge fund strategies including managed futures, is being attempted for private equity indices to create a liquid version of an illiquid asset, which raises many quant and replication problems.  #mech/structural_shift
  > we've had replication for a lot of hedge fund strategies including manage Futures and now people are saying it's like can we do this for private equity
  indicator: private equity index replication · asset: multi · horizon: years · testable: partly - replication tracking error can be measured · confidence: medium
  ^MT197-C01-1
- **Niels Kaastrup-Larsen** Financial engineering can create the perception of liquidity for inherently illiquid assets, which is a risk.  #mech/risk_management
  > Financial Engineers will come in and take something that is definitely IL liquid and by way of matching making it liquid which of course it it isn't
  indicator: liquid alternatives of illiquid assets · asset: multi · testable: no · confidence: medium
  ^MT197-C01-2

### C02
- **Niels Kaastrup-Larsen** In mid/late Sept 2024 trend-follower gains came from fixed income and precious metals, with sugar and grain counter-trend rallies hurting and coffee strength helping.  #mech/slow_reaction _(time-bound view)_
  > most of the performance is coming from sectors like fixed income precious metals
  indicator: sector P&L: fixed income, precious metals, sugar, grains, coffee · asset: commodities · direction: long coffee, long bonds and precious metals profitable · horizon: weeks · conditions: counter-trend rallies in sugar/grains hurt · testable: partly · confidence: medium
  ^MT197-C02-1
- **Niels Kaastrup-Larsen** Niels' trend barometer was 45 (neutral) on 25 Sep 2024; reported index numbers: BTOP50 +1.18% September (+3.92% YTD), SG CTA +1% (+2.42%), SG Trend +1.42% (+2.72%), short-term traders +0.82%, MSCI World +0.77% (+16.42%), S&P 500 +1.16% (~+20%).  #mech/slow_reaction _(time-bound view)_
  > my own Trend barometer yesterday finished at 45 so that's pretty neutral
  indicator: Top Traders trend barometer, BTOP50, SG indices · asset: multi · horizon: months · conditions: Sept 2024 · testable: yes - public index data · confidence: high
  ^MT197-C02-2
- **Mark Rzepczynski** Macro trends (growth path and interest-rate direction) will drive price trends and hence trend-following performance through the rest of 2024 and early 2025.  #mech/cycle_persistence _(time-bound view)_
  > macro Trends macro Trends macro trends that the macro environment
  indicator: macro environment, interest rates · asset: multi · horizon: months · conditions: slow-growth / no-growth and rate direction · testable: partly · confidence: medium
  ^MT197-C02-3

### C03
- **Niels Kaastrup-Larsen** The August 2024 carry unwind (yen reversal) hurt trend followers to some extent.  #mech/crowding_positioning _(time-bound view)_
  > reversals uh led to the uh carry uh onwi
  indicator: yen carry trade unwind · asset: fx · horizon: weeks · conditions: August 2024 BOJ hike · testable: yes · confidence: medium
  ^MT197-C03-1
- **Mark Rzepczynski** Trend and carry are uncorrelated and can be blended; carry does well in risk-on, trend does well in risk-off, which drives their low or negative correlation.  #mech/risk_premium
  > because they're uncorrelated how do you blend the two of those together to come up with a better strategy
  indicator: trend vs carry blend · asset: multi · direction: carry long in risk-on, trend long in risk-off · conditions: regime dependent · testable: yes - blend backtest conditional on risk regime · confidence: medium
  ^MT197-C03-2
- **Mark Rzepczynski** The size of carry as a strategy class is highly uncertain (estimates range from hundreds of billions to trillions) and 'carry' means different things (short-term active carry vs long-term mega carry across countries).  #mech/crowding_positioning
  > there's a tremendous amount of uncertainty surrounding carry because we never really know how large it is
  indicator: carry strategy AUM · asset: multi · testable: partly - data on positioning is limited · confidence: medium
  ^MT197-C03-3
- **Mark Rzepczynski** Investors prefer carry-like payoffs that earn a little each day when nothing happens, making it hard to sell trend following which pays when markets move.  #mech/behavioral
  > most investors prefer nothing happens really or nothing happening and at the same time they can earn a little bit of money every day
  indicator: carry vs trend investor preference · asset: multi · testable: no · confidence: medium
  **Correction (cross-check):** Wrong speaker. The passage begins 'indeed and actually you could say...' and ends 'but what you said about carry also nicely feeds into our first topic', so it is Niels replying to Mark, not Mark. → Niels (replying to Mark) says carry runs through society as a whole and ties to trend following because most investors prefer nothing to happen while earning a little every day, which is the challenge trend followers face in selling a strategy that pays when markets move.
  ^MT197-C03-4
- **Niels Kaastrup-Larsen** Central bank policies over decades fostered the carry regime (forward guidance reducing uncertainty).  #mech/policy_reaction
  > the fed and other central banks have really been responsible for the rise of the carry regime
  indicator: central bank forward guidance and carry · asset: multi · horizon: years · testable: no · confidence: medium
  ^MT197-C03-5

### C04
- **Mark Rzepczynski** The Fed's 50bp cut in Sept 2024 came with maximum market uncertainty (50/50 pricing the day before, versus usual 90-95% certainty), contradicting its forward guidance aim; a 50bp move usually signals a major policy reversal.  #mech/policy_reaction _(time-bound view)_
  > the day before the the Wednesday announcement it was almost a a 5050 chance between there being a 50 basis point and a 25 basis point C
  indicator: fed funds futures pricing before FOMC · asset: rates · horizon: days · testable: yes · confidence: high
  ^MT197-C04-1
- **Mark Rzepczynski** After the 50bp cut the dollar did not set a new low and 10- and 30-year Treasury prices fell, the opposite of the usual response, suggesting long-end investors did not want to hold bonds.  #mech/policy_reaction _(time-bound view)_
  > you look at the 10year and 30-year uh bond prices they actually fell
  indicator: 10y and 30y Treasury yields after cut · asset: rates · direction: long bonds sold · horizon: days · conditions: Sept 2024 · testable: yes · confidence: medium
  ^MT197-C04-2
- **Mark Rzepczynski** Atlanta Fed GDPNow was around 3% for the next quarter, well above Blue Chip consensus, so the Fed's 50bp cut looked odd given strong growth, above-target inflation and no recession precipice.  #mech/policy_reaction _(time-bound view)_
  > the GDP now forecast which is from the Atlanta Fed
  indicator: Atlanta Fed GDPNow vs Blue Chip · asset: rates · horizon: months · conditions: Sept 2024 · testable: yes · confidence: medium
  ^MT197-C04-3
- **Mark Rzepczynski** Systematic managers care about post-event behaviour (what happens after an action) rather than forecasting the event, so past 50bp cut episodes could be studied but the sample is small.  #mech/slow_reaction
  > they're always interested in what we call postevent Behavior we don't care about what the FED may do as a forecast
  indicator: post-event price behaviour · asset: multi · horizon: days · conditions: small sample of 50bp cuts · testable: yes - event study · confidence: high
  ^MT197-C04-4

### C05
- **Mark Rzepczynski** A trend follower does not forecast the Fed but follows portfolio adjustments after the event, and diversification across dollar, oil, equities and fixed income lets him exploit secondary effects across markets.  #mech/slow_reaction
  > I'll take advantage of that adjustment period post event
  indicator: post-event adjustment across markets · asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT197-C05-1
- **Mark Rzepczynski** Separate three things: what I think they should do, how the market perceives it, and what the market's price reaction says; the third drives the trade (continuation, reversal or mean reversion).  #mech/research_method
  > what is the market going to tell me in prices and how do I then exploit that
  indicator: price reaction to events · asset: multi · testable: no - process principle · confidence: high
  ^MT197-C05-2
- **Niels Kaastrup-Larsen** Trend systems react to an event only through the new price data: the post-event move enters the sample at once, but it takes time to change the signal, so adaptation lags the event.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > our systems will automatically take this into account because they're sampling uh you know a new data set that includes the day I the price move
  indicator: trend signal lookback / speed · asset: multi · direction: trend positions adjust after the price move, not before · horizon: days · conditions: lag depends on signal speed · testable: yes - measure signal response time after policy-event price moves · confidence: high
  ^MT197-C05-X1
- **Niels Kaastrup-Larsen** The September 2024 Fed cut was foreshadowed at the August Jackson Hole speeches (Powell: price stability under control, focus turning to the employment leg of the dual mandate), so the policy pivot itself was telegraphed even though the size (25 vs 50bp) was not.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > we know whatever happened this week was probably in the cards uh even when Jackson Hall um was being held in in August
  indicator: Fed communication (Jackson Hole), fed funds · asset: rates · horizon: months · conditions: Fed in an easing pivot · testable: partly - compare Jackson Hole signals with subsequent policy moves · confidence: medium
  ^MT197-C05-X2
- **Niels Kaastrup-Larsen** Trend systems do not forecast the Fed; they react to how markets (the real voting machine) interpret the news.  #mech/new _(added by map cross-check)_
  > we're just going to react to whatever the markets which are again the voting the real voting machine how the market interprets that
  indicator: post-event price reaction · asset: multi · horizon: days · testable: partly - post-event response studies · confidence: medium
  ^MT197-C05-R1

### C06
- **Mark Rzepczynski** Central bankers lack skin in the game, unlike traders who lose clients and assets when they underperform.  #mech/behavioral
  > the central Bankers often don't have skin in the game
  asset: rates · testable: no · confidence: medium
  ^MT197-C06-1
- **Niels Kaastrup-Larsen** A 50bp cut with equities at all-time highs is nearly unprecedented, and with low volatility and low uncertainty the cut looks rash; markets were not signalling a problem.  #mech/policy_reaction _(time-bound view)_
  > how many times has a central bank caught by 50 basis points at the same time as the equity markets being at new all-time highs
  indicator: Fed cut vs equity all-time highs · asset: equities · horizon: months · conditions: Sept 2024 · testable: yes - historical event list · confidence: medium
  ^MT197-C06-2
- **Niels Kaastrup-Larsen** Reading David Dredge: central banks never attribute the later inflation to their own extreme policies (zero rates, QE aimed at generating inflation), credit their latest tightening for restoring price stability, and blame exogenous shocks (Bailey cited Covid/Ukraine about 50 times), so their narratives are self-serving and a weak guide to future policy.  #mech/policy_reaction _(added by sonnet-xhigh cross-check)_
  > extreme policies like Zer QE fate um which were explic itly targeted at generating inflation are never attributed as having a role in the subsequent inflation
  indicator: central bank communication and inflation attribution · asset: rates · testable: no - narrative critique · confidence: medium
  ^MT197-C06-X1

### C07
- **Mark Rzepczynski** The KUU (known, unknown, unknowable) framework: act on what is measurable, avoid what cannot be handicapped, and diversify against the unknowable.  #mech/research_method
  > what is known what is unknown and then what is unknowable
  indicator: KUU framework · asset: multi · direction: tilt towards what is knowable (trends) · testable: no - conceptual · confidence: high
  ^MT197-C07-1
- **Mark Rzepczynski** Volatility rises around known-date events like the US election because uncertainty resolves then; the outcome is unknown but not unknowable.  #mech/seasonality _(time-bound view)_
  > right around that election date you're going to see heightened volatility because that's when uncertainty is going to be resolved
  indicator: US election volatility · asset: equities · direction: volatility up around election · horizon: weeks · conditions: election date · testable: yes - volatility around elections · confidence: medium
  ^MT197-C07-2
- **Mark Rzepczynski** The one-million-job downward employment revision was unknowable, so the response is to follow prices.  #mech/structural_shift _(time-bound view)_
  > the revisions and unemployment that we saw was something that was unknowable
  indicator: employment revisions · asset: multi · testable: no · confidence: medium
  ^MT197-C07-3
- **Niels Kaastrup-Larsen** True diversification (about 100 markets in a trend portfolio rather than 100 stocks) helps against the unknown and unknowable.  #mech/risk_management
  > the one thing that kind of helps on all fronts with this is just being Diversified
  indicator: number of markets in trend portfolio · asset: multi · testable: yes - diversification benefit vs number of markets · confidence: high
  ^MT197-C07-4
- **Mark Rzepczynski** Under the KUU framework, the more of the world one judges to be unknown or unknowable (and managers unable to know more than the market), the more sensible passive indexing is; Niels counters that the real lesson is true diversification (about 100 markets), which works for both active and passive.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > if you fall into the camp that there's a lot more unknowable information and there's a lot more Unknown about the world then you probably want to be more of a passive investor
  asset: multi · direction: passive/index investing when unknowable dominates · horizon: years · conditions: depends on belief about how much is knowable · testable: no - framework · confidence: medium
  ^MT197-C07-X1

### C08
- **Mark Rzepczynski** Long-only is not enough when stock-bond correlation is positive; trend followers who go long and short across asset classes handle the unknown best.  #mech/risk_management
  > the correlation between stocks and bonds is positive well then if you're long then that's not going to Long only that's not going to help you
  indicator: stock-bond correlation · asset: multi · direction: go long and short · conditions: positive stock-bond correlation · testable: yes · confidence: high
  ^MT197-C08-1
- **Mark Rzepczynski** Studies show algo aversion: investors respond slower to information generated by AI/algorithms than to the same information from humans, even if algorithms forecast better.  #mech/behavioral
  > investors were a little bit slower at responding to that new bit of information than if it was generated by a human
  indicator: algo aversion · asset: multi · testable: yes - experimental · confidence: medium
  ^MT197-C08-2

### C09
- **Niels Kaastrup-Larsen** Systematic funds are blamed for losses (the system's fault) whereas discretionary managers' losses are excused as unforeseeable.  #mech/behavioral
  > it's being blamed right but then when I think about this being a human
  asset: multi · testable: no · confidence: medium
  ^MT197-C09-1
- **Mark Rzepczynski** People forgive human managers (who give excuses) but not models, which cannot make excuses, so they do not trust models.  #mech/behavioral
  > as humans we're willing to forgive other humans we're unforgiving with respect to system and and models
  asset: multi · testable: no · confidence: high
  ^MT197-C09-2

### C10
- **Mark Rzepczynski** Following the model is usually better than overriding it in a one-off situation, though a mechanism for override exists.  #mech/risk_management
  > following the models in generally would be better off than actually turning the model off or reversing what the model told you to do
  indicator: model override · asset: multi · testable: yes - compare override vs no override · confidence: medium
  ^MT197-C10-1
- **Niels Kaastrup-Larsen** Several managers overrode models in March 2020 for risk management; a backtest is worth little if you tinker with the model.  #mech/research_method _(time-bound view)_
  > there were quite a few managers who um stepped in
  indicator: model override March 2020 · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT197-C10-2
- **Mark Rzepczynski** Systematic managers explain what they do poorly, and investors ask poor questions; the key is stating when and why a model should do well or poorly, not the tautology 'when there are trends'.  #mech/research_method
  > the number one flaw with systematic and Trend f following managers in general is that managers are not very good about explaining what they do
  asset: multi · testable: no · confidence: medium
  ^MT197-C10-3
- **Mark Rzepczynski** Explaining when trend following works needs fundamental research into exogenous, non-price conditions (macro and environmental factors necessary or sufficient for positive trend returns), which is an open research agenda beyond the tautology 'it does well when there are trends'.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > that still requires a lot of fundamental research to be able to say what are exogenous factors
  indicator: exogenous (non-price) drivers of trend-following returns · asset: multi · testable: yes - regress trend returns on macro and environment variables · confidence: medium
  ^MT197-C10-X1

### C11
- **Niels Kaastrup-Larsen** A rules-based approach avoids anchoring: it follows moves even if unprecedented, e.g. 10-year yields falling below 2% and to negative rates when many believed they could not.  #mech/behavioral
  > we will go with a market move or a trend for as long as it will take us even if it's never taken even even if it's never done this before
  indicator: bond yield trends · asset: rates · horizon: years · testable: partly · confidence: high
  ^MT197-C11-1
- **Niels Kaastrup-Larsen** Detailed parameter questions (20 vs 30 day volatility lookback) do not help investors understand future performance.  #mech/research_method
  > are you using a 20-day or a 30-day uh volatility flaw for example
  indicator: volatility lookback · asset: multi · testable: yes · confidence: medium
  ^MT197-C11-2
- **Niels Kaastrup-Larsen** A discretionary trader can anticipate (e.g. regime breaks) where a rules-based model cannot, which has value if done well, so a combination of systematic and discretionary approaches might be better than either alone.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > the advantage of a discretionary trade of course is that they can anticipate which a model can't do and and if they're very good at that that has value of course
  asset: multi · conditions: only if the discretionary manager is genuinely skilled · testable: partly - blended systematic/discretionary portfolios · confidence: low
  ^MT197-C11-X1
- **Mark Rzepczynski** Investors demand far more detail of systematic managers (lookback, testing, process) than they ever ask of discretionary managers whose decision process is no more transparent, so systematic managers must explain the 'why' not just the parameters.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > the bar that's set by investors is much higher for systematic managers than a discretionary manager
  asset: multi · testable: no · confidence: medium
  ^MT197-C11-X2

### C12
- **Mark Rzepczynski** Attribution (why money was made in crude or bonds, and which conditions allowed it) is more informative than contribution (how much was made per market).  #mech/research_method
  > there's a difference between performance attribution and contribution
  indicator: performance attribution · asset: multi · testable: yes · confidence: medium
  ^MT197-C12-1
- **Mark Rzepczynski** Three C's: connectedness, correlation and contagion; treat markets as a network of nodes whose connectedness (clusters, common traders, similar events) drives dynamic correlations.  #mech/crowding_positioning
  > what is market connectedness what are the correlations and what's the potential for contagion
  indicator: network connectedness of markets · asset: multi · testable: yes - network analysis · confidence: medium
  ^MT197-C12-2
- **Niels Kaastrup-Larsen** Investors often hold untested beliefs about system design (the best trend speed is three months; trading 500 markets must beat 100) that clash with a manager's evidence, so claims about speed and market count need evidence, not assertion.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > your Trend speed should be 3 months that's the best right well based on what evidence uh would you say that or you have to trade 500 markets that must be better than trading 100 markets
  indicator: trend speed; number of markets traded (100 vs 500) · asset: multi · testable: yes - compare Sharpe by trend speed and by market-universe size · confidence: medium
  ^MT197-C12-X1

### C13
- **Mark Rzepczynski** Portfolio construction should also exploit market connectedness: a Fed move spills to equities, bonds, dollar, then oil and commodities after a short delay, so cross-correlations and cross-trends could be used.  #mech/slow_reaction
  > the behavior of one market will spill over to another and that's an opportunity for exploitation
  indicator: cross-market spillover, variance decomposition · asset: multi · horizon: days · testable: yes - lead-lag spillover tests · confidence: medium
  ^MT197-C13-1
- **Niels Kaastrup-Larsen** Reaction patterns are reliable only within a sector (e.g. financials); beyond that few have high confidence, and trend following's strength is not needing to know how things play out.  #mech/research_method
  > as soon as you go outside uh the the the sector itself I think there are relatively few sectors where you can have high confidence in any kind of reaction pattern
  indicator: cross-sector spillover · asset: multi · testable: yes · confidence: medium
  ^MT197-C13-2
- **Mark Rzepczynski** Variance (shock) decomposition of cross-market spillovers could reveal the direction of causality between markets (a stock shock feeding bonds, dollar, commodities), which would guide portfolio construction, risk and opportunities.  #mech/new _(added by sonnet-xhigh cross-check)_
  > we should be able to decompose a shock and stocks on what it will on the impact on other markets and if we can know the direction of causality from one set of markets to another
  indicator: variance decomposition / directional spillover measures across markets · asset: multi · horizon: days · conditions: Niels doubts spillover patterns are reliable outside a single sector · testable: yes - estimate directional spillover indices and test lead-lag trades · confidence: medium
  ^MT197-C13-X1

### C14
- **Mark Rzepczynski** Markets trade in clusters (base metals driven by business cycle, precious metals, energy) with spillovers to the real economy.  #mech/structural_shift
  > we do know that markets trade in clusters so we know that there's a base metal clustered
  indicator: base metals, precious metals, energy clusters · asset: commodities · testable: yes - cluster analysis · confidence: medium
  ^MT197-C14-1
- **Mark Rzepczynski** Efficiency is dynamic (Andy Lo's adaptive markets hypothesis): varies by liquidity, valuation difficulty, hedger/speculator mix, participants and cycle, so trends can exist; markets are efficient but not all the time.  #mech/cycle_persistence
  > if you're a trend follower you really believe in an Adaptive markets hypothesis
  indicator: adaptive markets hypothesis · asset: multi · testable: partly · confidence: medium
  ^MT197-C14-2
- **Mark Rzepczynski** Cliff Asness argues social media makes markets less efficient; Mark takes a more nuanced dynamic view.  #mech/behavioral
  > social media is driving uh markets to be less efficient and that there's more gamesmanship
  asset: equities · testable: no · confidence: low
  ^MT197-C14-3
- **Niels Kaastrup-Larsen** Niels reports that Andrew Lo told him markets are efficient but not all the time, so periods of big moves (trends) are to be expected.  #mech/new _(added by map cross-check)_
  > he basically just said yeah I mean markets are efficient but not all the time so there will be these periods of time where you see these big moves that we call Trends
  indicator: efficiency regime · asset: multi · testable: no - conceptual · confidence: medium
  ^MT197-C14-R1

### C15
- **Mark Rzepczynski** Many market participants (including central bankers) have never experienced a large bear market, so their collective memory is poor and they expect policy to always support markets.  #mech/behavioral
  > you could be 40 years old and never seen a a a large bare market
  indicator: experience of bear markets · asset: equities · horizon: years · testable: no · confidence: medium
  ^MT197-C15-1
- **Mark Rzepczynski** Systematic managers backtest over long history, so a plan exists for equity declines (sell/short) even if the manager has not lived through a bear market.  #mech/risk_management
  > the systematic manager should be able to have a plan in place because his models allows for going both long and short
  indicator: long-short models · asset: equities · testable: yes · confidence: high
  ^MT197-C15-2
- **Niels Kaastrup-Larsen** Volatility picks up around trend turning points which makes trend followers cut risk, though sharp reversals still hurt.  #mech/slow_reaction
  > there is a pickup of volatility around these big turning points um and that in itself actually often triggers Trend followers to reduce their risk
  indicator: volatility-scaled risk at turning points · asset: multi · direction: reduce risk · horizon: days · testable: yes · confidence: medium
  ^MT197-C15-3
- **Niels Kaastrup-Larsen** Passive flows could amplify a sustained market decline, unlike the short 2-3 week dips since the central bank rescues of recent years.  #mech/liquidity_flows _(time-bound view)_
  > flows from passive Investments and and what that's going to do once the markets
  indicator: passive fund flows · asset: equities · horizon: months · conditions: sustained decline · testable: partly · confidence: low
  ^MT197-C15-4
- **Mark Rzepczynski** A 20% equity bear market would only take back about a year and a half of returns and not remove the overvaluation, yet policymakers (calls for a 75bp cut after the August 2024 carry unwind) act to prevent it; this shows over-sensitivity of policy to modest equity declines.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > a 20% correction in the stock market which would be a bare Market uh is you have a Devastation on a lot of people's wealth but on many measures that wouldn't really sort of eliminate all the overvaluation in stocks
  indicator: equity valuation; 20% drawdown · asset: equities · direction: policy support for equities (Fed put) expected on small declines · horizon: months · conditions: recent memory of only short dips, quickly rescued · testable: partly - compare policy reaction thresholds with drawdown depth · confidence: medium
  ^MT197-C15-X1

### C16
- **Mark Rzepczynski** The SG index is built from the largest managers by AUM, reconstituted yearly; a diversified portfolio of selected CTAs should be able to beat it.  #mech/research_method
  > they look at uh what is the top uh managers in terms of AUM and then they adjust this once a year
  indicator: SG CTA Index construction · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT197-C16-1
- **Niels Kaastrup-Larsen** The new SG investable CTA index is a giant backtest of a model, and buying a CTA replicator index is not the same as buying a stock index.  #mech/research_method
  > it's giant back test of a model uh people should be aware of that
  indicator: investable CTA replicator index · asset: multi · testable: yes · confidence: medium
  ^MT197-C16-2
- **Niels Kaastrup-Larsen** Citing Transtrend and Michael Green's 'Why bother being better': investors should look for managers who strive to differ from and beat the index rather than simply buying the CTA index, since passive concentration distorts markets and an index is not risk-free.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > he's also basically suggesting that investors should try and find managers who strive to be different from the index and ideally of course be better uh than the index
  indicator: SG CTA index versus selected managers · asset: multi · horizon: years · testable: partly - manager-selection value added versus the index · confidence: medium
  ^MT197-C16-X1

### C17
- **Niels Kaastrup-Larsen** Replicators carry manager risk too: they are small firms whose models could be flawed.  #mech/risk_management
  > I think there's a huge manager risk and often these replicators run very small firms much smaller than the underlying managers
  indicator: CTA replication · asset: multi · testable: no · confidence: medium
  ^MT197-C17-1
- **Mark Rzepczynski** Replicators aim for median manager returns, not a benchmark; median replication is suitable for low-cost investors with no manager skill, while most managers underperform their benchmarks.  #mech/research_method
  > a median uh replication strategy is not a benchmark replication
  indicator: median manager replication · asset: multi · testable: yes · confidence: medium
  ^MT197-C17-2

