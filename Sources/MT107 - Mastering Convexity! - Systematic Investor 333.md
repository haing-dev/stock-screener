---
source_id: MT107
title: "Mastering Convexity! - Systematic Investor 333"
date: 2025-02-09
channel: "Top Traders Unplugged"
url: 
words: 11478
claims: 60
added_by_crosscheck: 8
corrections: 1
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Richard Brennan (trend follower, East Coast Capital Management)", "Niels Kaastrup-Larsen (host, Dunn Capital)"]
tags: [source, layer0]
---
# Mastering Convexity! - Systematic Investor 333

**Speakers:** Richard Brennan (trend follower, East Coast Capital Management); Niels Kaastrup-Larsen (host, Dunn Capital)

**Summary:** Brennan presents convexity (Dave Dredge) as the core of trend following: Sharpe-world risk measures are flawed; small losses, anti-martingale pyramiding, and wide diversification harvest outliers. Kaastrup adds January 2025 dispersion data and cautions on open equity.

**Approach:** trend following, convexity, tail risk, position sizing, risk management

**Cross-check completeness estimate of first read:** 0.88 - first reader captured nearly all of Rich's convexity argument and Niels' data and interjections; missed the Niels/Asness risk-definition pushback, Rich's reply on closed-equity AUM and long-haul philosophy, option-hedge precision, linearity assumption, infinite yield and diversification-as-safety-net, and merged two speakers in the open-equity claim.

## Argument map

**Episode thesis:** Richard Brennan, drawing on Dave Dredge's 'Sharpe world' critique, argues that markets are non-linear (long muted regimes interrupted by explosive moves), so risk is the unforeseen, not historical volatility, and portfolios should be built for convexity: small, linear losses on one side of a barbell and amplified gains on the other, with brakes (stops, small bet sizes) that let a strategy accelerate in favorable regimes. Trend following is presented as convexity for opportunity capture as well as protection (anti-martingale scaling into outliers, wide diversification to find them, 'infinite yield' from one trend paying for many small losses), contrasted with concave mean-reversion and negative-skew strategies (LTCM) and with options-based tail protection. The host Niels adds the horizon-dependence of convexity, a counter on defining risk as permanent loss, the open-equity problem for new investors, and the view that a more divergent world with uncoordinated central banks favors trend.

### Richard Brennan (Guest; trend follower, East Coast Capital Management (Australia); self-described 'outlier hunter')
Fingerprint: #approach/trend_following #approach/crisis_alpha_convexity #approach/position_sizing_vol_target #approach/kelly_or_conviction_sizing #approach/diversification_risk_parity #approach/regime_detection #approach/research_robustness_overfitting #approach/volatility_options
_Speaker note: Referred to as Rich by the host; the ledger gives 'Richard Brennan'. Most of the episode is a prepared monologue inspired by Dave Dredge (tail-protection manager, quoted along with Taleb), whose ideas Rich adopts; claims quoting Dredge or Taleb are Rich's reported adoption of them. Caption quirks: 'sharp' for Sharpe, 'bit sizes' for bet sizes, 'night tram' for anti-martingale joke._

**Worldview premises**
- Markets are non-linear: long muted regimes alternate with explosive moves and large drawdowns, so an average-volatility description of risk is poor and risk must be managed by adapting to the current regime. _[empirical, stated; support: S&P 500 examples (5-year runs of 25%+, 50% GFC drawdown, 1987, 2002)]_ ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C04-1|C04-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C04-2|C04-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C05-X1|C05-X1]])
- Convexity is positive skew: amplify gains when volatility is favorable and cap losses with risk management; concave strategies (mean reversion, negative skew, pattern recognition) earn many small wins and then take sudden large losses when an unpredicted regime arrives. _[theoretical, stated; support: payoff-shape reasoning; LTCM example]_ ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C05-1|C05-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C05-2|C05-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C05-3|C05-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C08-1|C08-1]])
- Volatility is not all bad: adverse volatility should be limited but beneficial volatility exploited; smoothing funds only limit the adverse side and forgo upside, so the car with brakes beats the car optimised for average speed. _[theoretical, stated; support: Formula 1 analogy (Dredge)]_ ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C06-2|C06-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C06-3|C06-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C06-1|C06-1]])
- The most material market events arise from uncertainty absent from the historical sample, so using history to set expected returns blindsides investors; models trained on history collapse in unprecedented environments and a surviving backtest does not guarantee future survival. _[theoretical, stated; support: list of crises (1987, 2002, 2008, Asian crisis, LTCM, COVID)]_ ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C07-1|C07-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C08-3|C08-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C10-2|C10-2]])
- Smooth linear equity curves are temporary products of a predictable environment and later become concave; managers who lever up predictable returns blow up at regime shift. _[experience, stated; support: LTCM and mean-reversion examples]_ ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C07-3|C07-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C08-1|C08-1]])
- Traditional finance rests on five flawed assumptions: historical risk, normality, persistent correlations, estimable returns, and all volatility being bad; risk is a possibility distribution, not a probability distribution (Taleb). _[theoretical, stated; support: Dredge/Taleb quotations; list of crises]_ ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C11-1|C11-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C11-2|C11-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C10-2|C10-2]])
- Long calm periods raise fragility (avalanche, flood, forest-fire analogies), so low volatility is not safe, and VaR misses contagion because markets are connected complex adaptive systems. _[theoretical, stated; support: natural analogies, not data]_ ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C11-3|C11-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C11-4|C11-4]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C11-5|C11-5]])
- The 60/40 portfolio rested on a stock-bond correlation that was zero or negative and turned positive, leaving it with no brakes. _[empirical, stated; support: recent experience of positive correlation]_ ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C08-2|C08-2]])
- Risk is permanent loss of capital, not volatility; few trend followers ever blow up whereas mean-reversion strategies do, and no validated 20-30 year records exist for other styles. _[experience, stated; support: industry observation of blow-ups; absence of long records]_ ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C12-3|C12-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C12-4|C12-4]])
- Positive skew optimises long-term compounded wealth, and concave strategies with rare crippling losses create compounding drag. _[theoretical, stated; support: compounding arithmetic argument]_ ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C12-1|C12-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C12-2|C12-2]])
- Options are the most precise hedge for a traditional portfolio because they can be matched to a specific risk (market, correlation), whereas trend following offers less targeted, premium-free convexity, exposed to sudden short-term shocks and whipsaws. _[theoretical, stated; support: comparison of costs and design]_ ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-X2|C09-X2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-2|C09-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-3|C09-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C08-4|C08-4]])

**Chain: Why linear/concave strategies fail and convex ones compound**
1. predictable environment (mean reversion working, pattern recognition fitted, stock-bond correlation negative) → smooth linear equity curve of small wins: the strategy is optimised for a regime that persists temporarily ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C07-3|C07-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C08-1|C08-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C05-2|C05-2]])
2. apparent safety invites leverage → regime shift produces a catastrophic loss: high leverage or reliance on a correlation breaks when conditions change ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C08-1|C08-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C08-2|C08-2]])
3. rare crippling loss → compounding drag and lower long-run wealth: large losses require disproportionate gains to recover ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C12-2|C12-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C12-1|C12-1]])
4. convex process: small linear losses, uncapped gains → higher compounded wealth: positive skew shifts the distribution to the right ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C12-1|C12-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C07-2|C07-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C06-3|C06-3]])
- Evidence: LTCM, 60/40, F1 analogy; no data presented
- Fails when: short-term shocks hit medium-to-long-term trend models before positions change (whipsaws); reported decline in trend-follower skew is raised by the host.

**Chain: Why Sharpe, standard deviation and VaR mislead**
1. risk estimated from historical distributions → low volatility in the sample reads as low risk: VaR assumes calm periods reduce extreme-event risk ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C11-1|C11-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C11-3|C11-3]])
2. low volatility encourages leverage and complacency → fragility rises: stability breeds instability (avalanche, flood, forest fire) ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C11-3|C11-3]])
3. markets are connected adaptive systems → contagion makes losses larger than the trigger implies: VaR measures the tremor, not the catastrophe it can cause ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C11-4|C11-4]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C11-5|C11-5]])
4. unforeseen events (1987, 2002, 2008, COVID) keep recurring → volatility-based measures are flawed as risk definitions: crises came from events outside the sample ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C10-2|C10-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C12-3|C12-3]])
- Evidence: Crisis list; Dredge and Taleb as authorities
- Fails when: host counters that correlation-aware VaR, used properly, is a decent measure and better than Sharpe; also that 'permanent loss of all capital' is rare in any strategy so the definition is too narrow.

**Chain: How trend following embeds convexity: barbell, small bets, anti-martingale, diversification**
1. risk only a small fraction of closed-trade core capital per trade → losses are small and linear: small bet size is the ultimate stop, since stop orders can gap ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C13-5|C13-5]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C13-4|C13-4]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C16-1|C16-1]])
2. open profits let run; add to winners with an ensemble (anti-martingale) → positive convexity: one outlier pays for dozens of small losses: trends are material outliers whose location cannot be forecast ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C15-1|C15-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C15-4|C15-4]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C14-3|C14-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C15-X1|C15-X1]])
3. wide diversification across many markets → outliers are captured wherever they appear, with lower correlation and a larger opportunity set: cannot know in advance which market will have the next outlier ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C15-3|C15-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-4|C09-4]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C16-X1|C16-X1]])
4. survival by small bets → capital remains in play for compounding and for the next unknown opportunity: compounding needs time and skin in the game ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C16-2|C16-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C15-X1|C15-X1]])
- Evidence: Trend-following logic; judging on thousands of trades rather than individual results
- Fails when: trendless periods (stagnation and drawdowns), whipsaws, short-term shocks; martingale doubling is the concave opposite and fails catastrophically.

**Chain: Trend following versus options-based tail protection**
1. options give immediate protection and can be matched to the specific risk → they are the purest hedge for a traditional portfolio: design precision ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-X2|C09-X2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C08-4|C08-4]])
2. options cost premium and expire worthless; coverage limited to few markets → ongoing cost of insurance: paying for protection continuously ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-2|C09-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-4|C09-4]])
3. trend following has no explicit premium and covers many markets → convexity at no explicit cost plus opportunity capture, but exposed to short-term shocks: long/short models, wide coverage, medium-to-long horizon ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-2|C09-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-3|C09-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C04-3|C04-3]])
- Evidence: Cost and coverage comparison; trend followers are 'not a pure insurance programme'
- Fails when: short-term sell-offs where trend models cannot respond quickly enough.

**Decision process**
- [sizing] Risk each trade as a very small fraction of closed-trade core capital; let unrealised equity run, so the percentage of portfolio at risk is measured against core capital, not against open equity.. Why: Protects core capital while allowing a trade to explode in value. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C13-5|C13-5]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C13-4|C13-4]])
- [sizing] Take a small initial position when signals suggest a possible material outlier and add as it succeeds, applying an ensemble of models (anti-martingale); never double after losses (martingale).. Why: Anti-martingale is convex; martingale gives small gains but catastrophic risk. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C15-1|C15-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C15-2|C15-2]])
- [risk] Cut losses short with stops and small bet size as the ultimate stop; build brakes into the process rather than forecasting risk.. Why: Stop orders can gap in fast markets, whereas small size always bounds the loss. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C16-1|C16-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C06-1|C06-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C11-5|C11-5]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C13-4|C13-4]])
- [risk] Adapt risk to the current regime (accelerate in favorable regimes, brake in adverse ones) rather than assuming average volatility.. Why: Convex process responds dynamically to non-linear markets. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C04-2|C04-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C06-1|C06-1]])
- [universe] Trade a very wide range of markets, including unusual commodities, to find outliers wherever they appear.. Why: The location of the next outlier cannot be forecast. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C15-3|C15-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-4|C09-4]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C16-X1|C16-X1]])
- [signal] Ride winners until trends exhaust; one outlier (cocoa, an equity rally) pays for dozens of small losses; aim at 'infinite yield'.. Why: Open-ended payoff pays for the accumulated costs of small controlled losses. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C15-4|C15-4]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C14-3|C14-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C15-X1|C15-X1]])
- [research] Judge trend following on thousands of trades (the last 2,000 or 4,000), not on individual outcomes.. Why: Patience and long-horizon compounding. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C14-2|C14-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C14-X2|C14-X2]])
- [portfolio] For new capital, allocate AUM based on closed equity so that unrealised equity stays with existing investors; this is a business-of-trend-following adjustment rather than the philosophy itself.. Why: A new investor entering when open equity is large would face a drawdown that long-standing investors do not. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C14-X1|C14-X1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C14-X2|C14-X2]])

**Evidence style:** First principles, analogies (F1 car, avalanche, flood, forest fire, surfer, pilot, chef, casino martingale) and authority (Dredge, Taleb); little data; cites the existence of long trend-following records and the absence of comparable validated 20-30 year records for other styles as evidence of survival.

**Views at the time**
- (2025-02-01 (recorded February 1, 2025)) January 2025: his firm had a good month driven by commodities like coffee while the SG Trend Index fell, showing dispersion that comes from differing commodity exposure and model design.. Reasoning: Different trend followers hold different exposures and models. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C03-2|C03-2]])
- (2025-02-01) Markets are non-linear and risk comes from the unforeseen; convexity matters most now.. Reasoning: Long muted regimes followed by explosive moves; 60/40 correlation shift. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C04-1|C04-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C08-2|C08-2]])

### Niels Kaastrup-Larsen (Host, Top Traders Unplugged; veteran hedge fund manager (Dunn Capital))
Fingerprint: #approach/trend_following #approach/manager_selection_allocation #approach/behavioral_sentiment #approach/policy_reaction_central_banks #approach/crisis_alpha_convexity #approach/diversification_risk_parity
_Speaker note: Host; the ledger labels him 'host, Dunn Capital'. He states several own views and counter-points, so he is mapped. Claim C14-1 carries a correction: he only raised the new-investor open-equity risk; the closed-equity suggestion is Rich's reply (C14-X1)._

**Worldview premises**
- Divergent central bank policy (BOJ hiking, ECB cutting, Fed on hold) creates market divergence and manager dispersion that could suit trend models; a more divergent, less coordinated world favors trend. _[theoretical, stated; support: January 2025 observations; geopolitical anecdotes]_ ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C02-2|C02-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C16-3|C16-3]])
- Short-term models react to noise (the Nvidia drop of about $600bn reversed within days) that longer-term models ignore. _[experience, stated; support: one-week example]_ ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C02-1|C02-1]])
- Convexity depends on horizon: short-term managers and tail funds claim more of it, trend followers' skew has reportedly declined, and longer-term managers can argue that providing convexity daily costs too much bleed and does not matter for long-run results. _[theoretical, stated; support: recollection of a Quantica paper]_ ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-1|C09-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-X1|C09-X1]])
- A multi-asset portfolio with trend following cushions events nobody imagined; the question is what you are doing about what you are not worried about, and investors who think they are diversified often hold hidden short-volatility exposure. _[experience, stated; support: none beyond reasoning]_ ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C10-1|C10-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C16-3|C16-3]])
- Risk defined only as permanent loss of capital is too narrow, because complete loss is rare in any strategy and volatility can still feel like risk; long drawdowns hurt investor psychology more than deep short ones (Asness). _[behavioural, stated; support: Asness podcast heard in Miami]_ ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C12-X1|C12-X1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C13-1|C13-1]])
- The range and probability of extreme events is judged higher now; correlation-aware VaR, used properly, remains a decent risk measure and better than Sharpe. _[experience, stated; support: Alistair Williams podcast; personal experience with VaR]_ ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C13-2|C13-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C13-3|C13-3]])
- In funds whose open trade equity grew to 50-70% of NAV, new investors face a straight 50% drawdown that long-standing investors do not, so sizing on closed equity mainly suits one's own money with an infinite runway. _[institutional, stated; support: last year's observation of some managers]_ ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C14-1|C14-1]])

**Decision process**
- [research] Track a trend barometer (41 at end of January 2025, neutral) and monthly CTA indices (SG Trend, SG CTA, BTOP50, short-term traders, Bridge flat-fee trend).. Why: To gauge how trend following is performing; dispersion between indices is notable. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C03-3|C03-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C03-4|C03-4]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C03-1|C03-1]])

**Evidence style:** Anecdote, conferences and podcasts heard (Asness, Williams), index data, and his own experience.

**Views at the time**
- (2025-02-01 (data as of Thursday January 30)) January 2025 was a mixed month for trend: winners in equities after the election, German DAX, coffee, gold and live cattle; zinc was a drag; SG Trend -52bp, SG CTA +20bp, BTOP50 about +70bp, Bridge flat-fee -78bp; MSCI World +3.47%.. Reasoning: Observed index and market data. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C03-1|C03-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C03-3|C03-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C03-4|C03-4]])
- (2025-02-01) A divergent world (central banks acting independently, trade tensions) may favor trend strategies more now.. Reasoning: Divergence creates dispersion and trends. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C02-2|C02-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C16-3|C16-3]])

### Disagreements
- **Definition of risk**: Richard Brennan: Risk is permanent loss of capital, not volatility; trend followers rarely blow up. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C12-3|C12-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C12-4|C12-4]]); Niels Kaastrup-Larsen: Complete permanent loss is rare in any strategy, so he wants a definition between the two; volatility can still feel like risk. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C12-X1|C12-X1]])
- **Usefulness of VaR and similar measures**: Richard Brennan: Sharpe, standard deviation and VaR fail because crises come from unforeseen events; VaR misses contagion. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C10-2|C10-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C11-4|C11-4]]); Niels Kaastrup-Larsen: Correlation-aware VaR, used properly, is still a decent measure, better than Sharpe. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C13-3|C13-3]])
- **Sizing on closed versus open equity**: Richard Brennan: Risk a fraction of closed-trade core capital and let unrealised equity run; for outside money allocate new AUM using closed equity. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C13-5|C13-5]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C14-X1|C14-X1]]); Niels Kaastrup-Larsen: The principle suits one's own money; new investors in funds with large open equity face a straight 50% drawdown that others do not. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C14-1|C14-1]])
- **How much convexity trend following offers**: Richard Brennan: Trend following embeds convexity at no explicit premium but is exposed to short-term shocks; options are the precise hedge. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-2|C09-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-3|C09-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-X2|C09-X2]]); Niels Kaastrup-Larsen: Convexity depends on the horizon; short-term managers and tail funds claim more, trend skew has reportedly declined, and longer-term managers can argue daily convexity costs too much bleed. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-1|C09-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-X1|C09-X1]])

### Gaps and conflicts
- Rich claims trend following has convexity at no cost, but also says it is exposed to short-term shocks and whipsaws and is not a pure insurance program; the host notes trend skew has reportedly declined. No payoff data are shown. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-2|C09-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-3|C09-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-1|C09-1]])
- The claim that few trend followers blow up and no validated 20-30 year records exist for other styles is asserted without evidence or survivorship discussion. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C12-4|C12-4]])
- Natural analogies (avalanche, flood, forest fire) support the fragility argument but do not show that low volatility raises tail risk in markets. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C11-3|C11-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C11-4|C11-4]])
- 'Smooth linear curves later become concave' is shown with LTCM and mean reversion as examples; a counter-case of a smooth strategy that did not fail is not considered. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C07-3|C07-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C08-1|C08-1]])
- Rich's definition of the barbell (small linear losses, amplified gains) and the 'unrealised equity could be 5% of the value of the portfolio' remark are not quantified; the open-equity sizing rule is contested by the host. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C07-2|C07-2]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C13-5|C13-5]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C14-1|C14-1]])
- Rich's own wording says convexity cannot be had from historical statistics yet asserts that trend following has convex payoff; the evidence for the latter is the structure of the rules, not a measured skew. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C05-1|C05-1]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C14-3|C14-3]], [[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C09-1|C09-1]])
- (reader) The 60/40 critique (no brakes after correlation turned positive) is asserted from the recent correlation shift only; the earlier decades in which bonds did hedge are not discussed. ([[MT107 - Mastering Convexity! - Systematic Investor 333#^MT107-C08-2|C08-2]])

### Forward-looking inputs (reader synthesis)
(reader) Observable inputs the speakers say matter: (1) divergence between central banks (BOJ hiking, ECB cutting, Fed on hold) as a source of dispersion and trends; (2) the stock-bond correlation (positive now) as a break in the basis of 60/40; (3) regime of volatility (long muted periods followed by explosive moves) rather than average volatility; (4) trend persistence, since trend following pays when material trends exist and earns nothing in stagnation; (5) the open-equity share of NAV in trend funds as a risk for new investors. Horizon is the multi-year compounding horizon. Neither speaker forecasts a market direction.

### Reader inferences (not stated by the speakers)
- (reader) Rich's argument is a payoff-shape argument: rather than forecasting, he picks strategy classes (convex) whose payoff survives regime shifts, which is why he dismisses prediction-based risk measures.
- (reader) The host's horizon argument and Rich's no-premium claim point to the same unresolved question: how much of trend following's convexity exists at the horizon an investor cares about, given its lag in sudden shocks.
- (reader) Both speakers treat dispersion across trend managers as informative about model and market-exposure differences, linking it to the divergent macro environment rather than to randomness.
- (reader) The closed-equity discussion implies that risk measured on core capital understates the risk borne by a new investor, which is an allocator-side, not a model-side, problem.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, Greenland, banter, Dredge topics |
| C02 | 2 | Nvidia drop, Global Alts conference, central bank divergence |
| C03 | 4 | January winners, dispersion, index data |
| C04 | 3 | convexity defined, regimes, risk adaptation |
| C05 | 3 | trend vs mean reversion curves, convex vs concave |
| C06 | 3 | brakes analogy, adverse vs beneficial volatility, racetrack |
| C07 | 3 | uncertainty drives material events, barbell, linear illusion |
| C08 | 4 | LTCM, leverage, 60/40 correlation, tail protection |
| C09 | 4 | convexity by horizon, options cost, trend diversity |
| C10 | 2 | unimagined risks, Sharpe world critique |
| C11 | 5 | flawed assumptions, low vol fragility, VaR contagion |
| C12 | 4 | shifting distribution, concave drag, risk as permanent loss |
| C13 | 5 | drawdown length, VaR, trend barbell, core capital |
| C14 | 3 | open equity risk for new investors, thousands of trades |
| C15 | 4 | anti-martingale, diversification, let profits run |
| C16 | 3 | small bets, compounding, divergent world |
| C17 | 0 | paper plug, outro, next guest |

## Claims

### C02
- **Niels Kaastrup-Larsen** The Nvidia one-day drop (about 600 billion dollars) reversed within days, so short-term models reacted to noise that longer-term models ignored.  #mech/behavioral _(time-bound view)_
  > being a short-term uh manager where your models may, you know, react to a big sell-off like we saw on Monday
  indicator: Nvidia sell-off · asset: equities · direction: longer-horizon models gain by not reacting · horizon: days · conditions: single-day shock that reverses · testable: partly: compare speeds around sell-off days · confidence: medium
  ^MT107-C02-1
- **Niels Kaastrup-Larsen** Diverging central bank policy (BOJ hiking, ECB cutting, Fed on hold) creates market divergence and manager dispersion that could suit trend models.  #mech/policy_reaction _(time-bound view)_
  > the divergence in markets, which is most likely caused by central banks now having their own agenda instead of this very super coordinated agenda we saw a few years ago
  indicator: central bank policy divergence · asset: multi · horizon: months · conditions: post-coordination era · testable: partly: policy-rate dispersion vs trend returns · confidence: medium
  ^MT107-C02-2

### C03
- **Niels Kaastrup-Larsen** January 2025 trend winners were equities (post-election), German DAX, coffee, gold and live cattle; zinc was a drag.  #mech/slow_reaction _(time-bound view)_
  > Coffee has kind of helped out nicely now that cocoa is taking a little bit of a breather.
  indicator: DAX; coffee; cocoa; gold; live cattle; zinc · asset: multi · direction: long equities, coffee, gold, cattle · horizon: weeks · conditions: January 2025 · testable: yes: sector P&L attribution · confidence: medium
  ^MT107-C03-1
- **Richard Brennan** SG Trend Index fell while some managers gained in January because of differing commodity exposure and model differences, i.e. dispersion among trend followers.  #mech/crowding_positioning _(time-bound view)_
  > not all trend following is alike
  indicator: SG Trend Index vs manager returns · asset: multi · horizon: weeks · testable: yes: manager dispersion analysis · confidence: medium
  ^MT107-C03-2
- **Niels Kaastrup-Larsen** Kaastrup's trend barometer at 41 signals neutral trend performance; January CTA indices were mixed.  #mech/slow_reaction _(time-bound view)_
  > my trend barometer finished at 41. So, that's kind of a neutral stance uh on uh on performance.
  indicator: trend barometer (Dunn) · asset: multi · horizon: weeks · conditions: 31 January 2025 · testable: partly: proprietary indicator · confidence: medium
  ^MT107-C03-3
- **Niels Kaastrup-Larsen** Named data: SG Trend -52bp, SG CTA +20bp, Beta50 about +70bp, Bridge flat-fee trend -78bp, MSCI World +3.47 percent, long Treasury index -5 percent over 12 months.  #mech/slow_reaction _(time-bound view)_
  > SocGen Trend, as you mentioned, surprise, down 52 basis points as of Thursday
  indicator: SG Trend; SG CTA; Beta50; MSCI World · asset: multi · horizon: weeks · conditions: January 2025 · testable: yes: public indices · confidence: high
  ^MT107-C03-4

### C04
- **Richard Brennan** Markets are non-linear: long muted regimes alternate with explosive moves and large drawdowns, so average volatility is a poor description of risk.  #mech/structural_shift
  > financial markets are defined by convexity where small changes can lead to disproportionately large outcomes
  asset: multi · horizon: years · testable: partly: regime analysis of returns · confidence: high
  ^MT107-C04-1
- **Richard Brennan** Risk should be managed by adapting to the current regime, not by an average volatility assumption.  #mech/risk_management
  > Risk is being able to adapt to the market that's currently in play.
  asset: multi · testable: partly · confidence: medium
  ^MT107-C04-2
- **Richard Brennan** Trend following uses convexity for opportunity capture (diversification, outlier hunting) as well as protection, unlike tail-protection funds.  #mech/risk_premium
  > we embrace convexity at all levels, not just in protection, but also in looking for opportunities through diversification and by attacking what we call these outliers
  asset: multi · horizon: years · testable: partly · confidence: high
  ^MT107-C04-3

### C05
- **Richard Brennan** Trend following earns nothing in trendless periods (stagnation) and rises sharply in trends, giving a non-linear payoff.  #mech/slow_reaction
  > we don't expect that model to perform and so equity curves should expect drawdowns or what we call stagnation
  asset: multi · horizon: years · conditions: trendless markets · testable: yes · confidence: high
  ^MT107-C05-1
- **Richard Brennan** Mean reversion and negative-skew strategies yield many small wins then sudden large losses when an unpredicted regime hits (concave payoff).  #mech/risk_premium
  > when we are applying something like a mean reversion strategy or strategy with what we call negative skewed, we get a concave relationship
  indicator: skewness of strategy returns · asset: multi · horizon: years · conditions: regime shift · testable: yes · confidence: high
  ^MT107-C05-2
- **Richard Brennan** Convexity equals positive skew: amplify gains when volatility is favorable and cap losses with risk management.  #mech/risk_management
  > convexity, which is effectively positive skew, it ensures that favorable volatility accelerates gains while we mitigate loss losses through effective risk management
  indicator: return skewness · asset: multi · direction: long convexity · horizon: years · testable: yes · confidence: high
  ^MT107-C05-3
- **Richard Brennan** Traditional portfolio construction assumes a linear input-output world and so targets the straightest equity curve with the highest Sharpe ratio, which is inconsistent with non-linear markets where payoff shape matters more than smoothness.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > most traditional portfolios assume linearity. They're looking for the straightest possible um equity curve, the most linear equity curve, the curve with the highest Sharpe ratio
  indicator: Sharpe ratio; equity curve linearity · asset: multi · testable: partly - compare Sharpe-optimised vs skew-optimised portfolios · confidence: medium
  ^MT107-C05-X1

### C06
- **Richard Brennan** Convex process accelerates in favorable regimes and brakes (stops, small bets) in adverse regimes, rather than assuming constant conditions.  #mech/risk_management
  > convexity is about acceleration when conditions are favorable and braking effectively when conditions are not favorable
  indicator: stops; small bet sizes · asset: multi · testable: partly · confidence: high
  ^MT107-C06-1
- **Richard Brennan** Volatility splits into adverse and beneficial; smoothing funds only limit adverse volatility and forgo upside.  #mech/risk_management
  > we don't treat all volatility as the same. There is adverse volatility, and there is beneficial volatility.
  indicator: upside vs downside volatility · asset: multi · testable: yes: upside vs downside semivariance · confidence: medium
  ^MT107-C06-2
- **Richard Brennan** Exploiting upside volatility with good brakes gives higher compounded return than optimising for average speed, as an F1 car with brakes wins the lap.  #mech/behavioral
  > we can achieve a higher compounded return if we exploit upside volatility
  asset: multi · horizon: years · conditions: uncertain future environment · testable: partly · confidence: medium
  ^MT107-C06-3

### C07
- **Richard Brennan** Using history to set expected returns blindsides investors, because the most material events arise from uncertainty absent from the sample.  #mech/research_method
  > you're always going to be blindsided by these events that have never occurred in historical record like the COVID pandemic
  asset: multi · horizon: years · testable: partly · confidence: high
  ^MT107-C07-1
- **Richard Brennan** Barbell: keep losses small and linear on one side and amplify opportunity on the other, forcing asymmetry.  #mech/risk_management
  > the left side of the barbell is keeping our losses as small as possible, as linear as possible.
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT107-C07-2
- **Richard Brennan** Smooth linear equity curves reflect a temporary predictable environment and later become concave.  #mech/behavioral
  > these linear equity curves we often see put out by portfolio managers, they're actually the great illusion
  asset: multi · horizon: years · testable: partly: look at smooth-curve fund blow-ups · confidence: medium
  ^MT107-C07-3

### C08
- **Richard Brennan** Strategies that lever up predictable returns (LTCM, mean reversion, pattern recognition) fail at regime shift.  #mech/overshoot
  > The calamity occurs when suddenly the regime shifts with high leverage
  indicator: leverage on predictable returns · asset: multi · horizon: years · testable: partly · confidence: high
  ^MT107-C08-1
- **Richard Brennan** The 60/40 portfolio rested on a negative or zero stock-bond correlation which turned positive, leaving it with no brakes.  #mech/structural_shift
  > we have had stocks that are uncorrelated with bonds
  indicator: stock-bond correlation · asset: multi · horizon: years · conditions: correlation regime change · testable: yes: rolling stock-bond correlation · confidence: high
  ^MT107-C08-2
- **Richard Brennan** Models trained on history collapse in unprecedented environments; a backtest surviving does not ensure future survival.  #mech/research_method
  > What blindsides the traditional investment community is things that they never expected or never saw in their detailed historical data sets
  indicator: backtest · asset: multi · horizon: years · testable: partly · confidence: high
  ^MT107-C08-3
- **Richard Brennan** Tail protection funds add options to long-only portfolios to cover unforeseen collapses.  #mech/risk_management
  > typically someone like Dave Dredge or whatever, they'll employ options to provide that degree of protection for a traditional portfolio
  indicator: tail-protection options · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT107-C08-4

### C09
- **Niels Kaastrup-Larsen** Convexity depends on horizon; short-term managers and tail funds claim to offer more convexity, and trend followers' skew has reportedly declined.  #mech/structural_shift
  > even in with within our industry people might claim that oh, but trend followers are less provide less positive skew, less convexity today than they used to do
  indicator: trend following skewness · asset: multi · horizon: years · conditions: time frame dependent · testable: yes: skew over time · confidence: medium
  ^MT107-C09-1
- **Richard Brennan** Options protection costs premium (expiry worthless); trend following provides convexity without explicit premium, though with whipsaws.  #mech/risk_premium
  > There is no cost for our long short models in our trend following world, but we provide convexity at no cost.
  indicator: option premium vs trend · asset: multi · horizon: years · conditions: not perfect protection · testable: partly · confidence: medium
  ^MT107-C09-2
- **Richard Brennan** Medium-to-long-term trend models are exposed to sudden short-term shocks that options hedge immediately.  #mech/slow_reaction
  > we do have a degree of exposure and risk in relation to short-term adverse movements because our models can't respond quickly enough to their short-term movements
  asset: multi · horizon: days · conditions: sudden reversals · testable: yes · confidence: high
  ^MT107-C09-3
- **Richard Brennan** Trend following covers far more markets than options, giving diversified outlier exposure.  #mech/risk_premium
  > trend following offers better, more diverse opportunities in its ability to exploit opportunities
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT107-C09-4
- **Niels Kaastrup-Larsen** Counter-view on convexity horizon: longer-term managers can argue that supplying convexity at short horizons (daily) costs too much bleed and does not matter for long-run results, so convexity should be defined by time frame (Quantica has a paper on this).  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > there's too much bleed. It's too expensive to provide convexity on a daily basis because it doesn't matter uh in the long run
  indicator: convexity by horizon; bleed cost · asset: multi · conditions: depends on time frame · testable: yes - compare cost of short-horizon convexity with long-run payoff · confidence: low
  ^MT107-C09-X1
- **Richard Brennan** Options are the most precise hedge for a traditional portfolio because they can be matched to the specific risk (correlation risk, market risk), whereas trend following is a less targeted, free-of-premium form of convexity.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > options is probably the purest way to get um protection for a traditional portfolio for adverse risk events because you can align the option exposure to what you're trying to protect
  indicator: option hedge vs trend following · asset: multi · testable: partly - hedge effectiveness vs cost testable · confidence: medium
  ^MT107-C09-X2

### C10
- **Niels Kaastrup-Larsen** Trend following in a multi-asset portfolio cushions events nobody imagined, so ask what you are doing about what you are not worried about.  #mech/risk_management
  > having things like trend following in the portfolio will not necessarily completely alleviate the issue, but it will certainly reduce some of the pain
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT107-C10-1
- **Richard Brennan** Sharpe, standard deviation and VaR fail because crises (1987, 2002, 2008, COVID) come from unforeseen events; risk is not volatility.  #mech/research_method
  > one of the greatest misconceptions is the belief that risk equates to volatility
  indicator: Sharpe; standard deviation; VaR · asset: multi · horizon: years · testable: partly · confidence: high
  ^MT107-C10-2

### C11
- **Richard Brennan** Five flawed assumptions of traditional finance: historical risk, normality, persistent correlations, estimable returns, all volatility bad.  #mech/research_method
  > One is risk can be quantified using historical data. Two, markets behave in a linear fashion following normal distributions. Three, correlations persist into the future.
  asset: multi · horizon: years · testable: partly · confidence: high
  ^MT107-C11-1
- **Richard Brennan** Taleb: risk is about possible outcomes, not probabilities from the past.  #mech/research_method
  > risk is a possibility distribution, not a probability distribution
  asset: multi · testable: no · confidence: medium
  ^MT107-C11-2
- **Richard Brennan** Long calm periods raise fragility (avalanche, flood, forest fire analogies), so low volatility is not safe.  #mech/behavioral
  > low volatility environments encourage excessive leverage, and they make markets more fragile and vulnerable to shocks
  indicator: realised volatility; leverage · asset: multi · horizon: years · testable: yes: low vol then drawdown · confidence: high
  ^MT107-C11-3
- **Richard Brennan** VaR misses contagion because markets are connected complex adaptive systems.  #mech/risk_management
  > So, the assessment of VAR is going to totally underestimate the calamity.
  indicator: VaR · asset: multi · horizon: years · testable: partly · confidence: high
  ^MT107-C11-4
- **Richard Brennan** Risk must be built into portfolio design (convexity), not only forecasted.  #mech/risk_management
  > This is why risk cannot be managed exclusively through predictive models. It must be built into portfolio design.
  asset: multi · testable: no · confidence: high
  ^MT107-C11-5

### C12
- **Richard Brennan** Positive skew optimises long-term compounded wealth.  #mech/risk_premium
  > we're shifting the distribution to the right. So, we've got lots of small losses, but occasional massive wins
  indicator: return skewness · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT107-C12-1
- **Richard Brennan** Concave strategies with rare crippling losses cause compounding drag.  #mech/risk_premium
  > creates significant compounding drag and totally dilutes the compounding effect
  indicator: geometric vs arithmetic return · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT107-C12-2
- **Richard Brennan** Risk should be defined as permanent loss of capital, not volatility.  #mech/risk_management
  > Risk to me is permanent loss of capital.
  asset: multi · testable: no · confidence: high
  ^MT107-C12-3
- **Richard Brennan** Few trend followers ever blow up whereas mean-reversion strategies (LTCM) do; no validated 20-30 year records exist for other styles.  #mech/risk_premium
  > In a trend following world, hardly any. Why? Because they apply positive convexity.
  indicator: blow-up frequency · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT107-C12-4
- **Niels Kaastrup-Larsen** Niels, citing Asness, pushes back that complete permanent loss of capital is rare in any strategy, so defining risk only that way is too narrow; he wants something in between because volatility can still feel like risk even if it is not the same.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > I mean, how many strategies in our careers have we really seen blow up completely?
  indicator: risk definition (permanent loss vs volatility) · asset: multi · testable: no - definitional · confidence: medium
  ^MT107-C12-X1

### C13
- **Niels Kaastrup-Larsen** Long drawdowns hurt investor psychology more than deep short ones (Asness).  #mech/behavioral
  > the length of drawdown can be much more damaging to our psychology than actually a quick large drawdown
  indicator: drawdown duration · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT107-C13-1
- **Niels Kaastrup-Larsen** The range and probability of extreme events is judged higher now.  #mech/structural_shift _(time-bound view)_
  > the possibilities as well as the probabilities of something crazy happening is probably higher today than ever before
  asset: multi · testable: no · confidence: low
  ^MT107-C13-2
- **Niels Kaastrup-Larsen** Correlation-aware VaR, used properly, remains a decent risk measure, better than Sharpe.  #mech/risk_management
  > it's probably still a decent measure compared to some of the other ones
  indicator: VaR · asset: multi · testable: partly · confidence: low
  ^MT107-C13-3
- **Richard Brennan** Trend following is a barbell of small losses and let profits run, with very small bet sizes.  #mech/risk_management
  > our ability to cut losses short at all times and let profits run
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT107-C13-4
- **Richard Brennan** Risk each trade as a small fraction of closed-trade core capital, letting unrealised equity run.  #mech/risk_management
  > we're only exploiting a very small risk bet of our core capital to our trade
  indicator: core capital; open equity · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT107-C13-5

### C14
- **Niels Kaastrup-Larsen** Large open profits expose new investors to 50 percent drawdowns; allocate AUM on closed equity.  #mech/risk_management _(time-bound view)_
  > with some managers the open trade equity became so large that people who bought into those funds at a certain time had open trade equity of 50, 60, 70%
  indicator: open trade equity · asset: multi · horizon: months · conditions: concentrated winning trades in 2024 · testable: yes · confidence: medium
  **Correction (cross-check):** Two speakers merged: Niels only raises the risk (new investors holding funds with 50-70% open trade equity face large drawdowns, and the principle suits one's own money with an infinite runway). The suggestion to allocate AUM on closed equity is Rich's reply, not Niels's. → Niels: in funds whose open trade equity grew to 50-70% of NAV, new investors are exposed to a straight 50% drawdown that long-standing investors are not, so closed-equity sizing mainly suits own money; Rich replied separately that new AUM can be allocated on closed equity.
  ^MT107-C14-1
- **Richard Brennan** Trend following should be judged on thousands of trades, not individual outcomes.  #mech/research_method
  > Look at the the last 2,000 trades. Look at the last 4,000 trades.
  indicator: trade sample · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT107-C14-2
- **Richard Brennan** Trend following amplifies upside by letting profits run and concentrating in material trends.  #mech/slow_reaction
  > trend following is really aggressively looking to amplify upside
  asset: multi · horizon: years · testable: partly · confidence: high
  ^MT107-C14-3
- **Richard Brennan** Rich's answer to the new-investor problem: allocate new AUM using closed equity, so open (unrealised) equity stays with existing investors and is not a new investor's problem; there are different models for this.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > you could apply a process that applies it based on closed equity. Um the unrealized equity is not a problem with the new incoming investor.
  indicator: closed equity vs open equity for AUM allocation · asset: multi · conditions: funds with large open trade equity from a few trades · testable: partly - simulate new-investor drawdown under both bases · confidence: medium
  ^MT107-C14-X1
- **Richard Brennan** The philosophy of trend following is long-horizon compounding with patience; using it for other purposes (as an allocation inside traditional portfolios, or managing outside AUM) adds concerns, which Rich calls the business of trend following as distinct from trend following itself.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > do not do trend following unless you're prepared to do it for the long haul
  indicator: trend following horizon; trade sample · asset: multi · horizon: years · conditions: investors who cannot tolerate long drawdowns · testable: no - philosophy · confidence: high
  ^MT107-C14-X2

### C15
- **Richard Brennan** Take a small initial trade, add as it succeeds (anti-martingale) with an ensemble, for positive convexity.  #mech/risk_management
  > and if it continues to go my way, I what we call apply an anti-martingale degree of progression into it
  indicator: pyramiding · asset: multi · testable: yes · confidence: high
  ^MT107-C15-1
- **Richard Brennan** Martingale doubling after losses is concave: small gains but catastrophic risk.  #mech/risk_management
  > That is a concave strategy. That is a Martingale approach.
  indicator: martingale · asset: multi · testable: yes · confidence: high
  ^MT107-C15-2
- **Richard Brennan** Wide diversification is for finding outliers since their location cannot be forecast.  #mech/risk_premium
  > we're doing it to find those outliers wherever they may roam because these things are unpredictable
  indicator: number of markets · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT107-C15-3
- **Richard Brennan** Ride winners until trends exhaust; one outlier (cocoa, equity rally) pays for dozens of small losses.  #mech/risk_premium
  > So, these single outlier events, they can offset dozens of small losses.
  indicator: outlier trades · asset: commodities · horizon: years · testable: yes · confidence: high
  ^MT107-C15-4
- **Richard Brennan** Rich's aim is 'infinite yield': an open-ended payoff from letting profits run so that one trend pays for all accumulated costs of small controlled losses, which are the price of staying in the game for the next unknown opportunity.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > the principle there is a return that pays for all of the costs you've had over the course of time
  indicator: payoff asymmetry · asset: multi · horizon: years · conditions: requires patience and survival through losing streaks · testable: yes - profit factor of top trades vs cumulative losses · confidence: medium
  ^MT107-C15-X1

### C16
- **Richard Brennan** Small position size is the ultimate stop since stop orders can gap.  #mech/risk_management
  > Stops themselves can be broken. We know that in very fast-moving markets, they're not always observed
  indicator: position size · asset: multi · horizon: days · conditions: fast markets · testable: yes · confidence: high
  ^MT107-C16-1
- **Richard Brennan** Survival through small bets keeps capital in play for compounding.  #mech/risk_management
  > you're required to have skin in the game for a very long period of time to exploit the power of the exponential growth that compounding gives
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT107-C16-2
- **Niels Kaastrup-Larsen** Investors who think they are diversified hold hidden short volatility exposure; a more divergent world favours trend.  #mech/crowding_positioning _(time-bound view)_
  > people think they might be diversified, but in reality they're full of short ball strategies essentially
  indicator: hidden short vol · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT107-C16-3
- **Richard Brennan** Diversification in trend following serves three purposes: lower portfolio correlation and risk through diversity, a wider opportunity set, and capturing outliers wherever they appear.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > is diversification as safety net. It's not only about a safety net, but it's also about spreading that net wide to capture those outliers, expanding the opportunity set, and also risk reduction through diversity.
  indicator: number of markets; portfolio correlation · asset: multi · testable: yes - market count vs trend capture and risk · confidence: high
  ^MT107-C16-X1

