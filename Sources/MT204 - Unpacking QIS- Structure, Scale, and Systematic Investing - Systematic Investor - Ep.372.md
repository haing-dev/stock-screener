---
source_id: MT204
title: "Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372"
date: 2025-11-06
channel: "Top Traders Unplugged"
url: 
words: 10742
claims: 53
added_by_crosscheck: 12
corrections: 3
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Nick Balters (Goldman Sachs, QIS / systematic strategies)", "Morris Seabirds (host, standing in for Niels Kaastrup-Larsen)"]
tags: [source, layer0]
---
# Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372

**Speakers:** Nick Balters (Goldman Sachs, QIS / systematic strategies); Morris Seabirds (host, standing in for Niels Kaastrup-Larsen)

**Summary:** Late Oct 2025 systematic investor episode. Opens with trend-following performance (April 2025 V-shape whipsaw, speed as the driver of dispersion). Main topic: the roughly $1.3 trillion QIS (bank and asset-manager risk-premia index) market: size, reporting caveats, clients, thousands of indices, wrappers, data-mining control, and whether crowding erodes premia (commodity roll congestion decayed, vol selling insurance-like, trend benefits from early crowding).

**Approach:** QIS, risk premia, trend following, crowding, data mining, index design

**Cross-check completeness estimate of first read:** 0.88 - the first reader got the QIS size, client, wrapper, data-mining, congestion and crowding arguments; missed the SG short-term traders YTD data, currency attribution, why fixed income/FX are small, survey undercount, the packaging rationale, calculation-agent governance, scale-versus-capacity incentive, new-product-twist observation and the 'crowding overstated' conclusion; two speaker misattributions and one overstated figure.

## Argument map

**Episode thesis:** QIS (bank and asset-manager risk-premia indices) is a roughly $1.3tn, opaque, implementation-driven business whose size is uncertain and whose index count reflects customisation, with data mining controlled by culture and explainable performance. Crowding depends on the premium type: allocation-driven roll congestion decayed, vol selling shrinks but stays positive, trend may benefit from early crowding; the main risk is shared-signal externalities. The opening shows 2025 trend dispersion driven by speed around the April V-shape.

### Nick Balters (Goldman Sachs QIS/systematic strategies (regular Systematic Investor guest))
Fingerprint: #approach/replication_indexing #approach/research_robustness_overfitting #approach/positioning_crowding #approach/costs_execution #approach/portfolio_construction_stacking #approach/manager_selection_allocation #approach/trend_following
_Speaker note: Name is the caption spelling (likely Nick Baltas). Several ledger claims were mis-assigned to the host; corrections for C11-1 and C15-2 applied here._

**Worldview premises**
- QIS is a rules-based wrapper (like an S&P 500 index or future) that delivers a risk premium cheaply; growth is about implementation and operational ease, not a sudden belief in systematic investing. _[institutional, stated; support: Analogy to index futures; own experience at a bank]_ ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C07-2|C07-2]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C07-X1|C07-X1]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C07-3|C07-3]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C07-1|C07-1]])
- Part of QIS growth is substitution (exposure moved from CDA/swap), so reported size overstates genuinely new demand. _[institutional, stated; support: Reasoning on reporting; no data]_ ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C06-1|C06-1]])
- Reported QIS size is uncertain both ways: notional conventions, double counting between banks and managers, and unreported hedge-fund premia. _[institutional, stated; support: Reporting conventions; own guess of $600bn +/- $100bn for brokers 'making it up']_ ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C05-1|C05-1]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C05-2|C05-2]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C06-X1|C06-X1]])
- Thousands of indices exist because of client customisation (net vs gross return, exclusions), not serial replacement after overfitting. _[institutional, stated; support: Examples from practice]_ ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C09-1|C09-1]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C09-2|C09-2]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C09-X1|C09-X1]])
- Data mining is unavoidable; it is controlled by product culture and by explaining performance, not by process changes after drawdowns. _[experience, stated; support: Own role in product teams]_ ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C12-1|C12-1]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C12-2|C12-2]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C12-R1|C12-R1]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C13-1|C13-1]])
- Crowding depends on the premium type: allocation-driven premia (roll congestion) can vanish; risk-sharing premia (vol selling) shrink but stay positive because entry barriers rise; behavioural premia (trend) may benefit from early crowding. _[theoretical, stated; support: Car-insurance analogy; 2018-19 internal report on commodity congestion]_ ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C14-3|C14-3]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C15-1|C15-1]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C15-2|C15-2]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C15-X1|C15-X1]])
- Capacity is a binding design constraint; nothing is built for infinite scale and banks can close indices. _[institutional, stated; support: Practice]_ ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C11-2|C11-2]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C11-3|C11-3]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C11-X1|C11-X1]])
- The main crowding risk is externality: many investors with similar 60/40 plus overlay products deleverage on the same macro signals. _[theoretical, stated; support: Reasoning, no data]_ ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C15-4|C15-4]])
- Flows follow index performance; non-delivery of the premium dries up volume. _[experience, stated; support: Business logic]_ ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C16-1|C16-1]])

**Chain: Commodity roll congestion: decay and revival**
1. passive index investors must roll on a predictable schedule → net supply/demand on roll days moves prices: market inelastic to this passive flow ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C14-1|C14-1]])
2. pre-positioning before benchmark rolls → liquidity premium (congestion trade): provides liquidity ahead of passive flows ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C14-1|C14-1]])
3. passive roll demand shrank (smarter, enhanced beta exposures) → market became elastic, trade flattened 2015-18: flat, not negative, so not crowding by QIS ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C14-2|C14-2]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C13-3|C13-3]])
4. commodity demand returned after Russia-Ukraine → trade returned in 2022: passive demand re-emerged ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C14-2|C14-2]])
- Evidence: Internal 2018-19 report; performance path
- Fails when: Passive demand disappears (no premium) or QIS traders crowd (negative returns)

**Chain: Crowding by premium type**
1. risk-sharing premium (vol selling) → competition lowers returns: insurance price falls with more sellers ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C15-1|C15-1]])
2. lower returns → barrier to entry rises: fewer willing sellers below a threshold, so premium stays positive ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C15-1|C15-1]])
3. many similar products and overlays react to the same macro signal → simultaneous deleveraging, correlations unseen in backtests: externality ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C15-4|C15-4]])
- Evidence: Analogy and reasoning
- Fails when: Not tested; flows can reverse when indices underperform

**Chain: Why option wrappers on carry indices are tricky**
1. short-vol carry index earns premium for bearing occasional spikes → buying a call on it removes the premium: circular: the premium compensates the risk the call removes ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C10-1|C10-1]])
2. vol-targeting makes momentum less negatively skewed → option pricing on top is easier: moderates negative skew ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C10-2|C10-2]])
3. vol-targeting a strategy that recovers after spikes → cuts exposure when rebound begins: sub-optimal profile ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C11-1|C11-1]])
- Evidence: Economic reasoning
- Fails when: Strategies with linear, vol-controlled payoffs

**Decision process**
- [research] Control data mining via culture: call it out, treat tweaks as data-mined, ensure tweaks are not designed to make Sharpe look better after a drawdown.. Why: Unavoidable bias ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C12-1|C12-1]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C12-2|C12-2]])
- [research] Justify strategy changes by explaining recent performance, not repairing it.. Why: Client trust: explainable underperformance is acceptable, unexplained is worst ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C12-2|C12-2]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C13-1|C13-1]])
- [universe] Design indices for capacity; broader universes with frontier or illiquid assets support only a fraction of capacity.. Why: Profitability depends on scale ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C11-2|C11-2]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C11-X1|C11-X1]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C08-3|C08-3]])
- [execution] Close an index when it cannot be run without market impact.. Why: Protect investors and market ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C11-3|C11-3]])
- [other] Product development has four drivers: academic research, client appetite shifting to outcomes (defensive, yield, inflation, regime), technology, and market evolution.. Why: Describes how the product pipeline works ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C08-2|C08-2]])
- [other] Clients add timing and sizing on top of QIS implementation.. Why: QIS supplies implementation, not alpha ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C07-3|C07-3]])
- [other] Intraday momentum became crowded via QIS wrappers in 2021-22: defensive payoff intact but cost of carry up.. Why: Evidence of wrapper-driven crowding ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C15-3|C15-3]])
- [other] Most volume is delta-1 swaps; option wrappers are a small share rising from insurers.. Why: Client demand for capped loss ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C09-2|C09-2]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C10-R1|C10-R1]])

**Evidence style:** Practitioner reasoning and economic analogies; an internal report on commodity congestion; no backtest data shown on air.

**Views at the time**
- (2025-10-30) The $1.3tn QIS figure could be too high (double counting, substitution) or too low (unreported hedge funds).. Reasoning: Reporting conventions ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C05-1|C05-1]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C06-X1|C06-X1]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C06-1|C06-1]])
- (2025-10-30) Equity market kept absorbing negative news: a fragile vs resilient pendulum into November.. Reasoning: Observation ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C01-1|C01-1]])
- (2025-10-30) Fixed income and FX are in a growth phase within QIS.. Reasoning: Historic equity-centred academic work ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C05-X1|C05-X1]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C05-3|C05-3]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C04-4|C04-4]])
- (2025-10-30) Crowding concerns about QIS are generally overstated but not absent.. Reasoning: Premium-by-premium analysis ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C15-X1|C15-X1]])
- (2025-10-30) Dispersion in trend returns in 2025 is mostly explained by speed around the April V-shape.. Reasoning: Mid-speed whipsaw (hedged: 'not much data') ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C03-3|C03-3]])

### Morris Seabirds (Host standing in for Niels Kaastrup-Larsen; runs a systematic CTA book (uses 'we'))
Fingerprint: #approach/trend_following #approach/short_term_systematic #approach/research_robustness_overfitting #approach/position_sizing_vol_target #approach/costs_execution #approach/regime_detection
_Speaker note: Name is the caption spelling (likely Moritz Seibert). Attributions in the ledger follow the corrections list. A shared voice with Balters in places._

**Worldview premises**
- The dispersion of 2025 trend-following returns is driven by trading speed around the April V-shape, worth about 10% for the year. _[empirical, stated; support: Own book and index comparison; 'not that I have too much data to support it']_ ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C03-2|C03-2]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C02-X1|C02-X1]])
- Equity risk premium is about 6-8%, but the last five years delivered 15-20% annually except 2022. _[empirical, stated; support: Recall, not data]_ ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C02-2|C02-2]])
- Reacting to the last drawdown (SVB, dollar-yen, April) by tweaking systems is a recipe for underperformance. _[experience, stated; support: Own practice]_ ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C13-2|C13-2]])
- Many new risk-premium indices are small twists on existing ones, a sign of launch pressure and over-optimisation. _[experience, stated; support: Inbound pitches]_ ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C12-X1|C12-X1]])
- Hedge funds buy intraday momentum and vol strategies from banks because of operational burden. _[institutional, stated; support: Observation]_ ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C08-1|C08-1]])

**Chain: April 2025 V-shape and system speed**
1. April equity sell-off then recovery → fast systems capture the V; slow systems ride it: speed decides exposure at the turning points ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C03-3|C03-3]])
2. medium speed → whipsawed at the worst time: delivered exposure just as market recovered ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C03-3|C03-3]])
3. long-term system stopped out of nearly all equity indices → re-entry only by July-August: exits to flat (no-trade zone), wait for a new signal ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C04-1|C04-1]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C04-2|C04-2]])
- Evidence: Own book experience
- Fails when: Not tested on data

**Decision process**
- [signal] Exits are trailing stops or other rules that go to flat; no forced reversal to short.. Why: Neutral zone avoids reversing into the whipsaw ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C04-2|C04-2]])
- [risk] Do not change the system after a drawdown.. Why: Last-drawdown tweaking harms results ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C13-2|C13-2]])
- [research] Question new indices that are minor twists on old ones.. Why: Overfitting and product-for-product's-sake ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C12-X1|C12-X1]])
- [other] Watch the commodity roll (days 5-9) liquidity trade, now largely decayed.. Why: Example of crowding ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C13-3|C13-3]])

**Evidence style:** Own CTA book results and index data.

**Views at the time**
- (2025-10-29) As of 29 Oct 2025 S&P +18% YTD and MSCI World +22% decoupled from CTA indices (BTop50 +2.35%, trend ~flat, short-term traders -4.6%).. Reasoning: Performance update ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C02-1|C02-1]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C02-X1|C02-X1]])
- (2025-10-29) October trend gains in precious metals and livestock gave back after about 20 October.. Reasoning: Reversals in palladium, gold, silver, platinum and cattle ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C02-3|C02-3]])
- (2025-10-29) Rates were the main whipsaw in 2025; currencies second worst; equities the only clearly positive sector.. Reasoning: Own attribution ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C03-1|C03-1]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C03-X1|C03-X1]])
- (2025-10) Long-term system exited almost all equity markets in April and re-entered July-August.. Reasoning: Own book ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C04-1|C04-1]])

### Disagreements
- **Can the QIS size be trusted / how much is genuine growth**: Morris Seabirds: Takes the Alborne $1.3tn as a large and growing figure but flags delta/leverage ambiguity and double counting. ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C04-3|C04-3]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C06-X1|C06-X1]]); Nick Balters: Figure is uncertain both ways, partly substitution; broker-dealer ~$600bn +/- $100bn is a guess. ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C05-1|C05-1]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C05-2|C05-2]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C06-1|C06-1]])
- **Trend following and early crowding**: Nick Balters: Behavioural strategies like trend may benefit from early crowding; risk is negative skew management. ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C15-2|C15-2]]); Morris Seabirds: Asks if QIS crowding has removed premia as in roll congestion (the commodity roll trade has decayed). ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C13-3|C13-3]])
- **Why the congestion trade flattened**: Morris Seabirds: Suggests enough money crowded in so the effect has gone away. ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C13-3|C13-3]]); Nick Balters: Flat, not negative, so elastic market not QIS crowding. ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C14-2|C14-2]])

### Gaps and conflicts
- QIS size, broker-dealer estimate and the survey's reporting conventions are acknowledged guesses. ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C05-1|C05-1]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C05-2|C05-2]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C04-3|C04-3]])
- Crowding conclusions rest on analogy and one internal report; no data presented. ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C14-2|C14-2]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C15-1|C15-1]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C15-X1|C15-X1]])
- Speed explanation of 2025 dispersion is hedged as unsupported by data by the speaker. ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C03-2|C03-2]], [[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C03-3|C03-3]])
- Claim that equity momentum benefits from vol targeting asserted without evidence. ([[MT204 - Unpacking QIS- Structure, Scale, and Systematic Investing - Systematic Investor - Ep.372#^MT204-C10-2|C10-2]])

### Forward-looking inputs (reader synthesis)
Observable inputs: client flows into QIS, index performance versus promised premium, passive roll demand in commodities, simultaneous deleveraging in 60/40 plus overlay products, tech and listed options market evolution. Horizon: years for product cycles; flows react to underperformance.

### Reader inferences (not stated by the speakers)
- This episode is about market structure of derivatives wrappers, not return forecasting; its testable implications are about premium durability by type (allocation, risk-sharing, behavioural).
- Both speakers work in this industry, so statements on crowding and data mining are self-reported practice.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro; fragility vs resilience debate |
| C02 | 3 | Oct 2025 performance numbers; equities dominance; precious metals and livestock give-back |
| C03 | 3 | trend attribution by asset class; April V-shape and speed |
| C04 | 4 | trend exits in April; QIS size survey |
| C05 | 3 | size reporting conventions, double counting, asset class split |
| C06 | 1 | survey caveats, substitution effect, clients history |
| C07 | 3 | client types, QIS as rules-based index technology |
| C08 | 3 | intraday strategies, four pillars of product development |
| C09 | 2 | number of indices, customization, wrappers |
| C10 | 2 | wrappers, options on negatively skewed profiles, vol targeting |
| C11 | 3 | vol targeting vs recovery, scale and capacity |
| C12 | 2 | innovation versus data mining, product culture |
| C13 | 3 | explaining underperformance, crowding question, commodity congestion setup |
| C14 | 3 | congestion premium decay, risk-sharing versus allocation premia |
| C15 | 4 | insurance premium crowding, trend crowding, externalities |
| C16 | 1 | performance drives flows; outro |

## Claims

### C01
- **Nick Balters** In 2025 the equity market kept absorbing negative news (events against sentiment and growth) and stayed resilient, leaving a fragile-versus-resilient pendulum into November.  #mech/behavioral _(time-bound view)_
  > this year has been pretty much like a bit of a debate between fragility and resilience, right?
  asset: equities · horizon: months · testable: no - sentiment view · confidence: medium
  ^MT204-C01-1

### C02
- **Morris Seabirds** The S&P 500's Sharpe ratio in 2025 was far above every other asset and CTA index (S&P about +18% YTD, MSCI World +22%, BTop50 +2.35%, trend index about flat) as of 29 October 2025.  #mech/cycle_persistence _(time-bound view)_
  > The sharp ratio of the S&P 500 has now decoupled from everything else.
  indicator: BTop50, SG CTA, SG Trend, MSCI World, S&P 500 YTD returns · asset: equities · horizon: years · testable: yes - index data · confidence: high
  ^MT204-C02-1
- **Morris Seabirds** The long-run equity premium is about 6-8% a year, but the last five years delivered 15-20% annually except 2022 (inflation spike where equities and rates sold off together).  #mech/risk_premium _(time-bound view)_
  > the equity risk premium or you expect to make six seven eight something like that percent per year
  indicator: S&P 500 annual return · asset: equities · horizon: years · testable: yes - historical data · confidence: medium
  ^MT204-C02-2
- **Morris Seabirds** In October 2025 trend followers gained from long precious metals and livestock until about 20 October, then gave back open profits as palladium, gold, silver, platinum and cattle reversed.  #mech/overshoot _(time-bound view)_
  > And then a lot of give back of open trade profits uh on exactly these markets.
  indicator: precious metals and livestock trends · asset: commodities · direction: long metals and cattle, then reversal · horizon: weeks · testable: yes - price data · confidence: high
  ^MT204-C02-3
- **Morris Seabirds** As of 29 October 2025 the SG Short-Term Traders index was about +0.5% for October but -4.6% year to date, versus roughly flat for the SG Trend index and -1% for the SG CTA index, so short-horizon CTAs lagged badly in 2025 even though they did well in the April V-shape.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > The short-term traders index from Sockchen is up about half a percent this month and still down quite a bit minus 4.6% for the year
  indicator: SG Short-Term Traders index vs SG Trend / SG CTA · asset: multi · direction: short-term CTAs lagged longer-term trend in 2025 · horizon: years · conditions: 2025 whipsaw in rates and the April V-shape · testable: yes - index return data · confidence: high
  ^MT204-C02-X1

### C03
- **Nick Balters** In 2025 fixed income was the main whipsaw for trend followers, offset by gains in equities, gold, aluminium, copper and a sugar short.  #mech/slow_reaction _(time-bound view)_
  > rates keep on being the same story for the year. Keep on whipsing, keep on losing on the trend side.
  indicator: rate trend returns · asset: rates · horizon: months · conditions: range-bound rates · testable: yes - sector attribution · confidence: high
  ^MT204-C03-1
- **Morris Seabirds** The speed of response around the April 2025 equity V-shape (sell-off then recovery) explains most 2025 trend-follower dispersion, worth about 10% for the year.  #mech/slow_reaction _(time-bound view)_
  > I think that's the main driver of dispersion that we've seen this year in the trend following space.
  indicator: trend system speed / volatility response · asset: equities · horizon: months · conditions: sharp V-shaped reversals · testable: yes - compare fast and slow trend lookbacks over Apr-Dec 2025 · confidence: medium
  ^MT204-C03-2
- **Nick Balters** Fast short-term trend systems captured the V-shape in April, slow systems rode the whole V and recovered, and mid-speed systems got whipsawed at the worst time.  #mech/slow_reaction _(time-bound view)_
  > the short-term traders actually doing well in the Vshape
  asset: equities · direction: fast and slow outperform middle · horizon: months · conditions: V-shaped reversal · testable: yes - speed sweep in backtest · confidence: medium
  ^MT204-C03-3
- **Morris Seabirds** In Morris's CTA book currencies were flat in October 2025 (JPY the best contributor, AUD and GBP the worst) and the second-worst asset class of the year after rates; equities were the only clearly positive sector.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > year to date it's kind of the second worst past rates
  indicator: currency trend P&L (JPY, AUD, GBP) · asset: fx · horizon: months · conditions: 2025 trend-follower attribution · testable: yes - sector attribution of a CTA book · confidence: medium
  ^MT204-C03-X1

### C04
- **Morris Seabirds** Long-term trend system was stopped out of nearly all equity indices in April 2025 and re-entered only by July-August, so a slow exit/re-entry cost much of the year.  #mech/slow_reaction _(time-bound view)_
  > All the European indices, we we just lost all our own positions in April.
  indicator: trailing stop exits and re-entry · asset: equities · horizon: months · conditions: sharp reversals · testable: yes - rule-based · confidence: high
  ^MT204-C04-1
- **Morris Seabirds** Exits go to flat (neutral zone with no-trade area) rather than reversing into a short, so after a stop-out the system waits for a new trend signal.  #mech/risk_management
  > we're not forcing ourselves to reverse the position into shorts.
  indicator: trailing stops, no-trade zone · asset: multi · testable: yes - exit rule variant · confidence: high
  ^MT204-C04-2
- **Morris Seabirds** Alborne's H1 2025 survey puts QIS notional assets at about $1.3 trillion, split roughly 50/50 between bank and asset-manager QIS.  #mech/structural_shift _(time-bound view)_
  > they have hit a new all-time high at about$1,300 billion US
  indicator: Alborne QIS survey · asset: multi · horizon: years · testable: yes - survey data · confidence: medium
  ^MT204-C04-3
- **Morris Seabirds** QIS assets are over half equity, then multi-asset and commodities; fixed income (about $50bn), FX ($27bn) and credit ($13bn) are small relative to their market size.  #mech/structural_shift _(time-bound view)_
  > fixed income is only 50 billion even though fixed income markets are gigantically large markets
  indicator: QIS asset class split · asset: multi · testable: yes - survey data · confidence: high
  ^MT204-C04-4

### C05
- **Nick Balters** QIS size figures are uncertain because notional is reported inconsistently (unfunded swaps vs options, leverage and delta adjustment) and asset-manager and bank numbers may double count.  #mech/research_method
  > Do you do a look through leverage adjustment? Do you do delta adjustment if that is an option?
  asset: multi · testable: partly - requires disclosure · confidence: high
  ^MT204-C05-1
- **Nick Balters** Broker-dealer QIS is about $600bn plus or minus $100bn on a rough estimate; the market grew with winter periods around 2018 and 2021.  #mech/structural_shift _(time-bound view)_
  > the brokilla sum which is close to the 600 billion mark
  asset: multi · testable: no - speaker admits guess · confidence: low
  **Correction (cross-check):** Nick calls the $600bn (+/-$100bn) broker-dealer figure a rough guess ('I'm just making it up really'), and the 2018 and 2021 'winter periods' were setbacks in the growth, not periods of growth. → Nick's rough guess is that broker-dealer QIS is close to $600bn plus or minus $100bn (no hard data); the business has grown over the years with a few setback ('winter') periods, around 2018 and 2021.
  ^MT204-C05-2
- **Nick Balters** On the asset-manager side QIS is mainly equity long-only smart beta, while bank QIS is more evenly split and multi-asset/cross-asset carry baskets are growing.  #mech/structural_shift
  > the equity long only space is by far dominating the asset manager world
  indicator: smart beta / factor strategies · asset: equities · testable: no - descriptive · confidence: high
  ^MT204-C05-3
- **Nick Balters** Fixed income and FX are a small part of QIS because banks' QIS business grew out of equity long/short, commodity roll indices and delta-1 products, and academic risk-premia work has been mostly on equities; Nick sees fixed income and FX as now in a growth phase.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > part of the reason why you see less on the fixed income and effects side is that historically liquidity has improved
  indicator: QIS notional by asset class · asset: multi · direction: growth in rates and FX risk-premia indices · horizon: years · conditions: liquidity in options and delta-1 products matters for bank QIS · testable: partly - depends on survey data · confidence: medium
  ^MT204-C05-X1

### C06
- **Nick Balters** Part of QIS growth is substitution: exposure that was in a CDA or swap is repackaged as a QIS index, not genuine new strategy demand.  #mech/research_method
  > the market still consumes the same level of liquidity demand. it's just now marked under the QIS kind of badge
  asset: multi · testable: no - accounting caveat · confidence: medium
  ^MT204-C06-1
- **Nick Balters** The $1.3tn survey could also be too low, because hedge funds and other managers running risk-premium strategies do not report to it, so the true size is uncertain in both directions.  #mech/research_method _(added by sonnet-xhigh cross-check, time-bound view)_
  > maybe hedge funds, just you know, people trading risk premium strategies that are not reporting to that survey
  indicator: QIS survey size · asset: multi · conditions: survey coverage and reporting convention · testable: partly - needs alternative size estimates · confidence: medium
  ^MT204-C06-X1

### C07
- **Nick Balters** QIS began with commodity roll indices and post-GFC factor investing by Nordic pensions that replaced asset-class mixes with factor mixes (equity market neutral, vol carry).  #mech/structural_shift
  > done by some of the Nordic pensions to replace or maybe enhance um their risk profile by by risk factors
  asset: multi · horizon: years · testable: no - history · confidence: high
  ^MT204-C07-1
- **Nick Balters** A risk premium (volatility, equity, commodity carry) can be expressed as rules and wrapped as an index or swap, giving investors access like a futures contract on S&P 500.  #mech/risk_premium
  > if today we claim that volatility is rewarded and whoever is willing to sell insurance should be compensated that in itself can be described with a set of rules by selling some options
  indicator: volatility risk premium index · asset: multi · testable: yes - rules based · confidence: high
  ^MT204-C07-2
- **Nick Balters** Clients use QIS for implementation and add their own value through timing and sizing models.  #mech/research_method
  > utilize their internal models on timing utilize their internal models on sizing focus more on kind of bringing their alpha which is more of a timing element
  asset: multi · testable: no - business model · confidence: medium
  ^MT204-C07-3
- **Nick Balters** QIS grew not because clients suddenly believed in systematic investing but because an index or swap wrapper delivers a rules-based exposure with less operational burden and better cash efficiency than building it in-house.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > nobody suddenly thought that systematic is the way but systematic is the pay to deliver into an index format what otherwise could be a cumbersome and tedious process
  indicator: QIS wrappers · asset: multi · direction: growth in packaged systematic exposure · horizon: years · testable: no - explanatory claim on industry structure · confidence: medium
  ^MT204-C07-X1
- **Nick Balters** Balters: early QIS users were asset owners (pensions, sovereign wealth funds) and asset managers; the client base later widened to private banks and hedge funds.  #mech/new _(added by map cross-check)_
  > the primary users in the early days were either asset owners
  indicator: QIS client mix · asset: multi · horizon: years · conditions: since ~2010 · testable: no · confidence: medium
  ^MT204-C07-R1

### C08
- **Morris Seabirds** Hedge funds buy intraday momentum and vol strategies from banks through QIS because the operational and technology burden is high.  #mech/structural_shift
  > if the bank can you know kind of like every five minutes or what it is do like a a vulcar intraday strategy on the S&P 500 then I might be better off just buying it from them
  indicator: intraday momentum / intraday vol index · asset: equities · horizon: days · testable: no - business observation · confidence: medium
  ^MT204-C08-1
- **Nick Balters** QIS development has four drivers: academic research, shifting client appetite from hedge fund replacement to specific outcomes (defensive, yield, inflation, regime), technology, and market evolution (new commodities, listed short options).  #mech/research_method
  > a combination of four main pillars in terms of product development
  asset: multi · testable: no - framework · confidence: high
  ^MT204-C08-2
- **Nick Balters** New tradable markets (frontier commodities, listed options) allow out-of-sample tests net of cost on universes that could not be tested before.  #mech/research_method
  > allowing us to almost do out of sample testing on universes that otherwise would not be able to do so
  asset: multi · testable: partly - depends on data history · confidence: medium
  ^MT204-C08-3

### C09
- **Nick Balters** There are thousands of QIS indices mostly because of client customisation (tax treatment net vs gross total return, no equity upside, portfolio exclusions) not because designers kept replacing indices after overfitting.  #mech/research_method
  > any different implementation be it for a specific client ask or a specific need has to be a different index
  indicator: count of QIS indices · asset: multi · testable: no - descriptive · confidence: high
  ^MT204-C09-1
- **Nick Balters** Most QIS volume is delta-1 swap exposure; optionalised wrappers (call options capping losses) are a small share, rising in the last two to three years mainly from insurers.  #mech/structural_shift _(time-bound view)_
  > the vast majority has always been in the in the kind of the delta 1 space
  asset: multi · testable: no - descriptive · confidence: high
  ^MT204-C09-2
- **Nick Balters** QIS indices are run under governance: European benchmark rules require an independent calculation agent, and banks use either an internally separated calculation unit or an external agent, a business choice as long as governance holds.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > there's a lot of governance around this business. Um some others would be using external calculation agents
  indicator: QIS index calculation · asset: multi · conditions: benchmark regulation in Europe · testable: no - governance practice · confidence: medium
  ^MT204-C09-X1

### C10
- **Nick Balters** Buying a call on a short-vol carry index removes the premium, since the premium compensates for the occasional vol spike risk; banks quoting such options need vol control and sell at wider premia.  #mech/risk_premium
  > almost writing a call option to it in itself nullifies the existence of the premium in the first place
  indicator: call option on volatility carry index · asset: multi · testable: yes - option pricing logic · confidence: high
  ^MT204-C10-1
- **Nick Balters** Equity momentum is vol-targeted, which reduces its negative skew and makes option pricing on top easier.  #mech/risk_management
  > negative skew in equity momentum can be moderated by uh by vault targeting
  indicator: equity momentum with volatility target · asset: equities · testable: yes - backtest with and without vol target · confidence: medium
  ^MT204-C10-2
- **Morris Seabirds** Morris: for a call option on a QIS index, the issuing bank is effectively the only liquidity source, so it protects its book with vol control and quotes wide premia.  #mech/new _(added by map cross-check)_
  > the only party that will quote a price is you
  indicator: option on QIS index · asset: multi · conditions: bank-quoted option wrappers · testable: no · confidence: medium
  ^MT204-C10-R1

### C11
- **Morris Seabirds** Volatility targeting hurts strategies that recover after volatility spikes (rebounds), because it cuts exposure when the rebound starts, so options-friendly vol-targeting can be suboptimal.  #mech/risk_management
  > if you were to volatility target a strategy that is supposed to be reacting and recovering post the volatility spike you're kind of acting against its ability to recover
  indicator: volatility target on rebound strategy · asset: multi · conditions: post-spike recovery strategies · testable: yes - backtest · confidence: medium
  **Correction (cross-check):** Wrong speaker: the point that vol-targeting a strategy that recovers after volatility spikes works against it is Nick Balters', in his answer; the host only asked about vol targeting. → Nick Balters: volatility targeting a strategy that is meant to recover after a volatility spike works against its ability to recover and yields a sub-optimal profile, so making a QIS option-friendly through vol control has a cost.
  ^MT204-C11-1
- **Nick Balters** Illiquid and frontier markets may offer higher premia but have lower capacity; QIS design is conscious of capacity and nothing is built for infinite scale.  #mech/liquidity_flows
  > if there is a liquidity premium to be harvested or illiquidity or whatever it's worth it
  indicator: capacity versus liquidity premium · asset: commodities · testable: partly - capacity estimates · confidence: high
  ^MT204-C11-2
- **Nick Balters** Banks can close an index when a design can no longer be run without market impact, unlike an ETF.  #mech/risk_management
  > so there are multiple cases whereby a specific design cannot sustain anymore without being market impactful
  asset: multi · testable: no - practice · confidence: high
  ^MT204-C11-3
- **Nick Balters** Because QIS profitability depends on scale, popular bank trend/CTA indices cover only the deepest liquid markets (the host notes they omit smaller markets); broader indices with illiquid assets exist but support only a fraction of the capacity.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > Generally we build we build product for scale because that in itself is associated with how we can see the profitability of this business
  indicator: capacity of QIS indices · asset: multi · direction: liquid universe for scalable products · conditions: capacity versus liquidity premium trade-off · testable: partly - capacity estimates need market-impact data · confidence: medium
  ^MT204-C11-X1

### C12
- **Nick Balters** Data mining cannot be avoided; its control is product culture: call it out, look at tweaks as data-mined, and ensure new tweaks are not designed to make the Sharpe look better after a drawdown.  #mech/research_method
  > there is no way you can avoid data mining. If I were to show you like 10 back tests, you would basically drop the bottom one
  indicator: backtest selection bias · asset: multi · testable: partly - culture, not metric · confidence: high
  ^MT204-C12-1
- **Nick Balters** After a drawdown (April trend following) there is temptation to tweak speed or sizing, which is an overfitting bias; strategy changes should be justified by explaining, not repairing, recent performance.  #mech/behavioral
  > if only we're a bit slower or if only we're a bit uh I don't know overweight this asset class
  asset: multi · testable: no - process · confidence: high
  ^MT204-C12-2
- **Morris Seabirds** Many 'new' risk-premium indices pitched to a quant desk are small twists on existing strategies, a sign of pressure to launch products for their own sake and of over-optimisation.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > it's kind of like the same that you've had before, just a little bit of a of a new twist to it
  indicator: new QIS index proposals · asset: multi · testable: no - anecdotal observation · confidence: medium
  ^MT204-C12-X1
- **Nick Balters** Balters: data mining cannot be avoided because anyone shown ten backtests discards the worst one without thinking; the control is awareness and culture, not elimination.  #mech/new _(added by map cross-check)_
  > if I were to show you like 10 back tests, you would basically drop the bottom one
  indicator: backtest selection bias · asset: multi · testable: no - process statement · confidence: high
  ^MT204-C12-R1

### C13
- **Nick Balters** Explainable underperformance builds client trust; unexplained underperformance is worst.  #mech/research_method
  > if we cannot explain underperformance that's the worst thing that can happen
  asset: multi · testable: no - principle · confidence: high
  ^MT204-C13-1
- **Morris Seabirds** Reacting to SVB, the dollar-yen unwind and April by tweaking systems to avoid the last drawdown is a recipe for underperformance.  #mech/behavioral
  > reacting on the motion and just making the last draw down outperform is purely the recipe for underperformance
  asset: multi · testable: partly - overfitting logic · confidence: high
  ^MT204-C13-2
- **Morris Seabirds** The commodity index roll (days 5-9) liquidity provision trade worked 10-15 years ago but has largely decayed.  #mech/crowding_positioning
  > providing liquidity during that role and then reversing the position you know 5 days later I think that strategy has largely decayed
  indicator: GSCI-style roll period liquidity provision · asset: commodities · horizon: days · testable: yes - roll-window return study · confidence: medium
  ^MT204-C13-3

### C14
- **Nick Balters** Congestion trade: pre-position before predictable benchmark commodity index rolls and capture a liquidity premium from passive rolling demand.  #mech/liquidity_flows
  > I capture what is called the congestion premium which is nothing more than liquidity premium liquidity provision here
  indicator: commodity index roll schedule · asset: commodities · direction: buy before benchmark buys, sell before benchmark sells · horizon: days · testable: yes - roll-window event study · confidence: high
  ^MT204-C14-1
- **Nick Balters** The congestion trade flattened around 2015-18 not because QIS crowded it (which would give negative returns) but because the market became elastic as passive roll demand shrank; it came back in 2022 with commodity demand.  #mech/liquidity_flows
  > And the flattening out of the strategy, it's more that the initial demand for this liquidity is no longer there.
  indicator: commodity roll premium · asset: commodities · horizon: years · conditions: returns when passive roll demand is large · testable: yes - roll premium over time · confidence: medium
  ^MT204-C14-2
- **Nick Balters** Allocation-driven premia (roll congestion) can disappear with crowding or lack of demand; risk-sharing premia like volatility selling persist because someone must take the risk others will not.  #mech/risk_premium
  > this demand for commodity roles is not driven by some sort of risk sharing mechanism. It's purely allocation decision.
  indicator: premium type: allocation versus risk-sharing · asset: multi · testable: partly - classification is judgemental · confidence: high
  ^MT204-C14-3

### C15
- **Nick Balters** Crowding in an insurance-type premium (vol selling) lowers returns but not to zero because a barrier to entry rises as returns fall, so premia stay positive.  #mech/risk_premium
  > the premium to insure your car is going to drop purely by the by the economics of competition
  indicator: short volatility premium · asset: multi · horizon: years · conditions: risk-sharing premia · testable: yes - long-run premium trend · confidence: medium
  ^MT204-C15-1
- **Morris Seabirds** Behavioural strategies like trend following may benefit from early crowding; their issue is controlling negative skew events, not premium erosion.  #mech/crowding_positioning
  > trend following is actually benefiting from early crowding
  indicator: trend following crowding · asset: multi · testable: partly - hard to measure crowding · confidence: medium
  **Correction (cross-check):** Wrong speaker: Nick Balters makes the argument (trend following may benefit from early crowding; the problem is risk management of negative skew events); Morris only interjects 'to the fire'. → Nick Balters: behavioural strategies such as trend following may benefit from early crowding; the real issue is moderating negative-skew events (risk management), not premium erosion.
  ^MT204-C15-2
- **Nick Balters** Intraday momentum became crowded via QIS wrappers in 2021-2022: the defensive payoff remains but its cost of carry rose.  #mech/crowding_positioning _(time-bound view)_
  > maybe the cost of care of maintaining this defensive strategy has kind of increased over the years
  indicator: intraday momentum index · asset: equities · horizon: years · testable: yes - strategy return decomposition · confidence: medium
  ^MT204-C15-3
- **Nick Balters** The main crowding risk is externalities: many investors with similar 60/40 plus overlay products react to the same macro signals and deleverage together, creating correlations not seen in backtests.  #mech/crowding_positioning
  > those components now can expost realize correlations that we haven't seen in a back test.
  indicator: correlation of alternatives in stress · asset: multi · testable: partly - only post-event · confidence: medium
  ^MT204-C15-4
- **Nick Balters** Crowding concerns about QIS are generally overstated because they are not analysed strategy by strategy (liquidity-allocation premia, risk-sharing premia and behavioural strategies each react differently), but that does not mean there is no problem.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check)_
  > I think crowding implications have been overstated because they haven't necessarily been looked through the economics and the mechanics of the strategies
  indicator: QIS crowding by premium type · asset: multi · horizon: years · conditions: depends on the economic source of the premium · testable: partly - premium decay can be tested by strategy type · confidence: medium
  ^MT204-C15-X1

### C16
- **Nick Balters** Flows follow index performance: if QIS indices fail to deliver the premium, volume dries up and flows revert.  #mech/liquidity_flows
  > If your indices do not perform, if they do not provide the premium um that you know we suggest or expect there to be, then the volume will dry up.
  asset: multi · testable: partly - flow data · confidence: high
  ^MT204-C16-1

