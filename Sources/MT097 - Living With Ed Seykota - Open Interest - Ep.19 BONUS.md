---
source_id: MT097
title: "Living With Ed Seykota - Open Interest - Ep.19 BONUS"
date: 2025-11-09
channel: "Top Traders Unplugged"
url: 
words: 7110
claims: 25
added_by_opus: 4
corrections: 2
crosscheck: "opus cross-check"
speakers: ["Dave Drew (systematic trader, former apprentice of Ed Seykota)", "Moritz Seibert (host, Open Interest series)"]
tags: [source, layer0]
---
# Living With Ed Seykota - Open Interest - Ep.19 BONUS

**Speakers:** Dave Drew (systematic trader, former apprentice of Ed Seykota); Moritz Seibert (host, Open Interest series)

**Summary:** Bonus part of an Open Interest interview: Dave Drew recounts six months as Ed Seykota's apprentice and what he learned. Seykota was a technical discretionary trader, not a systematic one; key lessons are matching style to psychology, optimal bet size with high heat, not tinkering or cutting size in drawdowns, sizing off closed-trade equity.

**Approach:** trading psychology, position sizing, drawdown management, discretionary vs systematic, trend following

**Opus completeness estimate of first read:** 0.9 - anecdote-heavy episode with few method ideas; first reader captured the sizing and psychology points, missed Drew's backtest-before-implement process, investor-suitability caveat, drawdown-behavior point and data cleaning.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | cold open on Seykota drawdown tolerance; intro boilerplate; Drew introduces apprenticeship |
| C02 | 3 | Seykota is technical discretionary not systematic; general rules; Market Wizards misreading; chart drawing anecdote |
| C03 | 3 | The Trader's Window, apprenticeship style, end-of-day chart routine, psychology as market outcome |
| C04 | 4 | psychology must fit trading style; Drew's 15-month discretionary experiment 300% vs systems 20%; trade meaningful money |
| C05 | 3 | optimal bet size article, heat, risk of ruin vs growth; Seykota's drawdown tolerance; coping with losses |
| C06 | 4 | no memory of losses; do not tinker in drawdown; do not cut size, bet size must follow equity |
| C07 | 2 | drawdown-reduction rules harm recovery; closed vs open equity sizing; how he became apprentice (anecdote) |
| C08 | 0 | apprenticeship anecdotes, nothing actionable |
| C09 | 1 | data cleaning anecdote; Seykota's idea of self-limitation and worthiness |
| C10 | 0 | cookie anecdote, no method content; outro |
| C11 | 0 | outro boilerplate, nothing actionable |

## Claims

### C01
- **Dave Drew** Seykota's approach shows that maximizing return requires pushing bet size and tolerating large heat, but overshooting the optimum risks ruin, so extreme sizing is not advisable for most traders.  #mech/risk_management
  > if you want to get the optimal return, you have to push that bet size and the heat has to be high and most people can't do it
  indicator: bet size, drawdown (heat) · asset: multi · conditions: traders who can psychologically bear very large drawdowns · testable: partly: growth-optimal sizing is analytic but heat tolerance is personal · confidence: medium
  ^MT097-C01-1

### C02
- **Dave Drew** Seykota is a technical discretionary trader who used custom software only to display charts; the Market Wizards impression that he was a systematic computerized trader is wrong.  #mech/research_method
  > Ed is a technical discretionary trader he wrote all these programs to support the data presentation uh that he then used to make discretionary calls about buying and selling
  asset: multi · testable: no: discretionary judgment · confidence: high
  ^MT097-C02-1
- **Dave Drew** Seykota followed a few sacrosanct general rules: cut losses short, let profits ride, diversify.  #mech/risk_management
  > cut your losses short, let your profits ride, diversify
  asset: multi · direction: cut losers, hold winners · testable: partly: rules are testable as stops and trend riding · confidence: high
  ^MT097-C02-2
- **Dave Drew** Seykota's equity swings are enormous, so no institution would invest in him despite the very high returns, since his aim was maximum profit rather than controlled risk.  #mech/risk_management
  > his um his equity swings can be gigantic
  indicator: equity swings · asset: multi · conditions: institutional mandates · testable: no · confidence: medium
  ^MT097-C02-3
- **Dave Drew** Drew's own systematic practice was to backtest every rule before implementing it and then follow the algorithms strictly, the opposite of Seykota's discretionary chart reading.  #mech/research_method _(added by Opus)_
  > we have algorithms that we followed strictly and back tested everything before we would implement anything
  asset: multi · testable: no - description of process · confidence: high
  ^MT097-C02-X1

### C03
- **Dave Drew** Seykota's teaching is by apprenticeship and observation (the Jade master story in The Trader's Window) rather than explicit rules, so his skill cannot be programmed or taught directly.  #mech/behavioral
  > it talks about a jade master
  asset: multi · testable: no · confidence: medium
  ^MT097-C03-1
- **Dave Drew** In Seykota's view markets expose hidden psychological problems, so unresolved psychology is brought into trading and causes self-sabotage; hence he held group sessions to surface problems.  #mech/behavioral
  > everybody gets what they want from the markets and it's and markets are a a vehicle for people to work out their psychology
  asset: multi · testable: no · confidence: high
  ^MT097-C03-2
- **Dave Drew** Seykota spent little time on markets, looking at end-of-day charts for about 10 minutes, deciding approximate entries and stops for next day.  #mech/slow_reaction
  > at the end of the day when markets closed, we look at charts and it would take about maybe 10 minutes
  indicator: end-of-day charts · asset: multi · horizon: days · testable: partly · confidence: high
  ^MT097-C03-3

### C04
- **Dave Drew** A trading style must match the trader's psychology, since people who cannot follow a computerized system will tinker with it even if it is excellent.  #mech/behavioral
  > if your style of trading doesn't fit your psychology you're going to fail
  asset: multi · testable: no · confidence: high
  ^MT097-C04-1
- **Dave Drew** Seykota believed technical discretionary trading on price only (ignoring news) earns more than systematic trading.  #mech/slow_reaction
  > never listen to the news. What does the chart tell you? What does the price tell you?
  indicator: price charts · asset: multi · testable: partly: discretionary chart reading is hard to test · confidence: medium
  ^MT097-C04-2
- **Dave Drew** Trading with meaningful size is necessary to learn about oneself, because small money creates no real emotional stakes.  #mech/behavioral
  > you always have to trade with money that's meaningful in order for you to learn and understand yourself
  asset: multi · testable: no · confidence: medium
  ^MT097-C04-3
- **Dave Drew** Drew traded a personal account discretionary Seykota-style for 15 months, made 300% while his systems made 20% for investors, yet had to quit and see a psychiatrist because it did not fit him.  #mech/behavioral
  > So, I did this for about 15 months. made 300% return and absolutely went crazy because it was not my trading style
  asset: multi · horizon: months · conditions: style not matching trader psychology · testable: no: anecdote · confidence: high
  ^MT097-C04-4
- **Dave Drew** Discretionary chart trading cannot responsibly be offered to investors because it has no backtest or statistical record to justify it, so Drew kept investor money in tested systems and confined discretionary trading to a disclosed personal account.  #mech/research_method _(added by Opus)_
  > I said, I can't possibly do that for my investors. I don't have any, you know, back testing. I don't have anything to go on.
  asset: multi · conditions: managing outside capital · testable: no - governance principle · confidence: high
  ^MT097-C04-X1

### C05
- **Dave Drew** There is an optimal bet size given a known edge per trade (Seykota and Drew wrote an article on heat distribution), but because edge is unstable over time it is only a rule of thumb, and the optimal size is bigger than most people would use.  #mech/risk_management
  > There is actually an optimal bet size if you have a system with a known edge per trade
  indicator: edge per trade, heat distribution · asset: multi · direction: bet size near optimal Kelly-like · conditions: edge not stable · testable: yes: simulate growth vs bet size by backtest · confidence: high
  ^MT097-C05-1
- **Dave Drew** Betting too large raises risk of ruin steeply, while betting too little makes risk of ruin near zero but gives low returns.  #mech/risk_management
  > you go too far and your risk of ruin is douche
  indicator: risk of ruin · asset: multi · testable: yes · confidence: high
  ^MT097-C05-2
- **Dave Drew** To make a lot of money one must bet bigger than seems comfortable, taking considerable heat, but not so big as to risk ruin.  #mech/risk_management
  > you want to make a lot of money you have to bet bigger than you think but not too big
  asset: multi · testable: partly · confidence: medium
  ^MT097-C05-3

### C06
- **Dave Drew** Seykota showed no memory of recent losses and acted correctly each day, a discipline needed whether discretionary or systematic.  #mech/behavioral
  > every day was new and every day was do the right thing
  asset: multi · horizon: days · testable: no · confidence: high
  ^MT097-C06-1
- **Dave Drew** The worst time to change a system is during a drawdown; tinkering driven by drawdown psychology harms long-run results, so let statistics play out unless sure something is broken.  #mech/behavioral
  > that's the worst time to change something is in a draw down
  asset: multi · conditions: drawdowns · testable: partly: compare changes made in drawdown vs not · confidence: high
  ^MT097-C06-2
- **Dave Drew** Drawdown reduction rules (dialing risk back after losses) can keep a system underwater indefinitely, so size should instead scale with current equity.  #mech/risk_management
  > You can't have a draw down reduction rule where you're all of a sudden you know dialing back
  indicator: drawdown-based de-risking · asset: multi · direction: do not cut risk beyond equity scaling · testable: yes: simulate vs proportional sizing · confidence: high
  ^MT097-C06-3
- **Dave Drew** Bet size should scale proportionally with equity (2x at 2 million), rising and falling, otherwise risk of ruin rises if you only scale up.  #mech/risk_management
  > your bet size needs to change with your equity at some point
  indicator: account equity · asset: multi · direction: bet size proportional to equity · testable: yes · confidence: high
  ^MT097-C06-4
- **Dave Drew** How a trader behaves during drawdowns is one of the biggest determinants of long-run success, because drawdown psychology drives people to question and alter sound systems; confidence in solid long-term research is what keeps a systematic trader following the rules.  #mech/behavioral _(added by Opus)_
  > You know how people handle draw downs. I think it makes some of the biggest difference in who is successful over the long run
  asset: multi · horizon: years · conditions: during drawdowns · testable: partly - compare outcomes of rule changes made in drawdowns vs otherwise · confidence: high
  ^MT097-C06-X1

### C07
- **Dave Drew** Sizing from closed-trade equity (after stops) is more stable than from open-trade equity, which includes large open profits and encourages over-risking.  #mech/risk_management
  > Open equity it never works really. People can try it but closed equity or or equity after everything got wouldn't be stopped out
  indicator: closed-trade equity vs open-trade equity · asset: multi · direction: size off closed equity · testable: yes: compare sizing bases in backtest · confidence: medium
  **Correction (Opus):** Partly misattributed: Drew says only that open-equity sizing 'never works really' and closed equity is more stable; the reasoning that open equity includes big open profits and leads to over-risking, while closed equity is a stable step function, is Moritz Seibert's. → Drew: size from closed-trade equity rather than open-trade equity, which is more stable; Seibert adds the reason: open equity includes volatile open profits and invites over-risking.
  ^MT097-C07-1
- **Dave Drew** After a 50% drawdown bet size should be on the reduced equity base but not cut further, as extra de-risking gives too little risk to recover and distorts the statistics of the system.  #mech/risk_management
  > it probably shouldn't be 250,000 which would be too little risk put on to get out of the draw down
  indicator: drawdown recovery · asset: multi · testable: yes · confidence: medium
  **Correction (Opus):** Wrong speaker: the 1 million -> 500,000 example and the point that cutting to 250,000 would be too little risk and distorts the system's statistics are said by the host Moritz Seibert; Drew then agrees. → Moritz Seibert (Drew agreeing): after a 50% drawdown size on the reduced 500,000 base, not a further cut to 250,000, because extra de-risking leaves too little risk to recover and distorts the system's statistics.
  ^MT097-C07-2

### C09
- **Dave Drew** Seykota held that self-limiting beliefs (not feeling worthy) hold traders back, so psychological clearing is part of success.  #mech/behavioral
  > we limit ourselves in our success in the markets because we don't believe that we are deserving of great success
  asset: multi · testable: no · confidence: low
  ^MT097-C09-1
- **Dave Drew** End-of-day futures data downloads contained a lot of bad prints, so daily data cleaning (spotting bad data and finding correct values) was a necessary task before analysis.  #mech/research_method _(added by Opus)_
  > you'd get end of the day downloads and there was a lot of bad data and so I would each day I would look through all the data
  indicator: end-of-day futures price data quality · asset: multi · horizon: days · conditions: early 1990s data vendors · testable: partly - data error rates can be audited · confidence: high
  ^MT097-C09-X1

