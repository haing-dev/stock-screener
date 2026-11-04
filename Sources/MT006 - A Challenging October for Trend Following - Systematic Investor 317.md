---
source_id: MT006
title: "A Challenging October for Trend Following - Systematic Investor 317"
date: 2024-10-16
channel: "Top Traders Unplugged"
url: 
words: 10832
claims: 50
added_by_crosscheck: 5
corrections: 3
crosscheck: "opus cross-check"
speakers: ["Neils Kastrup-Larsen (host, Top Traders Unplugged)", "Rich Brennan (co-host, systematic trend-following manager)"]
tags: [source, layer0]
---
# A Challenging October for Trend Following - Systematic Investor 317

**Speakers:** Neils Kastrup-Larsen (host, Top Traders Unplugged); Rich Brennan (co-host, systematic trend-following manager)

**Summary:** Top Traders Unplugged weekly: October 2024 trend-following drawdown, Faber-style long-only trend overlay on SPY/TLT/EEM, and Brennan's outlier-hunting ensemble philosophy. Brennan argues for many uncorrelated systems with trailing stops and complex-adaptive-systems reasoning for why trends and fat tails exist.

**Approach:** trend following, ensemble systems, tactical asset allocation, complex adaptive systems

**Cross-check completeness estimate of first read:** 0.91 - first reader caught nearly all method and mechanism ideas; missed a few data points (sector signal strength, short-term index, concentrated investors) and the hindsight-bias remark

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro, hurricanes, ensemble weather forecasting analogy |
| C02 | 3 | October 2024 CTA losses by sector, hidden correlations, dispersion |
| C03 | 3 | trend barometer, index performance, benchmark representativeness |
| C04 | 2 | replicator tracking error; listener question on SPY/TLT/EEM tactical allocation |
| C05 | 5 | Faber 10m SMA overlay, benefits and costs |
| C06 | 4 | overlay cons, regime bias in three-asset tests |
| C07 | 4 | Buffett diversification, outlier hunting, staggered ensemble entries |
| C08 | 4 | fat tails, nonlinearity squared, concentration |
| C09 | 3 | max concentration, margin cap, trailing stops |
| C10 | 4 | loose pants ensemble, drawdown improvement, eight core systems, reaction not prediction |
| C11 | 2 | complex adaptive systems, fractals, Holland signals/boundaries/emergence |
| C12 | 3 | signals, boundaries, state space |
| C13 | 3 | path dependence, feedback loops |
| C14 | 2 | stability, outliers as natural, Wolfram intro |
| C15 | 2 | chaos, strange attractors, computational irreducibility |
| C16 | 0 | nothing actionable: outro and sponsor read |

## Claims

### C01
- **Rich Brennan** Ensemble forecasting models beat older single-method forecasts, used as an analogy for ensembles of trend systems.  #mech/new
  > these Ensemble models that they use for forecasting techniques are certainly better than what they used to be
  asset: other · testable: no - analogy only · confidence: medium
  ^MT006-C01-1

### C02
- **Neils Kastrup-Larsen** Trend followers who had just flipped to long bonds after years short were hit when the market delivered a meaningful correction, making fixed income the worst sector in October 2024.  #mech/slow_reaction _(time-bound view)_
  > fixed income has been the most difficult uh sector I think that Trend followers were just sort of settling into some long exposure over the summer after a few years riding the the short side of that market
  indicator: trend-following sector P&L (fixed income) · asset: rates · direction: CTAs lose on bond-trend flips into corrections · horizon: weeks · conditions: Right after a trend change into a new position · testable: partly - needs CTA sector attribution data · confidence: medium
  ^MT006-C02-1
- **Rich Brennan** Diversification across many markets can fail in a trend reversal because hidden correlations make many trends reverse together.  #mech/crowding_positioning _(time-bound view)_
  > subtly hidden beneath all of that Matrix of that very large diversification there hidden correlations and clearly everything sort of is reversing on us at the moment
  asset: multi · horizon: weeks · conditions: In broad trend reversals diversification benefit shrinks · testable: partly - measurable via correlation of trend-strategy P&L across sectors · confidence: medium
  ^MT006-C02-2
- **Rich Brennan** Dispersion of results among trend followers is large in 2024, so benchmark indices do not describe individual managers.  #mech/research_method _(time-bound view)_
  > I think dispersion is going to be one of the major topics that come out
  indicator: CTA return dispersion · asset: multi · horizon: years · testable: yes - cross-sectional spread of manager returns · confidence: medium
  ^MT006-C02-3
- **Neils Kastrup-Larsen** Trend-follower losses in a reversal concentrate where signals (and so positions) were strong; energy did little damage in October 2024 because its signals were weak, while meats (live cattle) were the only bright spot and currencies (GBP, AUD, NZD) corrected.  #mech/slow_reaction _(added by opus cross-check, time-bound view)_
  > energies kind of mixed probably not where the damage is too much so far in in terms of trend followers simply because I don't think signals are particular strong in that sector at the moment
  indicator: trend signal strength by sector · asset: multi · direction: weak-signal sectors lose little in reversals · horizon: weeks · conditions: signal-strength-scaled position sizing · testable: yes - sector P&L vs prior signal strength · confidence: medium
  ^MT006-C02-X1

### C03
- **Neils Kastrup-Larsen** A trend barometer (share of markets with a clear trend, short-horizon) reflects but does not predict how hard conditions are for trend followers; a reading near 14-20 is about the worst.  #mech/cycle_persistence _(time-bound view)_
  > it's certainly been very good at reflecting the challenges because it's down to 20 as of yesterday which is very low
  indicator: Top Traders trend barometer (Neils's trend parameter) · asset: multi · direction: low reading = hard for trend followers · horizon: weeks · conditions: Uses a shorter horizon than traditional medium/long-term trend following · testable: yes - level of barometer vs subsequent trend-following returns · confidence: medium
  **Correction (cross-check):** The definition 'share of markets with a clear trend' is not stated in the transcript (added by the reader). → Neils's trend barometer (shorter horizon than traditional trend following) reflects, but does not predict, how hard conditions are for trend followers; at 14-20 it reads 'as bad as it gets'.
  ^MT006-C03-1
- **Neils Kastrup-Larsen** In October 2024 to mid-month BTOP50 was -2.84% (+1.23% YTD), SG CTA -3.64% (-1.22% YTD) and SG Trend almost -5% (-2.6% YTD), versus MSCI World -0.33% and S&P 500 flat.  #mech/cycle_persistence _(time-bound view)_
  > Bop 50 as a Wednesday was down 2.84% in October still up 1.23%
  indicator: BTOP50, SG CTA, SG Trend, MSCI World, S&P 500 TR · asset: multi · direction: CTA benchmarks negative in October 2024 · horizon: weeks · testable: yes - published index returns · confidence: high
  ^MT006-C03-2
- **Rich Brennan** CTA benchmark indices are weighted toward the largest funds, so a wider equal-ish index (Top Traders Unplugged index) shows less gloom and the big-fund index misrepresents the group.  #mech/research_method
  > the these indexes uh are dealing with uh the very large funds a bit like the the cap waiting we see in the S&P 500
  indicator: SG CTA, SG Trend vs Top Traders Unplugged index · asset: multi · horizon: years · testable: yes - compare index construction and returns · confidence: medium
  ^MT006-C03-3
- **Neils Kastrup-Larsen** In the October 2024 trend reversal the SG short-term traders index fell much less (about -1.5% month, -0.75% YTD) than the SG Trend index (about -5%), i.e. short-horizon CTAs were hurt less.  #mech/slow_reaction _(added by opus cross-check, time-bound view)_
  > the so genc short-term Traders index down one and a quish and for the month and down 75 basis points for the year
  indicator: SG Short-Term Traders index vs SG Trend index · asset: multi · direction: short-term CTAs outperform trend CTAs in a sharp reversal · horizon: weeks · conditions: sharp trend reversal · testable: yes - index returns · confidence: high
  ^MT006-C03-X1

### C04
- **Neils Kastrup-Larsen** A trend-replication product shows large tracking error versus the CTA benchmark in 2024 (to the upside).  #mech/research_method _(time-bound view)_
  > his product has massive tracking error this year luckily it's to the upside for him
  indicator: replicator tracking error vs CTA index · asset: multi · horizon: years · testable: yes - tracking error is measurable · confidence: medium
  ^MT006-C04-1
- **Rich Brennan** Holding SPY, TLT and EEM (equities, long bonds, emerging markets) diversifies across weakly correlated asset classes and smooths returns, similar to all-weather portfolios.  #mech/risk_management
  > by investing in these uncorrelated ETFs we naturally obtain benefits of diversification that help to smooth the portfolio returns
  indicator: SPY, TLT, EEM · asset: multi · horizon: years · conditions: Depends on stock-bond correlation staying low · testable: yes - backtest ETF mix · confidence: medium
  ^MT006-C04-2

### C05
- **Rich Brennan** Faber-style tactical asset allocation: stay long an asset while price is above its 10-month simple moving average, otherwise move to cash or short bonds.  #mech/slow_reaction
  > he used a simple long-term moving average often a 10mon simple moving average to determine whether to be in or out of each of those three asset classes
  indicator: 10-month SMA on SPY/TLT/EEM (Faber 2007) · asset: multi · direction: long when price above 10m SMA, else cash · horizon: months · testable: yes - simple rule, long public history · confidence: high
  ^MT006-C05-1
- **Rich Brennan** A long-only moving-average overlay limits large drawdowns by exiting assets in prolonged downtrends.  #mech/risk_management
  > the main goal here is downside protection
  indicator: moving-average exit · asset: multi · direction: exit assets after prolonged downtrend · horizon: months · conditions: Works only for prolonged declines, not sharp short crashes · testable: yes · confidence: medium
  ^MT006-C05-2
- **Rich Brennan** The cost of the moving-average overlay is lag in re-entering after sharp quick recoveries, sacrificing upside.  #mech/slow_reaction
  > these strategies tend to lag in their re-entry after a sudden Market bounce
  indicator: moving-average re-entry · asset: multi · horizon: weeks · conditions: Sharp V-shaped recoveries · testable: yes - measurable from backtest · confidence: high
  ^MT006-C05-3
- **Rich Brennan** A trend-following overlay is slow risk mitigation, not an immediate hedge; options are the tool for short-term tail protection.  #mech/risk_management
  > if you wanted um pure um short-term protection you would typically go into TI risk protection strategies like options
  asset: multi · horizon: days · testable: partly - compare overlay vs options hedge in short crashes · confidence: medium
  ^MT006-C05-4
- **Rich Brennan** Applying the trend filter separately to several uncorrelated asset classes lets the portfolio rotate dynamically toward whichever asset is trending.  #mech/risk_management
  > when you for instance out of the Spy you might uh be still in the the the TLT and you might still be in the eem
  indicator: per-asset trend filter on SPY/TLT/EEM · asset: multi · direction: hold the assets that are above their moving average · horizon: months · testable: yes · confidence: medium
  ^MT006-C05-5

### C06
- **Rich Brennan** In sideways markets a moving-average filter produces repeated in-and-out whipsaw losses.  #mech/slow_reaction
  > you can enter these awful periods of whipsaw risk for instance when uh you're sort of going in and out of that simple moving average
  indicator: moving-average cross · asset: multi · horizon: weeks · conditions: Range-bound markets near the average · testable: yes · confidence: high
  ^MT006-C06-1
- **Rich Brennan** A long-only trend filter forgoes profit from downtrends, and long-short trend following gives extra correlation benefits at portfolio level.  #mech/risk_premium
  > the long only constraint is another con from my perspective in that you can't participate in the downside move
  indicator: long-only vs long/short trend · asset: multi · direction: long/short beats long-only on diversification · horizon: months · conditions: Assets with big downside potential · testable: yes · confidence: medium
  ^MT006-C06-2
- **Neils Kastrup-Larsen** The benefit of a protective rule like a trend overlay may take 10-20 years to show, so discipline and a good starting date matter.  #mech/research_method
  > you may not see the result for another 10 or 15 or 20 years
  asset: multi · horizon: years · testable: partly - depends on sample path · confidence: medium
  ^MT006-C06-3
- **Neils Kastrup-Larsen** A backtest on three instruments risks regime bias, e.g. bonds had falling rates for about 37 of the past 40 years, so a bond trend result may not repeat; prefer broader diversification.  #mech/research_method
  > if you only look at three instruments like that you may obviously be prone to the fact that they may have been in a specific regime
  indicator: long-bond trend backtest · asset: rates · horizon: years · conditions: Falling-rate regime inflates bond results · testable: yes - test across regimes · confidence: high
  ^MT006-C06-4
- **Neils Kastrup-Larsen** Despite its caveats (whipsaw, long-only, regime bias) both hosts judge the Faber-style long-only trend overlay a valid strategy, likely better than unmanaged buy-and-hold.  #mech/risk_management _(added by opus cross-check)_
  > yeah yeah probably better than doing nothing and just long only and closing your eyes
  indicator: 10-month SMA overlay vs buy-and-hold · asset: multi · direction: overlay over buy-and-hold · horizon: years · conditions: benefit may take 10-20 years to show · testable: yes - overlay vs buy-and-hold backtest · confidence: medium
  ^MT006-C06-X1

### C07
- **Rich Brennan** Buffett's remark applies to outlier hunters: they diversify widely not to reduce risk but because they do not know where outliers will appear.  #mech/behavioral
  > diversification is protection against ignorance
  asset: multi · testable: no - philosophical framing · confidence: medium
  ^MT006-C07-1
- **Rich Brennan** Trend following earns its profit from rare, massive outlier moves in the tails, while noise dominates most of the return distribution.  #mech/structural_shift
  > our goal is to capture those rare but massive price moves called outliers
  indicator: price return tails · asset: multi · direction: long/short outliers · horizon: months · testable: yes - decompose trend returns by tail events · confidence: high
  ^MT006-C07-2
- **Rich Brennan** Start with small bets and concentrate capital progressively as a trend persists, so capital stays mostly inactive during noise.  #mech/risk_management
  > we progressively concentrate our Capital into those Trends as outliers emerge
  asset: multi · direction: scale up with trend persistence · horizon: months · testable: yes - pyramiding rule · confidence: high
  ^MT006-C07-3
- **Rich Brennan** Staggered activation of multiple uncorrelated entry systems (Donchian, Keltner, Bollinger breakouts) builds position size only as a trend endures.  #mech/risk_management
  > we're trying to avoid investing all of our Capital At Once into one Trend that may or may not unfold into an outli
  indicator: Donchian, Keltner and Bollinger channel breakouts · asset: multi · direction: add systems as trend persists · horizon: months · testable: yes - ensemble backtest · confidence: high
  ^MT006-C07-4

### C08
- **Rich Brennan** All liquid markets show fat-tailed (leptokurtic) daily returns, with mean-reverting noise in the bulk and trending behaviour in the tails.  #mech/structural_shift
  > they all follow what they call a cpto kurtic signature with these big fat tails
  indicator: daily return distribution · asset: multi · horizon: days · testable: yes - kurtosis of daily returns · confidence: high
  ^MT006-C08-1
- **Rich Brennan** Each system in an ensemble captures the nonlinear price move, so an ensemble of 20 systems multiplies the payoff from outliers.  #mech/risk_premium
  > this is why I refer to our approach as being nonlinearity squared
  indicator: ensemble of 20 systems · asset: multi · horizon: months · testable: partly - ensemble payoff convexity testable · confidence: medium
  ^MT006-C08-2
- **Rich Brennan** Diversify broadly to find the markets in outlier trends, then concentrate risk there.  #mech/risk_management
  > diversifying for the specific purpose of being able to focus its capital towards what we call the events that matter
  asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT006-C08-3
- **Rich Brennan** Serial correlation from positive feedback drives outlier trends.  #mech/cycle_persistence
  > my knowledge of Serial correlation which is driving these nonlinear events through this amplification process this positive feedback process
  indicator: serial correlation of returns · asset: multi · horizon: months · testable: yes - autocorrelation tests · confidence: medium
  ^MT006-C08-4

### C09
- **Rich Brennan** The number of ensemble systems is limited in practice by futures margin when risk concentrates in expensive-margin markets (e.g. palladium).  #mech/risk_management
  > I'm capping out at 20 at the moment simply because its margin the margin on these instruments
  indicator: margin requirement · asset: commodities · conditions: Futures vs CFD implementation · testable: yes · confidence: high
  ^MT006-C09-1
- **Rich Brennan** During outlier moves correlations between markets break down, so uncorrelated systems riding the outlier improve results.  #mech/structural_shift
  > outliers naturally destroy correlations in markets
  indicator: cross-market correlation in outliers · asset: multi · horizon: weeks · conditions: In outlier events · testable: yes · confidence: medium
  ^MT006-C09-2
- **Rich Brennan** Every system in the ensemble uses a trailing stop so open profits are not given back.  #mech/risk_management
  > we must with each of our uncorrelated systems have trailing stops behind them at all times
  indicator: trailing stop · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT006-C09-3
- **Neils Kastrup-Larsen** Highly successful discretionary equity investors run very concentrated books (Buffett about 40% in Apple, Ackman 53% of a $10bn fund in three stocks, Nomad Investment Partners in one or two stocks), raising the question of how much concentration a trend system should allow.  #mech/risk_management _(added by opus cross-check, time-bound view)_
  > it says the headline says he has 53% of his hedge funds of you know which is10 billion do in just three stocks
  indicator: portfolio concentration (top holdings share) · asset: equities · horizon: years · testable: partly - holdings data, but survivorship of famous examples · confidence: medium
  ^MT006-C09-X1

### C10
- **Rich Brennan** An ensemble of many systems with individually tighter stops gives an aggregate looser trailing exit than two systems with wide stops.  #mech/risk_management
  > with an ensemble of 20 uncorrelated markets the sum total of those being applied to the outlier actually does have very loose pants
  indicator: ensemble trailing stops · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT006-C10-1
- **Rich Brennan** Adding more uncorrelated systems continuously improves drawdown and gives a small, diminishing MAR/CAGR increase with no sharp stopping point.  #mech/risk_management
  > the draw down because of the uncorrelated Ensemble is always improving as I'm putting more and more uncorrelated
  indicator: number of systems vs CAGR/drawdown · asset: multi · horizon: months · testable: yes - ensemble size sweep · confidence: medium
  ^MT006-C10-2
- **Rich Brennan** Most trend followers use few core approaches (about 5-10) with many parameter variations rather than 20 truly different systems.  #mech/research_method
  > we actually have eight core systems so the eight core systems but the variations in that are our parameter are variations as well
  asset: multi · testable: yes · confidence: medium
  **Correction (cross-check):** Wrong speaker for the 5-10 figure: Neils says there are only five or ten ways to do trend following; Rich says he runs eight core systems with parameter variations to reach his 20. → Rich builds his ensemble from eight core systems plus parameter variations; Neils notes there are only about five to ten distinct ways to trend-follow, so large ensembles are mostly parameter variants.
  ^MT006-C10-3
- **Rich Brennan** Trend following reacts to price moves and does not forecast them.  #mech/new
  > this nonpredictive philosophical approach which is basically reacting to Market moves it's not predicting it's reacting to them
  asset: multi · testable: no - philosophy · confidence: high
  ^MT006-C10-4
- **Rich Brennan** Using a larger ensemble of uncorrelated systems reduces the dependence on hindsight-chosen parameters (less overfitting risk) than picking a few optimised systems.  #mech/research_method _(added by opus cross-check)_
  > what I'm finding in my research is that the more I diversify with my uncorrelated systems the less how do I put it hindsight bias is required
  indicator: number of ensemble systems · asset: multi · direction: more systems = less hindsight bias · testable: partly - out-of-sample decay vs ensemble size · confidence: medium
  ^MT006-C10-X1

### C11
- **Rich Brennan** Markets behave like complex adaptive systems with fractal, scale-invariant structure that grow from small seeds into large trends, so no part is independent of the others.  #mech/structural_shift
  > they build from seeds or kernels and then um in a scale invariant way as they progressively evolve
  asset: multi · testable: partly - fractal/Hurst measures · confidence: medium
  ^MT006-C11-1
- **Rich Brennan** Holland's framework for markets: signals, boundaries and emergence.  #mech/new
  > at the core of these complex adaptive systems are these three processes signals boundaries and emergent processes
  asset: multi · testable: no - conceptual · confidence: medium
  ^MT006-C11-2

### C12
- **Rich Brennan** Agents interpret the same signal differently, so reactions to signals vary and keep evolving.  #mech/behavioral
  > these signals are not just simple data points but more importantly they interpretations of that information by the agent
  asset: multi · testable: no · confidence: medium
  ^MT006-C12-1
- **Rich Brennan** Boundaries such as risk rules and regulation limit the degrees of freedom of agents; a trend strategy has position limits, stops and leverage caps.  #mech/risk_management
  > in financial markets boundaries take the form of for instance risk management rules regulatory Frameworks and system parameters
  indicator: position size limits, stop-loss, leverage caps · asset: multi · testable: no · confidence: medium
  ^MT006-C12-2
- **Rich Brennan** Boundaries make the price path constrained and path-dependent rather than random.  #mech/structural_shift
  > this is not a a stochastic state space where anything is possible like a random move
  asset: multi · testable: partly · confidence: low
  ^MT006-C12-3

### C13
- **Rich Brennan** Stochastic (ergodic) models of markets lack path dependence, whereas real markets show path dependence.  #mech/structural_shift
  > they're not constrained by these time ordered constraints or spatial constraints there's no sense of path
  asset: multi · testable: partly - test path dependence · confidence: medium
  ^MT006-C13-1
- **Rich Brennan** Enduring trends come from positive feedback loops with serial dependence, which trend followers exploit.  #mech/cycle_persistence
  > enduring Trends is caused through positive feedback amplification nonlinear amplification
  asset: multi · horizon: months · testable: yes - autocorrelation · confidence: medium
  ^MT006-C13-2
- **Rich Brennan** Mean-reversion traders create negative feedback that interferes with trends, and this balance stabilises markets.  #mech/crowding_positioning
  > a mean reverter or a convergent Trader negative feedback loops what they're doing is that they are explicitly going against the trend
  asset: multi · testable: no · confidence: medium
  ^MT006-C13-3

### C14
- **Rich Brennan** Trend following is capacity-limited by the need for counterparties who trade against the trend.  #mech/crowding_positioning
  > we can't obviously all be Trend followers as the system would explode with positive feedback
  asset: multi · conditions: If too many follow trends, markets destabilise · testable: partly · confidence: medium
  **Correction (cross-check):** Misframed: Rich does not talk about capacity or counterparties; he says markets need mean-reverting/other participants to offset trend followers' positive feedback, which keeps the system stable. → If everyone were a trend follower positive feedback would make markets explode; the mix of trend followers (positive feedback) and other participants (negative feedback) at all scales is what keeps markets stable.
  ^MT006-C14-1
- **Rich Brennan** Outliers are natural and occur more often than normal-distribution models imply.  #mech/structural_shift
  > to be expected much more frequently than what these traditional stochastic models would have you believe
  indicator: tail frequency · asset: multi · testable: yes - tail frequency vs normal · confidence: high
  ^MT006-C14-2

### C15
- **Rich Brennan** Nonlinear deterministic dynamics limit prediction, which supports reacting rather than predicting.  #mech/structural_shift
  > the ability to predict into the future is is limited or impossible because of these strange attractors
  asset: multi · testable: no · confidence: low
  ^MT006-C15-1
- **Rich Brennan** Complex systems are computationally irreducible, hence inherently unpredictable for any embedded observer.  #mech/structural_shift
  > they would need a computer that lasted the length of this universe to iterate in such a way to be able to predict what the system is going to do next
  asset: multi · testable: no · confidence: medium
  ^MT006-C15-2

