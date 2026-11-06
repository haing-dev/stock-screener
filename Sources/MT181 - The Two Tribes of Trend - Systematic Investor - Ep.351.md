---
source_id: MT181
title: "The Two Tribes of Trend - Systematic Investor - Ep.351"
date: 2025-06-11
channel: "Top Traders Unplugged"
url: 
words: 11172
claims: 51
added_by_crosscheck: 11
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Richard Brennan (systematic trend follower, Stockcross)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# The Two Tribes of Trend - Systematic Investor - Ep.351

**Speakers:** Richard Brennan (systematic trend follower, Stockcross); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Systematic Investor series. Brennan splits trend followers into idiosyncratic (single-market) and correlation-conscious (cross-sectional) styles and links their relative fortunes to the globalization/deglobalization regime; he then covers futures data hygiene (back-adjustment, roll logic, proxies for micro contracts), minimum capital for retail trend following, and LLM pitfalls in strategy development.

**Approach:** trend following, data hygiene, retail futures, AI/LLM overfitting

**Cross-check completeness estimate of first read:** 0.85 - the first reader caught all main trend-style, data-hygiene, small-capital and LLM-pitfall ideas; misses are secondary caveats (platform tooling, Panama engine/contango detail, LLM confident-wrong and prompt-design points, illustrative-path caveat).

## Argument map

**Episode thesis:** Richard Brennan splits trend following into 'idiosyncratic' (market-by-market time-series momentum) and 'correlation-conscious' (cross-sectional, vol-targeted, portfolio-correlation-managed) tribes. The latter won 2008-2020 because coordinated central banks and globalisation made markets causally correlated; after 2020 fragmentation favoured the former, and April 2025 tariff whipsaws hit all. He argues drawdowns are inherent, trends persist because markets are complex adaptive systems, and that retail traders can now run a robust trend programme with micro/nano futures from about $200k if they get data (Panama back-adjustment, roll logic, survivorship, granularity, proxies) right and treat LLMs as pattern-matchers that overfit and cannot reason causally.

### Richard Brennan (Systematic trend follower (Stockcross, Australia); educator of retail trend followers)
Fingerprint: #approach/trend_following #approach/regime_detection #approach/diversification_risk_parity #approach/position_sizing_vol_target #approach/research_robustness_overfitting #approach/costs_execution #approach/portfolio_construction_stacking #approach/structural_themes
_Speaker note: Per ledger correction, the opening drawdown remarks (AQR needing a good reason, April cruel, SG Trend Index at worst monthly drawdown) are Brennan's, not Niels's. The fee answer in C08-1 (percentage fees scaled to lot size) is Brennan's._

**Worldview premises**
- Deep drawdowns are inherent to trend-following models, even for the longest-established managers; the process is to wait for the next high-water mark. _[experience, stated; support: Own drawdown experience in April-May 2025; SG Trend Index touching its worst monthly drawdown on record.]_ ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C02-1|C02-1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C02-X1|C02-X1]])
- Trends are an inherent property of complex adaptive systems, so they will persist although the participants in trend following will change. _[theoretical, stated; support: Belief in complex adaptive systems; no data offered ('is trend dead is not in my vernacular').]_ ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C08-2|C08-2]])
- Trend followers split into two styles: idiosyncratic (each market independent, time-series momentum) and correlation-conscious (groupings, asset classes, cross-sectional view, vol targeting). _[experience, stated; support: Own observation of the industry; the split dates from the early 2000s.]_ ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C02-3|C02-3]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C02-4|C02-4]])
- Large managers cut target vol from ~25% to 10-12% to attract institutional assets, trading off the classic style's two-way volatility for smoothness. _[experience, stated; support: Industry history recalled; no figures cited beyond the vol levels.]_ ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C03-1|C03-1]])
- Which tribe wins depends on the correlation regime: globalisation and coordinated central banks (2008-2020) made markets causally correlated, rewarding cross-sectional grouping; deglobalisation, fragmentation and lost coordination after 2020 favour idiosyncratic trends (cocoa, soybeans, gold). _[experience, stated; support: Narrative of post-GFC and post-2020 performance of large vs idiosyncratic managers.]_ ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C03-2|C03-2]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C03-3|C03-3]])
- Market correlations are fickle and change quickly with politics, so diversification should come from structurally uncorrelated trend systems (an ensemble) and not merely from adding correlated markets. _[theoretical, stated; support: Argument from correlation instability; his long-held preference ('others would argue').]_ ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-3|C05-3]])
- Backtests are for stress testing and finding where models break, not estimating future returns; robustness across regimes beats curve fitting. _[theoretical, stated; support: First principles; trend followers cannot know where the next trend will arise.]_ ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C11-1|C11-1]])
- Limited capital is an advantage: the constraint forces a lean process; skin in the game enforces discipline. _[behavioural, stated; support: Observation of $10k retail traders who over-diversify and trade carelessly.]_ ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C12-X1|C12-X1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C12-2|C12-2]])
- Large language models predict plausible text and popular patterns, not causal relationships, so strategies they propose look polished but are overfit and fragile. _[theoretical, stated; support: Own LLM tests (crude oil system) and a Substack anecdote of an LLM falsely claiming to have read articles.]_ ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C14-1|C14-1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C14-2|C14-2]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C14-X1|C14-X1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C14-X2|C14-X2]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C14-R1|C14-R1]])
- Retail traders are democratised: mini, micro and nano futures and institutional-grade platforms replace the $1-2M once needed for trend-following diversification. _[institutional, stated; support: Product and platform observation (QuantConnect, StrategyQuant X linking to Interactive Brokers).]_ ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C07-1|C07-1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C07-X1|C07-X1]])

**Chain: Why correlation-conscious trend won 2008-2020 and lost after**
1. Trend managers wanting institutional AUM in the early 2000s → vol cut from ~25% to 10-12% via correlation reduction and vol targeting: Smoother returns are more acceptable to institutions. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C03-1|C03-1]])
2. Globalisation and coordinated central bank policy post-GFC → markets become causally linked: Cross-sectional grouping can exploit linked moves. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C03-2|C03-2]])
3. Deglobalisation, fragmentation, lost central bank coordination after 2020 → assets less correlated; idiosyncratic trends (cocoa, soybeans, gold) emerge: Single-market trends dominate when cross-market links weaken. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C03-3|C03-3]])
4. Large AUM managers with complex correlation-reducing models → underperformance 2020-24 and worst drawdowns now: Their design assumed the earlier regime. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C03-3|C03-3]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-2|C05-2]])
- Evidence: Narrative recall of the industry; no performance statistics shown.
- Fails when: Not stated; Brennan notes not every manager sits at an extreme of the spectrum.

**Chain: April 2025 whipsaw and expected resolution**
1. Widespread tariff announcements → simultaneous shocks in equities, commodities (canola), currencies (yen, China): The policy reached across all sectors trend followers trade. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C04-1|C04-1]])
2. Whipsaws across all sectors → deep drawdown for all trend followers: No consistent direction to follow. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C04-1|C04-1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C02-1|C02-1]])
3. Uncertainty must resolve → a direction emerges and trends return: Regime unlikely to be sustained. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C04-1|C04-1]])
- Evidence: Own experience of April; a hope ('crossing my fingers').
- Fails when: Not stated.

**Chain: Bad futures data contaminates backtests**
1. Contracts expire and roll → raw series have artificial gaps: Gaps at each roll are illusions that create false signals. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C08-3|C08-3]])
2. Back-adjusting with the Panama method (subtract each roll gap from all earlier history) → history is re-adjusted at every new roll; early prices can go negative in backwardation; contango raises history: Preserves the live front price but shifts earlier levels. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C09-1|C09-1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C09-X1|C09-X1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C09-X2|C09-X2]])
3. Shifted historical price levels → rules using absolute price thresholds, long-lookback percent returns, mean reversion to long averages or fixed dollar stops mislead: Indicators must be agnostic to adjustment bias. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C10-1|C10-1]])
4. Mismatch of roll logic, survivorship, or data granularity between backtest and live → backtest and live results diverge: Delisted contracts and intraday inference are missing from the test. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C10-2|C10-2]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C10-3|C10-3]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C10-4|C10-4]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C09-2|C09-2]])
- Evidence: Practical experience (20+ years of CSI data); no quantified impact.
- Fails when: Engines that reject negative prices require another adjustment method.

**Chain: Why LLM-generated strategies fail**
1. LLM trained on popularity of models in forums → returns generic indicator stacks (SMA cross + RSI + ATR) with no market-specific logic: Pattern recognition, not causal reasoning. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C14-1|C14-1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C14-2|C14-2]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C14-R1|C14-R1]])
2. Auto-generating hundreds of strategies and backtesting them → mass data mining producing false positives that die live: No regime validation or structural filters. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C15-1|C15-1]])
3. Feeding historical charts and asking what entry would have worked → hindsight bias: The rules are trained on known outcomes. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C15-2|C15-2]])
4. Embedding the researcher's causal logic in the prompt → a more structurally sound answer: The prompt steers pattern recognition. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C15-X1|C15-X1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C15-3|C15-3]])
- Evidence: Own tests and anecdotes; no systematic study.
- Fails when: Use LLMs for debugging and code porting where they excel.

**Decision process**
- [portfolio] Use a system ensemble: about 10 structurally uncorrelated trend systems across 60-70 markets (500-600 return streams).. Why: Correlations among markets change on a dime with politics; structure guards against that. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-3|C05-3]])
- [universe] At $200k run about 10 uncorrelated markets with 5 ensemble systems; widen to ~30 markets at $400k and ~60 at $1M, adding standard contracts.. Why: Small capital cannot size equal risk per bet across 100 markets; hidden correlation and ruin. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C12-2|C12-2]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C12-3|C12-3]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C13-1|C13-1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C13-X1|C13-X1]])
- [sizing] ATR-based normalisation with equal risk per bet.. Why: Equalises risk across markets of different volatility. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C13-1|C13-1]])
- [research] Build the continuous back-adjusted series yourself (Panama method) with a single consistent roll trigger (open interest, volume or calendar) and re-adjust at each new roll.. Why: Ensures backtest matches live trading and understands the bias. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C08-3|C08-3]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C09-1|C09-1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C09-2|C09-2]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C09-3|C09-3]])
- [signal] Avoid absolute price thresholds, long-lookback percent returns, mean reversion to long averages and fixed dollar stops; use adjustment-agnostic indicators.. Why: Back-adjustment shifts price levels. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C10-1|C10-1]])
- [research] Keep backtest roll logic identical to live; use data including delisted contracts; act only on available OHLC points.. Why: Avoid backtest/live divergence and survivorship bias. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C10-2|C10-2]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C10-3|C10-3]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C10-4|C10-4]])
- [research] Extend short micro/nano histories with a proxy (standard contract on the same exchange with similar price structure, scaled for tick size and value), backtesting on 20-40 years; fallback is overlap or normalisation splicing.. Why: Three years of data overfits one regime. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C11-2|C11-2]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C12-1|C12-1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C11-1|C11-1]])
- [execution] Use platforms that integrate robustness testing and live broker execution; check per-contract fees on small contracts.. Why: Narrows the backtest-to-live gap; fixed fees hurt nanos. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C07-X1|C07-X1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C08-1|C08-1]])
- [research] Use LLMs for debugging syntax and porting code, but validate every output with causal logic and human review.. Why: LLMs cannot judge conceptual soundness (e.g. convexity of exit logic). ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C15-3|C15-3]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C15-X1|C15-X1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C14-X2|C14-X2]])

**Evidence style:** Practitioner experience and first-principles argument (robustness, causal logic); hypotheticals for capital growth; anecdotes and own LLM experiments; little quantitative performance evidence offered.

**Views at the time**
- (2025-06-11) Trend followers are deep in drawdown; April 2025 was cruel and May gave little respite; the SG Trend Index touched or slightly exceeded its worst monthly drawdown.. Reasoning: Tariff whipsaws across all sectors. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C02-1|C02-1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C02-X1|C02-X1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C04-1|C04-1]])
- (2025-06-11) The April-regime of whipsaws should not last long because a direction must emerge from the uncertainty.. Reasoning: Uncertainty is not sustainable; hope more than data. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C04-1|C04-1]])
- (2025-06-11) Idiosyncratic single-market trends are in favour in the post-2020 fragmented, deglobalising world.. Reasoning: Lost central bank coordination and geopolitical fragmentation. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C03-3|C03-3]])
- (2025-06-11) Retail trend following is viable from about $200k with micro/nano futures.. Reasoning: Enough diversification and skin in the game. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C12-2|C12-2]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C13-1|C13-1]])

### Niels Kaastrup-Larsen (Host, Top Traders Unplugged; 35 years in trend following)
Fingerprint: #approach/trend_following #approach/regime_detection #approach/debt_cycle_long_term #approach/diversification_risk_parity #approach/costs_execution #approach/manager_selection_allocation
_Speaker note: Host who states views on trend drawdowns, diversification and AI; also reads index data. Ledger attributes C02-1 wrongly to him (correction: Brennan); C08-1 is mixed (Niels asks the fee question)._

**Worldview premises**
- Trend following is still relevant because policy breaks will eventually produce trends a long/short manager can capture; the 'markets have changed, trend is dead' argument recurs in every drawdown. _[experience, stated; support: 35 years of experience; reasoning about reckless policy.]_ ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C06-2|C06-2]])
- Rising global debt, weak bond auctions in Japan and the US and a US 10-year that may settle above 5% mean institutions built portfolios for the old regime; cracks can produce trends with follow-through. _[theoretical, stated; support: Observed cracks in auctions; no data.]_ ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C04-2|C04-2]])
- A 12-14 month drawdown is not unusual and 2-3 months of strong follow-through in a few sectors can recover it. _[experience, stated; support: Repeated drawdowns over his career.]_ ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C04-3|C04-3]])
- Reversals in currencies, bonds and equities together is the worst case for trend in financial sectors; very large managers must tilt to financials and lose commodity diversification. _[theoretical, stated; support: Reasoning on capacity; his own speculation ('maybe this is the reason').]_ ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-1|C05-1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-2|C05-2]])
- Trading 70-80 less correlated markets may beat hundreds that eventually become highly correlated; combining structurally different trend types is an underappreciated diversification. _[experience, stated; support: Prior podcast discussions; agrees with Brennan.]_ ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-4|C05-4]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-X1|C05-X1]])
- Repeated reversals force much more dynamic risk budgeting across CTAs than the usual gradual change. _[empirical, stated; support: His inference from market moves ('I imagine').]_ ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C06-1|C06-1]])

**Decision process**
- [research] Track a trend barometer (36 in early June 2025: weak) and CTA index returns as a read on the environment.. Why: Reading the pulse of the industry. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-5|C05-5]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-6|C05-6]])
- [other] Prefer to know why one is long or short; sceptical of machine-learning patterns whose reasons are unclear because poor performance is hard to explain to investors.. Why: Explainability and investor trust. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C02-2|C02-2]])

**Evidence style:** Industry data, news articles (FT on AQR), anecdotes from guests, and long experience.

**Views at the time**
- (2025-06-11) Early June 2025: BTOP50 -4% YTD, SG CTA -8%, SG Trend -11%, short-term traders -3%, versus MSCI World +6.3% and S&P 500 TR +2%.. Reasoning: Reported data. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-6|C05-6]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-5|C05-5]])
- (2025-06-11) The 12-14 month drawdown is deep but not unprecedented and could recover quickly with follow-through.. Reasoning: Past drawdowns. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C04-3|C04-3]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-1|C05-1]])
- (2025-06-11) Debt build-up and bond-auction cracks will produce trends; trend is arguably more relevant than ever.. Reasoning: Illogical policy, fiscal strain. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C04-2|C04-2]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C06-2|C06-2]])
- (2025-06-11) AQR's adoption of machine learning improves returns so far but makes underperformance hard to explain.. Reasoning: FT article. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C02-2|C02-2]])

### Disagreements
- **How to get diversification: more markets or more systems**: Richard Brennan: Add structurally uncorrelated trend systems (ensemble) across 60-70 markets rather than relying on market count. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-3|C05-3]]); Niels Kaastrup-Larsen: Agrees system diversity is underappreciated; frames a smaller set of 70-80 less correlated markets as better than hundreds. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-4|C05-4]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-X1|C05-X1]])
- **Why big established managers have their worst drawdowns**: Richard Brennan: Their correlation-conscious, vol-targeted design was built for the globalised, coordinated 2008-2020 regime. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C03-3|C03-3]]); Niels Kaastrup-Larsen: Their size forces a tilt to financial futures, losing commodity diversification, in a year when financials reversed repeatedly. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-1|C05-1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-2|C05-2]])

### Gaps and conflicts
- The two-tribe explanation is a narrative without performance data separating the tribes, and Brennan concedes many managers lie between the extremes. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C02-3|C02-3]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C02-4|C02-4]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C03-2|C03-2]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C03-3|C03-3]])
- Hope that the April regime will end soon is unsupported ('crossing my fingers'); the trend-persistence premise rests on a theoretical belief in complex adaptive systems. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C04-1|C04-1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C08-2|C08-2]])
- Niels's explanation that size forced big managers into financials is speculative ('maybe') and conflicts in emphasis with Brennan's regime-correlation explanation. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-2|C05-2]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C03-3|C03-3]])
- Capital path ($200k to $400k to $1M) is hypothetical and explicitly flagged as unknowable by the host. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C13-X1|C13-X1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C13-1|C13-1]])
- Retail-feasibility claim of $200k as the sweet spot is an opinion based on available micro products, with no cost or performance analysis; fee impact on nanos is only partly addressed. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C12-2|C12-2]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C08-1|C08-1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C07-1|C07-1]])
- LLM critique relies on a single prompt experiment and a Substack anecdote; Niels's AQR example (ML helps returns) is not reconciled. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C14-2|C14-2]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C14-X1|C14-X1]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C02-2|C02-2]])
- Trend barometer and index returns are recitation with no forecast content. ([[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-5|C05-5]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C05-6|C05-6]], [[MT181 - The Two Tribes of Trend - Systematic Investor - Ep.351#^MT181-C06-1|C06-1]])

### Forward-looking inputs (reader synthesis)
(reader) Brennan: resolution of tariff uncertainty into a directional regime; fragmentation versus coordination among central banks (correlation regime); persistence of idiosyncratic commodity trends. Niels: global debt levels, weak government bond auctions and 10-year yields settling above 5%, breakouts following policy cracks. Horizons: months for drawdown recovery, years for regime.

### Reader inferences (not stated by the speakers)
- (reader) Brennan's regime story implies an observable input: the cross-market correlation level, with high correlation favouring cross-sectional/vol-targeted trend and low correlation favouring single-market trend.
- (reader) The data and LLM sections share one principle: any process that fits to known outcomes (adjusted history, short sample, LLM hindsight) overfits; robustness comes from structural logic.
- (reader) The two speakers do not truly conflict; they offer complementary explanations of the 2024-25 drawdown (regime of correlation vs capacity-driven sector tilt).

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, sponsor disclaimers, Japanese pen-tracking gadget (no method content) |
| C02 | 4 | AQR adopts machine learning; trend drawdowns; definition of idiosyncratic vs correlation-conscious trend |
| C03 | 3 | two tribes of trend: idiosyncratic versus correlation-conscious, history and regimes |
| C04 | 3 | April 2025 tariff whipsaw; debt and yields; drawdown length |
| C05 | 6 | multiple reversals, size and sector tilt, ensemble diversification, index returns |
| C06 | 2 | dynamic risk budgeting, is trend dead, teaser for data topics |
| C07 | 1 | democratization of retail futures trading, micro and nano contracts |
| C08 | 3 | nano fees, trends persist, why futures data and back-adjusting matter |
| C09 | 3 | Panama method, roll trigger, CSI data |
| C10 | 4 | adjustment bias in indicators, roll logic, survivorship, granularity |
| C11 | 2 | limited history of new contracts, proxies, tick scaling |
| C12 | 3 | splicing, minimum capital $200k, over-diversification trap |
| C13 | 1 | scaling ladder of markets with capital, AI segment starts |
| C14 | 2 | LLM limits: plausible text not causality, generic indicator stitching |
| C15 | 3 | LLM mass optimization, hindsight bias, blind debugging, Claude Opus 4 anecdote |
| C16 | 0 | AI-risk anecdotes (Tudor Jones, Musk robots), closing; nothing actionable |
| C17 | 0 | outro |

## Claims

### C02
- **Niels Kaastrup-Larsen** Trend followers were in deep drawdowns in spring 2025, with the SG Trend Index touching or slightly exceeding its worst monthly drawdown in history.  #mech/cycle_persistence _(time-bound view)_
  > AQR had better get a good reason for why the industry is going into their draw downs because we we're deep in our draw downs at the moment
  indicator: SG Trend Index drawdown · asset: multi · horizon: months · testable: yes: index drawdown is observable · confidence: high
  **Correction (cross-check):** Wrong speaker: the lines about AQR needing a good reason, April and May being cruel, and the SG Trend Index touching or exceeding its worst monthly drawdown are said by Richard Brennan (answering Niels's AQR remark), not by Niels Kaastrup-Larsen. → Richard Brennan: trend followers are deep in drawdown in spring 2025, April was particularly cruel and May gave little respite, and the SG Trend Index just touched or slightly exceeded the worst monthly drawdown in its history.
  ^MT181-C02-1
- **Niels Kaastrup-Larsen** AQR now uses machine learning to find market patterns even when the reason is unclear, which may help returns but makes poor performance hard to explain to investors; trend followers prefer knowing why they are long or short.  #mech/research_method _(time-bound view)_
  > The article mentioned that the shift has so far it's obviously a short time period uh improved returns but he also acknowledges uh Cliff that there are some drawbacks and that is how do you explain poor performance to investors?
  asset: multi · testable: no: opinion about explainability · confidence: medium
  ^MT181-C02-2
- **Richard Brennan** Idiosyncratic trend followers treat each market as independent and trade time-series momentum market by market, the traditional cut-losses-short approach of the 70s to 90s.  #mech/structural_shift
  > those that treat each individual market as independent and they're looking at time series momentum in an individual market
  indicator: time-series momentum per market · asset: multi · horizon: months · testable: yes: separable from cross-sectional trend in a backtest · confidence: high
  ^MT181-C02-3
- **Richard Brennan** Correlation-conscious trend followers look at groupings, asset classes and complexes (cross-sectional view) and manage portfolio correlation and volatility targeting; the industry split into these two styles in the early 2000s.  #mech/structural_shift
  > the correlation conscious segment those that treat trend following more in a cross-sectional viewpoint. They're looking at groupings, asset classes, complexes, um things that are trending.
  indicator: cross-sectional trend, correlation-aware sizing · asset: multi · horizon: months · testable: yes: the two styles can be implemented and compared · confidence: high
  ^MT181-C02-4
- **Richard Brennan** Deep drawdowns are an inherent feature of trend-following models (including for the longest-established managers), so they are expected to recur and the process is simply to wait for the next high-water mark.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > it's inevitable that um these periods occur with the nature of our models
  asset: multi · testable: yes - historical drawdown frequency and depth of trend indices · confidence: high
  ^MT181-C02-X1

### C03
- **Richard Brennan** Large trend managers cut target volatility from about 25% to 10-12% in the early 2000s to attract institutional assets, using correlation reduction and vol targeting, which smoothed returns at the cost of the two-way volatility of the classic style.  #mech/risk_management
  > They reduced their volatility. there was a significant attempt to reduce volatility and in that process um they looked at how do they reduce volatility
  indicator: target volatility 10-12% vs 25% · asset: multi · horizon: years · testable: yes: vol target is a parameter · confidence: high
  ^MT181-C03-1
- **Richard Brennan** Correlation-conscious trend following did very well from 2008 to 2020 because globalization and coordinated central bank policy made markets more causally correlated, which cross-sectional grouping could exploit.  #mech/structural_shift _(time-bound view)_
  > post um 2008 and I attributed that to a particular regime that was in place in globalization central bank coordination
  asset: multi · horizon: years · conditions: works in a globalized, centrally coordinated regime · testable: partly: regime dating is subjective · confidence: medium
  ^MT181-C03-2
- **Richard Brennan** After 2020 deglobalization, fragmentation and loss of central bank coordination made assets less correlated, favouring idiosyncratic trends (cocoa, soybeans, gold) and hurting the large correlation-conscious managers.  #mech/structural_shift _(time-bound view)_
  > I saw that the rise again of the idiosyncratic trend follower from 2020 up to 2024 and I saw a a a reduced performance of what I call a correlation conscious trend follower over that period
  asset: multi · direction: favor idiosyncratic single-market trend over cross-sectional grouping · horizon: years · conditions: works in fragmented, deglobalizing regime · testable: partly: compare the two styles by subperiod · confidence: medium
  ^MT181-C03-3

### C04
- **Richard Brennan** April 2025 tariff announcements hit equities, commodities and currencies at once and caused massive whipsaws for all trend followers; the speaker expects this regime not to last because a direction must emerge.  #mech/behavioral _(time-bound view)_
  > I'm associating that with the tariff policies. I'm associating that with the fact that these tariff policies were so widespread in their impact.
  asset: multi · horizon: months · testable: no: view about a policy episode · confidence: medium
  ^MT181-C04-1
- **Niels Kaastrup-Larsen** Rising global debt, weak bond auctions in Japan and the US and a 10-year yield that may settle above 5% mean institutions built portfolios for the old regime; when cracks appear trends can emerge with follow-through.  #mech/fiscal_debt _(time-bound view)_
  > what happens in in in this world if if 10 year interest rates settle above 5% and 75% is kind of your low point rather than zero
  indicator: US 10-year yield above 5% · asset: rates · horizon: years · conditions: trends follow once policy cracks appear · testable: partly: yield level is observable, outcome is a view · confidence: medium
  ^MT181-C04-2
- **Niels Kaastrup-Larsen** A 12-14 month trend-following drawdown is not unusual, and 2-3 months of strong follow-through in a few sectors can recover it.  #mech/cycle_persistence _(time-bound view)_
  > it's a draw down that's now running at 12 14 months but that in itself is not unusual uh frankly
  indicator: trend-following drawdown duration · asset: multi · horizon: months · testable: yes: drawdown durations can be measured historically · confidence: high
  ^MT181-C04-3

### C05
- **Niels Kaastrup-Larsen** The 2024-25 drawdown was unusual because currencies, bonds and equities all reversed several times, which is the worst case for trend following in financial sectors.  #mech/overshoot _(time-bound view)_
  > all three big financial sectors currencies bonds and um and equities they have all had significant reversals but also multiple reversals
  asset: multi · horizon: months · testable: yes: count trend reversals by sector · confidence: high
  ^MT181-C05-1
- **Niels Kaastrup-Larsen** Very large managers must tilt risk to liquid financial futures rather than commodities, losing diversification, which may explain why big established firms had their worst drawdowns.  #mech/risk_management
  > the size have meant that they had to tilt the risk towards financial markets rather than commodities
  asset: multi · direction: commodities give diversification for smaller managers · horizon: years · conditions: large AUM · testable: partly: need manager-level sector risk data · confidence: medium
  ^MT181-C05-2
- **Richard Brennan** Diversify with a system ensemble: about 10 structurally uncorrelated trend systems across 60-70 markets (500-600 return streams) rather than just adding correlated markets, because market correlations change quickly with politics.  #mech/risk_management
  > you might have 500 600 return streams comprising say 60 70 markets but 10 uncorrelated trend following systems to create 600 return streams
  indicator: ensemble of uncorrelated trend systems · asset: multi · horizon: years · testable: yes: measure correlation among system return streams · confidence: high
  ^MT181-C05-3
- **Niels Kaastrup-Larsen** Trading 70-80 less correlated markets may be a better bet than hundreds of eventually highly correlated markets.  #mech/risk_management
  > trading hundreds of markets versus trading maybe 70 or 80 that are less correlated and maybe a a better bet for your portfolio than just trading you know hundreds of markets which eventually will be much highly correlated
  asset: multi · horizon: years · testable: yes: compare diversification versus market count · confidence: medium
  ^MT181-C05-4
- **Niels Kaastrup-Larsen** A trend barometer reading of 36 (weak) goes with a challenging environment for trend following.  #mech/cycle_persistence _(time-bound view)_
  > my trend barometer stood at 36. So, still a little bit, uh, weak and and therefore we are still seeing, you know, some challenging um environment for for for trend following
  indicator: trend barometer (36) · asset: multi · horizon: months · testable: yes: barometer readings vs subsequent trend returns · confidence: medium
  ^MT181-C05-5
- **Niels Kaastrup-Larsen** Early June 2025 data: BarclayHedge BTOP50 -4% YTD, SG CTA index -8%, SG Trend about -11%, short-term traders -3%, MSCI World +6.3%, S&P 500 total return +2%.  #mech/cycle_persistence _(time-bound view)_
  > the Btop 50 is up 48 basis points, down only 4% for the year now. Sockchen CTA index also up about 43 basis points. It's down about 8% for the year.
  indicator: BTOP50, SG CTA, SG Trend, SG Short Term Traders index returns · asset: multi · horizon: months · testable: yes: published index figures · confidence: high
  ^MT181-C05-6
- **Niels Kaastrup-Larsen** Combining several structurally different types of trend following is an underappreciated form of diversification, because most managers run only one or two types and rely on multiple time frames instead.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > I think that's definitely a an underappreciated form of diversification because most managers use one or two different types of of trend following
  asset: multi · conditions: different system types, not just different lookbacks · testable: yes - correlation of distinct trend systems vs multi-lookback variants of one system · confidence: high
  ^MT181-C05-X1

### C06
- **Niels Kaastrup-Larsen** Repeated reversals forced much more dynamic risk budgeting in spring 2025, with big swings in total CTA risk rather than the usual gradual change.  #mech/risk_management _(time-bound view)_
  > I imagine um that actually risk budgeting has been quite dynamic the last couple of months meaning that we've actually seen big changes in the overall risk of CTAs.
  asset: multi · horizon: months · testable: partly: needs CTA risk exposure data · confidence: low
  ^MT181-C06-1
- **Niels Kaastrup-Larsen** Trend following is still relevant because policy breaks will eventually produce trends a long/short manager can capture; the argument that markets have changed and trend is dead recurs in every drawdown.  #mech/cycle_persistence _(time-bound view)_
  > maybe trend following is more relevant today than it's ever been because there's no logic in many of the things that is happening in the world
  asset: multi · horizon: years · testable: no: belief about the future · confidence: high
  ^MT181-C06-2

### C07
- **Richard Brennan** Mini, micro and nano futures (about 1/10, 1/100, 1/1000 of a standard lot) plus institutional-grade software let retail traders reach the diversification once needing $1-2 million.  #mech/structural_shift
  > mini contracts, micro contracts and in some cases what we call nano contracts
  indicator: mini/micro/nano futures contract sizes · asset: multi · horizon: years · testable: no: market-structure observation · confidence: high
  ^MT181-C07-1
- **Richard Brennan** Platforms such as QuantConnect and StrategyQuant X offer built-in robustness testing and link the backtest workflow to live broker execution (e.g. Interactive Brokers), narrowing the gap between backtest and live trading for retail trend followers.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > These are institutional-grade platforms that have incredible degrees of data analysis in it, robustness in it, the ability to robustly test your models.
  asset: multi · testable: no - tooling claim, not a market hypothesis · confidence: medium
  ^MT181-C07-X1

### C08
- **Niels Kaastrup-Larsen** Fixed per-contract commissions hurt small contracts: $5 each way on a nano costs far more relative to notional than on a standard contract at the same number of round turns; percentage fees scaled to lot size fix this.  #mech/risk_management
  > do brokers/ exchanges charge the same fee for a nano as that?
  indicator: commission per round turn vs contract size · asset: multi · testable: yes: cost model per contract size · confidence: medium
  **Correction (cross-check):** Mixed attribution: Niels only asks whether brokers charge the same per-contract fee for a nano as for a standard contract; the answer that fees are increasingly percentage-based and scaled to lot size is Richard Brennan's (and is stated as a general observation, not a guarantee that the problem is fixed). → Niels Kaastrup-Larsen: a flat $5 each way on a nano costs far more relative to notional than on a standard contract at the same number of round turns. Richard Brennan: many venues now charge percentage fees scaled to lot size, similar to standard contracts.
  ^MT181-C08-1
- **Richard Brennan** Trends will persist because they are an inherent property of complex adaptive systems, although the participants in trend following will change.  #mech/cycle_persistence
  > I believe in complex adaptive systems and um trends are an inherent nature of complex adaptive systems.
  asset: multi · horizon: years · testable: no: philosophical premise · confidence: high
  ^MT181-C08-2
- **Richard Brennan** Unadjusted stitched futures contracts contain artificial jumps at each roll that create false signals, so continuous back-adjusted series are required and should be built by the researcher.  #mech/research_method
  > If you back test the the raw data contracts, the gaps between the contracts are illusions and result in false signals if you don't adjust them.
  indicator: back-adjusted continuous futures series · asset: multi · testable: yes: compare signals on raw versus adjusted data · confidence: high
  ^MT181-C08-3

### C09
- **Richard Brennan** The Panama (difference) method keeps the current contract price and subtracts each roll gap from all earlier history, so the history must be re-adjusted at every new roll and early prices can turn negative in backwardation.  #mech/research_method
  > the price of the front contract remains as is but you adjust the prior contracts to that every time you've got a new contract emerging
  indicator: Panama difference back-adjustment · asset: multi · testable: yes: implementable and checkable · confidence: high
  ^MT181-C09-1
- **Richard Brennan** Define one consistent roll trigger (open interest, volume or calendar) and observe the price gap at the roll to compute the adjustment.  #mech/research_method
  > you need to define a consistent roll trigger. In other words, do you use open interest in the next contract or do you use volume or do you use the calendar to decide when to roll?
  indicator: roll trigger: open interest, volume or calendar · asset: multi · testable: yes: roll rule is a parameter · confidence: high
  ^MT181-C09-2
- **Niels Kaastrup-Larsen** CSI Data is named as a low-cost, clean futures data source with user-selectable roll and adjustment methods.  #mech/research_method
  > there is a very I would say inexpensive solution uh from a company in the US that have been doing this since the 70s and uh I think are known for having very clean data and that's CSI data
  indicator: CSI futures data · asset: multi · testable: no: vendor recommendation · confidence: high
  ^MT181-C09-3
- **Richard Brennan** Some backtest engines cannot handle the negative historical prices that Panama back-adjustment can create, in which case another adjustment method must be chosen, although most modern engines accept negative prices.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > some back testing engines don't like that. They don't like negative prices and they work won't work on it
  indicator: Panama back-adjusted continuous futures series · asset: commodities · conditions: backwardated markets with long history; engine that rejects negative prices · testable: yes - run the same system on difference-adjusted vs ratio-adjusted series · confidence: high
  ^MT181-C09-X1
- **Richard Brennan** Under Panama adjustment contango markets have their historical prices raised (and backwardated ones lowered), so only the current front contract shows the true live price while all earlier history is shifted.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > in contango where you find that the the future contracts are higher priced than the the current contract uh you find that the back adjustment process raises the prices
  indicator: roll gap between contracts (term-structure shape) · asset: commodities · direction: contango raises historical prices · conditions: difference (Panama) back-adjustment only · testable: yes - arithmetic property of the adjustment · confidence: high
  ^MT181-C09-X2

### C10
- **Richard Brennan** Because back-adjustment shifts historical price levels, avoid rules based on absolute price thresholds, long lookback percent returns, mean reversion to long averages and fixed dollar stops; use indicators agnostic to adjustment bias.  #mech/research_method
  > So you've got to avoid things that adopt absolute price thresholds. For instance, buy if crude is greater than $100 or sell if gold is less than $1,500.
  indicator: price-level-independent indicators · asset: multi · testable: yes: test signal sensitivity to adjustment method · confidence: high
  ^MT181-C10-1
- **Richard Brennan** Backtest roll logic must match live roll logic, otherwise backtest and live results diverge.  #mech/research_method
  > If you have a different roll logic, you're going to get a different
  asset: multi · testable: yes: compare results under two roll rules · confidence: high
  ^MT181-C10-2
- **Richard Brennan** Futures backtests suffer survivorship bias when delisted contracts and dead symbols are omitted, so use data including them.  #mech/research_method
  > You've got to try and use data that uh shows these delisted contracts, shows the dead symbols.
  asset: multi · testable: yes: compare universes with and without dead contracts · confidence: high
  ^MT181-C10-3
- **Richard Brennan** Data granularity must match execution: with only daily open-high-low-close data, rules should act only on those points and not infer positions between them.  #mech/research_method
  > using daily data when your signals are executed intraday
  indicator: OHLC daily data · asset: multi · testable: yes: compare daily versus intraday execution · confidence: high
  ^MT181-C10-4

### C11
- **Richard Brennan** A backtest should stress test models and find where they break, not estimate future returns; aim for robustness across regimes rather than curve fitting to one regime or market.  #mech/research_method
  > Your back test environment is where you stress test your models. Determine where they break.
  asset: multi · testable: partly: robustness criteria are definable · confidence: high
  ^MT181-C11-1
- **Richard Brennan** For new micro/nano contracts with about three years of data, extend history with a proxy: the standard contract on the same exchange with similar price structure (scaled for tick size and tick value), and backtest on 20-40 years of that.  #mech/research_method
  > you look on for instance something like CSI data for a standard contract of that same market that exists on the same exchange and hopefully has a similar price structure
  indicator: standard contract as proxy for micro contract · asset: multi · testable: yes: proxy and scaling are explicit · confidence: high
  ^MT181-C11-2

### C12
- **Richard Brennan** Alternative to proxies: overlap-based or normalization-based splicing of two similar series; try proxies first.  #mech/research_method
  > you can either overlap um splicing that that's where you have two contracts traded side by side for a period of time
  indicator: splicing of overlapping series · asset: multi · testable: yes: standard technique · confidence: medium
  ^MT181-C12-1
- **Richard Brennan** Roughly $200,000 is the minimum capital for a diversified retail trend program using micro/mini/nano futures, with enough skin in the game for discipline.  #mech/risk_management
  > $200,000 is basically what I'd regard as the minimum capital you need to adopt a suitable trend following process that gives a degree of diversification
  indicator: minimum capital $200,000 · asset: multi · testable: partly: sizing granularity can be simulated · confidence: medium
  ^MT181-C12-2
- **Richard Brennan** Trap one: with small capital, over-diversifying across 100 markets makes it impossible to size equal risk per bet, leaving hidden correlation and risk of ruin.  #mech/risk_management
  > They diversify as far as they can and they fragment their risk with too much diversification and um with that limited set of capital you cannot position size correctly
  asset: multi · conditions: limited capital · testable: yes: simulate position rounding at small capital · confidence: high
  ^MT181-C12-3
- **Richard Brennan** Limited capital is an advantage for a retail trend follower because it forces a lean process with no waste, no overfitting and no extreme risk, and enough money at stake keeps the trader careful and disciplined.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > constraint in this case is the edge. When you don't have um unlimited capital, you're forced to make every piece of your process count
  asset: multi · conditions: retail futures trader around $200k · testable: no - behavioural assertion about discipline · confidence: medium
  ^MT181-C12-X1

### C13
- **Richard Brennan** At $200k run about 10 uncorrelated markets with 5 ensemble systems and ATR-based equal-risk sizing, then widen to about 30 markets at $400k and 60 markets at $1 million, adding standard contracts.  #mech/risk_management
  > with levels of capital of about $200,000 you can comfortably allocate into about 10 uncorrelated markets. You can have five ensemble systems and you can deploy ATRbased normalization
  indicator: ATR-normalized equal risk per market · asset: multi · testable: yes: define and simulate the scaling ladder · confidence: medium
  ^MT181-C13-1
- **Niels Kaastrup-Larsen** The capital growth path from $200k to $400k to $1m used to illustrate when to add markets is hypothetical; actual performance and size are unknowable in advance, and the point is only that more assets allow more markets and systems.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > we have no way of knowing how how the portfolio will will evolve in terms of
  asset: multi · horizon: years · conditions: illustration, not a forecast · testable: no - illustrative scenario · confidence: high
  ^MT181-C13-X1

### C14
- **Richard Brennan** Large language models predict plausible text, not causal relationships, so strategies they propose look polished but lack robustness under stress and overfit.  #mech/research_method
  > they're actually pattern recognizing statistical models that predict plausible text. They predict plausible text, not the causal relationships.
  asset: multi · testable: partly: LLM-generated strategies can be backtested out of sample · confidence: high
  ^MT181-C14-1
- **Richard Brennan** An LLM asked for a crude oil system returned a forum-favourite SMA crossover with RSI and ATR filters, not based on oil's volatility regime, seasonality or term structure, so it only works because it is tuned to past conditions.  #mech/research_method
  > I asked Chat GPT for a crude oil trading system. It gave me an SMA crossover with an RSA or RSI and ATR filters.
  indicator: SMA crossover with RSI and ATR filters · asset: commodities · testable: yes: backtest out of sample · confidence: high
  ^MT181-C14-2
- **Richard Brennan** LLMs produce fluent, authoritative answers that can be false (even inventing books and citations) and claim to have read material they have not, because they lack verifiable truth-checking and symbolic reasoning, so every output used in strategy work must be validated.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > it's confidently wrong. It's giving authoritative sounding answers that are factually false
  asset: multi · conditions: any LLM-assisted research step · testable: partly - hallucination rates can be audited, not market-testable · confidence: high
  ^MT181-C14-X1
- **Richard Brennan** LLMs suit language, coding and pattern recognition, whereas causal reasoning needs other kinds of AI or mathematical models, so the type of AI should be matched to the task rather than treating AI as one universal fix.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > large language models are good for a particular purpose and function. But there are other different AI models for causal reasoning
  asset: multi · testable: no - qualitative tooling judgement · confidence: medium
  ^MT181-C14-X2
- **Richard Brennan** An LLM that surfaces a trading model has shown only that it is widely discussed in online communities, which it treats as evidence that it works, not that it is causally effective.  #mech/behavioral _(added by map cross-check)_
  > because they're pattern recognition there's been lots of mention of these models in the communities
  indicator: popularity of a model in online forums · asset: multi-asset · conditions: LLM used to generate strategies without causal guardrails · testable: partly - compare LLM-suggested strategies out of sample · confidence: high
  ^MT181-C14-R1

### C15
- **Richard Brennan** Auto-generating hundreds of strategies with AI and backtesting them is mass data mining that produces false positives which die in live trading unless regime validation and structural filters are applied.  #mech/research_method
  > Some traders use AI to generate hundreds of rule sets then auto back test them looking for alpha. But what's really happening there is this curve fitting on steroids.
  asset: multi · testable: yes: multiple-testing correction measurable · confidence: high
  ^MT181-C15-1
- **Richard Brennan** Feeding historical charts to an LLM and asking what entry would have worked creates hindsight bias; rules trained on known outcomes fail when uncertainty is real.  #mech/research_method
  > You're asking AI to reverse engineer entries from known outcomes.
  asset: multi · testable: yes: enforce point-in-time information · confidence: high
  ^MT181-C15-2
- **Richard Brennan** LLMs are useful for debugging syntax and porting code, but cannot judge whether a system is conceptually sound, for example whether exit logic destroys convexity; human validation with causal logic is needed.  #mech/research_method
  > the model can check if your code runs but it can't tell you if your system is conceptually sound or if your exit logic destroys for instance your convexity
  asset: multi · testable: no: judgement · confidence: high
  ^MT181-C15-3
- **Richard Brennan** Prompts are the control point for LLM use: embedding the researcher's own causal logic in the prompt steers the model's pattern recognition toward a structurally sound answer, whereas blind use yields the overfitting and hindsight problems described.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > prompts are critical for chat GPT. That's where the prompt is actually embedding causal logic into the syntax
  asset: multi · conditions: human supplies the causal hypothesis; LLM implements · testable: no - process advice · confidence: medium
  ^MT181-C15-X1

