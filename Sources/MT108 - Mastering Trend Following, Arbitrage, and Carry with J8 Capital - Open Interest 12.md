---
source_id: MT108
title: "Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12"
date: 2024-12-29
channel: "Top Traders Unplugged"
url: 
words: 7763
claims: 40
added_by_crosscheck: 6
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Tilman (J8 Capital co-founder)", "Vishal (J8 head of trading and portfolio management)", "Moritz Seibert (host, Open Interest series)"]
tags: [source, layer0]
---
# Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12

**Speakers:** Tilman (J8 Capital co-founder); Vishal (J8 head of trading and portfolio management); Moritz Seibert (host, Open Interest series)

**Summary:** J8 Capital runs a decomposed multi-strategy program (trend in commodities, FX, bonds; curve arbitrage, FX carry, inventory, vol term structure) risk-weighted by inverse realised vol at 10 percent target. Redwood adds an intraday strategy with low correlation to CTA indices; costs are the key hurdle.

**Approach:** trend following, carry, term structure arbitrage, multi-strategy, short-term trading

**Cross-check completeness estimate of first read:** 0.89 - first reader caught the J8 decomposition philosophy, trend/carry/arbitrage rules, risk weighting, leverage and Redwood points; missed a few mechanisms (outright vs relative VIX trade, diversification-to-leverage logic, holding period/universe of Redwood, equity exclusion caveat, cost components) and mis-attributed one answer to the host.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, host and guest bios |
| C02 | 1 | background of both guests, why systematic |
| C03 | 4 | GARS philosophy, decomposition into single return drivers |
| C04 | 4 | trend rules across markets, why no equities |
| C05 | 5 | equities exclusion, arbitrage and carry strategies |
| C06 | 6 | VIX term structure, risk allocation, target vol |
| C07 | 3 | leverage and margin, benchmark question, CTA nature |
| C08 | 4 | Redwood short-term strategy and diversification |
| C09 | 4 | intraday sampling, turnover, performance |
| C10 | 3 | transaction cost math, infrastructure |
| C11 | 0 | programming languages, business outlook, outro |
| C12 | 0 | outro |

## Claims

### C02
- **Tilman (J8 co-founder)** Translating economic fundamentals in commodities into rules-based strategies removes the emotional and behavioral biases of discretionary traders.  #mech/behavioral
  > translate those into a systematic strategy allows to take out all the discretionary emotional behavioral Finance aspects
  asset: commodities · testable: partly: compare rules vs discretionary results · confidence: medium
  ^MT108-C02-1

### C03
- **Tilman (J8 co-founder)** Beyond asset-class diversification, diversify across return drivers and models and weight signals by risk for an extra diversification gain.  #mech/risk_premium
  > you can also diversify AC cross model risk and if you if you wait the signals according to the risk assigned to a signal that you get an additional diversification boost
  indicator: risk-weighted signal combination · asset: multi · testable: yes: compare to asset-class-only diversification · confidence: medium
  ^MT108-C03-1
- **Tilman (J8 co-founder)** Build one sub-strategy per return driver (e.g. commodity trend, term-structure arbitrage, inventory) then combine in a risk-based portfolio, instead of one big model with filters.  #mech/risk_management
  > we decomposed all those different possible return drivers within the market create single strategy for each single return driver and risk component that we want to extract
  indicator: sub-strategy decomposition · asset: multi · testable: partly · confidence: medium
  ^MT108-C03-2
- **Tilman (J8 co-founder)** Decomposition keeps transparency on where returns come from and lets managers refine each risk driver separately.  #mech/research_method
  > instead of putting everything into one big modelist strategy where one may lose the oversight of where actually R return will dra on come from we decompose it
  asset: multi · testable: partly · confidence: medium
  ^MT108-C03-3
- **Tilman (J8 co-founder)** Each sub-strategy has one degree of freedom and simple parameters, so the overall product is complex but its parts are simple.  #mech/research_method
  > each single sub strategy that we construct therefore really consists of only one single uh degree of freedom
  asset: multi · testable: partly · confidence: medium
  ^MT108-C03-4

### C04
- **Tilman (J8 co-founder)** Same trend signal method across commodities, currencies and bonds but market-specific parameters.  #mech/slow_reaction
  > each single Market has their own parameterization so we look at each markers individually
  indicator: trend signal parameters · asset: multi · testable: yes: compare market-specific vs common parameters · confidence: high
  ^MT108-C04-1
- **Tilman (J8 co-founder)** A short-term momentum strategy hedges long-term trend drawdowns during reversals.  #mech/slow_reaction
  > it kicks in with returns and with with a hedge component where our long-term strategies may suffer draw Downs during reversal periods
  indicator: short-term momentum · asset: multi · horizon: days · conditions: trend reversal periods · testable: yes · confidence: medium
  ^MT108-C04-2
- **Tilman (J8 co-founder)** Equity indices have survival bias (losers removed) that truncates signals, so equities are excluded from long-term trend following.  #mech/structural_shift
  > you do have a survival bias within those indices which distorts let's say the long-term nature of a trend following approach
  indicator: equity index survivorship · asset: equities · horizon: years · testable: partly · confidence: medium
  ^MT108-C04-3
- **Tilman (J8 co-founder)** Equities depend on rates, FX and commodity inputs already traded, so adding equity trend duplicates exposure.  #mech/crowding_positioning
  > we want to avoid redundancy effects or resonance Effects by trading equities on top that will just be triggered by movements in the underly markets which we trade already anyways
  asset: multi · testable: partly: correlation of equity trend to other sleeves · confidence: medium
  ^MT108-C04-4

### C05
- **Tilman (J8 co-founder)** Commodities have clear supply and demand fundamentals; shares are mainly speculative instruments once issued.  #mech/structural_shift
  > whereas a commodity for example is uh a real input material into uh commod to into production into the economic uh life cycle so there's clear demand and Supply
  asset: commodities · testable: no · confidence: low
  ^MT108-C05-1
- **Tilman (J8 co-founder)** Adding equity index futures did not improve their long-term trend program.  #mech/slow_reaction
  > in our long-term long-term uh slow momentum or Trend following approach um we did not find any added value by adding Equity indes to our PL
  indicator: equity trend added value · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT108-C05-2
- **Tilman (J8 co-founder)** Term-structure arbitrage harvests roll yield between long and short ends of the futures curve, closing the short end when the curve turns unsustainable.  #mech/risk_premium
  > to profit from the RO yield differentials of the Futures along the term structure
  indicator: futures curve roll yield · asset: commodities · horizon: months · testable: yes · confidence: medium
  ^MT108-C05-3
- **Tilman (J8 co-founder)** FX carry (long high-yield, short low-yield vs USD) is reversed after a sell-off signalled by short-term realised volatility.  #mech/risk_premium
  > we reverse the trades when we observe a sell off in the market based on short-term realized volatility
  indicator: FX carry; realised volatility · asset: fx · direction: exit carry on vol spike · horizon: weeks · conditions: risk-off sell-off · testable: yes · confidence: medium
  ^MT108-C05-4
- **Tilman (J8 co-founder)** Commodity curvature indicates under- or oversupply; long undersupplied and short oversupplied commodities.  #mech/risk_premium
  > going long the under supplied one and short the oversupplied one because you would expect an oversupplied Mar surprises to fall in under supplied Mar prices to increase
  indicator: futures curve shape (December vs September) · asset: commodities · direction: long backwardation, short contango · horizon: months · testable: yes · confidence: medium
  ^MT108-C05-5
- **Tilman (J8 co-founder)** The exclusion of equity indices applies only to J8's slow trend program; equity index futures can make sense when traded differently (the short-term Redwood system trades them), so the redundancy argument is horizon-specific.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > that is not to say the trading Equity indices does not make sense if you trade them differently
  indicator: equity index futures in slow trend vs short-term strategy · asset: equities · conditions: slow multi-month trend program · testable: yes - add equities to short-term vs long-term systems and compare · confidence: medium
  ^MT108-C05-X1
- **Tilman (J8 co-founder)** J8 separates two carry/arbitrage styles: arbitraging time along a futures curve (commodity term structure, volatility term structure) versus arbitraging between markets (FX carry, commodity inventory/curvature selection).  #mech/risk_premium _(added by sonnet-xhigh cross-check)_
  > here we Arbitrage time when it comes to carry trade in caros scenes and the inventory picker in commodi there we Arbitrage between asset classes
  indicator: term-structure vs cross-market carry · asset: multi · testable: partly - classification of carry strategies · confidence: low
  ^MT108-C05-X2

### C06
- **Tilman (J8 co-founder)** Use futures curve shape as a real-time inventory proxy because inventory data is delayed, revised and imprecise.  #mech/research_method
  > inventory fundamental inory data that is often delayed and then also subject to Corrections
  indicator: inventory data vs curve slope · asset: commodities · testable: yes · confidence: medium
  ^MT108-C06-1
- **Tilman (J8 co-founder)** Rolling front-month VIX futures loses about 50-60 percent a year from roll costs, so a short position can arbitrage it out.  #mech/risk_premium
  > you have annualized losses of around 50 60% per Anon which are purely Rong losses
  indicator: VIX futures roll · asset: other · direction: short VIX front month via term structure · horizon: years · testable: yes: VIX futures roll return · confidence: medium
  ^MT108-C06-2
- **Tilman (J8 co-founder)** Short volatility carry has catastrophic tail risk in spikes, so it must be hedged and managed.  #mech/risk_management
  > if you go short the FR month of volatility and then you see a 300% volatility spike in the DI can completely be catastrophic event to your entire portfolio
  indicator: VIX spike · asset: other · horizon: days · conditions: vol spike · testable: yes · confidence: high
  ^MT108-C06-3
- **Tilman (J8 co-founder)** Allocate across strategies by inverse realised volatility (equal risk), which gave the most stable overall return.  #mech/risk_management
  > if we simply take the inverse of the realized volatility of each of the systems and then and then uh weighted proportionately so essentially equal risk weighted uh asset allocation
  indicator: inverse realised volatility · asset: multi · testable: yes · confidence: high
  ^MT108-C06-4
- **Tilman (J8 co-founder)** Realised volatility is stable while correlations and recent performance are unstable, so no correlation or performance tilts.  #mech/research_method
  > the realized volatility between assets is fairly stable over time whereas of course um correlations or shortterm all performance of certain strategies
  indicator: realised vol vs correlation stability · asset: multi · testable: yes · confidence: high
  ^MT108-C06-5
- **Tilman (J8 co-founder)** Futures are unfunded, so scale exposure to a 10 percent target volatility (realised 10.26 percent over 10 years).  #mech/risk_management
  > we scale the exposure of our futures to achieve a realized Target volatility of 10%
  indicator: target volatility · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT108-C06-6
- **Tilman (J8 co-founder)** J8's volatility strategy is a relative-value trade along the VIX/VSTOXX futures term structure (short front, long back) rather than outright short volatility, so it earns roll-yield differentials without depending on the equity risk premium.  #mech/risk_premium _(added by sonnet-xhigh cross-check)_
  > that strategy is purely long short on the T structure and it does not go WR the VIX Index
  indicator: VIX and VSTOXX futures term structure · asset: other · direction: short front, long back months · conditions: needs hedging against volatility spikes · testable: yes - roll-yield spread returns testable · confidence: medium
  ^MT108-C06-X1
- **Tilman (J8 co-founder)** Combining many uncorrelated sub-strategies lowers portfolio volatility, and because futures are unfunded the exposure can be levered up to restore the 10% target volatility, so diversification can be converted into return.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > you already have a super Diversified return stream um and and and the return and the volatility gets lower and lower and lower
  indicator: portfolio volatility vs strategy count; leverage · asset: multi · conditions: unfunded instruments, adequate margin · testable: yes - diversification gain converted via leverage · confidence: medium
  ^MT108-C06-X2

### C07
- **Tilman (J8 co-founder)** At 10 percent target vol, margin to equity is about 6-12 percent, so 1 million cash controls roughly 30 million of notional.  #mech/liquidity_flows
  > we just need to use between let's say six and 10 sometimes 12% margin Equity
  indicator: margin to equity · asset: multi · testable: yes · confidence: high
  ^MT108-C07-1
- **Tilman (J8 co-founder)** A simple index built from survey answers explained about 80 percent of CTA index returns: diversified, risk-weighted 12-month momentum.  #mech/slow_reaction
  > this index model broadly to let's say 80% of its returns broadly mimic or go or are similar to uh popular CTA Benchmark Ines
  indicator: 12-month momentum risk-weighted · asset: multi · horizon: years · testable: yes: replicate with simple 12-month momentum · confidence: medium
  ^MT108-C07-2
- **Tilman (J8 co-founder)** J8 is half traditional CTA and half alternative risk premia, so no single benchmark fits.  #mech/risk_premium
  > I would say we are 50% traditional CTA 50% % let's say alternative risk premium so CTA plus
  asset: multi · testable: no · confidence: medium
  ^MT108-C07-3

### C08
- **Vishal (J8, head of trading)** Redwood trades intraday breakouts measured in volatility terms within trend, volatility and positioning context.  #mech/slow_reaction
  > the base of the strategy is all about exploiting those extreme movements or not even extreme like I mean we talk in terms of like breakouts being measured in terms of volatility
  indicator: volatility-scaled breakouts; 3-5 minute sampling · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT108-C08-1
- **Vishal (J8, head of trading)** Short-term trading requires highly liquid futures for cheap entry and exit.  #mech/liquidity_flows
  > this strategy is focused on the big futures the future which have good liquidity uh which are easy to get in and get out
  asset: multi · horizon: days · testable: yes · confidence: high
  ^MT108-C08-2
- **Vishal (J8, head of trading)** Short-term strategy has low or negative correlation to CTA indices and improved risk-adjusted return in simulations.  #mech/risk_premium
  > this correlation of the short-term strategy to any of the CDA indices uh available across the board whether to SNP individually or to other industry benchmarks is quite low in fact some of them are quite bit negative also
  indicator: correlation to CTA indices · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT108-C08-3
- **Moritz Seibert (host)** Redwood's correlation with the short-term traders index is near zero.  #mech/risk_premium
  > found it practically nothing it's like very close to 0
  indicator: STTI correlation · asset: multi · horizon: days · testable: yes · confidence: medium
  **Correction (cross-check):** Wrong speaker: Moritz asks what Redwood's correlation to the short-term traders index is; the answer ('we ran it and found it practically nothing, very close to 0') is Vishal's. → Vishal: Redwood's correlation with the SG Short Term Traders Index is practically zero (close to 0).
  ^MT108-C08-4
- **Vishal (J8, head of trading)** Redwood's holding period is a few hours to a few days (3-5 days at most, mostly same day or next day), and unlike the main program it trades all asset classes including equity indices, in liquid futures only.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > very few of them are being held over like multiple days which can be like 3 to five days
  indicator: holding period; asset-class coverage of Redwood · asset: multi · horizon: days · conditions: highly liquid futures only · testable: yes - holding-period and universe checks · confidence: high
  ^MT108-C08-X1

### C09
- **Vishal (J8, head of trading)** Short-term trading is not simply counter-trend; each strategy uses its own horizon context including volatility.  #mech/research_method
  > my trend is defined in a slightly different way than the the long-term Trend
  asset: multi · horizon: days · testable: partly · confidence: medium
  ^MT108-C09-1
- **Vishal (J8, head of trading)** About 700 round trips per million per month (roughly 8,000 per year) across 12 futures.  #mech/risk_management
  > 700 round trips uh per million per month
  indicator: turnover · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT108-C09-2
- **Vishal (J8, head of trading)** Short-term systems get higher Sharpe at similar returns but must avoid whipsaws from noise.  #mech/slow_reaction
  > the real challenge in the short shortterm stuff is to avoid whiplashes because there's a lot of noise in the short-term space
  asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT108-C09-3
- **Vishal (J8, head of trading)** Vishal says performance is not highly sensitive to small cost changes; he lacks exact numbers.  #mech/risk_management
  > it's not anything substantial to say that the strategy is impacted by slightly varing um transaction cost
  indicator: transaction costs · asset: multi · horizon: days · testable: yes: cost sensitivity test · confidence: low
  ^MT108-C09-4

### C10
- **Moritz Seibert (host)** Moritz's math: at about 6 dollars per contract and 8,000 round turns per million, costs are about 10.8 percent a year, a very high hurdle for short-term strategies.  #mech/risk_management
  > when we do these 8 8,000 round turns per million per year you're down about 11% uh 10.8% to be exact in terms of uh expected execution and implementation cost
  indicator: execution cost per contract · asset: multi · horizon: years · conditions: per 6 dollar all-in contract cost · testable: yes · confidence: medium
  **Correction (cross-check):** Faithful to the speaker but the arithmetic does not reconcile: 8,000 round turns x 2 contracts x $6 = 9.6% (and 700 per month x 12 = 8,400 gives about 10.1%); 10.8% would need about 9,000 round turns at $12. Treat 10.8% as the speaker's rough figure, about 10% a year. → Moritz: at roughly 6 dollars all-in per contract and about 8,000-9,000 round turns per million per year, execution cost is roughly 10 percent a year (he states 10.8%), a very high hurdle for the short-term strategy.
  ^MT108-C10-1
- **Vishal (J8, head of trading)** Short-term systems can easily overtrade, so exposure and sensitivity must be controlled.  #mech/risk_management
  > you can easily do overtrading in the short-term space
  asset: multi · horizon: days · testable: yes · confidence: high
  ^MT108-C10-2
- **Vishal (J8, head of trading)** Intraday trading needs 24-hour automated infrastructure (FIX execution, alerts, monitoring desks in India and UK), an operational overhead.  #mech/risk_management
  > we have built our own in-house uh infrastructure for the fix uh execution
  asset: multi · testable: no · confidence: high
  ^MT108-C10-3
- **Moritz Seibert (host)** Cost build-up for a non-HFT futures trader: about 0.75 broker commission, 0.50 exchange fee, 0.50 clearing fee, plus spread, slippage and market impact, which brings the all-in cost to roughly 5-6 dollars per contract.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > there is like an execution Commission of 75 cents and there's always exchange fees whatever like 50 cents and clearing fees 50 cents
  indicator: per-contract execution cost components · asset: multi · conditions: firms without HFT infrastructure or exchange membership · testable: yes - cost components can be audited · confidence: medium
  ^MT108-C10-X1

