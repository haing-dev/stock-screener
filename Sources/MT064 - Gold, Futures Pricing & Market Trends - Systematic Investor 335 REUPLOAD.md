---
source_id: MT064
title: "Gold, Futures Pricing & Market Trends - Systematic Investor 335 [REUPLOAD]"
date: 2025-03-18
channel: "Top Traders Unplugged"
url: 
words: 16759
claims: 112
added_by_crosscheck: 19
corrections: 5
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Niels Kaastrup-Larsen (host, Top Traders Unplugged)", "Rob Carver (systematic futures trader and author)"]
tags: [source, layer0]
---
# Gold, Futures Pricing & Market Trends - Systematic Investor 335 [REUPLOAD]

**Speakers:** Niels Kaastrup-Larsen (host, Top Traders Unplugged); Rob Carver (systematic futures trader and author)

**Summary:** Rob Carver answers listener questions on leverage, markets vs systems, ETFs vs futures, signal scaling and missing data, then covers the Quantica sizing paper (volatility sizing, skew vs Sharpe) and a minutes-to-decades momentum/mean-reversion paper. Also discusses gold futures borrowing costs and macro consequences of Trump policies (higher inflation, higher risk premium).

**Approach:** trend following, systematic futures, position sizing, momentum and mean reversion, risk management, research method, macro policy

**Cross-check completeness estimate of first read:** 0.88 - first reader caught almost every technical idea (carry/funding in gold, sizing, skew vs Sharpe, time-scale paper, Trump macro); gaps are fee-structure remarks, a few data points, speaker attribution slips, and the listener's candle idea.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | gold futures carry and London to US gold flow |
| C02 | 4 | gold borrowing cost spike, mixed signals, multi-strat fees |
| C03 | 3 | pass-through fee drag, transparency, pod performance fees |
| C04 | 3 | early 2025 trend following performance by sector, trend barometer |
| C05 | 2 | index returns Feb 2025, leveraged ETF drag |
| C06 | 4 | leveraged ETF decay, Kelly, return stacking |
| C07 | 4 | markets vs systems, correlation, carry, capital |
| C08 | 4 | signals, ETF vs futures testing, costs, liquidity |
| C09 | 3 | total return comparison, ETF access, forecast scaling |
| C10 | 5 | regression and scaling, objective, CTA research |
| C11 | 6 | research frontiers: execution, alt data, ML, risk management |
| C12 | 4 | execution budget, discretionary trade lesson, mean reversion question |
| C13 | 4 | absolute mean reversion, Occam, EMA vs breakout |
| C14 | 4 | lag, weighting functions, overfit nonlinear |
| C15 | 4 | missing data and interpolation |
| C16 | 4 | Quantica position sizing paper, skew |
| C17 | 5 | Sharpe vs skew, geometric return |
| C18 | 2 | terminal wealth simulation, leverage caution |
| C19 | 5 | Safari and Schmidhuber time scale paper |
| C20 | 5 | momentum and mean reversion horizons, data |
| C21 | 4 | Trump macro: midterms, tariffs, deportation, supply chains |
| C22 | 4 | Trump macro: regulation risk premium, funding shocks, net view |
| C23 | 5 | lead-lag of bonds and gold vs equities, trust |
| C24 | 3 | policy lag, bond safety, fourth turning |
| C25 | 0 | nothing actionable: sign-off |

## Claims

### C01
- **Rob Carver** Gold has no yield, so its futures premium over spot is driven mainly by the borrowing (funding) cost, with storage cost small when spread over large inventories.  #mech/risk_premium
  > the Futures price will depend on the Spot Price Plus any kind of yield that you earn on it um you know less any interest rates funding the position
  indicator: gold futures minus spot, carry · asset: commodities · testable: yes - futures-spot spread is observable · confidence: high
  ^MT064-C01-1
- **Rob Carver** Gold moving from London to US vaults (or ownership rights moving) created an inventory imbalance across warehouses in early 2025.  #mech/liquidity_flows _(time-bound view)_
  > according according to market reports what's happening is that um gold is basically um being moved from London to the US
  indicator: London vs US gold inventories · asset: commodities · horizon: weeks · testable: partly - based on market reports, unclear who is moving it · confidence: low
  ^MT064-C01-2
- **Rob Carver** Gold's early-2025 rise can be argued to come from political instability and uncertainty, while a separate technical factor (the futures funding squeeze) is the part he finds interesting.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > Gold's gone up which you know is one of these things that happens um the and the causes of it are kind of we could argue about instability and uncertainty politically
  indicator: gold price, political uncertainty · asset: commodities · direction: gold up · horizon: months · conditions: rising political instability · testable: partly - gold versus policy-uncertainty index · confidence: medium
  ^MT064-C01-X1

### C02
- **Rob Carver** Gold borrowing costs normally track the risk-free dollar rate of about 4.5-5%.  #mech/risk_premium
  > they normally follow pretty closely the the sort of quote unquote risk-free rates you'd expect them to be about kind of four and a half 5%
  indicator: gold lease/borrowing rate · asset: commodities · testable: yes · confidence: high
  ^MT064-C02-1
- **Rob Carver** Gold borrowing costs jumped to 10-12% annualized (December future about 150 points over spot) because of warehouse inventory imbalance.  #mech/liquidity_flows _(time-bound view)_
  > but actually they they've jumped up S like 10 11 12% which is just you know crazy because of this this weird imbalance in inventories across warehouses
  indicator: gold futures-spot premium, borrowing cost · asset: commodities · horizon: weeks · conditions: inventory imbalance · testable: yes - spread data · confidence: medium
  ^MT064-C02-2
- **Rob Carver** He holds long gold, silver and bitcoin from trend, but carry is negative because futures trade well above spot, giving conflicting trend and carry signals.  #mech/slow_reaction _(time-bound view)_
  > so it's one of those weird situations where you're kind of getting mixed signals from the the price movement and the carry movement
  indicator: gold trend forecast vs carry · asset: commodities · direction: long gold with negative carry · horizon: weeks · conditions: backwardation/contango extreme · testable: yes - signals computable · confidence: medium
  ^MT064-C02-3
- **Niels Kaastrup-Larsen** Bloomberg estimates multi-manager pass-through fund clients effectively pay 7 and 20 up to 15 and 20 once pass-through expenses are counted, versus a 2 and 20 benchmark.  #mech/structural_shift _(time-bound view)_
  > they estimate clients effectively paying something like 7 and 20 or even up to 15 and 20
  indicator: hedge fund fees · asset: other · horizon: years · testable: yes - fee data · confidence: medium
  ^MT064-C02-4
- **Niels Kaastrup-Larsen** Institutional pressure pushed hedge fund fees down from 2 and 20, but multi-strategy pass-through funds that charge expenses on top now make 2 and 20 look cheap by comparison.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > interestingly enough of course uh now actually the 220 model can be seen as pretty cheap
  indicator: all-in hedge fund fee load · asset: other · horizon: years · conditions: multi-manager pass-through structures · testable: partly - Bloomberg-type fee estimates · confidence: high
  ^MT064-C02-X1

### C03
- **Niels Kaastrup-Larsen** A multi-strategy pass-through fund earned about 15.2% before fees in 2023 but the client received only 2.8% (caption ambiguous), illustrating large fee drag.  #mech/structural_shift _(time-bound view)_
  > what the client got was 2.8%
  indicator: net vs gross hedge fund returns · asset: other · horizon: years · testable: yes - fund data · confidence: low
  ^MT064-C03-1
- **Rob Carver** Multi-strategy pod funds charge expenses to client accounts outside headline fees, so institutions comparing headline fees underestimate costs; transparency has gone backwards compared with retail UCITS.  #mech/structural_shift
  > there's all this money kind of Disappearing out the back door kind of almost invisibly
  indicator: hedge fund expense transparency · asset: other · horizon: years · testable: partly - requires fee disclosure · confidence: medium
  ^MT064-C03-2
- **Rob Carver** In fund-of-funds and pod models, winning managers are paid performance fees even when the overall portfolio loses, ratcheting up costs.  #mech/structural_shift
  > you'd have to pay performance fees to the managers that were doing well
  indicator: fee structure · asset: other · horizon: years · testable: yes - fee structure · confidence: medium
  ^MT064-C03-3
- **Niels Kaastrup-Larsen** Net-of-fee return is the most important figure for an investor, which is why high pass-through fees are tolerated while net results stay good.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > I have argued before um that of course the net return is the most important thing uh to some extent
  indicator: net vs gross returns · asset: other · conditions: only holds if net returns stay high · testable: no - evaluation principle · confidence: medium
  ^MT064-C03-X1
- **Niels Kaastrup-Larsen** The rapid inflow into multi-strategy pods must come from large institutions, and it is surprising that pension funds and insurers accept fee levels they would have fought in other hedge fund allocations.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check, time-bound view)_
  > I am surprised that some of these um Pension funds insurance companies etc etc are accepting the level of fees
  indicator: capital flows into multi-strategy funds · asset: other · horizon: years · testable: partly - AUM growth of pod funds vs fee data · confidence: medium
  ^MT064-C03-X2

### C04
- **Niels Kaastrup-Larsen** In early 2025 the currency sector was the one tricky area for trend followers, mostly in February.  #mech/slow_reaction _(time-bound view)_
  > the only thing I can kind of see from my vantage point that's been a little bit tricky this year has been the currency sector um and that's mostly been in February actually
  indicator: currency trend returns · asset: fx · horizon: weeks · testable: yes - sector returns · confidence: medium
  ^MT064-C04-1
- **Niels Kaastrup-Larsen** Equities, coffee, gold and some metals contributed for trend followers in early 2025 while CTA indices stayed near zero.  #mech/slow_reaction _(time-bound view)_
  > you would think things like eques have done well for Trend followers coffee even some of the metals you mentioned gold for sure
  indicator: SG CTA index · asset: multi · direction: long equities, coffee, gold · horizon: weeks · testable: yes - returns · confidence: medium
  ^MT064-C04-2
- **Niels Kaastrup-Larsen** His Trend barometer reading of 30 signals weak trend strength in the market, a different measure from index returns.  #mech/slow_reaction _(time-bound view)_
  > my own Trend barometer finished yesterday at 30 which is actually a week reading
  indicator: Trend barometer · asset: multi · horizon: weeks · testable: yes - barometer series · confidence: medium
  ^MT064-C04-3
- **Niels Kaastrup-Larsen** Even in UCITS funds the stated expense ratio can omit extra costs such as research costs that only show up in the detailed documents, so headline ratios may understate what investors pay.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > when you drill down there are some other cost like research cost etc etc that that crop up
  indicator: expense ratio vs total costs · asset: other · testable: yes - compare stated expense ratio with realised cost drag · confidence: medium
  ^MT064-C04-X1
- **Rob Carver** A 1% year-to-date result after seven weeks (down 1.5% in January, up 2.5% in February) is statistical noise, so short-window performance says nothing about a system.  #mech/research_method _(added by sonnet-xhigh cross-check, time-bound view)_
  > I'm up like 1% for the year so basically noise to be honest
  indicator: short-window strategy return · asset: multi · horizon: weeks · conditions: windows much shorter than a year · testable: yes - standard error of a Sharpe estimate over seven weeks · confidence: high
  ^MT064-C04-X2

### C05
- **Niels Kaastrup-Larsen** By mid-Feb 2025 trend indices were roughly flat (BTOP50 +1.68%, SG CTA +0.77%, SG Trend +0.57%), the short-term traders index was negative, MSCI World +3.79% and S&P 500 TR +3%.  #mech/slow_reaction _(time-bound view)_
  > btop 50 is up uh 46 basis points as of Tuesday uh up 1.68% uh so far this year so that's actually doing uh the best of all of the indices
  indicator: BTOP50, SG CTA, SG Trend, short-term traders index · asset: multi · horizon: months · conditions: early 2025 · testable: yes - index data · confidence: high
  ^MT064-C05-1
- **Rob Carver** Leveraged ETFs are dangerous for long holding because volatility drag makes down-then-up moves end below the start, worse with leverage.  #mech/risk_management
  > if they go down 10% and they go up 10% you actually end up down so you're not you know back where you started
  indicator: leveraged ETFs, volatility drag · asset: multi · direction: avoid leveraged ETFs · horizon: years · conditions: volatile underlying, long hold · testable: yes - arithmetic · confidence: high
  ^MT064-C05-2
- **Niels Kaastrup-Larsen** The 20+ year Treasury index fell 32 basis points in February 2025 after hot inflation figures, which hurt long-duration trend positions, but was still slightly positive for the year.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > obviously hit a bit by these new inflation numbers but still up 15 basis points so far this year
  indicator: S&P 20+ year Treasury bond index, US CPI surprise · asset: rates · direction: long bonds down on inflation surprise · horizon: weeks · conditions: February 2025 · testable: yes - bond index return versus CPI surprise · confidence: high
  ^MT064-C05-X1
- **Niels Kaastrup-Larsen** The short-term traders CTA index kept struggling in early 2025 (down in February and year to date), the second year in a row it lagged longer-horizon trend indices.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > the short-term Traders index down 18 basis points uh in fib and down uh 12 basis points in this year so far and continues to struggle
  indicator: SG Short-Term Traders Index · asset: multi · direction: faster trend following underperforms · horizon: months · conditions: choppy markets, higher turnover costs · testable: yes - SG index series by horizon · confidence: medium
  ^MT064-C05-X2

### C06
- **Rob Carver** A leveraged ETF on a very volatile underlying such as Strategy (a levered bitcoin proxy) would be dragged toward zero over time.  #mech/risk_management
  > over a long period of time with very volatile assets is the the value of these will tend drift down
  indicator: leveraged ETF on volatile asset · asset: equities · horizon: years · conditions: very high volatility · testable: yes - simulation · confidence: high
  ^MT064-C06-1
- **Rob Carver** Appropriate leverage depends on the Kelly criterion, which uses expected performance of the asset or strategy.  #mech/risk_management
  > the appropriate level of Leverage and risk depends on something called the the Kelly criteria
  indicator: Kelly criterion · asset: multi · testable: yes - formula · confidence: high
  ^MT064-C06-2
- **Rob Carver** Rule of thumb: risk above about 20-30% volatility is probably more than justified by expected performance, so 2x S&P ETFs (30-40% vol) are too much while 1.5x 60/40 (about 12-15% vol) is fine.  #mech/risk_management
  > the risk you're getting on something is more than about 20 25 30% it's potentially quite likely that that's going to be more than the amount of risk you should actually be taking
  indicator: portfolio volatility · asset: multi · direction: cap volatility near 20-25% · testable: yes - Kelly sizing testable · confidence: medium
  ^MT064-C06-3
- **Rob Carver** Return-stacked products (2x S&P plus managed futures) are safe only while the correlation between managed futures and equities stays low; if it rises, volatility exceeds a safe level.  #mech/crowding_positioning
  > if the correlation of of manag Futures and S&P stays relatively low then is going to have a lowish risk and then applying some leverage to it is going to be fairly safe
  indicator: managed futures/S&P correlation · asset: multi · horizon: years · conditions: correlation stays low · testable: yes - correlation measurable · confidence: medium
  ^MT064-C06-4

### C07
- **Rob Carver** Adding markets gives more diversification than adding similar trend systems because of correlation.  #mech/risk_management
  > it's quite likely you'll get more diversification from adding more markets than by adding further Trend falling systems
  indicator: correlation of added market vs added trend system · asset: multi · direction: add markets first · conditions: already-diversified trend system · testable: yes - correlation testable · confidence: high
  ^MT064-C07-1
- **Rob Carver** A new market has correlation about 0.4-0.5 to existing ones, whereas another trend system has about 0.8-0.9.  #mech/risk_management
  > the extra Market is going and are probably going to have a correlation of 04.5 with the ones that are in there something like that another Trend following system would might have a correlation of 8.9
  indicator: correlation · asset: multi · testable: yes - computable · confidence: medium
  ^MT064-C07-2
- **Rob Carver** Once a portfolio has many markets, a different style (e.g. carry, correlation about 0.5) adds more than further markets.  #mech/risk_management
  > at that point the the pendulum swings from you know more markets being better to a different system being better
  indicator: carry correlation to trend · asset: multi · direction: add carry or other styles · conditions: after many markets are included · testable: yes - marginal diversification testable · confidence: medium
  ^MT064-C07-3
- **Rob Carver** Adding systems needs no extra capital if automated, adding markets does, though complexity rises.  #mech/risk_management
  > adding systems is to be free as far as capital goes whereas adding markets isn't
  asset: multi · conditions: automated trading · testable: no - practical · confidence: medium
  ^MT064-C07-4
- **Rob Carver** A second trend system is highly correlated with the first because there are only so many ways to do trend following, even at different speeds, which is why new markets diversify more than new trend variants.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > because there's only so many ways you can do Trend following even if you're doing it at different speed it's going to be fairly similar
  indicator: correlation between trend systems · asset: multi · conditions: trend systems on the same market set · testable: yes - correlation of trend variants · confidence: high
  ^MT064-C07-X1

### C08
- **Rob Carver** Adding many signals with tiny marginal gains is not worth the complexity.  #mech/research_method
  > I wouldn't just add a thousand different signals to my model just just because they all might produce a tiny marginal increase
  asset: multi · testable: partly - marginal benefit testable · confidence: medium
  ^MT064-C08-1
- **Rob Carver** Back test with the instrument you will trade: futures for futures, ETFs for ETFs (test what you trade, trade what you test).  #mech/research_method
  > if you're going to trade Futures then you really probably should be using Futures to actually testing with
  asset: multi · testable: yes - methodological · confidence: high
  ^MT064-C08-2
- **Rob Carver** An ETF wrapper usually costs more than futures: fees, provider profit and higher slippage from size.  #mech/structural_shift
  > all the things being equal I would expect the ETF to cost more money
  indicator: ETF expense ratio vs roll costs · asset: multi · horizon: years · testable: yes - cost comparison · confidence: medium
  ^MT064-C08-3
- **Niels Kaastrup-Larsen** ETF liquidity is variable, which matters when substituting ETFs for futures.  #mech/liquidity_flows
  > a lot of ETFs have been issued but they don't all have very good liquidity frankly
  indicator: ETF liquidity · asset: multi · testable: yes - volume/spread · confidence: medium
  ^MT064-C08-4
- **Rob Carver** To compare an ETF with futures, estimate your own annual roll cost and compare it with the ETF's total annual expense ratio, checking that the ratio includes all costs.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > you should be able to get a rough idea of how much it's going to cost you to roll and then compare that with the the um total annual expense ratio of the ETF
  indicator: futures roll cost vs ETF total expense ratio · asset: multi · horizon: years · testable: yes - cost accounting · confidence: high
  ^MT064-C08-X1

### C09
- **Rob Carver** Compare ETF and futures on total return: ETF includes dividends/interest less costs; futures back-adjusted prices need the risk-free rate added because margin earns interest.  #mech/research_method
  > essentially you want to be Computing a what I'd call A A true Total return Series
  indicator: total return series · asset: multi · testable: yes - methodological · confidence: high
  ^MT064-C09-1
- **Rob Carver** ETFs are useful for market access and small contract size (fractional shares) when capital is limited, but with enough capital futures are better.  #mech/structural_shift
  > the reason why you would want to go down the ETF route would potentially be Market access and contract size
  indicator: contract size · asset: multi · conditions: small capital · testable: no - practical · confidence: medium
  ^MT064-C09-2
- **Rob Carver** A signal (feature) is turned into a forecast by scaling it, like a z-score, so it says how big the forecast is.  #mech/research_method
  > if it's positive then I'm bullish if it's negative I'm bearish
  indicator: forecast scaling · asset: multi · testable: yes - methodological · confidence: high
  ^MT064-C09-3

### C10
- **Rob Carver** Regress volatility-normalized returns on the signal: the coefficient equals the forecast scaling, so regression and scaling are the same thing.  #mech/research_method
  > the coefficient on the regression is going to be something that tells you how big the wiggly line is you know is this a big forecast or a small forecast
  indicator: regression beta as forecast scale · asset: multi · testable: yes - methodological · confidence: high
  ^MT064-C10-1
- **Rob Carver** The regression intercept removes systematic long or short bias, which he prefers not to remove.  #mech/research_method
  > that's just a way of essentially removing any systematic bias from forecasts that are systematically long or systematically short which you may not want to do by the way
  indicator: regression alpha · asset: multi · testable: yes · confidence: medium
  ^MT064-C10-2
- **Rob Carver** The target of a forecast should be risk-adjusted returns because positions are sized by risk.  #mech/research_method
  > I would always be trying to forecast risk adjusted returns
  indicator: volatility-normalized return · asset: multi · testable: yes · confidence: high
  ^MT064-C10-3
- **Rob Carver** Some CTAs run unchanged models for years and it can still be a valid approach.  #mech/research_method
  > ctas that that you know have not changed their model for years not done any any research and just plugging in one quite quite happily
  asset: multi · horizon: years · testable: no - observation · confidence: medium
  ^MT064-C10-4
- **Rob Carver** Research at big CTAs is often adding new markets (such as AHL Evolution), which can give the biggest return for effort.  #mech/research_method
  > they could be doing things like for example implementing new markets
  asset: multi · direction: add markets · horizon: years · testable: partly · confidence: medium
  ^MT064-C10-5

### C11
- **Rob Carver** Execution matters more as assets grow; a big fund trading billions notional should invest in execution.  #mech/risk_management
  > the bigger bigger you are the more important execution is
  indicator: execution costs · asset: multi · conditions: large AUM · testable: yes · confidence: high
  ^MT064-C11-1
- **Rob Carver** Alternative data is a growth area for research.  #mech/structural_shift
  > people looking at alternative sources of data and and that's also quite a big growth area
  indicator: alt data · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT064-C11-2
- **Rob Carver** Neural networks and ML on existing data are less likely to add value; he is wary of teams focused exclusively on them (Renaissance excepted).  #mech/research_method
  > but I'll be very wary of any any any sort of team of researchers that were purely you know focusing exclusive on that area of improvement
  indicator: machine learning on existing data · asset: multi · horizon: years · testable: no - opinion · confidence: medium
  ^MT064-C11-3
- **Niels Kaastrup-Larsen** Few new ways of doing trend following exist, but combining more than one approach (e.g. moving average crossover plus another) may give better results.  #mech/research_method
  > I don't think necessarily that uh as an industry we're coming up with many new ways of doing Trend following
  indicator: trend following methods · asset: multi · horizon: years · testable: partly - combination testable · confidence: medium
  ^MT064-C11-4
- **Niels Kaastrup-Larsen** Risk management and risk forecasting offer the most room for evolution in trend following.  #mech/risk_management
  > where where I would suspect we see the most Evolution still and where there's still room to improve is probably risk management
  indicator: risk forecasting · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT064-C11-5
- **Niels Kaastrup-Larsen** Trend followers rarely blow up unless they run highly leveraged versions.  #mech/risk_management
  > it's rare um that you hear about a trend follower blowing up uh unless it's specifically because they were running like a 5x leverage version of their strategy
  indicator: leverage · asset: multi · horizon: years · conditions: excess leverage · testable: no - observation · confidence: medium
  ^MT064-C11-6
- **Rob Carver** A small trader can get decent execution from a simple algorithm only a few lines long, whereas execution becomes a major research area only for funds trading hundreds of millions or billions of notional a day.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > for me I can do pretty decent job of execution with an algorithm there a few lines of code long
  indicator: execution cost vs fund size · asset: multi · conditions: scales with traded notional · testable: partly - slippage versus size · confidence: high
  ^MT064-C11-X1
- **Niels Kaastrup-Larsen** Besides new data sources, firms are researching how to pre-process data before it enters the trading algorithms, which is an active frontier of improvement.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > it's actually also what to do with the data before they stick it into their uh algorithms that I think is is an area of of interest for these firms
  indicator: data cleaning and transformation · asset: multi · testable: partly - ablation of pre-processing steps · confidence: medium
  ^MT064-C11-X2

### C12
- **Rob Carver** AHL says 35-40% of research budget goes to execution to avoid losing out as inflows grow, raising strategy capacity.  #mech/risk_management
  > probably of the research budget 35 40% of that goes to of course execution
  indicator: execution share of research budget · asset: multi · horizon: years · testable: no - firm claim · confidence: medium
  **Correction (cross-check):** Wrong speaker and hedged source. Niels recalls a conversation from the SG CTA index interview series, saying 'I think maybe was AHL' said that probably 35-40% of the research budget goes to execution. Rob Carver does not say it. → Niels (recalling an interview in the SG CTA index series, possibly with AHL, said with some doubt) says that perhaps 35-40% of the research budget goes to execution to avoid losing out as inflows grow and capacity increases.
  ^MT064-C12-1
- **Rob Carver** His discretionary bond trade caught the yield top but was closed flat because he had no predefined stop or exit criteria; he concludes he should stay systematic.  #mech/behavioral
  > I made made a good entry decision but a poor exit decision
  indicator: discretionary bond trade · asset: rates · horizon: months · testable: no - single trade · confidence: high
  ^MT064-C12-2
- **Niels Kaastrup-Larsen** Moskowitz et al. (2012) show returns in years 2 through 5 are negatively related to subsequent returns, supporting a long-term mean reversion signal.  #mech/cycle_persistence
  > the authors show that returns returns years 2 through five are negatively related to subsequent returns
  indicator: past returns years 2-5 · asset: multi · horizon: years · testable: yes - published paper · confidence: high
  **Correction (cross-check):** Speaker is the listener Paul, whose written question Niels reads out, not Niels; the Moskowitz et al. (2012) reading is the listener's. → Listener Paul (read by Niels): Moskowitz, Ooi and Pedersen (2012) find returns in years 2 to 5 are negatively related to subsequent returns, so an absolute long-term mean reversion signal might raise standalone Sharpe.
  ^MT064-C12-3
- **Niels Kaastrup-Larsen** Rob's five-year relative mean reversion strategy has a negative Sharpe but improves a baseline trend-plus-carry portfolio.  #mech/research_method
  > the strategy has a negative sharp ratio but improves the performance of his Baseline Trend plus carrier strategy
  indicator: long-term mean reversion · asset: multi · horizon: years · conditions: combination with trend and carry · testable: yes · confidence: high
  **Correction (cross-check):** Speaker is the listener Paul (question read by Niels), describing Rob's strategy in his book; not Niels's own view. → Listener Paul (read by Niels): Rob's relative five-year mean reversion strategy in Advanced Futures Trading Strategies has a negative standalone Sharpe but improves a baseline trend-plus-carry portfolio.
  ^MT064-C12-4
- **Rob Carver** A systematic trader can attribute every trade's result exactly because all trades are in a database, whereas discretionary calls are rarely recorded, so their quality is hard to judge afterwards.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > if you ask me how a particular trade works out I can tell you with Precision because it's all in a big database
  indicator: trade-level record keeping · asset: multi · testable: no - process point · confidence: high
  ^MT064-C12-X1

### C13
- **Rob Carver** Absolute long-term mean reversion (negative multi-year momentum) should work in principle and is simpler than relative mean reversion and probably diversifying.  #mech/cycle_persistence
  > which is just negative momentum um so this should definitely work
  indicator: absolute long-term mean reversion · asset: multi · horizon: years · testable: yes - testable · confidence: medium
  ^MT064-C13-1
- **Rob Carver** Long-term signals are hard to show significant and may show a negative Sharpe in a back test.  #mech/research_method
  > there's a long-term signal it's going to be quite hard to get statistical significance
  indicator: long-term mean reversion · asset: multi · horizon: years · conditions: few independent observations · testable: yes - statistical · confidence: high
  ^MT064-C13-2
- **Rob Carver** Prefer the simplest version of a strategy (Occam's razor).  #mech/research_method
  > in terms of aom's Razor you know should always go for the simplest possible version of something
  asset: multi · testable: no - principle · confidence: high
  ^MT064-C13-3
- **Listener Samuel (question read by Niels)** EMA crossovers versus Donchian breakouts give similar back tests on a diversified basket.  #mech/slow_reaction
  > systematically don't change back tests all that much on a diversified basket
  indicator: EMA crossover vs Donchian breakout · asset: multi · horizon: years · conditions: diversified basket · testable: yes - back test · confidence: medium
  ^MT064-C13-4
- **Rob Carver** Long-term mean reversion in prices has an academic literature in equities (Thaler and others) and is related to the value effect, which supports a multi-year contrarian signal.  #mech/overshoot _(added by sonnet-xhigh cross-check)_
  > there's papers by people like Richard Thor and stuff on on moon reversion um and um you know it sort of related to the value effect and Equity
  indicator: multi-year past return vs subsequent return · asset: equities · direction: past long-term losers outperform · horizon: years · conditions: multi-year horizon, weak statistical power · testable: yes - long-horizon return reversal tests · confidence: medium
  ^MT064-C13-X1
- **Listener Samuel (question read by Niels)** Listener idea: scale trend exposure up or down according to the current state of monthly, quarterly or yearly candles, instead of rolling-window breakout or EMA signals, so exposure falls at once if a strong quarter turns.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > why not look at the current state of high time frame candles to increase exposure progressively
  indicator: monthly/quarterly/yearly candle state · asset: multi · direction: raise exposure as higher-timeframe candle confirms trend · horizon: months · testable: yes - calendar-period candle signals versus rolling signals · confidence: low
  ^MT064-C13-X2

### C14
- **Rob Carver** All indicators lag; lag can be reduced by shorter windows or weighting recent periods more, as in an EMA.  #mech/slow_reaction
  > we can reduce it by using less of the past and more recent periods
  indicator: moving average, EMA · asset: multi · testable: yes · confidence: high
  ^MT064-C14-1
- **Rob Carver** Moving averages and EMAs are weighting functions of past returns (flat or exponential).  #mech/research_method
  > both the moving average and exponential moving average and indeed any indicator that takes series of past returns is is a waiting function over those past returns
  indicator: weighting function · asset: multi · testable: yes · confidence: high
  ^MT064-C14-2
- **Rob Carver** Nonlinear responses to recent observations add parameters and risk overfitting.  #mech/research_method
  > I'm not generally a fan of um sort of nonlinear stuff um because it it's it it's not very intuitive and also it's highly potentially highly it could be highly overfit
  asset: multi · testable: yes - out-of-sample test · confidence: medium
  ^MT064-C14-3
- **Rob Carver** A separate short-horizon mean-reversion signal added tiny insignificant performance and was not worth the complexity.  #mech/research_method
  > I've judged that the complexity they add is not worth the tiny tiny insignificant performance that they had
  indicator: one-week mean reversion · asset: multi · horizon: weeks · testable: yes - own test · confidence: medium
  ^MT064-C14-4

### C15
- **Rob Carver** When contracts are delisted and relisted, the simplest approach is to ignore data before relisting.  #mech/research_method
  > the easiest thing to do is to ignore any data before February 2023 so basically ignore the period it was trading earlier and you know obviously ignore the Gap
  indicator: missing futures data · asset: commodities · testable: yes - data handling · confidence: high
  ^MT064-C15-1
- **Rob Carver** Better is a trading system that handles missing data by going flat until enough prices exist to form forecasts and volatility.  #mech/research_method
  > you'd be trading this thing until due 2020 and then you'd go to a position of zero until the price prices started coming in again
  indicator: missing data · asset: commodities · testable: yes · confidence: high
  ^MT064-C15-2
- **Rob Carver** Do not interpolate missing prices in back tests; 99.9% of the time it is wrong.  #mech/research_method
  > I would really really not interpolate data price data and then use that in a back test and say oh yes look at this is great I think it's a fundamentally stupid thing to do
  indicator: interpolation · asset: multi · testable: yes · confidence: high
  ^MT064-C15-3
- **Rob Carver** Interpolating is reasonable only for volatility estimation across overnight hours, using a Brownian bridge rather than cointegration/ECM.  #mech/research_method
  > estimating um a volatility and you've got hourly data but obviously you've got a period when markets are closed then it's probably a reasonable thing to do to get a better estimate of volatility
  indicator: hourly volatility estimate · asset: multi · horizon: hours · testable: yes · confidence: medium
  ^MT064-C15-4
- **Rob Carver** A chatbot's suggestion to fill missing contract data with cointegration or error-correction models is the kind of plausible but unsound advice he distrusts, so AI-suggested data repairs need expert review before use in a backtest.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > I'm not surprised that chat B GPT has suggested it because you know um I'm not a big a big fan of AI
  asset: other · testable: no - opinion on a tool · confidence: medium
  ^MT064-C15-X1

### C16
- **Rob Carver** Three position-sizing methods: fixed contracts, fixed notional, and fixed risk (volatility-scaled); Quantica finds volatility adjustment has the highest Sharpe.  #mech/risk_management
  > the third methodology is the methodology I use which is to say I want I want to get a certain number amount of risk on my contract
  indicator: position sizing, volatility · asset: commodities · testable: yes - Quantica paper · confidence: high
  ^MT064-C16-1
- **Rob Carver** Volatility-adjusted sizing has the highest Sharpe ratio (cocoa 2024 example).  #mech/risk_management
  > they come to the conclusion that the volatility adjustment has the highest shot ratio
  indicator: volatility-targeted sizing · asset: commodities · horizon: years · testable: yes · confidence: high
  ^MT064-C16-2
- **Rob Carver** Fixed-contract or fixed-notional sizing produces more positive skew (explosive moves like cocoa hit an unscaled position), as losers are closed.  #mech/risk_management
  > the closer to your sort of fixed position sizing the system you're running or even the noal position sizing the the greater the the ski you'll get
  indicator: skew by sizing method · asset: commodities · horizon: years · testable: yes - own work · confidence: high
  ^MT064-C16-3
- **Rob Carver** For leveraged futures traders volatility can be scaled freely so Sharpe is the measure, but skew cannot be created by leverage.  #mech/risk_premium
  > effectively the price of risk is is basically zero for a leverage Trader we can get any amount of risk that we want to get
  indicator: Sharpe ratio, skew · asset: multi · testable: no - conceptual · confidence: high
  ^MT064-C16-4

### C17
- **Niels Kaastrup-Larsen** Option selling and equity market neutral strategies have high Sharpe but negative skew, unlike trend following.  #mech/risk_premium
  > be something like um a equity Market neutral strategy they they tend to have um negative skew as well
  indicator: skew · asset: multi · testable: yes · confidence: medium
  **Correction (cross-check):** Wrong speaker. Rob Carver is speaking here, continuing his explanation of the Sharpe versus skew trade-off (the sentence runs across the C16/C17 boundary); Niels does not speak until later in C17. → Rob Carver: option selling (extreme) and equity market neutral (less extreme) strategies have good Sharpe ratios but negative skew, unlike trend following which has positive skew.
  ^MT064-C17-1
- **Rob Carver** The Sharpe ratio worth sacrificing to buy positive skew is small, so the higher Sharpe strategy is generally better.  #mech/risk_premium
  > the amount of Shar ratio you should be giving up to sort of quote unquote buy positive skew was actually very small
  indicator: Sharpe versus skew tradeoff · asset: multi · direction: prefer higher Sharpe · horizon: years · testable: yes - simulation · confidence: medium
  ^MT064-C17-2
- **Rob Carver** The geometric mean return (CAGR) maximizes terminal wealth and should be the key metric.  #mech/research_method
  > maximizing that basically maximizes the am amount of money that you have at the end of at the end of your investment Horizon
  indicator: geometric mean return, CAGR · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT064-C17-3
- **Rob Carver** Sharpe ratio is valid only when compared strategies have the same skew.  #mech/research_method
  > Shar ratio you know only works if everything has the same skew
  indicator: Sharpe ratio · asset: multi · testable: yes · confidence: high
  ^MT064-C17-4
- **Rob Carver** The lower Sharpe from constant-contract or constant-notional sizing cannot be justified by skew improvement.  #mech/risk_management
  > conceivable amount of improvement in skew that would justify that that lower shot ratio
  indicator: position sizing · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT064-C17-5
- **Rob Carver** Preference for positive skew is subjective: some investors will give up Sharpe to get it, but his risk-neutral, terminal-wealth analysis shows the Sharpe worth sacrificing for skew is small.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > in practice people have preferences to this sort of thing so some people really like positive skew and they'll you know happily give up more of them their aot ra to get it
  indicator: skew vs Sharpe trade-off · asset: multi · conditions: investors without special skew preference · testable: yes - utility or terminal-wealth simulation · confidence: medium
  ^MT064-C17-X1

### C18
- **Rob Carver** Simulating terminal wealth for different Sharpe and skew combinations shows the benefit of higher Sharpe outweighs lost upside volatility, so Sharpe can be optimised despite penalising upside volatility.  #mech/research_method
  > the additional benefits of of having a higher shot ratio massively more than compensate for the fact that we're not getting those big upside volatility moments
  indicator: Sharpe, skew, terminal wealth · asset: multi · horizon: years · testable: yes - simulation · confidence: medium
  ^MT064-C18-1
- **Rob Carver** Be cautious of high-Sharpe strategies that need much leverage or are opaque, since the back test may hide negative skew risk (Madoff).  #mech/risk_management
  > we should always be careful of high shot ratio strategies that require a lot of Leverage
  asset: multi · testable: partly · confidence: high
  ^MT064-C18-2

### C19
- **Rob Carver** Momentum works empirically across futures from about a month to a year, while multi-year periods show mean reversion.  #mech/slow_reaction
  > momentum seems to work well um empirically um certainly in Futures across multiple asset classes for time periods of say a month up to a year
  indicator: momentum 1m-12m · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT064-C19-1
- **Rob Carver** At very short horizons mean reversion works because HF traders buy bid and sell ask around a bouncing price.  #mech/liquidity_flows
  > mean reversion tends to work well because that's where the high frequency Traders are operating
  indicator: high-frequency price · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT064-C19-2
- **Rob Carver** Safari and Schmidhuber find mean reversion at horizons below an hour, strongest around 5 minutes.  #mech/cycle_persistence
  > for time periods of less than an hour mean reversion occurs okay um and the most I think the most me verion occurs at um roughly a five or five minute time window
  indicator: sub-hourly returns · asset: multi · horizon: days · conditions: sub-hour windows · testable: yes - published paper · confidence: medium
  ^MT064-C19-3
- **Rob Carver** Trading at 5-minute mean reversion horizons needs large engineering and testing effort.  #mech/risk_management
  > trading at those kinds of frequencies is a massive engineering and back testing exercise and it's not something that you should be casually doing
  indicator: high-frequency trading · asset: multi · horizon: days · testable: no - practical · confidence: high
  ^MT064-C19-4
- **Rob Carver** The paper fits a cubic polynomial across a very wide range of time frequencies to classify each horizon as momentum or mean reversion.  #mech/research_method
  > they look at probably the widest range of of time frequencies I've seen in any paper ever
  indicator: trend strength by horizon · asset: multi · testable: yes · confidence: medium
  ^MT064-C19-5

### C20
- **Rob Carver** Momentum prevails from about one hour out to one year (days, weeks, months), supporting CTAs.  #mech/slow_reaction
  > as long as long as you're not really a really fast Trader you should probably be a momentum Trader
  indicator: momentum 1 hour to 1 year · asset: multi · direction: long momentum · horizon: months · conditions: not a very fast trader · testable: yes - published paper · confidence: high
  ^MT064-C20-1
- **Rob Carver** Beyond a year the data show mean reversion, so a 2-4 year horizon favors a mean reversion strategy.  #mech/cycle_persistence
  > anything longer than a year is is when mean reversion kicks in
  indicator: multi-year returns · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT064-C20-2
- **Rob Carver** The paper uses data from 1692, about 330 years, and finds mean reversion out to long horizons.  #mech/research_method
  > they look at data out 16 years and they're still finding mean reversion out there and to do that they're looking at data from 1692
  indicator: long historical data · asset: multi · horizon: years · testable: yes - published paper · confidence: medium
  ^MT064-C20-3
- **Rob Carver** Trend following at short frequencies is hard because trading costs are hard to overcome.  #mech/risk_management
  > trading costs in particular are going to be very hard to overcome if you Trend following it short time frequencies
  indicator: trading costs · asset: multi · horizon: days · conditions: short horizons · testable: yes · confidence: high
  ^MT064-C20-4
- **Rob Carver** Trend lookbacks up to about 18 months may work; one year is strong and two years flat in the paper.  #mech/slow_reaction
  > two years is pretty much flat so you might get away with 18 months
  indicator: trend lookback length · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT064-C20-5

### C21
- **Rob Carver** A president who starts with majorities usually loses one in the midterms, so Trump has about two years to legislate.  #mech/seasonality _(time-bound view)_
  > majorities in the midterms that happens nearly all the time mainly because people just don't like sitting you know they don't like sitting governments
  indicator: US midterm elections · asset: other · horizon: years · testable: yes - historical record · confidence: medium
  ^MT064-C21-1
- **Rob Carver** Tariffs increase inflation in the US and globally through retaliation.  #mech/policy_reaction _(time-bound view)_
  > they won't just increase inflation the US will increase inflation globally I think um for sure you know would due to retaliation
  indicator: tariffs, inflation · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT064-C21-2
- **Rob Carver** Mass deportations cut labor supply and lift wages, adding to inflation.  #mech/policy_reaction _(time-bound view)_
  > simple supply and demand if you reduce the amount of Labor uh in the market um then that will probably increase wage costs
  indicator: labor supply, wages · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT064-C21-3
- **Rob Carver** Supply chains are fragile, so deportations and tariffs may cause shortages and inflation.  #mech/structural_shift _(time-bound view)_
  > what covid really showed us is that the the sort of network of Supply chains in the world is a very delicate and delicate thing
  indicator: supply chains · asset: commodities · horizon: months · testable: no - qualitative · confidence: medium
  ^MT064-C21-4
- **Rob Carver** Tariffs face the most pushback from Republicans and other people the president listens to, so tariff plans are the policy most likely to be diluted or reversed.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > it's probably the one of his policies that there's the most push back from in by people who actually he's going to listen to
  indicator: US tariff announcements and reversals · asset: multi · horizon: months · conditions: depends on how much he gets done before the midterms · testable: no - political forecast · confidence: low
  ^MT064-C21-X1

### C22
- **Rob Carver** Tariffs on integrated US-Canada auto supply chains would be inflationary.  #mech/policy_reaction _(time-bound view)_
  > Us cars bits of cars go backwards and forwards between Canada and and the us across the border
  indicator: auto supply chain · asset: multi · horizon: months · testable: no - qualitative · confidence: medium
  ^MT064-C22-1
- **Rob Carver** Unstable regulation, rule of law and frequently changed tariffs increase the risk premium, which is bad for equities.  #mech/risk_premium _(time-bound view)_
  > increase um you know what in Economist will call the risk premium so people will demand to be paid more um to hold risky assets
  indicator: equity risk premium · asset: equities · direction: short or avoid equities · horizon: months · conditions: policy uncertainty · testable: partly - ex ante view · confidence: medium
  ^MT064-C22-2
- **Rob Carver** Stopping government payments could cause unemployment, supply and demand shocks and uncertainty.  #mech/policy_reaction _(time-bound view)_
  > potentially it's going to make people unemployed it's going to cause Supply shocks it's going to cause demand shocks it's going to cause uncertainty
  indicator: government spending · asset: multi · horizon: months · testable: no - qualitative · confidence: medium
  ^MT064-C22-3
- **Rob Carver** Net view: policy uncertainty hurts equities and inflation hurts bonds, which favors CTAs.  #mech/policy_reaction _(time-bound view)_
  > it's going to be bad for equities I think there going to be inflation which is going to be Bann for bonds
  asset: multi · direction: short equities and bonds; long CTAs · horizon: months · testable: no - opinion · confidence: medium
  ^MT064-C22-4

### C23
- **Niels Kaastrup-Larsen** Fixed income and gold price in risk from Trump policies while equities show little angst.  #mech/slow_reaction _(time-bound view)_
  > we see the risk show showing up in only parts of the financial uh markets at the moment right uh so fixed income is probably showing uh a little bit more concern about what's going on
  indicator: bonds, gold vs equities · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT064-C23-1
- **Niels Kaastrup-Larsen** Erosion of trust in institutions over decades makes a disconnect between value and price.  #mech/structural_shift
  > an erosion of trust erosion of trust in institutions
  asset: multi · horizon: years · testable: no - qualitative · confidence: medium
  ^MT064-C23-2
- **Niels Kaastrup-Larsen** Where price and value disconnect, a price-following strategy like trend following is a good portfolio component.  #mech/slow_reaction
  > a price-based strategy that doesn't care about is it the right value or not but just follows the price
  indicator: trend following · asset: multi · horizon: years · conditions: value-price disconnect · testable: no - view · confidence: medium
  **Correction (cross-check):** Probable wrong speaker. 'I do agree with you that actually a price-based strategy that doesn't care about is it the right value or not' answers Niels's point about trust erosion and the value-price disconnect, so it reads as Rob agreeing with Niels. → Rob Carver (probable): in a world where price and value are disconnected, a price-following strategy such as trend following is a good thing to hold in a portfolio.
  ^MT064-C23-3
- **Rob Carver** In 2007-08 credit, mortgage and bond markets signalled trouble before equities.  #mech/slow_reaction
  > the equity markets for a long time thought everything was fine yeah um and it was in the the the bond markets and the debt in the you know the CDs markets
  indicator: credit spreads, MBS vs equities · asset: credit · horizon: months · testable: partly - lead-lag testable · confidence: medium
  ^MT064-C23-4
- **Rob Carver** Bond investors are more professional and conservative than equity investors (more retail now), so bonds and gold may lead equities on Trump risks.  #mech/behavioral _(time-bound view)_
  > the bond market could be a bit ahead of the curve and maybe even the gold market
  indicator: bond market, gold vs equities · asset: multi · horizon: months · testable: partly - lead-lag testable · confidence: low
  ^MT064-C23-5
- **Rob Carver** Bonds and equities react to different drivers: bonds focus on inflation, which Trump policies clearly raise, while the effect of inflation on equities is ambiguous, so bonds are the more direct place for policy risk to show first.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > the bond Market's probably more concerned about inflation rather than say you know the risks of a recession
  indicator: bond yields vs equity prices on inflationary policy · asset: rates · direction: bond yields up on inflationary policy · horizon: months · conditions: policy changes that raise inflation · testable: partly - event studies of tariff announcements on yields versus equities · confidence: medium
  ^MT064-C23-X1

### C24
- **Rob Carver** Trump policy effects reach jobs data with a lag and equities even later, so watch and wait.  #mech/slow_reaction _(time-bound view)_
  > there'd be quite a lag before they have an effect on the real economy and uh and start showing up in things like you know jobs numbers and and even bigger lack before they show up in equities
  indicator: jobs numbers · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT064-C24-1
- **Niels Kaastrup-Larsen** Government bonds may prove unsafe and equities a safe harbor in a public-private cycle turn (not a market forecast).  #mech/cycle_persistence _(time-bound view)_
  > I would not be surprised if what people think is safe I.E government bonds will turn out to be not so safe
  indicator: bond and equity safety · asset: multi · horizon: years · testable: no - speculative · confidence: low
  ^MT064-C24-2
- **Niels Kaastrup-Larsen** The Fourth Turning generational cycle suggests the period will turn more turbulent before it ends.  #mech/cycle_persistence _(time-bound view)_
  > the books uh that he or the book he wrote uh back in the early 90s the fourth turning I think that is a concept that we should not ignore at this
  indicator: generational cycle · asset: multi · horizon: years · testable: no - cyclical theory · confidence: medium
  ^MT064-C24-3

