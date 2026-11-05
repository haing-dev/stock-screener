---
source_id: QP12
title: "Modeling the Yield Curve (slides: Stine, Chua, Ramaswamy)"
type: paper
claims: 55
opus_only: 7
tags: [paper, layer0]
---
# Modeling the Yield Curve (slides: Stine, Chua, Ramaswamy)

**Authors:** Bob Stine (Wharton Statistics); Choong Tze Chua (Singapore Management University); Krishna Ramaswamy (Wharton Finance)

**Summary:** Question: how to model and forecast yield curves for cash (LIBOR/Eurodollar) and commodity futures (crude, heating oil, natural gas, soybean) in one framework. Method: decompose the curve into unconditional, maturity-specific and date-specific mean-reverting components, fitted to contract-level data cleaned of microstructure anomalies. Conclusion (slides only, detail in a separate paper): out-of-sample forecasts beat a random walk in most commodity/horizon cells, but no trading strategy or P&L is presented.

## Argument map

**Question:** Can the term structure of cash rates and of commodity futures (their implied 'yield curves') be modelled parsimoniously enough to forecast where the curve is heading, and how should noisy futures data be handled? For an investor this bears on forecasting carry/roll yield and curve shape in commodity futures.

**Thesis:** Decomposing a yield curve into a stable unconditional curve, a mean-reverting maturity-specific component and a date-specific component that rolls with each contract gives forecasts of commodity futures curves that beat a random walk out of sample; data should be handled contract by contract because yields derived from prices are noisy near expiry. ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C13-1|C13-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C14-1|C14-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C17-2|C17-2]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C35-1|C35-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C28-2|C28-2]])

### Foundations (premises)
- Deviations of the curve from its long-run shape mean-revert at a rate k. _[theoretical, stated; support: assumed lognormal mean-reverting SDEs; no test shown]_ ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C13-3|C13-3]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C14-2b|C14-2b]])
- Some shocks belong to a specific delivery date and travel with that contract toward expiry. _[theoretical, stated; support: modelling assumption E_s D_t(tau) = D_s(tau+t-s)]_ ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C14-1|C14-1]])
- A commodity futures curve can be read as an implied interest-rate curve that includes convenience effects. _[theoretical, stated; support: definition (log price slope)]_ ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C06-1|C06-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C20-1|C20-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C07-2|C07-2]])
- Futures prices are smoother and cleaner than the yields derived from them; contract time series are more consistent than constant-maturity series. _[empirical, stated; support: charts]_ ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C19-2|C19-2]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C23-2|C23-2]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C24-1|C24-1]])
- Related commodities share a common latent driver. _[empirical, stated; support: co-movement charts, cointegration of nearby contracts]_ ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C11-1b|C11-1b]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C31-2|C31-2]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C32-1|C32-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C34-2|C34-2]])

### Mechanism chain
- 1. futures prices across delivery dates → implied yield curve: log-price slope between adjacent contracts is a continuously compounded rate _[assertion]_ ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C06-1|C06-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C20-1|C20-1]])
- 2. yield curve today → unconditional + maturity + date components: separable decomposition with exponential bases _[assertion]_ ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C13-1|C13-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C14-2b|C14-2b]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C14-2|C14-2]])
- 3. maturity component today → maturity component later: decays toward zero at rate k (mean reversion) _[assertion]_ ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C13-3|C13-3]])
- 4. date component on a contract → same shock at shorter maturity later: the effect rolls down the curve with the contract _[assertion]_ ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C14-1|C14-1]])
- 5. forecast states → forecast curve better than no-change: predictable decay and roll-down are captured _[test]_ ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C17-3|C17-3]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C17-2|C17-2]])

### Design rationale
- **Forecast a few state parameters instead of the whole curve**: parsimony. Alternatives: predicting the curve point by point. Sensitivity: not shown ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C12-1|C12-1]])
- **Exponential (log-scale polynomial) basis functions**: better suited to describing rates; implied by lognormal SDE. Alternatives: plain polynomials. Sensitivity: number of terms and arbitrage-freeness flagged as open ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C12-2|C12-2]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C12-3|C12-3]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C14-2b|C14-2b]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C15-1|C15-1]])
- **Model specification (2,2,3)**: example only. Alternatives: other orders. Sensitivity: not shown ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C14-2|C14-2]])
- **Clean data along each contract with a running median of 3**: outliers easier to see by contract; avoid interpolation artefacts; avoid distorting real prices. Alternatives: cleaning along constant-maturity curves. Sensitivity: misses a few outliers and sustained (3-week) anomalies ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C23-1|C23-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C24-1|C24-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C25-1|C25-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C26-1|C26-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C26-2b|C26-2b]])
- **Recursive (expanding) re-estimation for out-of-sample forecasts**: not given. Alternatives: random walk benchmark. Sensitivity: horizons 65/125/250 days shown ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C17-3|C17-3]])
- **Work with contracts/prices rather than a function of maturity**: outliers, direct observation, statistical convenience. Alternatives: structural curve model f(tau). Sensitivity: not shown ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C28-1|C28-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C28-2|C28-2]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C19-2|C19-2]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C35-2|C35-2]])

### Evidence map
- Model beats random walk in 11 of 12 commodity/horizon cells (Newey-West statistic down to -8.7). Tests: steps 3-5: mean reversion and roll-down are forecastable. Rules out: that curve shape is a pure random walk for HO, NG, soybeans at 65-250 days. Does not rule out: (reader) gains come from seasonality (HO, NG, soy) any seasonal model would capture; loss function and sample periods are not stated; no trading P&L shown. Strength: moderate - out-of-sample but sample, loss and exact test not specified on slides ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C17-2|C17-2]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C35-1|C35-1]])
- Crude at 65 days is worse than random walk (+2.1). Tests: short-horizon predictability for crude. Rules out: . Does not rule out: (reader) crude curve has little seasonality, so the model's edge may be seasonal. Strength: moderate ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C17-2|C17-2]])
- Contract yields are far more volatile and non-Gaussian near expiry. Tests: need for contract-based robust handling. Rules out: Gaussian constant-variance treatment near expiry. Does not rule out: (reader) delivery/liquidity effects rather than economic information. Strength: strong - visible in charts ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C29-1|C29-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C30-1|C30-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C30-2b|C30-2b]])
- Nearby contracts appear cointegrated; spreads non-stationary as gap grows. Tests: latent common yield process. Rules out: . Does not rule out: (reader) multiple latent factors. Strength: weak - no test statistics shown ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C31-1|C31-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C31-2|C31-2]])

### Regimes
- near expiry (tau below a few weeks) → yields noisy, outlier-dominated, non-Gaussian; terminal usable date ~15 days ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C20-2|C20-2]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C29-1|C29-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C30-1|C30-1]])
- seasonal commodities (heating oil) → curve has a strong seasonal shape that the model must include ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C11-1|C11-1]])
- crude oil at short (65-day) horizon → model does not beat random walk ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C17-2|C17-2]])
- illiquid/non-trading contracts → stale prices create spurious yield spikes ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C22-1|C22-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C21-1|C21-1]])

### Gaps and conflicts
- [unspecified] Number of terms, the value of k and arbitrage-freeness are left to the paper ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C12-3|C12-3]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C15-1|C15-1]])
- [unspecified] Sample periods, training window length and loss function behind the forecast table are not given ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C17-3|C17-3]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C17-2|C17-2]])
- [untested] Forecast accuracy of yields is not translated into a tradeable strategy or P&L ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C35-1|C35-1]])
- [data] Median filter misses some outliers and sustained anomalies remain in the data ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C25-1|C25-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C26-2b|C26-2b]])
- [untested] Convenience-yield extraction (commodity minus cash yield) is proposed but not tested ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C34-1|C34-1]])
- [untested] Observation errors 'ought to be' uncorrelated: the check is stated as a requirement, no result shown ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C16-2|C16-2]])

### Relations to other strategies
- commodity carry / roll yield: **complement**. the implied yield curve is the term structure of carry; forecasting its shape forecasts roll yield ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C06-1|C06-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C17-2|C17-2]])
- Nelson-Siegel / dynamic factor yield-curve models: **special case**. (reader) exponential basis with level/hump components resembles Nelson-Siegel with an added contract-specific component ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C12-2|C12-2]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C15-1|C15-1]])
- seasonality in commodity curves: **complement**. heating-oil seasonality is a dominant feature of its curve ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C11-1|C11-1]])

### Forward-looking inputs (reader synthesis)
(reader) The current futures curve shape, decomposed into maturity-specific (mean-reverting at rate k) and contract-specific (rolling to expiry) parts, predicts the curve shape 3-12 months ahead, through steps 3-4 of the chain; the edge is largest for seasonal products (heating oil, soybeans, natural gas). It would stop working if curve deviations follow a random walk (no mean reversion), if seasonality is already fully priced into a seasonal-adjusted benchmark, or if data noise near expiry dominates.

### Reader inferences (not stated by the authors)
- (reader) Model gains may largely reflect seasonality: the weakest result is crude, the least seasonal of the four.
- (reader) No transaction-cost or trading test is given, so economic value of the forecast is unknown.
- (reader) The yield units on the commodity charts are labelled % but read like decimal per-year rates; magnitudes should be rechecked from data.
- (reader) The decomposition resembles Nelson-Siegel with an extra contract-specific factor.
- (reader) Using CRB Trader settlement prices with a median-3 filter is a reproducible cleaning step for any futures term-structure signal.

## Claims

### C04 (page 4)
- The yield curve on a date is the set of rates across maturities; the slide gives the 7 Nov 2008 Treasury curve as the example. _(construction, context)_ #mech/research_method
  > Curve on a given day is formed by connecting the rates over different maturities.
  data_needed: Treasury bill/bond yields by maturity · reported_result: 7 Nov 2008: 3m 0.269%, 6m 0.84%, 2y 1.32%, 5y 2.56%, 10y 3.79%, 30y 4.27% · exhibit: slide 4 table
  ^QP12-C04-1

### C05 (page 5)
- The cash curve used in the paper is built from Eurodollar contracts (LIBOR): each contract gives the rate on a 3-month deposit starting at a future date, plotted as instantaneous forward rates. _(construction, design_choice)_ #mech/research_method
  > Interest rate on a 3-month contract in the future
  data_needed: Eurodollar futures/option contracts (LIBOR), many maturities · exhibit: slide 5 chart
  ^QP12-C05-1
- The chart for 2008.16 (about Feb 2008) shows a forward curve that starts near 3.0-3.1% at the shortest maturities, dips to roughly 2% near tau 0.7-1, then rises to about 5.8% at tau 10 (read from chart, approximate). _(result, evidence)_ #mech/research_method
  > Plot shows instantaneous forward rates.
  reported_result: 2008.16: forward rate ~3.1% at tau~0.25, trough ~2% near tau~0.7, ~4.0% at tau 4, ~5.8% at tau 10 (approximate chart reading) · exhibit: slide 5 chart
  ^QP12-C05-2

### C06 (page 6)
- A commodity 'yield' is the interest rate implied by futures prices at successive delivery dates, so each commodity has its own curve of the same form as the cash curve. _(construction, premise)_ #mech/new
  > Interest rates implied by the prices of contracts for delivery of a commodity at some future date.
  data_needed: Commodity futures prices by contract
  ^QP12-C06-1
- For light crude on the same date (2008.16) the implied yield is about -0.03 at the shortest maturities, crosses zero near tau 2.5 and reaches about +0.01 at tau 8-9 (read from chart, units labelled %, as printed). _(result, evidence)_ #mech/research_method
  > Light crude oil, same date as prior slide
  reported_result: Light crude 2008.16: ~-0.03 at tau<1, 0 near tau 2.5, ~+0.01 at tau 8.5 (approximate chart reading, axis labelled '%' as printed; the scale looks like a fraction) · exhibit: slide 6 chart · conditions: negative short-end yield means front prices above deferred prices (backwardation)
  ^QP12-C06-2

### C07 (page 7)
- The authors pose, without answering on the slide, the link between the cash yield and commodity-implied yields, which contain a convenience-yield component. _(mechanism, premise)_ #mech/new
  > How is the yield for cash related to yields implied by commodities that include convenience factors?
  ^QP12-C07-1
- Stated aim: describe how fast the yield curve changes and whether its future shape can be predicted. _(mechanism, context)_ #mech/research_method
  > Can you predict where it’s headed?
  ^QP12-C07-2

### C09 (page 9)
- Over about 100 trading days the cash yield curve changes shape a lot at some points and little at others; the short end moves most (trough rises from about 3.0% to about 4.5%) while the long end (tau 6-10) stays near 5.5-6.0%. _(result, evidence)_ #mech/cycle_persistence
  > Some changes are large, other curves cluster together
  reported_result: Cash curves 10 trading days apart over ~100 days: short-end trough rises from ~3% (red, original) to ~4.5% (lightest grey); 10-year end stays ~5.6-6.1% (approximate chart reading) · exhibit: slide 9 chart · conditions: large short-end moves, small long-end moves
  ^QP12-C09-1

### C10 (page 10)
- Light crude yield curves over the same 100 days are much rougher than cash curves and swing from about -0.10 to above zero at the short end. _(result, evidence)_ #mech/new
  > Rather different appearance from cash, with much less smoothness
  reported_result: Crude curves 10 trading days apart: short-end yields range from about -0.10 to -0.02 (approximate chart reading); long end converges near 0 to +0.01 · exhibit: slide 10 chart
  ^QP12-C10-1

### C11 (page 11)
- Heating oil yield movements over 10-day intervals show a strong seasonal cycle across contract maturity (swing of roughly +0.2 to -0.2 within one year of maturity) that light crude does not show. _(result, evidence)_ #mech/seasonality
  > Strong seasonal pattern for heating oil that is not apparent in yield on light crude.
  reported_result: HO 10-day yield changes peak near +0.2 at tau~0.4-0.7, trough near -0.2 at tau~0.9-1.0; CL changes stay within about -0.15 to +0.03 (approximate chart reading) · exhibit: slide 11 chart · conditions: heating oil only; crude shows no comparable seasonality
  ^QP12-C11-1
- Heating oil and light crude implied yield curves move together over 10-day intervals, so curves of related products are linked. _(result, evidence, Opus only)_ #mech/research_method
  > Dependent movements over 10-day intervals for heating oil and light crude.
  data_needed: CL and HO futures prices (CRB Trader) · reported_result: Chart over tau 0.2-1.35 years: CL curves ~-0.15 to ~0 rising with tau; HO curves +0.2 to -0.2 (read from image) · exhibit: Slide 11 chart
  ^QP12-C11-1b

### C12 (page 12)
- A parsimonious parametric model reduces curve forecasting to forecasting a few parameters of a polynomial-like formula. _(construction, design_choice)_ #mech/research_method
  > Rather than have to predict a “curve”, forecast the value of certain parameters in a regression- like formula for the curve
  exact_rule: Express the whole curve as a low-dimensional parametric function and forecast its parameters rather than each maturity
  ^QP12-C12-1
- The curve is modelled as a polynomial-type expansion on a logarithmic (exponential-decay) scale, which suits interest-rate shapes. _(construction, design_choice)_ #mech/research_method
  > Model used resembles a polynomial, but on a logarithmic scale more suited to description of rates.
  exact_rule: Basis functions of the form exp(-k*tau)-type terms (see following slides) rather than ordinary polynomials in tau
  ^QP12-C12-2
- Two modelling issues left to the paper: how many polynomial terms to use, and whether the fitted model permits arbitrage. _(caveat, qualifier)_ #mech/research_method
  > Does the model allow arbitrage?
  ^QP12-C12-3

### C13 (page 13)
- The yield curve at date t and maturity tau is split into an unconditional curve U(tau), a maturity-specific part M_t(tau) and a date-specific part D_t(tau). _(construction, design_choice)_ #mech/research_method
  > Decompose the yield curve y t (τ) into three components
  exact_rule: y_t(tau) = U(tau) + M_t(tau) + D_t(tau) · data_needed: Yield curve panel by date and maturity
  ^QP12-C13-1
- U(tau) is the long-run unconditional mean curve: the conditional expectation of the curve at any date equals U(tau) in the long run. _(construction, design_choice)_ #mech/cycle_persistence
  > Long-term unconditional expectation
  exact_rule: E_s[y_s(tau)] = U(tau)
  ^QP12-C13-2
- The maturity-specific component factors as m_t*g(tau), where m_t is log-normal and decays toward zero at rate k, so deviations tied to a given maturity mean-revert. _(construction, mechanism_step)_ #mech/cycle_persistence
  > Maturity specific component is mean reverting
  exact_rule: M_t(tau)=m_t*g(tau); m_t log-normal SDE; E_s[m_t]=m_s*exp(-k(t-s)) for s<t
  ^QP12-C13-3

### C14 (page 14)
- The date-specific component D_t(tau) is attached to a contract's expiry date, so it slides toward tau=0 as time passes (E_s D_t(tau)=D_s(tau+t-s)) while also decaying, i.e. each contract carries its own date effect. _(construction, mechanism_step)_ #mech/cycle_persistence
  > Date specific term is also mean reverting, but captures effects that move toward origin with time
  exact_rule: E_s[D_t(tau)] = D_s(tau+t-s); if d_t is log-normal then h(tau)=exp(-k*tau) and E_s[D_t(tau)] = d_s*exp(-k(t-s))*exp(-k*tau)
  ^QP12-C14-1
- The worked specification (2,2,3) has a second-order unconditional curve, two maturity-specific functions m1=c1*(e^{-k tau}-e^{-2k tau}) and m2=c2*(e^{-k tau}-e^{-4k tau}), and three date-specific functions. _(construction, design_choice)_ #mech/research_method
  > Example (2,2,3)
  exact_rule: Orders (unconditional=2, maturity-specific=2, date-specific=3); maturity functions exp(-k tau)-exp(-2k tau) and exp(-k tau)-exp(-4k tau); constants c_m1, c_m2; k common shape constant
  ^QP12-C14-2
- If the date-specific state d_t follows a lognormal mean-reverting SDE, the date component has basis h(tau) = e^{-k tau} and E_s D_t(tau) = (d_s e^{-k(t-s)}) e^{-k tau}. _(construction, design_choice, Opus only)_ #mech/research_method
  > If d t follows log normal SDE, then h(τ) = e -kτ
  exact_rule: D_t(tau) = d_t e^{-k tau}; E_s D_t(tau) = d_s e^{-k(t-s)} e^{-k tau} = D_s(tau+t-s)
  ^QP12-C14-2b

### C15 (page 15)
- Both the maturity-specific basis M_t(tau) (hump shape, peaking about 0.3 near tau 0.5) and the date-specific basis D_t(tau) (decaying from 1.0 at tau 0 toward 0 by tau 3) are controlled by a single constant k. _(construction, design_choice)_ #mech/research_method
  > Constant k determines shapes
  reported_result: M_t(tau) peak about 0.3 near tau~0.5 and decays to ~0.1 by tau 3; D_t(tau) falls from 1.0 to ~0.1 by tau 3 (approximate chart reading) · exhibit: slide 15 charts
  ^QP12-C15-1

### C16 (page 16)
- The model's fitted state coefficients give a smoother curve than the raw day-by-day estimate; on 2006.87 the fitted curve (thick black) lies below the date-specific term and tracks the observed dots, with the date component dominating at the short end and the maturity component negative (to about -0.19). _(result, evidence)_ #mech/cycle_persistence
  > Estimates are smoother than those for each day
  reported_result: 2006.87 fit: observed short-end value ~0.5 at tau 0 falling to ~0 by tau 2; maturity component dips to about -0.19 near tau 0.25; unconditional component about -0.07 at tau 0 (approximate chart reading) · exhibit: slide 16 chart
  ^QP12-C16-1
- The fit is considered adequate only if observation errors are uncorrelated; the slide flags this as a diagnostic still to be checked. _(caveat, qualifier)_ #mech/research_method
  > Observation error ought to be uncorrelated
  exact_rule: Check that residual (observation) errors from the fitted state model are serially/cross-sectionally uncorrelated
  ^QP12-C16-2

### C17 (page 17)
- Forecasting method: take the fitted state, extrapolate it forward, and update it recursively as the forecast extends beyond the initial training period. _(construction, design_choice)_ #mech/research_method
  > Extrapolate fit
  exact_rule: Fit model on initial training window; extrapolate state forward; recursively re-fit/update as horizon extends past the training period; compare with a random-walk forecast
  ^QP12-C17-1
- The table reports a Newey-West test statistic of the model against a random-walk benchmark; negative values mean the model forecasts better. Crude at 65 days is the only positive cell (2.1, random walk better); all other cells are negative. _(result, conclusion)_ #mech/cycle_persistence
  > Negative values indicate our models dominate random walk (Newey-West statistic)
  reported_result: Newey-West statistic (negative = model beats random walk). 65d/125d/250d: Crude 2.1/-0.09/-2.2; Heating Oil -5.8/-8.7/-2.2; Natural Gas -1.6/-2.2/-1.4; Soybean -5.1/-7.4/-3.1. (Exhibit slide 17; sample period, loss function and significance cut-off not stated) · exhibit: slide 17 table · conditions: fails for crude at 65 days; weakest evidence for crude (-0.09 at 125 days is insignificant)
  ^QP12-C17-2
- Horizons of 65, 125 and 250 days are the out-of-sample forecast horizons tested; the model's edge is strongest at 65-125 days for heating oil and soybean and shrinks at 250 days. _(robustness, evidence)_ #mech/cycle_persistence
  > Recursively update as forecast extends beyond initial training period
  reported_result: Heating oil -5.8 (65d), -8.7 (125d), -2.2 (250d); soybean -5.1, -7.4, -3.1; natural gas -1.6, -2.2, -1.4 · exhibit: slide 17 table
  ^QP12-C17-3

### C18 (page 18)
- Data preparation for futures curves is the main practical burden of the project. _(caveat, qualifier, Opus only)_ #mech/research_method
  > Never underestimate the time that it takes to prepare the data.
  ^QP12-C18-1b

### C19 (page 19)
- Raw inputs are futures contract prices from CRB Trader; yields are not observed directly and are derived from the prices. _(construction, design_choice)_ #mech/research_method
  > Obtain prices of futures contracts from data vendor CRB Trader
  data_needed: Futures contract prices from CRB Trader (daily, by contract)
  ^QP12-C19-1
- The price curve across contracts is much smoother than the derived yield curve, so prices are the better object to inspect and clean. _(mechanism, premise)_ #mech/research_method
  > Prices are much smoother
  reported_result: 2008.16 light crude: price curve ~88-91 across tau 0-8, smooth; yields from the same data are jagged (about +-0.03) · exhibit: slide 19 charts
  ^QP12-C19-2

### C20 (page 20)
- Yield between adjacent contract maturities is the continuously compounded forward rate: y_t(tau) = [log p_t(tau+d) - log p_t(tau)]/d, evaluated at the midpoint of the two contracts. _(construction, design_choice)_ #mech/research_method
  > Compute the yield at the midpoint between two observed prices as the continuously compounded rate of interest
  exact_rule: y_t(tau) = (log p_t(tau+d) - log p_t(tau)) / d, d = gap between adjacent contract expiries, assigned to the midpoint tau + d/2 · data_needed: Futures prices for adjacent contracts, expiry dates
  ^QP12-C20-1
- Taking log differences between neighbouring prices magnifies noise, and the curve is only observed at discrete maturities, the last contract being about 15 days out, with no observed spot rate. _(caveat, qualifier)_ #mech/research_method
  > Differencing magnifies random noise
  conditions: noise magnification worst for adjacent short-dated contracts; shortest contract about 15 days; no spot price observed
  ^QP12-C20-2
- Derived yields contain anomalies from market microstructure that have to be cleaned before modelling. _(caveat, qualifier)_ #mech/research_method
  > Anomalies (aka, “market microstructure”)
  ^QP12-C20-3

### C21 (page 21)
- Cash (LIBOR) curves show ripples at about 10-day spacing caused by traders' preference for contracts at specific dates, which is microstructure, not information about rates. _(caveat, qualifier)_ #mech/liquidity_flows
  > Ripple induced by preference for contract at a specific date (market microstructure)
  reported_result: 1995.28 LIBOR curves: ripples visible in the 4-10 year range in three curves about 10 days apart (approximate chart reading) · exhibit: slide 21 chart · conditions: date-specific preference for particular contract expiries
  ^QP12-C21-1

### C22 (page 22)
- A stale price (contract did not trade, previous close carried) distorts the derived yield curve and shifts the rest of the curve; the slide shows 1999.35. _(caveat, qualifier)_ #mech/liquidity_flows
  > A contract for light crude did not trade this day, so price stayed same as on prior day
  reported_result: 1999.35 light crude: yield spike to about +0.05 and -0.10 near tau 1-6; price curve ~16.0-17.2 with a flat segment (approximate chart reading) · exhibit: slide 22 charts · conditions: illiquid or non-trading contract
  ^QP12-C22-1

### C23 (page 23)
- Data cleaning is done by tracking each contract (fixed expiry date) through time instead of holding maturity tau fixed, which avoids interpolation-induced jumps; in the (t,tau) grid a contract is a diagonal where t+tau is constant. _(construction, design_choice)_ #mech/research_method
  > Approach is to follow a contract over time rather than fixed maturity
  exact_rule: Index series by expiry date e = t + tau; clean each contract yield series along the diagonal rather than across maturities on a given day · data_needed: Contract-level daily price panel
  ^QP12-C23-1
- Contracts show a more consistent sequential pattern over time than yields across maturities on a fixed date, so outliers are easier to detect along a contract. _(mechanism, premise)_ #mech/research_method
  > Contracts have a more consistent sequential pattern than in yields over varying maturities
  ^QP12-C23-2

### C24 (page 24)
- Spikes in the yield series of a single contract (a few points deviating from the smooth path, e.g. near day 35 550 at about 0.27) stand out and can be filtered, whereas on the curve it is unclear which wiggles are real. _(construction, design_choice)_ #mech/research_method
  > Outliers are more easily identified in the sequence of yields associated with contract rather than over the yield curve itself.
  exact_rule: Detect outliers in each contract yield time series (see slide 25-26: moving median of length 3) · reported_result: Single contract yield series days 35 200-35 900: path rises from ~0 to peak ~0.3 near day 35 750 then falls to about -0.2; isolated outliers (~0.27 near 35 550, -0.16 near 35 100) (approximate chart reading) · exhibit: slide 24 chart
  ^QP12-C24-1

### C25 (page 25)
- The cleaning filter is deliberately conservative: it accepts that a few outliers survive so that real price moves are not smoothed away. _(caveat, qualifier)_ #mech/research_method
  > In order not to distort “real” prices, miss a few outliers.
  ^QP12-C25-1

### C26 (page 26)
- The length-3 moving median repairs isolated outliers but not a sustained anomaly: one contract shows a break lasting about 3 weeks (yield falling to about -1.5 around days 35 650-35 700) that the filter cannot fix. _(robustness, qualifier)_ #mech/research_method
  > Moving medians of length 3 cannot patch a period with a sustained anomaly.
  exact_rule: Outlier patch = moving median of length 3 along the contract series · reported_result: Anomaly persists about 3 weeks; yield dips to about -1.5 (approximate chart reading) · exhibit: slide 26 chart · conditions: fails for anomalies longer than about 2 observations
  ^QP12-C26-1
- One anomaly in the data persisted for about 3 weeks, so a short median filter leaves it in. _(caveat, qualifier, Opus only)_ #mech/research_method
  > persists for about 3 weeks
  reported_result: Chart: contract yield drops to ~-1.2 to -1.6 around day 35700 for about 3 weeks; cross-section shows discontinuity near tau~2.1 (read from image) · exhibit: Slide 26 chart
  ^QP12-C26-2b

### C28 (page 28)
- Time-series methods need a series at constant maturity, but yields at fixed tau are not observed on every day; interpolation to get them introduces artifacts. _(mechanism, premise)_ #mech/research_method
  > Cannot hold maturity τ fixed unless were able to observe y t (τ) for all t
  conditions: interpolation between observed contract points creates artifacts
  ^QP12-C28-1
- Therefore the authors use the single-contract series as the primary time series, and keep the structural model f(tau) for evaluating the curve at any maturity and deriving quantities. _(construction, design_choice)_ #mech/research_method
  > Following a single contract provides most direct series
  exact_rule: Use contract-level yield series y_t(tau) with fixed expiry as the time series; structural model supplies f(tau) at any maturity
  ^QP12-C28-2

### C29 (page 29)
- A contract's yield becomes more volatile as expiry approaches (tau to 0); the plotted contract (day 35694) swings between about -0.1 and 0.4 near its end. _(result, evidence)_ #mech/risk_premium
  > Contracts end, becoming more variable as τ approaches 0 where yield is more volatile.
  reported_result: Contract expiring day 35694: yield ~0 for first ~300 rows from expiration rising to a range of about -0.1 to +0.4 in the last ~100 rows (approximate chart reading) · exhibit: slide 29 chart · conditions: volatility rises toward expiry
  ^QP12-C29-1

### C30 (page 30)
- Cross-contract standard deviation of yields rises sharply as expiry nears and the variation is non-Gaussian near the origin; the classical SD reaches about 0.33 at 0-10 rows to expiration, while a robust SD is only about 0.21. _(result, evidence)_ #mech/risk_management
  > Very strong presence of outliers as τ nears 0
  reported_result: SD vs rows to expiration: classical SD ~0.33 at 0, ~0.17 at 50, ~0.08 at 200, ~0.04 at 400; robust SD ~0.21 at 0, ~0.04 at 400 (approximate chart reading) · exhibit: slide 30 chart · conditions: heavy-tailed near expiry; use robust scale there
  ^QP12-C30-1
- Variation in contract yields near expiry is non-Gaussian, so Gaussian time-series methods are inappropriate at the front end. _(caveat, qualifier, Opus only)_ #mech/research_method
  > Non−Gaussian variation near origin
  exhibit: Slide 30 chart caption
  ^QP12-C30-2b

### C31 (page 31)
- Differences between yields of adjacent contracts become non-stationary as the gap between their expiries widens, so contracts are cointegrated only when they are not too far apart. _(mechanism, mechanism_step)_ #mech/cycle_persistence
  > Differences in yields of adjacent contracts are non-stationary as time gap increases
  conditions: cointegration holds for nearby expiries only
  ^QP12-C31-1
- The non-stationarity is attributed to a latent underlying yield process, motivating a latent-variable state model; the degree of time separation also measures how fast the curve changes (a stochastic modulus of continuity). _(mechanism, mechanism_step)_ #mech/cycle_persistence
  > Interpret the source of non-stationarity as due to movements of some underlying yield process
  exact_rule: Treat the curve as driven by a latent yield state; measure speed of curve change by the time gap at which adjacent-contract yield differences become non-stationary
  ^QP12-C31-2
- How far apart contracts can be while staying cointegrated measures how quickly the yield curve changes shape. _(mechanism, mechanism_step, Opus only)_ #mech/research_method
  > Degree of time separation also measures the rate of change in the yield curve, a sort of stochastic modulus of continuity of the yield
  ^QP12-C31-2b

### C32 (page 32)
- Light crude contract prices of four contracts about 100 days apart in mid-1984 move together in a smooth, parallel way, supporting the use of prices over yields. _(result, evidence)_ #mech/research_method
  > Prices again seem simpler to use
  reported_result: Mid-1984, four light crude contracts: prices roughly 26-31 over about 500 days, nearly parallel (approximate chart reading) · exhibit: slide 32 chart
  ^QP12-C32-1

### C33 (page 33)
- In early 2007, four light crude contracts about 100 days apart again move together smoothly, with prices from about 55 to about 120 over the plotted span. _(result, evidence)_ #mech/research_method
  > Prices again seem simpler to use
  reported_result: Early 2007, four light crude contracts: prices rise from about 55-60 to about 100-120 (approximate chart reading) · exhibit: slide 33 chart
  ^QP12-C33-1

### C34 (page 34)
- Planned extension: subtract the cash yield from each commodity yield to isolate the convenience yield, which may be easier to model (possibly stationary). _(construction, design_choice)_ #mech/new
  > Model after subtracting out the yield for cash to extract a convenience yield
  exact_rule: convenience yield_t(tau) = commodity-implied yield_t(tau) - cash yield_t(tau) · data_needed: Commodity futures yields and LIBOR/Eurodollar cash yield
  ^QP12-C34-1
- Open problem: how to exploit the contemporaneous co-movement of yields across related products (e.g. soybean, soy meal, soy oil) in a multivariate model. _(caveat, qualifier)_ #mech/research_method
  > How to use the evident contemporaneous movements in prices or yields for various products (such as the various soy commodities)
  ^QP12-C34-2

### C35 (page 35)
- The authors summarise that the model beats a random-walk benchmark out of sample (supported by the slide 17 Newey-West statistics, with crude at 65 days the exception). _(result, conclusion)_ #mech/cycle_persistence
  > Out-of-sample performance superior to random walk benchmark
  reported_result: See slide 17 table: 11 of 12 cells negative (model better); crude 65d +2.1 · exhibit: slide 17 table
  ^QP12-C35-1
- The slides present a work in progress with many unresolved questions and no trading application, transaction costs or portfolio results. _(caveat, qualifier)_ #mech/research_method
  > Many unresolved questions
  ^QP12-C35-2
- The date-plus-maturity decomposition built for interest rates also applies to commodity futures curves. _(result, conclusion, Opus only)_ #mech/research_method
  > Date and maturity specific decomposition relevant for commodities as well
  ^QP12-C35-2b

