---
source_id: MT009
title: "AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419"
date: 2026-09-29
channel: "Top Traders Unplugged"
url: 
words: 11744
claims: 59
added_by_opus: 5
corrections: 2
crosscheck: "opus cross-check"
speakers: ["Nick Palus [caption spelling] (guest, quantitative strategies researcher, Goldman Sachs)", "Alan Dunne (guest host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419

**Speakers:** Nick Palus [caption spelling] (guest, quantitative strategies researcher, Goldman Sachs); Alan Dunne (guest host, Top Traders Unplugged)

**Summary:** Top Traders Unplugged Ep.419 (Sept 2026): record 2026 trend-following gains from short bonds, a Goldman chart of 45% negative-beta S&P stocks, and a review of an Alpha Architect VIX-dependent look-back paper that finds no edge over a static 10-month window. Second half reviews Andrew Ang's multi-agent AI asset allocation paper, its look-ahead, reproducibility and monoculture issues.

**Approach:** trend following, volatility scaling, AI agents, portfolio construction, backtest bias

**Opus completeness estimate of first read:** 0.90 - thorough first read; missed the front-end interpretation of the yield rise, the consensus-forecast miss, the cross-sectional vs time-series caveat, the trend-timing verdict and the vintage-model fix; one wrong direction (signal strength) and one wrong speaker

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | intro; Goldman chart of negative-beta S&P 500 stocks, AI mini-index |
| C02 | 3 | dispersion, yield debate, linear vs complex market reaction |
| C03 | 5 | point-in-time uncertainty, September 2026 CTA performance, rates and 60/40 |
| C04 | 4 | rate contribution, yield range history, bond signal strength |
| C05 | 3 | equity/commodity months, rate story, Alpha Architect VIX-lookback paper setup |
| C06 | 3 | paper design details and results |
| C07 | 5 | costs, trigger power, vol scaling approach |
| C08 | 3 | regime classification, complementary strategies, speed at turning points |
| C09 | 3 | false positives, V-shapes, intro to Ang agentic AI paper |
| C10 | 4 | agent pipeline: macro agent, asset-class agents, portfolio agents |
| C11 | 3 | portfolio method menu, researcher and adversarial agents, voting and scoring |
| C12 | 3 | CIO agent, five design principles, March 2026 results |
| C13 | 4 | 44% equity allocation, diversify under unclear regime, LLM backtest bias |
| C14 | 3 | look-ahead, non-determinism, monoculture risk |
| C15 | 3 | mapping the agent workflow to trend following |
| C16 | 2 | multiple objectives, human bandwidth, AI-run products |
| C17 | 1 | auditability and outro, disclaimer |

## Claims

### C01
- **Nick Palus (caption spelling)** About 45% of S&P 500 stocks have a negative 3-month beta to the index versus just under 20% at the dot-com peak (Goldman Sachs chart).  #mech/crowding_positioning _(time-bound view)_
  > about half of the stocks in S&P 500 have a negative beta to the index
  indicator: share of S&P 500 stocks with negative 3m beta · asset: equities · horizon: months · conditions: Cap-weighted index with narrow leadership · testable: yes - computable from stock returns · confidence: high
  ^MT009-C01-1
- **Nick Palus (caption spelling)** AI-stock dominance forms a mini-index within the S&P 500 and the rest decouple, which is clustering and concentration.  #mech/crowding_positioning _(time-bound view)_
  > The AI dominance um is effectively building its own kind of mini index within the index and all the rest are becoming less correlated to it
  indicator: S&P 500 concentration · asset: equities · horizon: months · testable: yes · confidence: medium
  ^MT009-C01-2

### C02
- **Nick Palus (caption spelling)** Equity decoupling creates dispersion opportunities and some argue for long-correlation positions.  #mech/crowding_positioning _(time-bound view)_
  > this decoupling in the equity space is creating opportunities for dispersion some people talk about you know going long correlation
  indicator: dispersion / implied correlation · asset: equities · direction: long correlation · horizon: months · testable: partly · confidence: low
  ^MT009-C02-1
- **Alan Dunne** Short-end yields repriced sharply from mid-August 2026 (2-year up at least 75bp), with a global move.  #mech/policy_reaction _(time-bound view)_
  > the 2-year yield has gone up um I know 75 bips or maybe a percent at least 75 pips I would say since the middle of August
  indicator: 2-year yield · asset: rates · horizon: weeks · testable: yes · confidence: high
  ^MT009-C02-2
- **Alan Dunne** Analysts wrongly assume linear cause and effect: the same fundamental change can have a large or small price effect depending on positioning, barriers and hedges, so markets are complex adaptive systems.  #mech/crowding_positioning
  > this kind of tendency amongst analysts to view the fundamentals and then the market reaction as as being very much linear
  indicator: positioning · asset: multi · testable: partly · confidence: medium
  ^MT009-C02-3
- **Alan Dunne** Because the September 2026 yield rise was led by a global short-end repricing, it points to higher expected policy rates from stronger growth or a prolonged Iran conflict, not only to fiscal or debasement concerns that would hit the long end.  #mech/policy_reaction _(added by Opus, time-bound view)_
  > it's as if everybody now has taken a much more bullish view on global growth or else sees you know the conflict in Iran um staying on much longer
  indicator: 2-year yields globally vs long-end yields · asset: rates · direction: short-end yields up · horizon: months · conditions: front-end-led sell-off · testable: partly - decompose curve moves into front-end vs term premium · confidence: low
  ^MT009-C02-X1

### C03
- **Nick Palus (caption spelling)** Even identifying the current market state is difficult, never mind predicting it.  #mech/research_method
  > it is a struggle to understand point in time what is actually happening in the market let alone predicting the markets
  asset: multi · testable: no · confidence: medium
  ^MT009-C03-1
- **Nick Palus (caption spelling)** In September 2026 rates were the strongest trend-following contributor, most programmes short fixed income.  #mech/cycle_persistence _(time-bound view)_
  > rates have been the strongest contributor to trend following strategies
  indicator: trend following sector contribution · asset: rates · direction: short bonds · horizon: weeks · testable: yes · confidence: high
  ^MT009-C03-2
- **Alan Dunne** September 2026 to the 23rd: SG Trend and SG CTA each about +3.7%, and about +15.25% year to date.  #mech/cycle_persistence _(time-bound view)_
  > sochen trend up about 3.7% and sochen CTA index up about 3.7% as well
  indicator: SG Trend, SG CTA · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT009-C03-3
- **Nick Palus (caption spelling)** About 80% of the month's gains across managers came from fixed income shorts, including the long end and 2-year futures.  #mech/cycle_persistence _(time-bound view)_
  > I'd say 80 80% of the cases concentrated in fixed income short positions and at the long end as well
  indicator: trend P&L attribution · asset: rates · direction: short bonds · horizon: weeks · testable: yes · confidence: high
  ^MT009-C03-4
- **Nick Palus (caption spelling)** Adding trend following to a 60/40 portfolio offsets the long bond core with a short bond position in a rate sell-off.  #mech/risk_management
  > if you've got a 60 uh 40 portfolio and you've taken out some of the allocation and added it to trend following that that trend following exposure now is short bonds
  indicator: 60/40 plus trend following · asset: multi · direction: trend is short bonds when yields rise · horizon: months · conditions: Rising-yield regimes · testable: yes · confidence: high
  ^MT009-C03-5
- **Nick Palus** In January-February 2026 the analyst consensus expected central-bank easing and normalisation, yet by September yields reached multi-year (in places decade) highs, showing how unreliable consensus rate forecasts are.  #mech/slow_reaction _(added by Opus, time-bound view)_
  > 6 months back, um analysts were projecting um rate cuts.
  indicator: analyst rate forecasts vs realised yields · asset: rates · horizon: months · testable: yes - consensus forecast errors · confidence: medium
  ^MT009-C03-X1

### C04
- **Nick Palus (caption spelling)** Rates, commodities and equities were equal contributors at the start of the month, but rates doubled their share in September.  #mech/cycle_persistence _(time-bound view)_
  > precisely because rates have doubled their contribution
  indicator: trend sector contribution · asset: rates · horizon: weeks · testable: yes · confidence: high
  ^MT009-C04-1
- **Nick Palus (caption spelling)** Rates did not trend until Q2 2026 and currencies lack trendiness, showing diversification across contributors over time.  #mech/cycle_persistence _(time-bound view)_
  > we hadn't seen actually rates kind of trending
  indicator: trend contribution by asset class · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT009-C04-2
- **Alan Dunne** The US 10-year yield stayed in a 3.5% to 5% range from October 2022, whipsawing trend followers, and then broke out.  #mech/cycle_persistence _(time-bound view)_
  > it had been a three and a half to 5% range since uh you know October 2022
  indicator: US 10-year yield · asset: rates · horizon: years · conditions: Range-bound yields hurt trend followers · testable: yes · confidence: high
  ^MT009-C04-3
- **Nick Palus (caption spelling)** Bond vol stayed contained, so a vol-scaled signal did not strengthen despite the large yield move; smooth moves raise P&L.  #mech/cycle_persistence _(time-bound view)_
  > no strengthening of those of those um of those signals which attest to the point that the the move has been greater than the volatility at which it comes along
  indicator: vol-scaled trend signals · asset: rates · horizon: weeks · conditions: Low-vol trending moves · testable: yes · confidence: medium
  **Correction (Opus):** Wrong direction: Nick says the volatility-scaled signals did NOT stay flat; they strengthened, because the yield move was larger than the (contained) bond volatility it came with ('no strengthening' is a caption error for 'now strengthening'). → Bond volatility stayed contained while yields rose sharply, so volatility-scaled trend signals strengthened (move larger than its volatility), and a smooth, low-vol move gives larger P&L than a choppy one.
  ^MT009-C04-4

### C05
- **Nick Palus (caption spelling)** 2026 and 2022 were strong trend years, 2022 driven by rates, the dollar and commodities (inflation and geopolitics); this is the third best year in 15.  #mech/cycle_persistence _(time-bound view)_
  > 2022, I guess, was a rate story, but it was also a dollar story as well.
  indicator: trend following annual returns · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT009-C05-1
- **Alan Dunne** Alpha Architect note tests faster look-backs in high VIX and slower in low VIX against a static window on five ETFs.  #mech/research_method
  > whether you can enhance a trend system or a momentum model uh by looking at the volatility um environment
  indicator: VIX-dependent lookback window · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT009-C05-2
- **Nick Palus (caption spelling)** The test picks the top one or two of S&P, US ex-S&P, international equities, global IG bonds and T-bills by momentum.  #mech/slow_reaction
  > Either the best or the two best assets out of the five based on their momentum
  indicator: relative momentum, five ETFs · asset: multi · direction: long the top 1-2 by momentum · horizon: months · testable: yes · confidence: high
  ^MT009-C05-3

### C06
- **Nick Palus (caption spelling)** VIX-triggered look-back switches are fragile: high-VIX periods in the nine-year extension amounted to only about three months.  #mech/research_method
  > as soon as you use kind of VIX triggers, everything becomes very parameterized and quite you know sensitive to to the choices you're making
  indicator: VIX triggers · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT009-C06-1
- **Nick Palus (caption spelling)** The design uses equal notional with no volatility scaling, so risk differs hugely between S&P and Treasuries.  #mech/risk_management
  > but $100 in S&P is not uh is much more risky than $100 in treasuries right
  indicator: equal notional vs vol-scaled · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT009-C06-2
- **Nick Palus (caption spelling)** The paper finds no significant benefit from VIX-conditioned look-backs versus a 10-month static window, outside a 2020-2021 period.  #mech/research_method
  > what they find broadly speaking is no significant value above and beyond a 10-month static look back
  indicator: 10-month static vs VIX-dependent lookback · asset: multi · horizon: months · testable: yes - paper result · confidence: high
  ^MT009-C06-3
- **Nick Palus** The Alpha Architect test is long-only relative (cross-sectional) momentum with monthly rebalancing, so its results do not transfer directly to directional time-series trend following, which takes long or short positions on each asset's own trend.  #mech/research_method _(added by Opus)_
  > a certain extent more of a cross-sectional momentum strategy because if you're picking the best, it is not clear that this is a long or a short position.
  indicator: cross-sectional vs time-series momentum · asset: multi · horizon: months · testable: yes - rerun with time-series signals · confidence: medium
  ^MT009-C06-X1

### C07
- **Nick Palus (caption spelling)** After costs, top-two selection shows no difference between dynamic and fixed windows; an apparent edge came from November 2020 (vaccine month).  #mech/research_method
  > when they use the top two there is no significant difference at all versus using the same two but coming from a kind of fixed window
  asset: multi · horizon: months · testable: yes · confidence: high
  ^MT009-C07-1
- **Nick Palus (caption spelling)** Trigger-based rules have low statistical power since they rarely activate; prefer a continuous function.  #mech/research_method
  > Um and triggers themselves um by nature lend themselves to very low statistical power because you need the trigger to be activated
  indicator: trigger rules · asset: multi · testable: yes · confidence: high
  ^MT009-C07-2
- **Alan Dunne** Some managers trade faster when market volatility is high and slower when it is low.  #mech/slow_reaction
  > this idea of trading faster when market vol is higher and slower um when it's
  indicator: volatility-dependent lookback · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT009-C07-3
- **Nick Palus (caption spelling)** Scale trend signals continuously by volatility (more volatile means weaker signal), instead of switching windows with triggers.  #mech/risk_management
  > But instead of us utilizing a different kind of window depending on volatility, we scale our signals by volatility.
  indicator: vol-scaled trend signal · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT009-C07-4
- **Nick Palus (caption spelling)** Volatility and correlation spikes together change the capital required for a vol target, so portfolio design should use both rather than the VIX.  #mech/risk_management
  > not only do you have volatility spikes, but you have correlation spiking, which also has implications on how much dollar is required for a specific volatility target
  indicator: asset volatility and correlation structure · asset: multi · horizon: days · conditions: Coordinated moves · testable: yes · confidence: medium
  ^MT009-C07-5

### C08
- **Nick Palus (caption spelling)** Do not over-parameterise trend following in trendless periods; add complementary strategies that benefit from those regimes.  #mech/risk_management
  > If they do not exist, I'm not going to try to recreate them with a more complicated structure.
  asset: multi · horizon: years · conditions: Trendless markets · testable: partly · confidence: high
  ^MT009-C08-1
- **Alan Dunne** Short-term momentum is stronger when realised volatility is higher.  #mech/slow_reaction
  > short-term managers and short-term momentum, they do tend to be tend to be stronger when you get higher probably higher realized volatility
  indicator: short-term momentum, realised volatility · asset: multi · horizon: weeks · conditions: High realised volatility · testable: yes · confidence: medium
  ^MT009-C08-2
- **Nick Palus (caption spelling)** Faster models help at turning points, but dynamically deploying speed in time to cut exposure is the open question.  #mech/research_method
  > can I deploy that speed dynamically and will it be fast enough to to cut to cut my exposures
  asset: multi · horizon: weeks · testable: partly · confidence: medium
  ^MT009-C08-3
- **Nick Palus** Using volatility to classify regimes where trend reversals are more likely, and so to time trend following, is very hard and he cannot show statistically that it is worth doing.  #mech/research_method _(added by Opus)_
  > I wouldn't necessarily argue that I can I can prove statistically at least using data um that this is um that this is a pursuit worth pursuing
  indicator: volatility-based regime classification for timing trend · asset: multi · testable: yes - out-of-sample trend timing tests · confidence: medium
  ^MT009-C08-X1

### C09
- **Nick Palus (caption spelling)** A timing indicator must be judged on false positives; calling 3 of 33 turning points tells nothing without them.  #mech/research_method
  > tell me your false positives and then we're going to have a conversation
  asset: multi · testable: yes · confidence: high
  ^MT009-C09-1
- **Nick Palus (caption spelling)** One V-shaped reversal a year for four years (Liberation Day, March 2026) hurts unconstrained trend followers, though recent results were good.  #mech/cycle_persistence _(time-bound view)_
  > these are all the vshapes that we have seen basically one per year for the last four years
  indicator: V-shaped drawdown episodes · asset: multi · horizon: years · conditions: V-shaped sell-offs and rebounds · testable: yes · confidence: medium
  ^MT009-C09-2
- **Nick Palus (caption spelling)** Andrew Ang's Old Bridge paper sets out an agentic AI architecture for institutional asset allocation.  #mech/new _(time-bound view)_
  > it basically talks about agentic architecture for asset management
  asset: multi · testable: partly · confidence: medium
  ^MT009-C09-3

### C10
- **Nick Palus (caption spelling)** Agentic AI turns the human into supervisor and fiduciary, with a policy statement defining risk, return and allowed assets.  #mech/new
  > that human in the loop becomes more of a supervisor more of a kind of the fiduciary
  asset: multi · testable: no · confidence: medium
  ^MT009-C10-1
- **Nick Palus (caption spelling)** The macro agent classifies the economic regime (expansion, late cycle, recession, recovery) with a confidence measure for regime identification risk.  #mech/new
  > it's not about identifying a regime, but it's also about producing a an assessment of the identification risk of that regime
  indicator: regime classification confidence · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT009-C10-2
- **Nick Palus (caption spelling)** Asset-class agents give an expected return, volatility, confidence and a memo for each of about 18 assets.  #mech/new
  > come up with an expected return of the asset class of a volatility estimate and some confidence around that
  indicator: capital market assumptions · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT009-C10-3
- **Nick Palus (caption spelling)** Run about 20 portfolio construction methods instead of one or two, using agents for scale.  #mech/new
  > why don't you actually allow the scale that agents can give you to run 20 portfolios
  indicator: portfolio construction methods · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT009-C10-4

### C11
- **Nick Palus (caption spelling)** The method set spans heuristics (equal weight, cap weight, inverse vol), return-based (mean-variance, Black-Litterman), risk-based (risk parity, max diversification, minimum variance) and non-traditional (CVaR, drawdown constraints).  #mech/risk_management
  > some are more risk based the risk parity max diversification minimum v some are as they call them non-traditional like a civar optimization
  indicator: portfolio construction menu · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT009-C11-1
- **Nick Palus (caption spelling)** An adversarial diversifier agent builds the principal component of the other portfolios and takes the opposite stance to find unseen correlation pockets.  #mech/risk_management
  > So this is now an agent that observes the rest and effectively builds a principal component of the rest and tries to do opposite stuff.
  indicator: principal component of portfolios · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT009-C11-2
- **Nick Palus (caption spelling)** Agents are scored 60/40 from peer votes and historical backtest measures (Sharpe, drawdown).  #mech/new
  > those two combined on a 60/40 kind of scaling basis give you the composite score of all the agents
  indicator: peer votes + backtest score · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT009-C11-3

### C12
- **Nick Palus (caption spelling)** In the March 2026 run the CIO agent picked different schemes from the agents' votes, driven by macro uncertainty.  #mech/new _(time-bound view)_
  > So the most popular allocation scheme um in their example is not the most popular in the selection of the CIO
  asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT009-C12-1
- **Nick Palus (caption spelling)** The paper's design: debate and peer review, natural-language audit trail, composable expertise and governable delegation, with human supervision.  #mech/new
  > there's an element of supervision rather than replacement
  asset: multi · testable: no · confidence: medium
  ^MT009-C12-2
- **Alan Dunne** The March 2026 macro agent found late-cycle conditions with stagflation risk.  #mech/new _(time-bound view)_
  > from a macro perspective they concluded it was late cycle with uh some stagflationary risks
  asset: multi · horizon: months · testable: no · confidence: medium
  ^MT009-C12-3

### C13
- **Alan Dunne** The final recommendation was 44% equities against a 60/40 benchmark.  #mech/new _(time-bound view)_
  > they came out at 44% equities
  asset: equities · direction: underweight equities · horizon: months · conditions: Late-cycle, mixed macro signals · testable: no · confidence: medium
  ^MT009-C13-1
- **Nick Palus (caption spelling)** When the macro regime is unclear, diversify more and rely less on return-based capital market assumptions.  #mech/risk_management
  > should we instead be more prone to diversify at the times that we cannot tell how the macro outcome uh is clear
  indicator: regime classification clarity · asset: multi · direction: more diversified · horizon: months · conditions: Unclear macro regime · testable: partly · confidence: medium
  ^MT009-C13-2
- **Nick Palus (caption spelling)** The CIO favoured cap-weight, vol-target, equal-weight and inverse-variance portfolios that use no return forecasts.  #mech/risk_management
  > I should then rather tilt my allocation towards risk oriented and more huristic allocation frameworks rather than trusting the data as much
  indicator: heuristic allocations · asset: multi · horizon: months · conditions: Unclear regime · testable: partly · confidence: low
  ^MT009-C13-3
- **Alan Dunne** LLM backtests suffer from look-ahead knowledge.  #mech/research_method
  > they all currently incorporate information now that they wouldn't have had back running it in real time
  asset: multi · testable: yes · confidence: high
  ^MT009-C13-4

### C14
- **Nick Palus (caption spelling)** Look-ahead bias in LLM research (knowledge in model parameters), plus data-mining as agents vote for the better-performing backtest.  #mech/research_method
  > you're using a model that was built today perhaps to build estimates for yesterday
  asset: multi · testable: yes · confidence: high
  ^MT009-C14-1
- **Nick Palus (caption spelling)** LLM outputs are non-reproducible, which blocks building a representative backtest.  #mech/research_method
  > LLMA models are not deterministic and even with the same model with the same prompt you might end up having a different answer
  asset: multi · testable: yes · confidence: high
  ^MT009-C14-2
- **Nick Palus (caption spelling)** Monoculture risk: agents sharing one LLM share correlated errors.  #mech/crowding_positioning
  > So if all agents follow the same model from one of the big kind of genai kind of companies, you might find yourself being exposed to some correlation in the in the model.
  asset: multi · testable: partly · confidence: medium
  ^MT009-C14-3
- **Alan Dunne** One fix for LLM look-ahead bias is to restrict backtests to model vintages available at each date, but older models may be too weak to run the analysis, so agentic allocation results must largely be taken at face value.  #mech/research_method _(added by Opus)_
  > maybe those ones weren't even computationally strong enough at that time to run these types of analysis
  indicator: point-in-time LLM model vintages · asset: multi · testable: partly - only forward or vintage-model tests · confidence: medium
  ^MT009-C14-X1

### C15
- **Nick Palus (caption spelling)** In a trend model the 'asset class agent' is past return scaled by volatility; confidence is volatility, so trend and capital-market-assumption forecasts are not comparable.  #mech/slow_reaction
  > we say the expected return is our past return maybe scaled by some measure of all or whatever
  indicator: past return vol-scaled · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT009-C15-1
- **Nick Palus (caption spelling)** A trend signal is itself an implicit regime indicator; trend followers need no macro agent.  #mech/slow_reaction
  > the fact that I observe a rise in in in my price is nothing more than an indicator of the regime
  asset: multi · horizon: months · testable: no · confidence: medium
  ^MT009-C15-2
- **Nick Palus (caption spelling)** Trend portfolio construction uses one or two methods, so the multi-method agent approach could add value there.  #mech/risk_management
  > the fourth which is portfolio construction this is the place that typically we go for one or two and that's about it
  indicator: portfolio construction · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT009-C15-3

### C16
- **Alan Dunne** The binding constraint in asset management is human decision bandwidth, which agentic AI relaxes.  #mech/structural_shift
  > it is the finite bandwidth of human decision makers
  asset: multi · testable: no · confidence: medium
  **Correction (Opus):** Wrong speaker: Nick reads this from the opening of the Ang paper; Alan only raised multiple objectives. → Nick (citing the paper): the binding constraint in asset management is the finite bandwidth of human decision makers, not data or model sophistication, which agentic AI relaxes.
  ^MT009-C16-1
- **Nick Palus (caption spelling)** Institutions value trend following because it deploys exposure faster than investment boards decide.  #mech/slow_reaction
  > we like trend following because it can be opportunistic and deploy the exposures faster than our ability to bring together the investment board
  asset: multi · horizon: months · conditions: Slow institutional decisions · testable: partly · confidence: medium
  ^MT009-C16-2

### C17
- **Nick Palus (caption spelling)** Agents debating in natural language are auditable but stochastic.  #mech/new
  > all becoming much more auditable and tractable. M but that in itself is stochastic.
  asset: multi · testable: no · confidence: medium
  ^MT009-C17-1

