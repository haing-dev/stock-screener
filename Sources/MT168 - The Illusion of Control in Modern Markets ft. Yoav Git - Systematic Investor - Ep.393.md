---
source_id: MT168
title: "The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393"
date: 2026-03-29
channel: "Top Traders Unplugged"
url: 
words: 11507
claims: 41
added_by_crosscheck: 9
corrections: 1
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Niels Kaastrup-Larsen (host, hedge fund manager)", "Yoav Git (co-host, systematic fixed-income researcher; speaker label in captions is Yuval/Yoav)"]
tags: [source, layer0]
---
# The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393

**Speakers:** Niels Kaastrup-Larsen (host, hedge fund manager); Yoav Git (co-host, systematic fixed-income researcher; speaker label in captions is Yuval/Yoav)

**Summary:** March 2026 Iran war shock: stocks and bonds sold off together, oil front-end spiked while the back barely moved, CTAs lost little. Git argues CTAs should hedge a common first factor (duration) rather than scale every position when spreads widen, reviews a flow-based excess-volatility paper (value, noise and trend traders), and frames CTA market-universe breadth by correlation and capacity.

**Approach:** trend following, fixed income, stock-bond correlation, risk management in crises, flows, excess volatility, market universe, capacity

**Cross-check completeness estimate of first read:** 0.85 - the first reader captured the crisis, flows, paper and capacity arguments well; missed the EM-algorithm method, the excess-volatility motivation, the initial-positioning dispersion point, the pre-announcement trading remark, the caveat that factor hedging is not worth it for liquid CTAs, and Niels's tracking-error point.

## Argument map

**Episode thesis:** Git argues the March 2026 Iran-war shock was a risk-off event (stocks and bonds sold off together, oil spiked at the front of the curve only) and that CTAs should hedge a common first factor (duration) instead of scaling every position when spreads widen. A flow-based excess-volatility paper (value, noise and trend traders) is reviewed and critiqued, and CTA market-universe breadth is framed by correlation and capacity.

### Yoav Git (Systematic fixed-income researcher/trader and co-host of the Systematic Investor series; works with Tom Babbage on commodities)
Fingerprint: #approach/macro_fundamental_topdown #approach/portfolio_construction_stacking #approach/costs_execution #approach/position_sizing_vol_target #approach/trend_following #approach/liquidity_flows #approach/market_internals_leading
_Speaker note: Caption labels the name Yuval/Yoav; ledger uses Yoav Git. Fixed income is his area; commodity view is relayed from colleague Tom Babbage._

**Worldview premises**
- Inflation regimes make the stock-bond correlation positive, so bonds fail as an equity hedge. _[empirical, stated; support: March 2026 selloffs in both; earlier talks]_ ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C04-2|C04-2]])
- Western fiscal stress makes inflation a way to erode debt, so higher yields are near-inevitable but untimeable. _[theoretical, stated; support: Weak 2-year auction; personal view]_ ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C05-2|C05-2]])
- Back-of-curve oil reflects fundamental supply and demand and is insulated from news-cycle shocks ('weather vs climate'). _[theoretical, stated; support: Colleague's framing; Brent 3y barely moved]_ ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C07-1|C07-1]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C03-2|C03-2]])
- Most volatility is noise; the EMH holds either because price is right (Shiller) or because there is no true price. _[theoretical, stated; support: Review of the excess-volatility paper]_ ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C12-1|C12-1]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C12-X5|C12-X5]])
- Markets are populated by three flows: value traders revert to target, noise traders inject volatility, trend followers trade returns. _[theoretical, stated; support: Flow model in the paper]_ ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C12-2|C12-2]])
- Genuine jumps in fundamental value (payrolls, weekend war) move prices without trading. _[empirical, stated; support: Examples: payroll liquidity shrinks then gaps, weekend Iran attack]_ ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C14-1|C14-1]])
- Value traders also face risk limits, so an unbounded (cubic) response is unrealistic. _[theoretical, stated; support: Risk-management reasoning]_ ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C15-1|C15-1]])
- Capacity limits risk per market so footprint remains unwindable; more AUM pushes risk into the biggest markets. _[institutional, stated; support: Industry practice]_ ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C15-2|C15-2]])
- CTA return is diversification times average market Sharpe; the value of many markets depends on their correlation. _[theoretical, stated; support: Blog post with Tom Babbage]_ ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C16-1|C16-1]])

**Chain: Oil shock to fixed income**
1. front-end supply constraint → oil spike at front of curve; back barely moves: long run over-producing (105 vs 102 mb/d) ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C03-2|C03-2]])
2. oil is ~6% direct inflation weight plus food and manufacturing → oil curve informs inflation curve: secondary effects ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C07-2|C07-2]])
3. bond sell-offs at long ends in US, UK, EM → risk-off event not only inflation expectations: TY 114 to 110 is more than a year's move in weeks; gold sold off too ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C03-3|C03-3]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C03-R1|C03-R1]])
- Evidence: Curve shape data and single episode
- Fails when: Narrative changes with each tweet

**Chain: CTA crisis de-risking: scale everything vs hedge the first factor**
1. shock lifts volatility and spreads (EM about 10bp) → CTAs scale every position down per market: rules-based volatility scaling ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C08-1|C08-1]])
2. correlations spike so assets become substitutes → selling Treasury futures hedges the common first factor as well as shrinking the whole book: first factor dominates volatility ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C08-2|C08-2]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C09-3|C09-3]])
3. closing a long-short alternative book → cost of about 5% illustrative: wide spreads, thin liquidity ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C09-2|C09-2]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C09-1|C09-1]])
4. constrained optimisation of factor vs specific risk → probably not worth it for a liquid-market CTA: can simply scale down ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C10-X4|C10-X4]])
- Evidence: Own March 2026 trading experience; contrasts with discretionary risk practice (Brevan)
- Fails when: Liquidity crisis where illiquid positions cannot be exited (host's objection)

**Chain: Crisis flow sequence**
1. weekend news gaps price → CTA flows when markets open as volatility gaps: models cut risk ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C10-2|C10-2]])
2. falling bonds → value traders closed out (long squeeze): cannot hold losing positions ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C11-1|C11-1]])
3. stabilisation → real money buys: value buyers ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C11-1|C11-1]])
4. escalation (South Pars) → renewed selling; gilt and Treasury squeezes: repeat of the sequence ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C11-1|C11-1]])
- Evidence: Observed March 2026 episode
- Fails when: Single episode, no flow data shown

**Chain: Pendulum of trend and value**
1. through the centre of value → trend followers dominate: impulse swings fast ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C13-2|C13-2]])
2. far from value → value traders dominate and push back: trend runs out of steam ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C13-2|C13-2]])
3. two balance points → markets spend time over- or under-priced: paper's result ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C13-2|C13-2]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C13-1|C13-1]])
- Evidence: Paper calibrated with EM algorithm on monthly data
- Fails when: Genuine value jumps, risk limits on value traders

**Chain: Capacity and market-universe breadth**
1. high correlation among chosen markets → few big markets lose little diversification: plateau reached quickly ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C16-1|C16-1]])
2. low-correlation hand-picked markets → capacity pushes risk to big markets: effective breadth shrinks ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C16-1|C16-1]])
3. index replication → high correlation is the aim: replicating a CTA at 80% correlation is accepted ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C16-2|C16-2]])
- Evidence: Blog post with Tom Babbage
- Fails when: Replicators' tracking error (host)

**Decision process**
- [risk] Scale each market down in stress by volatility (standard CTA); alternative: hedge the common first factor while limiting specific risk per market.. Why: Reduce cost in crises ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C08-1|C08-1]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C08-2|C08-2]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C09-3|C09-3]])
- [execution] Time of day of execution matters in a $20-25 oil daily range, making tracking of one's own model hard.. Why: Intraday volatility staggering ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C04-1|C04-1]])
- [research] Scenario analysis back to 1998 for surprise volatility: March 2026 ranked at the top.. Why: Stress test of model risk ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C04-1|C04-1]])
- [research] Estimate noise, value and trend populations with the EM algorithm (unlabelled mixtures).. Why: Calibration tool in the paper ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C02-X1|C02-X1]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C13-1|C13-1]])
- [universe] Choose market universe by correlation and capacity: correlated big markets for index-like CTA; low-correlation markets need capacity thinking.. Why: Return = diversification x average Sharpe ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C16-1|C16-1]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C15-2|C15-2]])
- [portfolio] Limit risk per market so the footprint can be unwound in a crisis.. Why: Avoid trading against oneself ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C15-2|C15-2]])

**Evidence style:** First-hand trading experience of March 2026, literature review of a flow-model paper, and simple economic reasoning; scenario analysis on history.

**Views at the time**
- (2026-03-25) March 2026 was a risk-off event, not just inflation: bonds sold off as much as equities and gold fell.. Reasoning: Long-end sell-off, EM back of curve ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C03-3|C03-3]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C04-2|C04-2]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C03-R1|C03-R1]])
- (2026-03-25) Higher yields are near-inevitable (fiscal stress, 2-year auction weakness) but timing unknowable.. Reasoning: Debt erosion via inflation ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C05-2|C05-2]])
- (2026-03-25) Fixed-income trend trading has been difficult since 2023: moves reverse violently within the month.. Reasoning: 2022 clean short vs choppy since ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C05-3|C05-3]])
- (2026-03-25) Oil: front-end spike due to supply constraints; the long end structurally oversupplied.. Reasoning: 105 vs 102 mb/d ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C03-2|C03-2]])
- (2026-03-25) The flow-model paper's calibration (noise first order, value second, trend negligible) matches the view that CTA footprints are small.. Reasoning: No autocorrelation created ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C13-1|C13-1]])
- (2026-03-25) Critique of the paper: ignores genuine jumps, cubic value response, monthly data, no predictive use.. Reasoning: Examples: payroll, weekend ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C14-1|C14-1]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C15-1|C15-1]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C14-R1|C14-R1]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C15-R1|C15-R1]])

### Niels Kaastrup-Larsen (Host and CTA industry commentator (former hedge fund manager))
Fingerprint: #approach/trend_following #approach/manager_selection_allocation #approach/regime_detection #approach/positioning_crowding #approach/replication_indexing #approach/behavioral_sentiment
_Speaker note: Host states his own opinions in the news round, trend-barometer data, and in objections to the guest._

**Worldview premises**
- Narratives are unpredictable (Danish election, gold in the Iran war), which supports a rules-based approach. _[experience, stated; support: Anecdote]_ ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C02-1|C02-1]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C03-1|C03-1]])
- Short-window dispersion between CTAs is largely initial-positioning luck, not model quality. _[experience, stated; support: Observation]_ ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C03-X2|C03-X2]])
- CTAs only lose less than bonds in surprises; they cannot claim protection. _[experience, stated; support: March 2026 numbers]_ ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C05-1|C05-1]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C06-3|C06-3]])
- Core-market CTAs can cut duration cheaply in stress; alternative-market CTAs face higher costs, hidden in monthly performance. _[institutional, stated; support: Market-universe paper discussion]_ ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C09-1|C09-1]])
- Keeping illiquid positions hedged with futures is dangerous in a liquidity crisis (correlations go to one, exits close). _[theoretical, stated; support: Reasoning]_ ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C10-1|C10-1]])
- In practice replicators have modest correlation to the CTA index and substantial tracking error. _[empirical, stated; support: Numbers cited from prior studies (not shown)]_ ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C16-X6|C16-X6]])

**Chain: Fragility signals in March 2026**
1. private credit funds gate on redemptions → fragility adds to market stress: redemptions exceed liquidity ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C06-1|C06-1]])
2. energy shock → may be rationing rather than price: Europe and Egypt vulnerable ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C06-2|C06-2]])
- Evidence: News and anecdotes
- Fails when: Not tested

**Decision process**
- [research] Track the trend barometer (52 over 44 markets) and CTA indices for breadth and relative results.. Why: Breadth gauge ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C06-3|C06-3]])
- [other] Event-driven reversals around announcements are hard for rules to anticipate; apparent front-running is noted but deferred.. Why: Manipulation topic deferred ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C04-X3|C04-X3]])

**Evidence style:** Narrative and index data; objections framed from the CTA industry.

**Views at the time**
- (2026-03-25) Industry lost little in March 2026; BTOP50 -2.25%, SG CTA -2%, SG Trend -2.6%; MSCI World -6%, bonds -2%, S&P -4.6% in March.. Reasoning: Index data as of Monday evening ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C06-3|C06-3]])
- (2026-03-25) Gold sold off both at war start and at de-escalation, which supports a rules-based approach.. Reasoning: Observation ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C03-1|C03-1]])
- (2026-03-25) Not a pure 2022 repeat claim; CTAs cannot claim protection.. Reasoning: Institutional question ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C05-1|C05-1]])
- (2026-03-25) Energy shocks can be about availability, not just price.. Reasoning: European rationing ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C06-2|C06-2]])

### Disagreements
- **Cost of crisis de-risking and the right universe**: Yoav Git: Scaling every position is expensive in alternative markets (closing a long-short book could cost on the order of 5%); a factor hedge via Treasury futures is better. ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C08-1|C08-1]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C09-2|C09-2]]); Niels Kaastrup-Larsen: For core-market CTAs this is cheap; the problem is specific to alternative markets and is hidden in monthly returns. ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C09-1|C09-1]])
- **Hedging with liquid futures while holding illiquid positions**: Yoav Git: Hedge first-factor risk with liquid duration while managing specific risk. ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C09-3|C09-3]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C08-2|C08-2]]); Niels Kaastrup-Larsen: In a liquidity crisis correlations go to one and illiquid exits close, so this risk is large. ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C10-1|C10-1]])
- **How CTA replication performs**: Yoav Git: Replicating a CTA index at 80% correlation is accepted while S&P demands 99%. ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C16-2|C16-2]]); Niels Kaastrup-Larsen: In practice replicators' correlation is modest and tracking error substantial. ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C16-X6|C16-X6]])

### Gaps and conflicts
- The 5% cost of closing a long-short alternative book is illustrative ('let's say'), not measured. ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C09-2|C09-2]])
- Git 'does not have the model' for the factor-hedge idea; no test shown. ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C08-1|C08-1]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C10-X4|C10-X4]])
- Flow sequence in March (CTA, value close-out, real money, squeeze) is narrated without flow data. ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C10-2|C10-2]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C11-1|C11-1]])
- Paper's calibration result (trend negligible) sits oddly with Git's remark that CTAs feature prominently in such models; the reader must reconcile prominence in the model structure with negligible estimated contribution. ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C11-2|C11-2]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C13-1|C13-1]])
- Back-of-curve oil is insulated 'weather vs climate' is attributed to a colleague and not evidenced. ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C07-1|C07-1]])
- Unverified: private credit gating, apparent pre-announcement trading in oil. ([[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C06-1|C06-1]], [[MT168 - The Illusion of Control in Modern Markets ft. Yoav Git - Systematic Investor - Ep.393#^MT168-C04-X3|C04-X3]])

### Forward-looking inputs (reader synthesis)
Observable inputs: spreads and liquidity costs in EM rates, front vs back of oil curve, stock-bond correlation, auction demand, CTA flows after volatility gaps, value-trader stop-outs. Horizon: weeks for flows, years for fiscal-driven yield rise.

### Reader inferences (not stated by the speakers)
- The flow model attributes first-order volatility to noise and negligible footprint to trend followers, which means trend following cannot be justified as a major source of price formation by this paper; the paper uses monthly data so cannot settle daily dynamics.
- Git's proposal is a risk-management rule change (factor-based de-risking) rather than a forecast.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro; EM algorithm explained |
| C02 | 1 | EM algorithm cont.; Danish election narrative lesson |
| C03 | 3 | gold behaviour in Iran war; inflation vs risk-off in oil curve and bonds |
| C04 | 2 | intraday execution timing risk, record surprise volatility, stock-bond correlation positive |
| C05 | 3 | CTAs vs 2022 analogy; weak 2-year auction; fiscal pressure and yields |
| C06 | 3 | private credit gating; supply vs price; index numbers March 2026 |
| C07 | 2 | index numbers; oil curve front vs back; weather vs climate; inflation expectations |
| C08 | 2 | flows and risk management in a rates shock; discretionary vs CTA hedging |
| C09 | 3 | core vs alternative market liquidity; closing book costs 5% |
| C10 | 2 | factor-based risk management as optimisation; liquidity crisis risk; flows begin |
| C11 | 2 | flow sequence in crisis: CTAs, value traders closed out; paper intro |
| C12 | 2 | efficient market hypothesis variants; three-player flow model |
| C13 | 2 | model calibration with EM; CTA contribution to volatility tiny; pendulum picture |
| C14 | 1 | pendulum dynamics; critique: news jumps are value changes, nonfarm payroll liquidity |
| C15 | 2 | critique: cubic response unrealistic; capacity and breadth blog starts |
| C16 | 2 | diversification times average market Sharpe; correlation and capacity; replication tracking |
| C17 | 0 | next guest, outro |

## Claims

### C02
- **Niels Kaastrup-Larsen** Danish election campaign narratives (Greenland, geopolitics expected) ended up dominated by animal welfare and clean water, showing narratives are unpredictable even for narrative-driven markets.  #mech/behavioral _(time-bound view)_
  > It ended up being animal welfare and clean drinking water.
  asset: other · testable: no - anecdote · confidence: low
  ^MT168-C02-1
- **Yoav Git** The EM (expectation-maximisation) algorithm estimates the parameters of mixed, unlabelled populations by alternating a probabilistic classification of each observation (E step) with re-estimating each distribution (M step) until it converges; it is the calibration tool later used to size the noise, value and trend-trader populations in the flow model.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > it's an iterative process, a little bit like the back propagation process that we have in machine learning these days
  indicator: EM algorithm for mixture-model calibration · asset: other · conditions: needs enough observations; iterative convergence · testable: yes - standard statistical method · confidence: high
  ^MT168-C02-X1

### C03
- **Niels Kaastrup-Larsen** Gold sold off both at war start and on de-escalation news in March 2026, an unpredictable response that supports a rules-based approach.  #mech/behavioral _(time-bound view)_
  > it seems like it's selling off when the war began, but it's almost like it's also selling off now that there might be a de-escalation of the war.
  indicator: gold · asset: commodities · horizon: weeks · testable: partly · confidence: medium
  ^MT168-C03-1
- **Yoav Git** The oil spike was concentrated at the front of the curve (supply constraints) while Brent three years out barely moved, because the long-run market is over-producing (about 105 mb/d produced vs 102 consumed).  #mech/structural_shift _(time-bound view)_
  > the spike in oil is at the front of the curve, right?
  indicator: Brent curve slope · asset: commodities · horizon: weeks · conditions: front-end shock vs structural oversupply · testable: yes - curve data · confidence: high
  ^MT168-C03-2
- **Yoav Git** Bond sell-offs at long ends of US/UK/EM curves (TY from 114 to 110, more than a year's move in weeks) point to a risk-off event rather than a pure inflation-expectations story.  #mech/liquidity_flows _(time-bound view)_
  > We've seen actually a sell-off at the back of the curve, um, which is sort of indicative that what this is happening is a bit of a much more of a risk-off event
  indicator: 10-year yield, TY futures, EM curves · asset: rates · horizon: weeks · testable: yes · confidence: medium
  ^MT168-C03-3
- **Niels Kaastrup-Larsen** Over the weeks around a shock, dispersion across CTAs is largely driven by initial positioning luck rather than model quality, so short-window results should not be over-read as skill.  #mech/research_method _(added by sonnet-xhigh cross-check, time-bound view)_
  > we know that positioning, initial positioning is so important, and um and you can be lucky, you can be unlucky with how you enter a situation like that
  indicator: dispersion of CTA returns around shocks · asset: multi · horizon: weeks · conditions: short windows around geopolitical shocks (March 2026) · testable: yes - cross-sectional dispersion of manager returns vs prior positioning · confidence: medium
  ^MT168-C03-X2
- **Yoav Git** Git: gold and long-term bonds behaved in ways inconsistent with a pure inflation-expectations story in March 2026, which indicates a risk-off event in addition to inflation narrative.  #mech/new _(added by map cross-check, time-bound view)_
  > behaving in a way that you wouldn't expect gold to behave in an inflation based
  indicator: gold behaviour in oil shock · asset: commodities · horizon: weeks · conditions: March 2026 Iran war · testable: partly - single episode · confidence: medium
  ^MT168-C03-R1

### C04
- **Yoav Git** With oil trading a $20-25 daily range (Brent near 120 then 90), execution time of day materially changes P&L and makes tracking one's own model difficult; scenario analysis back to 1998 ranks March 2026 surprise volatility at the top.  #mech/risk_management _(time-bound view)_
  > oil is traded in a range of say 20-25 dollars a day.
  indicator: intraday oil range · asset: commodities · horizon: days · conditions: extreme intraday volatility · testable: yes · confidence: high
  ^MT168-C04-1
- **Yoav Git** Inflation regimes produce positive stock-bond correlation, so bonds fail as an equity hedge; in March 2026 bonds sold off as much as equities.  #mech/cycle_persistence _(time-bound view)_
  > we're going to see correlation between bonds and equity being positive rather than negative
  indicator: stock-bond correlation · asset: multi · horizon: months · conditions: inflation-driven shocks · testable: yes · confidence: high
  ^MT168-C04-2
- **Niels Kaastrup-Larsen** Niels notes apparent trading in oil and equities just ahead of policy announcements (S&P selling off, then rallying before a Trump statement), suggesting event-driven reversals can be front-run and are hard for a rules-based process to anticipate; both speakers defer the market-manipulation topic.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > You should of course do like all the people in oil that apparently traded 10 minutes before the announcement.
  indicator: price moves just before announcements · asset: multi · horizon: days · conditions: geopolitical and policy headline events, March 2026 · testable: partly - event study of pre-announcement returns · confidence: low
  ^MT168-C04-X3

### C05
- **Niels Kaastrup-Larsen** Institutional investors ask whether March 2026 is a 2022 repeat; CTAs only lose less than bonds in surprises and cannot claim protection.  #mech/cycle_persistence _(time-bound view)_
  > could this be the beginning of another 2022 scenario?
  asset: multi · horizon: months · testable: no - speculative · confidence: low
  ^MT168-C05-1
- **Yoav Git** Weak 2-year US auction and Western fiscal stress suggest inflation is a way to erode debt, making higher yields near-inevitable though timing is unknowable.  #mech/fiscal_debt _(time-bound view)_
  > the weakness in the two-year bond auction recently um, in the US government
  indicator: 2-year Treasury auction · asset: rates · direction: yields higher · horizon: years · conditions: timing unknown · testable: partly · confidence: medium
  ^MT168-C05-2
- **Yoav Git** US rates have been choppy since 2023 (2022 was a clean short), making fixed-income trend trading difficult as moves reverse violently within the month.  #mech/slow_reaction _(time-bound view)_
  > the inability to decide for the markets to decide which way it's going um, since 2023.
  indicator: US rates trend · asset: rates · horizon: years · testable: yes · confidence: medium
  ^MT168-C05-3

### C06
- **Niels Kaastrup-Larsen** Private credit funds are gating on redemptions, adding fragility.  #mech/liquidity_flows _(time-bound view)_
  > private credit um is under attack. You've seen cracks. You've seen some funds beginning to gate
  indicator: private credit fund redemptions · asset: credit · horizon: months · testable: partly · confidence: medium
  ^MT168-C06-1
- **Niels Kaastrup-Larsen** Energy shocks can be supply availability (rationing) rather than price, affecting activity; Europe and Egypt show vulnerability.  #mech/structural_shift _(time-bound view)_
  > it's not necessarily just price. It's actually supply.
  indicator: oil and gas supply · asset: commodities · horizon: months · testable: no · confidence: low
  ^MT168-C06-2
- **Niels Kaastrup-Larsen** Trend barometer 52 (44 markets); BTOP50 -2.25%, SG CTA -2%, SG Trend -2.6%, short-term index about flat; MSCI World -6% in March, bonds -2%, S&P 500 -4.6% in March.  #mech/new _(time-bound view)_
  > my trend barometer is actually still in a relatively strong level at 52.
  indicator: trend barometer, CTA indices · asset: multi · horizon: weeks · testable: yes - index data · confidence: high
  ^MT168-C06-3

### C07
- **Yoav Git** Back-of-curve oil trading reflects fundamental supply and demand and is insulated from news-cycle shocks (weather vs climate).  #mech/structural_shift
  > the way he likes to talk about it is weather versus climate.
  indicator: back-end oil curve · asset: commodities · horizon: months · testable: partly · confidence: medium
  ^MT168-C07-1
- **Yoav Git** Energy has about 6% direct weight in inflation, with secondary effects via food and manufacturing, so the oil curve informs the inflation curve.  #mech/structural_shift
  > oil features uh energy features about 6% into the inflation uh directly as a component into into inflation.
  indicator: energy weight in CPI · asset: commodities · horizon: months · testable: yes · confidence: medium
  ^MT168-C07-2

### C08
- **Yoav Git** In a crisis CTAs scale all positions (longs and shorts) down per market, which is costly when EM spreads widen to about 10 bp; discretionary managers instead close the liquid duration exposure.  #mech/risk_management
  > normal CTAs, the the way we would normally manage risk is say, well, the volatility has spiked, and we would sell everything.
  indicator: position scaling rule · asset: rates · horizon: days · testable: yes - cost analysis · confidence: medium
  ^MT168-C08-1
- **Yoav Git** When correlations spike assets become substitutes, so selling Treasury futures hedges the common first factor as effectively as shrinking the whole book.  #mech/risk_management
  > hedging with the TY with the US Treasuries very quickly is actually as effective as you would do then just shrinking your entire portfolios
  indicator: common duration factor, TY futures · asset: rates · direction: short TY futures to hedge directional rates risk · horizon: days · conditions: needs correlation spike · testable: yes · confidence: medium
  ^MT168-C08-2

### C09
- **Niels Kaastrup-Larsen** Core-market (highly liquid futures) CTAs can cut duration cheaply in stress; alternative-market CTAs face higher costs, a difference hidden in monthly performance.  #mech/liquidity_flows
  > the difference between which market universe you put
  indicator: market universe liquidity · asset: multi · horizon: weeks · conditions: stress periods · testable: yes · confidence: medium
  ^MT168-C09-1
- **Yoav Git** Closing a long-short book in the stress cost about 5% of performance in alternative markets, so crisis de-risking is expensive.  #mech/risk_management _(time-bound view)_
  > let's say closing closing the book the long short book is like 5% of performance.
  indicator: closing cost · asset: rates · horizon: days · testable: yes · confidence: medium
  **Correction (cross-check):** Presented as an observed fact. Yoav gave the 5% as an illustrative figure ('let's say') for the cost of closing a long-short alternative-markets book and said he does not have a solution. → Illustratively, closing out a long-short book in alternative markets in stress could cost on the order of 5% of performance, so crisis de-risking there is expensive.
  ^MT168-C09-2
- **Yoav Git** Factor-based risk management: in crises the first (rates) factor dominates volatility, so manage factor risk directly while limiting specific risk per market.  #mech/risk_management
  > in times of crisis you have the first factor which has become very which is which is correlated and its volatility is dominate is dominating everything else.
  indicator: first principal component of portfolio risk · asset: multi · direction: reduce first-factor risk · horizon: days · conditions: optimisation problem · testable: yes - PCA risk · confidence: medium
  ^MT168-C09-3

### C10
- **Niels Kaastrup-Larsen** Keeping illiquid positions while hedging with futures is risky because in a liquidity crisis correlations go to one and exits close.  #mech/liquidity_flows
  > in a liquidity crisis yeah correlations may go to one but you can't get out.
  asset: multi · horizon: days · testable: partly · confidence: medium
  ^MT168-C10-1
- **Yoav Git** Crisis flow sequence: price gaps on the weekend news, CTAs cut risk as volatility gaps, equities and bonds both sell off.  #mech/liquidity_flows _(time-bound view)_
  > CTA flows coming in of course volatility as we discussed volatility is gapping we will start taking risk off.
  indicator: CTA flow · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT168-C10-2
- **Yoav Git** Hedging the common first factor while limiting specific risk per market is a constrained optimisation problem that is probably not worth the effort for a liquid-market CTA, which can simply scale the whole book down.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > certainly in the case of like liquid CTA probably not worth the hassle. You would just basically down gear everything
  indicator: factor-based risk reduction vs uniform down-gearing · asset: multi · horizon: days · conditions: liquid core markets where scaling down is cheap · testable: yes - compare crisis de-risking cost and outcome of both methods · confidence: medium
  ^MT168-C10-X4

### C11
- **Yoav Git** Next in the sequence, value traders holding falling bonds are closed out (long squeeze), then real money buys on stabilisation, then renewed selling after escalation (gilt and Treasury squeezes).  #mech/liquidity_flows _(time-bound view)_
  > suppose I'm a I'm a value trader and I'm I believe in bonds and I'm holding bonds and I'm holding bonds and bond it keeps ticking down
  indicator: value-trader forced selling · asset: rates · horizon: days · conditions: stress · testable: partly · confidence: medium
  ^MT168-C11-1
- **Yoav Git** Discretionary traders watch flows closely while CTAs pay almost none, yet CTAs feature in flow models as one of three player types.  #mech/research_method
  > CTAs in general pay almost next to no attention to flows
  asset: multi · testable: partly · confidence: medium
  ^MT168-C11-2

### C12
- **Yoav Git** Paper conclusion: most volatility is noise; the efficient market hypothesis can hold either because price is right (Shiller) or because there is no true price.  #mech/research_method
  > the vast majority of volatility is is sort of noise.
  indicator: excess volatility · asset: multi · testable: yes · confidence: medium
  ^MT168-C12-1
- **Yoav Git** Flow models use three players: value traders (revert to target price), noise traders (inject volatility), and trend followers (trade first derivative, returns).  #mech/liquidity_flows
  > The player number one is the Shiller player, the fundamental player.
  indicator: value/noise/trend agent model · asset: multi · testable: yes - calibrate · confidence: high
  ^MT168-C12-2
- **Yoav Git** If everyone were a Shiller-style value trader prices would jump to the equilibrium and then barely trade, so observed volatility and trading volume far exceed what pure value investing implies (the excess-volatility puzzle), which motivates flow-based models with noise and trend players.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > The problem with this world view is that markets are a lot noisier than what what we would get if everybody would be like that.
  indicator: excess volatility vs value-trader equilibrium · asset: multi · testable: yes - variance-ratio and volatility bound tests · confidence: high
  ^MT168-C12-X5

### C13
- **Yoav Git** EM-algorithm calibration of the model shows noise is the first order of volatility, value traders second, and trend followers negligible; CTAs create little autocorrelation because footprints are small.  #mech/research_method
  > by the way, CTAs or we do not contribute that much to the volatility.
  indicator: autocorrelation of returns · asset: multi · testable: yes - paper result · confidence: medium
  ^MT168-C13-1
- **Yoav Git** Pendulum picture: trend followers dominate through the centre, value traders dominate at extremes, so markets spend time over- or underpriced.  #mech/overshoot
  > the market is either spent a lot of the time being underpriced or overpriced rather than in the center.
  indicator: pendulum dynamics · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT168-C13-2

### C14
- **Yoav Git** Critique: prices gap on news without trading (nonfarm payroll, weekend Iran attack), so explaining all volatility by trading flows ignores genuine jumps in fundamental value.  #mech/structural_shift
  > half an hour before nonfarm payroll, nobody wants to trade.
  indicator: jumps, nonfarm payroll liquidity · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT168-C14-1
- **Yoav Git** Git: the flow paper sets out to disprove the efficient market hypothesis; in reality markets are a mixture of price-driven flows, flows and genuine changes in fundamental value.  #mech/new _(added by map cross-check)_
  > I don't like going all out to disprove something.
  indicator: flow model vs EMH · asset: multi · conditions: excess-volatility paper · testable: no · confidence: medium
  ^MT168-C14-R1

### C15
- **Yoav Git** Critique: assuming a cubic value-trader response (unbounded) is unrealistic because value traders face risk limits too; the paper uses monthly data so cannot inform daily trading.  #mech/research_method
  > Value traders gets get called out just as much as trend followers in terms of risk management.
  indicator: response function · asset: multi · testable: yes · confidence: medium
  ^MT168-C15-1
- **Yoav Git** Capacity limits risk per market so footprint stays unwindable; larger AUM pushes risk into the biggest markets.  #mech/risk_management
  > the amount of risk that we like to put into each market is limited precisely for the same discussion that we had that we don't want to trade against ourselves
  indicator: capacity per market · asset: multi · testable: yes · confidence: high
  ^MT168-C15-2
- **Yoav Git** Git: such flow models, as they stand, offer neither prediction nor a way to improve a trading model.  #mech/new _(added by map cross-check)_
  > these models are not useful for providing any prediction
  indicator: flow models · asset: multi · conditions: monthly data, long horizon · testable: no · confidence: medium
  ^MT168-C15-R1

### C16
- **Yoav Git** CTA return is diversification times average market Sharpe; if markets are highly correlated, trading only big markets costs little, but if you select low-correlation markets, capacity pushes risk into big markets and cuts effective breadth.  #mech/risk_management
  > the way CTAs make money is the diversification times the average market shop.
  indicator: market correlation, diversification · asset: multi · conditions: depends on correlation of the universe · testable: yes · confidence: medium
  ^MT168-C16-1
- **Yoav Git** Replicating the CTA index at 80% correlation is accepted while S&P replication demands 99%, because CTA constituents are opaque.  #mech/research_method
  > you have a 80% correlation and people think, "Oh, that's great.
  indicator: index replication correlation · asset: multi · testable: yes · confidence: medium
  ^MT168-C16-2
- **Niels Kaastrup-Larsen** Niels argues that although in theory few large markets should replicate a CTA index, in practice replicators' correlation to the index is modest and tracking error substantial.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > when you look at the numbers, that correlation isn't that great. I mean, the tracking error is substantial
  indicator: tracking error / correlation of replicators to CTA index · asset: multi · horizon: years · conditions: index replication with a small liquid universe · testable: yes - correlation and tracking error of replicator products · confidence: medium
  ^MT168-C16-X6

