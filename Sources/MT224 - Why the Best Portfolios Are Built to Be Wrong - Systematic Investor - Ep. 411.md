---
source_id: MT224
title: "Why the Best Portfolios Are Built to Be Wrong - Systematic Investor - Ep. 411"
date: 2026-08-02
channel: "Top Traders Unplugged"
url: 
words: 19153
claims: 62
added_by_crosscheck: 8
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Niels Kaastrup-Larsen (host)", "Rich Brennan (trend follower)", "Dave Dredge (CIO, Convex Strategies)"]
tags: [source, layer0]
---
# Why the Best Portfolios Are Built to Be Wrong - Systematic Investor - Ep. 411

**Speakers:** Niels Kaastrup-Larsen (host); Rich Brennan (trend follower); Dave Dredge (CIO, Convex Strategies)

**Summary:** Top Traders Unplugged episode (Aug 2026) on markets as complex adaptive systems. Dredge (convexity/options) and Brennan (trend) argue for non-ergodic, fat-tailed thinking: calm builds risk, leverage and price-insensitive flows drive moves, Sharpe/Kelly/VaR mislead. Prescriptions: add convexity, cap leverage, equal-risk sizing, widen the book, enter small.

**Approach:** trend following, convexity, long volatility, tail risk, complex systems

**Cross-check completeness estimate of first read:** 0.88 - the first reader captured nearly all of the main arguments, numbers and analogies from both Dredge and Brennan across all 28 chunks; the additions are secondary mechanisms (hidden single-anchor dependency, policy suppression of volatility, cash flows on the wealth path, agent model without news, enter-small rule) and one garbled-number correction.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro, performance data July 2026 |
| C02 | 2 | levered ETFs volatility drag, rates highs |
| C03 | 2 | framing: complex adaptive systems, Dredge on resilience |
| C04 | 1 | Brennan on reflexivity, non-stationarity, Mandelbrot |
| C05 | 2 | Feynman electrons, price insensitive flows, rational accounting man |
| C06 | 2 | bond market imbalance, leverage and loss-absorbing capital |
| C07 | 3 | agent-based model, 25% threshold |
| C08 | 3 | phase transition, sources of big moves, correlation assumptions |
| C09 | 2 | endogenous vs news, ergodicity intro |
| C10 | 1 | ergodicity, sequencing |
| C11 | 3 | return reshuffling, volatility drag, forest fire analogy |
| C12 | 2 | percolation, VaR and calm, rubber band |
| C13 | 3 | quiet markets, vol-targeted leverage, JGB example |
| C14 | 2 | leverage, thin vs fat tails, cocoa, sizing as the trend secret |
| C15 | 2 | Kelly criterion and being optimal |
| C16 | 2 | World Cup convex goalkeeper model |
| C17 | 1 | parking the bus; start of Sharpe discussion |
| C18 | 2 | October 2008 and Sharpe, failure modes |
| C19 | 2 | diversification critique, permanent coupling |
| C20 | 1 | diversification and kurtosis, cocoa |
| C21 | 3 | 125-year data, convexity implementation |
| C22 | 2 | long-dated option edge, convexity, tail truncation |
| C23 | 1 | synthetic option shape of trend, combining approaches |
| C24 | 3 | 50/50 mixes, Monday morning actions: incentives, leverage cap |
| C25 | 2 | equal risk, widen book, enter small, portable alpha question |
| C26 | 2 | leverage on convex vs concave; band-aid |
| C27 | 0 | outro, review contest |
| C28 | 2 | risk is accountability; close |

## Claims

### C01
- **Niels Kaastrup-Larsen** Late-July 2026 data point: trend barometer 45 (neutral); SG CTA +8.5% YTD, SG Trend +8.3%, short-term traders index +3.34% YTD, so slower trend beat short-term trend.  #mech/slow_reaction _(time-bound view)_
  > my trend barometer yesterday finished at 45 which is pretty neutral
  indicator: trend barometer; SG Trend and Short-Term Traders indices · asset: multi · horizon: months · conditions: July 2026 · testable: no - data points · confidence: high
  ^MT224-C01-1

### C02
- **Dave Dredge (CIO Convex Strategies, options/convexity)** Daily-rebalanced 2x levered ETFs suffer volatility drag: SK Hynix ETF fell 47% over three months while the stock ended +1% after a +125% peak, so over long horizons levered ETFs approach zero.  #mech/risk_management _(time-bound view)_
  > The two times levered ETF is down 47%.
  indicator: volatility drag of levered ETFs · asset: equities · direction: avoid long-term holding of daily levered ETFs · horizon: months · conditions: high volatility, path-dependent · testable: yes - geometric return maths · confidence: high
  ^MT224-C02-1
- **Dave Dredge (CIO Convex Strategies, options/convexity)** July 2026: multi-decade highs in long-dated yields in Japan, US and UK, Fed holding with three dissents and bond-market disappointment.  #mech/policy_reaction _(time-bound view)_
  > multi-year, multi-deade highs in longdated bond yields in Japan, in the US, in Britain.
  indicator: long-dated government bond yields · asset: rates · horizon: months · conditions: July 2026 · testable: no - description · confidence: high
  ^MT224-C02-2

### C03
- **Niels Kaastrup-Larsen** Framing: Dredge (options/convexity) and Brennan (trend following) both treat markets as complex adaptive systems, so Gaussian statistics are the wrong mathematics and risk is not volatility.  #mech/structural_shift
  > Both of you see markets as complex adapted systems rather than as statistical distributions to be sampled and estimated.
  asset: multi · testable: no - framing · confidence: high
  ^MT224-C03-1
- **Dave Dredge (CIO Convex Strategies, options/convexity)** Because the future path is unknowable (infinite paths around a strange attractor), investors should understand current initial conditions and build resilience (brakes) rather than forecast.  #mech/risk_management
  > It's about making your car as resilient as it can possibly be and then being able to react and respond to the unknowable path of
  asset: multi · direction: buy protection and keep ability to react · testable: no - philosophy · confidence: high
  ^MT224-C03-2

### C04
- **Rich Brennan** Markets are reflexive, non-stationary, computationally irreducible processes where agents react to a system that reacts to them, so outcomes cannot be forecast with linear statistics (Mandelbrot: roughness at every scale).  #mech/structural_shift
  > it's a world of of uh reflexivity you know where you know matter tells space how to curve and space tells matter how to move
  asset: multi · testable: no - conceptual · confidence: high
  ^MT224-C04-1
- **Rich Brennan** Observed return statistics are only the residue of a deeper, constraint-contingent process with many interacting variables, so inference from the distribution of outcomes cannot recover the process or forecast the outcome with fidelity.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > that's what I call a statistical residue of a process. The deep process itself shows that there are so many multivariate variables affecting the outcome
  asset: multi · testable: no - epistemic claim about statistics · confidence: medium
  ^MT224-C04-X1

### C05
- **Rich Brennan** Brennan claims little evidence that anyone has beaten the market despite clever quants, because inappropriate (Gaussian) mathematics is applied to a reflexive domain.  #mech/behavioral
  > there is very little evidence that anyone has significantly beaten the market. Uh, the market is the master.
  asset: multi · testable: no - assertion · confidence: medium
  ^MT224-C05-1
- **Dave Dredge (CIO Convex Strategies, options/convexity)** Dredge's dictum: positioning (especially price-insensitive flow) is what moves markets; he splits participants into 'rational accounting man' (price-insensitive, rule/regulation-driven: banks, pensions, insurers, central banks, FX reserve managers, passive) and boundedly rational agents with skin in the game.  #mech/crowding_positioning
  > positioning is the only thing that matters.
  indicator: share of price-insensitive participants / positioning · asset: multi · testable: partly - needs participant classification · confidence: high
  ^MT224-C05-2

### C06
- **Dave Dredge (CIO Convex Strategies, options/convexity)** The bond market is the biggest price-insensitive imbalance; holders (central banks, FX reserves, banks, pensions/insurers) sit on massive unrealised losses without cutting positions, because they do not mark to market, so the unwind of the 2020 bond bubble is incomplete.  #mech/fiscal_debt _(time-bound view)_
  > the bond market went well through that at the peak of what I call the mother of all bubbles of bond markets
  indicator: unrealised losses of non-price-sensitive bondholders · asset: rates · horizon: years · testable: partly - descriptive · confidence: medium
  ^MT224-C06-1
- **Dave Dredge (CIO Convex Strategies, options/convexity)** Leverage is the risk (left-skewed returns, fat tails); when regulators measure risk as volatility, low vol licenses leverage, imbalances build reflexively and unwind violently as loss-absorbing capital is depleted.  #mech/crowding_positioning
  > The lack of capital is the strange attractor at times pulling the market that direction because of the proliferation of loss management as that leverage has to get cleansed from the system.
  indicator: leverage, loss-absorbing capital · asset: multi · horizon: months · conditions: regulated space where vol = risk · testable: partly - leverage data · confidence: high
  ^MT224-C06-2
- **Dave Dredge** The first shock unwind of the bond-market imbalance in 2022, when rates rose from the 2020 bond bubble peak, gave trend followers one of their biggest opportunities in years, and the speaker argues the unwinding of the complexity is not finished.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check, time-bound view)_
  > the initial shock unwind of that imbalance in 2022 when interest rates went up and you had one of the biggest opportunities and trend that you've had in a long time
  indicator: bond market imbalance / interest rates · asset: rates · direction: trend gains in bond shorts when price-insensitive holders are forced to unwind · horizon: years · conditions: after leverage and price-insensitive demand built up in rates · testable: yes - trend P&L in rates around 2022 checkable · confidence: medium
  ^MT224-C06-X1

### C07
- **Rich Brennan** Price moves because of transactions; fundamentals, macro and flows are downstream, and an ecosystem of participant types (fundamental, trend, convergent, random) applies directed forces whose feedback creates fractal price structure.  #mech/structural_shift
  > the transaction event that moves price.
  indicator: participant forces · asset: multi · testable: no - microstructure view · confidence: medium
  ^MT224-C07-1
- **Rich Brennan** Agent-based model with only random traders gives Gaussian returns with no fat tails, memory or volatility clustering.  #mech/research_method
  > Um uh no fat tails, no memory, no volatility clustering. Um it was exactly what you you the outcomes you'd expect from the efficient market hypothesis
  indicator: simulated returns · asset: multi · testable: yes - simulation · confidence: high
  ^MT224-C07-2
- **Rich Brennan** At roughly 25% divergent (amplifying) participants, fat tails, volatility clustering and memory appear; passive investing counts as divergent because it follows a rule to buy the biggest.  #mech/crowding_positioning
  > about 25% and above of participants that are divergent. Um all of the signatures you see in the real market automatically come back into the market.
  indicator: share of divergent participants · asset: multi · testable: partly - simulation, share unobservable · confidence: medium
  ^MT224-C07-3

### C08
- **Rich Brennan** The simulation shows a sharp phase transition at about 25% divergent participation rather than a gradual change, so amplifying positions create the tails, memory and volatility clusters seen in real markets.  #mech/structural_shift
  > It was a transition event.
  indicator: threshold of divergent share · asset: multi · testable: partly · confidence: medium
  ^MT224-C08-1
- **Dave Dredge (CIO Convex Strategies, options/convexity)** Big moves come from lack of loss-absorbing capital plus unstable correlation assumptions: when correlation misbehaves, investors must cut risk, which changes correlation for the next investor and triggers divergent traders, a reflexive chain.  #mech/liquidity_flows
  > people because they're following very simplified rules of gaussian linearity uh erotic single slices of time they are taking more risk than they have the loss appetite for
  indicator: correlation instability; diversification assumptions · asset: multi · horizon: weeks · testable: partly · confidence: high
  ^MT224-C08-2
- **Dave Dredge (CIO Convex Strategies, options/convexity)** Portfolio risk missed is mostly correlation and volatility assumed constant in MPT/EMH frameworks; implicit leverage via volatility selling creates mispriced tails.  #mech/risk_management
  > most people do a pretty good job of managing the risk they manage or managing the risk they measure. But what they don't do a very good job of is managing the risk they assume, the risk they don't measure.
  indicator: correlation and volatility stability · asset: multi · testable: yes - compare realised vs assumed correlation · confidence: high
  ^MT224-C08-3

### C09
- **Rich Brennan** Citing Bouchaud, about 90% of big market moves come from endogenous sources, not news; activity picks up, liquidity thins, the book fragilises, then a trigger hits and settling takes longer than the orthodoxy assumes.  #mech/structural_shift
  > it was 90% of the moves were from indogenous sources
  indicator: news vs price move correlation; liquidity thinning · asset: multi · horizon: days · testable: yes - microstructure studies · confidence: high
  ^MT224-C09-1
- **Rich Brennan** Volatility clusters, so calm periods can persist while risk accumulates in the structure; the transition from calm to volatile catches everyone.  #mech/cycle_persistence
  > calm begets calm
  indicator: volatility clustering · asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT224-C09-2
- **Rich Brennan** The agent-based model reproduces fat tails, volatility clustering and memory with no news events at all, using only convergent, divergent and random participants, which supports the claim that these properties arise from market structure and not from information arrival.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > with no news events um I didn't need any news events in those agent-based models
  indicator: agent-based simulation · asset: multi · testable: partly - simulation result, real-world test is the Bouchaud news-correlation study · confidence: medium
  ^MT224-C09-X1

### C10
- **Dave Dredge (CIO Convex Strategies, options/convexity)** Investing is non-ergodic: the ensemble average does not equal the time average (geometric vs arithmetic mean), sequencing matters, and ruin ends the game (Peters, Taleb).  #mech/risk_management
  > a 50% draw down isn't corrected with a 50% recovery. You're not back. You got to get a 100% recovery to get back.
  indicator: geometric vs arithmetic return · asset: multi · horizon: years · testable: yes - arithmetic · confidence: high
  ^MT224-C10-1
- **Rich Brennan** External cash flows on the wealth path (taxes taken out, subscriptions or redemptions) change the path of the accumulated balance in a multiplicative process, so investors' real compounding differs from the additive returns reported by the manager.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > stuff is taken away taxes all of these things stuff is added redemptions are added into that wealth path
  indicator: accumulated balance / compounding path · asset: multi · horizon: years · testable: partly - simulate path with cash flows · confidence: medium
  ^MT224-C10-X1

### C11
- **Rich Brennan** Reshuffling 40 years of identical returns left Sharpe, Sortino, VaR and standard deviation unchanged but terminal wealth ranged from a 30% decline to an 84% decline, so order-dependent path matters and these metrics miss it.  #mech/research_method
  > all of the standard metrics sharp sortino variance at risk standard deviation they all stayed the same but what did change was the wealth
  indicator: reshuffled return sequence outcomes · asset: multi · horizon: years · testable: yes - bootstrap of return order · confidence: high
  ^MT224-C11-1
- **Rich Brennan** Volatility drag widens the gap between geometric and arithmetic paths in a compounding way, so wealth is a multiplicative process and arithmetic returns mislead.  #mech/risk_management
  > as volatility increases as Dave talks about volatility drag you find that that difference increases in a compounded manner.
  indicator: volatility drag · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT224-C11-2
- **Dave Dredge (CIO Convex Strategies, options/convexity)** Self-organised criticality: risk grows the longer there is no fire; diversification protects against a lightning strike on one tree but not against fire spreading through connectivity (leverage, correlation), as in a percolation threshold or an avalanche triggered by one snowflake.  #mech/cycle_persistence
  > the fire risk grows as the forest goes longer and longer without a fire because you get more clogged brush between the trees.
  indicator: time since last shock; connectivity · asset: multi · horizon: years · testable: partly - conceptual, hard to time · confidence: high
  ^MT224-C11-3

### C12
- **Dave Dredge (CIO Convex Strategies, options/convexity)** VaR measures the frequency of past fires, so protection (options) is cheapest exactly where risk is highest, after long calm and price-insensitive supply; that is his secret sauce, e.g. rising debt/GDP without a blow-up is more reason to worry.  #mech/risk_premium
  > things like value at risk are measuring the frequency, a short-term frequency of past fires. And it says, well, there hasn't been a fire, so there's no risk.
  indicator: VaR / realised volatility versus option price · asset: multi · direction: buy tail protection when realised vol is low · horizon: years · conditions: after long calm · testable: partly · confidence: high
  ^MT224-C12-1
- **Rich Brennan** Calm markets are not equilibrium; quiet is energy building like a stretched rubber band that traditional risk metrics hide.  #mech/structural_shift
  > Markets are not closed systems that equilibrate. Um they're open systems
  asset: multi · testable: no · confidence: medium
  ^MT224-C12-2

### C13
- **Rich Brennan** In his research quiet markets are the deepest coupled negative-feedback states (oscillations cancelling), and most risk events emerge from calm regimes via a volatility shock, not from already volatile regimes.  #mech/overshoot
  > they are the deepest coupled negative feedback states in the entire data set.
  indicator: volatility regime before risk events · asset: multi · horizon: days · testable: yes - condition on prior volatility · confidence: medium
  ^MT224-C13-1
- **Rich Brennan** Volatility-targeted sizing mechanically raises positions in calm and behavioural leverage-up adds to it; Japanese government bonds in 2018 had 9% trailing vol authorising 16.4x leverage, so a 6% move cost 9% of capital.  #mech/risk_management
  > They will have a period of calm and their models mechanistically increase the position size in that period of calm because they're saying it's a safe market.
  indicator: trailing volatility vs leverage · asset: rates · direction: cap leverage, do not equate calm with safety · horizon: months · conditions: after quiet periods · testable: yes - vol-target backtests around vol shocks · confidence: high
  **Correction (cross-check):** The JGB leverage figures are internally inconsistent as transcribed ('about 9% trailing volatility', '16.4 times leverage', a 'only 6% move' costing 9% of capital: 6% x 16.4 is about 98%), so the first reader's repetition of '9% trailing vol authorising 16.4x leverage, so a 6% move cost 9% of capital' is unreliable; the transcript opens with 'trailing volatility of a fraction', so the volatility was probably well under 1%. → Volatility-targeted sizing mechanically raises positions in calm periods and behavioural leverage-up adds to it; in the Japanese bond market (about 2018) very low trailing volatility authorised about 16.4x leverage, so a modest move cost about 9% of capital (exact volatility and move sizes garbled in the transcript).
  ^MT224-C13-2
- **Rich Brennan** High Sharpe ratios authorise more leverage, which is dangerous because the estimates are noisy and tails fat.  #mech/risk_management
  > A high sharp ratio well that's actually authorizing a higher leverage and uh that's exactly what you don't want to be doing.
  indicator: Sharpe ratio-based leverage · asset: multi · direction: reduce leverage after high Sharpe · testable: partly · confidence: medium
  ^MT224-C13-3

### C14
- **Dave Dredge (CIO Convex Strategies, options/convexity)** Own assets with thin tails and high natural volatility, and build hedges from things with artificially suppressed volatility and attracted leverage (bank/repo leverage, volatility selling), which have fat left tails; trend followers need only a few fat-tail winners with small losses (e.g. cocoa).  #mech/risk_premium
  > you want to own and invest in things with thin tails, things that have high natural
  indicator: suppressed volatility plus leverage · asset: multi · direction: long convexity in suppressed-vol assets · horizon: years · testable: partly · confidence: medium
  ^MT224-C14-1
- **Niels Kaastrup-Larsen** Niels argues the real trend-following edge is risk management and position sizing rather than breakout signals.  #mech/research_method
  > the whole secret that trend followers brought to the table back in the 70s is that they understood how to manage the risk and they understood how to size positions
  indicator: position sizing · asset: multi · testable: partly · confidence: medium
  ^MT224-C14-2
- **Dave Dredge** Central banks, governments and policy makers deliberately suppress volatility so that price-insensitive, rule-bound holders (banks, pensions, insurers) lever up in the assets policy wants to grow (government bonds, housing); suppressed volatility plus leverage is what produces the fragility and fat left tails.  #mech/policy_reaction _(added by sonnet-xhigh cross-check)_
  > through the active suppression of volatility, central banks, governments, policy makers, they want to take advantage again, rational accounting man, they want rational accounting man to lever up
  indicator: suppressed volatility plus leverage in policy-favoured assets · asset: multi · direction: fat left tails in assets with suppressed volatility · horizon: years · conditions: regulatory risk measures treat low volatility as low risk · testable: partly - volatility suppression vs later tail events measurable · confidence: medium
  ^MT224-C14-X1

### C15
- **Rich Brennan** Kelly-optimal sizing sits at a peak where overbetting quickly causes ruin, assumes perfect information, and uses estimates whose required sample explodes with fat tails; under-betting gives room for error.  #mech/risk_management
  > the problem of being optimal is that it foregoes the room for being wrong.
  indicator: Kelly fraction · asset: multi · direction: bet below Kelly · conditions: non-stationary, noisy, fat-tailed markets · testable: yes - simulate fractional vs Kelly under estimation noise · confidence: high
  ^MT224-C15-1
- **Rich Brennan** His tests show simple equal-risk fractional sizing outperforms Kelly-based sizing once regime changes and estimation noise are included, because noise often exceeds the signal; LTCM exceeded the peak assumptions and went to ruin.  #mech/research_method
  > it outperforms the the the Kelly approach when you start introducing things such as regime changes sufficient noise to your estimate
  indicator: equal-risk sizing vs Kelly sizing · asset: multi · direction: equal-risk over Kelly · horizon: years · conditions: with regime change and noise · testable: yes · confidence: medium
  ^MT224-C15-2

### C16
- **Dave Dredge (CIO Convex Strategies, options/convexity)** The S&P 500's 10 worst and 10 best months of 480 contribute almost all long-term returns, so the average is meaningless and what happens in the tails (penalty boxes) matters.  #mech/risk_premium
  > the two percentiles of returns, the 10 worst months out of 480 months and the 10 best months out of 480 months contribute almost all of the returns.
  indicator: S&P 500 monthly returns, extreme percentiles · asset: equities · horizon: years · testable: yes - decile contribution · confidence: high
  ^MT224-C16-1
- **Dave Dredge (CIO Convex Strategies, options/convexity)** World Cup study: tournaments in a non-ergodic knockout are won by defensive resilience near own box, then attacking efficiency near the opponent's box, then individual tail events; used as an analogy for convex portfolio construction.  #mech/behavioral
  > the convex goalkeeper theorem
  asset: other · testable: partly - sports data analogy, not a market test · confidence: medium
  ^MT224-C16-2

### C17
- **Dave Dredge (CIO Convex Strategies, options/convexity)** Parking the bus is like a covered call or 60/40: capping upside does not remove tail exposure; you must be convex on both sides where it matters.  #mech/risk_management
  > They did what is so common in the investment industry. They thought they could reduce risk by capping the upside.
  indicator: covered call, 60/40 · asset: multi · testable: partly · confidence: medium
  ^MT224-C17-1

### C18
- **Rich Brennan** October 2008 was 3.4% of total trend-portfolio wealth over 40 years yet the Sharpe ratio moved only from 914 to 931 (2 cents in the dollar), so Sharpe penalises convex strategies.  #mech/risk_management
  > October 2008, that was a fantastic period for trend followers. It was the single largest month in the return for the entire history of 40 years that that um I looked at.
  indicator: Sharpe contribution of largest month · asset: multi · horizon: years · testable: yes - recompute Sharpe with/without month · confidence: high
  ^MT224-C18-1
- **Rich Brennan** Two portfolios with identical Sharpe 1.5 (one concentrated Kelly bet, one wide book of small loosely related positions) differ in failure modes; Sharpe discards construction, so architecture and dependencies must be assessed.  #mech/research_method
  > consider two portfolios both with a a sharp ratio of 1.5.
  indicator: Sharpe ratio, portfolio architecture · asset: multi · testable: partly · confidence: high
  ^MT224-C18-2

### C19
- **Dave Dredge (CIO Convex Strategies, options/convexity)** Traditional diversification assumes stable correlation and ignores connectivity; diversification across things that can each lose everything is bad, whereas diversification across positions with unbounded upside (St. Petersburg paradox) is good.  #mech/risk_management
  > Yes, sometimes right just not when it matters the most right.
  indicator: correlation stability · asset: multi · testable: partly · confidence: high
  ^MT224-C19-1
- **Rich Brennan** Markets are permanently coupled via multi-product diversified agents; in calm regimes the coupling oscillates and cancels (apparent diversification) but in crisis it turns into trend and everything correlates; diversification must be judged by architecture (e.g. borrow short/lend long across a dozen markets is one rate bet).  #mech/crowding_positioning
  > I think that markets are always permanently coupled.
  indicator: correlation across markets by regime · asset: multi · horizon: weeks · testable: yes - measure correlation by regime · confidence: medium
  ^MT224-C19-2
- **Rich Brennan** A book that looks diversified across many markets can share one hidden dependency (borrow short and lend long across a dozen markets is a single interest-rate bet), like a thousand strands tied to one anchor; diversification must be judged by architecture and dependencies, not by correlation statistics.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > you might borrow short and lend long across a dozen markets during calm regimes and think it's fantastically diversified, but you're exposed to a a single interest rate bet
  indicator: hidden common exposure across positions · asset: multi · conditions: apparent diversification in calm regimes · testable: partly - factor decomposition of the book can reveal common exposure · confidence: high
  ^MT224-C19-X1

### C20
- **Rich Brennan** With fractal structure, greater diversification gives an initial drop in kurtosis then rising kurtosis, so more markets give more exposure to right-tail events (e.g. cocoa) rather than diluting tails.  #mech/risk_premium
  > with increased diversification we get an initial drop in curtosis and then a ramping up of curtasis
  indicator: portfolio kurtosis vs number of markets · asset: multi · direction: maximal diversification across markets · horizon: years · testable: yes - kurtosis vs breadth · confidence: medium
  ^MT224-C20-1

### C21
- **Rich Brennan** Using 125 years of Dow and S&P data, major moves hold the information and the rest is noise; larger samples expose bigger fractal structures, so drawdowns and returns ahead are larger than those seen.  #mech/risk_premium
  > the major material moves, the tail properties that Dave um is convincing us about, and I totally agree with him, they are the major drivers.
  indicator: 125 years of Dow Jones and S&P 500 data · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT224-C21-1
- **Dave Dredge (CIO Convex Strategies, options/convexity)** Convex Strategies frees clients' capital from poor diversifiers into explicit negative-correlation hedges so clients keep positive drift assets and the combination provides long gamma on the combined portfolio.  #mech/risk_management
  > I'm creating the trend following type benefit for our investors as opposed to running it ourself.
  indicator: negatively correlated hedge overlay · asset: multi · direction: long convexity overlay · horizon: years · testable: partly · confidence: high
  ^MT224-C21-2
- **Dave Dredge (CIO Convex Strategies, options/convexity)** Long-dated options are mispriced because volatility supply is dominated by price-insensitive structured-product sellers; buying a multi-year strip at a fixed price captures a triple mispricing (distribution, supply, product nonlinearity) and the seller may want to unwind after one tail.  #mech/risk_premium
  > we're buying longdated term periods of the missed pricing of the underlying distribution which itself is driven by the supply of volatility dominated by non-prics sensitive participants
  indicator: long-dated implied volatility vs distribution · asset: multi · direction: long long-dated options · horizon: years · conditions: where structured product supply depresses prices · testable: partly · confidence: medium
  ^MT224-C21-3

### C22
- **Dave Dredge (CIO Convex Strategies, options/convexity)** When positively convex, additional risk reduces total risk; the price of convexity is driven by non-price-sensitive participants; opposing views are welcome as convexity can be bought on either side.  #mech/risk_management
  > when you're positively convex, more risk is less risk.
  indicator: convexity · asset: multi · testable: no · confidence: high
  ^MT224-C22-1
- **Rich Brennan** Trend following and long options both truncate the left tail and leave the right tail open; stop-loss longs are synthetic calls; trend followers pay an implicit premium via whipsaws and foregone growth, with gap risk that options avoid.  #mech/risk_premium
  > truncate that left tail as we do it with our stops. We do it with our small bets.
  indicator: stop-loss as synthetic option · asset: multi · testable: partly · confidence: high
  ^MT224-C22-2

### C23
- **Dave Dredge (CIO Convex Strategies, options/convexity)** Long volatility and trend are complementary (different distribution parts and attachment points; trend has wider market breadth, options need efficient vol markets); combining them improves convexity.  #mech/risk_management
  > Every way you can add convexity add convexity.
  indicator: long vol plus trend combination · asset: multi · direction: combine long vol and trend · testable: partly · confidence: high
  ^MT224-C23-1

### C24
- **Rich Brennan** A 50/50 mix of S&P 500 and trend following (or long vol) yields almost the sum of the returns rather than the average because the correlation is negative in crises.  #mech/risk_premium
  > if you add the S&P and you know 50% 50% on capital, uh it's not just the average, it's almost the sum of the two.
  indicator: 50/50 S&P 500 plus trend · asset: multi · direction: combine equities with trend/long vol · horizon: years · testable: yes - blended portfolio backtest · confidence: medium
  ^MT224-C24-1
- **Dave Dredge (CIO Convex Strategies, options/convexity)** Fiduciary incentives should shift from calendar-year arithmetic returns to geometric wealth growth; do not optimise to a backward-looking expectation but build resilience by learning by doing.  #mech/behavioral
  > Expected return is a nonsensical number and it's destroyed more wealth for capital owners than maybe any other simple thing.
  asset: multi · testable: no · confidence: high
  ^MT224-C24-2
- **Rich Brennan** Cap leverage in absolute terms to break the automatic link between a quiet market and a large position, since most capital destruction comes from too much leverage in quiet markets.  #mech/risk_management
  > cap leverage in absolute terms
  indicator: absolute leverage cap · asset: multi · direction: cap leverage · testable: yes - compare to vol-target · confidence: high
  ^MT224-C24-3

### C25
- **Rich Brennan** Size every market to equal risk instead of tilting to the apparently strongest edge, because edge differences are smaller than estimation noise and tilting rebuilds a single cable and misses cocoa-like explosions.  #mech/risk_management
  > size every market with the same risk rather than tilting towards whichever edge looks currently strongest
  indicator: equal-risk weights vs edge-weighted · asset: multi · direction: equal risk across markets · testable: yes - test edge-weighted vs equal · confidence: high
  ^MT224-C25-1
- **Rich Brennan** Grow return by adding unrelated systems/markets rather than scaling existing bets; and enter small, letting open profit build the position.  #mech/risk_management
  > grow by widening the book, not by scaling the bets.
  indicator: number of independent bets · asset: multi · direction: add breadth, pyramid from open profit · testable: yes · confidence: high
  ^MT224-C25-2
- **Rich Brennan** Always enter positions small and let open profit build the position, so the market rather than leverage does the heavy lifting and individual bets stay small relative to estimation error.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > always enter small and let the market build the position out of open profit
  indicator: position size vs open profit · asset: multi · direction: pyramid on winners · testable: yes - test entry size and pyramiding rules · confidence: high
  ^MT224-C25-X1

### C26
- **Dave Dredge (CIO Convex Strategies, options/convexity)** Leverage on concave positions (low correlation in good markets, rising in bad) creates volatility drag and disasters; adding non-recourse leverage in the form of options on convex hedges is risk-reducing, enabling portable alpha / return stacking with trend or long vol.  #mech/risk_management
  > most people are levering concave risks.
  indicator: portable alpha, return stacking · asset: multi · direction: add convex overlay then take more equity risk · horizon: years · conditions: convexity must be genuine · testable: partly · confidence: high
  ^MT224-C26-1
- **Rich Brennan** Brennan views long-vol overlays on traditional portfolios as a band-aid; ideally rebuild the portfolio from first principles.  #mech/risk_management
  > I'm 100% trend so I never have to face this demon
  asset: multi · testable: no · confidence: medium
  ^MT224-C26-2
- **Niels Kaastrup-Larsen** Trend following (and by extension long volatility) acts as the enabler that lets investors keep holding equities through drawdowns, yet most investors have not adopted either strategy.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > trend following allows you to own equities.
  asset: equities · horizon: years · testable: partly - equity plus trend portfolio drawdown vs equity alone · confidence: medium
  ^MT224-C26-X1

### C28
- **Dave Dredge (CIO Convex Strategies, options/convexity)** Dredge's closing view: risk is managed by accountability and tacit knowledge, not by magic models; embedding VaR in BIS capital rules removed accountability and invited the GFC.  #mech/risk_management
  > risk is about accountability
  indicator: value at risk · asset: multi · testable: no · confidence: high
  ^MT224-C28-1
- **Niels Kaastrup-Larsen** Risk is everything not in your backtest.  #mech/research_method
  > risk is everything you didn't think of
  asset: multi · testable: no · confidence: high
  **Correction (cross-check):** Origin: 'risk is everything you didn't think of / not in your back test' is Dredge's line, said by the host quoting him ('you often remind everybody') and confirmed by Dredge ('That's right'). → Dave Dredge's maxim, quoted by the host and confirmed by Dredge: risk is everything you did not think of, everything not in your backtest.
  ^MT224-C28-2

