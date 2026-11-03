---
source_id: MT042
title: "Diversification is more important than ever! - Systematic Investor - Ep.385"
date: 2026-02-01
channel: "Top Traders Unplugged"
url: 
words: 11692
claims: 65
added_by_opus: 5
corrections: 4
crosscheck: "opus cross-check"
speakers: ["Niels Kaastrup-Larsen (host, Top Traders Unplugged; caption 'Neils Krup Larson')", "Katy Kaminski (AlphaSimplex, trend following researcher; caption 'Katie Kaminsky')"]
tags: [source, layer0]
---
# Diversification is more important than ever! - Systematic Investor - Ep.385

**Speakers:** Niels Kaastrup-Larsen (host, Top Traders Unplugged; caption 'Neils Krup Larson'); Katy Kaminski (AlphaSimplex, trend following researcher; caption 'Katie Kaminsky')

**Summary:** Top Traders Unplugged, late January 2026: weekly systematic investor review of trend following. Metals and multi-sector trends drove a strong start to 2026. Katy Kaminski's annual paper on dispersion: speed, market set and volatility estimation explain return differences.

**Approach:** trend following, CTA dispersion, volatility sizing, crisis alpha, commodities

**Opus completeness estimate of first read:** 0.92 - first reader was very thorough on mechanisms, numbers and design-choice findings; missed a few caveats (QIS AUM, unofficial data, inflation analogue, non-vol-adjusted returns) and misread two speed/vol statements.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, disclaimer, weather small talk; mention of gold and silver extremes |
| C02 | 7 | gold/Tether, central bank buying, dollar 200-month MA, commodity super cycle, replicators, metals YTD |
| C03 | 3 | return dispersion, narrow vs broad trends, silver vs gold, liquidity chat |
| C04 | 5 | CTAs not driving gold, vol-based sizing, trend index highs, negative press, currencies |
| C05 | 5 | January 2026 sector diversification, trend barometer, SocGen indicators, index numbers |
| C06 | 2 | market index numbers, book plug, press coverage, trend after shifts |
| C07 | 3 | booms and busts, 2025 trend vs macro, economic vs price trend correlation |
| C08 | 4 | complementarity, CPI/PCE data, design choices and dispersion |
| C09 | 3 | speed by year, shorter and longer windows, V-shaped shock |
| C10 | 5 | trade frequency, signal delay, speed definition, best lookback by year, Covid |
| C11 | 4 | CTA style analysis, reactivity, data preprocessing, narrow liquid-asset set |
| C12 | 5 | 10-asset concentration vs diversified, volatility estimation as calibration, 2022 and 2025 examples |
| C13 | 3 | vol window speed, asymmetric resizing, 2025 pure trend familiar |
| C14 | 5 | crisis alpha definition and traits, Covid vs 2022 trends, cyclicality, deglobalization |
| C15 | 2 | Omicron day then 2022, Makita paper, crowding and liquidity |
| C16 | 3 | CTA share of hedge fund AUM, 2026 research plans, geopolitical risk measures |
| C17 | 1 | trend and geopolitical risk preview; outro |

## Claims

### C02
- **Niels Kaastrup-Larsen** Tether holds gold on a scale comparable to sovereign funds and central banks, so stablecoin-linked flows may help explain extreme gold and metals moves and hint at a monetary system shift.  #mech/liquidity_flows _(time-bound view)_
  > like as big a holder of gold as some of the so you know sovereign wealth funds but also some of the central banks
  indicator: gold holdings of Tether · asset: commodities · direction: Gold up · testable: partly - holdings reported by press · confidence: medium
  ^MT042-C02-1
- **Niels Kaastrup-Larsen** Central banks have been net gold buyers every year since 2011 after being net sellers in 2000-2009, a structural change in gold demand.  #mech/structural_shift
  > it looks like there's been a positive buying of gold uh every single year since 2011 by central banks whilst in 2000 through 2009 they sold net gold every single year
  indicator: central bank net gold purchases · asset: commodities · direction: Gold up · horizon: years · testable: yes - World Gold Council data · confidence: high
  ^MT042-C02-2
- **Niels Kaastrup-Larsen** A break of the US dollar below its 200-month moving average would signal a structurally weak dollar world with implications across assets.  #mech/cycle_persistence _(time-bound view)_
  > the US dollar is flirting with its 200 month simple moving average trying to penetrate it to the downside
  indicator: US dollar index vs 200-month simple moving average · asset: fx · direction: Dollar down · horizon: years · conditions: if the break holds · testable: yes - price rule is testable · confidence: medium
  ^MT042-C02-3
- **Niels Kaastrup-Larsen** Commodity prices in dollars tend to rise when the dollar is weak.  #mech/cycle_persistence
  > commodities tend to do better in nominal price uh when when the dollar is weak um not always but but um often
  indicator: US dollar · asset: commodities · direction: Commodities up when dollar down · conditions: not always · testable: yes - regress commodity returns on dollar · confidence: medium
  ^MT042-C02-4
- **Niels Kaastrup-Larsen** Commodity super cycles start with a change in the monetary system; earlier false starts failed because no such change occurred, but this time may differ.  #mech/structural_shift _(time-bound view)_
  > a commodity super cycle really take off when you have some kind of change in the monetary system
  asset: commodities · direction: Commodities up · horizon: years · conditions: needs monetary-system change · testable: partly - few historical cases · confidence: medium
  ^MT042-C02-5
- **Niels Kaastrup-Larsen** Popular CTA replicators hold fewer markets and little commodity exposure, so in a commodity super cycle they could miss the diversification a full CTA offers.  #mech/structural_shift _(time-bound view)_
  > some of the most popular CTA products have not been the underlying CTAs, it's been the replicators who tend to have much less exposure to commodities
  asset: commodities · horizon: years · conditions: if commodities lead · testable: partly - compare replicator and CTA returns · confidence: medium
  ^MT042-C02-6
- **Niels Kaastrup-Larsen** In January 2026 silver, platinum and gold rose 68%, 35% and 27% year to date, evidence of strong commodity trends.  #mech/cycle_persistence _(time-bound view)_
  > silver is up 68% so far, uh, this year. Platinum 35% uh, and gold is only up 27% so far
  indicator: silver, platinum, gold YTD returns · asset: commodities · direction: Metals up · horizon: weeks · testable: yes - price data · confidence: high
  ^MT042-C02-7

### C03
- **Katy Kaminski** Trend followers' returns differ mainly by how much risk they allocate to the few big trends, which depends on their market set.  #mech/risk_management
  > positive returns come from big trends and you need to be exposed to these big trends and it's how much risk allocation you have to them that differentiates relative performance
  asset: multi · horizon: years · testable: yes - decompose CTA returns by market · confidence: high
  ^MT042-C03-1
- **Katy Kaminski** In 2025 only a narrow set of assets trended profitably, so managers in that set looked good.  #mech/cycle_persistence _(time-bound view)_
  > Last year it was a very narrow band of assets that actually did well in trending
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT042-C03-2
- **Katy Kaminski** In early 2026 trends are broad (copper, aluminum, silver, gold, platinum, palladium), so a diversified CTA captures more than a gold-only replicator.  #mech/cycle_persistence _(time-bound view)_
  > right now what we're seeing is a much more broad um you know range of trends
  asset: commodities · direction: Metals up · horizon: weeks · testable: yes · confidence: medium
  ^MT042-C03-3

### C04
- **Niels Kaastrup-Larsen** Trend followers bought gold long ago and are now cutting positions as volatility rises, so blaming CTAs for commodity spikes is wrong.  #mech/crowding_positioning _(time-bound view)_
  > we're not the ones buying gold right now. If anything, we're probably the ones selling into this rally because of expansion of volatility
  asset: commodities · direction: CTA selling into rally · horizon: weeks · testable: partly - positioning data · confidence: medium
  ^MT042-C04-1
- **Katy Kaminski** Volatility-targeted CTAs cut positions when asset volatility rises, giving profit taking and spreading risk across metals.  #mech/risk_management
  > as the V of assets go up, using a traditional CTA approach, you would actually reduce your positions
  indicator: asset volatility · asset: multi · direction: Position size down as vol rises · horizon: weeks · testable: yes - mechanical rule · confidence: high
  ^MT042-C04-2
- **Niels Kaastrup-Larsen** Many CTAs were near new highs in late January 2026, which tends to draw allocator interest.  #mech/crowding_positioning _(time-bound view)_
  > the gen trend index is getting very close to getting back at new all-time highs
  indicator: SG Trend Index · asset: multi · horizon: weeks · testable: yes - index data · confidence: medium
  ^MT042-C04-3
- **Niels Kaastrup-Larsen** Negative press on trend following (WSJ, Man Group 'all hands on deck' in 2025) came near the low, so bad coverage is a contrarian buy signal.  #mech/behavioral
  > negative press is not the worst thing we can get. It's usually a good sign uh and buying opportunity
  asset: multi · direction: Trend following up after negative press · horizon: months · testable: partly - needs press sentiment series · confidence: low
  ^MT042-C04-4
- **Niels Kaastrup-Larsen** A dollar break could revive the currency sector, and with equities and fixed income trending, big sectors working together lift CTA returns.  #mech/cycle_persistence _(time-bound view)_
  > what if it does break the 200 month moving average whatever I mean could currency as a sector come back and really um help out
  indicator: US dollar 200-month moving average · asset: fx · direction: Currency trend profits up · horizon: years · conditions: if dollar breaks · testable: partly - conditional on break · confidence: medium
  ^MT042-C04-5
- **Niels Kaastrup-Larsen** Trend followers that do not volatility-adjust keep full size as volatility explodes in a trending market (metals, January 2026), so they earn far more than vol-targeted CTAs in such a month, at the cost of larger risk.  #mech/risk_management _(added by Opus, time-bound view)_
  > for those who don't volatility adjust their positions, they're having a incredible maybe a worldbreaking uh month of January
  indicator: volatility-adjusted vs unadjusted trend returns · asset: commodities · horizon: weeks · conditions: strong trend accompanied by rising volatility · testable: yes - compare vol-scaled and constant-notional trend backtests in vol-expansion trends · confidence: medium
  ^MT042-C04-X1

### C05
- **Katy Kaminski** Trend following does best and is least exposed to reversal when profits come from many sectors at once, as in January 2026.  #mech/risk_management _(time-bound view)_
  > the profitability of trends has been diversified across multiple sectors
  asset: multi · horizon: weeks · conditions: when trends are spread across sectors · testable: yes - sector attribution · confidence: high
  ^MT042-C05-1
- **Katy Kaminski** January 2026 trends: equities up, short US dollar (AUD strong), precious and base metals up, energies still hard.  #mech/cycle_persistence _(time-bound view)_
  > this diversification of the different trends both the weak dollar theme combined with prog growth uh pro metals
  asset: multi · direction: Long equities, short USD, long metals · horizon: weeks · testable: yes · confidence: high
  ^MT042-C05-2
- **Katy Kaminski** On equity down days other trend positions (dollar, metals) offset, showing trend portfolios are not just equity exposure.  #mech/risk_management
  > I always find it useful when there's a day where the S&P is down and you see that the trends diversify
  asset: multi · horizon: days · conditions: risk-off days · testable: yes - conditional return analysis · confidence: medium
  ^MT042-C05-3
- **Niels Kaastrup-Larsen** Niels's trend barometer reading of 59 marks a strong trend environment in line with January performance.  #mech/cycle_persistence _(time-bound view)_
  > my trend barometer yesterday finished at 59
  indicator: Niels's trend barometer · asset: multi · horizon: weeks · testable: yes - indicator available · confidence: medium
  ^MT042-C05-4
- **Niels Kaastrup-Larsen** The SocGen Trend Indicator, a replication of manager positioning, rose 19.27% month to date, and CTA indices were up about 5-6%, so positioning is a proxy for manager returns.  #mech/crowding_positioning _(time-bound view)_
  > the information they put out is very useful for people if they want to understand how managers might be positioned
  indicator: SocGen Trend Indicator; SG Trend Index · asset: multi · horizon: weeks · testable: yes · confidence: medium
  **Correction (Opus):** Adds an inference not in the text ('positioning is a proxy for manager returns'); Niels says the SocGen Trend Indicator has not performed well historically but is useful for estimating how managers are positioned, and its 19.27% month-to-date gain may be a record. → The SocGen Trend Indicator has had weak historical performance but is useful for inferring CTA positioning; it was up 19.27% month to date (late January 2026), possibly a record, while CTA indices were up about 5-6%.
  ^MT042-C05-5

### C06
- **Katy Kaminski** Media profiles of trend following show up at performance extremes, so coverage is a sentiment marker.  #mech/behavioral
  > when Bloomberg or Wall the Wall Street Journal, anyone is sort of starts profiling trend falling, that's usually a sign that things are going really well or things are going really bad
  asset: multi · testable: partly - needs coverage data · confidence: low
  ^MT042-C06-1
- **Katy Kaminski** Last year's regime shifts created fundamental changes that are now maturing into strong trends in 2026.  #mech/structural_shift _(time-bound view)_
  > we've seen the aftermath of such huge shifts in fundamental relationships that are now sort of coming to a fruition and becoming really strong trends
  asset: multi · horizon: months · testable: no - narrative · confidence: medium
  ^MT042-C06-2

### C07
- **Katy Kaminski** Trend following needs boom-bust cycles, not steady markets or sudden shocks; strong US growth (all systems go until it's not) fits.  #mech/cycle_persistence
  > steady as you go is not good for us and shocks are not good but you know booms and busts are great
  asset: multi · horizon: years · testable: partly - classify regimes · confidence: medium
  ^MT042-C07-1
- **Katy Kaminski** In 2025 headline and shock-driven prices hurt price trend while macro and economic-trend strategies did better; in 2026 macro lags as fundamentals are clearer.  #mech/slow_reaction _(time-bound view)_
  > macro strategies and sort of more fundamental approaches or perhaps economic trend and things that kind of looked through the prices and focused on the fundamentals were a little bit better positioned
  indicator: SG Trend Index vs macro strategies · asset: multi · horizon: years · conditions: years with headline shocks · testable: yes - compare indices · confidence: medium
  ^MT042-C07-2
- **Katy Kaminski** Economic trend (growth acceleration, inflation change) and price trend are 40-50% correlated and differ in timing, so they complement each other.  #mech/research_method
  > they're roughly, you know, 40 50% correlated because they end up in the same trends
  indicator: economic trend signals vs price trend · asset: multi · horizon: years · testable: yes - correlation · confidence: high
  ^MT042-C07-3

### C08
- **Katy Kaminski** Price trend reacts faster than macro trend, which can be slow or wrong at turning points, while macro trend helps when prices are driven by sentiment.  #mech/slow_reaction
  > price trends can better capture some of the themes at different points and more aggressively than say a macro trend which can sometimes be slow or get the macro wrong when things change
  asset: multi · testable: yes · confidence: medium
  ^MT042-C08-1
- **Katy Kaminski** Official data releases such as CPI and PCE act as focal points that confirm or deny themes for price trends, despite missing US data during the shutdown.  #mech/policy_reaction
  > they are a focal point for price trends as well
  indicator: CPI, PCE releases · asset: multi · testable: partly · confidence: medium
  ^MT042-C08-2
- **Katy Kaminski** CTA design choices (speed, market count, risk allocation, vol sizing, position sizing) are manager-specific and have no single right answer.  #mech/research_method
  > the speed you trade, the number of markets you trade, the risk allocation, your volatility sizing, position sizing, all of these are sort of idiosyncratic decisions to individual managers
  asset: multi · horizon: years · testable: yes - decompose by design choice · confidence: high
  ^MT042-C08-3
- **Katy Kaminski** Managers' returns correlate highly yet design choices (market set, speed) cause large return gaps in extreme years, and the best choice flips from year to year.  #mech/research_method
  > in one year one the choice might look very smart and then the next year it could
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT042-C08-4
- **Katy Kaminski** Economic-trend models run on global data from many regions plus unofficial sources, so a gap in official US releases (the shutdown) only partly blinds them.  #mech/research_method _(added by Opus)_
  > there's also other methods and other data sources that people can use that are not necessarily the official
  indicator: official vs alternative macro data in economic trend signals · asset: multi · conditions: when official data are delayed or missing · testable: partly - can test signal degradation with missing releases · confidence: medium
  ^MT042-C08-X1

### C09
- **Katy Kaminski** In 2025 short and long lookbacks (12 months) did best while 4-9 month lookbacks did worst; in 2024 fast was hard and slow better.  #mech/cycle_persistence _(time-bound view)_
  > the worst time horizons are around 7 to n months or 4 to 9 months
  indicator: trend lookback window · asset: multi · horizon: years · testable: yes - lookback sweep · confidence: high
  ^MT042-C09-1
- **Katy Kaminski** Short-lookback models exit and re-enter after a V-shaped shock (Liberation Day), while medium windows get whipsawed.  #mech/slow_reaction
  > if you have a shorter window, you get out, you get back in, you keep moving, and you don't get rattled as much by sort of this extreme V-shaped move
  asset: multi · horizon: weeks · conditions: V-shaped reversals · testable: yes · confidence: medium
  ^MT042-C09-2
- **Katy Kaminski** The best trend speed changes by year; fast trend worked in 2022 and Covid, slow in other years, so no speed always wins.  #mech/cycle_persistence
  > the year before you saw the opposite that fast was really hard and slow again was better
  asset: multi · horizon: years · testable: yes · confidence: high
  **Correction (Opus):** The text does not say fast trend worked in 2022; Kaminski says fast was better in Covid (C10) and that fast was hard and slow better the year before 2025. → The best trend speed changes by year: fast was hard and slow better in 2024, faster was better in Covid, so no speed always wins.
  ^MT042-C09-3

### C10
- **Niels Kaastrup-Larsen** Weekly rebalancing (or delayed execution) cut differences in April 2025, so speed also depends on trade frequency and signal delays.  #mech/research_method _(time-bound view)_
  > if you only adjusted position once a week and you didn't you didn't really you know you didn't panic let's you know quote unquote panic uh during liberation day
  indicator: trade frequency; signal delay · asset: multi · horizon: weeks · testable: yes · confidence: medium
  **Correction (Opus):** Wrong meaning: Niels says the biggest differences between managers in 2025 arose in April (Liberation Day), driven by trade frequency (weekly traders who did not 'panic'), not that weekly trading cut differences. → In 2025 the largest return differences among CTAs arose in April around Liberation Day, partly from trade frequency: managers who adjusted positions only weekly did not react to the V-shaped move.
  ^MT042-C10-1
- **Niels Kaastrup-Larsen** Some managers delay trading 3 days after a signal, an execution-speed lever separate from lookback length.  #mech/research_method
  > we get the signal today but we we actually wait 3 days before we change uh positions based on that signal
  indicator: signal delay · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT042-C10-2
- **Katy Kaminski** Speed combines window, trade adjustment and signal smoothing; nonlinear or ML models can have time-varying speed.  #mech/research_method
  > it's not just the window size. It's you know how you adjust your trading. It's how you smooth your signals
  asset: multi · testable: partly · confidence: medium
  ^MT042-C10-3
- **Niels Kaastrup-Larsen** In 25 years of data the best lookback in about 70% of years was 200+ days, but some runs of years differ (56 days best in 2008); Nick Bolters's analysis agrees.  #mech/research_method
  > most years probably um eyeball bowling it now maybe 70% of the years it's kind of 200 days upwards
  indicator: best lookback by calendar year · asset: multi · horizon: years · testable: yes - calendar-year lookback sweep · confidence: medium
  ^MT042-C10-4
- **Katy Kaminski** In 2020 faster trend was better, again showing the best speed depends on the year's path.  #mech/cycle_persistence
  > in a year like co we definitely saw that as well being faster was better there
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT042-C10-5

### C11
- **Katy Kaminski** CTA style analysis shows the industry became slower and more diversified (carry, other risk premia), so the index return history is not what an allocator gets today.  #mech/structural_shift
  > early on CTAs were a lot faster than they are today
  indicator: SG Trend Index decomposition · asset: multi · horizon: years · testable: yes - published decomposition · confidence: high
  ^MT042-C11-1
- **Katy Kaminski** Fast reactivity matters in crises even though slower models did a little better recently.  #mech/slow_reaction
  > some of that reactivity is still very very important for sort of these crisis alpha or dislocation periods
  asset: multi · horizon: years · conditions: dislocation periods · testable: yes · confidence: medium
  ^MT042-C11-2
- **Niels Kaastrup-Larsen** Data preprocessing before signals is an important, undisclosed part of CTA edge.  #mech/research_method
  > what we do with the data before we we generate our signals
  asset: multi · testable: no - proprietary · confidence: low
  ^MT042-C11-3
- **Katy Kaminski** A trend portfolio of the 10 most liquid assets (gold, crude, yen, bonds) did well in 2021, 2024 and 2025 versus a wide basket.  #mech/cycle_persistence _(time-bound view)_
  > that narrow asset was actually positive for 2025, very positive in 2024 and also did well in 2021
  indicator: trend on top-10 liquid assets vs wide basket · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT042-C11-4

### C12
- **Katy Kaminski** The 10-asset trend portfolio underperformed a diversified basket for 10 years straight, so a concentrated set can be right for years or wrong for a decade; replication must be diversified.  #mech/research_method
  > there's actually a 10-year period where those 10 assets underperformed a diversified basket for 10 years in a row
  asset: multi · horizon: years · testable: yes - rolling comparison · confidence: high
  ^MT042-C12-1
- **Katy Kaminski** Volatility estimation sizes positions as risk, not alpha, but changes the return path depending on how fast it adjusts.  #mech/risk_management
  > volatility estimation is not really an alpha signal but it's a calibration
  indicator: volatility estimate speed · asset: multi · testable: yes · confidence: high
  ^MT042-C12-2
- **Katy Kaminski** CTAs treat each asset as a unit of risk and size by volatility and signal strength, not by notional value.  #mech/risk_management
  > we don't talk about dollars we don't talk about notional value we talk about risk and we allocate risk
  asset: multi · testable: yes · confidence: high
  ^MT042-C12-3
- **Katy Kaminski** In 2022 bond volatility doubled (about 4 to 8); slow vol estimates kept larger positions in the bond downtrend and captured more of it, while fast estimates cut risk early.  #mech/risk_management
  > in a year like 2022 having slower volatility estimates was very beneficial because trends were working
  indicator: bond volatility; volatility estimation speed · asset: rates · horizon: years · conditions: trending year with rising vol · testable: yes · confidence: high
  ^MT042-C12-4
- **Katy Kaminski** In 2025 slow vol estimates were better in H1 and fast better in H2, so speed of vol adjustment helps or hurts depending on path.  #mech/risk_management
  > We saw in the first half of the year it was better to um have slower volatility and then it was better to be faster
  asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT042-C12-5

### C13
- **Niels Kaastrup-Larsen** Short vol windows cut risk quickly in events like COVID, SVB, Liberation Day.  #mech/risk_management
  > if we have very short-term volatility estimation we can reduce our risk very quickly
  indicator: volatility estimation window · asset: multi · direction: Position size down · horizon: days · testable: yes · confidence: medium
  ^MT042-C13-1
- **Katy Kaminski** Cutting risk fast on a shock and restoring it fast later captures more; downsizing and resizing speeds need not be equal.  #mech/risk_management
  > if you adjusted the vault back down quickly again then you would be able to capture the second half of the year better
  asset: multi · horizon: months · testable: yes - asymmetric vol-estimation test · confidence: medium
  **Correction (Opus):** Omits Kaminski's point that faster volatility adjustment was painful at Liberation Day; the asymmetric downsize/resize speed idea is Niels's, in the same chunk. → Faster volatility adjustment hurt at Liberation Day (cutting into a V-shaped move) but, if vol estimates came back down quickly, captured more of the second half of 2025; Niels adds that the speed for cutting risk and for re-adding it need not be the same.
  ^MT042-C13-2
- **Niels Kaastrup-Larsen** 2025 looked unusual, but for pure trend it was typical: a few markets gave the profit, many were flat or negative.  #mech/cycle_persistence _(time-bound view)_
  > there were like a handful of markets that did all the work and then there are lots of markets that didn't really do so well
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT042-C13-3
- **Niels Kaastrup-Larsen** As deglobalization makes markets behave more independently, the choice of volatility-estimation speed matters more for trend returns.  #mech/structural_shift _(added by Opus)_
  > it's something that is perhaps becoming more important in an odd way as the world gets more delobalized and more independent in the way market behavior uh shows up
  indicator: volatility estimation speed; cross-market correlation · asset: multi · horizon: years · conditions: deglobalized, less correlated markets · testable: partly - can test dispersion of vol-speed variants vs cross-asset correlation · confidence: low
  ^MT042-C13-X1

### C14
- **Katy Kaminski** Crisis alpha means gains in dislocations, not in every bad equity month; the term is often misused for any crisis.  #mech/risk_premium
  > crisis alpha is finding our opportunities during periods of market dislocation and distress
  asset: multi · testable: yes · confidence: high
  ^MT042-C14-1
- **Katy Kaminski** Trend benefits crises via three traits: no directional bias (shorted bonds in 2022), liquidity (a 2008-style liquidity event would show it) and adaptability.  #mech/risk_premium
  > trend is a strategy where you know intrinsically it shouldn't have a bias if things are going up or things are going down
  asset: multi · horizon: years · testable: partly · confidence: high
  ^MT042-C14-2
- **Katy Kaminski** Covid and 2022 crises had opposite trends (long bonds/short energy vs long energy/short bonds); trend can capture a crisis only if its markets trend.  #mech/cycle_persistence
  > co was long bonds short energy and 2022 was long energy short bonds
  asset: multi · horizon: years · conditions: if crisis moves are outside traded markets, hard to capture · testable: yes · confidence: high
  ^MT042-C14-3
- **Katy Kaminski** Trend is cyclical and mean-reverting at strategy level: a great year like 2022 is followed by a tougher spell, then recovery.  #mech/cycle_persistence
  > it's cyclical but on a different cycle
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT042-C14-4
- **Katy Kaminski** After Liberation Day, deglobalization, policy divergence and geopolitical conflict create macro change and trends that favour trend following.  #mech/structural_shift _(time-bound view)_
  > the macro impact of changes in policy of diff of divergence across views globally and sort of potential geopolitical conflict and I think that creates macro change and themes and trends which we tend to benefit from
  asset: multi · horizon: years · testable: no - narrative · confidence: medium
  ^MT042-C14-5

### C15
- **Niels Kaastrup-Larsen** The best CTA period in decades (2022) followed a big one-day loss at Thanksgiving 2021, and Liberation Day may play the same role.  #mech/overshoot
  > managers losing a ton in one single day when they came out with this news about the Omicron virus
  asset: multi · horizon: months · testable: no - few observations · confidence: low
  ^MT042-C15-1
- **Katy Kaminski** Crowding concerns about CTAs are overstated since they trade very liquid markets and their AUM is small relative to those markets.  #mech/crowding_positioning
  > the idea that we're going to revert the yen trade and have more power than sort of the PM of Japan, I think, is is hard
  indicator: CTA AUM vs market liquidity · asset: fx · testable: partly - AUM and volumes · confidence: medium
  ^MT042-C15-2

### C16
- **Niels Kaastrup-Larsen** Managed futures fell from about 20% of hedge-fund assets around 2012 to under 10% (about 8% in Q2 2025), so the industry is not crowded.  #mech/crowding_positioning
  > the industry the CTA industry according to this chart uh was about 20% of the total hedge fund universe but now I think we're below 10%
  indicator: managed futures share of hedge fund AUM · asset: multi · horizon: years · testable: yes - Makita chart · confidence: medium
  ^MT042-C16-1
- **Katy Kaminski** Geopolitical risk can be measured with LLM or sentiment indicators from news data, with a UC Irvine paper on geopolitical risk and stock returns.  #mech/research_method
  > there's all sorts of LLM type, you know, sort of sentiment type indicators that one can build and look at sort of measuring using publicly available news data
  indicator: geopolitical risk index from news · asset: multi · testable: yes · confidence: medium
  ^MT042-C16-2
- **Katy Kaminski** Trade negotiations, balance and the dollar will shape macro themes over the next two years.  #mech/policy_reaction _(time-bound view)_
  > trade trade negotiations trade balance the dollar effect is going to have a huge impact on some of the macro themes over the two years
  asset: multi · horizon: years · testable: no - view · confidence: medium
  ^MT042-C16-3
- **Niels Kaastrup-Larsen** Official managed-futures AUM understates total trend-following capital because QIS products and pension funds run trend in-house, so the industry-share chart is an incomplete crowding gauge.  #mech/crowding_positioning _(added by Opus)_
  > I know a lot of strategies like QA strategies and maybe uh individual pension funds are doing trend following uh or something similar. So it doesn't tell you all all you need to know about AUM
  indicator: managed futures share of hedge fund AUM; QIS/in-house trend assets · asset: multi · horizon: years · testable: partly - QIS and in-house assets are not well reported · confidence: medium
  ^MT042-C16-X1

### C17
- **Katy Kaminski** Preview of research: trend following performs better when geopolitical risk is high or rising.  #mech/risk_premium
  > it likes disruption change and difficulty so increased geopolitical risk uh so as a preview to some of the things we found increased geopolitical risk and higher levels of geopolitical risk is generally positive
  indicator: geopolitical risk index · asset: multi · direction: Trend returns up when geopolitical risk rises · testable: yes - regress trend returns on GPR · confidence: medium
  ^MT042-C17-1
- **Katy Kaminski** Trend following tends to do better in periods of higher inflation, the same pattern as with higher geopolitical risk, because it benefits from disruption and change.  #mech/cycle_persistence _(added by Opus)_
  > answer is probably the same as you know higher inflation and things like this
  indicator: inflation level/change · asset: multi · direction: trend-following returns up when inflation is high · horizon: years · testable: yes - trend index returns conditioned on inflation regime · confidence: medium
  ^MT042-C17-X1

