---
source_id: MT099
title: "Major Market Moves for Trend Followers - Systematic Investor 308"
date: 2024-08-16
channel: "Top Traders Unplugged"
url: 
words: 11103
claims: 46
added_by_crosscheck: 6
corrections: 2
crosscheck: "opus cross-check"
speakers: ["Niels Kaastrup-Larsen (host)", "Nick Baltas (co-host, quant/trend-following practitioner; caption spells 'Nick Bolas')"]
tags: [source, layer0]
---
# Major Market Moves for Trend Followers - Systematic Investor 308

**Speakers:** Niels Kaastrup-Larsen (host); Nick Baltas (co-host, quant/trend-following practitioner; caption spells 'Nick Bolas')

**Summary:** Aug 2024 Systematic Investor: live debrief of the early-August yen-carry unwind and volatility spike (VIX 16 to 65, Nikkei -12%) for trend followers. Trend index lost about 6% in the month, within normal bounds; discusses speed, risk allocation across asset classes, dynamic sizing, 0DTE options, value-at-risk contagion and correlation externalities. Main conclusion: reversal after a spike is an expected cost of trend following; design choices (speed, balanced vs unconstrained risk, equity caps) explain manager dispersion.

**Approach:** trend following, CTA performance, carry trade unwind, volatility spike, risk allocation, signal speed, value at risk, dispersion between managers

**Cross-check completeness estimate of first read:** 0.87 - first reader was thorough on design choices, speeds and the August 2024 event; missed the pre-shock low-correlation setup, look-back vs shock length, bonds as historical driver, intraday momentum, risk-manager framing and the VaR contagion nuance.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro boilerplate and small talk (Olympics) |
| C02 | 3 | performance snapshot of indices (Aug 2024); trigger of event: weak US jobs, BOJ hike, Nikkei -12%, BOJ put |
| C03 | 2 | structuring the discussion; Monday emotions vs v-shape, 2024 equity strength, matching design choices to investor objectives |
| C04 | 3 | VIX 16 to 65, carry unwind, dispersion trades and vol selling losses, skew repricing; Crisis alpha in short supply |
| C05 | 3 | trend followers underperformed in sharp reversion; no alarm; Monday was a normal day, rules-based |
| C06 | 3 | exposure shifts over summer by sector: bonds flipped long, FX, commodities reversion, equities |
| C07 | 3 | what drove returns, bonds low-risk then directional; diversification and number of markets; non-traditional commodities |
| C08 | 2 | risk allocation in rates down to 10%; vol scaling vs asset-class balance |
| C09 | 2 | balanced asset-class risk vs unconstrained trend; speed short-term vs trend |
| C10 | 4 | short-term manager vs short-term trend follower; half-life of SG CTA Trend; true vs false positive Monday |
| C11 | 2 | asymmetric look-backs, solvency in drawdowns, impure trend with reversion |
| C12 | 3 | speed matters for rates and commodities; Volmageddon 356-day streak; March 2023 comparison |
| C13 | 3 | equity vs duration shock dispersion; defending 60/40; replicators vs benchmark; 0DTE options |
| C14 | 2 | 0DTE hedging, long vol did well, risk parity attribution skepticism; risk management and VaR question |
| C15 | 3 | VaR vs expected shortfall; parametric vs Monte Carlo; correlation dynamics and externalities |
| C16 | 2 | funding liquidity, overplayed systematic-selling narrative, headlines, outro |

## Claims

### C02
- **Niels Kaastrup-Larsen** A short-horizon trend barometer stood at 52 (fairly high) in the August 2024 reversal because short time frames adapt quickly, while longer trend indices were down.  #mech/slow_reaction _(time-bound view)_
  > my own Trend barometer uh probably to some people surprise is uh is is is fairly High 52 uh but people have to remember that it uses shorter term uh time frames
  indicator: Niels' trend barometer · asset: multi · horizon: weeks · conditions: short time frames benefited in range/fast reversal · testable: yes: barometer vs speed · confidence: medium
  ^MT099-C02-1
- **Niels Kaastrup-Larsen** As of 14 Aug 2024 CTA indices were down 3.6% (BTOP50), 4.45% (SG CTA), 5.98% (SG Trend) and 0.72% (SG Short-Term Traders) for the month, roughly flat for the year, while MSCI World was +8.2% and S&P 500 +12.4% YTD.  #mech/new _(time-bound view)_
  > beta 50 is down 3.6% for the month uh still up 1.55 for the year stock gen c Index is down 4.45% for the month
  indicator: BTOP50, SG CTA, SG Trend, SG Short-Term Traders, MSCI World, S&P 500 · asset: multi · horizon: months · testable: yes: public indices · confidence: high
  ^MT099-C02-2
- **Niels Kaastrup-Larsen** The BOJ stated publicly it would not hike if it upsets markets, effectively a BOJ put that enabled the rebound, after a small BOJ hike and weak US jobs triggered the biggest Nikkei daily loss since 1987.  #mech/policy_reaction _(time-bound view)_
  > the central bank is not going to change rates if it upsets the market so this is if anything
  indicator: BOJ policy, Nikkei, yen · asset: fx · horizon: days · conditions: August 2024 · testable: partly: central bank put events · confidence: medium
  ^MT099-C02-3

### C03
- **Nick Baltas** 2024 equities to end-July were in the top decile of any year since 1928, so the August drawdown was a reversal of an exceptional run, and trend indices had been outperforming until just before.  #mech/cycle_persistence _(time-bound view)_
  > 2024 as an equity market up until the end of July is almost at the top deile of any year since 1928
  indicator: US equity annual return rank since 1928 · asset: equities · horizon: months · testable: yes · confidence: medium
  ^MT099-C03-1
- **Nick Baltas** Investors flip between wanting faster or slower systems within days as the V-shaped dynamics unfold, so system speed should be tied to investor objectives rather than recent price action.  #mech/behavioral _(time-bound view)_
  > I was kind of having conversation with clients that they would be more like oh we should have like a faster system and then two days later they're like actually it's okay
  indicator: signal speed · asset: multi · horizon: days · conditions: V-shaped reversals whipsaw fast systems · testable: partly · confidence: medium
  ^MT099-C03-2

### C04
- **Nick Baltas** VIX spiked from 16 to 65 intraday on 5 Aug 2024 and fell back to 24 within a week, a spike-and-revert profile unfavorable to trend following.  #mech/overshoot _(time-bound view)_
  > we saw vix from 16% end of July spiking to 65% int on Monday which is a level we haven't seen since covid and it's now down to 24
  indicator: VIX · asset: equities · horizon: days · testable: yes: VIX history · confidence: high
  ^MT099-C04-1
- **Nick Baltas** The BOJ hike plus Fed cut expectations made dollar/yen less attractive and unwound the FX carry trade, causing carry losses.  #mech/crowding_positioning _(time-bound view)_
  > the famous FX Cur start unwinding so some carry losses were incurred by those rotations
  indicator: USD/JPY carry trade · asset: fx · direction: short JPY unwound · horizon: weeks · testable: partly: carry unwind episodes · confidence: medium
  ^MT099-C04-2
- **Nick Baltas** Equity dispersion trades and vol-selling lost money as correlations spiked; S&P skew moved from historic lows to its most attractive level in years, offering re-entry opportunities.  #mech/crowding_positioning _(time-bound view)_
  > dispersion trades lost money some volatility selling trades did lose money the skew in S&P over know um got repriced
  indicator: implied correlation, S&P skew, dispersion · asset: equities · horizon: weeks · conditions: after concentration in mega-cap AI/tech · testable: partly · confidence: medium
  ^MT099-C04-3
- **Nick Baltas** Just before the August 2024 shock US equity correlations were at record lows because returns were concentrated in a few mega-cap AI/tech names; such a low-correlation, high-concentration setup left dispersion and short-correlation trades exposed to a sudden correlation spike.  #mech/crowding_positioning _(added by opus cross-check, time-bound view)_
  > we're talking about the least correlated environment in the US market in equities which was the consequence of high level of concentration
  indicator: US equity implied/realized correlation; index concentration · asset: equities · direction: correlation up sharply from record lows; dispersion trades lose · horizon: weeks · conditions: high index concentration, crowded dispersion trades · testable: yes - implied correlation index levels before shocks · confidence: medium
  ^MT099-C04-X1

### C05
- **Nick Baltas** Trend followers are hurt by sharp mean reversion after a spike (as in March 2023, Feb 2018 VIX spike, Aug 2024); this cost is part of the exposure and not a sign the strategy is broken.  #mech/slow_reaction _(time-bound view)_
  > a massive reversion following a spike this was not the environment during March 2023
  indicator: trend-following drawdowns after spikes · asset: multi · horizon: weeks · conditions: sharp reversals · testable: yes: trend returns after vol spikes · confidence: high
  ^MT099-C05-1
- **Niels Kaastrup-Larsen** Trend followers operate by rules and treat a crash day as an ordinary day, unlike discretionary or other strategies that see frantic activity; trend gains of one early-year week exceed the loss of the August week.  #mech/risk_management _(time-bound view)_
  > Monday was a day like any other day there was nothing unusual from a trend falling perspective
  asset: multi · horizon: days · testable: no · confidence: high
  ^MT099-C05-2
- **Niels Kaastrup-Larsen** After the extreme one-day event of Thanksgiving 2020 trend strategies recovered quickly, showing one-day shocks need not damage trend returns.  #mech/cycle_persistence
  > the strategies came roaring back uh actually almost beginning on that day
  indicator: trend index after one-day shocks · asset: multi · horizon: weeks · testable: yes: event study · confidence: low
  **Correction (cross-check):** Wrong year: the caption says 'Thanksgiving 20121', i.e. late November 2021 (the Omicron Black Friday sell-off), not Thanksgiving 2020. → After the extreme one-day event around Thanksgiving 2021 trend strategies recovered quickly, showing one-day shocks need not damage trend returns.
  ^MT099-C05-3

### C06
- **Nick Baltas** Trend portfolios flipped from balanced to long across bond markets and tenors between June and early August 2024 after long range-bound markets.  #mech/slow_reaction _(time-bound view)_
  > the vast majority of markets across uh regions and Tenors are long so we long Bor Futures
  indicator: bond futures net trend position · asset: rates · direction: long bonds · horizon: months · testable: yes: CTA positioning · confidence: medium
  ^MT099-C06-1
- **Nick Baltas** Commodities rallied early 2024 then reversed sharply in July (BCOM -4.5%, GSCI -4%), flipping energy positions, while precious metals longs held.  #mech/slow_reaction _(time-bound view)_
  > July was a massive reversion I think bom was down by 4 and a half% GCI was down by 4%
  indicator: BCOM, GSCI · asset: commodities · horizon: months · conditions: July 2024 · testable: yes · confidence: medium
  ^MT099-C06-2
- **Nick Baltas** In 2024 YTD trend returns came from three components: the equity rally, JPY weakening and rising commodity prices, with an uninteresting bond market.  #mech/slow_reaction _(time-bound view)_
  > what has been driving returns here to date the equity rally the weakening of JPY and maybe some Rising commodity
  indicator: equities, JPY, commodities, bonds · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT099-C06-3

### C07
- **Nick Baltas** Under dynamic risk allocation, bonds received less and less risk in 2024 because they were not trending, then regained direction in August.  #mech/risk_management _(time-bound view)_
  > bonds started representing lower and lower and lower risk over the year just because there was no
  indicator: bond trendiness / risk allocation · asset: rates · horizon: months · conditions: dynamic allocation · testable: yes · confidence: medium
  ^MT099-C07-1
- **Niels Kaastrup-Larsen** Diversified portfolios were cushioned by grain downtrends and non-traditional commodity trends during July/August, which headlines focused on equities and yen missed.  #mech/risk_management _(time-bound view)_
  > the downtrends in some of the Commodities like uh grains um actually um got a
  indicator: grains and alternative commodities · asset: commodities · horizon: weeks · conditions: diversified portfolios · testable: yes · confidence: medium
  **Correction (cross-check):** Mixes speakers: Niels makes the grain-downtrend point; the observation that non-traditional, non-benchmark commodities gained almost every day in August is Nick Baltas's. → Niels: strengthening grain downtrends cushioned diversified trend portfolios in July; Nick: alternative non-benchmark commodities added performance almost daily in August 2024, showing the value of diversification insulated from macro moves.
  ^MT099-C07-2
- **Niels Kaastrup-Larsen** Return dispersion between managers depends on the number of markets traded: managers with few markets are hit and miss on Nikkei/yen exposure.  #mech/research_method
  > return dispersion we're going to be seeing between managers certainly also relates to uh the number of markets you trade
  indicator: number of markets traded · asset: multi · testable: yes · confidence: medium
  ^MT099-C07-3
- **Niels Kaastrup-Larsen** A few-day shock is too short relative to medium/long trend look-back windows to flip equity or yen positions; it mainly causes deleveraging and weaker signal strength while most positions continue, so trend portfolios change little after brief crashes.  #mech/risk_management _(added by opus cross-check, time-bound view)_
  > I don't think it's changed Direction frankly from because the move is relatively short in time only for only for Windows exactly
  indicator: trend signal look-back length vs shock duration · asset: multi · direction: long equities reduced, not reversed · horizon: days · conditions: short sharp shock followed by rebound · testable: yes - simulate signal changes through short shocks · confidence: medium
  ^MT099-C07-X1

### C08
- **Nick Baltas** With dynamic vol scaling, risk allocation fell to about 10% in rates (from 25% across equities, rates, FX, commodities) because rates did not trend while equities and commodities trended.  #mech/risk_management _(time-bound view)_
  > the risk allocation in rates was basically at the minimum we have seen for some time
  indicator: risk share by asset class · asset: multi · horizon: months · conditions: dynamic risk allocation · testable: yes · confidence: high
  ^MT099-C08-1
- **Nick Baltas** Dynamic sizing has two layers: vol scaling per asset, and whether to force equal risk across asset classes (e.g. 25% each) or let risk flow to the trending class; the latter caused most dispersion between managers.  #mech/risk_management
  > the second point and that's the one I have more comments on at least for the recent period is whether even after doing inverse volatility scaling
  indicator: asset-class risk budgeting · asset: multi · testable: yes: simulate fixed vs dynamic class budget · confidence: high
  ^MT099-C08-2
- **Nick Baltas** Bond futures were historically the main driver of trend-following returns, but after 2022 rates stopped trending and contributed little, which changes how a trend book's returns are composed.  #mech/structural_shift _(added by opus cross-check, time-bound view)_
  > historically that was the Big Driver of performance and and and over the last like know a year or [L280] two um it has not been
  indicator: trend P&L attribution by asset class · asset: rates · horizon: years · conditions: range-bound rates after 2022 · testable: yes - sector attribution of SG Trend / trend replication · confidence: medium
  ^MT099-C08-X1

### C09
- **Nick Baltas** A balanced asset-class risk allocation would have lost less in August (equities caused 60% of the loss) but would have captured less of the equity trend before; it is a trade-off between forced diversification and conviction in signals.  #mech/risk_management _(time-bound view)_
  > if you end up having equities contributing 60% of the loss by design a more balanced allocation between the forest classes would have F better
  indicator: asset-class allocation · asset: multi · horizon: months · conditions: equity-led drawdown · testable: yes · confidence: medium
  ^MT099-C09-1
- **Niels Kaastrup-Larsen** The host believes short-term trend following works less well than medium to long-term, and index data show SG Trend usually beats the short-term traders index.  #mech/slow_reaction
  > I don't believe that short-term Trend following works as well as um medium to long-term Trend following
  indicator: SG Short-Term Traders Index vs SG Trend · asset: multi · direction: medium/long-term trend preferred · horizon: years · testable: yes: compare speeds over time · confidence: medium
  ^MT099-C09-2

### C10
- **Niels Kaastrup-Larsen** A short-term manager exits by time-based or vol-based rules, not by trend change, so short-term managers are a different methodology from short-term trend followers.  #mech/research_method
  > short-term manager will not get out because the trend changes they'll get out by using a Time based stop
  indicator: time-based stops · asset: multi · horizon: days · testable: partly · confidence: medium
  ^MT099-C10-1
- **Nick Baltas** The SG CTA Trend index behaves like an exponentially weighted signal with about a 3-month half-life; Quantica showed a roughly 66-day half-life signal correlates highly with the index over 10-15 years.  #mech/research_method
  > around a 30mon half lifee on an exponentially weighted moving average basis
  indicator: EWMA trend signal half-life (about 3 months) · asset: multi · horizon: months · testable: yes: replicate the index with EWMA · confidence: medium
  ^MT099-C10-2
- **Nick Baltas** Faster systems helped on Monday but lost out in the recovery because they cut exposure, while medium-term signals lost more at first and recaptured part later; the gap between speeds closed by week-end, so signal speed outcomes depend on whether the reversal is a true or false positive.  #mech/slow_reaction _(time-bound view)_
  > A true positive in other words whether Monday was the start of a massive drw down
  indicator: signal speed · asset: multi · horizon: days · conditions: V-shape vs continued decline · testable: yes · confidence: high
  ^MT099-C10-3
- **Niels Kaastrup-Larsen** Look-backs are not necessarily symmetrical for entry and exit: a slow entry (e.g. three months to build) does not imply slow exits, and managers can design faster reaction in a medium-term system.  #mech/research_method
  > you can't assume that look backs are are symmetrical applied
  indicator: entry vs exit speed · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT099-C10-4

### C11
- **Nick Baltas** Assessing strategies should focus on turning points and market rotations and how they preserve capital because one must survive drawdowns to see new highs.  #mech/risk_management
  > remaining solvent in a drawdown is harder than in an NA move
  indicator: drawdown behavior at rotations · asset: multi · testable: partly · confidence: medium
  ^MT099-C11-1
- **Niels Kaastrup-Larsen** Many CTAs are no longer pure trend, which explains performance divergences; Baltas adds mean-reversion and carry components that helped (e.g. quickly going long Japan after losses).  #mech/research_method
  > many managers and there's nothing wrong with that um is not pure Trend anymore
  indicator: trend plus reversion plus carry blends · asset: multi · horizon: weeks · testable: yes: compare pure trend and blends · confidence: medium
  ^MT099-C11-2

### C12
- **Nick Baltas** In August 2024 speed mattered most in commodities and rates (no established trends), where shorter speeds did substantially better; equities, credit and FX showed little speed difference.  #mech/slow_reaction _(time-bound view)_
  > the two asset classes where you saw some differing Behavior specifically around a very shorter term speed and longer term speed
  indicator: speed in rates and commodities · asset: multi · direction: faster speed in non-trending markets · horizon: weeks · conditions: whipsaw markets · testable: yes · confidence: medium
  ^MT099-C12-1
- **Niels Kaastrup-Larsen** The S&P streak without a 2% drawdown before Volmageddon (Feb 2018) was about 356 days versus 351 days before August 2024; long calm streaks precede vol spikes (rule of thumb offered as a half-joke).  #mech/overshoot _(time-bound view)_
  > if the S&P goes for about 340 days without a 2%
  indicator: days since S&P 2% drawdown · asset: equities · direction: reduce long equities after about 340 calm days · horizon: days · conditions: long streak of low volatility · testable: yes: streak vs forward vol · confidence: low
  ^MT099-C12-2
- **Nick Baltas** In Aug 2024 the equity shock differentiated managers (fast/equity-defensive vs medium-term unconstrained), whereas in March 2023 the rates shock hit all trend programs similarly regardless of speed or equity constraints.  #mech/crowding_positioning _(time-bound view)_
  > equities which is typically the growth risk that becomes the differentiation factor between managers
  indicator: equity exposure caps; two-year Treasury sigma move March 2023 · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT099-C12-3

### C13
- **Nick Baltas** Defensive trend designs (no long equities) were around 0% month-to-date, so design choices (equity caps, speed, class balance) should be matched to what the investor needs to defend, e.g. 60/40 equity and rates risk.  #mech/risk_management
  > what are we trying to defend against if it's a 60/40 portfolio
  indicator: equity-defensive vs unconstrained trend · asset: multi · horizon: months · conditions: 60/40 investor · testable: partly · confidence: medium
  ^MT099-C13-1
- **Niels Kaastrup-Larsen** Replicator (trend replication) products outperformed the benchmark leading into July 2024 but the gap vanished in the six weeks after.  #mech/crowding_positioning _(time-bound view)_
  > there was a big dispersion between replicators and The
  indicator: trend replicators vs SG Trend benchmark · asset: multi · horizon: weeks · testable: yes · confidence: low
  ^MT099-C13-2
- **Nick Baltas** Selling 0DTE volatility lost money in the shock but is no different from selling longer tenors; long-vol and long-gamma holders profited and short correlation/dispersion were hit most.  #mech/risk_premium _(time-bound view)_
  > selling volatility in those markets did come at a negative return over the last week
  indicator: 0DTE options, implied correlation · asset: equities · direction: long vol hedges paid · horizon: days · conditions: vol shock · testable: partly · confidence: medium
  ^MT099-C13-3

### C14
- **Nick Baltas** Hedging zero-day options is harder since delta and gamma change quickly intraday, and whether dealers are short or long gamma can amplify or dampen moves; no data show 0DTE drove the event.  #mech/liquidity_flows _(time-bound view)_
  > hedging a zero day option to me appears to be more challenging
  indicator: 0DTE option gamma hedging · asset: equities · horizon: days · conditions: fast intraday moves · testable: partly · confidence: low
  ^MT099-C14-1
- **Nick Baltas** The sell-off was multi-dimensional (carry unwind, correlation spike, liquidity) and blaming risk parity, vol-targeting and CTAs alone is too simple; a postmortem with data on agents is needed.  #mech/liquidity_flows _(time-bound view)_
  > I don't think there was one you know one driver
  asset: multi · horizon: weeks · testable: no · confidence: medium
  ^MT099-C14-2
- **Nick Baltas** On the 5 August 2024 crash day the Nikkei showed strong intraday momentum, so strategies following intraday moves from the open would have profited; the net effect of short-dated option hedging depends on whether dealers are long or short gamma.  #mech/liquidity_flows _(added by opus cross-check, time-bound view)_
  > Niki for instance there was substantial intraday momentum that took place on Monday and had you been exposed to those intraday moves
  indicator: intraday momentum from the open · asset: equities · direction: follow intraday direction from the open · horizon: days · conditions: crash days with dealer short gamma · testable: yes - intraday momentum returns on high-vol days · confidence: medium
  ^MT099-C14-X1
- **Niels Kaastrup-Larsen** Trend followers should see themselves first as risk managers because they control risk taken but not returns the market offers; many managers have moved from stop losses with static sizing to VaR-based portfolio risk models, raising the worry that common VaR use synchronizes selling.  #mech/risk_management _(added by opus cross-check)_
  > first and foremost we're Risk Managers that's the part of the of the equation we have some input on we have no say in terms of what performance we can get from the markets
  indicator: stop-loss/static sizing vs VaR-based sizing · asset: multi · testable: partly - compare drawdown behaviour of static vs VaR-sized trend books · confidence: high
  ^MT099-C14-X2

### C15
- **Nick Baltas** Value at risk is only a threshold; use expected shortfall (conditional VaR) for the loss beyond it, and note that VaR is bounded by historical realizations (parametric or Monte Carlo variants).  #mech/risk_management
  > value at risk is just a point in a return distribution
  indicator: VaR, expected shortfall · asset: multi · testable: yes · confidence: high
  ^MT099-C15-1
- **Nick Baltas** Risk management should foresee correlation spikes and externalities from many investors holding similar portfolios and reacting to the same signals (e.g. FX carry), something VaR cannot capture.  #mech/crowding_positioning
  > I think the way I would look into risk management would be more along the lines of correlation
  indicator: correlation dynamics, crowded positioning · asset: multi · conditions: crowded trades · testable: partly · confidence: medium
  ^MT099-C15-2
- **Niels Kaastrup-Larsen** Correlations rise in a crisis, so back-tested diversification overstates protection.  #mech/risk_management
  > the only thing that goes up in a crisis Nick that's correlations
  indicator: cross-asset correlation · asset: multi · conditions: crisis periods · testable: yes · confidence: high
  ^MT099-C15-3
- **Nick Baltas** Contagion from risk models comes from many investors suffering losses at the same moment and unwinding together, not from the choice of VaR as such; the real question is whether the measure is right and whether people over- or under-react to it.  #mech/crowding_positioning _(added by opus cross-check)_
  > if people follow similar rules this cannot in itself have a I guess a contagion effect except the possibility that losses happen at the same time
  indicator: VaR / expected shortfall usage across investors · asset: multi · horizon: days · conditions: synchronized losses across similar portfolios · testable: partly - flow data around risk-limit breaches · confidence: medium
  ^MT099-C15-X1

### C16
- **Nick Baltas** When investors cannot lever up (funding liquidity constraint), one or two large moves can produce a vicious circle.  #mech/liquidity_flows
  > funding liquidity is is is is one of those catalysts right to to the extent you cannot level up anymore
  indicator: funding liquidity · asset: multi · horizon: days · conditions: constrained leverage · testable: partly · confidence: medium
  ^MT099-C16-1
- **Nick Baltas** Blaming systematic rule-followers (risk parity, vol targeting, CTAs) for each drawdown is overplayed since discretionary managers would also cut losses.  #mech/crowding_positioning _(time-bound view)_
  > I cannot see how differently a discretionary manager would act if they hold the Magnificent 7
  asset: equities · horizon: days · testable: no · confidence: medium
  ^MT099-C16-2

