---
source_id: MT160
title: "The AI Hype within Investing... a Step Too Far- - Systematic Investor 301"
date: 2024-06-25
channel: "Top Traders Unplugged"
url: 
words: 12855
claims: 60
added_by_crosscheck: 26
corrections: 1
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Rob Carver (systematic trader, author)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# The AI Hype within Investing... a Step Too Far- - Systematic Investor 301

**Speakers:** Rob Carver (systematic trader, author); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Systematic Investor 301: Rob Carver and Niels Kaastrup-Larsen on trend following vs tail hedging, VIX carry across the roll, why a systematic trader makes no election adjustments, and why LLMs in trading invite overfitting. Also fees and vol-adjusted fee comparison.

**Approach:** trend following, tail hedging, volatility carry, systematic research method

**Cross-check completeness estimate of first read:** 0.72 - the first reader caught the main arguments (tail hedging, trend vs puts, VIX carry at roll, elections, LLM overfitting, fees) but missed supporting data (index returns, positioning), the fee hurdle and two-tier points, UK fiscal comments and several caveats from Niels.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | sponsor intro and football banter |
| C02 | 2 | Nvidia commoditized chips; trend allocation timing and weak mean reversion |
| C03 | 3 | portfolio P&L, positioning and risk at half target |
| C04 | 2 | trend barometer, CTA index numbers, put-buying listener question |
| C05 | 3 | options trading experience; theory of negatively correlated hedge |
| C06 | 3 | overpriced downside vol; leveraged vs unleveraged tail hedging |
| C07 | 4 | tail hedge cost; trend vs puts; leverage danger |
| C08 | 2 | tail protection vs trend use cases; crisis alpha; roll carry question |
| C09 | 2 | VIX curve carry and election kink; back-adjusted series |
| C10 | 1 | roll carry immaterial; UK election politics |
| C11 | 2 | political risk through equity risk premium; US election |
| C12 | 1 | no system adjustments; three steps of political trading |
| C13 | 1 | market reaction difficulty, Brexit; AI hype intro |
| C14 | 2 | AI hype skepticism and LLM limits |
| C15 | 3 | Renaissance, LLM overfitting, pattern experiment |
| C16 | 1 | overfitting result, AI liability, fees intro |
| C17 | 1 | allocators and incentive fees; costs known returns unknown |
| C18 | 1 | two-tier fee system; vol-adjusted fees |
| C19 | 0 | nothing actionable: wrap-up and sponsor read |

## Claims

### C02
- **Rob Carver** Trend-following returns show weak mean reversion, so adding allocation after a modest drawdown is better timing than adding at a high watermark.  #mech/cycle_persistence
  > There is a sort of weak mean reversion effects in trend-following returns.
  indicator: trend-following strategy equity curve · asset: multi · direction: add trend allocation after a modest drawdown · horizon: months · conditions: weak effect only; market timing is hard · testable: partly - test allocation timing on trend index returns · confidence: medium
  ^MT160-C02-1
- **Rob Carver** Chip businesses (memory, CPUs, smartphone chips) have become commoditized with thin margins, so Nvidia's position is unusual and its highly rated stock reflects unpredictable shifts in leadership.  #mech/structural_shift
  > the thing about chips is is is one of those businesses that that has gradually got more commoditized over time.
  asset: equities · horizon: years · testable: no - qualitative · confidence: low
  **Correction (cross-check):** Mixes two speakers and overstates the margin point: Carver said memory chips are microscopic-margin, while CPU margins are 'better' but still commoditized; the remark on unpredictability of who would be talked about (Nvidia 2-3 years ago) is Niels's, not Carver's. → Carver: memory chips are heavily commoditized with microscopic margins, CPUs and smartphone chips are less so but also commoditized; Nvidia is the surprise. Niels adds that Nvidia's rise shows how unpredictable leadership is.
  ^MT160-C02-2
- **Rob Carver** Carver's own trend allocation went from +16% year-to-date at the late-April high to about +7.8% by late June right after he added allocation at the high, in line with trend indices: an anecdote of buying a trend fund at its high watermark.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > in in late April, I actually reached a high watermark of about um which would have So, the year-to-date figure would have been 16%
  indicator: trend-following P&L YTD · asset: multi · horizon: months · conditions: Single anecdote, in line with CTA indices. · testable: partly - fits the weak mean-reversion claim only anecdotally · confidence: high
  ^MT160-C02-X1

### C03
- **Rob Carver** After trends reversed or weakened, a volatility-targeted trend system automatically runs at about half its long-term risk target because forecasts and positions shrink.  #mech/risk_management _(time-bound view)_
  > Um my risk is running at just under 10% annualized standard deviations. That's about just under half of my kind of long-term target.
  indicator: portfolio volatility vs target · asset: multi · direction: lower exposure after trend weakness · horizon: months · conditions: after drawdown with weak trends · testable: yes - compare realized risk to target · confidence: high
  ^MT160-C03-1
- **Rob Carver** A short VIX position is effectively risk-on (long equities) because VIX falls when investors think equities are getting less risky, so the book is net long equity beta.  #mech/risk_premium _(time-bound view)_
  > my biggest short position actually is VIX. So, that's very much a pro risk-on um position
  indicator: VIX futures position · asset: other · direction: short VIX with long equity indices · horizon: weeks · conditions: when equity trends are up · testable: yes - correlation of positions with equities · confidence: medium
  ^MT160-C03-2
- **Rob Carver** Mid-2024 P&L: FX (yen, euro, Swiss franc), Asian equities (Taiwan, Nikkei) and cocoa were profitable while energies (gas) and metals (gold, platinum) lost money.  #mech/slow_reaction _(time-bound view)_
  > the markets that have done well have been uh interest in the effects, particularly yen
  indicator: sector P&L of a trend portfolio · asset: multi · direction: long FX and Asian equities; losses in energy and metals · horizon: months · testable: yes - sector P&L data · confidence: high
  ^MT160-C03-3
- **Rob Carver** Even a systematic trader who made an allocation timing mistake concludes that timing is too hard to do by judgement and should be left to the model.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > market timing is very difficult, as we as we always say, which is why we leave it to to our models to do that.
  asset: multi · testable: no - methodological stance · confidence: high
  ^MT160-C03-X1
- **Rob Carver** Carver's mid-2024 positioning: long equity indices (MIB, AEX, Nikkei, Nasdaq, S&P), yen and euro, cattle, short bonds and short VIX; cocoa was closed by the trend reversal. This is a positive-beta, pro-equity book with the roll (carry) position pointing the same way.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > I'm long MIB, which is the Italian stock index.
  indicator: positions by market · asset: multi · direction: long equities, FX, cattle; short bonds, VIX · horizon: months · conditions: Derived from trend and carry signals at the time. · testable: no - description of current positions · confidence: high
  ^MT160-C03-X2
- **Niels Kaastrup-Larsen** After a very strong Q1, trend followers had a difficult spring: fixed income was whipsawed by inflation data and hopes of rate cuts (Europe cutting, the Fed holding out), and metals were hard; Europe's equities lagged the US after the European elections.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > I think fixed income has probably been one of the more challenging sectors so far as far as I can tell.
  indicator: fixed income trend P&L; inflation data; Fed path · asset: rates · horizon: months · testable: partly - sector P&L by month is observable · confidence: medium
  ^MT160-C03-X3

### C04
- **Niels Kaastrup-Larsen** A trend barometer at 25 is close to the weakest level normally seen, in line with trend-follower performance in June 2024 (BTOP50 -2.79%, SG CTA -3%, Trend Index -3.57%) while equities rose.  #mech/cycle_persistence _(time-bound view)_
  > My own trend barometer is super weak. So in line with performance numbers it's 25
  indicator: trend barometer · asset: multi · horizon: months · conditions: after strong Q1, difficult Q2 for trend followers; fixed income and metals challenging · testable: yes - index data · confidence: medium
  ^MT160-C04-1
- **Niels Kaastrup-Larsen** Spitznagel's claim: a 2% allocation to far out-of-the-money puts and 98% to the S&P can beat the S&P on geometric return despite a negative expected return on the puts.  #mech/risk_premium
  > a portfolio with a 2% allocation to insurance and a 98% allocation to S&P 500 can theoretically achieve a higher geometric return
  indicator: systematic deep OTM put buying plus monetization · asset: equities · direction: long OTM puts, long S&P · horizon: years · conditions: requires a monetization rule when a crash occurs · testable: yes - backtest the put overlay · confidence: medium
  ^MT160-C04-2
- **Niels Kaastrup-Larsen** In June 2024 the CTA and trend indices were down 2 to 4% (SG CTA about -3%, Trend Index -3.57%, Short Term Traders -1.93%) while year-to-date they were +0.8% to +7.7% against MSCI +11.6% and S&P 500 +15.5%, so trend followers lagged a strong equity rally.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > Beta 50 down 2.79 for the month of June, up 6.41 uh, for the year.
  indicator: BTOP50, SG CTA, Trend Index, Short Term Traders Index, MSCI, S&P 500 YTD · asset: multi · direction: trend lags equities in a narrow rally · horizon: months · testable: yes - public index data · confidence: high
  ^MT160-C04-X1
- **Niels Kaastrup-Larsen** The Spitznagel result requires two pieces: a permanent systematic programme of far out-of-the-money puts (the crash date is unknowable) and an explicit rule to monetise the puts when volatility spikes (listener question relayed by Niels).  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > it would appear to be dependent upon a systematic program of buying far out of the money put options because you don't know in advance when the fast equity crash will occur, and then a monetization strategy
  indicator: far-OTM put programme; monetisation rule · asset: equities · horizon: years · conditions: Without the monetisation rule the payoff is not captured. · testable: yes - backtestable on option data · confidence: medium
  ^MT160-C04-X2

### C05
- **Rob Carver** Buying options is a long-run losing strategy because of the variance (insurance) premium, while selling volatility is dangerous in different ways around events.  #mech/risk_premium
  > buying optionality is is in the long run a long losing strategy because we because of the variance premium because of the insurance premium if you like.
  indicator: variance premium · asset: other · direction: short volatility earns premium; long optionality loses · horizon: years · testable: yes - implied vs realised volatility · confidence: high
  ^MT160-C05-1
- **Rob Carver** Adding a negative-return asset that is negatively correlated with the portfolio raises the Sharpe ratio, which allows more leverage and hence a higher geometric return.  #mech/risk_management
  > it's actually possible to improve the expected um either sharp ratio geometric return both can be improved by adding an asset to your portfolio that has a negative return but is negatively cause a negatively correlated
  indicator: portfolio Sharpe and geometric return · asset: multi · direction: add hedge then lever up · conditions: hedge must be strongly negatively correlated · testable: yes - portfolio optimisation test · confidence: high
  ^MT160-C05-2
- **Rob Carver** Equities are negatively skewed in the tails (1987 -25% day, no +25% day), so strategies with negative skew justify tail protection when leveraged.  #mech/risk_premium
  > there was once a 25% down day in the S&P 500 in 1987. There has never been a 25% up day.
  indicator: S&P 500 return skew · asset: equities · testable: yes - tail distribution · confidence: high
  ^MT160-C05-3
- **Rob Carver** Geometric (compound) return is the right ultimate performance measure, which is why a Sharpe-improving but return-reducing asset can still help once leverage is allowed.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > geometric return is is all the the kind of ultimate I write about it a lot but it's the ultimate performance measure it's what everything comes back to essentially.
  indicator: geometric return · asset: multi · testable: yes - standard result · confidence: high
  ^MT160-C05-X1
- **Rob Carver** Negatively skewed strategies include FX carry (especially emerging-market carry) and long stock holdings, particularly individual stocks, which are prone to sudden sharp losses.  #mech/risk_premium _(added by sonnet-xhigh cross-check)_
  > typical negatively skewed trading strategy. And then that could be something like FX carry, an extreme emerging market FX carry, but it could also just be buying stocks
  indicator: FX carry; single stocks · asset: multi · direction: carry and long-equity returns have sharp left tails · testable: yes - skewness measurable · confidence: high
  ^MT160-C05-X2
- **Rob Carver** For a leveraged book the danger is a gap drawdown too fast to de-risk, which vol-targeting cannot prevent and only an option or similar hard floor does; this is the case for tail protection.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > the drawdown being so fast that I can't de-risk my portfolio, and I'll basically lose all my money.
  asset: equities · horizon: days · conditions: Needs high leverage, e.g. 4x S&P. · testable: partly - gap risk is measurable · confidence: high
  ^MT160-C05-X3

### C06
- **Rob Carver** Out-of-the-money downside puts are systematically overpriced because investors hedge crashes, not rallies, and bid-offer spreads on far-OTM options are wide, so put buying persistently loses money.  #mech/risk_premium
  > people overprice volatility, but they overprice downside volatility even more
  indicator: OTM put implied vol skew · asset: other · direction: short downside vol earns premium · horizon: years · testable: yes - skew versus realized · confidence: high
  ^MT160-C06-1
- **Rob Carver** Unleveraged long-horizon investors (e.g. endowments) face no margin-call risk, so tail protection only reduces their return; it makes sense only for leveraged investors.  #mech/risk_management
  > I'm a bit skeptical as to why you need to buy tail protection, to be honest, because you're you're only going to see the costs and not the benefits
  asset: multi · direction: avoid tail hedge when unleveraged · horizon: years · conditions: investor has long horizon and no leverage · testable: partly - compare returns with and without hedge · confidence: high
  ^MT160-C06-2
- **Rob Carver** A tail-risk fund that buys puts only selectively (when cheap) may leave the investor unprotected at the moment of need, so claims of free insurance are suspect.  #mech/risk_management
  > any tail-risk manager that tells you they're going to give you their insurance policy for free, I'd be a bit skeptical.
  asset: other · testable: partly - fund track records in crisis · confidence: medium
  ^MT160-C06-3

### C07
- **Rob Carver** Paying about 2% per year for tail protection can be reasonable for a leveraged book because protection allows higher leverage; at 30% cost it does not.  #mech/risk_management
  > if it's going to cost you 2% of your portfolio to defend yourself against a you know, a 50% drawdown, that seems to me to me quite reasonable
  indicator: cost of tail hedge · asset: multi · direction: modest tail hedge for leveraged portfolios · horizon: years · conditions: hedge cost small relative to leverage gain · testable: yes - cost-benefit calculation · confidence: medium
  ^MT160-C07-1
- **Niels Kaastrup-Larsen** Option strategies respond to a sudden crisis first while trend following helps in prolonged drawdowns but may not help in the initial phase.  #mech/cycle_persistence
  > option strategies as kind of first responders in a crisis and then trend following was like the second responder
  indicator: options vs trend following crisis response · asset: multi · direction: long puts early; trend later · horizon: months · conditions: trend works in prolonged bear markets, random in fast crashes · testable: yes - compare strategy returns in crisis phases · confidence: medium
  ^MT160-C07-2
- **Rob Carver** Adding 10-30% trend following to a long-only portfolio raises Sharpe and geometric return without extra leverage because it has positive expected return and low correlation to markets.  #mech/risk_premium
  > If you add um trend following to a uh long only portfolio, you can improve your geometric return
  indicator: trend following allocation share in a traditional portfolio · asset: multi · direction: long trend following diversifier · horizon: years · conditions: uncorrelated; no extra leverage · testable: yes - blend backtest · confidence: high
  ^MT160-C07-3
- **Rob Carver** Adding trend following to a levered risk-parity portfolio lowers measured risk, tempting investors to lever up; in a crisis where trend also loses, all assets fall together with large leverage.  #mech/risk_management
  > you add a big slug of trend following say 30%. Um it's quite plausible that your your risk is going to fall
  indicator: portfolio leverage after trend allocation · asset: multi · conditions: when trend does the wrong thing in a crisis · testable: partly - scenario analysis · confidence: high
  ^MT160-C07-4
- **Niels Kaastrup-Larsen** A 50% drawdown happens less than once per decade, so paying 2% a year for protection accumulates to a large drag over ten years and the benefit must be compared with that.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > if you're paying 2% every year for 10 years, you know, it becomes meaningful.
  indicator: annual cost of tail protection · asset: equities · horizon: years · testable: yes - cost-benefit backtest · confidence: medium
  ^MT160-C07-X1

### C08
- **Niels Kaastrup-Larsen** Trend following should be seen as a non-correlated return strategy rather than crisis alpha because each crisis differs and trend response is not guaranteed.  #mech/cycle_persistence
  > it's dangerous to describe trend following as a crisis alpha strategy because no crisis is the same
  asset: multi · testable: partly - crisis-by-crisis trend performance · confidence: high
  ^MT160-C08-1
- **Rob Carver** VIX futures curve in contango (spot 13.4, then 15, 16.5, just under 19 in October) predicts roll-down, which is the carry signal behind a short-VIX position and reflects the gap between expected and realised vol.  #mech/risk_premium _(time-bound view)_
  > the spot VIX is about 13.4.
  indicator: VIX futures term structure carry · asset: other · direction: short VIX futures · horizon: months · conditions: curve upward sloping · testable: yes - carry backtest · confidence: high
  ^MT160-C08-2
- **Rob Carver** Match the tool to the investor: leveraged investors should buy tail protection (guaranteed payoff in a crash), unleveraged investors should buy trend following (positive expected return); trend must not be used to justify extra leverage.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > Leveraged investors should buy tail protection but should be wary of buying trend following if they're going to then use that as an excuse to apply even more leverage.
  asset: multi · testable: partly - argument, not test · confidence: high
  ^MT160-C08-X1

### C09
- **Rob Carver** VIX futures for November and December price below October because of the US election on 5 November, so event risk shows up as a kink in the term structure that changes carry signals when rolling.  #mech/policy_reaction _(time-bound view)_
  > November expiry and actually the December expiry as well, they're actually lower than October.
  indicator: VIX futures curve around US election · asset: other · horizon: weeks · conditions: around event dates · testable: yes - futures prices · confidence: high
  ^MT160-C09-1
- **Rob Carver** Computing trend and momentum on a single back-adjusted continuous price series avoids a forecast change at roll, whereas per-contract calculation changes positions at roll for no real reason.  #mech/research_method
  > I think it's more common to do what I do, which is form a single back adjusted price series of continuous contract
  indicator: back-adjusted continuous contract series · asset: multi · testable: yes - compare signal turnover · confidence: high
  ^MT160-C09-2

### C10
- **Rob Carver** Using carry of the held contract at roll versus a smoothed continuous series is an immaterial approximation; the EMA smoothing of carry absorbs the change, though seasonal markets like crude and gas are more affected.  #mech/research_method
  > Do I really care? Um, implementing what Lewis suggested would make my system a lot more complex
  indicator: roll carry smoothed with EMA · asset: commodities · conditions: stronger seasonality in crude and natural gas · testable: yes - test roll-carry handling · confidence: high
  ^MT160-C10-1
- **Rob Carver** Carver believes UK policy dialogue ignores that government deficit spending can be beneficial, and that a more counter-cyclical (he says pro-cyclical) fiscal stance since 2010 would have left the UK better off.  #mech/fiscal_debt _(added by sonnet-xhigh cross-check)_
  > the fact that that often governments spending more than they earn can be a good thing for example.
  indicator: UK fiscal stance · asset: multi · horizon: years · conditions: Opinion, no evidence given. · testable: no - opinion · confidence: medium
  ^MT160-C10-X1

### C11
- **Rob Carver** Political risk affects markets through the equity risk premium (drastic change raises required returns), and equity is a call option on enterprise value so volatility can even help.  #mech/risk_premium
  > there are essentially um two things that that that kind of can affect markets in terms of political risk. One is the effect it has on, you know, what we would call the the equity risk premium
  indicator: equity risk premium around elections · asset: equities · horizon: weeks · conditions: if change is drastic · testable: partly - event studies · confidence: medium
  ^MT160-C11-1
- **Rob Carver** The 2024 US election was finely balanced, and markets (VIX in October) priced a Trump win as the riskier outcome.  #mech/policy_reaction _(time-bound view)_
  > this thing's on a knife edge, it could go either way.
  indicator: VIX around the US election · asset: equities · direction: VIX higher into election · horizon: months · testable: partly - VIX term structure · confidence: medium
  ^MT160-C11-2
- **Rob Carver** Liz Truss's badly communicated economic plan nearly broke the UK financial system overnight, which is why both UK parties compete to look fiscally prudent: fiscal credibility shocks hit markets hard.  #mech/fiscal_debt _(added by sonnet-xhigh cross-check, time-bound view)_
  > nearly caused the entire UK financial system to disintegrate overnight, which is quite impressive.
  indicator: UK gilt market · asset: rates · direction: gilt yields up, sterling down on fiscal credibility loss · horizon: days · testable: partly - event study · confidence: high
  ^MT160-C11-X1
- **Rob Carver** A foregone election with near-identical platforms (UK 2024) creates little market uncertainty, unlike a close election with very different candidates.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > generally think that the Labour Party and the Conservative There's not going to be that much difference as far as the markets are concerned, at least initially.
  indicator: UK election; implied volatility · asset: equities · horizon: weeks · conditions: Holds when policy convergence is credible. · testable: partly - election event studies · confidence: medium
  ^MT160-C11-X2
- **Rob Carver** In the US system the popular vote does not decide the winner (2016), so even a lead in national polls leaves the presidency near 50/50.  #mech/research_method _(added by sonnet-xhigh cross-check, time-bound view)_
  > the US has a sort of system where you can lose the popular vote or do very badly in the popular vote and still become president
  indicator: polls; Electoral College · asset: equities · horizon: weeks · testable: partly - historical polls vs outcomes · confidence: high
  ^MT160-C11-X3

### C12
- **Rob Carver** A systematic trader should make no system adjustment for elections, referendums or payrolls, because trading political macro requires predicting the outcome, its implications and the market reaction better than everyone else.  #mech/risk_management
  > and the correct answer is nil. Nothing. Nothing.
  asset: multi · testable: partly - compare rule-based vs discretionary overrides · confidence: high
  ^MT160-C12-1
- **Rob Carver** In 2016 markets assumed Trump would be moderated by technocrats; by 2024 nobody believes it, so a Trump win is priced as a higher policy-risk outcome and the October VIX is bid up.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > I think everyone believes that that that, you know, if if the the crazy guy does get in, he's going to do crazy things.
  indicator: VIX October futures · asset: equities · direction: VIX up around the election · horizon: months · conditions: Rob's reading of consensus, not a measured quantity. · testable: partly - VIX term structure observable · confidence: medium
  ^MT160-C12-X1
- **Rob Carver** Staying engaged with political news is a behavioural trap: the more it plays on the mind, the harder it is to resist overriding the system, so the rule is to hold the position of 'do nothing'.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > it's all very well to be interested in this and read the news, but it doesn't mean I should actually do anything
  asset: multi · testable: no - discipline rule · confidence: high
  ^MT160-C12-X2

### C13
- **Rob Carver** Political event trading needs three steps (outcome, implications, market reaction), and the last is hardest because reactions are unpredictable (Brexit moved euro-dollar unexpectedly) and consensus outcomes are already priced.  #mech/behavioral
  > it's no good predicting a foregone conclusion. No one's going to give you any any kind of P&L for that.
  indicator: market reaction to political results · asset: fx · horizon: days · testable: no - qualitative · confidence: high
  ^MT160-C13-1
- **Rob Carver** If you believe you can forecast an election, express that on a betting site rather than by overriding the trading system, keeping the view separate from the systematic book.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > I think if you if you are you do think you can predict political outcomes, then, um, there are websites certainly in the UK where you can bet directly on the political outcome.
  asset: multi · horizon: weeks · conditions: Legality varies by country. · testable: no - practical suggestion · confidence: medium
  ^MT160-C13-X1
- **Niels Kaastrup-Larsen** Niels's caveat to Rob: many Trump-era policies were kept under Biden, so campaign rhetoric overstates the policy change an election produces.  #mech/policy_reaction _(added by sonnet-xhigh cross-check)_
  > actually, for the record, a lot of policies have been maintained actually under Biden, so, uh, you know, you never know what you get, uh, with these elections
  asset: multi · horizon: years · testable: partly - continuity of policy can be measured · confidence: medium
  ^MT160-C13-X2
- **Niels Kaastrup-Larsen** A BCG report puts global asset-management assets at $120 trillion in 2023 yet the industry faces fee compression, rising costs and passive competition.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > They talked about how it reached $120 trillion in 2023.
  indicator: global AUM · asset: multi · direction: fees down · horizon: years · testable: yes - public data · confidence: medium
  ^MT160-C13-X3

### C14
- **Rob Carver** Companies that pivoted to AI (other than Nvidia) have not done well, suggesting AI hype is not translating into returns.  #mech/behavioral _(time-bound view)_
  > if we look at the the share prices of of not of Nvidia, but if you look at other companies that have done a very strong pivot to AI, um they're not doing so well
  indicator: share prices of AI-pivot companies · asset: equities · horizon: months · testable: partly - basket of AI-pivot companies · confidence: low
  ^MT160-C14-1
- **Rob Carver** General large language models give meaningless platitudes on real data analysis tasks, so they are poor tools for evaluating strategy returns.  #mech/research_method
  > this assignment, which for what it's worth, involves analyzing some some returns data from a strategy and comparing it to a couple of benchmarks, is is kind of AI-proof.
  asset: other · testable: partly · confidence: medium
  ^MT160-C14-2
- **Rob Carver** Carver reads rising AI scepticism on social media, alongside weak share prices of non-Nvidia AI pivots, as a sign that the hype is fading.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > I am starting to see a bit of kind of, um, you know, skepticism creeping to my Twitter feed about AI
  indicator: social-media sentiment on AI · asset: equities · horizon: months · conditions: Anecdotal sentiment reading. · testable: partly - sentiment indices exist · confidence: low
  ^MT160-C14-X1

### C15
- **Rob Carver** Using off-the-shelf LLMs to find predictive patterns in financial data carries high overfitting risk and gives no statistical uncertainty or in-sample/out-of-sample discipline, unlike transparent fitting.  #mech/research_method
  > it's very unlikely that that you'll you'll get that kind of rigor using the LLM.
  indicator: LLM-derived signals · asset: multi · conditions: user does not understand the technology · testable: partly - test out-of-sample · confidence: high
  ^MT160-C15-1
- **Rob Carver** Non-linear patterns in financial data may exist that classical statistics miss (Renaissance hires AI specialists), but that is very different from applying generic LLM tools.  #mech/structural_shift
  > Renaissance Technologies. The I mean, you know, nobody knows what they do, but it's probably that cuz they aren't doing what
  indicator: non-linear pattern detection · asset: multi · conditions: requires deep expertise · testable: no - proprietary · confidence: low
  ^MT160-C15-2
- **Rob Carver** In an experiment fitting up/down sequence patterns, as pattern length rises from 1 to 10 periods (up to 1,024 patterns) in-sample returns improve until the equity curve is a straight line while out-of-sample performance deteriorates; simple one-lag trend following stays similar in and out of sample.  #mech/research_method
  > Get up to 10, and you're you've got
  indicator: pattern-length complexity vs in/out-of-sample performance · asset: multi · conditions: number of patterns grows exponentially · testable: yes - replicable experiment · confidence: high
  ^MT160-C15-3

### C16
- **Niels Kaastrup-Larsen** AI used in trading models without supervision and transparency raises liability and explainability issues, unlike transparent trend rules where the output is known.  #mech/risk_management
  > what about the liability? What about the liability of a firm using AI in its models
  asset: multi · testable: no - governance point · confidence: medium
  ^MT160-C16-1

### C17
- **Rob Carver** Since costs are known and returns are not, between two new managers choose the cheaper one, while established managers with great net returns (Renaissance) keep high fees.  #mech/research_method
  > I always say that costs are known and returns are unknown.
  indicator: manager fees · asset: multi · direction: prefer lower-fee new managers · horizon: years · conditions: absent other information on performance · testable: partly - fees vs net return · confidence: high
  ^MT160-C17-1
- **Rob Carver** Many managers charge incentive fees without a hurdle, i.e. on total return including cash interest instead of only excess over the risk-free rate, which matters most when rates are high.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > a lot of the people you're allocating to are still charging quite, you know, hefty incentive fees and incentive fees that don't have a hurdle, right?
  indicator: incentive fee hurdle vs risk-free rate · asset: multi · conditions: Material when short rates are high (50bp vs 500bp). · testable: yes - fee arithmetic · confidence: high
  ^MT160-C17-X1
- **Rob Carver** Ted Seides's point: allocators say they push hard on fees but keep investing in high-fee managers, so there is no real negotiation; investors really care about net performance (Renaissance), not the fee level.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > you guys are talking a big game, but actually when you look at who you're investing in
  asset: multi · testable: partly - allocator behaviour can be studied · confidence: medium
  ^MT160-C17-X2

### C18
- **Rob Carver** Compare fees after adjusting for volatility target: 2-and-20 on a 25% vol CTA equals 1-and-10 on half the vol, so CTAs look cheap relative to low-vol long/short funds.  #mech/research_method
  > you should always look at fees adjusting for volatility
  indicator: fee per unit of volatility · asset: multi · conditions: comparing high-vol CTAs with low-vol equity funds · testable: yes - calculation · confidence: high
  ^MT160-C18-1
- **Rob Carver** Fee structure becomes two-tier: new funds charge less, established funds with track records keep high fees, and raising fees later is awkward for seed investors.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > we were kind of going to end up with is a two-tier system where anyone, um, who's starting a who's starting a fund in the last few years is is going to have much lower fees
  asset: multi · horizon: years · testable: no - industry observation · confidence: medium
  ^MT160-C18-X1
- **Niels Kaastrup-Larsen** Niels disagrees with competing on the lowest fees: CTA fees have already fallen over 35 years to reasonable levels, strategies cost money to run, and net returns are what matter.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > I'm not in that camp. I don't believe that uh, to be uh, the right thing to do for our industry
  indicator: CTA fee levels · asset: multi · horizon: years · testable: no - opinion · confidence: high
  ^MT160-C18-X2
- **Rob Carver** Legacy fund fees were very high because they were launched in the early 1990s when interest rates were higher and trail fees to advisers were part of the model; the fee margin has come down since.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > fees on some of the legacy funds we had were just you know, eye-popping
  indicator: fee levels · asset: multi · direction: fees down · horizon: years · testable: no - historical anecdote · confidence: high
  ^MT160-C18-X3

