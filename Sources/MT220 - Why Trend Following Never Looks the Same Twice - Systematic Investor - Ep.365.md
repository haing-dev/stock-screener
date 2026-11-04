---
source_id: MT220
title: "Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365"
date: 2025-09-18
channel: "Top Traders Unplugged"
url: 
words: 9994
claims: 39
added_by_crosscheck: 11
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Niels Kaastrup-Larsen (host)", "Katy Kaminski (systematic researcher, AlphaSimplex)"]
tags: [source, layer0]
---
# Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365

**Speakers:** Niels Kaastrup-Larsen (host); Katy Kaminski (systematic researcher, AlphaSimplex)

**Summary:** Top Traders Unplugged ep. 365 (Sept 2025): Man AHL and Quantica papers on trend manager return dispersion (speed, allocation, alternative markets, carry), Kaminski's style factors and Mahalanobis turbulence, and why 2-3 different CTAs plus diversification beats chasing factors.

**Approach:** trend following, return dispersion, alternative markets, manager selection

**Cross-check completeness estimate of first read:** 0.80 - the first reader caught the four dispersion drivers, Man and Quantica findings, turbulence metric and the two-or-three-managers advice, but missed the performance table, fixed-income signal state, the Man hypothetical-manager method, random-signal studies, chance tracking gaps, and several Quantica points (per-market Sharpe, range-bound alt markets, two-edged crowding).

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | Intro; Fed bond trend signals; European political chaos |
| C02 | 1 | AirPods banter; hedge fund brand awareness ranking; September CTA update |
| C03 | 2 | Fixed income signals, SOFR vs Fed funds, cuts priced |
| C04 | 2 | Index performance numbers; Man AHL dynamics of dispersion intro |
| C05 | 3 | Four dispersion dimensions; speed and crisis; index constituents |
| C06 | 3 | Index investability, style drift, volatility and correlation math; alt markets |
| C07 | 2 | Sharpe of index replication; Chapter 11 of Trend Following book |
| C08 | 2 | Equal risk, 2008/2022 dispersion; adding managers |
| C09 | 2 | Main driver of dispersion; CTA style factors |
| C10 | 1 | Style factors; Mahalanobis turbulence |
| C11 | 2 | Magnitude vs correlation surprises; keep it simple |
| C12 | 2 | Quantica paper on alternative markets |
| C13 | 2 | Gas and power; Sharpe diversification argument |
| C14 | 2 | Crowding in alt markets; next research |
| C15 | 0 | Outro - nothing actionable |

## Claims

### C01
- **Katy Kaminski** US fixed income trend signals had barely moved despite many themes (Fed independence, inflation), so a breakout in bonds could be the next catalyst for trend followers.  #mech/slow_reaction _(time-bound view)_
  > if you look at the trend signals, they haven't moved much. So, I'm kind of thinking that could be a potential catalyst.
  indicator: US fixed income trend signals · asset: rates · horizon: weeks · testable: partly · confidence: low
  ^MT220-C01-1
- **Niels Kaastrup-Larsen** Bond yields react strongly to political and budget uncertainty, as with UK and French political chaos.  #mech/fiscal_debt _(time-bound view)_
  > bond yields are very good at reacting to it's uncertainty especially about budgets
  indicator: UK and French bond yields · asset: rates · horizon: months · testable: yes · confidence: medium
  ^MT220-C01-2

### C02
- **Niels Kaastrup-Larsen** In September 2025 equities, metals, sugar and oil products supported CTAs; livestock paused; managers disagreed on fixed income direction.  #mech/cycle_persistence _(time-bound view)_
  > Of course, equities, metals continue to do the heavy lifting, I
  indicator: CTA sector contributors · asset: multi · horizon: weeks · testable: no - descriptive · confidence: medium
  ^MT220-C02-1

### C03
- **Katy Kaminski** With SOFR near 3.4% and fed funds at 4.25-4.5%, rate cuts were priced in, so a trend in bonds needs a surprise relative to pricing (50bp cut or no cut), and the lack of trend reflects anticipation of the Fed.  #mech/policy_reaction _(time-bound view)_
  > the market has already decided that we're getting cuts. The biggest shocks are going to be if we get a lot more cuts or if we don't get enough.
  indicator: SOFR vs fed funds, priced cuts · asset: rates · horizon: weeks · testable: partly · confidence: medium
  **Correction (cross-check):** The surprise scenarios are wrong. Katy says the biggest shocks would be a lot more cuts than expected or not enough cuts, that a 50bp cut is what was expected or wanted (so not a surprise), and that getting no cut 'could be huge'. → With SOFR near 3.4% against fed funds at 4.25-4.5%, rate cuts were priced in, so bond trends need a surprise relative to pricing: a no-cut outcome (or far more cuts than expected) would be the shock, while a 50bp cut is what the market expected; the lack of a trend so far reflects anticipation of the Fed and the jobs data.
  ^MT220-C03-1
- **Niels Kaastrup-Larsen** Long yields can rise after rate cuts if investors consider cuts insufficient or fear inflation, since futures price future rates, not today's.  #mech/policy_reaction _(time-bound view)_
  > let's not forget what happened last time they caught actually bond yields went up.
  indicator: long yields after Fed cuts · asset: rates · horizon: weeks · testable: yes - event study · confidence: medium
  ^MT220-C03-2
- **Katy Kaminski** In September 2025 fixed income trend signals were mixed and weak, flipping between long and short: slightly more long signals in the US, short in the UK and some European bonds, which is why managers disagreed on bond direction.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > the signals have been very mixed and kind of weak and teetering around between should we be short, should we be long
  indicator: bond trend signals (US, UK, Europe) · asset: rates · direction: no consistent bond trend · horizon: weeks · conditions: September 2025 · testable: yes - signal data · confidence: medium
  ^MT220-C03-X1

### C04
- **Niels Kaastrup-Larsen** In 2025 short-term trend models struggled most on a vol-adjusted basis; Trend Barometer was weak because it uses shorter lookbacks.  #mech/slow_reaction _(time-bound view)_
  > we know that short-term models this year are probably the ones on a vol adjusted basis that are struggling the most.
  indicator: short-term trend model performance · asset: multi · horizon: months · conditions: 2025 regime · testable: yes · confidence: medium
  ^MT220-C04-1
- **Niels Kaastrup-Larsen** Return dispersion among trend managers is explained by design choices (speed, allocation, alternative markets, carry), so dispersion is the fingerprint of each system (Man AHL 'Dynamics of dispersion').  #mech/research_method
  > how fast you chase trends, which market you include, whether you tilt towards bonds or FX, or whether you sneak in a little bit of carry
  indicator: speed, allocation, alternative markets, carry · asset: multi · horizon: years · testable: yes - Man AHL paper · confidence: high
  ^MT220-C04-2
- **Niels Kaastrup-Larsen** Performance data to 8 Sep 2025: BTOP50 +91bp in September (-1.93% YTD), SG CTA about +1% (about -5.1% YTD), SG Trend +1.25% (-6.5% YTD), short-term traders +66bp (nearly -6% YTD), against MSCI World +90bp (+15.1% YTD), US Aggregate bonds +96bp (almost +6% YTD) and S&P 500 total return +86bp (+11.74% YTD), so in 2025 CTAs lagged both stocks and bonds.  #mech/new _(added by sonnet-xhigh cross-check, time-bound view)_
  > beta 50 is up 91 basis points but down only now 1.93% for the year
  indicator: BTOP50; SG CTA; SG Trend; SG Short-Term Traders; MSCI World; US Aggregate; S&P 500 TR · asset: multi · horizon: months · conditions: to 8 September 2025 · testable: yes - index data · confidence: high
  ^MT220-C04-X1

### C05
- **Katy Kaminski** Carry has about 30-40% correlation with trend, so adding carry smooths performance over different horizons.  #mech/risk_premium
  > Carrie as you know has about a 30 40% correlation with trend.
  indicator: carry vs trend correlation · asset: multi · direction: add carry to trend · horizon: years · testable: yes · confidence: medium
  ^MT220-C05-1
- **Katy Kaminski** Faster trend following helps most in crises; the industry has shifted to slower products that give less crisis protection, though slow ones did better recently.  #mech/slow_reaction
  > being faster is actually really helpful for really bad environments.
  indicator: trend speed and crisis performance · asset: multi · direction: favor faster trend for crisis alpha · horizon: months · conditions: crisis environments · testable: yes - Man AHL paper · confidence: high
  ^MT220-C05-2
- **Niels Kaastrup-Larsen** Index dispersion arises from specific constituents (one outlier in 2009; two discretionary managers in 2014 later removed), so understand makeup before concluding about manager risk or replication.  #mech/research_method
  > in 2009 just one constituent stood out with a doubledigit positive territory and the rest was kind of more flat to negative
  indicator: SG CTA constituents · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT220-C05-3
- **Katy Kaminski** Allocation choices create visible manager dispersion: in 2025 CTA ETFs that did not trade equities did relatively well, an example of asset-class tilt driving relative performance in a given year.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > CTA in the ETF space this year has you know does not use equities and that's been positive for them
  indicator: CTA ETF performance vs equity exposure · asset: multi · direction: avoiding equities helped in 2025 · horizon: months · conditions: 2025 only · testable: yes - fund returns · confidence: medium
  ^MT220-C05-X1

### C06
- **Katy Kaminski** CTA indices are not investable and manager style drifts over time, so study aspects (speed, markets) of managers rather than rely on index behavior.  #mech/research_method
  > you don't buy 2007's CTA, you buy 2025 CTA.
  indicator: CTA style drift · asset: multi · horizon: years · testable: yes - style evolution paper · confidence: high
  ^MT220-C06-1
- **Katy Kaminski** Dispersion between managers follows mathematically from differences in volatility and correlation among their returns, so theoretical dispersion can be estimated.  #mech/research_method
  > each of these managers as a random variable. They each have a volatility and mathematically you can think about what the range of differences is going to be.
  indicator: volatility and correlation of managers · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT220-C06-2
- **Katy Kaminski** Man AHL found outperformance and correlation benefits from alternative markets, though depending on the horizon.  #mech/structural_shift
  > they also demonstrate some outperformance of alternative markets.
  indicator: alternative markets · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT220-C06-3
- **Katy Kaminski** The Man AHL method builds many hypothetical trend managers with different designs and aggregates them over time, which allows studying design differences across environments without cherry-picking the best backtest version.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > create a bunch of different trend managers as hypotheticals and aggregate them over time and examine sort of behavioral differences in different environments
  indicator: hypothetical trend managers across speed, allocation, markets and carry · asset: multi · horizon: years · testable: yes - reproducible design · confidence: medium
  ^MT220-C06-X1

### C07
- **Katy Kaminski** Replicated indices give different Sharpe (about 0.75 backtest vs 0.36 actual) because longer lookbacks did better historically and managers differ, so focus on relative and conditional differences.  #mech/research_method
  > I'm not surprised that sharp ratios are different because it's a back test, right?
  indicator: replicated vs actual SG Trend index Sharpe · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT220-C07-1
- **Katy Kaminski** In Kaminski and Greyserman's book chapter 11, equal-risk allocation historically outperformed market-capitalization-weighted allocation, with dispersion driven by equity bias, carry, allocation and speed.  #mech/risk_premium
  > how equal risk outperformed historically in our analysis.
  indicator: equal risk vs liquidity-weighted allocation · asset: multi · direction: equal-risk weighting · horizon: years · testable: yes · confidence: medium
  ^MT220-C07-2

### C08
- **Katy Kaminski** Return dispersion between trend managers is greater in high-volatility years (2008, 2022) simply because moves are bigger.  #mech/risk_management
  > we did find that 2008 given the size of the moves regardless of you know which type of methodologies you use you had a bigger range
  indicator: market volatility vs dispersion · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT220-C08-1
- **Katy Kaminski** Combining two or three managers removes much of the return dispersion versus the index, but residual 3-4% (replication 500-600bp slippage) always remains.  #mech/risk_management
  > you adding at least two maybe three together gets you pretty far in terms of adjusting some of that return dispersion
  indicator: number of managers vs dispersion · asset: multi · direction: hold two to three different CTAs · horizon: years · testable: yes - random sampling · confidence: medium
  ^MT220-C08-2
- **Katy Kaminski** Random-signal experiments (alongside channel breakout versus moving average signals) separate how much return dispersion comes from asset allocation and position sizing versus from the entry signals themselves.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > we even had these sort of random signal studies too just to understand sort of how much of that is driven by the sort of allocation and how much of it is driven by signals themselves
  indicator: random signals vs breakout and moving-average signals · asset: multi · horizon: years · conditions: the chapter targeted dispersion, not performance · testable: yes - simulation design · confidence: medium
  ^MT220-C08-X1

### C09
- **Katy Kaminski** No single design factor (speed, allocation, alternative markets, carry) is the main driver; each dominates in different years, e.g. fixed income only in 2019.  #mech/cycle_persistence
  > I think any of these particular ones will kind of stick out in a given year depending on what's happening.
  indicator: drivers of manager dispersion · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT220-C09-1
- **Katy Kaminski** Create style factors for trend (speed, market size, correlated markets) to regress manager returns and explain relative performance as with equity style factors.  #mech/research_method
  > we realized like we're very irritated that there's no benchmark. So we started sort of explaining how you could design a benchmark and then we created style factors similar to equities.
  indicator: CTA style factors · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT220-C09-2
- **Katy Kaminski** An investor holding two or three CTAs who trails the index by 400-500bp should not treat it as a sign of poor selection: gaps of that size arise by chance between return streams with these correlations.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > happen by chance with two random variables that have those correlations.
  indicator: tracking gap vs CTA index · asset: multi · horizon: years · conditions: portfolio of 2-3 managers vs an index · testable: yes - dispersion simulation · confidence: medium
  ^MT220-C09-X1

### C10
- **Katy Kaminski** A Mahalanobis-distance turbulence metric gives a point-in-time measure of movement across managers, decomposable into magnitude surprise and correlation surprise, without needing a window of data.  #mech/research_method
  > you use the Malhanobis distance to talk about how much movement there is.
  indicator: Mahalanobis turbulence of CTA returns · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT220-C10-1

### C11
- **Katy Kaminski** Magnitude surprises (Brexit, SVB, Black Friday, Liberation Day) hurt CTAs, while correlation surprises mark inflection points where trend signals rotate and drive dispersion.  #mech/behavioral
  > CTAs do not do as well on magnitude surprise days, right?
  indicator: magnitude vs correlation surprise · asset: multi · horizon: days · testable: yes · confidence: medium
  **Correction (cross-check):** Liberation Day is listed among the observed magnitude surprises, but Katy says it is not in the data set and that she is 'pretty sure' it would be a magnitude surprise. → In the turbulence paper the large pure magnitude surprises include Brexit, SVB and Black Friday (Liberation Day is outside the sample and only presumed to be one); CTAs do worse on magnitude-surprise days, while correlation surprises mark inflection points where trend signals rotate and drive dispersion.
  ^MT220-C11-1
- **Katy Kaminski** Investors should start simple: pick two or three different CTAs, avoid analysis paralysis, because CTAs are among few alternatives without hidden equity beta and no style factor persists.  #mech/risk_management
  > pick two or three, at least two or three managers that you like, that you think are a little different
  asset: multi · direction: hold two to three different CTAs · horizon: years · testable: partly · confidence: high
  ^MT220-C11-2
- **Katy Kaminski** Combine a faster manager (for crisis alpha) with a slower manager or a replication product, since each style does better in different environments and no style factor persists.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > maybe you can have some of that and you can have a manager that's going to be faster because you think, I like the crisis alpha and that one's slow
  indicator: manager speed · asset: multi · direction: hold both fast and slow trend · horizon: years · testable: yes - blend backtest · confidence: medium
  ^MT220-C11-X1

### C12
- **Katy Kaminski** Quantica compared 50 traditional with 120 alternative markets (credit, gas and power, livestock); sector composition explains recent differences, and alternative markets had extreme outperformance in specific sectors during 2020-22 rather than structurally trending better.  #mech/structural_shift
  > things like credit, gas and power, um more
  indicator: alternative vs traditional market trend portfolios · asset: multi · horizon: years · testable: yes - Quantica Q3 2025 · confidence: high
  ^MT220-C12-1
- **Katy Kaminski** A trend follower should include all assets because an asset that never trended (metals, palladium, copper) can start trending.  #mech/research_method
  > every asset is an opportunity for trend. I just don't know which one is going to work, right?
  indicator: market universe breadth · asset: multi · horizon: years · testable: partly · confidence: high
  ^MT220-C12-2
- **Katy Kaminski** Extreme outperformance of alternative markets in 2020-22 raised investors' expectations, so three years of weaker results led to doubts about the thesis even though the earlier gain came from specific sectors; the lower correlation benefit is a long-horizon argument.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > when your expectations are high and it doesn't work for the last 3 years um people start questioning the thesis
  indicator: alternative-market trend performance · asset: multi · horizon: years · conditions: after an extreme performance period · testable: no - investor psychology · confidence: medium
  ^MT220-C12-X1

### C13
- **Niels Kaastrup-Larsen** Roughly 40-50% of alternative markets' outperformance came from gas and power, tied to the Ukraine shock, which cannot be replicated going forward.  #mech/structural_shift
  > I think it was like 40 or 50% of the outperformance came from uh gas and power
  indicator: gas and power contribution to alt-market trend P&L · asset: commodities · horizon: years · conditions: one-off event · testable: yes · confidence: medium
  ^MT220-C13-1
- **Katy Kaminski** Adding low-correlation trend P&L streams raises portfolio Sharpe mathematically, and alternative markets add diversification though higher costs reduce their net Sharpe.  #mech/risk_premium
  > on aggregate the more lowly correlated P&L streams that you can add the little bit higher your sharp is
  indicator: P&L stream correlation and Sharpe · asset: multi · direction: add uncorrelated alternative markets · horizon: years · conditions: net of higher transaction costs · testable: yes · confidence: medium
  ^MT220-C13-2
- **Katy Kaminski** To avoid over-reading a short period (managers in alternative markets only have about 10 years of data), Quantica measures Sharpe per individual market and adjusts for the period, then reasons from portfolio theory about correlation, instead of judging by which sectors won recently.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > they said let's look at sharp per market on each individual trend instead of thinking like I know which trends or this period was better
  indicator: Sharpe ratio per market; P&L stream correlations · asset: multi · horizon: years · conditions: short sample for alternative-market managers · testable: yes - per-market Sharpe estimates · confidence: medium
  ^MT220-C13-X1
- **Katy Kaminski** The recent weakness of alternative-market trend is explained by the assets that drove 2020-22 gains (gas and power, credit and similar) being range-bound since the COVID and Ukraine shocks, so it is a regime effect rather than proof the thesis is broken.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > recently those assets have been very rangebound um after the big shock of co
  indicator: gas and power, credit and other alternative-market trend P&L · asset: commodities · horizon: years · conditions: after 2022 energy shock · testable: yes - sector attribution · confidence: medium
  ^MT220-C13-X2

### C14
- **Niels Kaastrup-Larsen** Inflows after the alternative-market outperformance may have crowded less-liquid markets and added transaction costs, contributing to recent underperformance; crowding analysis (case study of one market) would test this.  #mech/crowding_positioning
  > now we actually have maybe too much money tracing these less liquid markets.
  indicator: capacity and crowding of alternative markets · asset: commodities · horizon: years · testable: yes · confidence: low
  ^MT220-C14-1
- **Katy Kaminski** Systematic macro did better than trend around Liberation Day, motivating research on economic trends versus technical trends.  #mech/research_method _(time-bound view)_
  > I've been thinking a lot about macro and systematic macro and some interesting connections between the two strategies
  indicator: systematic macro vs trend · asset: multi · horizon: months · testable: yes · confidence: low
  ^MT220-C14-2
- **Katy Kaminski** Crowding is two-edged for trend: it still works in the most crowded liquid markets, but capacity-limited markets may show a more normal Sharpe in backtests from when fewer participants were in them, so the benefit of alternative markets is diversification, not a better trend.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check)_
  > trend falling still works in some of the most crowded markets we know
  indicator: market liquidity and capacity · asset: multi · horizon: years · conditions: less liquid alternative markets · testable: partly - crowding case study of one market proposed · confidence: medium
  ^MT220-C14-X1

