---
source_id: MT056
title: "Finding Alpha in the Strait of Chaos ft. Andrew Beer - Systematic Investor - Ep.395"
date: 2026-04-13
channel: "Top Traders Unplugged"
url: 
words: 14342
claims: 75
added_by_crosscheck: 17
corrections: 5
crosscheck: "opus cross-check"
speakers: ["Andrew Beer (Dynamic Beta Investments, manager of DBMF replication ETF)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Finding Alpha in the Strait of Chaos ft. Andrew Beer - Systematic Investor - Ep.395

**Speakers:** Andrew Beer (Dynamic Beta Investments, manager of DBMF replication ETF); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Weekly systematic-investor episode, April 2026: CTA/trend performance during the Iran-conflict March reversal, then Beer argues simple, efficient replication of the SG CTA index beats complex hedge-fund models because of implementation costs, and that bank QIS trend products lose most of their backtest Sharpe live.

**Approach:** trend following, CTA replication, QIS products, implementation costs, managed futures ETFs

**Cross-check completeness estimate of first read:** 0.80 - first reader caught all major theses (complexity vs cost, QIS backtest decay, crowding in March) but missed QIS dispersion, wrapper-universe data, several data sources and Niels's counterpoints; 5 speaker/meaning errors.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | geopolitical tail risk |
| C02 | 3 | regime change, range of outcomes |
| C03 | 1 | AI for efficiency |
| C04 | 3 | trend barometer, CTA index returns, speed of models |
| C05 | 4 | Q1 CTA performance, Jan-Feb trend, March reversal, energy |
| C06 | 3 | derisking, short-term vs diversified, 2022 analogy |
| C07 | 3 | smart money March losses, crowding |
| C08 | 2 | CTA ETF vs mutual fund vs hedge fund complexity and returns |
| C09 | 4 | selection bias, early contrarian trades, signal vs implementation |
| C10 | 5 | quant on quant, capacity, cost of buying alpha |
| C11 | 5 | replication outperformance, true implementation costs |
| C12 | 3 | index composition bias, probability of beating index |
| C13 | 4 | data sources, index autocorrelation, active vs passive |
| C14 | 2 | allocator behavior, active ETF share |
| C15 | 3 | trend not a definable beta, QIS growth |
| C16 | 3 | QIS backtest vs live |
| C17 | 4 | QIS underperformance and dispersion, index immutability |
| C18 | 2 | swap wrappers, tax and reported fees |
| C19 | 1 | flawed UCITS trading cost reporting |
| C20 | 2 | tax efficiency, model-portfolio product design |
| C21 | 0 | nothing actionable: outro and disclaimer |

## Claims

### C01
- **Andrew Beer** Geopolitical shock with unknowable parameters (9/11-style tail event) is a major unhedgeable risk in the current environment, argued by analogy to 9/11.  #mech/new _(time-bound view)_
  > we've opened a Pandora's box that we don't really know what what what the parameters are
  asset: multi · testable: no - narrative opinion · confidence: medium
  ^MT056-C01-1

### C02
- **Andrew Beer** Earlier crises (GFC, pandemic) were fixed by Fed or fiscal action, but this ideology-driven geopolitical crisis cannot be, so it is a different regime that will persist.  #mech/structural_shift _(time-bound view)_
  > All of those more or less could be fixed by the Federal Reserve coming in with a big bazooka
  asset: multi · conditions: crisis driven by ideology rather than liquidity/credit · testable: no - qualitative regime claim · confidence: medium
  **Correction (cross-check):** Wrong speaker: the 'crises could be fixed by the Fed / this one is about ideology / different regime' view is the host Niels, continuing his question from C01. → Niels Kaastrup-Larsen: earlier crises (GFC, pandemic) could be fixed by Fed or fiscal action, but this ideology-driven geopolitical crisis cannot, so it is a different regime that will persist.
  ^MT056-C02-1
- **Andrew Beer** Geopolitical negotiation outcomes range from zero to ten, so markets whipsaw as they try to price each headline.  #mech/behavioral _(time-bound view)_
  > the range of outcomes is not like between you know four and six
  asset: multi · horizon: days · conditions: binary-like geopolitical headline risk · testable: partly - whipsaw/vol can be measured · confidence: medium
  ^MT056-C02-2
- **Andrew Beer** Escalation by a transactional negotiator lets the counterparty choose when to de-escalate, so unintended consequences and large two-sided jumps are possible.  #mech/behavioral _(time-bound view)_
  > in a war, the other side has a vote
  asset: multi · testable: no - qualitative · confidence: low
  ^MT056-C02-3

### C03
- **Andrew Beer** AI tools that cost hundreds of billions to build are cheap to use, giving asset managers large efficiency gains in programming and trade reconciliation rather than in the investment strategy itself.  #mech/structural_shift
  > they're basically giving us for like $20 a month
  asset: other · testable: no - business efficiency claim · confidence: medium
  ^MT056-C03-1

### C04
- **Niels Kaastrup-Larsen** A trend barometer reading near 48 signals a neutral, directionless trend environment where markets flip day to day on Middle East headlines.  #mech/cycle_persistence _(time-bound view)_
  > my own trend barometer yesterday uh closed at 48 which indicates kind of a neutral environment right now
  indicator: Niels trend barometer (proprietary) · asset: multi · horizon: days · testable: partly - proprietary gauge, definition not given · confidence: medium
  ^MT056-C04-1
- **Niels Kaastrup-Larsen** In whipsaw regimes of the last three years, slower trend models have fared better than faster ones, although speed may differentiate returns differently this time.  #mech/slow_reaction
  > being slow has certainly in these situations been useful
  asset: multi · direction: slow models better in choppy markets · horizon: months · conditions: headline-driven reversals; last three years only · testable: yes - compare fast vs slow trend indices · confidence: low
  ^MT056-C04-2
- **Niels Kaastrup-Larsen** Reported YTD index returns: BTOP50 above 8%, SG CTA about 8.5%, SG Trend about 8.5%, short-term traders 4.78% (as of a Tuesday in April 2026), showing CTAs positive despite the neutral trend environment.  #mech/risk_premium _(time-bound view)_
  > the Btop 50 index was up 83 basis points
  indicator: BTOP50, SG CTA, SG Trend, SG Short-Term Traders indices · asset: multi · horizon: months · testable: yes - public index data · confidence: high
  ^MT056-C04-3

### C05
- **Niels Kaastrup-Larsen** On a day when markets moved against CTA positioning, CTA returns were only slightly negative, which Niels attributes to risk management discipline.  #mech/risk_management _(time-bound view)_
  > I think that's a great testament really to how risk management um and how people are are um really focused on on this
  asset: multi · horizon: days · testable: partly - needs positioning data · confidence: medium
  ^MT056-C05-1
- **Andrew Beer** Q1 2026 SG CTA +7.5% while US equities fell and bonds were flat or down is an example of the crisis-alpha role of trend following, though one quarter is not a year.  #mech/risk_premium _(time-bound view)_
  > that should be one of those iconic quarters that you point to when it the strategy is really doing doing its job
  indicator: SG CTA index vs S&P 500 and bonds · asset: multi · direction: long CTAs as diversifier in equity drawdown · horizon: months · conditions: equity decline with flat/down bonds · testable: yes - quarterly index data · confidence: medium
  ^MT056-C05-2
- **Andrew Beer** Positions that worked in Jan-Feb (gold up 30%, non-US and EM equities) reversed violently in March when oil spiked, hitting funds that had been winning most.  #mech/overshoot _(time-bound view)_
  > I've called it the the the great macro doover of 2026
  indicator: gold, non-US equities, EM equities, crude oil · asset: multi · direction: trend positions reversed · horizon: weeks · conditions: geopolitical oil shock after strong two-month trends · testable: yes - price data · confidence: high
  ^MT056-C05-3
- **Andrew Beer** The replication model had no energy exposure at end-2025, added it from January as trends emerged, took a hit in March, and gradually de-risked positions that stopped working, including equity risk.  #mech/risk_management _(time-bound view)_
  > what we've seen in our portfolios is basically a gradual derisking
  indicator: trend signals in energy · asset: multi · direction: add energy exposure as trend forms; cut positions not working · horizon: months · testable: partly - model rule is proprietary · confidence: medium
  ^MT056-C05-4

### C06
- **Andrew Beer** Rather than full crash-protection mode, the manager partially de-risks (shin guards and pads) when positions reverse in an unstable market.  #mech/risk_management _(time-bound view)_
  > we've put on shinuards and knee pads maybe elbow pads
  asset: multi · direction: partial de-risk · conditions: unstable, headline-driven market · testable: no - discretionary description · confidence: medium
  ^MT056-C06-1
- **Niels Kaastrup-Larsen** Either short-term models that exit quickly or broad diversification across many contracts (not concentrated in WTI) may explain which CTAs fared better in March.  #mech/slow_reaction _(time-bound view)_
  > short-term models may have been a saving grace in March you know you may have gotten out faster
  asset: multi · direction: short-term trend or wide diversification reduced March losses · horizon: weeks · conditions: sharp reversal after escalation/de-escalation · testable: yes - compare fast vs diversified CTA returns · confidence: low
  **Correction (cross-check):** Wrong speaker: this is Andrew Beer speaking (he continues until 'We'll see.'), not Niels. → Andrew Beer: either short-term models that exited quickly or broad diversification across many contracts (not concentrated in WTI) may explain which CTAs fared better in March.
  ^MT056-C06-2
- **Andrew Beer** If the conflict raises inflation so stocks and bonds fall together as in 2022, trend following would again deliver a very strong year; if the world normalizes it lags equities.  #mech/cycle_persistence
  > it plays out through through stocks and bonds at the same time which again have the same risk which is inflation
  indicator: stock-bond correlation · asset: multi · direction: long trend following when stocks and bonds fall together · horizon: years · conditions: inflationary shock hitting both stocks and bonds · testable: yes - 2022 analog and stock-bond correlation regimes · confidence: medium
  ^MT056-C06-3
- **Andrew Beer** In the March 2026 environment the trend book held offsetting pairs (long crude with long gold, long international stocks against short S&P), so headline swings partly netted out across positions.  #mech/risk_management _(added by opus cross-check, time-bound view)_
  > you're sort of hedged I guess because you know they they're kind of not going up or down if you have if you're long uh international stocks but short the S&P
  indicator: cross-position offsets in CTA book · asset: multi · direction: long crude + long gold; long non-US equities vs short S&P · horizon: weeks · conditions: geopolitical whipsaw regime · testable: partly - needs position data or replicated positions · confidence: low
  ^MT056-C06-X1
- **Andrew Beer** Trend books positioned for ongoing geopolitical chaos are exposed to sharp reversal days on de-escalation news (e.g. a ceasefire announcement), similar to the Liberation Day reversal.  #mech/overshoot _(added by opus cross-check, time-bound view)_
  > from a positioning perspective when you see yourself kind of positioning for for like ongoing chaos.
  indicator: ceasefire / de-escalation headlines · asset: multi · direction: trend positions lose on de-escalation days · horizon: days · conditions: positions built on conflict trends (long oil, short bonds) · testable: yes - CTA index returns on de-escalation event days · confidence: medium
  ^MT056-C06-X2

### C07
- **Niels Kaastrup-Larsen** Longer-term trend managers remained long equities with reduced size, so the April equity rebound probably helped them, with currencies and precious metals also contributing.  #mech/slow_reaction _(time-bound view)_
  > longerterm managers are overall still long even though with smaller positions
  asset: equities · direction: long equities (smaller) · horizon: weeks · conditions: April 2026 rebound · testable: partly - needs positioning data · confidence: low
  ^MT056-C07-1
- **Andrew Beer** In March 2026 the funds that did best in Jan-Feb lost the most, so CTA drawdown reflected crowded smart-money positioning across hedge funds, not a CTA-specific failure as in the Liberation Day episode.  #mech/crowding_positioning _(time-bound view)_
  > the better you're doing in January, February, the more you got shellocked generally in in in March
  asset: multi · direction: winners of prior months were hit hardest · horizon: weeks · conditions: common smart-money trades reverse together · testable: yes - Bloomberg hedge-fund return rankings · confidence: medium
  ^MT056-C07-2
- **Andrew Beer** Named March 2026 returns: Citadel fixed income about -8%, Brevan Howard -6%, Capstone -15%, Marshall Wace Eureka -5%, plus wide dispersion among UCITS CTAs, supporting the crowding explanation.  #mech/crowding_positioning _(time-bound view)_
  > Brevin Howard was down six
  indicator: Bloomberg hedge fund return rankings (Nishant Kumar) · asset: multi · horizon: weeks · testable: yes - published monthly returns · confidence: medium
  **Correction (cross-check):** 'Cton down 15%' is most likely Caxton, not Capstone; the list (partly read by Niels) also includes an absolute-return fund down 6. → Named March 2026 returns: Citadel fixed income about -8%, Brevan Howard -6%, 'Cton' (likely Caxton) -15%, an absolute-return fund -6%, Marshall Wace Eureka -5%, plus wide dispersion among UCITS CTAs.
  ^MT056-C07-3
- **Andrew Beer** Bloomberg's hedge-fund return rankings (published by Nishant Kumar) are a timely data source for checking whether CTA drawdowns are shared by the wider macro hedge-fund space.  #mech/research_method _(added by opus cross-check)_
  > he covers hedge funds for Bloomberg and he publishes the basically the rankings or the returns rankings of underlying hedge funds and he puts it up on LinkedIn and his data is great and it's up to date
  indicator: Bloomberg hedge fund monthly return rankings · asset: multi · horizon: months · testable: partly - data source, not a signal · confidence: high
  ^MT056-C07-X1
- **Andrew Beer** Trend following is best seen as latching onto the same big trades that discretionary smart-money funds reach by other routes, so CTA and macro hedge-fund returns move together in reversals.  #mech/crowding_positioning _(added by opus cross-check)_
  > I often think about this this strategy as latching on to these kinds of smart money trades that that people are coming to the same conclusion but from a different perspective.
  indicator: CTA vs macro hedge fund return correlation · asset: multi · horizon: months · conditions: big consensus macro trades · testable: yes - correlation of CTA index with discretionary macro indices · confidence: medium
  ^MT056-C07-X2

### C08
- **Andrew Beer** The CTA product universe (hedge funds, then mutual funds and UCITS, then ETFs) falls in complexity, with ETFs simplified to plain trend with fewer instruments.  #mech/structural_shift
  > when people have done ETFs, they've tended to strip out a lot of complexity
  asset: multi · testable: yes - classify products by instrument count · confidence: high
  ^MT056-C08-1
- **Andrew Beer** Over the last five years the average CTA ETF returned about 6.1% a year with a higher Sharpe ratio than the SG CTA index and outperformed mutual funds and UCITS, so more complexity does not produce higher alpha.  #mech/research_method
  > which is 40 basis points higher on an edify basis than the socken CTA index
  indicator: average CTA ETF vs SG CTA index, Morningstar data · asset: multi · direction: simple/efficient CTA products outperform complex ones · horizon: years · conditions: only five years of reliable data, 16 ETFs · testable: yes - Morningstar fund returns · confidence: medium
  ^MT056-C08-2
- **Andrew Beer** Morningstar data: 16 managed-futures ETFs (from about 2 in 2019), 18 US mutual funds and 45 UCITS funds, with UCITS AUM below mutual-fund AUM; this population allows wrapper-by-wrapper performance comparisons, with short histories as a caveat.  #mech/research_method _(added by opus cross-check, time-bound view)_
  > There are 16 funds in that space. Uh when we got into the space in 2019, there are basically two. Um compare it. There are only 18 mutual funds.
  indicator: Morningstar managed futures fund universe by wrapper · asset: multi · horizon: years · conditions: data mostly recent · testable: yes - Morningstar category data · confidence: high
  ^MT056-C08-X1

### C09
- **Andrew Beer** ETF outperformance may be selection bias from a few funds launching and doing well; Beer says the evidence has not yet shown that and will re-check periodically.  #mech/research_method
  > this could all be selection bias a handful of funds happen to have launched
  asset: multi · testable: yes - re-test as the sample grows · confidence: medium
  ^MT056-C09-1
- **Andrew Beer** Trend signals pay by catching a few big moves early, e.g. shorting Treasuries in Sept 2020 once yields rose from 0.5% to 0.7%, buying gold below 3,000 after a decade of failure, shorting crude at 105-110 and riding it down.  #mech/slow_reaction
  > you can be early contrarian and right into a handful of big trades
  indicator: 10-year Treasury yield, gold, crude oil · asset: multi · direction: short Treasuries 2020, long gold, short crude · horizon: years · conditions: large persistent trends from a modest initial signal · testable: yes - trend backtests on these markets · confidence: high
  **Correction (cross-check):** Misread: 'shorting the end at 105 or 110 riding it down to 160' refers to shorting the yen (USD/JPY from 105-110 to 160), separate from buying crude oil earlier this year; it is not shorting crude. → Trend signals pay by catching a few big moves early: shorting Treasuries in Sept 2020 once 10y yields rose from 0.5% to 0.7%, buying gold below 3,000 after a decade of failure, buying crude early this year, and shorting the yen from 105-110 down to 160 per dollar.
  ^MT056-C09-2
- **Andrew Beer** Most dollars made in CTAs come from a handful of big cross-asset trades, not from many orthogonal positions, so replication focuses on clusters and cross-asset relationships.  #mech/structural_shift
  > not you know P&L from 100 different orthogonal positions
  asset: multi · direction: concentrate on clusters of related markets · testable: yes - decompose CTA P&L by position · confidence: medium
  ^MT056-C09-3
- **Andrew Beer** Use a complex model to detect the signal but a second decision (e.g. PCA/clustering) to implement it in fewer, more liquid contracts, such as one contract for global equity exposure.  #mech/risk_management
  > should I be long 15 different equity markets or should I compress that into a long EHA contract or a long EM contract
  asset: equities · direction: compress many correlated markets into one liquid contract · testable: yes - compare full vs compressed portfolios net of cost · confidence: medium
  ^MT056-C09-4

### C10
- **Niels Kaastrup-Larsen** Replication still needs complex underlying managers to produce the returns it replicates; complexity must exist somewhere even if the investor does not pay for it.  #mech/structural_shift
  > quant on top of quant
  asset: multi · testable: no - conceptual · confidence: medium
  ^MT056-C10-1
- **Andrew Beer** Intraday or high-frequency trend models may show very high Sharpe but only at tiny capacity, so signal quality must be weighed against implementation capacity.  #mech/risk_management
  > it works with $3 million, right? But it doesn't work with 50
  asset: multi · horizon: days · conditions: fails as assets scale from 3 million to 50 to 500 million · testable: yes - capacity analysis · confidence: medium
  ^MT056-C10-2
- **Andrew Beer** Gross excess return is worthless if the cost to implement it, including conditional liquidity, equals the gain; signal and implementation must be evaluated together.  #mech/risk_management
  > let's get 300 basis points of excess returns on this thing but it's going to cost me 300 basis points
  asset: multi · testable: yes - net-of-cost backtest · confidence: high
  ^MT056-C10-3
- **Andrew Beer** Equity-index signals from many markets can be aggregated and implemented in fewer positions, so signal complexity does not require implementation complexity.  #mech/research_method
  > Yes, you need complexity for the signal.
  asset: equities · testable: yes - test aggregation vs many-market implementation · confidence: medium
  ^MT056-C10-4
- **Andrew Beer** The replication model launched July 2016 outperformed each of the 20 SG CTA index constituents of that time on absolute and risk-adjusted return, supporting efficiency over complexity.  #mech/research_method
  > We have outperformed every single one on an absolute and riskadjusted basis.
  indicator: replication model vs SG CTA constituents · asset: multi · horizon: years · conditions: constituents as of 2016; later-added managers excluded · testable: yes - compare to constituent returns · confidence: high
  ^MT056-C10-5

### C11
- **Andrew Beer** Claimed excess return of 400 bp a year over the average SG CTA index constituent since July 2016.  #mech/research_method
  > We've outperformed the overall the average by 400 basis points a year.
  asset: multi · horizon: years · testable: yes - compute from published NAVs · confidence: high
  ^MT056-C11-1
- **Andrew Beer** True implementation costs (bid-ask, market impact in thin markets such as Chinese power or South African soybeans) are the unspoken problem of CTAs; quants are the dumb money that physical traders like Louis Dreyfus and Glencore pick off.  #mech/risk_management
  > what are the true implementation costs
  asset: commodities · direction: costs high in illiquid markets · conditions: thin supply-demand markets with informed physical traders · testable: partly - hard to observe impact cost · confidence: medium
  ^MT056-C11-2
- **Andrew Beer** A complex model trading a lot moves prices; when several similar managers trade together the price overshoots and then reverts, so execution looks fine against the close but adds hidden cost.  #mech/crowding_positioning
  > your execution price was slightly below where it ended for the day. But you're driving it.
  asset: multi · horizon: days · conditions: many managers trading the same signal at the same time · testable: partly - needs trade-level data · confidence: medium
  ^MT056-C11-3
- **Andrew Beer** Implementation costs rise geometrically with the number of positions, so by position 180 or 350 the marginal market is a coin toss on whether it trends enough to pay for its costs.  #mech/risk_management
  > it's a coin toss as to whether that market is going to trend enough
  asset: multi · direction: fewer markets, more efficient · horizon: years · conditions: disputed; some smart managers report hundreds of markets work · testable: yes - marginal-market contribution net of cost · confidence: medium
  ^MT056-C11-4
- **Niels Kaastrup-Larsen** Niels also doubts that trading hundreds of markets is better, though some peers do well with hundreds of markets due to exposure to different factors.  #mech/research_method
  > not a believer that trading hundreds of markets is necessarily better
  asset: multi · testable: yes - compare breadth vs performance · confidence: medium
  ^MT056-C11-5

### C12
- **Niels Kaastrup-Larsen** Comparison to constituents of a fixed starting set is biased because later managers that did better were added to the index, so index composition changes over time (survivorship/inclusion).  #mech/research_method
  > they get included in the index and so they're in the index today
  asset: multi · conditions: when comparing replication with a historical constituent list · testable: yes - point-in-time constituent list · confidence: medium
  **Correction (cross-check):** Wrong speaker: Niels only doubts the numbers; the survivorship/inclusion argument (later, better managers were added to the index) is Andrew Beer's reply. → Andrew Beer: none of the 2016 index constituents beat the replication; managers that did better were outside that group and were added to the index later, so comparisons against today's index members are biased by inclusion.
  ^MT056-C12-1
- **Andrew Beer** Beer could not beat the SG CTA index via own models, QIS products or manager selection, so he sought a structural efficiency advantage in capturing the same signal.  #mech/research_method
  > The way for me to beat the index over time was to capture the signal more efficiently.
  asset: multi · horizon: years · testable: yes - replication tracking and excess return · confidence: high
  ^MT056-C12-2
- **Andrew Beer** The replication beats the index in 54% of one-week rolling windows (overshoot +73 bp, undershoot -70 bp), which compounds to about 80% over a year and 90%+ over three years.  #mech/research_method
  > if you have a 54% chance probability you just keep doing it again and again and again
  asset: multi · horizon: weeks · conditions: no strong skew; small edge repeated often · testable: yes - rolling outperformance frequency · confidence: medium
  ^MT056-C12-3
- **Andrew Beer** An edge over a benchmark comes either from a higher hit rate or from positive skew of wins; replication's edge is a small hit-rate advantage with symmetric outcomes, not skew.  #mech/research_method _(added by opus cross-check)_
  > you're either have a higher probability of winning or you're or or you know you'll have some great skew when you win. We don't have great skew in that.
  indicator: weekly hit rate and win/loss size vs benchmark · asset: multi · horizon: weeks · testable: yes - hit rate and skew of weekly relative returns · confidence: high
  ^MT056-C12-X1

### C13
- **Niels Kaastrup-Larsen** Five to ten years of performance data is limited evidence about the future of a product.  #mech/research_method
  > 5 years, 10 years of data doesn't say much about the future
  asset: multi · testable: no - general statistical caution · confidence: high
  ^MT056-C13-1
- **Andrew Beer** Hedge funds cannot easily stop publishing; mutual fund and UCITS disclosure forces data, and a US multi-manager CTA mutual fund is the cleanest signal source.  #mech/research_method
  > I actually think the cleanest data on the space overall from a signal perspective is a multi-manager mutual fund in the US
  asset: multi · testable: yes - compare data sources · confidence: medium
  ^MT056-C13-2
- **Andrew Beer** The SG CTA index has lagged autocorrelation because European managers close before US afternoon moves, making the replication signal foggier.  #mech/slow_reaction
  > a lot of European managers have already closed their books
  indicator: SG CTA index · asset: multi · horizon: days · conditions: US-hour market moves after Europe close · testable: yes - test autocorrelation of index returns · confidence: medium
  ^MT056-C13-3
- **Andrew Beer** Passive beating active is mathematically settled, yet active still has more assets, so product choice reflects behavior and distribution, not only cost.  #mech/behavioral
  > An S&P 500 three basis point S&P 500 ETF is simply a better investment than trying to pick long only managers
  asset: equities · direction: passive low-cost over active · testable: yes - fee drag studies · confidence: high
  ^MT056-C13-4
- **Andrew Beer** Replication inputs need not be hedge-fund returns only: QIS product returns or the firm's own internal trend models (used for risk management, not invested) can also supply the signal.  #mech/research_method _(added by opus cross-check)_
  > we could build our own series of you know basically trend we run our own trend volume following models we just don't invest in them
  indicator: QIS returns; internal trend model returns · asset: multi · conditions: if hedge funds stopped publishing data · testable: yes - compare replication fit using each input set · confidence: medium
  ^MT056-C13-X1

### C14
- **Andrew Beer** Fund selectors optimize for defensible choices (e.g. AQR with its 70-page papers) rather than Sharpe, so career risk shapes allocation flows.  #mech/behavioral
  > fund selectors are not rational value maximizer, sharp ratio maximizers
  asset: multi · testable: no - qualitative · confidence: medium
  ^MT056-C14-1
- **Andrew Beer** Active ETFs are now 31% of the US mutual fund plus ETF business as mutual funds shrink, supporting wrapper migration.  #mech/structural_shift _(time-bound view)_
  > it's now 31% of the mutual funded ETF business in the US
  asset: other · horizon: years · testable: yes - industry data · confidence: medium
  ^MT056-C14-2
- **Niels Kaastrup-Larsen** A Goldman Sachs paper shows fund flows going heavily to passive and away from active managers, though Beer notes rising markets over the period and that active assets in dollars remain larger.  #mech/structural_shift _(added by opus cross-check)_
  > there was a chart in in that paper about the flows uh in terms of what has gone into active what has gone into passive
  indicator: active vs passive fund flows (Goldman Sachs paper) · asset: equities · direction: flows to passive, out of active · horizon: years · conditions: rising markets over the sample · testable: yes - fund flow data · confidence: medium
  ^MT056-C14-X1

### C15
- **Andrew Beer** Trend following is not an identifiable beta: different trend models or QIS products can differ by 20-30 points, unlike US large-cap equity indices.  #mech/research_method
  > you and I and all these people have different trend models or pick different QIS products and you're 20 points off
  asset: multi · horizon: years · testable: yes - dispersion across trend indices · confidence: high
  ^MT056-C15-1
- **Andrew Beer** Merger arbitrage replication also fails as a single beta: once parameters are specified, portfolios concentrate in different deals and diverge.  #mech/research_method
  > by the time we specify all the different parameters
  asset: other · testable: yes - dispersion across replicas · confidence: medium
  ^MT056-C15-2
- **Andrew Beer** Bank QIS products took off in 2012-13 after hedge funds embarrassed themselves in the GFC; allocators wanted cheaper, more liquid exposure.  #mech/structural_shift
  > the space really took off in I would say 2012 2013
  asset: multi · horizon: years · testable: no - history · confidence: medium
  ^MT056-C15-3
- **Andrew Beer** Factor-based replication works poorly for low-net strategies such as merger arbitrage, which is why a bolt-on QIS product was considered instead.  #mech/research_method _(added by opus cross-check)_
  > Our factor models don't do a good job with something like merger R, but there's a very low net.
  indicator: factor-model replication fit for merger arbitrage · asset: equities · conditions: low net exposure strategies · testable: yes - R-squared of factor replication by strategy · confidence: high
  ^MT056-C15-X1

### C16
- **Andrew Beer** Bank QIS products sold with long track records (e.g. G10 carry Sharpe 1.4 in backtest) show Sharpe near 0.2 live, as the track record is mostly a backtest.  #mech/research_method
  > What's your sharp ratio live? 02.
  indicator: G10 currency carry QIS Sharpe · asset: fx · direction: backtest Sharpe overstated · horizon: years · conditions: index launched with back-filled history · testable: yes - compare backtest to live Sharpe · confidence: high
  ^MT056-C16-1
- **Andrew Beer** QIS products are closed and replaced, so failing strategies disappear and surviving ones look better; this survivorship makes allocators unable to evaluate them.  #mech/research_method
  > sorry, that one's gone. We have a new G10 currency thing.
  asset: multi · testable: yes - track defunct products · confidence: medium
  ^MT056-C16-2
- **Andrew Beer** Index backtests are what the bank wishes it had traded, with dials tuned, so they are weak evidence of future results.  #mech/research_method
  > usually it's just made up stuff
  asset: multi · testable: yes - in-sample vs out-of-sample · confidence: high
  ^MT056-C16-3
- **Andrew Beer** Pension staff like QIS products partly because they get to act as portfolio managers with long backtests to present, a principal-agent issue that drives demand regardless of live results.  #mech/behavioral _(added by opus cross-check)_
  > It's a new principal agent issue. It's it's it's it's you're you're you're arming them with basically macro quantitative macro weapons.
  asset: multi · horizon: years · testable: no - motive statement · confidence: medium
  ^MT056-C16-X1
- **Andrew Beer** QIS strategies come in multiple versions (different vol targets, excess vs total return), so allocators must normalise for volatility and cash return before comparing products.  #mech/research_method _(added by opus cross-check)_
  > you might have four different indices of the same strategy with different vault targets. You'll have excess return versus total return.
  indicator: QIS index variants (vol target, ER vs TR) · asset: multi · testable: partly - data-handling caveat · confidence: high
  ^MT056-C16-X2
- **Andrew Beer** Trend exposure held through bank QIS products is in the hundreds of billions, and its buyers differ (fund selectors seeking a fiduciary vs staff wanting PM-style tools), so it is a large, separate pool of trend capital.  #mech/liquidity_flows _(added by opus cross-check)_
  > there's hundreds of billions of dollars in in QIS products and things out there.
  indicator: QIS trend AUM · asset: multi · horizon: years · testable: partly - AUM estimates hard to verify · confidence: low
  ^MT056-C16-X3

### C17
- **Andrew Beer** About 17 tracked QIS trend products have returned roughly 200 bp a year less than the SG CTA index.  #mech/research_method
  > has done 200 basis points of excess returns less than the sog CTA index
  indicator: 17 QIS trend products on Bloomberg vs SG CTA index · asset: multi · horizon: years · testable: yes - Bloomberg data · confidence: high
  ^MT056-C17-1
- **Andrew Beer** QIS trend products lose about 90% of their Sharpe ratio between in-sample backtest and out-of-sample live.  #mech/research_method
  > the drop from the insample sharp ratio to the out of sample sharp ratio is 90%
  asset: multi · horizon: years · testable: yes - Bloomberg data · confidence: high
  ^MT056-C17-2
- **Andrew Beer** Swap-based QIS trend products report no fees and can be layered as portable alpha, making them a bigger competitor to hedge funds than replication is.  #mech/structural_shift
  > you're basically get exposure to trend from banks for zero fees
  asset: multi · testable: no - business point · confidence: medium
  ^MT056-C17-3
- **Andrew Beer** Indices are not supposed to change after launch, so banks launch new indices for each enhancement, producing a constant stream of products without live history.  #mech/research_method
  > it's a constant series of launching new indices
  asset: multi · testable: no - industry practice · confidence: medium
  ^MT056-C17-4
- **Andrew Beer** Annual return dispersion among QIS trend products reaches up to 40 percentage points in some years, so the choice of product dominates any notion of a common trend beta.  #mech/research_method _(added by opus cross-check)_
  > That the dispersion among products in some years is up to 40%.
  indicator: cross-product return dispersion of ~17 QIS trend indices · asset: multi · horizon: years · testable: yes - Bloomberg QIS index data · confidence: high
  ^MT056-C17-X1
- **Niels Kaastrup-Larsen** Niels contrasts fixed QIS indices with CTAs that keep researching and upgrading models, arguing ongoing research improves a trend product over time.  #mech/research_method _(added by opus cross-check)_
  > like a quarter of our company is is in research and we do make upgrades. We do believe that our product today is better than what we had 10 years ago.
  asset: multi · horizon: years · testable: partly - compare live performance of evolving vs frozen models · confidence: medium
  ^MT056-C17-X2
- **Andrew Beer** Premialab aggregates bank QIS index data and is a source for allocators trying to compare QIS products.  #mech/research_method _(added by opus cross-check)_
  > there's a company called called Premier Lab which we don't use but they have a lot of I mean they basically [L700] try to aggregate all this stuff
  indicator: Premialab QIS database · asset: multi · testable: partly - data source · confidence: medium
  ^MT056-C17-X3

### C18
- **Andrew Beer** A swap-based ETF on an index can be 35 bp reported and more tax efficient, because derivatives allow a cheaper and tax-advantaged structure.  #mech/structural_shift _(time-bound view)_
  > meaningfully more tax efficient than any other product out there
  asset: multi · direction: swap/derivative wrapper · testable: yes - after-tax return calculation · confidence: medium
  ^MT056-C18-1
- **Andrew Beer** Reported fee comparisons ignore swap and trading costs; DBMF at 85 bp with near-zero trading cost competes against 170 bp mutual funds with about 200 bp trading costs.  #mech/risk_management
  > 170 basis point mutual funds out there that probably have 200 basis points in trading costs
  asset: multi · testable: yes - all-in cost comparison · confidence: medium
  ^MT056-C18-2
- **Niels Kaastrup-Larsen** Swap-based products on a manager's index report only the wrapper fee, not the underlying index fee, so reported expense ratios understate total cost.  #mech/research_method _(added by opus cross-check)_
  > you can just do a product use a swap and then you don't have to report any fees.
  indicator: reported expense ratio vs embedded swap fee · asset: multi · conditions: swap-based wrappers · testable: partly - requires swap term data · confidence: high
  ^MT056-C18-X1

### C19
- **Andrew Beer** UCITS fund transaction-cost calculations measure execution versus settlement, so pushing the price up while buying shows a negative cost, and some funds report zero costs when real costs are a couple of hundred bp.  #mech/risk_management
  > that's a negative trading cost because I'm comparing my execution price to the settlement price at the end of the day
  asset: multi · conditions: benchmark is end-of-day settlement price · testable: yes - implementation shortfall vs arrival price · confidence: high
  ^MT056-C19-1
- **Andrew Beer** Fee reporting can be gamed (e.g. 0% management / 40% incentive share classes reported as zero fee), so only net returns allow fair comparison.  #mech/research_method _(added by opus cross-check)_
  > they're bragging about having zero and 40 share class 40% incentive fee share classes because they can report the zero, not the 40.
  asset: multi · testable: no - anecdote · confidence: high
  ^MT056-C19-X1

### C20
- **Andrew Beer** Tax efficiency (futures held in the entity, not Cayman subs; swap structure) could save about 150 bp a year in after-tax returns.  #mech/structural_shift
  > an investor might save 150 basis points
  asset: multi · direction: tax-efficient wrapper · horizon: years · testable: yes - after-tax return model · confidence: low
  ^MT056-C20-1
- **Andrew Beer** Model-portfolio allocators with 25 bp expense ratios need a low-cost, tax-efficient, ETF-style trend allocation sized at 3-5%.  #mech/structural_shift
  > easy for that person to make this a three or a 5% allocation
  asset: multi · direction: 3-5% diversifier allocation · testable: no - product design · confidence: medium
  ^MT056-C20-2

