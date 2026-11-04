---
source_id: MT073
title: "How Alpha Hides in Plain Sight - Systematic Investor - Ep.362"
date: 2025-08-28
channel: "Top Traders Unplugged"
url: 
words: 12306
claims: 73
added_by_crosscheck: 3
corrections: 1
crosscheck: "opus cross-check"
speakers: ["Alan Dunne (host, sitting in for Niels, allocator/researcher)", "Yoav Git (guest co-host, quant CTA researcher, Cambridge)"]
tags: [source, layer0]
---
# How Alpha Hides in Plain Sight - Systematic Investor - Ep.362

**Speakers:** Alan Dunne (host, sitting in for Niels, allocator/researcher); Yoav Git (guest co-host, quant CTA researcher, Cambridge)

**Summary:** Systematic Investor ep. 362 (Aug 2025): Yoav Git discusses a futures-curve (spread) trend paper, COT-based evidence that trend is not at capacity, the Bank of England FX derivatives paper, and his blog on how CTAs fit with long-term capital-market-assumption allocators (Vanguard 30/70). Main conclusions: trade spreads only after dislocations create risk, speculator positioning shows no trend crowding, and long-horizon allocators are mean-reverting so systematic strategies complement them.

**Approach:** trend following, futures curve and spread trading, market structure, COT positioning, FX derivatives, asset allocation, capital market assumptions

**Cross-check completeness estimate of first read:** 0.95 - first reader covered nearly every idea (72 claims); only a cost figure, the CLS data source and the van Hemert FX-hedging reference were missed; one numeric misstatement on the Vanguard cut.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | nothing actionable: intro, holidays, comedy gig |
| C02 | 5 | fixed income trend difficulty, Japan yields, fiscal dominance, BlackRock hedge funds, CTA malaise |
| C03 | 5 | CTA performance, patience, trend as zero correlation; paper on curve trading intro |
| C04 | 5 | copper tariff dislocation, front vs back of curve, spread breakouts, static vs spread risk |
| C05 | 6 | sizing spreads, waiting for dislocation, trend vs carry/mean reversion in spreads |
| C06 | 5 | supply shocks and crack spreads, breakouts, residual volatility, LTCM analogy |
| C07 | 5 | risk-managed spread trading, currency basis, PCA factors of rates |
| C08 | 5 | mean-reverting PCA factors, speed, costs, using curves to select contracts |
| C09 | 5 | speculation in copper front curve, COT, trend capacity argument |
| C10 | 4 | COT loading on trend, no capacity evidence; FX market size |
| C11 | 3 | FX topography paper data, descriptive research approach |
| C12 | 2 | habitats of FX players along the curve, exposures |
| C13 | 3 | dealer risk, UK corporate hedging, concentration of dealers |
| C14 | 4 | spot vs derivative structure; Vanguard 70/30; allocator process and CTA exclusion |
| C15 | 3 | capital market assumptions, mean-reverting long-term allocators, Vanguard cut |
| C16 | 6 | allocator view, trend as tactical phasing, systematic strategies in optimisation |
| C17 | 3 | time horizons of CMA vs active traders, alpha as independent play |
| C18 | 1 | embedding systematic strategies like FX hedging and CTA; sign-off |

## Claims

### C02
- **Yoav Git** Trend following in fixed income has been difficult in 2025 because US yields oscillate indeterminately, while Japan shows a persistent climb and other markets show opposite drifts.  #mech/slow_reaction _(time-bound view)_
  > it has been a very difficult uh period for trend in fixed income
  indicator: trend signals in bond futures · asset: rates · horizon: months · conditions: range-bound US yields · testable: yes · confidence: high
  ^MT073-C02-1
- **Yoav Git** Japan's 10-year yield rose steadily from zero in 2022 to an all-time high in August 2025, a persistent trend benefiting trend followers.  #mech/slow_reaction _(time-bound view)_
  > they've started a long climb back in 2022 from zero now sitting at an all-time high last night
  indicator: Japan 10-year yield · asset: rates · direction: higher JGB yields · horizon: years · testable: yes · confidence: high
  ^MT073-C02-2
- **Alan Dunne** Fiscal dominance (monetary policy bending to fiscal needs at high debt) is becoming a market theme alongside rising Japanese yields.  #mech/fiscal_debt _(time-bound view)_
  > the idea that monetary policy will um kind of have to adapt to the fiscal stance you know when debt levels get so great
  indicator: long-end yields · asset: rates · direction: higher yields · horizon: years · conditions: high debt levels · testable: partly · confidence: medium
  ^MT073-C02-3
- **Alan Dunne** BlackRock recommended raising hedge fund allocations by 5%, reflecting a more volatile macro environment, though CTA allocators remain hesitant after poor H1 returns.  #mech/crowding_positioning _(time-bound view)_
  > recommending that investors increase their allocations to hedge funds by 5%
  indicator: hedge fund allocation · asset: multi · horizon: months · testable: no - recommendation · confidence: medium
  ^MT073-C02-4
- **Yoav Git** Investors hold off allocating to CTAs after six months of poor performance regardless of manager, even though the case for CTAs persists.  #mech/behavioral _(time-bound view)_
  > I think there is a general malaise in the CTA industry. Investors are waiting to see what's happening.
  indicator: CTA investor sentiment · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT073-C02-5

### C03
- **Yoav Git** The long-run reasons to hold CTAs are unchanged by a weak period.  #mech/risk_premium
  > alltime performance of CTAs, the reasons why they should invest in CTAs is that actually hasn't gone away at all
  asset: multi · horizon: years · testable: partly · confidence: high
  ^MT073-C03-1
- **Alan Dunne** As of late August 2025 the SG Trend index was down about 8.5% YTD and the SG CTA index nearly 7% down, with fixed income trends in Japan and Europe helping and FX/equities rangy.  #mech/slow_reaction _(time-bound view)_
  > year to date the trend index down 8 and a half% and the sock CTA index down just under 7%
  indicator: SG Trend index, SG CTA index · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT073-C03-2
- **Yoav Git** Judge trend following over long periods, not one to six months; it is painful like going down the stairs and up the elevator.  #mech/risk_management
  > it will be a mistake to look at at you know, one month performance, two months per even six month performance
  asset: multi · horizon: years · testable: partly · confidence: high
  ^MT073-C03-3
- **Yoav Git** Trend following offers zero correlation to the rest of a portfolio plus dynamic adaptation, a fundamental reason to hold it.  #mech/risk_premium
  > you're buying that that uh beautiful zero correlation to the um to the rest of the rest of your portfolio while you have a dynamic adjustment to market conditions
  indicator: correlation of trend to portfolio · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT073-C03-4
- **Yoav Git** A commodity is not one object: contracts for different delivery months (old crop vs new crop) differ by supply, demand, regulation, so curve points can be traded separately.  #mech/structural_shift
  > you can buy corn for delivery at different months and the different months may behave differently right
  indicator: futures curve by delivery month · asset: commodities · horizon: months · testable: yes · confidence: high
  ^MT073-C03-5

### C04
- **Yoav Git** Policy shocks such as copper tariffs create dislocations between adjacent contract spreads because one contract falls before and one after the tariff.  #mech/policy_reaction _(time-bound view)_
  > if I look at the difference between two deliveries two contracts Suddenly sometimes you get a dislocation uh and they behave differently
  indicator: copper calendar spread · asset: commodities · horizon: weeks · conditions: tariff announcements · testable: yes · confidence: high
  ^MT073-C04-1
- **Yoav Git** The front of the commodity curve is more volatile and driven by macro news, while long-dated prices follow long-term supply and demand.  #mech/structural_shift
  > the front of the curve is generally the one which is more volatile in the commodity business world and it is the one which is more affected by macronuse flow
  indicator: front vs deferred volatility · asset: commodities · testable: yes · confidence: high
  ^MT073-C04-2
- **Yoav Git** New participants crowd into the liquid front contract, increasing volume there.  #mech/crowding_positioning
  > when other players come onto the markets they tend to congregate where the the liquidity is and the front of the curve is where the liquidity is
  indicator: front-month volume · asset: commodities · horizon: years · testable: yes · confidence: high
  ^MT073-C04-3
- **Yoav Git** Calendar spreads show strong breakouts and reversals, and breakouts are violent, so a breakout rule fits spread trading.  #mech/slow_reaction
  > spreads exhibit strong breakouts and reversals and I like I like the what they say about breakouts because the um when spreads actually break do break out it's actually quite violent
  indicator: spread breakout · asset: commodities · direction: trade spread breakouts · horizon: days · testable: yes · confidence: medium
  ^MT073-C04-4
- **Yoav Git** Traditional CTAs hold roughly constant risk allocations per outright market, but this cannot be done for spreads.  #mech/risk_management
  > they allocate to each of the individual markets and that allocation is relatively static over time
  indicator: static risk allocation · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT073-C04-5

### C05
- **Yoav Git** Spread volatility is itself volatile, so targeting constant risk needs huge leverage and wipes you out in a dislocation (left-skewed).  #mech/risk_management
  > if you try to make this spread provide you with that risk you will have to leverage your position to such an extent that when a dislocation does happen you will be out of business
  indicator: spread volatility · asset: commodities · horizon: days · conditions: quiet spread regimes · testable: yes · confidence: high
  ^MT073-C05-1
- **Yoav Git** Only start trading a spread after a dislocation lifts its volatility to a minimum level, then size it dynamically.  #mech/risk_management
  > you have to wait until actually a dislocation happens you can't get into the trade first
  indicator: spread volatility threshold · asset: commodities · horizon: weeks · conditions: after a dislocation · testable: yes · confidence: high
  ^MT073-C05-2
- **Yoav Git** Allocating risk to transient risk factors (such as spreads) adds diversification because they are uncorrelated to the rest of the portfolio.  #mech/risk_premium
  > being able to allocate meaningful risk to risk factors that um rise and they are transient by nature is something which I think is quite important
  indicator: transient spread risk factors · asset: multi · horizon: weeks · testable: partly · confidence: medium
  ^MT073-C05-3
- **Alan Dunne** Most managers trade spreads for mean reversion/carry, not breakout trend.  #mech/research_method
  > a lot of managers trade spreads more from I suppose for the spread to revert to more mean reversion
  indicator: calendar spreads · asset: commodities · testable: yes · confidence: high
  ^MT073-C05-4
- **Yoav Git** Spread convergence follows cost of carry (interest, storage, convenience yield) and is slow, while dislocations arise when contracts are not substitutable.  #mech/risk_premium
  > the play for the convergence of these two things is is normally the carriage rate and it's a kind of a nice and slow process.
  indicator: cost of carry · asset: commodities · horizon: months · conditions: contracts fungible · testable: yes · confidence: high
  ^MT073-C05-5
- **Yoav Git** If two contracts are fungible they converge; a supply shock to one crop year breaks that and produces divergence.  #mech/structural_shift
  > if the two objects are funible then you will expect them to converge.
  indicator: spread convergence · asset: commodities · horizon: months · testable: yes · confidence: medium
  ^MT073-C05-6

### C06
- **Yoav Git** A real fundamental divergence (next crop shock) drives a short-lived trend in the spread.  #mech/slow_reaction
  > Okay. So then what you have is you have a real reason for that divergence between those spreads and that will create a a trend.
  indicator: corn old/new crop spread · asset: commodities · horizon: weeks · conditions: supply shock · testable: yes · confidence: high
  ^MT073-C06-1
- **Yoav Git** Refinery outages make crack spreads trend, a transient and diversifying risk factor unrelated to long-term oil.  #mech/structural_shift
  > unscheduled stoppage in those refineries, right? So suddenly suddenly what you have is you have uh that spread will start trending
  indicator: crack spread · asset: commodities · horizon: weeks · conditions: storms, outages · testable: yes · confidence: high
  ^MT073-C06-2
- **Yoav Git** Use breakout signals on spreads because a break signals a fundamental event.  #mech/slow_reaction
  > they use breakout rather than using sort of a smooth trading because you actually are looking for a breakout as an indication of something something fundamental happening there
  indicator: spread breakout signal · asset: commodities · horizon: days · testable: yes · confidence: medium
  ^MT073-C06-3
- **Yoav Git** Spread volatility is residual volatility after 90-98% correlation between legs, so it is tiny and needs 50x leverage to matter.  #mech/risk_management
  > But what they're looking for is like the residual volatility, the the difference in movement between the two.
  indicator: spread residual volatility · asset: commodities · testable: yes · confidence: high
  ^MT073-C06-4
- **Yoav Git** Leveraging a 2% residual-vol spread is the LTCM trap (on/off the run Treasuries); trade only when the spread becomes volatile.  #mech/risk_management
  > LTCM bumped up the risk profile by you know 50x 100x and then of course when those spreads we refuse to converge
  indicator: spread leverage · asset: rates · testable: yes · confidence: high
  ^MT073-C06-5

### C07
- **Yoav Git** After a structural break (tariff, refinery), spread volatility rises from about 2% to about 10% of leg vol, making it tradeable without much leverage.  #mech/risk_management
  > becomes 10% of the volatility and now it's interesting it's a it's actually a valid risk factor that you can trade with not too much leverage
  indicator: spread volatility share · asset: commodities · horizon: weeks · conditions: after a break · testable: yes · confidence: high
  ^MT073-C07-1
- **Yoav Git** Currency basis moves can trend when transient funding pressure arises (e.g., bond issuance in USD), so they are another transient factor to trade with strict risk rules.  #mech/liquidity_flows
  > a currency basis is the difference between uh funding funding in local currency versus the US
  indicator: cross-currency basis · asset: fx · horizon: weeks · conditions: funding pressure · testable: yes · confidence: medium
  ^MT073-C07-2
- **Yoav Git** Trade transient factors only while their volatility is sufficient, exit when it fades.  #mech/risk_management
  > the ability to say I'm going to wait until there is a sufficient risk to start trading it um and then I'm going to get out of this when when there isn't enough volatility
  indicator: volatility gating · asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT073-C07-3
- **Yoav Git** Making money from spreads is harder than from outrights because relative value is value-based rather than trend-based.  #mech/slow_reaction
  > relative value trades are called relative value because uh it's value rather than trend. So making money out of spreads is more difficult.
  asset: multi · testable: partly · confidence: medium
  ^MT073-C07-4
- **Yoav Git** In bond markets the top principal components trend very well and cover about 70% of risk, the middle ones still trend but smaller.  #mech/slow_reaction
  > maybe the first 25% of of PCA factors trend very well sort of then then we have like a 50% of the remaining uh PCA factors and they do trend
  indicator: PCA factors of bond markets · asset: rates · direction: trade top and middle PCA factors · testable: yes · confidence: medium
  ^MT073-C07-5

### C08
- **Yoav Git** The lowest PCA factors (pure RV trades) are strongly mean-reverting, not trending.  #mech/slow_reaction
  > they tend to actually move in the opposite direction. So they will tend to be uh actually very strongly mean reverting.
  indicator: bottom PCA factors · asset: rates · direction: avoid trend on bottom factors · testable: yes · confidence: medium
  ^MT073-C08-1
- **Yoav Git** Remove the smallest factors and overweight middle factors in a PCA-based trend system.  #mech/research_method
  > Or maybe you want to upweight the middle factors because although they are they are they they trend less
  indicator: PCA factor weighting · asset: rates · testable: yes · confidence: medium
  ^MT073-C08-2
- **Yoav Git** Spread trend should be traded faster than outright trend but not too fast because costs bite.  #mech/risk_management
  > fast but not as fast as you think
  indicator: spread trend speed · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT073-C08-3
- **Yoav Git** Spreads cost more per unit of risk since both legs trade, so fast spread trend may be uneconomic.  #mech/risk_management
  > the notional amount that I trade is higher and therefore my trading cost will be higher. So like per turnover the spread will be more expensive than trading outright.
  indicator: spread transaction cost · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT073-C08-4
- **Yoav Git** Use curve spreads to choose which contract to trade: if momentum wants to buy and the back is cheap, buy the back (supply/demand driven) rather than the front (macro driven).  #mech/risk_management
  > the back of the curve looks cheap while the front of the curve looks dear. If you if momentum wants to buy something then maybe you should buy the back.
  indicator: curve shape for contract selection · asset: commodities · direction: buy deferred contracts · horizon: weeks · testable: yes · confidence: medium
  ^MT073-C08-5
- **Yoav Git** Trading costs for slow outright trend are small, roughly 0.02-0.03 of Sharpe ratio, and slow trend is the dominant source of trend returns, which sets the cost benchmark that spread trading must beat.  #mech/research_method _(added by opus cross-check)_
  > if I'm trading the outright there's going to be a certain cost in sharper basis stuff. So maybe three two or three basis points of sharp okay so 002 of sharp
  indicator: transaction cost in Sharpe-ratio units · asset: commodities · horizon: months · conditions: slow outright trend vs faster spread trend · testable: yes - gross vs net Sharpe by speed and instrument · confidence: medium
  ^MT073-C08-X1

### C09
- **Yoav Git** Copper has become more speculative (CTAs, multistrats) at the front of the curve, seen in volume vs open interest and COT.  #mech/crowding_positioning
  > these days everybody is trading copper and as a result the copper has become sort of more speculative in nature right
  indicator: volume/open interest, COT in copper · asset: commodities · horizon: years · testable: yes · confidence: high
  ^MT073-C09-1
- **Yoav Git** Hedgers and producers dominate further out the curve, trade slowly, and give open interest with less volume, so contract dynamics differ along the curve.  #mech/liquidity_flows
  > they tend to trade more slowly so there's less volume there is more open interest
  indicator: stock vs flow along curve · asset: commodities · testable: yes · confidence: high
  ^MT073-C09-2
- **Alan Dunne** Where many risk-averse hedgers exist, speculators can earn a risk premium.  #mech/risk_premium
  > But if there's a lot of hedggers in a market, then there and they're risk averse, then in theory there's a there is a premium a risk.
  indicator: hedger/speculator mix · asset: commodities · testable: yes · confidence: medium
  ^MT073-C09-3
- **Yoav Git** Clients argue trend underperformed because too much money is in trend; Man's AUM argument says industry AUM is constant.  #mech/crowding_positioning
  > some an argument which comes up quite often is to say oh uh trend is at capacity.
  indicator: trend industry AUM · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT073-C09-4
- **Yoav Git** Industry AUM understates trend capital since QIS and multistrat pods also run trend.  #mech/crowding_positioning
  > Um the problem with this argument is that there is tons of trend being done at other places where you don't see it.
  indicator: hidden trend assets · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT073-C09-5

### C10
- **Yoav Git** Test crowding by regressing speculators' COT positions on trend signals; high beta would signal crowded trend.  #mech/research_method
  > if the industry was overly trend reliant then what you would see is you would see a good correlation yeah a beta between the speculators positioning in the cult report to your signal
  indicator: COT speculator positioning vs trend signal · asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT073-C10-1
- **Yoav Git** Speculators cut positions when volatility rises, a dominant effect now (volatility-based risk targeting).  #mech/risk_management
  > the speculators have become very sensitive to volatility. So the loading on changes in volatility i.e. if volatility goes up the it goes the speculators uh proportion goes down.
  indicator: speculator positioning vs volatility · asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT073-C10-2
- **Yoav Git** Loading on fast trend declined since the early 2000s while CTAs migrated to slow trend; slow trend loading did not rise, so the capacity argument is not supported.  #mech/crowding_positioning
  > What we don't see is we don't see like suddenly a huge rise or in fact any rise whatsoever in terms of the loading on on slow trend or mid-frequency trend in the data.
  indicator: COT loading on trend by speed · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT073-C10-3
- **Yoav Git** The FX market trades about 7.5 trillion daily (BIS 2022), dwarfing equities and including corporates, asset managers and funds.  #mech/liquidity_flows
  > the amount of daily trading in FX is something like 7.5 trillion
  indicator: BIS triennial survey · asset: fx · testable: yes · confidence: high
  ^MT073-C10-4

### C11
- **Yoav Git** A Bank of England-led paper (Topography of the FX derivative market) uses regulator-level non-anonymized London FX derivative data for 2015-2020.  #mech/research_method
  > They have 100 million transactions, millions of transactions in the London FX markets from 2015 to 2020. And it's non anonymized.
  indicator: London FX derivatives transaction data · asset: fx · testable: yes · confidence: high
  ^MT073-C11-1
- **Yoav Git** Describe data structure first before building predictive strategies; avoid overcomplicated models.  #mech/research_method
  > a lot of quans again rush into here's a trading strategy. Sit back just just look at the data. Let it tell you a story.
  asset: multi · testable: partly · confidence: high
  ^MT073-C11-2
- **Yoav Git** Understand the data before using machine learning on it.  #mech/research_method
  > it behooves us as corns rather than just shoving it into a machine to really understand what's going on
  asset: multi · testable: partly · confidence: high
  ^MT073-C11-3
- **Yoav Git** Few data sets show FX positioning; CLS, a major FX settlement provider, offers heavily anonymized flow data, which the regulator-level Bank of England data far exceeds in granularity.  #mech/research_method _(added by opus cross-check)_
  > there's uh CLS is one of the biggest providers they do settlement FX settlements and they offer some data which is very anonymized
  indicator: CLS FX settlement flow data · asset: fx · testable: partly - data availability statement · confidence: high
  ^MT073-C11-X1

### C12
- **Yoav Git** FX market makers hold risk in contracts up to one week; hedge funds and asset managers trade 1-3 months (IMM dates); corporates hold 2-3 year swaps, each in their own habitat along the curve.  #mech/liquidity_flows
  > most of it is up to one one week uh expiry right and and that's the most liquid part
  indicator: FX derivative maturity by participant · asset: fx · testable: yes · confidence: high
  ^MT073-C12-1
- **Alan Dunne** Hedge fund net FX exposures fluctuate widely, while dealers hold the opposite of hedgers.  #mech/crowding_positioning
  > the hedge funds uh specs their net exposures to the dollar euro and sterling fluctuate a lot
  indicator: net FX exposures by segment · asset: fx · horizon: weeks · testable: yes · confidence: medium
  ^MT073-C12-2

### C13
- **Yoav Git** UK corporates are structurally long sterling/short dollar from hedging, and dealers hold the opposite; US corporates are the unseen mirror position.  #mech/liquidity_flows
  > there's a structural short dollar for UK corporates right because they have they hedge their dollars back to the UK
  indicator: UK corporate FX hedging · asset: fx · horizon: years · testable: yes · confidence: medium
  ^MT073-C13-1
- **Yoav Git** Post-GFC dealers cannot hold large risk on their books, so risk is passed through to corporates and others in bonds, credit and FX.  #mech/liquidity_flows
  > the amount of risk which is available on the market that you are you are able to hold is actually not not not that great
  indicator: dealer risk capacity · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT073-C13-2
- **Yoav Git** The FX derivative market is star-shaped: the top five dealers and five market makers dominate, much more than 20 years ago.  #mech/structural_shift
  > the top five dealer and the top five market makers really dominate the everything
  indicator: dealer concentration · asset: fx · horizon: years · testable: yes · confidence: high
  ^MT073-C13-3

### C14
- **Yoav Git** FX spot is structured differently, with non-bank market makers, while derivatives are concentrated in few counterparties which may be a cause for concern.  #mech/structural_shift
  > the emergence of players like the the non-bank um market makers so like the XTX and the J Street
  indicator: FX spot vs derivative structure · asset: fx · testable: partly · confidence: medium
  ^MT073-C14-1
- **Alan Dunne** Vanguard recommends a 70/30 style allocation (bond-heavy, 30% equity per Yoav) despite BlackRock's hedge fund call.  #mech/behavioral _(time-bound view)_
  > Vanguard kind of going against the tide a little bit by suggesting they're suggesting 7030 is the optimal for the next decades
  indicator: Vanguard time-varying asset allocation model · asset: multi · horizon: years · testable: no · confidence: medium
  ^MT073-C14-2
- **Yoav Git** An allocator estimates the equity beta of each manager's P&L to track hidden equity exposure.  #mech/risk_management
  > we actually do try to figure out the the beta let's say the equity beta on each of the uh data sets and we fit the the P&L of each of uh the people that we allocate to
  indicator: manager P&L equity beta · asset: equities · horizon: months · testable: yes · confidence: medium
  ^MT073-C14-3
- **Yoav Git** Allocators cannot fit CTA positioning from P&L because CTAs change exposure too often, showing CTAs' lack of persistent correlation.  #mech/risk_management
  > we exclude you guys, we exclude CTAs because you guys change, you change your mind too too often
  indicator: CTA equity beta · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT073-C14-4

### C15
- **Yoav Git** The strategic equity-bond split, derived from 10-year capital market assumptions and a correlation matrix, is the allocator's key decision.  #mech/research_method
  > that's actually probably one of the most important decisions that you have to make about you know what's the proportion between equities and bonds
  indicator: capital market assumptions · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT073-C15-1
- **Yoav Git** Long-horizon CMA-based allocators are mean-reverting: after equities rise they cut expected return and underweight equity, taking the opposite side of trend.  #mech/behavioral
  > most most of these models are mean reverting by nature i.e. If equities go up, they will actually underweight equity.
  indicator: CMA-based allocation · asset: equities · direction: sell equities after rallies · horizon: months · testable: yes · confidence: high
  ^MT073-C15-2
- **Yoav Git** Vanguard cut its 10-year equity return forecast by half the June 2025 rally (10-11%), leading to a 30% equity / 70% bond allocation.  #mech/behavioral _(time-bound view)_
  > they only cut 50% of it. So we we they cut the expect long-term expectation to to equity by half a percent based on actually very short-term change in equities.
  indicator: Vanguard 10-year equity return forecast · asset: equities · direction: less equity · horizon: years · testable: yes · confidence: high
  **Correction (cross-check):** Wrong number: Vanguard cut its 10-year equity return expectation by about half a percentage point (about half of the roughly 1%/yr implied by the 10-11% June rally, from about 4.5%), not by half the rally itself. → After the 10-11% June 2025 equity rally Vanguard cut its 10-year US equity return assumption by about 0.5 percentage point (from roughly 4.5%), half the rally's per-year effect, and moved to about 30% equities / 70% bonds.
  ^MT073-C15-3

### C16
- **Yoav Git** Allocators dislike valuation-based models that have been underweight equity for years.  #mech/behavioral
  > we kind of don't like them because they they have been negative equity for years
  indicator: valuation-based long-term models · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT073-C16-1
- **Yoav Git** Selling equities after the June rally would have done poorly, as the S&P rose from 6.2k to 6.4k.  #mech/slow_reaction _(time-bound view)_
  > equity has been has been uh has been rising quite happily regardless of what Vanguard is saying
  indicator: S&P 500 · asset: equities · horizon: weeks · testable: yes · confidence: medium
  ^MT073-C16-2
- **Yoav Git** Long-horizon valuation metrics (Shiller PE, 10-year views) are only useful for very long horizons, not for tactical use.  #mech/research_method
  > all of these very long-term 10-year horizon things um uh all of these are uh maybe make sense if you're investing for 100 years
  indicator: Shiller PE · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT073-C16-3
- **Yoav Git** Trend can phase in or out a long-term allocation tactically, e.g. delay deallocating from equities while trend is strong.  #mech/slow_reaction
  > the role of trend not necessarily as a long-term but as a tactical as a long-term right but as a tactical way of you phasing in that long-term view
  indicator: trend as allocation overlay · asset: equities · horizon: months · testable: yes · confidence: medium
  ^MT073-C16-4
- **Yoav Git** Including systematic strategies in the optimization automatically adjusts the allocation as assumptions change.  #mech/risk_management
  > you will be able to create an optimal allocation over a much wider set of parameters
  indicator: systematic strategies in allocation · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT073-C16-5
- **Alan Dunne** A CTA allocation adds or removes equity exposure with the equity trend (long in bull, short in bear), a favorable portfolio effect.  #mech/slow_reaction
  > CTAs will modulate your overall equity exposure. So, if you have 50% equities and you have 20% CTA, you're going to pick up some more equity exposure in your CTA allocation
  indicator: CTA equity exposure · asset: equities · horizon: months · testable: yes · confidence: medium
  ^MT073-C16-6

### C17
- **Alan Dunne** Mean-variance frameworks were designed for assets, not for strategies that trade those same assets, creating a conceptual problem.  #mech/research_method
  > now we got the we're adding strategies such as CTA which are trading some of the assets that you're diversifying
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT073-C17-1
- **Yoav Git** Active traders operate at a three-month horizon, invisible to 10-year allocators, which is why they are uncorrelated and long-term allocators should not worry about their positioning.  #mech/risk_premium
  > they are playing in a different time horizon than you they're playing at the three-month horizon
  indicator: time horizon · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT073-C17-2
- **Yoav Git** Treat CTA/systematic alpha as independent of the CMA allocation, using its positioning only to modulate small tactical changes.  #mech/risk_management
  > in terms of alpha, you just think of it as almost an independent play
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT073-C17-3

### C18
- **Yoav Git** Allocators already embed systematic strategies such as FX hedging and could embed trend as another tool.  #mech/risk_management
  > some systematic strategies like FX hedging are part of the way that you embed are embedded into your process
  indicator: systematic FX hedge · asset: fx · horizon: years · testable: partly · confidence: medium
  ^MT073-C18-1
- **Yoav Git** An allocator with structural foreign-currency exposure (e.g. an Australian investor holding USD assets) should hedge it with a systematic rule; a van Hemert paper studies the best ways to hedge FX exposure, a simple model for embedding systematic strategies such as trend into allocation.  #mech/risk_management _(added by opus cross-check)_
  > there's a great paper by van Hemtt um about the best ways to hedge FX exposure
  indicator: systematic FX hedge ratio rules · asset: fx · horizon: months · conditions: investors with structural FX exposure · testable: yes - compare hedging rules historically · confidence: medium
  ^MT073-C18-X1

