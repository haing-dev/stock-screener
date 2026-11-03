---
source_id: MT070
title: "Harding Rewrites Winton's Quant Playbook in Search for Returns"
date: 2019-03-18
channel: "Bloomberg Television"
url: 
words: 8225
claims: 35
added_by_opus: 2
corrections: 0
crosscheck: "opus cross-check"
speakers: ["David Harding (founder, Winton)", "interviewer (Bloomberg Television)"]
tags: [source, layer0]
---
# Harding Rewrites Winton's Quant Playbook in Search for Returns

**Speakers:** David Harding (founder, Winton); interviewer (Bloomberg Television)

**Summary:** Bloomberg TV (Mar 2019) interview with Winton founder David Harding on why systematic strategies struggle. Trend following in futures became crowded, near-zero rates cut hedge fund returns, so Winton shifted to equity event, organizational-metric and technical strategies across 7000 stocks. Warns government data are unreliable and trend following is not a crash hedge.

**Approach:** trend following, systematic quant, equity event strategies, crowding, research method

**Opus completeness estimate of first read:** 0.94 - first reader captured essentially all mechanisms, research findings and risk methods accurately; missed only the no-discretionary-intervention governance rule and the reason redemption terms were lengthened (asset liquidity)

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 3 | low rates and crowding, innovation, 7000 stock portfolios, high-frequency data |
| C02 | 5 | crowded trend following, jungle model, edge decay, leverage and catastrophe risk |
| C03 | 3 | leverage, future of quant, agricultural futures |
| C04 | 4 | weather/long data, government data revisions, PMI study, equity strategies |
| C05 | 3 | momentum transfer, AI hype, responsibility, trend following forecast lowered |
| C06 | 2 | trend Sharpe, new strategies, client redemptions |
| C07 | 2 | fee and liquidity terms, hedge fund beta, competitors |
| C08 | 4 | Renaissance, vol knob, vol history |
| C09 | 3 | volatility not rising, trend following as hedge, future of discretionary |
| C10 | 2 | AI view, Hivemind spin-off |
| C11 | 1 | cloud computing; philanthropy (no content) |
| C12 | 1 | IP and quant future; outlook |

## Claims

### C01
- **David Harding** Hedge fund returns are weak when interest rates are near zero (no cash return) and strategies are crowded, deteriorating return-to-risk.  #mech/crowding_positioning _(time-bound view)_
  > with very low in low to zero interest rates um it's pretty tough to make money in the hedge fund game at the moment
  indicator: policy interest rate level; strategy crowding · asset: multi · horizon: years · conditions: low-rate environment · testable: partly - compare fund returns vs cash rate · confidence: high
  ^MT070-C01-1
- **David Harding** Successful strategies attract too much capital, driving returns down and forcing innovation.  #mech/crowding_positioning
  > any business that succeeds and isn't a monopoly tends to get too much capital applied to it that's what drives innovation
  indicator: strategy capacity · asset: multi · horizon: years · testable: partly - returns vs AUM · confidence: high
  ^MT070-C01-2
- **David Harding** Uses high-frequency data to measure correlation changes and emergence of new factors even though trading is long term; computing in the cloud allowed portfolios of 7000 stocks (from ~1000-1500 five years ago), now a third to a half of weight.  #mech/research_method
  > we use short-term data even though we don't
  indicator: intraday data for correlation and factor emergence · asset: equities · testable: partly · confidence: high
  ^MT070-C01-3

### C02
- **David Harding** Trend following in futures has become crowded and is seen as beta: fast versions crowded first, slower ones now, so returns shrink and the firm shifted toward equity strategies.  #mech/crowding_positioning
  > the faster strategies got very crowded in futures many many years ago we managed to avoid that by getting slower but even the slower strategies i fear are beginning to get a bit crowded now
  indicator: trend following in futures · asset: multi · direction: less trend following in futures · horizon: years · testable: yes - trend returns by era · confidence: high
  ^MT070-C02-1
- **David Harding** Markets are an evolving ecosystem, not a perfectly efficient system; edges decay but new ones emerge, so innovation is needed.  #mech/structural_shift
  > they're more like a kind of thriving ecosystem jungle
  asset: multi · horizon: years · testable: no - conceptual · confidence: high
  ^MT070-C02-2
- **David Harding** A simple 2/20-day moving-average crossover made large returns in the 1980s, which no longer works the same way, showing edge decay in simple trend rules.  #mech/crowding_positioning
  > the two and twenty day moving average crossover system you would have made that like a bandit in the 80s
  indicator: 20-day moving average crossover · asset: multi · horizon: days · conditions: 1980s · testable: yes - backtest by decade · confidence: high
  ^MT070-C02-3
- **David Harding** Today's lower hedge fund returns partly reflect near-zero cash rates (6% in 80s-90s) and halved leverage; doubling track record and adding 6% looks similar to the past.  #mech/risk_premium
  > for most of the 80s and 90s risk-free rates were six so hedge funds had six percent added in
  indicator: cash rate; leverage · asset: multi · horizon: years · testable: yes - compare returns net of cash and leverage · confidence: high
  ^MT070-C02-4
- **David Harding** Leverage cut because crowdedness plus fat tails creates risk of overnight catastrophic moves (LTCM, 2008); responsible managers avoid systemic risk.  #mech/crowding_positioning
  > the crowdedness creates the the risk of catastrophe the risk of an overnight massive move
  indicator: crowding; leverage · asset: multi · direction: reduce leverage · horizon: days · conditions: crowded strategies · testable: partly · confidence: high
  ^MT070-C02-5

### C03
- **David Harding** Uses about 2x gross leverage in long-short portfolios, versus ~10x rumoured for Goldman Global Alpha, conservative especially when serving less sophisticated clients.  #mech/risk_management
  > our leverage in a similar portfolio would be a fraction of that two times instead of ten times
  indicator: gross leverage · asset: equities · testable: no · confidence: high
  ^MT070-C03-1
- **David Harding** Quant investing has a bigger future because markets will not become efficient; competition is fierce but spurs progress and finance is not a natural monopoly.  #mech/structural_shift
  > the markets are not going to suddenly become efficient and then all you know quantitative strategy managers are going to disappear mysteriously
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT070-C03-2
- **David Harding** Agricultural futures work uses very long-term strategies because capacity is limited and large capital cannot trade in and out.  #mech/liquidity_flows
  > we can't afford to move those markets we can't afford to move in and out with a scale of capital we're operating on we have to be taking big long-term positions
  indicator: agricultural futures capacity · asset: commodities · direction: long-term positions · horizon: years · conditions: large AUM · testable: no · confidence: high
  ^MT070-C03-3

### C04
- **David Harding** Grain price data go back 1,200 years; researching weather changes and long time series could underpin an ag trading system (not yet found).  #mech/research_method
  > in the case of the grains we have data going back 1 200 years
  indicator: grain prices; weather patterns · asset: commodities · horizon: years · testable: yes - long data series · confidence: low
  ^MT070-C04-1
- **David Harding** Government economic statistics are revised heavily (US 2009 double dip erased nine years later; Japan growth 0.4 vs 2.5), so real-time fundamental data are untrustworthy for systematic macro.  #mech/research_method
  > it's always been difficult using you know government produced statistics in countries has always been difficult because they're revised so often
  indicator: revisions to GDP statistics · asset: multi · horizon: years · testable: yes - vintage vs revised data · confidence: high
  ^MT070-C04-2
- **David Harding** A long-run study of the PMI as a forecaster of the economy for betting on stock industries had too little data to prove anything after two years and millions in cost, and sunk cost should not force a result.  #mech/research_method
  > we spent perhaps two years and several million pounds to try and it was totally inconclusive
  indicator: purchasing managers index · asset: equities · horizon: years · testable: yes - insufficient data is itself the finding · confidence: high
  ^MT070-C04-3
- **David Harding** Futures trend-following systems applied unchanged to equities fail; equity strategies need event, organizational/governance metrics and customised technical strategies across 7000 stocks.  #mech/structural_shift
  > just taking futures trend following systems and applying them to um equities doesn't work at all
  indicator: trend following signal on single stocks · asset: equities · testable: yes - backtest futures trend on stocks · confidence: high
  ^MT070-C04-4

### C05
- **David Harding** Some momentum know-how from futures carries over to global equity technical strategies.  #mech/cycle_persistence
  > there is some of our knowledge of how to trade momentum in futures that has been applicable to our global equity technical
  indicator: momentum · asset: equities · testable: yes · confidence: medium
  ^MT070-C05-1
- **David Harding** AI view: deep learning has made progress but is not general intelligence; there is 1 part reality and 9 parts hype; responsibility for algorithms must stay with named humans.  #mech/research_method
  > one part reality and nine parts hype
  asset: other · testable: no · confidence: high
  ^MT070-C05-2
- **David Harding** Trend following should be expected to make less money over time, so he has lowered expectations yearly and diversified into other strategies, not abandoned it.  #mech/crowding_positioning
  > i've been lowering my forecast for the success of trend following year by year for years and years
  indicator: trend following forecast return · asset: multi · direction: reduce reliance on trend · horizon: years · testable: partly - forecast decay of trend returns · confidence: high
  ^MT070-C05-3
- **David Harding** Governance of a fully systematic book: researchers write and run the programs, execution is done by separate teams, and humans step in only to correct program errors, not to override signals with discretionary views.  #mech/risk_management _(added by Opus)_
  > if the program you know miscalculated something we would um you know we would do something we we are responsible for managing the money
  asset: multi · conditions: fully systematic trading, 24-hour global execution · testable: no - organisational practice · confidence: high
  ^MT070-C05-X1

### C06
- **David Harding** Trend following delivered a Sharpe ratio near 1 for 30 years but too much money and competition now; innovators survive.  #mech/crowding_positioning
  > we had a short ratio of best nearly one for 30 years
  indicator: trend following Sharpe ratio · asset: multi · horizon: years · testable: yes - trend Sharpe by period · confidence: high
  ^MT070-C06-1
- **David Harding** New strategies are statistical like trend following: they cannot be forecast to work in a given period, so diversification and a long horizon matter; judge managers over many years not months.  #mech/research_method
  > the systems we're moving into have the same properties as trend flow in other words they're unpredictable they're statistical systems we can't forecast when they're going to work
  asset: multi · direction: diversify across statistical strategies · horizon: years · testable: no · confidence: high
  ^MT070-C06-2

### C07
- **David Harding** Fee and liquidity terms moved to monthly notice and annual crystallisation, with management fee cut from 1% to 0.9% and performance fee from 20% to 16% as returns did not justify fees.  #mech/new
  > we've always historically as part of the sort of futures uh uh tradition we've always charged quarterly performance fees and now that's nearly all annual
  asset: multi · testable: no · confidence: high
  ^MT070-C07-1
- **David Harding** Hedge fund returns were sustained by the equity bull market beta spillover.  #mech/risk_premium
  > hedge fund industry gets quite a lot of uh knock-on benefit from
  indicator: equity bull market · asset: equities · horizon: years · testable: yes - hedge fund returns vs equity beta · confidence: medium
  ^MT070-C07-2
- **David Harding** Fund redemption terms were lengthened (monthly notice, less liquid than before) because the strategy mix now holds more small-company equities, matching investor liquidity to the liquidity of the assets.  #mech/liquidity_flows _(added by Opus)_
  > our own funds have moved more into line with other hedge funds having you know having more no longer notice period says because they got more investments in small companies
  indicator: fund notice period vs asset liquidity · asset: equities · horizon: months · conditions: shift from liquid futures to broader equity universes · testable: no - business terms · confidence: medium
  ^MT070-C07-X1

### C08
- **David Harding** Aligned business: focused solely on client money, relevant to institutions.  #mech/new
  > the fact that we are exclusively focused on managing money for clients as opposed to having also managing our own money is very attractive
  asset: multi · testable: no · confidence: low
  ^MT070-C08-1
- **David Harding** Renaissance's edge is cumulative scientific research by a large team over ~20 years, not a single data item or magic number.  #mech/research_method
  > they have a large body of world-beating scientists who have carried out a research project and built a cumulative body of intellectual property
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT070-C08-2
- **David Harding** Volatility is controlled by a single leverage 'volume knob' (10, 20 or 30 vol), independent of strategy changes.  #mech/risk_management
  > we broadly control our volatility by setting the level of gearing there it is almost as simple as there being one number
  indicator: target volatility / gearing · asset: multi · testable: yes - vol targeting · confidence: high
  ^MT070-C08-3
- **David Harding** Prolonged low volatility (2006-07) preceded the financial crisis; volatility spikes (2016 vol derivatives, 2018) hurt returns and cannot be solved for.  #mech/overshoot
  > a storm is people thought a storm was coming but they couldn't imagine what the storm was going to be
  indicator: low volatility regime · asset: equities · horizon: years · testable: partly · confidence: medium
  ^MT070-C08-4

### C09
- **David Harding** Volatility is not rising: measured in percent, 1933-34 was the highest; point-based charts mislead, so use log charts.  #mech/research_method
  > the idea that the markets are getting more volatile um is a silly idea really
  indicator: percent volatility vs point volatility · asset: equities · horizon: years · testable: yes · confidence: high
  ^MT070-C09-1
- **David Harding** Trend following is not a reliable hedge: it hedged in 2008, 2001-02, but in a 1987-style crash or Feb 2018 managed futures funds were long and lost because trends were up.  #mech/risk_management
  > if the market crashed the ctas we're going to lose a lot of money
  indicator: CTA equity net position · asset: multi · horizon: days · conditions: sudden crash after a long uptrend · testable: yes - CTA returns in crashes · confidence: high
  ^MT070-C09-2
- **David Harding** Active managers without real edge face pressure from data and performance evaluation; many discretionary strategies are simpler than thought and can be automated, as trend following was.  #mech/structural_shift
  > the future is bad for anyone who hasn't isn't adding real value
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT070-C09-3

### C10
- **David Harding** Simple trend algorithm produced ~15% compounded for 20 years, showing intelligence is not what limits returns.  #mech/cycle_persistence
  > the algorithm that's done the money making for assist is not very intelligent because um you didn't have to be very intelligent to make money
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT070-C10-1
- **David Harding** Spun off the data-cleaning business (Hivemind) because clean data are the unglamorous prerequisite for research and AI training.  #mech/research_method
  > it does the messy tedious work of organizing and cleaning data series so that you can do research into those data series
  indicator: data cleaning · asset: other · testable: no · confidence: high
  ^MT070-C10-2

### C11
- **David Harding** Cloud computing lets him rent huge compute for a short time for large experiments instead of owning machines, making research more efficient.  #mech/research_method
  > now you can just rent you know 50 000 computers for a minute
  indicator: cloud compute · asset: other · testable: no · confidence: high
  ^MT070-C11-1

### C12
- **David Harding** No IP protection and no publication in quant finance means advances are kept secret and knowledge progresses slowly; he expects the word quant to disappear as everyone uses computers.  #mech/structural_shift
  > we have no intellectual property protection unlike you know the software business
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT070-C12-1

