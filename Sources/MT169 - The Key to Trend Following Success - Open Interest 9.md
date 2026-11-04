---
source_id: MT169
title: "The Key to Trend Following Success - Open Interest 9"
date: 2024-07-15
channel: "Top Traders Unplugged"
url: 
words: 8420
claims: 27
added_by_crosscheck: 8
corrections: 0
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Moritz Seibert (host, Open Interest series)", "Cole Wilcox (CEO, Longboard Asset Management, single-stock trend following)"]
tags: [source, layer0]
---
# The Key to Trend Following Success - Open Interest 9

**Speakers:** Moritz Seibert (host, Open Interest series); Cole Wilcox (CEO, Longboard Asset Management, single-stock trend following)

**Summary:** Wilcox runs long-only, unleveraged trend following on about 2,500 US mid/small-cap stocks (Russell 3000 minus the top 100), holding 300-600 names. Edge: stock returns are a power law (4% of stocks create all wealth), so avoiding losers and catching every winner plus drawdown control gives lower beta, lower drawdown and similar compounding; breadth is chosen to minimise luck dispersion.

**Approach:** single-stock trend following, power law returns, long-only, drawdown control, breadth vs concentration, behavioral discipline

**Cross-check completeness estimate of first read:** 0.82 - the first reader captured the power-law thesis, universe, breadth/luck argument, volatility drag and behavioural alpha well; missed several operational and design points (index-trend left-tail value, equal-risk weighting, continuous risk-target rebalancing, cash-flow handling, rejection of securities lending and single-stock futures, Moritz's dilution counterpoint, complement vs replace).

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, Longboard background and sector aims |
| C02 | 2 | origin: trend on stocks after 2000-02 crash; goal is lower risk not zero correlation |
| C03 | 1 | universe (Russell 3000 minus top 100), rules, sources of alpha |
| C04 | 3 | power-law 96%/4% stat; avoid losers; downside risk management; beta lower |
| C05 | 3 | why long-only; correlation about 0.55 to S&P; US vs international |
| C06 | 2 | power law universal; index futures trend misses small caps; funding |
| C07 | 1 | fully funded, risk-weighted sizing with leverage cap; rebalancing and dividends |
| C08 | 1 | securities lending declined; single-stock futures; small/mid cap failure rates and outliers; holdings count |
| C09 | 1 | 300-600 names; breadth vs concentration luck dispersion |
| C10 | 3 | variance drain and behavioural alpha; avoiding 50% drawdowns |
| C11 | 1 | tortoise and hare; fit in client portfolios; correlation zero tradeoff |
| C12 | 1 | all-weather as investor satisfaction; lessons: stick to the process |
| C13 | 0 | outro |

## Claims

### C02
- **Cole Wilcox** Trend following was dominant in futures but not applied to stocks; after the 2000-02 tech wreck (market -50%) the firm researched trend on single stocks.  #mech/research_method
  > how come Trend following which was such a dominant kind of philosophy for a lot of these uh managers in the space uh wasn't being applied to like an a better Equity Mouse trrap
  asset: equities · horizon: years · testable: yes - published research · confidence: medium
  ^MT169-C02-1
- **Cole Wilcox** Objective differs from managed futures: reduce equity risk and drawdown while keeping equity-like returns rather than minimise correlation to equities.  #mech/risk_management
  > we're not trying to optimize for low correlation per se we're trying to optimize for lower risk investing lower draw down investing without sacrificing what you would otherwise get as being an equity investor
  asset: equities · horizon: years · testable: yes · confidence: high
  ^MT169-C02-2

### C03
- **Cole Wilcox** Universe: Russell 3000 minus the top 100 caps and illiquid micro-caps, leaving about 2,200-2,500 active mid/small caps; entry on price trend breakouts, equal risk per trade, exit on stops.  #mech/structural_shift
  > the top 50th percentile of market cap which eliminates up you know roughly the S&P 100
  indicator: Russell 3000 ex top 100 universe · asset: equities · direction: long only · testable: yes - backtest · confidence: high
  ^MT169-C03-1

### C04
- **Cole Wilcox** Stock returns are a power law (Bessembinder, 'capitalism distribution'): 96% of listed firms underperform T-bills, 4% create all wealth, so odds of picking a winner are low and avoiding losers matters.  #mech/research_method
  > 96% of companies that have ever been public generated returns that were worse than T bills collectively and the remaining 4% are responsible for 100% of the stock market's wealth creation
  indicator: distribution of stock returns · asset: equities · horizon: years · testable: yes - published study · confidence: high
  ^MT169-C04-1
- **Cole Wilcox** About 40% or more of Russell 2000 companies are unprofitable; avoiding them is a source of alpha versus index funds.  #mech/structural_shift _(time-bound view)_
  > I think right now maybe 40% or more of those companies are unprofitable and don't make money
  indicator: share of unprofitable small caps · asset: equities · direction: avoid loser stocks · testable: yes · confidence: medium
  ^MT169-C04-2
- **Cole Wilcox** Systematic downside risk management gives trend following a lower-beta, lower-volatility portfolio that still outperforms the index on long-term compounding.  #mech/risk_management
  > we're actively managing risk on the downside actively managing controlling draw down
  indicator: trend exits, beta · asset: equities · horizon: years · testable: yes · confidence: high
  ^MT169-C04-3

### C05
- **Cole Wilcox** Long-only chosen over long-short or market-neutral because investors want to swap equity beta for lower-risk equity beta with limited tracking error.  #mech/research_method
  > our particular strategy is very much formulated for the needs of our investor base and they're really
  asset: equities · testable: no - product design · confidence: medium
  ^MT169-C05-1
- **Cole Wilcox** Correlation of the strategy to the S&P 500 is about 0.55, low versus long-only but not versus managed futures or gold.  #mech/risk_management
  > you know you're kind of in like the point uh 55 Zone
  indicator: correlation to S&P 500 · asset: equities · horizon: years · testable: yes · confidence: high
  ^MT169-C05-2
- **Cole Wilcox** Tests on international stocks show the same effect; US focus is a product choice for US advisors.  #mech/research_method
  > it's just as effective
  asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT169-C05-3
- **Moritz Seibert** Equal-risk weighting across thousands of stocks avoids the concentration of a cap-weighted index in whatever sector dominates (tech now, energy 20 years ago) and thereby lowers correlation to broad equity beta; Cole agrees correlation is lower than long-only but not near zero.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > you're more like an equally weighted or equally risk weighted allocation to the equity space wouldn't that break up some of the correlation in the beta that you have to the overall Market already
  indicator: equal-risk weighted single-stock trend portfolio vs cap-weighted index · asset: equities · direction: lower correlation to equity beta · horizon: years · conditions: relative to long-only equity; not versus managed futures or gold · testable: yes - correlation of equal-risk vs cap-weighted portfolios · confidence: medium
  ^MT169-C05-X1

### C06
- **Cole Wilcox** The winner-take-all power law is a universal mathematical law of capital markets, supporting trend on single stocks across caps and countries.  #mech/structural_shift
  > a universally applicable strategy that works across Market capitalizations Works across countries
  asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT169-C06-1
- **Cole Wilcox** Equity index futures trend portfolios are dominated by large caps and underrepresent the small/mid-cap area where outliers and inefficiency concentrate; cash equities need full funding, unlike futures.  #mech/structural_shift
  > if you're trading a portfolio of equity index Futures and you're doing trend on them you're going to be dominated by indexes that are large cap by Nature
  indicator: equity index futures trend · asset: equities · horizon: years · conditions: funding costs matter in levered contexts · testable: yes · confidence: medium
  ^MT169-C06-2
- **Cole Wilcox** Much of the value of trend following on equity indexes comes from cutting the left tail of catastrophic market declines; the incremental edge from single stocks lies in the small and mid-cap area that index futures portfolios under-represent.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > a lot of the value of trend is being extracted from Trading indexes like because you're cutting out the left tail right of the the really catastrophic down movements of the market just by Trend following
  indicator: trend following on equity index futures · asset: equities · direction: reduce exposure in large drawdowns · horizon: years · conditions: index futures portfolios dominated by large caps · testable: yes - drawdown and tail statistics of trend on indexes vs buy-and-hold · confidence: high
  ^MT169-C06-X2

### C07
- **Cole Wilcox** Risk-weighted position sizing is capped at 100% funded; small/mid-cap volatility is high enough that the risk target is reached without leverage, and leveraging low-vol names is deemed a recipe for disaster.  #mech/risk_management
  > the underlying volatility of the positions that we trade are are investing into are the highest volatility segment of the equity markets
  indicator: volatility-based position size, leverage cap · asset: equities · testable: yes · confidence: high
  ^MT169-C07-1
- **Cole Wilcox** With hundreds of risk-weighted stock positions whose volatility keeps moving, the portfolio is rebalanced continuously to hold the target risk level, with a hard cap preventing leverage above 100% funded.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > we're constantly making rebalance trades to kind of calibrate the risk you know in the portfolio to where it needs to be
  indicator: portfolio risk target and position volatility · asset: equities · horizon: days · conditions: unleveraged long-only; cap at 100% exposure · testable: yes - turnover and tracking of risk target · confidence: high
  ^MT169-C07-X3
- **Cole Wilcox** Dividends and corporate-action cash flows are not reinvested stock by stock; they are added to the portfolio's cash and base trading level and spread proportionately across all positions, which simplifies operations in a 300-600 stock book.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > all of those cash flows come in and they just get added back to the base trading level right and then it's going to get dispersed proportionately throughout the portfolio
  indicator: dividends and corporate actions handling · asset: equities · horizon: days · conditions: large single-stock portfolios with frequent corporate actions · testable: no - operational method · confidence: high
  ^MT169-C07-X4

### C08
- **Cole Wilcox** Small/mid caps have more outliers and failures than large caps, so cutting losers is more effective (and 10-50 baggers more common); large caps rarely fail.  #mech/risk_premium
  > the small midcap sector has disproportionate outlier movements relative to large cap stocks
  asset: equities · horizon: years · conditions: cuts both ways · testable: yes · confidence: medium
  ^MT169-C08-1
- **Cole Wilcox** Longboard declined to lend out its shares for extra income because the small yield did not compensate for counterparty and rehypothecation risk and added complexity; the stated principle is not to take risks you are not paid for proportionally.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > the extra complexity for the amount of residual income that we come we kind of said like for us like the juice just isn't worth to squeeze
  indicator: securities lending income vs counterparty and rehypothecation risk · asset: equities · testable: no - cost/benefit judgement · confidence: high
  ^MT169-C08-X5
- **Cole Wilcox** Single-stock futures were not useful for the strategy because they restricted the tradable universe to large, liquid names, whereas the small and mid-cap segment where trend has the most edge was not covered.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > there was never any need for us to use Futures it definitely limited the universe right so that's the problem and then also those stocks would have been the larger cap names
  indicator: single-stock futures (OneChicago) · asset: equities · conditions: futures cover only larger-cap stocks · testable: no - historical product limitation · confidence: high
  ^MT169-C08-X6

### C09
- **Cole Wilcox** Holding 300-600 names (about 20% of the tradable set) avoids missing the 4% winners; concentrated top-50 portfolios have wide lucky/unlucky dispersion, so breadth minimises dispersion and maximises geometric compounding.  #mech/risk_management
  > the shest way to guarantee that you miss a move is to remove something from the tradable universe so that you never get signal on it
  indicator: portfolio breadth · asset: equities · horizon: years · testable: yes - random subset test · confidence: high
  ^MT169-C09-1
- **Moritz Seibert** Dilution argument: in a portfolio of hundreds of markets or stocks a single outlier winner has a smaller impact on returns than in a 40-50 name portfolio, so concentration can give more positive skew and 'bang for the buck' (Moritz's question, which Cole answers with luck-dispersion arguments).  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > if you have this big outlier trade happening um it has in all likelihood uh less of a footprint less of an effect in the portfolio that trades all these you know hundreds of markets
  indicator: portfolio breadth vs outlier trade contribution · asset: multi · direction: concentrated books have larger winners but wider dispersion · horizon: years · conditions: depends on whether the concentrated book includes the winners · testable: yes - simulate random concentrated subsets vs full universe · confidence: medium
  ^MT169-C09-X7

### C10
- **Moritz Seibert** Avoiding large drawdowns has compounding benefits and prevents behaviour-driven underperformance; being down 50% requires a 100% gain.  #mech/behavioral
  > you reduce the chance of being down 50% because when you're down 50% you need to make a 100 to come back up
  indicator: drawdown size · asset: equities · horizon: years · testable: yes · confidence: high
  ^MT169-C10-1
- **Cole Wilcox** Two alphas: mathematical (volatility drag reduction and optimal sizing raise compounding) and behavioural (smoother ride keeps investors from panic selling).  #mech/behavioral
  > there's the mathematical Alpha of the benefits of low volatility reduction and controlling volatility I mean like variance drain
  indicator: variance drain · asset: equities · horizon: years · testable: yes · confidence: high
  ^MT169-C10-2
- **Cole Wilcox** Concentrated managers can look better in short periods; the low-dispersion approach underperforms the leader at times but compounds better as hares make unforced errors.  #mech/behavioral
  > we're the tortoise just plotting along compounding through time
  indicator: relative performance · asset: equities · horizon: years · testable: partly · confidence: medium
  ^MT169-C10-3

### C11
- **Cole Wilcox** Correlation-zero diversifiers (managed futures, gold, commodity) give large tracking error vs equities so clients abandon them in bull markets; an equity-like trend fund offers a balanced all-weather experience.  #mech/behavioral
  > the downside of a correlation zero strategy is it's going to have a lot of tracking error relative to the stock market
  indicator: tracking error vs equities · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT169-C11-1
- **Cole Wilcox** Whether a single-stock trend fund should complement or replace a core equity holding depends on the client's constraints: blend it for most, replace beta for those who want no equity downside; it is not a fit for a goal of a correlation-zero alternatives portfolio.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > in some cases blending it you know uh with with with other things is the right thing to do for others who really don't want to have any downside risk of equity beta replacing it you know makes sense
  indicator: equity beta replacement vs blend · asset: equities · horizon: years · conditions: client needs and constraints · testable: no - allocation judgement · confidence: medium
  ^MT169-C11-X8

### C12
- **Cole Wilcox** Key lesson: discipline to stick to a good systematic process despite short-term feedback separates success from failure; many deviate under client pressure.  #mech/behavioral
  > sticking to your process and never deviating you know kind of from it is more important than having the best process ever
  asset: multi · horizon: years · testable: no · confidence: high
  ^MT169-C12-1

