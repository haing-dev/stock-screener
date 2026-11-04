---
source_id: MT059
title: "GBE Founder Cory Paddock- Great Traders Know When a Regime Change Is Coming"
date: 2025-10-09
channel: "Odds on Open"
url: https://www.youtube.com/watch?v=SUDKvKev1Js
words: 7046
claims: 23
added_by_crosscheck: 2
corrections: 0
crosscheck: "opus cross-check"
speakers: ["Cory Paddock (founder and CEO, GBE, discretionary power/energy trading firm)", "Interviewer (host, Odds on Open)"]
tags: [source, layer0]
---
# GBE Founder Cory Paddock- Great Traders Know When a Regime Change Is Coming

**Speakers:** Cory Paddock (founder and CEO, GBE, discretionary power/energy trading firm); Interviewer (host, Odds on Open)

**Summary:** Oct 2025 interview with a US power trader: power as an economics-plus-physics market where a few big setups make the year, edge comes from seeing structural paradigm shifts (coal to gas, wind and solar, data-centre demand) before the market, and history is recency-biased; also hiring, incentive design and trading own capital.

**Approach:** power trading, paradigm shifts, discretionary commodities, incentive alignment, recency bias

**Cross-check completeness estimate of first read:** 0.92 - short, mostly non-quantitative interview; first reader captured nearly all market and risk ideas, missing only the deregulation history and Cory's reply on variance-seeking traders; no errors found.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | power market nature, chunky P&L, deregulation |
| C02 | 1 | research pipeline, LLMs hallucinate |
| C03 | 4 | data sources, edge vs equities, paradigm-shift edge |
| C04 | 5 | history recency bias, coal to gas, wind/solar, demand growth, uncorrelated returns |
| C05 | 1 | rising supply and demand volatility, staying ahead |
| C06 | 0 | nothing actionable: hiring young talent, outliers |
| C07 | 2 | culture, explaining losses, screens identical on own capital |
| C08 | 2 | PJM West Hub contract design, P&L swings |
| C09 | 3 | few trades make the year, no forced setups, incentive alignment |
| C10 | 1 | put option incentive, certainty of pay, motivation |
| C11 | 0 | nothing actionable: closing |

## Claims

### C01
- **Cory Paddock** Power trading is a market built on both economics and physical grid constraints, a partly artificial construct with no perfect market design, which creates opportunities because few understand the details.  #mech/structural_shift
  > power is very much this this intersection of of economics and and physics
  asset: commodities · testable: no - descriptive · confidence: high
  ^MT059-C01-1
- **Cory Paddock** Power P&L is chunky and volatile with five to ten trades making most of the year, so no monthly profit target is sensible.  #mech/risk_management
  > somewhere between five and 10 trades make up for the majority of your year
  asset: commodities · horizon: years · conditions: weather-driven, unpredictable · testable: yes - trade-level P&L concentration · confidence: high
  ^MT059-C01-2
- **Cory Paddock** Traded US power markets only date from late-1990s/early-2000s deregulation (alongside gas), so market designs are still evolving and usable price histories are short.  #mech/structural_shift _(added by opus cross-check)_
  > power trading uh itself um is a relatively new construct. Um really only going back to the uh very tail end of the '9s, early 2000s
  indicator: US power market deregulation history · asset: commodities · horizon: years · testable: partly - limits available history · confidence: high
  ^MT059-C01-X1

### C02
- **Cory Paddock** LLMs help digest thousands of pages of market rules and train juniors but hallucinate and can be talked into agreeing with a wrong position, so a domain expert must correct them.  #mech/research_method
  > they're they're also like excellent at hallucinating
  asset: other · testable: no - practitioner view · confidence: high
  ^MT059-C02-1

### C03
- **Cory Paddock** Power traders use five-minute and tick-level grid data on generation, power flow and nodal prices, not just prices, and years of accumulated pattern recognition.  #mech/new
  > tick by tick um grid level data uh on the generation side on the power flow side
  indicator: nodal prices, generation, power flow, 5-minute data · asset: commodities · horizon: days · testable: yes - data series exist · confidence: high
  ^MT059-C03-1
- **Interviewer (Odds on Open host)** Equities are hard to find edge in because information (supply chains, customers) is public to everyone, whereas power has dispersed, hard-to-find information.  #mech/research_method
  > it's much harder to have edge there
  asset: equities · conditions: information not widely accessible · testable: no - qualitative · confidence: medium
  ^MT059-C03-2
- **Cory Paddock** The main source of edge is holding a view on a fundamental paradigm shift (where power will flow, surplus and deficiency) before the market, which is still trading the previous paradigm.  #mech/slow_reaction
  > having a a point of view on a paradigm shift
  asset: commodities · direction: position early for structural change · horizon: years · conditions: supply and demand constantly change; power amplified · testable: partly - needs identification of shifts ex-ante · confidence: high
  ^MT059-C03-3
- **Cory Paddock** Two traders trading the same product with the same data reduces missed information and forces discussion of what each sees.  #mech/risk_management
  > four sets of eyes on kind of all the same data
  asset: commodities · testable: no - process practice · confidence: medium
  ^MT059-C03-4

### C04
- **Cory Paddock** Historical analysis of 8-10 year old power data gives recency-biased insight because grid topology and price formation change dramatically; trades built on it are ones to fade.  #mech/structural_shift
  > we're happy to take the other side of that trade
  asset: commodities · direction: fade trades based on stale historical patterns · horizon: years · conditions: changing grid topology · testable: yes - test stability of power price relationships over time · confidence: high
  ^MT059-C04-1
- **Cory Paddock** When gas replaced coal, power flows built for coal plants reversed and shifted, producing downstream price effects the market did not predict.  #mech/structural_shift
  > all the power flows were set up to deliver coal fire coal fired electricity to to load centers
  asset: commodities · horizon: years · conditions: fuel switch from coal to gas · testable: yes - basis between nodes after plant relocation · confidence: medium
  ^MT059-C04-2
- **Cory Paddock** Wind (and later solar) introduction initially created negative prices because operators did not know how to optimize for it, offering opportunities that faded as operators adapted.  #mech/slow_reaction
  > at first you know we would see a lot of negative prices that has largely gone away
  indicator: negative power prices · asset: commodities · horizon: years · conditions: early period of new supply technology · testable: yes - negative price frequency · confidence: medium
  ^MT059-C04-3
- **Cory Paddock** After years of flat or falling power demand (efficiency, offshoring), demand is rising due to data centers, industrialization, EVs and heat pumps, a new paradigm for power prices.  #mech/structural_shift _(time-bound view)_
  > for the first time in in my career, we're seeing demand go up
  indicator: power load growth · asset: commodities · direction: power demand up · horizon: years · conditions: data centers main driver; EV and heat pump slower than expected · testable: yes - load data · confidence: medium
  ^MT059-C04-4
- **Cory Paddock** Power returns depend largely on weather and are uncorrelated with equities.  #mech/risk_premium
  > power returns so uncorrelated to what's happening in equities
  indicator: power returns vs equity returns · asset: commodities · conditions: big weather events · testable: yes - correlation · confidence: medium
  ^MT059-C04-5

### C05
- **Cory Paddock** Both demand volatility and supply volatility (wind and solar penetration) are rising, a new paradigm in which the edge is to see changes early and pivot quickly.  #mech/structural_shift _(time-bound view)_
  > demand volatility is is going up and then supply supply volatility is also going up
  asset: commodities · direction: higher power price volatility · horizon: years · testable: yes - realized vol of power prices · confidence: medium
  ^MT059-C05-1

### C07
- **Cory Paddock** Give traders a platform of grid fundamentals so that losses can be explained after the fact and ideas nudged back on track.  #mech/risk_management
  > there's nothing more frustrating than losing money and then not knowing why
  asset: commodities · testable: no - process · confidence: medium
  ^MT059-C07-1
- **Cory Paddock** When moving from a firm to own capital, keep identical information and screens so the only change is risk, not reduced information.  #mech/risk_management
  > we didn't cut a single corner in ensuring that our screens looked the same
  asset: commodities · testable: no - process · confidence: medium
  ^MT059-C07-2

### C08
- **Cory Paddock** The PJM West Hub balance-of-day product is a weighted average of several nodes and five-minute prices from hour 8 to 23, so part is quasi-settled and the remaining uncertainty is concentrated in the rest of the day.  #mech/new
  > it's actually a weighted average of all the five minute prices within houring 8 to 23 of that particular day
  indicator: PJM West Hub balance-of-day contract · asset: commodities · horizon: days · testable: yes - contract specification · confidence: high
  ^MT059-C08-1
- **Cory Paddock** Power P&L can swing within five minutes because prices are set in real time, creating a stressful position-sizing environment.  #mech/risk_management
  > a position can can go like instantly for you or against you within a five minute period
  asset: commodities · horizon: days · testable: yes - 5-minute price changes · confidence: high
  ^MT059-C08-2

### C09
- **Cory Paddock** Most trades are for learning and staying in the market; the goal is to preserve capital and knowledge to size up on the rare big setup.  #mech/risk_management
  > accumulate like future learning that you can apply to a big setup and that have have the capital behind you to to throw to throw at that setup
  asset: commodities · direction: size up on rare high-conviction setups · horizon: years · testable: partly - trade-level distribution · confidence: high
  ^MT059-C09-1
- **Cory Paddock** Lean years occur even with good trading because setups are absent; forcing trades without a setup is the worst mistake.  #mech/risk_management
  > the worst thing you can do is like try to force a set that's not there
  asset: commodities · horizon: years · conditions: no setup · testable: no - process rule · confidence: high
  ^MT059-C09-2
- **Interviewer (Odds on Open host)** Trader bonuses with no downside make the optimal strategy maximize variance (a free call option), so incentives must penalize losses.  #mech/behavioral
  > obviously assuming you can always keep your job the optimal strategy to maximize your earnings is to go for the highest volatility highest variance approaches
  asset: multi · conditions: asymmetric 15-20% bonus without loss sharing · testable: no - incentive theory · confidence: high
  ^MT059-C09-3
- **Cory Paddock** Traders who chase maximum variance because their bonus has no downside are not rewarded by the market over the long run, so screening for that mindset matters as much as pay design.  #mech/risk_management _(added by opus cross-check)_
  > the market doesn't really really reward people in the long run that um that go trying those strategies.
  asset: multi · horizon: years · conditions: bonus with no downside · testable: no - practitioner judgement · confidence: medium
  ^MT059-C09-X1

### C10
- **Cory Paddock** The firm adds a put-option-like loss feature to trader compensation to limit blowups, imperfectly, and removes uncertainty about getting paid.  #mech/risk_management
  > set up a bit of a put option within every within everybody's um uh incentive structure
  asset: commodities · testable: no - firm policy · confidence: medium
  ^MT059-C10-1

