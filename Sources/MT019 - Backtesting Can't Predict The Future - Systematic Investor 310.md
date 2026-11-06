---
source_id: MT019
title: "Backtesting Can't Predict The Future - Systematic Investor 310"
date: 2024-08-28
channel: "Top Traders Unplugged"
url: 
words: 10792
claims: 68
added_by_crosscheck: 6
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

## Argument map

**Episode thesis:** Richard Brennan argues that backtests overfit through hindsight selection and fitting to a known sequence of events and so cannot predict returns, and that only a walk-forward test on untouched out-of-sample data gives realistic drawdown (35-40% rather than 5-10%), CAGR and volatility benchmarks. He also argues that trends and mean reversion arise from collective trader impact (divergent versus convergent feedback forces) rather than from human behavioural bias, so AI agents will not end them, and that for 'outlier hunter' ensemble trend programs trade-return correlations, not price correlations, decide whether correlated markets diversify. Niels Kaastrup-Larsen adds that vol-scaled trend followers keep resizing after a volatility spike (so sell-side forced-selling estimates mislead), that convergence and systematic-macro strategies are what break in turbulence while sensible rule-based trend does not, and that the early-August 2024 shock was short and quickly reversed.

### Richard Brennan (Guest co-host; Australia-based systematic trend-following manager and researcher; self-described 'outlier hunter' using ensembles of trend models)
Fingerprint: #approach/trend_following #approach/research_robustness_overfitting #approach/regime_detection #approach/liquidity_flows #approach/behavioral_sentiment #approach/portfolio_construction_stacking #approach/diversification_risk_parity #approach/crisis_alpha_convexity
_Speaker note: Ledger spelling 'Richard Brennan' kept (captions give 'Richard Bren'/'Rich'). Captions carry no speaker labels; attribution is by content (Australia, 'our models', backtest vs walk-forward lecture, outlier hunter, I wasn't selling cocoa). Correction applied: the cocoa example of trend followers selling 80-90% of notional (MT019-C13-1) is Niels's; Brennan answers afterwards (C13-4). In C13, 'exogenous Africa supply news started the run, endogenous flows accelerated it' and 'large holders selling in April' are Brennan's._

**Worldview premises**
- Backtests always overfit; they should be used for sensitivity tests across simulated regimes but never to predict future expected returns. _[theoretical, stated; support: Comparison of backtest versus walk-forward results in his current research phase; argument from hindsight.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C06-1|C06-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C06-3|C06-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C06-2|C06-2]])
- Choosing the best of several parameter streams after the fact is a hindsight selection bias that cannot occur in live trading, and a backtest also overfits to noise and to a known sequence of events that the future will not repeat. _[theoretical, stated; support: Worked example with ten parameter settings over twenty years; 'we never have the road map'.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C06-4|C06-4]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C07-1|C07-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C07-2|C07-2]])
- Out-of-sample data, once used for development, is tainted; touching it to select or change models contaminates the test and results are far more sensitive to overfitting than people realise. _[theoretical, stated; support: Experience with in-sample/out-of-sample workflow; criticism of data-mining packages.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C07-4|C07-4]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C10-1|C10-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C10-2|C10-2]])
- A realistic out-of-sample equity curve resembles other managers' live track records, and its drawdown is much bigger (35-40%) than the backtest's (5-10%). _[empirical, stated; support: His own comparison (1970-2000 in-sample, 2000-2024 out-of-sample); 'trust me it is much bigger'. No dataset or specification given.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C07-5|C07-5]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C08-2|C08-2]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C09-1|C09-1]])
- Trend following depends on regime: in unfavourable regimes expect stagnation and drawdowns, so a volatile equity curve is normal and a straight line should not be expected; mean reversion modellers can expect no out-of-sample decay but trend followers cannot. _[theoretical, stated; support: Trends arrive irregularly; contrast with mean-reversion testing practice.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C08-1|C08-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C09-2|C09-2]])
- Trend followers' weak point is psychology, not the models: overriding rules causes errors, so discipline and patience are required. _[behavioural, stated; support: Plane-turbulence analogy and years of discussion on the podcast.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C03-3|C03-3]])
- Medium- to long-term trend following is more robust and has performed better than shorter-term trend following. _[empirical, stated; support: 'All the data that I've seen' (not cited).]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C03-4|C03-4]])
- Trends exist in any complex adaptive system, so human behavioural bias (prospect theory) is a symptom rather than the root cause; trends and mean reversion come from trader impact, the pressure of orders that must be matched. _[theoretical, stated; support: First-principles, physics-style argument; fundamentals and behaviour are 'derivative reasons'.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C10-3|C10-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C10-4|C10-4]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C13-R1|C13-R1]])
- Price impact is nonlinear (square-root law, Bouchaud), and groups of traders (trend followers, mean reverters, fundamental investors, HFT) exert collective forces whose combination moves price. _[empirical, stated; support: Bouchaud microstructure research cited.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C11-1|C11-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C11-2|C11-2]])
- Markets are nonstationary: the mix of participant groups changes as traders enter and leave, so the balance of divergent (positive-feedback) and convergent (negative-feedback) pressure shifts. _[theoretical, stated; support: Reference to Andrew Lo's adaptive markets hypothesis.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C11-3|C11-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C11-4|C11-4]])
- Market structure falls into three states: divergent wins (trend), convergent wins (mean reversion), or noise when neither wins and there is no directional move. _[theoretical, stated; support: Conceptual framework.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C12-1|C12-1]])
- In strong trends participants switch style to join them, amplifying the signal; so too many trend followers make trends more extreme, not extinct, while enough mean reverters can dissipate their own edge and the trend's. _[theoretical, stated; support: Feedback-loop reasoning; no data.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C12-2|C12-2]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C12-3|C12-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C12-4|C12-4]])
- AI agents also exert impact, so trends and mean reversion will persist and AI will not remove them. _[theoretical, stated; support: Extension of the agent-based, trader-impact view.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-1|C14-1]])
- Outliers are volatile and need an ensemble of models to extract; tiny differences in initial price paths (butterfly effect) produce widely dispersed trade results, so highly price-correlated markets can still have uncorrelated strategy returns. _[theoretical, stated; support: Brent versus WTI example with his own ensemble; nonlinear-mechanics analogy.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-2|C14-2]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-3|C14-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-4|C14-4]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-5|C14-5]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C15-1|C15-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C15-2|C15-2]])
- Publicly shown backtests (for example on Twitter) are beautiful equity curves; the industry should demand realism, since one never sees a bad backtest. _[behavioural, stated; support: Observation of social media and of a guest's remark that you never see a bad backtest.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C08-3|C08-3]])

**Chain: Why backtests mislead and what walk-forward testing fixes**
1. Full history laid out in hindsight → Selection among parameter streams and overfitting to noise and event order: The tester can pick the best stream and fit the known path; live trading has no such option. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C06-2|C06-2]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C06-4|C06-4]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C07-2|C07-2]])
2. Selected, overfit backtest → Upward-biased forward expectation and an unrealistically small drawdown: Hindsight selection bias. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C07-1|C07-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C08-2|C08-2]])
3. Develop on 1970-2000 only, then run untouched on 2000-2024 → Benchmarks for drawdown, CAGR and volatility that resemble live track records: Out-of-sample data simulates the right-hand side of the chart. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C07-3|C07-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C07-5|C07-5]])
4. Touching out-of-sample data to select or change models → Contamination and overfitting return: Tainted data cannot be reused. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C10-1|C10-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C07-4|C07-4]])
- Evidence: His own comparisons of backtest, out-of-sample and adaptive curves; figures (35-40% vs 5-10% drawdown) given without dataset or rules.
- Fails when: Out-of-sample data is reused for selection; also for trend followers one cannot expect no out-of-sample deterioration the way mean-reversion modellers do (regime dependence).

**Chain: Trader impact, divergent versus convergent forces and why trends persist**
1. Buyers and sellers must be matched → Price moves through order pressure, scaling with size by a square-root law: Mechanistic view of price formation. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C10-4|C10-4]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C11-1|C11-1]])
2. Groups of traders with the same model → Collective force that amplifies (divergent, positive feedback) or dissipates (convergent, negative feedback) trends: Aggregation of impacts across styles. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C11-2|C11-2]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C11-4|C11-4]])
3. A strong trend gets going → Mean reverters and others switch to trend, amplifying it: Fear of missing out; style switching. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C12-2|C12-2]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C12-3|C12-3]])
4. Enough mean reverters oppose a trend → Trend signal dissipates and a reversion to equilibrium follows: Convergence signals fight the prior trend. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C12-4|C12-4]])
5. Neither side dominates → Noise with no directional move: Third market structure. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C12-1|C12-1]])
- Evidence: Microstructure literature (Bouchaud), Lo's adaptive markets, and the 2024 cocoa run as an illustration; no test of the divergent/convergent mix.
- Fails when: Not stated; he treats the mix as nonstationary rather than breaking.

**Chain: Cocoa 2024 as an example of endogenous flows**
1. Supply news in Africa → Start of the cocoa run: Exogenous trigger. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C13-4|C13-4]])
2. Participants jumping on the bandwagon, global macro funds buying in March while dynamic-sizing trend followers sold → Acceleration of the trend and a higher price: Endogenous flow of participants. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C13-2|C13-2]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C13-4|C13-4]])
3. Large holders selling in April → Roughly 40% correction: Change in trader impact. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C13-4|C13-4]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C13-2|C13-2]])
- Evidence: Press reports and Brennan's recollection ('I can't remember the exact month'); Bouchaud's endogenous-over-exogenous conclusion is the host's gloss.
- Fails when: Not stated; Brennan notes the explanation is more intuitive than fundamental analysis, which is 'very complex and no guarantee'.

**Chain: Outlier hunting with ensembles: why correlated markets diversify**
1. Outlier (anomaly) with nonlinear, volatile price path → A single trend model is snagged by volatility and misses the move: Needs many models to maximise extraction. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C15-1|C15-1]])
2. Tiny differences in initial price paths → Widely dispersed trade results in nonlinear territory: Butterfly effect; trade correlation, not price correlation, matters. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-5|C14-5]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C15-2|C15-2]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-3|C14-3]])
3. Same ensemble on Brent and WTI → Quite uncorrelated return streams despite highly correlated prices: Small variations alter return profiles. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-4|C14-4]])
4. Strong outlier trend → Hold and pyramid with more models, accept big give-back at the turn: Outlier hunter's payoff structure. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C15-3|C15-3]])
- Evidence: His own test of an ensemble on Brent and crude (no numbers) and the 2024 cocoa episode.
- Fails when: Not stated; he says the conventional wisdom is right for nearly all other models.

**Decision process**
- [research] Develop and test models on in-sample data only (e.g. 1970-2000, multi-market over 30 years and about 100 markets); run the frozen models once on out-of-sample data (2000-2024) and never touch it afterwards.. Why: In-sample needs a lot of data for robustness; out-of-sample is the crucible for the whole process. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C07-3|C07-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C09-4|C09-4]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C10-2|C10-2]])
- [research] Compare three curves: the backtest ('pink unicorn'), the out-of-sample curve, and an adaptive workflow that periodically re-estimates in-sample and walks forward; set drawdown, CAGR and volatility expectations from the out-of-sample curve.. Why: Realistic benchmark; the backtest is always best and unrealistic. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C08-4|C08-4]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C09-1|C09-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C08-2|C08-2]])
- [research] Use backtests only for sensitivity tests across simulated regimes, not for expected-return forecasts; avoid data-mining packages that overfit and then try to remove it.. Why: Backtests are always overfit. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C06-3|C06-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C10-2|C10-2]])
- [signal] Prefer medium- to long-term trend following and treat short-term trading as different from trend following.. Why: Data he has seen suggest more robust and better performance. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C03-4|C03-4]])
- [signal] Run an ensemble of trend models per market for outliers; hold and pyramid with more systems getting in as the trend persists.. Why: A single system is snagged out by outlier volatility; ensemble maximises extraction. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C15-1|C15-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C15-3|C15-3]])
- [universe] Trade highly price-correlated markets (Brent and WTI) together when the ensemble's trade returns are uncorrelated.. Why: Trade correlation, not price correlation, determines diversification for outlier hunters. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-2|C14-2]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-3|C14-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-4|C14-4]])
- [sizing] Does not resize positions down with rising volatility after entry (cocoa 2024: held and added); accepts the big give-back when the trend turns.. Why: Outlier hunters stay with the trend; selling would miss the extreme move. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C15-3|C15-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-X1|C02-X1]])
- [risk] Follow the rules, with discipline and patience; do not override models under stress.. Why: Psychology is the weak point. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C03-3|C03-3]])

**Evidence style:** Argument from first principles and analogy (hindsight, physics of price impact, butterfly effect), and his own in-house walk-forward and ensemble tests reported without data; cites academic ideas (Bouchaud, Lo) and anecdotes such as cocoa.

**Views at the time**
- (late August 2024 (recording; upload 2024-08-28)) The early-August 2024 volatility shock was a short, sharp event that reversed quickly; trend models adapt fast and would have been well placed in a prolonged downtrend.. Reasoning: Trend followers were hit by the yen, Nikkei and Nasdaq early on but trends resumed. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C01-1|C01-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C01-2|C01-2]])
- (late August 2024 (recording; upload 2024-08-28)) The August losses came from the Nikkei, yen and equity indexes; equity indexes recovered within the month while the yen and Nikkei stayed down, and commodities kept trending well.. Reasoning: His own book. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C04-X1|C04-X1]])
- (late August 2024 (recording; upload 2024-08-28)) Monthly statistics hide intra-month volatility, so a month with a violent shock can look benign in the records.. Reasoning: Industry data is collected monthly. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C04-4|C04-4]])
- (late August 2024 (recording; upload 2024-08-28)) AI will not end trends or mean reversion; they are here to stay.. Reasoning: AI agents are traders whose orders exert impact. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-1|C14-1]])

### Niels Kaastrup-Larsen (Host of Top Traders Unplugged; veteran hedge fund manager; creator of the Trend Barometer)
Fingerprint: #approach/trend_following #approach/position_sizing_vol_target #approach/positioning_crowding #approach/manager_selection_allocation #approach/replication_indexing #approach/volatility_options #approach/research_robustness_overfitting #approach/costs_execution
_Speaker note: Mostly host, but states views on volatility-scaled trend sizing, what breaks in turbulence, carry in trend programs and sell-side flow estimates, so mapped. Correction applied: MT019-C13-1 (cocoa selling of 80-90% of notional) is his, not Brennan's. Correction applied to MT019-C05-3: SG CTA is +2.1% YTD (he caught his own slip), short-term traders +0.61% both month and year-to-date._

**Worldview premises**
- Vol-scaled trend followers become more defensive after a quick volatile event and keep selling after volatility rises even if prices recover, so a bounce does not mean a symmetric re-buy. _[institutional, stated; support: How volatility-targeted sizing works; 'some of us' resize, 'you don't'.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-1|C02-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-3|C02-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-X1|C02-X1]])
- Sell-side estimates of forced CTA equity selling (about $170B) are misleading because they ignore ongoing volatility-driven sizing and do not imply CTAs simply buy everything back. _[institutional, stated; support: Reasoning from vol-targeted sizing; no data.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-2|C02-2]])
- No market event breaks a rule-based trend system with sensible, tested (not AI-optimised) rules; drawdowns are painful but do not break the models, while convergence strategies and systematic macro tend to break in turbulence. _[experience, stated; support: Decades of trend history; the airplane-turbulence analogy (damage is inside, not structural).]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-4|C02-4]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-5|C02-5]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C03-1|C03-1]])
- Investor pressure for smoother returns pushes trend programs to add non-trend models such as carry, which dilutes the pure trend profile and may explain dispersion between managers. _[behavioural, stated; support: Observation of the industry; he expects August dispersion to show it.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C03-2|C03-2]])
- Volatility dampening and research that lowers drawdown are acceptable only if they do not change the long-term return profile or cause style drift; otherwise they just lower expectations. _[theoretical, stated; support: Aircraft-stabiliser analogy (stay on course).]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C03-5|C03-5]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C04-1|C04-1]])
- True diversification into commodities matters: managers concentrated in financials (to hold large AUM) suffered more in August. _[experience, stated; support: Cross-manager observation in the month.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C04-3|C04-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C04-2|C04-2]])
- Endogenous flows explain big moves more than exogenous news (Bouchaud), which fits the 2024 cocoa run in which global macro funds bought while dynamic-sizing trend followers sold. _[empirical, stated; support: Bouchaud's conclusion as the host recalls it; cocoa episode.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C13-1|C13-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C13-2|C13-2]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C13-3|C13-3]])
- Social-media backtests are unlikely to reproduce; big managers use some walk-forward process. _[experience, stated; support: Industry knowledge; not documented.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C09-3|C09-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C10-R1|C10-R1]])
- Not all managers use VaR-style volatility-sensitive risk models, so the market is not forced into synchronised selling. _[institutional, stated; support: 'A lot of people do but not everyone.']_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C15-4|C15-4]])
- Third-party indicators and data feeds can silently stop updating, so systematic users who rely on them face data-reliability risk. _[experience, stated; support: His Trend Barometer app stopped updating for a week.]_ ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C05-X1|C05-X1]])

**Chain: Quick vol spike and vol-scaled trend positioning**
1. Volatility rises in a short sharp event → Vol-scaled trend followers reduce exposure: Position sizes are tied to volatility. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-3|C02-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-1|C02-1]])
2. Prices rebound but volatility stays higher → CTAs may keep selling instead of buying back everything: Sell-side forced-selling estimates ignore this. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-2|C02-2]])
3. Trend followers split into those who resize continuously and those who hold size fixed after entry → Their flows and results differ in shocks: Different position management. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-X1|C02-X1]])
4. The shock was quick → The next shock may hurt less because positioning is more defensive: Positions already reduced. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-1|C02-1]])
- Evidence: Reasoning from sizing mechanics plus the August 2024 numbers read out (SG Trend -3.55%, short-term traders +0.61%); no flow data.
- Fails when: Not stated.

**Chain: Pressure for smoothness dilutes trend into non-trend models**
1. Investor pressure for return when there are no trends and for smoother returns → Managers add carry and other non-trend models: Wants a little extra return when trends are scarce. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C03-2|C03-2]])
2. Non-trend models in the program → Different performance in a turbulent month; dispersion between managers: Pure trend vs diluted profile. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C03-2|C03-2]])
- Evidence: Speculative; to be seen in end-of-month dispersion.
- Fails when: Not stated.

**Chain: VIX print versus futures and the speed of recovery**
1. VIX cash spike to about 65 that futures did not match → A short-lived volatility spike that subsided quickly: Like a fast news cycle. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C05-1|C05-1]])
2. Quick return to low-vol conditions → Trend Barometer (short timeframe) recovers to 61: Shorter-term signals recover quickly. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C05-2|C05-2]])
- Evidence: Blog post he read; barometer reading.
- Fails when: Not stated.

**Decision process**
- [sizing] Vol-scaled trend sizing: resize continuously with volatility rather than hold size fixed after entry.. Why: Keeps risk constant; after a vol rise exposure falls even if prices recover. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-3|C02-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-X1|C02-X1]])
- [research] Accept risk-reducing research (vol adjustment, lower drawdown) only if it leaves the long-term return profile and style unchanged.. Why: Otherwise it just lowers expectations or causes style drift. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C04-1|C04-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C03-5|C03-5]])
- [universe] Be truly diversified across sectors, including commodities, rather than concentrated in financials.. Why: Concentrated programs suffered more in August 2024. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C04-3|C04-3]])
- [research] Monitor trend through his Trend Barometer (61 late August) and track industry indices (Beta 50, SG CTA, SG Trend, short-term traders) against equities and bonds.. Why: Read on state and dispersion across managers. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C05-2|C05-2]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C05-3|C05-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C05-4|C05-4]])
- [risk] Keep sensible, tested rules and avoid AI-optimised tweaks.. Why: Rule-based trend with sensible rules does not break in turbulence. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-5|C02-5]])

**Evidence style:** Industry data read out weekly (indices, barometer), analogies (airplane turbulence), and long experience with trend managers; flags several views as untested.

**Views at the time**
- (late August 2024 (recording; upload 2024-08-28)) August 2024 was a roller coaster: equities were the hardest sector for trend followers, currencies (yen) difficult, fixed income divided, while sugar, coffee and grains trended well.. Reasoning: Observations from the month so far. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C04-2|C04-2]])
- (late August 2024 (recording; upload 2024-08-28)) The industry had not recovered as strongly as the managers he knows: Beta 50 -1.7% (+3.4% YTD), SG CTA -2.6% (+2.1% YTD), SG Trend -3.55% (+2.3% YTD), short-term traders +0.61%, against MSCI World +1% and S&P 500 TR +17.8% YTD.. Reasoning: Index numbers read out. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C05-3|C05-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C05-4|C05-4]])
- (late August 2024 (recording; upload 2024-08-28)) The calm may be the quiet before the storm when it really gets hairy; the quick volatile event is lucky because it leaves trend followers more defensive.. Reasoning: Little has changed across markets over a few weeks. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-R1|C02-R1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-1|C02-1]])
- (late August 2024 (recording; upload 2024-08-28)) Convergence and systematic-macro strategies are the ones likely to break in turbulence, not trend following.. Reasoning: Structure of those strategies. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C03-1|C03-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-5|C02-5]])

### Disagreements
- **Resizing positions when volatility rises (cocoa 2024)**: Niels Kaastrup-Larsen: Vol-scaled trend followers cut exposure as volatility rose (selling roughly 80-90% of notional in cocoa from January to April/May) and keep selling after a vol spike even if prices recover. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C13-1|C13-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-3|C02-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C02-X1|C02-X1]]); Richard Brennan: An outlier hunter does not resize down: he held cocoa and pyramided with more systems, accepting a big slap when the trend turned. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C15-3|C15-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C15-1|C15-1]])
- **Why trends exist: behavioural bias versus trader impact**: Richard Brennan: Behavioural bias (prospect theory) and fundamentals are symptoms; the root cause is trader impact and collective order flow, which AI agents will also exert. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C10-3|C10-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C10-4|C10-4]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-1|C14-1]]); Conventional view as characterised by Brennan: Trends come from behavioural bias (fear and greed) and from fundamental drivers; AI might make markets efficient enough to end trends. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C10-3|C10-3]])
- **Whether highly price-correlated markets add diversification**: Richard Brennan: True for nearly all models, but not for outlier hunters using ensembles, where trade-return correlation matters and Brent versus WTI returns are quite uncorrelated. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-2|C14-2]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-3|C14-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-4|C14-4]]); Conventional view as characterised by Brennan: Pick one of two highly correlated markets because diversification benefits dissipate after a certain number of markets. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-2|C14-2]])

### Gaps and conflicts
- The 35-40% out-of-sample versus 5-10% backtest drawdown comparison is asserted without dataset, rules, markets or sample size; the same-period live comparison with other managers is described, not shown. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C08-2|C08-2]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C07-5|C07-5]])
- Brennan says out-of-sample results are 'close to live track records of other managers', but also that out-of-sample data cannot be reused for selection; he does not say what happens to the first-use out-of-sample result once it is used to judge a program. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C07-5|C07-5]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C07-4|C07-4]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C10-1|C10-1]])
- Brennan's rule against hindsight selection conflicts with the practice of choosing his own program's rules after years of live experience; he does not address how the 2000-2024 period stays untouched when his own knowledge of it is in his design. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C07-3|C07-3]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C10-2|C10-2]])
- The ensemble/outlier-hunter claims (Brent versus WTI, 20 models) rest on his own test with no numbers; the butterfly-effect link is an analogy, not a test. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-4|C14-4]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C14-5|C14-5]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C15-2|C15-2]])
- Cocoa: Niels's 80-90% selling claim is generalised ('trend followers generally speaking'), not measured; Brennan cannot remember the month the run turned. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C13-1|C13-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C13-4|C13-4]])
- Corrections applied: cocoa example speaker (Niels), and the August index numbers (SG CTA +2.1% YTD, short-term traders +0.61% YTD). ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C13-1|C13-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C05-3|C05-3]])
- Niels says convergence strategies and systematic macro 'break' in turbulence, but also that some trend programs hold carry; the breaking claim is asserted from structure, not evidence. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C03-1|C03-1]], [[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C03-2|C03-2]])
- Brennan asserts medium- to long-term trend following has performed better than shorter-term, but cites no data and says short-term trading is not trend following. ([[MT019 - Backtesting Can't Predict The Future - Systematic Investor 310#^MT019-C03-4|C03-4]])

### Forward-looking inputs (reader synthesis)
(reader) The speakers claim no forward-looking input for prices: Brennan's thesis is that backtests cannot predict the future, so expectations should come from out-of-sample drawdown, CAGR and volatility benchmarks, with regime (favourable or unfavourable for trend) as the driver. Niels reads the Trend Barometer (short timeframe), index dispersion and model speed as state indicators, and expects volatility to stay higher after a spike, keeping vol-scaled trend followers defensive. The trader-impact framework implies watching the mix of divergent and convergent participants, but no observable proxy is named.

### Reader inferences (not stated by the speakers)
- (reader) Brennan's framework suggests a test: trend returns should be higher when order-flow concentration (many participants flipping to trend) is high; no measurable proxy is proposed in the episode.
- (reader) The disagreement over resizing volatility (Niels resizes, Brennan holds and pyramids) implies a testable difference in outlier-period performance: constant-risk sizing should lag in extreme trends and lose less at reversals.
- (reader) Walk-forward testing as described is a single split; it is sensitive to the choice of split date (2000), which the speaker does not discuss.

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
- **Niels Kaastrup-Larsen** Little has changed in most markets over a few weeks, so the calm could be the quiet before a harder stress.  #mech/new _(added by map cross-check, time-bound view)_
  > this could be quiet before the storm when it really gets hairy
  asset: multi · direction: n/a · horizon: weeks · conditions: after a quick volatile event · testable: no · confidence: low
  ^MT019-C02-R1

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
- **Niels Kaastrup-Larsen** Data-mining software vendors may sell an overfitting module and then a second module to remove the overfit.  #mech/research_method _(added by map cross-check)_
  > they'll make you pay for having something that gives you complete over optimized and overfitted result and then the next module you have to pay for is the one that takes it all out again
  asset: multi · direction: n/a · horizon: n/a · conditions: joking aside about vendors · testable: no · confidence: low
  ^MT019-C10-R1

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
- **Richard Brennan** Trader-impact explanations are more intuitive than fundamental analysis, which is complex and gives no guarantee that a given fundamental is what is causing the move.  #mech/new _(added by map cross-check)_
  > rather than having to worry about all the details of knowing your fundamental analysis and all of these things which is very complex and there's no guarantee that is actually causing that result
  asset: multi · direction: n/a · horizon: n/a · testable: no · confidence: medium
  ^MT019-C13-R1

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

