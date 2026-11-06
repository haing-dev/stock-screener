---
source_id: MT020
title: "Bill's Turtle Trading Journey, Modern Systematic Trading, and more!  - Open Interest 10"
date: 2024-10-26
channel: "Top Traders Unplugged"
url: 
words: 9987
claims: 55
added_by_crosscheck: 9
corrections: 1
crosscheck: "opus cross-check"
speakers: ["Bill Eckhardt (guest, co-creator of the Turtle system, Eckhardt Trading Company)", "Rob Santino (guest, president and COO, Eckhardt Trading Company)", "Moritz Seibert (host, Open Interest series)"]
tags: [source, layer0]
---
# Bill's Turtle Trading Journey, Modern Systematic Trading, and more!  - Open Interest 10

**Speakers:** Bill Eckhardt (guest, co-creator of the Turtle system, Eckhardt Trading Company); Rob Santino (guest, president and COO, Eckhardt Trading Company); Moritz Seibert (host, Open Interest series)

**Summary:** Eckhardt and Santino discuss the Turtle origins and how ETC evolved from published breakout rules: risk control first (utility theory), avoiding overfitting and underfitting, the E-score and Gauntlet testing process. Key views: futures returns are heavy-tailed so use robust statistics and long samples; reject high win-rate strategies; keep position sizes constant, no vol targeting; diversify to ~70 liquid markets; avoid stocks and CTA replication.

**Approach:** trend following, risk control and utility theory, overfitting and robust statistics, diversification, Turtle trading history

**Cross-check completeness estimate of first read:** 0.90 - first reader caught the core risk-control, fitting and statistics claims; missed several host elaborations (hidden mean reversion, SD vs normality, Mandelbrot evidence, long-term robustness) and Santino's replication call; one speaker error.

## Argument map

**Episode thesis:** Bill Eckhardt (co-creator of the Turtle rules) argues that futures markets are too close to random to predict (hit rate about 51-52%), so success comes from risk control built on utility theory, robust distribution-free statistics on long samples, and a research process (E-score, Gauntlet) designed to limit overfitting and underfitting. Eckhardt Trading Company therefore runs mostly trend following (about 80%) across about 70 liquid futures markets, keeps position sizes constant instead of targeting volatility, rejects high win-rate strategies, avoids stocks and regression-based CTA replication, and treats the discomfort of trading as the real edge ('pain arbitrage').

### Bill Eckhardt (Founder, Eckhardt Trading Company (ETC); co-creator of the Turtle trading rules with Richard Dennis; background in philosophy of science and mathematics)
Fingerprint: #approach/trend_following #approach/research_robustness_overfitting #approach/position_sizing_vol_target #approach/crisis_alpha_convexity #approach/behavioral_sentiment #approach/diversification_risk_parity #approach/costs_execution #approach/replication_indexing
_Speaker note: First podcast appearance. Auto-captions garble names ('Moret', 'Rich Dennis'). The intro calls Santino president and CEO while the ledger calls him COO; both appear. Which of Eckhardt and Santino answers a few mid-conversation questions on sizing is not always clear from the captions; the ledger's attribution (Santino for volatility and sizing) is kept._

**Worldview premises**
- Money flows from the many to the few; normal human reflexes (holding losers, enjoying trading) put you among the many and losing, so success requires going against inclination and suffering some discomfort. _[behavioural, stated; support: Anecdote about non-traders at parties who say losers need not be cut; career observation.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C01-1|C01-1]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C14-1|C14-1]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C14-2|C14-2]])
- Trading success needs more than entry rules: risk management and attitudes to profit and loss matter at least as much, and mechanizing trading is much harder than Dennis's 'weighted rules' view suggested. _[experience, stated; support: His account of the Turtle programme (Dennis ran risk control, Eckhardt developed rules).]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C01-2|C01-2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C02-1|C02-1]])
- A theory of trading should be built the way science builds theories: start oversimplified (as ballistics did) and add factors as research proves them relevant; he has formalised parts, not a complete theory. _[theoretical, stated; support: Philosophy of science analogy (cannonball trajectories).]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C02-2|C02-2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C03-1|C03-1]])
- Markets are not random but too close to random for simple predictions, so effort should go into risk control (which one can know and control) rather than prediction; accuracy is only about 51-52%. _[empirical, stated; support: Own experience; no data shown.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C03-2|C03-2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C04-1|C04-1]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C13-4|C13-4]])
- Utility theory gives a rigorous basis for risk aversion (diminishing marginal utility, losses weigh more than gains); risk-neutral and risk-loving utilities lead to ruin, shown by the St Petersburg paradox, so risk aversion is primary in leveraged futures trading. _[theoretical, stated; support: Decision theory, St Petersburg paradox, and observed traders who lost everything.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C04-2|C04-2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C04-4|C04-4]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C05-1|C05-1]])
- Most traders build a profitable system and graft risk control on afterwards ('Island of Dr Moreau'); ETC instead brings expected utility in at the ground floor and judges every idea by its effect on expected utility. _[experience, stated; support: Contrast with 'all other traders that I know of'.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C04-3|C04-3]])
- Futures returns and system trade results are radically non-normal with heavy tails (Mandelbrot: possibly no variance), so normal small-sample statistics, standard deviations and least-squares correlation give wrong answers; robust, distribution-free statistics are required. _[empirical, stated; support: Mandelbrot's cotton-price work; LTCM's failure; his own observation of leptokurtosis in every futures market.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-1|C12-1]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-3|C12-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-X2|C12-X2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C13-2|C13-2]])
- Robust statistics need 10 to 30 times more data, so ETC needs 10-20 years of data and cannot draw valid conclusions from two or three years, which would be overfitting. _[theoretical, stated; support: Statistical argument.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-2|C12-2]])
- Overfitting is real (some good traders lost everything) but underfitting is also costly because it ignores worthwhile market information; fitting should capture permanent features and ignore transitory ones, and some overfitting is unavoidable. _[theoretical, stated; support: In-house techniques to estimate the overfit; no figures shown.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C08-3|C08-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C09-1|C09-1]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C08-R3|C08-R3]])
- Summary statistics of signals (a moving average) discard structure; keeping the 20-day high and low retains position within the range. Structure cannot all be kept (combinatorially impossible), so research must discard structure while keeping what matters. _[theoretical, stated; support: Worked example of 20 closes into 1 versus 2 numbers.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C07-3|C07-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C08-1|C08-1]])
- Volatility is a moving-average process, so moving averages suit volatility; price is non-stationary and not an MA process, so moving averages and crossovers on price are counterproductive and have no theoretical support. _[theoretical, stated; support: Time-series statistics; a quip that traders also trade gold by the sun and silver by the moon.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C08-2|C08-2]])
- Futures prices do not mean-revert, but volatility does, so ETC's non-trend methods (about 20% of work) are neither trend following nor counter-trend, and not mean reversion. _[empirical, stated; support: Assertion; methods are not disclosed.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C07-2|C07-2]])
- High win-rate strategies (such as selling cheap options) periodically bust because they exploit the bulk of the distribution while the tails are heavy; ETC prefers a roughly 40% success rate with larger winners. _[empirical, stated; support: Principle used in rejecting any new system with a 70-80% success rate; no example data.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C13-3|C13-3]])
- Turtle breakout rules were widely published (one Turtle published the proprietary manual), so the edge was degraded by competition; trend following has been declared dead every few years, yet most of ETC's work is still trend following. _[experience, stated; support: Career-long observation; he left the Turtle rules even before they were released.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C05-4|C05-4]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C05-5|C05-5]])
- Red Queen effect: with more competition and technical analysis knowledge, a trader must improve as fast as possible just to hold his own. _[theoretical, stated; support: Alice in Wonderland analogy.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-1|C06-1]])
- Diversification is the greatest financial idea of the 20th century; ETC trades about 70 markets but avoids markets with too much slippage or too little liquidity, and many traders undercut diversification by concentrating on whichever few markets are hot. _[experience, stated; support: Slippage and liquidity measurement on all markets.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C10-3|C10-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C10-X1|C10-X1]])
- So-called alternative markets look better in backtests but slippage and difficulty exiting in a hurry make them worse in practice. _[experience, stated; support: Argument about paper versus practical performance.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C11-1|C11-1]])
- Single stocks differ from futures (splits, dividends, a market dominated by longs, while futures are balanced one long per short) and have a weaker trend component, so ETC specialises in futures where it has a relative advantage. _[experience, stated; support: Studied stocks but 'no claim of expertise'; relative-advantage argument.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C11-2|C11-2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C11-3|C11-3]])
- Replicating CTA indices by regression 'sounds like an invitation to really overfit', since futures price changes and trade results are radically non-normal. _[theoretical, stated; support: Statistical reasoning; no test of an actual product.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C11-4|C11-4]])
- Some Turtle trainees dropped out or could not get along, which showed they lacked the right emotional makeup. _[experience, stated; support: Anecdote.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C15-1|C15-1]])

**Chain: From unpredictable markets to risk control first**
1. Markets are not random but too close to random; accuracy only about 51-52% → Prediction cannot be the main edge: Simple predictions fail; profits come from handling outcomes. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C03-2|C03-2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C13-4|C13-4]])
2. Risk can be known, changed and controlled → Put ten times the emphasis on risk control as on prediction; decide what to do wherever the market goes: Risk control makes profits follow. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C04-1|C04-1]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C13-4|C13-4]])
3. Diminishing marginal utility of money → Risk aversion is a rigorous requirement; utility enters research at the ground floor: Risk-neutral or risk-loving utilities mean ruin in leveraged trading. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C04-2|C04-2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C04-3|C04-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C04-4|C04-4]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C05-1|C05-1]])
- Evidence: Utility theory, St Petersburg paradox, observed ruin of risk-loving traders; no performance data.
- Fails when: Not stated.

**Chain: Heavy tails and why robust statistics need long samples**
1. Futures price changes and trade results have heavy tails (leptokurtosis; possibly no variance) → Normal-distribution statistics, standard deviations and least-squares correlations are unreliable: Mandelbrot's evidence; LTCM's failure using normal theory. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-1|C12-1]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-3|C12-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-X2|C12-X2]])
2. Use robust, distribution-free statistics → Need 10 to 30 times more data, hence 10-20 years; two or three years is overfitting: They make no distribution assumptions and so waste information. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-2|C12-2]])
3. Heavy left tails in every market → Trading rules must intervene (stops, exit rules) to keep the left tail under control: Risk management is the main use of rules against leptokurtosis. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C13-2|C13-2]])
- Evidence: Mandelbrot's cotton-price studies (cited by the host); LTCM; his observation across futures markets.
- Fails when: Not stated.

**Chain: Why high win-rate strategies fail**
1. Strategies that sell cheap options or exploit oscillation around the mean → Success rates of 70-90% from exploiting the bulk of the distribution: Most observations sit around the mean (leptokurtosis). ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C13-3|C13-3]])
2. Tail events eventually materialise → Large, freakish, unprotected losses; periodic bust-outs: The strategy depends on the tails not happening. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C13-3|C13-3]])
3. Rule: reject any new system with a 70-80% success rate → Prefer roughly 40% success with winners much larger than losers: Cut losses, let profits run. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C13-3|C13-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C14-1|C14-1]])
- Evidence: Principle and long-sample observation; no numbers on specific systems.
- Fails when: Not stated.

**Chain: Constant position size versus volatility-resizing**
1. Volatility often rises as a trend extends → Resizing to current volatility would cut the position along with the trend: Hidden mean-reversion trade against the trend (host's point). ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-4|C06-4]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C07-X1|C07-X1]])
2. Keep entry size roughly constant to exit with a stop loss → Controlled risk and a synthetic long-optionality profile: Losses are capped while trend extension is fully captured. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C07-1|C07-1]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-4|C06-4]])
3. Higher volatility helps trend systems; low volatility should not be 'juiced up' → No portfolio volatility target; track each future's volatility for risk: Let systems run as designed. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-3|C06-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-2|C06-2]])
- Evidence: ETC tested adjusting to current volatility and found it counterproductive; no results shown.
- Fails when: Not stated.

**Chain: Why published rules decay**
1. Turtle rules and risk control were widely disclosed → Breakout systems heavily degraded: Competition on the same published edge. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C05-4|C05-4]])
2. Short-term systems show alpha decay (host) → Many Turtle students moved to longer holding periods; longer-term systems (around 200-day look-backs) still work: Edge persists where it is harder to arbitrage. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C05-3|C05-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C05-X1|C05-X1]])
3. More competition and technical analysis knowledge → Researchers must keep improving (Red Queen): Standing still means losing ground. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-1|C06-1]])
- Evidence: Eckhardt's own Turtle history; the host's observation about students.
- Fails when: Not stated; he says trend following has been declared dead repeatedly without it being so.

**Chain: Why ETC avoids replication and stocks**
1. Regression-based replication fits index returns with 10-20 markets → Invitation to overfit; radically non-normal data: Normal-theory regression on fat-tailed series. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C11-4|C11-4]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-X1|C12-X1]])
2. No predefined exits in replication portfolios → Exposure to discontinuity and gap events: Without stops losses are not known in advance (host's point, Eckhardt agrees). ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C13-1|C13-1]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C13-2|C13-2]])
3. Stocks differ structurally from futures → ETC does not trade them: Weaker trend component and no relative advantage. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C11-2|C11-2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C11-3|C11-3]])
- Evidence: Reasoning from distribution theory; no test of replication products.
- Fails when: Not stated; Santino says only 'it will end badly' as a prediction.

**Decision process**
- [research] Evaluate every idea by its effect on expected utility from the start of research, using a small class of utility functions chosen for commodity trading and client circumstances.. Why: Avoids grafting risk control onto a profit system. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C04-2|C04-2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C04-3|C04-3]])
- [research] E-score: combine many performance measures into one, and discount systems that earn most profit in a short span (for example 2 of 20 years).. Why: Guards against false impressions of quality. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C09-2|C09-2]])
- [research] Gauntlet: a barrage of tests designed to tear a system apart; also tests the program code for subtle glitches.. Why: Shows where a system fails and removes emotion. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C09-3|C09-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C10-1|C10-1]])
- [research] Use robust, distribution-free statistics with 10-20 years of data and in-house techniques to estimate and minimise overfit.. Why: Heavy tails and the data appetite of robust statistics. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-1|C12-1]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-2|C12-2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C08-3|C08-3]])
- [signal] Prefer signals that keep structure (e.g. 20-day high and low) to single summary statistics; use moving averages for volatility only, not for price.. Why: Price is non-stationary; volatility is a moving-average process. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C07-3|C07-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C08-2|C08-2]])
- [signal] Run short, medium and long-term systems with average trade lengths of about 4-5 days to 50-60 days; volatility enters five or six ways (sizing, measuring price change, risk control) alongside price.. Why: Covering several time horizons within trend following; about 80% trend, 20% non-trend, non-counter-trend methods. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C05-2|C05-2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-2|C06-2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C07-2|C07-2]])
- [sizing] Keep initial position size roughly constant from entry to exit; no portfolio volatility target; no readjustment to rising volatility; stop-loss for each trade.. Why: Volatility rises with trends and resizing cuts exposure when the trend is working. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-3|C06-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-4|C06-4]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C07-1|C07-1]])
- [risk] Reject any new system with a 70-80% success rate; accept about 40% winners with larger winners; cut losses, let profits run; place ten times more emphasis on risk control than on prediction.. Why: High win-rate systems depend on tails not happening. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C13-3|C13-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C13-4|C13-4]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C14-1|C14-1]])
- [universe] Trade about 70 futures markets, measuring liquidity and slippage on every market and avoiding illiquid or high-slippage ones; no single stocks.. Why: Diversification is valuable but slippage makes alternative markets worse than backtests suggest. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C10-3|C10-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C11-1|C11-1]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C11-2|C11-2]])
- [portfolio] Do not replicate CTA indices; do not concentrate on hot markets.. Why: Overfit and no exits; anti-diversification. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C11-4|C11-4]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C10-X1|C10-X1]])
- [other] Keep specific Gauntlet and overfit-estimation methods secret and unpublished.. Why: Industry competition (he says he would like to publish). ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C10-R2|C10-R2]])

**Evidence style:** First principles and mathematical argument (utility theory, statistics, philosophy of science) plus long personal experience and anecdote. He gives no backtest numbers, track record or performance data and says the key methods are secret, so claims about robustness are asserted rather than shown.

**Views at the time**
- (2024-10 (upload 2024-10-26; Open Interest 10)) Trend following is not dead and remains the majority (about 80%) of ETC's systematic work; non-trend methods are about 20%.. Reasoning: Trend following has been declared dead every few years; competition requires constant research. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C05-5|C05-5]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C07-2|C07-2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-1|C06-1]])
- (2024-10) ETC trades about 70 markets and avoids alternative markets that look better only on paper; it does not trade stocks.. Reasoning: Liquidity and slippage; relative advantage in futures. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C10-3|C10-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C11-1|C11-1]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C11-2|C11-2]])
- (2024-10) Regression-based CTA replication products are an invitation to overfit.. Reasoning: Non-normal data, no predefined exits. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C11-4|C11-4]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C13-2|C13-2]])
- (2024-10) Do not infer anything from two or three years of data; 10-20 years are needed.. Reasoning: Robust statistics need much more data. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-2|C12-2]])

### Rob Santino (President (and CEO/COO per the intro and ledger) of Eckhardt Trading Company; runs the research lab)
Fingerprint: #approach/trend_following #approach/research_robustness_overfitting #approach/position_sizing_vol_target #approach/costs_execution #approach/replication_indexing
_Speaker note: Answers on volatility, sizing, the Gauntlet and the firm's research culture. A couple of the sizing answers could be Eckhardt's; the ledger's attribution is kept._

**Worldview premises**
- Volatility enters ETC's systems in five or six ways (sizing, measuring price change, risk control) alongside price, so systems are based on both price and volatility. _[experience, stated; support: Own firm design; details withheld.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-2|C06-2]])
- ETC does not target portfolio volatility because higher volatility often helps trend systems and they do not want to juice up when volatility is low; they track individual futures' volatility for risk. _[experience, stated; support: Firm practice.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-3|C06-3]])
- Position sizes are held roughly constant from entry to exit because readjusting to rising volatility would cut the position along with the trend, which they found counterproductive. _[experience, stated; support: Testing at ETC; no results shown.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-4|C06-4]])
- The Gauntlet is a barrage of tests designed to tear a system apart, showing where it fails (as important as knowing why it works) and removing emotion; systems can have a strong 2-4 month run and then go flat. _[experience, stated; support: Formal process used for many years, also offered to outside ideas and University of Chicago students.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C09-3|C09-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C09-4|C09-4]])
- Regression-based CTA-index replication products are likely to end badly. _[experience, stated; support: Opinion, 'I'll go on record'.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-X1|C12-X1]])

**Decision process**
- [sizing] No portfolio volatility target; keep original position size roughly constant, with only small technical adjustments; monitor volatility of each future for risk.. Why: Volatility helps trends; resizing is counterproductive. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-3|C06-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-4|C06-4]])
- [research] Run systems through the Gauntlet and rely on the E-score, especially when blending systems.. Why: Know where failures are; remove emotion. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C09-3|C09-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C09-4|C09-4]])

**Evidence style:** Firm practice and process description; no results disclosed.

**Views at the time**
- (2024-10) Replication products will likely end badly.. Reasoning: Offered as opinion. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-X1|C12-X1]])

### Moritz Seibert (Host of the Open Interest series (Top Traders Unplugged); systematic trading practitioner)
Fingerprint: #approach/trend_following #approach/research_robustness_overfitting #approach/position_sizing_vol_target #approach/replication_indexing #approach/diversification_risk_parity
_Speaker note: Asks most questions but contributes substantive views on alpha decay, hidden mean reversion, fat tails and exits, so he is mapped. The ledger's C13-1 was wrongly attributed to Santino; it is Seibert (applied correction)._

**Worldview premises**
- Many Turtle students and systematic diversified trend followers moved to longer holding periods because of alpha decay in short-term systems; longer-term systems (around 200-day look-backs) continue to work and are robust with drawdowns. _[empirical, stated; support: Observation of the trend-following community.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C05-3|C05-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C05-X1|C05-X1]])
- Constant sizing with a stop-loss gives controlled risk and a synthetic long-optionality (volatility-seeking) profile. _[theoretical, stated; support: Payoff reasoning.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C07-1|C07-1]])
- Resizing an open trend position to rising volatility is a hidden mean-reversion trade against the trend, since volatility usually rises as the trend extends. _[theoretical, stated; support: Reasoning, 'not always true by definition but more often than not'.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C07-X1|C07-X1]])
- More markets give more independent bets and less noise in any run, though smaller portfolios can outperform for periods through concentration. _[experience, stated; support: Diversification is 'free' because the computer does the work.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C10-2|C10-2]])
- Futures returns are fat-tailed on both sides and jump-prone, possibly a stable Paretian distribution with no defined variance (Mandelbrot's cotton work); computing volatility as a standard deviation for sizing reintroduces normal-distribution assumptions, whereas range-based measures like ATR are not standard deviations. _[empirical, stated; support: Mandelbrot's 'Misbehavior of Markets'.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-X2|C12-X2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-X3|C12-X3]])
- Regression-based replication portfolios lack predefined exits and so are exposed to discontinuity and gap events; stops and exit rules that keep losses small keep a trader in business. _[theoretical, stated; support: Risk-management reasoning; he does not forecast how replication will end.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C13-1|C13-1]])
- The trend follower's edge is a pain arbitrage: enduring bad periods with individual losses kept small. _[behavioural, stated; support: Practitioner framing.]_ ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C14-2|C14-2]])

**Decision process**
- [sizing] Initial position sizing and keeping many small positions is the most important aspect of risk control; separately decide whether to hold size constant, or respond to correlations, volatility and VaR.. Why: Overtrading is the main risk. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C07-1|C07-1]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C07-X1|C07-X1]])

**Evidence style:** Practitioner reasoning and literature (Mandelbrot); no data.

**Views at the time**
- (2024-10) Short-term systems show alpha decay while 200-day-type trend systems remain robust.. Reasoning: Student shift to longer holding periods. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C05-3|C05-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C05-X1|C05-X1]])

### Disagreements
- **Volatility targeting and position resizing**: Rob Santino: ETC does not target portfolio volatility and keeps position sizes roughly constant; resizing to rising volatility is counterproductive. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-3|C06-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-4|C06-4]]); Moritz Seibert: Asks whether markets are normalised to a common volatility target (the common industry approach), then agrees that resizing is a hidden mean-reversion trade; notes that standard-deviation-based volatility reintroduces normality. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C07-X1|C07-X1]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-X3|C12-X3]])
- **Alternative markets and market count**: Moritz Seibert: Frames alternative markets as just markets, notes claims of better trending and risk-adjusted returns, and favours maximum diversification (more independent bets, less noise), while conceding that smaller portfolios can outperform for periods. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C10-2|C10-2]]); Bill Eckhardt: Alternative markets look better on paper but are worse in practice because of slippage and exit difficulty; trades about 70 markets and avoids illiquid ones. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C10-3|C10-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C11-1|C11-1]])
- **Is the non-trend part mean reversion or carry?**: Moritz Seibert: Asks whether ETC's non-trend add-on is mean reversion or carry. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C07-2|C07-2]]); Bill Eckhardt: It is not mean reversion because futures prices do not mean-revert (volatility does); the methods are neither trend nor counter-trend and are about 20% of the work. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C07-2|C07-2]])
- **Mechanising trading and risk control within the Turtle programme**: Bill Eckhardt: Mechanising trading is much harder than it looks; between him and Dennis he was the more risk-averse trader and Dennis controlled the programme's risk. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C02-1|C02-1]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C01-2|C01-2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C03-R1|C03-R1]]); Richard Dennis (as reported by Eckhardt): Thought trading could be mechanised with 'weighted rules' and ran risk control the Turtle way; he and Eckhardt argued often. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C02-1|C02-1]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C01-2|C01-2]])

### Gaps and conflicts
- No performance, backtest, E-score or Gauntlet results are disclosed; Eckhardt says the methods must stay secret, so claims such as accurate overfit estimation, 51-52% accuracy and the ~40% success target cannot be checked. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C09-2|C09-2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C13-4|C13-4]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C13-3|C13-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C10-R2|C10-R2]])
- Eckhardt says he knows of no one who does curve fitting yet also says some overfitting is inevitable and good traders lost everything from it; the tension is left unresolved. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C08-3|C08-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C09-1|C09-1]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C08-R3|C08-R3]])
- He argues no portfolio volatility target and constant size, yet says volatility enters ETC's systems five or six ways and that range-based measures exist; the exact role of volatility is not specified. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-2|C06-2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-3|C06-3]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-X3|C12-X3]])
- He says ETC moves from short-term systems for alpha decay (per the host), yet runs trades averaging 4-5 days, which the host calls short term; Eckhardt calls them 'short only relative to other traders'. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C05-2|C05-2]], [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C05-3|C05-3]])
- The mean-reversion denial says futures prices do not mean-revert; no evidence is given and many CTAs add reversion components. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C07-2|C07-2]])
- Ledger attribution fix: the point on replication lacking predefined exits (C13-1) is the host's, not Santino's; Eckhardt agrees wholeheartedly. ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C13-1|C13-1]])

### Forward-looking inputs (reader synthesis)
(reader) The speakers do not offer forward-looking market inputs; they say prediction is only 51-52% accurate. Their forward-looking claims are about process: use 10-20 years of data, robust statistics, constant sizing, stop losses, many liquid markets; expect more competition and edge decay so research must continue; expect replication products to end badly in a tail event. The horizon for trend systems is 4-5 to 50-60 day average trade lengths.

### Reader inferences (not stated by the speakers)
- (reader) Eckhardt's two themes, no prediction and robust statistics, imply that backtests on short samples (two or three years) or using Sharpe-type moments should be given little weight; this is directly testable against any claimed track record.
- (reader) The claim that high win-rate systems 'periodically bust out' is a convexity argument: a ~40% hit-rate, positive-skew profile with stops is long optionality, consistent with Seibert's 'synthetic long optionality'.
- (reader) Not targeting volatility means risk varies over time with volatility; a macro overlay using his framework would expect trend returns to be higher when volatility is high.
- (reader) The preference for futures over stocks rests on a structural claim (balanced longs/shorts, no dividends/splits) that explains the lack of trend in stocks; no empirical test is offered.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | intro; many-to-few principle; Eckhardt's role in Turtles |
| C02 | 2 | Eckhardt-Dennis background, mechanization, theory-building |
| C03 | 2 | ballistics analogy, ETC as research lab, risk aversion and prediction futility |
| C04 | 4 | risk control first, utility theory, risk-loving utilities |
| C05 | 5 | risk aversion; trade horizons; Turtle rule degradation; death of trend following |
| C06 | 4 | Red Queen; volatility use; no vol targeting; constant sizing |
| C07 | 3 | stop-loss optionality; vol mean-reverts; non-trend 20%; summary statistics |
| C08 | 3 | structure vs summary statistics, moving averages, overfitting and underfitting |
| C09 | 4 | underfitting, E-score, Gauntlet |
| C10 | 3 | Gauntlet tests code; alternative markets, diversification, liquidity and slippage |
| C11 | 4 | alternative markets slippage; stocks vs futures; replication; non-normality |
| C12 | 3 | robust statistics and data needs; LTCM; Mandelbrot |
| C13 | 4 | replication and stops; fat left tail; high win-rate systems; prediction vs risk control |
| C14 | 2 | human biases, cut losses, pain arbitrage; Turtle selection |
| C15 | 1 | Turtles drop-outs; outro |

## Claims

### C01
- **Bill Eckhardt** Money flows from the many to the few, so normal human reflexes put you among the many and losing; successful trading feels unpleasant and requires suffering and not following inclinations.  #mech/behavioral
  > the structure of the market is that the money flows from the many to the few so you have to be among the few not among the many
  asset: multi · testable: no - behavioral principle · confidence: high
  ^MT020-C01-1
- **Bill Eckhardt** Trading success needs more than entry rules: risk management and attitudes toward profit and loss; Dennis ran the Turtles' risk control while Eckhardt developed rules.  #mech/risk_management
  > there's more to trading than Simply Having rules you have risk management
  asset: multi · testable: no - qualitative · confidence: medium
  ^MT020-C01-2

### C02
- **Bill Eckhardt** Eckhardt thought mechanizing trading (versus Dennis' 'weighted rules' view) was much harder than it seemed.  #mech/research_method
  > it was much harder to mechanize what is needed for trading
  asset: multi · testable: no - opinion · confidence: medium
  ^MT020-C02-1
- **Bill Eckhardt** His approach was to build a theory of trading from the philosophy of science, formalizing pieces rigorously rather than a complete theory.  #mech/research_method
  > I have formalized certain parts of trading in a mathematically rigorous fashion
  asset: multi · horizon: years · testable: no - method statement · confidence: medium
  ^MT020-C02-2

### C03
- **Bill Eckhardt** Like ballistics, a trading theory starts oversimplified (few factors) and improves as research adds relevant factors.  #mech/research_method
  > because you have to oversimplify a problem sometimes in the beginning
  asset: multi · horizon: years · testable: no - analogy · confidence: medium
  ^MT020-C03-1
- **Bill Eckhardt** Markets are not random but too close to random for simple predictions, so focus should be on risk control, which one can know and control, rather than prediction.  #mech/risk_management
  > we can't be very successful about predicting where the Market's going to go it's too close
  indicator: market predictability · asset: multi · direction: focus on risk control not prediction · testable: partly - low predictability is testable · confidence: high
  ^MT020-C03-2
- **Bill Eckhardt** Eckhardt says that, of him and Richard Dennis, he was the more risk-averse trader; they disagreed throughout the Turtle years about risk.  #mech/new _(added by map cross-check, time-bound view)_
  > between the two of us I was the more risk averse Trader
  indicator: n/a · asset: futures · horizon: n/a · conditions: Turtle programme, 1980s · testable: no · confidence: high
  ^MT020-C03-R1

### C04
- **Bill Eckhardt** Do not predict the market; decide what to do wherever it goes: risk control first, with profitability following from correct risk control.  #mech/risk_management
  > instead you have to focus on risk control because that's something you you can know your risk you can change your risk you can control your risk
  asset: multi · testable: no - principle · confidence: high
  ^MT020-C04-1
- **Bill Eckhardt** Utility theory: marginal utility of money diminishes, so losses weigh more than gains and risk aversion is a rigorous concept; ETC uses a small class of utility functions suited to commodity trading and client circumstances.  #mech/risk_management
  > every dollar every new dollar that you make is a little smaller than the last one and more importantly every dollar that you lose is the little bigger than the last
  indicator: expected utility / risk aversion · asset: multi · testable: partly - utility-based sizing can be tested · confidence: high
  ^MT020-C04-2
- **Bill Eckhardt** Most traders build a profitable system first and graft risk control on afterwards; ETC brings expected utility in at the ground floor of research and judges every idea by its effect on expected utility.  #mech/risk_management
  > they graft risk control almost as an afterthought on their system on their profitability system
  asset: multi · testable: partly - design philosophy · confidence: medium
  ^MT020-C04-3
- **Bill Eckhardt** Risk-neutral and risk-loving utility functions lead to ruin (the St Petersburg paradox shows absurd infinite expected value bets).  #mech/risk_management
  > the risk loving ones to be died these are utility functions for somebody who wants to keep betting the ranch and eventually I think they're financially suicidal
  asset: multi · testable: no - theoretical argument · confidence: high
  ^MT020-C04-4

### C05
- **Bill Eckhardt** In futures trading with leverage, risk aversion is primary since risk-loving traders repeatedly lose all their money.  #mech/risk_management
  > one has to be risk averse that's the only thing that can that can work in this business
  asset: multi · testable: no - principle · confidence: high
  ^MT020-C05-1
- **Bill Eckhardt** ETC runs short, medium and long-term systems with average trade lengths from 4-5 days to 50-60 days.  #mech/slow_reaction
  > we have shortterm we have medium we have long-term systems but you know we have trades that that have a a four or five day average length
  indicator: trade horizon mix · asset: multi · horizon: weeks · testable: no - description · confidence: medium
  ^MT020-C05-2
- **Moritz Seibert** Many Turtle students moved to longer holding periods because of alpha decay in short-term systems.  #mech/slow_reaction
  > they have moved over to longer term hold periods because of the Alpha DK that we could deserve observe in the shorter term systems
  indicator: short-term trend alpha decay · asset: multi · direction: longer holding periods · horizon: years · testable: partly - trend returns by horizon over time · confidence: medium
  ^MT020-C05-3
- **Bill Eckhardt** Turtle rules (breakout systems) were widely published so their edge was degraded by competition; Eckhardt moved to different trend-following systems even before they were released.  #mech/crowding_positioning
  > they've been heavily degraded since we let the turtles go and all all this information got revealed
  indicator: published breakout rules · asset: multi · horizon: years · testable: partly - performance of published rules · confidence: high
  ^MT020-C05-4
- **Bill Eckhardt** Trend following has been declared dead every few years; the majority of ETC's work is still trend following with a small non-trend part.  #mech/cycle_persistence
  > the death of trend following has been highly exaggerated
  indicator: trend following · asset: multi · direction: long trend following · horizon: years · testable: yes - long history of trend returns · confidence: high
  ^MT020-C05-5
- **Moritz Seibert** While short-term trend systems show alpha decay, longer-term trend systems (around 200-day look-backs) still work and remain robust, with drawdowns.  #mech/slow_reaction _(added by opus cross-check)_
  > the longer term systems you know two and a day time frames things like that to the present day they continue to work and they go up and down and they're robust
  indicator: trend look-back length (about 200 days) · asset: multi · direction: favour long look-back trend systems · horizon: months · testable: yes - compare short vs long look-back trend returns over time · confidence: medium
  ^MT020-C05-X1

### C06
- **Bill Eckhardt** Red Queen effect: with more competition and technical analysis knowledge, a commodity trader must improve as fast as possible just to hold his own.  #mech/crowding_positioning
  > one has to keep researching to stay ahead of it
  asset: multi · horizon: years · testable: no - qualitative · confidence: high
  ^MT020-C06-1
- **Rob Santino** Volatility enters ETC's systems in five or six ways (position sizing, measuring price change, risk control) alongside price, so the systems are based on both.  #mech/risk_management
  > volatility enters into our trading system in several different ways and about five or six different ways
  indicator: volatility · asset: multi · testable: no - proprietary · confidence: medium
  ^MT020-C06-2
- **Rob Santino** ETC does not target portfolio volatility because higher volatility often helps trend systems and they do not want to juice up when volatility is low; they track individual futures' volatility for risk.  #mech/risk_management
  > in a lot of situations um increased volatility often helps us we don't want to restrain it
  indicator: portfolio volatility targeting · asset: multi · direction: no vol targeting · testable: yes - compare vol-targeted vs unscaled · confidence: medium
  ^MT020-C06-3
- **Rob Santino** Position sizes are kept roughly constant from entry to exit: readjusting to rising volatility would cut the position along with the trend, which they found counterproductive.  #mech/risk_management
  > since um volatility often increases with a trend we have found that and if we were readjusting to volatility we would
  indicator: post-entry volatility readjustment · asset: multi · horizon: weeks · testable: yes - test dynamic vs constant size · confidence: medium
  ^MT020-C06-4

### C07
- **Moritz Seibert** Constant sizing with a stop-loss gives controlled risk and a synthetic long-optionality (volatility-seeking) profile.  #mech/risk_management
  > which means controlled risk and therefore a sythetic long optionality profile if you will
  indicator: stop-loss · asset: multi · direction: long volatility profile · horizon: weeks · testable: partly · confidence: medium
  ^MT020-C07-1
- **Bill Eckhardt** ETC's non-trend methods (about 20% of work) are not mean reversion because futures prices do not mean revert while volatility does.  #mech/cycle_persistence
  > it's volatility that mean reverts uh price doesn't doesn't mean revert at least Futures prices
  indicator: futures prices vs volatility · asset: multi · testable: yes - autocorrelation tests · confidence: medium
  ^MT020-C07-2
- **Bill Eckhardt** Summary statistics of signals (e.g. a moving average) throw away structure; keeping the 20-day high and low gives more information (position within the range).  #mech/research_method
  > instead of boiling all the structure down into one number you're keeping some of the structure
  indicator: moving average vs high/low channel · asset: multi · horizon: days · testable: yes - signal comparison · confidence: medium
  ^MT020-C07-3
- **Moritz Seibert** Resizing an open trend position to rising volatility amounts to a hidden mean-reversion trade against the trend, because volatility usually rises as the trend extends.  #mech/risk_management _(added by opus cross-check)_
  > essentially executing a hidden Mar reversion trade against the direction of the trend that is not always true by definition but uh it is true in my experience more often than not
  indicator: post-entry volatility resizing · asset: multi · direction: do not cut trend positions as volatility rises · horizon: weeks · conditions: when volatility rises with the trend (usual but not always) · testable: yes - backtest constant vs vol-resized position sizing · confidence: medium
  ^MT020-C07-X1

### C08
- **Bill Eckhardt** Keeping all price-history structure is combinatorially impossible, so research must eliminate structure but keep what is important.  #mech/research_method
  > what you have to do is you have to find out you have to eliminate a lot of the structure but you have to keep enough of it
  asset: multi · testable: no - research problem · confidence: medium
  ^MT020-C08-1
- **Bill Eckhardt** Volatility is a moving-average process, so moving averages suit volatility, but price is non-stationary and not an MA process, so moving averages and crossovers on price are counterproductive.  #mech/research_method
  > it's appropriate to estimate volatility using moving averages
  indicator: moving average on price vs volatility · asset: multi · testable: yes - MA crossover vs breakout · confidence: medium
  ^MT020-C08-2
- **Bill Eckhardt** Fitting should capture permanent features and ignore transitory ones; some overfitting is inevitable, so ETC uses in-house techniques to estimate and minimize overfit.  #mech/research_method
  > to try to fit to the permanent features of the time series whereas you want to ignore the transitory features
  indicator: overfitting estimate · asset: multi · testable: yes - overfit estimators · confidence: high
  ^MT020-C08-3
- **Bill Eckhardt** Curve fitting (a nonlinear regression term) is the wrong word for what traders do; 'overfitting' is preferred, which implies that underfitting is also possible.  #mech/new _(added by map cross-check)_
  > curve fitting is simply the wrong term
  indicator: n/a · asset: n/a · horizon: n/a · conditions: System development · testable: no · confidence: high
  ^MT020-C08-R3

### C09
- **Bill Eckhardt** Underfitting is also bad because it ignores worthwhile market information; some good traders lost all their money from overfitting.  #mech/research_method
  > if you're afraid of overfitting one way is to underfit
  asset: multi · testable: partly · confidence: high
  ^MT020-C09-1
- **Bill Eckhardt** The E-score combines many performance measures (a 'Super Value') and discounts systems that earned most profit in a short span (e.g. 2 of 20 years), guarding against false impressions of quality.  #mech/research_method
  > a system might make too much of its money over too short a period of time well we have elements of the escore which which will test for that
  indicator: E-score · asset: multi · horizon: years · testable: yes - concentration of profits test · confidence: medium
  ^MT020-C09-2
- **Rob Santino** The Gauntlet is a barrage of tests designed to tear a system apart, showing where it fails, which is as important as knowing why it works, and removes emotion.  #mech/research_method
  > bill has spent as much time uh tearing systems apart as we do putting them together
  indicator: The Gauntlet · asset: multi · testable: partly - proprietary · confidence: medium
  ^MT020-C09-3
- **Rob Santino** Systems can have a strong 2-4 month run then go flat, so scientific testing and emotion removal are needed.  #mech/research_method
  > you could have systems that they might have a two three four month really strong run and then they just go flat or degrade
  asset: multi · horizon: months · testable: no - observation · confidence: low
  ^MT020-C09-4

### C10
- **Bill Eckhardt** The Gauntlet also tests the program code and finds subtle glitches that would otherwise be nearly impossible to find.  #mech/research_method
  > it actually tests the program too it can find very subtle glitches in the program
  indicator: The Gauntlet · asset: multi · testable: no - proprietary · confidence: medium
  ^MT020-C10-1
- **Moritz Seibert** More markets give more independent bets and less noise in any run, though smaller portfolios can outperform for periods because of concentration.  #mech/risk_management
  > the more markets we trade the more independent bets we can place um the better we can crystallize our Edge over time
  indicator: number of markets traded · asset: multi · direction: maximize diversification · horizon: years · testable: yes - performance vs number of markets · confidence: medium
  ^MT020-C10-2
- **Bill Eckhardt** ETC trades about 70 markets, believes in diversification as the greatest financial idea of the 20th century, but avoids markets with too much slippage or too little liquidity.  #mech/risk_management
  > we measure the liquidity and the trade slippage for all markets that we trade whether we're considering trading
  indicator: liquidity, slippage · asset: multi · direction: avoid illiquid markets · testable: yes - cost-adjusted market selection · confidence: high
  ^MT020-C10-3
- **Bill Eckhardt** Many traders undercut diversification by concentrating on whichever few markets are currently hot, which is anti-diversification despite its proven value.  #mech/behavioral _(added by opus cross-check)_
  > I still think a lot of Traders just like to jump on the latest bandwagon you know the latest few things that are hot and avoid everything else you know they're they're anti- diversifying
  indicator: market concentration of trader portfolios · asset: multi · testable: partly - compare concentrated hot-market portfolios vs broad ones · confidence: medium
  ^MT020-C10-X1
- **Bill Eckhardt** Eckhardt would like to publish parts of the Gauntlet but keeps the methods secret, and has not published anything specific about futures trading.  #mech/new _(added by map cross-check)_
  > this is an industry where we have to keep secrets
  indicator: n/a · asset: n/a · horizon: n/a · conditions: Competitive industry · testable: no · confidence: high
  ^MT020-C10-R2

### C11
- **Bill Eckhardt** Alternative markets look better in backtests but slippage and exit difficulty in a hurry make them worse in practice.  #mech/risk_management
  > on paper these Alternatives markets might appear better but in practice I I think they're actually worse
  indicator: alternative market slippage · asset: multi · testable: yes - backtest with realistic costs · confidence: medium
  ^MT020-C11-1
- **Bill Eckhardt** Single stocks have a weaker trend component than futures (splits, dividends, long-dominated), so ETC specialises in futures where it has relative advantage.  #mech/structural_shift
  > stocks don't really have the kind of robust Trend component that Futures tend to have in other words our systems don't apply very well to stocks
  indicator: trend strength in stocks vs futures · asset: equities · testable: yes - compare trend returns by asset · confidence: medium
  ^MT020-C11-2
- **Bill Eckhardt** Futures are balanced (one long per short) while stock markets are dominated by longs, so they are different processes.  #mech/structural_shift
  > whereas in the Futures Market there is exactly one long for every short and vice versa it's completely balanced
  asset: multi · testable: no - structural fact · confidence: high
  ^MT020-C11-3
- **Bill Eckhardt** Replicating CTA indices by regression 'sounds like an invitation to really overfit'; futures price changes and trade results are radically non-normal.  #mech/research_method
  > here's a fundamental fact and that is that the distribution the probability distribution of price change and also of trades in a Futures Trading System are not normally distributed
  indicator: CTA replication by regression · asset: multi · testable: yes - replication out-of-sample tests · confidence: medium
  ^MT020-C11-4

### C12
- **Bill Eckhardt** Use robust, distribution-free statistics because futures returns are heavy tailed (Mandelbrot: possibly no variance); small-sample normal statistics give wrong answers, standard deviation and least-squares correlation are unreliable.  #mech/research_method
  > you need to avoid normal techniques and you need to use what statisticians call robust or distribution free statistics
  indicator: robust statistics · asset: multi · testable: yes - compare robust vs normal estimates · confidence: high
  ^MT020-C12-1
- **Bill Eckhardt** Robust statistics need 10-30 times more data, so ETC needs 10-20 years of data and cannot conclude anything from two or three years (that is overfitting).  #mech/research_method
  > the drawback of such robust statistics is that they're kind of data Hogs you need 10 20 time 30 times as much data to make a reliable inference
  indicator: sample length · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT020-C12-2
- **Bill Eckhardt** LTCM failed because it relied on normal distribution theory despite fat tails.  #mech/risk_management
  > busted out spectacularly and it really was because they were using normal distribution Theory
  indicator: LTCM · asset: multi · horizon: years · testable: yes - historical case · confidence: medium
  ^MT020-C12-3
- **Rob Santino** Regression-based CTA-index replication products are likely to end badly.  #mech/research_method _(added by opus cross-check, time-bound view)_
  > I think on the replication question that's probably not going to have a good ending
  indicator: CTA replication ETFs · asset: multi · direction: negative outlook for replication strategies · horizon: years · testable: yes - replication ETF performance vs CTA indices over time · confidence: medium
  ^MT020-C12-X1
- **Moritz Seibert** Evidence cited from Mandelbrot's cotton-price work: futures returns are fat-tailed on both sides and jump-prone, possibly a stable Paretian distribution without a defined variance.  #mech/research_method _(added by opus cross-check)_
  > it is definitely tailed in both directions it is prone to jumps
  indicator: cotton price return distribution · asset: commodities · testable: yes - tail-index estimation on futures returns · confidence: medium
  ^MT020-C12-X2
- **Moritz Seibert** Computing volatility as a standard deviation for sizing reintroduces normal-distribution assumptions and their drawbacks; range-based measures like ATR are not standard deviations.  #mech/risk_management _(added by opus cross-check)_
  > many people would calculate volatility as a function of standard deviation under the assumption of normal distribution there you go again you're back
  indicator: standard deviation vs ATR volatility · asset: multi · direction: prefer robust volatility measures · conditions: heavy-tailed returns · testable: yes - compare sizing with SD vs ATR/robust estimators · confidence: medium
  ^MT020-C12-X3

### C13
- **Rob Santino** Replication portfolios lack predefined exits, exposing them to discontinuity and gap events; stops and exit rules keeping losses small are essential.  #mech/risk_management
  > keeping these losses small is what keeps you in business
  indicator: stop-loss exit rules · asset: multi · testable: partly · confidence: medium
  **Correction (cross-check):** Wrong speaker: the point that replication portfolios lack predefined exits and that keeping losses small keeps you in business is made by host Moritz Seibert (he opens 'and Rob maybe to your point'); Eckhardt then agrees. → Moritz Seibert: regression-based replication portfolios lack predefined exits, exposing them to discontinuity and gap events; stops and exit rules that keep losses small are essential.
  ^MT020-C13-1
- **Bill Eckhardt** All futures markets have heavy left tails (leptokurtosis), so trading rules must intervene to control the left tail via risk management.  #mech/risk_management
  > the left hand tail the one that represents losses is very heavy
  indicator: kurtosis, left tail · asset: multi · testable: yes - tail statistics · confidence: high
  ^MT020-C13-2
- **Bill Eckhardt** High win-rate strategies (selling cheap options) periodically bust out because they exploit the bulk of the distribution; ETC rejects any new system with 70-80% success and prefers a ~40% success rate with larger winners.  #mech/risk_premium
  > they make money 70 80 90% of the time but then they're subject to large freakish losses
  indicator: trade success rate · asset: multi · direction: avoid high-win-rate short-tail strategies · testable: yes - win rate vs tail loss · confidence: high
  ^MT020-C13-3
- **Bill Eckhardt** Predictive accuracy is about 51-52%, so put ten times as much emphasis on risk control as on prediction.  #mech/risk_management
  > you almost never know better than about 51 or 52% which way the Market's going
  indicator: hit rate · asset: multi · testable: yes - hit rate measurement · confidence: high
  ^MT020-C13-4

### C14
- **Bill Eckhardt** Normal human attitudes (hold losers) are dead wrong; traders must cut losses and let profits run.  #mech/behavioral
  > you have to get out of your losses you have to let your profits run
  asset: multi · direction: cut losses, run profits · testable: yes - disposition effect · confidence: high
  ^MT020-C14-1
- **Moritz Seibert** The trend follower's edge is a pain arbitrage: enduring bad periods while keeping individual losses small.  #mech/behavioral
  > this pain Arbitrage of sticking to your system during bad times when the going gets tough and nobody enjoys it
  asset: multi · horizon: years · testable: no - behavioral · confidence: medium
  ^MT020-C14-2

### C15
- **Bill Eckhardt** Some Turtle trainees dropped out or could not get along, which showed they lacked the right emotional makeup.  #mech/behavioral
  > there were some who dropped out you know fairly soon and that that indicated that they didn't have the right emotional makeup
  asset: multi · testable: no - anecdote · confidence: low
  ^MT020-C15-1

