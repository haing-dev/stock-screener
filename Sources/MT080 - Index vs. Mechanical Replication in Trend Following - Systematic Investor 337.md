---
source_id: MT080
title: "Index vs. Mechanical Replication in Trend Following - Systematic Investor 337"
date: 2025-03-08
channel: "Top Traders Unplugged"
url: 
words: 11689
claims: 51
added_by_crosscheck: 3
corrections: 0
crosscheck: "opus cross-check"
speakers: ["Katy Kaminsky (guest, Alpha Simplex, quantitative CTA)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Index vs. Mechanical Replication in Trend Following - Systematic Investor 337

**Speakers:** Katy Kaminsky (guest, Alpha Simplex, quantitative CTA); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Feb 2025 trend-following check-in and Katy's paper on index versus mechanical replication of managed futures for ETFs. Covers weak trend regime, BoJ and Trump-trade unwind, lookback window diversification (slower has higher Sharpe, shorter gives convexity), crowding via co-movement, Sharpe-based expected returns, replication pros/cons, informed regression to cut tracking error, and caution on CTA ETFs.

**Approach:** trend following, CTA replication / ETFs, crowding, lookback diversification

**Cross-check completeness estimate of first read:** 0.94 - first reader was very thorough; missed only the listener's position-fading practice, the risk-premia point on slow trend and the selection-bias reason for judging on tracking error.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro; BoJ divergence and carry trade |
| C02 | 4 | JGB short trade, Tesla/crypto asides, February CTA reversals |
| C03 | 3 | gas, cocoa reversals; Trump trade unwind, yields |
| C04 | 5 | Trend barometer, index numbers, co-movement crowding factor |
| C05 | 3 | co-movement uses, crowding, PCA comparison |
| C06 | 3 | lookback window dispersion; short vs long trend |
| C07 | 4 | 25-year best-lookback analysis; client objective |
| C08 | 2 | CTA ETF users |
| C09 | 2 | ETF investor behaviour; expected return question set-up |
| C10 | 2 | Sharpe-based expected returns; paper intro |
| C11 | 3 | index vs mechanical replication definitions |
| C12 | 5 | pros and cons; informed regression |
| C13 | 3 | combined method, tracking |
| C14 | 3 | tracking error and 'replication' wording |
| C15 | 1 | CTA ETF product differences |
| C16 | 3 | nomenclature, why simplified in ETFs |
| C17 | 1 | ETF liquidity; outro |

## Claims

### C01
- **Katy Kaminsky** Divergence in monetary policy and inflation (Bank of Japan versus others) raises the question of what happens to the carry trade if the BoJ hikes.  #mech/policy_reaction _(time-bound view)_
  > I keep getting a lot of questions about what's going to happen to the carry trade what's going to happen if the bank of J Japan uh hikes rates
  indicator: BoJ policy rate; carry trade positioning · asset: fx · direction: carry trade at risk if BoJ hikes · horizon: months · testable: partly: event risk, not a defined rule · confidence: medium
  ^MT080-C01-1

### C02
- **Niels Kaastrup-Larsen** The short JGB trade, the 'widow-maker', is finally paying trend followers after decades, with a BoJ policy shift as a potential driver.  #mech/policy_reaction _(time-bound view)_
  > the Widow trade the short jgb trade which uh which finally after decades seems to be throwing off a little bit of a profit
  indicator: JGB futures · asset: rates · direction: short JGBs · horizon: months · conditions: BoJ hiking · testable: yes · confidence: medium
  ^MT080-C02-1
- **Katy Kaminsky** Tesla should be viewed as an option that trades with large variability.  #mech/new _(time-bound view)_
  > just think of Tesla as an option it's going to trade like like an options contract
  indicator: Tesla · asset: equities · testable: no: comment · confidence: low
  ^MT080-C02-2
- **Niels Kaastrup-Larsen** Record one-day outflows from crypto ETFs (about $1bn) and the $1.5bn ether exchange hack coincided with crypto price weakness.  #mech/crowding_positioning _(time-bound view)_
  > the biggest uh one- day uh outflow uh from exchange trated funds happened this week on Tuesday um about a billion dollars
  indicator: crypto ETF flows · asset: other · direction: crypto down · horizon: days · testable: yes: ETF flow data public · confidence: medium
  ^MT080-C02-3
- **Niels Kaastrup-Larsen** February 2025 was poor for CTAs because of reversals in fixed income (bond prices supported) along with currency changes and equity weakness.  #mech/cycle_persistence _(time-bound view)_
  > it hasn't been a great month for CTA or Trend follows so far uh mainly things to as far as I can tell uh reversals uh in fixed income
  indicator: bond futures reversal · asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT080-C02-4

### C03
- **Niels Kaastrup-Larsen** Reversals in Dutch natural gas (TTF) and cocoa after long uptrends hurt long-term trend followers.  #mech/cycle_persistence _(time-bound view)_
  > Dutch net gas has had a big move uh this month a big drop actually in price um but it was in a pretty long-term uh uptrend
  indicator: TTF natural gas, cocoa · asset: commodities · horizon: weeks · conditions: after a long trend · testable: yes · confidence: high
  ^MT080-C03-1
- **Katy Kaminsky** The post-election trend mix (long US equities, short fixed income, long dollar) unravelled in Jan-Feb 2025 as markets doubted US exceptionalism, with risk-off trades the opposite, making trends difficult.  #mech/cycle_persistence _(time-bound view)_
  > we started out really sort of on that Trump trade in November so that was really you know long us um long um short fixed income coming out and also you had long dollar
  indicator: US vs non-US equities, USD, yields · asset: multi · horizon: months · conditions: trend reversal after policy-driven themes · testable: yes · confidence: medium
  ^MT080-C03-2
- **Katy Kaminsky** Policymakers cannot force bond yields down if inflation rises, because yields reflect buyers' appetite.  #mech/policy_reaction _(time-bound view)_
  > you can't really force that if you add inflation
  indicator: Treasury yields vs inflation · asset: rates · horizon: months · testable: no · confidence: medium
  ^MT080-C03-3

### C04
- **Niels Kaastrup-Larsen** A Trend barometer reading of 23 is almost the worst level, confirming a very weak trending environment.  #mech/cycle_persistence _(time-bound view)_
  > my Trend barometer yesterday it finished at 23 and for those who follow it on the website they know that 23 is really almost as bad as it it gets
  indicator: Trend barometer (Niels' own) · asset: multi · horizon: weeks · testable: yes: barometer defined by host · confidence: high
  ^MT080-C04-1
- **Niels Kaastrup-Larsen** February has seen big moves up and down historically, so the weak month is not extreme.  #mech/seasonality
  > there's been some big moves in February performance-wise both up and down over the uh over the year
  indicator: CTA February performance history · asset: multi · horizon: years · testable: yes · confidence: low
  ^MT080-C04-2
- **Niels Kaastrup-Larsen** Through 25 Feb 2025 trend indices were down roughly 1.3-2.9% for the month and slightly negative YTD.  #mech/cycle_persistence _(time-bound view)_
  > stockchain CT index down 2.33% uh down 1.72 for the year
  indicator: BTOP50, SG CTA, SG Trend, short-term traders · asset: multi · horizon: months · testable: yes: public index data · confidence: high
  ^MT080-C04-3
- **Niels Kaastrup-Larsen** Treasuries rallied about 5% in February while equities slipped, a sentiment reversal from the late-2024 short-bond trades.  #mech/cycle_persistence _(time-bound view)_
  > S&P us treasury bond index is actually up very strong up 5% and change so far in February up 5.4% so far this year
  indicator: US Treasury bond index · asset: rates · direction: bonds up · horizon: months · testable: yes · confidence: high
  ^MT080-C04-4
- **Katy Kaminsky** Co-movement (excess correlation of assets relative to their asset-class benchmark, beta adjusted; Nick Balter's work) is a pseudo measure of position crowding.  #mech/crowding_positioning
  > you can estimate um a pseudo crowding measure by measuring co-movement and co-movement is really the excess correlation relative to the
  indicator: co-movement factor · asset: multi · testable: yes: excess correlation is computable · confidence: high
  ^MT080-C04-5
- **Rick (listener question, read by Niels Kaastrup-Larsen)** A listener trades live systems that fade extreme or offside positioning, i.e. take the opposite side when positioning in a market becomes crowded, as a contrarian complement to trend.  #mech/crowding_positioning _(added by opus cross-check)_
  > I have been building and live trading offside systems fading extreme or offside positioning
  indicator: positioning extremes (e.g. CFTC or co-movement crowding) · asset: multi · direction: short crowded longs / long crowded shorts · horizon: weeks · conditions: extreme positioning · testable: yes - fade-the-crowd backtest on positioning data · confidence: low
  ^MT080-C04-X1

### C05
- **Katy Kaminsky** Excess co-movement within a group (e.g. precious metals in a tariff theme) indicates crowded positions and higher reversal risk; it can serve as a signal, filter or risk-management tool.  #mech/crowding_positioning
  > in that case um it could indicate that there's more reversal risk for those type of um assets
  indicator: excess co-movement · asset: commodities · direction: reversal risk up · horizon: months · conditions: crowded themes · testable: yes · confidence: medium
  ^MT080-C05-1
- **Katy Kaminsky** Crowded trades can extend (feedback trading, macro themes), which is part of why trend works; co-movement is used to attribute which crowded markets were profit centers.  #mech/crowding_positioning
  > crowded trades aren't necessarily always a bad thing
  indicator: co-movement attribution · asset: multi · horizon: months · conditions: trend-supporting themes · testable: yes · confidence: medium
  ^MT080-C05-2
- **Katy Kaminsky** Co-movement differs from PCA: it explicitly adjusts for asset-class beta, though the two are related.  #mech/research_method
  > principal component analysis is purely statistic ically based I think when you look at co- movement you actually are specifically adjusting for um an asset classes beta
  indicator: co-movement vs PCA · asset: multi · testable: yes · confidence: medium
  ^MT080-C05-3

### C06
- **Katy Kaminsky** The best trend window is idiosyncratic each year, so diversify signals across time horizons and methods to smooth capture of trend.  #mech/research_method
  > this is why we don't trade one window right because you know there's just a lot of noise in Trends and they are they have very different time series patterns
  indicator: trend lookback windows · asset: multi · horizon: years · testable: yes: window dispersion testable · confidence: high
  ^MT080-C06-1
- **Katy Kaminsky** Longer lookbacks have slightly higher Sharpe, while shorter ones are needed for convexity and crisis alpha (a 10-month window would not move in time for Covid).  #mech/slow_reaction
  > longer term has a slightly higher sharp ratio but shorter term is really important for convexity and for crisis Alpha
  indicator: lookback length · asset: multi · direction: longer = higher Sharpe; shorter = convexity · horizon: years · conditions: crisis years favour short windows · testable: yes · confidence: high
  ^MT080-C06-2
- **Katy Kaminsky** In 2024 with no crisis or drawdowns, longer-term trend and buy-and-hold risk-premia did better than fast systems.  #mech/cycle_persistence _(time-bound view)_
  > we didn't really have crisis last year we didn't have draw Downs so if that's the case you know guess what like longer term where risk Premia type strategies Buy and Hold actually did a lot better
  asset: multi · direction: longer-term outperformed · horizon: months · conditions: no-crisis year · testable: yes · confidence: medium
  ^MT080-C06-3

### C07
- **Niels Kaastrup-Larsen** In 15 of 25 years from 2000 to 2024 the best-performing lookback was over 200 days, confirming slower trend is better in the long run (though 2008 best was about 56 days).  #mech/cycle_persistence
  > about 15 of those 25 years uh the best the the absolute best look back period uh was uh more than 200 days
  indicator: best lookback by year · asset: multi · direction: longer lookbacks · horizon: years · testable: yes: Niels' own analysis · confidence: high
  ^MT080-C07-1
- **Niels Kaastrup-Larsen** The best lookback clusters in regimes: 2001-07 over 200 days, about a decade of shorter windows, then 2017-22 over 200 days.  #mech/cycle_persistence
  > there is a bit of clustering because 01 02 03 04 05 06 07 they all clustered at more than 200 days
  indicator: best lookback regimes · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT080-C07-2
- **Niels Kaastrup-Larsen** The SG Short-term Traders Index has shown almost no performance over time, supporting the need for slower trend.  #mech/cycle_persistence
  > there really isn't any performance in that index uh to be frank
  indicator: SG Short-term Traders Index · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT080-C07-3
- **Katy Kaminsky** Choose speed by client objective: the highest Sharpe favours slower trend, risk-mitigation clients care about conditional returns versus equities and want short-term reactivity.  #mech/risk_management
  > is a client looking for something that's the most compatible with equities or are they looking for something that has the highest sharp
  indicator: conditional returns of trend vs equities · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT080-C07-4
- **Katy Kaminsky** Longer-lookback trend partly harvests buy-and-hold risk premia, which raises long-run Sharpe but weakens its role as a defence in a bad year, where shorter-term reactivity matters.  #mech/risk_premium _(added by opus cross-check)_
  > as you go into longer Trend as well you're capturing some of the risk Premia which is good
  indicator: trend lookback length · asset: multi · direction: slow trend: more risk premia, less crisis protection · horizon: years · testable: yes - decompose slow-trend returns into static long exposure vs timing · confidence: medium
  ^MT080-C07-X1

### C08
- **Katy Kaminsky** CTA ETFs attract mostly individuals and RIA model portfolios in the US, and institutions use them as an easy, no-paperwork liquid allocation.  #mech/structural_shift _(time-bound view)_
  > slightly more uh more individual um and more sort of I think retail especially for the US
  indicator: CTA ETF adoption · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT080-C08-1
- **Katy Kaminsky** Institutions like ETFs for fast allocation changes and parking assets in CTA-like returns.  #mech/structural_shift
  > something that they can just buy in in a day or adjust their allocation without a lot of documentation
  asset: multi · testable: no · confidence: medium
  ^MT080-C08-2

### C09
- **Niels Kaastrup-Larsen** ETF anonymity and easy redemption hide the investor base, making holding period and return chasing hard to know and handholding difficult.  #mech/behavioral
  > people could just redeem their investment they didn't have to call the company and say oh I'm I'm thinking of redeeming or asking for paperwork Etc
  indicator: ETF holder behaviour · asset: multi · testable: partly · confidence: medium
  ^MT080-C09-1
- **Katy Kaminsky** The gap between fund returns and investor returns (Morningstar) exists in ETFs too; model portfolios with behavioural constraints help, and trying to trend-follow the trend follower is risky.  #mech/behavioral
  > just this idea of you know actual Returns versus investors behavioral returns
  indicator: investor vs fund returns · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT080-C09-2

### C10
- **Katy Kaminsky** Instead of expected returns, estimate a Sharpe ratio (e.g. 0.4-0.5) and multiply by the risk allocated (vol exposure) to get a long-term return estimate for trend following.  #mech/research_method
  > you should think about estimating your estimated uh sharp ratio that you think that you could achieve in in the strategy
  indicator: Sharpe times volatility allocation · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT080-C10-1
- **Niels Kaastrup-Larsen** Benchmarks starting in 2000 are arbitrary; long track records (50 years) are a better basis for expected Sharpe.  #mech/research_method
  > they start in year 2000 I just think that year 2000 is kind of arbitrary
  indicator: track record length · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT080-C10-2

### C11
- **Katy Kaminsky** CTA indices include non-investable markets so you cannot build the index from building blocks as in equities; ETF beta must be approximated.  #mech/structural_shift
  > a lot of the indices include Investments that you can't directly invest in that type of vehicle
  indicator: CTA index constituents · asset: multi · testable: yes · confidence: high
  ^MT080-C11-1
- **Katy Kaminsky** Index replication infers index positions (regression-based) while mechanical replication is a simplified individual strategy (e.g. moving average crossovers).  #mech/research_method
  > index replication is inferring positions of the index whereas mechanical replication is a method that is a simplified version of a typical strategy
  indicator: replication methods · asset: multi · testable: yes · confidence: high
  ^MT080-C11-2
- **Katy Kaminsky** Pro of index replication: aggregated industry view with less manager-parameter-specific risk.  #mech/research_method
  > it's often argued that there's less manager parameter specific risk because the parameters will change and move with the index as the managers change themselves
  indicator: index replication · asset: multi · testable: yes · confidence: medium
  ^MT080-C11-3

### C12
- **Katy Kaminsky** Con of index replication: slower and backward-looking, and risk management is inherited rather than designed.  #mech/slow_reaction
  > it can be a little slower to react because it's much more backward looking
  indicator: index replication · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT080-C12-1
- **Katy Kaminsky** Regression-based replication suffers misspecification and collinearity, giving chunky exposures less representative of actual positions.  #mech/research_method
  > especially as you do aggression there's a lot of colinearity so you know you may sort of end up with more chunky uh type of exposures
  indicator: regression collinearity · asset: multi · testable: yes · confidence: medium
  ^MT080-C12-2
- **Katy Kaminsky** Pro of mechanical replication: risk management and direct reaction; con is a single parameter set and manager return dispersion.  #mech/research_method
  > it allows you to incorporate all the risk management techniques and some of the tricks and tools of of ctas um and it can directly react uh more directly with Market movements
  indicator: mechanical replication · asset: multi · testable: yes · confidence: high
  ^MT080-C12-3
- **Katy Kaminsky** Single-strategy replication carries large return dispersion because a manager's window can be best one year and worst the next.  #mech/risk_management
  > one manager could be the best manager because they had that 11-month window this month you know as their focus and then they could be the bottom the next year
  indicator: manager return dispersion · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT080-C12-4
- **Katy Kaminsky** Combine mechanical and index replication ('informed regression', Bayesian-like) to lean on each when the other fails.  #mech/research_method
  > informed regression which is similar to a basian type of approach where you incorporate sort of individual strategy insights combined with index replication
  indicator: informed regression · asset: multi · testable: yes · confidence: medium
  ^MT080-C12-5

### C13
- **Katy Kaminsky** A single strategy picks up positioning shifts faster than index inference, while the aggregate view helps when one strategy is over-exposed relative to the industry.  #mech/slow_reaction
  > if you have a massive shift in positioning an individual strategy will pick that up quicker than the index itself
  indicator: individual vs index replication · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT080-C13-1
- **Katy Kaminsky** The paper evaluates tracking and goodness of fit to the index, not returns.  #mech/research_method
  > don't care about returns in this paper we care about tracking we care about goodness of fit
  indicator: tracking error · asset: multi · testable: yes · confidence: high
  ^MT080-C13-2
- **Niels Kaastrup-Larsen** Index replication loses correlation to the index during large dislocations, while mechanical replication breaks down less often.  #mech/slow_reaction
  > correlation between index replication and the index itself actually kind of breaks down often when uh there are some big uh dislocations happening
  indicator: replicator-index correlation · asset: multi · horizon: months · conditions: big industry dislocations · testable: yes · confidence: medium
  ^MT080-C13-3

### C14
- **Katy Kaminsky** Combining both approaches substantially reduces tracking error over longer horizons, though it stays high.  #mech/research_method
  > you see a substantial reduction in tracking error over uh longer time Horizons
  indicator: tracking error · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT080-C14-1
- **Niels Kaastrup-Larsen** With tracking error this large, 'replication' is misleading: an investor gets something that may be better or worse than the index.  #mech/risk_management
  > with a tracking area uh of this size then then people should be aware that that's probably not what they're going to get
  indicator: tracking error · asset: multi · testable: yes · confidence: high
  ^MT080-C14-2
- **Katy Kaminsky** Anyone wanting CTA beta must pick the method that gives the most beta-like exposure, since a single ETF can differ greatly from the industry.  #mech/risk_management
  > if you go in and you randomly pick an ETF you could get something very different from the industry
  indicator: single strategy vs industry · asset: multi · testable: yes · confidence: high
  ^MT080-C14-3
- **Katy Kaminsky** Replication methods should be judged on tracking error to the index, not on historical returns, because one can always select ex post the strategy with the best past return.  #mech/research_method _(added by opus cross-check)_
  > that's why we cared so much about tracking era um instead of you know looking at returns because as you know you can always pick the strategy historically that has the best return
  indicator: tracking error vs CTA index · asset: multi · horizon: years · testable: yes - out-of-sample tracking error comparison · confidence: high
  ^MT080-C14-X1

### C15
- **Niels Kaastrup-Larsen** Some new CTA ETFs trade only a couple of sectors, unlike the diversified managed futures norm, so results may differ widely.  #mech/structural_shift
  > it's not Diversified at all it's actually some of them are trading one or two at least two um sectors
  indicator: sector diversification of CTA products · asset: multi · testable: yes · confidence: medium
  ^MT080-C15-1

### C16
- **Katy Kaminsky** CTA ETF products need new nomenclature; portable alpha, beta and different asset class are the key distinctions in this innovation phase.  #mech/structural_shift
  > is it a portable Alpha strategy or not is it a beta strategy or not um does it have a different asset class uh exposure or not are the key three that I see
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT080-C16-1
- **Katy Kaminsky** Early 40-Act managed futures funds had low correlation to the industry index and later converged to high correlation, suggesting ETFs will also settle into buckets.  #mech/structural_shift _(time-bound view)_
  > look at the correlation to the index uh of the top you know mutual funds it was very low for the first few years of the 40 act space
  indicator: fund correlation to index · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT080-C16-2
- **Katy Kaminsky** ETF versions are simplified because daily intraday liquidity favours less turnover and markets that market makers can hedge.  #mech/structural_shift
  > you might choose for example less turnover in signals and you might also lean to markets that are easily hedged by market makers
  indicator: ETF turnover and market choice · asset: multi · testable: yes · confidence: medium
  ^MT080-C16-3

### C17
- **Katy Kaminsky** Mutual funds only need a daily mark so a wide market range is fine, while ETFs fit liquid markets with low turnover to limit slippage.  #mech/structural_shift
  > with a mutual fund you just have a daily Mark to Market really and so you know if you're trading you know a wide range of markets you don't have to think about that in day hedging
  asset: multi · testable: no · confidence: medium
  ^MT080-C17-1

