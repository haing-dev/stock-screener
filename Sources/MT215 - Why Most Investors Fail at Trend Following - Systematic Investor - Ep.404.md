---
source_id: MT215
title: "Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404"
date: 2026-06-14
channel: "Top Traders Unplugged"
url: 
words: 13221
claims: 68
added_by_crosscheck: 16
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Niels Kaastrup-Larsen (host, Top Traders Unplugged; transcript spells 'Neil Castro Lson')", "Eric Crittenden (founder, Standpoint, managed futures plus equities mutual fund; transcript spells 'Critan')", "Andrew Beer (managed futures ETF manager, DBi)"]
tags: [source, layer0]
---
# Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404

**Speakers:** Niels Kaastrup-Larsen (host, Top Traders Unplugged; transcript spells 'Neil Castro Lson'); Eric Crittenden (founder, Standpoint, managed futures plus equities mutual fund; transcript spells 'Critan'); Andrew Beer (managed futures ETF manager, DBi)

**Summary:** Systematic Investor Ep.404 (mid-June 2026): trend followers Eric Crittenden and Andrew Beer on managed futures ETFs, the trend-plus-equities combination, and why allocators fail at trend. Themes: behavioral reasons investors abandon trend, simple blunt rules beat complex ones out of sample, correlation-based optimization hurts, indices understate larger managers, sustainable Sharpe ratios are low for single strategies. Trend profits come from early, contrarian-looking entries enforced by algorithmic discipline; blend it with other assets.

**Approach:** trend following, managed futures ETFs, trend plus equities, portable alpha / return stacking, simplicity vs complexity, behavioral allocator failure, Sharpe ratio realism, CTA indices

**Cross-check completeness estimate of first read:** 0.85 - first reader captured the core trend, simplicity, Sharpe and behavioral arguments well; missed ETF mechanics detail, June 2026 monthly performance, index composition and ranking evidence, allocator segmentation and several product-design remarks.

## Argument map

**Episode thesis:** Eric Crittenden and Andrew Beer argue that trend plus equities is statistically close to an obvious combination but investors fail at it for behavioural reasons (benchmark-relative loss aversion, chasing winners, regret when equities double), so the product must be built to be held: a low-fee trend program at equal volatility contribution with equities, in a wrapper advisors can use. They also argue that simple, blunt trend rules beat complex ones out of sample (most trend returns map to 4-6 principal components; correlation-based optimisation hurt live), that trend profits come from early, uncomfortable, contrarian-looking entries enforced by algorithmic discipline ('contrarian tactical alpha'), and that sustainable Sharpe ratios of single strategies are low (about 0.3-0.4), so blending is the route to higher Sharpe. Niels pushes back with the case for large, complex managers (ISAM), the way CTA indices understate the best trend managers, and diligence on whether managers have their own money in the product.

### Eric Crittenden (Founder of Standpoint; manager of a managed futures plus equities mutual fund launched January 2020 (in the 29th year of his career))
Fingerprint: #approach/trend_following #approach/portfolio_construction_stacking #approach/behavioral_sentiment #approach/research_robustness_overfitting #approach/position_sizing_vol_target #approach/diversification_risk_parity #approach/crisis_alpha_convexity #approach/costs_execution
_Speaker note: Name transcribed 'Eric Critan' in captions. Statements are first-person about his fund, so attribution is secure._

**Worldview premises**
- Allocators buy what is up and sell when it stalls, and benchmark-relative loss aversion (prospect theory against the S&P 500 or 60/40) makes it nearly impossible to keep them in managed futures beyond a few quarters, even though adding it improves returns, volatility and drawdowns. _[behavioural, stated; support: Two decades of allocator experience in long/short equity and managed futures]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C07-1|C07-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C07-2|C07-2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C07-3|C07-3]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C07-X1|C07-X1]])
- A diversifier that raises returns and lowers risk at once does not fit style boxes (large cap growth, fixed income active), which complicates distribution. _[institutional, stated; support: Own distribution experience]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C08-1|C08-1]])
- Complex trend programs look better in hindsight and in presentations, but simple durable (blunt) rules hold up much better out of sample and in unprecedented events. _[experience, stated; support: Built complex and 'embarrassingly simple' programs; April 2020 negative crude oil example]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C12-2|C12-2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C12-3|C12-3]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C13-R1|C13-R1]])
- Most trend follower returns map to 4-6 principal components (energies, fixed income, grains, US dollar), about 90/10 Pareto, so adding many markets adds little; niche markets are nice-to-haves. _[empirical, stated; support: His own research over 20 years; attribution analysis]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C13-1|C13-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C03-4|C03-4]])
- Trend profits arrive when volatility and correlations rise; low-volatility, low-correlation periods bring whipsaws and few profits. _[empirical, stated; support: Experience; he appeals to Niels and Andrew as people who know this from long exposure to trend following]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C13-3|C13-3]])
- Trend profits come from algorithmic discipline that forces uncomfortable positions before they are socially safe; 50-70% of trades lose so losses must be small and winners held for years. _[experience, stated; support: Short equities 2002 and 2008, short energy before COVID, long cocoa up 400%, short natural gas for eight years, gold after 20 dead years]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C18-3|C18-3]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C18-4|C18-4]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C18-5|C18-5]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C19-1|C19-1]])
- A good single strategy sustains a Sharpe ratio of only about 0.3-0.4; combining such strategies gets nearer to 1, though sustainability is uncertain. _[empirical, stated; support: Sharpe vs track-record-length scatter plots of hedge funds and funds from many databases (since about 2008-09): none above 1 at 10 years, about 0.65 at 15-20 years]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C17-1|C17-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C17-2|C17-2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C17-3|C17-3]])
- Trend is hard to live with day to day, so blending it with other assets in a multi-asset product helps investors stay invested. _[behavioural, stated; support: Personal experience]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C19-2|C19-2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C07-4|C07-4]])

**Chain: Why allocators abandon managed futures**
1. Standalone managed-futures line item with its own monthly P&L → Constant questions from clients, regulators and compliance: Visible line-item risk invites micromanagement ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C07-X1|C07-X1]])
2. Benchmark-relative evaluation (S&P or 60/40) and loss aversion → Abandonment within a few quarters despite agreeing with the math: Prospect theory: losses weigh twice gains and relative to what others stare at ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C07-2|C07-2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C07-1|C07-1]])
3. Trend embedded with equities in one low-fee product → A set-and-forget holding with equity comfort and convexity to fill drawdowns: Owning large equity is comfortable when paired with a long-convexity trend component ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C07-4|C07-4]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C07-X2|C07-X2]])
- Evidence: Career observation of allocators; no data presented on holding periods.
- Fails when: Products fit no style box; complexity remains an obstacle to distribution.

**Chain: Why correlation-based optimisation hurt in live trading**
1. Overweighting uncorrelated markets via correlation, cointegration or copula optimisation → Lower profit and understated risk in live trading: Reality (crude oil, gold, etc.) behaves differently from the spreadsheet ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C13-2|C13-2]])
2. Trend profits concentrated in high-volatility, high-correlation periods → Diluting correlated winners and overweighting uncorrelated markets reduces gains when it matters: Money is made when correlation rises ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C13-3|C13-3]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C13-2|C13-2]])
- Evidence: Two years of his own research ('wasted two years'); anecdotal, no numbers given.
- Fails when: Not stated.

**Chain: Equal volatility contribution of trend and equities**
1. Not knowing which sleeve will do better → Equal volatility contribution (e.g. 100% of an 8%-vol managed futures program plus 50% of 16%-vol stocks): Neutral risk allocation between two close-to-uncorrelated return sources ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C08-2|C08-2]])
2. Choice of overall volatility → Competitive but survivable: Double risk invites VaR and compliance stress; half risks lagging inflation and fees ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C09-1|C09-1]])
- Evidence: Personal comfort and product-market fit; no optimisation presented.
- Fails when: New entrants run higher volatility products for their own psychological and market reasons.

**Decision process**
- [sizing] Equal volatility (risk) contribution from equities and trend/managed futures (100% of an 8%-vol program with 50% in 16%-vol stocks).. Why: The better performer is unknown. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C08-2|C08-2]])
- [risk] Pick a volatility level that is competitive but survivable.. Why: Double risk brings compliance stress; half risks lagging inflation and fees. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C09-1|C09-1]])
- [signal] Use simple, durable, blunt trend rules and avoid correlation, cointegration or copula-based reweighting.. Why: Complex rules look better in sample but fail out of sample. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C12-2|C12-2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C13-2|C13-2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C13-R1|C13-R1]])
- [universe] Reduce dimensionality (skip platinum, Japan, palm oil) when needed because they do not matter much for performance.. Why: Performance attribution shows little contribution; trend returns load on 4-6 components. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C03-4|C03-4]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C13-1|C13-1]])
- [execution] Hold losses small and winners for years, with algorithmic discipline to take uncomfortable positions.. Why: 50-70% of trades lose; payoff comes from rare long trends. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C18-3|C18-3]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C18-4|C18-4]])
- [other] Package the trend with low-fee, tax-efficient equity exposure, avoid hedge-fund fees and aim for something he would set and forget with his own money.. Why: Product-market fit and behavioural holdability. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C07-X2|C07-X2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C04-1|C04-1]])
- [portfolio] Combine multiple 0.3-0.4 Sharpe sources (equities, managed futures, tail hedging) to approach a Sharpe near 1.. Why: Single strategies cannot sustain high Sharpe. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C17-3|C17-3]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C17-2|C17-2]])

**Evidence style:** Practitioner experience with live capital ('simple beats complex out of sample'), anecdotes from specific trades, and one self-built cross-sectional hedge fund dataset (Sharpe vs track record). Distrusts academic elegance and spreadsheet results; no formal backtests shown.

**Views at the time**
- (2026-06 (recorded mid-June; upload 2026-06-14)) Mid-2026 has dislocation and uncertainty, which is fertile ground for trends and risk premia to collect.. Reasoning: Many trends and risk premia over the past 12-14 months since the April 2025 tariff drawdown. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C01-1|C01-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C01-2|C01-2]])
- (2026-06) The April 2025 tariff-tantrum drawdown was hard for trend followers, followed by 12-14 months of smooth, profitable trends and risk premia; this cannot be counted on forever.. Reasoning: Own experience. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C01-2|C01-2]])
- (2026-06) ETF distribution matters: many new advisors and individuals are ETF-only; market makers are building infrastructure so a diversified international futures portfolio could run in an ETF.. Reasoning: Evidence of improving market-maker infrastructure. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C03-3|C03-3]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C04-1|C04-1]])

### Andrew Beer (Manager of a managed futures replication ETF (DBi); product and allocator-behaviour voice)
Fingerprint: #approach/replication_indexing #approach/trend_following #approach/behavioral_sentiment #approach/manager_selection_allocation #approach/costs_execution #approach/portfolio_construction_stacking #approach/structural_themes
_Speaker note: Ledger corrected C15-1: the remark that big institutions do not pay the fees embedded in the SG CTA index is Beer's; the remark that indices drag in the biggest managers' blowups is Niels's._

**Worldview premises**
- Managed futures plus equities is statistically about as obvious a combination as exists (1+1 equals 3 or 4), and model allocators now want a third leg of the asset allocation stool. _[empirical, stated; support: Papers (Crochet at Fidelity, ManHL), many podcasts, BlackRock's $4bn single-day inflow]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C06-2|C06-2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C06-1|C06-1]])
- Since 2022 bonds stopped diversifying stocks, so ETF model allocators with only stocks and bonds look for a 3-5% alternative allocation; advisors say they want diversification but often do not act. _[empirical, stated; support: Allocator conversations]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C10-1|C10-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C10-2|C10-2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C10-X1|C10-X1]])
- Allocators fear regret: if equities double and the diversifier gains only 20%, they are blamed; blending trend with 50% equity avoids that. _[behavioural, stated; support: Allocator interviews (Eric's insight)]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C10-3|C10-3]])
- Capital-efficiency-focused allocators do not want to sell stocks, which drives demand for full portable-alpha products. _[behavioural, stated; support: Observation]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C11-1|C11-1]])
- Most alternative products are built by distribution teams chasing flows with no ownership over five years; average hedge fund mutual funds earned 2-3% a year after about 200bp fees, worse than random. _[institutional, stated; support: Industry statistic quoted from memory]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C09-2|C09-2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C09-3|C09-3]])
- Large firms launch trend products as a one-sided option, so allocators must vet the team's modelling credibility over 5-10 years; credible entrants hire experienced trend teams. _[institutional, stated; support: Examples of JP Morgan's quant team and Fidelity's hire of Rob Crochet]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C12-1|C12-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C11-X1|C11-X1]])
- Trend profits may come from clusters (energy, metals, equities) moving together rather than 70 independent instruments, and no well articulated evidence-based counter to this exists. _[empirical, stated; support: Crochet's simple 12-month lookback model (Sharpe about 1 at 12.5% vol; about 800bp had to be removed to resemble CTA universe returns)]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C14-1|C14-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C14-3|C14-3]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C14-4|C14-4]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C14-R1|C14-R1]])
- Published research hides discarded models, so readers see only final results (selection bias). _[theoretical, stated; support: Reading papers as a non-quant]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C14-2|C14-2]])
- Large managers are efficient: no hidden pool of high-Sharpe large trend managers exists; his simple replication has outperformed all but ISAM since mid-2016, and ranks third against current index constituents. _[empirical, stated; support: Own ETF's track record vs peer group (selection bias acknowledged)]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C16-1|C16-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C15-X2|C15-X2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C16-X1|C16-X1]])
- Trend alpha is lumpy: Dunn's very large 2022 gain carried its numbers for a decade. _[empirical, stated; support: One example]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C16-3|C16-3]])
- Managed futures is a dynamic tactical asset class; the money is made by early, uncomfortable entries (contrarian tactical alpha), not by joining crowded trends late, and the space needs better language. _[theoretical, stated; support: Trades: crude oil in January after declines, gold at 2200 after a decade of nothing, shorting Treasuries at 70bp in September 2020]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C17-5|C17-5]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C18-1|C18-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C18-2|C18-2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C18-X1|C18-X1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C17-R1|C17-R1]])
- ETF market makers hedge via the underlying, so ETFs on deep, liquid instruments trade within a penny or two of NAV while illiquid underlyings widen spreads; advisors fear avoidable visible mistakes. _[institutional, stated; support: Product design experience]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C05-1|C05-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C05-2|C05-2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C04-X1|C04-X1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C05-X1|C05-X1]])
- Allocators split into those who want a one-stop multi-strategy ETF for the alternatives bucket and those who assemble building blocks; the alternatives market is hundreds of submarkets, so a product should pick one allocator segment. _[institutional, stated; support: Product strategy]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C05-X2|C05-X2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C10-X1|C10-X1]])
- Large institutions do not pay the fees embedded in the SG CTA index, so index Sharpe ratios do not describe what they earn. _[empirical, stated; support: Institutional fee knowledge]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C15-1|C15-1]])

**Chain: Why allocators fail to hold diversifiers and how a blend solves it**
1. Equities double over 3 years while a diversifier gains 20% → Allocator is blamed even though diversification worked: Regret and benchmark-relative judgement ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C10-3|C10-3]])
2. Trend blended with 50% equity in one product → Allocator avoids the regret: The package still participates in equity gains ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C10-3|C10-3]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C11-1|C11-1]])
3. Advisors say they want diversification but do not act → Need to understand real decision-making rather than stated preferences: Actions do not follow words ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C10-2|C10-2]])
- Evidence: Conversations with allocators; BlackRock's $4bn single-day flow as demand evidence.
- Fails when: Not stated.

**Chain: Where trend profits come from: clusters and early contrarian entries**
1. Simple 12-month lookback model with Sharpe about 1 at 12.5% vol → CTA universe returns are far lower (about 800bp removed to resemble them): Possible reasons: short-term models exit before moves; risk controls cut positions ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C14-1|C14-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C14-4|C14-4]])
2. Profits from clusters (energy, metals, equities) moving together → Fewer independent bets than 70 instruments suggest: Oil, gold and equity complexes drag peers with them ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C14-3|C14-3]])
3. Early entries after long declines or dead markets (crude in January, gold at 2200, short Treasuries in 2020) → Alpha that is uncomfortable but not late-party trend following: Entries before consensus is safe ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C17-5|C17-5]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C18-1|C18-1]])
- Evidence: Crochet's simple-model paper; named trades; own ETF's relative track record since mid-2016.
- Fails when: Beer concedes it relies on others' quant work and no counter evidence yet; selection bias in published research.

**Chain: ETF microstructure and advisor adoption**
1. ETF holds deep liquid instruments → Market makers hedge easily and keep price within a penny or two of NAV: Less risk of moving the underlying ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C05-1|C05-1]])
2. Tight price to NAV → Advisors from the mutual fund world avoid visible mistakes and adopt it: Fear of a market order moving price 50bp ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C05-X1|C05-X1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C04-X1|C04-X1]])
3. Large model allocators use ETF desks, blocks and dark pools → Easy movement of large dollars is a selling point: Efficient execution at size ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C05-2|C05-2]])
- Evidence: Product experience.
- Fails when: Illiquid underlyings widen spreads.

**Decision process**
- [universe] Replication ETF built from the deepest, most liquid markets (around 10 instruments) to keep market makers within a penny or two of NAV.. Why: Liquid underlyings leave market makers no excuse; advisors dislike execution mistakes. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C05-1|C05-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C05-X1|C05-X1]])
- [other] Target one allocator segment (ETF model allocators needing a 3-5% diversifier) rather than the whole addressable market.. Why: The alternatives market is hundreds of submarkets with different needs. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C10-1|C10-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C10-X1|C10-X1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C05-X2|C05-X2]])
- [research] Vet a new trend entrant by the experience of the team and whether the product is a one-sided option for the firm.. Why: Large firms can close products if they fail. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C12-1|C12-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C11-X1|C11-X1]])
- [other] Use narrative framing (contrarian tactical alpha) to bridge the gap between statistics and allocators' actions.. Why: Allocators need a simple story; AI assistants favour the statistics. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C17-5|C17-5]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C18-X1|C18-X1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C17-R1|C17-R1]])

**Evidence style:** Allocator-behaviour observation and product experience; relies on others' quant work (Crochet, Eric); uses own fund's relative track record since mid-2016 (acknowledging selection bias); narrative framing.

**Views at the time**
- (2026-06) Sceptical of AI company valuations and circular financing, yet sees genuine optimism and wealth creation (SpaceX IPO at $135, private companies returning to public markets after two decades).. Reasoning: Burst of optimism after a long winter; public-to-private trend reversing. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C01-3|C01-3]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C02-X1|C02-X1]])
- (2026-06) BlackRock's multi-strategy ETF drew $4bn in one day, a starter gun for trillions in model portfolios seeking a third leg of allocation, which will eclipse mutual fund assets.. Reasoning: Model-portfolio demand for absolute return profiles. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C06-1|C06-1]])
- (2026-06) His simple trend replication has outperformed every large CTA but ISAM since mid-2016 and ranks third against current index constituents.. Reasoning: Own track record vs peers (with selection-bias caveat). ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C15-X2|C15-X2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C16-X1|C16-X1]])

### Niels Kaastrup-Larsen (Host (transcript spells his name 'Neil Castro Lson'); trend-following hedge fund manager)
Fingerprint: #approach/trend_following #approach/manager_selection_allocation #approach/regime_detection #approach/research_robustness_overfitting #approach/market_internals_leading
_Speaker note: Host states views on indices, manager diligence and complexity; the ledger corrected one claim to split his remarks from Beer's._

**Worldview premises**
- CTA indices include the biggest managers and their blowups and omit smaller managers who do well, so they may understate best-in-class trend; larger well-established managers show somewhat higher Sharpe over the last 10 to 15 years than the headline index figures. _[empirical, stated; support: Own peer-group comparison after system upgrades; not shown]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C15-1|C15-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C15-X1|C15-X1]])
- Investors should know whether a manager has a large share of net worth in the product versus a product that is one of many at a big asset manager. _[institutional, stated; support: His experience as a manager and observation of big asset managers entering]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C11-2|C11-2]])
- Complexity is not necessarily worse: ISAM, which is complex and trades hundreds of markets, has been the hardest manager to beat. _[empirical, stated; support: Beer's own ranking]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C16-2|C16-2]])
- What matters for drawdowns is what else is drawing down at the same time (Man Group paper 'Don't look down'). _[theoretical, stated; support: Cited paper, not summarised in detail]_ ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C17-4|C17-4]])

**Decision process**
- [research] Reads a trend barometer (43 = slightly weaker) and compares CTA indices with equities and bonds to describe the trend environment.. Why: Gauges the current trend regime. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C03-1|C03-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C03-2|C03-2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C03-X1|C03-X1]])
- [other] Due diligence should weigh how much of the manager's own net worth is in the product.. Why: Alignment versus one-of-many products at big asset managers. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C11-2|C11-2]])

**Evidence style:** Index figures and peer-group observation; asks questions and offers counterexamples.

**Views at the time**
- (2026-06 (about 12 June)) Trend barometer at 43 indicates a slightly weaker trend environment in June 2026, with equities and metals most challenging.. Reasoning: Barometer reading and recent performance. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C03-1|C03-1]])
- (2026-06) Year to date, SG CTA +9.83%, SG Trend +9.49%, Short-Term Traders +4.84%, versus MSCI World about +8%, S&P 500 +8.6% and global aggregate bonds +0.64%.. Reasoning: Index prints. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C03-2|C03-2]])
- (2026-06) In the first half of June, SG CTA fell 0.58% and SG Trend 0.84% versus MSCI World -2.39% and S&P 500 -2.4%: CTAs lost less than equities but did not hedge the pullback.. Reasoning: Index prints. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C03-X1|C03-X1]])

### Disagreements
- **Is simplicity better than complexity in trend following?**: Eric Crittenden: Simple, blunt rules hold up out of sample; complex ones look better in hindsight. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C12-2|C12-2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C13-1|C13-1]]); Andrew Beer: Simple replication has beaten every large CTA but one, and no evidence-based counter exists; large managers are efficient. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C15-X2|C15-X2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C16-1|C16-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C14-R1|C14-R1]]); Niels Kaastrup-Larsen: The hardest manager to beat (ISAM) is complex and trades hundreds of markets, a counterexample. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C16-2|C16-2]])
- **Do CTA indices represent the industry at its best?**: Niels Kaastrup-Larsen: Indices include the biggest managers and their blowups and omit smaller strong managers; larger established managers show higher Sharpe over 10-15 years than the index. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C15-1|C15-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C15-X1|C15-X1]]); Andrew Beer: The index is an accurate representation of large funds; institutions do not pay index fees; no secret pool of high-Sharpe large managers exists. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C15-1|C15-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C16-1|C16-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C16-X1|C16-X1]])
- **Is the trend-plus-equities combination mainly a product-design and behaviour problem or a statistical one?**: Eric Crittenden: No one disputes the math; the problem is behavioural (loss aversion, line-item risk), so build a set-and-forget product. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C07-2|C07-2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C07-3|C07-3]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C07-X2|C07-X2]]); Andrew Beer: Statistics are obvious (1+1=3 or 4) but narrative and distribution decide adoption; AI assistants accept the statistics but humans need language. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C06-2|C06-2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C18-X1|C18-X1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C17-R1|C17-R1]])

### Gaps and conflicts
- Eric's claim that combining two 0.4-Sharpe strategies gives about 1.1 (1.2 with another 0.3 from tail hedging and something else) does not follow from simple diversification: two uncorrelated 0.4-Sharpe strategies at equal risk combine to about 0.57, and 1.1 would need a correlation near -0.7; he acknowledges it may not be sustainable. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C17-3|C17-3]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C17-2|C17-2]])
- Eric's Sharpe-vs-track-record analysis (none above 1 at 10 years, about 0.65 maximum at 15-20 years) is a recollection of an old analysis (about 2008-09) across databases with survivorship and selection issues; he says he 'cannot prove this'. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C17-1|C17-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C17-2|C17-2]])
- Beer says simple replication outperforms nearly every large CTA, but the ranking is vs current index constituents (selection bias he acknowledges), and ISAM's numbers were not seen; also his rank depends on fees and implementation costs not discussed. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C15-X2|C15-X2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C16-X1|C16-X1]])
- Crochet's simple model result (Sharpe about 1 at 12.5% vol before costs, with about 800bp removed to look like CTA returns) is second-hand and Beer admits he is not a quant and cannot see the discarded models. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C14-1|C14-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C14-2|C14-2]])
- Tension: Eric says adding many markets adds little (4-6 components), Beer says clusters drive profit, yet Niels's counterexample (ISAM, hundreds of markets) and Eric's own universe reduction (niche markets are 'nice-to-haves') are not reconciled with a claim that breadth never matters. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C13-1|C13-1]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C14-3|C14-3]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C16-2|C16-2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C03-4|C03-4]])
- Eric says trend profits come when correlations rise, but also says the algorithmic discipline forces entries before trends are socially safe; the first is a state of the world, the second an entry timing, and the transcript does not say how they combine. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C13-3|C13-3]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C18-3|C18-3]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C17-5|C17-5]])
- The average hedge fund mutual fund statistic (2-3% a year after about 200bp fees) is stated without source or period. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C09-2|C09-2]])
- In the first read, a point about institutional fees embedded in the SG CTA index and the trend index's slightly higher Sharpe was attributed to Niels; it is Beer's. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C15-1|C15-1]])
- June 2026 index numbers are mid-month snapshots (to about 12 June) and the half-month fall is partial. ([[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C03-2|C03-2]], [[MT215 - Why Most Investors Fail at Trend Following - Systematic Investor - Ep.404#^MT215-C03-X1|C03-X1]])

### Forward-looking inputs (reader synthesis)
(reader) No explicit price forecasts. Inputs treated as relevant to future trend returns: (1) dislocation and uncertainty (policy shocks, tariffs) that create trends and risk premia; (2) rising volatility and correlation, which is when trend makes its money; (3) ETF model-allocator flows into alternatives (a $4bn single-day inflow) as demand evidence; (4) behaviour of allocators (regret, benchmark-relative loss aversion) as the limiting factor for adoption. Horizon: multi-year for trend payoffs; Sharpe sustainability questioned.

### Reader inferences (not stated by the speakers)
- (reader) Eric and Andrew agree on conclusions (simple, liquid, blended with equities) but have different evidence: Eric from decades of live trading and allocator behaviour, Andrew from product design, others' quant work and his fund's relative ranking.
- (reader) Both treat the trend-plus-equities combination as a solved statistical question and a distribution problem; none of the speakers discusses the cost to the combined product when equities and trend both lose (for example if rising correlation of stocks and bonds persists).
- (reader) The simple-vs-complex claim is supported by anecdote and by a single comparison (Beer's ETF vs large CTAs since mid-2016) that is exposed to survivorship and costs; Niels's ISAM counterexample is the only contrary datapoint.
- (reader) 'Contrarian tactical alpha' is a reframing, not a new mechanism: it restates that trend follows can enter before consensus, which conflicts with the usual description of trend following as joining existing moves.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 3 | intro, April 2025 tariff drawdown and smooth period since, trend-friendly dislocation, AI valuation skepticism |
| C02 | 0 | SpaceX IPO, AI, optimism; nothing actionable |
| C03 | 4 | June 2026 performance data, trend barometer, ETF wrapper for managed futures, market reduction |
| C04 | 1 | ETF distribution and tax, ETF pricing and market makers |
| C05 | 2 | market maker spreads depend on underlying liquidity, block trades, multi-strat ETF inflows |
| C06 | 2 | model portfolio demand for third leg, magic combo of trend plus equities |
| C07 | 4 | allocator behavior, prospect theory, managed futures benefit, product design rationale |
| C08 | 2 | wrapper and fund boxes, equal risk contribution sizing |
| C09 | 3 | choice of volatility level, hedge fund mutual fund returns, product development incentives |
| C10 | 3 | bonds as diversifier broke in 2022, allocator words vs actions, fear of equity outperformance |
| C11 | 2 | capital efficiency and portable alpha demand, manager skin in the game |
| C12 | 3 | one-sided option product launches, complexity vs simplicity in trend, COVID negative crude |
| C13 | 3 | principal components of trend returns, correlation optimization failure, trend profits in high vol and correlation |
| C14 | 4 | Crochet simple trend model, publication bias, instrument clusters, why CTA returns lag |
| C15 | 1 | index composition and fees, blowups, constituents bias |
| C16 | 3 | manager comparison, ISAM complexity counterexample, lumpy alpha, Sharpe vs track length start |
| C17 | 5 | Sharpe vs track record length, combining strategies, drawdown paper, CTA as contrarian alpha |
| C18 | 5 | contrarian tactical alpha, algorithmic discipline examples, loss rate, natural gas |
| C19 | 2 | gold example, blending trend with other assets, sign-off and legal |

## Claims

### C01
- **Eric Crittenden** Dislocation and uncertainty in mid-2026 create fertile ground for trends and risk premia to collect.  #mech/risk_premium _(time-bound view)_
  > is a fertile soil environment for finding trends and uh there's a lot of dislocation, a lot of uncertainty and I think a lot of risk premiums to collect going forward
  indicator: trend environment · asset: multi · direction: favors trend following · horizon: months · conditions: mid 2026 · testable: no - prediction · confidence: medium
  ^MT215-C01-1
- **Eric Crittenden** April 2025 tariff tantrums caused a hard drawdown for trend followers, followed by 12-14 months of many trends and risk premia.  #mech/cycle_persistence _(time-bound view)_
  > the tariff um tant tantrums that was going on in April of last year. Since then, it's basically been smooth sailing.
  indicator: trend follower returns after April 2025 · asset: multi · horizon: months · conditions: after sharp policy reversal · testable: yes - index returns · confidence: high
  ^MT215-C01-2
- **Andrew Beer** Beer is skeptical of AI company valuations and circular financing, while recognizing the real optimism and wealth creation.  #mech/overshoot _(time-bound view)_
  > when I see the valuations of AI companies and the kind of circular financing and everything that's going on in it
  indicator: AI valuations, circular financing · asset: equities · horizon: years · conditions: mid 2026 · testable: no - opinion · confidence: medium
  ^MT215-C01-3

### C02
- **Andrew Beer** In June 2026 the public-to-private trend of two decades is reversing: large private companies (SpaceX priced its IPO at $135) are listing, creating wealth and a source of optimism and equity supply alongside stretched AI valuations.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check, time-bound view)_
  > we have companies coming back into the public markets after two decades of basically public companies going private
  indicator: IPO issuance, private-to-public listings · asset: equities · direction: more equity supply from IPOs · horizon: years · conditions: high valuations and strong demand for AI and space names · testable: yes - IPO volume and subsequent index returns · confidence: medium
  ^MT215-C02-X1

### C03
- **Niels Kaastrup-Larsen** A trend barometer at 43 indicated a slightly weaker trend environment in June 2026, with equities and metals most challenging.  #mech/cycle_persistence _(time-bound view)_
  > my trend barometer finished yesterday at 43. That indicates a slightly weaker environment
  indicator: trend barometer · asset: multi · horizon: weeks · conditions: mid June 2026 · testable: yes - index defined by host · confidence: medium
  ^MT215-C03-1
- **Niels Kaastrup-Larsen** June 2026 data: SG CTA +9.83% YTD, SG Trend +9.49%, Short-Term Traders +4.84%, versus MSCI World about +8%, S&P 500 +8.6% and global aggregate bonds +0.64%.  #mech/cycle_persistence _(time-bound view)_
  > Stocken CTA index down 58 basis points but still up 9.83 for the year
  indicator: SG CTA, SG Trend, SG Short-Term Traders indices · asset: multi · horizon: months · conditions: as of mid June 2026 · testable: yes - published index data · confidence: high
  ^MT215-C03-2
- **Eric Crittenden** Diversified international futures portfolios could not run in an ETF because market makers lacked liquidity infrastructure, but this is changing.  #mech/liquidity_flows _(time-bound view)_
  > market makers are starting to um build the infrastructure such that a portfolio like ours would run smoothly and efficiently in an ETF structure
  indicator: ETF market maker capacity · asset: multi · horizon: years · conditions: international, less liquid futures · testable: no - structural · confidence: medium
  ^MT215-C03-3
- **Eric Crittenden** Niche markets (platinum, Japan, palm oil) are nice-to-haves; performance attribution shows they do not matter much, so reducing dimensionality for an ETF costs little.  #mech/research_method
  > you don't need all of these markets. We don't need to be trading platinum and Japan and you know, Malaysian palm oil and whatnot.
  indicator: number of markets traded · asset: multi · direction: trade fewer, liquid markets · testable: yes - ablate markets in backtest · confidence: high
  ^MT215-C03-4
- **Niels Kaastrup-Larsen** In the first half of June 2026 the SG CTA index fell 0.58% and SG Trend 0.84% (Short-Term Traders about -0.5%, 'Beta 50' -0.69%), while MSCI World lost 2.39% and the S&P 500 2.4%, so CTAs lost less than equities in the pullback but did not hedge it.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > Stocken CTA index down 58 basis points but still up 9.83 for the year. Stocken trend down 84 basis points up 9.49 for the year.
  indicator: SG CTA, SG Trend, SG Short-Term Traders, MSCI World, S&P 500 (June 2026 month to date) · asset: multi · horizon: weeks · conditions: equities and metals were the difficult sectors for trend · testable: yes - index data · confidence: high
  ^MT215-C03-X1

### C04
- **Eric Crittenden** Many new advisors and individual investors are ETF-only, so an ETF wrapper widens distribution; tax benefit is mainly on the equity sleeve.  #mech/structural_shift
  > the newest generations of advisors a lot of them are ETF only
  asset: multi · horizon: years · testable: no · confidence: high
  ^MT215-C04-1
- **Andrew Beer** Unlike a mutual fund (one end-of-day NAV), an ETF has an intraday NAV but trades at market prices set by bids and offers, and market makers who profit from order-book imbalance keep the price near NAV, though sometimes better and sometimes worse.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > with an ETF, you have an NAV that fluctuates during the day because you know what the underlying portfolio looks like and that changes your pricing
  indicator: ETF price versus intraday NAV, bid-ask spread · asset: multi · horizon: days · conditions: depth of market makers and liquidity of the underlying · testable: yes - premium or discount to NAV and spread data · confidence: high
  ^MT215-C04-X1

### C05
- **Andrew Beer** ETF market makers hedge via the underlying, so ETFs on deep, liquid instruments trade within a penny or two of NAV, while illiquid underlyings widen spreads.  #mech/liquidity_flows
  > the more complicated the underlying is, the more illquid the underlying is, the more the more risk they have of moving the price of the underlying
  indicator: ETF bid-ask versus NAV · asset: multi · direction: use deepest, most liquid markets · horizon: days · testable: yes - spread data · confidence: high
  ^MT215-C05-1
- **Andrew Beer** Large model allocators trade ETFs through ETF desks via blocks or dark pools; ease of moving large dollars is a selling point.  #mech/liquidity_flows
  > you have an ETF desk and the ETF desk will basically do block trades or trade in dark pools or things like that
  indicator: ETF block trades · asset: multi · horizon: days · testable: no · confidence: medium
  ^MT215-C05-2
- **Andrew Beer** Financial advisors fear visible, avoidable mistakes (for example a market order that moves an ETF price by 50 bp), so an ETF must trade tightly to NAV to be adopted by advisors who grew up with mutual funds.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > they're often incredibly focused on the one or two three things that can go wrong and make them look bad
  indicator: ETF execution slippage, spread · asset: multi · conditions: advisor-driven distribution · testable: no - qualitative · confidence: medium
  ^MT215-C05-X1
- **Andrew Beer** Allocators split into two groups: those who want a one-stop multi-strategy ETF that fills the alternatives bucket with an absolute-return profile, and those who want to assemble the building blocks themselves, which sets the product design.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > There are other allocators who want to build those building blocks themselves.
  indicator: multi-strategy ETF flows · asset: multi · horizon: years · conditions: model-portfolio allocators · testable: no - qualitative · confidence: medium
  ^MT215-C05-X2

### C06
- **Andrew Beer** A $4bn single-day inflow into BlackRock's new multi-strategy ETF shows trillions in model portfolios seeking a third leg of the asset allocation stool, which will eclipse mutual fund assets.  #mech/liquidity_flows _(time-bound view)_
  > We need a third leg of the asset allocation stool and how do we build that?
  indicator: ETF flows into alt/multi-strat products · asset: multi · horizon: years · conditions: mid 2026 · testable: partly - flow data · confidence: medium
  ^MT215-C06-1
- **Andrew Beer** Combining managed futures with equities is statistically about as obvious as it gets (1+1=3 or 4), with offerings from Fidelity/Crochet, ManHL, Hoffstein, JP Morgan, Winton and Aspect.  #mech/risk_management
  > about as statistically obvious as anything that managed futures as a strategy plus equities um is you know 1 plus 1 equals three or four
  indicator: trend plus equities blend · asset: multi · direction: combine trend with equities · horizon: years · testable: yes - published · confidence: high
  ^MT215-C06-2

### C07
- **Eric Crittenden** Allocators buy what is up and sell when it stalls, which makes it hard for them to hold uncorrelated strategies.  #mech/behavioral
  > They tend to uh buy things that are up a lot and sell them as soon as they stall out.
  indicator: allocator flows chasing performance · asset: multi · horizon: months · testable: yes - fund flow studies · confidence: high
  ^MT215-C07-1
- **Eric Crittenden** Under prospect theory, benchmark-relative loss aversion (S&P 500 or 60/40) made it nearly impossible to keep allocators in managed futures beyond a few quarters, even though adding it improves everything.  #mech/behavioral
  > a $10 gain gives you one unit of pleasure but a $10 loss gives you two units of pain
  indicator: loss aversion, benchmark relative · asset: multi · horizon: months · conditions: benchmark-relative investors · testable: partly · confidence: high
  ^MT215-C07-2
- **Eric Crittenden** Adding a decent managed futures program to any portfolio raises returns, lowers volatility and reduces drawdowns.  #mech/risk_management
  > returns go up, V goes down, draw downs get smaller, everything gets better
  indicator: managed futures added to portfolio · asset: multi · direction: add managed futures · horizon: years · testable: yes - blended backtest · confidence: high
  ^MT215-C07-3
- **Eric Crittenden** Owning a large equity position is comfortable when paired with a long-convexity trend component that fills drawdowns.  #mech/risk_management
  > I'm not afraid to own equities as long as I've got the long convexity trend component that can fill those potholes during the hard times or at least the expectation of that
  indicator: trend as convexity to equities · asset: equities · direction: equities plus trend · horizon: years · testable: yes · confidence: high
  ^MT215-C07-4
- **Eric Crittenden** Even after agreeing with the math, a standalone managed-futures holding creates a visible line item whose every monthly move triggers questions from clients, regulators and compliance; this micromanagement is a main reason allocators abandon it.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > They're staring at that line item risk. They're staring at the the statement risk.
  indicator: standalone line-item performance versus benchmark · asset: multi · horizon: months · conditions: benchmark-relative evaluation of each sleeve · testable: partly - holding periods of allocators in standalone managed futures versus blended products · confidence: high
  ^MT215-C07-X1
- **Eric Crittenden** A managed-futures product built without hedge-fund fees, scalable, and combined with low-fee tax-efficient equity exposure solves the product-market fit problem and a set-and-forget holding that the manager would use with his own money.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > if I can build a good managed features program and don't charge hedge fund fees, you know, don't charge the 2 and 20, uh, and have something that's scalable
  indicator: fee level, tax efficiency · asset: multi · horizon: years · testable: no - product design choice · confidence: medium
  ^MT215-C07-X2

### C08
- **Eric Crittenden** A diversifier that raises return and lowers risk does not fit style boxes (large cap growth, fixed income active), complicating distribution.  #mech/structural_shift
  > to get that benefit that we're talking about where you a diversifier that actually increases returns and lowers risk at the same time, you're not going to fit into any one of those boxes nicely
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT215-C08-1
- **Eric Crittenden** Size equity and trend sleeves for equal volatility contribution (e.g. 100% of an 8% vol managed futures program plus 50% of 16% vol stocks) because the better performer is unknown.  #mech/risk_management
  > I strive for equal risk contribution from the equities and from the trend side.
  indicator: equal risk contribution · asset: multi · direction: equal vol weights equities and trend · horizon: years · testable: yes - backtest of weights · confidence: high
  ^MT215-C08-2

### C09
- **Eric Crittenden** Choose the volatility level that is competitive but survivable: double risk invites VaR and compliance stress, half risks lagging inflation and fees.  #mech/risk_management
  > aggressive enough to be competitive, but not so aggressive that, you know, we're going to be scrambling in um, riskoff events
  indicator: target volatility · asset: multi · horizon: years · testable: no - judgement · confidence: medium
  ^MT215-C09-1
- **Andrew Beer** Average hedge fund mutual funds earned only 2-3% a year after about 200bp fees, worse than random, reflecting marketing-driven product development.  #mech/behavioral
  > the average hedge fund mutual fund has been a catastrophe for investors like 2 to 3% peranom returns after 200 basis points in fees
  indicator: liquid alternatives returns · asset: multi · horizon: years · testable: yes - fund data · confidence: high
  ^MT215-C09-2
- **Andrew Beer** Most products are built by distribution teams chasing flows with no ownership over five years, unlike managers building for their own capital.  #mech/behavioral
  > Normal product development in the mutual fund and ETF business is marketing and distribution people
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT215-C09-3

### C10
- **Andrew Beer** Since 2022 bonds stopped diversifying stocks, so ETF model allocators with only stocks and bonds look for a 3-5% alternative allocation.  #mech/structural_shift
  > Stock and bond correlations break down. bonds break down as a diversifier started in in 2022
  indicator: stock-bond correlation · asset: multi · direction: add managed futures 3-5% · horizon: years · conditions: post-2022 · testable: yes - rolling correlation · confidence: high
  ^MT215-C10-1
- **Andrew Beer** Advisors say they want diversification or tail protection but often do not act on products that deliver it.  #mech/behavioral
  > their their their actions often don't follow their words
  asset: multi · testable: no · confidence: medium
  ^MT215-C10-2
- **Andrew Beer** Allocators fear being blamed when equities double and their diversifier gains only 20%; blending trend with 50% equity avoids that regret.  #mech/behavioral
  > that's a success from a diversification perspective, I'm going to be blamed for it, but if I got 50% equity in there as well and I'm up 70, no one's going to complain
  indicator: career risk of diversifier · asset: multi · direction: blend trend with equities · horizon: years · conditions: equity bull markets · testable: no · confidence: medium
  ^MT215-C10-3
- **Andrew Beer** The alternatives market is not one pool but hundreds of submarkets with different needs, so a product succeeds by choosing one specific allocator segment (for example ETF model allocators who need a 3-5% diversifier) instead of trying to serve everyone.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > there is no addressable market. There are hundreds of submarkets out there.
  asset: multi · horizon: years · testable: no - business view · confidence: medium
  ^MT215-C10-X1

### C11
- **Andrew Beer** Capital-efficiency-focused allocators do not want to sell stocks, which drives demand for full portable-alpha (100% equity plus overlay) products.  #mech/structural_shift
  > they don't want to sell a penny
  indicator: portable alpha / return stacking · asset: multi · horizon: years · testable: no · confidence: medium
  ^MT215-C11-1
- **Niels Kaastrup-Larsen** Due diligence should weigh whether the manager has a large share of net worth in the product versus a product that is one of many at a big asset manager.  #mech/behavioral
  > the difference between what it means when you invest with a manager where they are really committed and invested in the product and in a product that is just one of a hundred
  indicator: manager skin in the game · asset: multi · horizon: years · testable: no · confidence: medium
  ^MT215-C11-2
- **Andrew Beer** Large-firm trend products are credible when built by experienced trend teams (JP Morgan's quant team, Fidelity's hire of Rob Crochet) rather than by generalists given an engineering degree, which is the diligence test between serious and opportunistic entrants.  #mech/research_method _(added by sonnet-xhigh cross-check, time-bound view)_
  > to me JP Morgan is doing something like very very serious and credible. They're going to a team who knows how to do this.
  indicator: team experience in trend following · asset: multi · horizon: years · conditions: new trend and managed-futures products from big asset managers · testable: no - qualitative · confidence: medium
  ^MT215-C11-X1

### C12
- **Andrew Beer** Large firms launch trend products as a one-sided option (market if it works, close if not), so allocators must vet the team's modelling credibility over 5-10 years.  #mech/behavioral
  > it's largely a one-sided option
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT215-C12-1
- **Eric Crittenden** Complex trend programs look better in hindsight and in presentations, but simple durable rules hold up much better out of sample.  #mech/research_method
  > the simple ones are the ones that hold up on data they haven't already seen
  indicator: simple vs complex trend models · asset: multi · direction: prefer simple rules · horizon: years · testable: yes - out-of-sample test · confidence: high
  ^MT215-C12-2
- **Eric Crittenden** In April 2020 simple trend rules kept the fund short crude oil when prices went negative, showing blunt tools handle unprecedented events.  #mech/risk_management
  > those were simple, blunt tools that put us on the right side of risk premium
  indicator: crude oil short 2020 · asset: commodities · direction: short · horizon: days · conditions: negative price event · testable: no - anecdote · confidence: high
  ^MT215-C12-3

### C13
- **Eric Crittenden** Most trend follower returns map to 4-6 principal components (energies, fixed income, grains, USD), about 90/10 Pareto, so adding many markets adds little.  #mech/research_method
  > the majority of the returns that trend followers collect can be mapped back to you know four, five, maybe six principal components
  indicator: principal components of trend returns · asset: multi · horizon: years · testable: yes - PCA of CTA returns · confidence: high
  ^MT215-C13-1
- **Eric Crittenden** Overweighting uncorrelated markets via correlation, cointegration or copula optimization reduced profit and understated risk in live trading.  #mech/risk_management
  > you make a lot less money. Uh, and you fool yourself into thinking you have less risk than you really do
  indicator: correlation-based weighting · asset: multi · direction: do not overweight uncorrelated markets · horizon: years · testable: yes - compare equal weight vs optimized · confidence: high
  ^MT215-C13-2
- **Eric Crittenden** Trend profits arrive when volatility and correlations rise; low-vol, low-correlation periods bring whipsaws and few profits.  #mech/cycle_persistence
  > in trend following you make your money in market environments where the ball's going up, the correlation's going up
  indicator: volatility and cross-asset correlation · asset: multi · direction: press risk when vol and correlation rise · horizon: months · conditions: low-vol gentle correlation periods are whipsaw · testable: yes - conditional returns · confidence: high
  ^MT215-C13-3
- **Eric Crittenden** Eric prefers what works with real money in the real world to academically elegant optimisation; blunt tools are less satisfying but work better to make money and control risk.  #mech/new _(added by map cross-check)_
  > I want to respect reality, not the elegance of of academia
  indicator: live-trading results vs spreadsheet models · asset: multi · direction: n/a · horizon: years · conditions: pushing real money into real markets · testable: no · confidence: high
  ^MT215-C13-R1

### C14
- **Andrew Beer** Crochet's ultra simple 12-month lookback trend model had a Sharpe of about 1 at 12.5% vol; to resemble CTA universe returns, about 800bp had to be removed.  #mech/cycle_persistence
  > this simple like super ultra simple trend following model that he built which is basically looking back over a year and reflexively just buying it
  indicator: 12-month lookback time-series momentum · asset: multi · direction: long if up over 12 months · horizon: years · testable: yes - replicable · confidence: high
  ^MT215-C14-1
- **Andrew Beer** Published research hides discarded models, so readers only see the final results (selection bias).  #mech/research_method
  > You're not shown the 37 models that were thrown out that didn't make it into the final paper.
  asset: multi · testable: no · confidence: medium
  ^MT215-C14-2
- **Andrew Beer** Trend profits may come from clusters (energy, metals, equities) moving together rather than 70 independent instruments.  #mech/research_method
  > are you making it from 70 instruments working in your favor or are there clusters of instruments because oil's going up and it's dragging the whole energy complex with it
  indicator: cluster concentration of trend P&L · asset: multi · horizon: months · testable: yes - P&L attribution · confidence: medium
  ^MT215-C14-3
- **Andrew Beer** Possible reasons for CTA Sharpe ratios far below a simple model's: short-term models exit before moves, and risk controls cut positions.  #mech/research_method
  > because the short-term models are getting people out at, you know, 9:31 before the markets move, not at the end of the day, uh, or the risk controls are kicking in
  indicator: CTA implementation shortfall · asset: multi · horizon: years · testable: yes - decompose · confidence: low
  ^MT215-C14-4
- **Andrew Beer** Beer says that in two years of making the argument that trend profits come from clusters and a simple signal captures them, he has seen no well-articulated, evidence-based counter-argument from the industry.  #mech/new _(added by map cross-check)_
  > I haven't seen uh a well articulated evidence-based counter response to that argument
  indicator: simple trend signal vs complex CTA returns · asset: managed futures · direction: simple signal competitive with CTA index · horizon: years · conditions: based on Crochet's paper and his own track record · testable: partly · confidence: medium
  ^MT215-C14-R1

### C15
- **Niels Kaastrup-Larsen** CTA indices include the biggest managers and their blowups, but omit smaller managers who do well, so may understate best-in-class trend; institutions also pay lower fees than those embedded in the index.  #mech/research_method
  > you get all the blowups in the index right because they're all usually the biggest managers then they blow up so that drags the index down
  indicator: SG CTA index composition · asset: multi · horizon: years · testable: partly - requires constituents · confidence: medium
  **Correction (cross-check):** Speaker mix-up and merge: the remarks that the index drags in the biggest managers' blowups and omits smaller managers are Niels's, but the point that big institutions do not pay the fees embedded in the SG CTA index (and that the trend index has a slightly higher Sharpe) is made by Andrew Beer, not Niels. → Niels: CTA indices contain the biggest managers and their blowups and omit smaller managers who do well, so they may not reflect the industry at its best. Beer: large institutions do not pay the fees built into the SG CTA index, so index Sharpe ratios do not describe what they earn.
  ^MT215-C15-1
- **Niels Kaastrup-Larsen** Looking back 10 to 15 years (after system upgrades), the larger, well-established trend managers show somewhat higher Sharpe ratios than the headline SG Trend or CTA index figures that the media quote, so the index mixture understates best-in-class trend.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > most of them I would say you know have certainly somewhat higher sharp ratio for sure
  indicator: SG Trend index Sharpe versus large-manager peer group, 10-15 year window · asset: multi · horizon: years · conditions: peer group of larger established managers · testable: yes - compare Sharpe of the peer group with the index over matching windows · confidence: medium
  ^MT215-C15-X1
- **Andrew Beer** Beer's simple trend replication has outperformed every large CTA but one (ISAM) since its mid-2016 start, and ranks third against current index constituents, evidence that large managers add little over a simple signal.  #mech/research_method _(added by sonnet-xhigh cross-check, time-bound view)_
  > from our start date when the starting gun went off in mid 2016 we've outperformed every single one
  indicator: relative performance versus large CTA peers since mid-2016 · asset: multi · horizon: years · conditions: self-reported ranking, subject to selection bias in the peer set · testable: yes - compare returns of the fund and peers over the same dates · confidence: medium
  ^MT215-C15-X2

### C16
- **Andrew Beer** No hidden pool of large, high-Sharpe trend managers exists; efficiency among large managers means a simple replication gets competitive rank.  #mech/research_method
  > I don't see some secret pool of large high sharp ratio managers except in very very limited circumstances
  indicator: large-manager Sharpe ratios · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT215-C16-1
- **Niels Kaastrup-Larsen** ISAM, which is complex and trades hundreds of markets, has been hardest to beat, a counterexample to simplicity being better.  #mech/research_method
  > they're not simple in any way, shape, or form, and they trade hundreds of markets
  indicator: complex multi-market CTA · asset: multi · horizon: years · testable: partly - one manager · confidence: low
  ^MT215-C16-2
- **Andrew Beer** Trend alpha is lumpy: Dunn's very large 2022 gain carried its numbers for a decade.  #mech/cycle_persistence
  > we know alpha is lumpy but but but your alpha was ultra super lumpy in a in in a very very compelling way
  indicator: Dunn 2022 performance · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT215-C16-3
- **Andrew Beer** Ranking against the current index constituents carries selection bias because managers drop out and are added and firms switch which fund represents them, so index and peer comparisons must account for membership changes.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > linking the the current manager which has selection bias also because you know Graham will switch from this one to that one and man will switch from this one to that one
  indicator: CTA index constituent turnover · asset: multi · horizon: years · conditions: backfilled or reconstituted manager indices · testable: yes - compare as-reported history with a point-in-time constituent list · confidence: medium
  ^MT215-C16-X1

### C17
- **Eric Crittenden** Plotting Sharpe ratios of hedge funds against track record length shows the maximum falls with length: none over 1 at 10 years and about 0.65 at 15-20 years.  #mech/research_method
  > You get out to 10, no one has a sharp ratio over one.
  indicator: Sharpe ratio vs track record length · asset: multi · direction: set realistic Sharpe expectations · horizon: years · testable: yes - fund database test · confidence: medium
  ^MT215-C17-1
- **Eric Crittenden** A good single strategy sustains a Sharpe ratio of about 0.3-0.4.  #mech/research_method
  > single strategies good ones have a sharp ratio somewhere between 3 and 04 sustainably
  indicator: sustainable Sharpe ratio · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT215-C17-2
- **Eric Crittenden** Combining 0.4-Sharpe strategies (equities, managed futures, tail hedging) gives a combined Sharpe of 1.1-1.2, sustainability uncertain but closer to 1 than any single strategy.  #mech/risk_management
  > if you combine strategies, you take a point4 from equities and you take a point4 from managed futures, you know, you get something like 1.1
  indicator: combined Sharpe of diversified strategies · asset: multi · direction: combine uncorrelated strategies · horizon: years · testable: yes - portfolio math · confidence: medium
  **Correction (cross-check):** Recorded as the speaker stated it, but the arithmetic does not hold under simple diversification: two uncorrelated strategies with Sharpe 0.4 at equal risk combine to about 0.57, and reaching 1.1 needs a correlation near -0.7. Treat the 1.1-1.2 figure as the speaker's unverified rule of thumb, and note he says himself that it may not be sustainable. → Eric Crittenden says that combining roughly 0.4-Sharpe strategies (equities, managed futures) gets a Sharpe near 1.1, and adding about 0.3 from tail-risk hedging and another strategy gets near 1.2; this is the speaker's claim and is not supported by simple arithmetic unless the strategies are strongly negatively correlated.
  ^MT215-C17-3
- **Niels Kaastrup-Larsen** A Man Group paper ('Don't look down') argues what matters for drawdowns is what else is drawing down at the same time.  #mech/risk_management
  > how what else is drawing down when you're drawing down
  indicator: drawdown overlap · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT215-C17-4
- **Andrew Beer** Reframing CTA as 'contrarian tactical alpha': money is made by early, uncomfortable entries, not by joining crowded trends late.  #mech/cycle_persistence
  > when the space makes money, it's it's it's not trend following. It's not getting into something late, right?
  indicator: entry timing of trend profits · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT215-C17-5
- **Andrew Beer** Beer believes the managed futures space has a messaging problem: the theory of the Sharpe ratio is not bridging to the experience of owning the product, and a simple narrative is needed.  #mech/new _(added by map cross-check)_
  > I believe we have a messaging issue with the space
  indicator: n/a · asset: managed futures · direction: n/a · horizon: n/a · conditions: distribution to allocators · testable: no · confidence: high
  ^MT215-C17-R1

### C18
- **Andrew Beer** Trend wins came from early contrarian-looking trades: crude oil in January after declines, gold at 2200 after a decade of nothing, shorting Treasuries in September 2020 at 70bp.  #mech/cycle_persistence
  > buying gold at 2200 after it's been dead money for a decade
  indicator: gold, crude, Treasuries · asset: multi · direction: enter trends early · horizon: months · testable: partly - anecdotes · confidence: medium
  ^MT215-C18-1
- **Andrew Beer** Managed futures is a dynamic, tactical asset class whereas other portfolio assets are static betas; because of low correlation all returns show up as alpha.  #mech/risk_management
  > This is the this this isn't a strategy. It's an asset class. It's an asset class that by its nature is dynamic and tactical.
  indicator: managed futures as asset class · asset: multi · horizon: years · testable: no · confidence: medium
  ^MT215-C18-2
- **Eric Crittenden** Algorithmic discipline forced uncomfortable positions (short equities in 2002 and 2008, short energy before COVID, long cocoa up 400%) that produced alpha.  #mech/behavioral
  > the algorithmic discipline to get into trends before they're socially and politically uh safe is crucially important
  indicator: systematic rule adherence · asset: multi · horizon: months · testable: no - anecdotal · confidence: high
  ^MT215-C18-3
- **Eric Crittenden** 50-70% of trend trades lose, so keep losses small and hold winners for years.  #mech/risk_management
  > in the trend following world, 50 60 sometimes 70% of your trades don't work out
  indicator: win rate and holding period · asset: multi · direction: cut losers, hold winners · horizon: years · testable: yes - trade stats · confidence: high
  ^MT215-C18-4
- **Eric Crittenden** Trend rules stayed short natural gas for eight years in a heavy contango market, capturing persistent roll-down.  #mech/cycle_persistence
  > at one point I was short natural gas I think for eight consecutive years
  indicator: natural gas futures, contango roll · asset: commodities · direction: short natural gas · horizon: years · conditions: persistent contango · testable: yes · confidence: high
  ^MT215-C18-5
- **Andrew Beer** AI assistants such as ChatGPT and Claude judge the trend-plus-equities combination on statistical outcomes and favor it, but human allocators need a simple narrative like 'contrarian tactical alpha' to act, so distribution depends on language as well as statistics.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > They're all looking at the statistical benefits of it but we need language.
  asset: multi · testable: no - anecdotal · confidence: low
  ^MT215-C18-X1

### C19
- **Eric Crittenden** Gold was dead money for two decades; trend rules ignored it, then went long after the breakout and held for 25 years.  #mech/cycle_persistence
  > algorithmic discipline forced you to not waste your time on it for 20 years and to be long and strong ever since then
  indicator: gold · asset: commodities · direction: long gold after breakout · horizon: years · testable: yes · confidence: high
  ^MT215-C19-1
- **Eric Crittenden** Trend is hard to live with day to day, so blending it with other assets in a multi-asset product helps investors stay invested.  #mech/behavioral
  > on a day-to-day basis it tends to drive people crazy which is why I blend it with other assets
  asset: multi · direction: blend trend with other assets · horizon: years · testable: no · confidence: high
  ^MT215-C19-2

