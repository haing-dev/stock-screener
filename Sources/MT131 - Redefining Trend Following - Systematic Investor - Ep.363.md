---
source_id: MT131
title: "Redefining Trend Following - Systematic Investor - Ep.363"
date: 2025-09-02
channel: "Top Traders Unplugged"
url: 
words: 10320
claims: 50
added_by_opus: 0
corrections: 0
crosscheck: "pending"
speakers: ["Niels Kaastrup-Larsen (host, hedge fund manager; transcribed Neils Krup Larson)", "Nick Bolters (co-host, quant researcher/QIS)"]
tags: [source, layer0]
---
# Redefining Trend Following - Systematic Investor - Ep.363

**Speakers:** Niels Kaastrup-Larsen (host, hedge fund manager; transcribed Neils Krup Larson); Nick Bolters (co-host, quant researcher/QIS)

**Summary:** Systematic Investor episode on August 2025 CTA performance, whether CTAs got slower or just more complex, the limits of SG Trend Index as trend beta, and Convex-style long-term compounding with short-term risk mitigation.

**Approach:** trend following, CTA benchmarks, carry, risk management, compounding

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, sponsor and holiday small talk |
| C02 | 3 | Greenland/Fed politics; CTA August performance by sector |
| C03 | 5 | oil, speed comparison, gold, rates, carry |
| C04 | 3 | trend barometer, index returns, speed vs structure question |
| C05 | 5 | correlation-based speed analysis and its limits |
| C06 | 4 | speed vs risk management, vol estimation, correlation caveats |
| C07 | 5 | 66-day half-life, speed definition, trend follower types |
| C08 | 4 | trend following objectives and investor expectations |
| C09 | 3 | beta-neutral diversifiers; SG index survivorship |
| C10 | 4 | trend beta definition, benchmark issues |
| C11 | 3 | better benchmark, QIS aggregates, 60/40 |
| C12 | 3 | Convex/Dredge long-term compounding, brakes analogy |
| C13 | 4 | fixed income issuance, loss asymmetry, mean-variance vs compounding, carry analogy |
| C14 | 4 | path dependence, solvency, Monte Carlo, insurance |
| C15 | 0 | outro: recap repeats earlier idea, next episode plug |

## Claims

### C02
- **Niels Kaastrup-Larsen** In August 2025 CTA gains came from equity trends plus a few commodities (live cattle, gold, silver) while wheat shorts paid on a bumper crop.  #mech/cycle_persistence _(time-bound view)_
  > we do see or at least from my vantage point continued strength in um the equity part of the CTA portfolio
  indicator: CTA/trend sector contribution · asset: multi · direction: long equities, cattle, gold, silver; short wheat · horizon: months · conditions: after a weak H1; vulnerable to policy announcements (copper tariff) · testable: partly - sector attribution can be computed from a trend backtest · confidence: medium
  ^MT131-C02-1
- **Niels Kaastrup-Larsen** Fixed income was the worst trend-following sector because rates stayed in wide trading ranges and CTAs were split long/short.  #mech/cycle_persistence _(time-bound view)_
  > fixed income in general has been pretty horrible uh for for trend followers because they've been stuck in in large trading ranges
  asset: rates · horizon: months · conditions: range-bound rates hurt trend following · testable: yes - trend P&L by sector · confidence: medium
  ^MT131-C02-2
- **Niels Kaastrup-Larsen** An attempt to remove Fed governor Lisa Cook could give the administration about five of seven board seats, raising Fed-independence risk.  #mech/policy_reaction _(time-bound view)_
  > direct attack on another Fed governor uh Lisa Cook um and trying to essentially change the the composition
  indicator: Fed board composition · asset: rates · testable: no - political judgement · confidence: low
  ^MT131-C02-3

### C03
- **Niels Kaastrup-Larsen** Oil traded sideways with no follow-through, so energy offered trend followers little.  #mech/cycle_persistence _(time-bound view)_
  > oil has kind of just been gyating up and down for for quite a while without too much of real follow through
  asset: commodities · horizon: months · conditions: range trading hurts trend following · testable: partly · confidence: medium
  ^MT131-C03-1
- **Nick Bolters** Slower trend speeds beat faster ones in recent months and years because V-shaped reversals (April 2025, August 2024) punish fast signals.  #mech/overshoot _(time-bound view)_
  > broadly speaking the slower the better for the month which seems to be the theme of the the last
  indicator: trend signal speed (lookback) · asset: multi · direction: slower speeds outperform · horizon: months · conditions: after sharp V-shaped reversals · testable: yes - compare speeds across years · confidence: medium
  ^MT131-C03-2
- **Nick Bolters** Gold was the top single-market contributor to trend programs in 2025 across an 80+ market universe.  #mech/cycle_persistence _(time-bound view)_
  > gold for sure. I think gold uh is probably the number one positive contributor year to date out of a universe of like know 80 plus markets
  indicator: gold trend · asset: commodities · direction: long gold · horizon: months · testable: yes - per-market attribution · confidence: medium
  ^MT131-C03-3
- **Nick Bolters** Rates had no trend in 2025, a disappointing year for fixed-income trend contribution.  #mech/cycle_persistence _(time-bound view)_
  > it's it's it's really kind of going around and whipsing uh with no specific direction
  asset: rates · horizon: months · conditions: whipsaw regime · testable: partly · confidence: medium
  ^MT131-C03-4
- **Nick Bolters** Beta-neutralised carry (outside trend following) had one of its best years, so CTAs that add carry, stop-loss or reversion sleeves did better.  #mech/risk_premium _(time-bound view)_
  > Kerry continues to have very very strong month or months or maybe year
  indicator: beta-neutral carry · asset: multi · direction: long carry · horizon: months · conditions: when trend is weak · testable: yes - add carry sleeve to a trend backtest · confidence: medium
  ^MT131-C03-5

### C04
- **Niels Kaastrup-Larsen** A trend barometer measuring trendiness over a short lookback read 34 in late August 2025, a weak trend environment consistent with poor CTA returns.  #mech/cycle_persistence _(time-bound view)_
  > my own trend barometer actually yesterday finished at 34. So that's still a weak reading.
  indicator: trend barometer (short lookback) · asset: multi · horizon: weeks · conditions: weak reading means poor trend conditions · testable: yes - construct a trendiness gauge · confidence: medium
  ^MT131-C04-1
- **Niels Kaastrup-Larsen** In 2025 the short-term traders index was the worst CTA sub-index (-6.29% YTD) versus trend index -7.39% and S&P +11%, so different speeds behaved very differently.  #mech/cycle_persistence _(time-bound view)_
  > short-term traders index. It's down one and a quarter% uh and it's now down 6.29%.
  indicator: SG short-term traders index vs SG trend index · asset: multi · horizon: months · testable: yes - public index data · confidence: medium
  ^MT131-C04-2
- **Nick Bolters** Apparent CTA slowing may be a change in structure (added features) rather than a change in signal speed.  #mech/structural_shift
  > CTAs have gotten slower over the past decade or so, maybe even more. Um but you question whether that's really a shift in speed or whether that's a shift in structure
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT131-C04-3

### C05
- **Nick Bolters** The usual evidence for CTAs slowing is ex-post: correlate stylised bottom-up fast-to-slow strategies with SG Trend Index on rolling 1-2 year windows and see slower ones correlate more recently.  #mech/research_method
  > you know if you run this analysis
  indicator: rolling correlation of speed-specific trend proxies to SG Trend Index · asset: multi · horizon: years · testable: yes - replicable · confidence: high
  ^MT131-C05-1
- **Nick Bolters** A change in correlation to a benchmark is necessary but not sufficient to infer a change in signal speed.  #mech/research_method
  > a shift in realized correlations is a necessary but not sufficient condition to infer that the speed has changed
  asset: multi · testable: yes - simulate feature additions · confidence: high
  ^MT131-C05-2
- **Nick Bolters** Adding stop-losses, carry, reversion or value signals, or new markets, shifts correlation to a trend benchmark in the same way a speed change would.  #mech/research_method
  > It can simply come as a consequence of me introducing stop-loss rules, introducing car signals, introducing reversion signals, amending my program
  asset: multi · testable: yes - ablation test of added components · confidence: high
  ^MT131-C05-3
- **Nick Bolters** The SG Trend Index is made of realised returns of real, evolving programs, not a simulation of today's algorithms, so speed-by-correlation analysis on it is questionable.  #mech/research_method
  > the fact that the so trend index in itself is a living creature of realized returns of real programs
  indicator: SG Trend Index · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT131-C05-4
- **Niels Kaastrup-Larsen** A long-term trend signal combined with agile risk management can look like a short-term model.  #mech/risk_management
  > you can have risk management filters that react much faster and it'll look like uh you have um you know short-term models in there
  asset: multi · testable: partly · confidence: medium
  ^MT131-C05-5

### C06
- **Nick Bolters** CTA model research mostly changes risk management (risk level, net/gross exposure, signal diversification) rather than signal speed.  #mech/risk_management
  > I think the response is more on the risk management side maybe let's reduce the level of risk we take maybe let's reduce the net or the gross exposure
  asset: multi · horizon: years · testable: no - practitioner claim · confidence: medium
  ^MT131-C06-1
- **Nick Bolters** Changing volatility or covariance estimation or exposure penalties can show up as an apparent change in speed.  #mech/research_method
  > even changing the way that volatility is estimated or the coverance is estimated or how you penalize some of your exposures might in itself appear exposed as a shift in the speed
  asset: multi · testable: yes - vary vol estimator · confidence: medium
  ^MT131-C06-2
- **Nick Bolters** Correlation alone cannot identify a strategy's behaviour: a value investor looks like a contrarian to a momentum trader.  #mech/research_method
  > if I take a correlation of a moment momentum trader to a value investor, I can equally say that it's a contarian
  asset: multi · testable: no - conceptual · confidence: medium
  ^MT131-C06-3
- **Nick Bolters** Conclusions on industry speed depend on market set, signal calculation (EWMA vs simple lookback), so results are fragile.  #mech/research_method
  > if we use exponential weighted moving average with the same look back window the story might be slightly different
  asset: multi · testable: yes - vary construction · confidence: medium
  ^MT131-C06-4

### C07
- **Nick Bolters** A paper maximising correlation to SG Trend Index found a best-fit half-life of about 66 business days over 15 years, which is not slow, so the 'CTAs have slowed' story is overstated.  #mech/research_method
  > know 66 business days of halfife for the last like know 15 years
  indicator: half-life of EWMA trend signal vs SG Trend Index · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT131-C07-1
- **Nick Bolters** CTA research is moving towards protecting the portfolio and anticipating falling signal-to-noise, not choosing a 3, 4 or 5 month speed.  #mech/risk_management
  > how can I protect my portfolio, how can be how can I anticipate the signal to noise dropping
  indicator: signal-to-noise of trend · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT131-C07-2
- **Niels Kaastrup-Larsen** Modern CTAs choose parameters dynamically so speed is not constant, which makes bucketing managers as short/medium/long term misleading.  #mech/structural_shift
  > the speed is not constant anyways. I mean we do dynamic select parameters on an ongoing basis
  asset: multi · testable: partly · confidence: medium
  ^MT131-C07-3
- **Nick Bolters** Different trend signals (sign of past return, EWMA, crossover) are functional transformations of each other, so effort belongs in portfolio construction and risk management rather than signal search (AQR paper).  #mech/research_method
  > different signals in a way um are functional transformations of each other
  indicator: trend signals (lookback, EWMA, crossover) · asset: multi · testable: yes · confidence: medium
  ^MT131-C07-4
- **Niels Kaastrup-Larsen** Trend followers split into replicators, core diversifiers, crisis risk offsetters, outlier hunters and pure trend followers, each serving a different investor purpose.  #mech/structural_shift
  > you could probably define four or including my extra definition, five types or categories of trend followers
  asset: multi · testable: no - taxonomy · confidence: medium
  ^MT131-C07-5

### C08
- **Nick Bolters** Trend following gives defensiveness in prolonged equity or macro drawdowns plus long-term returns, with decorrelation visible over long horizons rather than locally.  #mech/risk_management
  > trend followers or at least the strategy in a broad sense achieves two objectives
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT131-C08-1
- **Nick Bolters** Longer-term CTAs correlate more with equities long term because they are long in rallies, but they decorrelate around transition points.  #mech/cycle_persistence
  > whether you are 10 out of the 12 [L320] months long equities
  indicator: correlation of trend to equities · asset: equities · horizon: years · conditions: around turning points · testable: yes · confidence: medium
  ^MT131-C08-2
- **Nick Bolters** Whether trend following has worked depends on the investor's purpose (defensive vs absolute return vs inflation hedge); mismatched expectations cause disappointment in years like 2023-2025.  #mech/behavioral
  > what trend following is used for is that used for a defensive mandate
  asset: multi · horizon: years · testable: no - expectation management · confidence: medium
  ^MT131-C08-3
- **Nick Bolters** Diluting trend programs to target absolute return makes them less defensive in equity crises.  #mech/risk_management
  > the more you can dilute trend following programs to make them absolute return, the less defensive by nature you're going to make them
  asset: multi · testable: partly · confidence: medium
  ^MT131-C08-4

### C09
- **Nick Bolters** Trend following already carries equity beta, so add diversifiers such as beta-neutral carry or reversion rather than more beta.  #mech/risk_management
  > Why beta neutral? Because if beta is what you're getting from trend following
  indicator: beta-neutral carry/reversion · asset: multi · direction: add carry/reversion neutral to beta · conditions: when trend is not performing, e.g. 2025 · testable: yes · confidence: medium
  ^MT131-C09-1
- **Niels Kaastrup-Larsen** The SG Trend Index is the 10 biggest managers, shaped by AUM, survivorship and compromises of running billion-dollar programs, so it is not a pure measure of trend.  #mech/research_method
  > It's a snapshot of the 10 biggest managers
  indicator: SG Trend Index · asset: multi · horizon: years · testable: partly · confidence: high
  ^MT131-C09-2
- **Nick Bolters** Survivorship in the index means it reflects the best surviving managers and sets a higher bar than a plain trend beta.  #mech/research_method
  > it is the mans that either outperformed so their assets grew by outperformance or they managed to attract capital
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT131-C09-3

### C10
- **Nick Bolters** Calling the manager index 'trend beta' assumes risk-management and design choices net to zero alpha; otherwise it is beta plus or minus alpha.  #mech/research_method
  > we make a supposition here that they average to zero because if they do not average to zero
  asset: multi · testable: partly · confidence: medium
  ^MT131-C10-1
- **Nick Bolters** A live manager-based trend benchmark differs from a backtest of today's models because manager composition and design evolve through time.  #mech/research_method
  > a trend benchmark is different to a backtested performance of today's models
  asset: multi · testable: yes · confidence: medium
  ^MT131-C10-2
- **Niels Kaastrup-Larsen** Benchmark definition matters because some investors are paid bonuses on outperformance of trend benchmarks.  #mech/behavioral
  > there are big investors where they are paid bonuses based on their outperformance of these benchmarks
  asset: multi · testable: no · confidence: high
  ^MT131-C10-3
- **Niels Kaastrup-Larsen** The SG Trend Indicator (a signal-based, not manager-based index) tracks daily pure-trend performance well.  #mech/cycle_persistence
  > in terms of the daily direction, it seems to align pretty well with what I see from kind of pure trend performance
  indicator: SG Trend Indicator · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT131-C10-4

### C11
- **Nick Bolters** A better trend benchmark would be a simple bottom-up trend model as in academic papers, as bank QIS trend indices already do.  #mech/research_method
  > I think it would look um very similar to some of the some of the simple bottom up models
  asset: multi · testable: yes · confidence: medium
  ^MT131-C11-1
- **Nick Bolters** Third-party aggregated QIS trend indices have survivorship bias since banks drop or replace underperforming strategies.  #mech/research_method
  > some of the STRs that do not perform you know banks can decide to um to take them out
  indicator: bank QIS trend strategies · asset: multi · testable: partly · confidence: medium
  ^MT131-C11-2
- **Nick Bolters** There is no agreed best allocation benchmark, similar to 60/40 being used by convention.  #mech/behavioral
  > people use the 60/40 partly by convention rather than um academic prudence
  asset: multi · testable: no · confidence: medium
  ^MT131-C11-3

### C12
- **Niels Kaastrup-Larsen** Following Dave Dredge (Convex): portfolios built to look safe and near long-term average load up on correlated strategies that fall together; maximising long-term compounding requires different construction.  #mech/risk_management
  > if you want to build your portfolio um to have the highest long-term uh return
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT131-C12-1
- **Niels Kaastrup-Larsen** Race-car analogy: best 'brakes' (long volatility, trend following) let a portfolio run faster over the long run.  #mech/risk_management
  > you kind of have to build the car to have the best best brakes
  indicator: long volatility, trend following · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT131-C12-2
- **Niels Kaastrup-Larsen** Including crisis-protective strategies allows higher equity allocation (e.g. 80/20 instead of 60/40).  #mech/risk_management
  > it actually allows you to own more equities. Um so you could have an 80/20 portfolio
  asset: multi · direction: more equities when hedged with trend/long vol · horizon: years · testable: yes - portfolio simulation · confidence: medium
  ^MT131-C12-3

### C13
- **Niels Kaastrup-Larsen** Fiscal expansion means rising bond issuance, so portfolios will hold more fixed income, which is not a safe source of long-term real compounding.  #mech/fiscal_debt _(time-bound view)_
  > the issuance of fixed income products will just continue to grow
  indicator: government bond issuance · asset: rates · horizon: years · testable: no · confidence: medium
  ^MT131-C13-1
- **Nick Bolters** Losses compound asymmetrically (10% loss needs about 11% to recover), so short-term losses reduce long-term compounding.  #mech/risk_management
  > losing 10% would require you an 11% gain to go back to flat
  asset: multi · horizon: years · testable: yes - arithmetic · confidence: high
  ^MT131-C13-2
- **Nick Bolters** Unlike single-period mean-variance, a compounding investor targets long-horizon return while minimising short-horizon risk.  #mech/risk_management
  > the expected returns is now a long-term capital appreciation whereas the risk that we want to minimize becomes more of a short-term risk mitigation
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT131-C13-3
- **Nick Bolters** Carry harvesting resembles buying rental property: the yield is earned but spot-price drops can erase it, so short-term spot moves need controlling.  #mech/risk_premium
  > how a a a carry harvesting investor would perform or would operate
  indicator: carry · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT131-C13-4

### C14
- **Nick Bolters** Short-term drawdowns matter for how wealth accumulates over years, not just terminal wealth.  #mech/risk_management
  > the short-term drop doesn't have an impact on the day but does have an impact on how the acrual or the accumulation of wealth will play out
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT131-C14-1
- **Nick Bolters** Pension and income funds have annual solvency checkpoints, making short-term risk mitigation a requirement alongside long-term growth.  #mech/risk_management
  > you actually want to make sure that you can pay your pensions on an annual basis
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT131-C14-2
- **Nick Bolters** Monte Carlo sampling of 12-52 period sequences shows strategies with short-term downside mitigation (long vol, trend) have similar average arithmetic returns but a compounded return distribution shifted right.  #mech/research_method
  > the simulated compounded return would be substantially skewed to the to the right
  indicator: bootstrapped compounded return · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT131-C14-3
- **Nick Bolters** Long volatility or trend exposure should be judged in portfolio context, like insurance with negative standalone expected return that pays when needed.  #mech/risk_management
  > we pay insurance. Like in reality, insurance is a negative expected return investment
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT131-C14-4

