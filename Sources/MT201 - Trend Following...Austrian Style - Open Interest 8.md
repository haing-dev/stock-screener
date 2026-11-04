---
source_id: MT201
title: "Trend Following...Austrian Style - Open Interest 8"
date: 2024-06-23
channel: "Top Traders Unplugged"
url: 
words: 7451
claims: 38
added_by_crosscheck: 4
corrections: 1
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Michael nobow (SMN co-founder, Vienna CTA)", "Joseph valin (SMN head of quant research and risk)", "Moritz seibert (host)"]
tags: [source, layer0]
---
# Trend Following...Austrian Style - Open Interest 8

**Speakers:** Michael nobow (SMN co-founder, Vienna CTA); Joseph valin (SMN head of quant research and risk); Moritz seibert (host)

**Summary:** Austrian CTA SMN (27-year track record) describes agnostic medium/long-term trend following over 200 markets incl. exotic and synthetic ones. Dispersion among CTAs comes from universe and position sizing more than signals. Conclusion: stay symmetric long/short, avoid overfitting, diversify into low-liquidity markets after realistic costs.

**Approach:** trend following, diversification, market universe, risk management, CTA

**Cross-check completeness estimate of first read:** 0.90 - the first reader caught nearly every method and mechanism claim; only the robustness rationale for choosing trend following, the capacity argument, the sector/single-name equity idea and the volatility-is-non-directional rationale were missed.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro, outliers assumption |
| C02 | 0 | background, SMN origin story, no method content |
| C03 | 0 | origin of firm, hybrid discretion experiment mention |
| C04 | 3 | discretion experiment failed, sources of dispersion |
| C05 | 5 | biased signals, symmetric long/short, risk definition start |
| C06 | 3 | risk targeting, risk budgets, universe |
| C07 | 6 | diversification, synthetics, alternative markets rationale |
| C08 | 6 | research of illiquid markets, slippage, alpha |
| C09 | 4 | execution algos, synthetic markets, equity ideas |
| C10 | 4 | VIX handling, future of trend following |
| C11 | 2 | outliers cannot be arbitraged, lost decade, close |

## Claims

### C01
- **Michael nobow** Trend following needs no forecast; it only assumes that a broad portfolio will contain some large trend outliers over time, so direction and timing of the next one need not be known.  #mech/cycle_persistence
  > there's only one assumption behind the concepts and this assumption is a broadly Diversified portfolio will have a certain amount of train outliers over time
  asset: multi · direction: long/short follow trend · horizon: years · conditions: needs broad market diversification · testable: partly - outlier frequency can be measured but is the assumption itself · confidence: high
  ^MT201-C01-1

### C03
- **Michael nobow** SMN chose trend following (after testing technical indicators on the bank desk) because it was the concept it found most robust, with the Turtles' and local CTAs' success as extra motivation.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > it was the the concept that we where we found the highest robustness
  indicator: trend following robustness · asset: multi · direction: trend following over other technical approaches · testable: no - biographical rationale, not independently testable · confidence: medium
  ^MT201-C03-X1

### C04
- **Michael nobow** Adding discretionary overlays was tested only in a side fund, never in the flagship, because changing style in a live track record is to be avoided; the discretionary plus systematic mix failed.  #mech/research_method
  > this would have been a style shift and this is something you should never do
  asset: multi · testable: no - governance statement · confidence: high
  ^MT201-C04-1
- **Joseph valin** Dispersion among trend-following CTAs is explained more by market universe and position-sizing logic than by signal design.  #mech/research_method
  > the Universe and the position sizing logic they have more weight in differentiation than the third
  indicator: CTA return dispersion · asset: multi · testable: partly - could be tested with CTA fund data · confidence: medium
  ^MT201-C04-2
- **Joseph valin** Position sizing choices that differ across managers include constant versus flexible risk targeting and whether sizing uses only signal direction or the signal value.  #mech/risk_management
  > constant versus flexible risk targeting is one big issue
  asset: multi · testable: yes - alternative sizing rules can be backtested · confidence: high
  ^MT201-C04-3

### C05
- **Joseph valin** Some CTAs bias signals toward long positions in bonds and equities, which is another source of dispersion in trend following results.  #mech/research_method
  > giving more weight to long where the short signals for instance in the fixed income world or in the equity world
  asset: multi · testable: yes - long-only versus symmetric tilt can be backtested · confidence: high
  ^MT201-C05-1
- **Moritz seibert** Over the last 30-40 years long trades in equity and bond trend following beat short trades, while currencies and commodities show a different pattern; this is a sample-specific effect of secular bull markets.  #mech/structural_shift _(time-bound view)_
  > the long- sided trades and equities and bonds have been performing so much better than the shortsighted trades
  asset: multi · direction: long equities and bonds outperformed short · horizon: years · testable: yes - split trend returns by long and short side · confidence: medium
  ^MT201-C05-2
- **Michael nobow** Tilting signals to what worked in the past (for example removing short signals) is overfitting; SMN keeps equal risk on long and short signals in every market.  #mech/research_method
  > we try not to over optimize and and and this this is really dangerous because what works in the past probably doesn't work in the future
  asset: multi · direction: symmetric long/short · testable: partly - cannot prove out of sample absence of change · confidence: high
  ^MT201-C05-3
- **Michael nobow** Cocoa, historically a negative-return trend market, was the best CTA market in 2024, showing that the location of the next outlier cannot be predicted from history.  #mech/cycle_persistence _(time-bound view)_
  > this year the best Market in a uh CTA portfolio was uh the market Coco this is a market that was produced more or less always negative returns over time
  indicator: cocoa trend return · asset: commodities · horizon: years · testable: partly - single anecdote · confidence: high
  ^MT201-C05-4
- **Michael nobow** Removing short signals would improve a backtest during 30 years of bull markets in bonds and equities but would destroy the crisis alpha that trend following is expected to deliver.  #mech/risk_management
  > one of the characteristics of of ctas is that they are able to produce the the crisis alha
  asset: multi · direction: keep shorts in equities and bonds · conditions: crisis periods · testable: yes - compare long-only and long/short trend in drawdowns · confidence: high
  ^MT201-C05-5

### C06
- **Joseph valin** Volatility target is an annualised standard deviation goal met on average over the long run; the portfolio is not re-levered on days with few signals.  #mech/risk_management
  > we do not Target the overall um risk goal in terms of an deviation goal on a daily basis just on average long-term Bas
  indicator: annualised standard deviation target · asset: multi · direction: no re-levering when few signals · horizon: years · testable: yes - compare constant versus flexible risk targeting · confidence: high
  ^MT201-C06-1
- **Joseph valin** Each position has a risk budget or stop limit to control drawdown, complementing the symmetric standard deviation target with an asymmetric drawdown control.  #mech/risk_management
  > we have assigned stop loss limits for each or risk budgets for each position we're trading for each signal we are trading
  indicator: per-position risk budget · asset: multi · testable: yes - position-level stop rule can be backtested · confidence: high
  ^MT201-C06-2
- **Joseph valin** When a market makes a huge move (cocoa) and the exit level lags far below price, positions are cut so one market does not dominate; limits are deliberately broad so ordinary moves do not trigger cuts.  #mech/risk_management
  > the systems react on these developments by U reducing position uh the position size in case of a huge development in in individual price development
  indicator: distance from price to exit level, price volatility · asset: commodities · conditions: only after very large individual price moves · testable: yes - rule can be backtested · confidence: high
  ^MT201-C06-3

### C07
- **Michael nobow** More markets give more chances to catch outlier moves, so SMN began with about 70 markets and kept widening the universe.  #mech/risk_management
  > from the very beginning it was very important for us to diversify the risk by markets
  asset: multi · direction: more markets · testable: yes - breadth versus Sharpe in backtests · confidence: high
  ^MT201-C07-1
- **Michael nobow** Synthetic markets built as baskets or spreads of existing markets create return streams that look different from the underlying and add diversification.  #mech/risk_management
  > if we can produce a curve with uh two that looks different with two other curves then we would get more diversification
  asset: multi · testable: yes - build spreads and measure incremental diversification · confidence: high
  ^MT201-C07-2
- **Michael nobow** SMN dropped short-term systems around 2007-08 and concentrated on medium/long-term trend following as the most robust horizon.  #mech/research_method
  > only concentrate on medium to long term because we thought this is the this is the uh the thing that is most robust over time
  asset: multi · horizon: months · testable: partly - robustness is judgement · confidence: medium
  ^MT201-C07-3
- **Michael nobow** In the 2008 crisis CTAs did well but investors redeemed from them because CTAs were liquid, so crisis alpha did not bring new assets.  #mech/liquidity_flows _(time-bound view)_
  > investors because of the liquidity of CTS uh took out money because they needed it as well
  asset: multi · testable: no - anecdote · confidence: high
  ^MT201-C07-4
- **Michael nobow** Allocators prefer the biggest CTA shops because of career risk, so small firms can differentiate only by trading markets large funds cannot.  #mech/behavioral
  > the career risk for them when they lose money with them is lower
  asset: multi · testable: no - industry structure view · confidence: medium
  ^MT201-C07-5
- **Michael nobow** Alternative (illiquid, regional) markets move on local factors rather than the global risk-on/risk-off regime, so they correlate little with a classic futures portfolio.  #mech/risk_management
  > it's not this typical risk on riskof regime that you have with most of the high highest liquid financial and commodity markets they have their own moves and they don't correlate too much to the rest of the portfolio
  indicator: correlation of alternative markets with classic portfolio · asset: commodities · testable: yes - correlation and Sharpe contribution measurable · confidence: high
  ^MT201-C07-6
- **Michael nobow** Alpha in small alternative markets is capacity-limited: a multi-billion fund can trade them but the allocation is too small to move performance, so only a mid-sized CTA like SMN can use them as a real source of return.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > you can say you trade those markets but uh it doesn't have an effect on the outcome of the portfolio of performance wise
  indicator: fund size vs market liquidity · asset: commodities · direction: alternative markets add return mainly for smaller funds · horizon: years · conditions: needs assets small relative to market liquidity · testable: partly - capacity versus return analysis needs fund-level data · confidence: medium
  ^MT201-C07-X1

### C08
- **Joseph valin** Backtests of illiquid markets use deliberately high slippage assumptions, plus broker execution costs, to avoid overstating results.  #mech/research_method
  > we came up with really huge reasonable but still obviously much more higher slippage numbers incorporating our P testing
  asset: multi · conditions: slippage hard to know ex ante for illiquid markets · testable: yes - cost stress in backtests · confidence: high
  ^MT201-C08-1
- **Joseph valin** After stringent cost assumptions, adding less liquid markets still raises the portfolio Sharpe ratio significantly.  #mech/structural_shift
  > even after accounting for this High number of slippage and transaction costs explicit and implicit transaction cost there is sizable Alpha to capture
  indicator: portfolio Sharpe ratio with and without alternative markets · asset: commodities · testable: yes - incremental Sharpe test with cost stress · confidence: high
  ^MT201-C08-2
- **Joseph valin** Local commodity markets driven by local supply and demand show medium to long-term price cycles that trend systems capture well.  #mech/cycle_persistence
  > the pricing behavior in these less liquid markets is more cycle driven driven because in our case predominantly but not only but PR predominantly commodity markets local commodity markets more driven by local demand and Supply
  asset: commodities · horizon: months · testable: yes - trend profitability by market type · confidence: high
  ^MT201-C08-3
- **Joseph valin** Trends in alternative markets occur at different times from classic-market trends, lowering correlation and improving diversification.  #mech/risk_management
  > these Trends do not happen at the same time than with our classic universe meaning decreasing correlation and increasing diversification
  asset: commodities · testable: yes - correlation of trend returns · confidence: high
  ^MT201-C08-4
- **Joseph valin** SMN has standard rules to judge whether a backtest result is realistic because over-optimisation of the past is the main research risk.  #mech/research_method
  > the biggest enemy in researching is that the over optimization of the past
  asset: multi · testable: partly - rules not stated · confidence: high
  ^MT201-C08-5
- **Joseph valin** Slippage assumed for the smallest markets (nonfat dry milk, cheese) is roughly four to five times that of classic futures.  #mech/risk_management
  > I would assume right now it's really I think uh four to five times larger than the the classical ones
  indicator: assumed slippage multiple · asset: commodities · testable: partly - estimate stated from memory · confidence: low
  ^MT201-C08-6

### C09
- **Joseph valin** Tiny illiquid markets are traded with execution algorithms (TWAP or similar) over a day or two to spread liquidity, with instructions per market.  #mech/liquidity_flows
  > so in these markets we U decided to trade them with with Algos together with our Brokers
  asset: multi · conditions: illiquid markets, positions need more than one session · testable: no - execution practice · confidence: high
  ^MT201-C09-1
- **Joseph valin** The first synthetic markets (2009) were risk-parity baskets of an equity index and a government bond, for example S&P versus 10-year note.  #mech/risk_management
  > risk parity baskets it's a it's basically a combination between an equity
  indicator: equity/bond risk parity basket · asset: multi · testable: yes - basket trend backtest · confidence: high
  ^MT201-C09-2
- **Joseph valin** Correlation spreads between related commodities (New York versus London cocoa, wheat types) are traded as synthetic markets with their own trends; synthetics are roughly 20-25% of risk.  #mech/risk_management
  > a correlation spread we where we trade um two related Commodities like Coco versus London cocoa or different wheat wheat types
  indicator: spread of related commodity contracts · asset: commodities · testable: yes - spread trend backtest · confidence: high
  **Correction (cross-check):** The 20-25% of risk figure for synthetic markets was read out by the host (Moritz, citing a Hedge Fund Journal article), not stated by Joseph; SMN did not confirm the number. → Correlation spreads between related commodities (New York versus London cocoa, wheat types, South African maize and soybeans) are traded as synthetic markets with their own trends; the host cites an article putting synthetics at about 20-25% of SMN's risk budget.
  ^MT201-C09-3
- **Michael nobow** An equal-weighted versus cap-weighted stock index spread could provide a trend market, with an eventual trend outlier in the other direction after the Magnificent Seven run.  #mech/overshoot _(time-bound view)_
  > you could for example make a spread out of uh an equally uh weighted stock index versus uh volume weighted uh stock index
  indicator: equal-weighted minus cap-weighted index · asset: equities · direction: trend either way · horizon: months · testable: yes - spread trend backtest · confidence: low
  ^MT201-C09-4
- **Michael nobow** Breaking equity index futures into sectors or single names would add diversification to a trend portfolio, but SMN has not done it because it would need derivatives (counterparty risk) or a change of the fund prospectus.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > I think there would be a lot of possibilities for higher diversification as well in in our fund
  indicator: sector and single-stock trends · asset: equities · direction: more diversification from sector/single-name trend markets · conditions: fund prospectus and counterparty constraints · testable: partly - needs stock-level data, not tested in the talk · confidence: medium
  ^MT201-C09-X1

### C10
- **Joseph valin** Pure momentum on the VIX behaved poorly in the 2009-2019 lost decade, so SMN built an enhanced momentum model.  #mech/research_method
  > the behavior of the especially asset class volatility in our case you Equity volatility the behavior was not the most optimal one for the way we traded the other markets
  indicator: VIX futures momentum · asset: equities · testable: yes - compare pure and enhanced VIX momentum · confidence: high
  ^MT201-C10-1
- **Joseph valin** Enhanced VIX momentum uses price momentum, the volatility of volatility and the shape of the futures curve (spot versus future volatility).  #mech/slow_reaction
  > we take into account next to the price movement of volatility so the volatility of volatility actually also the shape of future and expected the the uh state of spot and future volatility
  indicator: VIX futures price, vol of vol, term-structure shape · asset: equities · testable: yes - rule can be replicated · confidence: high
  ^MT201-C10-2
- **Joseph valin** VIX positions are monitored on hourly snapshots of the curve with quick intraday exits because volatility can explode.  #mech/risk_management
  > we're moved to basically hourly hourly ticks in order to evaluate the the structure of the the current structure of the volatility
  indicator: VIX futures curve, hourly · asset: equities · horizon: days · testable: yes - needs intraday data · confidence: high
  ^MT201-C10-3
- **Michael nobow** Allocator interest in CTAs follows recent performance: after drawdowns investors say trend following no longer works, after good years they add, a pattern unchanged for 30 years.  #mech/behavioral
  > when you have uh a couple of good years then investors think probably it's a good idea to have a small proportionate portfolios with CTS as well
  asset: multi · testable: partly - flows versus performance data · confidence: medium
  ^MT201-C10-4
- **Joseph valin** Volatility is a non-directional asset class, so SMN argues it needs its own signal design rather than the plain price-momentum rule used for the directional markets.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > the ESS class volatility is really different to all the other more directional ESS classes
  indicator: VIX futures · asset: multi · conditions: VIX trend rule differs from rest of portfolio · testable: partly - compare pure vs enhanced momentum on VIX · confidence: medium
  ^MT201-C10-X1

### C11
- **Michael nobow** Trend following is unlikely to be arbitraged away because large outliers have causes other than CTA trading, though more noise could create more false signals.  #mech/structural_shift
  > arbitraging away this big outliers is impossible because there are other reasons for this then CTA trades
  asset: multi · horizon: years · testable: no - future-looking claim · confidence: medium
  ^MT201-C11-1
- **Michael nobow** The 2009-2020 lost decade (zero rates, QE) had few outliers, was artificial, and long quiet periods are followed by bigger-than-average moves, as seen now.  #mech/policy_reaction _(time-bound view)_
  > if it takes for a long time if the markets have for a long time no substantial moves then they are prepared having even bigger moves than uh on average after this period
  asset: multi · horizon: years · conditions: after long low-volatility periods · testable: partly - few historical episodes · confidence: medium
  ^MT201-C11-2

