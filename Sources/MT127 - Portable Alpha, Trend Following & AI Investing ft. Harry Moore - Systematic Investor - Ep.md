---
source_id: MT127
title: "Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep.412"
date: 2026-08-09
channel: "Top Traders Unplugged"
url: 
words: 13945
claims: 66
added_by_opus: 0
corrections: 0
crosscheck: "pending"
speakers: ["Harry Moore (Man Group, systematic/trend researcher)", "Niels Kaastrup-Larsen (host; caption 'Neils')"]
tags: [source, layer0]
---
# Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep.412

**Speakers:** Harry Moore (Man Group, systematic/trend researcher); Niels Kaastrup-Larsen (host; caption "Neils")

**Summary:** Top Traders Unplugged Systematic Investor Ep.412 (Aug 2026): Harry Moore (Man Group) and Niels discuss July/August 2026 trend-following dispersion (speed, market universe, yen intervention, AI-trade unwind), AI productivity in quant research, and two papers. Main points: trend is a cash-efficient, left-tail-uncorrelated alpha for portable alpha (needs about 40% cash, rebalancing/swap vs futures choices), and the Turtle rules map to volatility sizing, Kelly and drawdown-control mathematics.

**Approach:** trend following, portable alpha, risk management/position sizing, AI in quant research, diversification and tail correlation

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | nothing actionable: greetings, books and old phones small talk |
| C02 | 3 | Situational Awareness fund blow-up (theme concentration), BOJ/Fed yen intervention |
| C03 | 6 | Intervention vs rules-based trend, position sizing, 10-sigma move; trend barometer; July dispersion drivers |
| C04 | 4 | Themes (semis/software) dispersion, levered ETF decay, index performance data, CTA positioning, trend speed comparison starts |
| C05 | 4 | Speed results (20/60/130/260 day), slow outperformance, market-universe dispersion in energies |
| C06 | 3 | Fixed income dispersion, cross-sectional equity sector models, quality factor; AI trade bubble vs upside framing |
| C07 | 5 | AI bubble vs upside scenario, productivity gains, illusion of diversification in a 30-40% drawdown |
| C08 | 4 | Bonds also selling off, trend as left-tail diversifier, AI generation junior skills |
| C09 | 3 | AI changes quant researcher time split, hiring and testing |
| C10 | 2 | Humans reviewing code; cash efficiency of trend, freeing cash for cross-sectional/carry alphas |
| C11 | 3 | Cash-efficient access when private capital is illiquid; portable alpha construction; stacking returns |
| C12 | 1 | Portable alpha paper motivation, 2008 failure causes, cash buffer setup |
| C13 | 5 | Margin and cash buffers: 20% vs 40%, Monte Carlo, forced de-risking cost |
| C14 | 5 | Operational preference for no margin calls, liquid alpha, rebalancing replicates index issue |
| C15 | 3 | Rebalancing rule effects, swaps vs futures, caution on back-tested combinations; Turtle paper introduced |
| C16 | 3 | Turtle paper: range volatility estimate, Parkinson, volatility-based position sizing |
| C17 | 3 | Kelly criterion, Thorp, 2N stop equals 2% equity, correlation caps |
| C18 | 4 | Turtle drawdown rules and Grossman-Zhou, risk management is the edge |
| C19 | 3 | Leverage as tool, risk-balance of 50/50, choosing alpha uncorrelated in left tail |
| C20 | 2 | Check alpha vs worst 5% beta periods, trend negative correlation, volatility scaling lowers margin; outro |

## Claims

### C02
- **Harry Moore (Man Group, systematic/trend researcher)** A hedge fund that is dollar or market neutral on paper can still be concentrated in one theme (the other side of the AI trade), so a theme reversal caused a large loss; being right does not prevent trouble.  #mech/crowding_positioning _(time-bound view)_
  > even if on paper you look somewhat like dollar neutral or market neutral
  indicator: theme exposure (AI) · asset: equities · horizon: weeks · conditions: when a book is built around a single theme despite neutral beta · testable: partly: factor/theme concentration can be measured · confidence: high
  ^MT127-C02-1
- **Niels Kaastrup-Larsen (host; caption "Neils")** A 45 billion fund losing about two thirds in weeks shows that concentration and leverage on one idea are dangerous and diversification matters.  #mech/risk_management _(time-bound view)_
  > that diversification uh really does uh u matter
  asset: equities · horizon: weeks · testable: partly: concentration-loss anecdote · confidence: high
  ^MT127-C02-2
- **Niels Kaastrup-Larsen (host; caption "Neils")** Joint central-bank intervention in the yen hit trend followers who were short yen, though past interventions did not last long.  #mech/policy_reaction _(time-bound view)_
  > intervening uh in the Japanese yen only a couple of days before month end which you know it did have an effect
  indicator: USDJPY · asset: fx · direction: yen up, trend short-yen positions hurt · horizon: days · conditions: when intervention follows a long one-way yen move · testable: yes: intervention dates and trend returns are public · confidence: high
  ^MT127-C02-3

### C03
- **Niels Kaastrup-Larsen (host; caption "Neils")** Rules-based systems hold uncomfortable positions through intervention rumours while humans panic and exit.  #mech/behavioral
  > Humans start to panic. The rulesbased systems don't.
  asset: multi · horizon: days · testable: partly: systematic vs discretionary reaction can be compared · confidence: medium
  ^MT127-C03-1
- **Niels Kaastrup-Larsen (host; caption "Neils")** Position sizing must be set so that a single position (such as the yen) cannot hurt the portfolio too much when an intervention reverses it.  #mech/risk_management
  > it's the importance of stizing and and making sure that that one position um can't can't hit you too much
  indicator: position size limit · asset: multi · testable: yes: size caps vs loss can be tested · confidence: high
  ^MT127-C03-2
- **Niels Kaastrup-Larsen (host; caption "Neils")** The yen intervention produced a roughly 10 standard deviation move, rare and hard to simulate in market data, though such events exist.  #mech/risk_management _(time-bound view)_
  > I think it was like a 10 standard deviation move
  indicator: yen daily move · asset: fx · horizon: days · testable: partly: tail events are rare in samples · confidence: medium
  ^MT127-C03-3
- **Harry Moore (Man Group, systematic/trend researcher)** Authorities intervene when a move has run so far for so long that natural market forces are not reversing it.  #mech/policy_reaction
  > when you've when you've had a move go so far for for so long
  indicator: extended one-way FX moves · asset: fx · direction: reversal after extended move · horizon: months · conditions: after very long trends · testable: partly: intervention after extremes is testable · confidence: medium
  ^MT127-C03-4
- **Niels Kaastrup-Larsen (host; caption "Neils")** A trend barometer reading of 27 is a weak signal, implying a soft start to August for trend followers.  #mech/slow_reaction _(time-bound view)_
  > my trend barometer finished yesterday at 27. And that's a very low reading actually.
  indicator: trend barometer · asset: multi · horizon: weeks · testable: partly: barometer definition proprietary · confidence: medium
  ^MT127-C03-5
- **Harry Moore (Man Group, systematic/trend researcher)** July dispersion among trend managers came from asset-class risk weights, market inclusion choices and model speed, with long oil and long stocks positions diverging in outcome.  #mech/research_method _(time-bound view)_
  > choices of whether to exclude certain markets or whole asset classes would have created a lot a lot of dispersion in in July
  indicator: trend manager return dispersion · asset: multi · horizon: months · testable: yes: dispersion across indices is public · confidence: high
  ^MT127-C03-6

### C04
- **Harry Moore (Man Group, systematic/trend researcher)** Thematic trend positions (long tech hardware/semis, short software) were hurt in July, accounting for dispersion among managers.  #mech/crowding_positioning _(time-bound view)_
  > if you were trend following themes and you were you were long let's say u tech hardware companies you're long semiconductors and you were um uh short kind of software like that would have would have hurt
  indicator: semis vs software · asset: equities · horizon: months · testable: partly: theme baskets can be backtested · confidence: medium
  ^MT127-C04-1
- **Niels Kaastrup-Larsen (host; caption "Neils")** A 2x levered ETF lost over 40% while the underlying stock round-tripped to flat, showing volatility decay in levered retail products.  #mech/risk_management
  > the stock had gone up like 120% and then down to flat for over a 3 months period but the 2x levered uh ETF was down like 40 plus% for that period
  indicator: 2x levered single-stock ETF · asset: equities · horizon: months · conditions: in volatile round trips · testable: yes: path-dependence of levered ETFs is mathematically testable · confidence: high
  ^MT127-C04-2
- **Niels Kaastrup-Larsen (host; caption "Neils")** Early August 2026 trend index data: SG CTA index about -0.9% for the month, +7.15% YTD, BTOP50 +7.17% YTD, trend index +6.89%, short-term traders +3.3% YTD, MSCI World +12.5% YTD, S&P 500 +12.8% YTD.  #mech/slow_reaction _(time-bound view)_
  > The sock gen CG index is down 88 basis points up 7.15% so far this year.
  indicator: SG CTA, SG Trend, BTOP50, S&P 500 · asset: multi · horizon: months · testable: yes: public index data · confidence: high
  ^MT127-C04-3
- **Harry Moore (Man Group, systematic/trend researcher)** Estimated CTA positioning in Aug 2026: long equities, metals, energies and dollar; short fixed income.  #mech/crowding_positioning _(time-bound view)_
  > CTAs are still long equities probably long metals probably as you said long energies um probably long the dollar I would imagine and then still most likely short fixed income
  indicator: CTA positioning estimate · asset: multi · direction: long equities, metals, energies, dollar; short bonds · horizon: weeks · testable: partly: replication of positioning from trend signals possible · confidence: medium
  ^MT127-C04-4

### C05
- **Harry Moore (Man Group, systematic/trend researcher)** In 2026 YTD a standard trend model was negative at a 20-day lookback, less negative at 60, slightly positive at 130 and best at 260 days, so slower speeds did better.  #mech/slow_reaction _(time-bound view)_
  > if you had chosen a 20-day look back, again, this is just from this specific model, um, you would actually have been down uh, this year
  indicator: trend look-back (20/60/130/260 days) · asset: multi · direction: slower trend better · horizon: months · conditions: in a year without persistent turning points · testable: yes: speed-sorted trend returns can be computed · confidence: high
  ^MT127-C05-1
- **Niels Kaastrup-Larsen (host; caption "Neils")** Faster trend speeds win only after turning points that persist; absent those, slow models (short bonds, long energy, long stocks held throughout) outperform, echoing recent years.  #mech/slow_reaction _(time-bound view)_
  > we haven't had a a a turning point that that's that's persisted for long enough for for for the faster speeds to to kind of shine
  indicator: trend speed · asset: multi · direction: slow trend over fast trend · horizon: years · conditions: when reversals do not persist · testable: yes: speed vs regime test · confidence: high
  ^MT127-C05-2
- **Niels Kaastrup-Larsen (host; caption "Neils")** Blend some faster speeds with slow models to capture turning points.  #mech/slow_reaction
  > my my view is always to have some dynamism there that you can you can still capture some of those turning points
  indicator: trend speed mix · asset: multi · testable: yes: speed-blend backtest · confidence: medium
  ^MT127-C05-3
- **Harry Moore (Man Group, systematic/trend researcher)** Alternative markets (Nordic and Italian power) were more rangebound than crude and heating oil in 2026, so market universe drives trend performance dispersion.  #mech/structural_shift _(time-bound view)_
  > markets have have just tended to be a little bit more rangebound than we've seen in the more traditional energy markets this year
  indicator: market universe, power vs oil · asset: commodities · direction: trend profits in liquid oil · horizon: months · testable: yes: universe-sorted trend returns · confidence: high
  ^MT127-C05-4

### C06
- **Harry Moore (Man Group, systematic/trend researcher)** Fixed income has been difficult for trend for years because opposing forces (political pressure for rate cuts vs inflation and deficits) produce choppy reversals, more so in smaller markets such as Polish swaps.  #mech/cycle_persistence _(time-bound view)_
  > you've got the administrator administration shouting for uh rate cuts rate cuts you have markets follow that occasionally then you look at the inflation you look at rising deficits
  indicator: fixed income trend returns · asset: rates · horizon: years · conditions: when policy and fundamentals pull in opposite directions · testable: partly: trend returns in bonds are testable · confidence: medium
  ^MT127-C06-1
- **Harry Moore (Man Group, systematic/trend researcher)** Cross-sectional sector and factor trend models (semis vs software, value, momentum, quality) were profitable in 2026 but differently from index trend; quality struggled.  #mech/slow_reaction _(time-bound view)_
  > These cross-sectional models, I mean, from a from a high level have also been profitable just in a very very different way
  indicator: cross-sectional equity sector/factor trend · asset: equities · horizon: months · testable: yes: factor and sector series · confidence: medium
  ^MT127-C06-2
- **Harry Moore (Man Group, systematic/trend researcher)** AI is compared to railroads and dotcom cable building as a likely capex bubble.  #mech/overshoot
  > all of these comparisons back to the railroads back to laying cable in the.com bust
  indicator: AI capex · asset: equities · horizon: years · testable: partly: capex booms and subsequent returns can be studied · confidence: medium
  ^MT127-C06-3

### C07
- **Harry Moore (Man Group, systematic/trend researcher)** Bear case: AI shares the hallmarks of past bubbles (capex surge, mania) that end badly for markets even if useful infrastructure remains.  #mech/overshoot
  > It's got all the hallmarks of these prior periods where capex went through the roof.
  indicator: AI capex, equity valuations · asset: equities · horizon: years · testable: partly: analogy based · confidence: medium
  ^MT127-C07-1
- **Harry Moore (Man Group, systematic/trend researcher)** Stay balanced: the AI trade could also be right for 10 years, so one cannot predict and portfolios should be built for either outcome.  #mech/risk_management
  > Maybe there is this huge upside scenario where um the trade that we saw go wrong last month is the right trade and it works over over the next 10 years.
  asset: equities · horizon: years · testable: no: uncertainty argument · confidence: medium
  ^MT127-C07-2
- **Harry Moore (Man Group, systematic/trend researcher)** A portfolio of equities, bonds, commodities and private assets appears diversified in normal times but may all fall together in a 30-40% S&P crash.  #mech/risk_management
  > Now on paper, you look diversified, right? These assets they seem to have kind of in normal times somewhat low correlations with each other.
  indicator: cross-asset correlation in drawdown · asset: multi · horizon: months · conditions: in left-tail equity shocks · testable: yes: conditional correlations in drawdowns · confidence: high
  ^MT127-C07-3
- **Harry Moore (Man Group, systematic/trend researcher)** Private assets mark down slowly and return capital slowly, so they give only paper protection in a crash.  #mech/risk_management
  > they may mark down more slowly but at some point you're going to take hits there
  indicator: private asset marks · asset: other · horizon: years · testable: partly: smoothed returns understate drawdowns · confidence: medium
  ^MT127-C07-4
- **Harry Moore (Man Group, systematic/trend researcher)** Bonds and gold have sold off together, so they were not a reliable hedge for equity drawdowns in an inflationary environment.  #mech/cycle_persistence _(time-bound view)_
  > Then in bonds and gold like earlier in the year we saw again both of those sell off in a in a fairly correlated manner.
  indicator: bond and gold correlation · asset: multi · horizon: months · conditions: inflation above target for years · testable: yes: correlation series · confidence: high
  ^MT127-C07-5

### C08
- **Harry Moore (Man Group, systematic/trend researcher)** With inflation above target for many years, the Fed may not be able to cut rates to rescue markets, leaving bonds also vulnerable to a hard sell-off.  #mech/policy_reaction _(time-bound view)_
  > do they have the tools to really cut rates uh like we've seen in in the past to to kind of boy markets
  indicator: Fed funds, inflation · asset: rates · direction: bonds down alongside equities · horizon: years · conditions: when inflation stays above target · testable: partly: Fed reaction function · confidence: medium
  ^MT127-C08-1
- **Harry Moore (Man Group, systematic/trend researcher)** Trend follows prices across assets, going short bonds and equities or long commodities as narratives change, with no long-term view.  #mech/slow_reaction
  > trend doesn't have a long-term view on any of these markets right it trades them all
  indicator: trend following · asset: multi · direction: short bonds and equities in inflation shock; long commodities · horizon: months · testable: yes · confidence: high
  ^MT127-C08-2
- **Harry Moore (Man Group, systematic/trend researcher)** Trend following can short equities and even the AI theme (semis and hardware) in a break, offering something different from other holdings.  #mech/slow_reaction
  > It might even go short the AI theme
  indicator: trend short positions · asset: equities · direction: short equities/semis · horizon: months · conditions: in a left-tail break · testable: yes · confidence: medium
  ^MT127-C08-3
- **Harry Moore (Man Group, systematic/trend researcher)** In a left-tail shock, trend following is zero or negatively correlated to equities while other asset class correlations rise, making it a covariance-matrix diversifier.  #mech/risk_management
  > typically it's it's trend following that is that is zero or or kind of negatively correlated and other asset classes uh of correlations typically typically pick up
  indicator: trend vs equity correlation in stress · asset: multi · direction: long trend in portfolio for tail protection · horizon: months · conditions: in the left tail · testable: yes: conditional correlation tests · confidence: high
  ^MT127-C08-4

### C09
- **Harry Moore (Man Group, systematic/trend researcher)** AI summarises existing knowledge but cannot easily produce new alpha ideas, so it frees researchers to be creative rather than write Python.  #mech/research_method
  > very very difficult to come up with brand new kind of quantitative high alpha ideas
  asset: other · testable: partly: productivity claim · confidence: medium
  ^MT127-C09-1
- **Harry Moore (Man Group, systematic/trend researcher)** AI shifts quant research time from implementation (Python, backtest setup) toward ideas, from about 50/50 to 90/10, squeezing junior implementation roles.  #mech/research_method
  > if you could split that 50/50 and make it more like 9010 so that your top researchers have plenty more time to think and be creative
  asset: other · testable: partly: productivity measurable · confidence: medium
  ^MT127-C09-2
- **Harry Moore (Man Group, systematic/trend researcher)** Test researchers by having them critique an AI-generated piece, since AI use is unavoidable; the risk is skill atrophy from one-click answers.  #mech/research_method
  > give someone an AI generated piece, get them to get them to go and critically analyze it
  asset: other · testable: no: hiring practice · confidence: medium
  ^MT127-C09-3

### C10
- **Harry Moore (Man Group, systematic/trend researcher)** Trend on futures needs only about $20-25 of capital per $100 exposure, so allocators can add trend without selling existing holdings.  #mech/structural_shift
  > if I only need to use $20 or $25 to get my $100 of trend following gives me a few new levers
  indicator: futures margin/cash efficiency · asset: multi · testable: yes: margin-to-notional · confidence: high
  ^MT127-C10-1
- **Harry Moore (Man Group, systematic/trend researcher)** Freed cash can fund extra alphas such as cross-sectional trend or carry, which have lower correlation, positive Sharpe and add value.  #mech/risk_premium
  > It had lower correlation. It still had positive sharp. It was still additive
  indicator: cross-sectional trend, carry · asset: multi · testable: yes: add-on alpha backtests · confidence: medium
  ^MT127-C10-2

### C11
- **Harry Moore (Man Group, systematic/trend researcher)** Cash-efficient trend allows an allocation even when private assets are not returning capital quickly.  #mech/liquidity_flows
  > Imagine again, you're not getting your cash flows back as as fast as you want from from your private allocations.
  indicator: private asset distributions · asset: multi · horizon: years · testable: no: situational · confidence: medium
  ^MT127-C11-1
- **Niels Kaastrup-Larsen (host; caption "Neils")** Combining trend and equities in portable alpha yields roughly the sum of both return streams rather than the average.  #mech/risk_premium
  > actually you get almost the sum of the two return stream
  indicator: S&P 500 plus SG Trend stack · asset: multi · horizon: years · testable: yes: stacked return series · confidence: high
  ^MT127-C11-2
- **Harry Moore (Man Group, systematic/trend researcher)** Second-order portable-alpha design questions (rebalancing rule, cash buffer) are under-researched, motivating the paper.  #mech/research_method
  > how should I rebalance portable alpha or how much cash should I hold in a portable alpha structure like you don't find great answers
  asset: multi · testable: partly · confidence: high
  ^MT127-C11-3

### C12
- **Harry Moore (Man Group, systematic/trend researcher)** Portable alpha structures failed in 2008 due to insufficient liquidity and alpha-beta correlation; resilient designs must survive the GFC, the dotcom bust and COVID.  #mech/risk_management
  > in 2008 many of these structures failed right and the lines down which those structures failed those risks still exist
  indicator: alpha-beta correlation, liquidity · asset: multi · horizon: years · conditions: in stress events · testable: yes: stress-period simulation · confidence: high
  ^MT127-C12-1

### C13
- **Harry Moore (Man Group, systematic/trend researcher)** A futures- or swap-based beta needs unencumbered cash beyond margin, because a 10% fall exhausts 10% margin and counterparties call for more.  #mech/risk_management
  > if you've only supported your S&P with $10 of capital and the S&P falls by 10%. All of your margin is gone, right?
  indicator: margin and cash buffer · asset: equities · horizon: days · conditions: in sharp equity declines · testable: yes: margin simulation · confidence: high
  ^MT127-C13-1
- **Harry Moore (Man Group, systematic/trend researcher)** A 20% unencumbered cash buffer on S&P plus trend would have been fully drawn down in the GFC, dotcom and COVID, forcing beta sales.  #mech/risk_management
  > you get fully drawn down um in the GFC in the dotcom and in co
  indicator: S&P 500 plus SG Trend backtest 26-27 years · asset: equities · horizon: years · conditions: in major crashes · testable: yes: backtest · confidence: high
  ^MT127-C13-2
- **Harry Moore (Man Group, systematic/trend researcher)** Forced beta selling at the lows loses the rebound (about 30% in 2009) and produces large tracking error against the benchmark.  #mech/risk_management
  > if you were were selling in the early part of 2009 at a at a low in your equity component and you're knocked out that position, you miss kind of 29 30% of of upside.
  indicator: tracking error vs S&P · asset: equities · horizon: months · conditions: after forced deleveraging near lows · testable: yes · confidence: high
  ^MT127-C13-3
- **Harry Moore (Man Group, systematic/trend researcher)** About 40% cash (10% margin plus 30% unencumbered) means a forced degearing only once in 100-200 years, per Monte Carlo and real data.  #mech/risk_management
  > about once in every 1 to 200 years
  indicator: cash buffer 40% · asset: equities · horizon: years · testable: yes: Monte Carlo simulation · confidence: medium
  ^MT127-C13-4
- **Harry Moore (Man Group, systematic/trend researcher)** Only one historical path exists, so Monte Carlo is used to simulate severe drawdowns beyond the history.  #mech/research_method
  > you've only had one one path of of the truth that actually happened
  asset: multi · testable: yes · confidence: high
  ^MT127-C13-5

### C14
- **Harry Moore (Man Group, systematic/trend researcher)** Most investors want the manager to bear operational and cash-flow complexity, so a larger buffer is preferred over callable capital.  #mech/risk_management
  > They do not want to be getting margin calls um on a Monday.
  asset: multi · testable: no: client preference · confidence: medium
  ^MT127-C14-1
- **Harry Moore (Man Group, systematic/trend researcher)** Liquid alphas such as trend allow quick recapitalisation, making them good candidates for portable alpha.  #mech/liquidity_flows
  > If you if you have something that's like weekly dealing or monthly dealing, you can recapitalize quickly.
  asset: multi · testable: partly · confidence: medium
  ^MT127-C14-2
- **Harry Moore (Man Group, systematic/trend researcher)** Rebalancing the beta component periodically causes tracking error versus the index; to track closely, buy and hold or use tolerance bands.  #mech/research_method
  > as soon as you select a monthly rebalance, you no longer replicate the S&P.
  indicator: rebalance frequency · asset: equities · horizon: years · testable: yes: simulate rebalancing rules · confidence: high
  ^MT127-C14-3
- **Harry Moore (Man Group, systematic/trend researcher)** Recommended compromise: rebalance only when the S&P and trend sleeves drift more than about 10% out of balance.  #mech/risk_management
  > if my S&P and SG trend goes more than 10% out of whack, I will rebalance.
  indicator: tolerance band · asset: multi · testable: yes · confidence: medium
  ^MT127-C14-4
- **Harry Moore (Man Group, systematic/trend researcher)** In 2008 rebalancing back to target lost money because equities kept falling while trend rose; only buy and hold did better.  #mech/behavioral
  > Every time you rebalance you reby you increase your equity allocation into a continually falling equity market.
  indicator: rebalancing in 2008 · asset: equities · horizon: months · conditions: in persistent crashes · testable: yes · confidence: high
  ^MT127-C14-5

### C15
- **Harry Moore (Man Group, systematic/trend researcher)** Over the long run rebalancing frequency (monthly, quarterly, annual, 5-10% bands) makes little performance difference, but it matters in episodes such as 2008 and COVID.  #mech/research_method
  > over the long run, we found that in performance terms it kind of doesn't matter.
  indicator: rebalancing rule · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT127-C15-1
- **Harry Moore (Man Group, systematic/trend researcher)** Swap financing cost (about 40bp) is implicit in futures, so swaps vs futures give no structural performance advantage; the choice is operational, with futures lacking counterparty risk.  #mech/risk_premium
  > if you run this over time, it washes out, right? The you don't get a a a structural performance advantage
  indicator: futures vs swap cost · asset: multi · horizon: years · testable: yes: cost comparison · confidence: high
  ^MT127-C15-2
- **Niels Kaastrup-Larsen (host; caption "Neils")** Other popular stacked combinations may look great in backtests but hide risks not exposed in recent decades, partly through correlations.  #mech/research_method
  > we have seen uh some other combinations that may look great in a back test
  asset: multi · testable: partly · confidence: medium
  ^MT127-C15-3

### C16
- **Harry Moore (Man Group, systematic/trend researcher)** The Turtle rules were hand-calculable approximations of later decision and probability theory.  #mech/research_method
  > rules of thumb hand calculable pen and paper easy to do in a in a few minutes uh approximations of later decision theory mathematics
  indicator: Turtle trading rules · asset: multi · testable: yes · confidence: high
  ^MT127-C16-1
- **Harry Moore (Man Group, systematic/trend researcher)** The Turtles estimated volatility N with a range-based exponential estimator (half-life about 14 days), consistent with Parkinson's efficient range estimator.  #mech/risk_management
  > they use a rangebased estimate estimator very simple to update each day
  indicator: range-based volatility, Parkinson · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT127-C16-2
- **Harry Moore (Man Group, systematic/trend researcher)** Turtle units equalise risk across markets (one unit of crude equals one unit of Treasuries in risk), i.e. volatility-based position sizing.  #mech/risk_management
  > really what this is is this is volatility based um position sizing, right?
  indicator: N-based unit · asset: multi · testable: yes · confidence: high
  ^MT127-C16-3

### C17
- **Harry Moore (Man Group, systematic/trend researcher)** The Turtles' 2% equity per 2N stop corresponds to a fractional-Kelly size on the left of the optimum, giving up some growth for much lower ruin risk.  #mech/risk_management
  > Now any prudent manager will be on the left side of that hill, right? You are taking a little bit of less of the the upside for a much lower probability of of ruin.
  indicator: Kelly fraction, 2N stop · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT127-C17-1
- **Harry Moore (Man Group, systematic/trend researcher)** A stop at 2N equals a loss of 2% of equity per position.  #mech/risk_management
  > this equate this 2n equates to 2% of your total equity in your book
  indicator: 2N stop · asset: multi · testable: yes · confidence: high
  ^MT127-C17-2
- **Harry Moore (Man Group, systematic/trend researcher)** Turtles managed correlation with position-size caps on correlated markets instead of covariance inversion.  #mech/risk_management
  > the way they dealt with correlations was not in the actual construction but it was on position size caps.
  indicator: correlation caps · asset: multi · testable: yes · confidence: high
  ^MT127-C17-3

### C18
- **Harry Moore (Man Group, systematic/trend researcher)** Because managers run others' money, drawdown-control rules are needed; the Turtles cut equity 20% after a 10% loss, later formalised by Grossman and Zhou.  #mech/risk_management
  > like you cannot stomach an 80% draw down
  indicator: drawdown control rule · asset: multi · testable: yes: simulate drawdown rules · confidence: high
  ^MT127-C18-1
- **Harry Moore (Man Group, systematic/trend researcher)** Turtle drawdown rule: after losing 10% reduce book equity used for sizing by 20%.  #mech/risk_management
  > they lost 10% um in the market then they would cut their equity by 20%
  indicator: drawdown rule · asset: multi · testable: yes · confidence: medium
  ^MT127-C18-2
- **Niels Kaastrup-Larsen (host; caption "Neils")** The Turtles' edge was risk management and scaling rather than the breakout entry.  #mech/risk_management
  > the genius was not so much in buying a 100 day breakout
  asset: multi · testable: partly · confidence: high
  ^MT127-C18-3
- **Niels Kaastrup-Larsen (host; caption "Neils")** Trend followers control risk, not returns: small losses, intelligent scaling and surviving to catch outsized moves.  #mech/risk_management
  > we are probably risk managers first and foremost
  asset: multi · testable: partly · confidence: high
  ^MT127-C18-4

### C19
- **Harry Moore (Man Group, systematic/trend researcher)** A 50/50 portfolio holds roughly 85% of its risk in equities, so leverage on bonds improves risk balance and Sharpe versus a $100 capital constraint.  #mech/risk_management
  > 85% of the risk is equities, 15% is bonds, even though on paper it says 50/50
  indicator: risk contribution · asset: multi · testable: yes · confidence: high
  ^MT127-C19-1
- **Harry Moore (Man Group, systematic/trend researcher)** Leverage is a portfolio-construction tool that can raise Sharpe when assets are risk-balanced.  #mech/risk_management
  > you get a higher sharp um than you would by by by having the $100 constraint
  indicator: leverage · asset: multi · testable: yes · confidence: high
  ^MT127-C19-2
- **Harry Moore (Man Group, systematic/trend researcher)** Choose a portable alpha that is uncorrelated in the left tail; liquidity-provision strategies (short vol, merger arbitrage, basis trade) look good normally but have big left tails.  #mech/risk_management
  > What you also need to really investigate is not just that it's uncorrelated, but that it's uncorrelated in the left tail.
  indicator: alpha left-tail correlation · asset: multi · conditions: avoid liquidity-provision alphas · testable: yes · confidence: high
  ^MT127-C19-3

### C20
- **Harry Moore (Man Group, systematic/trend researcher)** Test alpha vs the worst 5% of beta returns; trend historically has low to negative correlation to equities in the worst periods.  #mech/research_method
  > like the worst 5% of beta returns, like the worst equity periods, and check that you still have no correlation
  indicator: trend vs equity correlation in worst 5% · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT127-C20-1
- **Harry Moore (Man Group, systematic/trend researcher)** Trend scales positions inversely with volatility, so it needs less margin in turning-point stress, unlike liquidity-provision strategies.  #mech/risk_management
  > Trend is actually reducing positions. It needs less margin to ride.
  indicator: volatility-scaled positions · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT127-C20-2

