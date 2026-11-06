---
source_id: MT221
title: "Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381"
date: 2026-01-03
channel: "Top Traders Unplugged"
url: 
words: 11793
claims: 59
added_by_crosscheck: 25
corrections: 4
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Niels Kaastrup-Larsen (host)", "Katie Kaminski (CTA researcher)", "Jim Kasang (volatility)", "Rob Carver (systematic trader)", "Mark Rzepczynski (CTA manager)", "Rich Brennan (CTA researcher)", "Alan Dunne (CTA researcher)", "Nick Baltas (researcher)", "Andrew Beer (replication ETF manager)", "Yoav Git (CTA manager)"]
tags: [source, layer0]
---
# Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381

**Speakers:** Niels Kaastrup-Larsen (host); Katie Kaminski (CTA researcher); Jim Kasang (volatility); Rob Carver (systematic trader); Mark Rzepczynski (CTA manager); Rich Brennan (CTA researcher); Alan Dunne (CTA researcher); Nick Baltas (researcher); Andrew Beer (replication ETF manager); Yoav Git (CTA manager)

**Summary:** Top Traders Unplugged year-end panel part two with ten systematic managers. Topics: total portfolio approach, long volatility, process stability, drawdown nature of CTAs, high-vol products and 2026 predictions. Conclusion: do not change trend models after pain, 2023-25 drawdown was volatility compression, and CTA allocations are far below optimal.

**Approach:** trend following, CTA, long volatility, portfolio construction

**Cross-check completeness estimate of first read:** 0.60 - the first reader caught the main TPA, process-stability, drawdown-structure and Sharpe/vol-compression arguments; it missed the AI-use remark, several allocator-behaviour mechanisms (narrative, iron spine, ETF drawdown visibility, no-single-event drawdowns, long vs deep), the Katie, Yov and Andrew 2026 predictions, and misattributed two C03 claims and the Barclay-vol statement.

## Argument map

**Episode thesis:** A ten-manager year-end panel argues that (1) total-portfolio optimisation theoretically implies far larger CTA allocations than the roughly 50bp most US institutions hold, but flows follow performance and career risk, so TPA will not change much quickly; (2) the 2023-25 trend drawdown is explained by volatility compression and a share of winning markets below break-even, not by model failure, so managers should not change models after pain and should stay true to their stated thesis; (3) CTA drawdowns come from nothing happening, are long rather than deep, and are smaller than perceived; and (4) long volatility and trend following provide true diversification that stock-bond mixes do not. The panel also debates high-vol products, capital efficiency and 2026 predictions (higher yields, 2022-like, roller coaster).

### Yoav Git (CTA manager (Israel); sells non-financialized trend risk factors)
Fingerprint: #approach/trend_following #approach/research_robustness_overfitting #approach/portfolio_construction_stacking #approach/regime_detection #approach/diversification_risk_parity #approach/costs_execution
_Speaker note: Ledger labels 'Yov'. Caption spelling varies. Assumed to be the speaker of C02, C07-C08 and C10-C11 per flow; turn boundaries rely on host cues._

**Worldview premises**
- Total-portfolio mean-variance optimisation implies a very large CTA allocation because of diversification (about 1/3 of risk even at CTA Sharpe 0.5 vs 1.5 for the rest), but flows follow performance, so TPA will not change allocations much. _[theoretical, stated; support: Simple optimisation arithmetic; observation that flows chase performance.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C02-1|C02-1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C02-2|C02-2]])
- CTA exposure should be matched to hedge the asset classes an allocator already holds; bucket-style allocation leaves CTAs at ~2%, too small to alter convexity. _[theoretical, stated; support: Long-held argument.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C02-3|C02-3]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C02-X2|C02-X2]])
- Recent CTA underperformance came from fewer outsized trends (volatility compression), not model breakdown; test it by measuring Sharpe extracted from markets that trended at a given underlying Sharpe versus history. _[empirical, stated; support: Measurement logic; says it is roughly unchanged for most CTAs.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C07-1|C07-1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C11-1|C11-1]])
- CTA drawdowns come from nothing happening, like buying straddles paid for via trading costs; only ~40% of markets need to win for a good year, and a drawdown comes when winners fall to 30-35%. _[theoretical, stated; support: Straddle analogy.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C10-1|C10-1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C10-2|C10-2]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C11-1|C11-1]])
- Drawdowns have no single event to blame, so they are harder for allocators to explain to an investment committee; they are long rather than deep. _[experience, stated; support: Allocator conversations.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C11-X1|C11-X1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C11-X2|C11-X2]])
- A manager should stay true to the style the investor hired (e.g., non-financialized markets, fast trend) and change only when the underlying market properties change. _[experience, stated; support: Example: iron ore front month where ~70% of volume is CTAs.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C08-1|C08-1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C08-X1|C08-X1]])
- AI is used cautiously (coding, summaries, testing message clarity), not in the models. _[experience, stated; support: Own practice.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C02-X1|C02-X1]])

**Chain: Why CTA drawdowns occur**
1. Volatility compression and calm markets → Fewer outsized trends: Trends are fewer and smaller ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C11-1|C11-1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C07-1|C07-1]])
2. Share of winning markets falls below break-even (~40% to 30-35%) → Multi-year drawdown without a single deep loss: Costs of straddle-like trading are not offset ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C10-2|C10-2]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C11-X2|C11-X2]])
- Evidence: Industry experience 2023-25.
- Fails when: Not stated; model breakdown test would show lower Sharpe extraction per unit of underlying trend.

**Decision process**
- [research] Diagnose underperformance by measuring Sharpe extracted from trending markets versus history before touching the model.. Why: Separates model failure from fewer trends. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C07-1|C07-1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C07-R1|C07-R1]])
- [universe] Drop markets that become financialized (e.g., CTAs ~70% of iron-ore front-month volume) because the product thesis is trading what others do not trade.. Why: Preserve the factor exposure the investor bought. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C08-1|C08-1]])

**Evidence style:** Industry experience and measurement logic; no data shown.

**Views at the time**
- (2025-12) Most likely outcome for 2026: 10-year Treasury yield around 6%; he would wish for equities +25%.. Reasoning: Rate view stated without reasoning. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C17-X1|C17-X1]])

### Unnamed panelist (possibly Andrew Beer) (Panelist agreeing with Yoav on TPA)
Fingerprint: #approach/manager_selection_allocation #approach/portfolio_construction_stacking #approach/diversification_risk_parity #approach/behavioral_sentiment
_Speaker note: Ledger names Jim for C03-3/C03-4 but the transcript brings Jim in only at the end of C04; the speaker is unidentified (ledger correction). C04-X1 (breaking anchoring; theatre) also follows this speaker's turn._

**Worldview premises**
- In a strategic allocation managed futures merits ~25% because almost nothing else is scalable, liquid, zero-correlated to stocks and bonds and pays off when needed (pod shops come close). _[theoretical, stated; support: Statistical measures cited from the GIC/JPM paper.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C03-3|C03-3]])
- US institutions hold ~6% in hedge funds with managed futures <10% of that (~50bp of the portfolio); career risk and benchmarking to hedge fund indices prevent moving it to ~30% of the sleeve. _[empirical, stated; support: Allocator structure.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C03-4|C03-4]])
- TPA could break anchoring to indices and legacy bucket sizes by forcing a statistical blank sheet, though much of TPA is theatre to win broader mandates. _[institutional, stated; support: Cautiously optimistic.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C04-X1|C04-X1]])

**Evidence style:** Statistical measures and observed allocator behaviour.

### Allan Dunne (CTA researcher (hedge fund allocator view))
Fingerprint: #approach/trend_following #approach/portfolio_construction_stacking #approach/macro_fundamental_topdown #approach/manager_selection_allocation #approach/diversification_risk_parity
_Speaker note: Name caption variants 'Alan/Allan Don'._

**Worldview premises**
- A hedge fund portfolio optimised within the total portfolio tilts to CTA, macro and commodities and away from equity long-short and credit, which duplicate held factors. _[empirical, stated; support: GIC/JP Morgan asset management paper.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C03-1|C03-1]])
- A trend program already behaves like a total portfolio approach because it dynamically allocates risk to the best risk-adjusted markets. _[theoretical, stated; support: Definition-based argument.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C03-2|C03-2]])
- TPA has an unresolved look-through problem: investment teams making tactical views while allocating to managers who also make tactical bets. _[institutional, stated; support: Reasoned.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C03-X1|C03-X1]])
- High-vol trend managers repeat a cycle of exceptional years, asset gathering, deep drawdown and asset loss; a high-vol ETF would follow the same flow cycle. _[experience, stated; support: Mulvaney as example.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C16-X1|C16-X1]])
- Wealth portfolios should hold a balanced diversified portfolio and then lever to the desired risk rather than add equities. _[theoretical, stated; support: Capital-efficiency logic.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C16-1|C16-1]])

**Evidence style:** Academic papers and industry examples.

**Views at the time**
- (2025-12) 2026 will be the year of the bond breakout: US 10-year yields up to 6% then down to 3.5%.. Reasoning: Unspecified; repeats an earlier prediction. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C16-2|C16-2]])

### Jim (volatility specialist; caption 'Jim Kasang') (Panelist focused on long volatility and portfolio construction)
Fingerprint: #approach/volatility_options #approach/crisis_alpha_convexity #approach/diversification_risk_parity #approach/regime_detection #approach/structural_themes #approach/behavioral_sentiment
_Speaker note: The ledger's C03 attributions are removed (not Jim). C12 attributions follow the host's cue 'perception of risk' after Katie._

**Worldview premises**
- 95% of investors diversify by holding more correlated assets; stocks and 60/40 each have about a 0.35 Sharpe over 125 years so bonds gave no Sharpe benefit; true diversification needs non-asset strategies such as trend and long volatility. _[empirical, stated; support: Allocators he asked cannot name the Sharpe; the 0.35 figure is quoted from memory.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C04-1|C04-1]])
- Academic research points to a long-volatility hedge as the one consistent diversifier and most important portfolio component. _[empirical, stated; support: 'Tons of academic research' (uncited); David Dredge conversation.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C04-2|C04-2]])
- The stock-bond structure dates from about 1985 and persists through recency bias and the long falling-rate era that removed the need to manage risk. _[experience, stated; support: History.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C05-X1|C05-X1]])
- Distribution width and tail fatness by regime (volatility) are forecastable while direction is not, so trend-model choice should rest on a forward view of the distribution, not backtest optimisation. _[theoretical, stated; support: Vol-desk framing.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C06-1|C06-1]])
- Managed futures drawdown (~15-16% over 25 years) is small relative to equities, and bonds' recent 15-16% drawdown after 20 years undercuts the view that CTAs are riskier. _[empirical, stated; support: Drawdown comparisons.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C12-1|C12-1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C12-X1|C12-X1]])
- Trend following earns most when the world changes (inflation shock, regime shifts over ~24 months) and struggles in noisy markets that total-portfolio allocators with static assumptions handle badly. _[theoretical, stated; support: Recent years' experience.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C12-2|C12-2]])

**Chain: Long volatility as brakes on a race car**
1. Long vol earns about zero long-run → Allocators remove it as a drag: Perceived as slowing the car ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C05-1|C05-1]])
2. Brakes give control into corners → Portfolio can keep risk on and accelerate on straights: Raises geometric performance ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C05-1|C05-1]])
- Evidence: Metaphor from David Dredge's conversation; no numbers.
- Fails when: Not stated.

**Chain: Why CTAs matter in a concentrated portfolio**
1. Portfolio concentrated in AI trade across equities, rates and more → Large loss if equities fall 50%: Concentration in one theme ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C12-X2|C12-X2]])
2. Trend program cuts losers and can go short → Protection: Disciplined loss-cutting vs narrative of conviction ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C12-X3|C12-X3]])
- Evidence: Reasoning, current positioning.
- Fails when: Noise year with no world change.

**Decision process**
- [signal] Choose trend model by forward view of return distribution (volatility regime, supply and demand) rather than backtest optimisation.. Why: Distribution is more predictable than direction. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C06-1|C06-1]])

**Evidence style:** Academic literature, metaphors and a few headline statistics from memory.

**Views at the time**
- (2025-12) 2026 resembles 2022: pain trade is stocks down and rates up; implied-vol and VIX hedges could pay; rates higher hurts those holding bonds for diversification.. Reasoning: Investors own stocks with long-vol bandaids and bonds as diversifier. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C16-3|C16-3]])

### Andrew Beer (Replication ETF manager (managed futures replication))
Fingerprint: #approach/replication_indexing #approach/manager_selection_allocation #approach/research_robustness_overfitting #approach/portfolio_construction_stacking #approach/costs_execution
_Speaker note: Ledger attribution used for C06-C07, C09, C13-C16._

**Worldview premises**
- A replication model left unchanged for ten years gives a fully consistent track record; the best outcome for an allocator is that the manager never needs changes, because it is hard to know whether changes help going forward. _[experience, stated; support: Own 10-year no-change record.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C06-2|C06-2]])
- A legitimate reason to revisit a model is evidence of industry-wide drift (all managers moving to 15-20 day models), visible against a benchmark or replication; without it do not change. _[theoretical, stated; support: Reasoned.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C09-X1|C09-X1]])
- Slower and simpler trend models outperformed more complex ones over the last three years; managers should own the design decisions that cost return in this regime. _[empirical, stated; support: Presented data (about 1,100bp cost used as illustration).]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C09-2|C09-2]])
- With wide dispersion and no persistence of alpha, allocators chase the recent winner and oversell it, producing a negative feedback loop when it underperforms. _[behavioural, stated; support: Allocator incentives.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C13-1|C13-1]])
- ETF holders see price and drawdown every minute, so drawdowns matter; allocators trained to buy the dip want a rebound story that honest CTA managers cannot give. _[behavioural, stated; support: Own ETF experience.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C13-X1|C13-X1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C13-X2|C13-X2]])
- Managed futures becomes a standard allocation if presented as a strategic long-term holding judged by portfolio benefit rather than lookbacks or positions. _[theoretical, stated; support: His stated thesis; to be tested in five years.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C13-X3|C13-X3]])
- Higher interest rates make capital efficiency (return stacking, portable alpha, yield stacking) valuable again; 2x/3x growth reflects need for efficiency, not more risk. _[theoretical, stated; support: Options exchanges (1971) analogy.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C15-1|C15-1]])
- The large pool of money is risk-averse allocators avoiding embarrassment, not leverage-seeking retail; niche ETF structures can reach multi-billion scale. _[experience, stated; support: Innovator sold for $2bn.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C14-X1|C14-X1]])

**Decision process**
- [research] Change nothing in the model unless evidence of structural deviation; accept a very high bar for changes.. Why: Hard to tell whether changes help; consistent record is valuable. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C06-2|C06-2]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C09-X1|C09-X1]])

**Evidence style:** Own track record, product experience and allocator observation.

**Views at the time**
- (2025-12) Outrageous 2026: institutions begin buying managed futures ETFs (low probability, high significance).. Reasoning: Allocators with 'hedge fund analyst' mandates look for hedge funds. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C16-X3|C16-X3]])

### Katie Kaminski (CTA researcher/manager)
Fingerprint: #approach/trend_following #approach/manager_selection_allocation #approach/behavioral_sentiment #approach/regime_detection
_Speaker note: Name 'Kaminsky' caption variant._

**Worldview premises**
- Managed futures drawdowns coincide with calm, equity-friendly, low-volatility environments, and recover faster when equity environments are challenging because hit ratio rises. _[empirical, stated; support: Own paper on managed futures drawdowns (bubble chart).]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C11-2|C11-2]])
- After a very challenging period, one or two strong years typically followed; manager top/bottom timing is trend-following-trend. _[empirical, stated; support: Fund-of-funds studies; mean reversion over longer horizons.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C11-3|C11-3]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C11-X3|C11-X3]])
- A daily-liquid high-vol CTA product cannot smooth prints as private equity does, so it will attract performance chasing and disappoint, as with Bitcoin; institutional adoption pushed managers to lower risk and size management. _[behavioural, stated; support: History of the industry.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C15-X1|C15-X1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C15-2|C15-2]])

**Evidence style:** Own research paper and history.

**Views at the time**
- (2025-12) 2026 will be a boom-and-bust roller coaster: rates fall and over-stimulation make conditions look strong before things fall apart.. Reasoning: Something brewing in the macro change of 2025. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C16-X2|C16-X2]])

### Rich Brennan (Australian systematic trend follower)
Fingerprint: #approach/trend_following #approach/research_robustness_overfitting #approach/behavioral_sentiment #approach/regime_detection

**Worldview premises**
- Markets change but process should not change in response to recent outcomes; a stable process does not remove drawdowns but prevents panic and rule changes (the main investor mistake). _[experience, stated; support: Own practice; asks panel how much change is evolution vs reaction to pain.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C05-2|C05-2]])

**Decision process**
- [research] Pre-commit to a stable process; explain to allocators how the strategy behaves in uncomfortable conditions.. Why: Stability builds trust and prevents behavioral drift. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C05-2|C05-2]])

**Evidence style:** Experience.

### Nick Baltas (Quant researcher (replication/benchmark work))
Fingerprint: #approach/replication_indexing #approach/research_robustness_overfitting #approach/trend_following #approach/regime_detection

**Worldview premises**
- Drawdowns are a prompt to review for blind spots but not a reason to change the model, especially when explained by repeated V-shaped reversals (yen, Liberation Day). _[experience, stated; support: Own practice.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C08-2|C08-2]])
- A replication of the CTA index need not change when underlying managers change models as long as the changes net out and managers do not become too fast to track. _[theoretical, stated; support: Aggregation logic.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C09-1|C09-1]])
- A benchmark model need not minimise tracking error; high tracking error in a year does not show the model works or fails. _[theoretical, stated; support: Outperformance matters.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C09-X2|C09-X2]])

**Decision process**
- [research] Treat pain as invitation to reflect, not to change.. Why: Avoid reacting to explainable underperformance. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C08-2|C08-2]])

**Evidence style:** Reasoning and benchmark practice.

### Rob Carver (Independent systematic trader)
Fingerprint: #approach/position_sizing_vol_target #approach/kelly_or_conviction_sizing #approach/trend_following
_Speaker note: His proposal is half in jest._

**Worldview premises**
- A Sharpe-1 strategy run at half Kelly implies roughly 40-50% annualised volatility, so high-vol CTA products are feasible and could be sold to retail with fees proportional to volatility. _[theoretical, stated; support: Kelly arithmetic.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C14-1|C14-1]])

**Decision process**
- [sizing] Half Kelly sizing for a Sharpe-near-1 strategy.. Why: Maximise growth with a safety margin. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C14-1|C14-1]])

**Evidence style:** First-principles arithmetic.

### Mark Rzepczynski (CTA/macro manager (also posed the opening AI and TPA questions))
Fingerprint: #approach/macro_fundamental_topdown #approach/policy_reaction_central_banks #approach/valuation_contrarian #approach/behavioral_sentiment
_Speaker note: Opening questions are not in the ledger._

**Worldview premises**
- Inflation is a sleeper risk; equity strength concentrated in MAG 7 can burst and drag the market. _[experience, stated; support: Prediction segment only.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C17-1|C17-1]])

**Evidence style:** Opinion.

**Views at the time**
- (2025-12) 2026 pessimist: higher inflation lifts Treasury yields, credit crises carry over, MAG 7 bubble bursts, stable to down equities; Europe resurges.. Reasoning: Higher inflation, 2025 credit problems, index concentration. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C17-1|C17-1]])

### Niels Kaastrup-Larsen (Host, Top Traders Unplugged)
Fingerprint: #approach/trend_following #approach/policy_reaction_central_banks #approach/manager_selection_allocation
_Speaker note: Barclay CTA volatility statement re-attributed to the host._

**Worldview premises**
- The Barclay CTA index ran at 20-25% annualised volatility in the 1980s and early 1990s and is below 5% in recent years. _[empirical, stated; support: Index data, quoted as an FYI.]_ ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C15-2|C15-2]])

**Evidence style:** Index data.

**Views at the time**
- (2025-12) The Fed will hike at least once in 2026 despite pressure and a new Trump-selected chair.. Reasoning: Stated without reasoning. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C17-2|C17-2]])

### Disagreements
- **Will total portfolio approach (TPA) help CTAs?**: Yoav Git: Theoretically very large allocation but in practice a buzzword; flows follow performance. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C02-1|C02-1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C02-2|C02-2]]); Unnamed panelist (possibly Andrew Beer): Could break anchoring to indices, but much is theatre; cautiously optimistic. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C03-4|C03-4]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C04-X1|C04-X1]]); Allan Dunne: Valid from the return lens and a CTA already acts like TPA, but look-through is unresolved. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C03-1|C03-1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C03-2|C03-2]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C03-X1|C03-X1]])
- **When should a trend manager change the model?**: Andrew Beer: Almost never; ten years without a change is the best outcome; only evidence of industry-wide drift justifies review. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C06-2|C06-2]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C09-X1|C09-X1]]); Jim (volatility specialist; caption 'Jim Kasang'): Moving from backtest optimisation to forward distribution views can improve process. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C06-1|C06-1]]); Yoav Git: Change only when market properties change (financialisation) or measurement shows model breakdown; do not drift from the sold style. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C07-1|C07-1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C08-1|C08-1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C08-X1|C08-X1]]); Nick Baltas: Pain invites review for blind spots but a very high bar for change. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C08-2|C08-2]])
- **Should CTAs offer high-volatility products?**: Rob Carver: Half-Kelly implies 40-50% vol; sell high-vol products to retail (half in jest). ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C14-1|C14-1]]); Katie Kaminski: Daily prints without smoothing mean performance chasing and disappointment. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C15-X1|C15-X1]]); Allan Dunne: High-vol managers repeat a boom-bust asset cycle; capital efficiency favours balanced products plus leverage. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C16-X1|C16-X1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C16-1|C16-1]]); Andrew Beer: Opportunity in capital-efficient stacked products rather than more risk per se. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C15-1|C15-1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C14-X1|C14-X1]])
- **2026 rates**: Allan Dunne: 10-year to 6% then down to 3.5%. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C16-2|C16-2]]); Yoav Git: 10-year around 6% most likely. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C17-X1|C17-X1]]); Niels Kaastrup-Larsen: Fed has to hike at least once. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C17-2|C17-2]]); Katie Kaminski: Rates go lower, boom-bust. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C16-X2|C16-X2]])

### Gaps and conflicts
- Speaker attribution is uncertain for C03-C04 (Jim vs unnamed panelist), C07 (Yoav vs others) and the host question turns; ledger corrections applied. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C03-3|C03-3]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C03-4|C03-4]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C04-X1|C04-X1]])
- The 25% and ~1/3 optimal-allocation claims rest on stated Sharpe and correlation assumptions (Sharpe 0.5 vs 1.5, zero correlation) that are not demonstrated. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C02-1|C02-1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C03-3|C03-3]])
- Stock/60-40 Sharpe of 0.35 over 125 years is quoted from memory; no source given. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C04-1|C04-1]])
- Volatility compression as the sole cause of 2023-25 underperformance is argued from a Sharpe-extraction test that is described but not shown. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C07-1|C07-1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C11-1|C11-1]])
- Andrew says changes are rarely helpful; Jim and Yoav propose forward-looking or thesis-driven adaptation, so 'never change' vs 'adapt to distribution' is not reconciled. ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C06-1|C06-1]], [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C06-2|C06-2]])

### Forward-looking inputs (reader synthesis)
(reader) Inputs named: share of markets winning (40% vs 30-35%), Sharpe extracted per unit of underlying trend, volatility compression, front-month CTA share of volume (financialisation), stock-bond correlation, rates and inflation regimes, manager dispersion and index volatility. Horizons: multi-year drawdowns recover over 1-2 years after challenging periods; 2026 views are annual.

### Reader inferences (not stated by the speakers)
- (reader) The panel's shared claim is that drawdown diagnosis should separate trend availability from model quality; this suggests a monitoring metric (winner share, Sharpe extraction) for the book.
- (reader) Several speakers (Jim, Yoav, Allan) converge on trend and long volatility as complements; only Jim attaches an explicit 2026 trade.
- (reader) The predictions segment is flagged by the host as 'outrageous', so treat 2026 views as low-confidence.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, disclaimers, agenda; AI and TPA questions posed |
| C02 | 3 | TPA for CTAs, AI use, CTA allocation sizing |
| C03 | 4 | TPA, optimisation context, institutional anchoring |
| C04 | 2 | big-picture diversification, Sharpe of S&P, long vol |
| C05 | 2 | brakes metaphor; process stability question |
| C06 | 2 | distribution forecasting, unchanged models |
| C07 | 1 | consistency, measuring causes of underperformance |
| C08 | 2 | financialization thesis, whether pain justifies change |
| C09 | 2 | replication model, slower and simpler outperformed |
| C10 | 2 | owning decisions; CTA drawdowns vs other hedge funds |
| C11 | 3 | hit ratio, paper on drawdowns, mean reversion of performance |
| C12 | 2 | drawdown depth, perception of risk, when trend earns |
| C13 | 1 | ETF drawdown views, allocator manager selection behaviour |
| C14 | 1 | retail high-vol product joke, Kelly, return stacking |
| C15 | 2 | capital efficiency, CTA vol history |
| C16 | 3 | high-vol trend, predictions Allan Jim |
| C17 | 2 | 2026 predictions, outro |

## Claims

### C02
- **Yov (CTA manager)** Mean-variance optimisation across a total portfolio implies a very large CTA allocation (about 1/3 of risk) even if CTA Sharpe is only 0.5 versus 1.5 for the rest, because of CTA diversification.  #mech/risk_premium
  > even if you expect your sharp ratio of your other portfolio to be one and a half and you think that CTAs are uh.5 sharp then in order to maximize your sharp you need to
  indicator: CTA Sharpe 0.5 vs rest-of-portfolio Sharpe 1.5 · asset: multi · direction: raise CTA/trend allocation to ~1/3 of risk · horizon: years · conditions: assumes zero correlation to the rest of the portfolio and stable Sharpes · testable: yes - simple optimiser calculation · confidence: medium
  ^MT221-C02-1
- **Yov (CTA manager)** Flows into CTAs are driven by past performance rather than by portfolio-theory arguments such as total portfolio approach (TPA), so TPA is unlikely to change CTA allocations much.  #mech/behavioral
  > In practice flows follows performance and that will be the most determining factor of flows into the CTA universe.
  asset: multi · horizon: years · testable: partly - flows vs trailing performance can be tested · confidence: medium
  ^MT221-C02-2
- **Yov (CTA manager)** CTA exposure should be chosen to hedge the allocator's existing asset-class exposure (fixed-income holders want fixed-income CTA, equity holders something different).  #mech/risk_management
  > you should think about CTAs in the context of the asset classes that you're holding in your own portfolio. So if you're if you're a fixed income manager, you should think about fixed income CTA.
  asset: multi · direction: match CTA sleeve to existing holdings · testable: partly - conditional hedge benefit can be measured · confidence: medium
  ^MT221-C02-3
- **Yov (CTA manager)** A CTA manager uses AI cautiously: it helps with coding, summarising client discussions and the team's own thinking, and as a test of message clarity (an AI misreading a presentation shows where the message is unclear), but it is not presented as a source of alpha.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > generally the approach has been very cautious on our side. Um it is able to help us in coding.
  indicator: AI/LLM tooling in research process · asset: other · conditions: cautious adoption; coding and summarisation uses · testable: no - process practice, no measurable claim · confidence: medium
  ^MT221-C02-X1
- **Yov (CTA manager)** Bucket-style hedge fund allocation (fixed slices for macro, long/short, real estate, private credit) leaves CTAs with about 2%, too small to change the total portfolio's convexity or diversification; looking at the whole portfolio instead is what would raise the CTA weight.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > And then CTAs get like 2% where they make a zero difference to the overall portfolio in terms of convexity, in terms of diversification.
  asset: multi · direction: larger CTA weight under whole-portfolio view · horizon: years · conditions: depends on allocator process (silo vs total portfolio) · testable: partly - allocation weights observable, benefit simulable · confidence: medium
  ^MT221-C02-X2

### C03
- **Allan (CTA researcher)** A hedge-fund portfolio optimised within the total portfolio (GIC / JP Morgan AM paper) tilts to CTA, macro and commodities and away from equity long-short and credit, which duplicate factors already held.  #mech/risk_premium
  > you get much more allocation to CTA macro commodities when you optimize in the context of the overall portfolio because you're going to have less allocation to long short equity and credit
  asset: multi · direction: long CTA/macro/commodity hedge funds; less equity L/S and credit · horizon: years · testable: yes - optimisation in the cited paper · confidence: medium
  ^MT221-C03-1
- **Allan (CTA researcher)** A trend-following programme already behaves like a total portfolio approach because it dynamically allocates risk to the markets with the best risk-adjusted opportunity rather than holding static weights.  #mech/structural_shift
  > it it does TPA already. it it it it evaluates the markets and assesses where are the best risk adjusted returns where where the best opportunities
  asset: multi · testable: no - conceptual · confidence: medium
  ^MT221-C03-2
- **Jim (volatility specialist)** Managed futures is nearly the only scalable, liquid strategy with zero correlation to stocks and bonds that pays off in stress, so a strategic allocation would be around 25%.  #mech/risk_premium
  > there aren't many things you have out there that have zero correlation to stocks and bonds and do well when you need it the most um that you can scale and do in liquid fashion
  asset: multi · direction: long managed futures ~25% of strategic allocation · horizon: years · testable: partly - correlation and crisis-alpha measurable; 25% is a judgement · confidence: medium
  **Correction (cross-check):** Speaker likely wrong: the host only introduces Jim at the end of C04 ('I certainly need to hear from Jim') and Jim starts with 'Yeah, look to take a step back'. The C03 speaker (agrees with Yov, cites the 6% US hedge fund allocation) is a different panelist, probably Andrew, and the transcript does not name him. → Unnamed panelist (not Jim; possibly Andrew): managed futures is almost the only scalable, liquid strategy with zero correlation to stocks and bonds that pays off when needed, so a strategic allocation would be about 25%; pod shops come close but not as scalable.
  ^MT221-C03-3
- **Jim (volatility specialist)** US institutions hold about 6% in hedge funds, of which managed futures is under 10%, i.e. about 50bp of the portfolio, far below optimal; career risk and benchmark anchoring prevent raising it to ~30% of the hedge-fund sleeve.  #mech/behavioral
  > a typical institutional um allocator in the US has about a 6% allocation to hedge funds today of which managed futures according to kind of the broad classification of hedge funds is sub 10%.
  asset: multi · horizon: years · conditions: benchmarked to hedge fund indices · testable: no - structural observation · confidence: medium
  **Correction (cross-check):** Same speaker problem as C03-3: attributed to Jim but the host brings Jim in only after this speaker finishes. Also the 30% figure is the managed futures share of the hedge fund sleeve ('from a 6 or 7% allocation to a 30% allocation which is where it should be'), which the claim states but attributes to Jim. → Unnamed panelist (not Jim): US institutions hold about 6% in hedge funds with managed futures under 10% of that, roughly 50bp of the portfolio; benchmarked to hedge fund indices it is career-risky to raise managed futures from 6-7% to about 30% of the hedge fund sleeve, which is where it should be.
  ^MT221-C03-4
- **Allan (CTA researcher)** Caveat to TPA: if the investment team makes tactical views and also allocates to hedge funds that already make tactical bets, it is unclear whether they look through those managers' positions or adjust for them, so TPA double counts or conflicts with manager-level tactical risk.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check)_
  > do they look through that or do they have to adjust for that in terms of their own views as well.
  asset: multi · conditions: when hedge fund tactical bets overlap with the allocator's own tactical views · testable: no - open question the speaker leaves unresolved · confidence: low
  ^MT221-C03-X1

### C04
- **Jim (volatility specialist)** Allocators rarely know long-run Sharpe ratios (S&P and 60/40 about 0.35 over 125 years), yet 95% of investors rely on stock/bond mixes whose diversification benefit is overstated; true diversification needs non-asset strategies like trend and long volatility.  #mech/risk_premium
  > what do you think the sharp ratio is of the S&P over the last 125 years?
  indicator: S&P 500 and 60/40 Sharpe over 125 years · asset: multi · direction: favour non-correlated strategies over stock/bond diversification · horizon: years · conditions: stocks and bonds are highly correlated in the tail · testable: yes - long-run Sharpe and correlation computable · confidence: medium
  **Correction (cross-check):** Overstates what was said about diversification: the speaker says stocks and 60/40 each have a Sharpe of about 0.35, i.e. adding bonds gives zero diversification benefit, and calls the stock/bond approach zero diversification, rather than merely overstated. → Jim: no allocator he asks can name the 125-year Sharpe of the S&P or of a 60/40 portfolio (both about 0.35), so bonds added no Sharpe benefit over stocks; yet 95% of investors diversify by holding more correlated assets, whereas true diversification comes from non-asset strategies such as trend following and long volatility.
  ^MT221-C04-1
- **Jim (volatility specialist)** Academic research identifies a long-volatility hedge as the one consistent diversifier and most important portfolio component.  #mech/risk_premium
  > the one thing that tons of academic research points to is the one thing that is a true uh consistent diversifier and the most important thing in portfolio is is a long volatility hedge
  indicator: long volatility hedge · asset: multi · direction: long volatility · horizon: years · testable: partly - depends on hedge implementation cost · confidence: medium
  ^MT221-C04-2
- **Jim (volatility specialist)** The real benefit of TPA for CTAs is that it can break allocators' anchoring to hedge fund indices and legacy bucket sizes, forcing a statistical blank-sheet allocation; but much of TPA is theatre to win broader mandates, so the speaker is only cautiously optimistic.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > breaking that anchoring mechanism and having people kind of start with a blank sheet sheet of paper
  asset: multi · direction: higher managed futures allocation if anchoring breaks · horizon: years · conditions: benchmark and career risk anchor allocators to hedge fund index weights · testable: no - qualitative view about institutional behaviour · confidence: medium
  ^MT221-C04-X1

### C05
- **Jim (volatility specialist)** Long volatility is like brakes on a race car: although it earns about zero in the long run, it lets the portfolio keep risk on in the straights and so raises geometric performance, rather than merely slowing it.  #mech/risk_management
  > the brakes give you control. The brakes allow you to slow down into the turn and accelerate out. You win races. You go faster by having V in the portfolio.
  indicator: long volatility / VIX allocation · asset: multi · direction: hold small permanent long-vol and add into risk · conditions: use the payoff to monetise by adding risk afterward · testable: partly - needs rule for re-risking after payoff · confidence: medium
  ^MT221-C05-1
- **Rich (CTA researcher)** A stable, pre-committed process does not remove drawdowns but prevents panic and rule changes made in response to recent outcomes, which is a main investor mistake.  #mech/research_method
  > what a stable process does do it doesn't eliminate the draw downs but it does prevent panic and behavioral drift.
  asset: multi · testable: no - behavioural discipline · confidence: high
  ^MT221-C05-2
- **Jim (volatility specialist)** Most of the investment world runs a simple long-only stock and bond mix whose structure only dates from about 1985, and it persists through recency bias and because the long falling-rate era removed the need to manage risk, so its apparent diversification is untested in a different regime.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > that again didn't exist until 1985 and doing it simply because of recency bias uh and a lack of needing to really manage risk and understand risk in a meaningful
  indicator: long-only stock/bond (60/40) allocation · asset: multi · horizon: years · conditions: a different rate/inflation regime would expose the lack of risk management · testable: partly - regime-dependent performance of 60/40 testable · confidence: medium
  ^MT221-C05-X1

### C06
- **Jim (volatility specialist)** Distribution width and tail fatness by regime (volatility) are forecastable while direction is not, so trend-model choice should be driven by a forward view of the return distribution and supply/demand factors rather than by backtest optimisation.  #mech/slow_reaction
  > We have actually a pretty good ability to predict distribution. predicting direction is hard.
  indicator: volatility regime / return distribution · asset: multi · horizon: months · testable: partly - vol forecastability is well documented; mapping to trend speeds is untested · confidence: medium
  ^MT221-C06-1
- **Andrew (replication ETF manager)** A trend replication model left unchanged for ten years gives a track record that is fully consistent; the best outcome for an allocator is that the manager never needs changes, because it is hard to know whether changes help going forward.  #mech/research_method
  > you know, tell us all the changes you've made in your model and the answer is none. Zero. Not a line of code, not an instrument.
  asset: multi · horizon: years · testable: partly - consistency of track record can be judged; change value unknowable · confidence: high
  ^MT221-C06-2

### C07
- **Yov (CTA manager)** Recent CTA underperformance is explained by fewer outsized trends (compression), not by model breakdown; diagnose by measuring the Sharpe extracted from markets that trended at a given underlying Sharpe versus history, which is roughly unchanged.  #mech/research_method _(time-bound view)_
  > the reason why we have seen the underperformance in the last few years is not because the model doesn't work is because we've seen this compression that we're talking about. We have seen just less outliers.
  indicator: Sharpe captured per unit of underlying market trend Sharpe · asset: multi · horizon: years · testable: yes - decomposition of returns into trend availability and capture · confidence: high
  ^MT221-C07-1
- **Yoav Git** Before changing any trend model, first understand the cause of underperformance by measuring properly (for example, Sharpe extracted from trending markets versus the past), and second understand and stay true to your thesis.  #mech/new _(added by map cross-check)_
  > truly actually understanding the causes for performance or underperformance i.e. actually measuring things properly
  indicator: Sharpe extracted per unit of underlying trend Sharpe · asset: multi · direction: diagnose · horizon: years · conditions: After a multi-year drawdown · testable: yes: extraction ratio is computable · confidence: high
  ^MT221-C07-R1
- **Andrew Beer** Owning one's investment decisions (admitting which choices were mistakes) differentiates quantitative managers and helps allocators build a mosaic of exposures; the asset allocation thesis and the source of excess returns are separate from individual design decisions.  #mech/new _(added by map cross-check)_
  > very good at owning their decisions
  indicator: manager transparency · asset: multi · direction: n/a · horizon: years · conditions: Cliff Asness cited as an example · testable: no · confidence: medium
  ^MT221-C07-R2

### C08
- **Yov (CTA manager)** A market where CTAs account for ~70% of front-month volume (SORA/Ionor example) is financialized; a manager selling non-financialized risk factors should drop it, since the thesis of the product is trading what others do not.  #mech/crowding_positioning _(time-bound view)_
  > about 70% of the of the volume in the front front month contract are CTAs Okay, to me that's a warning sign.
  indicator: share of front-month volume attributable to CTAs · asset: commodities · direction: exclude crowded markets from non-financialized trend programme · conditions: applies only if product thesis is low beta to the financialized universe · testable: partly - volume share data hard to obtain · confidence: medium
  ^MT221-C08-1
- **Nick (CTA replication researcher)** Drawdowns are a prompt to review for blind spots but not a reason to change the model, especially when the underperformance is explained by repeated V-shaped reversals (yen, Liberation Day).  #mech/research_method
  > I would say no. Is the pain an invitation to think about changing the model? Maybe.
  asset: multi · testable: no - governance rule · confidence: high
  ^MT221-C08-2
- **Yov (CTA manager)** A manager who sells a specific trend style (for example fast trend) should not drift away from that style when it underperforms, because style drift defeats the reason the investor hired them and loses the investors; model changes should follow the stated thesis, not recent pain.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > I'm not able to make money. I'm going to drift away from that space. That's actually going to be very bad. You're just going to lose your investors.
  asset: multi · conditions: applies when underperformance in the chosen style is explainable by the environment · testable: no - manager governance principle · confidence: medium
  ^MT221-C08-X1

### C09
- **Nick (CTA replication researcher)** A replication of the CTA index need not change when underlying managers change models, as long as their changes net out and managers do not become too fast for the replicator to track.  #mech/structural_shift
  > the replication model almost has an assumption on how the average underneath behaves. And as long as that remains through time, you don't really have to change your your your recipe
  indicator: CTA replication tracking error vs index · asset: multi · horizon: years · conditions: assumes manager changes average to zero · testable: yes - tracking error against index measurable · confidence: medium
  ^MT221-C09-1
- **Andrew (replication ETF manager)** Over the past three years slower and simpler trend models outperformed more complex or faster ones; allocators should ask managers to own design decisions that cost return in this regime.  #mech/slow_reaction _(time-bound view)_
  > over the past 3 years slower and simpler has worked better
  indicator: trend speed / model complexity performance · asset: multi · direction: long slower, simpler trend · horizon: years · conditions: 2023-2025 regime of high dispersion · testable: yes - compare speeds by period · confidence: medium
  ^MT221-C09-2
- **Andrew (replication ETF manager)** A legitimate reason to revisit a trend model is evidence of industry-wide drift (for example all managers moving to 15-20 day models), which would be visible against a benchmark or replication; absent such evidence of a structural deviation, underperformance alone does not justify changes.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check)_
  > if everybody goes to a 15-day model, it's not going to be a surprise, right?
  indicator: industry average trend speed vs own model · asset: multi · conditions: change only if structural deviation is understood and persistent · testable: partly - industry speed drift measurable via index replication · confidence: low
  ^MT221-C09-X1
- **Nick (CTA replication researcher)** A replication or benchmark model need not minimise tracking error to the CTA index, since outperformance matters; high tracking error in a given year does not by itself show the model works or fails.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > is the objective to minimize track and error probably not because obviously the outperformance is important
  indicator: tracking error to CTA index · asset: multi · testable: partly - tracking error and excess return vs index measurable but the speakers state no conclusion · confidence: low
  ^MT221-C09-X2

### C10
- **Yov (CTA manager)** CTA drawdowns come from nothing happening (whipsaw and volatility compression) rather than from a single event, as the strategy is like buying straddles paid via trading costs.  #mech/slow_reaction
  > the reason why CTAs tend to lose money is mostly um because nothing happens
  asset: multi · horizon: years · conditions: low realised-trend, low vol periods · testable: yes - drawdown attribution · confidence: high
  ^MT221-C10-1
- **Yov (CTA manager)** A trend portfolio needs only about 40% of markets to be winners for a good year because winners are outsized; drawdowns arise when winners drop to 30-35%.  #mech/risk_premium
  > you don't actually need 50% of your markets to be winners, you just need maybe 40% of your markets to be winners to have a good positive year.
  indicator: percentage of markets with winning trades · asset: multi · horizon: years · testable: yes - hit ratio by year · confidence: high
  ^MT221-C10-2

### C11
- **Yov (CTA manager)** Over 2023-2025 volatility compression pushed the share of winning markets below break-even, causing the industry's multi-year drawdown.  #mech/slow_reaction _(time-bound view)_
  > vault compression and the percentage of winners has just shrunk below the break even point and that's something that we have seen in the last in the last 3 years
  indicator: volatility compression; fraction of winning markets · asset: multi · horizon: years · conditions: 2023-2025 · testable: yes - measure hit ratio · confidence: medium
  ^MT221-C11-1
- **Katie (CTA researcher)** Managed futures drawdowns tend to coincide with calm, equity-friendly, low-volatility environments, and recoveries are faster in challenging equity environments because the hit ratio rises.  #mech/cycle_persistence
  > what we find is if you look at what's happening during a lot of our very challenging environments they tend to be pretty good environments for equities
  indicator: managed futures drawdowns vs equity regime · asset: multi · horizon: years · testable: yes - paper on largest managed futures drawdowns · confidence: medium
  ^MT221-C11-2
- **Katie (CTA researcher)** After a very challenging period for managed futures, one or two years of strong performance has typically followed, so timing manager tops and bottoms is trend-following-trend and not advisable.  #mech/overshoot
  > usually that's followed historically by one or two years of very positive performance.
  indicator: trailing multi-year managed futures return · asset: multi · direction: hold through drawdowns · horizon: years · conditions: longer-horizon mean reversion vs short-horizon persistence · testable: yes - forward returns after drawdowns · confidence: medium
  ^MT221-C11-3
- **Yov (CTA manager)** Because a CTA drawdown has no single event to blame (unlike a discrete bet gone wrong), allocators find it harder to explain to an investment committee and to stay patient, even though the cause is systematic (volatility compression, too few winning markets).  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > CTA drawdowns are much more difficult because there isn't necessarily a one event that will explain the draw down
  asset: multi · horizon: years · conditions: applies to CTA drawdowns from lack of trends rather than event losses · testable: no - behavioural observation · confidence: medium
  ^MT221-C11-X1
- **Yov (CTA manager)** CTA drawdowns are typically long rather than deep: volatility compression makes outsized trends hard to harvest for an extended period without a single deep loss, which answers the host's question of whether long or deep drawdowns are worse for the strategy.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check)_
  > in CTAs you don't necessarily see a very deep draw down but you might have a go through a situation where for a long period
  indicator: drawdown depth and duration · asset: multi · horizon: years · conditions: volatility compression regime · testable: yes - drawdown depth/duration of CTA indices measurable · confidence: medium
  ^MT221-C11-X2
- **Katie (CTA researcher)** Fund-of-funds studies show it is very difficult to pick the winning CTA in any single year and strategies on average recover after drawdowns, so short-run performance persistence is weak and mean reversion over longer horizons dominates; dispersion drives behavioural errors.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > it's very difficult to pick a winning manager in any one year
  indicator: manager performance persistence · asset: multi · horizon: years · testable: yes - persistence of manager returns testable · confidence: medium
  ^MT221-C11-X3

### C12
- **Jim (volatility specialist)** Managed futures maximum drawdown is about 15-16% over 25 years, much smaller than equities, so perceived risk exceeds actual risk.  #mech/risk_management
  > 16% draw down over 25 years like it's child's play compared to equities.
  indicator: managed futures index max drawdown · asset: multi · horizon: years · testable: yes - index data · confidence: high
  ^MT221-C12-1
- **Jim (volatility specialist)** Trend following earns most when the world changes a lot (inflation shocks, regime shifts over ~24 months) and struggles in noisy markets where little actually changes, which is what total portfolio allocators with static assumptions do badly.  #mech/slow_reaction
  > you're going to go through like the space is going to make money a lot of money when the world changes a lot right
  asset: multi · horizon: months · conditions: big change in information; fails in noise without regime change · testable: partly - needs regime-change measure · confidence: medium
  ^MT221-C12-2
- **Jim (volatility specialist)** Bonds went about 20 years without a meaningful drawdown and then suffered a drawdown of 15-16%, similar in size to the maximum drawdown of managed futures over 25 years, which undercuts the view that CTAs are riskier than traditional assets.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > bonds had didn't have a draw down for 20 years basically and now you've had a 15 16% draw down
  indicator: bond index drawdown vs managed futures max drawdown · asset: rates · horizon: years · testable: yes - drawdown comparison measurable · confidence: medium
  ^MT221-C12-X1
- **Jim (volatility specialist)** Portfolios are concentrated in the AI trade across equities, rates and other holdings; a year later with equities down 50% a trend programme that cuts losses and can go short would be the protection, so the case for CTAs is that the world may change sharply after a quiet, noisy period.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check, time-bound view)_
  > equities are down 50%. What are you going to do with your portfolio where you're all in on the AI trade across
  indicator: equity drawdown / AI-theme concentration · asset: equities · direction: trend following protects in an equity bear · horizon: years · conditions: trend benefits from large regime shifts, suffers in noise · testable: partly - crisis-alpha of trend in equity bears testable · confidence: medium
  ^MT221-C12-X2
- **Jim (volatility specialist)** Trend followers cut losing positions rather than holding with a white-knuckle grip, but many allocators want a narrative of conviction (an iron spine, such as buying Bitcoin at 20,000 because it would recover), so the strategy's disciplined loss-cutting is hard to sell.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > But a lot of allocators want to hear that you have a like an iron spine.
  asset: multi · testable: no - behavioural observation · confidence: medium
  ^MT221-C12-X3

### C13
- **Andrew (replication ETF manager)** With wide manager dispersion and no persistence of alpha, allocators chase the recent winner with a brand name and oversell it, creating a negative feedback loop when it underperforms.  #mech/behavioral
  > a typical allocator who is not as well versed in statistics of no persistence of alpha and a wide dispersion is will tend to um oversell a a given an individual manners outperforms
  indicator: manager dispersion; performance persistence · asset: multi · horizon: years · testable: yes - persistence of CTA manager returns · confidence: medium
  ^MT221-C13-1
- **Andrew (replication ETF manager)** In an exchange-traded wrapper the price and drawdown are visible every day and minute, so investors react to drawdowns more than in a monthly-reported fund; drawdowns do matter to ETF holders.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > no, people don't like draw down. They don't like it because you can see it every day. You can see it every minute.
  asset: multi · horizon: days · conditions: applies to daily-priced ETF vehicles · testable: no - behavioural observation · confidence: medium
  ^MT221-C13-X1
- **Andrew (replication ETF manager)** Allocators trained to buy the dip look for a story that explains a rebound after a drawdown, but financially sophisticated CTA managers honestly say they do not know it will rebound (they have exited the losing positions and will find new trends), and this honesty works against wider adoption.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > honesty and equivocation actually plays against the broader adoption of
  asset: multi · testable: no - behavioural observation · confidence: medium
  ^MT221-C13-X2
- **Andrew (replication ETF manager)** To make managed futures a standard allocation, present it as a strategic long-term holding judged by its benefit to the overall portfolio instead of model details such as lookback lengths or number of positions; the speaker expects this to be tested over five years.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > if you can get people to focus on this as a strategic long-term allocation and and basically get them focused on day one not on the gears and how they work
  asset: multi · horizon: years · testable: no - adoption prediction · confidence: low
  ^MT221-C13-X3

### C14
- **Rob (systematic trader)** A Sharpe-1 strategy run at half Kelly implies roughly 40-50% annualised volatility, so high-vol CTA products are feasible and could be sold to retail at higher fees as a proportion of vol (offered half in jest).  #mech/risk_management
  > even if we run that at sort of half Kelly, we we could be running at sort of annualized risk of sort of 40 50%.
  indicator: Sharpe ratio, Kelly fraction, volatility target · asset: multi · direction: scale volatility up to half Kelly · conditions: assumes Sharpe near 1 and positive skew · testable: yes - Kelly arithmetic · confidence: low
  ^MT221-C14-1
- **Andrew (replication ETF manager)** The large pool of money in managed futures products is risk-averse allocators focused on avoiding embarrassment, not leverage-seeking retail; niche ETF structures (return stacking, buffered, covered call) can still reach multi-billion scale (an ETF firm sold for about $2 billion).  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > the big money is is are the people who are riskaverse and and who spend 80% of their me mental energy how to avoid being embarrassed
  asset: multi · horizon: years · testable: no - commercial/market observation · confidence: low
  ^MT221-C14-X1

### C15
- **Andrew (replication ETF manager)** Higher interest rates make capital efficiency (return stacking, portable alpha, yield stacking) valuable again, so growth in 2x/3x and stacked ETFs reflects a need to do more with less capital, not a desire for more risk.  #mech/liquidity_flows
  > I wouldn't say leverage as much as capital efficiency right the the return stack
  indicator: interest rates / cash rate · asset: multi · horizon: years · conditions: after zero-rate era · testable: no - structural trend · confidence: medium
  ^MT221-C15-1
- **Katie (CTA researcher)** The Barclay CTA index volatility fell from 20-25% in the 1980s/early 1990s to below 5% in recent years as institutions entered and assets grew.  #mech/structural_shift
  > the Barkley uh CTA index were running at an annualized volatility of between 20 and 25%. And since then it's gone down and actually in the last few years we are now below 5%
  indicator: Barclay CTA index annualised volatility · asset: multi · horizon: years · testable: yes - index data · confidence: high
  **Correction (cross-check):** Wrong speaker: the Barclay CTA index volatility figures (20-25% in the 1980s and early 1990s, below 5% now) are stated by the host Neils, interjecting after Katie. Katie only supplied the explanation that institutions entered and assets grew. → Host Neils: the Barclay CTA index ran at 20-25% annualised volatility in the 1980s and early 1990s and is below 5% in recent years; Katie (preceding remark): institutional adoption and larger assets pushed managers toward lower-risk, size-management programmes.
  ^MT221-C15-2
- **Katie (CTA researcher)** A daily-liquid high-volatility CTA product cannot smooth its prints as private equity does, so it will attract performance-chasing inflows after good runs and then disappoint investors in drawdowns, as with Bitcoin; old-school high-vol CTAs avoided this because there was no daily ticker.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > it's going to be great when it goes up just like Bitcoin and it's going to be terrible when it goes down
  asset: multi · conditions: applies to daily-priced, high-volatility products · testable: no - behavioural prediction · confidence: medium
  ^MT221-C15-X1

### C16
- **Allan (CTA researcher)** Wealth portfolios should hold a balanced, diversified portfolio and then apply leverage to reach the desired risk, rather than adding equities for risk.  #mech/risk_management
  > you want more risk will give you more equities whereas in fact you should have a balanced portfolio and then decide how much leverage to apply to it
  asset: multi · direction: balanced portfolio plus leverage · testable: partly - risk parity-style backtest · confidence: medium
  ^MT221-C16-1
- **Allan (CTA researcher)** Prediction that US 10-year yields rise to 6% and then fall to 3.5% in 2026.  #mech/policy_reaction _(time-bound view)_
  > so I think next year will be the year of the bond breakout. So, US 10ear yields up to 6% and then down to 3 and a half%.
  indicator: US 10-year yield · asset: rates · direction: long volatility in rates · horizon: months · conditions: 2026 · testable: no - single prediction · confidence: low
  ^MT221-C16-2
- **Jim (volatility specialist)** 2026 resembles 2022 with stocks down and rates up as the pain trade, because investors hold stocks with long-vol band-aids and bonds as diversifier; VIX and implied vol hedges could pay.  #mech/crowding_positioning _(time-bound view)_
  > That 2026 will in a lot of ways look like 2022. Uh the pain trade will be market down and interest rates up.
  indicator: equities, interest rates, VIX · asset: multi · direction: short equities, short bonds, long VIX · horizon: months · conditions: 2026 · testable: no - prediction · confidence: medium
  ^MT221-C16-3
- **Allan (CTA researcher)** High-volatility trend managers (a long-standing example is Mulvaney) have a repeating cycle of exceptional years, asset raising, deep drawdown and asset loss, so a high-vol ETF version would probably follow the same flow cycle; institutions had moved to low-vol trend, with some swing back to high-vol launches.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > they go through exceptional periods raise some assets they have a draw down lose a lot of assets it repeats.
  asset: multi · horizon: years · testable: partly - manager return/AUM history testable · confidence: medium
  ^MT221-C16-X1
- **Katie (CTA researcher)** 2026 prediction: a boom-and-bust roller coaster, with rates falling and over-stimulation of the US economy making conditions look strong before things suddenly fall apart; 2026 could be a pivotal year for the macro change seen in 2025.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > rates go lower over stimulation of the US economy and we could things could look awesome and then suddenly things could fall apart.
  asset: multi · direction: boom then bust · horizon: months · testable: no - view with little supporting reasoning · confidence: low
  ^MT221-C16-X2
- **Andrew (replication ETF manager)** 2026 prediction (self-described low probability, high significance): institutions begin buying managed futures ETFs, as most institutional allocators hold a hedge fund analyst mandate and look for hedge funds rather than ETFs.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check, time-bound view)_
  > I think institutions start buying ETFs in the managed future space.
  asset: multi · horizon: years · testable: no - prediction · confidence: low
  ^MT221-C16-X3

### C17
- **Mark (CTA manager)** 2026 view: higher inflation raises Treasury yields, credit crises carry over from 2025, MAG 7 bubble bursts pulling equities down, and Europe resurges.  #mech/fiscal_debt _(time-bound view)_
  > You're going to see higher inflation, which means higher uh yields on uh on treasuries.
  indicator: inflation, Treasury yields, MAG 7 · asset: multi · direction: long Europe; short MAG 7, bonds · horizon: months · conditions: 2026 · testable: no - prediction · confidence: medium
  ^MT221-C17-1
- **Neils (host)** Prediction that the Fed has to hike at least once in 2026 despite political pressure.  #mech/policy_reaction _(time-bound view)_
  > the Fed the Fed will end up having to hike rates uh next year at least once.
  indicator: Fed funds rate · asset: rates · direction: short bonds · horizon: months · conditions: 2026 · testable: no - prediction · confidence: low
  ^MT221-C17-2
- **Yov (CTA manager)** 2026 view: equities up 25% would be the speaker's wish, but the more likely outcome is a 10-year Treasury yield of about 6%.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > Equities up 25%. Uh that will make me happy. Uh but I'm afraid I'm kind of uh I'm kind of in the camp of 6% 10 year rate uh most likely.
  indicator: US 10-year yield · asset: rates · direction: 10-year yield up to about 6% · horizon: months · testable: no - one-line prediction · confidence: low
  ^MT221-C17-X1

