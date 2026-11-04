---
source_id: MT113
title: "Navigating a New World Order- Macro Strategies for Uncertain Times - Pablo Calderini"
date: 2025-01-07
channel: "Graham Capital Management"
url: https://www.youtube.com/watch?v=x3HYAHlKe-c
words: 5661
claims: 41
added_by_crosscheck: 7
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Pablo Calderini (President and CIO, Graham Capital Management)", "Chief client officer (host, name garbled in captions)", "Scott (audience question)"]
tags: [source, layer0]
---
# Navigating a New World Order- Macro Strategies for Uncertain Times - Pablo Calderini

**Speakers:** Pablo Calderini (President and CIO, Graham Capital Management); Chief client officer (host, name garbled in captions); Scott (audience question)

**Summary:** Graham Capital client session (Jan 2023 context): post-GFC policy regime ended, hiking-cycle history, core inflation and changing stock-bond correlation justify macro as a complement to 60/40 with positive skew and negative conditional correlation. Describes quant trend and quant macro programs and tactical views.

**Approach:** discretionary macro, quant macro, trend following, portfolio construction, 60/40

**Cross-check completeness estimate of first read:** 0.86 - first reader captured nearly every argument of the slide-by-slide talk (hiking cycles, core inflation, stock-bond correlation, long-horizon variance, macro skew); missed a few supporting causal links and operating details (inflation drives correlation, Fed guidance blamed, concentrated multi-PM book, recency bias).

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | Graham intro; post-GFC accommodative regime vs inflation shock |
| C02 | 4 | Inflation not secular low; five hiking cycles; current cycle record; method of forward curves |
| C03 | 4 | Forward curve vs delivered; core vs energy inflation |
| C04 | 5 | Core persistence; stock-bond correlation regimes; stocks for the long run |
| C05 | 5 | Long-horizon variance; macro conditional correlation and skew |
| C06 | 3 | 20% macro in 60/40; Treasury 20 sigma; macro as complement |
| C07 | 5 | Current views: short equities, long EUR, JPY, gold |
| C08 | 5 | Quant side: trend and quant macro sub-strategies |
| C09 | 1 | Quant macro track and comparison with trend |

## Claims

### C01
- **Pablo Calderini** For ten years after the GFC every shock was met by very accommodative central banks (zero lower bound, sticky-low inflation), a special regime that is over after the 2022 inflation shock.  #mech/policy_reaction
  > there was not one crisis that the FED uh was not able to accommodate
  indicator: central bank policy response · asset: multi · horizon: years · conditions: post-GFC low-inflation regime · testable: partly: regime description · confidence: high
  ^MT113-C01-1
- **Pablo Calderini** The inflation shock must be met by a shock to real rates, so asset markets and central banks play a completely different game from the post-GFC decade.  #mech/policy_reaction
  > it's a shock that needs to be matched by another shock
  indicator: real rates · asset: rates · horizon: years · testable: partly: real rate shocks versus asset returns · confidence: high
  ^MT113-C01-2
- **Chief client officer (host)** Graham runs its discretionary multi-PM macro book concentrated, betting on its highest-conviction teams (about 15) rather than spreading across 50 to 150 teams, a portfolio-construction choice favouring conviction over breadth.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > rather than have 50 or 150 teams here we have roughly 15 today
  indicator: number of PM teams (about 15 vs 50-150) · asset: multi · testable: partly - needs PM-level returns to compare concentrated and diversified multi-PM books · confidence: medium
  ^MT113-C01-X1

### C02
- **Pablo Calderini** Inflation is no longer seen as a secular low (supply disruptions, geopolitics, fiscal expenditure), so central banks will be shyer about accommodative policy, leading to higher volatility and a harder time for 60/40.  #mech/structural_shift
  > inflation is not that sticky low central banks can do whatever they want with their balance sheets
  indicator: inflation, 60/40 portfolio · asset: multi · horizon: years · testable: partly: volatility regime comparison · confidence: high
  ^MT113-C02-1
- **Pablo Calderini** Of the last five hiking cycles since Volcker (1994-95 +300bp, 1999-2000 +175bp, 2005-06 +425bp, 2015-18, plus 2022), each ended with a crisis or turmoil (tequila, Asia, Nasdaq, GFC, 2018) after which the Fed gave up.  #mech/cycle_persistence
  > the last five hiking Cycles uh since post Volker
  indicator: Fed funds hiking cycles · asset: rates · horizon: years · testable: yes: event study of hiking cycle ends · confidence: high
  **Correction (cross-check):** Overstated: the 'five cycles' are four completed cycles (1994-95, 1999-2000, 2005-06, 2015-18) plus the still-running 2022-23 cycle; only the four completed cycles ended in turmoil, and the 2015-18 cycle ended with turmoil in 2018 while the cut came in March 2020 with covid. → In the four completed hiking cycles since Volcker (1994-95 +300bp, 1999-2000 +170-175bp, 2005-06 +425bp, 2015-18) the Fed stopped after turmoil (tequila and Asian crises, Nasdaq collapse, the global financial crisis, 2018 market turmoil); the current cycle is a fifth, still running.
  ^MT113-C02-2
- **Pablo Calderini** The 2022-23 hiking cycle is a record in magnitude and speed: double the average of previous four cycles (about 220bp) in half the time, heading to about 500bp.  #mech/policy_reaction _(time-bound view)_
  > the current height is double the average of the previous four hiking Cycles
  indicator: Fed hiking cycle size and speed · asset: rates · horizon: years · testable: yes: compare cycles · confidence: high
  ^MT113-C02-3
- **Pablo Calderini** Method: compare the forward curve on the first day of each hiking cycle with what the Fed delivered to judge how prepared (fragile) markets were; the less priced, the more fragile.  #mech/research_method
  > let's see how forward curves were on
  indicator: forward curve at first hike versus delivered · asset: rates · horizon: years · testable: yes: replicate for all cycles · confidence: medium
  ^MT113-C02-4

### C03
- **Pablo Calderini** In earlier hiking cycles forward pricing was close to what the Fed delivered for 18 months, so markets were well prepared and resilient.  #mech/slow_reaction
  > the FED actually did a fairly good job at least for the first 18 months always in guiding markets really well to what was to come
  indicator: forward curve minus delivered path · asset: rates · horizon: months · testable: yes: curve minus delivered · confidence: high
  ^MT113-C03-1
- **Pablo Calderini** In 2022 the Fed hiked about 300bp more than the forward curve priced at the first hike, a huge unprecedented shock to markets and a reason for fragility.  #mech/overshoot
  > the FED height 300 basis points more than what the markets were pricing
  indicator: forward curve minus delivered path · asset: rates · horizon: months · testable: yes: curve minus delivered · confidence: high
  ^MT113-C03-2
- **Pablo Calderini** The beta of asset returns to inflation is non-linear: higher inflation helps in deflation and hurts in high inflation, which is why regression coefficients look inconclusive.  #mech/structural_shift
  > if we are in a deflationary period higher inflation actually can be very positive for asset prices
  indicator: inflation beta to asset returns · asset: multi · horizon: years · conditions: depends on inflation regime · testable: yes: regime-split regression · confidence: high
  ^MT113-C03-3
- **Pablo Calderini** A Wharton study splitting inflation by drivers finds core inflation is a large negative shock for asset prices while energy/headline ex-core is nearly unimportant, because energy inflation is volatile and mean-reverting.  #mech/structural_shift
  > core inflation as always a massive negative shock for us at prices while NRC or headline inflation X score uh being almost unimportant
  indicator: core inflation vs energy inflation · asset: multi · direction: bearish equities on core inflation surprises · horizon: years · testable: yes: replicate with core vs energy · confidence: medium
  ^MT113-C03-4
- **Pablo Calderini** The 2022 hiking shock was a Fed communication failure: in past cycles good forward guidance (or good market reading) left markets resilient, whereas in 2022 the Fed hiked far beyond what it had guided, producing a larger shock to asset prices.  #mech/policy_reaction _(added by sonnet-xhigh cross-check)_
  > I would put the culprit on the on the FED right I would say by how badly the FED building guiding markets to to the actual outcome
  indicator: forward curve at first hike versus realised Fed path · asset: rates · horizon: months · conditions: larger gap between priced and delivered hikes means more fragility · testable: yes - compute priced-minus-delivered path for each cycle and relate to subsequent drawdowns · confidence: medium
  ^MT113-C03-X1

### C04
- **Pablo Calderini** Core inflation is persistent (rises stay) so it needs a larger policy response and causes a larger asset price reaction than energy inflation.  #mech/policy_reaction
  > it will entice a much a much bigger response by asset prices
  indicator: core inflation persistence · asset: multi · horizon: years · testable: yes: autocorrelation of core vs energy · confidence: high
  ^MT113-C04-1
- **Pablo Calderini** Bonds are held because their lower expected return buys a hedge; with a 400-500bp equity risk premium they only make sense with a low or negative correlation to stocks.  #mech/risk_management
  > it's once were correlated to equities you would have almost no bonds in your portfolio
  indicator: stock-bond correlation · asset: rates · horizon: years · testable: partly: portfolio theory · confidence: high
  ^MT113-C04-2
- **Pablo Calderini** The long-run stock-bond correlation is about zero, an average of periods of high positive and high negative correlation; it was very positive from the 1960s to 2000s in high-inflation periods.  #mech/cycle_persistence
  > the long run correlation between stocks and bonds is really around zero
  indicator: rolling stock-bond correlation · asset: rates · horizon: years · conditions: high inflation raises correlation · testable: yes: correlation versus inflation · confidence: high
  ^MT113-C04-3
- **Pablo Calderini** Going forward stock-bond correlation is expected near zero, not the -0.5 of the previous 20 years that made 60/40 a bonanza.  #mech/structural_shift _(time-bound view)_
  > it's hard to think we're going to go back to the the great days of minus 50 correlation between stocks and bonds
  indicator: stock-bond correlation · asset: rates · horizon: years · testable: partly: forecast · confidence: medium
  ^MT113-C04-4
- **Pablo Calderini** The 'stocks for the long run' argument relies on mean reversion and lower long-horizon variance, but variance forecasts forward must also estimate the unknown mean.  #mech/research_method
  > stocks for the long run
  indicator: long-horizon equity variance · asset: equities · horizon: years · testable: yes: replicate variance calc · confidence: medium
  ^MT113-C04-5
- **Pablo Calderini** High inflation pushes the stock-bond correlation up (to positive) because inflation shocks hit both assets; a falling-inflation regime gives negative correlation, so the sign of the correlation follows the inflation regime.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check)_
  > High inflation usually drives correlation up
  indicator: rolling stock-bond correlation versus inflation level · asset: multi · direction: stock-bond correlation rises when inflation is high · horizon: years · conditions: high-inflation regimes such as the 1960s-1990s; zero or near zero in 2022-23 · testable: yes - rolling correlation against CPI regimes · confidence: high
  ^MT113-C04-X1
- **Pablo Calderini** After 20 years of negative stock-bond correlation, newer market participants assume bonds always hedge stocks, an extrapolation of a regime that is not the long-run norm, which leaves 60/40 portfolios exposed when the sign flips.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > we have lived in this world of negative correlation for 20 years now to the point that I think that new newcomers to financial markets might
  indicator: stock-bond correlation · asset: multi · horizon: years · testable: partly - the 20-year negative-correlation fact is testable, the belief claim is not · confidence: medium
  ^MT113-C04-X2

### C05
- **Pablo Calderini** Without the degree of freedom from a known mean, proper long-horizon calculations raise equity volatility from about 17% to about 22%, so mean-variance should hold fewer equities.  #mech/risk_management
  > when you do proper calculations stocks are a lot more volatile in the long run
  indicator: long-horizon equity variance · asset: equities · direction: reduce equity weight · horizon: years · testable: yes: reproduce calculation · confidence: medium
  ^MT113-C05-1
- **Pablo Calderini** Bonds with low returns and zero correlation to stocks in a period of active monetary policy are not the diversifiers they were.  #mech/structural_shift _(time-bound view)_
  > are also not the diversifiers that they were
  indicator: bond-stock correlation · asset: rates · horizon: years · testable: partly · confidence: high
  ^MT113-C05-2
- **Pablo Calderini** Macro funds (HFRI macro index) have zero average correlation to equities but negative conditional correlation, gaining in large equity drawdowns.  #mech/risk_premium
  > the conditional correlation I our correlation to equities when equities are doing really badly it's negative
  indicator: HFRI macro index conditional correlation · asset: multi · direction: long macro · horizon: years · conditions: equity drawdowns · testable: yes: conditional correlation test · confidence: high
  ^MT113-C05-3
- **Pablo Calderini** Macro returns show positive skew (almost 4 sigma on the upside, no -3 sigma), valuable for portfolio construction.  #mech/risk_premium
  > we have that so-called positive skew which means that we tend to if we're gonna surprise you we're gonna surprise you on the upside
  indicator: skew of macro returns · asset: multi · horizon: years · testable: yes: skew measurement · confidence: high
  ^MT113-C05-4
- **Pablo Calderini** Investors focus too much on Sharpe, returns and standard deviation; skewness and conditional correlation should enter efficient portfolio construction.  #mech/research_method
  > skewness and conditional correlation are super important
  indicator: skew, conditional correlation · asset: multi · testable: yes: add to optimiser · confidence: high
  ^MT113-C05-5

### C06
- **Pablo Calderini** Adding 20% macro to a 60/40 over the last 20 years lowers return slightly but lowers volatility more, lifting information ratio from 0.66 to 0.75 and cutting worst drawdown from -36% to -29%.  #mech/risk_management
  > adding 20 macro might actually will actually cut the annual return a bit but we'll cut the volatility a lot more
  indicator: 60/40 plus 20% macro · asset: multi · direction: add macro allocation · horizon: years · testable: yes: backtest blend · confidence: high
  ^MT113-C06-1
- **Pablo Calderini** The March 2023 Treasury yield move was a 20 sigma event that hurt dynamic trading funds; Graham was little affected but is making risk systems more robust to such shocks.  #mech/risk_management _(time-bound view)_
  > what happened in threshold yields was uh really is 20 Sigma event
  indicator: Treasury yield moves · asset: rates · horizon: days · testable: partly: event · confidence: medium
  ^MT113-C06-2
- **Pablo Calderini** Macro is a complement to 60/40: it holds no long-term secular views (already in 60/40) and adds value by being tactical, dynamic and quick to cut positions when the thesis fails.  #mech/risk_management
  > we see it as a complement to the 60 40 portfolio we don't we don't hold very long term secular views
  asset: multi · testable: no: philosophy · confidence: high
  ^MT113-C06-3
- **Pablo Calderini** The 20-year average benefit of adding macro to 60/40 understates the benefit in stress years such as 2022, when macro can add more than the average.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > I also think these are our asses like we saw last year when things get really bad I think macro has the capacity to even improve on this right
  indicator: 60/40 plus macro portfolio in stress years · asset: multi · direction: long macro alongside 60/40 · horizon: years · conditions: bad years for 60/40 · testable: yes - split the sample by 60/40 drawdown years · confidence: medium
  ^MT113-C06-X1

### C07
- **Pablo Calderini** Short equities: earnings must fall and multiples are too high; either sticky core inflation forces the Fed to hike versus priced cuts, or core falls only via unemployment spike and recession cutting earnings; views are changeable.  #mech/policy_reaction _(time-bound view)_
  > we are we are short equities uh we were not short on the way up
  indicator: S&P earnings, multiples, fed funds futures pricing cuts · asset: equities · direction: short equities · horizon: months · testable: partly: scenario view · confidence: medium
  ^MT113-C07-1
- **Pablo Calderini** Long euro: US banking issues stop the Fed from hiking massively while the ECB is hawkish.  #mech/policy_reaction _(time-bound view)_
  > we actually like the Euro we feel that with the banking issues in the U.S
  indicator: Fed vs ECB policy · asset: fx · direction: long EUR · horizon: months · testable: partly · confidence: medium
  ^MT113-C07-2
- **Pablo Calderini** Long yen: extremely undervalued and a BoJ yield-curve-control change eventually coming.  #mech/policy_reaction _(time-bound view)_
  > Ian is extremely extremely undervalued so we we like Yen as well
  indicator: JPY valuation, BoJ YCC · asset: fx · direction: long JPY · horizon: months · testable: partly: valuation · confidence: medium
  ^MT113-C07-3
- **Pablo Calderini** Long gold, highest conviction: real rates are elevated and will come down, breakevens are too low, and the US debt ceiling negotiation is usually gold-bullish.  #mech/fiscal_debt _(time-bound view)_
  > we like gold I mean that's the one that we have the most conviction
  indicator: real rates, breakevens, debt ceiling · asset: commodities · direction: long gold · horizon: months · testable: yes: gold vs real rate and breakeven changes · confidence: high
  ^MT113-C07-4
- **Pablo Calderini** Discretionary macro value is the ability to change views and positions within a month rather than stick to a view.  #mech/risk_management
  > we can talk in a month and have completely different views
  asset: multi · testable: no: philosophy · confidence: high
  ^MT113-C07-5
- **Pablo Calderini** A fundamental short-equity view is held with humility: unknown market forces may keep equities supported, so risk management and a tactical hedge are used to limit the cost of being early or wrong.  #mech/risk_management _(added by sonnet-xhigh cross-check, time-bound view)_
  > cognizant though that there's Market forces supporting equities that are beyond our understanding and that's where it comes our uh our risk management and our tactical head
  asset: equities · direction: short equities with tactical risk control · horizon: months · conditions: fundamental view contrary to price action · testable: no - discretionary practice · confidence: medium
  ^MT113-C07-X1

### C08
- **Pablo Calderini** Quant macro blends price-based signals with fundamental data, giving a more dynamically evolving positioning than pure trend.  #mech/structural_shift
  > we do bring in fundamental data points into that font macro signal
  indicator: quant macro signal · asset: multi · testable: partly · confidence: medium
  **Correction (cross-check):** Wrong speaker: this passage is the host (Graham chief client officer) summarising the systematic side, not Pablo Calderini; the transcript says pure trend is price-driven and the quant macro strategy brings in fundamental data points. → The host (chief client officer) says Graham's pure trend following is price-driven while the quant macro strategy adds fundamental data to the price signal, so its positioning can evolve more dynamically.
  ^MT113-C08-1
- **Pablo Calderini** Trend program adds value via robust portfolio construction (mean-variance, PCA to estimate covariance matrix fast to mitigate risk) on a traditional time-series momentum signal.  #mech/risk_management
  > we have added value on top of trend
  indicator: covariance via PCA · asset: multi · testable: yes: PCA vs sample covariance · confidence: medium
  ^MT113-C08-2
- **Pablo Calderini** The quant macro program has four sub-strategies: trend, value (long-run reversion), carry and macro fundamentals, combined by mean-variance; running eight years with Sharpe above one.  #mech/structural_shift
  > one is based on on on Trend the other one is based on value or long-running reversion the other one is based on Curry
  indicator: trend, value, carry, macro · asset: multi · testable: yes: four-factor decomposition · confidence: high
  ^MT113-C08-3
- **Pablo Calderini** Fundamentals affect markets non-linearly and regime-dependently, so the macro signal uses about 900,000 time series, NLP sentiment and data compression with non-linear regression.  #mech/structural_shift
  > it's highly non-linear it depends on what regime you're on
  indicator: GDP, inflation, earnings, inventories, NLP sentiment · asset: multi · testable: partly: needs large data · confidence: medium
  ^MT113-C08-4
- **Pablo Calderini** Carry is not naive: they avoid simply buying high-carry assets and estimate an equilibrium required carry.  #mech/risk_premium
  > we try to come up with ideas of equilibrium of required cover
  indicator: carry vs equilibrium carry · asset: multi · testable: yes: adjusted carry · confidence: low
  ^MT113-C08-5
- **Pablo Calderini** Graham's trend-following program did really well in 2022, the year of the inflation shock and rate-hike regime, consistent with trend profiting from large macro dislocations.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > one is a trend following program right and that did really well last year
  indicator: Graham trend program return in 2022 · asset: multi · horizon: years · testable: partly - single-year performance claim · confidence: medium
  ^MT113-C08-X1

### C09
- **Pablo Calderini** Trend gains when equities tank; the quant macro program has less of that conditional benefit but a more stable return profile and higher information ratio than trend.  #mech/risk_premium
  > Trend following has a very nice negative conditional correlation to equities when equities tank
  indicator: trend vs quant macro conditional correlation · asset: multi · horizon: years · testable: yes: conditional correlation · confidence: medium
  ^MT113-C09-1

