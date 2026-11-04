---
source_id: MT140
title: "Robert Carver Ran a Multi-Billion Dollar Systematic Portfolio for Man AHL. Now He Invests Solo."
date: 2025-07-24
channel: "Odds on Open"
url: https://www.youtube.com/watch?v=y39Zf3GPpxE
words: 8576
claims: 42
added_by_crosscheck: 5
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Robert Carver (independent systematic futures trader, ex-Man AHL head of fixed income, author)", "Ethan (host, Odds on Open)"]
tags: [source, layer0]
---
# Robert Carver Ran a Multi-Billion Dollar Systematic Portfolio for Man AHL. Now He Invests Solo.

**Speakers:** Robert Carver (independent systematic futures trader, ex-Man AHL head of fixed income, author); Ethan (host, Odds on Open)

**Summary:** Odds on Open interview (July 2025) with Rob Carver on running billions at Man AHL and trading solo. Approach: slow diversified systematic futures (trend, carry, skew, relative value) earning risk premia, not inefficiencies; skepticism, explicit rather than implicit fitting, realistic backtests, and metrics beyond Sharpe (LTCM lesson); slow strategies make alpha decay undetectable; collaborative research review at AHL vs pod incentives.

**Approach:** systematic trend following, carry, skew, backtesting and overfitting, performance metrics, alpha decay, research process

**Cross-check completeness estimate of first read:** 0.92 - first reader extracted nearly every method point (Sharpe/LTCM, explicit versus implicit fitting, alpha decay, full list of trading rules, research review) accurately; missed founder-culture, institutional-incentive, pod-versus-collaborative and Man-is-not-a-pod-shop points plus the money-secondary hiring view.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | P&L abstraction and the $1bn week at AHL |
| C02 | 2 | experience with losses; AHL culture; systematic trading needs less market watching |
| C03 | 2 | quant skill sets by trading frequency; hiring path dependence |
| C04 | 1 | skepticism as key trait; Sharpe ratio and LTCM question |
| C05 | 5 | LTCM, Sharpe limits, peso problem, geometric return and bootstrapping |
| C06 | 2 | explicit vs implicit fitting |
| C07 | 4 | push fitting into explicit process; realistic backtests; alpha decay |
| C08 | 13 | decay of trend; Carver's trading rules list |
| C09 | 1 | career advice (excluded); risk premia not inefficiencies |
| C10 | 3 | rate of adding signals, strike rate, small-account innovation, crude portfolio construction; AHL idea flow |
| C11 | 2 | AHL collaborative research process and formal veto |
| C12 | 1 | pod shop vs Man AHL structure and incentives |
| C13 | 0 | people motivated by money; outro |

## Claims

### C01
- **Robert Carver** Abstract P&L into percentages and ideally avoid looking at P&L to avoid emotional reactions; Carver's fixed income pool lost about 10-11% in the worst week, equivalent to $1bn at fund level.  #mech/behavioral
  > if you did look at your P&L, then then definitely look at it in in percentages rather than in actual number terms
  asset: multi · horizon: days · testable: no · confidence: high
  **Correction (cross-check):** The $1bn is the whole-fund loss that a newly hired colleague remarked on; Carver's own fixed income pool lost about 10-11% in that week. The two figures are not equivalent. → In its worst week Carver's fixed income pool lost about 10-11% while the whole fund lost roughly $1bn (a newcomer from a discretionary fund was shocked); thinking in percentages and not looking at P&L makes such losses easier to handle.
  ^MT140-C01-1

### C02
- **Robert Carver** Experience of past market events (2008, COVID, April 2025 tariffs) makes large losses easier to stomach and expect.  #mech/behavioral
  > The first the first time you experience that kind of loss um is is going to be harder than the the the the second, third, fourth, 10th, 20th time you've experienced it.
  asset: multi · testable: no · confidence: high
  ^MT140-C02-1
- **Robert Carver** Systematic trading allows a more abstract, objective view without constantly following news.  #mech/behavioral
  > if you're trading systematically, then um, there's less need to be constantly observing the markets.
  asset: multi · testable: no · confidence: medium
  ^MT140-C02-2
- **Robert Carver** A firm's research culture follows its founders: AHL was founded by three physicists and outsiders who took a scientific outside view of markets, whereas many US CTAs came from pit-trading lineage with a more visceral, intuitive market understanding; each approach has strengths and weaknesses.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > firms sort of have carry the DNA of their founders within them
  asset: multi · testable: no - qualitative · confidence: medium
  ^MT140-C02-X1

### C03
- **Robert Carver** Required skills depend on trading frequency: high-frequency needs programmers and data analysts, low-frequency macro needs broader market and economic knowledge.  #mech/research_method
  > the more high frequency you're trading the more I think you can treat the market as an abstract object
  asset: multi · testable: no · confidence: medium
  ^MT140-C03-1
- **Robert Carver** Beliefs about what background makes the best quants may reflect path dependence from successful firms' hiring rather than causal skill.  #mech/behavioral
  > there is a degree of path dependence in that you know people will look at firms that have done well and say well what kind of people do they hire
  asset: other · testable: no · confidence: medium
  ^MT140-C03-2

### C04
- **Robert Carver** Skepticism is the key trait: almost every error comes from overconfidence in backtests, unclean data or forward bias in prices.  #mech/research_method
  > has ultimately been because people have been overconfident and have have trusted in their back test too much or assumed that their data was clean when it wasn't
  asset: multi · testable: no · confidence: high
  ^MT140-C04-1

### C05
- **Robert Carver** LTCM still had a Sharpe ratio above 3 after its collapse, so Sharpe is not an ideal metric; there are no ideal performance metrics.  #mech/research_method
  > even with that disastrous event that caused them to lose basically all their capital, um LTCM still had a sharp ratio of over three
  indicator: Sharpe ratio · asset: multi · horizon: years · testable: yes - recompute LTCM Sharpe · confidence: medium
  **Correction (cross-check):** Carver states the LTCM Sharpe figure from memory and says he has not checked it, so the number is low-confidence rather than a fact. → From memory (unchecked), LTCM still had a Sharpe ratio above 3 even including its final collapse, which Carver uses to show that Sharpe is not an ideal metric and that no performance metric is ideal.
  ^MT140-C05-1
- **Robert Carver** Sharpe assumes symmetric, normal returns; LTCM-type strategies (option selling, CDS premium: small gains, rare disasters) are negatively skewed and should not be judged by Sharpe.  #mech/risk_management
  > it's not appropriate to use a SH ratio to to judge their efficacy
  indicator: Sharpe ratio; skew · asset: multi · conditions: negative skew fat-left-tail strategies · testable: yes · confidence: high
  ^MT140-C05-2
- **Robert Carver** LTCM's failure was the peso problem: data too short to include outliers; any metric including outliers would have shown too much leverage.  #mech/research_method
  > their data sets weren't didn't go back long enough to see the outliers that would have killed them
  indicator: data length · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT140-C05-3
- **Robert Carver** Sharpe is the go-to metric for leveraged futures traders, but for unleveraged investors geometric return is more appropriate; maximising Sharpe maximises geometric return only under normality and free leverage.  #mech/risk_management
  > for people who can't use leverage and therefore sharp ratio is is sort of secondary to a measure like say geometric return
  indicator: Sharpe; geometric return · asset: multi · conditions: leverage available vs not · testable: yes · confidence: high
  ^MT140-C05-4
- **Robert Carver** Carver evaluates geometric return via bootstrap and considers a conservative percentile of the distribution rather than the median.  #mech/research_method
  > I'll look at it you know using say a bootstrapping technique and I'll use the distribution of those geometric returns
  indicator: bootstrapped geometric return · asset: multi · testable: yes · confidence: medium
  ^MT140-C05-5

### C06
- **Robert Carver** Explicit fitting done right weights parameter sets by statistical evidence (slightly more for the best) instead of choosing one best parameter, using rolling or expanding windows.  #mech/research_method
  > what you actually want is a portfolio of these parameters
  asset: multi · testable: yes · confidence: high
  ^MT140-C06-1
- **Robert Carver** Implicit fitting: choosing models or removing markets after seeing the backtest uses future performance knowledge, undoing robust explicit fitting.  #mech/research_method
  > swapping out one model and swapping in another model. But having done so importantly with full knowledge of the road's performance of those two models
  asset: multi · testable: yes · confidence: high
  ^MT140-C06-2

### C07
- **Robert Carver** Put all model choices into one explicit procedure where weights shift only as evidence accrues, giving a realistic backtest and avoiding choosing a model with hindsight.  #mech/research_method
  > to try and basically push as much as possible into the explicit fitting
  asset: multi · testable: yes · confidence: high
  ^MT140-C07-1
- **Robert Carver** Unrealistic backtest performance leads to excessive leverage (LTCM) and trading too fast with high costs, so a realistic backtest matters even if the final model is the same.  #mech/risk_management
  > if your past performance is unrealistically high, then both of those decisions will have been stupid ones
  asset: multi · testable: yes · confidence: high
  ^MT140-C07-2
- **Robert Carver** High-frequency alpha decays with half-life of 1.5-2 months and is detectable statistically in real time, requiring constant replacement.  #mech/structural_shift
  > if I was trading you know high frequency data I would expect my alpha decay to be have a halflife of about a month and a half or two months maybe
  indicator: alpha decay half-life · asset: multi · horizon: weeks · conditions: high frequency · testable: partly · confidence: medium
  ^MT140-C07-3
- **Robert Carver** For slow systems alpha decay with a half-life of 1-2 decades cannot be distinguished from noise, so it is not worth monitoring; basic trend following has decayed gradually over 50-60 years.  #mech/structural_shift
  > that decay process potentially happening with halflife of one or two decades uh which means it's almost impossible to distinguish it from the kind of just general statistical noise
  indicator: alpha decay · asset: multi · horizon: years · conditions: slow strategies · testable: yes · confidence: high
  ^MT140-C07-4

### C08
- **Robert Carver** Pure trend following may have stopped working for a decade, but low Sharpe makes this undetectable statistically.  #mech/research_method
  > because their performance is not that high to begin with, it's actually impossible to tell statistically whether that's the case
  indicator: trend following performance · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT140-C08-1
- **Robert Carver** Diversifying across many trading rules beyond pure trend reduces exposure to trend decay; slow trading lets Carver ignore decay.  #mech/risk_management
  > Um, so I'd be less exposed to a decay in the performance of pure trend anyway.
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT140-C08-2
- **Robert Carver** Acceleration rule: trend on trend; positive acceleration if momentum is increasing or a fall decelerates.  #mech/cycle_persistence
  > That's basically um a the a trend on a trend.
  indicator: acceleration (change in momentum) · asset: multi · direction: long when momentum increasing · horizon: months · testable: yes · confidence: medium
  ^MT140-C08-3
- **Robert Carver** Asset-class trend: apply a trend signal on the whole asset class (are equities overall bullish) and go long all its markets.  #mech/cycle_persistence
  > my trend signal on the whole asset class rather than just an individual market
  indicator: asset class trend · asset: multi · direction: long entire asset class when bullish · horizon: months · testable: yes · confidence: medium
  ^MT140-C08-4
- **Robert Carver** Breakout rule: go long or short when price is near the extreme of its range.  #mech/cycle_persistence
  > sees where a price is within a range and if it's near the extreme of that range then it goes longer or shorter
  indicator: breakout · asset: multi · direction: long near highs, short near lows · horizon: months · testable: yes · confidence: medium
  ^MT140-C08-5
- **Robert Carver** Carry rule: positions based on futures curve slope (contango versus backwardation).  #mech/risk_premium
  > looks at the slope of the uh futures curve um see whether it's in contango or backquidation
  indicator: futures curve slope · asset: multi · direction: long backwardation, short contango · horizon: months · testable: yes · confidence: medium
  ^MT140-C08-6
- **Robert Carver** Momentum rule: exponentially weighted moving average crossover on price.  #mech/cycle_persistence
  > average crossover. So that's momentum on the actual price itself.
  indicator: EWMAC · asset: multi · direction: long when fast EWMA above slow · horizon: months · testable: yes · confidence: medium
  ^MT140-C08-7
- **Robert Carver** Very slow relative mean reversion: assets mean revert at long horizons, so short the recent multi-year outperformer vs the laggard.  #mech/overshoot
  > let's say the S&P has outperformed the the footsy 100 for the last couple of years then I would go short the S&P and long the footsen
  indicator: multi-year relative return · asset: equities · direction: short past winner, long past loser (relative) · horizon: years · conditions: long horizons only · testable: yes · confidence: medium
  ^MT140-C08-8
- **Robert Carver** Short-horizon mean reversion exists but does not survive trading costs for Carver.  #mech/risk_management
  > I can't seem to get those strategies to work after trading costs
  asset: multi · horizon: days · conditions: after costs · testable: yes · confidence: medium
  ^MT140-C08-9
- **Robert Carver** Normalised momentum applies momentum to a risk-normalised price series, giving more normal distribution and cleaner signal.  #mech/research_method
  > perform a risk normalization on the price series. So that makes the price series itself more normally distributed and gives a cleaner signal
  indicator: risk-normalised price momentum · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT140-C08-10
- **Robert Carver** Relative carry: long higher-carry and short lower-carry markets within an asset class.  #mech/risk_premium
  > if the carry is higher in one particular part of the equities space say I you know go long that and short things with lower carry
  indicator: relative carry · asset: multi · direction: long high carry, short low carry within asset class · horizon: months · testable: yes · confidence: medium
  ^MT140-C08-11
- **Robert Carver** Relative momentum within asset classes: long recent relative winners; the opposite of slow mean reversion but at faster frequency.  #mech/cycle_persistence
  > So I go long things that have gone up relative to other things.
  indicator: relative momentum · asset: multi · direction: long relative winners · horizon: months · testable: yes · confidence: medium
  ^MT140-C08-12
- **Robert Carver** Skew rule: go long assets with recent extreme sharp falls (negative skew), absolute and relative, because the market pays a risk premium for them.  #mech/risk_premium
  > then I would actually go long those assets um because generally speaking the market pays a risk premium for assets like that
  indicator: historic skew · asset: multi · direction: long assets with negative skew · horizon: months · testable: yes · confidence: medium
  ^MT140-C08-13

### C09
- **Robert Carver** Carver believes his systematic returns are risk premia, not market inefficiencies, since the methods are public and long-existing.  #mech/risk_premium
  > I believe that basically all the money I make is from you know what an economist will call risk premier.
  asset: multi · horizon: years · testable: no · confidence: high
  ^MT140-C09-1

### C10
- **Robert Carver** Because he trades slowly with slow decay, Carver adds about one new signal a year or less, with a strike rate of about 20% of ideas researched, and prefers failing to overfitting.  #mech/research_method _(quote near)_
  > I might add like one thing a year on average if that maybe less.
  asset: multi · horizon: years · testable: no · confidence: high
  ^MT140-C10-1
- **Robert Carver** The main system innovation of the last decade was handling a small account while trading over 200 futures markets, unrelated to finding an edge.  #mech/research_method
  > I'm still able to trade over 200 futures markets with a very small account with a relatively small account size
  asset: multi · conditions: small accounts · testable: partly · confidence: high
  ^MT140-C10-2
- **Robert Carver** Crude portfolio construction works as well as sophisticated optimisation techniques.  #mech/research_method
  > the way I do my construction is actually quite crude because that works just as well as the more sophisticated techniques
  asset: multi · direction: simple weights · testable: yes · confidence: high
  ^MT140-C10-3
- **Robert Carver** Institutional incentives push researchers to keep producing new signals even when the existing slow, high-alpha system does not need them, which raises complexity and overfitting risk; an independent slow trader has no such pressure.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > working in institution I had to justify my salary right so I had to generate new ideas even if arguably they weren't necessary
  asset: multi · horizon: years · conditions: applies to low-frequency systems with slow decay · testable: no - organisational observation · confidence: high
  ^MT140-C10-X1

### C11
- **Robert Carver** At AHL a shared research library avoided redoing earlier work and allowed building on it, with seminars including traders and middle office to catch practical flaws.  #mech/research_method
  > any any research report that was written um anyone from the kind of quant team could go and look could go and read that
  asset: multi · testable: no · confidence: high
  ^MT140-C11-1
- **Robert Carver** Formal proposals for new strategies needed review by head of risk and CIO with veto; this rigour was valuable though mistakes still happened.  #mech/risk_management
  > the head of risk and the CIO had to kind of um they basically had the right of veto on these things
  asset: multi · testable: no · confidence: high
  ^MT140-C11-2
- **Robert Carver** Pod shops run teams in information silos that compete and share nothing, while a collaborative quant firm shares research openly, which avoids duplicated work and lets ideas be checked by others.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check)_
  > a kind of collaborative environment compared to say like a pod shop where people are very much in their own silos and they literally don't want to leak any information to the desk next to them
  asset: multi · testable: no - organisational structure · confidence: high
  ^MT140-C11-X1

### C12
- **Robert Carver** Pod shops pay a larger share of P&L to profitable teams and fire losers, attracting money-motivated people, while collaborative firms like Man AHL attract others.  #mech/behavioral
  > because of the pod structure, the compensation structure, you're going to take home a bigger percentage of your revenue
  asset: multi · testable: no · confidence: medium
  ^MT140-C12-1
- **Robert Carver** Corrects the host's premise: Man Group is a public company owning several hedge funds, none of them pod shops, and AHL has only about 100-120 front-office staff, so the talent-and-capital consolidation argument about Citadel and Millennium does not apply directly to it.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > I'm not sure I'd put manh in the same bucket as to millennial. So you know they're not a pod shop.
  asset: multi · testable: no - organisational fact · confidence: medium
  ^MT140-C12-X1

### C13
- **Robert Carver** Beyond a certain pay level extra money does not matter to most people, so the best quant hires are those motivated by culture and the work rather than money; the same applies to AI researchers offered nine-figure packages.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > I think the people you want working for you are those for whom money is a secondary consideration
  asset: multi · testable: no - hiring view · confidence: medium
  ^MT140-C13-X1

