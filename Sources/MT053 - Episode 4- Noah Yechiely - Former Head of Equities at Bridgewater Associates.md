---
source_id: MT053
title: "Episode 4- Noah Yechiely - Former Head of Equities at Bridgewater Associates"
date: 2024-12-27
channel: "Generating Alpha Podcast"
url: https://www.youtube.com/watch?v=JD-CkCfpHqw
words: 4479
claims: 13
added_by_opus: 4
corrections: 0
crosscheck: "opus cross-check"
speakers: ["Noah Yechiely (former head of equities, Bridgewater Associates)", "Amir and Owen (hosts, Generating Alpha podcast)"]
tags: [source, layer0]
---
# Episode 4- Noah Yechiely - Former Head of Equities at Bridgewater Associates

**Speakers:** Noah Yechiely (former head of equities, Bridgewater Associates); Amir and Owen (hosts, Generating Alpha podcast)

**Summary:** Noah Yechiely, ex-Bridgewater head of equities, on what a hedge fund is, market efficiency, strategy crowding and top-down versus bottom-up macro. Mostly career and hiring advice. Main points: markets are very efficient, public strategies decay, understand why a strategy works.

**Approach:** macro hedge fund, market efficiency, strategy decay, risk management

**Opus completeness estimate of first read:** 0.75 - short career/hiring interview; first reader caught the main ideas (uncorrelated returns, beta drift, efficiency, crowding, top-down vs bottom-up, ask why), missing the correlated-assets premise, migrating efficiency, the research-framework process and the politics-affects-all-stocks point; C05 and C07 have no claim-worthy content.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro; career; what a hedge fund is: uncorrelated returns |
| C02 | 3 | hedge fund types; drift to beta; market efficiency; niche inefficiencies |
| C03 | 3 | crowding erodes strategies; data democratisation; top-down vs bottom-up macro |
| C04 | 2 | Bridgewater investor traits (why not what), challenge own beliefs; consulting skills |
| C05 | 0 | hiring creativity and curiosity; math and science skills; no method |
| C06 | 0 | technical vs thinking skills; reading advice; understanding politics and world |
| C07 | 0 | life advice, follow your interest; nothing actionable |

## Claims

### C01
- **Noah Yechiely** A true hedge fund aims for returns uncorrelated with the market, which helps a portfolio because the stream rises when other assets fall; many so-called hedge funds are simply long-only.  #mech/risk_management
  > primary objective is um producing return that is uncorrelated
  indicator: correlation of fund returns with market · asset: multi · direction: add uncorrelated return stream to portfolio · conditions: Benefit appears when other assets are falling · testable: yes - correlation of fund returns to market is measurable · confidence: high
  ^MT053-C01-1
- **Noah Yechiely** Long-only assets tend to rise over time as payment for providing capital, but they are mostly correlated with each other, so a long-only mix gives limited diversification and an uncorrelated return stream is what adds most to a portfolio.  #mech/risk_premium _(added by Opus)_
  > but all assets tends to go up and down together they are correlated
  indicator: cross-asset correlation · asset: multi · direction: long assets earn a premium over time · horizon: years · testable: yes - cross-asset correlations and long-run asset returns are measurable · confidence: high
  ^MT053-C01-X1

### C02
- **Noah Yechiely** Many hedge funds drifted into holding assets long because that earns market returns over time on which they can charge fees, so they sell beta, not unique returns.  #mech/behavioral
  > selling a beta or selling regular IR regular returns that you can get in the market and they just charge more
  indicator: hedge fund beta · asset: multi · horizon: years · conditions: Because uncorrelated return is hard to produce · testable: yes - regress hedge fund returns on market factors · confidence: high
  ^MT053-C02-1
- **Noah Yechiely** Markets are very efficient: the whole hedge fund industry earns a few billion, a few basis points on hundreds of trillions of assets, because competing smart participants make uncorrelated returns hard.  #mech/risk_premium
  > markets are very efficient it's very hard to make uh money in markets
  indicator: hedge fund industry profit relative to market size · asset: multi · testable: partly - industry-level argument, efficiency claim is general · confidence: high
  ^MT053-C02-2
- **Noah Yechiely** Good hedge funds exploit niches that are inefficient for structural reasons, but the returns and capacity there are small.  #mech/structural_shift
  > particular niches in the market that are inefficient and there are there are reasons why they would be inefficient
  asset: multi · conditions: Niche inefficiencies have small capacity · testable: partly - capacity-limited niche alpha hard to test · confidence: medium
  ^MT053-C02-3
- **Noah Yechiely** Market efficiency is not uniformly rising: some markets have become more efficient, others less, and inefficiency migrates from one area to another over time, so where edges exist must be reassessed.  #mech/structural_shift _(added by Opus)_
  > some of the markets became more efficient some of the markets became less efficient um and the efficiency also moves from one thing to the other
  asset: multi · horizon: years · testable: partly - decay or revival of strategy returns by market and period can be measured · confidence: medium
  ^MT053-C02-X1

### C03
- **Noah Yechiely** Once a strategy becomes public and many investors follow it, its returns fall.  #mech/crowding_positioning
  > some strategies tend to work become public um many investors are following them and when you have many investors trying to chase the same U the same thing the returns are falling
  indicator: strategy returns after publication · asset: multi · direction: strategy returns decline with adoption · horizon: years · conditions: Applies to widely known strategies · testable: yes - compare returns before and after publication or crowding · confidence: high
  ^MT053-C03-1
- **Noah Yechiely** Data and analysis tools once available to a few are now public and cheap, so data- and technology-dependent edges in markets have become more efficient.  #mech/structural_shift
  > data that was not available it was only available to a particular handful of people
  indicator: alternative/public data availability · asset: equities · horizon: years · conditions: Applies to data-dependent strategies · testable: partly - alpha decay by data availability can be examined · confidence: medium
  ^MT053-C03-2
- **Noah Yechiely** Top-down macro investing targets aggregate forces (spending, growth, inflation) that move whole asset classes together, while bottom-up stock picking on company quality is neutralised when you hold both Boeing and Airbus.  #mech/slow_reaction
  > how much spending is in the market how much the economy is growing inflation and micro forces that are shifting the entire asset class together
  indicator: aggregate spending, growth, inflation · asset: multi · direction: long or short asset classes on macro drivers · conditions: Contrasts with micro/company-level drivers · testable: partly - framework, depends on indicator chosen · confidence: medium
  ^MT053-C03-3

### C04
- **Noah Yechiely** Successful investors understand the causal drivers of markets rather than following what worked in the past.  #mech/research_method
  > trying to figure out why things are happening rather than trying to see what worked in the past
  asset: multi · testable: no - process principle · confidence: medium
  ^MT053-C04-1
- **Noah Yechiely** Investors should challenge their own beliefs and, when a strategy shows a high Sharpe ratio, ask why it works and whether it will continue as in the past.  #mech/research_method
  > always assume that you're wrong rather than that you're right
  indicator: Sharpe ratio of a strategy · asset: multi · testable: partly - out-of-sample persistence checks · confidence: medium
  ^MT053-C04-2
- **Noah Yechiely** Investment research is the same analytical process as consulting or engineering: break a new problem into pieces, build a framework, then find data to test it.  #mech/research_method _(added by Opus)_
  > the approach how you break down the problem into its pieces how you build a framework to solve the problem how you find the data
  asset: multi · testable: no - general process advice · confidence: medium
  ^MT053-C04-X1

### C06
- **Noah Yechiely** Politics and geopolitics (e.g. US-China relations and whether tariffs go higher or lower) affect every company and market, so even bottom-up investors must understand the macro and political forces acting on their holdings.  #mech/policy_reaction _(added by Opus)_
  > whether you know like our relationship with China where the tariffs will be higher lower how it will play out
  indicator: US-China tariff levels · asset: multi · testable: partly - tariff-news sensitivity of stocks can be measured · confidence: high
  ^MT053-C06-X1

