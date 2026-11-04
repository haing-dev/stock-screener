---
source_id: MT205
title: "Unpacking the Chaos- What Today’s Market Signals Really Mean - Systematic Investor 343"
date: 2025-04-21
channel: "Top Traders Unplugged"
url: 
words: 12215
claims: 57
added_by_crosscheck: 10
corrections: 1
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Yo Kit (guest, systematic CTA manager and researcher)", "Neils Castro Larsson (host, hedge fund manager)"]
tags: [source, layer0]
---
# Unpacking the Chaos- What Today’s Market Signals Really Mean - Systematic Investor 343

**Speakers:** Yo Kit (guest, systematic CTA manager and researcher); Neils Castro Larsson (host, hedge fund manager)

**Summary:** Systematic Investor episode recorded 10 April 2025 after the tariff-pause reversal. Covers bond-market stress and failure of safe-haven behaviour, how trend followers lost in April (speed and de-risking after vol spikes), crisis alpha stats by drawdown stage (first vs second responders), why CTA diversification is about market beta to the first factor not market count, high manager-to-manager correlation (about 50%), and cost-aware signal design.

**Approach:** trend following, crisis alpha, diversification, CTA dispersion, stock-bond correlation, signal design, transaction costs

**Cross-check completeness estimate of first read:** 0.88 - the first reader caught the bond-market, first/second-responder, diversification-factor, correlation, cost and mean-reversion arguments; missed the EM liquidity and curve-divergence observations, Niels' dispersion expectation, the mid-April YTD numbers, the out-of-sample stress-test idea, model-type speed, the caveat on attributing vol surprises to CTAs, the 'all the same' allocator problem, the breakout exception to the cost logic and Niels' pushback on cost-gating.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro; MCP and AI chat, no market content |
| C02 | 4 | bond yield spike, stock-bond correlation, foreign ownership of US debt |
| C03 | 4 | bond rout caused tariff pause; safe-haven rethink; CTAs diversify |
| C04 | 2 | where trend followers lost or gained; credit |
| C05 | 4 | country dispersion, April performance numbers, CTA risk cutting |
| C06 | 3 | index numbers; Tyler Loving drawdown study |
| C07 | 4 | first vs second responders; CTA speed migration |
| C08 | 3 | negative skew, day-one crisis, risk management, commodities |
| C09 | 3 | market count vs correlation, trade diversification, costs |
| C10 | 3 | exit correlation, vol impact of extended trend |
| C11 | 2 | trend predictor dispersion, sources of alpha, capacity |
| C12 | 3 | diversification factor and beta to first component |
| C13 | 2 | low-beta markets, CFM dispersion study |
| C14 | 2 | CTA correlation stable, capacity offbeat, trend works |
| C15 | 3 | bank front-running calls, time and price in trend signals |
| C16 | 3 | playing forward positions, front running |
| C17 | 2 | cost-aware trading, mean-reverting signals |
| C18 | 0 | outro |

## Claims

### C02
- **Neils Castro Larsson** In the April 2025 tariff shock the 10-year Treasury yield had its largest 3-day jump since 2001, failing as a safe haven.  #mech/policy_reaction _(time-bound view)_
  > the US 10-year note saw the biggest 3-day jump since 2001
  indicator: US 10-year yield · asset: rates · direction: yields up, bonds down in equity sell-off · horizon: days · testable: yes - yield series · confidence: high
  ^MT205-C02-1
- **Neils Castro Larsson** Reliance on negative stock-bond correlation in crises is unsafe; 2022 broke it and the first two decades of the century were the anomaly.  #mech/structural_shift
  > relying uh on a certain correlation between stocks and bonds uh especially during crisis periods
  indicator: stock-bond correlation · asset: multi · horizon: years · conditions: inflation / supply shocks make correlation positive · testable: yes - rolling correlation · confidence: high
  ^MT205-C02-2
- **Yo Kit** In the tariff shock Treasuries and the dollar fell together while Japanese yields dropped, a unique cross-country divergence; the 30-year touched 5%.  #mech/policy_reaction _(time-bound view)_
  > the usual response that you kind of expected running as a safe haven to the US treasuries. Uh that certainly did not happen.
  indicator: UST yields, USD, JGB · asset: rates · horizon: days · testable: yes - price data · confidence: high
  ^MT205-C02-3
- **Yo Kit** About 30% of US debt is foreign owned and about $2 trillion must be refinanced each year, so a trade war can escalate to a capital war via foreign selling of Treasuries.  #mech/fiscal_debt _(time-bound view)_
  > if you start a trade war, this can quite happily escalate into capital war
  indicator: foreign ownership of US debt, auction demand · asset: rates · horizon: months · conditions: US relies on foreign bond buyers · testable: partly - foreign holdings TIC data · confidence: medium
  ^MT205-C02-4

### C03
- **Yo Kit** The Treasury rout probably forced the tariff pause because a bond market collapse is intolerable, unlike a temporary equity or goods price fall.  #mech/policy_reaction _(time-bound view)_
  > bond market in the US was actually much more potentially much more influential in causing the pause in the tariffs
  indicator: US 10y yield · asset: rates · horizon: days · testable: no - causal inference · confidence: medium
  ^MT205-C03-1
- **Yo Kit** When inflation is the concern, stocks and bonds are positively correlated, so a 60/40 portfolio cannot rely on bonds as a diversifier.  #mech/structural_shift
  > when there is concerns about inflation then you actually get positive correlation
  indicator: stock-bond correlation, inflation expectations · asset: multi · horizon: years · conditions: inflation regime · testable: yes - rolling correlation versus inflation · confidence: high
  ^MT205-C03-2
- **Neils Castro Larsson** Safe-haven assets need rethinking: gold held up, crypto would have been unsafe, and trend following may be a safe-haven because it adapts.  #mech/risk_management _(time-bound view)_
  > I even wonder if trend following could be quote unquote a safe asset because of the adaptability
  indicator: gold, CTA index · asset: multi · testable: partly - crisis sample small · confidence: low
  ^MT205-C03-3
- **Yo Kit** When one factor (inflation) drives commodities, equities and bonds together, diversification needs strategies like CTAs rather than traditional assets.  #mech/structural_shift
  > in the presence of inflation when you have uh one factor which is driving the correlation for all the other asset classes
  indicator: cross-asset correlation · asset: multi · horizon: years · conditions: inflation regime · testable: yes - correlation study · confidence: medium
  ^MT205-C03-4
- **Yo Kit** In the April 2025 shock US futures liquidity held up, but emerging-market spreads were all over the place and markets such as South Africa (also hit by local news) were very hard to trade, so execution costs rose most outside the deep markets.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check, time-bound view)_
  > the US market stayed fairly liquid
  indicator: futures liquidity, EM bid-offer spreads · asset: multi · horizon: weeks · conditions: tariff shock, April 2025 · testable: yes - bid-offer and slippage data by market · confidence: medium
  ^MT205-C03-X1
- **Neils Castro Larsson** During the April 2025 bond rout trend signals within developed-market fixed income diverged unusually, especially between the long and the short end of the curve, so one rates position per country would not capture the moves.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > there's a lot of divergence uh within the signals that we get as trend followers right now compared to what we normally see uh and certainly also between the long end and the short end
  indicator: trend signals by maturity within fixed income · asset: rates · direction: long end and short end trend in different directions · horizon: weeks · conditions: bond-market stress · testable: yes - signal dispersion across the curve · confidence: medium
  ^MT205-C03-X2

### C04
- **Neils Castro Larsson** In April 2025 equities and long-dollar currency trends hurt trend followers; energy shorts offset for longer-term models, while short-term models flipped long in March and then lost.  #mech/slow_reaction _(time-bound view)_
  > it's actually energies. Now again a little bit tricky because energies actually traded higher during the month of March.
  indicator: sector attribution April 2025 · asset: multi · horizon: weeks · conditions: speed of model · testable: yes - sector attribution · confidence: medium
  ^MT205-C04-1
- **Yo Kit** Credit trend positions lost heavily in April 2025: credit held up while equities fell, then dropped, giving a delayed hit that behaves like equity beta.  #mech/slow_reaction _(time-bound view)_
  > one area of fixed income which has definitely been very painful for us has been credit
  indicator: credit spread trend · asset: credit · horizon: weeks · testable: yes - credit trend backtest · confidence: high
  ^MT205-C04-2
- **Neils Castro Larsson** Niels expected that, because of the speed of the April 2025 move and the sectors involved, normally highly correlated trend followers would show very different results; Yo Kit later cites CFM data that dispersion was not unusual.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > I would expect that managers who are normally fairly highly correlated um will have seen very different results in the last uh few weeks
  indicator: dispersion between CTA managers · asset: multi · horizon: weeks · conditions: fast V-shaped shock; differences in speed and sector mix · testable: yes - cross-section of manager returns in April 2025 · confidence: low
  ^MT205-C04-X1

### C05
- **Yo Kit** Tariff shock caused wide country dispersion in bonds and FX (Australia/NZ yields up, Japan down; Brazil and Mexico currencies fell despite low tariffs), so tariff size did not map to price moves.  #mech/policy_reaction _(time-bound view)_
  > we saw a huge dispersion in terms of behavior across the the fixed income and the effect space
  indicator: country yield and currency moves · asset: fx · horizon: weeks · testable: yes - cross-country price data · confidence: high
  ^MT205-C05-1
- **Neils Castro Larsson** Mid-April 2025 CTA performance: BTop50 -4.76%, SG CTA -5.53%, SG Trend -5.89% and short-term traders only -0.69% MTD, as short-term models fared far better.  #mech/slow_reaction _(time-bound view)_
  > the Btop 50 index was down for April 4.76%
  indicator: BTop50, SG CTA, SG Trend, SG Short-term Traders · asset: multi · horizon: weeks · testable: yes - index data · confidence: high
  ^MT205-C05-2
- **Yo Kit** After a sharp down move CTAs cut risk and so miss much of the sharp rebound; CTA indices will not recover as fast as markets.  #mech/crowding_positioning _(time-bound view)_
  > that sort of volatility where we have a large sharp uh down move will be followed by CTAs across the board cutting the risk
  indicator: volatility-based position scaling · asset: multi · direction: CTAs reduce exposure after vol spike · horizon: days · conditions: V-shaped reversals · testable: yes - vol targeting in backtests · confidence: high
  ^MT205-C05-3
- **Neils Castro Larsson** Volatility explosion cuts position sizes even faster than trend reversal signals do.  #mech/risk_management
  > The fact that markets are changing direction is actually the expansion or the explosion
  indicator: realised volatility · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT205-C05-4
- **Neils Castro Larsson** Mid-April 2025 year-to-date: SG CTA almost -8%, SG Trend about -10% and BTop50 about -4.5%, while the short-term traders index was only -0.71%, MSCI World -6.5%, S&P 500 total return -6.9% and the US aggregate bond index +1.6%, so CTAs were losing more than equities in the sell-off.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > down 5.53 for the month so far as of Tuesday down almost 8% for the year
  indicator: BTop50, SG CTA, SG Trend, SG Short-Term Traders, MSCI World, S&P 500 TR · asset: multi · horizon: months · conditions: 8 April 2025 data · testable: yes - index return data · confidence: high
  ^MT205-C05-X1

### C06
- **Neils Castro Larsson** On 9 April 2025 the S&P 500 rose 9.52%, the third largest one-day move since 1950.  #mech/overshoot _(time-bound view)_
  > Up 9.52% yesterday. That's the third biggest oneday move since 1950.
  indicator: S&P 500 daily return · asset: equities · horizon: days · testable: yes - price data · confidence: high
  ^MT205-C06-1
- **Neils Castro Larsson** Study by Tyler Loving: SG CTA index was only down 3.56% when the S&P first fell 10% (19 Feb to 11 Mar 2025); across about ten 10% S&P drawdowns since 2000 the average was -3.18%, median -2.81%.  #mech/research_method
  > At that time, the sock gen index was down 3.56%.
  indicator: SG CTA index in first 10% S&P drawdown · asset: multi · horizon: weeks · testable: yes - event study · confidence: high
  ^MT205-C06-2
- **Neils Castro Larsson** CTAs struggle most when the S&P drawdown is fast, e.g. Volmageddon Feb 2018 and July-Aug 2007.  #mech/slow_reaction
  > when it happens very quickly CTAs are struggling the most
  indicator: SG CTA in fast S&P drawdowns · asset: multi · horizon: weeks · conditions: fast equity crashes from highs · testable: yes - event study · confidence: high
  ^MT205-C06-3

### C07
- **Neils Castro Larsson** CTAs are second responders: they deliver crisis alpha after the first 10% fall, not at the start.  #mech/slow_reaction
  > people should not expect CTAs or trend followers to be the first responders
  indicator: trend following crisis payoff by drawdown stage · asset: multi · horizon: months · testable: yes - staged drawdown analysis · confidence: high
  ^MT205-C07-1
- **Neils Castro Larsson** From S&P -10% to -20% the SG CTA index returned +20.38% in 2022, about +8% in 2007-08, about +11% in 2000-01 but about -0.9% in the fast 2020 Covid move.  #mech/cycle_persistence
  > the performance of the sog CTA uh index during thatus 10 toous 20 uh% uh of the S&P was actually positive 20.38%.
  indicator: SG CTA index from S&P -10% to -20% · asset: multi · horizon: months · conditions: slower crises; fast crises flat · testable: yes - event study with 4 episodes · confidence: high
  ^MT205-C07-2
- **Neils Castro Larsson** Trend followers are fully long equities when a crisis starts from an all-time high, so initial losses are unavoidable; diversification across other sectors matters.  #mech/slow_reaction
  > because we know that the positioning of a trend follower when an equity crisis starts it often starts actually from an all-time high
  indicator: trend positioning at equity highs · asset: equities · horizon: weeks · testable: yes · confidence: high
  ^MT205-C07-3
- **Yo Kit** The CTA industry moved from faster trading in the early 2000s to 1-3 month trend speeds, so the SG CTA index reacts more slowly to rapid crashes and still held residual equity longs in 2025.  #mech/structural_shift
  > CTAs have migrated to the slightly slower speed month you know month to three month horizon trend following
  indicator: average CTA trend speed · asset: multi · horizon: months · testable: yes - lookback comparison · confidence: medium
  ^MT205-C07-4

### C08
- **Yo Kit** Trend followers have positive convexity over months but negative skew day-to-day in each asset class, so a day-one cross-asset shock cannot be adjusted away.  #mech/risk_management
  > although CTAs have positive convexity on a month two month three month horizon they have negative skew there
  indicator: trend return skew · asset: multi · horizon: days · conditions: day-one crisis · testable: yes - skew by horizon · confidence: medium
  ^MT205-C08-1
- **Yo Kit** In an across-the-board crisis (oil, equities, FX and bonds all moving) market count does not diversify; rigorous risk management on day one is the defence.  #mech/risk_management _(time-bound view)_
  > it's actually very difficult to create a diversified portfolio at that point regardless of you know how many how many uh sort of futures you trade
  asset: multi · horizon: days · conditions: cross-asset crises · testable: partly - few episodes · confidence: high
  ^MT205-C08-2
- **Yo Kit** Commodity trend markets are the most consistent performers in equity crises, so large commodity weight is valuable (gold, metals okay, energy strong in April).  #mech/risk_management
  > which sectors are actually more consistent in performing during equity crisis and it was very clear from that uh paper uh there was the commodities
  indicator: sector contribution in equity crises · asset: commodities · direction: long/short commodities · horizon: months · testable: yes - crisis sector attribution · confidence: medium
  ^MT205-C08-3
- **Neils Castro Larsson** The April 2025 tariff shock lies outside historical data, so it is a genuine out-of-sample stress test; Niels proposes testing whether CTAs trading 400-600 markets did better or worse than those with a more concentrated portfolio.  #mech/research_method _(added by sonnet-xhigh cross-check, time-bound view)_
  > this is truly a uh something we have not seen in our historical data and whatever back test you did you probably would never have seen uh anything like this uh showing up
  indicator: CTA performance by market count · asset: multi · horizon: weeks · conditions: tariff shock; across-the-board crisis · testable: yes - compare managers by number of markets traded in April 2025 · confidence: medium
  ^MT205-C08-X1

### C09
- **Yo Kit** Market count matters little; diversification for CTAs depends on correlation structure and overweighting less correlated assets (per the Quantica paper), not on the square root of markets.  #mech/risk_management
  > I don't think we're going to see a material difference between managers to trade 200 or 50 um futures
  indicator: correlation structure of traded markets · asset: multi · testable: yes - portfolio test · confidence: high
  ^MT205-C09-1
- **Yo Kit** A sudden rise in cross-market correlation in a crisis defeats presumed diversification and hurts CTAs.  #mech/risk_management
  > when you see a shift in correlation structure that's very painful actually
  indicator: cross-market correlation · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT205-C09-2
- **Yo Kit** Trading-cost improvements are worth about 5 bp of Sharpe per year, so reducing market impact (mixing signals, trading the second contract rather than the first) is useful but small.  #mech/risk_management
  > We're talking about five basis points of sharp per year, give or take.
  indicator: transaction cost savings · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT205-C09-3
- **Neils Castro Larsson** Reaction speed in a sharp reversal depends not only on lookback parameters but also on model type, for example continuous trend-sizing systems versus breakout-type systems.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > whether you are more a continuous system or whether you're more like a breakout type system
  indicator: continuous vs breakout trend models · asset: multi · horizon: weeks · conditions: sharp V-shaped reversal · testable: yes - compare model families in April 2025 · confidence: low
  ^MT205-C09-X1

### C10
- **Yo Kit** CTAs enter trends gradually but exit together, since exits are driven by both signal changes and vol-based risk cuts when everyone holds risk.  #mech/crowding_positioning
  > They say entry is ra rather smooth but exit we all tend to exit at the same time.
  indicator: CTA entry vs exit timing · asset: multi · horizon: days · conditions: late in trends · testable: partly - position data needed · confidence: medium
  ^MT205-C10-1
- **Yo Kit** A volatility spike makes all risk-managed CTAs cut positions together, adding correlation of trading beyond signals.  #mech/crowding_positioning
  > So if volatility spikes then what you expect? You expect all CTAs that risk manage.
  indicator: volatility spike · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT205-C10-2
- **Yo Kit** When a trend is extended, historical volatility underestimates next-day vol; the extra volatility measures CTA market impact, and trend level adds 5-10% accuracy to vol forecasts.  #mech/crowding_positioning
  > if trend is overextended this same measure will tend to underestimate volatility
  indicator: residual volatility versus trend extension · asset: multi · horizon: days · conditions: extended trend with everyone positioned · testable: yes - regression of realised vol on trend level · confidence: medium
  ^MT205-C10-3
- **Neils Castro Larsson** The extra volatility seen when a trend is extended cannot be attributed to CTAs alone: closet trend followers, macro traders and ordinary de-risking investors also exit at the same time, so it measures the combined impact of trend-following behaviour (Yo Kit accepts this).  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > we can't be sure that it's the CTAs necessarily, right?
  indicator: unexpected volatility when trend is extended · asset: multi · horizon: days · conditions: extended trends followed by a vol spike · testable: partly - identification of the CTA share is hard · confidence: medium
  ^MT205-C10-X1

### C11
- **Yo Kit** Performance of different trend predictors over time diverges widely (100% to 400% cumulative), so predictor mix matters, and tilting to the predictor suitable for a market could add return.  #mech/research_method
  > they're showing the performance dispersion between trend predictors and it's it's huge right it's uh it's somewhere between you know up 100% to up 400%
  indicator: trend predictors (breakout, moving average, speeds) · asset: multi · horizon: years · testable: yes - predictor comparison · confidence: medium
  ^MT205-C11-1
- **Yo Kit** Two sources of trend alpha: long-term secular trends (e.g. bonds) and short-term autocorrelation; predictor design should match what is harvested in each market, plus cost.  #mech/cycle_persistence
  > there are two sources of alpha in a in a market. The first one is sort of long-term trend.
  indicator: long-term trend and short-term autocorrelation · asset: multi · horizon: years · testable: yes - decompose by horizon · confidence: medium
  ^MT205-C11-2

### C12
- **Yo Kit** CTA diversification is the volatility reduction factor (diversification factor 3 turns average market Sharpe 0.25 into 0.75), not the number of markets.  #mech/risk_management
  > That bumps up your sharp by a factor of three.
  indicator: diversification factor / portfolio vol reduction · asset: multi · testable: yes - measurable in portfolio · confidence: high
  ^MT205-C12-1
- **Yo Kit** Diversification is dominated by the average market beta to the first principal factor, not by the square root of N: with 100 stocks at 30% beta, index risk is $30 versus under $10 idiosyncratic.  #mech/risk_management
  > the dominant factor is actually the average market data to the first component to the index.
  indicator: average beta to first principal component · asset: multi · testable: yes - PCA on CTA universe · confidence: high
  ^MT205-C12-2
- **Yo Kit** Capacity constraints can be extra alpha: smaller managers can trade low-correlation markets (commodities) at meaningful size, which large managers cannot.  #mech/risk_management
  > Um 100% 100%.
  asset: commodities · testable: partly - capacity estimates · confidence: high
  ^MT205-C12-3

### C13
- **Yo Kit** Allocating meaningfully to low-beta markets (metals, some energy) lowers the portfolio's beta to the first factor and improves quality of diversification.  #mech/risk_management
  > if we are able to allocate more meaningfully to markets which have low beta to the rest of the city universe
  indicator: market beta to CTA first factor · asset: commodities · testable: yes - risk budget test · confidence: high
  ^MT205-C13-1
- **Yo Kit** CFM finds SG CTA members' pairwise 6-month correlation about 50% (70% loading on the index); Goldman found about 60% among CTAs vs about 30% for macro managers.  #mech/crowding_positioning
  > 50 50% correlation pearlwise basically means that we all have 70% loading on the sockchain index
  indicator: pairwise correlation between CTAs, loading on SG CTA index · asset: multi · horizon: years · testable: yes - manager return data · confidence: medium
  ^MT205-C13-2

### C14
- **Yo Kit** Pairwise CTA correlation has stayed around 50% since 2011, so there is no extra dispersion in 2025 and the trend engine still works (momentum is a macro factor).  #mech/cycle_persistence _(time-bound view)_
  > 50% correlation uh pale-wise average correlation has rem remained remarkably stable
  indicator: pairwise CTA correlation since 2011 · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT205-C14-1
- **Yo Kit** Trading off capacity for off-the-beaten-path markets improves diversification and reduces correlation to the CTA index and peers.  #mech/risk_management
  > being a slightly offbeat is very helpful
  indicator: correlation to SG CTA index · asset: multi · testable: partly · confidence: medium
  ^MT205-C14-2
- **Yo Kit** Because CTAs are about 70% loaded on the SG CTA index and about 50% correlated to each other, investors who are used to diversifying across macro managers see CTAs as interchangeable, which hurts the case for allocating to several of them.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > Well, if I've talked to one, I've talked them all. They're all the same
  indicator: pairwise manager correlation · asset: multi · horizon: years · testable: partly - allocator behaviour not tested · confidence: medium
  ^MT205-C14-X1

### C15
- **Yo Kit** Trend following works because returns are autocorrelated (hundreds of years of data) and the payoff is like buying an option at realised rather than implied vol.  #mech/cycle_persistence
  > buy an option at at realized V rather than implied V
  indicator: return autocorrelation · asset: multi · horizon: years · testable: yes - long-history tests · confidence: high
  ^MT205-C15-1
- **Neils Castro Larsson** Investment bank notes forecasting CTA flows were wrong in April 2025 because CTAs actually sold on volatility.  #mech/crowding_positioning _(time-bound view)_
  > in the next two weeks, CTAs have to buy $100 billion worth of equities or they have to sell hundred billion worth of equities
  indicator: bank CTA flow estimates · asset: equities · horizon: weeks · testable: yes - compare estimates with outcome · confidence: medium
  ^MT205-C15-2
- **Neils Castro Larsson** Long-lookback CTA models were not yet short equities in April because price moves were not long enough in duration; prior signal strength was many standard deviations bullish going into February.  #mech/slow_reaction _(time-bound view)_
  > trend following is really about two things. It's about the price but it's also about the time
  indicator: trend signal strength, lookback length · asset: equities · horizon: months · conditions: after a long run to all-time highs · testable: yes - signal path replay · confidence: high
  **Correction (cross-check):** Mixed speakers: Niels explains that price moves have not lasted long enough for long-lookback models to go short; the point that signal strength was many standard deviations bullish going into February (after an all-time high) is Yo Kit's reply. → Niels: long-lookback models were not yet short equities in April because the price decline had not lasted long enough (trend following depends on time as well as price). Yo Kit: signals were many standard deviations bullish going into February after the all-time high, so most CTA money was still long equities.
  ^MT205-C15-3

### C16
- **Yo Kit** A 1-3 month trend signal can be played forward since half the window is known, allowing smoother, cheaper trading into the likely future position.  #mech/research_method
  > if I look at a signal which is a moving average 30 days okay then I know that in 15 days time the last 15 days will be in that sample
  indicator: moving average signal play-forward · asset: multi · horizon: weeks · testable: yes - cost reduction test · confidence: medium
  ^MT205-C16-1
- **Neils Castro Larsson** Playing forward positions can cause the model to predict; the host prefers acting on today's signal.  #mech/research_method
  > it's a dangerous game because it sounds like we're now starting to predict something which we shouldn't do
  asset: multi · testable: no - opinion · confidence: medium
  ^MT205-C16-2
- **Yo Kit** Macro and prop desks do simulate CTA models forward to see where buying and selling pressure will occur, i.e. front-running risk is real.  #mech/crowding_positioning
  > the prop traders were interested in the CTA model playing it forward
  asset: multi · testable: no - anecdote · confidence: high
  ^MT205-C16-3

### C17
- **Yo Kit** Do not trade a short-term signal spike that will revert before costs are recouped, especially in expensive markets; awareness of expected signal path improves cost control.  #mech/risk_management
  > this signal is not going to stay positive for long enough to me to recoup my trading costs
  indicator: expected signal path versus costs · asset: multi · horizon: days · testable: yes - cost-aware execution backtest · confidence: medium
  ^MT205-C17-1
- **Yo Kit** Trend predictors are mean-reverting (OU-like): the stronger the signal, the stronger the pullback to zero, so one must fight costs more at high signal strength; committing at signal 2 to 2.3 persists longer than at 3 to 3.1.  #mech/research_method
  > that pull back to the origin becomes stronger the higher the most the stronger your signal is
  indicator: signal strength with OU decay · asset: multi · horizon: weeks · conditions: moving average crossover signals; breakouts differ · testable: yes - signal decay estimation · confidence: medium
  ^MT205-C17-2
- **Yo Kit** The cost-aware 'pull back to zero' logic applies to moving-average type predictors, which need fresh price support to hold a strong signal; a breakout system simply puts on the position and stays in it, so it does not manage cost this way.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > if you do breakout you put on the position and you stay in it
  indicator: moving-average crossover vs breakout predictor · asset: multi · conditions: depends on predictor family · testable: yes - cost analysis by predictor type · confidence: medium
  ^MT205-C17-X1
- **Neils Castro Larsson** Niels warns that skipping a trade because a spiking short-term signal 'will come back' risks missing the trend that does not revert (a type I versus type II error); Yo Kit replies that it is a cost-versus-alpha balance based on mean reversion of the predictor, not a price forecast.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > yeah well good until the day it's not
  indicator: cost-gating of short-term trend signals · asset: multi · horizon: days · conditions: expensive markets and short-term signals · testable: yes - backtest cost-gated versus ungated signals · confidence: medium
  ^MT205-C17-X2

