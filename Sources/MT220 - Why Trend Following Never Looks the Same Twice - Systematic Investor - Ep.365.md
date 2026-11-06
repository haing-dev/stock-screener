---
source_id: MT220
title: "Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365"
date: 2025-09-18
channel: "Top Traders Unplugged"
url: 
words: 9994
claims: 40
added_by_crosscheck: 12
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Niels Kaastrup-Larsen (host)", "Katy Kaminski (systematic researcher, AlphaSimplex)"]
tags: [source, layer0]
---
# Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365

**Speakers:** Niels Kaastrup-Larsen (host); Katy Kaminski (systematic researcher, AlphaSimplex)

**Summary:** Top Traders Unplugged ep. 365 (Sept 2025): Man AHL and Quantica papers on trend manager return dispersion (speed, allocation, alternative markets, carry), Kaminski's style factors and Mahalanobis turbulence, and why 2-3 different CTAs plus diversification beats chasing factors.

**Approach:** trend following, return dispersion, alternative markets, manager selection

**Cross-check completeness estimate of first read:** 0.80 - the first reader caught the four dispersion drivers, Man and Quantica findings, turbulence metric and the two-or-three-managers advice, but missed the performance table, fixed-income signal state, the Man hypothetical-manager method, random-signal studies, chance tracking gaps, and several Quantica points (per-market Sharpe, range-bound alt markets, two-edged crowding).

## Argument map

**Episode thesis:** Kaminski and Kaastrup-Larsen argue that return dispersion among trend followers is not random but the fingerprint of design choices (speed, asset-class allocation, alternative markets, carry), none of which dominates every year, so an investor cannot pick a winning factor and should hold two or three different CTAs. They add that the recent underperformance of alternative-market trend is a regime/sector effect (gas and power, credit after the COVID and Ukraine shocks), that alternative markets are a diversification argument rather than a better-trend argument, and that turbulence can be split into magnitude surprises (bad for CTAs) and correlation surprises (inflection points that drive dispersion).

### Katy Kaminski (Systematic researcher at AlphaSimplex; co-author (with Alex Greyserman) of a book on trend following; former CTA allocator)
Fingerprint: #approach/trend_following #approach/research_robustness_overfitting #approach/portfolio_construction_stacking #approach/manager_selection_allocation #approach/regime_detection #approach/crisis_alpha_convexity #approach/replication_indexing #approach/positioning_crowding
_Speaker note: Name spelled Katie Kaminsky in captions. Two ledger claims carry corrections: MT220-C03-1 (surprise scenarios: more cuts than expected or no cut would be the shock; a 50bp cut is what was expected) and MT220-C11-1 (Liberation Day is not in the turbulence data set; she only presumes it is a magnitude surprise). Both are cited under the corrected reading._

**Worldview premises**
- Return dispersion among trend managers follows from design choices (speed, asset allocation, alternative markets, carry) and from basic math of differing volatilities and correlations, so it is explainable and can be estimated theoretically. _[theoretical, stated; support: Man AHL 'Dynamics of dispersion', her book chapter 11, and treating managers as random variables.]_ ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C05-1|C05-1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C06-2|C06-2]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C07-2|C07-2]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C04-2|C04-2]])
- No single design factor is the main driver of dispersion; each dominates in a different year (fixed income in 2019, no equities in 2025), and no style factor persists. _[empirical, stated; support: Her style-factor tracking at AlphaSimplex and the Man paper's yearly results.]_ ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C09-1|C09-1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C05-X1|C05-X1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C11-2|C11-2]])
- Faster trend following gives more crisis protection; the industry has drifted to slower products, so replicators and slow managers get less crisis alpha even though slow did better recently. _[empirical, stated; support: Man AHL paper and her 'CTA style evolution' study; history of the CTA index.]_ ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C05-2|C05-2]])
- CTA indices are not investable and managers' styles drift, so one buys today's managers, not the index; study aspects of managers (speed, markets) rather than index behaviour. _[institutional, stated; support: Her style-drift study.]_ ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C06-1|C06-1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C07-1|C07-1]])
- A trend follower should include every asset, since assets that never trended (metals, palladium, copper, platinum) can start to trend. _[experience, stated; support: Past debates over excluding metals; recent trends in platinum, palladium, gold, nickel, copper.]_ ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C12-2|C12-2]])
- Adding low-correlation trend P&L streams raises portfolio Sharpe mathematically; alternative markets provide this diversification, but higher costs offset some of the Sharpe. _[theoretical, stated; support: Portfolio-theory argument in the Quantica paper and her own book.]_ ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C13-2|C13-2]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C06-3|C06-3]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C14-X1|C14-X1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C13-R1|C13-R1]])
- Extreme outperformance of alternative markets in 2020-22 came from specific sectors (gas and power, credit), raising expectations, which is why three weaker years caused doubt; those assets have been range-bound since the shocks. _[empirical, stated; support: Quantica's 50 traditional versus 120 alternative market comparison.]_ ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C12-1|C12-1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C12-X1|C12-X1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C13-X2|C13-X2]])
- Crowding is two-edged for trend: it still works in crowded liquid markets, but capacity-limited markets may have looked better in backtests when fewer participants traded them. _[theoretical, stated; support: No study; she wants a case-study analysis.]_ ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C14-X1|C14-X1]])
- Macro and systematic macro outperformed trend around Liberation Day, which motivates research on economic versus technical trends. _[experience, stated; support: Observed April 2025 results; paper in progress.]_ ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C14-2|C14-2]])

**Chain: Why fixed income trend signals have not built despite many themes**
1. Market already prices Fed cuts (SOFR near 3.4% versus fed funds at 4.25-4.5%) → Bond trend signals stay mixed and weak, teetering between long and short: The market has been anticipating the Fed, so no sustained one-way move. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C03-1|C03-1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C03-X1|C03-X1]])
2. Outcome that differs from pricing (far more cuts than expected, or no cut) → A large move and a trend catalyst: Only a surprise relative to pricing moves a priced market; a 50bp cut is what was expected. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C03-1|C03-1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C01-1|C01-1]])
- Evidence: Mixed signals in September 2025: slightly more long in the US, short in the UK and some European bonds; recent jobs data had already priced in cuts.
- Fails when: If futures price future rather than current rates, long yields can rise after cuts (host's point), so direction is not obvious.

**Chain: How design choices become return dispersion across trend managers**
1. Speed, allocation, alternative markets, carry differ across managers → Different return streams with different vol and correlation: Managers as random variables; range of differences set by volatility and correlation. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C05-1|C05-1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C06-2|C06-2]])
2. A year with a particular sector trend (2019 fixed income; 2025 no equities in ETFs) or a high-volatility year (2008, 2022) → A given factor dominates and the dispersion widens: Bigger moves amplify differences. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C09-1|C09-1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C08-1|C08-1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C05-X1|C05-X1]])
3. Combine two or three managers → Much of the dispersion versus the index disappears, but 3-4% remains: Residual tracking is normal even for replication (500-600bp slippage). ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C08-2|C08-2]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C09-X1|C09-X1]])
- Evidence: Man AHL hypothetical-manager aggregation, her chapter 11 random-sampling study, and a random-signal experiment.
- Fails when: Not stated; she stresses that no factor is persistent.

**Chain: Turbulence: magnitude versus correlation surprises**
1. Mahalanobis distance across manager returns → Point-in-time measure of movement with no data window: Correlation needs a window and averages away a one-day event. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C10-1|C10-1]])
2. Decompose into magnitude surprise and correlation surprise → Magnitude surprises (Brexit, SVB, Black Friday) hurt CTAs; correlation surprises are inflection points where trend signals rotate and drive dispersion: Shock versus change in how managers behave relative to each other. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C11-1|C11-1]])
- Evidence: Her paper 'Quantifying turbulence in CTAs'; plotted history of surprises.
- Fails when: Liberation Day is outside the sample and only presumed to be a magnitude surprise.

**Chain: Alternative markets: why they underperformed recently and what remains**
1. 2020-22 shocks (COVID, Ukraine) → Gas and power, credit and similar sectors trended extremely, 40-50% of the outperformance coming from gas and power: Specific sector events, not structural better trending. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C12-1|C12-1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C13-1|C13-1]])
2. Those assets became range-bound → Alternative-market managers lagged for about three years: Regime effect, not proof the thesis is broken. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C13-X2|C13-X2]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C12-X1|C12-X1]])
3. Money flowed into less-liquid markets → Possible crowding and higher transaction costs: Host's hypothesis; she wants a case-study test. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C14-1|C14-1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C14-X1|C14-X1]])
- Evidence: Quantica Q3 2025 paper; Sharpe per market adjusted for the period instead of reading which sectors won; only about 10 years of history for such managers.
- Fails when: Costs of exotic contracts reduce the net Sharpe; the benefit is diversification, not better trend.

**Decision process**
- [portfolio] Start simple: pick two or three CTAs that are different, avoid analysis paralysis, combine a faster manager (crisis alpha) with a slower manager or replication product.. Why: CTAs are among the few alternatives without hidden equity beta; no style factor persists; too much analysis creates false expectations. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C11-2|C11-2]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C11-X1|C11-X1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C08-2|C08-2]])
- [research] Track style factors for trend (speed, market size, correlated markets) and regress manager returns to explain relative performance, as equity style factors do.. Why: Disentangles benchmark from style tilts, year by year. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C09-2|C09-2]])
- [research] Study hypothetical trend managers built with many designs and aggregated over time rather than a single backtest; use random-signal experiments to split allocation from signal effects.. Why: Avoid cherry-picking the best backtest version. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C06-X1|C06-X1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C08-X1|C08-X1]])
- [research] Do not match absolute Sharpe of an index replication; focus on relative and conditional differences.. Why: Backtest Sharpe 0.75 versus actual 0.36 reflects that longer lookbacks did better and managers differ. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C07-1|C07-1]])
- [universe] Include all assets in a trend programme, accounting for costs of exotic contracts.. Why: Non-trending assets can start to trend; diversification raises Sharpe. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C12-2|C12-2]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C13-2|C13-2]])
- [research] Evaluate alternative markets by Sharpe per market adjusted for the period and portfolio theory, not by recent sector winners.. Why: Short 10-year history. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C13-X1|C13-X1]])
- [risk] Do not read a 400-500bp gap versus the index with two or three CTAs as poor selection.. Why: Such gaps arise by chance with these correlations. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C09-X1|C09-X1]])

**Evidence style:** Academic literature and her own studies (book chapter 11, CTA style evolution, turbulence paper), mathematical arguments about variance and diversification, and random-sampling or hypothetical-manager simulations; explicit about the short sample for alternative markets.

**Views at the time**
- (2025-09) US fixed income trend signals have barely moved despite many themes (Fed independence, inflation); a bond breakout could be the next trend catalyst.. Reasoning: Many calls from clients and press on fixed income while signals stay put. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C01-1|C01-1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C03-1|C03-1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C03-X1|C03-X1]])
- (2025-09) Bond market already prices cuts; surprise is needed (more cuts than expected or no cut) for a trend.. Reasoning: SOFR near 3.4%; jobs data baked in. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C03-1|C03-1]])
- (2025-09) Systematic macro did better than trend around Liberation Day; researching economic versus technical trends.. Reasoning: April 2025 results. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C14-2|C14-2]])
- (2025-09) In 2025 CTA ETFs that did not trade equities did relatively well.. Reasoning: Asset-class tilt example. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C05-X1|C05-X1]])

### Niels Kaastrup-Larsen (Host of Top Traders Unplugged; veteran hedge fund (trend following) manager)
Fingerprint: #approach/trend_following #approach/policy_reaction_central_banks #approach/manager_selection_allocation #approach/replication_indexing #approach/positioning_crowding #approach/geopolitics #approach/costs_execution
_Speaker note: Mostly asks questions and relays paper content; his own views are marked here only where he asserts them (bond market, index dispersion, crowding)._

**Worldview premises**
- Bond yields react strongly to political and budget uncertainty, as UK and French politics show in September 2025. _[empirical, stated; support: Current events.]_ ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C01-2|C01-2]])
- Long yields can rise after rate cuts if investors consider the cuts insufficient or fear inflation, because futures price future rates, not today's. _[theoretical, stated; support: Last cut episode, when yields rose.]_ ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C03-2|C03-2]])
- Index dispersion comes from specific constituents (one outlier in 2009; two discretionary managers in 2014 later removed); do not infer manager risk or the case for replication without understanding the makeup. _[empirical, stated; support: Man AHL paper page 3.]_ ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C05-3|C05-3]])
- Design choices explain return dispersion, so dispersion is the fingerprint of each trend system. _[theoretical, stated; support: Man AHL paper.]_ ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C04-2|C04-2]])
- Flows into alternative markets after their outperformance may have crowded them and raised costs, contributing to recent underperformance; roughly 40-50% of their outperformance came from gas and power tied to the Ukraine shock and cannot be replicated going forward. _[experience, stated; support: From memory; no data.]_ ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C14-1|C14-1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C13-1|C13-1]])

**Chain: Cuts that push long yields up**
1. Fed cuts already expected and shorts in place → Investors judge the cut insufficient or fear inflation: Futures price future, not today's, rates. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C03-2|C03-2]])
2. Insufficient cut → Long yields rise: Happened at the last cut. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C03-2|C03-2]])
- Evidence: Last cut episode, recalled.
- Fails when: Not stated.

**Decision process**
- [research] Understand an index's makeup and each constituent before drawing conclusions about manager risk or replication.. Why: Outliers and discretionary managers create dispersion. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C05-3|C05-3]])
- [risk] Test crowding in less-liquid markets, for example with a case study of one market.. Why: Possible role in recent underperformance. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C14-1|C14-1]])
- [signal] Uses his own Trend Barometer, which uses shorter lookbacks and was weak in September 2025.. Why: Short-term models struggled most on a vol-adjusted basis in 2025. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C04-1|C04-1]])

**Evidence style:** Industry observation, performance indices, and citing papers; asks questions to elicit Kaminski's research.

**Views at the time**
- (2025-09) CTA September 2025: equities, metals, sugar and oil products supported; livestock paused; managers disagree on fixed income direction.. Reasoning: Descriptive. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C02-1|C02-1]])
- (2025-09-08) Performance to 8 Sep 2025: BTOP50 +91bp (-1.93% YTD), SG CTA about +1% (about -5.1% YTD), SG Trend +1.25% (-6.5% YTD), short-term traders +66bp (nearly -6% YTD); MSCI World +15.1% YTD, US Aggregate almost +6%, S&P 500 TR +11.74%. CTAs lagged both stocks and bonds in 2025.. Reasoning: Descriptive. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C04-X1|C04-X1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C04-1|C04-1]])
- (2025-09) UK and French political chaos is a potential driver of bond yields.. Reasoning: Bond yields react to budget uncertainty. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C01-2|C01-2]])

### Disagreements
- **Why alternative-market trend lagged recently**: Niels Kaastrup-Larsen: Inflows into less-liquid markets may have crowded them and added costs, contributing to underperformance. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C14-1|C14-1]]); Katy Kaminski: Mostly a regime effect: the assets that drove 2020-22 gains went range-bound; crowding is two-edged and untested, so she would like a case study. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C13-X2|C13-X2]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C14-X1|C14-X1]])
- **How much an index (or replication) says about manager risk**: Niels Kaastrup-Larsen: Index dispersion depends on constituents; do not conclude replication is better without understanding where dispersion comes from. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C05-3|C05-3]]); Katy Kaminski: The index is not investable and managers drift; replication Sharpe differs from actual; look at relative and conditional differences. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C06-1|C06-1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C07-1|C07-1]])

### Gaps and conflicts
- Ledger claim MT220-C03-1 as originally worded had the surprise scenario wrong; the corrected reading (no cut or far more cuts than expected as the shock; a 50bp cut being expected) is used in the map. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C03-1|C03-1]])
- Liberation Day is described as a magnitude surprise although it is outside the paper's sample; Kaminski says only that she is 'pretty sure'. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C11-1|C11-1]])
- The causal claim that crowding explains recent alternative-market underperformance is untested; both speakers say so. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C14-1|C14-1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C14-X1|C14-X1]])
- Alternative-market managers have only about 10 years of history, so conclusions about their long-run Sharpe are weak. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C13-X1|C13-X1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C12-1|C12-1]])
- The replication Sharpe gap (0.75 backtest versus 0.36 actual) is explained by lookbacks and manager differences without a quantitative decomposition. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C07-1|C07-1]])
- The statement that managers in the Man AHL index have dispersion explained by design and the statement that no factor is the main driver leave open how much dispersion is explained at all. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C04-2|C04-2]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C09-1|C09-1]])
- Alternative-market performance claim: 40-50% from gas and power is from the host's memory. ([[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C13-1|C13-1]])

### Forward-looking inputs (reader synthesis)
(reader) Speakers point to: the Fed decision relative to pricing (a no-cut or much larger cut would be the catalyst for a bond trend), UK and French budget politics for yields, whether gas and power or credit leave their range, and crowding in less-liquid markets. Horizon: the next Fed meeting for bonds; years for the alternative-market diversification argument.

### Reader inferences (not stated by the speakers)
- (reader) Kaminski's advice to hold two or three different CTAs follows from her finding that no style factor persists and that 3-4% tracking vs the index always remains.
- (reader) The magnitude/correlation decomposition suggests a manager-level early-warning measure: rising correlation surprise marks regime rotation, rising magnitude surprise marks shock risk.
- (reader) Alternative markets are defended as diversifiers, not as better trend, so their case does not depend on the 2020-22 outperformance.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | Intro; Fed bond trend signals; European political chaos |
| C02 | 1 | AirPods banter; hedge fund brand awareness ranking; September CTA update |
| C03 | 2 | Fixed income signals, SOFR vs Fed funds, cuts priced |
| C04 | 2 | Index performance numbers; Man AHL dynamics of dispersion intro |
| C05 | 3 | Four dispersion dimensions; speed and crisis; index constituents |
| C06 | 3 | Index investability, style drift, volatility and correlation math; alt markets |
| C07 | 2 | Sharpe of index replication; Chapter 11 of Trend Following book |
| C08 | 2 | Equal risk, 2008/2022 dispersion; adding managers |
| C09 | 2 | Main driver of dispersion; CTA style factors |
| C10 | 1 | Style factors; Mahalanobis turbulence |
| C11 | 2 | Magnitude vs correlation surprises; keep it simple |
| C12 | 2 | Quantica paper on alternative markets |
| C13 | 2 | Gas and power; Sharpe diversification argument |
| C14 | 2 | Crowding in alt markets; next research |
| C15 | 0 | Outro - nothing actionable |

## Claims

### C01
- **Katy Kaminski** US fixed income trend signals had barely moved despite many themes (Fed independence, inflation), so a breakout in bonds could be the next catalyst for trend followers.  #mech/slow_reaction _(time-bound view)_
  > if you look at the trend signals, they haven't moved much. So, I'm kind of thinking that could be a potential catalyst.
  indicator: US fixed income trend signals · asset: rates · horizon: weeks · testable: partly · confidence: low
  ^MT220-C01-1
- **Niels Kaastrup-Larsen** Bond yields react strongly to political and budget uncertainty, as with UK and French political chaos.  #mech/fiscal_debt _(time-bound view)_
  > bond yields are very good at reacting to it's uncertainty especially about budgets
  indicator: UK and French bond yields · asset: rates · horizon: months · testable: yes · confidence: medium
  ^MT220-C01-2

### C02
- **Niels Kaastrup-Larsen** In September 2025 equities, metals, sugar and oil products supported CTAs; livestock paused; managers disagreed on fixed income direction.  #mech/cycle_persistence _(time-bound view)_
  > Of course, equities, metals continue to do the heavy lifting, I
  indicator: CTA sector contributors · asset: multi · horizon: weeks · testable: no - descriptive · confidence: medium
  ^MT220-C02-1

### C03
- **Katy Kaminski** With SOFR near 3.4% and fed funds at 4.25-4.5%, rate cuts were priced in, so a trend in bonds needs a surprise relative to pricing (50bp cut or no cut), and the lack of trend reflects anticipation of the Fed.  #mech/policy_reaction _(time-bound view)_
  > the market has already decided that we're getting cuts. The biggest shocks are going to be if we get a lot more cuts or if we don't get enough.
  indicator: SOFR vs fed funds, priced cuts · asset: rates · horizon: weeks · testable: partly · confidence: medium
  **Correction (cross-check):** The surprise scenarios are wrong. Katy says the biggest shocks would be a lot more cuts than expected or not enough cuts, that a 50bp cut is what was expected or wanted (so not a surprise), and that getting no cut 'could be huge'. → With SOFR near 3.4% against fed funds at 4.25-4.5%, rate cuts were priced in, so bond trends need a surprise relative to pricing: a no-cut outcome (or far more cuts than expected) would be the shock, while a 50bp cut is what the market expected; the lack of a trend so far reflects anticipation of the Fed and the jobs data.
  ^MT220-C03-1
- **Niels Kaastrup-Larsen** Long yields can rise after rate cuts if investors consider cuts insufficient or fear inflation, since futures price future rates, not today's.  #mech/policy_reaction _(time-bound view)_
  > let's not forget what happened last time they caught actually bond yields went up.
  indicator: long yields after Fed cuts · asset: rates · horizon: weeks · testable: yes - event study · confidence: medium
  ^MT220-C03-2
- **Katy Kaminski** In September 2025 fixed income trend signals were mixed and weak, flipping between long and short: slightly more long signals in the US, short in the UK and some European bonds, which is why managers disagreed on bond direction.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > the signals have been very mixed and kind of weak and teetering around between should we be short, should we be long
  indicator: bond trend signals (US, UK, Europe) · asset: rates · direction: no consistent bond trend · horizon: weeks · conditions: September 2025 · testable: yes - signal data · confidence: medium
  ^MT220-C03-X1

### C04
- **Niels Kaastrup-Larsen** In 2025 short-term trend models struggled most on a vol-adjusted basis; Trend Barometer was weak because it uses shorter lookbacks.  #mech/slow_reaction _(time-bound view)_
  > we know that short-term models this year are probably the ones on a vol adjusted basis that are struggling the most.
  indicator: short-term trend model performance · asset: multi · horizon: months · conditions: 2025 regime · testable: yes · confidence: medium
  ^MT220-C04-1
- **Niels Kaastrup-Larsen** Return dispersion among trend managers is explained by design choices (speed, allocation, alternative markets, carry), so dispersion is the fingerprint of each system (Man AHL 'Dynamics of dispersion').  #mech/research_method
  > how fast you chase trends, which market you include, whether you tilt towards bonds or FX, or whether you sneak in a little bit of carry
  indicator: speed, allocation, alternative markets, carry · asset: multi · horizon: years · testable: yes - Man AHL paper · confidence: high
  ^MT220-C04-2
- **Niels Kaastrup-Larsen** Performance data to 8 Sep 2025: BTOP50 +91bp in September (-1.93% YTD), SG CTA about +1% (about -5.1% YTD), SG Trend +1.25% (-6.5% YTD), short-term traders +66bp (nearly -6% YTD), against MSCI World +90bp (+15.1% YTD), US Aggregate bonds +96bp (almost +6% YTD) and S&P 500 total return +86bp (+11.74% YTD), so in 2025 CTAs lagged both stocks and bonds.  #mech/new _(added by sonnet-xhigh cross-check, time-bound view)_
  > beta 50 is up 91 basis points but down only now 1.93% for the year
  indicator: BTOP50; SG CTA; SG Trend; SG Short-Term Traders; MSCI World; US Aggregate; S&P 500 TR · asset: multi · horizon: months · conditions: to 8 September 2025 · testable: yes - index data · confidence: high
  ^MT220-C04-X1

### C05
- **Katy Kaminski** Carry has about 30-40% correlation with trend, so adding carry smooths performance over different horizons.  #mech/risk_premium
  > Carrie as you know has about a 30 40% correlation with trend.
  indicator: carry vs trend correlation · asset: multi · direction: add carry to trend · horizon: years · testable: yes · confidence: medium
  ^MT220-C05-1
- **Katy Kaminski** Faster trend following helps most in crises; the industry has shifted to slower products that give less crisis protection, though slow ones did better recently.  #mech/slow_reaction
  > being faster is actually really helpful for really bad environments.
  indicator: trend speed and crisis performance · asset: multi · direction: favor faster trend for crisis alpha · horizon: months · conditions: crisis environments · testable: yes - Man AHL paper · confidence: high
  ^MT220-C05-2
- **Niels Kaastrup-Larsen** Index dispersion arises from specific constituents (one outlier in 2009; two discretionary managers in 2014 later removed), so understand makeup before concluding about manager risk or replication.  #mech/research_method
  > in 2009 just one constituent stood out with a doubledigit positive territory and the rest was kind of more flat to negative
  indicator: SG CTA constituents · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT220-C05-3
- **Katy Kaminski** Allocation choices create visible manager dispersion: in 2025 CTA ETFs that did not trade equities did relatively well, an example of asset-class tilt driving relative performance in a given year.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > CTA in the ETF space this year has you know does not use equities and that's been positive for them
  indicator: CTA ETF performance vs equity exposure · asset: multi · direction: avoiding equities helped in 2025 · horizon: months · conditions: 2025 only · testable: yes - fund returns · confidence: medium
  ^MT220-C05-X1

### C06
- **Katy Kaminski** CTA indices are not investable and manager style drifts over time, so study aspects (speed, markets) of managers rather than rely on index behavior.  #mech/research_method
  > you don't buy 2007's CTA, you buy 2025 CTA.
  indicator: CTA style drift · asset: multi · horizon: years · testable: yes - style evolution paper · confidence: high
  ^MT220-C06-1
- **Katy Kaminski** Dispersion between managers follows mathematically from differences in volatility and correlation among their returns, so theoretical dispersion can be estimated.  #mech/research_method
  > each of these managers as a random variable. They each have a volatility and mathematically you can think about what the range of differences is going to be.
  indicator: volatility and correlation of managers · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT220-C06-2
- **Katy Kaminski** Man AHL found outperformance and correlation benefits from alternative markets, though depending on the horizon.  #mech/structural_shift
  > they also demonstrate some outperformance of alternative markets.
  indicator: alternative markets · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT220-C06-3
- **Katy Kaminski** The Man AHL method builds many hypothetical trend managers with different designs and aggregates them over time, which allows studying design differences across environments without cherry-picking the best backtest version.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > create a bunch of different trend managers as hypotheticals and aggregate them over time and examine sort of behavioral differences in different environments
  indicator: hypothetical trend managers across speed, allocation, markets and carry · asset: multi · horizon: years · testable: yes - reproducible design · confidence: medium
  ^MT220-C06-X1

### C07
- **Katy Kaminski** Replicated indices give different Sharpe (about 0.75 backtest vs 0.36 actual) because longer lookbacks did better historically and managers differ, so focus on relative and conditional differences.  #mech/research_method
  > I'm not surprised that sharp ratios are different because it's a back test, right?
  indicator: replicated vs actual SG Trend index Sharpe · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT220-C07-1
- **Katy Kaminski** In Kaminski and Greyserman's book chapter 11, equal-risk allocation historically outperformed market-capitalization-weighted allocation, with dispersion driven by equity bias, carry, allocation and speed.  #mech/risk_premium
  > how equal risk outperformed historically in our analysis.
  indicator: equal risk vs liquidity-weighted allocation · asset: multi · direction: equal-risk weighting · horizon: years · testable: yes · confidence: medium
  ^MT220-C07-2

### C08
- **Katy Kaminski** Return dispersion between trend managers is greater in high-volatility years (2008, 2022) simply because moves are bigger.  #mech/risk_management
  > we did find that 2008 given the size of the moves regardless of you know which type of methodologies you use you had a bigger range
  indicator: market volatility vs dispersion · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT220-C08-1
- **Katy Kaminski** Combining two or three managers removes much of the return dispersion versus the index, but residual 3-4% (replication 500-600bp slippage) always remains.  #mech/risk_management
  > you adding at least two maybe three together gets you pretty far in terms of adjusting some of that return dispersion
  indicator: number of managers vs dispersion · asset: multi · direction: hold two to three different CTAs · horizon: years · testable: yes - random sampling · confidence: medium
  ^MT220-C08-2
- **Katy Kaminski** Random-signal experiments (alongside channel breakout versus moving average signals) separate how much return dispersion comes from asset allocation and position sizing versus from the entry signals themselves.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > we even had these sort of random signal studies too just to understand sort of how much of that is driven by the sort of allocation and how much of it is driven by signals themselves
  indicator: random signals vs breakout and moving-average signals · asset: multi · horizon: years · conditions: the chapter targeted dispersion, not performance · testable: yes - simulation design · confidence: medium
  ^MT220-C08-X1

### C09
- **Katy Kaminski** No single design factor (speed, allocation, alternative markets, carry) is the main driver; each dominates in different years, e.g. fixed income only in 2019.  #mech/cycle_persistence
  > I think any of these particular ones will kind of stick out in a given year depending on what's happening.
  indicator: drivers of manager dispersion · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT220-C09-1
- **Katy Kaminski** Create style factors for trend (speed, market size, correlated markets) to regress manager returns and explain relative performance as with equity style factors.  #mech/research_method
  > we realized like we're very irritated that there's no benchmark. So we started sort of explaining how you could design a benchmark and then we created style factors similar to equities.
  indicator: CTA style factors · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT220-C09-2
- **Katy Kaminski** An investor holding two or three CTAs who trails the index by 400-500bp should not treat it as a sign of poor selection: gaps of that size arise by chance between return streams with these correlations.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > happen by chance with two random variables that have those correlations.
  indicator: tracking gap vs CTA index · asset: multi · horizon: years · conditions: portfolio of 2-3 managers vs an index · testable: yes - dispersion simulation · confidence: medium
  ^MT220-C09-X1

### C10
- **Katy Kaminski** A Mahalanobis-distance turbulence metric gives a point-in-time measure of movement across managers, decomposable into magnitude surprise and correlation surprise, without needing a window of data.  #mech/research_method
  > you use the Malhanobis distance to talk about how much movement there is.
  indicator: Mahalanobis turbulence of CTA returns · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT220-C10-1

### C11
- **Katy Kaminski** Magnitude surprises (Brexit, SVB, Black Friday, Liberation Day) hurt CTAs, while correlation surprises mark inflection points where trend signals rotate and drive dispersion.  #mech/behavioral
  > CTAs do not do as well on magnitude surprise days, right?
  indicator: magnitude vs correlation surprise · asset: multi · horizon: days · testable: yes · confidence: medium
  **Correction (cross-check):** Liberation Day is listed among the observed magnitude surprises, but Katy says it is not in the data set and that she is 'pretty sure' it would be a magnitude surprise. → In the turbulence paper the large pure magnitude surprises include Brexit, SVB and Black Friday (Liberation Day is outside the sample and only presumed to be one); CTAs do worse on magnitude-surprise days, while correlation surprises mark inflection points where trend signals rotate and drive dispersion.
  ^MT220-C11-1
- **Katy Kaminski** Investors should start simple: pick two or three different CTAs, avoid analysis paralysis, because CTAs are among few alternatives without hidden equity beta and no style factor persists.  #mech/risk_management
  > pick two or three, at least two or three managers that you like, that you think are a little different
  asset: multi · direction: hold two to three different CTAs · horizon: years · testable: partly · confidence: high
  ^MT220-C11-2
- **Katy Kaminski** Combine a faster manager (for crisis alpha) with a slower manager or a replication product, since each style does better in different environments and no style factor persists.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > maybe you can have some of that and you can have a manager that's going to be faster because you think, I like the crisis alpha and that one's slow
  indicator: manager speed · asset: multi · direction: hold both fast and slow trend · horizon: years · testable: yes - blend backtest · confidence: medium
  ^MT220-C11-X1

### C12
- **Katy Kaminski** Quantica compared 50 traditional with 120 alternative markets (credit, gas and power, livestock); sector composition explains recent differences, and alternative markets had extreme outperformance in specific sectors during 2020-22 rather than structurally trending better.  #mech/structural_shift
  > things like credit, gas and power, um more
  indicator: alternative vs traditional market trend portfolios · asset: multi · horizon: years · testable: yes - Quantica Q3 2025 · confidence: high
  ^MT220-C12-1
- **Katy Kaminski** A trend follower should include all assets because an asset that never trended (metals, palladium, copper) can start trending.  #mech/research_method
  > every asset is an opportunity for trend. I just don't know which one is going to work, right?
  indicator: market universe breadth · asset: multi · horizon: years · testable: partly · confidence: high
  ^MT220-C12-2
- **Katy Kaminski** Extreme outperformance of alternative markets in 2020-22 raised investors' expectations, so three years of weaker results led to doubts about the thesis even though the earlier gain came from specific sectors; the lower correlation benefit is a long-horizon argument.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > when your expectations are high and it doesn't work for the last 3 years um people start questioning the thesis
  indicator: alternative-market trend performance · asset: multi · horizon: years · conditions: after an extreme performance period · testable: no - investor psychology · confidence: medium
  ^MT220-C12-X1

### C13
- **Niels Kaastrup-Larsen** Roughly 40-50% of alternative markets' outperformance came from gas and power, tied to the Ukraine shock, which cannot be replicated going forward.  #mech/structural_shift
  > I think it was like 40 or 50% of the outperformance came from uh gas and power
  indicator: gas and power contribution to alt-market trend P&L · asset: commodities · horizon: years · conditions: one-off event · testable: yes · confidence: medium
  ^MT220-C13-1
- **Katy Kaminski** Adding low-correlation trend P&L streams raises portfolio Sharpe mathematically, and alternative markets add diversification though higher costs reduce their net Sharpe.  #mech/risk_premium
  > on aggregate the more lowly correlated P&L streams that you can add the little bit higher your sharp is
  indicator: P&L stream correlation and Sharpe · asset: multi · direction: add uncorrelated alternative markets · horizon: years · conditions: net of higher transaction costs · testable: yes · confidence: medium
  ^MT220-C13-2
- **Katy Kaminski** To avoid over-reading a short period (managers in alternative markets only have about 10 years of data), Quantica measures Sharpe per individual market and adjusts for the period, then reasons from portfolio theory about correlation, instead of judging by which sectors won recently.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > they said let's look at sharp per market on each individual trend instead of thinking like I know which trends or this period was better
  indicator: Sharpe ratio per market; P&L stream correlations · asset: multi · horizon: years · conditions: short sample for alternative-market managers · testable: yes - per-market Sharpe estimates · confidence: medium
  ^MT220-C13-X1
- **Katy Kaminski** The recent weakness of alternative-market trend is explained by the assets that drove 2020-22 gains (gas and power, credit and similar) being range-bound since the COVID and Ukraine shocks, so it is a regime effect rather than proof the thesis is broken.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > recently those assets have been very rangebound um after the big shock of co
  indicator: gas and power, credit and other alternative-market trend P&L · asset: commodities · horizon: years · conditions: after 2022 energy shock · testable: yes - sector attribution · confidence: medium
  ^MT220-C13-X2
- **Katy Kaminski** The Quantica paper does not argue that alternative markets trend better; it argues that they trend and add diversification, with higher costs offsetting part of any extra Sharpe.  #mech/new _(added by map cross-check)_
  > they don't argue that alt markets trend better per se
  indicator: Sharpe per market, correlation of P&L streams · asset: multi · horizon: long term · conditions: net of higher costs in exotic contracts · testable: yes: per-market Sharpe net of costs · confidence: medium
  ^MT220-C13-R1

### C14
- **Niels Kaastrup-Larsen** Inflows after the alternative-market outperformance may have crowded less-liquid markets and added transaction costs, contributing to recent underperformance; crowding analysis (case study of one market) would test this.  #mech/crowding_positioning
  > now we actually have maybe too much money tracing these less liquid markets.
  indicator: capacity and crowding of alternative markets · asset: commodities · horizon: years · testable: yes · confidence: low
  ^MT220-C14-1
- **Katy Kaminski** Systematic macro did better than trend around Liberation Day, motivating research on economic trends versus technical trends.  #mech/research_method _(time-bound view)_
  > I've been thinking a lot about macro and systematic macro and some interesting connections between the two strategies
  indicator: systematic macro vs trend · asset: multi · horizon: months · testable: yes · confidence: low
  ^MT220-C14-2
- **Katy Kaminski** Crowding is two-edged for trend: it still works in the most crowded liquid markets, but capacity-limited markets may show a more normal Sharpe in backtests from when fewer participants were in them, so the benefit of alternative markets is diversification, not a better trend.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check)_
  > trend falling still works in some of the most crowded markets we know
  indicator: market liquidity and capacity · asset: multi · horizon: years · conditions: less liquid alternative markets · testable: partly - crowding case study of one market proposed · confidence: medium
  ^MT220-C14-X1

