---
source_id: MT177
title: "The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139"
date: 2023-03-21
channel: "Top Traders Unplugged"
url: 
words: 14098
claims: 58
added_by_crosscheck: 10
corrections: 1
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Simon Judes (co-CIO, Winton)", "Niels Kaastrup-Larsen (host)", "Alan Dunne (co-host)"]
tags: [source, layer0]
---
# The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139

**Speakers:** Simon Judes (co-CIO, Winton); Niels Kaastrup-Larsen (host); Alan Dunne (co-host)

**Summary:** Judes explains Winton's scientific research approach, three-quarters trend plus one-quarter other signals, why long-term trend Sharpe is about 0.5 and fast trends deteriorated most. Adds that more genuinely diversifying markets matter via effective number of markets, risk is not volatility, and trend is often contrarian. Conclusions: no regime-based speed switching, humans own key parameters, scenario stress tests from history and correlation shocks.

**Approach:** trend following, CTA, research method, risk management, market diversification, machine learning

**Cross-check completeness estimate of first read:** 0.82 - first reader's 46 claims cover the core Winton method, speed, markets, risk and contrarian-trend arguments; additions are secondary reasoning (allocator mechanism, research structure, correlation condition, caveats).

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | intro, Winton overview and product structure |
| C02 | 4 | history effect, scientific philosophy, avoiding data mining |
| C03 | 2 | confidence via backtest vs rationale, sources of alpha, Harding 2018 comment question |
| C04 | 3 | long-term trend Sharpe 0.5, performance decline, three products |
| C05 | 3 | investor experience, smoothing drawdowns, crisis alpha traits |
| C06 | 3 | crisis alpha is necessary-not-sufficient, labels, allocator timing worries |
| C07 | 3 | averaging in, carry in the mix, 75/25 level, speed question |
| C08 | 3 | speed deterioration, research sources |
| C09 | 2 | types of research, event-driven model changes, March 2020 |
| C10 | 2 | no regime speed switching, machine learning data limits |
| C11 | 2 | observational vs experimental, parameters across markets |
| C12 | 2 | human responsibility for parameters, CTA replication |
| C13 | 2 | number of markets, effective independent markets |
| C14 | 2 | genuinely alternative markets, counterparty risk |
| C15 | 2 | barriers to entry, portfolio role, customised programs |
| C16 | 2 | risk is not volatility, historical stress replay |
| C17 | 3 | current scenario risks, leverage, correlation shock 2013 |
| C18 | 3 | 2013 outcome, equity beta cap, number of managers |
| C19 | 2 | return expectations, crowding, contrarian view of trend |
| C20 | 1 | trend as contrarian: German yields, closing priorities |
| C21 | 0 | nothing actionable: outro and plugs |

## Claims

### C01
- **Simon Judes** Winton's priorities are original research for new alpha sources and improvement of existing ones, plus hyper-vigilant risk management that monitors many possible scenarios.  #mech/research_method
  > what matters is original research to find new Alpha sources and you know improve our existing ones and on risk management
  asset: multi · testable: no - process statement · confidence: high
  ^MT177-C01-1
- **Simon Judes** Winton runs a diversified CTA that is 75% trend following and 25% other systematic macro strategies, alongside pure trend and quant multi-strategy products.  #mech/risk_management
  > there's a diversified CTA which is three-quarters Trend following and a quarter other systematic microstrategies and then we have pure Trend products as well
  indicator: trend / non-trend allocation · asset: multi · testable: partly - mix is a design choice testable via backtest · confidence: high
  ^MT177-C01-2

### C02
- **Simon Judes** Researchers' and firms' early market experiences (1987, 2008) shape how they parametrise and organise trend strategies, a behavioural source of differences between trend followers.  #mech/behavioral
  > people have been very influenced by their initial experiences
  asset: multi · testable: no - observation · confidence: medium
  ^MT177-C02-1
- **Simon Judes** Winton's philosophy is to approach markets with an open mind and use empirical scientific research, rejecting the efficient market hypothesis as a foundation, because good predictions are possible with hard work.  #mech/research_method
  > you can discover and improve successful investment strategies by applying empirical scientific research methods
  asset: multi · testable: no - philosophy · confidence: high
  ^MT177-C02-2
- **Simon Judes** Avoiding data-mining false positives requires shared statistical techniques for testing many hypotheses simultaneously and sequentially, which also drives hiring and training.  #mech/research_method
  > help you in particular test multiple hypotheses at the same time and sometimes also sequentially one after the other
  indicator: multiple-testing procedures · asset: multi · testable: yes - apply multiple-testing corrections to trial counts · confidence: high
  ^MT177-C02-3
- **Simon Judes** Process must prevent researchers from privately overfitting many ideas and presenting only the subset that looked good in a backtest.  #mech/research_method
  > avoiding situations where researchers privately overfit ideas and day touring and then only show you
  indicator: research trial log · asset: multi · testable: yes - log all trials and count them · confidence: high
  ^MT177-C02-4

### C03
- **Simon Judes** Backtest statistics give confidence in Sharpe and low correlation, and an economic rationale with testable intermediate relationships adds confidence; absence of a rationale lowers confidence rather than killing the idea.  #mech/research_method
  > if there is for example an economic rationale behind a particular idea then you can use that you can test the intermediate economic relationships and that can add additional confidence
  indicator: backtest Sharpe, correlation to existing strategies · asset: multi · testable: yes - tiered evidence thresholds · confidence: high
  ^MT177-C03-1
- **Simon Judes** Winton's alpha comes from a mixture of behavioural, structural and microstructure sources depending on strategy, so it is hard to say who is on the other side of the trades.  #mech/structural_shift
  > extremely diverse collection of alpha sources
  asset: multi · testable: no - generalisation declined · confidence: medium
  ^MT177-C03-2

### C04
- **Simon Judes** Harding's 2018 view is that long-term trend following Sharpe is around 0.5, enough on its own to run a fund only marginally, so other signals should be added to raise Sharpe.  #mech/slow_reaction
  > the long-term sharp outlook for Trend following is perhaps around a half
  indicator: trend following Sharpe ratio · asset: multi · horizon: years · testable: yes - Sharpe of trend indices over time · confidence: high
  ^MT177-C04-1
- **Simon Judes** Over a long window from the 1970s trend performance declined steadily for the strategies in use; the decline was first seen in Winton research around 2007 and was not just a post-2008 story.  #mech/crowding_positioning
  > then you actually find a consistent decline in the performance of trend um of the kind of trend strategies that people were trading at the time
  indicator: trend strategy performance since 1970s · asset: multi · direction: trend Sharpe down over time · horizon: years · testable: yes - rolling Sharpe of trend · confidence: high
  ^MT177-C04-2
- **Simon Judes** Winton responded to lower trend Sharpe expectations by splitting into pure trend, diversified CTA and multi-strategy products rather than abandoning trend.  #mech/structural_shift
  > instead of having one product uh dominated by Trend following we now have three products
  asset: multi · testable: no - business response · confidence: high
  ^MT177-C04-3
- **Niels Kaastrup-Larsen** Trend following should be judged by the improvement in total-portfolio Sharpe it delivers, not by its stand-alone Sharpe or a 'crisis alpha' mandate, because Sharpe was not created for single-strategy evaluation (reacting to the AQR paper on trend mandates).  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > my opinion is we probably should change the conversation to talk about the Improvement of portfolio shop that these strategies provide
  indicator: portfolio Sharpe improvement · asset: multi · conditions: when trend is held alongside traditional assets · testable: yes - marginal contribution to portfolio Sharpe can be computed · confidence: medium
  ^MT177-C04-X1

### C05
- **Simon Judes** Trend gave diversification in 2008 and 2022, but the long drawdowns in between make allocators drop it; judging by investor experience beats focusing on Sharpe or mandate labels.  #mech/behavioral
  > I think we prefer to look at the investor experience you look at situations where investors really needed diversification in 2008 uh last year and trend has done very well there
  indicator: trend returns in equity crises · asset: multi · horizon: years · testable: yes - trend vs equity drawdown episodes · confidence: medium
  ^MT177-C05-1
- **Simon Judes** Adding non-trend signals smooths drawdowns but reduces crisis effectiveness, so type and weight of added signals matter; Winton chooses 75% trend as the level that keeps the trend profile with some drift.  #mech/risk_management
  > there's Great Value in adding signals which smooth out those drawdowns
  indicator: non-trend signal weight · asset: multi · direction: drawdowns down, crisis convexity down · horizon: years · conditions: depends on which signals are added and their weight · testable: yes - blend-weight sweep · confidence: high
  ^MT177-C05-2
- **Niels Kaastrup-Larsen** Kaminski's crisis alpha traits: liquid, opportunistic (can move to where the action is) and unbiased (long as easily as short); in 2020 the best trade was long bonds and short energy, in 2022 the opposite.  #mech/slow_reaction
  > it needs to have um you know it needs to be opportunistic so that you you don't you're not stuck in the same asset class or in the same Market you can move around
  indicator: trend following across markets · asset: multi · horizon: years · testable: partly - trade direction by year documented · confidence: medium
  ^MT177-C05-3
- **Simon Judes** Allocators abandon trend after long drawdowns not from lack of faith but because each line item must be justified to an investment committee, which is why smoothing the drawdowns has great value.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > the people who are making these allocation decisions have to justify each line item to their investment committees and it becomes very difficult
  indicator: allocator behaviour in drawdowns · asset: multi · horizon: years · conditions: when allocation decisions are scrutinised line by line · testable: partly - allocator flows can be studied · confidence: high
  ^MT177-C05-X1

### C06
- **Simon Judes** Liquidity, opportunism and no bias are necessary, not sufficient, for crisis performance; trend does well in extended trends but fails when equities rise steadily then reverse sharply (Feb 2018).  #mech/slow_reaction
  > those three characteristics that you mentioned are prerequisites for something to function in that way but they don't guarantee that it's going to work
  indicator: trend following in sharp reversals · asset: equities · direction: trend loses · horizon: weeks · conditions: after a steady equity rise followed by a sharp downturn · testable: yes - trend returns around Feb 2018 type reversals · confidence: high
  ^MT177-C06-1
- **Simon Judes** Labels like crisis alpha mislead because trend only sometimes works in crises; describe its response in different environments instead.  #mech/research_method
  > the best thing is to really try and describe the strategy how it's going to react what it's going to do in different environments
  asset: multi · testable: no - communication advice · confidence: high
  ^MT177-C06-2
- **Simon Judes** Trend cannot be timed, but allocators bear personal risk if it underperforms right after they allocate, so concerns should be addressed rather than answered with statistics.  #mech/behavioral
  > even if you um can't time Trend following even if we agree that you can't time when it's going to work there's still a risk for the allocator
  asset: multi · testable: no - behavioural · confidence: medium
  ^MT177-C06-3
- **Niels Kaastrup-Larsen** Potential investors treat trend following as a tactical trade and assume that after a strong 2022 it is too late or cannot repeat, a market-timing mindset that trend followers need to counter.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > they kind of look at Trend following a little bit like a trade they try to time it and then also they have this notion that well it did so well in 2022 um it's either too late
  indicator: investor timing of trend allocation · asset: multi · horizon: months · conditions: after strong trend years · testable: partly - flows after good years can be checked · confidence: medium
  ^MT177-C06-X1

### C07
- **Simon Judes** A good year does not predict a bad next year: 2008 was good but all prior Winton years were also good, and good years come in sequences; investors can average in over months to ease timing worries.  #mech/cycle_persistence
  > there's no reason to think that next year will be um will be bad because last year was good
  indicator: trend annual returns · asset: multi · horizon: years · testable: yes - autocorrelation of annual CTA returns · confidence: medium
  ^MT177-C07-1
- **Simon Judes** Carry added to trend is not traded in equities because it adds long equity bias and reduces convexity; carry's currency-style small-gain/large-loss profile is mitigated by trading it in commodities and fixed income too.  #mech/risk_premium
  > we don't trade it on um equities um though because often that that does just add a long bias to your Equity portfolio
  indicator: carry signal across asset classes · asset: multi · direction: carry returns smoother across commodities and bonds than currencies · horizon: years · conditions: equities excluded because of long bias · testable: yes - carry by asset class · confidence: high
  ^MT177-C07-2
- **Simon Judes** The trend/non-trend mix depends on the opportunity set but is fixed so investors know what they receive.  #mech/risk_management
  > important to you know fix a level so that investors know what they're what they're going to get
  asset: multi · testable: no - governance choice · confidence: medium
  ^MT177-C07-3
- **Simon Judes** The non-trend quarter of the diversified CTA is a mixture of purely statistical signals, economic-rationale signals and non-trend technical signals, some faster than trend, with new signals added each year.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > some of them are purely statistical in nature some of them have economic rationales some of them are other technical signals like Trend following that are different from Trend following
  indicator: non-trend signals in Winton diversified program · asset: multi · testable: no - not specified · confidence: medium
  ^MT177-C07-X1

### C08
- **Simon Judes** Fast trend strategies deteriorated most since 1997 because everyone traded them; slow strategies started with lower Sharpe, so always choosing the best speed shows decline.  #mech/crowding_positioning
  > the largest deterioration is seen in the faster Trend strategies this is what everyone was trading
  indicator: trend speed (lookback) Sharpe · asset: multi · direction: fast trend Sharpe down, slow flat · horizon: years · testable: yes - speed-split Sharpe over time · confidence: high
  ^MT177-C08-1
- **Simon Judes** Maximising Sharpe alone favours very slow trend, but investors want responsiveness at turning points like 2008 and 2022, so some faster speed fits objectives even at lower Sharpe.  #mech/slow_reaction
  > if you're trying to purely maximize the the sharp ratio um then uh what our analysis has shown is that you really want to be very slow
  indicator: trend lookback choice · asset: multi · direction: slower speed gives higher Sharpe · horizon: years · conditions: investor objective is crisis responsiveness not Sharpe · testable: yes - speed-blend backtest · confidence: high
  ^MT177-C08-2
- **Simon Judes** Winton finds academic journals no longer at the forefront of alpha research and instead does original research, sometimes finding ideas from Chinese commodity markets that work globally.  #mech/research_method
  > one place we uh we haven't uh looked so much recently though is is in academic journals actually
  asset: multi · testable: no - process · confidence: medium
  ^MT177-C08-3

### C09
- **Simon Judes** Event-driven model adjustments: Feb 2007's reversal that hit CTA positions (crowding effect) led to volatility model changes that helped in Feb 2018.  #mech/crowding_positioning
  > often adjustments to our our volatility models for example have been prompted by new types of events
  indicator: CTA volatility models, Feb 2007 and Feb 2018 reversals · asset: multi · direction: CTA losses in sudden reversals after low-volatility equity rises · horizon: days · conditions: after rising equities on low volatility · testable: partly - two events · confidence: high
  ^MT177-C09-1
- **Simon Judes** Fast trend beat slow in Feb-Mar 2020 because the fall lasted one month before the Fed stepped in; Winton saw no evidence of a lasting change and slower trend has since done better again.  #mech/slow_reaction _(time-bound view)_
  > if on the other hand you took a month to turn around your positions then you lost all the way down and then you lost again on the way up
  indicator: fast vs slow trend in March 2020 · asset: equities · direction: fast trend gained in a one-month crash · horizon: weeks · conditions: short crash with sharp reversal · testable: partly - one episode · confidence: high
  ^MT177-C09-2
- **Simon Judes** Research has two streams: finding new alpha sources (new ideas or data inputs) and maintaining existing ones by reviewing trend speed, signal construction and volatility models.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > you've got your existing Alpha sources and you need to make sure you're doing them as well as you can and that involves reviewing things like the uh the speed of trend following
  asset: multi · testable: no - process description · confidence: high
  ^MT177-C09-X1

### C10
- **Simon Judes** Switching trend speed with the regime is an implicit call on policy (e.g. Fed intervention), which systematic managers should not make; discretionary macro managers do that.  #mech/research_method
  > you can see that this apparently technical statistical decision about which is the best speed at that moment amounts to just a call on what the FED is going to do and when
  indicator: regime-based speed switching · asset: multi · horizon: weeks · testable: partly - test regime-switching speed rules · confidence: high
  ^MT177-C10-1
- **Simon Judes** Machine learning lacks enough independent events for slow-trading strategies because few examples of crashes exist, but works for faster intraday strategies with many observations.  #mech/research_method
  > machine learning algorithms require a lot of data a lot of training data
  indicator: machine learning · asset: multi · conditions: slow time scales fail, fast time scales work · testable: yes - sample-size analysis · confidence: high
  ^MT177-C10-2

### C11
- **Simon Judes** Slow-horizon research is an observational science (cannot rerun a crash) while fast execution research is experimental and can iterate, so machine learning suits the latter.  #mech/research_method
  > in financial markets if you're talking about what happens on slower time scales how you deal with events like a market crash well you can't just create a market crash on demand
  asset: multi · testable: no - methodology · confidence: high
  ^MT177-C11-1
- **Simon Judes** Parameters are mostly universal across markets but adjusted for transaction cost, market impact, spreads and commissions.  #mech/risk_management
  > we're fairly Universal but they're not not completely there are practical differences often between uh between markets
  indicator: market-specific cost parameters · asset: multi · testable: yes - cost-adjusted parameters · confidence: high
  ^MT177-C11-2
- **Simon Judes** Claiming that a systematic process is fully automated hides that someone must still choose the parameters or the algorithm that chooses them (an infinite regress), so firms should deliberately decide at which level humans take responsibility.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > there's a temptation as a um as a Quant to say everything's automated I didn't do anything the the whole thing's done by a computer that's definitely the wrong thing to do
  indicator: parameter selection process · asset: multi · testable: no - governance principle · confidence: high
  ^MT177-C11-X1

### C12
- **Simon Judes** Humans should own early design decisions such as trend speed and asset allocation (made with analysis) rather than defer to an optimizer, preserving understanding of the portfolio.  #mech/research_method
  > our point of view has generally been that we try to push responsibility on the human fairly early so things like the trend following speed
  indicator: trend speed, asset allocation · asset: multi · conditions: avoid black boxes · testable: no - governance philosophy · confidence: high
  ^MT177-C12-1
- **Simon Judes** Regression-based CTA replication (about 95bp fee) is still a single-manager risk; Winton disagrees that it mitigates manager risk.  #mech/research_method
  > I think they are a single manager if you want to mitigate a single manager risk then obviously the fund of funds approach is the way to go
  indicator: CTA replication · asset: multi · testable: no - opinion · confidence: medium
  **Correction (cross-check):** The fee figure was supplied by the host, not Judes: Judes asked how much replication products charge and the host answered 'just shy of one percent' (85bp plus about 10bp). Judes' own view is only that replication does not mitigate single-manager risk and that fund-of-funds is the real route. → Judes disagrees that regression-based CTA replication mitigates single-manager risk (the replicator is itself a single manager; fund of funds is the way to diversify manager risk); the host noted such products charge just under 1% (about 95bp).
  ^MT177-C12-2

### C13
- **Simon Judes** Sharpe scales with the square root of the effective number of markets given correlations; 50-60 markets might be only 8-10 independent, so adding genuinely different markets adds a lot.  #mech/structural_shift
  > the number that goes into that square root is not the number of markets you trade but the effective number of markets when you've taken account of all of the correlations
  indicator: effective number of markets · asset: multi · direction: Sharpe up with uncorrelated markets · horizon: years · conditions: adding highly correlated markets adds nothing · testable: yes - effective-N from correlations · confidence: high
  ^MT177-C13-1
- **Simon Judes** Alternative markets outperformed major markets over the last decade, including the post-crisis period when mainstream trend struggled; European gas and power gave huge trends (gas up tenfold).  #mech/structural_shift _(time-bound view)_
  > the alternative markets portfolio they did extremely well in that period
  indicator: alternative markets trend portfolio · asset: commodities · direction: alternative market trend returns above major markets · horizon: years · testable: yes - split portfolio returns · confidence: high
  ^MT177-C13-2

### C14
- **Simon Judes** Added markets should be truly diversifying (Chinese futures, regional gas, power, freight, marine fuel) rather than equity sector ETFs or developed-market swaps correlated with existing exposure.  #mech/risk_management
  > the markets that you add have to genuinely be alternative and additive
  indicator: correlation of added markets · asset: multi · horizon: years · testable: yes - marginal contribution analysis · confidence: high
  ^MT177-C14-1
- **Simon Judes** Many OTC-traded alternative markets can be cleared on exchange, reducing counterparty risk close to major futures levels.  #mech/risk_management
  > there's still markets that where you can clear your position uh on the exchange so you can um really reduce the counterparty risk
  asset: multi · conditions: not always possible · testable: no - operational · confidence: medium
  ^MT177-C14-2
- **Niels Kaastrup-Larsen** Counterpoint to the more-markets argument: a 50-60 market classical portfolio already includes diversified commodities, and going from 100 to 200 markets mostly adds correlated financial markets unless the extras are genuinely alternative (e.g. Chinese futures).  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > a lot of the additional markets you see often are as you say financial markets that may have correlations to other markets that you may already have
  indicator: number of markets in trend portfolios · asset: multi · direction: Sharpe gain from extra markets small beyond about 100 · conditions: when added markets are correlated financial instruments · testable: yes - Sharpe vs effective number of markets · confidence: medium
  ^MT177-C14-X1
- **Simon Judes** Chinese futures are accessed onshore, through internationalised exchange contracts, via swaps and via the QFI route, an execution method for reaching a diversifying market that others cannot easily trade.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > we trade them now um via the internationalized markets via swaps and by the qfi route you know for our Global Investors
  indicator: Chinese futures access · asset: commodities · testable: no - implementation detail · confidence: high
  ^MT177-C14-X2

### C15
- **Simon Judes** Alternative markets carry extra returns partly because barriers to entry (software, operations, middle office) keep trend followers from extending into them easily.  #mech/risk_premium
  > these markets are by definition have a barrier to entry and that's you know one of the reasons why they have extra offers
  asset: multi · horizon: years · testable: no - structural reason · confidence: medium
  ^MT177-C15-1
- **Simon Judes** Trend allocation size and form (pure, capped beta) depend on the investor's drawdown tolerance and process, so there is no fixed rule; customised programs often vary alternative-market or China exposure rather than trend share.  #mech/risk_management
  > the answers depend on what the investors objectives are what their tolerance is for for drawdowns in particular parts of their book
  indicator: trend allocation size · asset: multi · testable: no - depends on investor · confidence: medium
  ^MT177-C15-2

### C16
- **Simon Judes** Risk is not volatility: in 2017 the VIX was at record lows while valuations were rich, and estimating loss risk is harder than estimating volatility, so use many risk measures besides volatility.  #mech/risk_management
  > there's a strange confusion that affects the CTA industry particularly which is to equate risk with volatility
  indicator: volatility as risk measure · asset: multi · testable: partly - compare vol vs drawdown predictors · confidence: high
  ^MT177-C16-1
- **Simon Judes** Risk management by replaying current positions through all historical environments (worst day or week) and asking whether the loss is acceptable, e.g. the 1990 Gulf War oil jump of 30%.  #mech/risk_management
  > we look at our current positions and we see how they would have performed in all the previous Market environments that we have data for
  indicator: worst day/week of current exposures · asset: multi · testable: yes - historical stress replay · confidence: high
  ^MT177-C16-2

### C17
- **Simon Judes** In early 2023 trend positions were short bonds and long equities, so a risk-off move with bonds rallying and equities falling (disinflationary bad news) is the main scenario risk.  #mech/crowding_positioning _(time-bound view)_
  > most things are short bonds and long equities so obviously the um the situation that's really worrisome is a very classic risk-off move where bonds rally inequities um decline
  indicator: trend positioning, stock-bond correlation · asset: multi · direction: portfolio losses if bonds up, equities down · horizon: months · conditions: modest positive stock-bond correlation currently · testable: partly - positioning-based scenario test · confidence: high
  ^MT177-C17-1
- **Simon Judes** Leverage varies naturally with signal strength and correlations, and risk measures decide whether to hold it inside a band.  #mech/risk_management
  > the way that these strategies operate the leverage naturally fluctuates as the signal strength varies and the correlation between markets varies
  indicator: leverage, correlation · asset: multi · testable: yes - leverage bands · confidence: medium
  ^MT177-C17-2
- **Simon Judes** Stylised stress test of correlation flips: before the 2013 taper tantrum trend was long bonds and long stocks with negative correlation, and a positive correlation scenario looked unacceptable, so risk was cut.  #mech/risk_management
  > you look at things like what if all the correlations change in whatever way would be worse for you
  indicator: stock-bond correlation scenario · asset: multi · testable: yes - correlation-shock scenario · confidence: high
  ^MT177-C17-3
- **Simon Judes** Recently stock-bond correlation has been modestly positive because of the inflation dynamic, so bonds no longer rally reliably in risk-off episodes and trend portfolios that are short bonds and long equities face a different scenario map.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > we've been seeing sort of modest positive correlation between those asset classes and obviously the dynamic with with inflation has made that somewhat different from the usual situation
  indicator: stock-bond correlation · asset: multi · direction: bonds and equities fall together when inflation drives markets · horizon: months · conditions: when inflation, not growth, is the dominant shock · testable: yes - rolling correlation · confidence: medium
  ^MT177-C17-X1

### C18
- **Simon Judes** Winton ran lower volatility ahead of the 2013 taper tantrum because of the correlation scenario, which helped that year.  #mech/risk_management _(time-bound view)_
  > we temporarily operated at a lower level of volatility and that really helped us actually in that year
  indicator: bond-stock correlation, volatility target · asset: rates · horizon: months · conditions: before bond/equity correlation turns positive · testable: partly - single year · confidence: high
  ^MT177-C18-1
- **Simon Judes** Capping equity long exposure in a trend program reduces long-term performance in proportion to the cap, helps crisis profile, and is offered as a bespoke option; neither is objectively better.  #mech/risk_management
  > you reduce the long-term performance to some extent depending on how big the you know how significant the cap is
  indicator: equity beta cap in trend · asset: equities · direction: long-run return down, equity beta down · horizon: years · testable: yes - capped vs uncapped backtest · confidence: high
  ^MT177-C18-2
- **Simon Judes** Using multiple trend managers cuts single-manager risk but loses fee netting; the investor chooses the trade-off.  #mech/risk_management
  > you can diversify and you reduce the single manager risk and on the other hand you don't and have fee netting
  indicator: number of trend managers · asset: multi · testable: partly - dispersion data · confidence: medium
  ^MT177-C18-3

### C19
- **Simon Judes** The decline in trend performance correlates strongly with growth in the number of traders, so 0.5 Sharpe is the expectation; long simulations only show underlying markets trend, not future Sharpe for a crowded strategy.  #mech/crowding_positioning
  > it's clear that that correlates very strongly to the growth of people trading the strategy
  indicator: trend Sharpe vs industry assets · asset: multi · direction: Sharpe down as trend AUM up · horizon: years · testable: yes - regress Sharpe on CTA AUM · confidence: medium
  ^MT177-C19-1
- **Simon Judes** Trend following is often contrarian to prevailing fundamental narratives, e.g. oil in 2014 when shale supply was underestimated against a peak-oil view.  #mech/behavioral
  > Trend following is most successful it's because it's actually a contrarian strategy
  indicator: oil price 2014 · asset: commodities · direction: trend short oil · horizon: months · conditions: when fundamental narrative opposes the move · testable: no - narrative-based single case · confidence: high
  ^MT177-C19-2
- **Alan Dunne** Lower trading costs and lower fees are partial offsets to the decline in gross trend Sharpe, so the investor's net outlook is less negative than the 0.5 gross estimate suggests.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > you've got lower trading costs now that you might have had in the past um which would be a positive and fees have probably come down for investors too
  indicator: trend net Sharpe after costs and fees · asset: multi · direction: net returns less depressed than gross · horizon: years · testable: partly - cost series available · confidence: low
  ^MT177-C19-X1

### C20
- **Simon Judes** Trends extend in time because a prevailing narrative says the market must go the other way, as in German yields that kept falling into negative territory against the belief they could never go below zero.  #mech/slow_reaction
  > for that to be a trend the movement has to be extended in time and often it can be extended because it is contrarian because there's a narrative
  indicator: German bond yields 2014-2016 · asset: rates · direction: long bonds · horizon: months · conditions: when a widespread belief rejects the move · testable: no - historical examples · confidence: high
  ^MT177-C20-1

