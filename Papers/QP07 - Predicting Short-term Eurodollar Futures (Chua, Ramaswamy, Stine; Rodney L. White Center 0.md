---
source_id: QP07
title: "Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 02-09)"
type: paper
claims: 112
opus_only: 9
tags: [paper, layer0]
---
# Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 02-09)

**Authors:** Choong Tze Chua (Singapore Management University, Lee Kong Chian School of Business); Krishna Ramaswamy (Wharton, University of Pennsylvania); Robert Stine (Wharton, University of Pennsylvania)

**Summary:** Can an arbitrage-free structural forward-curve model (unconditional + maturity-specific habitat + date-specific expectation components, Kalman-filtered) forecast Eurodollar forward rates better than a random walk, and can the forecasts be traded? Method: AIC-select a 6-state model on 1981-1991 data, then expanding-window out-of-sample forecasts 1991-2008 at 5/20/65/250 days. Result: RMSE lower than random walk at every horizon but not significant; trade signals earn positive mean profit (1.19 to 49.04 bp per trade) but nearly equal to always-long futures buy-and-hold.

## Argument map

**Question:** Can a structural, arbitrage-free model that splits the Eurodollar forward curve into a steady-state curve, decaying preferred-habitat distortions and calendar-date expectation shocks forecast future futures-implied forward rates better than a random walk, and can the forecasts be traded profitably?

**Thesis:** The AIC-selected 3-factor CFRS ED model forecasts Eurodollar forwards slightly better than a random walk at 5-250 day horizons (gains grow with horizon but are not statistically significant), and trading futures in the forecast direction earns 1.2-49bp per trade, only marginally more than always-long buy-and-hold but significantly so on days when the signals differ, especially at 65-250 days. ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C02-4|C02-4]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C02-5|C02-5]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-1|C18-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-2|C18-2]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-1|C19-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-2|C19-2]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-5|C19-5]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C20-2|C20-2]])

### Foundations (premises)
- The forward curve equals a steady-state curve plus maturity-specific (habitat) and date-specific (expectation) deviations. _[theoretical, stated; support: preferred habitat (Modigliani-Sutch 1966), expectations hypothesis, equilibrium models (CIR, Vasicek), CFRS (2008)]_ ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C02-1|C02-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C06-4|C06-4]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C06-7|C06-7]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C07-1|C07-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C07-8|C07-8]])
- Habitat distortions are localized, smooth and decay exponentially to zero at a fixed maturity. _[assumed, stated; support: intuition ('simple yet intuitive') plus the HJM no-arbitrage requirement]_ ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C08-3|C08-3]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C08-5|C08-5]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C10-2b|C10-2b]])
- Information about future spot rates is tied to calendar dates and rolls toward the short end over time. _[theoretical, stated; support: expectations hypothesis intuition, Treasury-financing example]_ ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C09-3|C09-3]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C09-7|C09-7]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C10-1|C10-1]])
- The pure expectations hypothesis forecasts worse than a random walk, so only part of the forward curve carries spot-rate information. _[empirical, stated; support: citations (CIR 1981; general literature)]_ ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C09-4|C09-4]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C09-5|C09-5]])
- The unconditional forward curve slopes upward, so forwards drift down on average (a term premium). _[empirical, stated; support: fitted U and the buy-and-hold result]_ ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C11-2|C11-2]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-3|C19-3]])
- Cross-sectional misfits (e.g. December contracts) are persistent microstructure distortions, not noise. _[empirical, stated; support: Figure 3 example; swap-hedging conjecture]_ ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C13-5|C13-5]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C17-2|C17-2]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C27-1|C27-1]])

### Mechanism chain
- 1. Habitat demand/supply at specific maturities → Smooth localized hump M in the forward curve: habitat investors ignore forward-spot links; neighbouring maturities are substitutes _[assertion]_ ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C06-4|C06-4]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C08-3|C08-3]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C10-2b|C10-2b]])
- 2. Hump M at fixed maturities → Decays toward zero at rate Km, so forward at that maturity is forecast to move back toward U + D: assumed exponential mean reversion consistent with HJM _[assertion]_ ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C08-5|C08-5]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C16-4|C16-4]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C25-1|C25-1]])
- 3. News about spot rates at a calendar date → Date-specific deviation D that keeps its calendar date and moves to shorter maturities: expectation about that date persists _[example]_ ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C09-7|C09-7]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C10-1|C10-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C26-1|C26-1]])
- 4. Upward-sloping U and decaying deviations → Model usually forecasts lower forwards; contract-specific microstructure residuals carried forward: forward drift is downward unconditionally; residuals persist _[test]_ ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C17-1|C17-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-3|C19-3]])
- 5. Forecast forward below (above) current forward → Long (short) futures earns the realised move: forecasts are more accurate than random walk _[test]_ ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-4|C18-4]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-1|C19-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-5|C19-5]])

### Design rationale
- **Use Eurodollar futures rather than Treasury forwards**: very liquid, rich data. Alternatives: Treasury forwards (CFRS 2008). Sensitivity: not shown; credit risk ignored ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C07-5|C07-5]])
- **Futures rate = instantaneous forward at contract midpoint**: simplifying assumption. Alternatives: none. Sensitivity: not shown (convexity ignored) ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C13-3|C13-3]])
- **Exponential basis functions with HJM-checked dynamics**: arbitrage-free, affine, estimable. Alternatives: basis choices can break no-arbitrage. Sensitivity: not shown ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C11-1|C11-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C11-4|C11-4]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C29-2|C29-2]])
- **Model selection by AIC among 6 combinations, at most 4 BMs, on 1981-91 training data**: parsimony with varying parameter counts. Alternatives: Models 1-6 in Table 2. Sensitivity: richer models might do better ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C14-2|C14-2]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C14-3|C14-3]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C14-4|C14-4]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C15-2|C15-2]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C22-1|C22-1]])
- **QML over Km and measurement variance only; U fitted on all data up to T**: non-Gaussian states; keeps estimation tractable. Alternatives: none. Sensitivity: not shown ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C16-1|C16-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C16-3|C16-3]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C29-4|C29-4]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C30-2b|C30-2b]])
- **Carry date-T contract residuals into the forecast**: December/swap microstructure persists short-term. Alternatives: treat as noise. Sensitivity: not shown ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C14-1|C14-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C17-1|C17-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C17-2|C17-2]])
- **Sign-only trades in every live contract, held to horizon, profit in bp**: simple test of forecast usefulness. Alternatives: buy-and-hold all contracts. Sensitivity: not shown ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-4|C18-4]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-5|C18-5]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-6|C18-6]])
- **Compare with buy-and-hold only on divergent-signal days**: signals usually coincide because of downward forward drift. Alternatives: full-sample difference. Sensitivity: full-sample mean differences are 0.03-0.43bp ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-3|C19-3]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-4|C19-4]])

### Evidence map
- Lower RMSE than random walk at all horizons, gap growing to 6.3bp at 250 days. Tests: steps 2-4 forecasting value. Rules out: . Does not rule out: (reader) that forecasts add nothing beyond random walk: none of the NW-stats is significant; the 250-day gain may mostly reflect the downward drift (term premium) in a falling-rate 1991-2008 period. Strength: weak - consistent sign but NW |t| <= 1.03 ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-1|C18-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-2|C18-2]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C23-2|C23-2]])
- Trading profits 1.19-49.04bp per trade, significant vs no trade. Tests: step 5. Rules out: zero mean directional payoff. Does not rule out: (reader) that profits are the term premium / falling rates, since buy-and-hold earns 97-99% of it; no transaction costs; overlapping trades. Strength: moderate - NW 2.4-3.1 but almost identical to buy-and-hold ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-1|C19-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-2|C19-2]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C24-1|C24-1]])
- Model beats buy-and-hold on divergent-signal days, NW 1.92/1.80/2.24/7.95. Tests: added value of predicting rises (D and M components). Rules out: at 65 and 250 days, that the edge is pure buy-and-hold. Does not rule out: (reader) few independent divergent episodes at 250 days with heavy overlap; statistic at 5 and 20 days below the 1.96 two-sided cut-off. Strength: moderate - strong only at 250 days ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-4|C19-4]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-5|C19-5]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C24-1|C24-1]])
- Model 5 has lowest AIC. Tests: choice of structure. Rules out: . Does not rule out: (reader) estimation problems: nested larger models (4, 6) have much lower likelihood than their parts, suggesting optimisation or specification issues. Strength: weak - in-sample, odd likelihood ordering ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C14-4|C14-4]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C22-1|C22-1]])
- Persistent contract-specific saw-tooth in 1997 curves. Tests: microstructure persistence premise. Rules out: . Does not rule out: (reader) contract-specific convexity or liquidity effects; one illustrative month only. Strength: weak - illustration ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C13-5|C13-5]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C27-1|C27-1]])

### Regimes
- Longer horizons (65-250 trading days) → larger RMSE gains and stronger edge over buy-and-hold ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C07-7|C07-7]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-1|C18-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-5|C19-5]])
- Short horizons (5-20 days) → RMSE nearly identical to random walk; edge vs buy-and-hold below conventional significance ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-1|C18-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C24-1|C24-1]])
- Times when the model predicts rising forwards → only source of difference from buy-and-hold ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-3|C19-3]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-4|C19-4]])

### Gaps and conflicts
- [conflict] Text says the model beats buy-and-hold significantly at all horizons, but NW-stats at 5 and 20 days (1.919, 1.804) are below 1.96 ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-5|C19-5]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C24-1|C24-1]])
- [conflict] Abstract claims better out-of-sample forecasts, yet no RMSE difference is statistically significant ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C02-4|C02-4]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-2|C18-2]])
- [conflict] Volatility term in the appendix is gamma^2 = (m + 2C1)Km^2 but the CFRS ED model uses gamma1^2 = (m1 + C1)Km^2 and gamma2^2 uses C1 rather than C2 ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C15-1|C15-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C29-2|C29-2]])
- [conflict] Measurement errors assumed serially uncorrelated in the filter, but the forecast step assumes residuals persist ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C17-2|C17-2]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C30-2|C30-2]])
- [data] Model 4 (SM1+SM2) and Model 6 (SM2+SM3) have far lower likelihood than SM2 or SM3 alone, odd for richer models ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C22-1|C22-1]])
- [unspecified] No transaction costs, position sizing, capital or return-based metrics; profit is bp per trade with overlapping daily trades ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-4|C18-4]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-5|C18-5]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C24-1|C24-1]])
- [untested] Eurodollar Libor includes bank credit risk outside the model; futures convexity ignored in the midpoint conversion ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C07-5|C07-5]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C13-3|C13-3]])
- [data] Training sample (1981-91) has ~9% rates and contracts to only ~4 years, while forecasts cover ~6% rates and contracts to 10 years ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C21-1|C21-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C21-2b|C21-2b]])
- [unspecified] Whether parameters (Km, sigma) are re-estimated daily or only U is refit is not fully explicit; Table 3 notes say the window expands daily ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C16-1|C16-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C23-1|C23-1]])
- [unspecified] U described as time-invariant but re-estimated from an expanding sample ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C08-2|C08-2]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C16-3|C16-3]])
- [unspecified] Text describes 4 date-specific curves on 3 bases and a 4-BM limit, while the selected model uses 3 BMs and 6 states; mapping from text to matrices relies on the page image ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C14-5|C14-5]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C15-1|C15-1]])

### Relations to other strategies
- random walk forecast: **substitute**. benchmark the model must beat ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C17-6|C17-6]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-1|C18-1]])
- carry / riding the curve (term premium): **complement**. buy-and-hold long futures earns nearly all of the model's profit; the model adds timing of when to step aside ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-6|C18-6]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-2|C19-2]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-3|C19-3]])
- expectations hypothesis: **special case**. the date-specific component is the EH part; the model adds habitat and steady-state parts ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C07-1|C07-1]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C09-4|C09-4]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C09-5|C09-5]])
- yield-curve shape mean reversion (relative value): **complement**. (reader) the maturity-specific component is a formal version of localized curve distortions that revert ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C08-5|C08-5]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C10-2b|C10-2b]])
- preferred habitat / segmentation: **special case**. explicitly modelled as the maturity-specific component ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C06-4|C06-4]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C08-3|C08-3]])

### Forward-looking inputs (reader synthesis)
(reader) The full Eurodollar (now SOFR) futures strip, decomposed into a long-run average curve, localized humps and calendar-tied expectation shocks, implies expected forward moves over weeks to a year: humps decay at fixed maturities (step 2), expectation shocks roll down (step 3), and the upward-sloping average curve implies a downward drift (step 4). Most of the predictive content at 3-12 months is the term-premium drift; the incremental signal is the model calling rises. It would stop working if the term premium disappears or inverts, in rate regimes unlike the training data, if habitat humps stop decaying (e.g. persistent policy-driven distortions), or once costs on frequent sign changes are counted.

### Reader inferences (not stated by the authors)
- (reader) Buy-and-hold earns 97-99% of the model's per-trade profit at every horizon, so the strategy is mainly a term-premium carry trade with a small timing overlay.
- (reader) The 1991-2008 test period had generally falling rates, which favours always-long futures and downward-drift forecasts.
- (reader) The 7.953 NW-stat at 250 days rests on overlapping one-year windows restricted to divergent days, so the effective number of independent observations is small.
- (reader) Treating the futures rate as an instantaneous forward ignores convexity, which matters for contracts several years out.
- (reader) Nested models with worse likelihood (Table 2) suggest the Kalman QML optimisation may not have converged reliably, which weakens the AIC choice.
- (reader) A modern replication would use SOFR futures and OIS forwards, since Eurodollar futures were discontinued in 2023.
- (reader) Figure 3 saw-tooth steps occur at the same contracts on all four dates, consistent with persistent contract-specific effects rather than noise.

## Claims

### C02 (page 2)
- Forward rate = unconditional curve + maturity-specific deviation + date-specific deviation. _(construction, premise)_ #mech/cycle_persistence
  > a three-part functional decomposition of the forward rate: a long-term, unconditional component, a maturity-specific component, and a date-specific component.
  exact_rule: F(tau;t)=U(tau)+M(tau;t)+D(tau;t)
  ^QP07-C02-1
- M reflects preferred-habitat supply/demand at specific maturities; D reflects changing expectations of future spot rates. _(mechanism, mechanism_step)_ #mech/liquidity_flows
  > The maturity-specific component captures preferred investment habitats, and the date-specific component captures shocks to expectations of future spot rates.
  ^QP07-C02-2
- Sample is 9 Dec 1981 to 28 Jan 2008; states estimated by Kalman filter. _(construction, design_choice)_ #mech/research_method
  > We demonstrate the use of this approach by fitting this model to yields over the period 12/9/1981 to 1/28/2008. The estimation is accomplished by using a Kalman filter
  exact_rule: Kalman filter, quasi-ML · data_needed: CME Eurodollar futures settlement prices 1981-12-09 to 2008-01-28
  ^QP07-C02-3
- Abstract claims better out-of-sample forecasts than the random walk (but Table 3 differences are not significant). _(result, conclusion)_ #mech/research_method
  > The estimated yield curve provides better out-of-sample predictions than the standard random walk model in forecasts over various horizons.
  reported_result: RMSE lower at all horizons; NW-stats -0.37 to -1.03, not significant (Table 3) · exhibit: Table 3 · conditions: the claim of 'better' is not statistically significant
  ^QP07-C02-4
- A trading scheme using forecast direction of forward rates is profitable on average. _(result, conclusion)_ #mech/research_method
  > We further show the profitability of a trading scheme that chooses futures positions based upon the anticipated forward curve.
  reported_result: mean profit 1.19 to 49.04 bp per trade across 5 to 250 day holds · exhibit: Table 4
  ^QP07-C02-5

### C06 (page 6)
- Authors judge term-structure models by out-of-sample forecast ability. _(construction, premise)_ #mech/research_method
  > An important characteristic that guides the choice from among these alternatives is the ability of the model to forecast forward rates or futures prices.
  ^QP07-C06-1
- Prior paper (Chua, Foster, Ramaswamy, Stine 2008, RFS) forecast US Treasury yields well out-of-sample versus competitors incl. random walk. _(citation, context)_ #mech/research_method
  > CFRS empirically select and estimate a member of this class using a sample of observed “training” data. The resulting model gave good out-of-sample forecasts of US Treasury yields when compared to several extant models that include the random walk model.
  ^QP07-C06-2
- Component 1: unconditional steady-state forward curve. _(mechanism, mechanism_step)_ #mech/cycle_persistence
  > 1. An unconditional curve that represents the steady-state forward curve;
  ^QP07-C06-3
- Component 2: maturity-specific curve from supply and demand of agents with term-specific loan needs. _(mechanism, mechanism_step)_ #mech/liquidity_flows
  > 2. A maturity-specific curve that embeds the influence of supply and demand from agents who have needs for loans of specific terms; and
  ^QP07-C06-4
- Component 3: date-specific curve holding expectations about spot rates at fixed future dates. _(mechanism, mechanism_step)_ #mech/policy_reaction
  > 3. A date-specific curve that embeds expectations about spot rates to prevail at fixed future dates.
  ^QP07-C06-5
- In preferred-habitat deviations expectations of future spot rates play no role; they reflect maturity preferences only (Modigliani-Sutch 1966). _(mechanism, mechanism_step)_ #mech/liquidity_flows
  > expectations of future spot rates play no role in this component.
  ^QP07-C06-6
- Date-specific curve holds all investor information on future spot rates, including monetary influences. _(mechanism, mechanism_step)_ #mech/policy_reaction
  > The date-specific curve embeds all of the information that investors have regarding the levels of future spot rates and summarizes the effects of fundamental monetary influences on expected future interest rates.
  ^QP07-C06-7

### C07 (page 7)
- D corresponds to the expectations hypothesis; M corresponds to deviations from steady state in CIR/Vasicek equilibrium models. _(mechanism, mechanism_step)_ #mech/policy_reaction
  > The curve of date-specific deviations corresponds to the influences of the expectations hypothesis.
  ^QP07-C07-1
- The model class is arbitrage-free (HJM-verified), unlike simple curve-fitting forecasts. _(caveat, premise)_ #mech/research_method
  > The model has the additional advantage of being demonstrably arbitrage-free.
  ^QP07-C07-2
- Test target: forecast 90-day forward rates at future dates using a representative member of the model class. _(construction, premise)_ #mech/research_method
  > Our objective here is to show that a representative member chosen from this class of models is able forecast 90-day forward rates to prevail at future dates.
  ^QP07-C07-3
- Forward rates are imputed from Eurodollar futures (liquid, rich data) rather than Treasury yields. _(construction, design_choice)_ #mech/research_method
  > In the actual estimation we use Eurodollar futures contracts to impute the forward rates.
  data_needed: Eurodollar futures prices
  ^QP07-C07-4
- Footnote 1: the model ignores default but Eurodollar futures settle to LIBOR, which carries credit risk. _(caveat, qualifier)_ #mech/research_method
  > The Eurodollar futures market settles to the rate on dollar-denominated inter-bank loans in London and therefore is affected by a credit risk;
  exhibit: footnote 1
  ^QP07-C07-5
- Model selected by AIC on a training sample, then rolled forward and compared to the random walk on a hold-out sample. _(construction, design_choice)_ #mech/research_method
  > We first select a member of the CFRS class using the Akaike information criterion over an initial set of training data;
  exact_rule: AIC model selection on initial training data, parameters estimated there, then out-of-sample comparison
  ^QP07-C07-6
- Authors conclude usefulness grows with horizon. _(result, conclusion)_ #mech/research_method
  > Our results indicate that the model is useful, most notably at longer forecast horizons.
  reported_result: RMSE gap 0.02 bp (5d) to 6.31 bp (250d) · exhibit: Tables 3-4
  ^QP07-C07-7
- Model equation (1): forward rate at time-to-maturity tau = unconditional + maturity-specific + date-specific. _(construction, design_choice)_ #mech/research_method
  > F (τ ; t) = U (τ ) + M (τ ; t) + D(τ ; t)
  exact_rule: F(tau;t)=U(tau)+M(tau;t)+D(tau;t), tau>0 time to forward start · exhibit: Equation 1
  ^QP07-C07-8

### C08 (page 8)
- Unconditional curve U(tau)=lim_{s->inf} E_t[F(tau;s)] (Eq 2): the expected forward curve in the distant future, so present information is of little use. _(construction, design_choice)_ #mech/research_method
  > This unconditional curve can be written:
  exact_rule: U(tau)=lim s->inf E_t[F(tau;s)]; time-invariant · exhibit: Equation 2
  ^QP07-C08-1
- U is estimated as the average of all historical curves (time invariant). _(construction, design_choice)_ #mech/research_method
  > The unconditional curve is time invariant and may be estimated by taking an average of all available historical curves.
  exact_rule: U(tau) = historical average of F(tau;.) (in the final model: parametric fit to all data up to T, see C16) · data_needed: all historical forward curves
  ^QP07-C08-2
- Preferred-habitat theory (Modigliani-Sutch): some participants care about their natural maturity and ignore the spot-rate implications of forwards. _(citation, mechanism_step)_ #mech/liquidity_flows
  > That model postulates that some market participants are primarily concerned with their natural maturity habitat, with little regard for the implication of the forward rates on future spot rates.
  ^QP07-C08-3
- Habitat effects stay local to a maturity region, they do not roll down toward spot, so they decay rather than shift. _(mechanism, mechanism_step)_ #mech/liquidity_flows
  > The actions of participants with preferred habi- tats affect only those maturities (and nearby maturities) of the forward curve rather than move progressively towards shorter maturities and eventually affect the spot rates.
  ^QP07-C08-4
- M mean-reverts pointwise to zero: E_t[M(tau;T)]=exp(-Km (T-t)) M(tau;t) (Eq 3), Km>0. _(construction, design_choice)_ #mech/cycle_persistence
  > We model the maturity-specific curve as a point-wise mean-reverting process that reverts to zero at a constant rate, so that
  exact_rule: E_t[M(tau;T)] = exp(-Km*(T-t)) * M(tau;t) for each fixed maturity tau; Km estimated · exhibit: Equation 3
  ^QP07-C08-5
- The maturity-specific curve may be the sum of several components, each reverting at its own rate (eq. 4). _(construction, design_choice, Opus only)_ #mech/research_method
  > specific curve can be comprised of two or more maturity-specific deviations
  exact_rule: M = M1 + M2 + ...; E_t[Mj(tau;T)] = exp(-Kmj(T-t)) Mj(tau;t) · exhibit: Equation 4
  ^QP07-C08-4b

### C09 (page 9)
- Boundary conditions: M(inf;t)=0 and M(0;t)=0 so spot-rate dynamics sit in D. _(construction, design_choice)_ #mech/research_method
  > The arbitrage-free formulation of the overall curve of maturity-specific deviations has the property that M (∞; t) = 0 for all t.
  exact_rule: M(inf;t)=0, M(0;t)=0 · exhibit: Figure 1
  ^QP07-C09-1
- Date-specific deviation derives from the Expectations Hypothesis (Fisher). _(citation, mechanism_step)_ #mech/policy_reaction
  > The concept of a date-specific deviation has its roots from the Expectations Hypothesis (Fisher (1896)).
  ^QP07-C09-2
- Intuition: a high forward rate signals a higher future spot rate at that date. _(mechanism, mechanism_step)_ #mech/policy_reaction
  > Therefore a high forward rate today should naturally point towards a higher spot rate at the corresponding date in the future.
  ^QP07-C09-3
- Empirically EH forecasts are generally worse than a random walk, so only part of the forward curve is treated as expectation. _(citation, premise)_ #mech/research_method
  > In empirical tests, forecasts of forward rates generated by the Expectations Hypothesis model are generally inferior to even the most basic benchmark, the random walk.
  ^QP07-C09-4
- Only the date-specific part of the forward curve is read as information about future spots. _(mechanism, mechanism_step)_ #mech/policy_reaction
  > The model proposed here attributes only a part of the current forward curve as containing information about future spot rates.
  ^QP07-C09-5
- CIR (1981): some versions of the EH admit arbitrage; later work (McCulloch, Fisher-Gilles, Longstaff) shows other forms can be consistent with no-arbitrage (footnote 2). _(citation, evidence)_ #mech/research_method
  > Cox, Ingersoll and Ross (1981) show that some versions of the Expectations Hypothesis admit arbitrage.
  exhibit: footnote 2
  ^QP07-C09-6
- Example: news of Treasury financing needs in January 2009 raises the 1-year forward rate around that date (date-specific shock). _(mechanism, evidence)_ #mech/fiscal_debt
  > Treasury needs new additional financing on (or around) s ≡ January 2009. This borrowing will drive up interest rates during that period.
  ^QP07-C09-7

### C10 (page 10)
- Date-specific deviation is attached to a calendar date: its expected value at that date is unchanged, so the curve shifts left in maturity as time passes (Eq 5). _(construction, design_choice)_ #mech/cycle_persistence
  > E t [D(s − T ; T )] = D(s − t; t)
  exact_rule: E_t[D(s-T;T)] = D(s-t;t), t<T<s · exhibit: Equation 5, Figure 2
  ^QP07-C10-1
- D(inf;t)=0, and D(0;t)=spot rate minus unconditional spot rate. _(construction, design_choice)_ #mech/research_method
  > At infinite maturity, the date- specific deviation must be zero because it is not plausible that one can have any information about the spot rate in the infinite future
  exact_rule: D(0;t)=F(0;t)-U(0); D(inf;t)=0
  ^QP07-C10-2
- M arises from abnormal pricing at certain maturities driven by habitat and preferences of individual and institutional investors. _(mechanism, mechanism_step)_ #mech/liquidity_flows
  > The maturity-specific deviation is caused by abnormal pricing of forward rates specific to certain maturities, driven by habitat and preferences of individual and institutional investors.
  ^QP07-C10-3
- Close substitutability across nearby maturities justifies modelling M as a smooth curve. _(mechanism, mechanism_step)_ #mech/liquidity_flows
  > Changes in demand or supply at a given maturity habitat can affect a range of surround- ing maturities — investors treat them as close substitutes — which allows us to treat the maturity-specific deviation as a smooth curve.
  ^QP07-C10-4
- No information on M dynamics, so exponential decay to zero is chosen as the simplest assumption (also needed for HJM no-arbitrage). _(construction, design_choice)_ #mech/cycle_persistence
  > a simple yet intuitive model for these deviations would be that they decay towards zero at some rate.
  exact_rule: exponential decay rate Km for M; HJM requires exponential form
  ^QP07-C10-5
- The general model can forecast negative forward rates; this is not ruled out a priori. _(caveat, qualifier)_ #mech/research_method
  > Given an observed term structure of forward rates that is positive at all maturities, it is possible to find maturity-specific and date-specific deviations that fit the current term structure but produce forecasts of negative forward rates in the future.
  conditions: not constrained in the fitted model; only HJM checked
  ^QP07-C10-6
- Habitat demand shifts spill to neighbouring maturities (close substitutes), so the maturity-specific deviation is a smooth curve averaging zero that is assumed to decay exponentially, which also meets the HJM no-arbitrage requirement. _(mechanism, mechanism_step, Opus only)_ #mech/new
  > investors treat them as close substitutes
  ^QP07-C10-2b

### C11 (page 11)
- Implementation: U, M and D are sums of exponential basis functions scaled by Brownian-motion-driven states; forward rate is exponentially affine in states. _(construction, design_choice)_ #mech/research_method
  > we employ sums of exponential basis functions for U (τ ) and similar basis functions (that are scaled by Brownian motions) to specify dynamic functional forms for M (τ ; t), and D(τ ; t).
  exact_rule: basis functions exp(-Km tau), exp(-2Km tau), exp(-4Km tau) with state-dependent scaling
  ^QP07-C11-1
- One-factor unconditional curve U1(tau)=C0-C1 exp(-2Km tau) (Eq 6): upward sloping, starts at C0-C1, asymptotes to C0. _(construction, design_choice)_ #mech/risk_premium
  > U 1 (τ ) = C 0 − C 1 e −2K m τ ,
  exact_rule: U1(tau)=C0 - C1*exp(-2*Km*tau) · exhibit: Equation 6
  ^QP07-C11-2
- One-factor maturity-specific deviation M1(tau;t)=m(t)[exp(-Km tau)-exp(-2Km tau)] (Eq 7), a fixed hump shape scaled by m(t). _(construction, design_choice)_ #mech/research_method
  > M 1 (τ ; t) = m(t) e −K m τ − e −2K m τ .
  exact_rule: M1 = m(t)*(exp(-Km*tau)-exp(-2*Km*tau)) · exhibit: Equation 7 (from page image)
  ^QP07-C11-3
- Footnote 5: the choice of exponential bases can break no-arbitrage, so the HJM conditions must be checked for each choice. _(caveat, qualifier)_ #mech/research_method
  > The precise choice of exponential bases can affect the arbitrage-free status of the model, making it important to verify the HJM conditions for each choice.
  exhibit: footnote 5
  ^QP07-C11-4

### C12 (page 12)
- One-factor M peaks at tau=ln2/Km and is zero at tau=0 and infinity. _(construction, design_choice)_ #mech/research_method
  > the deviation has a humped
  exact_rule: argmax tau of M1 = ln(2)/Km · exhibit: Equation 7
  ^QP07-C12-1
- One-factor date-specific deviation D1=d(t)exp(-2Km tau) (Eq 8): monotone up or down, zero at infinity. _(construction, design_choice)_ #mech/research_method
  > D 1 (τ ; t) = d(t) e −2K m τ .
  exact_rule: D1(tau;t)=d(t)*exp(-2*Km*tau); d(0)=D1(0;t) · exhibit: Equation 8
  ^QP07-C12-2
- State dynamics (Eq 10-11): dm=-Km m dt+gamma dB; dd=-2Km d dt+gamma dB, same diffusion to satisfy HJM. _(construction, design_choice)_ #mech/research_method
  > dm(t) = −m(t)K m dt + γ t dB(t),
  exact_rule: dm = -Km*m dt + gamma_t dB; dd = -2*Km*d dt + gamma_t dB · exhibit: Equations 10-11
  ^QP07-C12-3
- One-factor model forces M and D innovations to be perfectly correlated; multi-factor versions are used to avoid this. _(caveat, qualifier)_ #mech/research_method
  > the maturity-specific curve and the date-specific curve are driven by the same Brownian motion, so that their innovations are perfectly correlated.
  conditions: one-factor illustration only; final model has 3 Brownian motions
  ^QP07-C12-4
- M1 is humped with peak at tau = ln2/Km and a fixed shape scaled by the Ito process m(t). _(construction, design_choice, Opus only)_ #mech/research_method
  > to scale the deviation which has a fixed shape.
  exact_rule: peak of M1 at tau = ln(2)/Km
  ^QP07-C12-1b

### C13 (page 13)
- Forward SDE under one factor (Eq 12), shown to satisfy HJM in Appendix A.1. _(construction, design_choice)_ #mech/research_method
  > dF 1 (τ ; t) = −K m (2C 1 + m(t))e −2K m (τ ) dt + e −K m (τ ) γ t dB(t).
  exact_rule: dF1 = -Km*(2*C1+m(t))*exp(-2Km tau) dt + exp(-Km tau) gamma_t dB · exhibit: Equation 12; Appendix A.1
  ^QP07-C13-1
- Data: daily prices of all CME Eurodollar futures contracts 9 Dec 1981 to 28 Jan 2008. _(construction, design_choice)_ #mech/research_method
  > For the period 12/9/1981 to 1/28/2008, we obtain daily prices of all Eurodollar futures con- tracts listed in the Chicago Mercantile Exchange.
  data_needed: CME Eurodollar futures daily prices, all listed contracts
  ^QP07-C13-2
- Forward rate mapping: price P(tau;t)=100 minus annualised 90-day LIBOR for t+tau to t+tau+90; instantaneous forward at the middle (tau+45) days equals 100-P. _(construction, design_choice)_ #mech/research_method
  > f (τ + 45; t) = 100 − P (τ ; t).
  exact_rule: f(tau+45 days; t) = 100 - P(tau;t) · data_needed: Eurodollar futures price P
  ^QP07-C13-3
- Typical day has about 40 contracts (max 45), maturities from 45 days to just over 10 years; training sample averages about 10 contracts out to 4 years. _(construction, evidence)_ #mech/research_method
  > A typical day would see approximately 40 active contracts, with the maximum being 45. The maturities of the forward rates range from 45 days
  reported_result: 40 contracts typical, 45 max; training avg ~10 contracts, maturity up to 4 years · exhibit: Table 1
  ^QP07-C13-4
- December Eurodollar contracts show systematic blips, possibly from swap users; the smooth model cannot fit them. _(caveat, qualifier)_ #mech/liquidity_flows
  > there are persistent blips in the data for December contracts, perhaps caused by those
  ^QP07-C13-5

### C14 (page 14)
- Persistent December-contract microstructure effects are carried forward into the forecast. _(construction, design_choice)_ #mech/research_method
  > In order to build a useful model for prediction, we elected to incorporate these microstructure features into the forecast.
  exact_rule: see C17 residual carry-forward
  ^QP07-C14-1
- Candidate set restricted to at most 4 Brownian motions. _(construction, design_choice)_ #mech/research_method
  > We restricted the alternative models to have no more than 4 Brownian Motions (BMs) that serve as driving state variables.
  exact_rule: max 4 BMs; combinations of arbitrage-free units SM1-SM3 · conditions: a larger model set might do better (C15)
  ^QP07-C14-2
- Model selection training window is 12/09/1981 to 10/28/1991, 2500 days. _(construction, design_choice)_ #mech/research_method
  > we fit each model over the period 12/09/1981 to 10/28/1991, using daily data from the Eurodollar futures market (2500 days of data).
  exact_rule: training sample = first 2500 trading days · reported_result: 2500 days
  ^QP07-C14-3
- AIC picks Model 5 (SM1+SM3) among six candidates. _(result, evidence)_ #mech/research_method
  > Model 5 obtains the lowest AIC among the 6 candidate models. We therefore chose Model 5 (henceforth CFRS ED model) for empirical implementation reported in the rest of this paper.
  reported_result: AIC (x1e7): M1 6.4600, M2 0.8199, M3 0.1971, M4 1.7853, M5 0.1198, M6 2.6824; log-lik M5 -0.0599e7 · exhibit: Table 2
  ^QP07-C14-4
- Final model: 3 independent BMs, 1 unconditional curve, 2 maturity-specific and 4 date-specific curves, 3 exponential bases exp(-Km tau), exp(-2Km tau), exp(-4Km tau). _(construction, design_choice)_ #mech/research_method
  > The CFRS ED model, driven by 3 independent Brownian motions, is the sum of the un- conditional curve, 2 maturity-specific curves, and 4 date-specific curves fitted to 3 exponential
  exact_rule: basis {exp(-Km tau), exp(-2Km tau), exp(-4Km tau)}; f=F3+eps (Eq 13-14) · exhibit: Equations 13-14
  ^QP07-C14-5

### C15 (page 15)
- State vector has 6 variables: m1, m2, d1..d4; state-space matrices M, D and drift matrices Vm, Vd are given (Eq 15-16, read from page image). _(construction, design_choice)_ #mech/cycle_persistence
  > Therefore there are 6 state variables in this system: m 1 (t), m 2 (t), d 1 (t), d 2 (t), d 3 (t) and d 4 (t).
  exact_rule: Vm=diag(-Km,-Km); Vd=diag(-2Km,-2Km,-4Km,-2Km); gamma1^2=(m1+C1)Km^2; gamma2^2=(m2+C1)Km^2/4; gamma3^2=(3 m2+4 C2)2Km^2; u=(C0,0,-C1,-C2) · exhibit: Equations 15-16 (page image)
  ^QP07-C15-1
- Model set was limited (<=4 BMs); richer forms might forecast better, so results are for one representative member. _(caveat, qualifier)_ #mech/research_method
  > it is possible that more extensive forms may perform better than our model in forecast accuracy.
  ^QP07-C15-2

### C16 (page 16)
- Step 1: choose Km and measurement-error variance sigma*^2 by maximising the Kalman quasi-likelihood on all data up to T. _(construction, design_choice)_ #mech/research_method
  > search for a point that maximizes the quasi-likelihood.
  exact_rule: argmax over {Km, sigma*^2} of quasi-ln L using all dates and maturities up to T · data_needed: all Eurodollar forwards up to T
  ^QP07-C16-1
- Unconditional curve re-fit at each T on all data to T: U=C0-C1 exp(-2Km tau)-C2 exp(-4Km tau). _(construction, design_choice)_ #mech/research_method
  > to fit the unconditional forward curve of the form: U (τ ) = C 0 − C 1 e −2K m τ − C 2 e −4K m τ
  exact_rule: refit C0,C1,C2 on all history up to T each forecast date (expanding window)
  ^QP07-C16-2
- Deviations from the fitted U are the Kalman filter observations z_t = f - U. _(construction, design_choice)_ #mech/research_method
  > Subtract the fitted unconditional forward curve from the observed forward rates to obtain the cross-section of deviations.
  exact_rule: z_t = f(tau;t) - U_hat(tau) = A x_t + eps_t
  ^QP07-C16-3
- Forecast: decay each state at its rate: m_i(T2)=m_i(T) exp(-Km (T2-T)); d_1,d_2,d_4 decay at 2Km, d_3 at 4Km. _(construction, design_choice)_ #mech/cycle_persistence
  > we evolve these estimates forward according to their respective decay rates to obtain forecasts for future date T 2 :
  exact_rule: m_hat(T2)=m_hat(T)*exp(-Km(T2-T)); d1,d2,d4*exp(-2Km(T2-T)); d3*exp(-4Km(T2-T)) · exhibit: Section 3.3 step 2
  ^QP07-C16-4

### C17 (page 17)
- Step 3: add today's cross-sectional fit residual eps(tau+(T2-T);T) to the forecast, treating residuals as persistent microstructure distortion not noise. _(construction, design_choice)_ #mech/liquidity_flows
  > Because this microstructure persists in time, our forecast for the future data is
  exact_rule: f_hat(tau;T2)= smooth forecast + eps(tau+(T2-T);T), i.e. residual at the maturity that will have rolled to tau
  ^QP07-C17-1
- Assumption that fit residuals are persistent micro-structure effects. _(caveat, premise)_ #mech/research_method
  > the imprecise cross-sectional fits are not measurement noise per se, which should dissipate over a longer term, but are market micro-structure distortions that can be expected to persist over the short-term.
  conditions: over a short term; may not hold at 250 days
  ^QP07-C17-2
- Selection uses data to 28 Oct 1991 only; each forecast uses only data available at its date, so forecasts are out-of-sample (model choice among 6 not re-done). _(robustness, evidence)_ #mech/research_method
  > model selection in section 3.2 uses only data up to 10/28/1991 while forecast generation in section 3.3, uses only the data that is available up to the date that the forecast is being made.
  ^QP07-C17-3
- Forecast horizons: 5, 20, 65, 250 trading days (week, month, quarter, year). _(construction, design_choice)_ #mech/research_method
  > We make forecasts for 5-trading-days, 20-trading-days, 65-trading-days and 250-trading-days ahead, approximately corresponding to 1-calendar-week,
  exact_rule: horizons 5/20/65/250 trading days
  ^QP07-C17-4
- Benchmark: random walk, each contract's price unchanged (forecast change = 0). _(construction, design_choice)_ #mech/research_method
  > the Eurodollar futures prices of each contract remains unchanged over the forecasting period, the random walk model (RW model).
  exact_rule: RW forecast = current forward rate for each contract
  ^QP07-C17-5
- Accuracy metric: cross-sectional RMSE per date, then time-series mean and s.d.; difference tested by Newey-West. _(construction, design_choice)_ #mech/research_method
  > For each date, we measure the cross-sectional square root of the mean squared forecast errors (RMSE).
  exact_rule: RMSE_t = sqrt(mean over contracts of (forecast - actual forward at end)^2); average over dates
  ^QP07-C17-6
- Forecasts are judged by RMSE of predicted futures-implied forward rates and by profits of a simple trading strategy. _(construction, design_choice, Opus only)_ #mech/research_method
  > of prediction of future forward rates implied by Eurodollar futures prices, as measured using
  ^QP07-C17-3b

### C18 (page 18)
- RMSE gain over random walk grows with horizon: 0.02 bp at 5 days to 6.31 bp at 250 days. _(result, evidence)_ #mech/research_method
  > The differences in RMSE start from 0.02 basis points (12.53 for the CFRS ED model vs 12.55 for the RW model) for 5-day-ahead forecasts, and monotonically increase to an economically significant 6.31 basis points
  reported_result: RMSE bp CFRS vs RW: 5d 12.53 vs 12.55; 20d 25.39 vs 25.69; 65d 48.03 vs 48.63; 250d 98.58 vs 104.89 (6% lower); n=4095/4080/4035/3850; 1991-2008 · exhibit: Table 3
  ^QP07-C18-1
- RMSE improvements are not statistically significant at any horizon. _(result, evidence)_ #mech/research_method
  > Panel B of Table 3, shows that the CFRS ED model is consistently more accurate, but the differences are not statistically significant at the usual levels.
  reported_result: NW-stat: 5d -0.594, 20d -1.030, 65d -0.365, 250d -0.658 (negative = CFRS better) · exhibit: Table 3 Panel B · conditions: forecast accuracy edge unproven; overlapping windows
  ^QP07-C18-2
- NW statistic is needed because overlapping forecast windows create serial correlation; footnote 6 also offers Diebold-Mariano. _(caveat, qualifier)_ #mech/research_method
  > this structure is very evident in our situation because of the over-lapping forecasting windows.
  exhibit: footnote 6
  ^QP07-C18-3
- Trading rule: forecast forward below current -> short the forward (long the futures); above -> long the forward (short futures); hold to end of forecast period. _(construction, design_choice)_ #mech/cycle_persistence
  > Each trade signal generated is based on whether the forecasted forward rate is above or below the current Eurodollar-implied forward rate.
  exact_rule: signal_i = sign(f_hat(tau;T+h) - f(tau;T)) per contract; long forward (short futures) if >0, short forward (long futures) if <0; hold h days (h=5/20/65/250); all contracts alive at end of period
  ^QP07-C18-4
- Profit = cross-sectional average move in the predicted direction over the holding period, in bp (no transaction costs reported). _(construction, design_choice)_ #mech/research_method
  > The profitability on each trade is then calculated as the cross-sectional average movement in (or against) the predicted direction over the length of the forecasting period, expressed in basis points.
  exact_rule: profit_t = mean over contracts of signal * (forward at end - forward at start) in bp; no costs · conditions: no transaction costs, margin or carry accounted
  ^QP07-C18-5
- Benchmark: always long every Eurodollar futures contract (equivalent to riding the yield curve / short forwards). _(construction, design_choice)_ #mech/risk_premium
  > we also measure the profitability of an alternative trading strategy that always buys-and-holds a long position in all the traded Eurodollar futures contracts,
  exact_rule: signal = always short forward (long futures)
  ^QP07-C18-6
- Footnote 6: NW statistic = mean of daily RMSE differences divided by its Newey-West standard error; Diebold-Mariano would be an alternative. _(construction, design_choice, Opus only)_ #mech/research_method
  > The mean difference divided by this NW standard error is our reported NW statistic.
  exhibit: footnote 6
  ^QP07-C18-7b

### C19 (page 19)
- CFRS trading strategy mean profit per trade rises from 1.19 bp (5d) to 49.04 bp (250d) and is significantly positive. _(result, evidence)_ #mech/research_method
  > The average profit per trade ranges from 1.19 basis point for the 5-day holding period strategy to 49.04 basis points for the 250-day holding period strategy.
  reported_result: mean bp (s.d.): 5d 1.19 (13.70); 20d 4.59 (27.25); 65d 14.18 (51.42); 250d 49.04 (105.48); NW vs no trade: 3.061, 2.896, 2.666, 2.409; n 4095/4080/4035/3850; 1991-2008; gross · exhibit: Table 4
  ^QP07-C19-1
- Always-long-futures buy-and-hold earns almost the same: 1.16 bp to 48.74 bp. _(result, evidence)_ #mech/risk_premium
  > The buy-and-hold strategy’s profits ranges from 1.16 basis point for the 5-day holding period strategy to 48.74 basis points for the 250-day holding period strategy.
  reported_result: B&H mean bp (s.d.): 5d 1.16 (13.80); 20d 4.46 (27.56); 65d 13.75 (52.32); 250d 48.74 (106.21) · exhibit: Table 4 · conditions: excess of CFRS over buy-and-hold is only 0.03 bp (5d), 0.13 (20d), 0.43 (65d), 0.30 (250d) per trade (computed from Table 4)
  ^QP07-C19-2
- Because the unconditional curve slopes up, the model mostly predicts forward rates fall, so its trades mostly equal long-futures carry/roll-down. _(mechanism, mechanism_step)_ #mech/risk_premium
  > the CFRS ED model will, more often than not, predict a fall in forward rates, due to the fact that unconditionally, the term structure of the forward curve is upward sloping (hence, unconditionally, the drift of forward rates is downwards).
  ^QP07-C19-3
- Value over buy-and-hold is tested only on dates when the model signal diverges from always-long. _(construction, design_choice)_ #mech/research_method
  > we exclude all the dates when the trade signals are identical for both strategies, and only use those dates when their forecasted directions diverge.
  exact_rule: compare CFRS vs B&H profit only on days with different signs (NW-stat on that subset)
  ^QP07-C19-4
- Authors say CFRS beats buy-and-hold at all horizons, strongest at 250 days (NW 7.953); but the 5 and 20 day statistics (1.919, 1.804) are below 1.96. _(result, conclusion)_ #mech/research_method
  > the profitability of the CFRS ED model is signifi- cantly higher than that for the buy-and-hold for all holding periods, and especially so for the 65-day and 250-day holding periods, with NW-stat reaching 7.953.
  reported_result: NW-stat CFRS vs B&H: 5d 1.919; 20d 1.804; 65d 2.243; 250d 7.953 · exhibit: Table 4 Panel B · conditions: text claim of significance at all horizons conflicts with 5/20-day statistics under 1.96; the difference is only on divergent days (the number of divergent days is not given)
  ^QP07-C19-5

### C20 (page 20)
- Conclusion: model performs well relative to random walk (accuracy edge small and not significant). _(result, conclusion)_ #mech/research_method
  > The selected representative of our model class performs well in forecasts over various hori- zons, relative to the Random Walk model.
  exhibit: Table 3
  ^QP07-C20-1
- Conclusion: strategy outperforms buy-and-hold, most at long holds. _(result, conclusion)_ #mech/research_method
  > The chosen model also supports the construction of a trading strategy that significantly outperforms the returns of a buy-and-hold strategy, especially over longer holding periods.
  exhibit: Table 4
  ^QP07-C20-2
- Further model search and other data (not just Eurodollar) are left for future work. _(caveat, qualifier)_ #mech/research_method
  > We leave to future work the task of searching for the superior models from this general class as well as the extension to other types of data.
  ^QP07-C20-3

### C21 (page 21)
- Table 1: nearest contract mean forward rate 6.09% (full sample) vs 8.93% (training); mean maturities 76.7 days (contract 1) to 3651.9 (contract 45); full-sample counts 6600 obs for contracts 1-2 falling to 57 for contract 45; training sample only up to contract 16 (about 4 years, S.D. maturity about 26 days). _(result, evidence)_ #mech/research_method
  > Table 1: Summary statistics of Eurodollar futures data for full sample (12/09/1981 to 1/28/2008) and training sample (12/09/1981 to 10/28/1991)
  reported_result: Full sample contract 1 mean 6.091 s.d. 2.939 (n 6600); contract 12 mean 6.400; contract 42 mean 6.736 s.d. 0.827; training contract 1 mean 8.933 s.d. 2.296 (n 2500); contract 16 mean 9.063 s.d. 0.322 (n 536) · exhibit: Table 1 (page image) · conditions: mean forward curve slopes up in the full sample (6.09 to 6.74 across contracts 1 to 42), but nearly flat in training sample (8.93 to 9.06)
  ^QP07-C21-1
- The training sample (1981-91) had forward rates near 9% and contracts only to about 4 years, versus about 6.2% and up to 10 years in the full sample. _(caveat, qualifier, Opus only)_ #mech/research_method
  > Contract Number refers to the n-th nearest
  reported_result: training fwd means 8.9-9.4% vs full 6.0-6.7% · exhibit: Table 1
  ^QP07-C21-2b

### C22 (page 22)
- Table 2: six models built from SM1, SM2, SM3; Model 5 = SM1+SM3 has 6 states, 4 free parameters, log-likelihood -0.0599e7, AIC 0.1198e7 (lowest). _(result, evidence)_ #mech/research_method
  > AIC is calculated via the formula: −2 ln L + 2K, where L is the likelihood, and K is the number of free parameters in the model.
  reported_result: Model (state dim, params, logL e7, AIC e7): M1 SM1 (2,3,-3.2300,6.4600); M2 SM2 (3,3,-0.4099,0.8199); M3 SM3 (4,4,-0.0985,0.1971); M4 SM1+SM2 (5,3,-0.8926,1.7853); M5 SM1+SM3 (6,4,-0.0599,0.1198); M6 SM2+SM3 (7,4,-1.3412,2.6824) · exhibit: Table 2 · conditions: the AIC values differ by orders of magnitude, suggesting the quasi-likelihood is not a proper density likelihood (it is a quasi-ML with measurement error variance estimated)
  ^QP07-C22-1
- Sub-model formulae: SM1 (1 BM), SM2 (2 BM), SM3 (2 BM) each add a maturity-specific term and date-specific terms with exponentials exp(-Km), exp(-2Km), exp(-4Km); SM3 uses m3(t)(2e^-Km - e^-2Km - e^-4Km). _(construction, design_choice)_ #mech/research_method
  > d 3,3 (t)e −2K m (s−t)
  exact_rule: SM1: U + m1(e^-Km - e^-2Km) + d11 e^-2Km; SM2: U + m2(2e^-Km - 2e^-2Km) + 2 d21 e^-2Km + d22 e^-Km; SM3: U + m3(2e^-Km - e^-2Km - e^-4Km) + d31 e^-2Km + d32 e^-4Km + d33 e^-2Km (s-t exponent) · exhibit: Table 2 notes
  ^QP07-C22-2

### C23 (page 23)
- Forecasts use an expanding training window advanced one day at a time, starting with the first 2500 days. _(construction, design_choice)_ #mech/research_method
  > The training window is then expanded forward one day
  exact_rule: expanding window; first forecast after 2500 days; re-estimate daily · exhibit: Table 3 note
  ^QP07-C23-1
- Table 3 (page image): CFRS vs RW RMSE bp (s.d. across dates): 5d 12.53 (8.47) vs 12.55 (8.51); 20d 25.39 (16.25) vs 25.69 (16.36); 65d 48.03 (28.80) vs 48.63 (31.46); 250d 98.58 (53.93) vs 104.89 (66.64); NW-stat -0.594, -1.030, -0.365, -0.658; forecasts 4095/4080/4035/3850. _(result, evidence)_ #mech/research_method
  > 5-day-ahead
  reported_result: see claim; relative RMSE reduction 0.2%, 1.2%, 1.2%, 6.0% for 5/20/65/250 days (computed) · exhibit: Table 3 · conditions: no statistically significant difference
  ^QP07-C23-2

### C24 (page 24)
- Table 4 (page image): mean bp (s.d.) CFRS 1.19 (13.70), 4.59 (27.25), 14.18 (51.42), 49.04 (105.48); buy-and-hold 1.16 (13.80), 4.46 (27.56), 13.75 (52.32), 48.74 (106.21) for 5/20/65/250-day holds; NW CFRS vs no trade 3.061, 2.896, 2.666, 2.409; CFRS vs buy-and-hold 1.919, 1.804, 2.243, 7.953; n 4095/4080/4035/3850. _(result, evidence)_ #mech/research_method
  > This table shows the profitability of trading strategies that capitalizes on the forecasts of the CFRS ED model, as well as a buy-and-hold model.
  reported_result: as listed; excess of CFRS over buy-and-hold: 0.03, 0.13, 0.43, 0.30 bp (computed) · exhibit: Table 4 · conditions: profit statistics are cross-sectional averages with overlapping periods; no costs
  ^QP07-C24-1
- NW comparison vs buy-and-hold uses only days where signals differ; positive NW means CFRS better. _(construction, design_choice)_ #mech/research_method
  > using only days when the trades of the 2 strategies are different.
  exhibit: Table 4 note
  ^QP07-C24-2

### C25 (page 25)
- Figure 1 (illustrative, M=0.05e^-0.2t-0.1e^-0.4t+0.05e^-0.8t, Km=0.4): deviation is negative below about 2 years (trough about -0.0036 near 1 year) and positive beyond (peak about 0.0065 near 6.5 years); the whole curve shrinks in place toward zero (1y-ahead peak 0.0043, 2y-ahead about 0.0029). _(construction, evidence)_ #mech/cycle_persistence
  > We expect the maturity-specific deviation to decay exponentially to zero at rate K m (In this illustration, we set K m = 0.4) as time passes
  reported_result: illustration only, not data: peak 0.0065 -> 0.0043 -> 0.0029 at 6.5 years · exhibit: Figure 1
  ^QP07-C25-1

### C26 (page 26)
- Figure 2 (illustrative, D=0.04e^-0.2t-0.05e^-0.4t): the curve slides toward shorter maturity keeping its shape (peak about 0.008 near 4.5 years moves to about 2.5 years after 2 years); the zero-maturity value rises from -0.010 to about +0.005. _(construction, evidence)_ #mech/policy_reaction
  > We expect the date-specific deviation curve to shift to the left uniformly as time passes
  reported_result: illustration only: D(0) -0.010 now, about -0.001 after 1 year, about +0.005 after 2 years · exhibit: Figure 2
  ^QP07-C26-1

### C27 (page 27)
- Figure 3: Eurodollar-implied forward curves on four dates (20 Oct, 3 Nov, 18 Nov, 3 Dec 1997) share the same saw-tooth pattern at contract maturities even as the level falls (10-year forward 7.35% on Oct 20 to 6.77% on Dec 3). _(result, evidence)_ #mech/liquidity_flows
  > Figure 3: Illustration of Market Micro-structure Issues
  reported_result: 10-year forward about 7.36% (20 Oct 1997), 7.15% (3 Nov), 6.95% (18 Nov), 6.77% (3 Dec); maturity 0 forward about 5.75-5.92%; persistent small blips by contract · exhibit: Figure 3
  ^QP07-C27-1

### C28 (page 28)
- Figure 4 (rotated page image): training sample 12/09/1981-10/28/1991; forecasts start 10/28/1991 for 5/20/65/250-day horizons (first targets 11/04/1991, 11/25/1991, 01/30/1992, 10/22/1992) and run to the last forecasted day 01/28/2008 (latest origins 01/29/2007, 10/22/2007, 12/27/2007, 01/18/2008). _(construction, evidence)_ #mech/research_method
  > Figure 4: Timeline for Model Estimation and Forecasts
  reported_result: date markers read from rotated image · exhibit: Figure 4
  ^QP07-C28-1

### C29 (page 29)
- Appendix A.1: market price of risk kappa_t = gamma_t/Km and gamma_t^2=(m(t)+2C1)Km^2 make the drift satisfy HJM, so the one-factor model is arbitrage-free. _(construction, design_choice)_ #mech/research_method
  > For this version of the 1-Brownian motion arbitrage-free unit, we choose the market price of risk κ t as: 7
  exact_rule: sigma(t,s)=exp(-Km(s-t))gamma_t; kappa_t=gamma_t/Km; gamma_t^2=(m+2C1)Km^2; HJM drift = -Km(2C1+m)exp(-2Km(s-t)) · exhibit: Appendix A.1, Eq 17-20
  ^QP07-C29-1
- Market price of risk is proportional to the state diffusion, as in CIR. _(construction, design_choice)_ #mech/risk_premium
  > Notice that the market price of risk is proportional to the diffusion term of the state variable, just as in the CIR model.
  ^QP07-C29-2
- Footnote 7: other market-price-of-risk forms require different gamma or U so the model stays arbitrage-free. _(caveat, qualifier)_ #mech/research_method
  > If the market price of risk takes on another form, the model requires a different specification
  exhibit: footnote 7
  ^QP07-C29-3
- The state innovations are non-Gaussian, so the standard Kalman filter is not conditionally unbiased (Chen-Scott 2002); the authors use quasi-ML anyway. _(caveat, qualifier)_ #mech/research_method
  > If the innovations in the unobserved state variables are not Gaussian (which is the case for our model), estimates from the standard
  ^QP07-C29-4

### C30 (page 30)
- QML estimation: assume Gaussian innovations, optimise Km and sigma*^2 over the quasi-log-likelihood. _(construction, design_choice)_ #mech/research_method
  > by assuming that the innovations are indeed Gaussian in order to obtain a quasi-log-likelihood from the Kalman filter, and then optimize over that quasi-log-likelihood
  exact_rule: QML over (Km, sigma*^2)
  ^QP07-C30-1
- Measurement errors assumed homoscedastic and uncorrelated across maturities and time: Var(eps)=sigma*^2 I (Eq 24). _(construction, design_choice)_ #mech/research_method
  > To allow for statistical estimation, we now simplify the model by adding the assumption that the measurement errors are homoscedastic and both cross-sectionally and serially uncorrelated:
  exact_rule: Sigma_eps = sigma*^2 * I · exhibit: Equation 24 · conditions: at odds with the persistent December-contract residuals treated as microstructure in C17
  ^QP07-C30-2
- Transition equation: x_t = W x_{t-1} + xi_t with W_ii=exp(delta*V_ii), Q_t approx delta*Sigma(m)Sigma(m)' (Eq 25-27). _(construction, design_choice)_ #mech/research_method
  > We can now derive the transition equation of the Kalman filter as the discretized version of the stochastic process
  exact_rule: W=diag(exp(delta*V_ii)); Q_t = delta*Sigma Sigma'; measurement matrix A_j=[(e^{k tau_j})'M,(e^{k tau_j})'D] · exhibit: Equations 22-27
  ^QP07-C30-3
- Only Km (decay rate) and sigma*^2 (measurement-error variance) are optimised by QML; C0, C1, C2 come from the unconditional-curve fit. _(construction, design_choice, Opus only)_ #mech/research_method
  > parameters in the model that we need to optimize over the quasi-log-likelihood are
  ^QP07-C30-2b
- Measurement equation: z_t = f(tau;t) - U_hat(tau) = A x_t + eps_t with row A_j = [e(tau_j)'M, e(tau_j)'D]. _(construction, design_choice, Opus only)_ #mech/research_method
  > where A is the measurement matrix for the state variables
  exact_rule: x_t = [m(t); d(t)]; A_j = [e(tau_j)'M, e(tau_j)'D] (eqs. 21-23) · exhibit: Equations 21-23
  ^QP07-C30-3b

### C31 (page 31)
- Kalman initialisation: states at unconditional mean zero, covariance at unconditional variance. _(construction, design_choice)_ #mech/research_method
  > we set the initial estimates of the state vector at its unconditional mean, which is zero ( ~x ˆ 0 = 0), and set the initial covariance matrix at the unconditional variance Var(~x t ).
  exact_rule: x0=0; P0=Var(x_t)
  ^QP07-C31-1
- Kalman prediction and update equations (Eq 28-33): x_{t|t-1}=W x_{t-1|t-1}; P_{t|t-1}=W P W'+Q_t; update with gain P A' H^-1 v_t; H_t=A P A' + sigma*^2 I; ln L = -(nT/2) ln 2pi - 1/2 sum(ln|H_t| + v_t' H_t^-1 v_t). _(construction, design_choice)_ #mech/research_method
  > The predicting equations:
  exact_rule: standard Kalman recursions as in DeJong-Santa-Clara, Geyer-Pichler, Babbs-Nowman · exhibit: Equations 28-33
  ^QP07-C31-2
- Footnote 8: diffusion terms depend on the m states and must be non-negative, so states breaching the bound are reset to the nearest feasible value. _(construction, design_choice)_ #mech/research_method
  > The diffusion terms, which are functions of the maturity-specific state variables, must be constrained to be non-negative.
  exact_rule: clip m states so gamma^2>=0 · exhibit: footnote 8
  ^QP07-C31-3
- Footnote 8: state variables that would make diffusions negative are reset to the boundary value. _(construction, design_choice, Opus only)_ #mech/research_method
  > values of the state variables that do breach the constraints with ones that just satisfy it
  exact_rule: If gamma^2 < 0 implied by state, set state to value giving gamma^2 = 0 · exhibit: footnote 8
  ^QP07-C31-2b

