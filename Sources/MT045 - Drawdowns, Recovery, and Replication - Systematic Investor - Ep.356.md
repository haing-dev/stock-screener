---
source_id: MT045
title: "Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356"
date: 2025-07-17
channel: "Top Traders Unplugged"
url: 
words: 11233
claims: 59
added_by_crosscheck: 7
corrections: 1
crosscheck: "opus cross-check"
speakers: ["Niels Kaastrup-Larsen (host, Top Traders Unplugged)", "Katy Kaminski (AlphaSimplex, trend following researcher; caption 'Katie Kaminsky')"]
tags: [source, layer0]
---
# Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356

**Speakers:** Niels Kaastrup-Larsen (host, Top Traders Unplugged); Katy Kaminski (AlphaSimplex, trend following researcher; caption 'Katie Kaminsky')

**Summary:** Top Traders Unplugged Ep.356 (mid July 2025): Katy Kaminski on her paper about managed futures drawdowns and recovery, exogenous vs endogenous shocks, a non-parametric regime paper and CTA replication. Conclusions: drawdowns coincide with strong equities and recover fast in stress, rebalance rather than time trend, replicators outperformed due to slower speed and smaller sets.

**Approach:** trend following, drawdown recovery, regimes, replication, shocks

**Cross-check completeness estimate of first read:** 0.94 - first reader covered the drawdown paper, shock types, regime method and replication debate well; missed one disagreement (low rates vs Trump for 2015-19), the turbulence metric and the Denmark/euro aside, and misattributed one explanation.

## Argument map

**Episode thesis:** Katy Kaminski (AlphaSimplex) and Niels Kaastrup-Larsen (Systematic Investor Ep. 356, recorded in early-to-mid July 2025, uploaded 17 July) argue that managed-futures drawdowns come when equities do well and recover quickly when equities are stressed, so trend is useful in both states, that trend should not be timed but rebalanced into (it mean-reverts at long horizons), and that trend remains one of the few robust equity complements that pays in distress. Fast-reversing exogenous shocks such as Liberation Day are the worst for trend while fundamentals-based endogenous shocks (monetary policy, inflation) tend to help. Kaminski reviews a non-parametric regime method (Harvey et al.) as an empirical filter and explains that CTA replicators outperformed in 2025 mainly because they are smaller in market set and slower, not through luck.

### Katy Kaminski (Guest; trend-following researcher and chief research strategist at AlphaSimplex (Boston); lead author of the managed-futures drawdown paper discussed)
Fingerprint: #approach/trend_following #approach/crisis_alpha_convexity #approach/regime_detection #approach/replication_indexing #approach/portfolio_construction_stacking #approach/research_robustness_overfitting #approach/diversification_risk_parity
_Speaker note: Ledger spelling 'Katy Kaminski' (captions 'Katie Kaminsky'). Her China-markets explanation is explicitly 'my first guess'. She did not claim to have memorised replication tracking-error numbers. Remarks on the Harvey et al. regime paper are a reading of someone else's work, with her own criticisms._

**Worldview premises**
- Trend drawdowns tend to occur while equities do very well, and recoveries are faster when equities are stressed and slower when equities keep making new highs, so trend looks good coming out of a drawdown in either state. _[empirical, stated; support: Her paper plotting drawdown depth, duration and recovery of the SG Trend Index against equity returns; the largest managed-futures drawdown above 10% was 2015-2019.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C05-1|C05-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C05-3|C05-3]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C06-1|C06-1]])
- Drawdown and recovery times vary a lot, so the current drawdown could recover quickly or slowly; the CTA winter (2010-2014, second longest) came after the GFC recovery and ended with the 2014 energy collapse. _[empirical, stated; support: Historical drawdown plot.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C05-2|C05-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C08-4|C08-4]])
- Trend should not be timed ('trend following squared'); because the strategy mean-reverts over longer horizons, investors should rebalance (buy after drawdowns, trim after gains), as many institutions do after a big year like 2022. _[empirical, stated; support: Long histories showing 15-20% drawdowns followed by strong recoveries; institutional behaviour she observes.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C09-2|C09-2]])
- Trend following is one of the few robust equity complements that pays in distress and no better alternative has been found; institutions layer defensive diversifiers ('first, second, third responders') with trend as one layer. _[empirical, stated; support: Empirical evidence including her drawdown paper and CFM work on skew; she notes papers exist with significant p-values but few with comparable robustness.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C10-1|C10-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C10-2|C10-2]])
- Fixed-income trend depends on regime: strong in falling rates with a steep curve, strong short when the curve is inverted, mixed when flat; fixed income was choppy in 2025 so trend signals gave it little weight. _[empirical, stated; support: Her earlier fixed-income paper; 2025 steepening/flattening and Fed back-and-forth.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C07-1|C07-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C04-1|C04-1]])
- Initial rhetoric-driven shocks are bad for trend; trends emerge once fundamental data show the new direction (e.g., a copper tariff linked to copper). Isolated tariff events can start trends in metals; the commodity sector gives diversification most investors do not hold directly. _[theoretical, stated; support: Observation of copper/platinum signals building on trade tension.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C08-1|C08-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C03-2|C03-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C03-3|C03-3]])
- Trump 1.0 tweets produced little trend, whereas Trump 2.0 coincides with larger global change in geopolitics, supply chains and alliances; the 2015-2019 drawdown was not mainly a trade-war effect but also reflected the very low rate environment. _[experience, stated; support: Her earlier study of Trump's tweets found little trend.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C07-4|C07-4]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C07-X1|C07-X1]])
- Exogenous shocks that reverse quickly (whipsaw) are the worst for trend but those that extend can help; Covid was less damaging than Liberation Day because supply-chain trouble was anticipated and bonds rallied, giving trends outside equities. After Liberation Day, further shocks (copper tariffs) get smaller reactions, and endogenous shocks (monetary policy, inflation), being fundamental valuation shifts, tend to help trend and are more likely next. _[theoretical, stated; support: Comparison of Covid and Liberation Day; turbulence metrics (magnitude-of-surprise) to size shocks.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C11-1|C11-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C11-2|C11-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C11-3|C11-3]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C11-4|C11-4]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C11-X1|C11-X1]])
- A three-day shock followed by a rebound is too short to detect statistically, unlike Covid which lasted a month or two, so shorter-term trend did well in Covid but not on Liberation Day. _[empirical, stated; support: Horizon argument; no data cited.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C12-2|C12-2]])
- Pre-defining regimes (rising or falling rates) creates bias and rule-based regime definitions overfit history, so non-parametric methods and walk-forward testing that account for how many variables were tried are preferable; the Harvey et al. method uses seven standardised state variables and a Euclidean distance of the current month to all past months, then assumes strategies that did well in similar months will do well next. _[theoretical, stated; support: Her reading of the paper; critics say the seven variables were chosen with hindsight; she calls it data filtering and not macro.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C12-3|C12-3]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C13-1|C13-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C13-2|C13-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C14-1|C14-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C14-R2|C14-R2]])
- Trend likely connects to recessionary regimes (e.g., an inverted curve in fixed income), which the non-parametric method could test. _[theoretical, stated; support: Her fixed-income paper; her stated homework assignment.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C14-2|C14-2]])
- Replicators outperformed in 2025 mainly because they are smaller in market set and slower, so they reacted less to Liberation Day; tracking error is within the expected range; regression-based replication is the slowest, mechanical or hybrid replication faster; differences reflect market regimes (e.g., cocoa missed) not luck. _[empirical, stated; support: Her replication paper's methodology (not updated since); she did not recall exact tracking-error figures.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C15-1|C15-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C15-2|C15-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C15-3|C15-3]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C16-1|C16-1]])
- Tracking error depends on market set and implementation, so investors must understand the replicator's inputs and trading to measure it; replication can be a separate strategy combined with CTAs to reduce dispersion. _[institutional, stated; support: Her replication paper; client feedback.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C16-2|C16-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C16-3|C16-3]])
- China-focused CTA programs did worse than traditional CTAs in June 2025, probably because Chinese futures are commodity heavy: energies spiked and reversed on geopolitics while supply-chain metals trended differently from other markets (her stated first guess, unchecked). _[experience, stated; support: Guess; she had not looked at the data.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C02-1|C02-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C02-R1|C02-R1]])
- Discretionary investors who cut equities in April find it psychologically hard to buy back at record highs, whereas systematic managers are indifferent; sentiment shifted in early July 2025 toward better growth with rotation into US small caps. _[behavioural, stated; support: Observation of investor sentiment over the previous two weeks.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C04-3|C04-3]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C04-4|C04-4]])

**Chain: Trend drawdown timing relative to equity state**
1. Equities making new highs and conditions benign → Trend drawdowns (trend is harder when things are good) and slower recoveries: Plotting each SG Trend Index drawdown against equity returns shows a clear theme. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C05-3|C05-3]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C06-1|C06-1]])
2. Equity stress → Faster trend recovery from drawdowns: Trend does well in distress, rebuilding quickly. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C06-1|C06-1]])
3. Trend mean-reverts at long horizons → Rebalance into it after drawdowns rather than time it: Strong recoveries once they begin; unpredictable start. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C09-2|C09-2]])
4. Blend trend with S&P 500 → Nearly the sum of both returns (portable alpha), driving new overlay products: Low correlation with positive carry in both; the host's own numbers. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C06-2|C06-2]])
- Evidence: Kaminski's drawdown paper (bubble chart of drawdown depth, length and equity return); the host's blended-return illustration.
- Fails when: The next recovery could be slow or fast; the timing of when recovery starts is unknown ('when does it start?').

**Chain: Exogenous versus endogenous shocks and trend**
1. Rhetoric-driven exogenous shock that reverses within days (Liberation Day tariff announcement, three-day move, then rebound) → Whipsaw losses; short horizon too brief to detect statistically: Understood instantly by everyone, no time to position; quick reversal. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C11-1|C11-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C12-2|C12-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C11-5|C11-5]])
2. Slowly understood shock (Covid), bonds rally, supply-chain anticipated → Trends outside equities; time to get short energy: News is digested at different speeds. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C11-2|C11-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C11-5|C11-5]])
3. Further tariff shocks after the first (copper) → Smaller market reactions, fragile positions that the next statement can reverse: The change has already occurred; tariffs can be reversed. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C11-3|C11-3]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C08-2|C08-2]])
4. Endogenous shocks (monetary policy, inflation, structural rates change as in 2022) → Trends that extend, because they are fundamental revaluations: They shift how assets are valued. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C11-4|C11-4]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C08-3|C08-3]])
- Evidence: CFM exogenous/endogenous work (relayed by the host); Kaminski's turbulence paper and her case comparison; order reversal of short-term versus long-term managers (April versus May-June 2025).
- Fails when: Exogenous shocks that extend can help; in Trump 2.0 the supply-chain and alliance change may be large enough to produce sustained trends.

**Chain: Non-parametric regime filter**
1. Seven standardised state variables (equities, yield-curve shape, volatility, copper, etc.) → Euclidean distance of this month to every past month in seven-dimensional state space: Defines how similar the present is to any history without defining regimes. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C13-1|C13-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C12-3|C12-3]])
2. Rank past months by similarity → Look at which strategies (value, trend) did well in similar months and overweight them next month: Assumes regimes are somewhat persistent. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C13-2|C13-2]])
- Evidence: The Harvey et al. paper as she summarises it; she says she would like to grill the authors about implementation.
- Fails when: If the variables were chosen with hindsight or many more were tried (e.g., 70 and the best seven shown); needs walk-forward testing.

**Chain: Why replicators outperformed in 2025**
1. Replicators trade a smaller, mostly developed-market set and move slowly → They reacted less to the Liberation Day shock and stayed near average CTA returns: Slow and small market sets avoid whipsaw. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C15-1|C15-1]])
2. Replicators miss markets outside their set (cocoa) → Differences reflect market regimes, not luck: Regime-dependent market coverage. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C16-1|C16-1]])
3. Regression-based replication is the slowest; hybrid or mechanical versions are faster → Tracking error depends on implementation and market set: Method determines speed. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C15-3|C15-3]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C16-2|C16-2]])
- Evidence: Her replication paper (not updated); she cites tracking error within expected range.
- Fails when: Host raises luck: slow strategy happened to be right this time and could differ next year. She replies it is regime variation.

**Decision process**
- [portfolio] Do not time trend; rebalance into it after drawdowns and trim after gains.. Why: Mean reversion at long horizons; large recoveries once they begin. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C09-2|C09-2]])
- [portfolio] Build layered defensive portfolios of different diversifiers, with trend as one layer.. Why: Trend is robust but not a silver bullet. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C10-1|C10-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C10-2|C10-2]])
- [signal] In 2025 fixed income was underweighted by trend signals because of choppy steepening/flattening; weight depends on regime (falling rates with steep curve, or short with inverted curve).. Why: Fixed-income trend is regime-dependent. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C04-1|C04-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C07-1|C07-1]])
- [research] Use walk-forward tests and account for how many variables were tried; avoid rule-based regime definitions; prefer non-parametric similarity filters.. Why: Rules overfit history. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C14-1|C14-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C12-3|C12-3]])
- [research] Use turbulence (magnitude-of-surprise) metrics to identify and size exogenous shocks when studying their effects on trend.. Why: Quantifies shock size across assets. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C11-X1|C11-X1]])
- [other] Evaluate replication by understanding inputs (market set, trading speed) so tracking error can be measured; treat replication as a separate strategy to combine with CTAs.. Why: Tracking error varies with approach. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C16-2|C16-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C16-3|C16-3]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C15-3|C15-3]])
- [other] Look for fundamental data confirming the new direction rather than trading rhetoric-driven shocks.. Why: Rhetoric shocks are often bad for trend. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C08-1|C08-1]])

**Evidence style:** Empirical and visual (bubble charts of drawdowns against equity returns), long-history studies and her own papers; skeptical of rule-based regimes; admits what she has not checked (China markets, replication numbers).

**Views at the time**
- (2025-07 (early-mid July 2025)) Equities and a weak dollar trended most in 2025 (the dollar began to revert in July); fixed income choppy; energies spiked, reversed and rebounded in June-July; metals tied to trade policy more interesting.. Reasoning: Observed trend contribution by sector. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C03-5|C03-5]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C04-1|C04-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C04-2|C04-2]])
- (2025-07) Sentiment toward equities has tentatively turned positive (growth better than thought; rotation to US small caps), and systematic managers are indifferent while discretionary investors struggle to buy back at record highs.. Reasoning: Two-week sentiment shift. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C04-3|C04-3]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C04-4|C04-4]])
- (2025-07) The current managed-futures drawdown could recover fast or slowly, but is not a reason to leave; rebalance into it.. Reasoning: Drawdown history. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C05-2|C05-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C09-2|C09-2]])
- (2025-07) Further tariff shocks (copper) bring smaller reactions; endogenous shocks (monetary policy, inflation) are more likely next and would help trend.. Reasoning: The shock has already occurred. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C11-3|C11-3]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C11-4|C11-4]])
- (2025-07-09/10) Metals (copper, platinum) are building long signals on trade tension and potential tariffs, with small positioning so far.. Reasoning: Isolated event linked to trend; fundamental data needed to confirm. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C03-2|C03-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C08-1|C08-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C03-R4|C03-R4]])

### Niels Kaastrup-Larsen (Host of Top Traders Unplugged; veteran CTA manager (35 years in the industry))
Fingerprint: #approach/trend_following #approach/crisis_alpha_convexity #approach/behavioral_sentiment #approach/replication_indexing #approach/manager_selection_allocation #approach/portfolio_construction_stacking
_Speaker note: Reports CTA index levels and relays papers (Man Group, Ilmanen/AQR, CFM, Harvey et al.). He attributes the China-markets explanation to himself in the original ledger entry; correction: he only reported the underperformance and said he does not know why (the explanation is Kaminski's guess)._

**Worldview premises**
- Trend should be judged by its portfolio effect, not stand-alone Sharpe, and it is fantastic that something typically does poorly when equities do great: it would be worse if it always did poorly when equities were poor. _[theoretical, stated; support: Common-sense argument; criticism of those who use Sharpe for single line items.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C10-3|C10-3]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C10-R3|C10-R3]])
- A blend of trend following and the S&P 500 gives nearly the sum of both returns, which explains the stream of new portable-alpha overlay products. _[empirical, stated; support: His own return illustrations.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C06-2|C06-2]])
- Bonds have more inbuilt momentum while equities revert (V-shapes), so fixed income gives the best trend profits. _[empirical, stated; support: Ilmanen's paper (AQR) and his own return distributions.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C06-3|C06-3]])
- The worst trend drawdown-recovery combinations coincided with Trump trade-war periods (2018 and 2025); the post-Liberation Day S&P recovery (57 days, no Fed support) was the fastest ever from a 20% drawdown, a V-shape trend following is not built for. _[empirical, stated; support: Kaminski's chart and a colleague's statistic.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C07-2|C07-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C07-3|C07-3]])
- Tariff-driven positions such as long copper are fragile because the next statement can reverse them; recoveries often follow a real narrative change across a broad range of markets (e.g., rates rising after the post-GFC period). _[theoretical, stated; support: Examples from the CTA winter and 2022.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C08-2|C08-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C08-3|C08-3]])
- CTA index drawdowns of about 20% are small next to a 55% S&P 500 drawdown, and rolling 12-month CTA returns below -5% are rare compared to those above +15% (about 2-4 versus 59 instances, per the Man paper). _[empirical, stated; support: Man paper statistic (as of end of April).]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C08-5|C08-5]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C09-1|C09-1]])
- Investors chase performance and rarely rebalance into trend after poor returns; he sees people selling trend after it has done well. _[experience, stated; support: 35 years of industry experience.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C09-3|C09-3]])
- Trend works because everyone gets news at the same time but digests it at different speeds: a tariff is understood instantly, Covid took time, leaving room to position short energy. CFM's work separates exogenous (Liberation Day) from endogenous (2022 rates positioning) shocks. _[theoretical, stated; support: CFM paper and Covid example.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C11-5|C11-5]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C10-4|C10-4]])
- Short-term CTAs beat long-term in April 2025 (as expected for an exogenous shock) but the order reversed in May-June. _[empirical, stated; support: Official performance numbers.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C12-1|C12-1]])
- Replicators outperforming their benchmarks in 2025 implies either a large tracking error or a separate alpha strategy rather than replication. _[theoretical, stated; support: Logical argument; Andrew (a replication manager) scheduled as a guest.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C14-3|C14-3]])
- China-focused CTA programs did worse than traditional CTAs in June 2025; he does not know why (his firm does not trade Chinese markets). Staying outside the euro has served Denmark well. _[experience, stated; support: Observed programme returns; personal view on the euro.]_ ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C02-1|C02-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C02-X1|C02-X1]])

**Chain: Tariff news to copper to CTA positioning**
1. US tariff news on copper → COMEX copper up about 13% in a day, largest since 1968, while London and Chinese copper unaffected: Tariff only applies to the US-traded contract. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C03-1|C03-1]])
2. CTAs long metals before the move → Probably on the right side: Long metals signals built on trade tension. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C03-1|C03-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C03-4|C03-4]])
3. Tariff can be reversed by the next statement → Positions are fragile and not fundamentally anchored: He wants something more substantial than a tariff. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C08-2|C08-2]])
- Evidence: Market move and index reporting.
- Fails when: Reversal of tariff statements.

**Decision process**
- [other] Evaluate trend by contribution to the portfolio rather than as a line item with Sharpe.. Why: Sharpe misused for single strategies. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C10-3|C10-3]])
- [other] Watch replicators' tracking error and ask whether outperformance is tracking error or a separate alpha.. Why: Defining a tracking-error band is needed as products multiply. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C14-3|C14-3]])

**Evidence style:** Industry statistics from papers (Man, AQR, CFM), index levels, 35 years of experience, direct challenge questions.

**Views at the time**
- (2025-07 (early-mid July 2025)) Mid-July 2025 CTA indices are down about 3% to 10% year to date (BTOP50 -3.19%, SG CTA -7.4%, SG Trend -10%, short-term traders -5.11%) while MSCI World is +8.7% and S&P 500 +5.85%.. Reasoning: Index levels as of the previous night. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C04-5|C04-5]])
- (2025-07 (first week or so of July)) In early July CTAs are long equities and metals and short US fixed income with some gains in livestock and grains; European fixed income is tricky; July so far feels better than April-June.. Reasoning: Manager positioning and performance. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C03-4|C03-4]])
- (2025-07 (the day before recording)) COMEX copper's 13% one-day surge is likely a good outcome for CTAs but not a fundamental basis for lasting positions.. Reasoning: Tariff-driven. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C03-1|C03-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C08-2|C08-2]])
- (2025-07) Replication strategies' outperformance in 2025 means either large tracking error or a separate alpha strategy.. Reasoning: Benchmarks vs replicators. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C14-3|C14-3]])

### Disagreements
- **Why replicators outperformed CTAs in 2025**: Niels Kaastrup-Larsen: Either tracking error is large or replicators are a separate alpha strategy; also raises luck. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C14-3|C14-3]]); Katy Kaminski: Not luck: replicators are smaller in market set and slower, so they avoided much of the Liberation Day whipsaw; tracking error is within expected range, and regression-based replication is the slowest. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C15-1|C15-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C15-2|C15-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C15-3|C15-3]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C16-1|C16-1]])
- **Cause of the 2015-2019 trend drawdown**: Niels Kaastrup-Larsen: Trump trade-war periods (2018 and 2025) coincide with the two worst drawdown-recovery combinations; Trump and CTA performance do not go hand in hand. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C07-2|C07-2]]); Katy Kaminski: The 2015-2019 drawdown was not mainly a Trump effect; very low rates also contributed; Trump 1.0 tweets did not create much trend. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C07-X1|C07-X1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C07-4|C07-4]])
- **Are tariff-driven moves a basis for trend positions?**: Katy Kaminski: Once fundamental data (e.g., copper tariffs linked to copper) show the new direction, trends emerge in asset classes; isolated events can link to trends that extend. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C08-1|C08-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C03-2|C03-2]]); Niels Kaastrup-Larsen: Positions based on tariff statements are fragile because they can be reversed next week; wants something more substantial than a tariff. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C08-2|C08-2]])
- **Do investors rebalance into trend after drawdowns?**: Katy Kaminski: Many institutions understand and rebalance (adjust allocations after profits in 2022); the right behaviour is to rebalance rather than time. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C09-2|C09-2]]); Niels Kaastrup-Larsen: Rarely sees investors rebalancing into trend after poor returns; sees them selling after good returns. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C09-3|C09-3]])
- **Why the China-focused CTA programs did worse in June 2025**: Niels Kaastrup-Larsen: Reports the underperformance and says he does not know why. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C02-1|C02-1]]); Katy Kaminski: First guess: Chinese futures are commodity heavy and energies were shocked while supply-chain metals trended, unlike other markets. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C02-1|C02-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C02-R1|C02-R1]])

### Gaps and conflicts
- The drawdown-state finding (drawdowns while equities do well, quick recoveries in stress) rests on equity returns as the only state variable and a graph described verbally; the causal story that trend underperforms when things are good is not tested for confounding (e.g., rates regime). ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C05-3|C05-3]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C06-1|C06-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C07-X1|C07-X1]])
- Kaminski says 'do not time, rebalance', but also says recoveries are strong once they start and the big question is when; the practical difference between rebalancing into a drawdown and timing a recovery is not defined. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C09-2|C09-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C06-1|C06-1]])
- Replicator outperformance is attributed to slowness and smaller market sets, but she did not recall tracking-error numbers and the paper has not been updated; the host raises luck and her response is regime variation, not a quantitative test. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C15-2|C15-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C15-1|C15-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C16-1|C16-1]])
- The Harvey et al. regime method is described from memory with open implementation questions (how many state variables were tried, hindsight selection of seven); Kaminski's own expectation of a trend link to recessionary regimes is a hypothesis awaiting test. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C14-1|C14-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C14-2|C14-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C12-3|C12-3]])
- The claim that Covid was less damaging than Liberation Day because supply chain trouble was anticipated and bonds rallied is an interpretation; the statement that further shocks get smaller reactions and endogenous shocks are 'more likely next' is a forecast without evidence. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C11-2|C11-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C11-3|C11-3]])
- The explanation for the China-focused CTA underperformance is a first guess by Kaminski, and the host's ledger attribution had to be corrected; no data was looked at. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C02-1|C02-1]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C02-R1|C02-R1]])
- Man paper statistics (number of rolling 12-month returns below -5% versus above +15%) are quoted from memory with an end-of-April cutoff; the exact counts (2 versus 59) are approximate. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C09-1|C09-1]])
- Claim that no better alternative to trend has been found is limited to her knowledge of papers; she acknowledges papers with significant p-values exist but with less robustness. ([[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C10-1|C10-1]])

### Forward-looking inputs (reader synthesis)
(reader) Inputs the speakers treat as informative for trend: the equity state (drawdowns coincide with strong equities; recoveries are faster in stress), the yield-curve shape for fixed-income trend (steep with falling rates, inverted for short trend), whether shocks are exogenous and quickly reversing or endogenous (monetary policy, inflation), fundamental confirmation of tariff or trade changes in metals and other commodities, turbulence (magnitude-of-surprise) metrics, and the seven-variable similarity filter. Horizon is months for regime and drawdown recovery, but Kaminski explicitly says timing trend is not advisable; the actionable input is rebalancing.

### Reader inferences (not stated by the speakers)
- (reader) Kaminski's through-line is that trend's value is conditional and portfolio-level: it pays when equity investors most need it (distress), and its drawdowns coincide with periods when the investor's equities are doing well, so the net portfolio experience is acceptable.
- (reader) Both speakers explain 2025 by shock type (rhetoric-driven exogenous shocks that reverse hurt; fundamental endogenous shifts help), which is a regime reading without a tested rule to trade on.
- (reader) The replication discussion shows a general principle in the episode: the speed and breadth of a strategy's implementation matter more than its labelled category when explaining a year's relative performance.
- (reader) The host's role is to supply counter-evidence and practical observation (investors do not rebalance; tariff positions fragile), and Kaminski's role is to supply conditional empirical structure.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, CME floor traders lawsuit; nothing actionable |
| C02 | 1 | China-focused CTA programs in June, euro and Bulgaria, dollar weakness chat |
| C03 | 5 | COMEX copper surge on tariffs, metals trends, July positioning, asset classes trending |
| C04 | 5 | fixed income and energies in trend, equity sentiment shift, index numbers, intro to drawdown paper |
| C05 | 3 | why the paper, drawdown sizes, durations and equity state during drawdowns |
| C06 | 3 | recovery speed vs equity regime, portable alpha blend, bond vs equity momentum |
| C07 | 4 | fixed income regimes, trade-war drawdowns, fastest S&P recovery, Trump 2.0 vs 1.0 |
| C08 | 5 | rhetoric vs fundamentals, copper tariff, CTA winter, CTA vs equity drawdown size |
| C09 | 3 | rolling returns, rebalancing not timing, investor behaviour, alternatives to trend |
| C10 | 4 | trend as equity complement, exogenous vs endogenous shocks intro |
| C11 | 5 | shock types and trend, Covid vs Liberation Day, digestion speed |
| C12 | 3 | short vs long term in shocks, introduction of non-parametric regime paper |
| C13 | 2 | regime paper method: state variables, distance metric, historical filtering |
| C14 | 3 | overfitting, trend and recessionary regimes, replication outperformance question |
| C15 | 3 | replication tracking error, slower and smaller sets, regression vs mechanical |
| C16 | 3 | replication regimes and tracking error; outro |
| C17 | 0 | outro |

## Claims

### C02
- **Niels Kaastrup-Larsen** China-focused CTA programs underperformed traditional CTAs in June 2025, probably because Chinese futures are commodity heavy and geopolitical moves hit energies hard, while metals trended.  #mech/cycle_persistence _(time-bound view)_
  > CTA programs that are focused on China markets actually had somewhat of a different experience in June, doing somewhat worse than the traditional CTA programs
  indicator: China-focused CTA programs vs traditional CTAs · asset: commodities · horizon: weeks · conditions: June 2025 · testable: yes - index comparison · confidence: medium
  **Correction (cross-check):** Attributes the explanation to Niels; Niels only reports that China-focused CTA programs did worse in June 2025 and says he does not know why. The commodity-heavy explanation is Kaminski's explicitly labelled first guess. → Niels: China-focused CTA programs did worse than traditional CTAs in June 2025. Kaminski (a guess): Chinese futures are commodity heavy, energies were shocked by geopolitics while some supply-chain metals trended, so results there differed from other markets.
  ^MT045-C02-1
- **Niels Kaastrup-Larsen** Staying outside the euro (Denmark) has worked better than joining because the country keeps control of its own interest rates, and the krone has stayed strong.  #mech/policy_reaction _(added by opus cross-check)_
  > I actually think Denmark has done better than the Euro zone because they stand outside and can still determine their own interest rates
  indicator: Danish krone; Denmark vs euro-area growth · asset: fx · horizon: years · testable: partly - Denmark vs euro-area outcomes, though the krone is pegged to the euro · confidence: medium
  ^MT045-C02-X1
- **Katy Kaminski** Kaminski's first guess for why China-focused CTA programs did worse in June 2025: Chinese futures are mostly commodities, which saw large geopolitically driven moves, energies were shocked while some supply-chain metals trended in a way not seen in other markets.  #mech/new _(added by map cross-check, time-bound view)_
  > the Chinese markets are a lot of commodity focused particularly the futures
  indicator: share of commodities in Chinese futures programs · asset: commodities · horizon: June 2025 · conditions: geopolitical conflict hitting energies · testable: yes - decompose China-program returns by sector · confidence: low
  ^MT045-C02-R1

### C03
- **Niels Kaastrup-Larsen** COMEX copper rose about 13% in a day on tariff news (largest since 1968) while London and Chinese copper were unaffected, and CTAs were likely on the right side.  #mech/policy_reaction _(time-bound view)_
  > this is the largest single day price surge in records going back to 1968
  indicator: COMEX copper · asset: commodities · direction: Copper up · horizon: days · conditions: tariff announcement · testable: yes - price data · confidence: high
  ^MT045-C03-1
- **Katy Kaminski** Isolated tariff events can start trends: long signals in metals (copper, platinum) were building on trade tension and potential tariffs.  #mech/policy_reaction _(time-bound view)_
  > it shows how isolated incidents can actually directly link to trends that extend
  indicator: metals trend signals · asset: commodities · direction: Long metals · horizon: months · testable: partly · confidence: medium
  ^MT045-C03-2
- **Katy Kaminski** The commodity sector provides diversification that most investors do not hold directly, which CTAs supply.  #mech/risk_management
  > it just shows the diversification of the commodity sector that you know a lot of investors don't really have exposure to directly
  asset: commodities · testable: partly · confidence: medium
  ^MT045-C03-3
- **Niels Kaastrup-Larsen** In early July 2025 CTAs were long equities and metals and short US fixed income with some gains in livestock and grains; European fixed income was tricky.  #mech/cycle_persistence _(time-bound view)_
  > also some short exposure in fixed income, US fixed income I should say, probably doing okay for for managers
  indicator: CTA positioning · asset: multi · direction: Long equities, long metals, short US bonds · horizon: weeks · testable: partly · confidence: medium
  ^MT045-C03-4
- **Katy Kaminski** Equities and a weak dollar trended most in 2025, though the dollar had started to revert in July.  #mech/cycle_persistence _(time-bound view)_
  > the two asset classes that have actually trended the most this year has been equities recently
  asset: multi · direction: Long equities, short USD · horizon: months · testable: yes · confidence: high
  ^MT045-C03-5
- **Katy Kaminski** Kaminski thinks CTA positioning in copper going into the tariff surge was probably small, though the event shows how isolated incidents can link to trends that extend.  #mech/new _(added by map cross-check, time-bound view)_
  > I think positioning probably small
  indicator: CTA copper position size · asset: commodities · conditions: COMEX copper tariff surge · testable: yes - manager position data · confidence: low
  ^MT045-C03-R4

### C04
- **Katy Kaminski** Fixed income was choppy (steepening and flattening, Fed back and forth) so trend signals gave it little weight.  #mech/cycle_persistence _(time-bound view)_
  > fixed income is definitely underweighted by trend falling signals
  asset: rates · horizon: months · testable: yes · confidence: high
  ^MT045-C04-1
- **Katy Kaminski** Energies spiked, reversed and rebounded in June-July 2025, which was hard for trend following, while metals tied to trade policy were more interesting.  #mech/overshoot _(time-bound view)_
  > energies were really tricky last month because they shocked big and then they came back down and now they're back up again
  indicator: energy prices · asset: commodities · horizon: weeks · testable: yes · confidence: high
  ^MT045-C04-2
- **Katy Kaminski** Discretionary investors who cut equities in April find it psychologically hard to buy back at record highs, while systematic managers are indifferent.  #mech/behavioral _(time-bound view)_
  > to now having to suddenly consider buying back at all-time highs I mean these are psychologically very difficult decisions to make
  asset: equities · horizon: months · testable: partly · confidence: medium
  ^MT045-C04-3
- **Katy Kaminski** Sentiment shifted in early July 2025 toward better growth with rotation into US small caps, a tentative environment for equities.  #mech/behavioral _(time-bound view)_
  > I've seen a pretty large shift in sentiment um in the last two weeks or so where the world is kind of saying actually growth looks a little better than we thought
  indicator: growth sentiment, small vs large cap · asset: equities · direction: Equities up · horizon: weeks · testable: partly · confidence: medium
  ^MT045-C04-4
- **Niels Kaastrup-Larsen** Mid-July 2025 CTA indices were down about 3% to 10% year to date while MSCI World was up 8.7% and S&P 500 up 5.85%.  #mech/cycle_persistence _(time-bound view)_
  > Stocken trend flat for the month so far, down 10% for the year
  indicator: CTA indices year to date · asset: multi · horizon: months · testable: yes - index data · confidence: high
  ^MT045-C04-5

### C05
- **Katy Kaminski** Among managed-futures drawdowns above 10%, the largest was 2015-2019 (Trump's first term era), and the paper plots drawdown depth, duration and recovery.  #mech/research_method
  > the largest draw down was actually between 2015 and 2019
  indicator: SG Trend Index drawdowns · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT045-C05-1
- **Katy Kaminski** Drawdown and recovery times vary a lot, so the current drawdown could recover fast or slowly.  #mech/cycle_persistence
  > that just shows that there's a lot of variation across different draw down periods
  indicator: drawdown duration and recovery · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT045-C05-2
- **Katy Kaminski** Trend drawdowns tend to occur while equities are doing very well (shown with equity returns during each SG Trend Index drawdown).  #mech/risk_premium
  > equities tend to be doing very well. Um, when things are difficult for us
  indicator: equity return during trend drawdown · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT045-C05-3

### C06
- **Katy Kaminski** Recoveries from trend drawdowns are faster when equities are stressed and slower when equities keep making new highs, so trend is useful in both.  #mech/cycle_persistence
  > it tends to be really challenging environments, recovery is a lot faster
  indicator: drawdown recovery time vs equity returns · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT045-C06-1
- **Niels Kaastrup-Larsen** A blend of trend following and the S&P 500 gives nearly the sum of both returns (portable alpha), explaining the stream of new overlay products.  #mech/risk_management
  > you almost get the sum of the two meaning both returns on top of each other
  indicator: trend plus equity blend · asset: multi · horizon: years · testable: yes - blend backtest · confidence: high
  ^MT045-C06-2
- **Niels Kaastrup-Larsen** Per Ilmanen's paper, bonds have more inbuilt momentum while equities revert (V-shapes), so fixed income gives the best trend profits.  #mech/behavioral
  > even though people think of say fixed income as more mean reverting, it actually has an more of an inbuilt momentum
  indicator: trend returns by asset class · asset: multi · direction: Bond trend > equity trend · horizon: years · testable: yes · confidence: medium
  ^MT045-C06-3

### C07
- **Katy Kaminski** Fixed-income trend depends on regime: strong in falling rates with a steep curve, strong short when the curve is inverted, mixed when flat as now.  #mech/cycle_persistence
  > trend has done very well in a falling rate environment especially when the curve is steep
  indicator: rate direction, yield curve slope · asset: rates · direction: Long bonds in falling rates with steep curve; short when inverted · horizon: years · testable: yes - regime study · confidence: high
  ^MT045-C07-1
- **Niels Kaastrup-Larsen** The two worst trend drawdown-recovery combinations coincided with Trump trade-war periods, 2018 and 2025.  #mech/policy_reaction
  > the worst two are really the uh the trade war number one which is Trump's first uh term and then now the liberation
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT045-C07-2
- **Niels Kaastrup-Larsen** The post-Liberation Day S&P recovery (57 days, no Fed support) was the fastest ever from a 20% drawdown, a V-shape that trend following is not built for.  #mech/overshoot _(time-bound view)_
  > the recovery that we've seen in the S&P 500 uh, since liberation day uh, of a 20% or more draw down is the quickest recovery on record
  indicator: S&P 500 recovery time · asset: equities · horizon: weeks · testable: yes - price data · confidence: high
  ^MT045-C07-3
- **Katy Kaminski** Trump 1.0 tweets did not create much trend, but Trump 2.0 coincides with larger global change in geopolitics and supply chains.  #mech/structural_shift _(time-bound view)_
  > we were doing a a study of Trump's tweets and we just didn't find that much trends that he could trump
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT045-C07-4
- **Katy Kaminski** Kaminski disputes that the 2015-2019 trend drawdown was mainly a Trump trade-war effect; the very low rate environment of that period was also a cause.  #mech/policy_reaction _(added by opus cross-check)_
  > I don't necessarily think that the longest draw down was particularly just linked to that particular presidency. It was just a period with very low rates as well.
  indicator: policy rate level during trend drawdowns · asset: multi · direction: trend returns weaker when rates are pinned near zero · horizon: years · conditions: disagrees with Niels's Trump attribution · testable: yes - trend returns conditioned on rate level · confidence: medium
  ^MT045-C07-X1

### C08
- **Katy Kaminski** For trend, initial rhetoric-driven shocks are bad, but once fundamental data show the new direction (e.g. copper tariffs) trends emerge in asset classes.  #mech/slow_reaction
  > the initial shock is often bad because it's based on rhetoric and people realizing that change is coming
  asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT045-C08-1
- **Niels Kaastrup-Larsen** Tariff-driven positions (long copper) are fragile because tariffs can be reversed by the next statement.  #mech/policy_reaction _(time-bound view)_
  > I'm hoping for something a little bit more substantial than than a tariff
  asset: commodities · horizon: weeks · testable: no · confidence: medium
  ^MT045-C08-2
- **Niels Kaastrup-Larsen** Trend recoveries often follow a real narrative change in a broad range of markets, such as rates rising after the post-GFC period.  #mech/structural_shift
  > recoveries are often linked to kind of an real narrative change
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT045-C08-3
- **Katy Kaminski** The 'CTA winter' (2010-2014, second longest drawdown) came after the GFC when the world recovered and ended with the 2014 energy collapse.  #mech/cycle_persistence
  > that period before 2014 before energies um exploded
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT045-C08-4
- **Niels Kaastrup-Larsen** CTA index drawdowns of about 20% are small next to a 55% S&P 500 drawdown.  #mech/risk_management
  > CTA drawdowns are so much smaller than equity draw down
  indicator: drawdown comparison · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT045-C08-5

### C09
- **Niels Kaastrup-Larsen** The Man paper shows rolling 12-month CTA returns below -5% are very rare compared to returns above +15% (about 59 vs 2-4 instances).  #mech/research_method
  > the rolling 12 months return that are less than minus5% for the CTA index
  indicator: rolling 12-month CTA index return · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT045-C09-1
- **Katy Kaminski** Do not time trend following; the strategy mean-reverts at long horizons, so rebalance (buy after drawdowns, trim after gains).  #mech/cycle_persistence
  > the key is you shouldn't time, but you should, you know, rebalance
  asset: multi · horizon: years · testable: yes - rebalancing study · confidence: high
  ^MT045-C09-2
- **Niels Kaastrup-Larsen** Investors chase performance and rarely rebalance into trend after poor returns.  #mech/behavioral
  > I see people selling trend after it's done well. I rarely see people buying trend when it's done poorly
  asset: multi · horizon: years · testable: partly - flow data · confidence: medium
  ^MT045-C09-3

### C10
- **Katy Kaminski** Trend following is one of few robust equity complements that pays in distress; no better alternative has been found.  #mech/risk_premium
  > it's one of the few things that tends to on average um do well during periods of distress or challenging equity markets
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT045-C10-1
- **Katy Kaminski** Institutions build layered defensive portfolios of different diversifiers, trend as one layer.  #mech/risk_management
  > I have my you know my first responders, my second responders, my third responders
  asset: multi · testable: no · confidence: medium
  ^MT045-C10-2
- **Niels Kaastrup-Larsen** Evaluate trend by its portfolio effect, not stand-alone Sharpe.  #mech/risk_management
  > a lot of people like to look at individual line items rather than looking at what the effect on the portfolio is doing and they use sharp for something they should never use sharp for
  asset: multi · testable: yes · confidence: medium
  ^MT045-C10-3
- **Niels Kaastrup-Larsen** CFM's work separates exogenous shocks (Liberation Day tariffs) from endogenous ones (2022 rates positioning) for CTA performance.  #mech/research_method
  > exogenous shocks and impacts on CTO CTA performance versus indogenous so things that comes from inside the system and not from the outside
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT045-C10-4
- **Niels Kaastrup-Larsen** A diversifier that does poorly when equities do great is acceptable and even desirable; it would be a lot worse if it always did poorly when equities were doing poorly.  #mech/new _(added by map cross-check)_
  > it would be a lot worse if it always did poorly when your equities were doing poorly
  indicator: trend returns versus equity returns · asset: multi-asset · testable: partly - conditional correlation of trend to equity regimes · confidence: high
  ^MT045-C10-R3

### C11
- **Katy Kaminski** Exogenous shocks that reverse quickly (whipsaw) are the worst for trend, but those that extend can help.  #mech/overshoot
  > an exogenous shock that is not sustainable in shorter term that just is sort of a whipssaw those are the worst
  asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT045-C11-1
- **Katy Kaminski** Covid was less damaging than Liberation Day because supply chain trouble was anticipated and bonds rallied, giving trends outside equities.  #mech/slow_reaction
  > they started buying bonds so there were some interesting trends that actually leaked out in other asset classes in COVID
  asset: multi · direction: Long bonds, short energy · horizon: months · testable: partly · confidence: medium
  ^MT045-C11-2
- **Katy Kaminski** After Liberation Day, further shocks (copper tariffs) get smaller reactions; endogenous shocks (monetary policy, inflation) are more likely next.  #mech/behavioral _(time-bound view)_
  > the market is much more reticent to react because the change and the shock has already occurred
  asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT045-C11-3
- **Katy Kaminski** Endogenous shocks (policy, inflation) tend to help trend because they are fundamental valuation shifts.  #mech/structural_shift
  > endogenous shocks tend to be more positive for uh trend perhaps because it's it's really a fundamental based shift in sort of how people are valuing assets
  asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT045-C11-4
- **Niels Kaastrup-Larsen** Trend works because news is digested at different speeds; a tariff is understood instantly but Covid took time, leaving time to position short energy.  #mech/slow_reaction
  > we all get the news at the same time but we kind of digest it at different speeds
  asset: multi · horizon: weeks · testable: no · confidence: medium
  ^MT045-C11-5
- **Katy Kaminski** Turbulence metrics (magnitude-of-surprise measures across assets) can be used to identify and size exogenous shocks when studying their effect on trend following.  #mech/research_method _(added by opus cross-check)_
  > we wrote a great paper a couple years ago on turbulence and actually that man paper mentioned the turbulence metrics
  indicator: market turbulence index (magnitude surprise) · asset: multi · horizon: days · testable: yes - turbulence index vs trend returns · confidence: medium
  ^MT045-C11-X1

### C12
- **Niels Kaastrup-Larsen** Short-term CTAs beat long-term in April 2025 but the order reversed in May-June.  #mech/cycle_persistence _(time-bound view)_
  > Short-term doing better like it should uh compared to long-term, but actually it's kind of completely reversed in the last uh couple of months
  indicator: short-term vs long-term CTA · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT045-C12-1
- **Katy Kaminski** A three-day shock followed by rebound is too short to detect statistically, unlike Covid, which lasted a month or two.  #mech/slow_reaction
  > in liberation day it was really just you know a three-day move two or three days
  asset: multi · horizon: days · testable: yes · confidence: high
  ^MT045-C12-2
- **Katy Kaminski** A non-parametric regime approach avoids pre-defining regimes (rising or falling rates), which creates bias; critics say the seven state variables were chosen with hindsight.  #mech/research_method
  > nonparametric means that you're not sort of defining parameters to define regimes
  asset: multi · testable: yes · confidence: high
  ^MT045-C12-3

### C13
- **Katy Kaminski** The Harvey et al. regime method standardises seven state variables (equities, yield curve shape, volatility, copper, etc.) and measures Euclidean distance of the current month to every past month.  #mech/research_method
  > what is known as a uklidian distance measure or a measure of similarity
  indicator: seven state variables; Euclidean distance · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT045-C13-1
- **Katy Kaminski** Strategies that did well in similar past months are expected to do well next month, so one overweights trend or value accordingly.  #mech/cycle_persistence
  > if it did well in all those past events, we assume that regimes are somewhat persistent
  indicator: regime similarity forecast · asset: multi · horizon: months · testable: yes - walk-forward test · confidence: medium
  ^MT045-C13-2

### C14
- **Katy Kaminski** Rule-based regime definitions overfit history, so tests must be walk-forward and account for how many variables were tried.  #mech/research_method
  > you come up with all these huge parameter space of decisions you're very likely to fit history
  asset: multi · testable: yes · confidence: high
  ^MT045-C14-1
- **Katy Kaminski** Trend likely connects to recessionary regimes (e.g. inverted curve in fixed income), which the non-parametric method could test.  #mech/cycle_persistence
  > I'm pretty certain um you're going to see some regime connection between trend um and certain sort of more recessionary regimes
  asset: multi · horizon: years · testable: yes - proposed · confidence: medium
  ^MT045-C14-2
- **Niels Kaastrup-Larsen** Replicators outperformed their benchmarks in 2025, implying either large tracking error or a separate alpha strategy.  #mech/research_method _(time-bound view)_
  > replication strategies have done quite a lot better uh than uh the benchmarks they're trying to replicate
  indicator: replicator vs benchmark return · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT045-C14-3
- **Katy Kaminski** Kaminski characterises the non-parametric regime method as data filtering rather than macro analysis; the only macro element is the choice of the seven state variables, which invites the objection about how many variables were tried.  #mech/new _(added by map cross-check)_
  > I would say that it's not macro in the sense that it's it's basically data filtering
  indicator: similarity of current month to past months in state-variable space · asset: multi-asset · horizon: monthly · conditions: regimes assumed somewhat persistent · testable: yes - walk-forward test of the similarity filter · confidence: medium
  ^MT045-C14-R2

### C15
- **Katy Kaminski** Replicators are smaller in market set and slower, so they reacted less to Liberation Day shock and kept near average CTA returns.  #mech/slow_reaction _(time-bound view)_
  > most of the replicator strategies out there are, you know, a little smaller in asset set. They also, um, are tending to be more slow in terms of, you know, how they move
  asset: multi · horizon: months · testable: yes · confidence: high
  ^MT045-C15-1
- **Katy Kaminski** Replicator tracking error in 2025 is within expected range per the paper's methodology.  #mech/research_method _(time-bound view)_
  > tracking error is kind of within range uh for for what we expect
  indicator: tracking error · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT045-C15-2
- **Katy Kaminski** Regression-based replication is slowest; mechanical or hybrid replication can be faster to track CTA performance.  #mech/research_method
  > regression based is really sort of looking at the past and that is the slowest approach
  indicator: replication method speed · asset: multi · testable: yes · confidence: high
  ^MT045-C15-3

### C16
- **Katy Kaminski** Replicators miss markets outside their set (cocoa), so differences reflect market regimes not luck.  #mech/structural_shift
  > if you were trying to trade Coco two years ago like replication cannot pick that up
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT045-C16-1
- **Katy Kaminski** Tracking error depends on market set and implementation, so investors must understand inputs to measure it.  #mech/research_method
  > you're running an a replicated replication strategy that has no European debt and only trades US, you're going to see variation where you don't capture those European moves
  indicator: tracking error vs market set · asset: rates · testable: yes · confidence: high
  ^MT045-C16-2
- **Katy Kaminski** Replication can be a separate strategy combined with CTAs to reduce dispersion.  #mech/risk_management
  > it's just another strategy that can be combined with other CTAs that might smooth the overall dispersion
  asset: multi · testable: partly · confidence: medium
  ^MT045-C16-3

