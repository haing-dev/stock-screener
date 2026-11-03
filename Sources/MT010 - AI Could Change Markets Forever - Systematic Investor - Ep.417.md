---
source_id: MT010
title: "AI Could Change Markets Forever - Systematic Investor - Ep.417"
date: 2026-09-13
channel: "Top Traders Unplugged"
url: 
words: 12565
claims: 50
added_by_opus: 3
corrections: 0
crosscheck: "opus cross-check"
speakers: ["Niels Kastrup-Larsen (host, Top Traders Unplugged; caption spelling Neils Castro Razen)", "Rob Carver (co-host, systematic trader and author)"]
tags: [source, layer0]
---
# AI Could Change Markets Forever - Systematic Investor - Ep.417

**Speakers:** Niels Kastrup-Larsen (host, Top Traders Unplugged; caption spelling Neils Castro Razen); Rob Carver (co-host, systematic trader and author)

**Summary:** Top Traders Unplugged Ep.417 (Sept 2026): bond-market debt worries, the Simplify CTA ETF abandoning systematic discipline, and Rob Carver on fitting rule weights (average individual, asset-class and global fits) and limiting discretion to entries. Also AI risks in quant research, trend-following speed in V-shaped vs secular high-volatility regimes, and Man Group's quant-winter note.

**Approach:** trend following, systematic vs discretionary, forecast weight fitting, AI in quant research, volatility regimes

**Opus completeness estimate of first read:** 0.93 - first reader was thorough and accurate; missed Rob's view that Treasury buybacks are immaterial, the politics-vs-data point on asset-class fitting, and his reading of the paper's out-of-sample result

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro, bond market worries and government debt |
| C02 | 3 | Norway wealth fund, Treasury buybacks, bonds and trend followers, Rob short bonds |
| C03 | 2 | Simplify managed futures ETF subadvisor change, ETF structure risks |
| C04 | 3 | ETF now energy only, style drift, Millennium AUM |
| C05 | 2 | trend barometer, Rob's year and risk, market poised |
| C06 | 2 | SPR, September 2026 index performance, reader question on forecast weights |
| C07 | 1 | fitting level for rule weights, overfitting individual fits |
| C08 | 3 | pooled vs asset-class fit, averaging three fits |
| C09 | 2 | matrix fit, no-fitting prior, discretion plus systematic question |
| C10 | 3 | systematic means follow system, test difficulty, unleveraged trading |
| C11 | 4 | limit discretion to entries, retail losses, exit skill |
| C12 | 3 | exits, stop loss, vol scaling debate, AI governance intro |
| C13 | 3 | AI risks: overfitting, buggy code, governance |
| C14 | 3 | AI-driven retail trading, LLM bias toward trend following, VIX article intro |
| C15 | 4 | revisiting research, VIX-dependent speed, V-shapes |
| C16 | 4 | speed in COVID vs tariff tantrum, volatility meanings, simplicity prior |
| C17 | 3 | Man Group quant factors R-squared, quant winter, diversification |
| C18 | 1 | manager diversification; outro and disclaimer |
| C19 | 0 | nothing actionable: disclaimer fragment |

## Claims

### C01
- **Rob Carver** Late summer 2026: worries over government and AI-complex corporate debt, and US fiscal promises, are pushing yields up.  #mech/fiscal_debt _(time-bound view)_
  > pumping up yields and making the life of uh central bankers quite difficult
  indicator: government bond yields · asset: rates · horizon: months · testable: partly · confidence: medium
  ^MT010-C01-1

### C02
- **Niels Kastrup-Larsen** Norway's sovereign wealth fund proposed cutting government debt from 70% to 50% of its bond portfolio (about 5% of its total, roughly $100bn), while the US Treasury expands long-end buybacks, e.g. 6bn in 10-20 year bonds.  #mech/liquidity_flows _(time-bound view)_
  > last week it proposed chopping the weight of government debt in its bond portfolio from 70 to 50%
  indicator: sovereign wealth fund bond allocation, Treasury buybacks · asset: rates · horizon: months · testable: yes · confidence: medium
  ^MT010-C02-1
- **Niels Kastrup-Larsen** Big bond trends are good for trend followers; bonds drove returns in late 2021 to early 2023 and have detracted in the last two years, so a new bond trend could be coming.  #mech/cycle_persistence _(time-bound view)_
  > we know um from the CTA world that when you get big trends in bonds that's usually kind of an interesting uh time for for trend followers because it is a a big part of the overall portfolio
  indicator: bond trends in CTA portfolios · asset: rates · direction: short bonds · horizon: years · conditions: Bond trends · testable: yes · confidence: medium
  ^MT010-C02-2
- **Rob Carver** Rob's own positioning: short US 10-year and Korean 10-year bonds.  #mech/slow_reaction _(time-bound view)_
  > I am short um US bonds, specifically 10 years
  indicator: US 10-year, Korean 10-year · asset: rates · direction: short bonds · horizon: months · testable: no - disclosure of position · confidence: high
  ^MT010-C02-3
- **Rob Carver** Treasury long-end buybacks of a few billion dollars are far too small to hold down US yields; at most they are a policy signal, and yields have kept rising despite them.  #mech/liquidity_flows _(added by Opus, time-bound view)_
  > 6 billion in in the US bond market is it's not even a drop in the ocean. It's like a drop a drop inside a drop in the ocean.
  indicator: Treasury buyback size vs market size · asset: rates · direction: buybacks do not lower long yields · horizon: weeks · conditions: buybacks small relative to issuance · testable: yes - yield reaction around buyback operations · confidence: high
  ^MT010-C02-X1

### C03
- **Niels Kastrup-Larsen** The Simplify managed futures ETF (ticker CTA) manager overrode subadvisor signals and removed the subadvisor, moving mainly to long energy, which investors in a systematic fund did not expect.  #mech/behavioral _(time-bound view)_
  > the manager so simplify basically stepped in and took some decisions based on on what you know exposure should be rather than following um the uh the signals
  indicator: Simplify Managed Futures Strategy ETF · asset: commodities · direction: long energy · horizon: months · testable: no - anecdote · confidence: medium
  ^MT010-C03-1
- **Niels Kastrup-Larsen** ETF wrappers carry a risk that the strategy or the subadvisor changes without notice, unlike a fund run by the actual advisor.  #mech/risk_management
  > the underlying strategy can change, you know, in a heartbeat
  asset: multi · testable: no · confidence: medium
  ^MT010-C03-2

### C04
- **Rob Carver** According to Seeking Alpha the ETF went from over 50 markets to energy only, losing diversification across many markets, which is why low-Sharpe strategies like trend following make money.  #mech/risk_management _(time-bound view)_
  > they've gone from um having over 50 markets, which is kind of, you know, an sort of reasonable amount of diversification
  indicator: number of markets traded · asset: multi · testable: partly - need diversification-Sharpe evidence · confidence: high
  ^MT010-C04-1
- **Rob Carver** Investors want diversified trend following and resist style drift, which limits research innovation at managers.  #mech/behavioral
  > investors are very concerned about style drift
  asset: multi · testable: no · confidence: high
  ^MT010-C04-2
- **Niels Kastrup-Larsen** Millennium nearing $100bn AUM shows large allocations to multi-manager pods.  #mech/liquidity_flows _(time-bound view)_
  > Millennium apparently is nearing hundred billion dollars under management
  indicator: multi-manager AUM · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT010-C04-3

### C05
- **Niels Kastrup-Larsen** Trend barometer at 57 (strong), though equity momentum seems to be weakening after equities were a bright spot.  #mech/cycle_persistence _(time-bound view)_
  > my trend barometer finished yesterday at 57
  indicator: trend barometer, equity momentum · asset: multi · horizon: weeks · testable: yes · confidence: medium
  ^MT010-C05-1
- **Rob Carver** Rob feels markets are poised for a shock without reacting, which means little trend profit; his risk is about a third of average and his year is about +7.5% mostly from early weeks.  #mech/behavioral _(time-bound view)_
  > where the market's kind of tottering on the edge of something, right?
  indicator: trend system risk usage · asset: multi · horizon: months · conditions: Markets poised without firm reaction · testable: no - qualitative · confidence: low
  ^MT010-C05-2

### C06
- **Rob Carver** The US Strategic Petroleum Reserve keeps falling and will hit a limit, a possible catalyst along with midterms and the new Fed chair.  #mech/policy_reaction _(time-bound view)_
  > it is going to reach a crunch point where they can't release any more from there
  indicator: US SPR level · asset: commodities · horizon: months · testable: partly · confidence: medium
  ^MT010-C06-1
- **Niels Kastrup-Larsen** Mid-September 2026: BTOP50 +1.15% (YTD +12.42%), SG Trend about +12.1% YTD, versus MSCI World +12.78% and S&P 500 TR +12.45% YTD, world bonds -0.32% YTD.  #mech/cycle_persistence _(time-bound view)_
  > the Btop 50 index is up 1.15% so far in September, up 12.42% so far this year
  indicator: BTOP50, SG Trend, MSCI World, S&P 500 TR · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT010-C06-2

### C07
- **Rob Carver** Fitting rule weights per instrument is overfitting; fitting per asset class or pooled across all instruments does about as well.  #mech/research_method
  > you probably shouldn't um fit everything individually because then you really do have a lot of noise and not much signal
  indicator: forecast weights fit level · asset: multi · horizon: years · testable: yes - Rob's blog tests · confidence: high
  ^MT010-C07-1
- **Rob Carver** Whether to use different rule weights (more carry, faster or slower trend) by asset class was partly decided by organisational politics in asset-class research teams; it should instead be treated as an empirical question tested on data.  #mech/research_method _(added by Opus)_
  > that's actually um partly a political question in a way because um you know um as as people managing a specific part of our portfolio, we we you know we'd get very protective about it
  indicator: asset-class-specific vs pooled rule weights · asset: multi · conditions: asset-class team structure (AHL example) · testable: yes - compare pooled vs asset-class fits out of sample · confidence: medium
  ^MT010-C07-X1

### C08
- **Rob Carver** Pooled (all instruments) and asset-class fits both work; with few instruments (e.g. 2 bonds, 3 equities, 1 FX) do not fit by asset class.  #mech/research_method
  > both did pretty well um and so um it's probably fine to do either of those
  indicator: pooled vs asset-class fit · asset: multi · horizon: years · conditions: Small portfolios · testable: yes · confidence: high
  ^MT010-C08-1
- **Rob Carver** Most robust: average the individual, asset-class and global fits, which has about 0.98 to 0.99 correlation with global-only fitting, mattering more for small portfolios.  #mech/research_method
  > I could just put a third of my risk capital in each and that's equivalent to just taking the average of those three
  indicator: average of three fits · asset: multi · horizon: years · conditions: Small portfolios · testable: yes · confidence: high
  ^MT010-C08-2
- **Niels Kastrup-Larsen** Some managers use global parameters with different models for diversification.  #mech/research_method
  > use global parameter selection but then you have different models
  asset: multi · testable: no · confidence: medium
  ^MT010-C08-3

### C09
- **Rob Carver** A matrix fit that allocates to fast trend in cheap, diversifying markets adds complexity but little value.  #mech/research_method
  > I did look at that and found that it you know it makes things very complicated and it doesn't really add a lot of value
  indicator: matrix fit · asset: multi · horizon: years · testable: yes - blog test · confidence: medium
  ^MT010-C09-1
- **Rob Carver** Default to no fitting; fit only with strong, robust, out-of-sample evidence.  #mech/research_method
  > my prior is to do no fitting yeah at all and only if I see strong evidence of add value will I do some fitting
  asset: multi · testable: no · confidence: high
  ^MT010-C09-2

### C10
- **Rob Carver** Systematic trading means following the system; overriding signals makes the system impossible to test.  #mech/research_method
  > they did agree that that yes all right systematic trading does actually mean literally blindly doing exactly what the system tells you
  asset: multi · testable: no · confidence: high
  ^MT010-C10-1
- **Rob Carver** Ignoring system signals when inconvenient is the worst way to mix discretion and systematic.  #mech/research_method
  > it makes it very hard to test um, whether your system's actually working or not
  asset: multi · testable: yes · confidence: high
  ^MT010-C10-2
- **Rob Carver** Non-leveraged traders must rank positions and use path-dependent swap rules.  #mech/risk_management
  > You have to be able to rank and order positions and and have sort of path dependent rules about swapping in and out positions
  asset: multi · conditions: Unleveraged accounts · testable: partly · confidence: medium
  ^MT010-C10-3

### C11
- **Rob Carver** Limit discretion to what and when to buy; make speed, exits and position size rule-based.  #mech/research_method
  > limit the discretionary part of a trading strategy to one tiny part, which is the what should I buy and when decision
  asset: multi · testable: partly - test skill statistically · confidence: medium
  ^MT010-C11-1
- **Rob Carver** 95% of retail traders lose money, mainly from position, cost and risk management errors, not entries alone.  #mech/behavioral
  > 95% of retail traders lose money about 5% make money
  indicator: retail trader outcomes · asset: multi · testable: yes · confidence: medium
  ^MT010-C11-2
- **Rob Carver** Skill in entries and in exits are separate; mutual fund managers pick well but exit poorly.  #mech/behavioral
  > there are a lot of mutual fund managers with genuine skill at finding good stocks but actually terrible skill in choosing when to exit those positions
  asset: equities · testable: yes - academic research cited · confidence: medium
  ^MT010-C11-3
- **Rob Carver** Discretionary exits are allowed only with a statistically significant track record of skill.  #mech/research_method
  > essentially a statistically significant track record that proves that you have skill in doing that
  asset: multi · testable: yes · confidence: high
  ^MT010-C11-4

### C12
- **Niels Kastrup-Larsen** Trend models enter at about the same time; managers differ in risk management and exit.  #mech/risk_management
  > I think where the big differentiator is between managers is actually how they manage the risk along the trade but also where they get out
  indicator: exit rules · asset: multi · horizon: months · testable: yes - compare exit rules · confidence: medium
  ^MT010-C12-1
- **Rob Carver** Where discretion is retained, use a simple stop-loss to hand exits to a rule.  #mech/risk_management
  > you should use a stop loss which is something I don't use myself of course
  indicator: stop loss · asset: multi · testable: yes · confidence: medium
  ^MT010-C12-2
- **Rob Carver** Biggest debate: whether to resize positions for volatility after entry or let them ride.  #mech/risk_management
  > the biggest debate um in the industry is over vol scaling after you after entry right
  indicator: post-entry vol scaling · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT010-C12-3

### C13
- **Rob Carver** AI in quant research mainly risks overfitting, needing guard rails and non-AI code.  #mech/research_method
  > the biggest risk is potentially that it will just overfit um and you need to put very strong guard rails around it
  asset: multi · testable: yes · confidence: high
  ^MT010-C13-1
- **Rob Carver** AI code review found a serious bug but introduced a worse one that would have deleted all short positions, so AI-written code needs oversight.  #mech/risk_management
  > I'd be really concerned if if people had you know live production code actually trading that that had been written by II with either no or or insufficient human oversight
  asset: multi · testable: no · confidence: high
  ^MT010-C13-2
- **Rob Carver** Governance and code oversight apply equally to AI-assisted systems.  #mech/risk_management
  > oversight governance and processes around code implementation are absolutely key
  asset: multi · testable: no · confidence: high
  ^MT010-C13-3

### C14
- **Rob Carver** A wave of consumer-grade AI trading may raise turnover, risk and volatility, but evidence is too early.  #mech/behavioral _(time-bound view)_
  > there will be quite a small percentage who are using AI correctly
  indicator: retail/institutional AI-driven trading · asset: multi · horizon: years · testable: partly · confidence: low
  ^MT010-C14-1
- **Rob Carver** Uninformed AI-driven retail herds create opportunities to trade the other side.  #mech/crowding_positioning _(time-bound view)_
  > I think we're going to see a herd of uninformed AIdriven uh retail investors. Um, and uh, I think there'll be opportunities there.
  asset: multi · direction: trade against AI retail herd · horizon: years · testable: no - method unclear · confidence: low
  ^MT010-C14-2
- **Rob Carver** LLMs recommend large trend-following allocations because their training text advocates it, so their advice is circular.  #mech/behavioral
  > it's been trained on reading the internet and you know on the internet there are lots of people saying including myself and you
  asset: multi · testable: no · confidence: medium
  ^MT010-C14-3

### C15
- **Rob Carver** Revisit published research after about 10 years for out-of-sample evidence (Alpha Architect VIX and trend; Lasse Pedersen 100-year trend paper).  #mech/research_method
  > 10 years is long enough normally to get some additional evidence
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT010-C15-1
- **Rob Carver** Rob trades less momentum when volatility is high, while the article trades faster when VIX is high.  #mech/risk_management
  > when the market's more volatile I I trade less momentum
  indicator: VIX-dependent speed · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT010-C15-2
- **Niels Kastrup-Larsen** Slow trend following handled the tariff tantrum V-shape well, so being fast in high vol may not pay.  #mech/slow_reaction
  > being slow during periods like um the tariff tantrum whatever it was called liberation day
  indicator: slow vs fast trend in V-shape · asset: multi · horizon: weeks · conditions: V-shaped sell-offs · testable: yes · confidence: medium
  ^MT010-C15-3
- **Rob Carver** In a V-shaped market be very fast or very slow, not medium speed; 2008 was a secular turn, not a V.  #mech/slow_reaction
  > if the market is doing a Vshape, you want to be either very slow or very fast
  indicator: trend speed in V-shaped markets · asset: multi · horizon: weeks · conditions: V-shaped markets · testable: yes · confidence: medium
  ^MT010-C15-4

### C16
- **Rob Carver** In COVID 2020 fast and slow trend followers did well and medium speed did worst, while in the 2025 tariff tantrum (very quick V) fast trend did worst.  #mech/slow_reaction
  > slow trend following also very slow trend following also did well kind of medium speed would have done the worst
  indicator: trend speed in COVID vs tariff tantrum · asset: multi · horizon: weeks · testable: yes · confidence: medium
  ^MT010-C16-1
- **Rob Carver** High volatility can mean 2008, 2020 or the tariff tantrum, with different optimal speeds, and one cannot know ahead which.  #mech/research_method
  > effectively high volatility could mean one of three different things
  indicator: volatility regimes · asset: multi · testable: yes · confidence: high
  ^MT010-C16-2
- **Rob Carver** High volatility does not help trend following as the straddle intuition suggests, since results depend on trend speed, reaction speed and trading speed.  #mech/cycle_persistence
  > when volatility is high trend following doesn't do as well is actually counterintuitive because people expect that high volatility is good for trend following
  indicator: volatility vs trend following returns · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT010-C16-3
- **Rob Carver** Rob will not implement VIX-based speed changes: prior toward simplicity, though the finding is not random data mining.  #mech/research_method
  > I have a prior towards simplicity which means I have a prior towards not doing this kind of thing
  asset: multi · testable: no · confidence: high
  ^MT010-C16-4
- **Rob Carver** Rob reads the decade-later Alpha Architect update as showing that VIX-dependent trend speed still seems to work out of sample, while warning that the headline result hides much and should not be copied into a system without understanding it.  #mech/research_method _(added by Opus)_
  > they they did find that it still this thing still seems to work.
  indicator: VIX-dependent lookback vs static lookback · asset: multi · horizon: months · conditions: out-of-sample extension of 2016-17 study · testable: yes - replicate on own data · confidence: low
  ^MT010-C16-X1

### C17
- **Rob Carver** Man Group note: classic factors (value, momentum) did badly in the 2018-2020 quant winter, and factor R-squared in manager returns varies over 25 years.  #mech/crowding_positioning
  > the quant winter was in it was 2018 to 2020 and and this was a period of time when these these factors did didn't do very well
  indicator: value and momentum factors, 2018-2020 · asset: equities · horizon: years · testable: yes · confidence: high
  ^MT010-C17-1
- **Rob Carver** Quant equity managers differ and do not simply hold basic factors.  #mech/research_method
  > quant equity quant managers are not all the same and they are doing things differently
  indicator: manager factor R-squared · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT010-C17-2
- **Rob Carver** Diversification across managers disappears in crowded events like the quant winter.  #mech/crowding_positioning
  > diversification has a habit of going away during events like the quant winter when everyone does
  asset: equities · horizon: weeks · conditions: Crowded unwinds · testable: yes · confidence: medium
  ^MT010-C17-3

### C18
- **Rob Carver** Diversify across managers since picking the best is hard; quant equity offers rising idiosyncratic performance.  #mech/risk_management
  > if you can afford it you should you should definitely diversify because it's very hard to to pick who the best manager will be
  asset: equities · horizon: years · testable: partly · confidence: medium
  ^MT010-C18-1

