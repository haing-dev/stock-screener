---
source_id: MT120
title: "October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.374"
date: 2025-11-20
channel: "Top Traders Unplugged"
url: 
words: 10187
claims: 54
added_by_crosscheck: 17
corrections: 3
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Katie Kaminski (co-host, trend following researcher and portfolio manager)", "Neils Kostrup Larsen (host, hedge fund manager)"]
tags: [source, layer0]
---
# October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.374

**Speakers:** Katie Kaminski (co-host, trend following researcher and portfolio manager); Neils Kostrup Larsen (host, hedge fund manager)

**Summary:** November 2025 Systematic Investor recap: trends working again after a tough H1 (Liberation Day three-day turbulence shock), precious metals and equities leading, short-term traders lagging. Kaminski stresses parameter robustness and combining methods, discusses AQR-style economic trend, total portfolio approach, alternatives growth and managed futures for target-retirement worst cases.

**Approach:** trend following, CTA performance recap, economic trend, parameter robustness, total portfolio approach, managed futures in retirement

**Cross-check completeness estimate of first read:** 0.80 - first reader captured most numeric and strategic points but missed several mechanism steps (inflation turbulence mechanism, shock-duration logic, AQR response-lag rationale, no-significance caveat), sector colour and mis-attributed two inflation claims to Katie instead of Neils

## Argument map

**Episode thesis:** Trend following has recovered after a hard H1 2025 (a three-day Liberation Day magnitude shock that fell outside any backtest), led by equities and precious metals, with fixed income and short-term traders the laggards. Kaminski's core method claim is that strategies should be judged on out-of-sample results and robustness to parameter choices, then combined across schools, price trend with economic trend, and viewed as part of a total portfolio. Both speakers argue trend is a true diversifier whose value is greatest in stress and unstable inflation, and expect more private-wealth money to alternatives.

### Katie Kaminski (Co-host; trend-following researcher and portfolio manager (Boston))
Fingerprint: #approach/trend_following #approach/research_robustness_overfitting #approach/crisis_alpha_convexity #approach/portfolio_construction_stacking #approach/regime_detection #approach/manager_selection_allocation #approach/diversification_risk_parity
_Speaker note: Caption spells 'Katie Kaminsky'. Ledger corrections moved the inflation study and Dunn track-record remarks (C03-3, C03-4) to the host; they are not hers._

**Worldview premises**
- A total-portfolio view values trend following more than a bucket-by-bucket view, because trend is one of the few strategies whose effect is risk reduction for the whole portfolio, which line-item optimisation hides. _[theoretical, stated; support: Locally optimal versus globally optimal; success of risk-mitigation buckets; no data offered in this episode.]_ ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C02-2|C02-2]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C02-X2|C02-X2]])
- It is easy to overfit the past, so a strategy is only credible if its statistics stay stable when the parameter choices are permuted and if it holds out of sample. _[theoretical, stated; support: Reasoning from the problem of living forward in time; no study cited.]_ ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C06-1|C06-1]])
- No single parameter school (fixed or dynamic, recent or long data, per-market or common) is reliable, because each banks on one view of the world; aggregating several is the most diversified choice. _[theoretical, stated; support: Philosophical argument; the example is that bonds under a divided Fed may not behave as in the past.]_ ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C06-2|C06-2]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C07-1|C07-1]])
- Trend following is most valuable in stress: in the worst equity quintiles it shows convexity, because in stress fundamentals matter less than price changes. In calm positive-fundamental years such as 2025 it matters less and economic trend can win. _[empirical, stated; support: Her plot of SG Trend returns by equity-return quintile, presented in an academic talk that week.]_ ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C11-1|C11-1]])
- Large turbulent (high magnitude surprise) days hurt CTAs and normally recover within a day or so; a sustained three-day shock is outside the backtest and is hard for trend systems. _[empirical, stated; support: Her own turbulence-metrics paper; Liberation Day is the first three-day case in her data.]_ ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C08-1|C08-1]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C08-2|C08-2]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C08-X1|C08-X1]])
- Macro managers and trend followers mostly harvest the same global trends across asset classes by different entry methods, so macro returns correlate highly with trend. _[empirical, stated; support: A coming paper on macro trading, not yet public.]_ ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C10-1|C10-1]])
- Managed futures lift outcomes for individuals, who live one sample path, because they cut maximum drawdown in equity-heavy portfolios and so reduce the chance of retiring into a crash. _[theoretical, stated; support: Cash-flow model of target-retirement portfolios (unfinished); 2008 example.]_ ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C14-1|C14-1]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C14-2|C14-2]])
- Some managed futures added to stocks and bonds improves diversification more than expected because it is one of few really different return sources. _[experience, stated; support: Alternatives-completion work at her firm; no numbers given.]_ ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C13-1|C13-1]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C12-R2|C12-R2]])

**Chain: Why trend struggled in H1 2025 and recovered in H2**
1. Liberation Day tariff shock → erratic, headline-driven price discovery: Markets had to assess a shock before the macro world had actually changed. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C07-4|C07-4]])
2. three consecutive days of magnitude surprise → trend systems cannot ride through: A one-day shock is bounded, a three-day consistent move is large and sits outside the backtest; the trend follower must balance trend strength against volatility. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C08-2|C08-2]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C08-X1|C08-X1]])
3. headline risk calms and macro change shows up → more consistent price trends in Q3-Q4: With less noise, trends persist and trend systems get paid. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C07-4|C07-4]])
- Evidence: Quarterly pattern of trend returns; her turbulence data series ('lots of years') in which the three-day run is unique.
- Fails when: She says one-off events lack statistical significance, so the mechanism cannot be confirmed and she would not change the model mechanically.

**Chain: Why economic trend helped in 2025 and when it will not**
1. headline risk causes chaos in price trends → price trend noisy: Price reacts to every headline. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C09-2|C09-2]])
2. economic trend follows overall themes of the economy → filters the noise: Fundamentals stayed positive (S&P +16%), so a macro-theme signal ignored the price swings. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C09-2|C09-2]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C11-1|C11-1]])
3. in stress, fundamentals become irrelevant → price trend dominates: Prices change faster than data; trend's convexity appears in the worst equity quintiles. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C11-1|C11-1]])
- Evidence: AQR's 2025 result as reported in a CityWire article (relayed by the host), and her quintile plot.
- Fails when: Macro indicators can also predict a trend that never occurs; economic trend is 'more art', essentially macro under another name; official data can go missing (40-day US gap).

**Chain: Why unstable inflation helps trend followers**
1. inflation surges in one pocket (electricity) and falls in others → turbulence in relative prices: Pockets move at different speeds. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C04-X1|C04-X1]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C03-X2|C03-X2]])
2. relative-price turbulence → more price trends: Inflation is itself about how much prices move. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C04-X1|C04-X1]])
- Evidence: Only the host's track-record observation (C03-4); her own remark is a theoretical link.
- Fails when: Not stated; she notes bonds were hard for trend even in 18 months of fairly stable inflation (host).

**Decision process**
- [research] Rank strategies first on out-of-sample results and on how stable the performance statistics stay when the (about five) parameters are permuted; then check downside capture, upside capture and Sharpe.. Why: It is easy to overfit the past; the decisions you made must not drive the statistics. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C06-1|C06-1]])
- [signal] Combine parameter schools: fixed and dynamic parameters, recent and long data, per-market and common settings; machine-learning adaptation can add some value over a classic moving-average crossover.. Why: Any single school banks too much on one view; the past may not resemble the present. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C06-2|C06-2]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C07-1|C07-1]])
- [risk] Do not change the model after a one-off shock such as Liberation Day, but re-examine how volatility estimation and signals respond to sustained shocks.. Why: Three days is not statistically significant, yet it was not in the backtest. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C08-3|C08-3]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C09-X1|C09-X1]])
- [portfolio] Combine price trend with economic/macro strategies depending on the investor's mandate; risk-mitigation clients keep trend for its stress behaviour and accept modest results in strong equity years.. Why: Each approach has days of sunshine and rain. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C11-2|C11-2]])
- [other] Reach private-wealth and model-portfolio channels through wrappers like ETFs and by educating model-portfolio researchers.. Why: Private wealth is the next wave of allocations to alternatives. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C12-2|C12-2]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C12-R1|C12-R1]])

**Evidence style:** Mixed: her own published research (turbulence metrics, crisis-alpha quintile plots, target-retirement cash-flow model), first-principles reasoning on robustness and diversification; little hard data stated in the episode itself.

**Views at the time**
- (2025-11-20) Trend following is working again: H1 2025 was hard after Liberation Day, H2 much better as calmer markets show consistent trends.. Reasoning: Headline noise faded and macro change began to show in prices. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C07-4|C07-4]])
- (2025-11-20) Precious metals surged as a hedge alongside equities with a weak dollar, possibly aided by central bank buying.. Reasoning: Investors hold equities but buy the safe asset as insurance. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C04-4|C04-4]])
- (2025-11-20) Fixed income trends were hard because the market wants US cuts that are not delivered, though risk in the asset class may now be lower and interesting next year; energies went back and forth.. Reasoning: Waiting for cuts that do not arrive. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C04-3|C04-3]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C04-X3|C04-X3]])
- (2025-11-20) The weak-dollar theme shows a pivot, unclear whether it reflects an expected slowdown and unexpected cuts or a bottom after a large move.. Reasoning: Stated as an open question. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C04-X4|C04-X4]])
- (2025-11-20) Inflation can re-emerge in pockets (electricity, US healthcare, insurance); price rises arrive unevenly but drift up, so inflation matters for the next few years.. Reasoning: Uneven price rises in specific sectors. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C03-X2|C03-X2]])
- (2025-11-20) A very long-term view that ignored early-year noise helped in 2025; faster systems traded whipsaws.. Reasoning: Frequency mismatch for faster systems. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C05-4|C05-4]])
- (2025-11-20) A wave of private wealth money into alternatives is coming.. Reasoning: Concern about 60/40 and new access products. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C12-2|C12-2]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C12-R1|C12-R1]])

### Niels Kaastrup-Larsen (Host (Top Traders Unplugged); hedge fund manager)
Fingerprint: #approach/trend_following #approach/debt_cycle_long_term #approach/structural_themes #approach/manager_selection_allocation #approach/positioning_crowding #approach/behavioral_sentiment
_Speaker note: Caption spells 'Neils Kostrup Larsen'. Ledger corrections assign to him the inflation study and the Dunn track-record points, and the price-is-truth point._

**Worldview premises**
- Price data is the pure, hard-to-manipulate signal, while official economic data can be delayed, manipulated or missing; the market price is the only truth. _[institutional, stated; support: Industry saying; the 40-day US data gap and the firing of the data head as illustration.]_ ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C02-1|C02-1]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C01-1|C01-1]])
- Trend following does well in high and rising inflation, and what matters is the instability of inflation, not its level. _[empirical, stated; support: A long inflation study at his firm and Dunn's track record: worst CTA era 2000-2019 (low, stable inflation); fastest compounding 1982-2000 (low but unstable inflation).]_ ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C03-3|C03-3]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C03-4|C03-4]])
- Pure trend following does not predict and cannot anticipate, because it needs price data and time to adjust; every approach, including systematic macro, has sunshine and lean periods. _[experience, stated; support: IPM (Swedish systematic macro) example: strong record, then stopped working and closed.]_ ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C10-2|C10-2]])
- Fiduciaries who give trend zero or 1% are hard to justify because no paper shows trend fails to add value to a portfolio. _[institutional, stated; support: Twenty years of thinking about fiduciary duty; absence of contrary white papers.]_ ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C12-1|C12-1]])
- Private equity and private credit are familiar equity and credit exposure in another wrapper, so only trend-like strategies are real alternatives. _[theoretical, stated; support: Assertion; the Dunn crisis-period paper he mentions is the supporting reference.]_ ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C13-X1|C13-X1]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C15-X1|C15-X1]])
- Funds that judge each holding by what it adds to the whole portfolio (total portfolio approach; Hawaii pension dropped buckets) should move trend following up their list of valuable components. _[institutional, stated; support: Hawaii pension anecdote (former head, now at Goldman Sachs); Calpers vote on total portfolio approach cited as context; no data.]_ ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C03-1|C03-1]])
- Equity trends are supported by heavy fund inflows until politicians disrupt them. _[empirical, stated; support: A Deutsche Bank chart of weekly equity fund flows against the 2010-2024 median.]_ ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C04-1|C04-1]])

**Chain: AI data centres to electricity prices to inflation**
1. AI build-out (data-centre spending up about 400% in two years) → electricity demand: US data centres use 183 TWh, expected to more than double in 4-5 years; 26% of Virginia supply. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C03-X1|C03-X1]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C03-2|C03-2]])
2. electricity demand → electricity prices as a new inflation source: He offers it as a good guess for where inflation could come from; no price evidence. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C03-2|C03-2]])
- Evidence: Ed Yardeni blog post, relayed second-hand.
- Fails when: Not stated.

**Chain: Unstable inflation as the regime for trend**
1. low but unstable inflation (1982-2000) → best compounding in Dunn's trend record: Contrast with the stable-inflation 2000-2019 worst period. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C03-4|C03-4]])
2. central banks unable to control inflation → environment he expects: Not constant 8-10% inflation but uncontrollable inflation. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C03-X3|C03-X3]])
- Evidence: One firm's track record over two periods; no other CTAs or statistics.
- Fails when: Not stated; he notes bonds were hard for trend followers even with stable inflation over 18 months.

**Decision process**
- [signal] Treat price as the primary truth; consider per-market trend parameters informed by market elasticity (reaction speed), without overoptimising.. Why: Some markets react faster than others. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C02-1|C02-1]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C07-2|C07-2]])
- [other] Know the end client; ETF flows hide the investor's identity, so a manager cannot stop clients from reallocating at the wrong time (such as after Q2 2025).. Why: Reaching clients avoids unnecessary hardship from badly timed allocations. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C13-2|C13-2]])

**Evidence style:** Relays articles, data series and index prints (Deutsche Bank, Yardeni, CityWire on AQR, Capgemini, SG indices) and his firm's track record; anecdotes (IPM). Hosting role, so few self-built tests.

**Views at the time**
- (2025-11-20) Markets barely reacted to 40 days without official US data, so routine data is perhaps not essential.. Reasoning: Observed non-reaction. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C01-1|C01-1]])
- (2025-11-20) Expect an unstable, uncontrollable inflation environment resembling 1982-2000, which favours trend.. Reasoning: Central banks cannot control it. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C03-X3|C03-X3]])
- (2025-11-20) October 2025 started soft but trend followers re-aligned with longer trends: equities and precious metals strong, softs mixed, currencies recovering, fixed income the main challenge.. Reasoning: Fund-flow support for equities. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C04-2|C04-2]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C04-1|C04-1]])
- (2025-11-11) Metals-led commodity gains (silver +73%, platinum +68%, gold +59% YTD) show why commodities belong in trend portfolios; trend indices were around flat to +2.6% YTD, BTOP50 up five of the last six years.. Reasoning: Breadth of markets traded. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C05-1|C05-1]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C05-2|C05-2]])
- (2025-11-11) Short-term traders lagged in 2025 (-4.8% vol-adjusted) despite many short-term corrections.. Reasoning: Event-risk whipsaws; frequency mismatch (view shared by Kaminski). ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C05-3|C05-3]])
- (2025-11-20) AQR coped well in 2025 by mixing price trend with economic trend (50/50 in one program) and single-name equities, while headline risk caused chaos in price trends.. Reasoning: Relayed from a CityWire article; he flags that the no-data period will test it. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C09-1|C09-1]])
- (2025-11-20) Alternatives could grow from about $4 trillion to $12 trillion by 2034 (Everest Group: $30 trillion by 2030), with private wealth and family offices allocating far more than institutions.. Reasoning: Capgemini and Everest Group projections as cited. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C11-3|C11-3]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C12-1|C12-1]])
- (2025-11-20) Bank QIS and similar systematic strategies exceed official CTA assets yet are opaque, so disclosure regulation is suggested.. Reasoning: Size and opacity. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C07-3|C07-3]])

### Disagreements
- **Can economic trend anticipate, or is it still reactive?**: Niels Kaastrup-Larsen: Pure trend following does not predict or anticipate; economic trend sounds a little predictive, and all approaches, like IPM, have lean periods. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C10-2|C10-2]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C10-X1|C10-X1]]); Katie Kaminski: Economic trend is a way to take the same global trends by a different entry method; it filtered noise in 2025 but is an art and can predict trends that never occur. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C09-2|C09-2]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C10-1|C10-1]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C09-X2|C09-X2]])
- **When trend beats economic trend**: Katie Kaminski: In stress, price trend wins as fundamentals become irrelevant; in calm positive-fundamental years economic trend can win; the mix depends on mandate. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C11-1|C11-1]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C11-2|C11-2]]); Niels Kaastrup-Larsen: Recent economic-trend performance is the 'sunshine' phase; he warns the pattern may reverse like IPM's. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C10-2|C10-2]])

### Gaps and conflicts
- The mechanism for why unstable inflation helps trend is theoretical; the only evidence is one firm's track record over two eras, offered by the host, and C03-4 is not statistically tested. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C03-4|C03-4]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C04-X1|C04-X1]])
- Kaminski's evidence on turbulence (three-day Liberation Day run) is a single event with no significance, as she admits. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C08-2|C08-2]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C09-X1|C09-X1]])
- Several quantitative figures (alternatives to $12tn, Everest $30tn, 183 TWh, 400% data-centre spend) are second-hand and the caption mangles 'sensors' for the facilities that house chips. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C11-3|C11-3]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C03-2|C03-2]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C03-X1|C03-X1]])
- Target-retirement and macro-vs-trend papers are unfinished, so conclusions about worst-case improvement are asserted not shown. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C14-1|C14-1]], [[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C10-1|C10-1]])
- Host cites BTOP50 'up four of five years including this year' then corrects to 'five of the last six'; only 2023 (-1.85%) was down. ([[MT120 - October Market Recap- Missing Data, Strong Equities, and more - Systematic Investor - Ep.3#^MT120-C05-2|C05-2]])

### Forward-looking inputs (reader synthesis)
(reader) Inputs named as leading or conditioning future trend returns: inflation instability across pockets (electricity, healthcare, insurance) rather than the level; whether central banks deliver the US cuts markets expect (fixed income trends); dollar direction (slowdown and cuts versus bottoming); equity fund flows as support for the equity trend; sustained multi-day magnitude surprises as a regime in which trend systems struggle; restoration of official data for economic-trend signals. Horizons are the next few years for inflation, and roughly a year for fixed income ('next year perhaps').

### Reader inferences (not stated by the speakers)
- (reader) Kaminski's robustness test implies a parameter-permutation sensitivity metric could be a candidate screen for any strategy in a backtest framework.
- (reader) Both speakers frame trend as a crisis hedge in stress and an inflation-instability play, yet they also say trend was only modest in the strong-equity regime of 2025; value is regime-dependent rather than constant.
- (reader) The unstable-inflation thesis rests on one track record (Dunn) and may be confounded by the 1980s-90s interest-rate regime.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro; US government shutdown, 40 days without official data |
| C02 | 2 | data gaps and economic trend signals; price as the only truth; total portfolio approach vs buckets |
| C03 | 4 | Hawaii dropped buckets; data-centre electricity demand and inflation; trend following benefits from unstable inflation |
| C04 | 4 | inflation turbulence; Oct 2025 trend update; equity fund flows; sector review and precious metals |
| C05 | 4 | precious metals YTD; Nov 2025 index numbers; short-term traders lag in 2025 |
| C06 | 2 | evaluating strategies: out-of-sample and parameter robustness, overfitting; parameter philosophies |
| C07 | 4 | combine methods with different assumptions; market elasticity; QIS opacity; Q1/Q2 vs Q3/Q4 trend |
| C08 | 3 | turbulence metrics: Liberation Day three-day magnitude surprise; effect on vol and signals |
| C09 | 2 | AQR economic trend plus price trend (50/50) coped well in 2025; trend capture question |
| C10 | 2 | economic trend vs price trend correlation with macro; predictive vs reactive; IPM cautionary tale |
| C11 | 3 | trend convexity in stress; each approach has sunshine and rain; alternatives growth article begins |
| C12 | 2 | fiduciary case for trend; private wealth access; alternatives completion |
| C13 | 2 | know-your-client in ETFs; how to capture alternatives flows; two upcoming papers |
| C14 | 2 | managed futures in target retirement portfolios (sequence risk); outro |
| C15 | 0 | outro, next guest and paper offer (nothing actionable) |

## Claims

### C01
- **Neils Kostrup Larsen** Markets barely reacted to 40 days without official US economic data, questioning how much investors need routine data releases.  #mech/policy_reaction _(time-bound view)_
  > despite whatever it was, 40 days of no government data, the markets didn't really seem to be too bothered about that
  indicator: official macro data availability · asset: multi · horizon: weeks · testable: partly - one episode (Oct to Nov 2025 shutdown) · confidence: medium
  ^MT120-C01-1

### C02
- **Neils Kostrup Larsen** Price data is the pure, hard-to-manipulate signal, whereas official economic data can be delayed, manipulated or missing, which weakens economic-trend signals.  #mech/research_method
  > the only truth is the market price because that's where the market is caring
  indicator: price vs official economic data · asset: multi · direction: prefer price trend over economic data signals · conditions: small commodity markets may be manipulable · testable: partly - robustness comparison of economic vs price signals · confidence: medium
  **Correction (cross-check):** Mixed speakers: price being the pure truth and data manipulation are Neils, but the point that economic-trend signals are weakened by missing official data is Katie. → Neils: price data is the pure signal, official data can be delayed or manipulated. Katie: an economic-trend strategy is weakened when official data are missing.
  ^MT120-C02-1
- **Katie Kaminski** Bucket-by-bucket optimisation misses total-portfolio effects; under a total portfolio approach, trend following's total-portfolio risk reduction (locally vs globally optimal) should raise its allocation.  #mech/risk_management _(time-bound view)_
  > the line item problem and sort of this subdivision of labor in the investment management creates this very siloed view
  indicator: trend following allocation under total portfolio approach (CalPERS vote) · asset: multi · direction: raise trend allocation · horizon: years · conditions: institutional adoption of total portfolio approach · testable: partly - portfolio-level marginal contribution · confidence: medium
  ^MT120-C02-2
- **Katie Kaminski** A trend strategy built on economic data (such as AQR's economic trend) depends on official releases, so a 40-day gap in US data exposes a weakness, comparable to losing exchange price data for 40 days, even though economic data change slowly.  #mech/research_method _(added by sonnet-xhigh cross-check, time-bound view)_
  > economic trend no data That's not a great situation to be in
  indicator: economic-trend signals reliant on official data · asset: multi · horizon: weeks · conditions: when official data releases are suspended · testable: no - anecdotal observation about data dependence · confidence: medium
  ^MT120-C02-X1
- **Katie Kaminski** Siloed line-item and bucket construction makes each piece look optimised but hides total-portfolio effects; trend following gives total-portfolio risk reduction that many other alternatives do not, which is why a total portfolio approach fits it.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > the line item problem and sort of this subdivision of labor in the investment management creates this very siloed view
  indicator: trend following vs other alternatives in total portfolio risk · asset: multi · direction: higher allocation to trend under a total portfolio approach · conditions: depends on how the portfolio is evaluated (local line item vs global) · testable: partly - compare marginal contribution to total risk · confidence: medium
  ^MT120-C02-X2

### C03
- **Neils Kostrup Larsen** The Hawaii pension fund stopped using asset buckets and evaluated investments individually for portfolio contribution.  #mech/structural_shift
  > they completely stopped using anything to do with buckets
  asset: multi · testable: no - anecdote · confidence: medium
  ^MT120-C03-1
- **Neils Kostrup Larsen** AI data centres drive large electricity demand (US 183 TWh, expected to double in 4 to 5 years; 26% of Virginia supply), making electricity prices a plausible new inflation source.  #mech/structural_shift _(time-bound view)_
  > 26% of total electricity supply in Virginia is consumed by data centers
  indicator: data-centre power demand and electricity prices · asset: commodities · horizon: years · testable: partly - data public · confidence: medium
  ^MT120-C03-2
- **Katie Kaminski** Trend following performs well in high and rising inflation.  #mech/cycle_persistence
  > trend falling does really well in high inflation and rising inflation
  indicator: inflation level and change · asset: multi · direction: long trend · horizon: years · conditions: high or rising inflation · testable: yes - long inflation study referenced · confidence: high
  **Correction (cross-check):** Wrong speaker: the inflation study and the statement that trend following does well in high and rising inflation are Neils (referring to a study done at Dunn), not Katie. → Neils Kostrup Larsen: Trend following performs well in high and rising inflation, according to a long study of inflation and trend following.
  ^MT120-C03-3
- **Katie Kaminski** The worst CTA period was 2000 to 2019 with low and stable inflation, while Dunn's best compounding came in 1982 to 2000 with low but unstable inflation, so inflation instability matters more than level.  #mech/cycle_persistence
  > we don't care so much about the level of inflation but we care that it's not stable
  indicator: inflation volatility / stability · asset: multi · direction: long trend · horizon: years · conditions: unstable inflation · testable: yes - trend returns by inflation-volatility regime · confidence: medium
  **Correction (cross-check):** Wrong speaker: the 2000-2019 worst period and the Dunn track-record comparison (referring to a Dunn track record) are Neils, not Katie. → Neils Kostrup Larsen: The worst CTA period was 2000 to 2019 with low and stable inflation, while the Dunn track record compounded fastest in 1982 to 2000 with relatively low but unstable inflation, so instability matters more than level.
  ^MT120-C03-4
- **Neils Kostrup Larsen** Ed Yardeni's post reports data-centre build spending up about 400% in two years, with the Microsoft CEO saying the bottleneck is not chips but the facilities to house them (caption says 'sensors'), underpinning the electricity demand story.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > it had gone up the spending like 400% uh in 2 years
  indicator: data-centre capex · asset: other · horizon: years · testable: partly - spending series available · confidence: medium
  ^MT120-C03-X1
- **Katie Kaminski** Inflation can re-emerge in pockets such as electricity, US healthcare and insurance costs; price increases arrive unevenly but drift upward, so inflation remains an important topic for the next few years.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > price increases may not come linearly and we know this with inflation but they do drift
  indicator: sector price pockets (electricity, healthcare, insurance) · asset: multi · horizon: years · testable: partly - sectoral CPI components · confidence: low
  ^MT120-C03-X2
- **Neils Kostrup Larsen** Forward view: the environment to expect is not constant 8 to 10% inflation but inflation that is unstable and that central banks cannot control, which resembles the 1982 to 2000 period that was best for his firm's trend track record.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > just that we can't control it or central banks can't control it
  indicator: inflation instability · asset: multi · direction: favourable for trend following · horizon: years · conditions: unstable inflation regime · testable: partly - compare CTA returns across inflation volatility regimes · confidence: medium
  ^MT120-C03-X3

### C04
- **Neils Kostrup Larsen** Deutsche Bank data show 2025 equity fund inflows far above the 2010-2024 weekly average, supporting the equity trend until politicians disrupt it.  #mech/liquidity_flows _(time-bound view)_
  > the total equity fund flow in in percentage of assets and it compares this year week by week uh with uh the average
  indicator: equity fund flows % of assets vs 2010-2024 median · asset: equities · direction: long equities · horizon: months · testable: yes - flow data · confidence: medium
  ^MT120-C04-1
- **Neils Kostrup Larsen** October 2025 started soft but trend followers re-aligned with longer-term trends: equities, precious metals, softs mixed, currencies recovering, fixed income the main challenge.  #mech/cycle_persistence _(time-bound view)_
  > October had a couple of days in in in in October. The first couple of days of October was actually a little bit soft
  indicator: trend sector performance Oct 2025 · asset: multi · direction: long equities and precious metals · horizon: weeks · conditions: fixed income difficult · testable: yes - sector P&L · confidence: high
  ^MT120-C04-2
- **Katie Kaminski** Fixed income trends were hard because the market wants US cuts but they are not delivered, though risk in the asset class may now be lower.  #mech/policy_reaction _(time-bound view)_
  > the market wants cuts, especially for the US, but they're waiting for them
  indicator: US rate cut expectations · asset: rates · horizon: months · testable: partly - one year · confidence: medium
  ^MT120-C04-3
- **Katie Kaminski** Precious metals surged as a hedge alongside equities with a weak dollar, possibly aided by central banks.  #mech/risk_premium _(time-bound view)_
  > it looks a little bit like a hedge right so you know you want the equities but if you're worried you buy the safe asset
  indicator: gold, silver, platinum, palladium · asset: commodities · direction: long precious metals · horizon: months · conditions: weak dollar · testable: partly - one-year · confidence: low
  ^MT120-C04-4
- **Katie Kaminski** Mechanism for why unstable inflation helps trend followers: inflation surging in one pocket (e.g. electricity) and dropping in others is turbulence in relative prices, and inflation is itself about how much prices move, which produces price trends.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check)_
  > that sort of turbulence in the inflation sort of changes that probably causes more sort of is indicative of price trends
  indicator: inflation turbulence across components · asset: multi · horizon: years · testable: partly - dispersion of CPI components vs trend returns · confidence: low
  ^MT120-C04-X1
- **Neils Kostrup Larsen** Even with relatively stable inflation over the previous 18 months, bonds where one would expect a link to inflation have been a hard market for trend followers.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > even in a relatively stable inflation environment we've had the last 18 months
  indicator: bond trend profitability · asset: rates · horizon: months · testable: no - descriptive · confidence: medium
  ^MT120-C04-X2
- **Katie Kaminski** Energy markets have moved back and forth in 2025 and were among the hard trades for trend followers.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > things like energies that have been back and forth
  indicator: energy futures trend · asset: commodities · horizon: months · testable: no - descriptive · confidence: medium
  ^MT120-C04-X3
- **Katie Kaminski** Currencies showed a pivot in the weak-dollar theme late in 2025: unclear whether the dollar was moving on an expected slowdown and unexpected rate cuts or had simply bottomed after a large move, which makes currencies a different asset class to watch.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > you have seen a little pivot in the sort of weak dollar theme
  indicator: US dollar trend · asset: fx · horizon: months · testable: no - open question · confidence: low
  ^MT120-C04-X4

### C05
- **Neils Kostrup Larsen** By mid-November 2025 silver was up 73%, platinum 68% and gold 59% while orange juice was down 65%, showing why commodities belong in trend portfolios.  #mech/cycle_persistence _(time-bound view)_
  > Silver is up 73% this year. Platinum 68% and gold 59%
  indicator: gold, silver, platinum, orange juice YTD · asset: commodities · direction: long precious metals · horizon: months · testable: yes - price data · confidence: high
  ^MT120-C05-1
- **Neils Kostrup Larsen** BTOP50 was up in five of the last six years, with the only loss in 2023 (-1.85%), and about +2.59% YTD at 11 Nov 2025; SG CTA -0.35% and SG Trend +0.86% YTD; trend barometer 57.  #mech/cycle_persistence _(time-bound view)_
  > the only down year uh was in 2023 where it lost 1.85%
  indicator: BTOP50, SG CTA, SG Trend, trend barometer · asset: multi · horizon: years · testable: yes - index data · confidence: high
  ^MT120-C05-2
- **Neils Kostrup Larsen** The SG Short-Term Traders index lagged in 2025 (down 4.8% vol-adjusted) despite short-term corrections, because of event-risk whipsaws and frequency mismatch.  #mech/slow_reaction _(time-bound view)_
  > The only real lagard I find which is surprising to me is the short-term traders index
  indicator: SG Short-Term Traders index · asset: multi · horizon: months · conditions: frequency mismatch with headline shocks · testable: yes - index data · confidence: medium
  ^MT120-C05-3
- **Katie Kaminski** In 2025 a very long-term view that ignored early-year noise (e.g. in equities) helped, while faster systems traded whipsaws.  #mech/slow_reaction _(time-bound view)_
  > having sort of ironically like just a very long-term view this year in some asset classes would have been very helpful
  indicator: long vs short trend speed · asset: equities · direction: slow outperformed · horizon: months · conditions: headline-driven reversals · testable: yes - speed comparison · confidence: medium
  ^MT120-C05-4

### C06
- **Katie Kaminski** Judge strategies primarily by out-of-sample performance and by how stable statistics remain when parameters are permuted, because overfitting the past is easy; then also look at downside/upside capture and Sharpe.  #mech/research_method
  > it's really sort of the robustness of those parameter choices that matter to me the most
  indicator: parameter robustness / permutation stability · asset: multi · testable: yes - permutation tests · confidence: high
  ^MT120-C06-1
- **Katie Kaminski** Combine parameter schools (fixed vs dynamic, recent vs long data, per-market vs common) rather than rely on one view.  #mech/research_method
  > you should do a little bit of most of those things
  indicator: parameter selection methods · asset: multi · testable: partly - ensemble of parameter sets · confidence: medium
  ^MT120-C06-2

### C07
- **Katie Kaminski** Advanced or machine-learning parameter adaptation may add some value over classic moving-average rules, but the past may not resemble the present (e.g. bonds under a divided Fed).  #mech/structural_shift
  > adjust those parameters over time, things like machine learning
  indicator: adaptive parameters · asset: multi · testable: partly - out-of-sample comparison · confidence: medium
  ^MT120-C07-1
- **Neils Kostrup Larsen** Market elasticity (reaction speed) differs by market and might inform per-market trend parameters, without overoptimising.  #mech/slow_reaction
  > some markets react more quickly than other markets
  indicator: market elasticity · asset: multi · testable: partly - estimate per-market speed · confidence: low
  ^MT120-C07-2
- **Neils Kostrup Larsen** Bank QIS and similar systematic strategies are larger than official CTA assets yet opaque, so regulation to disclose them is suggested.  #mech/new
  > Why is it completely opaque to the world how these strategies are are because they are so big in size
  asset: multi · testable: no - opinion · confidence: medium
  ^MT120-C07-3
- **Katie Kaminski** Trend followers struggled in H1 2025 after the Liberation Day shock (erratic, headline-driven price discovery before macro changed) and improved in H2 as calmer markets showed consistent trends.  #mech/cycle_persistence _(time-bound view)_
  > Q1 and Q2 were very challenging. Q3 and Q4 have been much better
  indicator: trend strategy H1 vs H2 2025 · asset: multi · horizon: months · conditions: after headline shock fades · testable: yes - P&L by quarter · confidence: high
  ^MT120-C07-4

### C08
- **Katie Kaminski** Turbulent (high magnitude surprise) days are very negative for CTAs, which usually recover the next day or so.  #mech/overshoot
  > turbulent days so like high magnitude surprise days
  indicator: turbulence / magnitude surprise metric · asset: multi · horizon: days · testable: yes - turbulence metric from paper · confidence: high
  ^MT120-C08-1
- **Katie Kaminski** Liberation Day was the first time in the studied history that magnitude surprise lasted three consecutive days, a sustained shock that is hard for trend systems because it is not in the backtest.  #mech/structural_shift _(time-bound view)_
  > liberation day was actually three days in a row
  indicator: three consecutive turbulence days · asset: multi · horizon: days · conditions: unprecedented in data · testable: yes - event count · confidence: high
  ^MT120-C08-2
- **Katie Kaminski** Recent events should not change the model, but they raise questions about how volatility estimates and signals respond to sustained shocks.  #mech/risk_management
  > it also begs the question of like examining how you measure your volatility and how it reacts to a much more sustained shock
  indicator: volatility estimate response to sustained shocks · asset: multi · horizon: days · testable: yes - stress test of vol estimator · confidence: medium
  ^MT120-C08-3
- **Katie Kaminski** Trend systems can usually ride through a one-day shock, whose impact is bounded, but a three-day consistent move is large; the trend follower's problem is balancing trend strength against volatility, and such a sustained move was not in the backtest.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > a three-day consistent move is is pretty large
  indicator: magnitude surprise days, duration of shock · asset: multi · horizon: days · conditions: sustained multi-day shocks · testable: partly - rare event · confidence: medium
  ^MT120-C08-X1

### C09
- **Neils Kostrup Larsen** AQR coped well in 2025 by combining price trend with economic trend (50/50 in one program) and single-name equities, while headline risk caused chaos in price trends.  #mech/slow_reaction _(time-bound view)_
  > not just using price data for their trend models
  indicator: economic trend plus price trend, AQR · asset: multi · horizon: months · conditions: headline-driven markets favor fundamentals-based trend · testable: partly - build economic trend model · confidence: medium
  ^MT120-C09-1
- **Katie Kaminski** In headline-driven 2025, economic trend filtered noise and worked well; but macro indicators can also predict a trend that never occurs, so trend capture of economic models must be measured.  #mech/slow_reaction _(time-bound view)_
  > if you stepped back and perhaps followed the fundamentals and looked at sort of what the overall themes of the economy were, you know, you might have sifted through some of that noise
  indicator: economic trend / macro indicators vs price trend · asset: multi · horizon: months · conditions: 2025 headline noise · testable: yes - measure trend capture of economic trend · confidence: medium
  ^MT120-C09-2
- **Katie Kaminski** Analysis of one-off events such as Liberation Day lacks statistical significance, so they warrant thought about volatility estimation and signal response but not mechanical parameter changes.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > statistical significance. Um, they're one-off events
  indicator: single-event analysis · asset: multi · testable: no - sample size of one · confidence: medium
  ^MT120-C09-X1
- **Katie Kaminski** Economic trend is more art than rule: it is essentially macro under a different name, so one has to distill which macro strategies connect to trend and how much trend they capture.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > it's a little bit more of an art to understand exactly what what you're using
  indicator: economic trend implementation choices · asset: multi · testable: partly - needs definition of economic trend inputs · confidence: medium
  ^MT120-C09-X2

### C10
- **Katie Kaminski** Many macro managers' returns correlate highly with trend following because both capture global trends across asset classes by different entry methods.  #mech/structural_shift
  > macro and we have a paper coming that we've been working on on macro trading it has a very high correlation with trend falling
  indicator: macro manager correlation with trend · asset: multi · horizon: years · testable: yes - correlation of macro index to trend · confidence: medium
  ^MT120-C10-1
- **Neils Kostrup Larsen** Pure trend following does not predict, and cannot anticipate, because it needs price data and time to adjust; economic trend feels more predictive and every approach (e.g. systematic macro IPM) has sunshine and lean periods.  #mech/cycle_persistence
  > we don't try to predict
  indicator: predictive economic data vs price trend · asset: multi · horizon: years · testable: partly - historical strategy comparison · confidence: medium
  ^MT120-C10-2
- **Neils Kostrup Larsen** Per the AQR article, trends form because investors respond to information with different lags, and economic data is used to diversify responsiveness by capturing developments not yet visible in price.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > investors have different um time lag in terms of how they respond that's how trends form
  indicator: economic data vs price trend lag · asset: multi · horizon: months · testable: partly - lead-lag between economic indicators and prices · confidence: medium
  ^MT120-C10-X1

### C11
- **Katie Kaminski** Trend's convexity shows in the worst equity quintiles (crisis alpha): in stress fundamentals matter less than price changes, while in calm positive-fundamental years like 2025 (S&P +16%) economic trend can win.  #mech/cycle_persistence
  > in times of stress you know often times the fundamentals become irrelevant right and so it's really about the world changing and prices are changing
  indicator: SG Trend returns by equity quintile · asset: multi · horizon: months · conditions: stress vs benign fundamentals · testable: yes - quintile analysis · confidence: high
  ^MT120-C11-1
- **Katie Kaminski** Combining price trend and economic/macro strategies depends on investor mandate: risk-mitigation investors use trend for its stress behaviour and accept modest results in strong equity years.  #mech/risk_management
  > depending on the investor combining them can make sense
  asset: multi · testable: no - judgement · confidence: medium
  ^MT120-C11-2
- **Neils Kostrup Larsen** A Capgemini article projects alternatives rising from about $4 trillion to $12 trillion by 2034 (Everest Group sees $30 trillion by 2030), with high-net-worth investors at 20 to 25% and family offices at 30 to 50% allocation.  #mech/structural_shift _(time-bound view)_
  > from the current $4 trillion or so invested. um all the way to about $12 trillion by 2034
  indicator: alternatives AUM projections · asset: multi · horizon: years · testable: no - forecasts by consultants · confidence: medium
  ^MT120-C11-3

### C12
- **Neils Kostrup Larsen** Fiduciaries giving trend zero or 1% allocation are hard to justify since no paper argues trend fails to add value to a portfolio, and the shift toward private wealth access may raise allocations.  #mech/structural_shift
  > there's never been a white paper written to suggest uh the opposite
  indicator: fiduciary allocation to trend · asset: multi · horizon: years · testable: no - opinion · confidence: medium
  ^MT120-C12-1
- **Katie Kaminski** Private wealth and model-portfolio investors are gaining access to alternatives through ETFs and new products as concern over 60/40 grows.  #mech/structural_shift
  > Access is a function of both new products and new legislation
  indicator: access to alternatives for private wealth · asset: multi · horizon: years · testable: no - industry trend · confidence: medium
  ^MT120-C12-2
- **Katie Kaminski** Access of private wealth investors to alternatives is widening through new products (such as ETFs) and new legislation, a slow evolution that has sped up as concern about 60/40 grew.  #mech/new _(added by map cross-check)_
  > Access is a function of both new products and new legislation. For example, the ETF market is a good example of that.
  indicator: private wealth access · asset: alternatives · horizon: years · testable: no - qualitative · confidence: medium
  ^MT120-C12-R1
- **Katie Kaminski** Her firm builds portfolios of alternatives together ('alternatives completion'), the approach from which she argues that some managed futures adds more than expected.  #mech/new _(added by map cross-check)_
  > we have been you know for a long time in the alternatives completion space. So like building portfolios of alternatives together.
  indicator: alternatives completion · asset: alternatives · horizon: years · testable: no - qualitative · confidence: medium
  ^MT120-C12-R2

### C13
- **Katie Kaminski** Adding even some managed futures to stocks and bonds improves diversification more than expected because it is one of the few genuinely different return sources.  #mech/risk_management
  > having some trend falling or managed futures of any type actually gets you farther than you would think
  indicator: managed futures added to 60/40 · asset: multi · direction: add small trend allocation · horizon: years · testable: yes - portfolio blend backtest · confidence: medium
  ^MT120-C13-1
- **Neils Kostrup Larsen** Knowing the end client lets managers prevent mistimed allocation decisions after bad stretches such as Q2 2025; ETF flows hide the investor identity.  #mech/behavioral
  > if you know your clients and you can actually reach out and talk to them um you can avoid a lot of uh unnecessary uh hardship on their side
  indicator: investor timing of trend allocations · asset: multi · horizon: months · testable: no - behavioural · confidence: medium
  ^MT120-C13-2
- **Neils Kostrup Larsen** Private equity and private credit are not truly alternative, being familiar equity and credit exposure in a different wrapper, whereas true alternatives such as trend following offer a different return source.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > that's not really that alternative, right? That's really just um the same thing in a different um you know, clothing.
  indicator: private equity and private credit vs trend following · asset: multi · horizon: years · testable: partly - correlation of private assets with public markets · confidence: medium
  ^MT120-C13-X1

### C14
- **Katie Kaminski** In a model of target-retirement cash flows, managed futures improve the worst-case (bottom 5%) outcomes caused by poor timing of allocations or withdrawals.  #mech/risk_management
  > managed futures can improve some of the down you know the worst case scenarios or some of the sort of bottom 5%
  indicator: managed futures in target retirement portfolios · asset: multi · direction: add managed futures · horizon: years · conditions: sequence-of-returns risk near retirement · testable: yes - cash-flow simulation · confidence: medium
  ^MT120-C14-1
- **Katie Kaminski** Because individuals experience one sample path, managed futures' reduction of maximum drawdown in equity-heavy portfolios helps avoid retiring into a crash like 2008 (market down 60%).  #mech/risk_management
  > trend falling especially with equities has a naturally you know more diversified approach and it has lower maximum draw downs on average
  indicator: maximum drawdown reduction by managed futures · asset: multi · horizon: years · conditions: near retirement · testable: yes - drawdown comparison · confidence: medium
  ^MT120-C14-2

### C15
- **Neils Kostrup Larsen** A Dunn paper compares alternative investment strategies including trend in crisis periods to test which are true alternatives that diversify in stress.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > where we compare all the alternative investment strategies including trend and see how they perform
  indicator: alternative strategies in crisis periods · asset: multi · conditions: crisis periods · testable: yes - comparison across crisis windows · confidence: medium
  ^MT120-C15-X1

