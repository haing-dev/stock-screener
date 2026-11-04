---
source_id: MT019
title: "Backtesting Can't Predict The Future - Systematic Investor 310"
date: 2024-08-28
channel: "Top Traders Unplugged"
url: 
words: 10792
claims: 65
added_by_crosscheck: 3
corrections: 2
crosscheck: "opus cross-check"
speakers: ["Richard Brennan (guest, systematic trend-following manager and researcher)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Backtesting Can't Predict The Future - Systematic Investor 310

**Speakers:** Richard Brennan (guest, systematic trend-following manager and researcher); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Brennan and Niels review the August 2024 volatility shock and trend-following performance, then Brennan argues backtests overfit and recommends walk-forward out-of-sample testing (OOS drawdowns 35-40% versus 5-10% in backtests); that trends come from trader impact feedback (divergent vs convergent forces, cocoa example) so AI will not end them; and that highly correlated markets can still diversify outlier-hunting ensemble models via trade correlation.

**Approach:** trend following, backtesting and walk-forward, complex adaptive systems, trader impact, diversification

**Cross-check completeness estimate of first read:** 0.95 - first reader captured essentially every method and mechanism claim; only a sizing-style distinction and minor data/operational points were missing; one speaker error.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | intro; Aug 2024 vol event and trend followers' adaptation |
| C02 | 5 | CTA forced-selling estimates, vol-driven positioning, turbulence analogy |
| C03 | 5 | convergence strategies break, carry creep, psychology, look-back, volatility dampening |
| C04 | 4 | research caution, August sector performance, diversification, intramonth vol |
| C05 | 4 | VIX vs futures, trend barometer, August index numbers |
| C06 | 4 | backtest vs walk-forward, hindsight, selection bias |
| C07 | 5 | statistical bias, overfit, walk-forward design, benchmark with live managers |
| C08 | 4 | regime expectation, OOS drawdown, realism, adaptive process |
| C09 | 4 | three curves, mean reversion vs trend validation, in-sample size |
| C10 | 4 | contaminating OOS, data mining; AI and trends, trader impact |
| C11 | 4 | square-root law, collective impact, nonstationary mix, divergent vs convergent |
| C12 | 4 | three market structures, style switching, crowded trend followers, mean reversion dissipation |
| C13 | 4 | cocoa example, endogenous vs exogenous, AI and trends |
| C14 | 5 | AI cannot end trends; correlated markets and outlier hunters |
| C15 | 4 | ensembles, butterfly effect, cocoa, VaR crowding |
| C16 | 0 | outro, nothing actionable |

## Claims

### C01
- **Richard Brennan** In early August 2024 a sharp volatility event (yen carry unwind, Nasdaq and S&P drop) hurt trend followers, but it reversed quickly and trends resumed.  #mech/slow_reaction _(time-bound view)_
  > we got slapped slapped around by the Japanese Yen and um the NASDAQ coming off and the S&P 500 coming off
  indicator: JPY, Nasdaq, S&P 500 in Aug 2024 · asset: multi · direction: trend followers lose on sharp reversals · horizon: weeks · conditions: short sharp event followed by reversal · testable: yes - August 2024 CTA performance · confidence: high
  ^MT019-C01-1
- **Richard Brennan** Trend models adapt quickly: had the sell-off become a prolonged downtrend they would have adjusted and been well positioned.  #mech/slow_reaction
  > the good thing about our models is they they're very quick to adapt
  indicator: trend following models · asset: multi · horizon: weeks · testable: yes - trend following in drawdown regimes · confidence: medium
  ^MT019-C01-2

### C02
- **Niels Kaastrup-Larsen** A quick volatile event makes vol-scaled trend followers more defensive in positioning, so the next shock hurts less; expect performance dispersion and model speed to matter.  #mech/risk_management _(time-bound view)_
  > that usually makes us become a little bit more defensive in our positioning
  indicator: volatility-scaled position sizes · asset: multi · direction: reduce risk after vol spike · horizon: weeks · testable: yes - position size vs volatility · confidence: medium
  ^MT019-C02-1
- **Niels Kaastrup-Larsen** Sell-side estimates of forced CTA equity selling ($170B) are misleading: CTAs may keep selling after a rebound if volatility stays higher, and do not simply buy everything back.  #mech/crowding_positioning _(time-bound view)_
  > oh CT have to sell 170 billion I think was the number of equities
  indicator: estimated CTA equity selling · asset: equities · horizon: weeks · testable: partly - estimates are model based · confidence: medium
  ^MT019-C02-2
- **Niels Kaastrup-Larsen** Volatility-targeted trend followers reduce exposure after a vol rise even if prices recover.  #mech/risk_management
  > even if the markets bounce back we might be selling still because it's more volatile so we need to adjust positions
  indicator: volatility targeting · asset: equities · direction: sell after vol rise · horizon: weeks · conditions: for vol-adjusted programs · testable: yes - position sizing rule · confidence: high
  ^MT019-C02-3
- **Niels Kaastrup-Larsen** Analogy: severe turbulence hurts those inside but not the structure; similarly trend-following drawdowns are painful but do not break the models.  #mech/risk_management
  > none of the planes have any structural damage
  indicator: trend following drawdowns · asset: multi · horizon: years · conditions: unless rules are abandoned · testable: no - analogy · confidence: medium
  ^MT019-C02-4
- **Niels Kaastrup-Larsen** No market event breaks a rule-based trend system with sensible, tested rules (not AI-optimised); convergence strategies and systematic macro are the ones that tend to break.  #mech/risk_management
  > it's very hard for me to imagine that any Market event would break a trend following system unless you start doing things you shouldn't do
  indicator: trend following · asset: multi · horizon: years · conditions: sensible rules, long-tested · testable: partly - robustness vs stress events · confidence: medium
  ^MT019-C02-5
- **Niels Kaastrup-Larsen** Trend followers split into those who resize positions continuously with volatility (and keep selling after a vol spike) and those who hold position size fixed after entry, so their flows and results differ in volatility shocks.  #mech/risk_management _(added by opus cross-check)_
  > well some of us I know you you don't but some of us would need to adjust positions according
  indicator: dynamic vs static position sizing · asset: multi · direction: vol-adjusters sell after vol spikes; static sizers do not · horizon: weeks · conditions: volatility shocks · testable: partly - compare manager returns by sizing style around vol spikes · confidence: medium
  ^MT019-C02-X1

### C03
- **Niels Kaastrup-Larsen** Convergence strategies and systematic macro tend to break in turbulence, unlike trend following.  #mech/risk_management
  > other strategies that I see do break are of course tend to be convergence strategies and even quote unquote these systematic macro strategies
  indicator: convergence and systematic macro strategies · asset: multi · horizon: years · testable: partly - strategy comparison in stress months · confidence: low
  ^MT019-C03-1
- **Niels Kaastrup-Larsen** Investor pressure pushes trend programs to add non-trend models such as carry to smooth returns, which dilutes the pure trend profile and may explain dispersion between managers.  #mech/behavioral _(time-bound view)_
  > there's always going to be a pressure from investors to uh either return better when there are no Trends but also to smooth out returns in general
  indicator: carry in trend programs · asset: multi · horizon: months · testable: yes - compare pure vs diversified trend programs · confidence: medium
  ^MT019-C03-2
- **Richard Brennan** The trend follower's weak point is psychology: overriding rules causes errors, so discipline and patience are required.  #mech/behavioral
  > our models are incredibly robust but our ability out to our psychology to hold and and respect what these models do
  asset: multi · horizon: years · testable: no - behavioral · confidence: high
  ^MT019-C03-3
- **Richard Brennan** Medium to long-term trend following is more robust and has performed better than shorter-term trend following.  #mech/slow_reaction
  > I'm a big fan of sort of medium to long term I think all the data that I've seen suggest that is more robust in the long run and has performed better than shorter term
  indicator: trend look-back length · asset: multi · direction: prefer medium/long-term trends · horizon: years · testable: yes - performance by look-back · confidence: medium
  ^MT019-C03-4
- **Niels Kaastrup-Larsen** Dampening volatility via volatility adjustment is like an aircraft stabiliser.  #mech/risk_management
  > we're trying to find things that will dampen the uh Vol volatility of the prog which is what volatility adjusting is doing
  indicator: volatility adjustment · asset: multi · horizon: days · testable: yes - vol scaling backtests · confidence: medium
  ^MT019-C03-5

### C04
- **Niels Kaastrup-Larsen** Risk-reducing research is acceptable only if it does not change the long-term return profile or cause style drift, otherwise it just lowers expectations.  #mech/research_method
  > it's fine if we can find things to improve and say lower the volatility or reduce the draw down as long as we don't change the profile and the perform long-term performance of the program
  asset: multi · horizon: years · testable: yes - compare return profile before/after · confidence: medium
  ^MT019-C04-1
- **Niels Kaastrup-Larsen** In August 2024 equities were the hardest sector for trend followers, currencies (yen) difficult, fixed income divided, while sugar, coffee and grains trended well.  #mech/slow_reaction _(time-bound view)_
  > equities have been the most challenging sector for for Trend followers by quite a margin
  indicator: sector P&L in Aug 2024 · asset: multi · direction: equities losses, softs and grains gains · horizon: weeks · testable: yes - sector attribution · confidence: medium
  ^MT019-C04-2
- **Niels Kaastrup-Larsen** True diversification into commodities matters; managers concentrated in financials (to hold large AUM) suffered more in the month.  #mech/risk_management _(time-bound view)_
  > just the importance of true diversification in a portfolio if you're too heav heavy on financials because you want to have massive AUM
  indicator: financials vs commodities exposure · asset: multi · horizon: months · testable: yes - compare manager universes · confidence: medium
  ^MT019-C04-3
- **Richard Brennan** Monthly industry statistics hide intra-month volatility, so a month with a severe shock can look benign in the record.  #mech/research_method
  > if you analyze things on a month-by-month basis you won't see this intram month volatility and that's a bit deceptive
  indicator: monthly returns · asset: multi · horizon: weeks · testable: yes - compare daily vs monthly drawdowns · confidence: high
  ^MT019-C04-4
- **Richard Brennan** In August 2024 the trend-follower losses came from the Nikkei, yen and Nasdaq/equity indexes; equity indexes recovered within the month while the yen and Nikkei positions stayed down, and commodities kept trending.  #mech/crowding_positioning _(added by opus cross-check, time-bound view)_
  > the equity indexes have all pretty well recovered the the Yen and the um Nicki are still down
  indicator: Nikkei, JPY, Nasdaq, commodity trends Aug 2024 · asset: multi · horizon: weeks · testable: yes - market returns for the month · confidence: high
  ^MT019-C04-X1

### C05
- **Niels Kaastrup-Larsen** The VIX cash spike to about 65 was not matched by VIX futures; the spike subsided very quickly back to low-vol conditions, like a fast news cycle.  #mech/overshoot _(time-bound view)_
  > did the vix really hit 65 or you know because the Futures didn't the Futures didn't hit 65
  indicator: VIX vs VIX futures · asset: equities · horizon: days · testable: yes - VIX data · confidence: medium
  ^MT019-C05-1
- **Niels Kaastrup-Larsen** Trend Barometer (short timeframe) recovered to 61 in late August after the early-month shock, mirroring the quick recovery (but the app stopped updating).  #mech/slow_reaction _(time-bound view)_
  > it finished at 61 yesterday
  indicator: TTU Trend Barometer · asset: multi · horizon: weeks · testable: partly - proprietary · confidence: low
  ^MT019-C05-2
- **Niels Kaastrup-Larsen** August 2024 data: Beta 50 -1.7% (+3.4% YTD), SG CTA -2.6% in August, SG Trend -3.55% (+2.3% YTD), short-term traders +0.61%, so industry recovered less than managers Brennan and Niels know.  #mech/slow_reaction _(time-bound view)_
  > beta 50 is down still 1.7% up 3.4% for the year sock gen CG index down 2.6 6% in August up 3.4% for the year
  indicator: Beta 50, SG CTA, SG Trend, SG Short Term Traders · asset: multi · horizon: months · testable: yes - published index figures · confidence: medium
  **Correction (cross-check):** Incomplete/garbled numbers: the host corrects himself to SG CTA +2.1% YTD (not 3.4%), and the short-term traders index is +0.61% for both the month and the year. → August 2024: Beta 50 -1.7% (+3.4% YTD), SG CTA -2.6% (+2.1% YTD), SG Trend -3.55% (+2.3% YTD), SG Short-Term Traders +0.61% (+0.61% YTD).
  ^MT019-C05-3
- **Niels Kaastrup-Larsen** August 2024 traditional markets: MSCI World +1% (+13.84% YTD), global sovereign bonds +1% (+1.58% YTD), S&P 500 TR +1% (+17.8% YTD).  #mech/new _(time-bound view)_
  > the S&P 500 total return up about 1% in August up 17.8% so far this year
  indicator: MSCI World, S&P 500, global bonds · asset: multi · horizon: months · testable: yes - published index figures · confidence: medium
  ^MT019-C05-4
- **Niels Kaastrup-Larsen** Third-party indicators and data feeds can silently stop updating (as the Trend Barometer app did), so systematic users such as replicators relying on others' data face data-reliability risk.  #mech/research_method _(added by opus cross-check)_
  > they are using other people's STA and it just shows you that sometimes these things are not uh to be relied on
  indicator: third-party data feeds · asset: multi · testable: no - operational caution · confidence: medium
  ^MT019-C05-X1

### C06
- **Richard Brennan** Backtests significantly introduce overfitting, with marked differences between backtest and walk-forward/out-of-sample results.  #mech/research_method
  > the back test process actually significantly introduces over fitting into the process
  indicator: backtest vs walk-forward results · asset: multi · testable: yes - compare in-sample vs out-of-sample · confidence: high
  ^MT019-C06-1
- **Richard Brennan** Live trading is on the right-hand side of the chart with no hindsight; backtests give hindsight advantage, as do macro causal narratives given after the event.  #mech/research_method
  > with a back test when you've got the history laid out you know every deviation all in hindsight you've got the benefit of This Magnificent hindsight position
  asset: multi · testable: no - conceptual · confidence: high
  ^MT019-C06-2
- **Richard Brennan** Backtests are useful for sensitivity tests across simulated regimes but should never be used to predict future expected returns because they are always overfit.  #mech/research_method
  > back testing is useful for doing things like um undertaking sensitivity tests on your models
  asset: multi · testable: yes - sensitivity analysis · confidence: high
  ^MT019-C06-3
- **Richard Brennan** Selection bias: with ten parameter settings, choosing the best-looking stream uses hindsight selection and biases the forward expectation.  #mech/research_method
  > you've got 10 parameter choices and your results are 10 different return streams
  indicator: parameter selection · asset: multi · testable: yes - parameter selection simulation · confidence: high
  ^MT019-C06-4

### C07
- **Richard Brennan** Choosing among alternatives with hindsight introduces statistical bias that cannot occur in live trading and should not be done in backtests.  #mech/research_method
  > biasing your result that's what we call a statistical bias associated with a hindsight selection process
  asset: multi · testable: yes · confidence: high
  ^MT019-C07-1
- **Richard Brennan** A backtest overfits to noise and every past event as the full road map is known, whereas the future order of events is unknown.  #mech/research_method
  > your back test is inevitably going to overfit to that perfect scenario that's laid down
  asset: multi · testable: yes · confidence: high
  ^MT019-C07-2
- **Richard Brennan** Use walk-forward out-of-sample testing: develop in-sample (e.g. 1970-2000), then test untouched out of sample (2000-2024) to anticipate live drawdown and performance.  #mech/research_method
  > a far better way to undertake testing for anticipating what your future performance is going to be is what I'm referring to as a walk forward using out of sample data
  indicator: in-sample / out-of-sample split · asset: multi · horizon: years · testable: yes - split sample · confidence: high
  ^MT019-C07-3
- **Richard Brennan** Once data is used for development and robustness testing it is tainted and cannot serve as out-of-sample.  #mech/research_method
  > you have tainted that data once you've used it you can never use it again
  asset: multi · testable: yes · confidence: high
  ^MT019-C07-4
- **Richard Brennan** An out-of-sample equity curve is close to live track records of other managers, unlike the glorious backtest.  #mech/research_method
  > you can Benchmark that against the live track records of other fund managers and lo and behold you're going to find it's very similar
  indicator: out-of-sample vs live manager track records · asset: multi · horizon: years · testable: yes - compare to CTA indices · confidence: medium
  ^MT019-C07-5

### C08
- **Richard Brennan** Trend following depends on regime; in an unfavorable regime expect stagnation and drawdowns, so expect a volatile equity curve, not a straight line.  #mech/research_method
  > you've got to have a favorable Trend following regime for your Trend following models to be working
  indicator: trend following regime · asset: multi · horizon: years · conditions: unfavorable trend regime · testable: yes - regime-based performance · confidence: high
  ^MT019-C08-1
- **Richard Brennan** Out-of-sample drawdown is far larger (35-40%) than the backtest drawdown (5-10%), giving a realistic benchmark for maximum drawdown, CAGR and volatility.  #mech/research_method
  > the back test draw down is going to say 10% 5% or something the the outer sample draw down is going to say 35% 40% something
  indicator: maximum drawdown out-of-sample · asset: multi · horizon: years · testable: yes - his own results · confidence: medium
  ^MT019-C08-2
- **Richard Brennan** Backtests shown publicly (e.g. on Twitter) are beautiful equity curves; one should demand realism.  #mech/behavioral
  > you never see a bad um back test and the reality is you want to see a bad you want to see realism you want to see realism
  asset: multi · testable: no - observation · confidence: medium
  ^MT019-C08-3
- **Richard Brennan** An adaptive workflow periodically re-estimates in-sample and walks forward, and the result should be compared with the static model on the same period.  #mech/research_method
  > you might have an Adaptive proc built in where you might use a insample component from 1970 up to 2000 and then periodically you might um do do a walk forward
  indicator: adaptive walk-forward · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT019-C08-4

### C09
- **Richard Brennan** Compare three curves (backtest 'pink unicorn', out-of-sample, adaptive); the backtest is always the best but unrealistic.  #mech/research_method
  > recognizing that the back test Equity curve is always going to be far superior than the other models
  asset: multi · testable: yes · confidence: high
  ^MT019-C09-1
- **Richard Brennan** Mean reversion modellers expect no out-of-sample deterioration after finding a pattern, but trend followers cannot, because trends arrive irregularly with favorable and unfavorable regimes.  #mech/research_method
  > but in our world of trend following we never know when the next Trends are going to be so we don't have that luxury of assuming that The Continuous trajectory going on into the future
  asset: multi · testable: partly - contrasts mean reversion vs trend validation · confidence: medium
  ^MT019-C09-2
- **Niels Kaastrup-Larsen** Social-media backtest results are unlikely to reproduce; big managers use some walk-forward process.  #mech/research_method
  > clearly they're going to be showing some uh type of of back tested results which are you know unlikely to be uh uh reproduced in the future for sure
  asset: multi · testable: no - observation · confidence: low
  ^MT019-C09-3
- **Richard Brennan** In-sample development needs a lot of data for robustness; multi-market testing over 30 years and 100 markets provides it.  #mech/research_method
  > you might decide that um multimarket testing um is the way to develop robustness
  indicator: multi-market in-sample set · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT019-C09-4

### C10
- **Richard Brennan** Selecting or changing models after seeing out-of-sample results contaminates the test with statistical bias; people underestimate how sensitive results are to overfitting.  #mech/research_method
  > that's really starting to interfere with that that process and contaminating um your process with statistical bias
  asset: multi · testable: yes · confidence: high
  ^MT019-C10-1
- **Richard Brennan** Avoid data-mining packages that overfit and then remove it afterwards (Monte Carlo etc.); never touch out-of-sample data so you do not need to extract overfitting later.  #mech/research_method
  > never never touch that out of sample data that's gold to you
  asset: multi · testable: yes · confidence: high
  ^MT019-C10-2
- **Richard Brennan** Trends exist in any complex adaptive system, so human behavioural bias (prospect theory) is a symptom, not the root cause.  #mech/structural_shift
  > Trends are are omnipresent in any complex adaptive system
  asset: multi · testable: no - theory · confidence: medium
  ^MT019-C10-3
- **Richard Brennan** Trends and mean reversion arise from trader impact: orders that must be matched and that exert pressure on price, not from news, fundamentals or human behaviour per se.  #mech/liquidity_flows
  > I'd like to suggest that it's actually Trader impacts that is responsible for Trends and mean reversion in the financial markets
  indicator: trader order flow impact · asset: multi · testable: partly - microstructure · confidence: medium
  ^MT019-C10-4

### C11
- **Richard Brennan** Market impact follows a square-root law (Bouchaud), a nonlinear relation between order size and price impact.  #mech/liquidity_flows
  > it follows a square root law larger orders have more gravitas more impact in the market than smaller orders
  indicator: square-root market impact · asset: multi · horizon: days · testable: yes - well-documented microstructure · confidence: high
  ^MT019-C11-1
- **Richard Brennan** Groups of traders (trend followers, mean reverters, fundamentals, HFT) exert collective forces, and their combination moves price.  #mech/crowding_positioning
  > it's the aggregated effect of all of these Trader impacts the collective impact of all of that which is responsible for moving price
  indicator: group trader impact · asset: multi · testable: partly - needs flow decomposition · confidence: medium
  ^MT019-C11-2
- **Richard Brennan** Markets are nonstationary: the mix of participant groups changes as traders enter and leave, so the balance of divergent and convergent pressure shifts.  #mech/structural_shift
  > this this Trader impact changes over the course of time the the relative mix of participants doing a similar thing changes
  indicator: participant mix · asset: multi · horizon: years · testable: partly - proxy needed · confidence: medium
  ^MT019-C11-3
- **Richard Brennan** Divergent pressures (positive feedback) amplify trends and convergent pressures (negative feedback) dissipate trend signals.  #mech/cycle_persistence
  > we can start looking at two different pressures that are working in the market Divergent pressures those that are amplifying each other
  asset: multi · testable: partly · confidence: medium
  ^MT019-C11-4

### C12
- **Richard Brennan** Three market structures: divergent wins (trend), convergent wins (mean reversion), or noise when neither wins and there is no directional move.  #mech/cycle_persistence
  > but there is a third class of Market structure which is noise which is when the convergent and Divergent neither win there's a battle going on
  indicator: regime classification · asset: multi · direction: trend following fails in noise · testable: partly - needs regime classifier · confidence: medium
  ^MT019-C12-1
- **Richard Brennan** Participants switch style to join strong trends, amplifying the signal, so the mix moves toward divergent behaviour in strong trends.  #mech/crowding_positioning
  > I'm going to change my style from mean reversion or high frequency trade whatever I'm going to jump on board that Trend
  asset: multi · direction: trends extend · horizon: weeks · conditions: strong trends · testable: partly - flow data · confidence: low
  ^MT019-C12-2
- **Richard Brennan** Too many trend followers does not kill trend following; it makes trends more extreme because their impact is collectively amplifying.  #mech/crowding_positioning
  > if there are too many Trend followers in the market TR Trends get more extreme because everyone is doing the same thing
  indicator: trend follower crowding · asset: multi · direction: trends extend when crowded · horizon: years · testable: yes - compare trend returns vs AUM · confidence: medium
  ^MT019-C12-3
- **Richard Brennan** Convergence (mean reversion) signals fight a prior trend, so the mean reverter's edge dissipates when enough of them oppose the trend (and the trend signal dissipates if they win).  #mech/crowding_positioning
  > to apply convergence you're usually commencing from a Divergent premise in other words price has made an Excursion away from an equilibrium
  indicator: mean reversion crowding · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT019-C12-4

### C13
- **Richard Brennan** Cocoa 2024 example: trend followers who size dynamically sold 80-90% of notional Jan-May as volatility rose.  #mech/risk_management _(time-bound view)_
  > selling 80 85 90% of their notional position simply because the volatility was picking up
  indicator: cocoa; trend follower positions · asset: commodities · direction: reduce size as vol rises · horizon: months · testable: yes - vol-scaled position · confidence: medium
  **Correction (cross-check):** Wrong speaker: the cocoa example (trend followers selling 80-90% of notional Jan-May 2024 as volatility rose) is given by Niels, who introduces it as 'a really good example'; Brennan replies afterwards. → Niels Kaastrup-Larsen: in the 2024 cocoa run, trend followers who size dynamically sold roughly 80-90% of their notional between January and April/May as volatility rose.
  ^MT019-C13-1
- **Niels Kaastrup-Larsen** Global macro funds bought cocoa as trend followers sold in March 2024, carrying the price higher before a roughly 40% correction.  #mech/crowding_positioning _(time-bound view)_
  > so they started buying Coco in March right at the same time we were selling but initially that maybe with other people carried the price higher actually even though Trend followers were selling
  indicator: cocoa; macro fund buying vs CTA selling · asset: commodities · horizon: months · testable: partly - positioning data · confidence: low
  ^MT019-C13-2
- **Niels Kaastrup-Larsen** Bouchaud's conclusion: endogenous forces (flows) explain big moves more than exogenous news.  #mech/overshoot
  > endogenous forces are actually much more responsible for uh big moves than the exogenous which is like news events and stuff like that
  asset: multi · testable: yes - microstructure research · confidence: medium
  ^MT019-C13-3
- **Richard Brennan** For cocoa, supply news in Africa began the run but participants jumping on the bandwagon accelerated it, and large holders selling in April probably caused the sell-off.  #mech/overshoot _(time-bound view)_
  > the acceleration of that Trend was certainly I think attributed to endogenous forces
  indicator: cocoa · asset: commodities · horizon: months · testable: partly - case study · confidence: low
  ^MT019-C13-4

### C14
- **Richard Brennan** AI agents also exert impact, so trends and mean reversion will persist; AI will not remove them.  #mech/structural_shift
  > I think Trends and mean reversion are here to stay for eternity because I think that they're a universal symptom of how collect Dynamics working complex adaptive systems
  asset: multi · horizon: years · testable: no - forecast · confidence: medium
  ^MT019-C14-1
- **Richard Brennan** Conventional wisdom that highly correlated markets add no diversification is correct for most models but not for 'outlier hunter' trend followers using ensembles of models.  #mech/risk_management
  > for nearly all models except the outly hunter I would say 100% correct however for the outly hunter I'd say Incorrect
  indicator: price correlation vs trade correlation · asset: multi · conditions: outlier-hunting ensembles only · testable: yes - compare correlation of returns vs prices · confidence: medium
  ^MT019-C14-2
- **Richard Brennan** What matters is the correlation of strategy returns from trading each market, not price correlations.  #mech/risk_management
  > the important thing for the outlaw Hunter is not the price correlations it's the trade correlations
  indicator: trade (return-stream) correlation · asset: commodities · testable: yes · confidence: high
  ^MT019-C14-3
- **Richard Brennan** Applying the same ensemble to Brent and WTI gives quite uncorrelated return streams despite highly correlated prices.  #mech/risk_management
  > I find that their performance results their return streams are really quite uncorrelated
  indicator: Brent vs WTI ensemble return correlation · asset: commodities · direction: trade both Brent and WTI · conditions: ensembles of trend models in outlier moves · testable: yes - own backtest · confidence: medium
  ^MT019-C14-4
- **Richard Brennan** In nonlinear outlier territory, small differences in price paths lead to significantly dispersed trade results.  #mech/structural_shift
  > what you find is that when you are in this nonlinear territory very small variations are sufficient cause significantly dispersed results
  asset: multi · testable: partly · confidence: medium
  ^MT019-C14-5

### C15
- **Richard Brennan** Outliers are volatile and need an ensemble of models to maximize extraction, since a single system is snagged by the volatility.  #mech/risk_management
  > if you apply a single system to an outlaw you're going to fail because it might Capture One Outlaw but it's going to be snagged out of a volatility move of one outlier
  indicator: ensemble trend models · asset: multi · horizon: months · conditions: outlier trends · testable: yes - ensemble vs single model · confidence: medium
  ^MT019-C15-1
- **Richard Brennan** Butterfly effect: tiny initial differences create dispersed outcomes in tail events, so correlated markets can still diversify.  #mech/structural_shift
  > this is the very small differences in initial state are sufficient to create significant um dispersion in the nonlinear mechanics that arises from that result
  asset: multi · testable: no - analogy · confidence: low
  ^MT019-C15-2
- **Richard Brennan** An outlier hunter holds and pyramids a strong trend (cocoa 2024) and accepts the big give-back when it turns.  #mech/risk_management _(time-bound view)_
  > I wouldn't have been selling into trend on Coco in 2024
  indicator: cocoa · asset: commodities · direction: hold or add to outlier trends · horizon: months · testable: partly - anecdote · confidence: medium
  ^MT019-C15-3
- **Niels Kaastrup-Larsen** Even if many managers use VaR-style risk models sensitive to volatility, not all do, so the market is not forced into synchronized selling.  #mech/crowding_positioning
  > the answer is of course not everyone uses valued risk a lot of people do but not everyone and therefore it still works
  indicator: VaR-based risk management · asset: multi · horizon: weeks · testable: partly - data on adoption · confidence: low
  ^MT019-C15-4

