---
source_id: MT222
title: "Why Trend Following Works - Systematic Investor - Ep.391"
date: 2026-03-15
channel: "Top Traders Unplugged"
url: 
words: 10347
claims: 42
added_by_crosscheck: 10
corrections: 0
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Niels Kaastrup-Larsen (host)", "Rich Brennan (trend follower, Dunn, author The Fractals of Finance)"]
tags: [source, layer0]
---
# Why Trend Following Works - Systematic Investor - Ep.391

**Speakers:** Niels Kaastrup-Larsen (host); Rich Brennan (trend follower, Dunn, author The Fractals of Finance)

**Summary:** Systematic Investor episode where Brennan presents empirical research from 68 futures markets since 1984: Hurst exponent 0.866, fat tails (tail exponent 3.33, five-sigma 5,791x too frequent) and volatility clustering (0.353) as evidence of structural feedback; applies it to the March 2026 crude oil spike. Conclusions: bell-curve risk and fixed vol targeting understate risk and trend following is structurally supported.

**Approach:** trend following, fat tails, volatility clustering, oil shock, agent-based model

**Cross-check completeness estimate of first read:** 0.85 - the first reader captured nearly every number and argument from Brennan's Hurst, tail and clustering research and the oil case study; it missed some secondary points (political management of energy prices, the stock-bond co-fall in March, Dunn's daily risk target, the two ways to harvest volatility expansion, trend followers' own role in the feedback loop).

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro; oil 66 to 119 spike setup |
| C02 | 3 | dry undergrowth, positioning, inflation analogy |
| C03 | 3 | patience of models, hormuz barrels trapped |
| C04 | 3 | oil transmission to inflation, SocGen indices |
| C05 | 2 | short vs long-term indices; trend barometer; March performance |
| C06 | 4 | March moves, trend regime, pod shops; research design |
| C07 | 2 | memoryless logic test, Hurst exponent 0.866 |
| C08 | 1 | autocorrelation clarification, magnitude memory |
| C09 | 3 | fat tails, volatility clustering, convergent/divergent participants |
| C10 | 1 | divergent participants, dynamic position sizing |
| C11 | 2 | vol targeting vs tails, agent-based threshold |
| C12 | 3 | phase transition, regimes, practical implications |
| C13 | 1 | Dunn track record, structure conclusions |
| C14 | 3 | inflation, rate cycle, recency bias, trend profitable even in bad regime |
| C15 | 0 | outro |

## Claims

### C01
- **Rich Brennan** WTI drifted down from about 87 to 66 dollars over roughly 18 months in an orderly decline before a sudden spike to about 119 dollars (+80%), a setup in which shorts built up and volatility was suppressed.  #mech/overshoot _(time-bound view)_
  > The WTI fell from around 87 US dollars all the way down to roughly 66 US dollars over about 18 months.
  indicator: WTI crude oil price · asset: commodities · horizon: months · conditions: 2024-2026 oil episode · testable: partly - single episode · confidence: medium
  ^MT222-C01-1

### C02
- **Rich Brennan** Heavy short positioning, suppressed volatility and a long one-directional drift leave a market structurally coiled (dry undergrowth); a catalyst then triggers an outsized spike because momentum/amplifying participants had left.  #mech/crowding_positioning _(time-bound view)_
  > Short interest had built up steadily. The market had been quiet long enough that the amplifying forces, the momentum traders, the the trend signals had largely stepped away.
  indicator: short interest / positioning, volatility, absence of trend signals · asset: commodities · horizon: months · conditions: after long quiet drift with crowded positioning · testable: partly - positioning and vol compression measurable · confidence: medium
  ^MT222-C02-1
- **Rich Brennan** The 30% reversal from 119 to 84 within days is a position-driven overshoot unwinding as spike-chasers are stopped out and momentum signals flip.  #mech/overshoot _(time-bound view)_
  > that's a system that overshot with the participants who chased the spike getting stopped out, momentum signals flipping.
  indicator: crude oil price after spike · asset: commodities · direction: fade after spike once participants stopped out · horizon: days · testable: partly - single episode · confidence: medium
  ^MT222-C02-2
- **Niels Kaastrup-Larsen** The better inflation was managed during the 2010s, the larger the buildup for a consequential break (pandemic trigger took inflation from 2% to 10-11%), the same coiled-spring dynamic as oil.  #mech/overshoot
  > as soon as the pandemic came and was maybe in that case kind of the trigger, we saw inflation go up by 4 or 500% right from 2% to 10 11%.
  indicator: inflation · asset: multi · horizon: years · conditions: well-managed or suppressed regime · testable: partly - analogy · confidence: medium
  ^MT222-C02-3
- **Niels Kaastrup-Larsen** Risk planning has to include events that seem unimaginable; the oil spike from 66 to 119 followed by a 30% reversal is one visualisation of such an event, which standard risk models would treat as impossible.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > you had to be able to kind of imagine the unimaginable, right?
  asset: multi · testable: no - general principle · confidence: medium
  ^MT222-C02-X1
- **Rich Brennan** Governments with an electoral incentive manage energy prices lower (political agenda, intervention); this can hold prices down for a while, but when it stops working the market reasserts itself sharply, adding to the coiled-spring build-up in oil.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > we know that the current administration, maybe even the previous administration, they would like to have lower energy prices, right?
  indicator: crude oil / administration price management · asset: commodities · direction: oil spike risk after managed low prices · horizon: months · conditions: works only until policy management fails · testable: no - political judgement · confidence: medium
  ^MT222-C02-X2

### C03
- **Rich Brennan** Trend models wait patiently; cocoa took about 15 years to deliver, so diversification of investment process matters for the 99% of portfolio that otherwise relies on opinions.  #mech/risk_management
  > We never get tired. The models just wait. They they don't you know, even if it takes a year or even if it takes three years.
  asset: multi · horizon: years · testable: no - qualitative · confidence: high
  ^MT222-C03-1
- **Rich Brennan** Portfolios should be built for being wrong; trend following provides a non-correlated stream that pays off when forecasts fail.  #mech/risk_management
  > it's about what you have in your portfolio when you're wrong. It's not just about being right.
  asset: multi · testable: no - principle · confidence: high
  ^MT222-C03-2
- **Niels Kaastrup-Larsen** About 20 million bpd trapped by the Hormuz disruption equals the pandemic demand loss; as storage fills producers must cut output or shut refineries that are slow to restart, creating second-order effects.  #mech/liquidity_flows _(time-bound view)_
  > we've got about 20 million barrels per day trapped in that area. And 20 million barrels, that's actually the same amount that we saw in terms of demand destruction when the whole world closed down during the pandemic.
  indicator: oil barrels trapped; storage levels · asset: commodities · horizon: weeks · testable: partly - supply data · confidence: medium
  ^MT222-C03-3

### C04
- **Rich Brennan** Oil-driven cost increases pass through transport, manufacturing, food and wages, and prices are sticky downward (fuel surcharges are not cut), so inflation lingers after the commodity retraces; central banks tend to hike quickly, as the 1970s tolerance was costly.  #mech/policy_reaction
  > Prices go up fast and come down slowly.
  indicator: crude oil price, inflation, central bank response · asset: multi · direction: oil spike raises inflation and rates · horizon: months · testable: partly - pass-through measurable · confidence: medium
  ^MT222-C04-1
- **Rich Brennan** Trend followers need not decide whether a spike is a fundamental repricing or a positioning overshoot; they stay positioned to follow the confirmed trend.  #mech/research_method
  > Those two scenarios have very different consequences for bonds, currencies, equities, central bank policy. But I suppose as trend followers, you and me needles, we don't need to decide this in in advance.
  asset: multi · testable: no - philosophy · confidence: high
  ^MT222-C04-2
- **Niels Kaastrup-Larsen** The SocGen Trend Index reached a new all-time high end Feb 2026 while the SocGen Short-Term Traders index recovered only about 50% of its drawdown; long-term strategies outperformed short-term ones, contrary to mid-2025 narrative.  #mech/slow_reaction _(time-bound view)_
  > our SocGen trend following index uh hit a new all-time high at the end of February.
  indicator: SocGen Trend Index vs SocGen Short-Term Traders index · asset: multi · direction: long slower trend over short-term · horizon: years · conditions: 2025-2026 · testable: yes - index data · confidence: high
  ^MT222-C04-3

### C05
- **Niels Kaastrup-Larsen** A trend barometer reading of 50 indicates good breadth of trends in a classical trend portfolio.  #mech/slow_reaction _(time-bound view)_
  > My own trend barometer finished at 50 uh last night. Uh that's still a strong reading, uh meaning that there is fair fairly good breath in in a classical portfolio of trend following.
  indicator: trend barometer (Niels' breadth measure) · asset: multi · horizon: weeks · conditions: March 2026 · testable: partly - definition not given · confidence: medium
  ^MT222-C05-1
- **Niels Kaastrup-Larsen** Trend followers caught the oil spike because models flipped in mid-February; energy gains offset losses in equities, currencies and fixed income during early March 2026.  #mech/slow_reaction _(time-bound view)_
  > trend followers, I would say most of them were on the right side of the move despite what you mentioned correctly is that trend uh sorry, oil uh had been in a downtrend for quite a while
  indicator: trend signal change in crude oil · asset: commodities · direction: long energy · horizon: weeks · conditions: March 2026 · testable: partly - episode · confidence: medium
  ^MT222-C05-2
- **Niels Kaastrup-Larsen** In early March 2026 the oil shock hit stocks (MSCI World about -2.8% month to date, flat for the year) and bonds (US aggregate about -1.2%) together, so bonds gave no hedge; the SG CTA and Trend indices fell only about 2.1% on the month and were still up about 6.1% for the year, with energy gains offsetting equity, currency and fixed income losses.  #mech/risk_management _(added by sonnet-xhigh cross-check, time-bound view)_
  > aggregate bond index in the US is down 1.21%, so no help from from bonds
  indicator: MSCI World, US aggregate bond index, SG CTA and Trend index returns (Mar 2026) · asset: multi · direction: trend index loses less than stocks; bonds fail as hedge in an oil-driven inflation shock · horizon: weeks · conditions: energy supply shock with positive stock-bond correlation · testable: yes - index returns for the month checkable · confidence: high
  ^MT222-C05-X1

### C06
- **Niels Kaastrup-Larsen** March 2026: heating oil up 52% and crude up 40% month to date while silver and platinum fell about 9%, likely from liquidations to raise cash.  #mech/liquidity_flows _(time-bound view)_
  > Heating oil, to just give an example, despite the correction, it's still up 52% so far this month and crude is up around 40% from the end of February so far this month.
  indicator: heating oil, crude, silver, platinum · asset: commodities · horizon: weeks · conditions: March 2026 · testable: no - descriptive data point · confidence: high
  ^MT222-C06-1
- **Niels Kaastrup-Larsen** Multi-strategy pod shops struggled in March 2026 when tail events hit.  #mech/crowding_positioning _(time-bound view)_
  > some of these quote-unquote multi pot shops or multi-strat funds or whatever has had a a little bit of a a tough time in March.
  indicator: multi-manager hedge fund returns · asset: multi · horizon: weeks · conditions: March 2026 · testable: no - anecdotal · confidence: low
  ^MT222-C06-2
- **Rich Brennan** In regimes with fat-tail events (gold, metals, energy, deglobalization), most strategies fail except trend following and long-vol, making the coming regime beneficial for trend followers and hard for pod shops.  #mech/cycle_persistence _(time-bound view)_
  > you usually find that when you start getting into a market that's uh, exhibits these tail properties, uh, nearly all strategies fall over apart from um, the good old trend followers, um, long vol strategies
  asset: multi · direction: long trend following and long vol; avoid alternative styles · horizon: months · conditions: tail-event regime · testable: partly - needs regime definition · confidence: medium
  ^MT222-C06-3
- **Rich Brennan** The Fractals of Finance research tests whether trend patterns are a structural property of markets using 68 futures markets across 8 classes with daily data from 1984.  #mech/research_method
  > 68 uh, futures markets across eight different uh, classes. So we have equities, bonds, currencies, energies, metals, agriculturals using daily data uh stretching back to 1984.
  indicator: 68 futures markets daily 1984+ · asset: multi · horizon: years · testable: yes - study design · confidence: high
  ^MT222-C06-4

### C07
- **Rich Brennan** Logic test: a memoryless market implies no persistence, normal returns and steady volatility; finding persistence, fat tails and volatility clustering together shows feedback is structural.  #mech/structural_shift
  > If we find that trends do persist, that returns are not bell-shaped, and that volatile periods do cluster together, and if we find all three of these things simultaneously in every market we can study
  indicator: persistence, tail shape, volatility clustering · asset: multi · horizon: years · testable: yes - three testable predictions · confidence: high
  ^MT222-C07-1
- **Rich Brennan** Average Hurst exponent across 68 markets is 0.866 (decade averages 0.707 to 0.757), meaning long-range dependence in the scaling of price moves, present in every market and decade.  #mech/cycle_persistence
  > the average Hurst exponent was not.5, it was 0.866.
  indicator: Hurst exponent · asset: multi · direction: trend following supported · horizon: years · testable: yes - Hurst estimation (but estimator sensitivity to sample size and bias is a caveat) · confidence: high
  ^MT222-C07-2
- **Rich Brennan** Trend following works not because each day's direction predicts the next but because the conditions that sustain trends (high volatility, one-directional clustering, amplifying participants) persist once established; the market does not reset to a blank slate each day.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check)_
  > the conditions which sustain a trend, elevated volatility, clustering of moves in one direction, amplifying participant behavior, tend to persist once they're established.
  indicator: Hurst exponent / volatility regime persistence · asset: multi · direction: trend continuation once volatility regime is established · horizon: weeks · conditions: conditions persist after being established · testable: partly - regime persistence and conditional trend returns testable · confidence: high
  ^MT222-C07-X1

### C08
- **Rich Brennan** Simple day-to-day directional autocorrelation averages near zero across large samples; the memory sits in the magnitude and clustering of moves, so trend works through volatility expansion out of calm, not daily autocorrelation.  #mech/slow_reaction
  > the directional correlation effectively averages out to zero. But this is this is something I'll reserve for the the later podcast with you. It's a very deceptive average.
  indicator: autocorrelation of returns · asset: multi · horizon: days · conditions: directional autocorrelation near zero on average but 'deceptive' · testable: yes - autocorrelation tests · confidence: medium
  ^MT222-C08-1
- **Rich Brennan** The memory captured by the Hurst exponent is a property of the price process (energy accumulation, volatility clustering, persistence of a trending state) rather than a simple daily directional signal, so it cannot be arbitraged away as easily as directional autocorrelation.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > something that can't be arbitraged away as easily because it's not a simple signal you can trade on
  indicator: Hurst exponent · asset: multi · testable: partly - persistence of the structural property over time is testable, the non-arbitrage claim is an argument · confidence: medium
  ^MT222-C08-X1

### C09
- **Rich Brennan** Five-sigma daily moves occur 5,791 times more often than a normal distribution predicts, with a power-law tail exponent of about 3.33 in every liquid market.  #mech/risk_management
  > five sigma events occurred 5,791 times more frequently than the standard model predicts.
  indicator: five-sigma daily move frequency; tail exponent 3.33 · asset: multi · testable: yes - tail statistics · confidence: high
  ^MT222-C09-1
- **Rich Brennan** Volatility clustering is strong: the average autocorrelation of absolute daily move size is 0.353 across 68 markets.  #mech/cycle_persistence
  > we measured this using the auto correlation of the size of daily moves across all 68 markets, and the average was 0.353.
  indicator: autocorrelation of absolute daily returns · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT222-C09-2
- **Rich Brennan** Markets contain convergent (stabilising) participants creating the tall narrow peak of the distribution and divergent (amplifying) participants such as trend followers, momentum, stop-loss and margin calls creating the fat tails.  #mech/crowding_positioning
  > Value buyers, for example, arbitrageurs, mean reversion traders, they fit into this class of convergent trader. They produce the actual tall, narrow peak of the curve
  indicator: convergent vs divergent participant mix · asset: multi · testable: partly - mechanism, not directly observable · confidence: medium
  ^MT222-C09-3

### C10
- **Niels Kaastrup-Larsen** Trend systems with dynamic position sizing reduce exposure as volatility expands, so they may sell during a spike and dampen rather than amplify; this differs from vol-buying approaches.  #mech/risk_management
  > as counterintuitive as it may sound, but we'll probably be selling oil the last few days in order to adjust our positions down within a certain risk framework.
  indicator: volatility-adjusted position size · asset: commodities · direction: reduce position as volatility expands · horizon: days · conditions: dynamic position sizing, daily risk target · testable: yes - compare to fixed sizing · confidence: medium
  ^MT222-C10-1
- **Rich Brennan** Trend followers are not external observers: as divergent (amplifying) participants they are part of the feedback system that creates the fat tails and trends they profit from, so trend following is alignment with a structural feature of price formation rather than just a style.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check)_
  > We are participants in the feedback system itself that generate the very phenomena we exploit.
  asset: multi · testable: no - conceptual claim · confidence: medium
  ^MT222-C10-X1
- **Niels Kaastrup-Larsen** Volatility expansion can be harvested two ways: buying cheap volatility and selling it on the spike (the Dave Dredge approach) or mechanically via trend following with dynamic position sizing; the difference lies in how position size is treated as vol rises.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > expansion by buying cheap vol and sell it when you get out. But but you can also do it um in a more mechanical way like we do.
  indicator: volatility expansion · asset: multi · direction: long cheap vol vs trend following with vol-scaled sizing · testable: partly - compare payoffs of long vol and vol-sized trend around vol spikes · confidence: medium
  ^MT222-C10-X2

### C11
- **Rich Brennan** Volatility targeting assumes recent vol predicts the future and is calibrated to the middle of the distribution; with tail exponent 3.33 it underestimates the chance of losses, e.g. oil sized for the calm 66-80 range then hitting 119.  #mech/risk_management
  > let's say you size positions to target a fixed volatility level. You're therefore implicitly assuming that recent volatility is a reasonable guide to future uh to the future.
  indicator: volatility targeting, tail exponent · asset: multi · conditions: fails after prolonged calm · testable: yes - backtest vol targeting vs fixed risk · confidence: medium
  ^MT222-C11-1
- **Rich Brennan** Agent-based simulation shows a sharp threshold at roughly 25-30% divergent (amplifying) participation: below it markets are calm and bell-shaped; above it trends, volatility clusters and fat tails emerge.  #mech/crowding_positioning
  > below a certain level of divergent participation, roughly 25 to 30% in the models that we applied, uh the simulated market behaves in a very stable way
  indicator: share of divergent participants in simulation · asset: multi · testable: partly - simulation, share not observable · confidence: medium
  ^MT222-C11-2
- **Niels Kaastrup-Larsen** Dunn targets a daily risk level rather than a fixed volatility target, while many managers still use a fixed volatility target; the host argues this distinction matters because of the fat-tailed return distribution.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > at Dawn at least we use we use a daily risk target. Not a daily volatility target.
  indicator: daily risk target vs fixed volatility target · asset: multi · horizon: days · conditions: fat tails make a fixed vol target unreliable · testable: partly - compare drawdown of risk-target vs vol-target sizing · confidence: medium
  ^MT222-C11-X1

### C12
- **Rich Brennan** Trend/range regimes reflect the balance between stabilising and amplifying participants, driven by observable conditions (volatility, positioning, fear, momentum, margin levels); a quiet market is not evidence trend following stopped working, and strategies should be robust across regimes.  #mech/cycle_persistence
  > Regime changes are not random weather.
  indicator: volatility, positioning, momentum, margin levels · asset: multi · horizon: months · testable: partly - regime proxies needed · confidence: medium
  ^MT222-C12-1
- **Rich Brennan** The oil spike was a phase transition when the shock pushed amplifying participation above threshold; it reverted because the participant mix was not durably changed, and persistence depends on whether the supply disruption is real and sustained.  #mech/overshoot _(time-bound view)_
  > the geopolitical shock was the catalyst that pushed participation above that threshold
  indicator: crude oil · asset: commodities · direction: trend if sustained, revert towards mid-70s if resolved · horizon: months · testable: no - scenario · confidence: low
  ^MT222-C12-2
- **Rich Brennan** Risk frameworks based on bell curves (position sizing, VaR, 2-3 sigma stress tests) understate risk; diversification across asset classes is participation in different feedback environments with the same structure.  #mech/risk_management
  > Position sizing, value at risk calculations, stress tests calibrated to two or three sigma moves, all of these carry more exposure than they appear to.
  indicator: VaR, sigma-based stress tests · asset: multi · testable: yes · confidence: high
  ^MT222-C12-3
- **Rich Brennan** Because trend memory (Hurst 0.866) is a persistent structural feature, trend signals are not noise that dissolves on inspection, which gives an empirical basis for holding trend positions with conviction even when they are uncomfortable.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > that's the empirical basis for conviction in trend following signals even when the positions feel uncomfortable for us.
  indicator: Hurst exponent 0.866 · asset: multi · testable: no - argument for conviction, not a test · confidence: medium
  ^MT222-C12-X1
- **Rich Brennan** Conditional oil view: if the geopolitical situation resolves, stabilising participants reassert and WTI returns toward the mid-70s; if the disruption is sustained, the new price level builds its own structural support and the spike becomes a genuine trend rather than a spike-and-revert.  #mech/overshoot _(added by sonnet-xhigh cross-check, time-bound view)_
  > if the geopolitical situation resolves, the stabilizing forces reassert and prices return towards the mid-70s.
  indicator: WTI crude · asset: commodities · direction: WTI to about mid-70s if resolved; persistent trend if sustained · horizon: months · conditions: depends on whether the supply disruption is real and persistent · testable: yes - price path versus the two scenarios · confidence: medium
  ^MT222-C12-X2

### C13
- **Niels Kaastrup-Larsen** Dunn's record shows only two runs of eight consecutive winning months in 50 years; regimes can pay consistently once established, but 6-12 months of small monthly losses are normal while markets wait for a new regime.  #mech/cycle_persistence
  > we've only had two periods now where we've had eight monthly winning month.
  indicator: consecutive winning months in trend programme · asset: multi · horizon: months · testable: yes - from track record · confidence: medium
  ^MT222-C13-1

### C14
- **Rich Brennan** A sustained oil spike would revive high inflation and interest rates (Australian cash 17.5% in the 1990s), producing significant trends and a healthy decade for trend following.  #mech/policy_reaction _(time-bound view)_
  > if this oil move is sustained um the inflation is going to come roaring back.
  indicator: oil, inflation, interest rates · asset: multi · direction: long trend following; rates higher · horizon: years · conditions: if oil move is sustained · testable: no - view · confidence: medium
  ^MT222-C14-1
- **Niels Kaastrup-Larsen** Interest rates after a 40-year cycle of lower lows have started making higher highs, and rate regimes and the stock-bond correlation persist once established, so recency bias toward the old normal is dangerous.  #mech/cycle_persistence _(time-bound view)_
  > we had, you know, 40 years of of of lower lows in in interest rates. Now we've started only recently, really, getting higher highs in interest rates.
  indicator: interest rate cycle, stock-bond correlation · asset: rates · horizon: years · testable: partly - long cycles have few observations · confidence: medium
  ^MT222-C14-2
- **Niels Kaastrup-Larsen** Trend following was still profitable (though less so) in the unfavourable 2010s environment, so it is a robust strategy and not disaster insurance only.  #mech/risk_premium
  > even through the period where it wasn't necessarily conducive for trend following, we still made money.
  indicator: trend following returns across regimes · asset: multi · horizon: years · testable: yes - track record · confidence: medium
  ^MT222-C14-3

