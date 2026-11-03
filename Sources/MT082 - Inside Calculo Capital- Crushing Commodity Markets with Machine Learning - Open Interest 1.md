---
source_id: MT082
title: "Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 15"
date: 2025-04-27
channel: "Top Traders Unplugged"
url: 
words: 7343
claims: 46
added_by_opus: 0
corrections: 0
crosscheck: "pending"
speakers: ["Philip Engel Carlson (founder, Calculo Capital)", "Ola Hansen (Saxo Bank commodity strategist, Calculo board member)", "Moritz Seibert (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 15

**Speakers:** Philip Engel Carlson (founder, Calculo Capital); Ola Hansen (Saxo Bank commodity strategist, Calculo board member); Moritz Seibert (host, Top Traders Unplugged)

**Summary:** Interview with Calculo Capital, a Copenhagen short-term (2 to 5 day) systematic commodity CTA. Classical breakout trend-following entries, machine learning used only for exits via pattern matching to historical trades; plus Saxo's commodity outlook for early 2025 (precious metals, tariffs, natural gas).

**Approach:** trend following, commodities, machine learning exits, short-term CTA

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | Teaser of ML matching, disclaimers, host intro of Calculo and fund profile |
| C02 | 6 | Commodity market review early 2025; precious metals; long-term themes (deglobalisation, defence) |
| C03 | 7 | Energy transition, demographics, mining supply, softs, natural gas, Calculo gas trade |
| C04 | 6 | Copper, COMEX tariff premium, physical flows, silver |
| C05 | 4 | Calculo focus on commodities, holding period, liquidity, supply shocks |
| C06 | 6 | Entry signals, ML risk management, hurricane example, price-only inputs |
| C07 | 4 | Flat positions, exit methodology, ML matching, daily bars |
| C08 | 3 | Trend-only entries, ML for exit only |
| C09 | 3 | Execution timing, why Ola invests, BCOM drawdowns |
| C10 | 6 | Index design, roll yield, track record |
| C11 | 0 | Domicile, growth plans, outro (nothing actionable) |

## Claims

### C01
- **Moritz Seibert** Calculo Capital is a Copenhagen systematic CTA that trades only commodities with 1 to 10 day holding periods and uses machine learning in its trading process.  #mech/slow_reaction
  > Third, because they are short-term withholding periods of 1 to 10 days per trade.
  asset: commodities · horizon: days · testable: partly - strategy description, not a testable claim itself · confidence: high
  ^MT082-C01-1

### C02
- **Ola Hansen** The Bloomberg Commodity Index was up almost 10% in the first weeks of 2025, ahead of equities, with all sectors posting gains.  #mech/cycle_persistence _(time-bound view)_
  > I watch something like the Bloomberg commodity index which uh which is broadly exposed to agricultural com metals and energy and it's up nearly 10%
  indicator: Bloomberg Commodity Index YTD · asset: commodities · direction: commodities up · horizon: weeks · testable: yes - index data · confidence: high
  ^MT082-C02-1
- **Ola Hansen** Strong demand for gold and other precious metals, which yield nothing and cost money to store, is a hedge against an uncertain, unbalanced world.  #mech/risk_premium _(time-bound view)_
  > that really is just an expression of an a world that is not in balance.
  indicator: gold and precious metals prices · asset: commodities · direction: precious metals up · horizon: months · conditions: When uncertainty is high · testable: partly - needs an uncertainty measure · confidence: medium
  ^MT082-C02-2
- **Ola Hansen** Central banks buying gold for three years to diversify away from US dollar assets (plus private investors) is a persistent source of gold demand.  #mech/liquidity_flows _(time-bound view)_
  > Not only central banks who have been buying for the past three years in order to diversify their
  indicator: central bank gold purchases · asset: commodities · direction: gold up · horizon: years · testable: yes - central bank gold purchases are published · confidence: high
  ^MT082-C02-3
- **Ola Hansen** Rising government debt burdens, especially in the US, push investors into precious metals as a fiscal-risk hedge.  #mech/fiscal_debt
  > the fiscal debt worries that uh that that basically comes with the the rising debt burdens we're seeing around the world
  indicator: government debt levels and gold · asset: commodities · direction: gold up · horizon: years · testable: partly - debt vs gold relationship · confidence: medium
  ^MT082-C02-4
- **Ola Hansen** Deglobalisation moves production closer to home, which needs a lot of commodities and could raise some prices.  #mech/structural_shift
  > we're seeing the the deglobalization where production is being moved closer to home.
  asset: commodities · direction: commodities up · horizon: years · testable: no - thematic · confidence: medium
  ^MT082-C02-5
- **Ola Hansen** Rising European defence spending requires steel and rare-earth minerals, supporting commodity demand.  #mech/fiscal_debt
  > We have the increased spending on defense coming through in Europe now in a in a big way.
  indicator: European defence budgets · asset: commodities · direction: steel and rare earths up · horizon: years · testable: partly - spending is public · confidence: medium
  ^MT082-C02-6

### C03
- **Ola Hansen** The energy transition raises power demand (EVs, data centers, cooling), so it supports copper, aluminium, lithium, cobalt, nickel and silver.  #mech/structural_shift
  > the energy transition is also a question of of we're moving towards increased use of power and it's not only towards electrical vehicles it's also towards data centers
  indicator: power demand and electrification metals · asset: commodities · direction: copper, aluminium, lithium, cobalt, nickel, silver up · horizon: years · testable: partly - demand forecasts · confidence: medium
  ^MT082-C03-1
- **Ola Hansen** An ageing population with accumulated savings will spend that money, adding to consumption and commodity demand.  #mech/structural_shift
  > the money that we are saved in over decades that's that will be spent
  asset: commodities · direction: consumption up · horizon: years · testable: no - thematic · confidence: low
  ^MT082-C03-2
- **Ola Hansen** Continuing urbanisation in emerging markets underpins commodity demand.  #mech/structural_shift
  > urbanization undergoing in especially in emerging markets that will also underpin the demand.
  asset: commodities · direction: commodity demand up · horizon: years · testable: no - thematic · confidence: medium
  ^MT082-C03-3
- **Ola Hansen** Mining projects take many years, so miners must guess prices 10 to 12 years ahead, which holds back investment and can cause future metal shortfalls.  #mech/structural_shift
  > mining companies they have to look 10 to 12 years out and try to gauge what the price would be out there.
  indicator: mining capex vs lead times · asset: commodities · direction: metal prices up from shortfall · horizon: years · testable: partly - capex data · confidence: medium
  ^MT082-C03-4
- **Ola Hansen** Softs are produced in small geographic areas, so weather in West Africa (cocoa) and Brazil (coffee) drives large price moves.  #mech/structural_shift _(time-bound view)_
  > making them much more exposed to any weather developments.
  indicator: weather in cocoa and coffee regions · asset: commodities · direction: cocoa and coffee spikes · horizon: months · testable: yes - weather and price data · confidence: high
  ^MT082-C03-5
- **Ola Hansen** Rising US gas exports, domestic demand and European LNG demand underpin a long-term bullish case for natural gas.  #mech/structural_shift _(time-bound view)_
  > US exports of gas is rising. US demand for gas as well is also rising and that will over time underpin prices.
  indicator: US natural gas exports and demand · asset: commodities · direction: natural gas up · horizon: years · testable: partly - fundamental data · confidence: medium
  ^MT082-C03-6
- **Philip Engel Carlson** Calculo's short Henry Hub natural gas trade, held more than two years, was exited by a rally on 20 February 2025 after a cold weather outlook, an example of a trend position ending only when the trend reverses.  #mech/cycle_persistence _(time-bound view)_
  > We got kicked out of a short Henry hop position which we've had on for more than two years.
  indicator: Henry Hub natural gas · asset: commodities · direction: short natural gas · horizon: years · testable: no - single trade · confidence: high
  ^MT082-C03-7

### C04
- **Ola Hansen** Tariff worries lifted US COMEX futures prices of gold, silver, copper and platinum above London spot prices because imported metal would face tariffs.  #mech/policy_reaction _(time-bound view)_
  > we're seeing right now that futures prices for gold, silver, copper, platinum, they have all been uh been
  indicator: COMEX vs London metal premium · asset: commodities · direction: COMEX premium up · horizon: weeks · conditions: While tariff threat on metals persists · testable: yes - COMEX-LME spreads · confidence: high
  ^MT082-C04-1
- **Ola Hansen** The COMEX-London premium made it profitable to ship physical gold and silver to New York and sell futures against it, drawing in large inventories; the cash and carry basis on gold was about 10% annualised.  #mech/liquidity_flows _(time-bound view)_
  > if you have access to physicals and you can sell the future against it, you are earning a handsome handsome return.
  indicator: COMEX cash-and-carry basis · asset: commodities · direction: metal stocks flow into US · horizon: weeks · conditions: Premium persists · testable: yes - basis and inventory data · confidence: high
  ^MT082-C04-2
- **Ola Hansen** When the premium narrows, physical gold in US vaults with no end user may be sold or hedged, a possible small negative for prices.  #mech/liquidity_flows _(time-bound view)_
  > then there's a lot of physical gold sitting in the US uh with no uh end user.
  indicator: COMEX gold inventories · asset: commodities · direction: gold down · horizon: months · conditions: Spread normalises · testable: partly - needs inventory data · confidence: low
  ^MT082-C04-3
- **Ola Hansen** Chinese copper demand has held up despite the construction downturn, and data centers and power transmission add demand beyond EVs.  #mech/structural_shift _(time-bound view)_
  > the de demand in China has held up phenomenally well even though the construction
  indicator: China copper demand · asset: commodities · direction: copper up · horizon: months · testable: partly - demand data · confidence: medium
  ^MT082-C04-4
- **Ola Hansen** In the gold rush the shovel supplier made the money, so power-grid builders such as Siemens Energy (up 300%) capture the AI and electrification boom, as Nvidia did.  #mech/structural_shift _(time-bound view)_
  > It was the guy who supplied the shovels.
  indicator: power infrastructure stocks · asset: equities · horizon: years · testable: no - analogy · confidence: medium
  ^MT082-C04-5
- **Ola Hansen** Gold shorts can borrow from the Bank of England but silver has no lender of last resort, so silver gets squeezed harder.  #mech/liquidity_flows _(time-bound view)_
  > because if you are if you have a if you're short gold in London market, you can go to the Bank of England and uh and and lease gold from uh from them.
  indicator: silver vs gold lending · asset: commodities · direction: silver squeezes · horizon: weeks · testable: partly - lease rates · confidence: medium
  ^MT082-C04-6

### C05
- **Ola Hansen** Silver carries higher tariff risk than gold because gold is quasi-monetary and much silver comes from Mexico.  #mech/policy_reaction _(time-bound view)_
  > there's probably more higher risk that tariffs would be added to silver than to gold being a a monetary
  indicator: tariff exposure of silver · asset: commodities · direction: silver premium · horizon: weeks · testable: no - speculation · confidence: low
  ^MT082-C05-1
- **Philip Engel Carlson** Calculo holds trades 2 to 5 days: it captures the alpha move and uses AI to choose the exit.  #mech/slow_reaction
  > it's more like 2 to 5 days actually.
  asset: commodities · horizon: days · testable: partly - holding period stated · confidence: high
  ^MT082-C05-2
- **Philip Engel Carlson** Supply constraints from weather or regional events create fear and price moves, which trend following can capture; this works in commodities and not in equities or rates, which explains the commodities-only focus.  #mech/slow_reaction
  > This fear sparks price movements and these movements is actually what we uh want to capture in our trend following model.
  indicator: price breakouts after supply shocks · asset: commodities · direction: long after upward shock, short after downward · horizon: days · conditions: Works where supply and demand are physically constrained · testable: partly - compare trend returns by asset class · confidence: high
  ^MT082-C05-3
- **Philip Engel Carlson** Calculo trades only the most liquid metals, agriculturals, softs and energies, which also lets it scale.  #mech/risk_management
  > we only do trade the liquid stuff.
  indicator: market liquidity · asset: commodities · conditions: Excludes small markets such as orange juice · testable: partly - liquidity filter · confidence: high
  ^MT082-C05-4

### C06
- **Moritz Seibert** Shorter-horizon traders are much more sensitive to market liquidity than slow trend followers, who do not need to trade daily.  #mech/risk_management
  > with your trading frequency you're absolutely much more sensitive to that
  indicator: liquidity · asset: commodities · horizon: days · testable: partly - cost and capacity by horizon · confidence: medium
  ^MT082-C06-1
- **Philip Engel Carlson** Entries are classical CTA breakouts and the advanced part is the post-entry risk management, which aims at low-volatility access to commodities.  #mech/slow_reaction
  > Basically we use only uh price patterns as our entry.
  indicator: price breakouts · asset: commodities · direction: long breakout up, short breakout down · horizon: days · testable: yes - breakout rules are testable · confidence: high
  ^MT082-C06-2
- **Philip Engel Carlson** Machine learning applied to risk management reduces volatility and gives a smoother return profile than plain trend following.  #mech/risk_management
  > commodities can be volatile and and it through the use of AI, we can sort out a lot of the volatility and create a more linary return profile.
  indicator: machine-learning exit signal · asset: commodities · horizon: days · testable: partly - compare with and without ML exit · confidence: medium
  ^MT082-C06-3
- **Philip Engel Carlson** A hurricane threat first adds a risk premium (the price jump), then the market waits on the storm path; the system gets signals from price momentum and candlesticks during this limbo.  #mech/overshoot
  > after this initial risk premium being put into the market, the market will look at the hurricane development
  indicator: price patterns after weather shocks · asset: commodities · horizon: days · testable: partly - event study of weather shocks · confidence: medium
  ^MT082-C06-4
- **Philip Engel Carlson** After a shock move the market often goes sideways, which is enough for the model to take profit and then re-enter the trend if it resumes.  #mech/overshoot
  > So quite often we do participate in these movements where the market uh stabilizes a bit and trades sideways and this is often enough for us to exit the positions capturing the alpha
  indicator: sideways consolidation after a spike · asset: commodities · direction: exit after spike, re-enter on resumption · horizon: days · testable: partly - rule testable · confidence: medium
  ^MT082-C06-5
- **Philip Engel Carlson** The system uses price only, with no weather input and no manual override of signals.  #mech/research_method
  > there's no manual input in regards to selecting signals.
  indicator: price only · asset: commodities · testable: no - process statement · confidence: high
  ^MT082-C06-6

### C07
- **Philip Engel Carlson** The model can be flat, partly long or partly short, with no mandatory allocation to any market or sector.  #mech/risk_management
  > we only want to participate in in real alpha periods
  indicator: position flexibility · asset: commodities · testable: partly - compare to always-invested · confidence: high
  ^MT082-C07-1
- **Philip Engel Carlson** About 75 to 80% of trades are closed by machine learning exits and the rest by classical stops and trailing stops.  #mech/risk_management
  > 75 80% of our trades is handled via the machine learning exits.
  indicator: stops vs ML exits · asset: commodities · horizon: days · testable: partly - exit mix reportable · confidence: high
  ^MT082-C07-2
- **Philip Engel Carlson** Each day the open trade's candlestick and momentum features are matched to a database of historical trades with known T+1 and T+2 outcomes, then classified as keep or eliminate.  #mech/research_method
  > when we take this new data put into our database, it finds a match that is as close to something it has seen before.
  indicator: nearest-neighbour matching on candlestick and momentum features · asset: commodities · direction: exit when matched history shows adverse outcome · horizon: days · conditions: Needs a large trade history · testable: yes - algorithm described · confidence: high
  ^MT082-C07-3
- **Philip Engel Carlson** Capturing parts of trends and avoiding counter-moves gives a smoother ride but not the whole trend, as classical longer-term CTAs do; ML uses daily bars.  #mech/risk_management
  > we try to capture bits and pieces of these existing trends and trying to vet out any counter moves along the way.
  indicator: daily bars · asset: commodities · horizon: days · conditions: Trade-off: smoother returns but misses the tail of trends · testable: partly - compare to long-horizon trend · confidence: high
  ^MT082-C07-4

### C08
- **Philip Engel Carlson** Entries are trend only with no mean reversion.  #mech/slow_reaction
  > We use trend following strategies to enter the markets. Trend only.
  asset: commodities · horizon: days · testable: yes · confidence: high
  ^MT082-C08-1
- **Philip Engel Carlson** Machine learning is not used for entry because predicting where the market moves is a guess; it is used only for exits, where it avoids learning noise about direction.  #mech/research_method
  > I do believe that trends have strength.
  asset: commodities · horizon: days · testable: partly - compare ML-entry vs ML-exit · confidence: high
  ^MT082-C08-2
- **Philip Engel Carlson** Using ML only as a risk-off element avoids the overfitting problem of price prediction models.  #mech/research_method
  > we actually only use it as a riskoff element which changes the picture quite a bit compared to trying to build a fully AI model that tries to predict the price targets.
  asset: commodities · horizon: days · testable: partly · confidence: high
  ^MT082-C08-3

### C09
- **Philip Engel Carlson** Machine learning exits are timed at the most liquid hours and are flags of possible correction, not firm predictions, so execution is done in liquid periods.  #mech/risk_management
  > timed towards the most liquid time in the US.
  indicator: time-of-day liquidity · asset: commodities · horizon: days · testable: partly - execution cost study · confidence: medium
  ^MT082-C09-1
- **Ola Hansen** The long-only Bloomberg Commodity Index had a 77-month, 38% drawdown from 2015 to 2020 and a further 22% drop after 2022, so a long/short strategy with similar returns and lower volatility is preferable.  #mech/risk_management
  > We had the two biggest one was a 77 months draw down between 15 and 20 where it fell 38%.
  indicator: Bloomberg Commodity Index drawdowns · asset: commodities · horizon: years · testable: yes - index history · confidence: high
  ^MT082-C09-2
- **Ola Hansen** Commodity strategy returns tend to be positive in bad equity months, lowering portfolio volatility.  #mech/risk_management
  > we had to have bad months for equities we quite often find that uh that there's actually some uh positive months coming in through the commodities.
  indicator: commodity strategy vs equity monthly returns · asset: multi · horizon: months · testable: yes - correlation in down months · confidence: low
  ^MT082-C09-3

### C10
- **Moritz Seibert** Commodities have no equity-like positive drift, so they should be traded both long and short.  #mech/risk_premium
  > commodities don't have the equity drift or anything like that.
  asset: commodities · direction: long and short · testable: partly - commodity risk premium debate · confidence: medium
  ^MT082-C10-1
- **Ola Hansen** Cocoa was not in the Bloomberg Commodity Index because of its size, so the index missed the cocoa rally, while natural gas, a member, dragged it down.  #mech/structural_shift _(time-bound view)_
  > because it's a relatively small market, is not a BCOM member.
  indicator: BCOM composition · asset: commodities · horizon: years · testable: yes - index membership · confidence: high
  ^MT082-C10-2
- **Ola Hansen** Index rebalancing in January forced sales of a winner whose weight had grown extreme (cocoa).  #mech/liquidity_flows _(time-bound view)_
  > there was a massive re rebalancing in in the when January came because the the percentage share of expos exposure to coco out of the total was uh had gone quite extreme
  indicator: index rebalancing · asset: commodities · horizon: weeks · testable: yes - rebalance data · confidence: medium
  ^MT082-C10-3
- **Ola Hansen** Smart-roll commodity ETFs have not outperformed the main total return indices.  #mech/research_method
  > I don't find them having been particularly successful uh they haven't really outperformed uh the uh the main uh total return in in the indices.
  indicator: smart-roll commodity ETFs · asset: commodities · horizon: years · testable: yes - ETF vs index returns · confidence: medium
  ^MT082-C10-4
- **Moritz Seibert** In contango, a short position earns roll yield (natural gas); Calculo benefited from the upward-sloping curve but does not roll monthly and is aware of seasonality.  #mech/risk_premium
  > you have been making money being short simply on the the role of the uh the role from a from a from a low to a high contract.
  indicator: commodity futures curve slope (contango) · asset: commodities · direction: short in contango · horizon: months · conditions: Applies in contango markets · testable: yes - roll yield is measurable · confidence: medium
  ^MT082-C10-5
- **Philip Engel Carlson** Calculo reports equity-like returns at two-thirds of stock index volatility since 2018, non-correlated and non-cyclical.  #mech/risk_management _(time-bound view)_
  > that we over the past seven years almost since inception has actually delivered equity-like returns at 2/3 of the volatility of uh the broad stock indices.
  indicator: fund track record · asset: commodities · horizon: years · conditions: Self-reported · testable: partly - track record claim, not verified · confidence: medium
  ^MT082-C10-6

