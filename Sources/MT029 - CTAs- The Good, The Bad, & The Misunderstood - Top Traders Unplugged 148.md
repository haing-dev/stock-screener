---
source_id: MT029
title: "CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148"
date: 2025-04-03
channel: "Top Traders Unplugged"
url: 
words: 12726
claims: 53
added_by_crosscheck: 9
corrections: 6
crosscheck: "opus cross-check"
speakers: ["Graham Robertson (Man AHL, CEO of Man AHL)", "Rob Carver (independent systematic trader and author)", "Yav Git (Gresham Research, Safi fixed income CTA)", "Niels Kaastrup-Larsen (host, hedge fund manager)"]
tags: [source, layer0]
---
# CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148

**Speakers:** Graham Robertson (Man AHL, CEO of Man AHL); Rob Carver (independent systematic trader and author); Yav Git (Gresham Research, Safi fixed income CTA); Niels Kaastrup-Larsen (host, hedge fund manager)

**Summary:** Top Traders Unplugged 148 (April 2025): three former AHL colleagues discuss asset-class-specific vs multi-asset CTA design, liquidity and trend, under-allocation to CTAs, execution costs and technology. Conclusions: trend arises from sustained imbalances (Yav) though Rob doubts asset-class differences; execution mostly matters in illiquid markets; large-AUM products risk lowering Sharpe.

**Approach:** trend following, execution and trading costs, fixed income CTA, CTA allocation

**Cross-check completeness estimate of first read:** 0.88 - content coverage is good (missed Rob's rebuttal, Graham's liquidity and allocator points, two execution claims), but speaker attribution in the unlabelled captions was wrong or mixed in 6 of 44 claims.

## Argument map

**Episode thesis:** Three former AHL colleagues (Graham Robertson, Rob Carver, Yav Git) and host Niels Kaastrup-Larsen debate whether trend following should be built per asset class or as one multi-asset program. Yav argues trends come from sustained imbalances that differ by asset class (rate gradients in fixed income and EM FX, valuation anchors in equities, slow supply in commodities, no anchor in crypto), so implementation, risk and execution should be tailored; Rob doubts the asset-class differences and the execution gains and prefers one general risk model. They also discuss why CTAs are under-allocated (a 0.7 Sharpe beside 1.5-Sharpe peers, a crude convexity hedge, unattractive high-volatility share classes) and whether large-AUM entrants such as BlackRock and Fidelity will help or lower the perceived Sharpe.

### Yav Git (Founder of Safi (fixed income CTA, Gresham Research); ex-Brevan Howard, Winton and head of fixed income and innovation at AHL)
Fingerprint: #approach/trend_following #approach/macro_fundamental_topdown #approach/costs_execution #approach/position_sizing_vol_target #approach/crisis_alpha_convexity #approach/liquidity_flows #approach/commodity_fundamentals #approach/manager_selection_allocation
_Speaker note: Captions render names as 'Y git', 'Yav', 'y', and the transcript has several speaker mix-ups corrected in the ledger (see claim corrections for C03-1, C09-1, C17-1). His claims are the most numerous; where a claim is attributed to Graham in captions but belongs to him, the ledger correction is applied._

**Worldview premises**
- Trends arise from sustained imbalances: an interest-rate gradient between central banks creates sustained carry flows and positive autocorrelation (like a metal bar held at two temperatures); EURUSD without a gradient shows little trend while high-carry EM currencies trend strongly. _[theoretical, stated; support: Analogy and what he sees in data; Rob calls the theory 'cute' and unproven.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C08-1|C08-1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C08-2|C08-2]])
- Crypto trends well because it has no valuation anchor and is in permanent imbalance; it also has enormous right skew, so risk control and position management should differ from other asset classes. _[theoretical, stated; support: Reference to a crypto paper (Graham and a co-author); no data here.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C05-2|C05-2]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C05-X1|C05-X1]])
- Equity trend is weaker than other sectors because value traders inject negative autocorrelation; in commodities supply takes time to meet demand (AI power demand example), creating sustained imbalance. _[theoretical, stated; support: First-principles reasoning.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C09-2|C09-2]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C09-3|C09-3]])
- Liquidity is mainly a limit on diversification and capacity, not an explainer of performance; Rob's blog found no correlation, but he thinks it measures the wrong liquidity (the imbalance matters). _[empirical, stated; support: Agrees with Rob's blog conclusion but argues the choice of liquidity measure.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C09-1|C09-1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C09-4|C09-4]])
- A CTA's utility to an allocator is crisis alpha and convexity relative to what the allocator holds, so asset-class-specific trend products (for example fixed income only) are better building blocks than one pooled program. _[theoretical, stated; support: Argument from allocator utility; his own firm is built that way (a commercial interest).]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C05-1|C05-1]])
- A single market's trend Sharpe is only about 0.25, so tailoring implementation per asset class to lift it to 0.30 adds real value after diversification. _[empirical, stated; support: Rough figures quoted from memory; no table.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-1|C06-1]])
- Commodity markets diversify naturally (equal weight works), whereas fixed income has a high loading on the Fed as a common factor and strong left skew, like multi-strat pods, so it needs cleverer construction and tighter risk control. _[empirical, stated; support: Own experience running fixed income portfolios.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-5|C06-5]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C07-1|C07-1]])
- About 70-75% of AHL's P&L over 25 years came from fixed income, and even since 2010 (after the secular decline in rates ended) fixed income has been the most consistent trend asset across periods and speeds, unlike FX. _[empirical, stated; support: Own recollection of AHL's P&L and consistency across speeds; the figure is not documented here and Niels challenges it as being the 30-40 year rate decline.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C07-3|C07-3]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C07-5|C07-5]])
- Fixed income liquidity is fragmented across many maturities of the same issuer, so execution must tolerate partial fills or substitute bonds and use many brokers, not only big banks. _[institutional, stated; support: Safi was designed to accept partial fills or different bonds on the same curve.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C07-2|C07-2]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C09-5|C09-5]])
- After the GFC transaction reporting and central clearing improved OTC liquidity visibility, but broker relationships remain valuable; in less liquid OTC markets you cannot exit when volatility spikes, so a diversified portfolio must exist before the crisis. _[experience, stated; support: Experience across 2000s to today.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C11-1|C11-1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C11-2|C11-2]])
- CTAs are a crude way to buy convexity because they may not pay off in a given crisis; a tailored Treasury put replication would be more precise. _[theoretical, stated; support: Argument by comparison with an ETF replicating a Treasury put; an investment committee would see a miss as game over.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C11-3|C11-3]])
- Inside an absolute-return bucket a 0.7 Sharpe CTA beside peers at 1.5 lowers dollar returns, so under-allocation is rational unless leverage is available; CTAs need about 1.2-1.3 Sharpe or a tailored crisis role. _[theoretical, stated; support: Bucket arithmetic (private credit, private equity, multi-strat and long-short together at Sharpe 2).]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C12-1|C12-1]])
- Trend following has positive skew and does not harvest a liquidity premium, so it deserves a larger allocation if made easier to hold. _[theoretical, stated; support: Assertion; likely Yav per the ledger.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C13-1|C13-1]])
- For liquid CTAs execution costs about 5bp of Sharpe a year, so it is production work, but in illiquid markets it costs 30-40bp of Sharpe and matters; the real cost is crossing the spread, not delay. _[empirical, stated; support: His blog and two conference talks on execution.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C14-1|C14-1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C14-2|C14-2]])
- Technology tightly integrated with research accelerates and cleans implementation, and technologists spot issues researchers miss; open-sourcing core infrastructure attracts top technologists and improved code quality at AHL. _[experience, stated; support: Weekly AHL tech meetings and the Arctic DB story; he was initially sceptical of open source and was proved wrong.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C16-3|C16-3]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C17-1|C17-1]])
- BlackRock and Fidelity's large AUM targets make a high-Sharpe diversified product hard, risking a perception of CTAs as a 0.5 Sharpe strategy. _[experience, stated; support: Speculation, flagged as pure speculation by the host.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C18-1|C18-1]])
- Around 2011-2013 the pressure on AHL's earnings from the liquid CTA program pushed it to diversify the Evolution program into alternative and OTC markets. _[experience, stated; support: Own recollection (the ledger correction assigns this part to Yav).]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C03-1|C03-1]])

**Chain: Sustained imbalance creates trend (asset-class by asset-class)**
1. Two central banks hold different policy rates → Sustained carry flows in one direction: Central banks tolerate the carry trade (Japan boosting the economy, Australia worried about inflation), so the flow is sustainable. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C08-1|C08-1]])
2. Sustained flow → Positive autocorrelation, trend: Persistent buying pressure; EM currencies with strong carry trend strongly while EURUSD with no gradient does not. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C08-1|C08-1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C08-2|C08-2]])
3. No valuation anchor (crypto) → Permanent imbalance and big trends: No one knows the true value, so price moves of +20% or -50% are not corrected. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C05-2|C05-2]])
4. Equity valuation traders → Weaker equity trend: Value traders inject negative autocorrelation. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C09-2|C09-2]])
5. Demand shock in commodities (AI power demand) → Price imbalance until supply arrives: Power plants and grids take years to build, so price must rise first. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C09-3|C09-3]])
- Evidence: Data observations in FX (EURUSD vs EM) and qualitative reasoning; no statistical test shown (Rob says no significant difference exists).
- Fails when: No sustained imbalance (EURUSD without a rate gradient); Rob thinks the theory is unproven.

**Chain: Why asset-class specific implementation adds Sharpe**
1. Single-market trend Sharpe is about 0.25 → A small implementation gain matters: Raising 0.25 to 0.30 per market adds value after diversification. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-1|C06-1]])
2. Fixed income loads on the Fed and has left skew → Needs cleverer construction and tighter risk control than commodities: Naturally diversified commodities can use equal weight, whereas fixed income markets move together on one factor. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-5|C06-5]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C07-1|C07-1]])
3. Fragmented bond liquidity → Execution must tolerate partial fills or substitute bonds: Many maturities of the same issuer, unlike one stock per company. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C07-2|C07-2]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C09-5|C09-5]])
4. Crypto's right skew → Different risk control: A generalist implementation would leave alpha on the table. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C05-X1|C05-X1]])
- Evidence: Yav's own experience; a rough Sharpe figure from memory.
- Fails when: Rob's counter: a generalised optimiser and risk model that handles higher moments and diversification differences can do the same without separate funds.

**Chain: Execution: patient trading saves more than delay costs**
1. Most CTAs treat execution as a production line → Costs of about 5bp of Sharpe in liquid markets and 30-40bp in illiquid ones: The cost is crossing the spread and taking liquidity, not delay. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C14-1|C14-1]])
2. Delaying the signal a day → Alpha loses only 1-2bp: Trend signals decay slowly, so delay is cheap. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C14-2|C14-2]])
3. Give the desk the raw signal and several days → Partial, patient execution saves spread: Many CTAs already smooth signals for days then force execution within hours, which is the worst of both. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C14-2|C14-2]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C15-1|C15-1]])
4. Pay execution desk a performance fee → Treated as an alpha source: A due-diligence test of whether the manager cares. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C14-X1|C14-X1]])
- Evidence: Cost analysis from his blog; not published numbers here.
- Fails when: Rob: with 4bp of costs (half commissions) only about 2bp could be saved in liquid futures, and giving traders discretion creates a short-horizon alpha desk needing skills that may not exist.

**Chain: Why CTAs are under-allocated**
1. Allocator seeks convexity for an existing portfolio → CTA is a crude, untailored hedge: It may not pay off in a given crisis, leaving the allocator embarrassed before the committee. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C11-3|C11-3]])
2. Allocator seeks return in an absolute-return bucket → A 0.7-Sharpe CTA lowers dollar returns beside 1.5-Sharpe peers: Private credit, private equity, multi-strat and long-short together have Sharpe 2; leverage is not available. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C12-1|C12-1]])
3. Large AUM entrants → Perception of 0.5 Sharpe: A high-Sharpe diversified product is hard at BlackRock and Fidelity scale. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C18-1|C18-1]])
- Evidence: Reasoning from allocator constraints; no survey.
- Fails when: If a CTA reaches about 1.2-1.3 Sharpe or is tailored to a crisis role (his own conditions).

**Decision process**
- [universe] Run asset-class-specific trend products (fixed income and FX/rates in Safi; commodities by a colleague) that investors can mix as building blocks.. Why: The CTA's utility depends on what the allocator holds; implementation differs by asset class. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C05-1|C05-1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-1|C06-1]])
- [portfolio] Equal weight across commodity markets; fixed income built to offset the Fed factor.. Why: Commodities diversify naturally; fixed income loads on one risk factor. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-5|C06-5]])
- [risk] Tighter risk control for fixed income than for naturally diversified commodity books; risk control for crypto specific to right skew.. Why: Left skew similar to multi-strat pods; right skew in crypto. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C07-1|C07-1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C05-X1|C05-X1]])
- [execution] Give the execution desk the raw signal and several days; accept partial fills or different bonds on the same curve; use many brokers.. Why: Crossing the spread is the main cost; delay costs only 1-2bp a day. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C14-2|C14-2]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C15-1|C15-1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C09-5|C09-5]])
- [execution] Pay the execution desk a performance fee.. Why: Aligns the desk with saving the spread, and signals that the firm treats execution as alpha. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C14-X1|C14-X1]])
- [risk] Build a properly diversified portfolio before a crisis in less liquid OTC markets.. Why: Cannot exit when volatility spikes, unlike futures CTAs. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C11-2|C11-2]])
- [research] Pair research and technology side by side; open-source core infrastructure.. Why: Technologists catch issues researchers miss and open source attracts talent. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C16-3|C16-3]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C17-1|C17-1]])

**Evidence style:** Mix of first-principles mechanisms (imbalance, rate gradients, analogies), practitioner experience at AHL, Winton and Safi, and approximate numbers from memory (Sharpe 0.25 per market, 5bp and 30-40bp execution costs, 70-75% of AHL P&L). He gives no statistical tests and acknowledges that his theory is not proven.

**Views at the time**
- (2025-04) BlackRock and Fidelity entering trend following may push the perception of CTAs down toward a 0.5 Sharpe strategy.. Reasoning: Large AUM targets make a high-Sharpe diversified product hard. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C18-1|C18-1]])
- (2025-04) To earn a place among absolute-return peers CTAs need about 1.2-1.3 Sharpe or a tailored role (convexity or crisis alpha) rather than a 0.7 Sharpe generalist.. Reasoning: Allocator bucket arithmetic. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C12-1|C12-1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C11-3|C11-3]])
- (2025-04) Fixed income has been the most consistent trend asset since 2010 despite the end of the secular decline in rates.. Reasoning: Consistency across periods and speeds; FX less so in developed markets. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C07-5|C07-5]])
- (2025-04) AI-driven power demand in the US creates sustained supply-demand imbalance and trend in energy.. Reasoning: Power plants and grids take time to build, so price must adjust. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C09-3|C09-3]])

### Rob Carver (Independent systematic trader, author and blogger; former head of fixed income at AHL (left 2013))
Fingerprint: #approach/trend_following #approach/research_robustness_overfitting #approach/costs_execution #approach/position_sizing_vol_target #approach/portfolio_construction_stacking #approach/replication_indexing
_Speaker note: Speaker mix-ups corrected per ledger: the high-vol share-class remark (C12-2) is attributed to Rob as probable, not Graham; the statement that fixed income dominates CTA P&L (C07-4) belongs to the host, not Rob._

**Worldview premises**
- A standalone CTA should choose the weights across asset classes itself, because it can optimise the portfolio and understands how the building blocks interact; individual units make sense only if the buyer wants crisis alpha or tail hedging. _[theoretical, stated; support: Portfolio-optimisation reasoning.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-4|C06-4]])
- There is no strong statistically significant difference in trend performance across asset classes, and crypto has too short a history to tell; observed gaps (equity weaker than VIX or fixed income) may reflect higher carry in fixed income. _[empirical, stated; support: A table from his latest book; he is sceptical of Yav's imbalance theory ('cute but unproven').]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-2|C06-2]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-3|C06-3]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C08-X1|C08-X1]])
- A single universal risk model that includes higher moments can handle assets with different distributions such as crypto, so separate asset-class funds are not needed. _[theoretical, stated; support: Methodological argument; no demonstration.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-4|C06-4]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C08-X1|C08-X1]])
- Trend following does not suffer the crowding that spread and relative-value trades do: profits so far do not reduce future returns, so the liquidity-alpha link differs for momentum versus reversion strategies. _[theoretical, stated; support: Comparison with spread compression cycles; no data given.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C10-1|C10-1]])
- The mix of reversion players (stat arb in single stocks, curve trades in bonds) versus momentum players in a market may confuse how trendy it is, compared with gold or crude. _[theoretical, stated; support: Speculation ('I would imagine').]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C10-2|C10-2]])
- Futures liquidity has two measures, volume and open interest, which matter differently for building and liquidating positions (Korean stocks: high volume, low open interest; interest rate futures the reverse). _[experience, stated; support: Examples from futures markets.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C10-3|C10-3]])
- With trading costs of about 4bp of Sharpe (half commissions), only about 2bp can be saved through execution effort on liquid futures, so the effort is not worthwhile there; the benefit exists mainly in OTC bonds. _[empirical, stated; support: Back-of-the-envelope calculation for his own system.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C15-2|C15-2]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C15-X1|C15-X1]])
- Giving traders discretion over patient execution turns a CTA into a CTA plus a short-horizon alpha desk, needing skills and technology that may not exist; at 30bp costs Rob would slow the signal further or stop trading the market. _[theoretical, stated; support: Reasoning about organisational scope.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C16-1|C16-1]])
- Speeding up a trend program would add positive skew and tail protection but cost alpha, moving away from where trend works best, and would make it a synthetic option product. _[theoretical, stated; support: Reasoning; no numbers.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C12-3|C12-3]])
- Open-sourcing a trading system forces better code quality, testing and documentation. _[experience, stated; support: Own experience open-sourcing the second version of his trading system.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C17-2|C17-2]])
- High-vol share classes give capital efficiency but few allocators see high vol as good, and many prefer low-vol funds; changing the products may be the lever rather than education. _[institutional, stated; support: Memory of AHL's high-vol share classes; speaker attribution probable (ledger correction).]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C12-2|C12-2]])
- AHL reorganised in 2011 from strategy teams to asset-class teams, and Rob was placed in charge of fixed income, which held a diverse group of assets and strategies. _[experience, stated; support: Own recollection.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C03-R1|C03-R1]])

**Chain: Execution effort is worth little in liquid futures**
1. Total trading cost of about 4bp of Sharpe → Half is commission: For an institution commissions are negligible and cannot be saved. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C15-2|C15-2]])
2. Only about 2bp is bid-ask → Little to save by execution effort: Not worth the effort on liquid markets; useful in weird OTC bonds. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C15-2|C15-2]])
3. Giving traders leeway → CTA becomes CTA plus an alpha desk: A separate alpha strategy with a horizon of hours or days needs skills that might not exist. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C16-1|C16-1]])
- Evidence: His own system's costs; AHL experience of execution windows (an hour per order, none beyond the day).
- Fails when: Costs are about 30bp: then he would slow the signal or stop trading the market.

**Chain: Trend does not decay from crowding the way spread trades do**
1. Spread or RV traders rush in → Spreads compress and everyone exits together: Leverage is needed to hold yield; the cycle is a liquidity cycle. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C10-1|C10-1]])
2. Momentum traders buy what has risen → More room to rise, not less: Past profits do not reduce future returns for trend followers. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C10-1|C10-1]])
- Evidence: Reasoning by contrast; no data.
- Fails when: Not stated; he says the proportion of reversion players can confuse trendiness.

**Decision process**
- [portfolio] A standalone CTA chooses the asset weights through its own optimisation using a universal risk model with higher moments.. Why: Avoids separate funds; handles crypto's distribution. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-4|C06-4]])
- [execution] Does not put much effort into execution in liquid futures; would slow the signal or stop trading a market if costs reach 30bp.. Why: Only about 2bp can be saved. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C15-2|C15-2]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C16-1|C16-1]])
- [research] Tests trend by asset class and liquidity using blog analyses and book tables, and reports no significant liquidity link.. Why: No statistically significant difference found; short history for crypto. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-2|C06-2]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-3|C06-3]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C09-1|C09-1]])
- [research] Open-sources his trading system.. Why: Forces better code quality, testing and documentation. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C17-2|C17-2]])

**Evidence style:** Empirical and sceptical: asks for statistical significance, reports what his own data and book table show, does back-of-the-envelope cost calculations and distrusts theories that are untested.

**Views at the time**
- (2025-04) High-vol share classes may help capital efficiency but allocators prefer low-vol funds, so changing product design is the lever, not education.. Reasoning: Decades of banging heads on education. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C12-2|C12-2]])
- (2025-04) Speeding up trend would add tail protection but cost alpha, so it is not what trend following should be.. Reasoning: Moves away from the speeds where trend works best. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C12-3|C12-3]])

### Graham Robertson (CEO of Man AHL (current AHL leader))
Fingerprint: #approach/trend_following #approach/manager_selection_allocation #approach/liquidity_flows #approach/portfolio_construction_stacking #approach/policy_reaction_central_banks
_Speaker note: Speaks least and several claims captioned to him belong to others (ledger corrections for C03-1, C13-4, C17-1). Claims left to him: the Fed-put/range-bound context, market size versus liquidity, institutions' steady allocations, and the view that more adoption is better._

**Worldview premises**
- Around 2011-2013 traditional liquid trend struggled in range-bound markets as the Fed put emerged, while OTC and alternative markets less affected by it (the Evolution program) kept earning during the CTA winter, so researching new markets with different price drivers added genuine value. _[experience, stated; support: AHL experience; Evolution program results.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C03-1|C03-1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C04-1|C04-1]])
- Market size is not liquidity: industry players that dominate a market and its transaction costs shape how it trades and how trend performs there, so a single 'how liquid' measure is misleading. _[theoretical, stated; support: Years of experience; no data.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C10-X1|C10-X1]])
- Large institutions keep a steady trend-following allocation through good and bad years, but wealth-segment investors and the media largely ignore it (an FT article on handling volatility did not mention trend following), which is where under-allocation lies. _[experience, stated; support: The FT article anecdote; description of institutional behaviour.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C12-X1|C12-X1]])
- Open-sourcing core infrastructure is a way to attract the best technologists. _[experience, stated; support: AHL's experience; Yav was initially sceptical.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C17-1|C17-1]])
- The more investors hold trend strategies the better for the industry, including via large entrants. _[behavioural, stated; support: Brief assertion; no argument.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C18-R1|C18-R1]])

**Chain: Diversifying into OTC markets during the CTA winter**
1. Fed put emerges and markets range-bound (2011-2013) → Traditional liquid trend struggles: Central banks suppress trends in the liquid markets that trend programs trade. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C03-1|C03-1]])
2. OTC and alternative markets less affected by the Fed put → Evolution program keeps earning: Different price drivers from the liquid markets. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C04-1|C04-1]])
3. New markets researched → Genuine value added: Diversification in price drivers helped through the winter. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C04-1|C04-1]])
- Evidence: AHL's own experience in 2011-2013.
- Fails when: Not stated.

**Decision process**
- [universe] Research new, harder-to-access OTC markets for different price drivers.. Why: They were less affected by the Fed put and added value during the winter. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C04-1|C04-1]])

**Evidence style:** Institutional experience and anecdote (AHL history, the FT article); little quantitative support offered in this conversation.

**Views at the time**
- (2025-04) Wealth investors should hold more trend following; making it easier (capital efficiency, higher vol) is the solution.. Reasoning: Trend following is absent from wealth-market commentary. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C12-X1|C12-X1]])
- (2025-04) BlackRock and Fidelity entering the space is welcome: more people holding the strategy is better.. Reasoning: Stated briefly. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C18-R1|C18-R1]])

### Niels Kaastrup-Larsen (Host (Top Traders Unplugged); CTA manager)
Fingerprint: #approach/trend_following #approach/crisis_alpha_convexity #approach/manager_selection_allocation #approach/costs_execution #approach/debt_cycle_long_term
_Speaker note: Argues positions as a CTA manager: challenges the focus on fixed income, rejects high-vol and crisis-alpha framing, and flags fixed income protection. Ledger corrections moved C07-4 and C13-4 to him._

**Worldview premises**
- Fixed income dominates CTA P&L because it is the largest and most liquid sector and enjoyed a 30-40 year favourable trend that has made little recently, so focusing on it risks fitting to the past. _[empirical, stated; support: What he sees from his own vantage point; flagged as speculation ('I'm speculating').]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C07-4|C07-4]])
- Higher-vol share classes did not make CTAs institutional before, and investors who say they prefer high vol give smaller allocations, so more vol will not fix under-allocation. _[experience, stated; support: Conversations with investors; the deleveraging after institutions began investing in about 2000.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C13-2|C13-2]])
- CTAs are not designed to profit from equity crises; good crisis returns result from the strategy and diversification, so selling them as crisis alpha is a mistake and uncorrelated returns are the real value. _[experience, stated; support: His own view; credits the originator of the term crisis alpha (caption 'ktie') while disagreeing with the framing.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C13-3|C13-3]])
- Heavy government bond issuance means trend following should also be considered as protection for fixed-income portfolios, not just equities. _[theoretical, stated; support: His own view, labelled as such.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C13-4|C13-4]])
- Large CTAs spend about 35-40% of research effort on execution. _[empirical, stated; support: Interviews with CTAs in the SG CTA index.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C16-2|C16-2]])
- On a Sharpe-improvement calculation CTAs are completely under-represented in portfolios. _[theoretical, stated; support: Reference to a short paper on the right allocation to a 40/60 portfolio; the host puts the question to Yav, who accepts the premise.]_ ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C11-R1|C11-R1]])

**Evidence style:** Practitioner interviews and challenge questions; notes the sources of his claims (interview series, anecdotes) rather than data.

**Views at the time**
- (2025-04) Trend following should be considered as protection for fixed-income portfolios given heavy government issuance, not only equities.. Reasoning: Bond supply to fund policy changes. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C13-4|C13-4]])
- (2025-04) Do not sell CTAs as crisis alpha; sell uncorrelated returns.. Reasoning: Managers do not design for equity crises. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C13-3|C13-3]])

### Disagreements
- **Asset-class-specific funds versus one multi-asset CTA**: Yav Git: Asset-class-specific products are better building blocks because the CTA's utility is relative to what the allocator holds, and implementation, risk and execution differ by asset class. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C05-1|C05-1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-5|C06-5]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C07-1|C07-1]]); Rob Carver: A standalone CTA should choose weights itself; specialised execution already exists within a multi-asset CTA and a generalised optimiser and risk model can handle different distributions and diversification. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-4|C06-4]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C08-X1|C08-X1]])
- **Do asset classes trend differently, and why?**: Yav Git: Differences come from sustained imbalances: rate gradients in fixed income and EM FX, value traders in equities, slow supply in commodities, no anchor in crypto. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C08-1|C08-1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C09-2|C09-2]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C09-3|C09-3]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C05-2|C05-2]]); Rob Carver: No strong statistically significant difference; equity trend is weaker than VIX or fixed income, possibly because carry is higher in fixed income; crypto history is too short. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-2|C06-2]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-3|C06-3]])
- **Is fixed income's dominance a past regime or a lasting feature?**: Niels Kaastrup-Larsen: Fixed income dominates because it is the biggest sector and had a 30-40 year secular trend and has made little recently, so focusing on it may be optimised to the past. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C07-4|C07-4]]); Yav Git: Even since 2010, after the rate decline ended, fixed income has been the most consistent asset across periods and speeds, unlike FX. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C07-5|C07-5]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C07-3|C07-3]])
- **Does patient execution add value in liquid futures?**: Yav Git: Giving the desk several days and the raw signal saves more than the 1-2bp of alpha lost, even in liquid bond futures such as the 5-year Bobl. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C14-2|C14-2]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C15-1|C15-1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C15-X1|C15-X1]]); Rob Carver: With total costs of about 4bp of Sharpe only about 2bp can be saved; effort is worth it only in OTC bonds, and discretion creates an alpha desk. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C15-2|C15-2]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C16-1|C16-1]])
- **Higher volatility share classes and the crisis-alpha pitch**: Rob Carver: High-vol share classes give capital efficiency but allocators prefer low-vol funds, so product design is the lever. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C12-2|C12-2]]); Niels Kaastrup-Larsen: More vol did not make CTAs institutional and investors give smaller allocations; CTAs should not be sold as crisis alpha. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C13-2|C13-2]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C13-3|C13-3]]); Yav Git: A CTA is a crude hedge for convexity; the issue is Sharpe, and CTAs need about 1.2-1.3 Sharpe or a tailored role. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C11-3|C11-3]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C12-1|C12-1]])
- **Will BlackRock and Fidelity entering trend following help?**: Yav Git: Large AUM targets make a high-Sharpe diversified product hard and risk a perception of a 0.5 Sharpe strategy. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C18-1|C18-1]]); Graham Robertson: The more people hold these strategies the better. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C18-R1|C18-R1]])

### Gaps and conflicts
- Several claims were captioned to the wrong speaker (C03-1, C07-4, C09-1, C12-2, C13-4, C17-1); ledger corrections were applied, but the C12-2 attribution to Rob is only probable. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C03-1|C03-1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C07-4|C07-4]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C09-1|C09-1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C12-2|C12-2]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C13-4|C13-4]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C17-1|C17-1]])
- Yav's imbalance theory is stated as mechanism but no statistical test or table is offered; Rob explicitly calls it unproven and says no significant difference between asset classes exists in his data. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C08-1|C08-1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-2|C06-2]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C08-X1|C08-X1]])
- The 70-75% share of AHL P&L from fixed income is asserted from memory with no period split; Niels notes that most of it came from the 30-40 year rate decline, and Yav replies that consistency continued after 2010 without giving figures. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C07-3|C07-3]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C07-4|C07-4]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C07-5|C07-5]])
- Yav quotes a per-market trend Sharpe of about 0.25 and a gain to 0.30 from asset-class tailoring without a source; his execution claim for the 5-year Bobl is not backed by figures, and Rob's 4bp / 2bp calculation is a back-of-the-envelope estimate for his own system. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C06-1|C06-1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C15-X1|C15-X1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C15-2|C15-2]])
- Yav's commercial interest (a fixed income CTA offered as a building block) and Niels's advocacy for CTAs may colour the asset-class and under-allocation arguments. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C05-1|C05-1]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C12-1|C12-1]])
- Yav says CTAs are a crude hedge for convexity, but Niels says CTAs should not be sold as crisis alpha; neither gives data on how often CTAs paid off in past equity or bond crises. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C11-3|C11-3]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C13-3|C13-3]])
- The claim that large CTAs spend 35-40% of research effort on execution contradicts the common description of execution as a production line costing about 5bp; the conversation does not reconcile them. ([[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C16-2|C16-2]], [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C14-1|C14-1]])

### Forward-looking inputs (reader synthesis)
(reader) Inputs the speakers say lead trend returns: central bank rate gradients (for FX and carry-driven trend in fixed income and EM currencies), the absence of valuation anchors (crypto), supply lags against demand shocks (energy, AI power demand), and the share of value or reversion traders (negative autocorrelation in equities). For allocation: Sharpe relative to the absolute-return bucket (1.2-1.3 needed), and the effect of large-AUM entrants on the perceived Sharpe. Horizons are months to years.

### Reader inferences (not stated by the speakers)
- (reader) The asset-class debate turns on whether the dispersion in trend performance across sectors is signal or noise: Rob asks for significance, Yav argues from mechanism; neither shows a test that would separate them, so the disagreement is about priors, not data.
- (reader) Yav's imbalance theory predicts that trend strength is greatest where an observable persistent flow exists (rate differentials, supply bottlenecks); a testable form is trend Sharpe by carry magnitude, which Rob's remark about carry in fixed income partly supports.
- (reader) The execution disagreement depends on the cost level of the market: both agree that execution matters when costs reach 30-40bp and not when they are 4-5bp, so the real difference is the status of liquid bond futures.
- (reader) The under-allocation arguments (Sharpe beside peers, crude hedge, high vol) explain why Niels's and Yav's allocators hold CTAs mainly for hedging, which Rob's tail-protection comment implies is at odds with trend's natural speed.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | nothing actionable: intro, guests and banter (teaser repeated in C18) |
| C02 | 0 | nothing actionable: guest backgrounds and AHL history |
| C03 | 1 | AHL fixed income team; traditional trend struggled in range-bound Fed put era |
| C04 | 1 | alternative markets helped during CTA winter; AHL culture and open research (no method claims) |
| C05 | 2 | asset-class specific CTA building blocks; crypto trends |
| C06 | 5 | Rob's skepticism on asset class differences; Fed factor in bonds |
| C07 | 5 | asset-class risk and execution differences; fixed income share of CTA P&L |
| C08 | 2 | sustained imbalance theory of trend; FX carry and trend; liquidity intro |
| C09 | 5 | liquidity vs performance; equities value traders; commodities supply; execution in bonds; crowding in trend |
| C10 | 3 | participant mix; volume vs open interest |
| C11 | 3 | OTC liquidity; crisis management; CTAs as crude convexity |
| C12 | 3 | absolute return bucket Sharpe problem; high vol; speed vs skew |
| C13 | 4 | skew and no liquidity premium; vol and crisis alpha; bond context |
| C14 | 2 | execution cost; delay cost; patient execution |
| C15 | 2 | signal buffering; execution savings only in OTC markets |
| C16 | 3 | execution desk alpha; research share; technology; open source start |
| C17 | 2 | open source; code quality; chat jokes (no claims) |
| C18 | 1 | BlackRock and Fidelity entry; wrap-up |
| C19 | 0 | nothing actionable: outro |

## Claims

### C03
- **Graham Robertson** Around 2011-2013 traditional liquid trend struggled in range-bound markets with the Fed put emerging, which put pressure on a firm whose earnings depended on the liquid CTA program.  #mech/policy_reaction _(time-bound view)_
  > traditional Trend was struggling you know things were range bound
  indicator: liquid trend program returns, Fed put · asset: multi · horizon: years · conditions: range-bound markets suppressed by central banks · testable: yes - trend returns by period · confidence: medium
  **Correction (cross-check):** Mixes speakers: the pressure on AHL's earnings from the liquid CTA program and the drive for Evolution diversity is Yav's point; Graham adds the range-bound markets and Fed put. → Around 2011-2013 traditional liquid trend struggled in range-bound markets as the Fed put emerged (Graham); because AHL's earnings were tied to the liquid CTA program, this pushed it to diversify the Evolution program (Yav).
  ^MT029-C03-1
- **Rob Carver** In 2011 AHL reorganised from strategy teams (trend, relative value, global macro) to asset-class teams, and Rob Carver was put in charge of fixed income, a diverse group including cash bonds, credit default swaps and interest rate swaps.  #mech/research_method _(added by map cross-check, time-bound view)_
  > they decided it would make more sense to organize things around asset class and I was put in charge of fixed income
  indicator: organisation by asset class · asset: fixed_income · horizon: years · conditions: AHL from 2011 · testable: no · confidence: high
  ^MT029-C03-R1

### C04
- **Graham Robertson** Alternative and OTC markets less affected by the Fed put (the Evolution program) kept earning during the CTA winter, so researching new markets with different price drivers added genuine value.  #mech/structural_shift
  > diversification in terms of price drivers uh markets was was really helpful to us
  indicator: alternative markets trend program · asset: multi · horizon: years · conditions: liquid trend struggling · testable: yes - alt-market vs liquid trend returns · confidence: medium
  ^MT029-C04-1

### C05
- **Yav Git** Because the utility of a CTA is crisis alpha and convexity relative to what the allocator holds, asset-class-specific trend products (e.g. fixed income only) are better building blocks than one pooled program.  #mech/structural_shift
  > if I'm a bond portfolio holder and I worry about Bond convexity and uh crisis halfa for bonds then what do I care about coffee
  indicator: asset-class-specific CTA building blocks · asset: multi · horizon: years · testable: partly - relates to allocator needs · confidence: medium
  ^MT029-C05-1
- **Yav Git** Crypto trends well because it has no valuation anchor and is in permanent imbalance, so big trends form.  #mech/structural_shift
  > why why crypto currencies actually Trend very well because there is no valuation
  indicator: crypto trend returns · asset: other · horizon: years · testable: partly - short history · confidence: medium
  ^MT029-C05-2
- **Yav Git** Crypto has enormous right skew, so risk control and position management for trend in crypto should differ from other asset classes; a generalist implementation leaves alpha on the table.  #mech/risk_management _(added by opus cross-check)_
  > the way you do the risk anal the risk control on it the way you manage the position um actually needs to be different because it
  asset: other · conditions: assets with strong right skew · testable: yes - compare skew-aware vs standard vol sizing on crypto trend · confidence: medium
  ^MT029-C05-X1

### C06
- **Yav Git** A single market's trend Sharpe is only about 0.25, so tailoring implementation per asset class to raise it to 0.30 adds real value after diversification.  #mech/research_method
  > the average Market sharp Alpha isn't particularly high in Trend it's like you know 25 basis points if we can get it to 30 that really adds value to the investor
  indicator: single-market trend Sharpe about 0.25 · asset: multi · testable: yes - per-market Sharpe · confidence: medium
  ^MT029-C06-1
- **Rob Carver** Rob is skeptical that some asset classes trend better than others; no strong statistically significant difference exists and crypto has too short a history, though equity trend looks weaker than VIX or fixed income, possibly due to higher carry in fixed income.  #mech/research_method
  > I've never really seen a sort of strong statistically significant effect in in performance between different asset classes
  indicator: trend performance by asset class · asset: multi · horizon: years · testable: yes - test asset-class Sharpe differences with error bars · confidence: medium
  ^MT029-C06-2
- **Rob Carver** In Rob's data equity trend does less well than trend in VIX or fixed income, which may relate to carry being naturally higher in fixed income.  #mech/structural_shift
  > Equity trenders is sort of welln doesn't do as well as say I don't know Trend in in vix or Trend in in fxed income
  indicator: trend returns by asset class table · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT029-C06-3
- **Rob Carver** A single universal risk model that includes higher moments can handle assets with different distributions such as crypto, so separate asset-class funds are not needed; a standalone CTA should choose the asset weights itself.  #mech/risk_management
  > that's the sort of thing you can deal with with a kind of universal risk model that just takes higher moments into account
  indicator: risk model with skew and kurtosis · asset: multi · testable: yes - compare universal vs tailored models · confidence: medium
  ^MT029-C06-4
- **Yav Git** Commodity markets diversify naturally (equal weight works), but fixed income has high loading on the Fed as a common factor, so portfolio construction there must be cleverer.  #mech/structural_shift
  > when we come to fixed income we have much bigger issue because there's a very high loading on the FED as a risk factor
  indicator: Fed factor loading across bond markets · asset: rates · testable: yes - factor/PCA analysis of bond returns · confidence: medium
  ^MT029-C06-5

### C07
- **Yav Git** A fixed income trend portfolio has strong left skew, like multi-strat pods, so it needs tighter risk control than naturally diversified commodity portfolios.  #mech/risk_management
  > if you think about uh fixed income portfolio it's got very strong left skew
  indicator: skew of fixed income trend portfolio · asset: rates · testable: yes - measure skew by sector · confidence: medium
  ^MT029-C07-1
- **Yav Git** Bond liquidity is fragmented across many maturities of the same issuer, so execution must tolerate partial fills or substitute bonds, unlike equities.  #mech/risk_management
  > you have multip bonds for the same issuer whereas in equities you have just one one stock for the for a company
  asset: rates · horizon: days · testable: no - practitioner knowledge · confidence: medium
  ^MT029-C07-2
- **Yav Git** About 70-75% of AHL's P&L over the last 25 years came from fixed income, so implementation specific to that sector matters.  #mech/structural_shift
  > about 70 75% of the p&l has come from fixed income
  indicator: sector share of CTA P&L · asset: rates · horizon: years · testable: yes - sector attribution · confidence: medium
  ^MT029-C07-3
- **Rob Carver** Rob argues fixed income dominates CTA P&L because it is the largest and most liquid sector and enjoyed a secular decline in rates for 30-40 years that ended around 2010-2012, and recently made little.  #mech/structural_shift
  > secondly we've had a very nice you know environment overall trend in fixed income for the last 30 40 years
  indicator: secular trend in rates, CTA fixed-income P&L · asset: rates · horizon: years · testable: yes - sector P&L by era · confidence: medium
  **Correction (cross-check):** Wrong speaker: the host (Niels) says 'let me just ask one thing Rob and then I'll let you jump in' and challenges Yav from his CTA vantage point. The dating of the end of the secular rate decline (around 2010) is Yav's reply, not part of this argument. → Niels Kaastrup-Larsen: fixed income dominates CTA P&L because it is the largest, most liquid sector and enjoyed a 30-40 year favourable trend; it has made little recently, so focusing on it risks fitting to the past.
  ^MT029-C07-4
- **Yav Git** Even since 2010 fixed income has been the most consistent asset class for trend across periods and speeds, unlike FX.  #mech/cycle_persistence
  > fixed income has been very consistent not just in terms of um consistency over time so different periods in time also different speeds
  indicator: fixed income trend consistency 2010-2025 · asset: rates · horizon: years · testable: yes - consistency by sector · confidence: medium
  ^MT029-C07-5

### C08
- **Yav Git** Trends arise from sustained imbalances, such as an interest-rate gradient between central banks, which creates sustained carry flows and positive autocorrelation; EURUSD without such gradient shows little trend while EM currencies with high carry trend strongly.  #mech/structural_shift
  > the way I think about what causes trend is sustained imbalance the sustainable imbalance in in the asset class
  indicator: interest rate differential, carry · asset: fx · horizon: years · conditions: large persistent rate gradients · testable: yes - trend strength vs carry/rate differential · confidence: medium
  ^MT029-C08-1
- **Yav Git** Emerging market currencies with strong carry show strong trend, whereas developed-market FX like EURUSD does not trend well.  #mech/structural_shift
  > when you see em currencies where you see very strong carry you see actually very strong Trend as well
  indicator: carry and trend in EM vs DM FX · asset: fx · horizon: years · testable: yes - Sharpe of FX trend by carry bucket · confidence: medium
  ^MT029-C08-2
- **Rob Carver** Rob rejects Yav's case for single-asset-class funds: specialised execution already exists inside a multi-asset CTA, and a generalised optimiser and risk model can handle differing diversification and distributions; he also calls Yav's sustained-imbalance theory of trends unproven.  #mech/research_method _(added by opus cross-check)_
  > you wouldn't have the same person executing cash equities as you would have executing cash Bonds in a CT anyway
  asset: multi · testable: partly - compare generalised vs asset-class-specific implementations · confidence: medium
  ^MT029-C08-X1

### C09
- **Rob Carver** Rob's blog found no correlation between market liquidity and trend performance, though Yav argues the wrong liquidity is measured (the imbalance matters) and liquidity mainly caps diversification and capacity.  #mech/research_method
  > looking at liquidity and seeing if it correlates with performance and it doesn't
  indicator: market liquidity vs trend performance · asset: multi · horizon: years · testable: yes - blog test · confidence: medium
  **Correction (cross-check):** Speaker: Yav Git says this, summarising Rob's blog, and adds his own objection; Rob does not speak here. → Yav Git: Rob's blog found no correlation between market liquidity and trend performance; Yav agrees but argues the wrong liquidity is measured (the imbalance matters), and liquidity mainly limits diversification and capacity.
  ^MT029-C09-1
- **Yav Git** Equity trend is weaker because value traders add negative autocorrelation.  #mech/crowding_positioning
  > the thing that really harms Equity is valuation and the fact that value Traders inject negative autocorrelation which makes it very difficult for Trend followers to harvest Trend inequity
  indicator: equity trend Sharpe, value investor activity · asset: equities · horizon: years · testable: partly - hard to measure value-trader share · confidence: medium
  ^MT029-C09-2
- **Yav Git** In commodities, supply takes time to meet demand shocks (e.g. AI power demand), creating sustained price imbalance and trend; liquidity should be judged by physical versus financial market size.  #mech/structural_shift _(time-bound view)_
  > if energy uh requirements in the US because of AI grows 5% next year it will take time to build power plants and to get to upgrade the electricity grid and price needs to meet that demand
  indicator: supply-demand imbalance, physical vs financial market size · asset: commodities · horizon: years · testable: partly · confidence: medium
  ^MT029-C09-3
- **Yav Git** Liquidity limits how much risk can go into small diversifying markets, so one must either accept small size or cap capacity to keep diversification.  #mech/risk_management
  > but generally we would like to think about liquidity as a way for us to manage diversity and it's a restriction for us
  indicator: market liquidity, capacity · asset: multi · testable: no - qualitative · confidence: medium
  ^MT029-C09-4
- **Yav Git** Better execution in fixed income comes from understanding who holds inventory and using many brokers rather than only big banks; systems should accept partial fills or different bonds on the same curve.  #mech/risk_management
  > is really understanding who is the one who is actually holding the inventory who's the biggest players in that in that market
  indicator: dealer inventory, multiple brokers · asset: rates · horizon: days · testable: partly - execution data · confidence: medium
  ^MT029-C09-5

### C10
- **Rob Carver** Trend following does not suffer the crowding that spread and RV trades do (profits do not reduce future returns), so the liquidity-alpha link differs for momentum versus reversion strategies.  #mech/crowding_positioning
  > the more the market goes up the more opportunity there is for the market to go up more
  indicator: momentum vs reversion trade crowding · asset: multi · testable: partly · confidence: medium
  ^MT029-C10-1
- **Rob Carver** The proportion of reversion players (stat arb in single stocks, curve trades in bonds) versus momentum players in a market may confuse trendiness, compared with gold or crude.  #mech/crowding_positioning
  > I would imagine in like single stock equities there's a lot more people doing you know statar type strategies and playing reversion trades
  indicator: share of reversion traders by market · asset: multi · testable: partly - participant composition hard to measure · confidence: low
  ^MT029-C10-2
- **Rob Carver** Futures liquidity has two measures, volume and open interest (e.g. Korean stocks high volume low open interest, interest rate futures the reverse), which matter differently for position building and liquidation.  #mech/research_method
  > there are two measures of liquidity right there's volume and open interest and you can have markets with incredibly high volume
  indicator: volume vs open interest · asset: multi · testable: yes - liquidity metrics · confidence: high
  ^MT029-C10-3
- **Graham Robertson** Market size is not liquidity: the industry players who dominate a market and its transaction costs shape how it trades and how trend performs there, so a single 'how liquid' measure is misleading.  #mech/research_method _(added by opus cross-check)_
  > liquidity is a term that's often misused you can talk about the size of the market and people will call that liquidity of the market but it's not necessarily the same thing
  indicator: market size vs transaction costs vs participant mix · asset: multi · testable: partly - needs participant-composition data · confidence: medium
  ^MT029-C10-X1

### C11
- **Yav Git** After the GFC transaction reporting and central clearing of swaps improved OTC market liquidity visibility, though broker relationships remain valuable.  #mech/structural_shift
  > I think things after GFC have become a lot better in terms of reporting of transactions
  indicator: OTC transaction reporting, clearing · asset: rates · horizon: years · testable: no - structural · confidence: medium
  ^MT029-C11-1
- **Yav Git** In less liquid OTC markets you cannot exit when vol spikes as futures CTAs do, so a properly diversified portfolio must be built before the crisis.  #mech/risk_management
  > on day one you're just stuck with the position and you have to manage that risk
  indicator: portfolio diversification before crisis · asset: multi · horizon: days · conditions: illiquid OTC markets · testable: partly · confidence: medium
  ^MT029-C11-2
- **Yav Git** CTAs are a crude way to buy convexity or crisis alpha because they may not pay off in a given crisis; a tailored Treasury put replication would be more precise.  #mech/risk_premium
  > then ctas are very crude fuzzy way to get convexity right because it is really not tailored to my underlying portfolio
  indicator: CTA payoff in crises · asset: multi · horizon: years · testable: yes - CTA returns in crisis episodes · confidence: medium
  ^MT029-C11-3
- **Yav Git** If one uses the mathematics of improving Sharpe, CTAs are completely under-represented in portfolios (a short paper by Graham on the right allocation to add to a 40/60 portfolio is cited), though CTAs remain difficult to allocate to.  #mech/new _(added by map cross-check)_
  > we're completely under represented right
  indicator: CTA allocation in 40/60 portfolios · asset: multi · horizon: years · conditions: On a Sharpe-improvement calculation · testable: yes · confidence: medium
  ^MT029-C11-R1

### C12
- **Yav Git** Inside an absolute-return bucket a 0.7 Sharpe CTA beside peers at 1.5 lowers dollar returns, so under-allocation is rational unless leveraged; CTAs need about 1.2-1.3 Sharpe or a tailored crisis role.  #mech/behavioral
  > adding risk adding a CTA is actually very detrimental in terms of dollar terms now it will be great from a sharp point of view and if you could leverage then that will add value
  indicator: Sharpe of CTA vs absolute return peers · asset: multi · horizon: years · testable: yes - portfolio math · confidence: medium
  ^MT029-C12-1
- **Graham Robertson** High-vol share classes give capital efficiency, but many allocators do not value them and prefer low-vol funds, so product design is the lever.  #mech/behavioral
  > the problem is I guess not that many people necessarily understand that the High Vol is a good thing
  indicator: volatility target of share class · asset: multi · testable: no - preference · confidence: medium
  **Correction (cross-check):** Probable wrong speaker: the high-vol share class remark ('I remember back in the day and I'm sure it's still the case AHL was offering High Vol share classes') is by a former AHL person and continues into Rob's 'I like Yav saying...'; it is most likely Rob Carver, not Graham (current AHL CEO). → Rob Carver (probable): high-vol share classes give capital efficiency, but few allocators see high vol as good and many prefer low-vol funds; changing the products may be the lever.
  ^MT029-C12-2
- **Rob Carver** Speeding up a trend program would give more positive skew and tail protection but at the cost of alpha, moving away from where trend works best.  #mech/risk_management
  > something kind of more tail proty would be to speed it up and give it more positive skew um and and then that would be probably at the cost of alpha
  indicator: trend speed, skew · asset: multi · direction: faster models more skew, less alpha · horizon: months · testable: yes - skew and Sharpe by lookback · confidence: medium
  ^MT029-C12-3
- **Graham Robertson** Large institutions keep a steady trend-following allocation through good and bad years, but wealth-segment investors and the media largely ignore it (an FT article on handling volatility did not mention trend following), which is where under-allocation lies.  #mech/behavioral _(added by opus cross-check)_
  > larger investors tend to have an allocation to Trend following thick and thin
  asset: multi · horizon: years · testable: no - anecdotal · confidence: medium
  ^MT029-C12-X1

### C13
- **Yav Git** Trend following has positive skew and does not harvest a liquidity premium, so it deserves a larger allocation if made easier to hold.  #mech/risk_premium
  > it's one of the only strategies which has you know the positive skew and it's not actually harvesting liquidity premium
  indicator: skew of trend following · asset: multi · horizon: years · testable: yes - skewness and premia exposure · confidence: high
  ^MT029-C13-1
- **Niels Kaastrup-Larsen** Higher-vol share classes did not make CTAs institutional before and investors who prefer high vol give smaller allocations, so more vol will not fix under-allocation.  #mech/behavioral
  > I remember the times when we had more V in our industry and that actually didn't make it institutional at all
  indicator: vol targets and allocation size · asset: multi · horizon: years · testable: no - anecdotal · confidence: medium
  ^MT029-C13-2
- **Niels Kaastrup-Larsen** CTAs are not designed to profit from equity crises; good crisis returns result from the strategy and diversification, so selling them as crisis alpha is a mistake and uncorrelated returns are the real value.  #mech/structural_shift
  > generally speaking I don't think we as managers are designing our uh products to make money specifically when there is an equity crisis
  indicator: CTA returns in equity crises · asset: multi · horizon: years · testable: yes - crisis-period returns · confidence: medium
  ^MT029-C13-3
- **Graham Robertson** Heavy fixed income issuance to fund government changes means trend following should be considered as protection for bond portfolios, not just equities.  #mech/fiscal_debt _(time-bound view)_
  > maybe people start need to start thinking about Trend following in the context of a fixed income portfolio not just an equity uh portfolio
  indicator: trend following as bond hedge · asset: rates · horizon: years · testable: partly - bond-trend correlation · confidence: low
  **Correction (cross-check):** Wrong speaker: Niels says this ('that's just my own view here') and moves to the next topic in the same turn. → Niels Kaastrup-Larsen: heavy government bond issuance to fund policy changes means trend following should also be considered as protection for fixed-income portfolios, not just equities.
  ^MT029-C13-4

### C14
- **Yav Git** For liquid CTAs execution costs about 5bp of Sharpe per year, so execution is production work; for illiquid markets it can cost 30-40bp of Sharpe and matters.  #mech/risk_management
  > it cost us a maybe five basis points of sharp per per year
  indicator: execution cost in Sharpe basis points · asset: multi · horizon: years · testable: yes - cost accounting · confidence: high
  ^MT029-C14-1
- **Yav Git** Delaying signals by a day costs only 1-2bp, so execution desks should be given several days to trade patiently, using partial execution to avoid crossing the spread, which is the real cost.  #mech/risk_management
  > if you lag your strategy suppose you say okay I'm going to lag my signals by a day you find that actually your Alpha doesn't Decay that much you will maybe lose one or two basis points
  indicator: alpha decay from lagging signals, spread crossing · asset: multi · direction: slower, patient execution · horizon: days · testable: yes - lag test and execution backtest · confidence: high
  ^MT029-C14-2
- **Yav Git** Due-diligence test: asking whether a CTA pays its execution desk a performance fee reveals whether it treats execution as an alpha source or as a production line.  #mech/research_method _(added by opus cross-check)_
  > do you pay performance fee to your execution desk
  asset: multi · testable: no - due-diligence heuristic · confidence: medium
  ^MT029-C14-X1

### C15
- **Yav Git** Many CTAs smooth signals for days then force execution within hours; better to give the desk the raw signal and tell it to trade slowly, saving costs.  #mech/risk_management
  > you will take a signal and you will sit on it for 5 days because you're buffering it and then ex insist that execution desk execute it within half a day
  indicator: signal buffering vs execution window · asset: multi · horizon: days · testable: yes - compare smoothing vs patient execution · confidence: medium
  ^MT029-C15-1
- **Rob Carver** With trading costs of about 4bp Sharpe (half commissions), only about 2bp can be saved through execution effort on liquid futures, so effort is not worthwhile there; benefit exists mainly in OTC bonds.  #mech/risk_management
  > and half of that's commission which for an institution is negligible right so only only two basis of points of that is Bid ask so I could only save two basis points of shot
  indicator: trading cost 4bp Sharpe · asset: multi · testable: yes - cost decomposition · confidence: high
  ^MT029-C15-2
- **Yav Git** Yav claims patient execution saves more than the alpha lost from delay even in liquid bond futures (e.g. 5-year Bobl), not only in illiquid OTC bonds; Rob disagrees for liquid futures.  #mech/risk_management _(added by opus cross-check)_
  > the benefits of waiting far outweighs the loss of alpha even for those markets
  indicator: execution cost vs signal-delay alpha decay · asset: rates · horizon: days · conditions: disputed for liquid futures · testable: yes - compare spread savings from passive fills vs alpha decay from delay · confidence: high
  ^MT029-C15-X1

### C16
- **Rob Carver** Giving traders discretion over patient execution turns a CTA into CTA plus a short-horizon alpha desk, requiring skills that may not exist; with 30bp costs Rob would slow the signal further or stop trading the market.  #mech/risk_management
  > fund has become a CTA plus a he like like a trading desk with a horizon of a few hours
  indicator: execution desk alpha · asset: multi · horizon: days · testable: partly · confidence: medium
  ^MT029-C16-1
- **Niels Kaastrup-Larsen** Large CTAs spend about 35-40% of research effort on execution.  #mech/research_method
  > we probably spend 35 to 40% of all our research just on execution
  indicator: research allocation to execution · asset: multi · testable: no - interview statement · confidence: medium
  ^MT029-C16-2
- **Yav Git** Technology tightly integrated with research accelerates and cleans implementation and technologists spot issues researchers miss.  #mech/research_method
  > technology um when it is really married to the research when you work side by side um is really uh a great boost to what we do
  asset: multi · testable: no - organisational practice · confidence: medium
  ^MT029-C16-3

### C17
- **Graham Robertson** Open-sourcing foundations (e.g. Arctic DB) attracts top technologists and improved code quality at AHL.  #mech/research_method
  > open source is good uh in fact the we open source a lot of the basic um Foundation of our um of what we do
  asset: multi · testable: no - organisational · confidence: medium
  **Correction (cross-check):** Speaker mostly wrong: Graham only says open source attracts the best technologists; the Arctic DB story and 'we open source a lot of the basic foundation' are Yav Git's (he was the initial sceptic at AHL). → Graham Robertson and Yav Git: open-sourcing core infrastructure (e.g. Arctic DB) attracts top technologists and improved code quality at AHL; Yav says he was first sceptical and was proved wrong.
  ^MT029-C17-1
- **Rob Carver** Open-sourcing a trading system forces better code quality, testing and documentation.  #mech/research_method
  > the discipline of knowing that lots of other people are going to look at your code it makes you more likely to to write good quality code and and you know test and document it properly
  asset: multi · testable: no · confidence: medium
  ^MT029-C17-2

### C18
- **Yav Git** BlackRock and Fidelity's large AUM targets make a high-Sharpe diversified product hard, risking a perception of CTAs as a 0.5 Sharpe strategy.  #mech/crowding_positioning _(time-bound view)_
  > but I think it will be very difficult to create a popular Diversified Pro product um at the AUM that they they will be targeting
  indicator: capacity vs Sharpe of mass-market trend products · asset: multi · horizon: years · testable: partly - capacity curves · confidence: medium
  ^MT029-C18-1
- **Graham Robertson** From Graham Robertson's perspective, the more investors hold trend-following strategies in their portfolios the better, including through the entry of firms like BlackRock and Fidelity.  #mech/new _(added by map cross-check)_
  > the more people have these strategies within their portfolios the better
  indicator: trend-following adoption · asset: multi · horizon: years · conditions: Large asset managers launching trend products · testable: no · confidence: medium
  ^MT029-C18-R1

