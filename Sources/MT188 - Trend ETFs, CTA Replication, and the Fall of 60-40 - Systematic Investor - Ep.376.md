---
source_id: MT188
title: "Trend ETFs, CTA Replication, and the Fall of 60-40 - Systematic Investor - Ep.376"
date: 2025-12-02
channel: "Top Traders Unplugged"
url: 
words: 12073
claims: 45
added_by_crosscheck: 11
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Andrew Beer (co-host, DBMF managed-futures replication ETF)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Trend ETFs, CTA Replication, and the Fall of 60-40 - Systematic Investor - Ep.376

**Speakers:** Andrew Beer (co-host, DBMF managed-futures replication ETF); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Dec 2025 Systematic Investor: Beer and Kaastrup-Larsen discuss the shift away from 60/40 as bonds stopped diversifying, why a 10-market replication ETF (DBMF) beat the CTA index in 2025, a Simplify index-based CTA ETF and the true-cost debate for swaps vs fees, and how to explain trend following ('cloudy crystal ball', someone knows something). Also Nordic roundtable on short-term vs long-term models and alpha/beta separation.

**Approach:** trend following, CTA replication, managed futures ETF, 60/40, fees and implementation costs, alpha-beta separation

**Cross-check completeness estimate of first read:** 0.85 - the first reader caught the main replication, cost-debate, crystal-ball and alpha/beta arguments with correct numbers; it missed research-method points (index survivorship, hypothetical-number scepticism, timing noise, sensitivity of design to cost assumptions), tax structuring and the allocator manager-blending point, and slightly overstated the effect of slow de-risking.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, Thanksgiving chat, Goldman article lead-in |
| C02 | 3 | 60/40 paradigm shift, bonds failing as diversifier, liquid alts demand, trend ETFs |
| C03 | 2 | pod shops (Dalio view), Bitcoin pullback, November market recap |
| C04 | 2 | portfolio de-risking, concentration (yen, euro), CTAs contrarian after Liberation Day |
| C05 | 3 | sources of 2025 DBMF outperformance: simplicity, slow de-risking, noise; replication as alternative data |
| C06 | 2 | replication design target, 10-market signal question, signal vs complexity |
| C07 | 3 | replication is technological efficiency; index performance YTD figures; Simplify ETF intro |
| C08 | 2 | index around replication strategy, swaps, ETF derivatives rules, Simplify CTA |
| C09 | 3 | Simplify index ETF fees; all-in implementation costs of CTAs |
| C10 | 2 | fee disclosure vs implementation costs; turnover of CTA portfolios; instrument count costs |
| C11 | 1 | ETF model portfolios have zero diversifier; swap fee transparency concern |
| C12 | 2 | incentive fees and costs vs return over cash; zero reported transaction costs |
| C13 | 2 | narrative for managed futures; contrarian early and right; someone knows something |
| C14 | 2 | detectors/crystal ball metaphor; trend follower needs no forecast |
| C15 | 2 | insider-buying analogy; who the alpha comes from; Mr. Market as PM |
| C16 | 2 | Nordic roundtable: short vs long models, esoteric markets, human judgement |
| C17 | 1 | heterogeneity, alpha-beta separation, core allocation then single manager risk |
| C18 | 0 | outro, nothing actionable |

## Claims

### C02
- **Andrew Beer** In this decade bonds stopped working as a diversifier, behaving like lousy equity exposure (lower returns, similar drawdown, higher volatility), pushing allocators to add a diversifying 'other' bucket.  #mech/structural_shift
  > the the playbook of 6040 just stopped working
  indicator: stock-bond correlation / bond diversification · asset: multi · direction: less bonds, more diversifiers such as managed futures · horizon: years · conditions: post-2020 inflation regime · testable: yes - bond diversification and 60/40 stats · confidence: high
  ^MT188-C02-1
- **Andrew Beer** Managed futures is a statistically obvious diversifier but is still zero in many portfolios; easy ETF access could make it standard.  #mech/structural_shift
  > manager futures is one of those really statistically obvious allocations. If you give them uh easy and efficient ways of investing to it,
  asset: multi · direction: add managed futures · horizon: years · testable: partly · confidence: medium
  ^MT188-C02-2
- **Niels Kaastrup-Larsen** Goldman expects wealth allocations flowing more to liquid alternatives than illiquid ones; large managers (BlackRock, Fidelity, Invesco) are launching trend ETFs.  #mech/liquidity_flows _(time-bound view)_
  > they were actually expecting more money going into liquid alternatives, not so much these illlquid alternatives
  asset: multi · horizon: years · testable: no · confidence: low
  ^MT188-C02-3
- **Andrew Beer** Allocation paradigm shifts (Kuhn's structure of scientific revolutions) happen abruptly rather than gradually: once the 60/40 playbook broke, wealth managers jump to a new framework (stocks, shrinking bonds, plus an 'other' diversifier bucket) without explaining the break, which is what opens the door for managed futures and other alternatives.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > a new paradigm is established and then all of a sudden people hop over from the old paradigm to the new paradigm without kind of explaining why they made the jump.
  asset: multi · direction: flows move from bonds to diversifying alternatives · horizon: years · conditions: after a long-standing portfolio rule visibly fails (bonds not diversifying in this decade) · testable: partly - fund-flow data into alternatives after 2022 · confidence: medium
  ^MT188-C02-X1

### C03
- **Niels Kaastrup-Larsen** Dalio is not bullish on multi-manager pod shops because internal competition makes them uncollegial; pod shops are the current hot alternative.  #mech/crowding_positioning _(time-bound view)_
  > they asked him about the multistrat, the pot shops and what his prediction was for them. And actually he was not particularly bullish about their uh ability um going forward.
  asset: multi · horizon: years · conditions: pod shops · testable: no - opinion · confidence: low
  ^MT188-C03-1
- **Andrew Beer** Pod shops face diminishing team quality as inflows grow, yet they have defied naysayers for years with leverage and risk controls.  #mech/crowding_positioning
  > I can't believe that your 300th team is as good as your fifth team that you've hired.
  indicator: number of pods/teams · asset: multi · horizon: years · conditions: capacity of pod shops · testable: partly · confidence: medium
  ^MT188-C03-2

### C04
- **Andrew Beer** A 10-market replication portfolio is more concentrated than diversified CTAs, so it carries idiosyncratic risk (more short yen helped; more short euro hurt in 2025).  #mech/risk_management _(time-bound view)_
  > one of the things in our portfolios is obviously we're more concentrated in our positions and usually uh sometimes there's idiosyncratic risk associated with that.
  indicator: portfolio concentration · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT188-C04-1
- **Andrew Beer** Trend followers that stayed long equities after Liberation Day were contrarian and early; many human strategists capitulated.  #mech/slow_reaction _(time-bound view)_
  > just how contrarian it was to maintain this kind of bullish position in the let it run hot trade um after liberation day.
  asset: equities · direction: stay long equities · horizon: months · conditions: after April 2025 shock · testable: no - single episode · confidence: medium
  ^MT188-C04-2
- **Niels Kaastrup-Larsen** In November 2025 short-term trend managers struggled even though the headline trend indices looked flat, so aggregate index moves can hide dispersion between short-term and longer-term models.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > some short-term managers uh have had real challenges in November, which um the surface numbers don't really um explain.
  indicator: short-term CTA performance versus trend index · asset: multi · direction: short-term models underperformed · horizon: weeks · conditions: zigzag month with mid-month reversals · testable: yes - compare SG Short-Term Traders Index with SG Trend Index monthly · confidence: medium
  ^MT188-C04-X1

### C05
- **Andrew Beer** After Liberation Day secondary and esoteric markets were more volatile than major ones, so portfolios with many exotic markets were whipsawed more.  #mech/risk_management _(time-bound view)_
  > complexity actually hurt portfolios. The more positions you had in more esoteric markets if you're getting whipsaw you were getting whipsaw more there.
  indicator: market universe breadth · asset: multi · horizon: weeks · conditions: volatile shock · testable: yes - compare core vs wide universe · confidence: medium
  ^MT188-C05-1
- **Andrew Beer** A replication fund with a short but not very short lookback was slower to de-risk, which helped when the shock reversed (about 500bp of 2025 outperformance came in days after Liberation Day).  #mech/slow_reaction _(time-bound view)_
  > we're always looking back in a you know pretty short rear it's a rearview window but it's a pretty short rearview window. um uh you know we can be a little bit slower to derisk and that definitely helped us
  indicator: signal lookback; speed of de-risking · asset: multi · horizon: days · conditions: V-shaped reversals · testable: yes · confidence: medium
  **Correction (cross-check):** Attributes the full ~500bp of post-Liberation-Day outperformance to slower de-risking. The speaker says the 500bp arose in the days after Liberation Day mostly because the major-market-only portfolio was less whipsawed than portfolios with esoteric markets; slower de-risking is a separate second factor that added only 'a couple of points' when Trump changed course. → A replication fund with a short-but-not-very-short lookback was a little slower to de-risk in April 2025, and when the tariff shock reversed it still held residual risk, adding roughly two points of return; the larger ~500bp outperformance in the days after Liberation Day came mainly from holding only 10 major markets (see C05-1).
  ^MT188-C05-2
- **Niels Kaastrup-Larsen** Replication using fund exposures yields tracking error, so it is closer to an alternative-data CTA than a true tracker.  #mech/research_method
  > maybe instead of it being a replication strategy to me maybe it's kind of an alternative data strategy
  indicator: tracking error vs SG CTA index · asset: multi · horizon: years · testable: yes · confidence: low
  ^MT188-C05-3
- **Andrew Beer** A third source of divergence from the CTA index is pure timing noise: a fixed weekly rebalance day sometimes gains and sometimes loses a few days of signal drift relative to peers, so some relative performance is luck rather than design.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > we rebalance on Mondays. Sometimes it feels like a great decision. Sometimes you know you you really wish you'd rebalance the prior Thursday or the next Tuesday or something.
  indicator: weekly rebalance timing · asset: multi · horizon: weeks · conditions: most visible around sharp reversals · testable: yes - shift the rebalance weekday and measure P&L dispersion · confidence: medium
  ^MT188-C05-X1

### C06
- **Andrew Beer** The replication design assumed hedge-fund index costs (management, incentive, implementation) of about 200bp conservatively, targeting index plus 400bp, and it delivered that or more.  #mech/research_method
  > we really tried to aim for for stock gench and index plus 400 basis points.
  indicator: SG CTA index; replication of 10 factors · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT188-C06-1
- **Andrew Beer** If 10 major markets reproduce CTA beta, crisis alpha and zero stock-bond correlation, the CTA signal is a major-market signal and extras (shorter-term models, vol controls, exotic markets) may detract.  #mech/research_method
  > If you can get that same statistical characteristics only 10 instruments then is the signal itself of the space really a major market signal
  indicator: 10-instrument replication · asset: multi · horizon: years · conditions: unproven; will take years · testable: partly - needs long outperformance record · confidence: medium
  ^MT188-C06-2

### C07
- **Andrew Beer** Replication is an efficiency innovation to capture the trend signal, not a diluted version of CTA alpha; the industry largely disagrees.  #mech/structural_shift
  > I actually think it's I I I would actually argue it's almost more of a technological innovation of finding a way to capture that signal
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT188-C07-1
- **Niels Kaastrup-Larsen** As of late Nov 2025: BTOP50 +1.05% YTD, SG CTA -3.06%, SG Trend -0.79%, SG Short-Term Traders -5.76% YTD.  #mech/slow_reaction _(time-bound view)_
  > Btop 50 is down 18 basis point uh 0.18. It's up 1.05%. 05% so far this year.
  indicator: BTOP50; SG CTA; SG Trend; SG Short-Term Traders · asset: multi · horizon: months · testable: yes - index data · confidence: high
  ^MT188-C07-2
- **Andrew Beer** The same 10-factor replication has run weekly (Mondays) since July 2016 without change, now with a 9.5-year track record in different vehicles.  #mech/research_method
  > our core replication strategy, which is in an ETF in the US and in a use fund in Europe, um, was launched in the middle of 2016 as an active strategy.
  asset: multi · horizon: years · testable: yes - live record · confidence: high
  ^MT188-C07-3
- **Andrew Beer** Whether the extras that most CTAs add (short-term models, vol controls, exotic markets) destroy value relative to a 10-market major-market signal is not yet known and will take several more years of live evidence to resolve; the 2024-2025 outperformance is suggestive, not conclusive.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > We don't know the answer to that, and we're actually not going to know the answer to that for a few years.
  asset: multi · horizon: years · conditions: needs several more years of live data across regimes · testable: yes - out-of-sample comparison of 10-market versus wide-universe CTA indices · confidence: medium
  ^MT188-C07-X1
- **Andrew Beer** Derivative-based strategy indices can be created overnight and closed or replaced if they fail, so a bank-published index with a backfilled history carries survivorship and selection bias unless the rules were fixed and live before the history was shown.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > we can create an index on Monday if it's not working by Thursday we'll shut it down we'll launch a new one the following Monday
  indicator: strategy index track records · asset: multi · conditions: applies to rules-based swap/derivative indices launched by banks · testable: yes - compare backfilled index performance with performance after launch · confidence: high
  ^MT188-C07-X2

### C08
- **Andrew Beer** Wealth managers lack a tradable index for CTA exposure, so an index around the replication strategy lets allocators model and benchmark it with long history (and via swaps).  #mech/structural_shift
  > you can't actually, it's not like if you benchmark a manager to the S&P 500, you have a default.
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT188-C08-1
- **Andrew Beer** The 2019 SEC derivatives rule made derivative-based ETFs easier, enabling trend and managed futures ETFs.  #mech/structural_shift
  > In the US in 2019, there was a change in rules around the use of derivatives and ETFs
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT188-C08-2
- **Andrew Beer** Allocators are rightly sceptical of hypothetical backtests, so credibility for an index comes from running the identical rules live for years without changes before building a benchmark on them.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > by 2024, having now proven year after year after year after year this rep replication strategy worked without changing it, we then could launch an index around it.
  asset: multi · horizon: years · testable: yes - compare rule stability and live versus backtest returns · confidence: high
  ^MT188-C08-X1

### C09
- **Andrew Beer** Simplify's index-based managed futures ETF charges 20bp plus 15bp acquired fund expenses; swap costs of accessing the index are not shown in the headline fee.  #mech/structural_shift
  > they've priced it very low, a 20 basis point management fee and then a 15 basis points of of of acquired fund expenses.
  indicator: fees · asset: multi · horizon: years · testable: no · confidence: high
  ^MT188-C09-1
- **Andrew Beer** Trading 10 liquid futures contracts less often cuts implementation costs, giving about 350bp annual outperformance over a decade versus funds trading hundreds of contracts.  #mech/risk_management
  > 350 basis points of annual outperformance over a decade. Uh the reason it's so pronounced is because there are efficiencies that we've tapped into
  indicator: implementation cost; turnover · asset: multi · horizon: years · testable: yes - cost decomposition · confidence: medium
  ^MT188-C09-2
- **Niels Kaastrup-Larsen** Implementation costs of a CTA strategy (~300bp) are real costs even if not paid to the manager, and should be compared apples to apples.  #mech/risk_management
  > it costs 300 basis points to implement this CTA
  indicator: implementation cost · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT188-C09-3
- **Andrew Beer** Simplify's existing CTA ETF is a different product from the DBMF-style replication (it trades only two of four asset classes and had a very different return profile, up about 24% in 2024), so the same label covers materially different exposures.  #mech/research_method _(added by sonnet-xhigh cross-check, time-bound view)_
  > they only trade two of the four different asset classes they're up 24% or something in 2024 I mean it's very very different return profile
  indicator: Simplify Managed Futures Strategy ETF (CTA) · asset: multi · horizon: years · testable: yes - compare return series and asset-class exposures · confidence: medium
  ^MT188-C09-X1

### C10
- **Andrew Beer** CTAs with short-term models, vol controls and many instruments can turn over notional about 20 times a year, so implementation cost per added instrument (70 to 190 markets) matters.  #mech/risk_management
  > your $100 might turn over 20 times during the course of a year. 20 times like that may turn over on a on a notional basis, right?
  indicator: portfolio turnover; number of instruments · asset: multi · direction: limit instruments · horizon: years · testable: yes - turnover and cost estimates · confidence: medium
  ^MT188-C10-1
- **Andrew Beer** Versus multi-manager Abby Capital, about 350bp better over time: roughly 100bp from performance differential in the ETF, extra volatility, and 150bp not explained by management fees.  #mech/research_method
  > we do about 350 basis points better than them over time okay three reasons
  asset: multi · horizon: years · testable: yes · confidence: low
  **Correction (cross-check):** The caption is garbled and the first-reader claim treats '100bp performance differential in the ETF' as one of three additive reasons; the speaker also says the 150bp is what is not explained by the management-fee difference, which suggests the first ~100bp is a fee/cost difference and that part of the gap may just be higher volatility in a rising market. → Beer says the ETF beats the multi-manager Abbey Capital by about 350bp over time: about 100bp from a cost/performance differential in the ETF, some from taking somewhat more volatility in a rising market, and at least another ~150bp that the management-fee difference does not explain. Low confidence because the transcript caption is unclear.
  ^MT188-C10-2

### C11
- **Andrew Beer** About 80% of US ETF assets cost below 20bp; ETF model portfolios hold only stocks and bonds, with zero diversifier exposure.  #mech/structural_shift
  > 80% of the assets have expense ratios still below 20 basis points.
  indicator: ETF expense ratios · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT188-C11-1

### C12
- **Andrew Beer** SG Trend index returned about 300bp over cash net of fees, about 500bp before fees, framing fee debates.  #mech/risk_premium
  > net of fees the sock gen CTNX has done 300 basis points over cash, right? So, so let's say prefee that's 500 basis points
  indicator: SG Trend Index vs cash · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT188-C12-1
- **Andrew Beer** US fund reporting rules allow zero reported transaction costs in some CTA mutual funds, hiding true implementation costs.  #mech/research_method
  > You've got people who report zero transaction costs because the US rules are so bad around calculating transaction costs.
  indicator: reported transaction costs · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT188-C12-2
- **Andrew Beer** Accessing a strategy through swaps or derivatives on an index allows structuring flexibility (notes, principal protection, excess-return versions) that can improve tax efficiency, so tax effectiveness should be counted alongside fees when comparing implementations.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > I believe that there is a lot more flexibility on the structuring side that can also solve things on the tax side for people
  asset: multi · conditions: depends on investor tax status and vehicle · testable: partly - after-tax return comparison of swap, ETF and fund wrappers · confidence: medium
  ^MT188-C12-X1

### C13
- **Andrew Beer** Trend following has episodes where it is contrarian, early and right (short Treasuries Sept 2020, short yen at breakout from 105-110 band, long gold below $3,000).  #mech/slow_reaction
  > what I love about the space is that every now and then it's contrarian early and right in a big way
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT188-C13-1
- **Andrew Beer** Price trending from 10 to 12 signals that someone knows something; trend following latches onto new information (inflation, policy), not sentiment changes, as with the yen from 110 to 160.  #mech/slow_reaction
  > someone knows something what do they know that I don't know
  indicator: price trend as information · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT188-C13-2

### C14
- **Andrew Beer** CTAs act as detectors across many markets, signalling major changes early (yen, Treasuries, crude oil in 2022).  #mech/slow_reaction
  > they've built these global detectors around these local markets to to get an early warning sign that that something big is changing.
  indicator: trend signals across markets · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT188-C14-1
- **Niels Kaastrup-Larsen** If a forecast is right, the price path will produce the trend signal anyway; trend following captures correct views without needing to forecast.  #mech/cycle_persistence
  > if the crystal ball is right we will pick that up. That is our signal. So we don't need the crystal ball actually.
  asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT188-C14-2

### C15
- **Andrew Beer** Prices reveal informed participants voting with their portfolios (like insider buys and sells), so one can follow without knowing what they know.  #mech/slow_reaction
  > You don't need to know what they know. You just need to know that they're buying or selling their own stock.
  asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT188-C15-1
- **Andrew Beer** Trend alpha comes from slow institutional models, such as 60/40 portfolios rebalancing into falling bonds in 2022, which cannot change as the world changes.  #mech/crowding_positioning _(time-bound view)_
  > It's every 6040 portfolio that was dialing up their exposure to bonds going into 2022 because they needed to rebalance it up.
  indicator: rebalancing flows · asset: rates · direction: short bonds in 2022 · horizon: months · testable: partly · confidence: medium
  ^MT188-C15-2
- **Andrew Beer** Trend following using only historical prices has worked for about 50 years despite academic weak-form efficiency arguments, and its profits come from institutions with slow, fixed models rather than from other trend followers.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > studying historical prices which academics tell us it shouldn't work. Why? It's worked for 50 years, right?
  indicator: long-run trend following track record · asset: multi · horizon: years · testable: yes - long-run trend index returns net of costs · confidence: high
  ^MT188-C15-X1

### C16
- **Andrew Beer** At the Stockholm roundtable CTAs debated short-term vs long-term models, esoteric vs core markets, risk controls, and AI/alternative data (AQR); equally smart people disagreed on the same data.  #mech/research_method
  > shorterm versus longerterm models. Um uh more more esoteric markets versus versus the core markets.
  asset: multi · testable: no · confidence: medium
  ^MT188-C16-1
- **Andrew Beer** Enhancements such as added short-term models are presented with false certainty, backed by selective evidence, while the business is ultimately human judgement.  #mech/research_method
  > it's presented with a certainty. you know, we are adding short-term models because by the time it's it's presented
  asset: multi · testable: partly · confidence: medium
  ^MT188-C16-2
- **Andrew Beer** CTA design choices are highly sensitive to small changes in assumed implementation costs or signal speed, which is why equally smart managers reach opposite conclusions on the same data; the heterogeneity of approaches across the space is therefore a healthy feature.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > small changes in assumptions around implementation costs or speed or things like that can have an
  indicator: assumed implementation cost; signal speed · asset: multi · testable: yes - sensitivity analysis of net returns to cost and speed assumptions · confidence: medium
  ^MT188-C16-X1

### C17
- **Andrew Beer** Alpha/beta separation: hold a cheap core replication/beta allocation and then take more single-manager or commodity risk (e.g. AQR, which had a train wreck in prior six years then a strong 5).  #mech/risk_management
  > you can take more single manager risk if you feel you have the beta solved.
  indicator: core-satellite allocation · asset: multi · direction: core beta plus satellite managers · horizon: years · testable: partly · confidence: medium
  ^MT188-C17-1
- **Andrew Beer** Because allocators cannot yet get the core trend signal efficiently, they bolt together several managers to average out differences, ending up with an index-like blend of 'beta adjacent' strategies that is inefficient compared with owning the core directly and adding satellites.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > they'll take four of the six or four of the eight people in the room and put them together into a portfolio to try to cancel out a lot of these differences
  asset: multi · horizon: years · conditions: holds if a cheap, efficient core trend allocation is available · testable: yes - compare a multi-manager blend with a core-plus-satellite portfolio on net Sharpe and fees · confidence: medium
  ^MT188-C17-X1

