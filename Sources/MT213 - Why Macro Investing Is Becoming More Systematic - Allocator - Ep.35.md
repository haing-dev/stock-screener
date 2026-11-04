---
source_id: MT213
title: "Why Macro Investing Is Becoming More Systematic - Allocator - Ep.35"
date: 2026-06-06
channel: "Top Traders Unplugged"
url: 
words: 11507
claims: 65
added_by_crosscheck: 8
corrections: 0
crosscheck: "sonnet-xhigh cross-check"
speakers: ["George Patterson (Managing Director and CIO, PGIM Quantitative Solutions; transcript spells 'Pim')", "Alan Dunn (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Why Macro Investing Is Becoming More Systematic - Allocator - Ep.35

**Speakers:** George Patterson (Managing Director and CIO, PGIM Quantitative Solutions; transcript spells 'Pim'); Alan Dunn (host, Top Traders Unplugged)

**Summary:** Allocator interview (Ep.35, mid-2026) with the CIO of PGIM Quantitative Solutions (quant equity and multi-asset, $110bn) on systematic macro and multi-asset solutions. Approach: mid-horizon fundamental regime models (Gaussian mixture, traditional quadrants) plus short-term tactical overlay, many models combined, LLM text analysis, human in the loop. Conclusions: guard against in-sample optimization, expect faster policy responses, inflation above about 4% is the threshold that hurts, commodities as inflation hedge.

**Approach:** systematic macro, multi-asset, regime models, Gaussian mixture, LLM and NLP, overfitting and research process, inflation hedging, downside protection

**Cross-check completeness estimate of first read:** 0.91 - first reader captured nearly every method and view (regime models, inflation 4% rule, multi-model, in-sample discipline, LLM use, faster policy response); missed a few supporting remarks (real-asset hedges, overfit incentive, non-stationarity, complexity debate). C16 career advice and C17 disclaimer are not claim-worthy.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 3 | intro, model assumptions and regime shifts, team design, positive macro view |
| C02 | 2 | PGIM Quant scale, evolution of macro investing from big concentrated bets to systematic, alternative data |
| C03 | 3 | strategy evolution with NLP, 60/40 critique and diversification tools, client customization |
| C04 | 4 | privates and liquidity needs, oil/inflation principal component, 4% inflation threshold, LLM monitoring |
| C05 | 3 | mid-horizon fundamentals plus tactical overlay, commodities as inflation hedge |
| C06 | 4 | Gaussian mixture regime model, no market data, multiple models, quadrant approach |
| C07 | 5 | multi-model winners, pattern-matching bias, sticking to process, fundamentals-heavy models |
| C08 | 3 | few degrees of freedom, priors, COVID data gaps and manual intervention, multi-asset structure |
| C09 | 5 | options downside protection, long vol in 2022, evolution of NLP/LLM use |
| C10 | 4 | text data for alpha and risk, LLM sentiment strengths and limits, bots and short-term prices |
| C11 | 4 | human in loop, AI and jobs, forward curves unreliable, 2026 rate swings |
| C12 | 3 | fiscal tipping point, small edge in quant models, simplicity vs complexity, in-sample problem |
| C13 | 4 | avoid in-sample optimization, kill-the-research test, out-of-sample humility |
| C14 | 6 | decay of signals, faster policy response and crashes, retail participation and meme stocks |
| C15 | 3 | retail creates opportunity, AI capex vs dot-com, emerging markets neglect, quantum computing |
| C16 | 1 | technology commercialization, career advice and sign-off |
| C17 | 0 | podcast legal disclaimer and outro |

## Claims

### C01
- **George Patterson** Model users must continuously check whether a model's assumptions still hold and whether the data regime has shifted.  #mech/research_method
  > are the assumptions behind the model still valid? Has there been some regime shift in the data?
  asset: multi · testable: partly - requires explicit assumption checks · confidence: high
  ^MT213-C01-1
- **George Patterson** Pure model output should be combined with market awareness and a multi-disciplinary team (economics, finance, computer science, math).  #mech/research_method
  > quantitative is a very useful tool but you also have to pay attention to what's going on in the market
  asset: multi · testable: no - process preference · confidence: high
  ^MT213-C01-2
- **George Patterson** As of mid-2026 PGIM's models see an overall positive macro environment for risk assets, with the US economy surprisingly resilient.  #mech/cycle_persistence _(time-bound view)_
  > We still see like an overall positive macro environment for risk assets.
  indicator: PGIM regime model · asset: multi · direction: pro-risk · horizon: months · conditions: mid 2026 · testable: partly - model not disclosed · confidence: medium
  ^MT213-C01-3

### C02
- **George Patterson** Better data and technology mean the large concentrated discretionary macro bets of the 1990s no longer exist; macro investing has become more systematic and nimble.  #mech/structural_shift
  > the big opportunities that the the macro concentrated traders have had in the '9s really just don't exist today
  asset: multi · horizon: years · testable: no - structural statement · confidence: medium
  ^MT213-C02-1
- **George Patterson** Web-scraped prices, behavior tracking and geospatial data now give a much tighter real-time view of consumers than monthly GDP.  #mech/research_method
  > web scraping prices we have um you know you can track behavior there's geospatial
  indicator: web-scraped prices, geospatial data · asset: multi · horizon: months · testable: yes - alternative data · confidence: high
  ^MT213-C02-2

### C03
- **George Patterson** The macro drivers (inflation, growth) are the same, but NLP on news feeds and foreign-language sources gives faster proxies than monthly or quarterly government data.  #mech/research_method
  > Now, with language processing, you can be monitoring news feeds.
  indicator: NLP news and text measures of inflation and growth · asset: multi · horizon: weeks · testable: yes - build text indices · confidence: high
  ^MT213-C03-1
- **George Patterson** 60/40 fails when bonds stop being defensive (1994, 2022) after sudden bond moves, although 60/40 remains a long-term core.  #mech/risk_management
  > where again, you had like uh sudden moves in the bond market that really cause bonds to not work as a defensive instrument
  indicator: 60/40 portfolio, stock-bond correlation · asset: multi · horizon: years · conditions: rate-shock inflationary regimes · testable: yes - historical returns · confidence: high
  ^MT213-C03-2
- **George Patterson** Institutions can now obtain diversification through overlays, convexity or downside protection and return stacking; retail has access to derivative income and protection products.  #mech/risk_management
  > you can become much more involved in overlays um or solutions that are going to give you a little bit of convexity or downside protection
  indicator: overlays, return stacking · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT213-C03-3

### C04
- **George Patterson** Privates cannot be traded without large discounts, so clients seek liquid, systematic ways to return to their strategic allocation.  #mech/liquidity_flows
  > you largely can't trade them unless you're willing to accept a material discount
  indicator: private markets liquidity · asset: multi · horizon: years · testable: no - client need · confidence: high
  ^MT213-C04-1
- **George Patterson** Since the Middle East military actions, markets have been dominated by one factor: oil up, inflation up, equities down (or the reverse), so one asset explains the rest.  #mech/behavioral _(time-bound view)_
  > there's been one principal component right it's been you know oil's up equity down
  indicator: oil price as principal component · asset: multi · direction: oil up: equities down · horizon: weeks · conditions: 2026 Middle East conflict · testable: yes - PCA of cross-asset returns · confidence: medium
  ^MT213-C04-2
- **George Patterson** PGIM uses language models to track how inflation is discussed plus flow monitoring, to treat inflation as a risk factor.  #mech/research_method
  > advanced language models to kind of see how people are talking about this in the marketplace
  indicator: LLM inflation narrative, market flows · asset: multi · horizon: weeks · testable: yes · confidence: medium
  ^MT213-C04-3
- **George Patterson** Rule of thumb: below about 4% inflation equities still do fine (commodities gain importance); above 4% there is material impact on fiscal policy and markets.  #mech/policy_reaction
  > if inflation's under 4% you can still do okay with equities
  indicator: inflation level, 4% threshold · asset: equities · direction: equities ok below 4%, trouble above · horizon: months · conditions: inflation near but under 4% · testable: yes - equity returns by inflation bucket · confidence: medium
  ^MT213-C04-4
- **George Patterson** In mid-2026 the oil-driven inflation rise is a genuine risk factor that will trim GDP growth but is not yet large enough to cause a recession or major downturn, and inflation is not expected to cross the roughly 4% threshold in the near term.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > It is definitely going to weigh on the economy and and shave a bit off of GDP
  indicator: inflation level versus the 4% threshold, oil price · asset: multi · direction: growth slightly lower, equities still acceptable below 4% inflation · horizon: months · conditions: inflation below about 4% · testable: yes - equity and growth outcomes by inflation bucket · confidence: medium
  ^MT213-C04-X1

### C05
- **George Patterson** Mid-horizon regime views come from fundamentals (forward rates, GDP, profits, jobs) and are combined with a short-term tactical view.  #mech/research_method
  > the mid- horizon view is much more tied to fundamentals
  indicator: forward rates, GDP, corporate profits, employment · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT213-C05-1
- **George Patterson** A tactical inflation-risk overlay shrank active exposures while staying pro-risk.  #mech/risk_management _(time-bound view)_
  > have caused us to kind of shrink some of our active exposures just because of the of the really the tactical overlay on top of that
  indicator: tactical overlay · asset: multi · direction: reduce active risk · horizon: weeks · conditions: elevated inflation risk · testable: partly · confidence: medium
  ^MT213-C05-2
- **George Patterson** Commodities are the best liquid inflation hedge, performing especially in inflation shocks, though they are the 'forgotten stepchild' of multi-asset; equities hedge only up to a threshold.  #mech/risk_management
  > commodities are still one of the best liquid tools
  indicator: commodity futures vs inflation shocks · asset: commodities · direction: long commodities in inflation shocks · horizon: months · conditions: inflation shocks · testable: yes · confidence: high
  ^MT213-C05-3
- **George Patterson** Macro indicators and forward rates point to a benign pro-risk backdrop; PGIM expects the current conditions to persist for roughly 3 to 6 months or to year-end, not reverting fully to earlier levels but probably not worsening.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > 3 to 6 months, end of the year, we expect, you know, things will be they're not going to go back to where they were, but they're not they're probably not going to get worse
  indicator: macro indicators, forward rates · asset: multi · direction: stay pro-risk · horizon: months · conditions: inflation shock stays contained · testable: no - one dated view · confidence: medium
  ^MT213-C05-X1
- **George Patterson** Real estate and infrastructure hedge inflation over the long term, while liquid commodities (energy has had huge returns this year on geopolitical risk) hedge in the short term, so the hedge is built from several instruments with different horizons.  #mech/risk_premium _(added by sonnet-xhigh cross-check)_
  > real estate infrastructure etc those all give you some long-term uh in you know hedging against inflation
  indicator: real assets, commodities versus inflation · asset: multi · direction: long real assets and commodities against inflation · horizon: years · conditions: inflation shocks favor commodities; real assets work over long horizons · testable: yes - inflation betas of real assets versus commodities by horizon · confidence: medium
  ^MT213-C05-X2

### C06
- **George Patterson** A Gaussian mixture model treats the economy as a latent state and classifies regimes from many data points.  #mech/research_method
  > Gaussian mixture model that basically views the world, views the economy as some sort of unobservable state
  indicator: Gaussian mixture regime classification · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT213-C06-1
- **George Patterson** The regime model avoids market prices because they move faster than the economy and would contaminate the medium-term economic state.  #mech/research_method
  > we don't use any like market-based data there because markets can move much faster than the overall economy
  asset: multi · horizon: months · testable: yes - ablation test · confidence: medium
  ^MT213-C06-2
- **George Patterson** Alongside statistical regime models they use a traditional growth/inflation framework (high and rising, high and falling).  #mech/cycle_persistence
  > where are we in inflation is inflation you know inflation high and rising you know high and falling
  indicator: inflation level and direction · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT213-C06-3
- **George Patterson** No single model is best; combine multiple regime and valuation models rather than trusting one scenario.  #mech/research_method
  > Often times what you really want to do is you want to combine multiple models together.
  asset: multi · testable: yes - ensemble vs single · confidence: high
  ^MT213-C06-4
- **George Patterson** The multi-asset portfolio is built to balance exposure to growth, inflation and relative valuation views together rather than being a pure growth or pure inflation bet.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > we don't have a portfolio that's just a growth portfolio or just an inflation portfolio. We're trying to balance all of those things together.
  indicator: growth, inflation and valuation signals · asset: multi · testable: partly - diversification across macro themes can be measured · confidence: medium
  ^MT213-C06-X1

### C07
- **George Patterson** Winners of Kaggle model competitions use multi-model ensembles, supporting the multi-model approach.  #mech/research_method
  > they're all multimodel the winners are usually like a multimodel approach
  asset: multi · testable: yes · confidence: medium
  ^MT213-C07-1
- **George Patterson** Analog thinking ('this is like year X') is a human pattern-matching bias; the thinking goes into model construction, then the model is used if assumptions hold.  #mech/behavioral
  > I think people do get a little too attached to like okay my you know my particular analysis says that you know we're in a regime we're in a regime just like a particular year in the past
  indicator: historical analogs · asset: multi · testable: no - process · confidence: medium
  ^MT213-C07-2
- **George Patterson** The hardest part of systematic investing is sticking to the process during losses and external pressure.  #mech/behavioral
  > the hardest part of this job is being patient and sticking with your guns
  asset: multi · conditions: drawdowns · testable: no · confidence: high
  ^MT213-C07-3
- **George Patterson** About 80% of the macro model is fundamentals-based, with a small price/statistical component.  #mech/research_method
  > most of the model probably 80% is really derived on fundamentals
  indicator: fundamental vs price inputs · asset: multi · horizon: months · testable: partly - model composition · confidence: medium
  ^MT213-C07-4
- **George Patterson** Purely statistical black-box models get abandoned in underperformance because they cannot be understood; models grounded in economic insight can be held.  #mech/behavioral
  > that's when you're going to get nervous and you're going to unplug it because you don't understand it
  asset: multi · conditions: when the model underperforms · testable: no · confidence: high
  ^MT213-C07-5

### C08
- **George Patterson** Macro has few independent observations, so models must be built with explicit priors and insight rather than regression coefficients dropped in.  #mech/research_method
  > the degrees of freedom is very very very few
  asset: multi · horizon: years · conditions: macro data · testable: yes - count effective observations · confidence: high
  ^MT213-C08-1
- **George Patterson** A small, shorter-term statistical component complements the fundamental macro model.  #mech/research_method
  > We do have some small statistical components um just because again you need to pay attention to those
  indicator: short-term statistical signals · asset: multi · horizon: weeks · testable: partly · confidence: medium
  ^MT213-C08-2
- **George Patterson** In COVID, data were released late and inputs (e.g. for cruise lines, airlines) did not update, requiring manual intervention; the investment philosophy comes before the model.  #mech/risk_management
  > you had to kind of get inter you had to intervene in the model because the updates the inputs were just not updated
  indicator: stale data inputs · asset: multi · horizon: weeks · conditions: data disruption crises · testable: no - judgement · confidence: high
  ^MT213-C08-3

### C09
- **George Patterson** Outright puts are expensive; downside protection is better paid for by replacing equity with long-dated call exposure and rebalancing.  #mech/risk_management
  > just going out and buying puts is expensive
  indicator: put cost, call substitution · asset: equities · direction: replace equity with calls · horizon: months · testable: yes - option backtest · confidence: high
  ^MT213-C09-1
- **George Patterson** Defensive equity strategies and sector rotation are other cheaper dynamic downside protection routes.  #mech/risk_management
  > more defensive equity strategies or you know sector rotation that kind of gives you a bit more downside protection
  indicator: defensive sectors · asset: equities · direction: rotate to defensives · horizon: months · testable: yes · confidence: medium
  ^MT213-C09-2
- **Alan Dunn** Long-volatility protection paid in COVID but not in 2022 because vol rose moderately without spiking while equities fell.  #mech/risk_management
  > 2022 when the equity market went down but volatility was moderately high without ever spiking very high and longv kind of strategies didn't provide an enormous amount of convexity
  indicator: VIX, long volatility · asset: equities · horizon: months · conditions: slow-grind selloffs · testable: yes - historical · confidence: medium
  ^MT213-C09-3
- **George Patterson** Language models are a rich source of data and alpha for both quant equity and multi-asset.  #mech/research_method
  > That's just been a very rich source of data and a rich source of alpha that we found.
  indicator: LLM text signals · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT213-C09-4
- **George Patterson** Text-signal methods evolved from bag-of-words counts to BERT/FinBERT sentiment to LLM theme detection, while keeping traceability to raw data.  #mech/research_method
  > in the early days it was like counting positive words versus negative words, which is called the bag of words method
  indicator: bag of words, FinBERT, LLM · asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT213-C09-5

### C10
- **George Patterson** Text (reports, websites, 10-Ks) is a rich data source, and extraction advances matter more for risk than for alpha.  #mech/research_method
  > the ability to extract things both on the alpha side, but more importantly on the risk side have become have just really advanced by leaps and bounds
  indicator: text mining · asset: multi · horizon: weeks · testable: yes · confidence: medium
  ^MT213-C10-1
- **George Patterson** BERT/FinBERT are surprisingly good at sentiment, and LLMs are effective at assessing tone of speeches and text versus past patterns.  #mech/research_method
  > Actually, Bird is surprisingly good or Finnbert's surprisingly good in terms of extracting sentiment.
  indicator: FinBERT sentiment of central bank speech · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT213-C10-2
- **George Patterson** LLMs are statistical next-token predictors only as good as their training data, so evaluation tasks must fit that.  #mech/research_method
  > all of these models are only as good as the data they've been trained on
  asset: multi · testable: yes · confidence: high
  ^MT213-C10-3
- **George Patterson** Automated bots may over-react to headlines and drive short-term moves, but evidence is hard to find.  #mech/crowding_positioning
  > there are, you know, automated strategies that are that are probably um, you know, in need of uh in in need of, you know, continual refinement and maybe driving prices in the short term
  asset: multi · horizon: days · testable: no - unobservable · confidence: low
  ^MT213-C10-4

### C11
- **George Patterson** PGIM keeps a human in the loop, with portfolio managers reviewing trades for consistency with the investment philosophy.  #mech/risk_management
  > It's not it's not kind of unconstrained robo trading.
  asset: multi · testable: no · confidence: high
  ^MT213-C11-1
- **George Patterson** AI follows past technology waves: it eliminates some jobs but creates others and boosts productivity.  #mech/structural_shift
  > yes certain types of jobs may get eliminated or reduced but other jobs are created
  asset: multi · horizon: years · testable: no - opinion · confidence: medium
  ^MT213-C11-2
- **George Patterson** Rate forward curves rarely predict policy accurately, often pricing hikes or cuts that never occur, so forecasts must be revised and managers nimble.  #mech/policy_reaction
  > rarely is it accurate. I mean it often times they're forecasting hikes which then never materialize
  indicator: forward curve implied policy rates · asset: rates · horizon: months · testable: yes - forward vs realized · confidence: high
  ^MT213-C11-3
- **Alan Dunn** In early 2026 the Citrini report pushed yields down in February, then the March strike in Iran reversed rates, moving the market from pricing cuts to possible hikes.  #mech/policy_reaction _(time-bound view)_
  > as we went into March, we had the strike in Iran and and we had a big reversal in rates
  indicator: yields, rate expectations · asset: rates · direction: yields up · horizon: months · conditions: Feb-Mar 2026 · testable: yes · confidence: high
  ^MT213-C11-4
- **George Patterson** Building and calibrating AI models is expensive, and nobody may yet be making money from them, so the productivity benefit arrives with high cost and uncertain commercial payoff.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > It costs, you know, hundreds of thousands or if not millions of dollars of time to calibrate these models
  indicator: AI model development cost · asset: equities · horizon: years · conditions: early stage of commercialization · testable: no - qualitative · confidence: low
  ^MT213-C11-X1

### C12
- **George Patterson** Unresolved US debt to GDP will hit a tipping point, but its timing has no formula, so a nimble stance is needed.  #mech/fiscal_debt
  > at some point they are going to become painful enough. We are going to you know hit the so-called tipping point.
  indicator: US debt to GDP, term premium · asset: rates · horizon: years · testable: no - timing unknowable · confidence: medium
  ^MT213-C12-1
- **George Patterson** Quant models have only a small edge (right slightly more than 50%); many small bets add up and give a smoother ride than big calls (Moneyball).  #mech/research_method
  > we want to be right a little bit more than 50% of the time
  indicator: hit rate, breadth · asset: multi · testable: yes · confidence: high
  ^MT213-C12-2
- **George Patterson** Prefer just enough model complexity to represent the world, leaning simple.  #mech/research_method
  > we want just enough complexity to to do like the to basically do what we need to do
  asset: multi · testable: partly · confidence: medium
  ^MT213-C12-3
- **Alan Dunn** Quant researchers are debating simplicity versus complexity: the long-held rule of parsimonious, few-input models has been challenged by research arguing that more complex models can be justified.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > there's a research piece came out saying no that's not correct actually that maybe there is a case uh for more complexity um which kicked off a whole debate
  asset: multi · testable: yes - compare out-of-sample performance of simple versus complex models · confidence: medium
  ^MT213-C12-X1

### C13
- **George Patterson** Optimizing in-sample performance is the worst error; ask what the sample captured and whether it will persist.  #mech/research_method
  > the absolute worst thing you can do is is optimize in sample performance
  asset: multi · testable: yes · confidence: high
  ^MT213-C13-1
- **George Patterson** Researchers must state what assumptions would make their research fail, with a devil's-advocate debate, to guard against overfitting.  #mech/research_method
  > what do you have to do to kill this research?
  asset: multi · testable: yes - procedural · confidence: high
  ^MT213-C13-2
- **George Patterson** With noisy data you can always find a period supporting any thesis, so economic findings must hold across periods.  #mech/research_method
  > you can always find some period to prove some thesis that you want, but it may not work all the time
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT213-C13-3
- **George Patterson** Freeze parameters at research time and compare live out-of-sample performance; signals are typically positive but weaker than expected.  #mech/research_method
  > if you freeze it at that point once we've gone live what has been the outof sample performance
  indicator: out-of-sample decay · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT213-C13-4
- **George Patterson** Researchers who want to make a name push to lift a strategy's information ratio (for example from 1 to 1.5), which creates an incentive to overfit in sample, so the team lead asks what would kill the research.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > how do I how do I turn this from a you know an IR of one to an IR of 1.5
  indicator: information ratio · asset: multi · conditions: junior researchers under career incentive · testable: partly - decay from in-sample to live IR can be measured · confidence: high
  ^MT213-C13-X1
- **George Patterson** Markets are non-stationary because participants' behavior changes over decades, so relationships found in any one sample need continuous monitoring and may not persist.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > they don't stay the same and that, you know, what people are doing today is very different than what they were doing 20 and 30 years ago
  asset: multi · horizon: years · testable: yes - rolling out-of-sample stability tests of signals · confidence: high
  ^MT213-C13-X2

### C14
- **George Patterson** Live signal performance is usually still positive but below the in-sample estimate.  #mech/research_method
  > usually it's like positive but not as positive as we thought it was
  indicator: signal decay · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT213-C14-1
- **George Patterson** If a signal decayed over about 3 months in sample, use somewhat shorter parameters going forward because the world is getting faster.  #mech/slow_reaction
  > if that's the case today's parameter should probably be somewhat shorter
  indicator: signal lookback · asset: multi · direction: shorten lookbacks · horizon: months · conditions: recent faster markets · testable: yes · confidence: medium
  ^MT213-C14-2
- **George Patterson** Policy responses and crashes are now faster (GFC slow, SVB overnight bank run, COVID record-short move), so shutoffs must be designed in up front.  #mech/policy_reaction
  > policy response is much faster now
  indicator: policy response speed · asset: multi · horizon: weeks · testable: partly · confidence: medium
  ^MT213-C14-3
- **George Patterson** Panic selling at the COVID bottom missed the rebound, so fast V-shaped moves reward staying with the process.  #mech/overshoot
  > If you if you got if you panicked at the bottom of COVID you really missed out on the rebound.
  indicator: COVID 2020 crash and rebound · asset: equities · horizon: weeks · conditions: fast policy-backstopped crises · testable: yes · confidence: high
  ^MT213-C14-4
- **George Patterson** Retail-driven meme stocks can move against a correct model in the short run, so position sizing must survive them.  #mech/crowding_positioning
  > you can be right in the long run but you just can't afford to maintain the position in the short run
  indicator: meme stocks · asset: equities · horizon: weeks · conditions: US equities · testable: partly · confidence: high
  ^MT213-C14-5
- **George Patterson** Irrational retail investors in equities are a feature that creates opportunity.  #mech/behavioral
  > that's a that's a feature that's not a problem
  indicator: retail participation · asset: equities · horizon: months · testable: partly · confidence: medium
  ^MT213-C14-6

### C15
- **George Patterson** Bonds are mostly institutional with fewer speculative extremes, whereas equities have retail flows that create opportunities, if one avoids the steamroller.  #mech/behavioral
  > in the equity market, you have retail investors and that's really creates a lot of opportunities
  indicator: retail participation · asset: equities · horizon: months · testable: partly · confidence: medium
  ^MT213-C15-1
- **George Patterson** Unlike 1999, today's mega-cap leaders have cash flows, though there are pockets of excess and the AI capex cycle's payoff is unproven.  #mech/overshoot _(time-bound view)_
  > the tech bubble was all about names that were not profitable
  indicator: mega-cap profitability, AI capex · asset: equities · horizon: years · conditions: mid 2026 · testable: partly · confidence: medium
  ^MT213-C15-2
- **George Patterson** Emerging markets have been ignored and changes in earnings plus long-term growth make institutions ask about them as a strategic opportunity.  #mech/structural_shift _(time-bound view)_
  > I think people have probably ignored emerging markets for a period of time.
  indicator: emerging market equities · asset: equities · direction: long EM · horizon: years · testable: partly · confidence: medium
  ^MT213-C15-3

### C16
- **George Patterson** New technologies such as quantum computing take long to move from lab to robust commercial scale, as with semiconductors.  #mech/structural_shift
  > it's going to take time for it to become commercially viable
  asset: other · horizon: years · testable: no · confidence: medium
  ^MT213-C16-1

