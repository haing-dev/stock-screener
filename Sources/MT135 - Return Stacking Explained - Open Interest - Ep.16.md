---
source_id: MT135
title: "Return Stacking Explained - Open Interest - Ep.16"
date: 2025-06-07
channel: "Top Traders Unplugged"
url: 
words: 11510
claims: 54
added_by_crosscheck: 17
corrections: 4
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Cory Hoffstein (Newfound Research / Return Stacked)", "Adam Butler (Resolve Asset Management / Return Stacked)", "Moritz (Open Interest host)", "Moritz (co-host, Takahi Capital partner)"]
tags: [source, layer0]
---
# Return Stacking Explained - Open Interest - Ep.16

**Speakers:** Cory Hoffstein (Newfound Research / Return Stacked); Adam Butler (Resolve Asset Management / Return Stacked); Moritz (Open Interest host); Moritz (co-host, Takahi Capital partner)

**Summary:** Open Interest ep.16 (Apr-Jun 2025): return stacking and portable alpha ETFs; top-down and bottom-up replication of the SG Trend Index; ETF capacity and liquidity; stacking limits; merger arbitrage and gold/Bitcoin overlays.

**Approach:** return stacking, replication, trend following, portable alpha, merger arbitrage

**Cross-check completeness estimate of first read:** 0.80 - first reader captured every main design point (return stacking, wrapper limits, bottom-up and top-down replication, blend, 18f-4, merger arbitrage, overlays); missed supporting reasons (blend motivation, wrapper trade-offs, dispersion sources, funded beta, fee squeeze) and mislabelled several speakers in the Cory/Adam exchange.

## Argument map

**Episode thesis:** Cory Hoffstein and Adam Butler (Return Stacked) argue that portable alpha, packaged as capital-efficient ETFs ('return stacking'), lets investors keep core stock and bond beta while adding diversifying return streams such as trend, carry and merger arbitrage. Their trend product replicates the SG Trend Index beta cheaply by blending a bottom-up fitted trend model (70%) with a top-down regression on recent index returns (30%), because the two have comparable fit but weakly correlated tracking errors; generic trend beta is becoming a commodity that performance-fee managers must beat with differentiated, fat-tail, or faster strategies.

### Cory Hoffstein (Co-founder, Return Stacked Portfolio Solutions (joint venture) and Newfound Research; product designer of the ETF suite)
Fingerprint: #approach/replication_indexing #approach/portfolio_construction_stacking #approach/trend_following #approach/diversification_risk_parity #approach/costs_execution #approach/manager_selection_allocation #approach/structural_themes #approach/behavioral_sentiment
_Speaker note: Captions give no names, so attribution rests on dialogue cues. Several passages were corrected in the ledger to Cory (C07-3 data window, C09-2 fat-tail attenuation, C13-2 and C13-3 high-vol overlay and client tolerance); those corrections are applied here. Where a passage runs on without a visible change of speaker, attribution is uncertain._

**Worldview premises**
- Portable alpha (return stacking) lets investors keep core stock and bond beta and free capital through futures and swaps for other alpha sources; it has been an institutional tool for about 40 years and a ticker packages it for people who will not run a derivatives book. _[institutional, stated; support: History from PIMCO in the 1980s; his own career building alternatives.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C02-1|C02-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C02-X1|C02-X1]])
- Selling alternatives by asking investors to sell some core stocks and bonds repeatedly disappointed in the 2010s (non-stop US 60/40 outperformance); a capital-efficient stack removes that behavioural obstacle. _[behavioural, stated; support: Own experience in the 2010s.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C02-2|C02-2]])
- Dispersion among trend managers comes from implementation choices (markets, speeds, risk weights, constraints); fitting parameters to the index removes arbitrary dispersion and delivers 'trend beta'. _[theoretical, stated; support: Design rationale for the replication.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C07-X1|C07-X1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C09-X1|C09-X1]])
- The SG Trend Index is made of the largest managers, whose less liquid markets matter little to P&L, so a limited-market replication tracks them well; around 80% of their risk sits in the same ~20 markets and fat-tail weights average toward zero across managers. _[empirical, stated; support: Reasoning from managers' scale; coffee in 2023-24 as an idiosyncratic bet that averaged out.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C08-2|C08-2]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C09-2|C09-2]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C09-1|C09-1]])
- Fitting trend weights needs 15-20 years of data because markets can contribute no P&L for a decade, making it impossible to tell untraded markets from untrending ones; annual reruns will not change weights meaningfully. _[empirical, stated; support: Training on 2000-10 versus 2010-20 gives different market weights.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C07-3|C07-3]])
- A top-down regression is flexible and captures manager innovation and unobserved markets but is backward-looking, blind to positions in markets with no recent P&L, and untethered mechanically from trend following. _[theoretical, stated; support: Example of the 2023 regional bank crisis when managers flipped bond positions within 2-3 days; Swiss franc approximated by gold and euro.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C10-1|C10-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C10-2|C10-2]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C10-X1|C10-X1]])
- A bottom-up model and a top-down regression track the trend index about equally well but have weakly correlated tracking errors, so blending 30% top-down and 70% bottom-up lowers aggregate tracking error; the blend is still a trend following strategy. _[empirical, stated; support: Tracking error and correlation results quoted (tracking-error correlation about 0.2-0.3 in the captions).]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C10-3|C10-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C11-X1|C11-X1]])
- Top-down regression struggles with fast multi-day mean-reversion models in the broader CTA index, so replicating the CTA index bottom-up is harder than replicating the trend index; Andrew Beer's fund uses only top-down. _[empirical, stated; support: Statistical power argument (20-40 contracts, 20-40 days).]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C11-2|C11-2]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C11-X2|C11-X2]])
- Generic trend beta can be bought in QIS for 10-15 bp, so performance-fee managers must differentiate (spreads, breakouts, speed, fat-tail markets); generic trend managers will be squeezed out by cheaper implementations. _[institutional, stated; support: Conversations with institutions buying trend beta from banks.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C12-4|C12-4]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C12-X1|C12-X1]])
- A longer tail of markets raises Sharpe but diverts risk from markets tied to big macro factors, reducing the crisis offset (citing Quantica). _[empirical, stated; support: Quantica research cited from memory.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C12-3|C12-3]])
- A high-volatility trend strategy is a capital-efficient version of a low-vol one, but most clients cannot tolerate more than about 10% vol (citing Cliff Asness), so products moved to 10-12% vol. _[behavioural, stated; support: Observation of institutional products; 50-vol example.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C13-2|C13-2]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C13-3|C13-3]])
- Stack only low-correlation components (equity plus trend); regulation (SEC Rule 18f-4: 20-day 99% VaR capped at 20% or 2x the benchmark) limits how far stacking can be pushed. _[institutional, stated; support: Regulatory rule description.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C14-1|C14-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C14-2|C14-2]])
- Merger arbitrage earns a spread consisting of time value of money plus a deal-break risk premium (about 200-250 bp over SOFR in 20 years) with low correlation to equity, bond and credit premia (about 0.5 to credit). _[empirical, stated; support: Generic strategy history; no source cited.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C15-1|C15-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C15-2|C15-2]])
- An ETF cannot be closed, so the strategy must run identically at small and large size; at extreme scale performance would degrade and self-correct. _[institutional, stated; support: Structural fact of ETFs; wants track record continuity.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C05-3|C05-3]])
- Diversifying strategies (trend, carry, merger) and diversifying assets (gold, Bitcoin) are different overlay buckets for stock-bond portfolios; gold and Bitcoin are a store-of-value diversifier. _[theoretical, stated; support: Product roadmap logic.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C16-2|C16-2]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C17-1|C17-1]])
- Futures-based ETF trend products use a subset of the most liquid US and European markets versus the full set in mutual fund and hedge fund versions. _[institutional, stated; support: Observation of competitor products.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C03-2|C03-2]])

**Chain: Portable alpha raises adoption of alternatives**
1. Advisers told to sell core stocks and bonds to fund alternatives → constant disappointment against US 60/40 and abandonment: Behavioural: investors abandon the alternative when core outperforms. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C02-2|C02-2]])
2. Futures and swaps free capital (capital efficiency) → keep core beta and add alternative alpha on top: Same dollar earns beta plus overlay. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C02-1|C02-1]])
3. Tickerised ETF wrapper → accessible to wealth managers and individuals: No derivatives book to manage. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C02-X1|C02-X1]])
- Evidence: Conceptual; history of portable alpha since the 1980s.
- Fails when: Stacked components correlated with each other in a drawdown (equity and trend falling together in April 2025); constrained by SEC VaR rule.

**Chain: Why 30% top-down and 70% bottom-up**
1. Top-down regression follows manager innovation and unobserved markets → flexible and adaptive tracking: Does not need to know how managers build weights. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C10-1|C10-1]])
2. Top-down looks back 20-40 days and cannot see markets with no recent P&L → lags regime shifts (2023 bank crisis) and has blind spots: Regression needs variance. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C10-2|C10-2]])
3. Bottom-up fits time-series momentum lookbacks to the index → mechanistic trend process with about 0.8 daily correlation: Parameters fitted over 15-20 years. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C07-3|C07-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C09-3|C09-3]])
4. Weakly correlated tracking errors of the two → blend reduces tracking error and adds process diversification: Pros and cons are almost opposite. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C10-3|C10-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C10-X1|C10-X1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C11-X1|C11-X1]])
- Evidence: Tracking error and correlation tests reported; statistically indistinguishable fit.
- Fails when: If all managers shift speed or markets at once, a fixed bottom-up fit does not adapt (host point); fast mean-reversion in a broad CTA index defeats the top-down regression.

**Chain: Limited universe still tracks the trend beta**
1. The index holds large managers who trade in proportion to liquidity → less liquid markets contribute little to aggregate P&L: Scale limits fat-tail impact. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C08-2|C08-2]])
2. 80% of risk in the same ~20 markets; fat-tail weights differ across managers → fat-tail weights average toward zero: Not all managers trade the same signals. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C09-2|C09-2]])
3. Common markets cover 70-80% of global futures liquidity → 26-27 markets replicate the full universe closely: All players trade in proportion to liquidity. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C05-2|C05-2]])
- Evidence: Replication results; coffee 2023-24 as an example of offsetting dispersion.
- Fails when: Idiosyncratic bets create temporary dispersion (coffee).

**Chain: Commoditisation of trend beta**
1. Replication ETFs and QIS deliver trend beta at low cost (10-15 bp) → performance-fee managers must beat the cheap benchmark over the long run: Beta is the beta. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C12-4|C12-4]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C12-2|C12-2]])
2. Generic trend charges performance fees → squeezed out; room remains for spreads, breakouts, speed, fat tail: Differentiation required. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C12-X1|C12-X1]])
3. Longer tail of markets → higher Sharpe but weaker crisis offset: Risk budget moves away from macro-factor markets. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C12-3|C12-3]])
- Evidence: Quantica paper; institutional conversations.
- Fails when: Not stated.

**Chain: Merger arbitrage as a stacked return stream**
1. Deal announced at a buyout price → target trades below the price: Time value of money plus deal-break credit-like risk. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C15-1|C15-1]])
2. Capture the spread → about 200-250 bp over SOFR historically with low correlation to other risk premia: Risk premium for bearing deal failure. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C15-1|C15-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C15-2|C15-2]])
3. Machine-learning screen on spread, acquirer and industry → index of deals clearing a return hurdle: Estimate close probability and expected return. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C16-1|C16-1]])
4. Share-component deals need a hedge → short or swap on the acquirer; swaps avoid borrow and recall risk: ETF constraint on locating shares. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C16-1|C16-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C16-X1|C16-X1]])
- Evidence: Generic strategy history and the licensed Alpha Beta index.
- Fails when: Deal breaks; short-leg recall.

**Decision process**
- [portfolio] Offer building blocks that stack an overlay on a core exposure (equity plus trend, bond plus trend, bond plus merger, equity plus multi-asset carry, equity plus gold and Bitcoin) so wealth managers build portfolios.. Why: Keep beta, add diversifiers without giving up core. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C02-1|C02-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C16-2|C16-2]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C17-1|C17-1]])
- [signal] Replicate the SG Trend Index with a 70% bottom-up fitted trend model and 30% top-down robust regression, rebalanced daily.. Why: Blend lowers tracking error and adds process diversification. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C10-3|C10-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C11-X1|C11-X1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C09-3|C09-3]])
- [universe] Run 26-27 liquid futures markets spanning equity, bond, commodity and currency; keep the same universe at all sizes; use back-month contracts to expand capacity beyond CFTC front-month limits.. Why: Replicates the full universe closely; ETF cannot close. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C05-2|C05-2]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C05-3|C05-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C05-1|C05-1]])
- [research] Fit trend weights using 15-20 years of data and cross-validation; rerun annually without expecting material weight changes; check for systematic drift in trend length.. Why: Shorter windows give unstable market weights. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C07-3|C07-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C08-1|C08-1]])
- [execution] Trade the ETF as a one-way buy and hold; use institutional desks for NAV-based or risk quotes for size; accept 20-30 bp spreads for small trades.. Why: Market makers widen quotes when they cannot see the basket. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C04-1|C04-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C04-X1|C04-X1]])
- [risk] Stack only low-correlation components; respect SEC Rule 18f-4 VaR limits; rebalance nightly; keep collateral for the trend overlay at 25-30% of NAV with a cash buffer.. Why: Ruin risk negligible and margin does not force sales in a drawdown. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C14-1|C14-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C14-2|C14-2]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C14-3|C14-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C14-X1|C14-X1]])
- [sizing] Target trend volatility of about 10-13.5% (stack on S&P with a 13.5% vol trend system) because clients cannot tolerate more.. Why: Line-item risk too large above about 10% vol. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C13-3|C13-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C14-3|C14-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C13-2|C13-2]])
- [universe] Use the mutual fund version for a wider and more diverse set of futures markets than the ETF; ETF wrapper for tax advantage and intraday access.. Why: ETF market-maker hedging limits illiquid markets. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C03-1|C03-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C03-X2|C03-X2]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C09-X1|C09-X1]])
- [other] Merger arbitrage via a licensed machine-learning index of US-listed deals that clear a hurdle rate, hedged short or via swaps for stock components.. Why: Systematic deal selection; avoids borrow risk. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C16-1|C16-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C16-X1|C16-X1]])

**Evidence style:** Backtest-style replication statistics (correlation about 0.8, tracking error, cross-validation), design rationale and regulatory/operational detail; cites others' research (Quantica, Asness) from memory; reasoning about industry structure and fees.

**Views at the time**
- (2025-04-15) Replication ETFs form a fair, cheap benchmark; generic trend with performance fees will be squeezed; differentiation lies in the fat tail, spreads and breakouts.. Reasoning: Trend beta available for 10-15 bp in QIS. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C12-4|C12-4]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C12-X1|C12-X1]])
- (2025-04-15) Gold and Bitcoin overlay on US equity is a store-of-value diversifier for a stock-bond portfolio; gold in particular a long-term diversifier.. Reasoning: Thematic store-of-value narrative; diversifying assets bucket. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C17-1|C17-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C16-2|C16-2]])
- (2025-04-15) Merger arbitrage is a diversifying return stream worth stacking on bonds.. Reasoning: Low correlation to equity, bond and credit premia. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C15-2|C15-2]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C16-1|C16-1]])
- (2025-04-15) April 2025: a drawdown in the CTA space after equities fell; may be early innings with recovery in 30-50 days (host view); the stacks showed no dislocation.. Reasoning: Nightly rebalancing and collateral buffers (Adam). ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C14-3|C14-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C13-X1|C13-X1]])

### Adam Butler (Co-founder, Return Stacked Portfolio Solutions; Resolve Asset Management Global (futures-based alternatives, risk parity and active strategies))
Fingerprint: #approach/replication_indexing #approach/trend_following #approach/research_robustness_overfitting #approach/costs_execution #approach/portfolio_construction_stacking #approach/position_sizing_vol_target #approach/diversification_risk_parity
_Speaker note: Captions give no speaker labels; attribution follows dialogue cues and ledger corrections (C07-3, C09-2, C13-2, C13-3 moved to Cory). Adam leads the bid-ask, bottom-up regression, validation and margin-management answers._

**Worldview premises**
- Mutual fund wrappers can trade a wider futures set than ETFs because ETF market makers need liquid hedges for creations and redemptions; the choice is a trade-off between tax efficiency, intraday liquidity and platform access versus market breadth. _[institutional, stated; support: Operational experience running both.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C03-1|C03-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C03-X2|C03-X2]])
- Spreads of small ETF trades in a less liquid futures basket average 20-30 bp and widen in stress, and are persistent because market makers cannot see the basket; large trades through institutional desks can be done near NAV, and a long holding period smooths the cost. _[experience, stated; support: Own fund trading experience.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C04-1|C04-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C04-X1|C04-X1]])
- Any fund faces a capacity trade-off: more diverse bets raise expected performance but liquidity limits what can trade at size; CFTC front-month limits can be bypassed using back-month contracts for 10x or more capacity. _[institutional, stated; support: Practical knowledge of futures limits.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C05-X1|C05-X1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C05-1|C05-1]])
- A 26-27 market universe covering equities, bonds, commodities and currencies (70-80% of global futures liquidity) replicates the full CTA universe closely because all players trade in proportion to liquidity; he admits being surprised. _[empirical, stated; support: Replication research.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C05-2|C05-2]])
- A grid of time-series momentum lookbacks (5-300 days per market) can span continuous moving-average-crossover rules, so regressing on it can mimic them; breakout systems with trailing stops and entry-only vol scaling have far more degrees of freedom and are not spanned. _[theoretical, stated; support: Design reasoning.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C06-1|C06-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C06-X1|C06-X1]])
- The bottom-up replication gets about 0.8 daily correlation to the SG Trend Index (an average of 10 funds with different styles). _[empirical, stated; support: Own regression fit since 2000.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C07-1|C07-1]])
- Fitted market weights change by decade (S&P trendless in 2000-10, trendy 2010-20) but sector weights and trend speeds are stable under cross-validation, and there is no evidence that trend length rose systematically over 2000-2020 (considered 'largely mythical'). _[empirical, stated; support: Cross-validation tests across training windows.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C08-1|C08-1]])
- Top-down is kept as an expression of epistemological humility: managers constantly innovate and it captures idiosyncratic methods the continuous bottom-up misses, even though the bottom-up has the better average fit. _[theoretical, stated; support: Comparison of fit on the trend index.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C11-1|C11-1]])
- Carry, skewness, seasonality and relative-value features improve the fit to the broader CTA index far more than to the trend index, where the gain is marginal. _[empirical, stated; support: Own bottom-up experiments.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C12-1|C12-1]])
- Nightly rebalancing keeps the beta/trend ratio fixed after losses; trend collateral needs only 25-30% of NAV with a 40-50% cash buffer, so risk of ruin is negligible, as seen in the April 2025 drawdown. _[experience, stated; support: Audit of performance, margin use and balance in April 2025.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C14-3|C14-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C14-X1|C14-X1]])

**Chain: Bottom-up fitted trend model**
1. Build time-series trend strategies per market (5 to 300 day lookbacks) → span continuous moving-average and momentum rules: Weights on long and short averages replicate crossovers. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C06-1|C06-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C06-X1|C06-X1]])
2. Regress all strategies on the SG Trend Index since 2000 → risk weights by market and speed that best fit: Objective is to look like the index. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C06-1|C06-1]])
3. Result → about 0.8 daily correlation; intermediate speeds; roughly equal 25% sector risk weights: The average trend follower is sector balanced (Cory's description). ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C07-1|C07-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C07-2|C07-2]])
4. Check across training windows → sector weights and speeds stable: Market weights vary with decade because trendiness varies. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C08-1|C08-1]])
- Evidence: Regression results and cross-validation.
- Fails when: Breakout systems with trailing stops are not spanned; managers shifting style would not be tracked by a fixed fit.

**Chain: Why ETF spreads persist and capacity is limited**
1. Market makers cannot see the active futures basket → wide, thin quotes: Hedging illiquid markets across time zones is hard. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C04-X1|C04-X1]])
2. Small trades without a risk quote → 20-30 bp average spread, wider in stress: Cost of crossing the spread. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C04-1|C04-1]])
3. Hold for the long term → cost smooths out: One-way entry. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C04-1|C04-1]])
- Evidence: Own trading experience.
- Fails when: Chaotic markets or economic news widen spreads further.

**Chain: Stack margin management in a drawdown**
1. Portfolio loses value (100 to 97) → both beta and trend exposure scaled down nightly: Keeps the 1:1 ratio. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C14-3|C14-3]])
2. Cash-funded ETF beta plus S&P futures top-up → collateral always sufficient for the trend overlay: 25-30% collateral need versus 40-50% cash. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C14-3|C14-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C14-X1|C14-X1]])
- Evidence: April 2025 audit showed no dislocation.
- Fails when: Not stated.

**Decision process**
- [research] Regress per-market lookback strategies on the SG Trend Index and test stability across training windows and cross-validation; check for drift in trend length.. Why: Ensure the replication generalizes. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C06-1|C06-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C08-1|C08-1]])
- [universe] 26-27 liquid markets across four sectors; use back-month contracts to widen capacity.. Why: Replicates the full universe and scales. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C05-2|C05-2]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C05-1|C05-1]])
- [execution] Seek NAV-based or risk quotes through institutional desks for size; one-way entry.. Why: Tight fills for substantial size. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C04-1|C04-1]])
- [portfolio] Keep the top-down leg alongside the bottom-up leg to capture innovation and idiosyncratic methods; add features (carry, skew, seasonality) only if the target is the broader CTA index.. Why: Epistemological humility; marginal gain against the trend index. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C11-1|C11-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C12-1|C12-1]])
- [risk] Rebalance strategies nightly; fund equity beta with cash where efficient and top up with futures while holding enough collateral.. Why: Avoid margin-driven forced sales. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C14-3|C14-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C14-X1|C14-X1]])

**Evidence style:** Quantitative replication statistics (daily correlation about 0.8; cross-validation across 3/4 to 80% of data), operational track record of running the funds, and mechanical reasoning about market structure.

**Views at the time**
- (2025-04-15) April 2025 drawdown handled without dislocation in margin or the balance of beta and overlay.. Reasoning: Audit of margin consumption and balance. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C14-3|C14-3]])
- (2025-04-15) Replication of the trend index with a limited universe works and the sector weights generalise; the trend length did not drift over 2000-2020.. Reasoning: Cross-validation results. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C05-2|C05-2]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C08-1|C08-1]])

### Moritz (co-hosts; two people named Moritz) (Open Interest hosts (Moritz Seibert and his Takahi Capital partner Moritz Heiden as guest co-host))
Fingerprint: #approach/trend_following #approach/replication_indexing #approach/manager_selection_allocation #approach/position_sizing_vol_target #approach/costs_execution
_Speaker note: The ledger lists two Moritz speakers; captions do not separate them. They are merged here. They ask questions and add views on benchmark competition, volatility levels and the April 2025 drawdown._

**Worldview premises**
- Replication ETFs form a cheap benchmark that performance-fee hedge funds must beat over the long run; market forces squeezing generic trend managers are 'fair and square'. _[institutional, stated; support: Assertion.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C12-2|C12-2]])
- Trend funds now run 8-12% volatility, so returns lack the punch of 1980s-90s CTAs, trading off stress payoff; investors can no longer tolerate 20-25% volatility whereas 25 years ago equities at 20% volatility were fine. _[experience, stated; support: Observation of the industry.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C13-1|C13-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C13-R1|C13-R1]])
- A levered risk-parity bond and equity allocation and some QIS products already work as portable alpha, so investors may hold the concept unknowingly. _[theoretical, stated; support: Product analysis.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C03-X1|C03-X1]])
- A fixed bottom-up fit cannot adapt if managers change style, unlike a top-down regression; recalibration frequency is a design question. _[theoretical, stated; support: Challenge to the guests.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C07-X2|C07-X2]])
- As of 15 April 2025 the CTA space had a drawdown (equities and trend both falling); he hopes it is early innings and that trend recovers within 30-50 days. _[experience, stated; support: Recent P&L.]_ ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C13-X1|C13-X1]])

**Chain: Industry fee compression**
1. Cheap replication ETFs deliver trend beta → hedge funds charging performance fees must beat the ETFs: Beta available without performance fees. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C12-2|C12-2]])
- Evidence: None.
- Fails when: Luck component over short horizons.

**Decision process**
- [other] Prefers trading fat-tail or alternative markets, spreads and punchier higher-volatility returns for differentiation.. Why: Provide stress payoff that low-vol products lack. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C13-1|C13-1]])

**Evidence style:** Industry observation and challenge questions.

**Views at the time**
- (2025-04-15) CTA space in a drawdown on 15 April 2025, hoping for recovery within 30-50 days.. Reasoning: Equities and trend both fell. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C13-X1|C13-X1]])

### Disagreements
- **Relative quality of top-down versus bottom-up replication**: Cory Hoffstein: Both replicate the trend index about equally well (statistically indistinguishable) and the top-down works though it is mechanically untethered from trend; blend them for lower tracking error. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C10-3|C10-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C10-X1|C10-X1]]); Adam Butler: The bottom-up has the better average fit track record, but the top-down sometimes overwhelms it by catching idiosyncratic manager methods, which is why it is kept. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C11-1|C11-1]])
- **Whether a replication is 'divorced from trend following'**: Critics (as characterised by Cory): Replication is totally divorced from trend following. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C11-X1|C11-X1]]); Cory Hoffstein: The 70% bottom-up leg applies true trend signals fitted to the index and the 30% top-down leg adds process diversification. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C11-X1|C11-X1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C10-X1|C10-X1]])
- **Value of a long tail of markets**: Cory Hoffstein: The ETF delivers trend beta with a handful of common markets; a longer tail raises Sharpe but weakens crisis offset; fat-tail trading is for managers adding alpha. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C09-X1|C09-X1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C12-3|C12-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C09-2|C09-2]]); Moritz (co-hosts): They like trading fat-tail and alternative markets, spreads and punchier returns; the question is how much stress payoff you want. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C13-1|C13-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C13-R1|C13-R1]])
- **Recalibration of a fixed bottom-up fit**: Moritz (co-hosts): A fixed fit has no response function if managers change speed or markets. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C07-X2|C07-X2]]); Cory Hoffstein: It is non-trivial; 15-20 years are needed and annual reruns will not change weights meaningfully. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C07-3|C07-3]]); Adam Butler: Sector weights and speeds were stable in cross-validation and no systematic lengthening of trend speeds was found. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C08-1|C08-1]])

### Gaps and conflicts
- Speaker attribution is uncertain for several passages (ledger corrections move C07-3, C09-2, C13-2, C13-3 to Cory). ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C07-3|C07-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C09-2|C09-2]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C13-2|C13-2]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C13-3|C13-3]])
- The 0.8 daily correlation is in-sample against an average of 10 funds; the quoted tracking-error correlation (about 2.3 in the captions, likely 0.2-0.3) is garbled and no out-of-sample figure is given. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C07-1|C07-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C10-3|C10-3]])
- Fitting needs 15-20 years but the weights are said to be stable under cross-validation; training on 2000-10 versus 2010-20 gave different market weights, so stability applies only at sector and speed level. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C07-3|C07-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C08-1|C08-1]])
- Claim that 26-27 markets replicate the full universe 'closely' is not quantified. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C05-2|C05-2]])
- Spread estimates of 20-30 bp are given as typical without data and assume small trades. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C04-1|C04-1]])
- Merger arbitrage return (200-250 bp over SOFR) and correlation of 0.5 to credit are stated without sources. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C15-1|C15-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C15-2|C15-2]])
- Whether adding carry, skew, seasonality features to the bottom-up model is justified is left open: marginal against the trend index but material against the CTA index. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C12-1|C12-1]])
- The statement that ETF performance would 'self-correct' at $20bn or more is unsupported by capacity analysis. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C05-3|C05-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C05-X1|C05-X1]])
- Top-down regression blind spots (no P&L in markets over the lookback) are acknowledged, with only a vague 'things you can do to manage around that'. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C10-2|C10-2]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C11-X2|C11-X2]])
- Claim that stacking ruin risk is negligible rests on one April 2025 episode. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C14-3|C14-3]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C14-X1|C14-X1]])
- Gold and Bitcoin are treated as diversifying assets with a store-of-value narrative but no evidence is given. ([[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C17-1|C17-1]], [[MT135 - Return Stacking Explained - Open Interest - Ep.16#^MT135-C16-2|C16-2]])

### Forward-looking inputs (reader synthesis)
(reader) The speakers are product builders rather than forecasters. Observable inputs they use: the daily SG Trend Index and the CTA index returns (regressed on a recent 20-40 day window), fitted risk weights by sector (about 25% each), trend speeds (intermediate), merger-arbitrage spread and deal-close probability features, and bid-ask spreads and NAV premia for ETF execution. They offer no price forecasts; the April 2025 hope for a trend recovery in 30-50 days is a host remark.

### Reader inferences (not stated by the speakers)
- (reader) The central argument is that trend 'beta' is largely determined by a small set of common markets and speeds, so it is replicable and will be priced like beta; alpha is claimed only in the fat tail and differentiated design.
- (reader) The 30/70 blend is a process-diversification decision: neither method is shown to dominate, and the blend reduces tracking error by combining weakly correlated errors.
- (reader) The guests have a commercial interest in the replication and stacking products, so claims about the adequacy of limited universes and negligible ruin risk are framed by that interest.
- (reader) Several mechanics (SEC 18f-4 VaR cap, CFTC front-month limits, ETF creation/redemption) bound the design, so practical constraints rather than signal quality drive many choices.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | preview of later point (30/70 blend), intro, guest background |
| C02 | 2 | portable alpha and return stacking concept |
| C03 | 2 | ETF vs mutual fund; ETF liquidity |
| C04 | 1 | bid-ask spreads and ETF trading |
| C05 | 3 | capacity, CFTC limits, universe size, no closing |
| C06 | 1 | bottom-up replication method |
| C07 | 3 | bottom-up fit, resulting weights, recalibration |
| C08 | 2 | stability of fitted weights; market set limits |
| C09 | 3 | dispersion, fat-tail markets, top-down method |
| C10 | 3 | top-down pros/cons; blend |
| C11 | 2 | rationale for blend; CTA index replication |
| C12 | 4 | feature families, ETFs as benchmark, crisis offset |
| C13 | 3 | vol levels, high-vol trend, client vol tolerance |
| C14 | 3 | stacking limits, 18f-4, margin |
| C15 | 2 | April drawdown ops; merger arbitrage |
| C16 | 2 | merger arb index; gold/Bitcoin product |
| C17 | 1 | gold plus Bitcoin overlay; outro |

## Claims

### C02
- **Cory Hoffstein** Portable alpha / return stacking keeps core stock and bond beta and uses futures, swaps and capital efficiency to free capital for other alpha sources (trend, carry, merger arb).  #mech/risk_management
  > how can you keep your beta in your portfolio, the core stocks and bonds that institutions are building their strategic asset allocation around, but search for alpha in more fruitful places
  indicator: return stacking · asset: multi · direction: long stocks/bonds plus overlay · horizon: years · testable: yes - backtest overlay on 60/40 · confidence: high
  ^MT135-C02-1
- **Cory Hoffstein** Selling alternatives by asking investors to cut stocks and bonds failed in the 2010s; a capital-efficient stacked product avoids that behavioural obstacle.  #mech/behavioral
  > struggled against the non-stop outperformance particularly here in the US of a core US6040
  asset: multi · horizon: years · conditions: strong US 60/40 period · testable: no · confidence: medium
  ^MT135-C02-2
- **Cory Hoffstein** Portable alpha was an institutional tool for about 40 years and out of reach for individuals and wealth managers who will not run a derivatives book; return stacking packages it as a ticker so the capital-efficient structure can be bought without managing the derivatives.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > has largely been out of the reach for most individuals and wealth managers who aren't going to manage a book of derivatives themselves
  indicator: portable alpha / return stacking wrapper · asset: multi · horizon: years · conditions: Needs a fund wrapper that runs the derivatives. · testable: no - product description · confidence: high
  ^MT135-C02-X1

### C03
- **Adam Butler** Mutual fund wrappers can trade a wider futures set than ETFs because ETF market makers need liquid hedges for creations and redemptions.  #mech/liquidity_flows
  > the mutual fund strategies are able to trade a a slightly wider and more diverse group of futures markets
  asset: multi · testable: no · confidence: high
  ^MT135-C03-1
- **Cory Hoffstein** Futures-based ETF trend products use a subset of the most liquid US and European markets versus the full set in their mutual fund and hedge fund versions.  #mech/structural_shift
  > most of the futures based products that are coming out from Alpha Simplex and ManHL and Invesco and Black Rockck tend to be subset a
  asset: multi · testable: no · confidence: high
  ^MT135-C03-2
- **Moritz (co-host)** A levered risk-parity bond and equity allocation (and some QIS products) already works as a portable-alpha product, so investors may hold the concept without knowing it; return stacking makes it explicit.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > a risk parity type of bond and equity allocation depending on which level volume run it on um is something like a portable alpha product at the end of the day
  indicator: risk parity as stacking · asset: multi · conditions: Depends on the volatility target and leverage used. · testable: partly - risk parity exposure decomposes into stacked beta · confidence: medium
  ^MT135-C03-X1
- **Adam Butler** Wrapper choice is a trade-off: an ETF gives tax efficiency, intraday liquidity and easy platform access, whereas a mutual fund (end-of-day NAV) can trade a wider futures set; the same strategy can run in both.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > the ETF wrapper has some tax advantages. It has the intraday liquidity. It has the ease of platform access etc.
  indicator: ETF vs mutual fund wrapper · asset: multi · direction: ETF for access, mutual fund for market breadth · conditions: US tax treatment; Europe lacks the ETF tax advantage. · testable: no - structural trade-off · confidence: high
  ^MT135-C03-X2

### C04
- **Adam Butler** Small-size ETF trades in less liquid futures baskets face bid-ask spreads of 20-30 bp on average and wider in stress; large trades via institutional desks can be done near NAV, and holding long term smooths cost.  #mech/risk_management
  > badass spreads of 20 30 [L160] basis points on average I don't think are unusual
  indicator: ETF bid-ask spread · asset: multi · horizon: days · conditions: small trade size, chaotic markets · testable: yes - observe spreads · confidence: medium
  ^MT135-C04-1
- **Adam Butler** Because market makers cannot see the full basket of an active futures ETF, they widen and thin quotes, so wide spreads are a persistent feature, not a temporary one; the cost is worth it for a one-way buy-and-hold investor.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > The market makers are always going to whenever there's less uh transparency, they're going to widen out and thin out
  indicator: ETF bid-ask spread and basket transparency · asset: multi · direction: wider spreads with less transparency · conditions: Persistent when underlying markets are less liquid and traded daily. · testable: yes - spread vs basket transparency · confidence: medium
  ^MT135-C04-X1

### C05
- **Adam Butler** CFTC limits on front-month positions can be bypassed by trading back-month contracts, giving 10x or more capacity.  #mech/risk_management
  > CFTC limits that limit the number of contracts that can be held in the front month
  asset: multi · testable: yes · confidence: high
  ^MT135-C05-1
- **Adam Butler** A 26-27 market universe covering equities, bonds, commodities and currencies (70-80% of global futures liquidity) replicates the full CTA universe closely because all players trade in proportion to liquidity.  #mech/research_method
  > you can get pretty darn close in replication space with a much more finite universe of markets as long as you're spanning the equity index, bond index, commodity, and currencies
  indicator: replication with ~26 markets · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT135-C05-2
- **Cory Hoffstein** An ETF cannot be closed to inflows, so the strategy must be run identically at all sizes; at extreme scale performance would degrade and self-correct.  #mech/liquidity_flows
  > you can't close the ETF. So, we have to be able to run it at in theory infinite scale.
  indicator: capacity · asset: multi · conditions: very large AUM · testable: no · confidence: medium
  ^MT135-C05-3
- **Adam Butler** Any fund faces a capacity trade-off: more diverse bets raise expected performance, but liquidity limits what can be traded at size, so at some point the markets you can trade no longer matter to P&L; this holds for hedge funds, mutual funds and ETFs.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > there's a trade-off between accessibility, liquidity, and the diversity of bets that are available
  indicator: fund capacity vs market breadth · asset: multi · direction: breadth up, capacity down · conditions: Binding as assets grow. · testable: partly - capacity estimates need liquidity data · confidence: high
  ^MT135-C05-X1

### C06
- **Adam Butler** Bottom-up replication: for each market build time-series trend strategies with lookbacks from 5 to 300 days and regress them on the SG Trend Index (daily since 2000) to pick the weights that best fit.  #mech/research_method
  > we regressed all of these individual market individual trend length strategies on the societ general trend index over the very long term
  indicator: SG Trend Index regression · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT135-C06-1
- **Adam Butler** A grid of time-series momentum lookbacks can span continuous moving-average-crossover trend rules (long averages positive, short negative), so a regression on a lookback grid can mimic them; breakout systems with trailing stops and entry-only vol scaling have far more degrees of freedom and are not spanned.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > you can model a moving average cross by taking by weighting for example uh longer term moving averages positively and shorter term moving averages negatively
  indicator: time-series momentum lookback grid as basis for trend rules · asset: multi · conditions: Applies to continuous trend signals, not event-driven breakouts. · testable: yes - the span can be tested · confidence: medium
  ^MT135-C06-X1

### C07
- **Adam Butler** The bottom-up replication achieves about 0.8 daily correlation to the SG Trend Index, which is an average of 10 funds with differing styles.  #mech/research_method
  > the bottomup strategy actually does just a really good job with an average correlation daily correlation in the neighborhood of kind of 0.8
  indicator: SG Trend Index replication correlation · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT135-C07-1
- **Cory Hoffstein** Fitting to the SG Trend Index gives intermediate trend speeds and about equal 25% risk weights in equities, bonds, commodities and currencies, with commodity risk split evenly between metals and energies.  #mech/structural_shift
  > You get intermediate term trend speeds and you get 25% of your risk weight pretty much in equity indices, in bonds, in commodities, in currencies.
  indicator: fitted sector risk weights · asset: multi · direction: equal risk across four sectors · horizon: years · testable: yes · confidence: high
  ^MT135-C07-2
- **Adam Butler** Fitting trend weights needs 15-20 years of data because a market that produced no P&L in a decade cannot be distinguished from one managers did not trade.  #mech/research_method
  > for all the markets you're trading to have gone through meaningful periods of contributing positive or negative P&L
  asset: multi · horizon: years · testable: yes · confidence: high
  **Correction (cross-check):** Attributed to Adam Butler. The 15-20 year training-window answer comes from Cory's reply to the recalibration question; Adam only speaks from 'We also, when we were investigating this ...' and then says 'to Corey's point'. → Cory: fitting trend weights needs 15-20 years of data because a market that produced no P&L in a decade cannot be told apart from one managers did not trade, so rerunning each year will not change weights meaningfully.
  ^MT135-C07-3
- **Cory Hoffstein** Dispersion among trend managers comes from implementation choices: which markets, which trend speeds, how much risk weight per market and which constraints; a replication fits all these parameters to the index to remove arbitrary dispersion.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > that comes from what markets are you trading, what trend speeds are you trading, how much risk weight are you giving each market
  indicator: sources of trend manager dispersion · asset: multi · conditions: Cory's 30-second summary of the bottom-up approach. · testable: yes - dispersion attribution to markets, speed and weights · confidence: high
  ^MT135-C07-X1
- **Moritz (co-host)** A fixed bottom-up fit cannot adapt if the underlying managers change style (for example shifting to faster trends or different markets), unlike a top-down regression, so recalibration frequency is a design question.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > with the bottom up approach, you don't necessarily have that response function
  indicator: bottom-up vs top-down replication adaptiveness · asset: multi · horizon: years · conditions: Concern if the index managers' style shifts; Cory answers that annual reruns hardly change the weights. · testable: yes - refit on rolling windows · confidence: medium
  ^MT135-C07-X2

### C08
- **Adam Butler** Fitted market weights change by decade (S&P trendless in 2000-10, trendy 2010-20) but sector weights and trend speeds stay stable under cross-validation, and there is no evidence that trend length rose systematically 2000-2020.  #mech/research_method
  > the sector weight was still very consistent
  indicator: fitted weights over time · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT135-C08-1
- **Cory Hoffstein** The trend index consists of the largest managers, whose less liquid markets matter little to P&L, so a limited-market replication tracks them well.  #mech/liquidity_flows
  > as you grow in AUM the less liquid markets that you trade end up having a smaller impact on total portfolio P&L
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT135-C08-2

### C09
- **Cory Hoffstein** Idiosyncratic bets such as coffee in 2023-24 created manager dispersion that later reversed, and on average dispersion balances out.  #mech/cycle_persistence _(time-bound view)_
  > coffee was a big one, uh, in 2024, uh, and 2023
  indicator: coffee · asset: commodities · horizon: years · testable: yes · confidence: medium
  ^MT135-C09-1
- **Adam Butler** Large trend managers put about 80% of risk in the same ~20 markets, and averaging the fat-tail weights across managers attenuates toward zero, so the beta can be captured with a handful of common markets.  #mech/research_method
  > 80% of their risk weights probably in the same 20 markets we could all rattle off the top of our head
  indicator: risk weight concentration · asset: multi · horizon: years · testable: yes · confidence: medium
  **Correction (cross-check):** Speaker is given as Adam, but the passage continues without a break from the speaker who gave the coffee example (C09-1, Cory); no change of speaker is shown. → Same speaker as C09-1 (Cory): large trend managers put about 80% of risk in the same ~20 markets; averaging the fat-tail weights across managers attenuates toward zero, so the beta can be captured with a handful of common markets.
  ^MT135-C09-2
- **Cory Hoffstein** Top-down replication: run a robust regression of recent index returns on futures markets to find the long/short basket that mimics it, assuming weights hold one day ahead.  #mech/research_method
  > is a regressionbased approach, right? Where we're going to look at the most recent performance of something like the sock gen trend index
  indicator: robust regression of SG Trend Index on futures · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT135-C09-3
- **Cory Hoffstein** The ETF aims to deliver trend beta and beat the category over the long run through lower fees, while managers who want to add alpha should trade the fat tail of markets (which the mutual fund version does).  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > to deliver the beta of the category and we're trying to outperform that over the long run through feed differentials
  indicator: fee differential vs CTA beta · asset: multi · direction: lower fees give net outperformance of beta · horizon: years · conditions: Valid if the replication tracks the beta closely. · testable: yes - compare ETF net return with the index net of fees · confidence: medium
  ^MT135-C09-X1

### C10
- **Cory Hoffstein** Top-down regression is flexible and can approximate untraded markets (e.g. Swiss franc via gold and euro) and capture manager innovation.  #mech/research_method
  > it can capture the return of markets that we're not necessarily trading because of the way regression works
  asset: multi · horizon: days · testable: yes · confidence: high
  ^MT135-C10-1
- **Cory Hoffstein** Top-down weights lag by the 20-40 day lookback (regional bank crisis 2023 shift missed) and cannot see positions in markets with no recent P&L.  #mech/research_method
  > it is by definition rearward facing
  asset: multi · horizon: days · conditions: after sudden manager repositioning, flat markets · testable: yes · confidence: high
  ^MT135-C10-2
- **Cory Hoffstein** Top-down and bottom-up replicate the trend index equally well, but their tracking errors are weakly correlated, so a 30% top-down / 70% bottom-up blend lowers tracking error.  #mech/research_method
  > the two systems are almost identical, they're statistically indistinguishable
  indicator: blend of top-down and bottom-up replication · asset: multi · direction: blend 30/70 · horizon: years · testable: yes · confidence: high
  ^MT135-C10-3
- **Cory Hoffstein** The top-down regression works but is mechanically untethered from trend following, which is why a mechanistic bottom-up system with almost opposite strengths and weaknesses is added; the two have fairly uncorrelated tracking errors.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > but it's also untethered mechanically from trend following
  indicator: top-down regression replication · asset: multi · conditions: Top-down has no built-in trend rule. · testable: yes - tracking error correlation of the two methods · confidence: high
  ^MT135-C10-X1

### C11
- **Adam Butler** Top-down is kept because managers constantly innovate; it captures idiosyncratic methods the continuous bottom-up misses, even though bottom-up has better average fit.  #mech/research_method
  > the top down is an expression of epistemological humility
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT135-C11-1
- **Cory Hoffstein** Replicating the broader CTA index (with mean reversion, VIX trading, carry) is harder bottom-up; Andrew Beer's CTA fund uses only top-down.  #mech/research_method
  > I'll say it makes it harder to do the bottom up for sure.
  indicator: SG CTA index replication · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT135-C11-2
- **Cory Hoffstein** Replication is not divorced from trend following: the 70% bottom-up leg applies true trend signals with parameters fitted to the index, and the 30% top-down leg adds process diversification.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > Our replication approach is truly applying trend following signals. I think a lot of people get that wrong when they talk about replication
  indicator: blend of bottom-up (70%) and top-down (30%) · asset: multi · conditions: Cory's response to critics of replication. · testable: no - definitional claim · confidence: high
  ^MT135-C11-X1
- **Cory Hoffstein** A top-down regression struggles to capture the fast, multi-day mean-reversion models in the broader CTA index because 20-40 daily observations of 20-40 contracts are not enough to fit them, so it ends up capturing mostly the trend part.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > if they're using faster mean reversion models, it could be very difficult to pick that up
  indicator: top-down replication of the SG CTA index · asset: multi · direction: trend explains most of the CTA index but the mean-reversion part is missed · horizon: days · conditions: Gets worse as non-trend sleeves grow. · testable: yes - R-squared of CTA index regression on trend only · confidence: medium
  ^MT135-C11-X2

### C12
- **Adam Butler** Adding carry, skewness, seasonality and relative-value features improves fit to the CTA index much more than to the trend index, where the gain is marginal.  #mech/research_method
  > They improve the explanatory fit against the CTA index to a larger extent than they improve it relative to the trend index
  indicator: explanatory fit · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT135-C12-1
- **Moritz (co-host)** Replication ETFs form a cheap benchmark that performance-fee hedge funds must beat over the long run.  #mech/research_method
  > you better beat these ETFs who replicate, as you say, or who give access, costefficient access to the beta of our industry
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT135-C12-2
- **Cory Hoffstein** Per Quantica, a longer tail of markets raises Sharpe but diverts risk from markets tied to big macro factors, reducing crisis offset.  #mech/risk_management
  > because you're putting so much of your risk budget in this longer tale of markets, you don't necessarily get the same crisis offset
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT135-C12-3
- **Cory Hoffstein** Generic trend beta is available in QIS at 10-15 bp, so managers must differentiate through spreads, breakout, speed, or fat-tail markets.  #mech/structural_shift
  > those hedge funds that are doing very generic trend, uh, I think you're right, are just going to get squeezed out by lower cost
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT135-C12-4
- **Cory Hoffstein** Funds charging performance fees for generic trend will be squeezed out by cheaper implementations of the same beta, while fee room remains for managers with real innovation in fat-tail markets, spreads, breakouts and other differentiators.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > are just going to get squeezed out by lower cost, more efficient data implementations
  indicator: fee pressure on generic trend · asset: multi · direction: fees for generic trend compress · horizon: years · conditions: Applies to managers whose returns resemble the beta. · testable: partly - fee and market-share trends · confidence: medium
  ^MT135-C12-X1

### C13
- **Moritz (co-host)** Trend funds now run 8-12% volatility, so returns lack the punch of 1980s-90s CTAs, trading off stress payoff.  #mech/structural_shift
  > most of the funds in our space have lowered their volatility profiles in recent years
  indicator: CTA target vol · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT135-C13-1
- **Adam Butler** A high-vol trend strategy is a capital-efficient version of a low-vol one (50 vol with a fifth of capital equals 10 vol) and at the limit a portable alpha overlay.  #mech/risk_management
  > a very high ball [L520] trend strategy
  asset: multi · testable: yes · confidence: medium
  **Correction (cross-check):** Attributed to Adam, but the co-host next responds 'to what Corey just said about the blowout risk' and 'I agree with you, Cory', so the passage is Cory's. → Cory: a high-volatility trend strategy is a capital-efficient version of a low-vol one (50 vol with a fifth of the capital equals 10 vol) and at the limit a portable alpha overlay, ignoring knock-out leverage risk.
  ^MT135-C13-2
- **Adam Butler** Most clients cannot tolerate more than about 10% vol and line-item risk, so products shifted to 10-12% vol.  #mech/behavioral
  > most clients can't tolerate more than 10 ball
  asset: multi · horizon: years · testable: no · confidence: medium
  **Correction (cross-check):** Attributed to Adam, but it is the same passage by Cory (co-host replies 'I agree with you, Cory'). → Cory (citing Cliff Asness): most clients cannot tolerate more than about 10% volatility and line-item risk is too big, so the major players moved to 10-12% vol and products with higher vol struggle.
  ^MT135-C13-3
- **Moritz (co-host)** As of 15 April 2025 the CTA space had just had a drawdown (equities and trend both falling), and the host hopes it is early innings and that trend recovers within 30-50 days, a reminder that high-stress payoffs arrive with drawdowns first.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > 10 days ago, we had a little bit of a draw down event, I guess, in the CTA space
  indicator: CTA drawdown April 2025 · asset: multi · direction: trend recovers after drawdown · horizon: weeks · conditions: Low-confidence hope, not evidence. · testable: yes - trend returns after April 2025 · confidence: low
  ^MT135-C13-X1
- **Moritz (co-hosts)** A co-host says most investors can no longer tolerate 20-25% volatility and its drawdowns, whereas 25 years ago equity markets at 20% volatility were fine, so institutional allocators dialled volatility down at a cost.  #mech/new _(added by map cross-check)_
  > the pain of 20% volatility or 25% volatility and the potential draw down that that could come with is something that most investors can no longer tolerate
  indicator: portfolio volatility level accepted by allocators · asset: multi · direction: n/a · horizon: years · conditions: institutional allocator behaviour · testable: no - observation about preferences · confidence: medium
  ^MT135-C13-R1

### C14
- **Cory Hoffstein** Stack only low-correlation components such as equity plus trend, which diversify each other.  #mech/risk_management
  > you would not combine things that are closely correlated
  asset: multi · direction: stock plus trend · testable: yes · confidence: medium
  ^MT135-C14-1
- **Cory Hoffstein** SEC Rule 18f-4 caps fund VaR at 20% or two times the benchmark, limiting how far stacking can be pushed.  #mech/risk_management
  > you can only have a 20day 99 percentile VAR of either 20% or two times your relevant benchmark
  indicator: 20-day 99% VaR · asset: multi · conditions: US ETFs and mutual funds · testable: yes · confidence: high
  ^MT135-C14-2
- **Adam Butler** Nightly rebalancing keeps the beta/trend ratio fixed after losses; trend collateral needs only 25-30% of NAV with 40-50% cash buffer, so ruin risk is negligible, as seen in the April 2025 drawdown.  #mech/risk_management
  > the risk of ruin is is fairly negligible and also I mean we only need at maximum kind of 25 or 30% uh of the of the total portfolio value to collateralize
  indicator: margin usage · asset: multi · horizon: days · conditions: drawdown in both stocks and trend · testable: yes · confidence: high
  ^MT135-C14-3
- **Adam Butler** Stack design: hold equity beta in a cash-funded ETF where that is efficient and top up with S&P futures, while keeping enough cash as collateral for futures strategies, so margin never forces a sale during a drawdown.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > we want to have as much allocated to cash uh funded beta where it makes sense, for example, in equities where it's more cash efficient
  indicator: funded beta plus futures collateral · asset: multi · horizon: days · conditions: Equities are the most cash-efficient to hold funded. · testable: yes - margin usage can be audited · confidence: medium
  ^MT135-C14-X1

### C15
- **Cory Hoffstein** Merger arbitrage earns a spread equal to time value of money plus deal-break risk premium; generic strategies earned about 200-250 bp over SOFR over 20 years.  #mech/risk_premium
  > it typically doesn't get all the way to the buyout price
  indicator: merger arbitrage spread · asset: equities · direction: long deal targets · horizon: years · testable: yes · confidence: high
  ^MT135-C15-1
- **Cory Hoffstein** Merger arbitrage has low correlation to equity, bond and credit premia (about 0.5 to credit), making it a diversifying stack.  #mech/risk_premium
  > correlation of just 0.5 to the credit risk premium
  indicator: merger arbitrage correlation · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT135-C15-2

### C16
- **Cory Hoffstein** The Alpha Beta merger arbitrage index uses machine learning on spread, acquirer and industry to estimate deal-close probability and includes only deals that clear a return hurdle; stock-deal acquirers are hedged short or via swaps.  #mech/risk_premium
  > they're using a machine learning model to look at effectively the quality of the deal
  indicator: Alpha Beta merger arbitrage index · asset: equities · horizon: months · conditions: US-listed deals above size threshold · testable: partly · confidence: medium
  ^MT135-C16-1
- **Cory Hoffstein** Stacked suite distinguishes diversifying strategies (trend, carry, merger) from diversifying assets (gold, Bitcoin) as overlays on equities and bonds.  #mech/risk_management
  > There's diversifying strategies and there's diversifying assets.
  asset: multi · testable: no · confidence: medium
  ^MT135-C16-2
- **Cory Hoffstein** A merger-arbitrage ETF avoids the borrow-fee and recall risk on the short hedge leg of stock-for-stock deals by hedging via swaps as an alternative to physical shorts; most deals are cash, so hedging is rarely needed.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > we can do specific short location but we can also get these names on swap
  indicator: merger arbitrage short hedge · asset: equities · direction: swap hedge instead of borrow · conditions: Applies to stock-for-stock deals. · testable: yes - hedge cost comparison · confidence: medium
  ^MT135-C16-X1

### C17
- **Cory Hoffstein** A risk-balanced gold plus Bitcoin overlay on US equity offers a store-of-value diversifier to a stock-bond portfolio.  #mech/structural_shift
  > gold in particular, and I think Bitcoin is proving some of these features, uh, can be a very interesting long-term diversifier for a stock bond portfolio
  indicator: gold, Bitcoin · asset: multi · direction: long gold and Bitcoin overlay · horizon: years · testable: partly · confidence: low
  ^MT135-C17-1

