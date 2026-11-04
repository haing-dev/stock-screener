---
source_id: MT168
title: "The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393"
date: 2026-03-29
channel: "Top Traders Unplugged"
url: 
words: 11507
claims: 38
added_by_crosscheck: 6
corrections: 1
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Niels Kaastrup-Larsen (host, hedge fund manager)", "Yoav Git (co-host, systematic fixed-income researcher; speaker label in captions is Yuval/Yoav)"]
tags: [source, layer0]
---
# The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393

**Speakers:** Niels Kaastrup-Larsen (host, hedge fund manager); Yoav Git (co-host, systematic fixed-income researcher; speaker label in captions is Yuval/Yoav)

**Summary:** March 2026 Iran war shock: stocks and bonds sold off together, oil front-end spiked while the back barely moved, CTAs lost little. Git argues CTAs should hedge a common first factor (duration) rather than scale every position when spreads widen, reviews a flow-based excess-volatility paper (value, noise and trend traders), and frames CTA market-universe breadth by correlation and capacity.

**Approach:** trend following, fixed income, stock-bond correlation, risk management in crises, flows, excess volatility, market universe, capacity

**Cross-check completeness estimate of first read:** 0.85 - the first reader captured the crisis, flows, paper and capacity arguments well; missed the EM-algorithm method, the excess-volatility motivation, the initial-positioning dispersion point, the pre-announcement trading remark, the caveat that factor hedging is not worth it for liquid CTAs, and Niels's tracking-error point.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro; EM algorithm explained |
| C02 | 1 | EM algorithm cont.; Danish election narrative lesson |
| C03 | 3 | gold behaviour in Iran war; inflation vs risk-off in oil curve and bonds |
| C04 | 2 | intraday execution timing risk, record surprise volatility, stock-bond correlation positive |
| C05 | 3 | CTAs vs 2022 analogy; weak 2-year auction; fiscal pressure and yields |
| C06 | 3 | private credit gating; supply vs price; index numbers March 2026 |
| C07 | 2 | index numbers; oil curve front vs back; weather vs climate; inflation expectations |
| C08 | 2 | flows and risk management in a rates shock; discretionary vs CTA hedging |
| C09 | 3 | core vs alternative market liquidity; closing book costs 5% |
| C10 | 2 | factor-based risk management as optimisation; liquidity crisis risk; flows begin |
| C11 | 2 | flow sequence in crisis: CTAs, value traders closed out; paper intro |
| C12 | 2 | efficient market hypothesis variants; three-player flow model |
| C13 | 2 | model calibration with EM; CTA contribution to volatility tiny; pendulum picture |
| C14 | 1 | pendulum dynamics; critique: news jumps are value changes, nonfarm payroll liquidity |
| C15 | 2 | critique: cubic response unrealistic; capacity and breadth blog starts |
| C16 | 2 | diversification times average market Sharpe; correlation and capacity; replication tracking |
| C17 | 0 | next guest, outro |

## Claims

### C02
- **Niels Kaastrup-Larsen** Danish election campaign narratives (Greenland, geopolitics expected) ended up dominated by animal welfare and clean water, showing narratives are unpredictable even for narrative-driven markets.  #mech/behavioral _(time-bound view)_
  > It ended up being animal welfare and clean drinking water.
  asset: other · testable: no - anecdote · confidence: low
  ^MT168-C02-1
- **Yoav Git** The EM (expectation-maximisation) algorithm estimates the parameters of mixed, unlabelled populations by alternating a probabilistic classification of each observation (E step) with re-estimating each distribution (M step) until it converges; it is the calibration tool later used to size the noise, value and trend-trader populations in the flow model.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > it's an iterative process, a little bit like the back propagation process that we have in machine learning these days
  indicator: EM algorithm for mixture-model calibration · asset: other · conditions: needs enough observations; iterative convergence · testable: yes - standard statistical method · confidence: high
  ^MT168-C02-X1

### C03
- **Niels Kaastrup-Larsen** Gold sold off both at war start and on de-escalation news in March 2026, an unpredictable response that supports a rules-based approach.  #mech/behavioral _(time-bound view)_
  > it seems like it's selling off when the war began, but it's almost like it's also selling off now that there might be a de-escalation of the war.
  indicator: gold · asset: commodities · horizon: weeks · testable: partly · confidence: medium
  ^MT168-C03-1
- **Yoav Git** The oil spike was concentrated at the front of the curve (supply constraints) while Brent three years out barely moved, because the long-run market is over-producing (about 105 mb/d produced vs 102 consumed).  #mech/structural_shift _(time-bound view)_
  > the spike in oil is at the front of the curve, right?
  indicator: Brent curve slope · asset: commodities · horizon: weeks · conditions: front-end shock vs structural oversupply · testable: yes - curve data · confidence: high
  ^MT168-C03-2
- **Yoav Git** Bond sell-offs at long ends of US/UK/EM curves (TY from 114 to 110, more than a year's move in weeks) point to a risk-off event rather than a pure inflation-expectations story.  #mech/liquidity_flows _(time-bound view)_
  > We've seen actually a sell-off at the back of the curve, um, which is sort of indicative that what this is happening is a bit of a much more of a risk-off event
  indicator: 10-year yield, TY futures, EM curves · asset: rates · horizon: weeks · testable: yes · confidence: medium
  ^MT168-C03-3
- **Niels Kaastrup-Larsen** Over the weeks around a shock, dispersion across CTAs is largely driven by initial positioning luck rather than model quality, so short-window results should not be over-read as skill.  #mech/research_method _(added by sonnet-xhigh cross-check, time-bound view)_
  > we know that positioning, initial positioning is so important, and um and you can be lucky, you can be unlucky with how you enter a situation like that
  indicator: dispersion of CTA returns around shocks · asset: multi · horizon: weeks · conditions: short windows around geopolitical shocks (March 2026) · testable: yes - cross-sectional dispersion of manager returns vs prior positioning · confidence: medium
  ^MT168-C03-X2

### C04
- **Yoav Git** With oil trading a $20-25 daily range (Brent near 120 then 90), execution time of day materially changes P&L and makes tracking one's own model difficult; scenario analysis back to 1998 ranks March 2026 surprise volatility at the top.  #mech/risk_management _(time-bound view)_
  > oil is traded in a range of say 20-25 dollars a day.
  indicator: intraday oil range · asset: commodities · horizon: days · conditions: extreme intraday volatility · testable: yes · confidence: high
  ^MT168-C04-1
- **Yoav Git** Inflation regimes produce positive stock-bond correlation, so bonds fail as an equity hedge; in March 2026 bonds sold off as much as equities.  #mech/cycle_persistence _(time-bound view)_
  > we're going to see correlation between bonds and equity being positive rather than negative
  indicator: stock-bond correlation · asset: multi · horizon: months · conditions: inflation-driven shocks · testable: yes · confidence: high
  ^MT168-C04-2
- **Niels Kaastrup-Larsen** Niels notes apparent trading in oil and equities just ahead of policy announcements (S&P selling off, then rallying before a Trump statement), suggesting event-driven reversals can be front-run and are hard for a rules-based process to anticipate; both speakers defer the market-manipulation topic.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > You should of course do like all the people in oil that apparently traded 10 minutes before the announcement.
  indicator: price moves just before announcements · asset: multi · horizon: days · conditions: geopolitical and policy headline events, March 2026 · testable: partly - event study of pre-announcement returns · confidence: low
  ^MT168-C04-X3

### C05
- **Niels Kaastrup-Larsen** Institutional investors ask whether March 2026 is a 2022 repeat; CTAs only lose less than bonds in surprises and cannot claim protection.  #mech/cycle_persistence _(time-bound view)_
  > could this be the beginning of another 2022 scenario?
  asset: multi · horizon: months · testable: no - speculative · confidence: low
  ^MT168-C05-1
- **Yoav Git** Weak 2-year US auction and Western fiscal stress suggest inflation is a way to erode debt, making higher yields near-inevitable though timing is unknowable.  #mech/fiscal_debt _(time-bound view)_
  > the weakness in the two-year bond auction recently um, in the US government
  indicator: 2-year Treasury auction · asset: rates · direction: yields higher · horizon: years · conditions: timing unknown · testable: partly · confidence: medium
  ^MT168-C05-2
- **Yoav Git** US rates have been choppy since 2023 (2022 was a clean short), making fixed-income trend trading difficult as moves reverse violently within the month.  #mech/slow_reaction _(time-bound view)_
  > the inability to decide for the markets to decide which way it's going um, since 2023.
  indicator: US rates trend · asset: rates · horizon: years · testable: yes · confidence: medium
  ^MT168-C05-3

### C06
- **Niels Kaastrup-Larsen** Private credit funds are gating on redemptions, adding fragility.  #mech/liquidity_flows _(time-bound view)_
  > private credit um is under attack. You've seen cracks. You've seen some funds beginning to gate
  indicator: private credit fund redemptions · asset: credit · horizon: months · testable: partly · confidence: medium
  ^MT168-C06-1
- **Niels Kaastrup-Larsen** Energy shocks can be supply availability (rationing) rather than price, affecting activity; Europe and Egypt show vulnerability.  #mech/structural_shift _(time-bound view)_
  > it's not necessarily just price. It's actually supply.
  indicator: oil and gas supply · asset: commodities · horizon: months · testable: no · confidence: low
  ^MT168-C06-2
- **Niels Kaastrup-Larsen** Trend barometer 52 (44 markets); BTOP50 -2.25%, SG CTA -2%, SG Trend -2.6%, short-term index about flat; MSCI World -6% in March, bonds -2%, S&P 500 -4.6% in March.  #mech/new _(time-bound view)_
  > my trend barometer is actually still in a relatively strong level at 52.
  indicator: trend barometer, CTA indices · asset: multi · horizon: weeks · testable: yes - index data · confidence: high
  ^MT168-C06-3

### C07
- **Yoav Git** Back-of-curve oil trading reflects fundamental supply and demand and is insulated from news-cycle shocks (weather vs climate).  #mech/structural_shift
  > the way he likes to talk about it is weather versus climate.
  indicator: back-end oil curve · asset: commodities · horizon: months · testable: partly · confidence: medium
  ^MT168-C07-1
- **Yoav Git** Energy has about 6% direct weight in inflation, with secondary effects via food and manufacturing, so the oil curve informs the inflation curve.  #mech/structural_shift
  > oil features uh energy features about 6% into the inflation uh directly as a component into into inflation.
  indicator: energy weight in CPI · asset: commodities · horizon: months · testable: yes · confidence: medium
  ^MT168-C07-2

### C08
- **Yoav Git** In a crisis CTAs scale all positions (longs and shorts) down per market, which is costly when EM spreads widen to about 10 bp; discretionary managers instead close the liquid duration exposure.  #mech/risk_management
  > normal CTAs, the the way we would normally manage risk is say, well, the volatility has spiked, and we would sell everything.
  indicator: position scaling rule · asset: rates · horizon: days · testable: yes - cost analysis · confidence: medium
  ^MT168-C08-1
- **Yoav Git** When correlations spike assets become substitutes, so selling Treasury futures hedges the common first factor as effectively as shrinking the whole book.  #mech/risk_management
  > hedging with the TY with the US Treasuries very quickly is actually as effective as you would do then just shrinking your entire portfolios
  indicator: common duration factor, TY futures · asset: rates · direction: short TY futures to hedge directional rates risk · horizon: days · conditions: needs correlation spike · testable: yes · confidence: medium
  ^MT168-C08-2

### C09
- **Niels Kaastrup-Larsen** Core-market (highly liquid futures) CTAs can cut duration cheaply in stress; alternative-market CTAs face higher costs, a difference hidden in monthly performance.  #mech/liquidity_flows
  > the difference between which market universe you put
  indicator: market universe liquidity · asset: multi · horizon: weeks · conditions: stress periods · testable: yes · confidence: medium
  ^MT168-C09-1
- **Yoav Git** Closing a long-short book in the stress cost about 5% of performance in alternative markets, so crisis de-risking is expensive.  #mech/risk_management _(time-bound view)_
  > let's say closing closing the book the long short book is like 5% of performance.
  indicator: closing cost · asset: rates · horizon: days · testable: yes · confidence: medium
  **Correction (cross-check):** Presented as an observed fact. Yoav gave the 5% as an illustrative figure ('let's say') for the cost of closing a long-short alternative-markets book and said he does not have a solution. → Illustratively, closing out a long-short book in alternative markets in stress could cost on the order of 5% of performance, so crisis de-risking there is expensive.
  ^MT168-C09-2
- **Yoav Git** Factor-based risk management: in crises the first (rates) factor dominates volatility, so manage factor risk directly while limiting specific risk per market.  #mech/risk_management
  > in times of crisis you have the first factor which has become very which is which is correlated and its volatility is dominate is dominating everything else.
  indicator: first principal component of portfolio risk · asset: multi · direction: reduce first-factor risk · horizon: days · conditions: optimisation problem · testable: yes - PCA risk · confidence: medium
  ^MT168-C09-3

### C10
- **Niels Kaastrup-Larsen** Keeping illiquid positions while hedging with futures is risky because in a liquidity crisis correlations go to one and exits close.  #mech/liquidity_flows
  > in a liquidity crisis yeah correlations may go to one but you can't get out.
  asset: multi · horizon: days · testable: partly · confidence: medium
  ^MT168-C10-1
- **Yoav Git** Crisis flow sequence: price gaps on the weekend news, CTAs cut risk as volatility gaps, equities and bonds both sell off.  #mech/liquidity_flows _(time-bound view)_
  > CTA flows coming in of course volatility as we discussed volatility is gapping we will start taking risk off.
  indicator: CTA flow · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT168-C10-2
- **Yoav Git** Hedging the common first factor while limiting specific risk per market is a constrained optimisation problem that is probably not worth the effort for a liquid-market CTA, which can simply scale the whole book down.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > certainly in the case of like liquid CTA probably not worth the hassle. You would just basically down gear everything
  indicator: factor-based risk reduction vs uniform down-gearing · asset: multi · horizon: days · conditions: liquid core markets where scaling down is cheap · testable: yes - compare crisis de-risking cost and outcome of both methods · confidence: medium
  ^MT168-C10-X4

### C11
- **Yoav Git** Next in the sequence, value traders holding falling bonds are closed out (long squeeze), then real money buys on stabilisation, then renewed selling after escalation (gilt and Treasury squeezes).  #mech/liquidity_flows _(time-bound view)_
  > suppose I'm a I'm a value trader and I'm I believe in bonds and I'm holding bonds and I'm holding bonds and bond it keeps ticking down
  indicator: value-trader forced selling · asset: rates · horizon: days · conditions: stress · testable: partly · confidence: medium
  ^MT168-C11-1
- **Yoav Git** Discretionary traders watch flows closely while CTAs pay almost none, yet CTAs feature in flow models as one of three player types.  #mech/research_method
  > CTAs in general pay almost next to no attention to flows
  asset: multi · testable: partly · confidence: medium
  ^MT168-C11-2

### C12
- **Yoav Git** Paper conclusion: most volatility is noise; the efficient market hypothesis can hold either because price is right (Shiller) or because there is no true price.  #mech/research_method
  > the vast majority of volatility is is sort of noise.
  indicator: excess volatility · asset: multi · testable: yes · confidence: medium
  ^MT168-C12-1
- **Yoav Git** Flow models use three players: value traders (revert to target price), noise traders (inject volatility), and trend followers (trade first derivative, returns).  #mech/liquidity_flows
  > The player number one is the Shiller player, the fundamental player.
  indicator: value/noise/trend agent model · asset: multi · testable: yes - calibrate · confidence: high
  ^MT168-C12-2
- **Yoav Git** If everyone were a Shiller-style value trader prices would jump to the equilibrium and then barely trade, so observed volatility and trading volume far exceed what pure value investing implies (the excess-volatility puzzle), which motivates flow-based models with noise and trend players.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > The problem with this world view is that markets are a lot noisier than what what we would get if everybody would be like that.
  indicator: excess volatility vs value-trader equilibrium · asset: multi · testable: yes - variance-ratio and volatility bound tests · confidence: high
  ^MT168-C12-X5

### C13
- **Yoav Git** EM-algorithm calibration of the model shows noise is the first order of volatility, value traders second, and trend followers negligible; CTAs create little autocorrelation because footprints are small.  #mech/research_method
  > by the way, CTAs or we do not contribute that much to the volatility.
  indicator: autocorrelation of returns · asset: multi · testable: yes - paper result · confidence: medium
  ^MT168-C13-1
- **Yoav Git** Pendulum picture: trend followers dominate through the centre, value traders dominate at extremes, so markets spend time over- or underpriced.  #mech/overshoot
  > the market is either spent a lot of the time being underpriced or overpriced rather than in the center.
  indicator: pendulum dynamics · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT168-C13-2

### C14
- **Yoav Git** Critique: prices gap on news without trading (nonfarm payroll, weekend Iran attack), so explaining all volatility by trading flows ignores genuine jumps in fundamental value.  #mech/structural_shift
  > half an hour before nonfarm payroll, nobody wants to trade.
  indicator: jumps, nonfarm payroll liquidity · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT168-C14-1

### C15
- **Yoav Git** Critique: assuming a cubic value-trader response (unbounded) is unrealistic because value traders face risk limits too; the paper uses monthly data so cannot inform daily trading.  #mech/research_method
  > Value traders gets get called out just as much as trend followers in terms of risk management.
  indicator: response function · asset: multi · testable: yes · confidence: medium
  ^MT168-C15-1
- **Yoav Git** Capacity limits risk per market so footprint stays unwindable; larger AUM pushes risk into the biggest markets.  #mech/risk_management
  > the amount of risk that we like to put into each market is limited precisely for the same discussion that we had that we don't want to trade against ourselves
  indicator: capacity per market · asset: multi · testable: yes · confidence: high
  ^MT168-C15-2

### C16
- **Yoav Git** CTA return is diversification times average market Sharpe; if markets are highly correlated, trading only big markets costs little, but if you select low-correlation markets, capacity pushes risk into big markets and cuts effective breadth.  #mech/risk_management
  > the way CTAs make money is the diversification times the average market shop.
  indicator: market correlation, diversification · asset: multi · conditions: depends on correlation of the universe · testable: yes · confidence: medium
  ^MT168-C16-1
- **Yoav Git** Replicating the CTA index at 80% correlation is accepted while S&P replication demands 99%, because CTA constituents are opaque.  #mech/research_method
  > you have a 80% correlation and people think, "Oh, that's great.
  indicator: index replication correlation · asset: multi · testable: yes · confidence: medium
  ^MT168-C16-2
- **Niels Kaastrup-Larsen** Niels argues that although in theory few large markets should replicate a CTA index, in practice replicators' correlation to the index is modest and tracking error substantial.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > when you look at the numbers, that correlation isn't that great. I mean, the tracking error is substantial
  indicator: tracking error / correlation of replicators to CTA index · asset: multi · horizon: years · conditions: index replication with a small liquid universe · testable: yes - correlation and tracking error of replicator products · confidence: medium
  ^MT168-C16-X6

