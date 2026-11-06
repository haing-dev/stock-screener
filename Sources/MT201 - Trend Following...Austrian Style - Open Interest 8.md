---
source_id: MT201
title: "Trend Following...Austrian Style - Open Interest 8"
date: 2024-06-23
channel: "Top Traders Unplugged"
url: 
words: 7451
claims: 41
added_by_crosscheck: 7
corrections: 1
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Michael nobow (SMN co-founder, Vienna CTA)", "Joseph valin (SMN head of quant research and risk)", "Moritz seibert (host)"]
tags: [source, layer0]
---
# Trend Following...Austrian Style - Open Interest 8

**Speakers:** Michael nobow (SMN co-founder, Vienna CTA); Joseph valin (SMN head of quant research and risk); Moritz seibert (host)

**Summary:** Austrian CTA SMN (27-year track record) describes agnostic medium/long-term trend following over 200 markets incl. exotic and synthetic ones. Dispersion among CTAs comes from universe and position sizing more than signals. Conclusion: stay symmetric long/short, avoid overfitting, diversify into low-liquidity markets after realistic costs.

**Approach:** trend following, diversification, market universe, risk management, CTA

**Cross-check completeness estimate of first read:** 0.90 - the first reader caught nearly every method and mechanism claim; only the robustness rationale for choosing trend following, the capacity argument, the sector/single-name equity idea and the volatility-is-non-directional rationale were missed.

## Argument map

**Episode thesis:** SMN's founders argue trend following needs no forecast, only a broad portfolio that will contain large outliers, so they keep equal long and short risk (to keep crisis alpha), avoid overfitting, and widen the universe to over 200 markets, including synthetic and illiquid alternative markets that correlate little with classic futures. They manage risk with an average volatility target plus per-position budgets, execute illiquid markets with algorithms, and see no arbitrage of outliers after the zero-rate lost decade.

### Michael Nobow (Co-founder of SMN (the N in SMN), Vienna systematic CTA since 1997; ex-Austrian bank derivatives trader)
Fingerprint: #approach/trend_following #approach/diversification_risk_parity #approach/research_robustness_overfitting #approach/crisis_alpha_convexity #approach/manager_selection_allocation
_Speaker note: Caption spelling 'Michael nobow'; three-speaker conversation (host plus two guests), speakers separable by who answers. Statements about performance are firm self-reports._

**Worldview premises**
- Trend following needs no forecast; the single assumption is that a broadly diversified portfolio will contain large trend outliers over time. _[theoretical, stated; support: Core philosophy after 27 years; no formal proof.]_ ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C01-1|C01-1]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C11-2|C11-2]])
- The location of the next outlier cannot be predicted from history (cocoa, historically negative-return, was the best CTA market in 2024), so tilting signals to what worked is overfitting. _[empirical, stated; support: Cocoa 2024 example.]_ ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C05-3|C05-3]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C05-4|C05-4]])
- Short signals in equities and bonds are needed for crisis alpha; removing them would improve a backtest over 30 years of bull markets but destroy crisis protection. _[theoretical, stated; support: Reasoning about backtest vs crisis alpha.]_ ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C05-5|C05-5]])
- More markets means more chances to catch outliers; market diversification is in SMN's DNA. _[experience, stated; support: Started with about 70 markets in 1996 and kept widening.]_ ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-1|C07-1]])
- Synthetic markets (baskets or spreads) create return streams that differ from the underlying and add diversification. _[theoretical, stated; support: Idea that a combination curve differs from its two inputs.]_ ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-2|C07-2]])
- Alternative (illiquid, regional) markets move on local factors, not on the global risk-on/risk-off regime, so correlate little with a classic futures portfolio. _[empirical, stated; support: SMN research since 2011.]_ ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-6|C07-6]])
- Alpha in small markets is capacity-limited: multi-billion funds cannot use them, so only a mid-sized CTA can make them a real return source. _[theoretical, stated; support: Logic of size.]_ ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-X1|C07-X1]])
- Allocators prefer the biggest CTA shops because of career risk, and flow chases performance: after drawdowns they say trend following does not work, after good years they add. _[behavioural, stated; support: Observed for 30 years; 2008 crisis redemptions despite crisis alpha.]_ ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-5|C07-5]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-4|C07-4]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C10-4|C10-4]])
- Medium and long-term trend following is the most robust horizon; short-term systems were dropped around 2007-08. _[experience, stated; support: Own testing for ten years.]_ ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-3|C07-3]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C03-X1|C03-X1]])
- Trend following cannot be arbitraged away because outliers have causes beyond CTA trading, though more noise may create more false signals; the 2009-2020 lost decade was artificial (zero rates, QE) and long quiet periods are followed by bigger moves. _[theoretical, stated; support: Reasoning from policy regime; 'as we see now'.]_ ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C11-1|C11-1]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C11-2|C11-2]])
- A style shift in a live track record should never be done, so new ideas such as discretionary overlays are tested only in a side fund; the discretionary-plus-systematic mix failed. _[experience, stated; support: SMN's own side-fund experiment.]_ ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C04-1|C04-1]])

**Chain: Why diversification beats forecasting**
1. No forecast of direction, timing or location of outliers → Broad portfolio so some outliers are caught: Only assumption: outliers exist ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C01-1|C01-1]])
2. More markets and non-classic markets → More chances to catch outliers, lower correlation: Local factors and different timing ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-1|C07-1]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-6|C07-6]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C08-4|C08-4]])
3. Unpredictable location (cocoa) → Symmetric long and short signals, equal risk in every market: Anything else is overfitting ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C05-3|C05-3]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C05-4|C05-4]])
- Evidence: Cocoa 2024; 27-year track record.
- Fails when: Fails if there are no outliers (2009-2020 lost decade), as he admits.

**Chain: Smaller size and alternative markets**
1. 2008 crisis alpha did not bring new assets → Allocators choose the biggest shops because of career risk: Liquid CTAs were redeemed in a crisis ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-4|C07-4]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-5|C07-5]])
2. Cannot compete on size → Differentiate via alternative markets large funds cannot trade: Capacity of small markets is limited ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-5|C07-5]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-X1|C07-X1]])
3. Local-factor markets → Low correlation and higher Sharpe after costs: Cycle-driven pricing and different timing of trends ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-6|C07-6]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C08-2|C08-2]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C08-3|C08-3]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C08-4|C08-4]])
- Evidence: Project started 2011, implemented 2014; Sharpe 'significantly' higher after stringent costs.
- Fails when: Not stated: capacity limits if the firm grows.

**Chain: Quiet periods precede large moves**
1. Zero rates, QE and money printing → Few outliers in 2009-2020: Artificial regime ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C11-2|C11-2]])
2. Long period without substantial moves → Bigger-than-average moves after: Markets are prepared for bigger moves ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C11-2|C11-2]])
- Evidence: Claims it is visible now (2024).
- Fails when: Not stated.

**Decision process**
- [signal] Medium to long-term trend following only; no short-term systems since 2007-08.. Why: Most robust horizon. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-3|C07-3]])
- [signal] Equal risk on long and short signals in every market; no tilt to past winners.. Why: Avoid overfitting; keeps crisis alpha. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C05-3|C05-3]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C05-5|C05-5]])
- [universe] Widen the universe continuously: about 70 markets at the start, then synthetics (2009), alternative markets (2014).. Why: More markets, more outliers. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-1|C07-1]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-2|C07-2]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-R1|C07-R1]])
- [universe] Entry of equal-weighted vs cap-weighted stock index spreads or sector/single-name trend markets considered but not done (derivatives counterparty risk, prospectus).. Why: More diversification potential. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C09-4|C09-4]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C09-X1|C09-X1]])
- [research] Test new ideas in a side fund, never change the flagship style.. Why: Preserve a consistent track record. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C04-1|C04-1]])
- [research] Originally chose trend following because it was the most robust concept; Turtles and local CTAs as motivation.. Why: Robustness. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C03-X1|C03-X1]])

**Evidence style:** Long track record (27 years), experience, logic about robustness; no data shown.

**Views at the time**
- (2024-06-23) Trend following is unlikely to be arbitraged away; the lost decade was artificial and a return of larger moves is now visible.. Reasoning: Outliers have causes other than CTA trading; quiet periods precede big moves. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C11-1|C11-1]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C11-2|C11-2]])
- (2024-06-23) An equal-weighted vs cap-weighted stock index spread could provide a trend market, with an eventual large outlier in the other direction after the Magnificent Seven run.. Reasoning: The run cannot go on forever. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C09-4|C09-4]])
- (2024-06-23) Cocoa was the best CTA market in 2024 despite a negative history.. Reasoning: Outlier location unpredictable. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C05-4|C05-4]])

### Joseph Valin (Head of quantitative research and risk management at SMN (joined 2006))
Fingerprint: #approach/trend_following #approach/position_sizing_vol_target #approach/research_robustness_overfitting #approach/costs_execution #approach/volatility_options #approach/portfolio_construction_stacking
_Speaker note: Caption 'Joseph valin'; background in business administration and discretionary trading with quantitative support._

**Worldview premises**
- Dispersion among trend-following CTAs is explained more by market universe and position-sizing logic than by signal design, though biased signals (long bias in bonds and equities) add dispersion. _[empirical, stated; support: Discussed on a prep call; no data.]_ ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C04-2|C04-2]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C04-3|C04-3]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C05-1|C05-1]])
- Over-optimisation of the past is the main research risk; backtests are judged by a standard set of rules for realism. _[experience, stated; support: SMN's research process.]_ ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C08-5|C08-5]])
- Alternative markets are cycle-driven by local supply and demand, with medium to long-term cycles trend systems capture well, at different times from classic markets. _[empirical, stated; support: Backtests with stringent costs.]_ ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C08-3|C08-3]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C08-4|C08-4]])
- Volatility is a non-directional asset class that needs its own signal design rather than the plain price-momentum rule. _[theoretical, stated; support: VIX behaviour in the lost decade.]_ ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C10-X1|C10-X1]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C10-1|C10-1]])
- Slippage in illiquid markets is hard to know ex ante, so high assumptions are used. _[experience, stated; support: Smallest markets about four to five times classic slippage.]_ ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C08-1|C08-1]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C08-6|C08-6]])

**Chain: Alternative markets pass a cost-stress test**
1. Slippage hard to know for illiquid markets → Use deliberately high slippage plus broker execution costs: Avoid overstating results ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C08-1|C08-1]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C08-6|C08-6]])
2. Stringent realism rules on backtests → Sharpe of whole portfolio still rises significantly: Local cycles and different timing ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C08-2|C08-2]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C08-5|C08-5]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C08-3|C08-3]])
- Evidence: Backtests with stress costs; milk and cheese ~4-5x slippage.
- Fails when: Real slippage may differ; as stated the number is from memory.

**Chain: VIX enhancement**
1. Pure momentum on VIX did poorly in the 2009-2019 lost decade → Enhanced model with price momentum, vol of vol and curve shape: Volatility is non-directional ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C10-1|C10-1]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C10-2|C10-2]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C10-X1|C10-X1]])
2. VIX can explode → Hourly curve snapshots with quick intraday exits: Speed of risk ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C10-3|C10-3]])
- Evidence: Research project that ended around 2020.
- Fails when: Not stated.

**Decision process**
- [sizing] Volatility target is an annualised standard deviation goal met on average over the long run; no re-levering on days with few signals.. Why: Positions come only from long/medium-term trend signals. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C06-1|C06-1]])
- [risk] Each position has a risk budget/stop limit to control drawdown, complementing the symmetric standard deviation target.. Why: Asymmetric drawdown control. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C06-2|C06-2]])
- [risk] After a huge price move in one market (cocoa) with the exit far below price, positions are cut; limits are broad so ordinary moves do not trigger cuts.. Why: Prevent one market from dominating. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C06-3|C06-3]])
- [execution] Trade illiquid markets with execution algos (TWAP-style) over a day or two with per-market instructions.. Why: Positions need more than one session. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C09-1|C09-1]])
- [portfolio] Synthetics: risk-parity baskets (S&P vs 10-year note, 2009) and correlation spreads between related commodities (NY vs London cocoa, wheat types, South African maize and soybeans); host cites 20-25% of risk.. Why: Create new return streams. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C09-2|C09-2]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C09-3|C09-3]])
- [research] Standard rules for evaluating whether a backtest is realistic.. Why: Over-optimisation. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C08-5|C08-5]])
- [signal] VIX via enhanced momentum (price momentum, vol of vol, curve shape), hourly monitoring.. Why: Volatility is non-directional. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C10-1|C10-1]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C10-2|C10-2]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C10-3|C10-3]])

**Evidence style:** Backtests with stress costs and realism rules; practical execution detail.

**Views at the time**
- (2024-06-23) Dispersion in trend following in 2023-24 is mainly universe and sizing, with some signal bias effect.. Reasoning: Prep-call analysis. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C04-2|C04-2]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C04-3|C04-3]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C05-1|C05-1]])

### Moritz Seibert (Host of the Open Interest series, Top Traders Unplugged)
Fingerprint: #approach/trend_following #approach/research_robustness_overfitting #approach/costs_execution
_Speaker note: Host; caption 'Moritz seibert'. Brings data points and challenges to the guests._

**Worldview premises**
- Over the last 30-40 years long trades in equity and bond trend following beat short trades, while currencies and commodities differ; this is a sample-specific effect of secular bull markets. _[empirical, stated; support: Own knowledge of CTA backtests.]_ ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C05-2|C05-2]])
- More markets are better for catching outliers (host puts it as a proposition and the guests agree). _[theoretical, implicit; support: Posed as a leading question.]_ ()
- Large CTAs have reach, so small CTAs differentiate by markets they cannot trade; the host is interested in how small markets are traded. _[experience, implicit; support: Interview framing.]_ ()

**Decision process**
- [other] Asks whether to bias signals long given 30-40 years of data.. Why: Test of the guests' philosophy. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C05-2|C05-2]])

**Evidence style:** Questions and anecdotes.

### Disagreements
- **Bias signals toward long in equities and bonds?**: Moritz Seibert: Notes long trades beat short trades over 30-40 years and asks if SMN would tilt signals. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C05-2|C05-2]]); Michael Nobow: No: equal risk in long and short; tilting to the past is overfitting and kills crisis alpha. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C05-3|C05-3]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C05-5|C05-5]]); Joseph Valin: Some CTAs do bias, and this is a source of dispersion. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C05-1|C05-1]])
- **Could trend following decay?**: Moritz Seibert: Asks whether returns are decaying or episodic; the strategy may be evergreen. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C11-1|C11-1]]); Michael Nobow: Cannot be arbitraged away, but more noise could mean more false signals. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C11-1|C11-1]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C10-4|C10-4]])

### Gaps and conflicts
- Correction applied: the 20-25% synthetic risk share was read by the host from a Hedge Fund Journal article; SMN did not confirm it. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C09-3|C09-3]])
- The claim that adding illiquid markets raises Sharpe 'significantly' after costs is stated with no figures; slippage multiple is from memory ('I don't have the number'). ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C08-2|C08-2]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C08-6|C08-6]])
- Michael's explanation of why synthetic markets add diversification rests on the idea that a combination curve looks different from its inputs, with no test shown. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-2|C07-2]])
- 2008 crisis alpha did not attract assets; the argument that small size is the only differentiator assumes allocator behaviour not shown. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-4|C07-4]], [[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C07-5|C07-5]])
- Statement that the lost decade was 'artificial' and that quiet periods precede big moves is asserted without evidence. ([[MT201 - Trend Following...Austrian Style - Open Interest 8#^MT201-C11-2|C11-2]])

### Forward-looking inputs (reader synthesis)
(reader) Inputs: none are used as forecasts; SMN says it is agnostic to direction. Observable input for the thesis is the presence of large outliers after long quiet periods and policy regimes (zero rates, QE) that suppress them (years); correlation of alternative markets vs classic (ongoing); allocator flows follow performance (annual).

### Reader inferences (not stated by the speakers)
- (reader) SMN's edge claim rests on capacity: the alternative-markets Sharpe uplift likely shrinks if the firm grows.
- (reader) 'No forecast, symmetrical signals' is a robustness choice that pays in crisis at the cost of some backtest return.
- (reader) The 20-25% synthetic share quoted by the host is unconfirmed, so risk allocation to synthetics is uncertain.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro, outliers assumption |
| C02 | 0 | background, SMN origin story, no method content |
| C03 | 0 | origin of firm, hybrid discretion experiment mention |
| C04 | 3 | discretion experiment failed, sources of dispersion |
| C05 | 5 | biased signals, symmetric long/short, risk definition start |
| C06 | 3 | risk targeting, risk budgets, universe |
| C07 | 6 | diversification, synthetics, alternative markets rationale |
| C08 | 6 | research of illiquid markets, slippage, alpha |
| C09 | 4 | execution algos, synthetic markets, equity ideas |
| C10 | 4 | VIX handling, future of trend following |
| C11 | 2 | outliers cannot be arbitraged, lost decade, close |

## Claims

### C01
- **Michael nobow** Trend following needs no forecast; it only assumes that a broad portfolio will contain some large trend outliers over time, so direction and timing of the next one need not be known.  #mech/cycle_persistence
  > there's only one assumption behind the concepts and this assumption is a broadly Diversified portfolio will have a certain amount of train outliers over time
  asset: multi · direction: long/short follow trend · horizon: years · conditions: needs broad market diversification · testable: partly - outlier frequency can be measured but is the assumption itself · confidence: high
  ^MT201-C01-1
- **Moritz Seibert** Host states SMN today trades over 200 markets and 300 instruments, a very broad universe including alternative and synthetic markets.  #mech/new _(added by map cross-check, time-bound view)_
  > today they trade more than 200 markets and more than 300 instruments
  asset: multi · conditions: broad universe · testable: yes · confidence: high
  ^MT201-C01-R1

### C03
- **Michael nobow** SMN chose trend following (after testing technical indicators on the bank desk) because it was the concept it found most robust, with the Turtles' and local CTAs' success as extra motivation.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > it was the the concept that we where we found the highest robustness
  indicator: trend following robustness · asset: multi · direction: trend following over other technical approaches · testable: no - biographical rationale, not independently testable · confidence: medium
  ^MT201-C03-X1

### C04
- **Michael nobow** Adding discretionary overlays was tested only in a side fund, never in the flagship, because changing style in a live track record is to be avoided; the discretionary plus systematic mix failed.  #mech/research_method
  > this would have been a style shift and this is something you should never do
  asset: multi · testable: no - governance statement · confidence: high
  ^MT201-C04-1
- **Joseph valin** Dispersion among trend-following CTAs is explained more by market universe and position-sizing logic than by signal design.  #mech/research_method
  > the Universe and the position sizing logic they have more weight in differentiation than the third
  indicator: CTA return dispersion · asset: multi · testable: partly - could be tested with CTA fund data · confidence: medium
  ^MT201-C04-2
- **Joseph valin** Position sizing choices that differ across managers include constant versus flexible risk targeting and whether sizing uses only signal direction or the signal value.  #mech/risk_management
  > constant versus flexible risk targeting is one big issue
  asset: multi · testable: yes - alternative sizing rules can be backtested · confidence: high
  ^MT201-C04-3
- **Joseph Valin** Joseph says the 2006 SMN experiment combining trend signals with human discretion in a partner-money fund failed, and the firm went back to systematic only.  #mech/research_method _(added by map cross-check)_
  > the experiment failed to be honest
  asset: multi · direction: discretionary overlay did not add · conditions: discretionary plus systematic mix · testable: no - no figures given · confidence: high
  ^MT201-C04-R1

### C05
- **Joseph valin** Some CTAs bias signals toward long positions in bonds and equities, which is another source of dispersion in trend following results.  #mech/research_method
  > giving more weight to long where the short signals for instance in the fixed income world or in the equity world
  asset: multi · testable: yes - long-only versus symmetric tilt can be backtested · confidence: high
  ^MT201-C05-1
- **Moritz seibert** Over the last 30-40 years long trades in equity and bond trend following beat short trades, while currencies and commodities show a different pattern; this is a sample-specific effect of secular bull markets.  #mech/structural_shift _(time-bound view)_
  > the long- sided trades and equities and bonds have been performing so much better than the shortsighted trades
  asset: multi · direction: long equities and bonds outperformed short · horizon: years · testable: yes - split trend returns by long and short side · confidence: medium
  ^MT201-C05-2
- **Michael nobow** Tilting signals to what worked in the past (for example removing short signals) is overfitting; SMN keeps equal risk on long and short signals in every market.  #mech/research_method
  > we try not to over optimize and and and this this is really dangerous because what works in the past probably doesn't work in the future
  asset: multi · direction: symmetric long/short · testable: partly - cannot prove out of sample absence of change · confidence: high
  ^MT201-C05-3
- **Michael nobow** Cocoa, historically a negative-return trend market, was the best CTA market in 2024, showing that the location of the next outlier cannot be predicted from history.  #mech/cycle_persistence _(time-bound view)_
  > this year the best Market in a uh CTA portfolio was uh the market Coco this is a market that was produced more or less always negative returns over time
  indicator: cocoa trend return · asset: commodities · horizon: years · testable: partly - single anecdote · confidence: high
  ^MT201-C05-4
- **Michael nobow** Removing short signals would improve a backtest during 30 years of bull markets in bonds and equities but would destroy the crisis alpha that trend following is expected to deliver.  #mech/risk_management
  > one of the characteristics of of ctas is that they are able to produce the the crisis alha
  asset: multi · direction: keep shorts in equities and bonds · conditions: crisis periods · testable: yes - compare long-only and long/short trend in drawdowns · confidence: high
  ^MT201-C05-5

### C06
- **Joseph valin** Volatility target is an annualised standard deviation goal met on average over the long run; the portfolio is not re-levered on days with few signals.  #mech/risk_management
  > we do not Target the overall um risk goal in terms of an deviation goal on a daily basis just on average long-term Bas
  indicator: annualised standard deviation target · asset: multi · direction: no re-levering when few signals · horizon: years · testable: yes - compare constant versus flexible risk targeting · confidence: high
  ^MT201-C06-1
- **Joseph valin** Each position has a risk budget or stop limit to control drawdown, complementing the symmetric standard deviation target with an asymmetric drawdown control.  #mech/risk_management
  > we have assigned stop loss limits for each or risk budgets for each position we're trading for each signal we are trading
  indicator: per-position risk budget · asset: multi · testable: yes - position-level stop rule can be backtested · confidence: high
  ^MT201-C06-2
- **Joseph valin** When a market makes a huge move (cocoa) and the exit level lags far below price, positions are cut so one market does not dominate; limits are deliberately broad so ordinary moves do not trigger cuts.  #mech/risk_management
  > the systems react on these developments by U reducing position uh the position size in case of a huge development in in individual price development
  indicator: distance from price to exit level, price volatility · asset: commodities · conditions: only after very large individual price moves · testable: yes - rule can be backtested · confidence: high
  ^MT201-C06-3

### C07
- **Michael nobow** More markets give more chances to catch outlier moves, so SMN began with about 70 markets and kept widening the universe.  #mech/risk_management
  > from the very beginning it was very important for us to diversify the risk by markets
  asset: multi · direction: more markets · testable: yes - breadth versus Sharpe in backtests · confidence: high
  ^MT201-C07-1
- **Michael nobow** Synthetic markets built as baskets or spreads of existing markets create return streams that look different from the underlying and add diversification.  #mech/risk_management
  > if we can produce a curve with uh two that looks different with two other curves then we would get more diversification
  asset: multi · testable: yes - build spreads and measure incremental diversification · confidence: high
  ^MT201-C07-2
- **Michael nobow** SMN dropped short-term systems around 2007-08 and concentrated on medium/long-term trend following as the most robust horizon.  #mech/research_method
  > only concentrate on medium to long term because we thought this is the this is the uh the thing that is most robust over time
  asset: multi · horizon: months · testable: partly - robustness is judgement · confidence: medium
  ^MT201-C07-3
- **Michael nobow** In the 2008 crisis CTAs did well but investors redeemed from them because CTAs were liquid, so crisis alpha did not bring new assets.  #mech/liquidity_flows _(time-bound view)_
  > investors because of the liquidity of CTS uh took out money because they needed it as well
  asset: multi · testable: no - anecdote · confidence: high
  ^MT201-C07-4
- **Michael nobow** Allocators prefer the biggest CTA shops because of career risk, so small firms can differentiate only by trading markets large funds cannot.  #mech/behavioral
  > the career risk for them when they lose money with them is lower
  asset: multi · testable: no - industry structure view · confidence: medium
  ^MT201-C07-5
- **Michael nobow** Alternative (illiquid, regional) markets move on local factors rather than the global risk-on/risk-off regime, so they correlate little with a classic futures portfolio.  #mech/risk_management
  > it's not this typical risk on riskof regime that you have with most of the high highest liquid financial and commodity markets they have their own moves and they don't correlate too much to the rest of the portfolio
  indicator: correlation of alternative markets with classic portfolio · asset: commodities · testable: yes - correlation and Sharpe contribution measurable · confidence: high
  ^MT201-C07-6
- **Michael nobow** Alpha in small alternative markets is capacity-limited: a multi-billion fund can trade them but the allocation is too small to move performance, so only a mid-sized CTA like SMN can use them as a real source of return.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > you can say you trade those markets but uh it doesn't have an effect on the outcome of the portfolio of performance wise
  indicator: fund size vs market liquidity · asset: commodities · direction: alternative markets add return mainly for smaller funds · horizon: years · conditions: needs assets small relative to market liquidity · testable: partly - capacity versus return analysis needs fund-level data · confidence: medium
  ^MT201-C07-X1
- **Michael Nobow** The alternative-markets project began around 2011 after the financial crisis and was implemented in 2014, a multi-year research step before live trading.  #mech/research_method _(added by map cross-check, time-bound view)_
  > we started with this project I think 2011 but we implemented it in 2014
  asset: commodities · horizon: years · conditions: alternative markets research · testable: yes - dates observable · confidence: medium
  ^MT201-C07-R1

### C08
- **Joseph valin** Backtests of illiquid markets use deliberately high slippage assumptions, plus broker execution costs, to avoid overstating results.  #mech/research_method
  > we came up with really huge reasonable but still obviously much more higher slippage numbers incorporating our P testing
  asset: multi · conditions: slippage hard to know ex ante for illiquid markets · testable: yes - cost stress in backtests · confidence: high
  ^MT201-C08-1
- **Joseph valin** After stringent cost assumptions, adding less liquid markets still raises the portfolio Sharpe ratio significantly.  #mech/structural_shift
  > even after accounting for this High number of slippage and transaction costs explicit and implicit transaction cost there is sizable Alpha to capture
  indicator: portfolio Sharpe ratio with and without alternative markets · asset: commodities · testable: yes - incremental Sharpe test with cost stress · confidence: high
  ^MT201-C08-2
- **Joseph valin** Local commodity markets driven by local supply and demand show medium to long-term price cycles that trend systems capture well.  #mech/cycle_persistence
  > the pricing behavior in these less liquid markets is more cycle driven driven because in our case predominantly but not only but PR predominantly commodity markets local commodity markets more driven by local demand and Supply
  asset: commodities · horizon: months · testable: yes - trend profitability by market type · confidence: high
  ^MT201-C08-3
- **Joseph valin** Trends in alternative markets occur at different times from classic-market trends, lowering correlation and improving diversification.  #mech/risk_management
  > these Trends do not happen at the same time than with our classic universe meaning decreasing correlation and increasing diversification
  asset: commodities · testable: yes - correlation of trend returns · confidence: high
  ^MT201-C08-4
- **Joseph valin** SMN has standard rules to judge whether a backtest result is realistic because over-optimisation of the past is the main research risk.  #mech/research_method
  > the biggest enemy in researching is that the over optimization of the past
  asset: multi · testable: partly - rules not stated · confidence: high
  ^MT201-C08-5
- **Joseph valin** Slippage assumed for the smallest markets (nonfat dry milk, cheese) is roughly four to five times that of classic futures.  #mech/risk_management
  > I would assume right now it's really I think uh four to five times larger than the the classical ones
  indicator: assumed slippage multiple · asset: commodities · testable: partly - estimate stated from memory · confidence: low
  ^MT201-C08-6

### C09
- **Joseph valin** Tiny illiquid markets are traded with execution algorithms (TWAP or similar) over a day or two to spread liquidity, with instructions per market.  #mech/liquidity_flows
  > so in these markets we U decided to trade them with with Algos together with our Brokers
  asset: multi · conditions: illiquid markets, positions need more than one session · testable: no - execution practice · confidence: high
  ^MT201-C09-1
- **Joseph valin** The first synthetic markets (2009) were risk-parity baskets of an equity index and a government bond, for example S&P versus 10-year note.  #mech/risk_management
  > risk parity baskets it's a it's basically a combination between an equity
  indicator: equity/bond risk parity basket · asset: multi · testable: yes - basket trend backtest · confidence: high
  ^MT201-C09-2
- **Joseph valin** Correlation spreads between related commodities (New York versus London cocoa, wheat types) are traded as synthetic markets with their own trends; synthetics are roughly 20-25% of risk.  #mech/risk_management
  > a correlation spread we where we trade um two related Commodities like Coco versus London cocoa or different wheat wheat types
  indicator: spread of related commodity contracts · asset: commodities · testable: yes - spread trend backtest · confidence: high
  **Correction (cross-check):** The 20-25% of risk figure for synthetic markets was read out by the host (Moritz, citing a Hedge Fund Journal article), not stated by Joseph; SMN did not confirm the number. → Correlation spreads between related commodities (New York versus London cocoa, wheat types, South African maize and soybeans) are traded as synthetic markets with their own trends; the host cites an article putting synthetics at about 20-25% of SMN's risk budget.
  ^MT201-C09-3
- **Michael nobow** An equal-weighted versus cap-weighted stock index spread could provide a trend market, with an eventual trend outlier in the other direction after the Magnificent Seven run.  #mech/overshoot _(time-bound view)_
  > you could for example make a spread out of uh an equally uh weighted stock index versus uh volume weighted uh stock index
  indicator: equal-weighted minus cap-weighted index · asset: equities · direction: trend either way · horizon: months · testable: yes - spread trend backtest · confidence: low
  ^MT201-C09-4
- **Michael nobow** Breaking equity index futures into sectors or single names would add diversification to a trend portfolio, but SMN has not done it because it would need derivatives (counterparty risk) or a change of the fund prospectus.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > I think there would be a lot of possibilities for higher diversification as well in in our fund
  indicator: sector and single-stock trends · asset: equities · direction: more diversification from sector/single-name trend markets · conditions: fund prospectus and counterparty constraints · testable: partly - needs stock-level data, not tested in the talk · confidence: medium
  ^MT201-C09-X1

### C10
- **Joseph valin** Pure momentum on the VIX behaved poorly in the 2009-2019 lost decade, so SMN built an enhanced momentum model.  #mech/research_method
  > the behavior of the especially asset class volatility in our case you Equity volatility the behavior was not the most optimal one for the way we traded the other markets
  indicator: VIX futures momentum · asset: equities · testable: yes - compare pure and enhanced VIX momentum · confidence: high
  ^MT201-C10-1
- **Joseph valin** Enhanced VIX momentum uses price momentum, the volatility of volatility and the shape of the futures curve (spot versus future volatility).  #mech/slow_reaction
  > we take into account next to the price movement of volatility so the volatility of volatility actually also the shape of future and expected the the uh state of spot and future volatility
  indicator: VIX futures price, vol of vol, term-structure shape · asset: equities · testable: yes - rule can be replicated · confidence: high
  ^MT201-C10-2
- **Joseph valin** VIX positions are monitored on hourly snapshots of the curve with quick intraday exits because volatility can explode.  #mech/risk_management
  > we're moved to basically hourly hourly ticks in order to evaluate the the structure of the the current structure of the volatility
  indicator: VIX futures curve, hourly · asset: equities · horizon: days · testable: yes - needs intraday data · confidence: high
  ^MT201-C10-3
- **Michael nobow** Allocator interest in CTAs follows recent performance: after drawdowns investors say trend following no longer works, after good years they add, a pattern unchanged for 30 years.  #mech/behavioral
  > when you have uh a couple of good years then investors think probably it's a good idea to have a small proportionate portfolios with CTS as well
  asset: multi · testable: partly - flows versus performance data · confidence: medium
  ^MT201-C10-4
- **Joseph valin** Volatility is a non-directional asset class, so SMN argues it needs its own signal design rather than the plain price-momentum rule used for the directional markets.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > the ESS class volatility is really different to all the other more directional ESS classes
  indicator: VIX futures · asset: multi · conditions: VIX trend rule differs from rest of portfolio · testable: partly - compare pure vs enhanced momentum on VIX · confidence: medium
  ^MT201-C10-X1

### C11
- **Michael nobow** Trend following is unlikely to be arbitraged away because large outliers have causes other than CTA trading, though more noise could create more false signals.  #mech/structural_shift
  > arbitraging away this big outliers is impossible because there are other reasons for this then CTA trades
  asset: multi · horizon: years · testable: no - future-looking claim · confidence: medium
  ^MT201-C11-1
- **Michael nobow** The 2009-2020 lost decade (zero rates, QE) had few outliers, was artificial, and long quiet periods are followed by bigger-than-average moves, as seen now.  #mech/policy_reaction _(time-bound view)_
  > if it takes for a long time if the markets have for a long time no substantial moves then they are prepared having even bigger moves than uh on average after this period
  asset: multi · horizon: years · conditions: after long low-volatility periods · testable: partly - few historical episodes · confidence: medium
  ^MT201-C11-2

