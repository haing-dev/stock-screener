---
source_id: MT211
title: "When Prices Stop Making Sense - Systematic Investor - Ep.378"
date: 2025-12-17
channel: "Top Traders Unplugged"
url: 
words: 10216
claims: 70
added_by_crosscheck: 11
corrections: 0
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Alan Don (guest host, Top Traders Unplugged, sitting in for Niels)", "Mark (systematic/CTA researcher, Chicago)"]
tags: [source, layer0]
---
# When Prices Stop Making Sense - Systematic Investor - Ep.378

**Speakers:** Alan Don (guest host, Top Traders Unplugged, sitting in for Niels); Mark (systematic/CTA researcher, Chicago)

**Summary:** Systematic trend-following discussion (Ep.378, Dec 2025) after the Fed's third 2025 cut: prices are primal but not value, signal vs noise and unmeasurable uncertainty, thin holiday liquidity. Covers bubbles (gold, cocoa, AI credit), where momentum works best (industry/factor > country/stock), and the total portfolio approach vs trend overlays. Conclusion: use price signals but smooth them, treat uncertainty explicitly, and use trend as a diversifier when bonds hedge less.

**Approach:** trend following, momentum, signal vs noise, bubbles, total portfolio approach, Fed policy, diversification

**Cross-check completeness estimate of first read:** 0.88 - first reader caught nearly every mechanism and number (Fed, term premium, momentum breadth, cocoa and gold, uncertainty types, TPA overlay); it missed some host-side points (dissents, household equity exposure, bubbles as the rationale for trend, TPA benchmark) and small model-design remarks.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | intro, SocGen CTA/trend index December performance, holiday liquidity and signals |
| C02 | 3 | Fed meeting: messy signals, avoiding announcement days, SEP dispersion and 2026 projections |
| C03 | 5 | Fed QT to bill purchases, AI productivity read, signal vs noise framework, payroll overstatement |
| C04 | 4 | use prices vs fundamentals, bond value rule of thumb, term premium, safe asset must diversify |
| C05 | 4 | fiscal dominance/financial repression, relative safety and gold, prices are primal |
| C06 | 4 | prices vs value, overbought/oversold anchors, smoothing, narratives lead prices |
| C07 | 4 | year-end liquidity and signal noise, bad-print handling, CME outage, wealth effect start |
| C08 | 5 | wealth, collateral and fragility, central bank gold buying, reflexive wealth effects, leverage, bubble research |
| C09 | 5 | optimism and crashes, hard-to-value assets and bubbles, gold regime change, cocoa evidence, credit concerns |
| C10 | 3 | First Brands fraud, bezzle, credit market extremes, cross-market spillovers, momentum history |
| C11 | 6 | momentum everywhere but stronger in some places, lag one month, types of momentum, why it persists |
| C12 | 5 | hard-to-value assets and persistence, aggregation, earnings vs commodity signals, taxonomy of uncertainty |
| C13 | 3 | examples of uncertainty (outage, thin volume, copper spread, survey data), total portfolio approach intro |
| C14 | 5 | TPA definition, 60/40 weakness, trend overlay on 70/30 for 4% tracking error, TPA vs trend following |
| C15 | 1 | TPA reference portfolio, diversification is primal, wrap-up and sign-off |

## Claims

### C01
- **Mark** Holiday periods thin liquidity, which degrades signal quality, so a systematic trader must decide whether to follow every signal near year end.  #mech/seasonality
  > big impact on liquidity. It has an impact on you know uh what signals you receive and you have to start making some decisions on whether you should follow all signals
  indicator: trading volume around holidays · asset: multi · direction: reduce or ignore signals · horizon: weeks · conditions: year-end holiday period · testable: partly - could test signal hit rate in low-volume weeks · confidence: medium
  ^MT211-C01-1
- **Alan Don** SocGen CTA index was down 2.06% and the SG Trend index down 0.16% year to date in mid-December 2025, with improvement in late-year trends.  #mech/cycle_persistence _(time-bound view)_
  > Sochen CTA now down 2% on the year 2.06% and the sock gen trend uh close to flat down 0.16%
  indicator: SG CTA index, SG Trend index · asset: multi · horizon: months · conditions: as of Dec 9, 2025 · testable: yes - published index series · confidence: high
  ^MT211-C01-2
- **Alan Don** The December 2025 FOMC cut 25 bp to 3.50-3.75% (third cut of the year) with dissents from both the hawkish and dovish sides, so the committee split on direction even though the cut itself was expected.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > there were a number of descents to the um 25 basis point cut on both sides
  indicator: FOMC dissents, fed funds rate · asset: rates · horizon: weeks · conditions: committee dissent on both sides signals divided policy direction · testable: partly - dissent counts are public but the sample is tiny · confidence: high
  ^MT211-C01-X1

### C02
- **Mark** Around FOMC announcements uncertainty is high and prices can reverse sharply, so short-term models may do better avoiding the Fed window.  #mech/policy_reaction
  > right around the Fed announcements is that you you get some uh high uncertainty. When you have high uncertainty, you could have large reversals in price.
  indicator: FOMC announcement dates · asset: multi · direction: avoid or flatten short-term positions around FOMC · horizon: days · conditions: applies to short-horizon models; long-term rates still matter for cost of capital · testable: yes - event-window backtest on FOMC dates · confidence: medium
  ^MT211-C02-1
- **Mark** Wide dispersion in FOMC dot projections (from hikes to six cuts) signals a high-uncertainty Fed in 2026 and so more risk in rates trading.  #mech/policy_reaction _(time-bound view)_
  > we're going to be in a high uncertainty Fed environment for 2026, which is means there going to be more risk if you trade in the interest rate complex
  indicator: FOMC SEP dispersion · asset: rates · direction: higher rates risk · horizon: months · conditions: when the dot spread is wide · testable: partly - dispersion of dots is observable, link to risk untested here · confidence: medium
  ^MT211-C02-2
- **Mark** Despite a third cut, Fed projections show core PCE at 2.6% and growth at 2.3% in 2026, i.e. still-high inflation with stronger growth than before.  #mech/policy_reaction _(time-bound view)_
  > the projected inflation for the PCE for the core is going to be at 2.6 for 2026
  indicator: Fed SEP core PCE and GDP projections · asset: rates · horizon: years · conditions: Dec 2025 SEP · testable: yes - published projections · confidence: high
  ^MT211-C02-3
- **Mark** A divided FOMC shows independence but sends a messy set of signals, so market participants cannot easily read the policy direction, which raises uncertainty around policy events.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > It shows that there's independence on the FOMC, but at the same times that means that the Fed is not speaking with one voice.
  indicator: FOMC dissent and dispersion · asset: rates · direction: higher uncertainty in rates · horizon: months · conditions: when several members dissent and forecasts are widely dispersed · testable: partly - dissent or dot dispersion could proxy for policy uncertainty · confidence: medium
  ^MT211-C02-X1
- **Alan Don** Data gaps and technical distortions in the post-shutdown releases (acknowledged by Powell) make the incoming economic data an additional source of uncertainty for the January meeting.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > even Pal said himself that some of the data that comes through you know there will maybe technical factors that will distort it so that is another source of uncertainty
  indicator: official macro data quality (post-shutdown releases) · asset: multi · horizon: weeks · conditions: when official data are missing or distorted · testable: no - one-off data disruption · confidence: medium
  ^MT211-C02-X2

### C03
- **Alan Don** The Fed's projections of higher growth without lower unemployment imply it is buying the AI productivity story.  #mech/structural_shift _(time-bound view)_
  > they're forecasting higher growth but not translating into improved um unemployment
  indicator: Fed SEP growth and unemployment · asset: multi · horizon: years · testable: no - interpretation of a forecast · confidence: medium
  ^MT211-C03-1
- **Alan Don** The Fed ended balance-sheet runoff and began Treasury bill purchases to keep reserves sufficient after repo-market disruptions, a liquidity easing.  #mech/liquidity_flows _(time-bound view)_
  > we've gone from QT to some form of QE again
  indicator: Fed balance sheet, T-bill purchases, repo stress · asset: rates · direction: supportive for liquidity · horizon: months · testable: partly - balance sheet series available · confidence: medium
  ^MT211-C03-2
- **Mark** A trend signal's quality can be measured as signal strength divided by volatility, a signal-to-noise ratio, which scales how much to trust it.  #mech/research_method
  > we can look at the strength of our signal divided by our our volatility. we could get a signal to noise ratio
  indicator: signal strength / volatility · asset: multi · testable: yes - computable from price series · confidence: medium
  ^MT211-C03-3
- **Mark** Risk has a measurable part (volatility) and an unmeasurable part (uncertainty, e.g. Fed dissents or policy changes with tiny samples) that is hard to turn into a model input.  #mech/risk_management
  > it's not just the volatility which is measurable but it's also what is not measurable which is the uncertainty
  asset: multi · conditions: small samples make uncertainty hard to quantify · testable: no - uncertainty by definition not directly measured · confidence: medium
  ^MT211-C03-4
- **Mark** Powell's remark that payroll growth may be overstated by about 60,000 a month implies the real job market is flat or negative, so labor data carries observational uncertainty.  #mech/policy_reaction _(time-bound view)_
  > if you said that, you know, job creation was overstated by 60,000 a month, then well, we've gone from a positive job market to something that uh uh is uh negative
  indicator: nonfarm payrolls · asset: multi · horizon: months · conditions: Dec 2025 · testable: partly - benchmark revisions testable · confidence: medium
  ^MT211-C03-5
- **Alan Don** When Fed messaging is too subtle to model, a systematic investor can ignore the narrative and read the market's own price reaction in the following days instead.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > I guess you can you can ignore all of that and just look at how the markets trade in the day I suppose the days after.
  indicator: post-announcement price reaction · asset: multi · horizon: days · conditions: when policy communication cannot be turned into measurable noise or signal · testable: yes - event-study of post-FOMC drift versus pre-event positioning · confidence: medium
  ^MT211-C03-X1

### C04
- **Mark** When fundamental data is noisy, the central design choice for a systematic model is how much information beyond price to include.  #mech/research_method
  > that becomes the the key balancing act is is that how much other information should you use in models beyond on price
  asset: multi · testable: partly - compare price-only vs price plus macro models · confidence: medium
  ^MT211-C04-1
- **Mark** A rule of thumb values 10-year yields as expected inflation plus real GDP growth (about 2.6 + 2.3 = 4.9) plus any term premium, putting fair value near the high 4s versus the market near 4.1-4.2%.  #mech/policy_reaction _(time-bound view)_
  > they say let's look at uh what real GDP is. Let's look with the expected inflation.
  indicator: 10y yield vs expected inflation + real GDP · asset: rates · direction: bonds look rich versus this anchor · horizon: years · conditions: depends on positive term premium · testable: yes - compute nominal GDP proxy versus yield · confidence: medium
  ^MT211-C04-2
- **Mark** Term premium fell near zero while bonds were a reliable hedge; with high debt that hedge role is less assured, which argues for a higher premium.  #mech/fiscal_debt
  > the term premium was you was knocked down to something close to to to zero because the bonds were such a a good hedge
  indicator: term premium (ACM / Kim-Wright) · asset: rates · direction: term premium up, bond prices down · horizon: years · conditions: when debt is high and bonds stop hedging equities · testable: yes - term premium and stock-bond correlation are observable · confidence: medium
  ^MT211-C04-3
- **Mark** A safe asset is defined by diversification; if bonds no longer diversify equities, investors must find other diversifiers such as trend following.  #mech/risk_management
  > Because a safe asset should be a diversifying asset. If bonds are not a diversifying asset, then what is and what should you do with your portfolio?
  indicator: stock-bond correlation · asset: multi · direction: add non-bond diversifiers (trend following) · horizon: years · conditions: when stock-bond correlation turns positive · testable: yes - rolling correlation and drawdown tests · confidence: high
  ^MT211-C04-4
- **Alan Don** The term premium reflects supply and demand for safe assets: it fell to zero or below when safe assets were scarce and is positive again now that the balance (and fiscal-dominance fears) have changed.  #mech/fiscal_debt _(added by sonnet-xhigh cross-check)_
  > the term premium kind of went to zero if maybe even negative when there was um a shortage of of safe assets
  indicator: term premium · asset: rates · direction: higher term premium when safe-asset supply is large relative to demand · horizon: years · conditions: regimes of safe-asset shortage versus heavy issuance · testable: yes - term premium estimates against Treasury supply and demand measures · confidence: medium
  ^MT211-C04-X1

### C05
- **Mark** Large US deficits can only be resolved outside default by inflation, likely via financial repression that holds rates below inflation.  #mech/fiscal_debt
  > the only way that you could solve those deficit problems outside of a default is that you can inflate your way out of that.
  indicator: debt to GDP, real rates · asset: rates · direction: inflation up, real yields suppressed · horizon: years · testable: partly - real-rate history after high-debt episodes · confidence: medium
  ^MT211-C05-1
- **Mark** If Treasuries are seen as less safe in relative terms, demand shifts to other safe assets like gold, whose supply is constrained, driving large price moves.  #mech/liquidity_flows _(time-bound view)_
  > if relative safety in the US has gone down then the demand for other potentially safe assets should go up
  indicator: gold price, Treasury relative safety · asset: commodities · direction: gold up · horizon: months · conditions: gold supply cannot be created by fiat · testable: partly - hard to measure relative safety · confidence: medium
  ^MT211-C05-2
- **Mark** Mark argues the US Treasury term premium should be higher given deficits and reduced relative safety.  #mech/fiscal_debt _(time-bound view)_
  > I would argue that uh there should be a greater term premium in the US market
  indicator: US term premium · asset: rates · direction: long yields up · horizon: years · testable: partly - model-based premium estimates · confidence: medium
  ^MT211-C05-3
- **Mark** 'Prices are primal': whatever other data says, the price reveals the current supply-demand balance, so price is the anchor for systematic models.  #mech/research_method
  > you always have the price is telling you where there's a some balance between supply and demand
  indicator: price · asset: multi · testable: no - a guiding principle · confidence: high
  ^MT211-C05-4
- **Alan Don** The tail risk in US debt need not be outright default; a fiscal crisis could bring debt swaps or maturity extensions, and the term premium should in theory price these miscellaneous risks.  #mech/fiscal_debt _(added by sonnet-xhigh cross-check)_
  > It mightn't be an outright default but you could have you know if we got into some kind of fiscal crisis down the road you could have debt swaps or maturity extensions all of these kind of things.
  indicator: term premium, debt to GDP · asset: rates · direction: higher term premium and weaker long bonds in a fiscal crisis · horizon: years · conditions: very high debt to GDP · testable: no - tail event with no sample · confidence: low
  ^MT211-C05-X1

### C06
- **Mark** A price shows balance between supply and demand but not true value, so bubble-like prices (gold, silver above $60, individual stocks) can be informative without being fair.  #mech/overshoot
  > that prices are primal, but that's not the same as value
  asset: multi · testable: no - conceptual · confidence: high
  ^MT211-C06-1
- **Mark** A trend follower can add overbought/oversold or value-anchor indicators to guard against prices detached from value.  #mech/overshoot
  > I might also use some other indicators to try to tell me is is that whether something could be overbought or oversold
  indicator: overbought/oversold, value anchors · asset: multi · direction: reduce trend exposure when stretched · testable: yes - add stretch filter to trend backtest · confidence: medium
  ^MT211-C06-2
- **Mark** Smoothing prices (e.g. moving average) extracts a cleaner signal from noisy price processes.  #mech/research_method
  > you wanted to use some kind of smoothing mechanism that could be a moving average at the very simplest form
  indicator: moving averages · asset: multi · testable: yes - standard · confidence: high
  ^MT211-C06-3
- **Mark** A recent FX study using LLM-extracted news narratives found narratives develop first and prices follow with a carryover, so trends can reflect narrative trends as well as fundamentals.  #mech/slow_reaction
  > then prices follow narratives as opposed to lead narratives
  indicator: LLM news narrative measures · asset: fx · direction: price continues in narrative direction · horizon: months · conditions: FX · testable: yes - replicate with news text data · confidence: medium
  ^MT211-C06-4

### C07
- **Mark** Year-end volume decline makes small order changes move prices more, so signals get noisier as liquidity falls.  #mech/seasonality
  > there's more likelihood that a small change in uh in in trading in volume will have a big a bigger impact on price. So your signals are going to get noisier as liquidity declines.
  indicator: trading volume · asset: multi · direction: downweight signals · horizon: weeks · conditions: late December · testable: yes - compare signal accuracy in thin periods · confidence: high
  ^MT211-C07-1
- **Mark** Intraday liquidity and signal quality are U-shaped, highest at the open and close and lowest midday, which affects execution timing.  #mech/liquidity_flows
  > liquidity and and the quality of signals you know intraday is is U-shaped
  indicator: intraday volume profile · asset: multi · direction: trade near open or close · horizon: days · testable: yes - intraday data · confidence: medium
  ^MT211-C07-2
- **Mark** Prices from thin days such as the Friday after Thanksgiving may be ignored or downweighted in models, although month-end volume complicates this.  #mech/research_method
  > normally you might ignore prices that occur on a Friday after Thanksgiving
  indicator: price data filtering · asset: multi · horizon: days · conditions: thin holiday sessions · testable: yes - data cleaning rule · confidence: medium
  ^MT211-C07-3
- **Mark** After the 11-hour CME outage, a modeler must decide whether to trust post-outage prices, smooth, or drop signals; there is no rule and each choice is a model judgement.  #mech/research_method _(time-bound view)_
  > Do you try to smooth do you drop out signals?
  indicator: CME outage price gap · asset: multi · horizon: days · conditions: Nov 2025 CME outage at month end · testable: no - a one-off judgement · confidence: low
  ^MT211-C07-4
- **Mark** Every systematic model has a 'personality' because the modeler must make many judgement calls on what data and prices to include or exclude, so two sensible builders produce different signals from the same markets.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > when you start looking at all the different choices you make, the modeler has to start making choices and decisions of what to include or exclude in a model
  asset: multi · testable: partly - sensitivity of results to data-handling choices can be tested · confidence: high
  ^MT211-C07-X1
- **Mark** National holidays close some markets while others stay open, so cross-market price series become asynchronous and the modeler must choose how to treat the missing or stale prices.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > You have the Thanksgiving holiday in the United States. So, you have that Thursday off. Okay. You know, other markets are still open.
  indicator: holiday calendar, stale prices · asset: multi · horizon: days · conditions: holidays that close one country's market only · testable: yes - compare signal and return outcomes under different holiday-price treatments · confidence: high
  ^MT211-C07-X2

### C08
- **Mark** Rising asset prices create collateral that is levered up, making the economy more fragile in bubbles.  #mech/crowding_positioning
  > if you use that wealth that's been created as collateral, well then what happens is that you could actually increase more leverage
  indicator: leverage, collateral values · asset: multi · direction: fragility up · horizon: months · conditions: bubble phases · testable: partly - leverage data available · confidence: medium
  ^MT211-C08-1
- **Mark** Central banks have been strong net buyers of gold, adding demand pressure beyond price gains; some retail demand outside the US also.  #mech/liquidity_flows _(time-bound view)_
  > the central banks uh beyond their increases in marktomarket is that they've been just been strong buyers of gold
  indicator: central bank gold purchases (WGC) · asset: commodities · direction: gold up · horizon: years · testable: yes - WGC data · confidence: medium
  ^MT211-C08-2
- **Alan Don** Rising equity markets lower volatility and margin requirements, letting leveraged holders add risk, and lower companies' cost of capital: a reflexive loop that reverses in a downturn.  #mech/crowding_positioning
  > very often volatility goes down so so margin requirements ments are lower so people can lever up
  indicator: volatility, margin requirements · asset: equities · direction: leverage up then forced selling on reversal · horizon: months · conditions: US households hold about $40tn of equity · testable: partly - reflexivity hard to isolate · confidence: medium
  ^MT211-C08-3
- **Mark** Leverage is higher overall, especially at large multi-strategy pod hedge funds that can lever due to diversification.  #mech/crowding_positioning _(time-bound view)_
  > we do know that leverage is higher especially for for hedge funds
  indicator: hedge fund leverage · asset: multi · horizon: years · testable: yes - regulatory and fund data · confidence: medium
  ^MT211-C08-4
- **Mark** Harvard Business School research finds bubbles and crashes are closely linked to optimistic analyst fundamentals expectations, which fuel FOMO and raise crash probability.  #mech/behavioral
  > It's closely linked to optimistic analyst expectations.
  indicator: analyst earnings expectations · asset: equities · direction: crash risk up · horizon: months · testable: yes - analyst estimate data · confidence: medium
  ^MT211-C08-5
- **Alan Don** US households hold about $40 trillion of equities and the wealthier cohort drives a K-shaped economy, so the economy has become sensitive to the stock market and a significant downturn would reverse the positive wealth effects and add economic fragility.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > I think US households own about 40 trillion dollars of of US equity so if they if that market has a significant downturn those positive um wealth effects those positive re reflex processes go into reverse.
  indicator: household equity holdings (about $40 trillion) · asset: equities · direction: equity drawdown feeds into weaker consumption · conditions: high household equity ownership and leverage · testable: yes - wealth-effect elasticity of consumption to equity prices · confidence: medium
  ^MT211-C08-X1

### C09
- **Mark** Assets that are harder to value are more bubble-prone because true value is unknowable.  #mech/overshoot
  > when it's harder to value an asset, then it's more likely to have a bubble because we don't know what is the true value
  indicator: valuation uncertainty · asset: multi · testable: partly - requires a valuation uncertainty proxy · confidence: medium
  ^MT211-C09-1
- **Mark** Gold may be in a regime change because central banks are buying, safe-asset supply from Treasuries is falling, and retail abroad is buying on government uncertainty.  #mech/structural_shift _(time-bound view)_
  > Is there a regime change going on with gold? Well, central banks are changing their behavior.
  indicator: gold · asset: commodities · direction: gold up · horizon: years · testable: no - narrative · confidence: medium
  ^MT211-C09-2
- **Mark** The gold rally is not driven by US retail ETF demand or visible speculation, so standard bubble signatures do not apply.  #mech/crowding_positioning _(time-bound view)_
  > retail demand in the US through ETFs is not as strong as what it as it has been in the past
  indicator: gold ETF flows · asset: commodities · horizon: months · testable: yes - ETF flow data · confidence: medium
  ^MT211-C09-3
- **Mark** In cocoa, COT large speculators, volatility and volume all fell while prices rose, contradicting the idea that bubbles show more speculation, volatility and volume.  #mech/crowding_positioning
  > large speculators were actually declining before a lot of the big move in the cocoa price
  indicator: COT large speculator positions, cocoa volatility and volume · asset: commodities · horizon: months · conditions: cocoa 2024-25 rally · testable: yes - COT data · confidence: high
  ^MT211-C09-4
- **Alan Don** Heavy debt issuance for AI data centers combined with rising asset values is a bubble warning, per Howard Marks's note.  #mech/overshoot _(time-bound view)_
  > there are things going on in the debt market that should give investors concern
  indicator: AI-related debt issuance · asset: credit · horizon: months · conditions: late-cycle · testable: partly - issuance data · confidence: medium
  ^MT211-C09-5

### C10
- **Mark** Galbraith's 'bezzle': at market extremes fraud and embezzlement surface (e.g. First Brands financing), a sign of credit froth.  #mech/overshoot _(time-bound view)_
  > when you have very frothy markets or when you have market extremes you have something called the the bezel
  indicator: credit frauds, receivables financing · asset: credit · direction: credit stress up · horizon: months · conditions: market extremes · testable: partly - anecdotal · confidence: medium
  ^MT211-C10-1
- **Mark** Spreads are very tight but issuers and investors are beginning to demand premia for uncertain AI data center debt, which should be equity financed.  #mech/overshoot _(time-bound view)_
  > the credit markets are uh at a market extreme and we're starting to see cracks in the behavior
  indicator: credit spreads, AI financing premia · asset: credit · direction: spreads wider · horizon: months · conditions: tight spreads · testable: yes - spread data · confidence: medium
  ^MT211-C10-2
- **Mark** Even futures-only traders should watch credit because cracks change risk aversion and shift capital into Treasuries, which feeds into price models.  #mech/liquidity_flows
  > Markets are a complex system and so there's interactions across markets and assets
  indicator: credit stress · asset: multi · direction: long Treasuries, risk off · horizon: weeks · testable: partly - cross-asset spillover tests · confidence: medium
  ^MT211-C10-3
- **Alan Don** Bubbles and boom-bust cycles are recurring features of markets and move partly independently of fundamentals, which is the usual justification for momentum and trend-following strategies that follow price rather than fundamentals.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > The fact that these are recurring um patterns, recurring features of the financial market landscape, that they are moves that are somewhat um you know, unlin from fundamentals.
  indicator: price trend · asset: multi · direction: long trend in booming markets, short in busts · horizon: months · conditions: recurring bubble and bust episodes · testable: yes - trend returns conditional on bubble and bust episodes · confidence: medium
  ^MT211-C10-X1

### C11
- **Mark** Momentum works across markets, countries, industries, factors and stocks and across sub-periods, with occasional failures.  #mech/cycle_persistence
  > momentum is everywhere. It works you know across all time periods.
  indicator: momentum · asset: multi · direction: long winners, short losers · horizon: months · testable: yes - extensive literature · confidence: high
  ^MT211-C11-1
- **Mark** Industry and factor momentum are stronger than country, beta or individual stock momentum, so tilting momentum bets there does better.  #mech/cycle_persistence
  > for industries there's much stronger momentum effect than what you'd find in in individual stocks
  indicator: industry and factor momentum · asset: equities · direction: overweight industry/factor momentum · horizon: months · testable: yes - factor data · confidence: medium
  ^MT211-C11-2
- **Mark** Stock momentum shows intermediate-term persistence but short-term reversal, so strategies skip the most recent month.  #mech/overshoot
  > a lot of times for momentum strategies you lag one month because you you get sort of reversals in the very short run
  indicator: 12-1 month momentum · asset: equities · direction: skip last month · horizon: months · testable: yes - standard · confidence: high
  ^MT211-C11-3
- **Mark** Momentum exists in news, fundamentals and earnings surprises, imperfectly correlated with price momentum, allowing diversified momentum sources.  #mech/slow_reaction
  > there's momentum in news, there's momentum in fundamentals, there's momentum in in uh surprise effects in earnings
  indicator: news, fundamentals, earnings momentum · asset: equities · direction: combine momentum types · horizon: months · testable: yes · confidence: medium
  ^MT211-C11-4
- **Mark** Momentum persists because people take time to digest and attend to information, so prices respond over an extended period.  #mech/slow_reaction
  > people take time to digest information
  asset: multi · horizon: months · testable: no - explanation · confidence: medium
  ^MT211-C11-5
- **Mark** Assets that are harder to value are more likely to show momentum, since it takes time to learn true value.  #mech/slow_reaction
  > if an asset is higher to uh harder to value yes that there will be more likely to be persistence or momentum
  indicator: valuation difficulty · asset: multi · direction: stronger momentum in hard-to-value assets · horizon: months · testable: partly - needs proxy · confidence: medium
  ^MT211-C11-6

### C12
- **Mark** Assets with little analyst coverage (e.g. small caps) have more persistence in price behavior.  #mech/slow_reaction
  > or there's less analyst attention there's more likely to be persistence
  indicator: analyst coverage · asset: equities · direction: stronger momentum in low-coverage stocks · horizon: months · testable: yes - coverage data · confidence: medium
  ^MT211-C12-1
- **Mark** Aggregating stocks into industries reduces noise, so trends are cleaner at industry level than individual stocks.  #mech/research_method
  > But if I look at the industry there may be actually trends.
  indicator: industry aggregation · asset: equities · horizon: months · testable: yes · confidence: medium
  ^MT211-C12-2
- **Mark** Post-earnings drift and punctuated quarterly information mean equity momentum needs earnings-aware handling unlike commodity trend following.  #mech/slow_reaction
  > we know that there's persistence in uh or uh you know after earnings announcements
  indicator: post-earnings announcement drift · asset: equities · direction: follow earnings surprise direction · horizon: months · testable: yes · confidence: high
  ^MT211-C12-3
- **Mark** Commodities have seasonality and lack earnings-style punctuation, so signals should differ from equities.  #mech/seasonality
  > there are certain seasonality uh you know associated with uh with certain markets
  indicator: commodity seasonality · asset: commodities · horizon: months · testable: yes · confidence: medium
  ^MT211-C12-4
- **Mark** A stochastic optimization text lists ten uncertainty types (observational, prognostic, experimental, transitional, inferential, model, exogenous, control implementation, algorithmic, goal), each of which affects signals.  #mech/research_method
  > there's observational uncertainty, there's there's prognostic uh or forecasting uncertainty
  asset: multi · testable: no - taxonomy · confidence: medium
  ^MT211-C12-5

### C13
- **Mark** Tariff-driven divergence between COMEX and LME copper creates ambiguity about which price to use to generate trend signals.  #mech/structural_shift _(time-bound view)_
  > if you looked at uh copper prices in New York versus Lond London copper prices there's a big divergence between the two prices
  indicator: COMEX vs LME copper spread · asset: commodities · horizon: months · conditions: tariff regime · testable: yes - compare signals on the two prices · confidence: medium
  ^MT211-C13-1
- **Mark** Falling survey response rates and partisan splits in consumer surveys add measurement uncertainty to macro data.  #mech/research_method
  > there's measurement problems with a lot of the fundamental data because people don't respond to the surveys
  indicator: BLS surveys, consumer confidence · asset: multi · testable: partly · confidence: medium
  ^MT211-C13-2
- **Mark** Market-based 5y5y inflation looks anchored near 2.5% while consumer surveys show unanchored higher inflation, which matters for consumer behavior.  #mech/behavioral _(time-bound view)_
  > if you look at expectations in fiveyear 5year forward prices it looks like they're fairly well anchored at around 2 and a.5%
  indicator: 5y5y inflation breakeven, consumer inflation surveys · asset: rates · horizon: years · testable: yes - series available · confidence: medium
  ^MT211-C13-3

### C14
- **Mark** Total portfolio approach (e.g. CalPERS) replaces fixed strategic weights with flexible adjustment toward overall return or volatility goals.  #mech/risk_management
  > you allow for more of adjustments in the assets you hold to reach some overall goal of you know the return or controlled volatility
  asset: multi · horizon: years · testable: partly - definition vague · confidence: medium
  ^MT211-C14-1
- **Mark** The 60/40 portfolio may not provide enough diversification, so investors seek alternatives.  #mech/risk_management
  > the 6040 stock bond portfolio, it it may not provide the diversification you need
  indicator: 60/40 portfolio · asset: multi · horizon: years · conditions: positive stock-bond correlation · testable: yes · confidence: medium
  ^MT211-C14-2
- **Alan Don** A 30% overlay of the SG Trend index on a 70/30 stock-bond portfolio yields about 4% tracking error, matching the CalPERS TPA target, a simple way to make a static portfolio adaptive.  #mech/risk_management
  > if you added a I think it was a 30% overlay to the sock genen trend index you achieve um a 4% tracking error
  indicator: SG Trend index overlay on 70/30 · asset: multi · direction: add trend overlay · horizon: years · testable: yes - computable · confidence: medium
  ^MT211-C14-3
- **Alan Don** Trend following already allocates dynamically across and within asset complexes, covering much of what TPA wants.  #mech/risk_management
  > Obviously trend following achieves a lot of what TPA is trying to do already.
  indicator: trend following · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT211-C14-4
- **Mark** Portfolio weights should respond to changes in volatility and correlation rather than staying fixed.  #mech/risk_management
  > those weights you know uh should respond to changes in uh in uh volatility and and correlation coariance
  indicator: volatility, covariance · asset: multi · direction: dynamic weights · horizon: months · testable: yes · confidence: medium
  ^MT211-C14-5

### C15
- **Mark** Diversification is the foundation of portfolio construction; start from a strategic allocation and adapt with market conditions.  #mech/risk_management
  > diversification is primal to portfolio construction
  asset: multi · horizon: years · testable: no - principle · confidence: high
  ^MT211-C15-1
- **Alan Don** A total portfolio approach still needs a reference benchmark (70/30 at CalPERS), and the origin of that benchmark is arbitrary (likely consultant-driven); Mark replies the strategic starting allocation and TPA process need better definition before the adaptive part can be judged.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > It does leave open the question where does that come from? Why is that the the appropriate benchmark?
  indicator: reference portfolio / tracking error to benchmark · asset: multi · horizon: years · conditions: TPA with a fixed reference portfolio and tracking-error budget · testable: no - governance question · confidence: medium
  ^MT211-C15-X1

