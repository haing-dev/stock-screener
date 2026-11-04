---
source_id: MT174
title: "The Next Evolution of Trend Following ft. Nick Baltas - Systematic Investor - Ep.410"
date: 2026-07-26
channel: "Top Traders Unplugged"
url: 
words: 11695
claims: 42
added_by_crosscheck: 16
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Nick Baltas (systematic quant strategist at a large investment bank)", "Niels Kaastrup-Larsen (host)"]
tags: [source, layer0]
---
# The Next Evolution of Trend Following ft. Nick Baltas - Systematic Investor - Ep.410

**Speakers:** Nick Baltas (systematic quant strategist at a large investment bank); Niels Kaastrup-Larsen (host)

**Summary:** Systematic Investor Ep.410 (July 2026): trend and carry performance in 2026, AI in research, Graham paper on market universe size, Run One River defence framework, and thematic/narrative momentum papers.

**Approach:** trend following, carry, thematic investing, defensive overlays

**Cross-check completeness estimate of first read:** 0.70 - first reader captured the two main papers (Graham universe size, Run One River defence layers), the thematic/narrative arguments and the performance narrative accurately; missed the July month-to-date index numbers, client-demand comments, five-of-seven-months record, portable-alpha leverage logic (two points), the third-bucket specification, narrative life cycle and lead-lag mechanism, theme transience in covariance, the price-as-objective and price-path-as-proxy discussion, and Niels's sector-grouping scepticism

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, Die with Zero book, banter |
| C02 | 1 | AI model turnover, concert; AI in firms |
| C03 | 2 | AI use in research, hallucinations, morning agent |
| C04 | 2 | coffee, June/July CTA trend recovery and weak signals |
| C05 | 2 | 2026 performance, carry and reversion, V shape in March |
| C06 | 2 | index numbers, Graham paper on universe size intro |
| C07 | 2 | universe size results |
| C08 | 2 | Run One River Perfect Hedge paper |
| C09 | 2 | trend speed as hedge, portable alpha question |
| C10 | 1 | equity-bond shock, thematics paper intro |
| C11 | 2 | quant investing pillars and risk models |
| C12 | 2 | themes as tagging, correlation and momentum |
| C13 | 1 | themes in risk models and narrative momentum |
| C14 | 2 | covariance bias, narrative momentum results |
| C15 | 1 | backtesting themes and point-in-time data |
| C16 | 1 | narrative zoo, evergreen topics, skepticism |
| C17 | 1 | attention, dimensionality, wrap-up |

## Claims

### C02
- **Niels Kaastrup-Larsen** The frontier AI model changes every few weeks (versus months last year), making firm-level AI integration and tool choice hard; using a version one step behind captures most of the benefit.  #mech/structural_shift
  > the quote unquote best model at the moment get replaced like every 10 I think it was every 10 days or every 19 days
  indicator: best-model turnover · asset: other · horizon: months · testable: no - anecdotal · confidence: medium
  ^MT174-C02-1

### C03
- **Nick Baltas** AI is mainly used for research (collecting, synthesising information, coding) with human in the loop; open-ended factual queries can be confidently wrong, so outputs require expert checking.  #mech/research_method
  > The primary use at least in my view and the things that we do we see on the day-to-day is more to enhance research
  indicator: LLM-assisted research · asset: other · conditions: Closed-form tasks easier to verify than open questions · testable: no · confidence: high
  ^MT174-C03-1
- **Niels Kaastrup-Larsen** A simple AI agent can collect CTA index performance and top stories each morning and flag relevant research papers, though numbers are sometimes wrong when websites lag.  #mech/research_method
  > build a little agent that goes out every morning before I wake up and I've given it certain things to collect for me like performance of the main CTA indices
  indicator: automated CTA index monitoring · asset: other · horizon: days · testable: no · confidence: medium
  ^MT174-C03-2
- **Nick Baltas** AI output is checkable today because current practitioners were trained without AI and can spot errors; Baltas worries about how later cohorts will keep that judgement if everything becomes a prompt, and Niels adds that without expertise supervision the output can run uncontrolled, so human expertise stays the control layer.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > we have been trained without it and we can assess the output and we have the wisdom or maybe the experience or the expertise to call the bluff from the truth
  asset: other · horizon: years · conditions: Holds while models still make plausible errors; may change as models improve · testable: no - qualitative judgement about skills and oversight · confidence: medium
  ^MT174-C03-X1

### C04
- **Niels Kaastrup-Larsen** In 2026 June was weak and early July soft for CTAs, then trend recovered led by energies, currencies and fixed income, with only some markets in each sector participating (a trend-pickers market).  #mech/slow_reaction _(time-bound view)_
  > we had a weak June as as as an industry. We had a soft start to July. Now things seems to be turning around in the last week or so for CTAs and trend followers.
  indicator: CTA indices June-July 2026 · asset: multi · horizon: weeks · conditions: 2026 · testable: yes · confidence: high
  ^MT174-C04-1
- **Nick Baltas** Models that limit position size on weak signals lagged in a rates sell-off because a small short is lucky only without strong signals; strong profit came from rates shorts and commodities.  #mech/slow_reaction _(time-bound view)_
  > some of the models that actually try to put a threshold on how aggressive they would be with weak signals have been lagging a bit behind
  indicator: signal-strength threshold in trend sizing · asset: rates · horizon: weeks · conditions: July 2026 · testable: partly · confidence: medium
  ^MT174-C04-2

### C05
- **Nick Baltas** In 2026 carry was strong in FX and commodities (backwardation from geopolitical activity), complementing trend, and reversion had a strong four or five months, so the diversified multi-strategy aggregation worked.  #mech/risk_premium _(time-bound view)_
  > Kerry has been very very strong both in the effect space and as you would imagine the commodity space with the backoration we're seeing
  indicator: carry returns in FX and commodities · asset: multi · direction: long carry in commodities with backwardation · horizon: months · conditions: 2026 geopolitical backdrop · testable: yes · confidence: high
  ^MT174-C05-1
- **Nick Baltas** A V-shaped equity move occurs about once a year (March 2026), but this one was a fast recovery instead of a fast drop, so it hurt trend less; dynamic volatility scaling added value.  #mech/overshoot _(time-bound view)_
  > the typical Vshapes you know the the one per year so we had one this year right in March.
  indicator: dynamic volatility scaling of trend · asset: equities · horizon: months · conditions: V-shape with fast recovery · testable: yes · confidence: medium
  ^MT174-C05-2
- **Nick Baltas** Client demand for trend and diversifiers is rising across the board, driven by recent performance and protection data points and by trend being seen as a defensive trade; Baltas adds that institutions are becoming more focused on protecting the downside, which is why defence frameworks keep being published.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check, time-bound view)_
  > there is certainly increased interest you know across all fronts
  indicator: client interest / allocations to trend following and diversifiers · asset: multi · direction: inflows to trend and diversifiers up · horizon: months · conditions: July 2026, after weak equity spells and geopolitical risk · testable: partly - CTA fund flows can be measured, interest cannot · confidence: medium
  ^MT174-C05-X1
- **Nick Baltas** In 2026 Baltas's trend programs were positive in five of seven months (if July closed positive); the two losing months were June (reversion primarily in equities) and March (the V-shaped equity move), so the year's losses came from equity reversals.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > that's the seven month of the year right that's the fifth out of seven um assuming it closes positive
  indicator: monthly trend program returns 2026 · asset: multi · direction: trend positive most months, losses in equity reversals · horizon: months · conditions: One bank's trend programs, to late July 2026 · testable: yes - monthly returns of trend indices · confidence: medium
  ^MT174-C05-X2

### C06
- **Niels Kaastrup-Larsen** CTA indices were about +10% YTD at end of July 2026 against MSCI World +9% and the aggregate bond index -0.12% YTD.  #mech/slow_reaction _(time-bound view)_
  > beta 50 is up 1.34% in July up 10% so far this year CT index up 0.89% 89% in July, up 10.37% for the year.
  indicator: SG CTA Index; SG Trend Index; BTOP50 · asset: multi · horizon: months · conditions: Data to 22 July 2026 · testable: yes · confidence: high
  **Correction (cross-check):** The index figures were read 'as of Wednesday' (the recording was on a Friday, upload date 26 July 2026), so they are to about 22 July, not end of July; July was a partial month, and Niels also gave July month-to-date figures that the claim omits. → As of the Wednesday before the Friday recording (about 22 July 2026) the Beta 50 index was about +10% YTD (+1.34% in July), the SG CTA index +10.37% YTD (+0.89% in July), the SG Trend index +10.15% YTD (+0.94% in July) and the short-term traders index +4.52% YTD; MSCI World was +9% YTD and the US aggregate bond index -0.12% YTD.
  ^MT174-C06-1
- **Nick Baltas** A trend follower delivers long-term returns and crisis alpha; if crisis alpha is the aim, use a small core universe because principal components (equity, duration) dominate in downturns, while for long-term performance add more diversifying markets.  #mech/risk_management
  > high level long-term positive returns and some downside protection, some crisis alpha.
  indicator: market universe size · asset: multi · direction: small core for defence; broad for returns · horizon: years · conditions: Crisis alpha driven by equity and duration · testable: yes · confidence: high
  ^MT174-C06-2
- **Niels Kaastrup-Larsen** In July 2026 (to the Wednesday before recording) trend and CTA indices were up about 0.9-1.3% while both MSCI World (-0.84%) and the US aggregate bond index (-0.96%) fell, an example of trend gaining when equities and bonds fall together, which is the main equity-bond shock; the short-term traders index was slightly down.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > US aggregate bond index down 96 basis points and down 12 basis point now for the year
  indicator: Beta 50 +1.34%, SG CTA +0.89%, SG Trend +0.94%, MSCI World -0.84%, US Agg -0.96% (July 2026 month-to-date) · asset: multi · direction: trend positive when equities and bonds both fall · horizon: weeks · conditions: Partial month; a rates sell-off helped short positions · testable: yes - index returns are public · confidence: high
  ^MT174-C06-X1

### C07
- **Nick Baltas** Graham Capital finds beyond 70-80 liquid markets, adding less liquid macro markets (currencies, EM equities, swaps) adds little, but exotic commodities, including Chinese ones, still add return up to more than 100 markets, with a liquidity hump.  #mech/structural_shift
  > as soon as you cross 70 to 80 markets, the less liquid markets do not really add much in terms of performance.
  indicator: number and liquidity of markets · asset: multi · direction: add exotic commodities, not macro · horizon: years · conditions: Commodity diversification only · testable: yes · confidence: high
  ^MT174-C07-1
- **Nick Baltas** A practical universe is 50-100 markets; going broader costs capacity or adds nothing because adding same-factor markets splits a fixed risk budget.  #mech/risk_management
  > we typically operate between the 50 and the 100.
  indicator: universe size · asset: multi · testable: yes · confidence: medium
  ^MT174-C07-2

### C08
- **Nick Baltas** A defensive portfolio has three layers: option-based hedges as first responders (reactive, costly), trend following as second responder for multi-month crises, and a diversifying third bucket (e.g. alternative risk premia) that moderates carry cost.  #mech/risk_management
  > The first responders and that's like more like
  indicator: hedge layering · asset: multi · testable: partly · confidence: high
  ^MT174-C08-1
- **Nick Baltas** The diversifying third bucket cannot be short gamma, because financing a hedge with downside risk turns the overlay into a relative-value trade rather than a defence.  #mech/risk_management
  > it cannot be a short gamma exposure
  indicator: short gamma financing of hedges · asset: multi · testable: partly · confidence: medium
  ^MT174-C08-2
- **Nick Baltas** Specification for the third defensive bucket: flat-to-negative correlation to equities and a payoff that is neither convex nor concave (for example alternative risk premia), so it can offset the bleed of the first two layers without adding downside risk.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > flat to negative correlation to equity markets. Obviously not convex but certainly not concave either.
  indicator: correlation to equities; payoff convexity of the diversifying sleeve · asset: multi · horizon: years · conditions: A short-gamma sleeve fails the test (see C08-2) · testable: yes - correlation and convexity of candidate sleeves can be measured · confidence: medium
  ^MT174-C08-X1

### C09
- **Niels Kaastrup-Larsen** Shorter-term trend may hedge a few days better but costs more in the long run and has become worse over the last decade; slower can be better.  #mech/slow_reaction
  > if we made the trend following side more responsive, i.e. shorter term, it will be a better hedge.
  indicator: trend lookback speed · asset: multi · direction: slower trend · horizon: years · testable: yes · confidence: medium
  ^MT174-C09-1
- **Nick Baltas** In portable alpha, trend on top of equities should limit its long-equity participation to avoid doubling risk on the upside.  #mech/risk_management
  > enhancing equities with a trend follower. I think it should come from the perspective of perhaps reduced upside participation in the trend program.
  indicator: trend overlay on equities · asset: equities · direction: cap long equity in trend overlay · horizon: years · conditions: Equity-only portfolio · testable: partly · confidence: medium
  ^MT174-C09-2
- **Nick Baltas** The Run One River report tabulates by year which trend model, which speed and which structure (an integrated trend program versus a portfolio of asset-class trends) did best, implying leadership rotates between years, so a speed or structure should not be chosen from one year's ranking.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > They have different speeds for trend followers and they show which year which speed has done better.
  indicator: annual ranking of trend speeds and trend constructions · asset: multi · horizon: years · conditions: Baltas describes the content only; the conclusion about rotation is an inference · testable: yes - rank speeds and structures per year in a trend universe · confidence: low
  ^MT174-C09-X1
- **Niels Kaastrup-Larsen** In portable alpha, the notional leverage from a trend overlay is less risky than it looks, because the added exposure has historically been negatively correlated to equities in longer equity crises, so it works as a hedge rather than extra risk.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > the kind of extra leverage you're adding is quote unquote the trend which historically at least we can't talk about the future historically has been negatively correlated uh when your uh equities have gone into a longer crisis
  indicator: correlation of trend to equities in prolonged equity drawdowns · asset: multi · direction: trend overlay offsets equity losses · horizon: months · conditions: Historical pattern; fails if trend is long equities into a fast reversal · testable: yes - correlation in drawdown episodes · confidence: medium
  ^MT174-C09-X2

### C10
- **Nick Baltas** For an equity-bond portfolio the main shock is inflation, when both fall, which unfolds over a quarter or more; unconstrained medium-term trend is the hedge for that.  #mech/cycle_persistence
  > The equity bond portfolio is not facing its worst challenge when equities are falling. It is when both are falling.
  indicator: simultaneous equity-bond drawdowns · asset: multi · direction: unconstrained trend for equity-bond portfolio · horizon: months · conditions: Inflation shocks · testable: yes · confidence: high
  ^MT174-C10-1
- **Nick Baltas** Leverage itself is not the problem with stacking trend on a portfolio; the danger is added leverage on the asset the portfolio is already concentrated in, so for an equity-only portfolio moderate the long-equity risk of the overlay, while for equity-bond portfolios keep trend unconstrained.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > it's not that the increased leverage is creating the concern here it's the increased leverage on the asset that you're highly concentrated
  indicator: overlap between overlay exposure and core portfolio concentration · asset: equities · direction: limit overlay's long exposure to the core asset · conditions: Depends on the main shock the investor fears (equities down versus equities and bonds down) · testable: partly - compare overlay variants in equity-only versus equity-bond portfolios · confidence: medium
  ^MT174-C10-X1
- **Nick Baltas** At the Goldman-hosted research conference machine learning, nonlinear models and LLM-based sentiment and thematic mapping appeared in almost every topic (portfolio construction, equity forecasting), showing AI/ML tools are now standard in financial economics research.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > AI and the use of the machine learning and AI models has become now you know very very common um in pretty much all the topics we had
  asset: other · horizon: years · conditions: Anecdote from one conference · testable: no - anecdotal observation · confidence: medium
  ^MT174-C10-X2

### C11
- **Nick Baltas** Low beta earns excess risk-adjusted return because leverage-constrained investors with benchmarks overbid high-beta names; systematic returns come from risk premium or structural/behavioral inefficiency.  #mech/risk_premium
  > lowrisk stocks are typically coming with a greater than expected uh sharp ratio uh primarily
  indicator: low beta / low vol · asset: equities · direction: long low beta · horizon: years · conditions: Leverage constraints · testable: yes · confidence: high
  ^MT174-C11-1
- **Nick Baltas** Risk model factors (such as countries) explain risk but are not necessarily rewarded; risk models reduce dimensionality.  #mech/research_method
  > Risk factors are not always risk premier. risk factors explain risk.
  indicator: risk model factors · asset: multi · testable: yes · confidence: high
  ^MT174-C11-2

### C12
- **Nick Baltas** A theme is just a tag grouping assets with a common feature; as investors allocate by theme, correlations within it rise beyond sector links.  #mech/behavioral
  > themes are nothing more than a tagging operation.
  indicator: thematic basket correlation · asset: equities · horizon: months · testable: yes · confidence: medium
  ^MT174-C12-1
- **Nick Baltas** Theme allocation creates price pressure and short-term dislocation that momentum signals pick up, so thematic hype contributes to trends.  #mech/slow_reaction
  > if the market is not elastic enough, it starts building some some some short-term price dislocation.
  indicator: thematic flows · asset: equities · direction: long momentum in hyped themes · horizon: weeks · conditions: Inelastic market · testable: partly · confidence: medium
  ^MT174-C12-2
- **Nick Baltas** Since COVID investment theses have shifted toward themes (the stay-at-home theme being one example), with banks building thematic baskets that hedge funds use for active bets or hedges; this flow into themes is a driver of the rising within-theme correlation.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > there has been a bit of transition in the investment thesis um more around thematics
  indicator: thematic basket products and usage · asset: equities · horizon: years · conditions: Post-2020 regime · testable: partly - thematic ETF/basket growth is measurable · confidence: medium
  ^MT174-C12-X1

### C13
- **Nick Baltas** Themes are another dimensionality-reduction layer with both risk implications (covariance structure) and potential dynamic allocation returns, even without a clear risk premium (like a stagflation narrative), akin to a trend-following mindset of intertemporal demand.  #mech/behavioral
  > theatics in my mind is another way of of of of reducing dimensionality
  indicator: thematic exposure · asset: multi · horizon: months · conditions: No long-term premium implied · testable: no · confidence: medium
  ^MT174-C13-1

### C14
- **Nick Baltas** Ignoring thematic clusters in the covariance matrix biases risk estimates and misallocates risk; a theme-aware risk model (Lee) is better and applies beyond stocks to cross-asset trend portfolios.  #mech/research_method
  > account for those then our prediction of portfolio risk is biased downwards sorry it's biased upwards
  indicator: covariance matrix with thematic factors · asset: multi · conditions: Theme associations are short-lived · testable: yes · confidence: medium
  **Correction (cross-check):** The direction of the bias is omitted. Baltas says that if thematic clusters are ignored the predicted portfolio risk is biased (he says downwards, then corrects himself to upwards), concluding that the portfolio is riskier than the model suggests. Read with 'we're more risky than what we should have been', this means the risk model understates actual risk. → If thematic clusters are left out of the covariance matrix, the risk model understates the portfolio's true risk and misdistributes risk across positions (Baltas misspeaks on the direction but concludes the portfolio is riskier than reported); a theme-aware risk model (the Lee paper, tested on stocks) corrects this and the idea extends to cross-asset trend portfolios.
  ^MT174-C14-1
- **Nick Baltas** Narrative momentum: stocks exposed to rising narratives outperform those exposed to fading ones, a signal distinct from price momentum that could enhance allocation models.  #mech/slow_reaction
  > the stocks that happen to have higher exposure on naratives that are becoming more popular outperform those that have less exposure to narratives that are fading.
  indicator: narrative-exposure momentum · asset: equities · direction: long stocks exposed to rising narratives; short those tied to fading ones · horizon: months · conditions: Narratives rise, peak and fade over months · testable: yes · confidence: medium
  ^MT174-C14-2
- **Nick Baltas** Theme-driven clusters are transient, so a covariance matrix that captures them has to be updated dynamically to reflect how risk is distributed tomorrow, not just historical correlations.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > thematic association is short-lived
  indicator: dynamic covariance estimation with thematic factors · asset: multi · horizon: months · conditions: Applies to cross-asset trend portfolios as well as stocks · testable: yes - compare static versus theme-aware covariance forecasts · confidence: medium
  ^MT174-C14-X1
- **Nick Baltas** Narratives have a life cycle (rise, peak, fade) rather than appearing and vanishing overnight, so an asset's exposure to a rising narrative is persistent enough to be measured as a beta and to predict returns over the short term.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check)_
  > They come they stay and they fade and through that cycle of popularity picking up at some point hitting the peak and then starts dropping
  indicator: narrative popularity trend; asset beta to narrative strength · asset: equities · direction: long exposure to rising narratives, short fading ones · horizon: months · conditions: Needs point-in-time narrative data · testable: yes - narrative momentum paper provides a framework · confidence: medium
  ^MT174-C14-X2
- **Nick Baltas** Narrative or fundamental demand precedes price momentum: an underlying engine creates excess demand before the price trend appears, so narrative exposure could be an earlier signal than price. Economic-trend models likewise treat the underlying trend as latent and use several proxies (past price path, economic regime, thematic exposure).  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > there is a reason why price momentum exists. So if you go a few months back before price momentum was there there is an underlying engine that is creating excess demand
  indicator: narrative exposure as a lead signal for price momentum · asset: multi · direction: narrative strength leads price trend · horizon: months · conditions: Speculative mechanism; lead-lag has to be tested · testable: yes - lead-lag between narrative exposure and subsequent price momentum · confidence: medium
  ^MT174-C14-X3

### C15
- **Nick Baltas** The narrative-momentum paper builds point-in-time data from 13.3 million articles since about 2013 into 347 narratives, with robustness checks on narrative definitions.  #mech/research_method
  > they take the 13.3 million articles and they they and they structure that into 347 narratives.
  indicator: text-based narrative index · asset: equities · testable: yes · confidence: high
  ^MT174-C15-1
- **Niels Kaastrup-Larsen** Price data is objective and recorded for decades, which makes trend research easy to test; thematic strategies lack an equivalent, since themes appear and vanish and it is unclear what the underlying data is or how to back-test them without look-ahead.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > the beauty about price is that it's uh it's objective. It's recorded.
  asset: multi · conditions: Baltas answers with point-in-time article data and evergreen topics (see C15-1, C16-1) · testable: no - statement about research data quality · confidence: high
  ^MT174-C15-X1

### C16
- **Nick Baltas** Look-ahead in narrative backtests is analogous to the factor zoo; using 30-60 evergreen topics (trade wars, stagflation, capex) reduces the problem since new themes correlate with them.  #mech/research_method
  > We can make the argument that narratives are also correlated.
  indicator: evergreen narrative set · asset: equities · testable: yes · confidence: medium
  ^MT174-C16-1
- **Niels Kaastrup-Larsen** Sceptical view: simple sector grouping captures most of the clustering that thematic work tries to model, and thematic investing may partly be a way for Wall Street to get investors excited, since energy or healthcare companies already react similarly.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > you're not going to be completely wrong by putting healthare companies together and just say yeah this is healthare
  indicator: sector classifications versus thematic baskets · asset: equities · conditions: Baltas replies that themes add information when they cut across sectors (for example memory chips within the AI theme) · testable: yes - compare risk models with and without thematic factors beyond sectors · confidence: low
  ^MT174-C16-X1

### C17
- **Nick Baltas** Themes help discretionary investors reduce dimensionality because attention is limited.  #mech/behavioral
  > and there is too much dimensionality.
  asset: multi · testable: no · confidence: medium
  ^MT174-C17-1
- **Nick Baltas** The price path is not necessarily the best predictor of the underlying signal, only the most observable and validated one; the macro regime, the price path and thematics are different transformations of the same underlying signal (denoising the truth), and in a prolonged growth regime they all point the same way (buy equities) and correlate.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > itself is not necessarily the best predictor but it's an easily observable easily calculated and empirically validated
  indicator: price trend versus macro regime versus thematic exposure as signals · asset: multi · horizon: months · conditions: Signals agree in a prolonged growth regime and diverge at turning points · testable: yes - compare signal combinations out of sample · confidence: medium
  ^MT174-C17-X1

