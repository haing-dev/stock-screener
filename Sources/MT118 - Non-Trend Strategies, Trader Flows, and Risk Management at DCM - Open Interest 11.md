---
source_id: MT118
title: "Non-Trend Strategies, Trader Flows, and Risk Management at DCM - Open Interest 11"
date: 2024-12-02
channel: "Top Traders Unplugged"
url: 
words: 9017
claims: 44
added_by_crosscheck: 11
corrections: 4
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Jerome Callo (guest, founder DCM Systematic, ex-BlueTrend)", "Moritz Seibert (host, Open Interest series)"]
tags: [source, layer0]
---
# Non-Trend Strategies, Trader Flows, and Risk Management at DCM - Open Interest 11

**Speakers:** Jerome Callo (guest, founder DCM Systematic, ex-BlueTrend); Moritz Seibert (host, Open Interest series)

**Summary:** Open Interest ep. 11 with DCM Systematic: a 25+ model non-trend multi-strategy fund built around behavioural flow anticipation (term structure, month end, shock overshoot, CTA positioning), relative value, and slow macro/cross-asset models, with proactive scenario risk management and a never-short-VIX rule. Sceptical that machine learning transfers directly to daily financial data.

**Approach:** non-trend CTA, behavioural flows, relative value, fast mean reversion, volatility, risk management, machine learning

**Cross-check completeness estimate of first read:** 0.81 - first reader captured the main design ideas (flow anticipation, term structure, shock overshoot, FX three-factor residuals, never short VIX, scenario risk, ML limits); missed the allocator-role and trend-blend exchange, role-based model retention, VIX asymmetry, hedging overlay status, cross-asset lead-lag motivation, persistence counterpoint and three speaker attributions.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | teaser on risk system, intros, guest background (DCM Systematic, ex-BlueTrend) |
| C02 | 2 | why non-trend: orthogonal diversifier to CTA allocations; markets as supply/demand not just time series |
| C03 | 2 | three model families: behavioural flows, relative value, macro; anticipating carry traders via term structure |
| C04 | 4 | behavioural models holding 5-10 days; shock impulse overshoot models; risk parity de-risking flows |
| C05 | 3 | August 2024 yen carry unwind; consensus risk across 25 models and portfolio overlay; end-of-month flow effects |
| C06 | 3 | CTA positioning vs CFTC data; relative value; fast mean reversion on residuals of three-factor G10 FX model |
| C07 | 2 | stat-arb residuals; WTI vs Brent spread via term structure; limited neutrality |
| C08 | 2 | never short VIX, long vol bias; risk system uses stylised scenarios (Volmageddon) |
| C09 | 4 | proactive vs reactive risk; VIX asymmetry after Volmageddon; vol targeting acts as take-profit; retail short vol convexity |
| C10 | 3 | portfolio hedging research; macro bucket: slow inflation signals; FX carry risk-off neutralisation; ~19 independent degrees of freedom in 75 futures |
| C11 | 2 | cross-asset proxy for Brent via FX; 98% automation; ML role intro |
| C12 | 3 | why ML/LLMs struggle in finance: noisy learned signals, limited data, weak signal-to-noise, non-stationarity |
| C13 | 2 | sticky month-end effects vs decayed GSCI roll premium; moving target; outro |

## Claims

### C01
- **Jerome Callo** Risk management should ensure that no scenario can put the fund out of business, by listing what could go wrong (carry reversal, taper tantrum, oil shock) and adding each to the risk system.  #mech/risk_management
  > at any point in time you cannot be in a position that would put you out of business right you can control that
  indicator: scenario-based risk system · asset: multi · testable: partly - stress scenarios can be defined and tested · confidence: high
  ^MT118-C01-1

### C02
- **Jerome Callo** Mathematical models simplify a complex reality driven by supply, demand and constraints, so a single momentum driver is not enough and other approaches (relative value, behavioural models) can add return.  #mech/structural_shift
  > markets are not just a Time series but they are you know Supply and demands and all all kind of con straints
  indicator: multi-driver models beyond momentum · asset: multi · testable: partly - framework · confidence: high
  ^MT118-C02-1
- **Jerome Callo** DCM deliberately avoids trend signals so its program is orthogonal to the CTA index and sits next to trend allocations in a broader portfolio.  #mech/risk_management
  > we should not overlap too much with uh Trend following programs because that part of the space is well covered by large Market participants
  indicator: non-trend diversified strategy · asset: multi · testable: yes - measure correlation to SG CTA index · confidence: high
  ^MT118-C02-2
- **Moritz Seibert** Adding a trend-following component to a 25-model non-trend book would probably still raise risk-adjusted returns, even though correlation to trend followers would rise, because trend has a positive expected return and diversifies the models.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > it would probably still improve the risk adjusted returns of the portfolio right you would have a higher correlation than as a result to Trend following
  indicator: trend model added to a multi-strategy book · asset: multi · direction: add trend to the book · conditions: at the cost of higher correlation to CTA indices · testable: yes - backtest the blend · confidence: medium
  ^MT118-C02-X1

### C03
- **Jerome Callo** It may be easier to forecast the positioning of large systematic participants (carry, value, momentum, risk parity, trend) than to forecast the market, because they cannot unwind large positions quickly.  #mech/crowding_positioning
  > is it easier to forast the market directly or to forecast certain Market participants that are using certain strategies
  indicator: forecast of other participants' positioning · asset: multi · direction: trade ahead of or against flows · horizon: days · conditions: large managers need days to unwind · testable: partly - needs proxies for participants' positions · confidence: high
  ^MT118-C03-1
- **Jerome Callo** Term-structure slope across futures lets one anticipate carry-trader repositioning, since a market does not flip between contango and backwardation overnight; models gauge the state and its evolution over a five to 10 day horizon.  #mech/crowding_positioning
  > looking at the term structure and uh typically trying to anticipate carry Traders while looking at the slope of ter structures on many instruments
  indicator: futures term-structure slope (contango/backwardation) · asset: multi · direction: trade the expected carry-trader flow · horizon: days · conditions: initially worked in FX and spread to other asset classes · testable: yes - term-structure slope signal · confidence: high
  ^MT118-C03-2
- **Jerome Callo** The fund concedes that trend following has a positive expected return and that an optimal blend with it exists, but sees choosing that blend as the allocator's job; the fund's own role is to be non-overlapping so the allocator is not doubling up on what they already hold.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > we we think that's more the the role of of or the mission of of the allocator than our own to to do that
  asset: multi · testable: no - product positioning · confidence: high
  ^MT118-C03-X1
- **Jerome Callo** The term-structure carry-trader anticipation signal, first found in FX, worked across many other asset classes with only risk-system adjustments, which gave confidence that it is a genuine principle and not a narrow data-mined result.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > we expanded that to the the other asset classes and what we saw is that the same principle perhaps with some adjustment in terms of the risk system was was working uh pretty well
  indicator: futures term-structure slope across asset classes · asset: multi · horizon: days · testable: yes - signal performance by asset class · confidence: medium
  ^MT118-C03-X2

### C04
- **Jerome Callo** A behavioural flow-anticipation model must be about twice as fast as the flow it tries to anticipate, giving a 5 to 10 day holding period and very low correlation to CTA indices.  #mech/crowding_positioning
  > give or take twice as fast as the thing you're trying to anticipate
  indicator: holding period 5 to 10 days · asset: multi · horizon: days · testable: yes - holding-period design · confidence: medium
  ^MT118-C04-1
- **Jerome Callo** After a large (two-sigma) shock, markets tend to overshoot and then normalise within about a week rather than continue, so shock impulse models fade the shock.  #mech/overshoot
  > what follows of a large shock like a Sigma shock on the commodity markets what do you see after that
  indicator: two-sigma price shock in commodities · asset: commodities · direction: fade the shock · horizon: days · testable: yes - event study · confidence: medium
  ^MT118-C04-2
- **Moritz Seibert** After a sharp equity fall, risk-parity and vol-control funds must cut exposure as prices fall and volatility rises, creating selling flow that can be exploited for a few days.  #mech/liquidity_flows
  > billions of risk parity and Vault control trades sitting there that now need to get drisk because they're still long
  indicator: two-sigma S&P 500 drop · asset: equities · direction: short the flow then buy back · horizon: days · conditions: vol-targeting funds long going into the shock · testable: yes - event study after sigma shocks · confidence: medium
  ^MT118-C04-3
- **Jerome Callo** The shock-reversal model is run market-neutral across equity indices to limit directional risk, while other models handle vol spikes with long-volatility positioning.  #mech/risk_management
  > we have an implementation of that principle that would try to keep a market neutrality across different indices
  indicator: cross-index market neutral overlay · asset: equities · horizon: days · testable: partly - design · confidence: medium
  ^MT118-C04-4

### C05
- **Jerome Callo** With 25+ models the portfolio can end up with all models pointing the same way (e.g. the August 2024 yen carry unwind), so a portfolio-level overlay should cap aggregate directional, factor (carry) or risk-on exposure.  #mech/crowding_positioning _(time-bound view)_
  > it can happen that at time they are in a consensus view on on something right
  indicator: portfolio overlay on aggregate positioning · asset: multi · direction: cap aligned exposures · horizon: days · conditions: when models are in consensus · testable: yes - aggregate exposure cap testable · confidence: high
  **Correction (cross-check):** Overstated: Jerome says that in the August 2024 unwind different anticipation models gave different results and the overall outcome was difficult; model consensus is raised as a general risk that can occur with 25+ models, not as what happened in August. → With 25+ models there is a risk that models reach a consensus view and the portfolio becomes exposed to a narrow set of trades; after a difficult August 2024 yen carry unwind (models gave mixed results), DCM is researching a portfolio overlay that looks at all positioning and can cap aggregate direct, factor (carry) or risk-on exposure.
  ^MT118-C05-1
- **Jerome Callo** End-of-month flow effects persist because large pools of capital rebalance on a monthly schedule, even though the inefficiency is documented.  #mech/seasonality
  > I tend to be surprised still by the end of month effects
  indicator: month-end calendar effect · asset: multi · horizon: days · testable: yes - calendar effect study · confidence: medium
  **Correction (cross-check):** Wrong speaker: the reflection that month-end effects persist because large pools of capital run on a monthly schedule is the host's comment closing the behavioural bucket, not Jerome Callo's. → Moritz Seibert (host) says he is still surprised that month-end effects persist despite academic papers, because humans and large pools of capital like to run on a monthly schedule and keep trading at month end because that is how it has always been done.
  ^MT118-C05-2
- **Moritz Seibert** Risk premia, factor and bank QIS strategies trade billions on rules and leave predictable footprints in prices that can be exploited.  #mech/crowding_positioning
  > all of that leaves um skit marks in the markets which which you can exploit
  indicator: footprints of QIS/risk premia flows · asset: multi · horizon: days · testable: partly - footprints hard to measure · confidence: medium
  ^MT118-C05-3
- **Jerome Callo** A bad episode (the August 2024 yen carry unwind) is treated as a data point to improve the risk system, with changes made through balanced discussion with the team rather than as a reaction to the last loss.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > it's always very useful to have this kind of negative data points because that's essentially where you can potentially improve the the risk system
  indicator: drawdown episodes as research input · asset: multi · conditions: avoid changing the system just to avoid the last pain · testable: no - process statement · confidence: medium
  ^MT118-C05-X1

### C06
- **Jerome Callo** Scaling estimated trend and carry positioning to the whole CTA industry and comparing with CFTC net speculator/hedger positions shows how big crowded positions are, and the best opportunities arise when an over-traded position must unwind.  #mech/crowding_positioning
  > you can have a a decent idea of okay how much do they represent
  indicator: estimated CTA positioning vs CFTC commitments · asset: multi · direction: trade against crowded unwind · horizon: weeks · conditions: concentrated or over-traded positions · testable: yes - CFTC data, CTA position estimate · confidence: medium
  ^MT118-C06-1
- **Jerome Callo** G10 FX returns versus USD are about 80 to 90% explained by three stable factors (all-vs-dollar, carry, Europe vs rest), a rare stationary stylised fact.  #mech/structural_shift
  > you can explain L up to 80 90% of the variant um using a three Factor model
  indicator: three-factor model of G10 FX returns (dollar, carry, Europe) · asset: fx · horizon: days · testable: yes - PCA of G10 FX returns · confidence: high
  ^MT118-C06-2
- **Jerome Callo** After neutralising the known FX factors, the 10 to 15% idiosyncratic residuals are short-lived and mean revert over roughly 10 to 20 days, supporting a fast mean-reversion strategy.  #mech/overshoot
  > we have to play with the 10 15 person left of unexplained variance which is anything that is more ideosyncratic to a certain currency
  indicator: FX residual after factor neutralisation · asset: fx · direction: fade residual · horizon: days · testable: yes - residual mean reversion test · confidence: high
  ^MT118-C06-3
- **Jerome Callo** Relative value is built either as pair spreads (Brent vs WTI, soybean oil vs soybean meal) or as larger baskets (FX, grains) with zero or controlled net exposure.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > can be a spread like an instrument versus another like Brands versus WTI or you know something like soy oil versus soy meal or it can be a larger basket with a zero net exposure
  indicator: Brent-WTI spread; soy oil-soy meal spread; FX and grain baskets · asset: commodities · conditions: net exposure zero or controlled · testable: yes - spread and basket backtests · confidence: high
  ^MT118-C06-X1

### C07
- **Jerome Callo** Strictly market-neutral relative value (e.g. WTI vs Brent) forces overtrading or excessive leverage, so DCM allows slack and derives positions from term structure with a limited directional exposure.  #mech/risk_management
  > if you impose a very strict Market neutrality there is some kind of overtrading happening or you have to leverage too much
  indicator: WTI-Brent spread, term structure · asset: commodities · horizon: days · conditions: highly correlated pairs have little spread volatility · testable: partly - design choice · confidence: medium
  ^MT118-C07-1
- **Moritz Seibert** Pairing the steeper-backwardation contract with its neighbour neutralises spot risk while collecting roll-down yield, an RV carry construction.  #mech/risk_premium
  > you what you can do is almost neutralize the the spot return risk using Brands to to offset whatever exposure you have to WTI spots
  indicator: roll yield, term-structure slope · asset: commodities · direction: long steeper backwardation, offset spot with the other · horizon: weeks · testable: yes - roll-yield spread backtest · confidence: medium
  **Correction (cross-check):** Likely wrong speaker: the host only offers the hypothetical of WTI in steeper backwardation than Brent; the roll-down and spot-risk neutralisation argument ('your example, that's a great setup') is Jerome Callo's reply. → Jerome Callo says that with WTI in steeper backwardation than Brent, one can separate carry and spot components, offset WTI spot exposure with Brent and still collect the WTI roll-down yield, keeping an offsetting Brent position purely as a risk neutraliser.
  ^MT118-C07-2

### C08
- **Jerome Callo** The program never holds a net short VIX position, because its role is to provide diversification in drawdowns; it uses beta-adjusted VIX curve spreads and a fast model that goes long VIX when hedging demand rises.  #mech/risk_management
  > would um completely forbid the system the program to have a net short positioning on vix
  indicator: VIX futures curve; short-dated implied vol hedging demand · asset: equities · direction: long VIX in shock risk; never net short · horizon: days · testable: yes - rule and curve signals · confidence: high
  ^MT118-C08-1
- **Jerome Callo** Risk management should be proactive using stylised scenarios (e.g. Volmageddon shape: front VIX months hit most) injected into the optimiser as a loss constraint, rather than only scaling after realised volatility.  #mech/risk_management
  > what could go spectacularly wrong with a certain asset class
  indicator: scenario-based loss constraint in optimiser · asset: equities · testable: yes - scenario stress in the solver · confidence: high
  ^MT118-C08-2
- **Jerome Callo** Hedging-role models (such as long-VIX shock models) can produce no returns for years and have false alarms, yet are kept because their function is protection in shocks, so models are judged by role in the portfolio, not stand-alone return.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > we can see certain models producing no returns for years and years but we know their function we know their role we we know we want to have them
  indicator: long-volatility shock models · asset: multi · horizon: years · conditions: when the model's role is diversification in drawdowns · testable: partly - role-based evaluation needs a conditional return test · confidence: high
  ^MT118-C08-X1

### C09
- **Moritz Seibert** Proactive risk management stress-tests current positioning against past scenarios such as Volmageddon, while reactive risk management adjusts positions after the fact.  #mech/risk_management
  > proactive and reactive risk management
  indicator: scenario replay / stress test · asset: multi · testable: yes - stress test of current positions · confidence: high
  ^MT118-C09-1
- **Jerome Callo** On 6 Feb 2018 (Volmageddon) the DCM program, long the front of the VIX curve, still netted about +3 to +4% after giving some back the next day.  #mech/risk_management _(time-bound view)_
  > the net pnl on that was plus three or plus 4% actually
  indicator: long front VIX / short back VIX curve position · asset: equities · direction: long front vix · horizon: days · testable: yes - event P&L · confidence: high
  ^MT118-C09-2
- **Jerome Callo** Volatility-based risk management naturally cuts exposure after large gains (as in March 2020), working like automatic profit-taking and protecting capital.  #mech/risk_management _(time-bound view)_
  > the book kind got got really reduced in exposure for couple of months or so and indeed um saved Capital saved the gains
  indicator: volatility targeting after shocks · asset: multi · horizon: months · conditions: after volatility spikes · testable: yes - exposure vs realised vol after shocks · confidence: medium
  ^MT118-C09-3
- **Moritz Seibert** Many retail and other traders sit in short-volatility trades, so volatility shocks force liquidation and leave an exploitable convex footprint.  #mech/crowding_positioning
  > there are many Traders including retail Traders all around the world Expos exposed to short volatility trades
  indicator: short-volatility crowding · asset: equities · direction: long volatility · horizon: days · testable: partly - positioning data limited · confidence: medium
  **Correction (cross-check):** Wrong speaker: the passage about retail and other traders in short-volatility trades, the painful unrealised losses forcing them out and the added convexity follows 'we came back and made more' and is Jerome Callo's reasoning, not the host's. → Jerome Callo says the volatility spectrum may leave a larger exploitable footprint than any other market because many traders, including retail, are exposed to short-volatility trades; shocks make unrealised losses painful, force them out and add convexity.
  ^MT118-C09-4
- **Moritz Seibert** VIX price action is asymmetric: it jumps up fast and fades gradually, so a long-volatility position can monetise the spike and a volatility-targeted book that de-risks after the gain keeps the profit.  #mech/overshoot _(added by sonnet-xhigh cross-check)_
  > it can you know jump up very fast but there's typically I would believe a a more gradual Fade Out of of of the action
  indicator: VIX spike and decay profile · asset: multi · direction: long volatility into shocks, reduce after the spike · horizon: days · conditions: after volatility shocks · testable: yes - VIX event study · confidence: medium
  ^MT118-C09-X1

### C10
- **Jerome Callo** Macro models use inflation from CPI prints and from an in-house real-time nowcast built from equity sectors, giving holding periods of a month to a couple of months in fixed income and FX.  #mech/policy_reaction
  > slower signals that are typically used on fixed income or FX uh thinking of inflation for instance
  indicator: inflation CPI and nowcast from equity sectors · asset: rates · horizon: months · testable: yes - nowcast replicable · confidence: medium
  ^MT118-C10-1
- **Jerome Callo** FX carry loses in equity risk-off shocks, so a regression-based risk-off factor is included in the risk system and neutralised in FX models.  #mech/risk_management
  > a carry trade in effects would be hurt when there is a shock on the S&P 500
  indicator: FX carry sensitivity to S&P 500 shocks · asset: fx · direction: neutralise risk-off exposure · horizon: days · testable: yes - regression beta to equity shocks · confidence: high
  ^MT118-C10-2
- **Jerome Callo** A universe of about 75 futures contains only about 19 independent degrees of freedom, a compression that has grown since 2008 as markets became globally linked and liquidated together.  #mech/structural_shift _(time-bound view)_
  > how many independent degrees of freedom do I really have in that in that pack you see it's more than it's more like 20 we've done the exercise I think couple of weeks ago and it was 19
  indicator: effective number of independent bets (PCA) in 75 futures · asset: multi · horizon: years · testable: yes - PCA of returns · confidence: high
  ^MT118-C10-3
- **Jerome Callo** Each of the 25 models neutralises certain factors locally (US dollar carry, yield-curve level), but there is as yet no portfolio-level systematic hedging overlay; building one with an overview of the whole portfolio is the next research step.  #mech/risk_management _(added by sonnet-xhigh cross-check, time-bound view)_
  > up to now something very local and the next step um hopefully this here is to have the full overview of the portfolio with some hedging trades coming up there
  indicator: factor neutralisation inside models; portfolio hedge overlay · asset: multi · testable: no - research agenda · confidence: medium
  ^MT118-C10-X1
- **Jerome Callo** Rather than treating the compression to about 19 independent bets as only bad for diversification, DCM uses it to build cross-asset lead-lag models that exploit linked markets, since globalised flows make markets move together.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > more what we we call cross asset models which is uh lead lag relationships between different asset classes
  indicator: lead-lag between asset classes · asset: multi · horizon: days · conditions: markets liquidated and traded together after 2008 · testable: yes - lead-lag regressions · confidence: medium
  ^MT118-C10-X2

### C11
- **Jerome Callo** A proxy for Brent built from currency pairs by robust regression (correlation about 0.5-0.6) lets a behavioural signal on Brent be traded through an FX basket, transferring signals across asset classes.  #mech/new
  > let's try to get the best proxy of Brands using a bunch of currency pairs using you know some kind of robust regression techniques
  indicator: Brent proxy from FX pairs via robust regression · asset: commodities · horizon: days · conditions: proxy correlation about 0.56 · testable: yes - regression proxy and signal transfer · confidence: medium
  ^MT118-C11-1
- **Jerome Callo** Execution is 98% automated with pre-trade previews and manual send but no discretionary modification, with a human monitoring the process.  #mech/risk_management
  > I would call that 98% automated in our case
  asset: multi · testable: no - operational · confidence: high
  ^MT118-C11-2

### C12
- **Jerome Callo** Machine-learning models fitted to daily data usually recover a noisier version of known signals (risk premium, carry, momentum), so they add little beyond hand-built versions; higher-frequency data is more promising.  #mech/research_method
  > noisy version of something we know of like okay it's a risk premium it's a a car trade it's a momentum signal
  indicator: machine learning on daily data · asset: multi · horizon: days · conditions: works better with minute-bar data · testable: yes - compare learned vs engineered signal · confidence: medium
  ^MT118-C12-1
- **Jerome Callo** Financial data has far fewer observations than the parameters of modern AI models, and signal-to-noise is weak (e.g. an earnings surprise offset by a Fed cut), so models cannot disentangle effects.  #mech/research_method
  > in in finance we we don't have so much data
  indicator: sample size and signal-to-noise for ML · asset: multi · testable: partly - statistical argument · confidence: high
  ^MT118-C12-2
- **Jerome Callo** Markets lack stationarity because participants change behaviour and arbitrage away patterns, so patterns from 10 years ago may no longer hold, unlike protein folding rules.  #mech/structural_shift
  > participants are changing the behaviors all the time
  indicator: non-stationarity of market patterns · asset: multi · horizon: years · testable: partly - out-of-sample decay · confidence: high
  ^MT118-C12-3

### C13
- **Moritz Seibert** The GSCI and DJ-UBS commodity index roll window (business days 5 to 9) once paid a large liquidity premium that has largely decayed as investors moved to smarter index implementations spreading roll across the curve.  #mech/liquidity_flows
  > massive liquidity premium associated with um the earlier versions of the S&P gsci commodity index providing liquidity to that essentially roll window of business day 5 to9
  indicator: GSCI roll window, business days 5 to 9 · asset: commodities · horizon: days · conditions: decayed after investors adopted smarter indices · testable: yes - roll window return study · confidence: high
  ^MT118-C13-1
- **Moritz Seibert** Month-end effects are sticky because humans run month-end accounting and portfolio adjustments, unlike other anomalies that decay once published.  #mech/behavioral
  > it is human beings that run end of month accounting um and portfolio adjustments
  indicator: month-end flow · asset: multi · horizon: days · testable: yes - calendar effect · confidence: medium
  ^MT118-C13-2
- **Jerome Callo** Non-stationarity is not universal: some behavioural flow patterns such as month-end rebalancing have persisted for 20-30 years, so each pattern must be judged on its own persistence rather than assuming all patterns decay.  #mech/seasonality _(added by sonnet-xhigh cross-check)_
  > mentioned the end of months rebalancing which is was there 20 30 years ago and still is there so so you can't really make a generalization of of of everything
  indicator: month-end rebalancing effect · asset: multi · horizon: years · conditions: patterns driven by institutional calendars persist; patterns that are publicly arbitraged can decay · testable: yes - long-sample test of month-end effect · confidence: medium
  ^MT118-C13-X1
- **Jerome Callo** Because market participants and structure keep changing, the fund treats research as a continuous process and expects its model set to have new components and removed ones over time.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > so that's why we you know stay very focused on research and we see it as a continuous process
  asset: multi · horizon: years · testable: no - process statement · confidence: high
  ^MT118-C13-X2

