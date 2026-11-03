---
source_id: MT116
title: "Nick Baltas on Trend Following in 2026- Signals, Structure & Strategy - Systematic Investor - Ep.282"
date: 2026-01-17
channel: "Top Traders Unplugged"
url: 
words: 10904
claims: 40
added_by_opus: 0
corrections: 0
crosscheck: "pending"
speakers: ["Nick Baltas (host/co-host, systematic strategist)", "Neils Kostrup Larsen (host, hedge fund manager)"]
tags: [source, layer0]
---
# Nick Baltas on Trend Following in 2026- Signals, Structure & Strategy - Systematic Investor - Ep.282

**Speakers:** Nick Baltas (host/co-host, systematic strategist); Neils Kostrup Larsen (host, hedge fund manager)

**Summary:** Weekly Systematic Investor episode: Baltas and Larsen review trend following in early 2026 and 2025 dispersion across speed and universe (slow and small won the last 3-4 years but not historically). They then summarise three December 2025 papers: a consultant primer on trend, nonlinear time series momentum, and ATP's theory of trend payoff. Conclusion: do not change trend design to chase recent results.

**Approach:** trend following, CTA dispersion, nonlinear time series momentum, signal sizing, crisis alpha

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, sponsor read, travel small talk |
| C02 | 3 | momentum as slow information digestion; narrative data as pre-price signal; no-prediction stance |
| C03 | 2 | conditional exposure to narratives; signal-to-noise beyond return/vol; politics small talk |
| C04 | 3 | Jan 2026 trend start; 2025 dispersion across programs; universe and speed |
| C05 | 2 | classical trend-following return structure; CTA index numbers; book plug |
| C06 | 4 | speed vs universe ranking study over 25 years; slow won last 3 years |
| C07 | 2 | small universes outperform recently but worst 2002-2009; replicator caveat; 2022 fast best |
| C08 | 3 | do not react to dispersion; V-shaped reversals cause it; fixed income sector fell since 2022 |
| C09 | 3 | diversified full-breadth universe preferred; dynamic tilt; Mikita (Mercer-type consultant) paper intro, RMS framework |
| C10 | 4 | trend program design choices; non-trend signals (mean reversion, micro indicators, carry trades) maintain allocation; access routes widen |
| C11 | 2 | transition; Mikita behavioural point; intro to nonlinear time series momentum paper (Moskowitz et al., Dec 2025) |
| C12 | 3 | binary vs linear vs sigmoid trend signals; cost of binary flipping |
| C13 | 3 | neural network learns transfer function; tails flatten and may revert |
| C14 | 3 | neural net vs sigmoid complexity; ATP paper On the Autonomy of Trend intro; vol dependence and trend |
| C15 | 3 | directional vs timing components; iid returns still give crisis alpha beyond thresholds; convex smile |
| C16 | 0 | outro and plugs |

## Claims

### C02
- **Nick Baltas** Trend and momentum exist because information is digested slowly, so a continued price move in one direction is the signal.  #mech/slow_reaction
  > momentum trend and following at the end of the day it's just perhaps um an expression of uh of slow digestion of information
  indicator: price trend / momentum · asset: multi · direction: follow the established move · conditions: works if slow digestion persists · testable: partly - conceptual explanation, signal itself is testable · confidence: high
  ^MT116-C02-1
- **Nick Baltas** News and narrative data collected before prices fully move could give a momentum signal ahead of price-based trend signals.  #mech/slow_reaction
  > if we end up achieving to get hold of prior to the price formation happening it's almost as if we'll get the momentum before the momentum itself plays out in the prices
  indicator: narrative / media information data from an aggregator vendor · asset: multi · direction: trade ahead of price momentum · conditions: unknown; being explored · testable: partly - idea is early, needs narrative dataset and test · confidence: medium
  ^MT116-C02-2
- **Neils Kostrup Larsen** Pure trend following avoids any prediction or story and so is protected when narratives (e.g. Japan hike should lift yen) fail to show up in prices.  #mech/risk_management _(time-bound view)_
  > how important it is not to have any kind of prediction in your in your model
  indicator: trend following with no view · asset: multi · conditions: narratives often fail to move price (Japan rate rise, yen did not strengthen) · testable: partly - principle, evidenced by one anecdote · confidence: high
  ^MT116-C02-3

### C03
- **Nick Baltas** Asset reactions to a narrative or macro theme are conditional, appearing only beyond a threshold, so exposure should be measured conditionally.  #mech/structural_shift
  > equity prices are not necessarily impacted too much about inflation unless inflation is rising beyond a specific threshold
  indicator: inflation level vs equity reaction · asset: equities · conditions: only above an inflation threshold · testable: yes - threshold conditional regression is testable · confidence: medium
  ^MT116-C03-1
- **Nick Baltas** Quantifying signal-to-noise in a market, beyond return divided by volatility, is important for avoiding V-shaped reversals, and non-price information may help.  #mech/research_method
  > signal to noise quantification is important specifically for the Vshapes
  indicator: signal-to-noise ratio; return over volatility · asset: multi · testable: partly - proxy is return/vol, richer versions undefined · confidence: medium
  ^MT116-C03-2

### C04
- **Nick Baltas** Trend conditions were strong for seven consecutive months into January 2026, driven by metals and equities.  #mech/cycle_persistence _(time-bound view)_
  > it is kind of the seventh month in a row where we're seeing very strong conditions uh for trend
  indicator: trend index performance; metals and equities · asset: multi · direction: long metals and equities · horizon: months · testable: yes - CTA index data is observable · confidence: high
  ^MT116-C04-1
- **Nick Baltas** Dispersion in 2025 trend programs came mainly from which markets were traded (universe breadth) and trend speed; faster and more diversified programs lagged.  #mech/structural_shift _(time-bound view)_
  > I think the universe and the speed are probably the two most important um pillars of dispersion at least for the last year
  indicator: trend speed (3m, 6m, 12m lookback); universe breadth · asset: multi · horizon: months · conditions: in 2025 only equities and precious metals trended while rates repeatedly failed · testable: yes - compare speed and universe variants over 2025 · confidence: medium
  ^MT116-C04-2
- **Nick Baltas** Trend programs of different speeds stayed highly correlated in 2025 because the same few markets drove gains and the same markets (rates) caused losses.  #mech/crowding_positioning _(time-bound view)_
  > the correlations were relatively elevated anyway because to your point there were a few markets that exhibited strong trends
  indicator: scaled correlation of trend programs · asset: multi · horizon: months · conditions: when few markets trend · testable: yes - outlier-scaled correlation analysis · confidence: medium
  ^MT116-C04-3

### C05
- **Neils Kostrup Larsen** A year where gains come from a handful of markets with many small losses is the classic trend following payoff shape, so 2025 was typical in structure.  #mech/cycle_persistence
  > most managers probably made all the money in only a handful of markets and other than that we had many small losses maybe one or two bigger losses
  indicator: trend following return distribution · asset: multi · horizon: years · testable: yes - return concentration is measurable · confidence: high
  ^MT116-C05-1
- **Neils Kostrup Larsen** In early January 2026 the SG CTA index was up about 4.4%, trend index 4.67% and short-term traders 1.75%.  #mech/cycle_persistence _(time-bound view)_
  > gen CTA index up uh 4 and a4% very strong trend index even more so up 4.67% and the short-term traders index up 1.75%
  indicator: SG CTA, trend and short-term traders indices · asset: multi · direction: long trend; short-term traders lag · horizon: weeks · testable: yes - published index data · confidence: high
  ^MT116-C05-2

### C06
- **Nick Baltas** If volatilities and correlations are stable, trend lookback speed drives more performance dispersion between programs than sizing method (dynamic vs static, correlation use).  #mech/structural_shift
  > speed will create more of a dispersion than the sizing
  indicator: trend speed vs sizing method · asset: multi · horizon: years · conditions: assumes stable vols and correlations; not tested · testable: yes - can be tested by fixing universe and varying speed vs sizing · confidence: low
  ^MT116-C06-1
- **Nick Baltas** Over the last three years slow trend speeds (around 12 months, second best 9 months) ranked best in a 25-year ranking of annual speed performance, unprecedented three years in a row.  #mech/slow_reaction _(time-bound view)_
  > for the last three years and that's exactly what I said in the in the December discussion if you were slow you would have out outperformed
  indicator: trend lookback speed from 2 to 12 month half-life · asset: multi · direction: slow trend outperformed · horizon: years · conditions: driven by V-shaped reversals (SVB, dollar yen, Liberation Day) hurting fast signals · testable: yes - rank speeds by annual return, 25 years · confidence: high
  ^MT116-C06-2
- **Nick Baltas** Over roughly the last four years a concentrated universe (DBMF-like) outperformed a broad 80 to 100 market universe, which Baltas had not seen before in the 25-year history.  #mech/structural_shift _(time-bound view)_
  > universe wise having been small is possibly quite dominantly the outperformer for
  indicator: trend universe size (small vs 80-100 markets) · asset: multi · direction: small universe · horizon: years · conditions: recent regime; was worst in other eras · testable: yes - rank universes by annual return · confidence: high
  ^MT116-C06-3
- **Nick Baltas** A medium-sized universe is best built thoughtfully (e.g. a few major ex-US equity indices, more tenors in rates) instead of many currencies and few equities.  #mech/research_method
  > you can broaden up a small universe by just having maybe more tenors in specific interest rate markets
  indicator: universe construction · asset: multi · testable: partly - judgemental construction · confidence: medium
  ^MT116-C06-4

### C07
- **Neils Kostrup Larsen** Small trend universes were the worst performer each year from the tech bubble aftermath through 2009, so recent small-universe outperformance by replicators should not be extrapolated.  #mech/cycle_persistence
  > being small or trading a small universe was the worst universe every single year for something like seven years in a row
  indicator: trend universe size · asset: multi · horizon: years · conditions: era dependent: small universes win since 2016, lost 2002 to 2009 · testable: yes - historical ranking by year · confidence: high
  ^MT116-C07-1
- **Nick Baltas** In 2022 the fastest trend speeds ranked best, the opposite of the last three years, showing the best speed flips with the regime of sustained trends versus reversals.  #mech/cycle_persistence _(time-bound view)_
  > in 2022 you you conclude based on your analysis that actually being very were very quick
  indicator: trend speed · asset: multi · direction: fast outperformed in 2022 · horizon: years · conditions: sustained trends in commodities, rates and dollar · testable: yes - annual speed ranking · confidence: medium
  ^MT116-C07-2

### C08
- **Nick Baltas** Changing trend design (speed, universe) in response to recent out- or under-performance is the wrong approach; discipline and trust in the process matter more.  #mech/risk_management
  > reacting to out or underperformance is is the wrong recipe
  indicator: trend design · asset: multi · testable: partly - chasing recent winners can be tested as a meta-strategy · confidence: high
  ^MT116-C08-1
- **Nick Baltas** Recent dispersion came from V-shaped reversals (mean reversion beyond trend dynamics), not from longer-duration trends being better.  #mech/overshoot _(time-bound view)_
  > it is more about that the Vshapes are the ones to have caused this dispersion rather than oh actually you should have been longer term
  indicator: V-shaped reversals · asset: multi · horizon: months · testable: partly - reversal events identifiable ex post · confidence: medium
  ^MT116-C08-2
- **Neils Kostrup Larsen** After 2022 many concluded to keep trading mostly fixed income because it had been the best sector for 20 years, yet it has been the worst sector since 2022, so sector concentration on the past is risky.  #mech/cycle_persistence _(time-bound view)_
  > pretty much since 2022, it's been kind of the worst sector to trade
  indicator: fixed income trend sector contribution · asset: rates · horizon: years · testable: yes - sector attribution of trend · confidence: high
  ^MT116-C08-3

### C09
- **Neils Kostrup Larsen** Over about 20 years every trend sector has been profitable but contribution rotates over time, so a full-breadth portfolio is the more intuitive design.  #mech/structural_shift
  > all sectors have actually been profitable
  indicator: sector contribution to trend following · asset: multi · direction: broad diversified universe · horizon: years · testable: yes - sector level backtest · confidence: medium
  ^MT116-C09-1
- **Nick Baltas** Baltas favors dynamic allocation across sectors, tilting toward areas with positive trend in the sector return signal, rather than static equal weights.  #mech/slow_reaction
  > I see it more as an opportunity set that, you know, to the extent it's available to us, we tilt in favor or against depending on the intertemporal trend
  indicator: sector-level trend signal for risk allocation · asset: multi · direction: tilt toward trending sectors · horizon: months · testable: yes - tilt rule is testable · confidence: medium
  ^MT116-C09-2
- **Nick Baltas** Defensive strategies range from reactive, high-bias, expensive tail hedges to carry-generating but not downside-protecting ones, with trend following as the intermediate component (RMS framework of first and second responders).  #mech/risk_management
  > we wrote a paper back in 2019 as to how we think of defensive solutions and what are the different pillars
  indicator: tail hedges, trend, carry · asset: multi · testable: partly - framework, crisis behaviour measurable · confidence: medium
  ^MT116-C09-3

### C10
- **Nick Baltas** Trend program design differences that matter: universe, speed, diversifying non-trend signals, stop-loss and profit-taking, static vs dynamic risk allocation, and volatility targeting leverage.  #mech/research_method
  > Stop-loss and profit uh taking triggers
  indicator: trend program design dimensions · asset: multi · testable: partly - each dimension can be varied in backtest · confidence: medium
  ^MT116-C10-1
- **Nick Baltas** In 2025 mean reversion, micro indicators and carry trades all did well and diversified trend, so programs that included them differed from pure trend.  #mech/cycle_persistence _(time-bound view)_
  > 2025 was a strong strong strong year for all those concepts
  indicator: mean reversion, micro indicators, carry · asset: multi · horizon: months · testable: partly - one-year observation · confidence: high
  ^MT116-C10-2
- **Nick Baltas** Non-trend components help investors stay allocated to trend following during its drawdowns, which matters because investors feel losses more than gains (concave utility).  #mech/behavioral
  > allow it to be maintained in an location at times that it's actually not performing well
  indicator: non-trend signals alongside trend · asset: multi · testable: no - behavioural benefit hard to test · confidence: medium
  ^MT116-C10-3
- **Nick Baltas** Institutions can now access trend through CTAs, mutual funds, UCITS, ETFs and QIS, reflecting more mainstream demand.  #mech/structural_shift
  > institutions have a variety of possibilities in terms of accessing the the style
  asset: multi · testable: no - industry observation · confidence: high
  ^MT116-C10-4

### C11
- **Nick Baltas** Trend allocations often fail because of investor behaviour, i.e. reacting to drawdowns by cutting, not because of the strategy itself.  #mech/behavioral
  > a lot of trend following allocation kind of fails mostly because of the behavior or mostly because of the kind of reaction pattern of of investors
  indicator: investor behaviour in trend allocations · asset: multi · horizon: years · testable: no - behavioural, not directly testable · confidence: medium
  ^MT116-C11-1
- **Nick Baltas** The nonlinear time series momentum paper proposes letting the data (via a neural network) determine how past returns map to positions instead of imposing a sigmoid.  #mech/research_method
  > if there are those nonlinearities instead of us forcing them by some sort of a parametric approach let's say we know we utilize something that is called a sigmoid
  indicator: past return to position transfer function · asset: multi · testable: yes - paper replication with neural net vs sigmoid · confidence: medium
  ^MT116-C11-2

### C12
- **Nick Baltas** Linear scaling of position by signal magnitude improves on a binary long/short signal because weak signals get small positions.  #mech/risk_management
  > if it's a basis point positive, then maybe I should do a basis point allocation rather than a 1% allocation
  indicator: trend signal magnitude · asset: multi · direction: scale position with signal size · testable: yes - binary vs linear backtest · confidence: high
  ^MT116-C12-1
- **Nick Baltas** Beyond a certain size the signal should be capped, giving a sigmoid shape (linear near zero, flat in the extremes), because estimation noise and reversion make extreme signals less reliable.  #mech/overshoot
  > there is a point whereby I just want to
  indicator: trend signal sigmoid transformation · asset: multi · direction: cap exposure at extreme signals · conditions: extreme signals e.g. three Sharpe-ratio units of past return · testable: yes - test sigmoid vs linear · confidence: high
  ^MT116-C12-2
- **Nick Baltas** Binary signals only win via an early start, but when a signal oscillates around zero they flip full positions and accrue large trading costs, so net of costs linear or sigmoid sizing is preferable.  #mech/risk_management
  > with two full positive and two full negative exposure you'll end up acrewing a lot of costs
  indicator: binary vs linear/sigmoid sizing · asset: multi · conditions: choppy, near-zero signals · testable: yes - net-of-cost comparison · confidence: high
  ^MT116-C12-3

### C13
- **Nick Baltas** Past returns continue to predict future returns near zero but revert in the extremes, so the return-to-position map is nonlinear.  #mech/overshoot
  > the data generating process is such whereby you have this continuation of return but in the tails it ends up reverting
  indicator: past return vs future return nonparametric relation · asset: multi · direction: flatten or reverse at extreme past returns · testable: yes - nonparametric regression · confidence: medium
  ^MT116-C13-1
- **Nick Baltas** Keeping the sign of the signal (long if positive, short if negative) preserves a trend strategy; letting the model flip sign at extremes mixes in a reversion engine that is better run separately for allocation and attribution.  #mech/research_method
  > the minute we depart from it it is no longer just a trend strategy
  indicator: trend with reversal in tails · asset: multi · testable: partly - design choice · confidence: medium
  ^MT116-C13-2
- **Nick Baltas** The paper uses a neural network to estimate the transfer function per asset class and finds tail flattening and even reversion at extremes.  #mech/research_method
  > they use a neural network to effectively um um if you like extract the way that past return translates into future return
  indicator: neural network transfer function from past returns · asset: multi · testable: yes - replicable · confidence: medium
  ^MT116-C13-3

### C14
- **Nick Baltas** A neural network transfer function agrees with the sigmoid theory, so it is open whether its extra complexity adds value over a parametric sigmoid.  #mech/research_method
  > whether this incremental complexity will bring significant value versus having a sigmoid that in itself kind of be in itself behaves um in line with with with expectations
  indicator: neural network vs sigmoid trend sizing · asset: multi · testable: yes - head to head backtest · confidence: medium
  ^MT116-C14-1
- **Nick Baltas** Trend following can profit even when returns are independent if volatility is serially dependent, so autocorrelation of returns is not required.  #mech/structural_shift
  > even if returns are independent if volatility in itself is serally dependent you can still benefit from a trend following strategy
  indicator: volatility clustering · asset: multi · testable: yes - simulation or empirical · confidence: medium
  ^MT116-C14-2
- **Nick Baltas** The ATP paper derives a trend follower's expected payoff conditional on the cumulative past return over a horizon, with a directional and a timing component.  #mech/research_method
  > if I'm observing a significant draw down what is my expected payoff from being a trend follower
  indicator: conditional payoff of binary trend signal on past cumulative return · asset: multi · testable: yes - derive and test conditional payoff · confidence: medium
  ^MT116-C14-3

### C15
- **Nick Baltas** Even when returns are iid, a trend follower earns positive expected payoff conditional on a deep drawdown beyond a threshold, which explains crisis alpha without serial correlation.  #mech/structural_shift
  > beyond specific thresholds mathematically defined a trend follower can still um deliver positive return and specifically in the draw down specifically as a crisis alpha
  indicator: trend payoff conditional on drawdown · asset: multi · direction: long trend in drawdown assets · horizon: months · conditions: beyond mathematically defined threshold of cumulative past return · testable: yes - conditional payoff measurement · confidence: medium
  ^MT116-C15-1
- **Nick Baltas** Besides getting the average direction right (e.g. holding equities with a positive premium), the timing of turning to align with the price process determines trend following profit.  #mech/slow_reaction
  > how quickly can you turn into a situation whereby your um price process um is aligned in terms of direction with your signaling
  indicator: speed of signal turning · asset: multi · testable: partly - theory component, speed measurable · confidence: medium
  ^MT116-C15-2
- **Nick Baltas** Trend following has a convex payoff versus the market (smile shape), gaining in large moves in either direction.  #mech/cycle_persistence
  > the convex profile of trend followers, the smile shape
  indicator: trend payoff vs market return · asset: equities · conditions: large market moves · testable: yes - regress on market and squared market · confidence: medium
  ^MT116-C15-3

