---
source_id: MT013
title: "AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387"
date: 2026-02-15
channel: "Top Traders Unplugged"
url: 
words: 14157
claims: 89
added_by_crosscheck: 13
corrections: 3
crosscheck: "opus cross-check"
speakers: ["Andrew Beer (co-host, DBi / DBMF managed-futures replication ETF)", "Tom Roble (co-host, SG CTA/Trend index research; captioned name)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged; captioned 'Neil's Krup Larson')"]
tags: [source, layer0]
---
# AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387

**Speakers:** Andrew Beer (co-host, DBi / DBMF managed-futures replication ETF); Tom Roble (co-host, SG CTA/Trend index research; captioned name); Niels Kaastrup-Larsen (host, Top Traders Unplugged; captioned 'Neil's Krup Larson')

**Summary:** Top Traders Unplugged Systematic Investor Ep.387 (Feb 2026): Beer, Roble and Kaastrup-Larsen review 2025-26 trend-following performance (gold, non-US equities, April 2025 deleveraging), debate short- vs long-term models and risk management, and critique liquid alternatives, replication and QIS products. Main conclusions: long-term models paid, short-term models were a costly risk tool, CTA alpha is being early contrarian and right, and many liquid-alt products fail because they are sold not bought.

**Approach:** trend following, CTA, managed futures replication, liquid alternatives, QIS, risk allocation, gold, non-US equities

**Cross-check completeness estimate of first read:** 0.87 - good coverage of the main threads; missed 2025 sector attribution (gold/non-US equities, poor bonds, short JGBs), CTA VaR mix, replication tracking variance, rebalance speed in V-reversals, track-record length, equity long-short fee math and the don't-time-trend advice; two speaker errors.

## Argument map

**Episode thesis:** Andrew Beer argues that CTA alpha is being early, contrarian and right, and that 2025's flat CTA space despite gold +60% and rallying equities came from short-term models: they have roughly zero Sharpe, whipsaw on sentiment oscillation without a change in fundamental value, and are a costly risk-management tool, while long-term models captured lasting shifts (gold, non-US equities). Tom Roble (SG) adds that with few trending markets in 2025 risk allocation and risk management decided manager returns, that non-US investors are rethinking US risk, and that concentrated programs are hard to sell. Both Beer and host Niels Kaastrup-Larsen critique liquid-alternative, replication and QIS products as sold rather than bought and often opaque, with Beer calling for allocators to define the signal they want and implement it efficiently.

### Andrew Beer (co-founder of a managed-futures replication ETF firm (DBi / DBMF, captioned as 'ABF'/'DBI'); former allocator and commodity firm founder; co-host)
Fingerprint: #approach/trend_following #approach/replication_indexing #approach/research_robustness_overfitting #approach/costs_execution #approach/manager_selection_allocation #approach/structural_themes #approach/portfolio_construction_stacking
_Speaker note: Recorded around Thursday 12 February 2026 (index data as of Tuesday 10 February; uploaded 2026-02-15). He cannot talk about DBMF flows for compliance reasons. Captions garble names (Roble captioned 'Roble'; Simplify as 'simplified'). His account of 'our' performance refers to his firm's replication._

**Worldview premises**
- Valuable trends occur when fair value really changes and informed participants like the asset more at each higher price (10 to 11 to 12). Sentiment oscillation without a change in fundamental value (10 to 11 to 9) is noise captured by locals and high-frequency traders, and whipsaws trend followers. _[theoretical, stated; support: a stylised price-path model of fair value versus sentiment; experience running a fundamental commodity firm (Pinnacle) where traders waited for CTA signals to trade against them]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C11-2|C11-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C11-3|C11-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C11-4|C11-4]])
- Short-term trend models have no strong Sharpe ratio and are a costly risk-management tool (higher trading costs); allocating risk to a zero-Sharpe component to reduce volatility is a poor trade, and risk management should not be conflated with that. Long-term models capture lasting shifts. _[empirical, stated; support: SG trend indicator factor analysis for 2025 (long-term about +20%, short-term -12 to -15%); his own view of shorter-term models over many years]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C09-1|C09-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C09-2|C09-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C09-3|C09-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C09-4|C09-4]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-1|C12-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-2|C12-2]])
- CTA alpha comes from being early, contrarian and right. In 2025 CTAs added equity risk after Liberation Day and held gold while human strategists feared recession; non-US equities and gold, which narratives had mistimed for 15 years, were finally captured. _[experience, stated; support: 2025 outcomes; his recollection of 2020 calls (short Treasuries, long gold, short yen); gold failing in 2022 then soaring in 2024 for different reasons]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C07-1|C07-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C07-2|C07-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C07-3|C07-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C07-4|C07-4]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C11-R3|C11-R3]])
- When CTAs de-risk after a volatility spike, local traders who know the market trade against them, so CTAs pay implementation costs and liquidity dries up; backtests understate this cost, and adding many non-core markets makes de-risking drawdowns worse. _[theoretical, stated; support: Liberation Day experience; a former Goldman metals desk head's comment about local knowledge versus systematic traders]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-3|C12-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-4|C12-4]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-5|C12-5]])
- Hedging a long-term trend model out of fear of tail events (out-of-the-money puts) or paying for protection against a bad whipsaw costs too much; allocators' fear of a Friday loss turning into a worse Monday is not something one is paid to cater to. _[theoretical, stated; support: SVB example; reasoning about costs]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C13-2|C13-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C13-3|C13-3]])
- The liquid-alternative category (hedge fund strategies in mutual funds, UCITS and ETFs) has been astonishingly bad: 2-3% over 15 years with about 200bp fees while equities rose about 14% a year. Products are designed by salespeople to meet demand, not on investment merit, and capital flows to the largest sales forces (sold, not bought). _[empirical, stated; support: Wilshire category data cited; failed multi-manager mutual funds (Blackstone, Neuberger Berman); product launch incentives]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C13-4|C13-4]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C13-5|C13-5]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C14-1|C14-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C15-1|C15-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C17-1|C17-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C16-5|C16-5]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C16-X2|C16-X2]])
- Backtests of risk-premia and replication products overstate Sharpe (G10 carry 1.2); live results fall about 75% short of backtests. After the 2007 quant losses the narrative shifted to harvesting permanent risk premia, which understated risk; calling trend a risk premium is misleading because different designers' trend indices differ greatly. _[experience, stated; support: his 2013-14 papers and later outcomes; Standard Life GARS (promised equity beta 0.2 with cash plus 5; reached $90 billion)]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C16-2|C16-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C16-3|C16-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C16-4|C16-4]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C20-1|C20-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C19-4|C19-4]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C20-2|C20-2]])
- Allocation to managed futures should be a core allocation and not traded tactically; allocators who want to time something should time another asset. Few allocators actively trade it. _[institutional, stated; support: client feedback behind his product plan (line-item constraint, model allocators)]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C18-X1|C18-X1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C17-2|C17-2]])
- AI-driven economic disruption should help trend following because trend needs real economic change; asset management stays a people business, but AI-assisted allocations already recommend managed futures as a core element. _[experience, stated; support: an investor's 15-minute AI allocation analysis; his own PR firm AI-voice episode]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C02-1|C02-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C02-2|C02-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C02-3|C02-3]])
- Private equity is essentially leveraged equity with smoothed marks, which is less attractive when valuations are high and expected 10-year returns low; allocators overcommitted expecting distributions that did not arrive. _[theoretical, stated; support: Dan Rasmussen's research (Verdad); secondaries market growth]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C05-1|C05-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C05-2|C05-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C05-X1|C05-X1]])

**Chain: Why short-term models detracted in 2025 and long-term models did not**
1. Sentiment shifts (Liberation Day shock, rebound) without a change in the state of the world → Short-term models are whipsawed violently: price oscillates around unchanged fair value; locals and HFTs trade the oscillation ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C11-3|C11-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-1|C12-1]])
2. Lasting shifts (move out of US assets, gold, non-US equities) visible in prices and in flows at the margin → Long-term models get behind the trend and capture it: fair value is changing and informed participants like the asset more at higher prices ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C11-2|C11-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-1|C12-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C07-3|C07-3]])
3. Gold +60% and equities rallying → CTA space flat in 2025 because short-term trend lost 12-15% while long-term trend gained about 20%: short-term allocation carried zero Sharpe and trading costs ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C09-1|C09-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C09-2|C09-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C09-3|C09-3]])
- Evidence: SG trend indicator factor analysis (Tom Roble's report), mirrored by Nick Baltas and Katie Kaminski analysis according to Beer.
- Fails when: In the initial April 2025 shock short-term models preserved capital better than long-term models (they lost later in chop), so protection over a few days is where they help; Beer judges that too costly.

**Chain: Why CTA de-risking after a spike is expensive**
1. Volatility spikes and CTAs cut risk → Local traders in that market see the selling and trade against it: liquidity dries up when CTAs sell at once ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-3|C12-3]])
2. Many non-core markets in the book → Larger implementation costs and deeper drawdowns during de-risking: less liquid markets where outsiders get picked off ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-4|C12-4]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-5|C12-5]])
3. Slower (weekly) de-risking and keeping a little risk on → Better outcome around Liberation Day because the selloff reversed: faster de-risking sold near the low ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-X2|C12-X2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-X1|C12-X1]])
- Evidence: His firm's relative performance around Liberation Day versus the index (about four drivers of variation; -500bp in 2023, outperformance in 2024 and 2025).
- Fails when: Slow de-risking would hurt in a sustained crash; he says his firm was 'slow to derisk' and benefited when Trump changed his mind.

**Chain: Why liquid-alternative products fail investors**
1. Product designed by salespeople to meet distribution demand rather than investment conviction → Launches with no investment view on which product is best: incentive is assets under management, not outcomes ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C13-5|C13-5]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C14-1|C14-1]])
2. Large firms with large sales forces → Capital goes to them regardless of product quality (AQR in mutual fund form, line-item constraints): allocators do not want to ask hard questions and take brand-based manager risk ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C17-1|C17-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C17-2|C17-2]])
3. Aggressive return promises with low equity beta (GARS) or backtested Sharpe → Realised results far below promise (about 75% decay): backtests overstate and cost layers eat return ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C16-2|C16-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C16-3|C16-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C16-5|C16-5]])
- Evidence: Wilshire data, GARS, multi-manager mutual funds, risk premia products.
- Fails when: Some products work when built from an investment need (the SEI mandate: beta 0.2, cash plus 5, expense under 100bp) and some quant multi-strategy products have done better.

**Decision process**
- [signal] Allocate to the signal wanted (long-term trend) and implement it as efficiently and cheaply as possible, not by picking managers on narrative.. Why: manager risk is very high (two 0.8-correlated long-term models can be 20 points apart in a year) ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C15-3|C15-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C20-2|C20-2]])
- [risk] Do not use short-term models or out-of-the-money put hedges as risk management; accept the occasional bad whipsaw.. Why: zero Sharpe component, higher costs and a hedge bill that kills the business ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C09-4|C09-4]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C13-3|C13-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-2|C12-2]])
- [execution] De-risk slowly (weekly execution) so as not to sell at the low after a spike; keep non-core markets limited.. Why: implementation costs, local trader front-running and fast reversals ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-X2|C12-X2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-4|C12-4]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-5|C12-5]])
- [research] Due diligence on QIS and bank trend indices: ask when the index launched, how similar earlier indices performed, and the realised Sharpe over a stated period; combine several banks' flavours of trend to diversify design risk.. Why: narratives talk about engineering, not returns; many allocators suspended belief ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C15-2|C15-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C19-3|C19-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C20-3|C20-3]])

**Evidence style:** Allocator and product-builder track record, stylised models (10-11-9 versus 10-11-12), data cited from third parties (Wilshire, SG trend indicator), his own papers and anecdotes of failed products; strong opinions delivered as rants.

**Views at the time**
- (2026-02-12 (recording; data as of 2026-02-10)) 2025 was gold plus non-US (including emerging) equities, roughly half the trend profit each, with whipsaw losses in rates and currencies; the same themes continued into 2026.. Reasoning: factor analysis; fundamental rotation out of US assets finally showing in prices ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C09-X2|C09-X2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C07-3|C07-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C07-4|C07-4]])
- (2026-02-12) Attitude to US markets has shifted from FOMO to concern about predictability and rule of law, drawing attention to hedge funds that can make money; renewed interest in hedge funds as private equity overexposure unwinds.. Reasoning: allocator conversations; private equity distributions did not arrive; high equity valuations and software exposure to AI disruption ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C05-3|C05-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C05-1|C05-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C05-X1|C05-X1]])
- (2026-02-12) Disruption from AI should be good for trend following, and AI asset-allocation analyses recommend managed futures as a core element.. Reasoning: trend needs real change in the economy ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C02-1|C02-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C02-3|C02-3]])
- (2026-02-12) Hopes 2026 is the trendiest year ever.. Reasoning: strong start to the year ()

### Tom Roble (SG CTA / trend index research (Societe Generale); co-host)
Fingerprint: #approach/trend_following #approach/nowcasting_data #approach/position_sizing_vol_target #approach/geopolitics #approach/macro_fundamental_topdown #approach/manager_selection_allocation #approach/research_robustness_overfitting
_Speaker note: Authored the 2025 review and the SG trend indicator used in the factor analysis. Ledger corrections applied: the concentrated-program remark (C10-4) and the QIS curve-steepener remark (C18-1) are his, not the host's._

**Worldview premises**
- Trend following normally shows a speed factor in which longer-term models outperform shorter-term ones; 2025 followed that pattern, but the 'classic contradiction' is how to square this with investors who cannot look at performance over such a long-term lens. _[empirical, stated; support: SG trend indicator and prior analysis by Katie Kaminski]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C08-2|C08-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C08-R2|C08-R2]])
- When few markets trend, risk allocation and risk management decide manager returns: in 2025 average breakout z-scores across about 200-500 parameters were poor, bonds were poor and metals (precious metals in 2025, softs and metals in 2024) drove commodity profits two years running. _[empirical, stated; support: SG trend indicator with about 200-500 breakout parameters across markets; manager return range in 2026]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C06-3|C06-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C06-4|C06-4]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C06-X1|C06-X1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C08-3|C08-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C08-4|C08-4]])
- CTAs managed precious-metals risk much better than an unmanaged trend portfolio: they cut risk quickly in the late-January 2026 selloff, silver risk was small relative to gold, and proprietary trend-strength and overextension models size down late in trends; actual VaR was much larger in equities and FX. _[empirical, stated; support: SG trend indicator (hypothetical, little risk management) versus manager reports he saw]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C08-5|C08-5]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C08-6|C08-6]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C08-7|C08-7]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C09-X1|C09-X1]])
- After 2025 non-US investors rethink US risk. Dollar weakness cut a euro investor's S&P 500 return to about 2.5% versus 16% in USD and weakened the dollar's safe-haven status; global equity markets are too small for a wholesale reallocation, so the shift is limited to specific parts of US risk. _[empirical, stated; support: calculation for a euro investor in 2025; investor and manager conversations]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C03-1|C03-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C03-2|C03-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C03-3|C03-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C03-4|C03-4]])
- The environment (stubborn inflation, geopolitics, commodities returning from compressed volatility, higher rates) favours long-short tactical global macro, and QIS is used by macro funds for finite thematic bets (curve steepeners), outsourcing execution and financing. _[experience, stated; support: client conversations at a bank with an active QIS business]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C05-4|C05-4]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C18-1|C18-1]])
- Investors whose core risk is equities want asymmetric diversification, which trend delivers better than multi-strategy funds; the hedge fund industry splits into scalable tactical-asset-allocation strategies (CTAs, with falling costs) and pure alpha that goes in and out of vogue. _[institutional, stated; support: investor discussions that week]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C11-1|C11-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C14-3|C14-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C14-2|C14-2]])
- Concentrated trend programs create return but are hard to sell because of investment-committee constraints and strategic allocations. _[institutional, stated; support: client conversations; refers to a London CTA manager without naming]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C10-4|C10-4]])

**Chain: Why dollar weakness changed the US-asset calculus for foreign investors in 2025**
1. Dollar weakens in 2025 and loses safe-haven status → A euro investor's S&P 500 gain shrinks from 16% to about 2.5%: currency exposure dominates the foreign investor's return ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C03-2|C03-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C03-3|C03-3]])
2. US risk seen as higher and no dollar hedge in stress → Non-US investors rethink which US assets they hold, not wholesale selling: global equity markets are too small to absorb a wholesale shift ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C03-1|C03-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C03-4|C03-4]])
- Evidence: Euro-investor calculation; discussions with investors and managers.
- Fails when: Not discussed; he says investors are not looking to sell entirely.

**Chain: Why 2025 trend performance depended on risk allocation**
1. Few broadly trending markets (poor average breakout z-scores; bonds poor) → Return depended on being in the few trending markets (metals) with the right risk: opportunity not broad across equities, currencies and bonds ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C06-3|C06-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C06-X1|C06-X1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C08-3|C08-3]])
2. Managers cut risk fast as precious metals reversed → Small losses in the late-January 2026 selloff and YTD returns of about 8-15% by early 2026: monitoring of trend overextension and size down late in trends ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C08-5|C08-5]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C08-7|C08-7]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C08-4|C08-4]])
- Evidence: SG trend indicator breakout z-scores; manager return range.
- Fails when: If one is not trading the right markets (for example metals) the opportunity is missed.

**Decision process**
- [research] Run a trend indicator of breakout models across about 200-500 parameters from very short to super long term and across all potentially tradable markets, using average z-scores as an opportunity-set measure similar to a barometer.. Why: measures how broad the trending opportunity is and where it is ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C06-3|C06-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C06-5|C06-5]])
- [risk] Size down late in trends using proprietary trend-strength and overextension models; cut risk in line with volatility.. Why: protect profits in overextended markets such as precious metals ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C08-7|C08-7]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C08-5|C08-5]])

**Evidence style:** Data-driven: SG trend indicator and index data, report analysis, euro-investor arithmetic and investor/manager conversations.

**Views at the time**
- (2026-02-12) Early 2026 trends are best in smaller equity indices (Kospi, Nikkei, OMX, IBEX 35); market selection matters.. Reasoning: SG trend indicator ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C06-5|C06-5]])
- (2026-02-12) Non-US investors rethink US risk after 2025; the shift is partial (S&P 500 +16% in 2025 in USD).. Reasoning: dollar weakness, higher perceived US risk ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C03-1|C03-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C03-2|C03-2]])
- (2026-02-12) The environment is better for long-short tactical global macro (stubborn inflation, geopolitics, commodities returning, higher rates).. Reasoning: macro environment ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C05-4|C05-4]])
- (2026-02-10) Manager returns range about 8-15% year to date by mid-February 2026, with the trend index peaking at about 7%.. Reasoning: manager data ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C08-4|C08-4]])

### Niels Kaastrup-Larsen (host of Top Traders Unplugged; veteran hedge fund manager and trend follower)
Fingerprint: #approach/trend_following #approach/manager_selection_allocation #approach/position_sizing_vol_target #approach/replication_indexing #approach/behavioral_sentiment #approach/positioning_crowding
_Speaker note: Speaks as a modern trend follower who adjusts position size with volatility. Ledger corrections applied to C10-4 and C18-1 (both are Tom Roble's)._

**Worldview premises**
- A modern trend follower with variable position sizing cuts risk as volatility rises, giving up some profit in strong trends but avoiding disaster when stops trigger over the weekend; managers with static positions and hundreds of markets get little from outliers because each market is a tiny risk allocation. _[experience, stated; support: gold and silver selloff of 29-30 January 2026; unnamed managers insisting on static sizing did no better in 2025]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C10-1|C10-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C10-2|C10-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C10-3|C10-3]])
- In 2025 trend followers saw the usual pattern: a few big winners, several small losers and many that barely moved; profits came mostly from metals and select equities, with short JGBs another winner, and equity profits were limited because April deleveraging forced cuts. _[empirical, stated; support: performance observation across trend followers]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C08-1|C08-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C09-5|C09-5]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C10-X1|C10-X1]])
- Strategies go in and out of favour, so 5-10 years of track record says little about the next 5-10 years; replication and QIS products that do things differently may not deliver the CTA outcome in all regimes (the last 10 years differ from the first 10 of the millennium), and QIS trend products publish no returns so cannot be evaluated. _[experience, stated; support: analyses by Nick Baltas and Katie Kaminski cited; absence of published returns]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C16-X1|C16-X1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C19-1|C19-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C19-2|C19-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C19-R1|C19-R1]])
- A replication ETF with large tracking error to the CTA index is better viewed as an alternative-data trend strategy than as a cost saving. _[experience, stated; support: his reading of the tracking error]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C16-1|C16-1]])
- Hedge funds improved managers, structures and processes under competition and mark-to-market discipline, while private equity merely grew bigger. _[experience, stated; support: Dan Rasmussen (Verdad) email]_ ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C04-2|C04-2]])

**Decision process**
- [sizing] Adjust positions with volatility rather than keeping them static.. Why: reduces risk when volatility expands; avoids a bad Monday after a Friday signal ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C10-1|C10-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C10-2|C10-2]])
- [portfolio] A concentrated, few-market program with large risk allocation is how to make 50-80% returns, but it needs a different set of investors.. Why: hundreds of markets dilute outliers ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C10-3|C10-3]])

**Evidence style:** Cites index data, other guests' analysis, anecdotes of investor behaviour and discussion with managers; openly states when he is 'not an expert' (QIS).

**Views at the time**
- (2026-02-10 close (recorded Thursday 2026-02-12)) His trend barometer at 50 (mid-February 2026) indicates a productive and consistent trend environment; SG Trend Index +6.43% YTD versus the S&P 500 about +1.5%.. Reasoning: index and barometer data ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C06-1|C06-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C06-2|C06-2]])
- (2026-02-12) Trend leadership rotated in February from metals to equities, natural gas and currencies.. Reasoning: performance attribution ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C07-5|C07-5]])
- (2026-02-12) Strategies that do not predict but profit from change may do well in 2026 given how much is going on in the world.. Reasoning: geopolitical and policy change ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C20-4|C20-4]])
- (2026-02) Google's issuance of a 100-year bond (last by Motorola in 1997) is rare and may say something about duration expectations.. Reasoning: unusual issuance ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C04-1|C04-1]])

### Disagreements
- **Static versus variable position sizing and market count**: Niels Kaastrup-Larsen: Variable sizing protected managers (silver and gold gap risk) and static-size managers with 300-500 markets did not do better in 2025; punchy returns need few markets and a big allocation. ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C10-1|C10-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C10-2|C10-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C10-3|C10-3]]); Andrew Beer: More non-core markets raise de-risking drawdowns through implementation costs; supports slower, weekly de-risking and limited markets. ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-4|C12-4]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-5|C12-5]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-X2|C12-X2]]); Tom Roble: Concentrated programs create return but are hard to sell to investment committees. ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C10-4|C10-4]])
- **What replication products are and whether QIS/replication delivers**: Niels Kaastrup-Larsen: The replication ETF's large tracking error makes it an alternative-data trend strategy rather than a cost saving; QIS trend products publish no returns; different methods may not deliver the CTA outcome in all regimes. ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C16-1|C16-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C19-1|C19-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C19-2|C19-2]]); Andrew Beer: Built the product on allocator feedback (line-item constraints, ETF at 85bp); a huge fan of QIS when one knows what one is doing; criticism is aimed at products sold not bought and at unrealistic Sharpe promises. ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C15-3|C15-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C17-2|C17-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C18-2|C18-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C15-2|C15-2]]); Tom Roble: QIS is used thematically by clients to outsource execution and financing of finite macro themes. ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C18-1|C18-1]])
- **Are short-term models worth their risk-management role?**: Andrew Beer: Short-term models have zero Sharpe, cost too much and detract; they only helped in the first April 2025 shock. ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C09-3|C09-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C09-4|C09-4]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C13-1|C13-1]]); Tom Roble: Longer-term models normally outperform; the real issue is reconciling that with investors who cannot look at performance over long periods. ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C08-2|C08-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C08-R2|C08-R2]])

### Gaps and conflicts
- Beer's 2025 factor result (long-term +20%, short-term -12 to -15%) is read from memory of Roble's report and not defined (no specification of what 'short-term' and 'long-term' mean); the claim that short-term models have no strong Sharpe is stated as a view, with no numbers shown. ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C09-2|C09-2]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C09-3|C09-3]])
- Beer notes short-term models did better in the initial April 2025 shock but later lost; the net 2025 verdict therefore mixes protection value against chop losses, which he does not quantify. ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C13-1|C13-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C09-1|C09-1]])
- Beer's claim that CTA alpha is being early, contrarian and right sits uneasily with trend following being mechanical and price-based; his examples (2020 short Treasuries, long gold below $3,000) are after-the-fact. ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C07-1|C07-1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C11-R3|C11-R3]])
- The 75% backtest-to-live decay and the 2-3% liquid-alt return come from his recollection and an unspecified Wilshire dataset; Roble notes classification of 'liquid alternatives' mixes true hedge funds with multi-asset funds. ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C16-3|C16-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C13-4|C13-4]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C14-2|C14-2]])
- Beer says he cannot discuss his own product's flows; his replication-versus-hedge-fund tracking differences (-500bp in 2023, large outperformance 2024-25) are self-reported. ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C12-X1|C12-X1]])
- Niels's claim about managers with static positions doing no better in 2025 is not supported by data shown and does not name them; ledger flags speaker corrections on C10-4 and C18-1. ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C10-3|C10-3]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C10-4|C10-4]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C18-1|C18-1]])
- Tom Roble says CTAs had less precious-metals risk than assumed, while Beer and Niels speak of large gold and silver exposure; the VaR report he cites is one report. ([[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C09-X1|C09-X1]], [[MT013 - AI, Risk, and the Future of Systematic Investing - Systematic Investor - Ep.387#^MT013-C08-5|C08-5]])

### Forward-looking inputs (reader synthesis)
(reader) Beer treats real changes in fair value (informed participants liking an asset more at each higher price) as the signal for lasting trends, i.e. long-term trend and flow shifts out of US assets, gold and non-US equities. Roble uses the breadth of breakout z-scores across 200-500 parameters, risk allocation to the few trending markets, and dollar weakness and non-US investor behaviour. Niels uses his trend barometer (50) and rotation of leadership. Horizons are months to a year for long-term trend; a few days for short-term protection.

### Reader inferences (not stated by the speakers)
- (reader) Beer's 10-11-9 versus 10-11-12 model implies a testable distinction between sentiment noise and fundamental change: the short-term-versus-long-term performance gap should widen when price oscillates without a persistent flow, and narrow in regime shifts; he offers no way to tell the two apart in real time.
- (reader) Roble's framing (opportunity set measured by average breakout z-score; manager returns then decided by risk allocation) implies that in weak-opportunity years dispersion across managers is mostly a risk management artefact, supporting Beer's point about cost-aware de-risking.
- (reader) The three speakers agree liquid-alt and replication products need transparency of realised Sharpe, but differ on whether low tracking error to an index is the right test; Niels and Beer both treat tracking error as secondary to realised outcomes.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | Intro and disclaimers; Beer on AI narrative and AI-generated voice anecdote (no testable claim) |
| C02 | 3 | AI disruption as positive for trend; allocators remain a people business; AI allocation analysis includes managed futures |
| C03 | 4 | Roble on shift away from US dollar/US exceptionalism; euro investor S&P return; Olympics chatter |
| C04 | 2 | Olympics chatter; Google 100-year bond; Rasmussen on why hedge funds improved vs private equity |
| C05 | 4 | Private equity overcommitment and leverage; FOMO to US-risk reappraisal; macro hedge fund environment |
| C06 | 5 | Trend barometer 50 and index returns Feb 2026; 2025 diverse opportunity set, metals, commodities, European indices |
| C07 | 5 | CTAs early contrarian after Liberation Day; non-US equity rotation and gold as failed-then-successful trades; Feb leadership shift |
| C08 | 7 | 2025 familiar trend year; risk allocation, longer-term models, manager dispersion, silver risk, overextension models |
| C09 | 5 | Gold up 60% yet CTA space flat; short-term models detracted; short-term trend as costly risk management; April deleveraging |
| C10 | 4 | Dynamic position sizing vs static; stop execution gap risk; market count dilution; concentrated CTAs hard to sell |
| C11 | 4 | Role of CTA vs multistrat; what is CTA alpha (early contrarian); noise vs information-driven trends |
| C12 | 5 | Short vs long models; zero-Sharpe short-term trend; local traders exploit CTA de-risking; non-core positions |
| C13 | 5 | Short-term models in April drawdown; allocator fear of whipsaw; liquid alts poor results; product development |
| C14 | 3 | Liquid alts sold by salespeople; classification of hedge funds vs quasi alternatives; scalable TAA vs pure alpha |
| C15 | 3 | Failed multi-manager mutual funds; QIS marketing ignores realised Sharpe; allocator discipline |
| C16 | 5 | DBMF tracking error and alt-data view; Standard Life GARS; back-test decay; manager-replication limits |
| C17 | 2 | Products sold not bought; AQR mutual fund and manager risk; DBMF origin and ETF design |
| C18 | 2 | Model allocators; QIS as thematic implementation; ETF model portfolios and innovation |
| C19 | 4 | QIS transparency, replication risk, due diligence on index history, risk premia labeling |
| C20 | 4 | Risk premia narrative history; manager risk in trend; allocators combining flavours; outlook and sign-off |
| C21 | 0 | Housekeeping, sign-off and sponsor reads |

## Claims

### C02
- **Andrew Beer** AI-driven economic disruption should be positive for trend following because trend strategies need real change in the economy to profit.  #mech/structural_shift _(time-bound view)_
  > I believe that that is actually going to be very very positive for for for trend falling we need real economic change to to make money
  indicator: trend following · asset: multi · direction: trend profits up with disruption · horizon: years · conditions: if AI causes broad repricing · testable: no: forward view · confidence: medium
  ^MT013-C02-1
- **Andrew Beer** Asset management remains a people business, so allocators will not hand manager selection to AI, though AI will help average allocators become more sophisticated.  #mech/behavioral _(time-bound view)_
  > I don't think asset allocators are going to say uh you know what let's have AI pick the next hedge fund for me.
  asset: other · horizon: years · testable: no: opinion · confidence: medium
  ^MT013-C02-2
- **Andrew Beer** AI asset-allocation analyses recommend managed futures as a core element, suggesting spreading knowledge will increase allocations to trend.  #mech/structural_shift _(time-bound view)_
  > it actually did say all right if you want to achieve these investment objectives it it you know it brought managed futures as one of the core um elements of doing that
  indicator: managed futures allocation in AI-generated portfolios · asset: multi · direction: more allocation to trend · horizon: years · testable: no: anecdotal · confidence: low
  ^MT013-C02-3

### C03
- **Tom Roble** After 2025 non-US investors see higher US risk and are rethinking US asset exposure, though not wholesale selling.  #mech/liquidity_flows _(time-bound view)_
  > the perception as investors is that the period of US exceptionalism is is maybe over
  indicator: US dollar and US assets for foreign investors · asset: multi · direction: less US allocation · horizon: years · testable: partly: foreign flow data · confidence: medium
  ^MT013-C03-1
- **Tom Roble** Dollar weakness cut a euro investor's 2025 S&P 500 return to about 2.5% versus 16% in USD, so currency exposure dominates foreign returns.  #mech/risk_management _(time-bound view)_
  > a euro investor uh with the same S&P 500 investment was up just 2 and a half% last year
  indicator: S&P 500 in EUR vs USD · asset: fx · horizon: months · conditions: when USD falls · testable: yes: public data · confidence: high
  ^MT013-C03-2
- **Tom Roble** The dollar's safe-haven status weakened in 2025, removing the usual hedge for non-US holders of US assets.  #mech/risk_premium _(time-bound view)_
  > normally you have non-American investors can rely on the US dollar to rise in times of stress and the US dollar has enjoyed the status of being a safe haven currency
  indicator: USD in risk-off episodes · asset: fx · direction: USD down in stress · horizon: months · conditions: 2025 regime · testable: yes: USD vs equity drawdowns · confidence: medium
  ^MT013-C03-3
- **Tom Roble** Global equity markets are too small to absorb a wholesale reallocation from the US, so the shift is limited to specific parts of US risk.  #mech/liquidity_flows
  > global equity markets don't have the capacity for a wholesale shift in in investor assets away from the US
  indicator: capacity of non-US equity markets · asset: equities · horizon: years · testable: partly · confidence: medium
  ^MT013-C03-4

### C04
- **Niels Kaastrup-Larsen** Google issuing a 100-year bond is rare (last in 1997 by Motorola) and may say something about duration expectations.  #mech/behavioral _(time-bound view)_
  > apparently has not happened since 1997 where Motorola issued a 100red-year bond
  indicator: century bond issuance · asset: rates · testable: partly: rarity of century bonds · confidence: low
  ^MT013-C04-1
- **Niels Kaastrup-Larsen** Hedge funds improved managers, structures and processes under competition and mark-to-market discipline while private equity merely grew bigger.  #mech/structural_shift
  > hedge funds in his view simply had to improve because of the competition and the attention that private equity was given um by by investors for so long
  asset: other · horizon: years · testable: no: opinion · confidence: medium
  ^MT013-C04-2

### C05
- **Andrew Beer** Allocators overcommitted to private equity expecting distributions that did not arrive, creating over-exposure and driving the secondaries market and renewed hedge fund interest.  #mech/liquidity_flows
  > they would overcommit to it with the expectation that they would get money back in a certain period of time
  indicator: private equity distributions · asset: other · direction: hedge fund inflows · horizon: years · testable: partly: allocation surveys · confidence: medium
  ^MT013-C05-1
- **Andrew Beer** Private equity is essentially leveraged equity with smoothed marks, which is less attractive when equity valuations are high and expected 10-year returns low.  #mech/risk_premium
  > the return characteristic of private equity essentially being some version of leverage equity
  indicator: private equity return characteristics · asset: equities · horizon: years · conditions: high valuations · testable: yes: Rasmussen research · confidence: medium
  ^MT013-C05-2
- **Andrew Beer** The attitude to US markets has shifted from FOMO to concern about predictability and rule of law, drawing attention to hedge funds that can make money in this environment.  #mech/behavioral _(time-bound view)_
  > the attitude used to be FOMO about the US markets and now has has has come to people saying like, well, wait a second
  asset: equities · horizon: years · testable: no · confidence: medium
  ^MT013-C05-3
- **Tom Roble** Stubborn inflation, geopolitics, commodities returning from compressed volatility and rates higher than recent history make the environment better for long-short tactical global macro.  #mech/cycle_persistence _(time-bound view)_
  > We've got stubborn inflation. We've got geopolitical dislocations and tensions.
  asset: multi · horizon: years · conditions: as of early 2026 · testable: no: view · confidence: medium
  ^MT013-C05-4
- **Andrew Beer** Allocators are heavily exposed through private equity to software companies that AI could disrupt, adding to the case against long-term leveraged long equity exposure.  #mech/structural_shift _(added by opus cross-check, time-bound view)_
  > being you know up to their gills and things like software stocks that could be disrupted
  indicator: private equity exposure to software · asset: equities · direction: PE/software valuations down if AI disrupts · horizon: years · conditions: high equity valuations and AI disruption · testable: partly - PE software exposure vs subsequent marks · confidence: medium
  ^MT013-C05-X1

### C06
- **Niels Kaastrup-Larsen** The host's trend barometer at 50 indicates a productive and consistent trend environment in Feb 2026.  #mech/cycle_persistence _(time-bound view)_
  > my own trend barometer finished yesterday at 50 and that's still a pretty productive environment for trend following
  indicator: Trend barometer (host's own) · asset: multi · horizon: months · conditions: as of Feb 2026 · testable: partly: proprietary · confidence: medium
  ^MT013-C06-1
- **Niels Kaastrup-Larsen** SG Trend Index was up 6.43% YTD to mid-Feb 2026 and S&P 500 about 1.5%, so trend outperformed equities.  #mech/cycle_persistence _(time-bound view)_
  > Stocken trend index up 1.65% uh for the month, up 6.43% for the year.
  indicator: SG Trend Index, S&P 500, Beta 50 · asset: multi · horizon: months · conditions: as of mid-Feb 2026 · testable: yes: public index data · confidence: high
  ^MT013-C06-2
- **Tom Roble** In 2025 average breakout z-scores across about 200-500 parameters were poor, so risk allocation to the few trending markets (metals) decided performance.  #mech/cycle_persistence _(time-bound view)_
  > on average last year the zed scores so the opportunity sets is similar to your kind of barometer I think uh was pretty poor
  indicator: breakout model z-scores across parameters and markets · asset: multi · horizon: months · conditions: when breadth of trends is low · testable: yes: SG breakout indicator · confidence: medium
  ^MT013-C06-3
- **Tom Roble** Commodities drove trend profits two years running but from different sources: softs and metals in 2024, precious metals in 2025.  #mech/cycle_persistence _(time-bound view)_
  > in 2025, it's really been the precious metals that have been the key performance drivers
  indicator: precious metals, cocoa, coffee trends · asset: commodities · horizon: years · testable: yes · confidence: high
  ^MT013-C06-4
- **Tom Roble** In early 2026 smaller equity indices (Kospi, Nikkei, OMX, IBEX 35) show the best trends, so market selection matters.  #mech/cycle_persistence _(time-bound view)_
  > we're seeing really good trending markets in Cosby, Niki, the Swedish OMX, and IBEX 35
  indicator: trend indicator by market · asset: equities · direction: long non-US equity indices · horizon: months · conditions: early 2026 · testable: yes · confidence: medium
  ^MT013-C06-5
- **Tom Roble** Bond markets offered poor trend opportunities for CTAs in 2025.  #mech/cycle_persistence _(added by opus cross-check, time-bound view)_
  > In fact you bonds was really poor last year.
  indicator: breakout-model z-scores in bond futures (SG trend indicator) · asset: rates · horizon: years · conditions: 2025 · testable: yes - trend returns by sector in 2025 · confidence: high
  ^MT013-C06-X1

### C07
- **Andrew Beer** CTA alpha comes from being early, contrarian and right, e.g. adding equity risk and keeping gold after Liberation Day.  #mech/slow_reaction
  > CTAs generate alpha when they're early contrarian and right.
  indicator: trend following alpha · asset: multi · horizon: years · testable: partly · confidence: high
  ^MT013-C07-1
- **Andrew Beer** Human strategists feared recession after Liberation Day; CTAs, which do not care about narratives, rode the rebound and kept positions.  #mech/behavioral _(time-bound view)_
  > human strategists after liberation day were really rattled and really wrong
  asset: equities · horizon: weeks · conditions: after sharp equity selloffs · testable: partly · confidence: medium
  ^MT013-C07-2
- **Andrew Beer** Fundamental rotation to non-US equities failed for 15 years but has finally occurred in the last couple of years, which trend captured.  #mech/cycle_persistence _(time-bound view)_
  > people have been talking about a fundamentally driven rotation into non- US equities for 15 years and it hasn't worked
  indicator: non-US vs US equity relative performance · asset: equities · direction: long non-US equities · horizon: years · testable: yes · confidence: medium
  ^MT013-C07-3
- **Andrew Beer** Gold failed for 15 years and did not rise in 2022 when expected, then soared from 2024 for different reasons, showing narratives mislead and trend works.  #mech/slow_reaction _(time-bound view)_
  > gold was a failed trade for a decade and a half
  indicator: gold price · asset: commodities · direction: long gold · horizon: years · testable: yes · confidence: high
  ^MT013-C07-4
- **Niels Kaastrup-Larsen** In Feb 2026 trend leadership rotated from metals to equities, natural gas and currencies.  #mech/cycle_persistence _(time-bound view)_
  > the leadership has changed a little bit in February. It's not so much medals uh anymore.
  indicator: trend returns by sector · asset: multi · horizon: weeks · conditions: Feb 2026 · testable: yes · confidence: medium
  ^MT013-C07-5

### C08
- **Niels Kaastrup-Larsen** In 2025 trend followers saw the usual pattern of a few big winners and several small losers despite unusual events.  #mech/cycle_persistence _(time-bound view)_
  > Yet from a trend following perspective, it was a very familiar year. Few markets did all the heavy lifting.
  indicator: trend returns concentration · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT013-C08-1
- **Tom Roble** Longer-term trend models normally outperform shorter-term ones (speed factor); 2025 followed that.  #mech/slow_reaction
  > we normally see a much stronger preference for longerterm models outperforming
  indicator: trend speed factor · asset: multi · direction: long-term models outperform · horizon: years · testable: yes: Kaminski analysis · confidence: medium
  ^MT013-C08-2
- **Tom Roble** With few trending markets in 2025, risk allocation and risk management decided manager returns.  #mech/risk_management
  > it's really the allocation of risk last year that was the key thing and how you managed that risk.
  asset: multi · horizon: years · conditions: low breadth of trends · testable: yes · confidence: medium
  ^MT013-C08-3
- **Tom Roble** Manager returns in early 2026 ranged about 8-15% YTD, showing good risk management.  #mech/risk_management _(time-bound view)_
  > we still got many managers in that 10 to 15% range
  indicator: manager dispersion · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT013-C08-4
- **Tom Roble** Unmanaged trend portfolios swing heavily in precious metals, while actual CTAs cut risk quickly during the late-January 2026 selloff.  #mech/risk_management _(time-bound view)_
  > please ask us for the data on the SG trend indicator, which is our hypothetical model-based portfolio, which with with very limited u risk management, and you'll see some very interesting swings in the precious metals markets
  indicator: SG trend indicator (unmanaged) · asset: commodities · horizon: weeks · conditions: precious metals reversals · testable: yes · confidence: medium
  ^MT013-C08-5
- **Tom Roble** Silver risk allocation in CTAs was small relative to gold because it is a smaller market.  #mech/risk_management _(time-bound view)_
  > silver has caught a lot of headlines but it's not as big a market as gold and so maybe the allocation of risk to that market wasn't as big
  indicator: silver vs gold risk allocation · asset: commodities · horizon: months · testable: yes · confidence: medium
  ^MT013-C08-6
- **Tom Roble** CTAs use proprietary trend-strength and overextension models to size down late in trends.  #mech/risk_management
  > we've had CTAs kind of building proprietary models over the years to help them work out when trends are overextended
  indicator: trend strength, overextension · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT013-C08-7
- **Tom Roble** Roble says the speed factor creates a classic contradiction between the evidence that longer-term models pay off and investors who cannot assess performance over such long horizons.  #mech/new _(added by map cross-check)_
  > it's the classic sort of uh contradiction about how you marry your investors who maybe can't always look at the performance with
  indicator: speed factor and investor horizon · asset: multi · direction: n/a · horizon: years · conditions: investors with short evaluation horizons · testable: partly · confidence: medium
  ^MT013-C08-R2

### C09
- **Andrew Beer** In 2025 gold rose 60% and equities rallied yet the CTA space was flat, because short-term models detracted.  #mech/slow_reaction _(time-bound view)_
  > gold is up 60%. Right? I mean I mean this should have been a banner year for the space
  indicator: gold; SG CTA index · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT013-C09-1
- **Andrew Beer** In SG's trend-indicator factor analysis long-term trend returned about +20% in 2025 while short-term trend lost 12-15%.  #mech/slow_reaction _(time-bound view)_
  > you're up 20% or something in in in long-term trend according to that and you're down you know 12, 13, 14, 15 and short-term trend
  indicator: SG trend indicator by speed · asset: multi · direction: long speed models · horizon: years · conditions: 2025 · testable: yes · confidence: medium
  ^MT013-C09-2
- **Andrew Beer** Short-term trend models have no strong Sharpe and are costly risk management tools that raise trading costs.  #mech/risk_management
  > they're a riskmanagement tool and they're often a costly risk management tool
  indicator: short-term trend Sharpe ratio · asset: multi · direction: avoid large risk to short-term models · horizon: years · testable: yes: speed-bucket Sharpe · confidence: high
  ^MT013-C09-3
- **Andrew Beer** Allocating risk to a zero-Sharpe component to reduce volatility is a poor trade.  #mech/risk_management
  > If you're going to allocate a meaningful amount of money to something that has a zero sharp ratio over time
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT013-C09-4
- **Niels Kaastrup-Larsen** Trend profits in 2025 equities were limited because April deleveraging forced cuts and some managers went short before the rebound.  #mech/crowding_positioning _(time-bound view)_
  > it really was all about the April uh deleveraging thanks to liberation day
  indicator: April 2025 trend equity positions · asset: equities · horizon: weeks · testable: yes · confidence: medium
  ^MT013-C09-5
- **Tom Roble** Despite the headlines, CTAs had less risk in precious metals than assumed; their VaR allocation was much larger in equities and FX.  #mech/risk_management _(added by opus cross-check, time-bound view)_
  > I looked at a CTA report today and there was a much bigger allocation of VAR to equities and FX.
  indicator: CTA VaR allocation by sector · asset: multi · horizon: weeks · conditions: early 2026, after the precious metals selloff · testable: partly - needs CTA risk-allocation reports · confidence: medium
  ^MT013-C09-X1
- **Andrew Beer** In 2025 trend gains came roughly half from gold and half from non-US equities, while rates and currencies produced whipsaw losses.  #mech/cycle_persistence _(added by opus cross-check, time-bound view)_
  > it was making money in gold and non- US equities um was about about half the performance each and then you got whipsaw and and hope you didn't lose too much money in in rates and currencies
  indicator: trend return attribution by sector (2025) · asset: multi · direction: long gold, long non-US equities · horizon: years · conditions: 2025 · testable: yes - sector attribution of CTA indices · confidence: high
  ^MT013-C09-X2

### C10
- **Niels Kaastrup-Larsen** A modern trend follower with variable position sizing sold precious metals as volatility rose, giving up some profit.  #mech/risk_management _(time-bound view)_
  > even though we made most money in in precious metals, we were selling precious metals all year, right?
  indicator: vol-scaled position sizing · asset: commodities · horizon: months · conditions: vol expansion · testable: yes · confidence: medium
  ^MT013-C10-1
- **Niels Kaastrup-Larsen** Stops triggered on Friday execute Monday, so weekend-style gaps can destroy managers who do not cut risk with volatility.  #mech/risk_management _(time-bound view)_
  > you may trigger your signal you may trigger your stop but you may not execute that trade until the next day
  indicator: execution lag in stop-outs (Jan 2026 gold/silver) · asset: commodities · horizon: days · conditions: fast crashes · testable: yes · confidence: medium
  ^MT013-C10-2
- **Niels Kaastrup-Larsen** Managers with static positions and hundreds of markets get little from outliers; to make 50-80% returns you need few markets and a large risk allocation.  #mech/risk_management
  > they often trade three four 500 markets. And therefore any one market even if you don't touch your position size becomes a very small risk allocation in reality
  indicator: number of markets traded · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT013-C10-3
- **Niels Kaastrup-Larsen** Concentrated trend programs create return but are hard to sell given investment committee constraints and strategic allocations.  #mech/risk_management
  > if you really want to have punchy returns and make those 50 60 80% returns yeah then you actually have to have a fairly small set of markets
  asset: multi · horizon: years · testable: partly · confidence: medium
  **Correction (cross-check):** Likely wrong speaker: the 'London CTA manager... difficult to sell to investors' remark is Tom Roble's; Niels replies 'you don't need many investors'. → Tom Roble: concentrated trend programs create return but are hard to sell given investment committee constraints and strategic allocations.
  ^MT013-C10-4
- **Niels Kaastrup-Larsen** Most 2025 trend profits came from metals or select equities, with short Japanese government bonds (JGBs) another profitable trend.  #mech/cycle_persistence _(added by opus cross-check, time-bound view)_
  > a couple of them also in the say short JTBs
  indicator: JGB futures · asset: rates · direction: short JGBs · horizon: years · conditions: 2025, BOJ tightening · testable: yes - JGB trend returns 2025 · confidence: medium
  ^MT013-C10-X1

### C11
- **Tom Roble** Investors whose core risk is equities want asymmetric diversification, which trend delivers better than multi-strategy funds.  #mech/risk_management
  > trend following is really good at diversifying that and so the investors sort of continued fascination with multistrat isn't necessarily meeting the requirements
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT013-C11-1
- **Andrew Beer** Valuable trends occur when fair value changes and informed participants like the asset more at each higher price.  #mech/slow_reaction
  > The valuable trends for CTAs are when it's something's at 10, fair market value is 10, and then the information changes.
  asset: multi · horizon: months · testable: no: conceptual · confidence: high
  ^MT013-C11-2
- **Andrew Beer** Sentiment-driven oscillation without change in fundamental value is noise captured by locals and high-frequency traders, while trend followers get whipsawed.  #mech/slow_reaction
  > the smart money selling at 11, buying at 9, selling at 11, buying at 9
  asset: multi · horizon: days · testable: no · confidence: high
  ^MT013-C11-3
- **Andrew Beer** Fundamental commodity traders waited for CTA signals to trigger selling and bought from them, a cost for CTAs.  #mech/crowding_positioning
  > they waited for the day when CTAs when some signal went off somewhere and CTAs were selling
  indicator: CTA flow · asset: commodities · horizon: days · testable: partly · confidence: medium
  ^MT013-C11-4
- **Andrew Beer** Beer cites his firm's September 2020 move into short Treasuries (and later long gold below $3,000 and short yen near 105-106) as early contrarian calls that illustrate CTA alpha.  #mech/new _(added by map cross-check, time-bound view)_
  > I remember the moment in September of 2020 when we started shorting treasuries
  indicator: early contrarian trend entry · asset: bonds · direction: short Treasuries · horizon: years · conditions: none stated · testable: yes - position history · confidence: medium
  ^MT013-C11-R3

### C12
- **Andrew Beer** Short-term models are whipsawed by sentiment shifts without real change in the state of the world, while long-term models capture lasting shifts such as the move out of US assets.  #mech/slow_reaction
  > the shorter term models are the ones that are going to get whipssawed violently when you have these changes in sentiment like we had last year
  indicator: short vs long trend models · asset: multi · horizon: months · conditions: sentiment swings vs structural shifts · testable: yes · confidence: high
  ^MT013-C12-1
- **Andrew Beer** Risk management should not be conflated with allocating heavily to a zero-Sharpe strategy.  #mech/risk_management
  > if you're going to introduce something into your into your portfolio and allocate a lot of risk to something with a zero sharp ratio, no thanks
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT013-C12-2
- **Andrew Beer** When CTAs de-risk after a vol spike, local traders in that market trade against them, so CTAs pay implementation costs and liquidity dries up.  #mech/crowding_positioning
  > you're not executing at at you know there the liquidity dries up in that market because they can see you coming
  indicator: CTA de-risking impact · asset: multi · horizon: days · conditions: vol spikes in niche markets · testable: partly · confidence: medium
  ^MT013-C12-3
- **Andrew Beer** Adding many non-core markets increases drawdowns during de-risking because of implementation costs.  #mech/risk_management _(time-bound view)_
  > this diversification into a lot of excess positions, you know, non increasingly non-core positions, I think it hurt people after liberation day
  indicator: number of markets · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT013-C12-4
- **Andrew Beer** Backtests understate costs because they ignore being picked off by local traders.  #mech/research_method
  > when you're building these models, you have to make certain assumptions about implementation costs and I don't think most people factor in um uh getting taken advantage of by local traders
  indicator: implementation cost assumptions · asset: multi · testable: yes · confidence: medium
  ^MT013-C12-5
- **Andrew Beer** A futures-based CTA replication can deviate from the hedge funds it tracks by several hundred bp a year (about -500 bp in 2023, large outperformance in 2024-2025), driven by about four sources of variation.  #mech/research_method _(added by opus cross-check)_
  > You know, in 2023, they all went against us and we underperformed by 500 basis points.
  indicator: replication tracking difference vs SG CTA index · asset: multi · horizon: years · testable: yes - annual tracking difference of replication ETFs vs index · confidence: high
  ^MT013-C12-X1
- **Andrew Beer** Slow (weekly) de-risking helped around Liberation Day because the sell-off reversed quickly; faster de-risking sold near the low.  #mech/risk_management _(added by opus cross-check)_
  > we were slow to derisk and and balanced when Trump Trump changed his mind.
  indicator: rebalance frequency of trend portfolio · asset: equities · horizon: weeks · conditions: sharp policy-driven sell-offs that reverse quickly (V-shaped) · testable: yes - compare trend models by rebalance speed in V-shaped reversals · confidence: medium
  ^MT013-C12-X2

### C13
- **Andrew Beer** In the initial April 2025 shock short-term models preserved capital better than long-term ones; they lost later in chop.  #mech/slow_reaction _(time-bound view)_
  > really short-term models were fine during that you know they actually they they actually preserved capital much better than longerterm guys
  indicator: short-term models in April 2025 shock · asset: multi · horizon: weeks · conditions: initial sharp selloffs · testable: yes: SG factor data · confidence: medium
  ^MT013-C13-1
- **Andrew Beer** Allocators fear the bad whipsaw and a Friday loss turning into a worse Monday, but paying for protection costs too much.  #mech/behavioral
  > investor preferences are often to live in paralyzing fear about what a bad lipsaw looks like
  asset: multi · horizon: years · testable: no · confidence: high
  ^MT013-C13-2
- **Andrew Beer** Hedging a long-term trend model with out-of-the-money puts out of fear of tail events is a losing business.  #mech/risk_management
  > let's do a long-term trend model and then and then buy out of the money puts on equities because that's what we're afraid of
  indicator: put overlay on trend · asset: equities · horizon: years · testable: partly · confidence: medium
  ^MT013-C13-3
- **Andrew Beer** Liquid alternative funds returned 2-3% over 15 years with about 200 bp fees while equities rose about 14% a year.  #mech/research_method
  > The returns over 15 years according to Wilshire's data is between two and 3%. And the fee structures on average is about 200 basis points
  indicator: Wilshire liquid alternatives universe · asset: multi · horizon: years · testable: yes: Wilshire data · confidence: high
  ^MT013-C13-4
- **Andrew Beer** Liquid-alt products are launched to feed distribution rather than from investment conviction, which explains poor outcomes.  #mech/behavioral
  > a typical firm has a huge distribution infrastructure to support and they have no view on which is the best product that they're going to launch
  asset: other · horizon: years · testable: partly · confidence: high
  ^MT013-C13-5

### C14
- **Andrew Beer** Products designed by salespeople to meet demand rather than investment merit, like a car designed by the showroom salesman, fail investors.  #mech/behavioral
  > most products that are developed in the space are developed by sales people who think they can sell it over the next year or two
  asset: other · horizon: years · testable: partly · confidence: high
  ^MT013-C14-1
- **Tom Roble** Liquid-alt category data may mix true hedge funds with quasi multi-asset funds labelled multi-strat, so classification matters.  #mech/research_method
  > are we talking about real hedge funds in that data or are we talking about quasi alternatives
  asset: other · testable: yes: classification audit · confidence: medium
  ^MT013-C14-2
- **Tom Roble** Hedge fund industry splits into scalable strategies forming part of tactical asset allocation (like CTAs, with falling costs) and pure alpha that goes in and out of vogue.  #mech/structural_shift
  > strategies that become scalable that form part of a larger longer term tactical asset allocation that you want to have as a core holding like a CTA
  asset: other · horizon: years · testable: no · confidence: medium
  ^MT013-C14-3

### C15
- **Andrew Beer** Multi-manager mutual fund and ETF products failed as a business model.  #mech/structural_shift
  > even Blackstone gave up on that you know I mean Newberg Burman shut down their fault like it was a failed business model
  asset: other · horizon: years · testable: partly · confidence: medium
  ^MT013-C15-1
- **Andrew Beer** QIS/premium providers talk about engineering and research, not realised Sharpe ratios, so due diligence should ask for realised Sharpe over a stated period.  #mech/research_method
  > I kept asking these questions like what's the realized sharp ratio of the strategy for over what period of time and what do you think it's going to be be going forward and why?
  indicator: realised Sharpe ratio · asset: multi · testable: yes · confidence: high
  ^MT013-C15-2
- **Andrew Beer** Allocators should define the signal they want and implement it efficiently, not pick managers by narrative.  #mech/research_method
  > get very very clear about what you're expecting a product to do and how you're expecting to achieve to achieve it
  asset: multi · testable: no · confidence: medium
  ^MT013-C15-3

### C16
- **Niels Kaastrup-Larsen** A replication ETF has large tracking error to the index, so it is better viewed as an alternative-data trend strategy than as a cost saving.  #mech/research_method
  > I feel at least that the tracking error to the index that it's trying to mirror is too large for that
  indicator: tracking error of replication vs SG CTA index · asset: multi · horizon: years · testable: yes: tracking error · confidence: medium
  ^MT013-C16-1
- **Andrew Beer** Standard Life GARS promised equity beta 0.2 with cash plus 5, a top-decile hedge fund result, and was unrealistic though it reached $90 billion.  #mech/research_method
  > Okay, that's a top quartortile maybe a top decile hedge fund portfolio over time.
  indicator: beta 0.2 and cash+5 promise · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT013-C16-2
- **Andrew Beer** Risk premia backtests overstate Sharpe (G10 carry 1.2); live results drop about 75% from backtest.  #mech/research_method
  > G10 currency carry does not have a long-term sharp ratio 1.2. I'm sorry that's that's a back test.
  indicator: G10 carry Sharpe in backtest vs live · asset: fx · horizon: years · testable: yes · confidence: high
  ^MT013-C16-3
- **Andrew Beer** Backtested to live performance decay of risk premia products is about 75%.  #mech/research_method
  > something like 75% or something
  indicator: backtest-to-live decay · asset: multi · horizon: years · testable: yes · confidence: low
  **Correction (cross-check):** Duplicate of MT013-C16-3 (same 75% backtest-to-live decay point). → Merge into MT013-C16-3: risk premia backtests overstate Sharpe (G10 carry 1.2); live results fall about 75% short of backtests.
  ^MT013-C16-4
- **Andrew Beer** A multi-manager mutual fund of hedge fund managers cannot achieve the promised return objectives after costs and constraints.  #mech/research_method
  > a mutual fund that tries to pick six underlying hedge fund managers and hires them in managed accounts is not going to achieve the return objectives
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT013-C16-5
- **Niels Kaastrup-Larsen** Strategies go in and out of favour, so 5-10 years of track record says little about the next 5-10 years; past underperformance does not predict future underperformance.  #mech/research_method _(added by opus cross-check)_
  > Even if you have 5 years of underperformance doesn't mean the next 5 years, the next 10 years won't
  indicator: manager/strategy track record length · asset: multi · horizon: years · testable: yes - persistence of 5-year relative performance across managers · confidence: medium
  ^MT013-C16-X1
- **Andrew Beer** Equity long-short funds with 0.4-0.5 equity beta need more stock-selection alpha than is realistic to overcome mutual fund costs, so they are unlikely to add value.  #mech/research_method _(added by opus cross-check)_
  > equity long short as a as a category if you have a beta of 0.5 or point4 to equities it it's not going to the amount of stock selection alpha and other things you need to do
  indicator: equity long-short beta vs fees · asset: equities · horizon: years · conditions: in mutual fund/liquid alt wrappers with high fees · testable: yes - alpha of liquid equity long-short funds after fees · confidence: high
  ^MT013-C16-X2

### C17
- **Andrew Beer** Capital flows to the largest firms with the largest sales forces, not to the best products.  #mech/behavioral
  > most alternative liquid alternative products are sold not bought.
  asset: other · horizon: years · testable: partly · confidence: high
  ^MT013-C17-1
- **Andrew Beer** Allocators with line-item limits chose AQR for brand, taking idiosyncratic manager risk they did not understand.  #mech/behavioral
  > the reason AQR went to 14 billion in assets in their mutual fund was because a lot of allocators were basically saying it's AQR a it's AQR what can go wrong
  asset: other · horizon: years · testable: partly · confidence: medium
  ^MT013-C17-2

### C18
- **Niels Kaastrup-Larsen** Macro funds use bank QIS indices for thematic bets like curve steepeners, outsourcing execution and financing.  #mech/risk_management
  > global macro hedge funds who want to access some sort of curve steepener or some sort of thematic play for a finite period of time who will use the QIS
  indicator: QIS thematic exposure · asset: rates · horizon: months · testable: no · confidence: medium
  **Correction (cross-check):** Wrong speaker: 'SG has a very active QIS business... often we have global macro hedge funds who want to access some sort of curve steepener' is Tom Roble (SG), not the host. → Tom Roble: macro funds use bank QIS indices for thematic bets like curve steepeners, outsourcing execution and financing.
  ^MT013-C18-1
- **Andrew Beer** Low-cost ETF model portfolios create a market for beta-like alternative indices at low fees.  #mech/structural_shift
  > lowcost ETF model portfolios that that that require things that are look and feel more betalike
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT013-C18-2
- **Andrew Beer** Managed futures exposure should be held as a core allocation, not traded tactically; allocators who want to time something should time another asset.  #mech/behavioral _(added by opus cross-check)_
  > very few allocators actively trade which they should I tell them if you're going to actively trade you you find something else to trade.
  asset: multi · horizon: years · testable: partly - investor flow timing vs buy-and-hold returns of trend funds · confidence: high
  ^MT013-C18-X1

### C19
- **Niels Kaastrup-Larsen** QIS trend-replication products do not publish returns, so cannot be evaluated.  #mech/research_method
  > have no transparency. We have no idea what the returns actually are.
  indicator: QIS transparency · asset: multi · testable: partly · confidence: medium
  ^MT013-C19-1
- **Niels Kaastrup-Larsen** Replication using different methods may not deliver the CTA outcome in all regimes; the last 10 years differ from the first 10 of this millennium.  #mech/research_method
  > when you do things really differently why would you expect to be able to deliver the same outcome
  indicator: replication tracking · asset: multi · horizon: years · conditions: regime dependent · testable: yes · confidence: medium
  ^MT013-C19-2
- **Andrew Beer** Due diligence on bank trend indices should ask when launched and how prior similar indices performed, as many allocators suspended belief.  #mech/research_method
  > when did you actually launch this index right if you if you launched the index three weeks ago then have you launched other indices that look like this how did those do right
  indicator: index launch date and track record · asset: multi · testable: yes · confidence: high
  ^MT013-C19-3
- **Andrew Beer** Calling trend a risk premium is misleading because different designers' trend indices differ greatly.  #mech/research_method
  > risk premium implies that if the three of us design it, it's going to look the same
  indicator: trend index dispersion · asset: multi · testable: yes · confidence: high
  ^MT013-C19-4
- **Niels Kaastrup-Larsen** Kaastrup-Larsen says he is open to surprise both ways: innovative replication structures may outperform for a time, but eventually they may not work in all regimes.  #mech/new _(added by map cross-check)_
  > I'm open to surprise both ways in a sense that yes, there's going to be periods where these innovative structures uh outperform
  indicator: innovative CTA replication structures · asset: multi · direction: n/a · horizon: years · conditions: regime dependence · testable: partly · confidence: medium
  ^MT013-C19-R1

### C20
- **Andrew Beer** After 2007 quant losses the narrative shifted to risk-premia harvesting as permanent, which understated risk.  #mech/behavioral
  > we're just harvesting risk premia that have been around for 70 years and these are permanent features of the market
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT013-C20-1
- **Andrew Beer** Two long-term trend models with correlation 0.8 can still be 20 points apart in a year, so manager risk is high.  #mech/research_method
  > manager risk as we talk about is very very high in this space
  indicator: dispersion across trend models · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT013-C20-2
- **Andrew Beer** Sophisticated allocators now combine several banks' flavours of trend to diversify design risk.  #mech/risk_management
  > how as an investor how how is an allocator do I want to put these together into a package thereby becoming almost like an outsourced uh uh portfolio manager
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT013-C20-3
- **Niels Kaastrup-Larsen** Strategies that do not predict but profit from change may do well in 2026 given the amount going on in the world.  #mech/cycle_persistence _(time-bound view)_
  > maybe this could be a good year for us
  asset: multi · horizon: months · testable: no · confidence: low
  ^MT013-C20-4

