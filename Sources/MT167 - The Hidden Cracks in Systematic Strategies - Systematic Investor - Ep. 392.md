---
source_id: MT167
title: "The Hidden Cracks in Systematic Strategies - Systematic Investor - Ep. 392"
date: 2026-03-22
channel: "Top Traders Unplugged"
url: 
words: 11836
claims: 51
added_by_crosscheck: 14
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Niels Kaastrup-Larsen (host, hedge fund manager)", "Nick Baltas (co-host, QIS / systematic strategies practitioner)"]
tags: [source, layer0]
---
# The Hidden Cracks in Systematic Strategies - Systematic Investor - Ep. 392

**Speakers:** Niels Kaastrup-Larsen (host, hedge fund manager); Nick Baltas (co-host, QIS / systematic strategies practitioner)

**Summary:** March 2026 update: oil and gas backwardation hit commodity curve carry; faster trend speeds outperformed slower ones; Middle East shock raises stagflation risk. Discusses zero-DTE options and trend following, three Man Group papers (optimal market mix, agentic AI research workflow, quant equity renaissance), and certainty (Fed put) vs uncertainty for trends.

**Approach:** trend following, QIS, commodity curve carry, market universe, options gamma, AI research workflow, quant equity factors, stagflation

**Cross-check completeness estimate of first read:** 0.80 - the first reader caught the headline themes (curve carry, QIS, gas vs oil, speed, 0DTE, Man papers, certainty vs uncertainty); missed some causal reasoning (curve-carry risk premium and origin, recession defensiveness, factor macro-sensitivity stats, regime model, 2010s trend winter cause, pinning) and mangled the index-numbers claim.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro; Bloomberg CTA drawdown headline; QIS topic |
| C02 | 3 | commodity curve carry hit by backwardation in gas and oil; QIS size |
| C03 | 3 | gas vs oil dynamics, low correlation, portfolio construction |
| C04 | 4 | trend following captured oil via vol scaling; pod shops attrition; Fed stagflation comments |
| C05 | 3 | stagflation risk, 2022 memories, Gulf tourism aftermath; March trend update |
| C06 | 2 | faster speeds outperform slower; commodities as driver; commodity share of universe |
| C07 | 2 | commodity risk budget and asset-class tagging; trend barometer and index numbers; reader question set-up |
| C08 | 2 | zero-DTE options volume; dealer gamma and trend vs mean reversion |
| C09 | 2 | options use for risk management; dealers long gamma; short-term strategies struggle |
| C10 | 2 | why options data is not needed for 3-24 month trends; test what you trade |
| C11 | 3 | Man paper on optimal market mix; duality of trend following |
| C12 | 3 | core universe maximises crisis alpha; broad universe maximises Sharpe |
| C13 | 1 | cash efficiency; 900 markets; equity factors not diversifying |
| C14 | 2 | Man paper on agentic AI trend research |
| C15 | 1 | AI supervision, hallucination example; quant equity paper start |
| C16 | 2 | quant winter causes; dynamic allocation; new data; signal correlations |
| C17 | 1 | trend winter in 2010s; certainty vs uncertainty and the Fed put; outro |

## Claims

### C01
- **Niels Kaastrup-Larsen** Bloomberg headlined a CTA drawdown (trend index 'down 4%', actually about -2% in March) after 8 consecutive positive months, showing how little correction triggers headlines.  #mech/behavioral _(time-bound view)_
  > worst drawdown since liberation day
  indicator: Trend Index · asset: multi · horizon: months · testable: yes - index data · confidence: medium
  ^MT167-C01-1

### C02
- **Nick Baltas** Commodity curve carry (long back, short front) lost years of performance in Q1 2026 from back-to-back backwardation shocks in gas (cold weather) and oil (Middle East supply concerns).  #mech/risk_premium _(time-bound view)_
  > the classic short commodity spread, the curve carry
  indicator: commodity curve carry (long back end, short front) · asset: commodities · direction: short front / long back of commodity curves · horizon: months · conditions: loses when supply shock is large; mean reverts if shock not permanent · testable: yes - curve carry backtests · confidence: high
  ^MT167-C02-1
- **Nick Baltas** Backwardation mean-reverts quickly unless the supply shock is permanent, so curve-carry losses recover mark-to-market when curves normalise.  #mech/overshoot _(time-bound view)_
  > unless um you know, the supply shock is permanent, uh mean reverts very quickly
  indicator: commodity curve slope · asset: commodities · direction: curve carry recovers after normalisation · horizon: weeks · conditions: not if supply shock permanent · testable: yes · confidence: medium
  ^MT167-C02-2
- **Nick Baltas** QIS (quantitative investment strategies) market size is estimated at USD 600-700 billion, multi-asset and spanning retail and institutional products.  #mech/crowding_positioning _(time-bound view)_
  > it is probably now on the 6 to 700 billion mark
  indicator: QIS AUM · asset: multi · testable: partly - industry estimate · confidence: low
  ^MT167-C02-3
- **Nick Baltas** Commodity curve carry (long the back end, short the front) has historically been rewarded because it earns a risk premium shared between commodity consumers and producers, which is why its drawdowns tend to be temporary unless the supply shock is permanent.  #mech/risk_premium _(added by sonnet-xhigh cross-check)_
  > that historically has been well rewarded because that that is the risk premium that is shared between consumers and and and producers
  indicator: commodity futures curve carry (back vs front) · asset: commodities · direction: long deferred contracts, short front contracts · horizon: years · conditions: fails when backwardation persists, e.g. supply shock or weather shock · testable: yes - curve-carry returns across commodities · confidence: high
  ^MT167-C02-X1

### C03
- **Niels Kaastrup-Larsen** Natural gas pricing depends heavily on transportation cost while oil does not, so gas and oil react to different shocks.  #mech/structural_shift _(time-bound view)_
  > the person explained it's very different dynamics that drives those two
  indicator: nat gas vs oil · asset: commodities · testable: partly · confidence: low
  ^MT167-C03-1
- **Nick Baltas** Gas and oil have near-zero statistical correlation; oil complex is homogeneous, gas is the most volatile with a right-skewed tail, so clustering and vol scaling in portfolios matter.  #mech/risk_management
  > there's pretty much zero. Like there's very little correlation between the gases and the oil complex.
  indicator: correlation nat gas vs oil · asset: commodities · testable: yes - correlation calc · confidence: medium
  ^MT167-C03-2
- **Nick Baltas** Commodity index weights by production and liquidity ignore volatility, so risk exposure to volatile markets exceeds the notional weight.  #mech/risk_management
  > it doesn't account for volatility so then you end up being exposed in risk terms more than what your notional exposure suggests
  indicator: commodity index weights · asset: commodities · testable: yes · confidence: medium
  ^MT167-C03-3
- **Nick Baltas** Long-only systematic commodity exposure rolled at the front suffers negative roll yield, so QIS designers moved to the back of the curve and then shorted the front, which is how the commodity curve-carry strategy originated.  #mech/risk_premium _(added by sonnet-xhigh cross-check)_
  > then you realize that doing it on the front has a negative roll yield. You do it on the back end of the curve, you realize you have some alpha, you short the front, here's your curve.
  indicator: roll yield of front vs back contracts · asset: commodities · direction: long back / short front of commodity curve · horizon: years · conditions: contango markets; rolling by futures replaces physical holding · testable: yes - roll yield by contract maturity · confidence: high
  ^MT167-C03-X2
- **Nick Baltas** Oil can be hit by both a supply shock (price up) and a macro demand shock (price down), so its tails are bidirectional, whereas natural gas is driven by winter weather and is more right-skewed, so the two need different risk treatment.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > there is a supply shock as it currently is the case, but also there's a macro shock that can drive
  indicator: oil vs natural gas return distribution skew · asset: commodities · direction: oil two-sided fat tails; gas right tail · horizon: months · conditions: geopolitical supply shock vs recession-driven demand collapse · testable: yes - return skewness of oil vs gas · confidence: medium
  ^MT167-C03-X3

### C04
- **Nick Baltas** Trend following with volatility scaling captured the oil move yet automatically reduced risk as volatility spiked.  #mech/risk_management _(time-bound view)_
  > given the rise in the volatility it is reducing risk exposure precisely because yes it might be spiking but it's spiking so aggressively
  indicator: volatility-scaled trend · asset: commodities · horizon: weeks · testable: yes · confidence: medium
  ^MT167-C04-1
- **Nick Baltas** Multi-strategy diversification in commodity systematics (trend, skew, value) paid off year to date as skew and value benefited from the petroleum rally.  #mech/risk_management _(time-bound view)_
  > the skew or value dynamics that we have discussed here you know have been benefiting
  indicator: commodity skew and value signals · asset: commodities · horizon: months · testable: partly · confidence: medium
  ^MT167-C04-2
- **Niels Kaastrup-Larsen** Bloomberg/Goldman data: share of pod-shop traders leaving to set up their own firms rose from 9% (2023) to 12% (2024) and 17% (2025), with fewer investors planning to raise allocations.  #mech/crowding_positioning _(time-bound view)_
  > in 23 according to their numbers the numbers quoted in the article 9% of people would set up their own would leave and set up their own in 24 it's 12% and in 25 it was 17%
  indicator: pod shop trader attrition · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT167-C04-3
- **Niels Kaastrup-Larsen** Powell distinguishes today from 1970s stagflation by unemployment levels, but rates have moved higher and cuts the White House wants may not come.  #mech/policy_reaction _(time-bound view)_
  > Powell kind of does not really think we're we're we're in a stagflationary environment just yet
  indicator: stagflation, Fed funds · asset: rates · direction: higher rates · horizon: months · testable: partly · confidence: medium
  ^MT167-C04-4

### C05
- **Nick Baltas** Oil shocks feed inflation nowcasts, memories of 2022 return, and stagflation risk is judged elevated versus two months earlier; the key unknown is whether the oil shock is permanent.  #mech/policy_reaction _(time-bound view)_
  > inflation volatility is back the question as to how central banks will act or react to the current situation is here
  indicator: oil price, inflation nowcast · asset: multi · direction: stagflation risk higher · horizon: months · conditions: depends on escalation of Middle East conflict · testable: partly · confidence: medium
  ^MT167-C05-1
- **Niels Kaastrup-Larsen** After-effects of conflict on Gulf tourism and activity may be more damaging than higher oil prices alone.  #mech/structural_shift _(time-bound view)_
  > are you likely to say to suggest another holiday in in in some of those countries even if the war stops
  indicator: Gulf tourism · asset: other · horizon: years · testable: no - speculative · confidence: low
  ^MT167-C05-2
- **Niels Kaastrup-Larsen** March 2026 corrections in equities, bonds and precious metals after eight straight positive industry months; precious metals may be sold to raise cash.  #mech/liquidity_flows _(time-bound view)_
  > selling off bonds markets have been selling off precious metals quite severely actually in some of the markets where maybe it's an easy way for people to raise cash
  asset: multi · horizon: weeks · testable: partly · confidence: low
  ^MT167-C05-3

### C06
- **Nick Baltas** In March 2026 faster trend speeds outperformed slower ones, the mirror image of the prior years when slower speeds better navigated V-shapes.  #mech/slow_reaction _(time-bound view)_
  > faster speeds at the moment are substantially outperforming slower speeds
  indicator: trend speed dispersion · asset: multi · horizon: weeks · conditions: V-shaped reversals favour fast; sustained trends favour slow · testable: yes - speed split P&L · confidence: medium
  ^MT167-C06-1
- **Nick Baltas** Typical QIS trend books hold 10-40 commodities out of 20-60 markets, with commodities around a quarter of risk.  #mech/risk_management
  > something like a big commodity universe maybe tilted more towards the liquid markets or 15 to 20 is a reasonable number.
  indicator: commodity risk share · asset: commodities · testable: partly - industry survey · confidence: low
  ^MT167-C06-2
- **Nick Baltas** In March 2026 trend P&L was roughly flat: the oil complex (heating oil, gasoil, Brent) and short rates positions were positive while equities were hit, which Nick sees as a statistical non-event for trend following.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > commodities have been the big driver of performance here and to your point it's it's the oil complex so literally from heating oil gas oil brand
  indicator: trend P&L attribution by sector, March 2026 · asset: multi · direction: long oil complex, short rates positive; equities negative · horizon: months · conditions: month-to-date snapshot · testable: yes - sector attribution of trend index · confidence: medium
  ^MT167-C06-X4

### C07
- **Nick Baltas** Philosophical divergence: treating energy, metals and ags as separate asset classes (seven in total) rather than one commodity class gives commodities a higher risk budget because intra-commodity correlation is lower than within equities.  #mech/risk_management
  > instead of having four asset classes, you have seven, but three of them span the universe of commodities.
  indicator: asset-class tagging and cluster risk budgets · asset: commodities · testable: yes - correlation clusters · confidence: medium
  ^MT167-C07-1
- **Nick Baltas** Trend barometer at 45 (neutral); SG CTA -1.38% in March (+6.82% YTD), short-term trend index +3.55% YTD; MSCI World -4.64% in March and ~-1.3% YTD; S&P 500 TR down about 3% YTD; bonds offered no diversification.  #mech/new _(time-bound view)_
  > my trend barometer finished at 45 uh last night. So that's kind of neutral.
  indicator: trend barometer, SG CTA, MSCI World · asset: multi · horizon: weeks · testable: yes - published index data · confidence: high
  **Correction (cross-check):** Series mislabelled and incomplete. The transcript (garbled) gives: an 'SG 6 index' [likely CTA index] -1.38% March / +6.82% YTD; a 'short-term trend' series -1.77% March / +6.87% YTD (likely SG Trend index); and the short-term traders index -0.25% March / +3.55% YTD. The +3.55% belongs to the short-term traders index, and MSCI World YTD is garbled ('three 1.34%') so -1.3% is uncertain. US Aggregate bonds were -1.5% in March and +0.17% YTD. → Trend barometer 45 (neutral). Early March 2026: SG CTA-type index -1.38% month / +6.82% YTD; trend series -1.77% / +6.87%; short-term traders index -0.25% / +3.55% YTD (still better in March); MSCI World -4.64% in March (YTD figure garbled); US Agg -1.5% March / +0.17% YTD; S&P 500 TR -3.61% March / about -3% YTD.
  ^MT167-C07-2
- **Niels Kaastrup-Larsen** Since 2023 trend returns have been driven by commodity trends (cocoa, then coffee and live cattle, later precious metals and oil), so the share of commodities in a trend universe has had a large effect on recent results.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > ever since 2023 when cocoa started sort of making noises uh in the portfolio and then came coffee and live cattle and all of that stuff
  indicator: commodity contribution to trend returns since 2023 · asset: commodities · horizon: years · conditions: recent regime of strong commodity trends · testable: yes - contribution analysis of commodity vs financial sectors · confidence: medium
  ^MT167-C07-X5

### C08
- **Nick Baltas** About 60% of S&P options volume is zero-DTE and more than half of that is retail, democratising cheap intraday leverage.  #mech/crowding_positioning _(time-bound view)_
  > currently the volume in S&P options um 60% of it is zero DTs and 40 is anything from daily up to you know, longer-term tenors.
  indicator: zero-DTE share of S&P options volume · asset: equities · testable: yes - exchange data · confidence: high
  ^MT167-C08-1
- **Nick Baltas** Dealer gamma hedging: when investors sell options dealers are long gamma, buy dips and sell rallies, forcing mean reversion; negative gamma (e.g. leveraged ETFs) forces buy high / sell low and exacerbates trends.  #mech/liquidity_flows
  > selling out of the money options you know, to generate some carry for instance, then dealers would typically be like you know, long gamma
  indicator: dealer gamma exposure · asset: equities · horizon: days · conditions: long gamma dampens trends; short gamma amplifies · testable: yes - gamma data vs trend returns · confidence: medium
  ^MT167-C08-2

### C09
- **Nick Baltas** Study (Vilkov et al., 0DTE) finds dealers net long gamma, implying intraday reversals rather than trends, possibly explaining weak short-term trend performance recently.  #mech/liquidity_flows _(time-bound view)_
  > dealers are typically more long gamma than short gamma, and therefore, there is an argument to be made that short-term reversions have become more prevalent than than than than intraday trends
  indicator: dealer gamma, intraday returns · asset: equities · direction: short-term trend underperforms · horizon: days · testable: yes · confidence: medium
  **Correction (cross-check):** Attribution overstated. Nick hedged that he might misrepresent the paper and said the dealer-long-gamma finding supports more short-term reversals than intraday trends; the link to weak short-term trend performance was Niels's own suggestion, with Nick saying 0DTE is 'certainly a force' but not that it is proven. → A study (attributed with hedging to Greg Vilkov and co-authors) finds dealers are typically more long gamma than short gamma, implying more intraday reversals than trends; Niels then suggests this may help explain weak short-term trend results recently, which Nick treats as plausible but unproven.
  ^MT167-C09-1
- **Nick Baltas** Zero-DTE options could be used as cheap intraday protection for long-term trend positions without cutting the underlying exposure.  #mech/risk_management
  > premium to be spent on a zero DT option to just cover that exposure
  indicator: zero-DTE puts overlay · asset: equities · direction: buy short-dated puts against long equity trend · horizon: days · conditions: at a premium cost · testable: yes - overlay backtest · confidence: low
  ^MT167-C09-2
- **Nick Baltas** Dealer-gamma and option-flow distortions matter mainly for short-term trend managers; for long-term managers a near-zero signal already means small exposure, so the signal measurement probably does not need to change.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > if your signal is very close to zero, anyway, your risk exposure would be small, to be honest with you
  indicator: trend signal strength (near zero) · asset: equities · horizon: weeks · conditions: long-horizon trend signals; shorter horizons more exposed to option-driven mean reversion · testable: partly - compare short vs long lookback performance in 0DTE era · confidence: medium
  ^MT167-C09-X6
- **Nick Baltas** On option expiry dates large open interest creates a gravitational pull ('pinning') of price toward the strike, which can distort measured price signals around expiries, although the effect on medium-term trend followers is unclear.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > power towards the you know, the strike price that um that the open interest is large
  indicator: option open interest by strike on expiry days · asset: equities · direction: price pinned toward high-open-interest strike · horizon: days · conditions: expiry days; matters mostly for short-term signals · testable: yes - price behaviour near expiry vs open interest · confidence: low
  ^MT167-C09-X7
- **Niels Kaastrup-Larsen** Niels offers a second possible cause for recent weak short-term trend results: multi-manager pod shops adding convergent, mean-reverting flow alongside the 0DTE options complex; he states he does not know.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check, time-bound view)_
  > Could also be the pod shops, uh but they're probably also part of maybe the zero DTA options market, I have no idea.
  indicator: short-term trend performance vs pod-shop activity · asset: multi · direction: short-term trend weaker · horizon: months · conditions: recent period · testable: partly - hard to attribute to pod flows · confidence: low
  ^MT167-C09-X8

### C10
- **Niels Kaastrup-Larsen** Option volume data (single-day bets) is irrelevant for 3-24 month trends; trend models are built and tested on futures data so should trade futures.  #mech/research_method
  > you test what you trade and you trade what you test, right?
  indicator: futures price data · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT167-C10-1
- **Nick Baltas** Option-implied information such as skew might serve as a sentiment filter or multiplier on trend signals; smoothing already absorbs whipsaws indirectly.  #mech/behavioral
  > option implied information, like you know, skew, um providing some sort of sentiment indicator
  indicator: option skew · asset: equities · horizon: months · testable: yes - test skew overlay · confidence: low
  ^MT167-C10-2

### C11
- **Nick Baltas** Man Group paper links objective to universe: choose universe and speed to match whether you want defensiveness or return.  #mech/research_method
  > the point of you want to be defensive, this is the universe to do it with.
  indicator: market universe · asset: multi · testable: yes · confidence: medium
  ^MT167-C11-1
- **Nick Baltas** Managed futures has a duality of objectives: long-term positive return plus crisis alpha; commodity curve and rate volatility are other such strategies.  #mech/risk_premium
  > it's one of the very few systematic strategies that deliver long-term positive returns and kind of downside protection
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT167-C11-2
- **Nick Baltas** In a crisis, correlations go to extremes and principal components drive returns, so a core liquid universe maximises crisis alpha.  #mech/risk_management
  > when you have a massive correction, it is not that assets fall, it is principal components that are falling.
  indicator: principal components of asset returns · asset: multi · direction: long bonds, short equities · horizon: weeks · testable: yes · confidence: medium
  ^MT167-C11-3
- **Nick Baltas** Commodity curve carry is defensive in a non-inflationary recession because it is short the front of commodity curves, which is why Nick lists it with trend following and rate volatility as a rare strategy combining positive long-term return with crisis alpha.  #mech/risk_premium _(added by sonnet-xhigh cross-check)_
  > So, in a non-inflationary recession, it actually performs well.
  indicator: commodity curve carry in recessions · asset: commodities · direction: short front of curve profits as commodity demand falls · horizon: months · conditions: non-inflationary recession; fails in supply-shock backwardation · testable: yes - curve-carry returns in recession regimes · confidence: medium
  ^MT167-C11-X9

### C12
- **Nick Baltas** Core universe maximises crisis alpha; broader universe (alternative commodities, EM equities, factors) maximises long-term Sharpe via independent bets but is less defensive.  #mech/risk_premium
  > this expansion of the universe, by design, brings idiosyncratic risk that, with the assumption of trendiness, would provide longer-term diversification and therefore return and therefore maximum long-term sharp ratio is achieved with a broader universe
  indicator: market universe breadth · asset: multi · horizon: years · conditions: tradeoff between defence and long-term Sharpe · testable: yes - Man paper results · confidence: medium
  ^MT167-C12-1
- **Nick Baltas** Crisis protection had been attributed to speed; the paper shifts attention to market universe as the driver of defensiveness.  #mech/research_method
  > I plead guilty that, you know, I was all always going back to the speed discussion
  asset: multi · testable: partly · confidence: medium
  ^MT167-C12-2
- **Nick Baltas** Cash-efficient trend portfolios (low margin per unit of risk) resemble the max-crisis-alpha core liquid universe, so objectives converge.  #mech/risk_management
  > the lower that margin is, the more capital efficient the portfolio can be
  indicator: margin requirement · asset: multi · testable: yes · confidence: medium
  ^MT167-C12-3

### C13
- **Niels Kaastrup-Larsen** The Man paper identifies roughly 900 tradable markets including 60 equity factors; Nick doubts the 60 factors are diversifying since five or six factors explain the equity cross-section.  #mech/research_method
  > there are approximately 900 different markets we could trade
  indicator: number of markets, equity factors · asset: multi · testable: yes · confidence: medium
  ^MT167-C13-1

### C14
- **Nick Baltas** Man paper on agentic AI: an agent can rediscover a hidden feature of a breakout signal, but human judgment is needed to frame questions and guard against multiple testing and overfitting; different LLMs give different outcomes.  #mech/research_method
  > extremely extremely important not just from how you frame the questions and how you guide the process and how you interpret the results but also kind of guarding safeguarding against multiple testing, overfitting
  indicator: LLM-driven signal research · asset: multi · testable: yes · confidence: medium
  ^MT167-C14-1
- **Nick Baltas** LLM answer to the trend-following YTD question was wrong ('mixed') when Jan-Feb 2026 were among the best starts; AI output needs supervision, especially for policyholder money.  #mech/research_method _(time-bound view)_
  > How has the first two months of the year been for trend following of all things?
  asset: multi · testable: yes · confidence: high
  ^MT167-C14-2
- **Nick Baltas** Because a systematic pipeline (data, signal, risk, optimiser, liquidity and vol targets) is deterministic, task-specific AI agents narrow in scope but deep in analysis can be run under a supervisor, unlike broad, shallow chatbots.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > So very narrow in terms of scope but very deep in terms of uh in terms of analysis.
  asset: multi · conditions: needs human supervision and multiple-testing safeguards · testable: no - qualitative · confidence: medium
  ^MT167-C14-X10

### C15
- **Niels Kaastrup-Larsen** Building trend systems rewards simplification; AI tends to expand, which may be incompatible with cleaning signals.  #mech/research_method
  > actually the skill and and the experience goes towards actually stripping things down so you get the the cleanest signal, less noise
  asset: multi · testable: no - opinion · confidence: low
  ^MT167-C15-1
- **Nick Baltas** After the 2018-20 quant winter, multi-strategy quant equity long/short strategies recovered strongly post-COVID, motivating the question of whether a repeat is likely.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > post COVID significant resurrection. So the multi strategy quant equity, the long short space has had very strong performance.
  indicator: multi-strategy quant equity long/short performance · asset: equities · horizon: years · conditions: post-2020 regime · testable: yes - factor and quant-equity index returns · confidence: medium
  ^MT167-C15-X11

### C16
- **Nick Baltas** Quant winter 2018-20 had two causes: macro regime (rates) hurting value and momentum, and factor crowding causing forced unwinds and fire sales.  #mech/crowding_positioning
  > One was that the macro regime was not very accommodative for some of the factors
  indicator: equity factors · asset: equities · horizon: years · conditions: macro factors explain more than 50% of factor return variation in stress vs about 20% normally · testable: yes · confidence: medium
  ^MT167-C16-1
- **Nick Baltas** Quant equity paper: new data (geolocation, card, patents, sentiment) lowered alpha-model correlations from 70-80% to 40-50% and dynamic factor allocation adds regime resilience.  #mech/structural_shift
  > alpha models back in the days, um you know, would have um correlations of like, you know, uh 70 to 80%. These days more like, you know, 40 to 50.
  indicator: alpha model correlation, regime model · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT167-C16-2
- **Nick Baltas** In stress periods classical macro factors explain over 50% of equity factor return variation versus about 20% in normal times, so factor books become macro-dependent exactly when crowding unwinds.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check)_
  > classical macro factors can explain more than 50% of factor return variation which is quite substantial if you were to think that in a normal times it's more like you know 20%
  indicator: share of factor return variance explained by macro factors · asset: equities · horizon: months · conditions: stress periods vs normal times · testable: yes - R-squared of factor returns on macro factors by regime · confidence: high
  ^MT167-C16-X12
- **Nick Baltas** The Man quant-equity paper uses a four-regime macro model (recession, early expansion, late expansion, overheating) to explain which factor premia were rewarded in each regime and to understand the quant winter.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check)_
  > They use an internal model they have for regime identification. So no surprise you typically have kind of recession, early expansion, late expansion and then overheating.
  indicator: macro regime model: recession / early / late expansion / overheating · asset: equities · direction: factor premia vary by regime · horizon: years · conditions: regime identified by an internal model · testable: yes - factor returns conditional on regime · confidence: medium
  ^MT167-C16-X13

### C17
- **Nick Baltas** Under fundamental certainty (e.g. a Fed put) prices revert to their prior valuation; under uncertainty price trends carry information about fundamentals and continue.  #mech/behavioral
  > Certainty brings reversions. Uncertainty allows price trends to continue
  indicator: policy uncertainty · asset: multi · direction: trends stronger under uncertainty · horizon: months · testable: partly - uncertainty indices vs trend returns · confidence: medium
  ^MT167-C17-1
- **Niels Kaastrup-Larsen** The disappointing trend-following returns of the 2010s are attributed to a macro environment of low, stable inflation and little GDP movement, which gave trends little to work with; the open question is whether today's research would cope better if it recurred.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check)_
  > when you think about the macroeconomic environment, low inflation, stable inflation, uh very little movement on GDP and so on and so forth, of course um that's not necessarily the best environment.
  indicator: inflation and GDP volatility regime · asset: multi · direction: trend returns lower in stable macro regimes · horizon: years · conditions: low and stable inflation, little GDP movement · testable: yes - trend returns conditional on inflation and growth volatility · confidence: medium
  ^MT167-C17-X14

