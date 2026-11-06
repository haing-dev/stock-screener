---
source_id: MT099
title: "Major Market Moves for Trend Followers - Systematic Investor 308"
date: 2024-08-16
channel: "Top Traders Unplugged"
url: 
words: 11103
claims: 49
added_by_crosscheck: 9
corrections: 2
crosscheck: "opus cross-check"
speakers: ["Niels Kaastrup-Larsen (host)", "Nick Baltas (co-host, quant/trend-following practitioner; caption spells 'Nick Bolas')"]
tags: [source, layer0]
---
# Major Market Moves for Trend Followers - Systematic Investor 308

**Speakers:** Niels Kaastrup-Larsen (host); Nick Baltas (co-host, quant/trend-following practitioner; caption spells 'Nick Bolas')

**Summary:** Aug 2024 Systematic Investor: live debrief of the early-August yen-carry unwind and volatility spike (VIX 16 to 65, Nikkei -12%) for trend followers. Trend index lost about 6% in the month, within normal bounds; discusses speed, risk allocation across asset classes, dynamic sizing, 0DTE options, value-at-risk contagion and correlation externalities. Main conclusion: reversal after a spike is an expected cost of trend following; design choices (speed, balanced vs unconstrained risk, equity caps) explain manager dispersion.

**Approach:** trend following, CTA performance, carry trade unwind, volatility spike, risk allocation, signal speed, value at risk, dispersion between managers

**Cross-check completeness estimate of first read:** 0.87 - first reader was thorough on design choices, speeds and the August 2024 event; missed the pre-shock low-correlation setup, look-back vs shock length, bonds as historical driver, intraday momentum, risk-manager framing and the VaR contagion nuance.

## Argument map

**Episode thesis:** A live debrief of the early-August 2024 yen-carry unwind and volatility spike (VIX 16 to 65 and back to 24 within a week; biggest Nikkei one-day fall since 1987) argues that a sharp spike-and-revert is an expected cost of trend following, not a sign the strategy is broken: the SG Trend index lost about 6% in a month that followed a very strong equity run. Nick Baltas shows that dispersion between managers comes from design choices (signal speed, balanced versus unconstrained risk across asset classes, equity caps, pure trend versus added reversion/carry), so choices should be matched to what the investor needs to defend; both speakers reject the lazy blame of risk parity, vol targeting and CTAs and point instead to correlation externalities and crowded positions.

### Nick Baltas (Co-host; quantitative practitioner running systematic trend-following strategies (dynamic risk allocation))
Fingerprint: #approach/trend_following #approach/position_sizing_vol_target #approach/positioning_crowding #approach/volatility_options #approach/dealer_hedging_flows #approach/regime_detection #approach/research_robustness_overfitting #approach/diversification_risk_parity
_Speaker note: Caption spells 'Nick Bolas'. Turns are separable from the host's by question/answer structure; two ledger claims mixed speakers and are applied below (C07-2 split; C05-3 date corrected to Thanksgiving 2021). Numbers such as the VIX path are quoted from memory in conversation._

**Worldview premises**
- Sharp mean reversion after a spike (March 2023 rates, Feb 2018 VIX spike, Aug 2024) hurts trend followers; the cost is part of the exposure the investor subscribes to, particularly when equity exposure is unconstrained, and it does not show the strategy is broken. _[experience, stated; support: Comparison of three episodes; none of the people he speaks to became concerned about trend following as a theme.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C05-1|C05-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C05-R2|C05-R2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C04-1|C04-1]])
- The August 2024 drawdown was a reversal of an exceptional run: equities to end-July were in the top decile of any year since 1928 and trend indices had been outperforming until just before. _[empirical, stated; support: Return history since 1928 (quoted from his own data).]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C03-1|C03-1]])
- Signal speed should be tied to investor objectives, not to recent price action; clients asked for faster systems on Monday and slower ones two days later as the V shape unfolded. _[behavioural, stated; support: Client conversations in the same week.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C03-2|C03-2]])
- Speed outcomes depend on whether a reversal is a true or false positive: faster systems win if the turn is real and lose the recovery if it is a V; the gap between fast and medium speeds widened on Monday and closed by week end. _[empirical, stated; support: Own strategy statistics for the week.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C10-3|C10-3]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C12-1|C12-1]])
- The medium-term benchmark (SG CTA Trend) behaves like an exponentially weighted signal with about a 3-month half-life, not a 3-month window. _[empirical, stated; support: Own replication plus Quantica research (about a 66-day half-life correlating highly with the index over 10-15 years).]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C10-2|C10-2]])
- Dynamic risk allocation across asset classes lets risk flow to trending classes; forcing equal risk (25% each) versus letting it flow is the design choice that caused most of the dispersion between managers in August 2024. Neither is right or wrong; it is a trade-off between forced diversification and conviction. _[theoretical, stated; support: Own risk-allocation numbers (rates fell to about 10% of risk; equities caused 60% of the loss).]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C08-1|C08-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C08-2|C08-2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C09-1|C09-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C08-R3|C08-R3]])
- Bond futures used to drive trend returns but after 2022 rates stopped trending, so the book's returns now come from equities, JPY and commodities. _[empirical, stated; support: Own attribution for 2024 year to date.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C08-X1|C08-X1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C06-3|C06-3]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C07-1|C07-1]])
- Assessing strategies should focus on turning points and rotations and on capital preservation, since one must remain solvent through a drawdown to reach new highs. _[theoretical, stated; support: Argument by survivorship ('otherwise it is paper money').]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C11-1|C11-1]])
- Added reversion or carry components can help in such months (his reversion signal went long Japan quickly after the loss), which makes many managers no longer pure trend. _[experience, stated; support: His own book; the host raises the 'not pure trend' point first.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C11-2|C11-2]])
- Equity dispersion trades and vol selling lost because correlations spiked from record lows driven by concentration in a few AI/mega-cap names; skew and implied levels then offered re-entry. _[empirical, stated; support: Market observations over the week.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C04-X1|C04-X1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C04-3|C04-3]])
- Value at risk is only a threshold; use expected shortfall for losses beyond it, and VaR is bounded by historical realisations. Contagion arises from many investors suffering losses at once and unwinding together, not from the measure itself. _[theoretical, stated; support: Standard risk-management theory (parametric, Monte Carlo and historical variants).]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C15-1|C15-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C15-X1|C15-X1]])
- Good risk management should foresee correlation spikes and the externalities of many investors holding similar portfolios and reacting to the same signals (FX carry is the example); VaR cannot capture this. _[theoretical, stated; support: Example of crowded FX carry; historical correlations understate the problem.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C15-2|C15-2]])
- Funding liquidity constraints (inability to lever up) can turn one or two big moves into a vicious circle. _[theoretical, stated; support: None beyond statement.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C16-1|C16-1]])
- Blaming systematic rule-followers (risk parity, vol targeting, CTAs) for each drawdown is overplayed, since discretionary managers would also cut losses; the sell-off was multi-dimensional (carry, correlation, liquidity). _[experience, stated; support: Argument by analogy (a discretionary holder of the Magnificent 7 would also cut); no agent-level data, and he asks for a postmortem when data allow.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C14-2|C14-2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C16-2|C16-2]])
- 0DTE option selling lost money but is no different from selling longer tenors; hedging a zero-day option is harder as delta and gamma change quickly, and dealer long/short gamma can amplify or dampen moves, but there is no data that 0DTE drove the event. _[theoretical, stated; support: Option theory; he disclaims having studied the market closely.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C13-3|C13-3]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C14-1|C14-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C14-X1|C14-X1]])

**Chain: August 2024 yen-carry unwind to trend-follower losses**
1. BOJ hike and Fed cut expectations → Dollar/yen less attractive; FX carry unwinds with losses: Narrower rate differential removes the carry reward. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C04-2|C04-2]])
2. Record-low equity correlations from mega-cap concentration, plus crowded short-vol and dispersion trades → Correlation spike and a VIX jump from 16 to 65: Correlation and dispersion short positions were exposed to a sudden move. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C04-X1|C04-X1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C04-3|C04-3]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C04-1|C04-1]])
3. Equity market falls (Nikkei biggest daily loss since 1987) → Trend portfolios long equities and short yen lose; equity part contributed 60% of the loss: Positions built in the year-to-date rally and JPY weakness are hit by the reversal. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C02-3|C02-3]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C09-1|C09-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C06-3|C06-3]])
4. BOJ signals it will not hike if it upsets markets (a 'BOJ put') → Rapid rebound; V shape; VIX back to 24 within a week: Central-bank backstop and re-entry at attractive implied levels. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C02-3|C02-3]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C04-1|C04-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C04-3|C04-3]])
5. Sharp spike then reversal → Trend losses for the month (about 6% for SG Trend), mostly reversing a prior gain: Trend followers lose to a spike-and-revert; the loss is an expected feature. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C05-1|C05-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C03-1|C03-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C02-2|C02-2]])
- Evidence: Index numbers as of 14 Aug 2024 (BTOP50 -3.6%, SG CTA -4.45%, SG Trend -5.98%, SG Short-Term Traders -0.72% month to date; S&P 500 +12.4% year to date); VIX path; own risk-allocation data.
- Fails when: A loss of this kind turns into a deeper drawdown only if the turn is a true positive rather than a V; faster systems do better in that case.

**Chain: Why managers' August outcomes diverged**
1. Rates stopped trending (dynamic risk allocation), commodities and equities trended → Dynamic allocators had only about 10% of risk in rates versus 25% under balanced allocation: Risk follows trendiness at the asset-class level. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C08-1|C08-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C07-1|C07-1]])
2. More risk in equities (unconstrained, medium speed) → Larger August loss than balanced or equity-defensive designs: Equities caused 60% of the loss; a balanced allocation loses less but captured less of the earlier rally. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C09-1|C09-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C12-3|C12-3]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C12-R1|C12-R1]])
3. Equity-defensive designs with no long equities → Roughly 0% month to date: They do not hold the exposure that was hit. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C13-1|C13-1]])
4. Number of markets and non-trend features (reversion, carry) → Further dispersion: Few-market books are hit-or-miss on Nikkei/yen; mean-reversion components helped. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C07-3|C07-3]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C11-2|C11-2]])
- Evidence: Own numbers for the week and the March 2023 comparison; dispersion observed across managers.
- Fails when: In March 2023 the shock was in rates and hit all trend programs similarly regardless of speed or equity caps, so the same design choices would not have separated managers.

**Chain: Signal speed after a V-shaped shock**
1. Shock hits on Monday → Faster systems cut exposure and lose less on Monday: Short half-life signals adapt immediately. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C10-3|C10-3]])
2. Prices rebound through the week → Faster systems miss the recovery; medium-term signals regain part of their Monday loss: Medium signals keep exposure; the gap closes by week end. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C10-3|C10-3]])
3. No established trend in rates and commodities → Shorter speeds do substantially better there; in equities, credit and FX speed made little difference: Whipsawed markets reward quick response. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C12-1|C12-1]])
- Evidence: Own signal comparisons for the month of August 2024.
- Fails when: Not stated; he notes that the answer reverses if the shock was a true positive.

**Chain: Correlation externalities and contagion**
1. Many investors hold similar portfolios (FX carry) for similar objectives → Realised correlations low in history but high when all react to the same global growth shock: Unrecognised crowding; the externality is invisible in the back test. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C15-2|C15-2]])
2. Funding constraints and losses at the same time → Synchronous unwinding and a vicious circle after one or two big moves: Investors cannot lever up and must cut together. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C16-1|C16-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C15-X1|C15-X1]])
3. Crisis → Back-tested diversification overstates protection: Correlations rise in a crisis. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C15-3|C15-3]])
- Evidence: Illustration with the FX carry trade and the August episode; no statistical test.
- Fails when: Not stated.

**Chain: Option-market amplification (0DTE and gamma)**
1. Short-dated options held by dealers or traders → Delta and gamma change quickly intraday, making hedging harder: Expiry within hours. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C14-1|C14-1]])
2. Dealers short or long gamma → Moves amplified if short gamma, contained if long gamma: Hedge flows follow the direction of the move or oppose it. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C14-1|C14-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C14-X1|C14-X1]])
- Evidence: Theory only; he says there are no data showing that 0DTE drove the event, and long-gamma holders profited as expected.
- Fails when: Not stated; he disclaims the effect pending data.

**Decision process**
- [sizing] Vol scale every exposure and allocate risk dynamically between asset classes (e.g. rates fell to about 10% when not trending) instead of forcing 25% each across equities, rates, FX and commodities.. Why: Concentrates risk where trends exist; he personally prefers dynamic vol scaling and dynamic allocation but acknowledges the defensive benefit of a balanced allocation. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C08-1|C08-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C08-2|C08-2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C08-R3|C08-R3]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C09-1|C09-1]])
- [signal] Medium-term trend signal of roughly a 3-month exponential half-life, with a combination of speeds; may add mean-reversion and carry components.. Why: Matches the benchmark and adds diversification; reversion helped in August by going long Japan quickly. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C10-2|C10-2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C11-2|C11-2]])
- [portfolio] Match speed, equity caps and class balance to what the investor needs to defend (e.g. 60/40 risk in equities and rates).. Why: Equity-defensive designs were about 0% while unconstrained medium-term designs lost in August; different objectives need different treatment. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C13-1|C13-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C03-2|C03-2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C12-3|C12-3]])
- [risk] Use expected shortfall, not only VaR, and monitor correlation dynamics and crowding externalities.. Why: VaR is a threshold bounded by history and cannot see crowded-position correlation spikes. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C15-1|C15-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C15-2|C15-2]])
- [research] Assess strategies on turning points and rotations and wait for data before blaming risk parity, vol targeting or CTAs or 0DTE.. Why: Solvency in drawdown matters; the sell-off was multi-dimensional. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C11-1|C11-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C14-2|C14-2]])
- [execution] Strategies following intraday moves from the open in Nikkei on 5 August would have profited from strong intraday momentum.. Why: Intraday momentum on the crash day. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C14-X1|C14-X1]])

**Evidence style:** Data from his own strategies and indices over a short window (one week to one month), compared with March 2023 and Feb 2018; theory (VaR, option gamma) and practitioner reasoning. He is open that conclusions rest on a few episodes and wants a postmortem with agent-level data.

**Views at the time**
- (2024-08-16 (Friday; index data as of 14 Aug)) The August episode was a learning week and an opportunity, not an alarm for trend following; the sell-off reversed within days.. Reasoning: Spike-and-revert is a known cost; VIX back at 24 and S&P recovering. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C05-1|C05-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C04-1|C04-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C03-1|C03-1]])
- (2024-08-16) Trend portfolios have flipped to long bonds across regions and tenors since June after a long range-bound period; commodities reversed in July (energy flipped) while precious metals longs held; equities and JPY positions depend on speed.. Reasoning: Signal transitions with speed and smoothing. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C06-1|C06-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C06-2|C06-2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C07-1|C07-1]])
- (2024-08-16) S&P skew moved from historic lows to its most attractive level in years, so there are re-entry opportunities in implied levels.. Reasoning: Repriced skew after the correlation spike. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C04-3|C04-3]])
- (2024-08) Alternative (non-benchmark) commodity trends added performance almost daily in August 2024, showing the value of diversification insulated from macro moves.. Reasoning: Insulation from equity and yen moves. (Corrected from the host to Baltas.) ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C07-2|C07-2]])

### Niels Kaastrup-Larsen (Host of Top Traders Unplugged; veteran trend follower and CTA)
Fingerprint: #approach/trend_following #approach/manager_selection_allocation #approach/crisis_alpha_convexity #approach/policy_reaction_central_banks #approach/position_sizing_vol_target #approach/research_robustness_overfitting
_Speaker note: Caption spells 'Neils Castro Larson'. He frames topics and states views of his own on trend following, speed and risk management, so he is mapped. The 'Thanksgiving 20121' caption is read as Thanksgiving 2021 (applied correction)._

**Worldview premises**
- Trend followers are rule-followers: a crash day is an ordinary day with no frantic activity, and the loss of one week is smaller than the gain of some single weeks earlier in the year. Trend came back quickly after the extreme one-day event around Thanksgiving 2021. _[experience, stated; support: Personal trading experience.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C05-2|C05-2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C05-3|C05-3]])
- A BOJ put exists: the BOJ said it would not hike if it upsets markets, which enabled the rebound after a small, telegraphed hike and weak US jobs triggered the biggest Nikkei fall since 1987. _[institutional, stated; support: Events of the week.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C02-3|C02-3]])
- A few-day shock is too short relative to medium and long look-back windows to flip equity or yen positions; it mainly deleverages and weakens signal strength, so trend books change little after brief crashes. _[theoretical, stated; support: Reasoning from look-back lengths.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C07-X1|C07-X1]])
- Fully diversified trend portfolios have components (such as strengthening grain downtrends) that cushioned July and August and are missed by equity and yen headlines; dispersion between managers depends on the number of markets traded. _[experience, stated; support: Observation of the month.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C07-2|C07-2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C07-3|C07-3]])
- Short-term trend following works less well than medium to long-term; the index data show SG Trend usually beats the short-term traders index. Short-term managers exit by time- or vol-based rules, so they are a different methodology, not just a shorter time frame. _[experience, stated; support: Index data, no study; he says he has never seen data that short-term trend works as well.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C09-2|C09-2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C10-1|C10-1]])
- Look-backs are not symmetrical for entry and exit: a slow entry does not mean a slow exit, so managers can design faster reaction into medium-term systems, which is a source of edge and uniqueness. _[experience, stated; support: Practitioner view.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C10-4|C10-4]])
- Many CTAs are no longer pure trend, which explains performance divergences, and it is hard for an investor to understand differences between managers; replicator products led the benchmark into July 2024 and the gap vanished in six weeks. _[empirical, stated; support: Observation of replicator versus benchmark performance.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C11-2|C11-2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C13-2|C13-2]])
- Trend followers are first risk managers: they control the risk taken, not the returns the market offers. Many have moved from stop losses with static sizing to VaR-based portfolio risk, which raises the worry that common VaR use synchronises selling. _[experience, stated; support: Personal view; asked of Baltas as an open question.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C14-X2|C14-X2]])
- Correlations rise in a crisis, so back-tested diversification overstates protection. _[empirical, stated; support: 'The only thing that goes up in a crisis is correlations'.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C15-3|C15-3]])
- Long calm streaks precede volatility spikes: the S&P streak without a 2% drawdown was about 356 days before Volmageddon (Feb 2018) and 351 days before August 2024 (offered half in jest). _[empirical, stated; support: Two data points.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C12-2|C12-2]])
- The short-horizon trend barometer stood at 52 during the August reversal because short time frames adapt quickly, while longer trend indices were down. _[empirical, stated; support: His own barometer.]_ ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C02-1|C02-1]])

**Chain: Why brief crashes barely change trend portfolios**
1. A shock lasting only a few days → Too short relative to medium/long look-backs to flip equity or yen positions: Signals average over months. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C07-X1|C07-X1]])
2. Positions largely intact → Deleveraging and weaker signal strength rather than reversal; continuation afterwards: Volatility scaling cuts size while direction stays. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C07-X1|C07-X1]])
- Evidence: General reasoning; no position data for the week.
- Fails when: Faster systems do flip, and the longer a shock lasts the more signals turn.

**Decision process**
- [risk] Run by rules, treat a crash day as an ordinary day, and see the trend follower first as a risk manager.. Why: Control of risk, not returns, is the part trend followers can influence. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C05-2|C05-2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C14-X2|C14-X2]])
- [signal] Prefer medium- to long-term trend over short-term trend; short-term managers use time- or vol-based exits.. Why: Index evidence that SG Trend usually beats the short-term traders index. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C09-2|C09-2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C10-1|C10-1]])
- [universe] Trade many markets including less conventional commodities.. Why: Few-market books are hit-or-miss; diversification cushioned July and August. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C07-2|C07-2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C07-3|C07-3]])
- [other] Expect equity-exit rules or market-neutral add-ons to differ by manager; manager look-back design (fast exit, slow entry) is a source of edge.. Why: Symmetry of look-backs cannot be assumed. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C10-4|C10-4]])

**Evidence style:** Personal experience, index data and anecdote from the week; rules of thumb (the 351/356-day streak) offered with humour. He explicitly says he has never seen data on short-term trend and relies on SG index comparisons.

**Views at the time**
- (2024-08-16) The week was not a big event for trend followers and the community handled it well; August losses are a normal part of the year.. Reasoning: Rules-based reaction; a big carry trade was shaken, and earlier single weeks gained more. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C05-2|C05-2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C02-2|C02-2]])
- (2024-08-16) Central banks now vocalise a put (the BOJ), which markets took as good news.. Reasoning: BOJ said it would not hike if it upsets markets. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C02-3|C02-3]])
- (2024-08-16) The endogenous size of the carry trade was probably bigger than people realised, with correlation and crowding effects.. Reasoning: Offered as a closing comment after Baltas on externalities. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C15-3|C15-3]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C14-X2|C14-X2]])

### Disagreements
- **Speed: short-term versus medium/long-term trend**: Niels Kaastrup-Larsen: Short-term trend following does not work as well as medium to long term (SG Trend usually beats short-term traders); short-term managers are a different methodology. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C09-2|C09-2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C10-1|C10-1]]); Nick Baltas: Neither speed is better in general: it depends on whether the reversal is a true or false positive, speed mattered mainly in rates and commodities, and speed should reflect investor objectives. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C10-3|C10-3]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C12-1|C12-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C03-2|C03-2]])
- **Did the shock flip trend positions?**: Niels Kaastrup-Larsen: A few-day shock is too short to flip equity or yen positions in medium/long systems; mostly deleveraging and weaker signals. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C07-X1|C07-X1]]); Nick Baltas: Depending on speed, a fraction or most markets turned; equities are a big transition, though he accepts equities may not have flipped for most medium-term programs. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C06-1|C06-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C10-3|C10-3]])
- **Does common VaR use create contagion?**: Niels Kaastrup-Larsen: Worries that many managers moving from stop losses to VaR-based risk could synchronise forced selling. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C14-X2|C14-X2]]); Nick Baltas: Contagion comes from simultaneous losses and synchronous unwinding, not from the VaR measure; the real issue is whether it is the right measure and whether people over- or under-react, and crowded positions matter more. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C15-1|C15-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C15-X1|C15-X1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C15-2|C15-2]])
- **Balanced versus dynamic asset-class risk allocation**: Nick Baltas: A balanced allocation would have lost less in August (equities 60% of the loss) but gives up conviction in trending classes; he personally likes dynamic allocation but calls it a design trade-off. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C09-1|C09-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C08-2|C08-2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C08-R3|C08-R3]]); Niels Kaastrup-Larsen: Asks about dynamic versus static sizing for investor perception of risk, and notes managers hold firm beliefs in one or the other; states no preference. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C14-X2|C14-X2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C10-4|C10-4]])

### Gaps and conflicts
- Most statements rest on one week and a few comparable episodes (Mar 2023, Feb 2018); there is no systematic study and conclusions on speed and balanced allocation are a posteriori. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C12-3|C12-3]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C10-3|C10-3]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C09-1|C09-1]])
- Baltas says the risk-allocation point is a hypothesis since he has not looked at long-term data. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C08-1|C08-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C08-2|C08-2]])
- No data support or refute that 0DTE options or risk-parity/vol-target/CTA selling drove the move; both speakers call for a postmortem when agent-level data exist. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C14-1|C14-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C14-2|C14-2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C16-2|C16-2]])
- The 351/356-day calm streak rule of thumb is based on two episodes and offered as a half-joke. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C12-2|C12-2]])
- Host claims short-term trend works less well but says he has never seen data; the support is the index comparison for one month and the year. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C09-2|C09-2]])
- Ledger attribution fixes: C07-2 mixes speakers (grains is Niels; non-benchmark commodities is Baltas) and C05-3 should read Thanksgiving 2021. Index numbers quoted are as of 14 August, before final month-end values. ([[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C07-2|C07-2]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C05-3|C05-3]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C02-2|C02-2]])

### Forward-looking inputs (reader synthesis)
(reader) Observable inputs the speakers treat as leading or diagnostic: VIX level and the spike-and-revert profile; BOJ and Fed policy gaps that drive yen carry; equity correlation and concentration (record-low correlations preceded the shock); S&P skew and implied correlation as re-entry signals; length of the calm streak without a 2% drawdown; trendiness by asset class (rates versus equities and commodities) which drives dynamic risk allocation; funding liquidity and crowded positions. Horizon is days to weeks for the shock and months for speed effects.

### Reader inferences (not stated by the speakers)
- (reader) The structure of the argument implies that whether faster or slower systems are better cannot be known ex ante; the choice is a payoff-shape decision tied to the investor's liabilities rather than a forecast.
- (reader) The record-low correlation plus concentration setup suggests a testable relation: shock severity for short-correlation and dispersion trades rises when index correlation is at a low and top-name concentration is high.
- (reader) Baltas's rates-risk-at-10% remark implies a dynamic-allocation book was structurally short on diversification into a rates shock like March 2023, which a balanced allocation would not have been; the two episodes are mirror images.
- (reader) The two speakers agree that the crowded FX carry trade was the main amplifier but neither offers a measure of crowding; positioning data (CFTC yen shorts) would be a candidate input.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro boilerplate and small talk (Olympics) |
| C02 | 3 | performance snapshot of indices (Aug 2024); trigger of event: weak US jobs, BOJ hike, Nikkei -12%, BOJ put |
| C03 | 2 | structuring the discussion; Monday emotions vs v-shape, 2024 equity strength, matching design choices to investor objectives |
| C04 | 3 | VIX 16 to 65, carry unwind, dispersion trades and vol selling losses, skew repricing; Crisis alpha in short supply |
| C05 | 3 | trend followers underperformed in sharp reversion; no alarm; Monday was a normal day, rules-based |
| C06 | 3 | exposure shifts over summer by sector: bonds flipped long, FX, commodities reversion, equities |
| C07 | 3 | what drove returns, bonds low-risk then directional; diversification and number of markets; non-traditional commodities |
| C08 | 2 | risk allocation in rates down to 10%; vol scaling vs asset-class balance |
| C09 | 2 | balanced asset-class risk vs unconstrained trend; speed short-term vs trend |
| C10 | 4 | short-term manager vs short-term trend follower; half-life of SG CTA Trend; true vs false positive Monday |
| C11 | 2 | asymmetric look-backs, solvency in drawdowns, impure trend with reversion |
| C12 | 3 | speed matters for rates and commodities; Volmageddon 356-day streak; March 2023 comparison |
| C13 | 3 | equity vs duration shock dispersion; defending 60/40; replicators vs benchmark; 0DTE options |
| C14 | 2 | 0DTE hedging, long vol did well, risk parity attribution skepticism; risk management and VaR question |
| C15 | 3 | VaR vs expected shortfall; parametric vs Monte Carlo; correlation dynamics and externalities |
| C16 | 2 | funding liquidity, overplayed systematic-selling narrative, headlines, outro |

## Claims

### C02
- **Niels Kaastrup-Larsen** A short-horizon trend barometer stood at 52 (fairly high) in the August 2024 reversal because short time frames adapt quickly, while longer trend indices were down.  #mech/slow_reaction _(time-bound view)_
  > my own Trend barometer uh probably to some people surprise is uh is is is fairly High 52 uh but people have to remember that it uses shorter term uh time frames
  indicator: Niels' trend barometer · asset: multi · horizon: weeks · conditions: short time frames benefited in range/fast reversal · testable: yes: barometer vs speed · confidence: medium
  ^MT099-C02-1
- **Niels Kaastrup-Larsen** As of 14 Aug 2024 CTA indices were down 3.6% (BTOP50), 4.45% (SG CTA), 5.98% (SG Trend) and 0.72% (SG Short-Term Traders) for the month, roughly flat for the year, while MSCI World was +8.2% and S&P 500 +12.4% YTD.  #mech/new _(time-bound view)_
  > beta 50 is down 3.6% for the month uh still up 1.55 for the year stock gen c Index is down 4.45% for the month
  indicator: BTOP50, SG CTA, SG Trend, SG Short-Term Traders, MSCI World, S&P 500 · asset: multi · horizon: months · testable: yes: public indices · confidence: high
  ^MT099-C02-2
- **Niels Kaastrup-Larsen** The BOJ stated publicly it would not hike if it upsets markets, effectively a BOJ put that enabled the rebound, after a small BOJ hike and weak US jobs triggered the biggest Nikkei daily loss since 1987.  #mech/policy_reaction _(time-bound view)_
  > the central bank is not going to change rates if it upsets the market so this is if anything
  indicator: BOJ policy, Nikkei, yen · asset: fx · horizon: days · conditions: August 2024 · testable: partly: central bank put events · confidence: medium
  ^MT099-C02-3

### C03
- **Nick Baltas** 2024 equities to end-July were in the top decile of any year since 1928, so the August drawdown was a reversal of an exceptional run, and trend indices had been outperforming until just before.  #mech/cycle_persistence _(time-bound view)_
  > 2024 as an equity market up until the end of July is almost at the top deile of any year since 1928
  indicator: US equity annual return rank since 1928 · asset: equities · horizon: months · testable: yes · confidence: medium
  ^MT099-C03-1
- **Nick Baltas** Investors flip between wanting faster or slower systems within days as the V-shaped dynamics unfold, so system speed should be tied to investor objectives rather than recent price action.  #mech/behavioral _(time-bound view)_
  > I was kind of having conversation with clients that they would be more like oh we should have like a faster system and then two days later they're like actually it's okay
  indicator: signal speed · asset: multi · horizon: days · conditions: V-shaped reversals whipsaw fast systems · testable: partly · confidence: medium
  ^MT099-C03-2

### C04
- **Nick Baltas** VIX spiked from 16 to 65 intraday on 5 Aug 2024 and fell back to 24 within a week, a spike-and-revert profile unfavorable to trend following.  #mech/overshoot _(time-bound view)_
  > we saw vix from 16% end of July spiking to 65% int on Monday which is a level we haven't seen since covid and it's now down to 24
  indicator: VIX · asset: equities · horizon: days · testable: yes: VIX history · confidence: high
  ^MT099-C04-1
- **Nick Baltas** The BOJ hike plus Fed cut expectations made dollar/yen less attractive and unwound the FX carry trade, causing carry losses.  #mech/crowding_positioning _(time-bound view)_
  > the famous FX Cur start unwinding so some carry losses were incurred by those rotations
  indicator: USD/JPY carry trade · asset: fx · direction: short JPY unwound · horizon: weeks · testable: partly: carry unwind episodes · confidence: medium
  ^MT099-C04-2
- **Nick Baltas** Equity dispersion trades and vol-selling lost money as correlations spiked; S&P skew moved from historic lows to its most attractive level in years, offering re-entry opportunities.  #mech/crowding_positioning _(time-bound view)_
  > dispersion trades lost money some volatility selling trades did lose money the skew in S&P over know um got repriced
  indicator: implied correlation, S&P skew, dispersion · asset: equities · horizon: weeks · conditions: after concentration in mega-cap AI/tech · testable: partly · confidence: medium
  ^MT099-C04-3
- **Nick Baltas** Just before the August 2024 shock US equity correlations were at record lows because returns were concentrated in a few mega-cap AI/tech names; such a low-correlation, high-concentration setup left dispersion and short-correlation trades exposed to a sudden correlation spike.  #mech/crowding_positioning _(added by opus cross-check, time-bound view)_
  > we're talking about the least correlated environment in the US market in equities which was the consequence of high level of concentration
  indicator: US equity implied/realized correlation; index concentration · asset: equities · direction: correlation up sharply from record lows; dispersion trades lose · horizon: weeks · conditions: high index concentration, crowded dispersion trades · testable: yes - implied correlation index levels before shocks · confidence: medium
  ^MT099-C04-X1

### C05
- **Nick Baltas** Trend followers are hurt by sharp mean reversion after a spike (as in March 2023, Feb 2018 VIX spike, Aug 2024); this cost is part of the exposure and not a sign the strategy is broken.  #mech/slow_reaction _(time-bound view)_
  > a massive reversion following a spike this was not the environment during March 2023
  indicator: trend-following drawdowns after spikes · asset: multi · horizon: weeks · conditions: sharp reversals · testable: yes: trend returns after vol spikes · confidence: high
  ^MT099-C05-1
- **Niels Kaastrup-Larsen** Trend followers operate by rules and treat a crash day as an ordinary day, unlike discretionary or other strategies that see frantic activity; trend gains of one early-year week exceed the loss of the August week.  #mech/risk_management _(time-bound view)_
  > Monday was a day like any other day there was nothing unusual from a trend falling perspective
  asset: multi · horizon: days · testable: no · confidence: high
  ^MT099-C05-2
- **Niels Kaastrup-Larsen** After the extreme one-day event of Thanksgiving 2020 trend strategies recovered quickly, showing one-day shocks need not damage trend returns.  #mech/cycle_persistence
  > the strategies came roaring back uh actually almost beginning on that day
  indicator: trend index after one-day shocks · asset: multi · horizon: weeks · testable: yes: event study · confidence: low
  **Correction (cross-check):** Wrong year: the caption says 'Thanksgiving 20121', i.e. late November 2021 (the Omicron Black Friday sell-off), not Thanksgiving 2020. → After the extreme one-day event around Thanksgiving 2021 trend strategies recovered quickly, showing one-day shocks need not damage trend returns.
  ^MT099-C05-3
- **Nick Baltas** In the week after the shock, no one among the practitioners Baltas speaks to became concerned about trend following itself; the underperformance was seen as part of what the strategy is.  #mech/new _(added by map cross-check, time-bound view)_
  > by no measure did we see anyone becoming concerned about Trend following as a um as a systematic theme
  indicator: investor sentiment toward trend following · asset: multi · horizon: weeks · conditions: After the August 2024 reversal; unconstrained equity exposure · testable: no · confidence: medium
  ^MT099-C05-R2

### C06
- **Nick Baltas** Trend portfolios flipped from balanced to long across bond markets and tenors between June and early August 2024 after long range-bound markets.  #mech/slow_reaction _(time-bound view)_
  > the vast majority of markets across uh regions and Tenors are long so we long Bor Futures
  indicator: bond futures net trend position · asset: rates · direction: long bonds · horizon: months · testable: yes: CTA positioning · confidence: medium
  ^MT099-C06-1
- **Nick Baltas** Commodities rallied early 2024 then reversed sharply in July (BCOM -4.5%, GSCI -4%), flipping energy positions, while precious metals longs held.  #mech/slow_reaction _(time-bound view)_
  > July was a massive reversion I think bom was down by 4 and a half% GCI was down by 4%
  indicator: BCOM, GSCI · asset: commodities · horizon: months · conditions: July 2024 · testable: yes · confidence: medium
  ^MT099-C06-2
- **Nick Baltas** In 2024 YTD trend returns came from three components: the equity rally, JPY weakening and rising commodity prices, with an uninteresting bond market.  #mech/slow_reaction _(time-bound view)_
  > what has been driving returns here to date the equity rally the weakening of JPY and maybe some Rising commodity
  indicator: equities, JPY, commodities, bonds · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT099-C06-3

### C07
- **Nick Baltas** Under dynamic risk allocation, bonds received less and less risk in 2024 because they were not trending, then regained direction in August.  #mech/risk_management _(time-bound view)_
  > bonds started representing lower and lower and lower risk over the year just because there was no
  indicator: bond trendiness / risk allocation · asset: rates · horizon: months · conditions: dynamic allocation · testable: yes · confidence: medium
  ^MT099-C07-1
- **Niels Kaastrup-Larsen** Diversified portfolios were cushioned by grain downtrends and non-traditional commodity trends during July/August, which headlines focused on equities and yen missed.  #mech/risk_management _(time-bound view)_
  > the downtrends in some of the Commodities like uh grains um actually um got a
  indicator: grains and alternative commodities · asset: commodities · horizon: weeks · conditions: diversified portfolios · testable: yes · confidence: medium
  **Correction (cross-check):** Mixes speakers: Niels makes the grain-downtrend point; the observation that non-traditional, non-benchmark commodities gained almost every day in August is Nick Baltas's. → Niels: strengthening grain downtrends cushioned diversified trend portfolios in July; Nick: alternative non-benchmark commodities added performance almost daily in August 2024, showing the value of diversification insulated from macro moves.
  ^MT099-C07-2
- **Niels Kaastrup-Larsen** Return dispersion between managers depends on the number of markets traded: managers with few markets are hit and miss on Nikkei/yen exposure.  #mech/research_method
  > return dispersion we're going to be seeing between managers certainly also relates to uh the number of markets you trade
  indicator: number of markets traded · asset: multi · testable: yes · confidence: medium
  ^MT099-C07-3
- **Niels Kaastrup-Larsen** A few-day shock is too short relative to medium/long trend look-back windows to flip equity or yen positions; it mainly causes deleveraging and weaker signal strength while most positions continue, so trend portfolios change little after brief crashes.  #mech/risk_management _(added by opus cross-check, time-bound view)_
  > I don't think it's changed Direction frankly from because the move is relatively short in time only for only for Windows exactly
  indicator: trend signal look-back length vs shock duration · asset: multi · direction: long equities reduced, not reversed · horizon: days · conditions: short sharp shock followed by rebound · testable: yes - simulate signal changes through short shocks · confidence: medium
  ^MT099-C07-X1

### C08
- **Nick Baltas** With dynamic vol scaling, risk allocation fell to about 10% in rates (from 25% across equities, rates, FX, commodities) because rates did not trend while equities and commodities trended.  #mech/risk_management _(time-bound view)_
  > the risk allocation in rates was basically at the minimum we have seen for some time
  indicator: risk share by asset class · asset: multi · horizon: months · conditions: dynamic risk allocation · testable: yes · confidence: high
  ^MT099-C08-1
- **Nick Baltas** Dynamic sizing has two layers: vol scaling per asset, and whether to force equal risk across asset classes (e.g. 25% each) or let risk flow to the trending class; the latter caused most dispersion between managers.  #mech/risk_management
  > the second point and that's the one I have more comments on at least for the recent period is whether even after doing inverse volatility scaling
  indicator: asset-class risk budgeting · asset: multi · testable: yes: simulate fixed vs dynamic class budget · confidence: high
  ^MT099-C08-2
- **Nick Baltas** Bond futures were historically the main driver of trend-following returns, but after 2022 rates stopped trending and contributed little, which changes how a trend book's returns are composed.  #mech/structural_shift _(added by opus cross-check, time-bound view)_
  > historically that was the Big Driver of performance and and and over the last like know a year or [L280] two um it has not been
  indicator: trend P&L attribution by asset class · asset: rates · horizon: years · conditions: range-bound rates after 2022 · testable: yes - sector attribution of SG Trend / trend replication · confidence: medium
  ^MT099-C08-X1
- **Nick Baltas** Baltas personally prefers dynamic vol scaling and dynamic risk allocation across markets and asset classes (stated as a preference, with the allocation question later described as a trade-off).  #mech/new _(added by map cross-check)_
  > I personally like Dynamic Vol scaling and dynamic risk allocation between markets and as class
  indicator: asset-class trendiness · asset: multi · horizon: months · conditions: Trend-following book with four major asset classes · testable: yes: dynamic versus balanced allocation backtest · confidence: high
  ^MT099-C08-R3

### C09
- **Nick Baltas** A balanced asset-class risk allocation would have lost less in August (equities caused 60% of the loss) but would have captured less of the equity trend before; it is a trade-off between forced diversification and conviction in signals.  #mech/risk_management _(time-bound view)_
  > if you end up having equities contributing 60% of the loss by design a more balanced allocation between the forest classes would have F better
  indicator: asset-class allocation · asset: multi · horizon: months · conditions: equity-led drawdown · testable: yes · confidence: medium
  ^MT099-C09-1
- **Niels Kaastrup-Larsen** The host believes short-term trend following works less well than medium to long-term, and index data show SG Trend usually beats the short-term traders index.  #mech/slow_reaction
  > I don't believe that short-term Trend following works as well as um medium to long-term Trend following
  indicator: SG Short-Term Traders Index vs SG Trend · asset: multi · direction: medium/long-term trend preferred · horizon: years · testable: yes: compare speeds over time · confidence: medium
  ^MT099-C09-2

### C10
- **Niels Kaastrup-Larsen** A short-term manager exits by time-based or vol-based rules, not by trend change, so short-term managers are a different methodology from short-term trend followers.  #mech/research_method
  > short-term manager will not get out because the trend changes they'll get out by using a Time based stop
  indicator: time-based stops · asset: multi · horizon: days · testable: partly · confidence: medium
  ^MT099-C10-1
- **Nick Baltas** The SG CTA Trend index behaves like an exponentially weighted signal with about a 3-month half-life; Quantica showed a roughly 66-day half-life signal correlates highly with the index over 10-15 years.  #mech/research_method
  > around a 30mon half lifee on an exponentially weighted moving average basis
  indicator: EWMA trend signal half-life (about 3 months) · asset: multi · horizon: months · testable: yes: replicate the index with EWMA · confidence: medium
  ^MT099-C10-2
- **Nick Baltas** Faster systems helped on Monday but lost out in the recovery because they cut exposure, while medium-term signals lost more at first and recaptured part later; the gap between speeds closed by week-end, so signal speed outcomes depend on whether the reversal is a true or false positive.  #mech/slow_reaction _(time-bound view)_
  > A true positive in other words whether Monday was the start of a massive drw down
  indicator: signal speed · asset: multi · horizon: days · conditions: V-shape vs continued decline · testable: yes · confidence: high
  ^MT099-C10-3
- **Niels Kaastrup-Larsen** Look-backs are not necessarily symmetrical for entry and exit: a slow entry (e.g. three months to build) does not imply slow exits, and managers can design faster reaction in a medium-term system.  #mech/research_method
  > you can't assume that look backs are are symmetrical applied
  indicator: entry vs exit speed · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT099-C10-4

### C11
- **Nick Baltas** Assessing strategies should focus on turning points and market rotations and how they preserve capital because one must survive drawdowns to see new highs.  #mech/risk_management
  > remaining solvent in a drawdown is harder than in an NA move
  indicator: drawdown behavior at rotations · asset: multi · testable: partly · confidence: medium
  ^MT099-C11-1
- **Niels Kaastrup-Larsen** Many CTAs are no longer pure trend, which explains performance divergences; Baltas adds mean-reversion and carry components that helped (e.g. quickly going long Japan after losses).  #mech/research_method
  > many managers and there's nothing wrong with that um is not pure Trend anymore
  indicator: trend plus reversion plus carry blends · asset: multi · horizon: weeks · testable: yes: compare pure trend and blends · confidence: medium
  ^MT099-C11-2

### C12
- **Nick Baltas** In August 2024 speed mattered most in commodities and rates (no established trends), where shorter speeds did substantially better; equities, credit and FX showed little speed difference.  #mech/slow_reaction _(time-bound view)_
  > the two asset classes where you saw some differing Behavior specifically around a very shorter term speed and longer term speed
  indicator: speed in rates and commodities · asset: multi · direction: faster speed in non-trending markets · horizon: weeks · conditions: whipsaw markets · testable: yes · confidence: medium
  ^MT099-C12-1
- **Niels Kaastrup-Larsen** The S&P streak without a 2% drawdown before Volmageddon (Feb 2018) was about 356 days versus 351 days before August 2024; long calm streaks precede vol spikes (rule of thumb offered as a half-joke).  #mech/overshoot _(time-bound view)_
  > if the S&P goes for about 340 days without a 2%
  indicator: days since S&P 2% drawdown · asset: equities · direction: reduce long equities after about 340 calm days · horizon: days · conditions: long streak of low volatility · testable: yes: streak vs forward vol · confidence: low
  ^MT099-C12-2
- **Nick Baltas** In Aug 2024 the equity shock differentiated managers (fast/equity-defensive vs medium-term unconstrained), whereas in March 2023 the rates shock hit all trend programs similarly regardless of speed or equity constraints.  #mech/crowding_positioning _(time-bound view)_
  > equities which is typically the growth risk that becomes the differentiation factor between managers
  indicator: equity exposure caps; two-year Treasury sigma move March 2023 · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT099-C12-3
- **Nick Baltas** March 2023 saw a move of roughly six standard deviations (by his hazy recollection) in the two-year Treasury, unprecedented in decades and the main reason for the large trend reversion that month.  #mech/new _(added by map cross-check, time-bound view)_
  > however many Sigma moves for the two year Point uh in the treasury market it was like about 6
  indicator: 2-year Treasury yield move in sigma · asset: rates · direction: reversion hurt trend · horizon: days · conditions: March 2023 banking stress · testable: yes: compute the sigma move from yield data · confidence: low
  ^MT099-C12-R1

### C13
- **Nick Baltas** Defensive trend designs (no long equities) were around 0% month-to-date, so design choices (equity caps, speed, class balance) should be matched to what the investor needs to defend, e.g. 60/40 equity and rates risk.  #mech/risk_management
  > what are we trying to defend against if it's a 60/40 portfolio
  indicator: equity-defensive vs unconstrained trend · asset: multi · horizon: months · conditions: 60/40 investor · testable: partly · confidence: medium
  ^MT099-C13-1
- **Niels Kaastrup-Larsen** Replicator (trend replication) products outperformed the benchmark leading into July 2024 but the gap vanished in the six weeks after.  #mech/crowding_positioning _(time-bound view)_
  > there was a big dispersion between replicators and The
  indicator: trend replicators vs SG Trend benchmark · asset: multi · horizon: weeks · testable: yes · confidence: low
  ^MT099-C13-2
- **Nick Baltas** Selling 0DTE volatility lost money in the shock but is no different from selling longer tenors; long-vol and long-gamma holders profited and short correlation/dispersion were hit most.  #mech/risk_premium _(time-bound view)_
  > selling volatility in those markets did come at a negative return over the last week
  indicator: 0DTE options, implied correlation · asset: equities · direction: long vol hedges paid · horizon: days · conditions: vol shock · testable: partly · confidence: medium
  ^MT099-C13-3

### C14
- **Nick Baltas** Hedging zero-day options is harder since delta and gamma change quickly intraday, and whether dealers are short or long gamma can amplify or dampen moves; no data show 0DTE drove the event.  #mech/liquidity_flows _(time-bound view)_
  > hedging a zero day option to me appears to be more challenging
  indicator: 0DTE option gamma hedging · asset: equities · horizon: days · conditions: fast intraday moves · testable: partly · confidence: low
  ^MT099-C14-1
- **Nick Baltas** The sell-off was multi-dimensional (carry unwind, correlation spike, liquidity) and blaming risk parity, vol-targeting and CTAs alone is too simple; a postmortem with data on agents is needed.  #mech/liquidity_flows _(time-bound view)_
  > I don't think there was one you know one driver
  asset: multi · horizon: weeks · testable: no · confidence: medium
  ^MT099-C14-2
- **Nick Baltas** On the 5 August 2024 crash day the Nikkei showed strong intraday momentum, so strategies following intraday moves from the open would have profited; the net effect of short-dated option hedging depends on whether dealers are long or short gamma.  #mech/liquidity_flows _(added by opus cross-check, time-bound view)_
  > Niki for instance there was substantial intraday momentum that took place on Monday and had you been exposed to those intraday moves
  indicator: intraday momentum from the open · asset: equities · direction: follow intraday direction from the open · horizon: days · conditions: crash days with dealer short gamma · testable: yes - intraday momentum returns on high-vol days · confidence: medium
  ^MT099-C14-X1
- **Niels Kaastrup-Larsen** Trend followers should see themselves first as risk managers because they control risk taken but not returns the market offers; many managers have moved from stop losses with static sizing to VaR-based portfolio risk models, raising the worry that common VaR use synchronizes selling.  #mech/risk_management _(added by opus cross-check)_
  > first and foremost we're Risk Managers that's the part of the of the equation we have some input on we have no say in terms of what performance we can get from the markets
  indicator: stop-loss/static sizing vs VaR-based sizing · asset: multi · testable: partly - compare drawdown behaviour of static vs VaR-sized trend books · confidence: high
  ^MT099-C14-X2

### C15
- **Nick Baltas** Value at risk is only a threshold; use expected shortfall (conditional VaR) for the loss beyond it, and note that VaR is bounded by historical realizations (parametric or Monte Carlo variants).  #mech/risk_management
  > value at risk is just a point in a return distribution
  indicator: VaR, expected shortfall · asset: multi · testable: yes · confidence: high
  ^MT099-C15-1
- **Nick Baltas** Risk management should foresee correlation spikes and externalities from many investors holding similar portfolios and reacting to the same signals (e.g. FX carry), something VaR cannot capture.  #mech/crowding_positioning
  > I think the way I would look into risk management would be more along the lines of correlation
  indicator: correlation dynamics, crowded positioning · asset: multi · conditions: crowded trades · testable: partly · confidence: medium
  ^MT099-C15-2
- **Niels Kaastrup-Larsen** Correlations rise in a crisis, so back-tested diversification overstates protection.  #mech/risk_management
  > the only thing that goes up in a crisis Nick that's correlations
  indicator: cross-asset correlation · asset: multi · conditions: crisis periods · testable: yes · confidence: high
  ^MT099-C15-3
- **Nick Baltas** Contagion from risk models comes from many investors suffering losses at the same moment and unwinding together, not from the choice of VaR as such; the real question is whether the measure is right and whether people over- or under-react to it.  #mech/crowding_positioning _(added by opus cross-check)_
  > if people follow similar rules this cannot in itself have a I guess a contagion effect except the possibility that losses happen at the same time
  indicator: VaR / expected shortfall usage across investors · asset: multi · horizon: days · conditions: synchronized losses across similar portfolios · testable: partly - flow data around risk-limit breaches · confidence: medium
  ^MT099-C15-X1

### C16
- **Nick Baltas** When investors cannot lever up (funding liquidity constraint), one or two large moves can produce a vicious circle.  #mech/liquidity_flows
  > funding liquidity is is is is one of those catalysts right to to the extent you cannot level up anymore
  indicator: funding liquidity · asset: multi · horizon: days · conditions: constrained leverage · testable: partly · confidence: medium
  ^MT099-C16-1
- **Nick Baltas** Blaming systematic rule-followers (risk parity, vol targeting, CTAs) for each drawdown is overplayed since discretionary managers would also cut losses.  #mech/crowding_positioning _(time-bound view)_
  > I cannot see how differently a discretionary manager would act if they hold the Magnificent 7
  asset: equities · horizon: days · testable: no · confidence: medium
  ^MT099-C16-2

