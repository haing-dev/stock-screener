---
source_id: MT079
title: "If Trend Following was an Olympic Sport - Systematic Investor 306"
date: 2024-08-01
channel: "Top Traders Unplugged"
url: 
words: 11358
claims: 51
added_by_opus: 0
corrections: 0
crosscheck: "pending"
speakers: ["Mark rinsky (guest, Systematic Investor co-host, rules-based investor)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# If Trend Following was an Olympic Sport - Systematic Investor 306

**Speakers:** Mark rinsky (guest, Systematic Investor co-host, rules-based investor); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Weekly trend-following chat (July 2024): Treasury bill issuance as offset to QT, trend giveback and calm-regime risk, market add/drop rules, how to read backtests and build systems, stock-bond correlation, GIC/JPM paper placing trend following as loss mitigation, caution on LLM/ML, and law of small numbers.

**Approach:** trend following, CTA portfolio construction, backtesting, macro liquidity

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, Olympic analogy; nothing actionable |
| C02 | 3 | Treasury bill issuance offsets Fed (Hudson Bay paper) |
| C03 | 4 | issuance rule of thumb, trend giveback, calm regimes |
| C04 | 4 | cost of crisis alpha, July 2024 trend performance |
| C05 | 4 | when to add/remove markets |
| C06 | 6 | market selection criteria, vol floors, cocoa |
| C07 | 3 | cocoa, vol targeting in pegs, backtest value |
| C08 | 4 | backtest to system/factory, Sharpe anecdote |
| C09 | 4 | three components of a system, simple rules, risk management |
| C10 | 3 | stocks vs bonds, correlation risk |
| C11 | 3 | GIC/JPM hedge fund framework |
| C12 | 2 | trend following fits the framework |
| C13 | 3 | Stocks Crisis and False Alarms; prices as null |
| C14 | 3 | price action vs data; LLM and ML caveats |
| C15 | 3 | tech revolutions, public to private information |
| C16 | 2 | law of small numbers; outro |
| C17 | 0 | outro and sponsor; nothing actionable |

## Claims

### C02
- **Mark rinsky** Heavy Treasury bill issuance relative to coupons acts as de facto QE that offsets Fed tightening, which helps explain strong US growth, slow disinflation and easy financial conditions.  #mech/policy_reaction _(time-bound view)_
  > the activist treasury issuance of more more bills than coupons has had an impact of providing quantitative uh easing that's offset what the FED has been doing
  indicator: bill vs coupon issuance share (Hudson Bay paper) · asset: rates · direction: easier financial conditions, lower long yields · horizon: months · conditions: while Treasury skews issuance to bills · testable: yes: Treasury issuance composition is public · confidence: medium
  ^MT079-C02-1
- **Mark rinsky** Bills are near-money and usable as collateral, so more bills adds money-like assets, while fewer coupons makes risky long-duration supply scarcer and lowers long-term rates.  #mech/liquidity_flows
  > so if you issue more uh bills it's as if you're issuing more money
  indicator: bill share of issuance; coupon supply · asset: rates · direction: long yields down when coupon supply falls · horizon: months · testable: partly: transmission channel hard to isolate · confidence: medium
  ^MT079-C02-2
- **Mark rinsky** The 2016 money market fund rules raised structural demand for short-term instruments, so Treasury has room to issue more bills.  #mech/structural_shift
  > there's a greater demand for treasury bills because of the way we've changed the regulations on U money market funds that came around in 2016
  indicator: money market fund assets · asset: rates · horizon: years · testable: yes · confidence: medium
  ^MT079-C02-3

### C03
- **Mark rinsky** Treasury's rule of thumb is about 15% bills, but actual issuance has been much higher, shifting supply versus demand along the curve.  #mech/policy_reaction _(time-bound view)_
  > we'll do about 15% in bills and the rest in coupons they've done numbers that are much higher on the on the bill side
  indicator: bills as % of issuance · asset: rates · horizon: months · testable: yes · confidence: medium
  ^MT079-C03-1
- **Niels Kaastrup-Larsen** Trend followers gave back performance for three months through July 2024, which strains investor conversations but may open entry points.  #mech/cycle_persistence _(time-bound view)_
  > somewhat Relentless giveback of performance that Trend followers have experienced in the past three months and actually it continued in July
  indicator: CTA performance · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT079-C03-2
- **Niels Kaastrup-Larsen** If macro calms again (inflation and rates controlled), trend followers may struggle as in the decade to 2019.  #mech/policy_reaction _(time-bound view)_
  > might have a bit of a struggle like they had in the uh the 10 years uh leading into 2019 where everything was well controlled by central banks
  indicator: inflation, rate volatility · asset: multi · horizon: years · conditions: calm central-bank-controlled macro · testable: partly: regime comparison is loose · confidence: low
  ^MT079-C03-3
- **Niels Kaastrup-Larsen** Drawdowns in trend following offer entry points because too few investors hold it.  #mech/behavioral _(time-bound view)_
  > it also opens up for some great entry points because still around you know in terms of investors there are still way too few who have exposure to Trend filling
  asset: multi · direction: allocate to trend following after drawdown · horizon: years · testable: partly · confidence: medium
  ^MT079-C03-4

### C04
- **Mark rinsky** The cost of crisis alpha and low correlation is poor performance in calm, sideways markets with lower rate and inflation volatility, and investors forget the crisis benefits when rebalancing.  #mech/risk_premium
  > the cost with that of having low correlation is the fact that when there is calm periods in the market such as when uh where we have interest rates have volatility has come down
  indicator: trend following vs volatility regime · asset: multi · direction: trend following weak in calm markets · horizon: months · conditions: low rate/inflation vol, sideways markets · testable: yes: performance by vol regime testable · confidence: high
  ^MT079-C04-1
- **Niels Kaastrup-Larsen** In July 2024 trend followers suffered reversals across currencies (yen strength), equities, metals, energy and bonds, a transition period.  #mech/cycle_persistence _(time-bound view)_
  > currencies have been uh as far as I can tell has been hit pretty hard not least from the the strength the new found strength of the Japanese uh Yen
  indicator: USDJPY and cross-asset reversals · asset: multi · horizon: weeks · conditions: trend reversals · testable: yes · confidence: medium
  ^MT079-C04-2
- **Niels Kaastrup-Larsen** A Trend barometer of 36 indicates a weak environment and negative month for trend followers.  #mech/cycle_persistence _(time-bound view)_
  > my own Trend barometer closed yesterday at 36 that's weak it's not super weak but it is weak
  indicator: Trend barometer (Niels' own) · asset: multi · horizon: weeks · testable: yes: barometer defined by host · confidence: medium
  ^MT079-C04-3
- **Niels Kaastrup-Larsen** In July 2024 trend indices were down about 1.5-2.2% for the month and up about 5-6% YTD; MSCI World up about 10% YTD and the bond index slightly down.  #mech/cycle_persistence _(time-bound view)_
  > St gen CTA index down 2.19% in July up 4.91% uh for the year
  indicator: BTOP50, SG CTA, SG Trend, SG Short-term Traders; MSCI World; S&P Global Developed Sovereign Bond · asset: multi · horizon: months · testable: yes: public index data · confidence: high
  ^MT079-C04-4

### C05
- **Mark rinsky** Do not drop a market from a trend portfolio just because it lost money for years: it may be a diversifier whose future is unknown.  #mech/research_method
  > if let's say a a market has been trading poorly over the last few years that doesn't mean it's going to trade poorly going forward
  indicator: market-level past performance · asset: multi · horizon: years · testable: yes: removal rules can be backtested · confidence: high
  ^MT079-C05-1
- **Mark rinsky** Dropping short-term interest rate markets near the zero bound would have been wrong because rates went negative; one-sided-market assumptions fail.  #mech/research_method
  > rates are never going to go below zero so therefore uh and if we're getting close to the zero bound let's of course drop that market
  indicator: short-term interest rate futures near zero bound · asset: rates · horizon: years · testable: yes · confidence: high
  ^MT079-C05-2
- **Mark rinsky** Central-bank-intervention markets (managed FX) that punish speculators justify lower exposure.  #mech/policy_reaction
  > central banks actually intervene because they want to punish speculators
  indicator: managed currencies · asset: fx · direction: reduce exposure · horizon: years · conditions: central bank not profit-maximizing · testable: partly · confidence: medium
  ^MT079-C05-3
- **Mark rinsky** Market selection criteria: two-sided markets with hedgers and speculators; markets with only speculators are a problem.  #mech/research_method
  > you want to have two-sided markets where you have hedgers and both speculators if it's pure speculative then that could be a a problem
  indicator: hedger participation · asset: multi · testable: partly: hedger share via COT data · confidence: medium
  ^MT079-C05-4

### C06
- **Mark rinsky** Markets with only professional traders (little retail) are harder to make money in.  #mech/crowding_positioning
  > all professional Traders it's going to be harder to make money
  indicator: participant mix · asset: multi · testable: partly · confidence: medium
  ^MT079-C06-1
- **Mark rinsky** Drop markets when volume or open interest fall below minimums, because illiquidity brings jump risk; avoid brand-new markets.  #mech/risk_management
  > the volume starts to fall below a certain threshold or open interest Falls I'd want to drop it out because uh because then then you could get more likely a jump risk which could work against you
  indicator: volume and open interest minimums · asset: multi · testable: yes: thresholds testable · confidence: high
  ^MT079-C06-2
- **Mark rinsky** When reviewing a market, check how it earned (one trade or many, choppiness) rather than whether it made money.  #mech/research_method
  > not so much if it makes money or loses money but how it makes the money and lose the money is it all coming with a single trade
  indicator: trade-level P&L concentration · asset: multi · testable: yes · confidence: medium
  ^MT079-C06-3
- **Niels Kaastrup-Larsen** Use volatility floors and multiple lookbacks so that suppressed volatility (Swiss franc, short rates) does not lead to oversized positions.  #mech/risk_management
  > there you have to have some safeguards some volatility flaws that you know doesn't prevent you is the word I'm looking for here prevents you from sizing up and and getting really badly hurt
  indicator: volatility floor; multi-horizon volatility · asset: multi · conditions: pegged or administered markets · testable: yes: vol-floor effect can be backtested · confidence: high
  ^MT079-C06-4
- **Niels Kaastrup-Larsen** Cocoa was unprofitable for trend followers for 15-20 years and then turned extremely profitable in 2023-24, so removing markets for past losses is dangerous.  #mech/research_method _(time-bound view)_
  > Coco literally was not profitable as far as I can tell for the last 15 or 20 years prior to the beginning of January 2023
  indicator: cocoa trend returns · asset: commodities · horizon: years · testable: yes · confidence: high
  ^MT079-C06-5
- **Niels Kaastrup-Larsen** A market that makes little money but pays when others lose still adds diversification value.  #mech/risk_management
  > there's nothing wrong with having a market that doesn't really make money for you if it makes money when a lot of other things is not making money for you in your portfolio
  indicator: market-level diversification · asset: multi · horizon: years · testable: yes: marginal contribution testable · confidence: medium
  ^MT079-C06-6

### C07
- **Mark rinsky** An index excluding cocoa (Credit Suisse managed futures index) underperformed CTAs that held cocoa; few markets are dropped except for liquidity.  #mech/research_method _(time-bound view)_
  > it underperformed relative to a lot of ctas who did have Coco
  indicator: cocoa in CTA portfolios · asset: commodities · horizon: months · testable: yes · confidence: high
  ^MT079-C07-1
- **Mark rinsky** Volatility targeting increases size when volatility is artificially low (Swiss franc peg), which was the worst action when the peg broke.  #mech/risk_management
  > I will increase my exposure in those markets that have low volatility and then if let's say there is a spike in volatility I could be on a wrong wrong-sided on that market
  indicator: realised volatility in pegged markets · asset: fx · horizon: days · conditions: pegged or manipulated markets · testable: yes · confidence: high
  ^MT079-C07-2
- **Mark rinsky** Backtests are valuable not for performance or Sharpe (all look good) but for insight into the manager's care in research and treatment of transaction costs and realism.  #mech/research_method
  > I've never seen a bad back test in terms of performance and sharp
  indicator: backtest assumptions · asset: multi · testable: partly · confidence: high
  ^MT079-C07-3

### C08
- **Mark rinsky** Due diligence should ask about backtest assumptions and costs to judge the manager's rigour.  #mech/research_method
  > you get insight into the manager in terms of how careful he is with his uh with his research how careful he is at being able to account for all of the realism in the market
  asset: multi · testable: partly · confidence: high
  ^MT079-C08-1
- **Mark rinsky** Anyone can build a good model; what matters is applying it across many markets, building portfolios and a full system.  #mech/research_method
  > how does someone build a system not a model and there's a difference between the two I can always come up with a good model
  asset: multi · testable: no · confidence: high
  ^MT079-C08-2
- **Mark rinsky** Move from backtest (laboratory) to factory: inputs, outputs, timing, costs, and execution must be realistic.  #mech/research_method
  > you have to take off your scientist hat you have to put on the hat of an engineer and then you have to say I am building a factory
  asset: multi · testable: partly · confidence: high
  ^MT079-C08-3
- **Mark rinsky** Investors' Sharpe thresholds conflict (one rejects below 2, another above 1.25), so research process matters more than the numbers.  #mech/research_method
  > I would say it's the process of how you do your research which is more important than the actual numbers you generate
  indicator: backtest Sharpe ratio · asset: multi · testable: no · confidence: medium
  ^MT079-C08-4

### C09
- **Mark rinsky** Evaluate systematic managers by return generation, portfolio construction and risk management.  #mech/research_method
  > any portfolio you build has to be related to three components one what is the process for return generation two what is the portfolio construction and what is the risk management
  asset: multi · testable: partly · confidence: high
  ^MT079-C09-1
- **Mark rinsky** Regression or model-based signals risk parameter instability, so simple rules are preferred.  #mech/research_method
  > if it's more regression based or it's model based then there's a potential for parameter un uh instability in some sense you you actually like simple rules
  indicator: signal complexity · asset: multi · testable: yes: parameter stability testable · confidence: high
  ^MT079-C09-2
- **Mark rinsky** Portfolio construction (diversification) is the one free lunch available.  #mech/risk_management
  > that's where you're getting the only free lunch available in finance which is diversification
  indicator: diversification · asset: multi · testable: yes · confidence: high
  ^MT079-C09-3
- **Mark rinsky** Risk management belongs in the model's entry and exit rules, with a stop loss as a fail-safe protecting investor principal.  #mech/risk_management
  > a good model should incorporate uh risk management in the portfolio construction and decision rules that you determine when to get long but then you also have a uh determination of when to exit
  indicator: stop loss · asset: multi · testable: yes · confidence: high
  ^MT079-C09-4

### C10
- **Mark rinsky** When valuation and the rate outlook give compelling reasons for both stocks and bonds, follow price trends instead.  #mech/slow_reaction _(time-bound view)_
  > perhaps the best way to approach it is to look at this from a trend following perspective and let the prices themselves tell you what you should do
  indicator: price trend · asset: multi · direction: follow trend in stocks and bonds · horizon: months · conditions: when fundamental case is ambiguous · testable: yes · confidence: medium
  ^MT079-C10-1
- **Mark rinsky** If stock-bond correlation turns positive, 60/40 volatility rises and bonds lose their diversification role, so risk should be monitored via the off-diagonal covariance terms.  #mech/risk_management
  > if correlations change on you and if correlation especially if you have the classic 6040 portfolio it turns positive is is that you're really going to get a lot more volatility in your overall portfolio
  indicator: stock-bond correlation · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT079-C10-2
- **Niels Kaastrup-Larsen** The one-year rolling stock-bond correlation was at a multi-year high in mid-2024, exposing portfolios to higher risk.  #mech/structural_shift _(time-bound view)_
  > the one-year rolling correlation is actually at the highest it's been in a very very long time
  indicator: one-year rolling stock-bond correlation · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT079-C10-3

### C11
- **Mark rinsky** When stock-bond correlation is positive, bonds are no longer diversifiers and the choice becomes relative valuation.  #mech/risk_premium
  > to really start to think about valuation because uh then it's a relative return situation not a diversification question
  indicator: relative valuation of stocks vs bonds · asset: multi · conditions: positive correlation · testable: partly · confidence: medium
  ^MT079-C11-1
- **Mark rinsky** GIC/JPMorgan paper classifies hedge fund strategies into loss mitigation, equity diversifiers, equity complements and equity substitutes.  #mech/research_method
  > there's loss mitigation strategies equity diversifiers and we'll call Equity complements and Equity substitutes
  indicator: hedge fund strategy buckets · asset: multi · testable: yes · confidence: high
  ^MT079-C11-2
- **Mark rinsky** Classify strategies by equity correlation, drawdown mitigation relative to equities, and alpha after beta.  #mech/research_method
  > one you want to look at what's the correlation with equities
  indicator: correlation to equities, relative drawdown, alpha · asset: multi · testable: yes · confidence: high
  ^MT079-C11-3

### C12
- **Mark rinsky** In the GIC/JPM framework managed futures ranked second for alpha after beta and global macro first.  #mech/structural_shift
  > lo and behold bage Futures is probably number two number one was uh was a global ma Global macro
  indicator: alpha after beta by strategy · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT079-C12-1
- **Mark rinsky** Trend following meets all three criteria (low equity correlation, drawdown mitigation, positive alpha); not an equity substitute.  #mech/structural_shift
  > if you look at what is the strategy that seems to fit within that it's probably Trend following on all three of those counts
  indicator: trend following · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT079-C12-2

### C13
- **Mark rinsky** Being wedded to one model produces false alarms, e.g. post-GFC QE did not cause rampant inflation; entertain alternatives.  #mech/research_method
  > we often use judgment that's you know wedded in a specific model or school of thought
  asset: multi · horizon: years · testable: no · confidence: high
  ^MT079-C13-1
- **Mark rinsky** Doomsday macro forecasts are often wrong; Covid saw a sharp drop but a fast recovery, better than expected.  #mech/behavioral
  > we have a lot of of of macroeconomists or are doomsday or is is they they they make their bones by uh by suggesting that the world is going to come to an end
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT079-C13-2
- **Mark rinsky** Use prices as the null hypothesis and let prices speak before departing.  #mech/research_method
  > prices are Primal and use prices as your sort of your null hypothesis
  indicator: price · asset: multi · testable: no · confidence: high
  ^MT079-C13-3

### C14
- **Mark rinsky** Don't chase data releases such as PCE; the price reaction to the data is what drives positions.  #mech/slow_reaction
  > what's the price action that you see in markets in the next couple of days and that's going to be what the real driver
  indicator: price reaction to macro data · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT079-C14-1
- **Mark rinsky** A paper found LLMs add little to time series forecasting, so model building is harder than expected.  #mech/research_method _(time-bound view)_
  > they looked at llm large language model uh models and they tied it to time series
  indicator: LLM time-series forecasts · asset: multi · testable: yes · confidence: medium
  ^MT079-C14-2
- **Mark rinsky** Machine learning performs well in expansions but poorly in recessions because training data has few recession periods.  #mech/research_method
  > she learning does pretty well during up parts of the business cycle but then when you hit the down uh the downdraft when you hit a recession
  indicator: ML performance across business cycle · asset: multi · conditions: recessions · testable: yes · confidence: medium
  ^MT079-C14-3

### C15
- **Niels Kaastrup-Larsen** Every technology wave in 30 years was predicted to hurt trend following, and it has not.  #mech/structural_shift
  > people were quick to to kind of state that this would have a negative impact on Trend following
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT079-C15-1
- **Mark rinsky** Prices are public and discounted rapidly, so models and new techniques are valuable only if they turn the same public data into private insight others do not have.  #mech/research_method
  > the purpose of building models is to take public information which could be past prices or macro data and then we want to turn it into private information
  asset: multi · testable: no · confidence: high
  ^MT079-C15-2
- **Mark rinsky** Adopting new techniques should be gradual, not a binary switch from old to new models.  #mech/research_method
  > the answer is not going to be digital like like we just need to switch and it's an onoff switch that we should go from one set of models to a new set of models
  asset: multi · testable: no · confidence: medium
  ^MT079-C15-3

### C16
- **Mark rinsky** Law of small numbers: extrapolating from small samples, which affects trend and quant models that decide on limited data, so check sample size and distribution.  #mech/behavioral
  > we often extrapolate from a small sample on what we might think what will happen in the in the future as opposed to using a very large sample
  indicator: sample size in model decisions · asset: multi · testable: yes · confidence: high
  ^MT079-C16-1
- **Mark rinsky** Gambler's fallacy and hot hand: knowing the distribution implies mean reversion, not knowing it implies following the hot hand.  #mech/behavioral
  > if you know the distribution then you probably you're always going to be a uh a mean reverter if you don't know the distribution then you might sort of follow the hot hand
  asset: multi · testable: partly · confidence: medium
  ^MT079-C16-2

