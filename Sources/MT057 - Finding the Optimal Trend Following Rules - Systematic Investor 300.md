---
source_id: MT057
title: "Finding the Optimal Trend Following Rules - Systematic Investor 300"
date: 2024-06-18
channel: "Top Traders Unplugged"
url: 
words: 9923
claims: 39
added_by_crosscheck: 7
corrections: 0
crosscheck: "opus cross-check"
speakers: ["Rich Brennan (Australian systematic trend follower)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Finding the Optimal Trend Following Rules - Systematic Investor 300

**Speakers:** Rich Brennan (Australian systematic trend follower); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** June 2024 systematic-investor episode: a choppy period where trend managers gave back about half of Q1 gains, answers on CFD costs and ATR sizing, then Brennan summarizes a 2023 paper deriving optimal trend rules via Markov and semi-Markov regime models that matches practitioners backtests, and argues AI threatens short-term but not medium/long-term trend following.

**Approach:** trend following, regime switching, Markov models, position sizing, CFD costs, AI and quant research

**Cross-check completeness estimate of first read:** 0.88 - first reader covered the paper's logic, CFD costs, ATR sizing and AI view well; missed the rule families, portability, behavioral-vs-formal rationale, Niels's holy-grail caveat and Baum-Welch reference; no factual errors found.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | whipsaw environment |
| C02 | 3 | Fed repricing, trend giveback, rebalance into trend |
| C03 | 5 | trend barometer, index returns, CFD cost structure |
| C04 | 2 | backtest costs, ATR sizing across price levels |
| C05 | 1 | paper intro, using LLMs to read papers |
| C06 | 3 | ad hoc optimization vs math, paper findings |
| C07 | 1 | Markov model of market states |
| C08 | 2 | hidden Markov, trend duration |
| C09 | 3 | semi-Markov, equivalence with autoregression |
| C10 | 3 | MACD optimal, dynamic adjustment, forecast horizon |
| C11 | 3 | AI and short-term competition, core rules |
| C12 | 2 | Medallion, short-term horizon, external clients |
| C13 | 3 | capacity and market impact, CTA edge vs AI |
| C14 | 0 | nothing actionable: ChatGPT list, plugs |
| C15 | 0 | nothing actionable: outro |

## Claims

### C01
- **Rich Brennan** A choppy pogo-stick market with many whipsaws produces successes in some assets and failures in others, a hard period for trend models.  #mech/cycle_persistence _(time-bound view)_
  > I'm referring to it as a pogos stic environment at the moment
  asset: multi · horizon: weeks · conditions: June 2024 whipsaw conditions · testable: yes - trend index returns · confidence: high
  ^MT057-C01-1

### C02
- **Niels Kaastrup-Larsen** The Fed dot plot moved from several cuts to maybe one, and Niels thinks inflation is sticky (high for longer) and the next move might even be a hike, leaving markets without a clear path.  #mech/policy_reaction _(time-bound view)_
  > it's not going to be that easy to get rid of inflation and high for longer
  indicator: Fed dot plot · asset: rates · direction: fewer cuts; possible hike · horizon: months · testable: partly - view on policy path · confidence: medium
  ^MT057-C02-1
- **Niels Kaastrup-Larsen** Trend managers had given back about half of Q1 returns, broad-based across metals, fixed income and currencies, which is not unusual for trend following.  #mech/cycle_persistence _(time-bound view)_
  > maybe half of q1's returns have been uh given back by managers
  asset: multi · horizon: months · conditions: drawdowns of this size are normal for trend · testable: yes - CTA index drawdown data · confidence: medium
  ^MT057-C02-2
- **Niels Kaastrup-Larsen** After allocators rebalanced out of trend following following its 2022 win, stocks at all-time highs and trend in a drawdown may be a good point to rebalance back into trend as a diversifier.  #mech/behavioral _(time-bound view)_
  > maybe it's time to reverse that uh equation and rebalance back into Trend
  asset: multi · direction: increase trend allocation after a drawdown with equities at highs · horizon: years · conditions: trend has lagged and equities near highs · testable: partly - rebalancing rule backtest · confidence: low
  ^MT057-C02-3

### C03
- **Niels Kaastrup-Larsen** A trend barometer reading of 27 indicates a weak trend environment, consistent with the poor CTA returns.  #mech/cycle_persistence _(time-bound view)_
  > finished at 27 yesterday so that's a pretty weak reading so completely in line with the returns we see
  indicator: Niels trend barometer (proprietary) · asset: multi · horizon: days · testable: partly - proprietary gauge · confidence: medium
  ^MT057-C03-1
- **Niels Kaastrup-Larsen** Reported mid-June 2024 returns: SG CTA -2.16% for the month and +7.15% YTD, SG Trend -2.5% and +8.89%, short-term traders -2% and +0.69%, versus MSCI World +10.58% and S&P 500 +14.65% YTD.  #mech/risk_premium _(time-bound view)_
  > stock gen CTA down 2.16 % uh for June
  indicator: SG CTA, SG Trend, SG Short-Term Traders, MSCI World, S&P 500 · asset: multi · horizon: months · testable: yes - index data · confidence: high
  ^MT057-C03-2
- **Rich Brennan** CFD trading carries broker spreads, slippage and holding (swap) costs, which are larger than futures costs and depend on broker margin-making rather than centralized exchanges.  #mech/risk_management
  > there'll be holding costs which in our world of cfds we call swap costs
  indicator: CFD swap rate, spread, slippage · asset: multi · testable: yes - broker cost data · confidence: high
  ^MT057-C03-3
- **Rich Brennan** When the trend direction has positive swap the trade earns carry on top of trend; the swap differs by asset and direction.  #mech/risk_premium
  > has positive swap on top of the the trend value we've got the the benefit of the carry trade
  indicator: CFD swap (carry) · asset: multi · direction: trade trend direction with positive swap · conditions: holding period long enough to accrue swap · testable: yes - add swap carry to trend backtest · confidence: medium
  ^MT057-C03-4
- **Rich Brennan** Trends in assets with negative swap make long holds expensive, so swap costs can materially reduce performance and should be monitored on a dashboard.  #mech/risk_management
  > if you're holding for extended periods the cost of that um swap can become quite large
  indicator: CFD swap rate · asset: multi · direction: avoid long holds on negative-swap markets · horizon: months · conditions: extended holding periods · testable: yes - cost-adjusted backtest · confidence: high
  ^MT057-C03-5
- **Rich Brennan** For long-holding trend systems, cash CFDs give access to more markets than dated CFDs but carry daily overnight financing, so the choice depends on monitoring that holding cost against the wider market set.  #mech/risk_management _(added by opus cross-check)_
  > like Dennis I I trade cash cfds as well
  indicator: cash vs dated CFD overnight financing · asset: multi · horizon: months · conditions: long holding periods · testable: yes - compare net returns after financing for cash vs dated CFDs · confidence: medium
  ^MT057-C03-X1

### C04
- **Rich Brennan** Backtest first for trend suitability, then add actual broker costs, which may eliminate some markets or models as untradeable.  #mech/research_method
  > then once that test is done you need to import back the costs associated with your broker
  asset: multi · testable: yes - net-of-cost backtest · confidence: high
  ^MT057-C04-1
- **Rich Brennan** When prices and ATR rise several-fold over decades, keep a constant dollar risk per trade (stop = multiple of 25-day ATR) and let contract counts change; large early position counts are expected, not a bug.  #mech/risk_management
  > I risk per trade let's say an example of $500 per trade
  indicator: 25-period ATR; fixed dollar risk per trade · asset: multi · direction: position size = risk / (ATR multiple) · horizon: years · conditions: long backtests where price level and vol change · testable: yes - volatility-based sizing backtest · confidence: high
  ^MT057-C04-2

### C05
- **Rich Brennan** Use an LLM to read and explain academic quant papers to lay readers step by step.  #mech/research_method
  > download the PDF from that white paper into chat GPT
  asset: other · testable: no - workflow tip · confidence: high
  ^MT057-C05-1

### C06
- **Rich Brennan** The 2023 paper (Optimal trend following rules in two-state switching regime models) says trend followers build models by ad hoc heavy optimization and proposes mathematical formulas (Markov processes, autoregression) to derive optimal models.  #mech/research_method
  > the methods that they deploy to come up with their models tends to be what they refer to as ad hoc
  asset: multi · horizon: years · testable: yes - replicate the paper · confidence: medium
  ^MT057-C06-1
- **Rich Brennan** The mathematically optimal models are simple, medium-to-long-term holds with loose parameter sets, matching those found through practitioner backtesting.  #mech/research_method
  > actually agree with the optimal models that for instance you and I come to with our back testing process
  asset: multi · direction: simple, long-hold trend models · horizon: months · testable: yes - parameter grids · confidence: medium
  ^MT057-C06-2
- **Rich Brennan** Stark applied the equity-derived optimal parameters to futures on unseen data and got a Sharpe ratio of about 1.2 over 20-30 years.  #mech/research_method
  > found that on unseen data they were very effective models that got him a sharp of about 1.2
  asset: multi · horizon: years · conditions: out-of-sample futures · testable: yes - reproducible backtest · confidence: medium
  ^MT057-C06-3
- **Rich Brennan** The paper compares three trend-rule families - moving-average crossovers (simple, linearly weighted, exponentially weighted), MACD and momentum - where linear and exponential weights put more weight on recent prices.  #mech/research_method _(added by opus cross-check)_
  > a linear moving average does is it is it weights um the the the moving average in a in a linear way such that when you're using a look back of say 50 days
  indicator: SMA / LMA / EMA crossover, MACD, momentum · asset: multi · horizon: months · testable: yes - rule families are fully specified · confidence: high
  ^MT057-C06-X1
- **Rich Brennan** An analytically derived optimal rule can be ported quickly to new markets without fresh brute-force optimisation, which also reduces data-mining risk relative to market-by-market backtesting.  #mech/research_method _(added by opus cross-check)_
  > once the mathematics has been defined it allows you to very quickly use it in other Market Landscapes
  asset: multi · conditions: regime-switching model assumptions hold · testable: yes - out-of-market test of derived parameters · confidence: medium
  ^MT057-C06-X2

### C07
- **Rich Brennan** A Markov model infers a chosen number of market states from the data via Bayesian inference, giving the probability of being in each state and a transition matrix, which may not match bull/bear labels.  #mech/research_method
  > it's using the data as opposed to our assumptions as to what those states are
  indicator: Markov state and transition matrix · asset: multi · conditions: number of states chosen by the researcher · testable: yes - fit Markov/HMM models · confidence: medium
  ^MT057-C07-1

### C08
- **Rich Brennan** In a hidden Markov model, trend-model returns act as thermometers of the market state, giving state-dependent weights per model and a short-term forecast of the next state.  #mech/research_method
  > we can use our Trend following models as a bit like thermometers
  indicator: returns of long-only, short-only, mean-reverting models as state observations · asset: multi · direction: allocate to models by state · horizon: days · testable: yes - HMM on strategy returns · confidence: medium
  ^MT057-C08-1
- **Rich Brennan** Trend strength waxes and wanes via autocorrelation, and the longer a trend persists the greater the chance it ends, which a strict Markov model cannot represent.  #mech/cycle_persistence
  > the longer you are in a trend the greater the chance that trend is going to end
  asset: multi · direction: trend exit hazard rises with age · horizon: months · testable: yes - duration analysis of trends · confidence: medium
  ^MT057-C08-2

### C09
- **Rich Brennan** A semi-Markov model lets transition probabilities change with trend duration, giving both model allocation and when to switch between models.  #mech/research_method
  > how those transition probabilities change over the course of time as that Trend endures
  indicator: semi-Markov duration-dependent transition probability · asset: multi · testable: yes - semi-Markov fit · confidence: medium
  ^MT057-C09-1
- **Rich Brennan** Autoregression (serial correlation across many lags) and Markov models are mathematically equivalent views of the same trend persistence, so moving-average, EMA, MACD and momentum rules can be optimized analytically.  #mech/research_method
  > they're mathematically equivalent
  asset: multi · testable: yes - paper proof · confidence: medium
  ^MT057-C09-2
- **Rich Brennan** Under a plain Markov two-state model the exponential moving average was the best trend rule.  #mech/research_method
  > the EMA was the best model to use in trending environments
  indicator: EMA · asset: multi · conditions: simple Markov two-state regime model · testable: yes - paper result · confidence: medium
  ^MT057-C09-3

### C10
- **Rich Brennan** Under the more realistic semi-Markov model MACD was the best rule, with optimal parameters matching what practitioners find.  #mech/research_method
  > they found that actually the macd model was the better model
  indicator: MACD · asset: multi · conditions: semi-Markov regime model · testable: yes - paper result · confidence: medium
  ^MT057-C10-1
- **Rich Brennan** Short-term regime forecasts from Markov models could let trend models adjust dynamically to reduce late entry and early exit from trends.  #mech/slow_reaction
  > often late to enter a trend and early to leave a trend
  asset: multi · direction: dynamic model weighting · horizon: days · testable: partly - needs forecast accuracy evidence · confidence: low
  ^MT057-C10-2
- **Rich Brennan** Regime prediction is only reliable over a very short horizon (days to a week), like weather forecasts out to about 14 days, and decays quickly afterwards.  #mech/research_method
  > predictive certainty about what's the next Market regime is a very shortterm um finding
  asset: multi · horizon: weeks · conditions: ML and AI methods; beyond one week the accuracy fades · testable: yes - forecast decay test · confidence: medium
  ^MT057-C10-3
- **Rich Brennan** Trend following was previously justified mainly by behavioral-bias narratives; the regime-switching derivation gives a formal statistical rationale linking serial correlation to optimal rule parameters.  #mech/slow_reaction _(added by opus cross-check)_
  > we could explain it in narrative form about behavioral biases and these sort of things that create Trends but now there's a paper suggesting that we can actually get a mathematical formula
  asset: multi · horizon: months · testable: partly - theory statement · confidence: high
  ^MT057-C10-X1

### C11
- **Rich Brennan** To avoid competing with AI, favor medium-to-long-term trends, since the short-term space will become much more competitive as AI improves.  #mech/structural_shift
  > keep away from that short-term space because that short-term space with AI advancements
  asset: multi · direction: medium/long horizon over short · horizon: years · testable: no - forward-looking opinion · confidence: medium
  ^MT057-C11-1
- **Niels Kaastrup-Larsen** Niels speculates the same methods could extend to optimal position sizing, and says his firm already uses dynamic parameter selection.  #mech/risk_management
  > maybe it could calculate what what would the optimal position size be at any given time
  asset: multi · testable: no - speculation · confidence: low
  ^MT057-C11-2
- **Niels Kaastrup-Larsen** Technology advances repeatedly predicted the end of trend following, yet core rules have worked for 50 years; AI is a helpful tool, not a revolution.  #mech/structural_shift
  > Trend following following the core principles that we always come back to uh still seems to be working very well
  asset: multi · horizon: years · testable: partly - long-run trend index · confidence: medium
  ^MT057-C11-3
- **Niels Kaastrup-Larsen** Niels cautions that analytically 'optimal' parameters cannot be a holy grail; if everyone could derive them the edge would not hold, so the result supports but does not settle parameter choice.  #mech/research_method _(added by opus cross-check)_
  > it almost sounds like the Holy Grail right everyone who these could then end up with the optimal uh parameters which of course we know is not going to be the case
  asset: multi · testable: no - caveat · confidence: medium
  ^MT057-C11-X1

### C12
- **Rich Brennan** Medallion operates on one-day to one-week horizons using many data sources and Markov models with a top-level allocator by market state.  #mech/structural_shift
  > operates um particularly in the shortterm time frame you know from one day to one week
  asset: multi · horizon: days · testable: no - external claim about a private fund · confidence: low
  ^MT057-C12-1
- **Niels Kaastrup-Larsen** Niels questions why the same technology did not beat benchmarks for Renaissance external funds.  #mech/research_method
  > why is it that they could make so much money in Medallion but they couldn't make any money for their external clients
  asset: equities · testable: no - anecdotal · confidence: medium
  ^MT057-C12-2
- **Rich Brennan** The Baum-Welch algorithm (Leonard Baum, Renaissance) is the estimation method needed to fit hidden Markov regime models, which Renaissance used from its code-breaking origins.  #mech/research_method _(added by opus cross-check)_
  > Lenny Bal who is responsible for what they call the Bal Welsh algorithm which is necessary for these Markoff processes
  indicator: Baum-Welch HMM estimation · asset: multi · testable: partly - method reference · confidence: medium
  ^MT057-C12-X1

### C13
- **Rich Brennan** Short-term high-alpha models have capacity limits from market impact; the scalable external equity fund used medium-to-long-term trend models and performed only marginally.  #mech/risk_management
  > he knew he couldn't add any more aom to his existing models because the market impact of those models would get too significant
  asset: equities · horizon: days · conditions: larger AUM raises market impact · testable: partly - capacity arguments · confidence: medium
  ^MT057-C13-1
- **Rich Brennan** AI will quickly take over short-term prediction, but CTAs have the advantage in medium-to-long-term trends; mean reversion and HFT are more at risk.  #mech/structural_shift
  > in the medium to long-term space I honestly think that if there's anyone out here who's got a competive Advantage news it's us the ctas
  asset: multi · direction: trend following over mean reversion and HFT · horizon: years · testable: no - opinion · confidence: medium
  ^MT057-C13-2
- **Niels Kaastrup-Larsen** Trend following works only when diversified across many markets and sectors; single-market trend following does not work.  #mech/risk_management
  > if there's one thing you shouldn't do is to do Trend following on a single sector uh or single Market it doesn't work
  asset: multi · testable: yes - diversification backtest · confidence: high
  ^MT057-C13-3
- **Rich Brennan** Rich doubts that Markov/AI forecasting methods work at medium-to-long horizons because uncertainty compounds, so their edge is confined to the short term.  #mech/research_method _(added by opus cross-check)_
  > when you're dealing in the medium to long-term space uh for these uh mathematical processes to work I'm a tiny bit doubtful of it because there is so much uncertainty in these markets
  indicator: regime-model forecast accuracy by horizon · asset: multi · horizon: months · conditions: horizons beyond about a week · testable: yes - forecast accuracy decay by horizon · confidence: medium
  ^MT057-C13-X1

