---
source_id: MT108
title: "Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12"
date: 2024-12-29
channel: "Top Traders Unplugged"
url: 
words: 7763
claims: 44
added_by_crosscheck: 10
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Tilman (J8 Capital co-founder)", "Vishal (J8 head of trading and portfolio management)", "Moritz Seibert (host, Open Interest series)"]
tags: [source, layer0]
---
# Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12

**Speakers:** Tilman (J8 Capital co-founder); Vishal (J8 head of trading and portfolio management); Moritz Seibert (host, Open Interest series)

**Summary:** J8 Capital runs a decomposed multi-strategy program (trend in commodities, FX, bonds; curve arbitrage, FX carry, inventory, vol term structure) risk-weighted by inverse realised vol at 10 percent target. Redwood adds an intraday strategy with low correlation to CTA indices; costs are the key hurdle.

**Approach:** trend following, carry, term structure arbitrage, multi-strategy, short-term trading

**Cross-check completeness estimate of first read:** 0.89 - first reader caught the J8 decomposition philosophy, trend/carry/arbitrage rules, risk weighting, leverage and Redwood points; missed a few mechanisms (outright vs relative VIX trade, diversification-to-leverage logic, holding period/universe of Redwood, equity exclusion caveat, cost components) and mis-attributed one answer to the host.

## Argument map

**Episode thesis:** J8 Capital's Tilman argues that a systematic futures programme should be built by decomposing return drivers into simple single-purpose sub-strategies (commodity, currency and bond trend; curve arbitrage; FX carry; inventory; volatility term structure), weighted by inverse realised volatility and scaled to a 10% target volatility, because diversification across models adds a free diversification gain and keeps the source of returns transparent. Vishal adds the Redwood intraday strategy (breakouts in volatility terms, 12 liquid futures including equity indices) as a return driver with near-zero correlation to CTA indices, while host Moritz Seibert presses on the roughly 10% a year execution-cost hurdle that such short-term trading must overcome.

### Tilman (Co-founder of J8 Capital Management (London systematic hedge fund; Global Absolute Return strategy live since January 2015); civil engineer by training with a PhD in project-finance risk; formerly structured derivatives (Parkplace, UBS, AIG Financial Products, Dow Jones-AIG Commodity Index))
Fingerprint: #approach/trend_following #approach/carry #approach/relative_value_arbitrage #approach/commodity_fundamentals #approach/diversification_risk_parity #approach/position_sizing_vol_target #approach/portfolio_construction_stacking #approach/volatility_options
_Speaker note: Auto-captions garble names ('Tilman saxs', 'Morits seber'); the surname is not given reliably. Referred to as Tilman (J8 co-founder). Two of the ledger's speaker labels for Moritz's questions were fixed per its corrections._

**Worldview premises**
- Translating economic fundamentals in commodities into rules-based strategies removes the emotional and behavioural biases of discretionary traders. _[experience, stated; support: His experience building the Dow Jones-AIG commodity index and rules-based strategies.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C02-1|C02-1]])
- Besides diversification across asset classes, one can diversify across return drivers and models, and weighting signals by risk gives an additional diversification boost ('no free lunch other than diversification'). _[theoretical, stated; support: Appeal to Fama and French's no-free-lunch view (caption garbled); no data.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C03-1|C03-1]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C03-R1|C03-R1]])
- Decomposing returns into one sub-strategy per return driver, then combining them in a risk-based portfolio, is better than one big model with filters because it keeps transparency on where returns come from and lets each driver be refined separately. _[theoretical, stated; support: Design argument; contrast with how 'many CTAs' build trend models with filters.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C03-2|C03-2]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C03-3|C03-3]])
- Each sub-strategy should have a single degree of freedom and simple parameters: the product is complex but its parts are simple. _[theoretical, stated; support: Design choice.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C03-4|C03-4]])
- Equity indices have survival bias (losers drop out), which truncates the signal that a trend follower wants to carry through the whole economic cycle of an underlying; equities also depend on rates, FX and commodity inputs already traded, so adding equity trend duplicates exposure. _[theoretical, stated; support: Reasoning from index construction; adding equity index futures did not improve J8's long-term trend programme in tests.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C04-3|C04-3]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C04-4|C04-4]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-2|C05-2]])
- Commodities have clear supply and demand fundamentals, while shares are mainly speculative instruments once issued. _[theoretical, stated; support: Economic argument.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-1|C05-1]])
- The equity exclusion applies to the slow trend programme only; equity index futures make sense when traded differently (as in Redwood), so the redundancy argument is horizon-specific. _[theoretical, stated; support: He defers to Vishal's short-term system.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-X1|C05-X1]])
- A short-term momentum strategy hedges the long-term trend programme's drawdowns during reversals. _[experience, stated; support: Design intent; his recently added cross-asset short-term momentum.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C04-2|C04-2]])
- Two styles of carry/arbitrage: arbitraging time along a futures curve (commodity and volatility term structure) versus arbitraging between markets (FX carry, commodity inventory/curvature selection). _[theoretical, stated; support: Conceptual taxonomy.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-X2|C05-X2]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-3|C05-3]])
- Futures curve shape is a real-time proxy for inventory because inventory data is delayed, revised and imprecise; curvature indicates under- or oversupply, so go long undersupplied and short oversupplied commodities. _[theoretical, stated; support: Reasoning from curve shape; no test shown.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-5|C05-5]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-1|C06-1]])
- Rolling front-month VIX futures loses about 50-60% a year in roll costs; shorting it arbitrages the roll out, but the short has catastrophic tail risk in spikes (for example a 300% jump) and must be hedged and managed. J8 trades a relative-value trade on the VIX/VSTOXX futures term structure rather than outright short volatility. _[empirical, stated; support: Long-run behaviour of rolling front-month VIX futures; the figure is from his recollection.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-2|C06-2]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-3|C06-3]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-X1|C06-X1]])
- Realised volatility is stable over time while correlations and recent performance are unstable, so allocate by inverse realised volatility (equal risk) and use no correlation or performance tilts; this gave the most stable overall return. _[empirical, stated; support: J8's own testing; no figures shown.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-4|C06-4]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-5|C06-5]])
- Combining many uncorrelated sub-strategies lowers portfolio volatility, and because futures are unfunded, exposure can be levered up to restore the 10% target volatility, converting diversification into return; realised volatility was 10.26% over 10 years, and margin is about 6-12% of equity. _[empirical, stated; support: Own realised volatility over ten years; 1 million cash controls about 30 million of notional.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-6|C06-6]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-X2|C06-X2]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C07-1|C07-1]])
- A simple index built from survey answers (about 120 replies over three years from brokers, CTAs, consultants and investors) explained about 80% of CTA index returns: a diversified, risk-weighted 12-month momentum portfolio. J8 sees itself as half traditional CTA and half alternative risk premia, so no single benchmark fits. _[empirical, stated; support: His own surveys at J8's founding; the index and the 80% figure are not shown.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C07-2|C07-2]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C07-3|C07-3]])
- The trend signal method is the same across commodities, currencies and bonds, with market-specific parameters. _[experience, stated; support: J8 design.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C04-1|C04-1]])
- FX carry (long high-yield, short low-yield currencies against USD) is reversed after a sell-off signalled by short-term realised volatility. _[experience, stated; support: J8 rule.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-4|C05-4]])
- J8's objective is to give investors access to systematic investing in a broad, diversified and holistic way; it would add outside traders only if they offer something it has not considered. _[institutional, stated; support: Business description.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C11-R2|C11-R2]])

**Chain: Decomposition and risk-weighting to a stable return**
1. Split strategies by return driver (one sub-strategy each, one degree of freedom) → Transparent and separately refinable sources of return: No big model with filters to obscure where returns come from. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C03-2|C03-2]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C03-3|C03-3]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C03-4|C03-4]])
2. Weight sub-strategies by inverse realised volatility → Equal-risk portfolio with the most stable overall return: Realised volatility is stable while correlations and recent performance are not. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-4|C06-4]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-5|C06-5]])
3. Diversified, lower-volatility combination of unfunded futures → Lever to the 10% target volatility, turning diversification into return: Unfunded futures let exposure be scaled; margin is only 6-12% of equity. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-6|C06-6]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-X2|C06-X2]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C07-1|C07-1]])
- Evidence: Ten-year realised volatility of 10.26% against the 10% target; no return, Sharpe or drawdown figures disclosed.
- Fails when: Not stated; the stability of realised volatility is the key assumption.

**Chain: Why equities are excluded from slow trend following**
1. Equity indices drop their losers (survival bias) → Signals are truncated, so trend following cannot ride a full cycle as in oil or gold: Constituent selection removes the down-leg. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C04-3|C04-3]])
2. Equities rely on interest rates, FX and commodity inputs → Equity trend signals are triggered by moves in markets already traded (redundancy): Same underlying drivers. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C04-4|C04-4]])
3. Tests of adding equity index futures → No improvement to the long-term trend programme: Empirical finding. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-2|C05-2]])
- Evidence: In-house testing, no results shown.
- Fails when: Equity index futures can add value if traded differently (Redwood), so the exclusion is horizon-specific.

**Chain: Curve shape as a carry and inventory signal**
1. Price of a far contract versus a near one on the same commodity → Curve slope or curvature indicates under- or oversupply: Official inventory data are delayed, revised and imprecise. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-1|C06-1]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-5|C05-5]])
2. Long undersupplied and short oversupplied commodities → Profits when oversupplied prices fall and undersupplied rise: Supply imbalance corrects through price. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-5|C05-5]])
3. Long the longer end and short the shorter end of the curve → Harvests roll yield; the short end is closed when the curve turns unsustainable: Natural built-in risk management. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-3|C05-3]])
- Evidence: Reasoning only; no returns shown for these sleeves.
- Fails when: Not stated.

**Chain: Volatility term-structure arbitrage**
1. Rolling front-month VIX futures → About 50-60% annual roll losses: Contango and roll costs. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-2|C06-2]])
2. Short front month, long back (VIX/VSTOXX) → Earns roll-yield differentials without depending on the equity risk premium: Relative-value rather than outright short volatility. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-X1|C06-X1]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-3|C05-3]])
3. Volatility spike (for example 300%) → Catastrophic loss on the short leg: Short volatility carry has tail risk; must be hedged and managed. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-3|C06-3]])
- Evidence: Behaviour of rolling VIX futures (his figure); no details of the hedge.
- Fails when: A volatility spike that hits the short leg harder than the long leg.

**Decision process**
- [signal] Same trend method across commodities, currencies and bonds, with market-specific parameters; add a cross-asset short-term momentum sleeve to hedge reversals.. Why: Consistent logic with individual parameterisation; short-term sleeve hedges long-term drawdowns in reversals. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C04-1|C04-1]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C04-2|C04-2]])
- [universe] Exclude equity indices from the long-term trend programme (survival bias, redundancy); include them only in the short-term Redwood strategy.. Why: Truncated signals and duplicated exposure. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C04-3|C04-3]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C04-4|C04-4]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-2|C05-2]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-X1|C05-X1]])
- [signal] Run separate sleeves: commodity term-structure arbitrage; inventory selection from curve shape; FX carry reversed on a sell-off signalled by short-term realised volatility; VIX/VSTOXX term-structure relative value.. Why: One return driver per sub-strategy. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-3|C05-3]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-4|C05-4]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-5|C05-5]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-X1|C06-X1]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-1|C06-1]])
- [sizing] Allocate across strategies by inverse realised volatility (equal risk); no correlation or performance tilts.. Why: Realised volatility is stable, correlations and recent performance are not. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-4|C06-4]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-5|C06-5]])
- [sizing] Scale overall exposure to a 10% target volatility using unfunded futures (margin about 6-12% of equity, so 1 million cash controls about 30 million notional).. Why: Diversification lowers volatility and leverage restores the target. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-6|C06-6]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-X2|C06-X2]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C07-1|C07-1]])
- [risk] Hedge and manage the tail risk of short volatility carry.. Why: Spikes could be catastrophic. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-3|C06-3]])
- [portfolio] Benchmark as half CTA, half alternative risk premia, since no single index fits.. Why: CTA universe ~ diversified risk-weighted 12-month momentum; J8 adds carry and arbitrage. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C07-2|C07-2]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C07-3|C07-3]])

**Evidence style:** Design reasoning and in-house testing; ten-year realised volatility of 10.26% is the only performance statistic. No returns, Sharpe, drawdowns, or test results are shown, and the survey-based benchmark index is described without detail.

**Views at the time**
- (2024-12 (upload 2024-12-29; Open Interest 12)) J8 is growing both the investment management and a hosting (incubator) business, aims to launch a fund vehicle for global professional investors, and is raising seed capital; it would allocate to an outside trader only if the idea is something new.. Reasoning: Business plan: the managed accounts run about 350 (units unclear), with own research the core. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C11-R2|C11-R2]])
- (2024-12) J8's combined programme is a cross between traditional CTA and alternative risk premia, so benchmarking against a multi-strategy hedge fund or a CTA index alone does not fit.. Reasoning: Half CTA-like momentum, half carry and arbitrage; heavy commodity focus. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C07-3|C07-3]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C07-2|C07-2]])

### Vishal (Head of trading and portfolio management at J8 Capital (joined December 2020); previously built quantitative short-term trading models at ION Asset Architecture and ARB Trading Group; IIT engineering degree)
Fingerprint: #approach/short_term_systematic #approach/trend_following #approach/costs_execution #approach/market_internals_leading #approach/diversification_risk_parity #approach/position_sizing_vol_target
_Speaker note: Auto-captions; first name only is given. His answer on Redwood's correlation to the short-term traders index was attributed to the host in the ledger and is corrected here. His numbers on costs are explicitly rough._

**Worldview premises**
- Redwood trades intraday breakouts measured in volatility terms within a context of trend, volatility and positioning; holding periods run from a few hours to a few days (3-5 days at most, mostly same day or next day), sampled every 3-5 minutes. _[experience, stated; support: Description of own system; no performance shown.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-1|C08-1]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-X1|C08-X1]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-R3|C08-R3]])
- Short-term trading requires highly liquid futures for cheap entry and exit, so Redwood trades 12 big futures across all asset classes including equity indices. _[experience, stated; support: Design constraint.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-2|C08-2]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-X1|C08-X1]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C09-2|C09-2]])
- The short-term strategy has low or negative correlation to CTA indices and improved risk-adjusted return when added to the main programme in simulations; its correlation with the SG Short Term Traders Index is practically zero. _[empirical, stated; support: Simulation results ('we did a lot of simulations'); no numbers beyond 'very close to 0'. (Corrected from the host to Vishal.)]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-3|C08-3]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-4|C08-4]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-R4|C08-R4]])
- Short-term trading is not simply counter-trend: each strategy uses its own horizon context including volatility, and a longer-term mean-reversion view may coincide with a prevailing short-term trend. _[theoretical, stated; support: Design philosophy.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C09-1|C09-1]])
- Short-term systems get a higher Sharpe at similar or slightly better returns, but the challenge is avoiding whipsaws from noise and overtrading, so exposure and sensitivity must be controlled. _[experience, stated; support: Own results; no figures.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C09-3|C09-3]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C10-2|C10-2]])
- Intraday trading needs 24-hour automated infrastructure (FIX execution, alerts, monitoring desks in India and the UK, hybrid Python/Julia/Java), an operational overhead. _[institutional, stated; support: Own set-up.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C10-3|C10-3]])
- Performance is not highly sensitive to small changes in costs, though he has no exact numbers on hand. _[experience, stated; support: Multiple brokers; recollection only.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C09-4|C09-4]])
- Roughly 700 round trips per million per month (about 8,000 per year) across 12 futures. _[empirical, stated; support: Own figure; the 'per million' basis is not defined.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C09-2|C09-2]])

**Chain: Why an intraday strategy diversifies a CTA programme**
1. Intraday breakouts defined in volatility terms and context of trend, volatility and positioning → Return stream that differs in horizon and approach from slow trend following: Different time frame and trade logic. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-1|C08-1]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C09-1|C09-1]])
2. Low or negative correlation to CTA indices → Improved risk-adjusted return in the combined programme: Additional uncorrelated return driver. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-3|C08-3]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-4|C08-4]])
3. Quick reaction to changes → Hedge during reversals where long-term trend suffers (Tilman's point): Short-term system exits and reverses early. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C04-2|C04-2]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C09-3|C09-3]])
- Evidence: Simulations by J8; correlation to the SG Short Term Traders Index about zero.
- Fails when: Costs and overtrading overwhelm the edge; whipsaws in noisy markets.

**Decision process**
- [universe] Trade 12 highly liquid futures across commodities, currencies, bonds and equity indices.. Why: Cheap entry and exit are needed for short-term trading. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-2|C08-2]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-X1|C08-X1]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C09-2|C09-2]])
- [signal] Sample every 3-5 minutes; trade breakouts measured in volatility and in the context of trend, volatility and positioning; long and short.. Why: React quickly to big moves; context decides whether a move is trend or reversion. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-1|C08-1]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-R3|C08-R3]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C09-1|C09-1]])
- [execution] In-house FIX execution infrastructure with alerts and 24-hour monitoring desks in India and the UK; multiple brokers.. Why: Intraday trading has no off hours; glitches must be caught. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C10-3|C10-3]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C09-4|C09-4]])
- [risk] Control exposure and system sensitivity to avoid overtrading and whipsaws.. Why: Overtrading magnifies transaction costs in the short-term space. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C09-3|C09-3]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C10-2|C10-2]])

**Evidence style:** Simulations and practitioner experience; he gives correlation to the short-term index (~0), Sharpe 'higher' and returns 'par or slightly better' without numbers, and says he lacks cost figures to hand.

**Views at the time**
- (2024-12) The short-term Redwood strategy adds a different return driver that blends well with the slow long-term programme.. Reasoning: Low or negative correlation to CTA indices; higher Sharpe in simulations. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-3|C08-3]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-4|C08-4]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C09-3|C09-3]])

### Moritz Seibert (Host of the Open Interest series (Top Traders Unplugged); systematic trading practitioner)
Fingerprint: #approach/costs_execution #approach/short_term_systematic #approach/trend_following #approach/research_robustness_overfitting
_Speaker note: Caption 'Moret/Morits seber'. He asks questions but also supplies a cost calculation; two of his turns were mis-assigned in the ledger (the Redwood correlation answer is Vishal's, not his)._

**Worldview premises**
- For a non-HFT futures trader, the all-in cost per contract (commission about 0.75, exchange fee 0.50, clearing fee 0.50, plus spread, slippage and market impact) is roughly 5-6 dollars. _[experience, stated; support: Back-of-envelope sum; Vishal accepts $6 as fair if it includes bid/offer.]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C10-X1|C10-X1]])
- At roughly 6 dollars per contract and about 8,000 round turns per million per year, execution cost is around 10% a year (he states 10.8%), a very high hurdle that a short-term strategy must beat with a very accurate system. _[empirical, stated; support: His arithmetic, which does not fully reconcile (8,000 x 2 x $6 would be about 9.6%).]_ ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C10-1|C10-1]])

**Chain: Cost hurdle for high-turnover systems**
1. About 8,000 round turns per million per year at around $6 a contract → Roughly 10% annual execution drag: Costs scale linearly with turnover. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C10-1|C10-1]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C10-X1|C10-X1]])
2. A cost drag of about 10% a year → Risk-adjusted returns before cost must be very high for the strategy to net a profit: The system has to recover the drag and then some. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C10-1|C10-1]])
- Evidence: Back-of-envelope with unit costs; Vishal does not give his own number.
- Fails when: Per-contract costs or turnover are lower than assumed (Vishal says costs are not substantial but has no figures).

**Evidence style:** Back-of-envelope arithmetic and probing questions; not a source of strategy claims.

**Views at the time**
- (2024-12) The transaction-cost hurdle for a high-turnover intraday futures strategy is roughly 10% a year, so the strategy must be extremely accurate.. Reasoning: About 8,000 round turns per million and $6 per contract. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C10-1|C10-1]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C10-X1|C10-X1]])

### Disagreements
- **Equity indices in a trend programme**: Tilman: Excluded from the slow trend programme because of survival bias and redundancy with rates, FX and commodities; adding them did not improve results. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C04-3|C04-3]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C04-4|C04-4]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-2|C05-2]]); Vishal: Redwood trades equity indices (among all asset classes) because it works on intraday breakouts in liquid futures; Tilman concedes this is sensible when traded differently. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-X1|C08-X1]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-X1|C05-X1]])
- **How binding is the cost hurdle for short-term trading?**: Moritz Seibert: About 10% a year in execution cost (at about 8,000 round turns per million and $6 a contract); an extremely good system is needed to recover it. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C10-1|C10-1]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C10-X1|C10-X1]]); Vishal: Agrees with the point and the need to avoid overtrading, but says performance is not highly sensitive to small cost changes and he lacks exact numbers; says he controls exposure to avoid overtrading. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C09-4|C09-4]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C10-2|C10-2]])
- **Which benchmark fits J8?**: Moritz Seibert: Asks whether J8, with eight strategies across styles and holding periods, should be benchmarked against multi-strategy hedge funds rather than CTAs. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C07-3|C07-3]]); Tilman: Neither fits: the CTA universe is essentially a diversified risk-weighted 12-month momentum portfolio (his survey index explained about 80% of CTA index returns); J8 is about 50% traditional CTA and 50% alternative risk premia ('CTA plus'), heavily commodity-focused. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C07-2|C07-2]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C07-3|C07-3]])

### Gaps and conflicts
- No returns, Sharpe ratios, drawdowns or correlations are disclosed for the programme or for Redwood; the only numbers are the 10.26% realised volatility over ten years and the near-zero correlation to the short-term traders index. Redwood's evidence is simulation. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-6|C06-6]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-3|C08-3]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-4|C08-4]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-R4|C08-R4]])
- The cost arithmetic does not reconcile: 8,000 round turns x 2 contracts x $6 is about 9.6%, not 10.8%; and 700 round trips per month times 12 is 8,400. Treat 10.8% as a rough figure of about 10% a year; 'per million' is not defined (capital or notional). ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C10-1|C10-1]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C09-2|C09-2]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C10-X1|C10-X1]])
- Vishal says costs matter little yet gives no numbers, while the host's calculation suggests a very large drag; the two views are not reconciled. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C09-4|C09-4]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C10-1|C10-1]])
- The 80% explanatory power of the survey-based 'CTA index' is asserted without the index definition or sample period. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C07-2|C07-2]])
- The 50-60% a year loss from rolling VIX futures and the survival-bias argument for equities are stated as facts without data; the survival-bias argument also applies to commodity index constituents of the benchmark indices only weakly. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C06-2|C06-2]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C04-3|C04-3]])
- Tilman says adding equity index futures 'did not improve' the long-term programme while giving three a priori reasons for excluding them; the test results are not shown. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C05-2|C05-2]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C04-3|C04-3]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C04-4|C04-4]])
- Ledger attribution fixes applied: the near-zero correlation answer (C08-4) is Vishal's; the cost arithmetic (C10-1) is the host's and is only approximate. ([[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C08-4|C08-4]], [[MT108 - Mastering Trend Following, Arbitrage, and Carry with J8 Capital - Open Interest 12#^MT108-C10-1|C10-1]])

### Forward-looking inputs (reader synthesis)
(reader) The speakers give almost no forward-looking market inputs. Inputs their rules use: futures curve shape (slope and curvature) as an inventory and carry signal; short-term realised volatility as the trigger to reverse FX carry; realised volatility of each sub-strategy for weights and the 10% target; intraday volatility-scaled breakouts in a trend, volatility and positioning context. Horizon ranges from hours to days (Redwood) to 12-month momentum (slow programme).

### Reader inferences (not stated by the speakers)
- (reader) The 'decomposition' design implies that each sleeve should be separately testable; a replication or adoption study could check whether the equal-risk combination beats each sleeve and a single filtered model, which J8 does not show.
- (reader) The claim that realised volatility is stable while correlations are not is the key assumption behind inverse-volatility weights and the 10% target; it is testable on sleeve returns, especially around volatility spikes.
- (reader) The cost-hurdle exchange implies that net-of-cost Sharpe of an intraday strategy depends on turnover per unit of capital, so capital-based and notional-based 'per million' definitions give different drags.
- (reader) Tilman's reasons for excluding equities (survival bias, redundancy, speculative nature) rest on structure rather than evidence; a test of equity trend after controlling for rates, FX and commodity trends could check the redundancy claim.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, host and guest bios |
| C02 | 1 | background of both guests, why systematic |
| C03 | 4 | GARS philosophy, decomposition into single return drivers |
| C04 | 4 | trend rules across markets, why no equities |
| C05 | 5 | equities exclusion, arbitrage and carry strategies |
| C06 | 6 | VIX term structure, risk allocation, target vol |
| C07 | 3 | leverage and margin, benchmark question, CTA nature |
| C08 | 4 | Redwood short-term strategy and diversification |
| C09 | 4 | intraday sampling, turnover, performance |
| C10 | 3 | transaction cost math, infrastructure |
| C11 | 0 | programming languages, business outlook, outro |
| C12 | 0 | outro |

## Claims

### C02
- **Tilman (J8 co-founder)** Translating economic fundamentals in commodities into rules-based strategies removes the emotional and behavioral biases of discretionary traders.  #mech/behavioral
  > translate those into a systematic strategy allows to take out all the discretionary emotional behavioral Finance aspects
  asset: commodities · testable: partly: compare rules vs discretionary results · confidence: medium
  ^MT108-C02-1

### C03
- **Tilman (J8 co-founder)** Beyond asset-class diversification, diversify across return drivers and models and weight signals by risk for an extra diversification gain.  #mech/risk_premium
  > you can also diversify AC cross model risk and if you if you wait the signals according to the risk assigned to a signal that you get an additional diversification boost
  indicator: risk-weighted signal combination · asset: multi · testable: yes: compare to asset-class-only diversification · confidence: medium
  ^MT108-C03-1
- **Tilman (J8 co-founder)** Build one sub-strategy per return driver (e.g. commodity trend, term-structure arbitrage, inventory) then combine in a risk-based portfolio, instead of one big model with filters.  #mech/risk_management
  > we decomposed all those different possible return drivers within the market create single strategy for each single return driver and risk component that we want to extract
  indicator: sub-strategy decomposition · asset: multi · testable: partly · confidence: medium
  ^MT108-C03-2
- **Tilman (J8 co-founder)** Decomposition keeps transparency on where returns come from and lets managers refine each risk driver separately.  #mech/research_method
  > instead of putting everything into one big modelist strategy where one may lose the oversight of where actually R return will dra on come from we decompose it
  asset: multi · testable: partly · confidence: medium
  ^MT108-C03-3
- **Tilman (J8 co-founder)** Each sub-strategy has one degree of freedom and simple parameters, so the overall product is complex but its parts are simple.  #mech/research_method
  > each single sub strategy that we construct therefore really consists of only one single uh degree of freedom
  asset: multi · testable: partly · confidence: medium
  ^MT108-C03-4
- **Tilman** Tilman invokes 'no free lunch other than diversification' (attributed in the caption to Fama and French) as the basis for diversifying across models and return drivers.  #mech/new _(added by map cross-check)_
  > there's no no free lunch in capital markets other than diversification
  indicator: n/a · asset: multi · horizon: n/a · conditions: Portfolio construction across return drivers · testable: partly: diversification benefit of risk-weighted sleeves · confidence: medium
  ^MT108-C03-R1

### C04
- **Tilman (J8 co-founder)** Same trend signal method across commodities, currencies and bonds but market-specific parameters.  #mech/slow_reaction
  > each single Market has their own parameterization so we look at each markers individually
  indicator: trend signal parameters · asset: multi · testable: yes: compare market-specific vs common parameters · confidence: high
  ^MT108-C04-1
- **Tilman (J8 co-founder)** A short-term momentum strategy hedges long-term trend drawdowns during reversals.  #mech/slow_reaction
  > it kicks in with returns and with with a hedge component where our long-term strategies may suffer draw Downs during reversal periods
  indicator: short-term momentum · asset: multi · horizon: days · conditions: trend reversal periods · testable: yes · confidence: medium
  ^MT108-C04-2
- **Tilman (J8 co-founder)** Equity indices have survival bias (losers removed) that truncates signals, so equities are excluded from long-term trend following.  #mech/structural_shift
  > you do have a survival bias within those indices which distorts let's say the long-term nature of a trend following approach
  indicator: equity index survivorship · asset: equities · horizon: years · testable: partly · confidence: medium
  ^MT108-C04-3
- **Tilman (J8 co-founder)** Equities depend on rates, FX and commodity inputs already traded, so adding equity trend duplicates exposure.  #mech/crowding_positioning
  > we want to avoid redundancy effects or resonance Effects by trading equities on top that will just be triggered by movements in the underly markets which we trade already anyways
  asset: multi · testable: partly: correlation of equity trend to other sleeves · confidence: medium
  ^MT108-C04-4

### C05
- **Tilman (J8 co-founder)** Commodities have clear supply and demand fundamentals; shares are mainly speculative instruments once issued.  #mech/structural_shift
  > whereas a commodity for example is uh a real input material into uh commod to into production into the economic uh life cycle so there's clear demand and Supply
  asset: commodities · testable: no · confidence: low
  ^MT108-C05-1
- **Tilman (J8 co-founder)** Adding equity index futures did not improve their long-term trend program.  #mech/slow_reaction
  > in our long-term long-term uh slow momentum or Trend following approach um we did not find any added value by adding Equity indes to our PL
  indicator: equity trend added value · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT108-C05-2
- **Tilman (J8 co-founder)** Term-structure arbitrage harvests roll yield between long and short ends of the futures curve, closing the short end when the curve turns unsustainable.  #mech/risk_premium
  > to profit from the RO yield differentials of the Futures along the term structure
  indicator: futures curve roll yield · asset: commodities · horizon: months · testable: yes · confidence: medium
  ^MT108-C05-3
- **Tilman (J8 co-founder)** FX carry (long high-yield, short low-yield vs USD) is reversed after a sell-off signalled by short-term realised volatility.  #mech/risk_premium
  > we reverse the trades when we observe a sell off in the market based on short-term realized volatility
  indicator: FX carry; realised volatility · asset: fx · direction: exit carry on vol spike · horizon: weeks · conditions: risk-off sell-off · testable: yes · confidence: medium
  ^MT108-C05-4
- **Tilman (J8 co-founder)** Commodity curvature indicates under- or oversupply; long undersupplied and short oversupplied commodities.  #mech/risk_premium
  > going long the under supplied one and short the oversupplied one because you would expect an oversupplied Mar surprises to fall in under supplied Mar prices to increase
  indicator: futures curve shape (December vs September) · asset: commodities · direction: long backwardation, short contango · horizon: months · testable: yes · confidence: medium
  ^MT108-C05-5
- **Tilman (J8 co-founder)** The exclusion of equity indices applies only to J8's slow trend program; equity index futures can make sense when traded differently (the short-term Redwood system trades them), so the redundancy argument is horizon-specific.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > that is not to say the trading Equity indices does not make sense if you trade them differently
  indicator: equity index futures in slow trend vs short-term strategy · asset: equities · conditions: slow multi-month trend program · testable: yes - add equities to short-term vs long-term systems and compare · confidence: medium
  ^MT108-C05-X1
- **Tilman (J8 co-founder)** J8 separates two carry/arbitrage styles: arbitraging time along a futures curve (commodity term structure, volatility term structure) versus arbitraging between markets (FX carry, commodity inventory/curvature selection).  #mech/risk_premium _(added by sonnet-xhigh cross-check)_
  > here we Arbitrage time when it comes to carry trade in caros scenes and the inventory picker in commodi there we Arbitrage between asset classes
  indicator: term-structure vs cross-market carry · asset: multi · testable: partly - classification of carry strategies · confidence: low
  ^MT108-C05-X2

### C06
- **Tilman (J8 co-founder)** Use futures curve shape as a real-time inventory proxy because inventory data is delayed, revised and imprecise.  #mech/research_method
  > inventory fundamental inory data that is often delayed and then also subject to Corrections
  indicator: inventory data vs curve slope · asset: commodities · testable: yes · confidence: medium
  ^MT108-C06-1
- **Tilman (J8 co-founder)** Rolling front-month VIX futures loses about 50-60 percent a year from roll costs, so a short position can arbitrage it out.  #mech/risk_premium
  > you have annualized losses of around 50 60% per Anon which are purely Rong losses
  indicator: VIX futures roll · asset: other · direction: short VIX front month via term structure · horizon: years · testable: yes: VIX futures roll return · confidence: medium
  ^MT108-C06-2
- **Tilman (J8 co-founder)** Short volatility carry has catastrophic tail risk in spikes, so it must be hedged and managed.  #mech/risk_management
  > if you go short the FR month of volatility and then you see a 300% volatility spike in the DI can completely be catastrophic event to your entire portfolio
  indicator: VIX spike · asset: other · horizon: days · conditions: vol spike · testable: yes · confidence: high
  ^MT108-C06-3
- **Tilman (J8 co-founder)** Allocate across strategies by inverse realised volatility (equal risk), which gave the most stable overall return.  #mech/risk_management
  > if we simply take the inverse of the realized volatility of each of the systems and then and then uh weighted proportionately so essentially equal risk weighted uh asset allocation
  indicator: inverse realised volatility · asset: multi · testable: yes · confidence: high
  ^MT108-C06-4
- **Tilman (J8 co-founder)** Realised volatility is stable while correlations and recent performance are unstable, so no correlation or performance tilts.  #mech/research_method
  > the realized volatility between assets is fairly stable over time whereas of course um correlations or shortterm all performance of certain strategies
  indicator: realised vol vs correlation stability · asset: multi · testable: yes · confidence: high
  ^MT108-C06-5
- **Tilman (J8 co-founder)** Futures are unfunded, so scale exposure to a 10 percent target volatility (realised 10.26 percent over 10 years).  #mech/risk_management
  > we scale the exposure of our futures to achieve a realized Target volatility of 10%
  indicator: target volatility · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT108-C06-6
- **Tilman (J8 co-founder)** J8's volatility strategy is a relative-value trade along the VIX/VSTOXX futures term structure (short front, long back) rather than outright short volatility, so it earns roll-yield differentials without depending on the equity risk premium.  #mech/risk_premium _(added by sonnet-xhigh cross-check)_
  > that strategy is purely long short on the T structure and it does not go WR the VIX Index
  indicator: VIX and VSTOXX futures term structure · asset: other · direction: short front, long back months · conditions: needs hedging against volatility spikes · testable: yes - roll-yield spread returns testable · confidence: medium
  ^MT108-C06-X1
- **Tilman (J8 co-founder)** Combining many uncorrelated sub-strategies lowers portfolio volatility, and because futures are unfunded the exposure can be levered up to restore the 10% target volatility, so diversification can be converted into return.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > you already have a super Diversified return stream um and and and the return and the volatility gets lower and lower and lower
  indicator: portfolio volatility vs strategy count; leverage · asset: multi · conditions: unfunded instruments, adequate margin · testable: yes - diversification gain converted via leverage · confidence: medium
  ^MT108-C06-X2

### C07
- **Tilman (J8 co-founder)** At 10 percent target vol, margin to equity is about 6-12 percent, so 1 million cash controls roughly 30 million of notional.  #mech/liquidity_flows
  > we just need to use between let's say six and 10 sometimes 12% margin Equity
  indicator: margin to equity · asset: multi · testable: yes · confidence: high
  ^MT108-C07-1
- **Tilman (J8 co-founder)** A simple index built from survey answers explained about 80 percent of CTA index returns: diversified, risk-weighted 12-month momentum.  #mech/slow_reaction
  > this index model broadly to let's say 80% of its returns broadly mimic or go or are similar to uh popular CTA Benchmark Ines
  indicator: 12-month momentum risk-weighted · asset: multi · horizon: years · testable: yes: replicate with simple 12-month momentum · confidence: medium
  ^MT108-C07-2
- **Tilman (J8 co-founder)** J8 is half traditional CTA and half alternative risk premia, so no single benchmark fits.  #mech/risk_premium
  > I would say we are 50% traditional CTA 50% % let's say alternative risk premium so CTA plus
  asset: multi · testable: no · confidence: medium
  ^MT108-C07-3

### C08
- **Vishal (J8, head of trading)** Redwood trades intraday breakouts measured in volatility terms within trend, volatility and positioning context.  #mech/slow_reaction
  > the base of the strategy is all about exploiting those extreme movements or not even extreme like I mean we talk in terms of like breakouts being measured in terms of volatility
  indicator: volatility-scaled breakouts; 3-5 minute sampling · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT108-C08-1
- **Vishal (J8, head of trading)** Short-term trading requires highly liquid futures for cheap entry and exit.  #mech/liquidity_flows
  > this strategy is focused on the big futures the future which have good liquidity uh which are easy to get in and get out
  asset: multi · horizon: days · testable: yes · confidence: high
  ^MT108-C08-2
- **Vishal (J8, head of trading)** Short-term strategy has low or negative correlation to CTA indices and improved risk-adjusted return in simulations.  #mech/risk_premium
  > this correlation of the short-term strategy to any of the CDA indices uh available across the board whether to SNP individually or to other industry benchmarks is quite low in fact some of them are quite bit negative also
  indicator: correlation to CTA indices · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT108-C08-3
- **Moritz Seibert (host)** Redwood's correlation with the short-term traders index is near zero.  #mech/risk_premium
  > found it practically nothing it's like very close to 0
  indicator: STTI correlation · asset: multi · horizon: days · testable: yes · confidence: medium
  **Correction (cross-check):** Wrong speaker: Moritz asks what Redwood's correlation to the short-term traders index is; the answer ('we ran it and found it practically nothing, very close to 0') is Vishal's. → Vishal: Redwood's correlation with the SG Short Term Traders Index is practically zero (close to 0).
  ^MT108-C08-4
- **Vishal (J8, head of trading)** Redwood's holding period is a few hours to a few days (3-5 days at most, mostly same day or next day), and unlike the main program it trades all asset classes including equity indices, in liquid futures only.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > very few of them are being held over like multiple days which can be like 3 to five days
  indicator: holding period; asset-class coverage of Redwood · asset: multi · horizon: days · conditions: highly liquid futures only · testable: yes - holding-period and universe checks · confidence: high
  ^MT108-C08-X1
- **Vishal** Redwood samples the market every 3 to 5 minutes (different systems at 3 or 5) and computes outputs each time; a trade is not necessarily taken.  #mech/new _(added by map cross-check)_
  > we are sampling the market every 3 minutes to 5 minutes
  indicator: intraday price, volatility, trend and positioning context · asset: futures · horizon: minutes to days · conditions: Liquid futures only · testable: no · confidence: high
  ^MT108-C08-R3
- **Vishal** The evidence for Redwood's low correlation and enhanced risk-adjusted return when added to the main programme comes from simulations, not a live record.  #mech/new _(added by map cross-check)_
  > lot of simulations and what we realized was that this kind of alpha that we are getting
  indicator: n/a · asset: futures · horizon: n/a · conditions: Before and after adding the short-term strategy · testable: no · confidence: high
  ^MT108-C08-R4

### C09
- **Vishal (J8, head of trading)** Short-term trading is not simply counter-trend; each strategy uses its own horizon context including volatility.  #mech/research_method
  > my trend is defined in a slightly different way than the the long-term Trend
  asset: multi · horizon: days · testable: partly · confidence: medium
  ^MT108-C09-1
- **Vishal (J8, head of trading)** About 700 round trips per million per month (roughly 8,000 per year) across 12 futures.  #mech/risk_management
  > 700 round trips uh per million per month
  indicator: turnover · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT108-C09-2
- **Vishal (J8, head of trading)** Short-term systems get higher Sharpe at similar returns but must avoid whipsaws from noise.  #mech/slow_reaction
  > the real challenge in the short shortterm stuff is to avoid whiplashes because there's a lot of noise in the short-term space
  asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT108-C09-3
- **Vishal (J8, head of trading)** Vishal says performance is not highly sensitive to small cost changes; he lacks exact numbers.  #mech/risk_management
  > it's not anything substantial to say that the strategy is impacted by slightly varing um transaction cost
  indicator: transaction costs · asset: multi · horizon: days · testable: yes: cost sensitivity test · confidence: low
  ^MT108-C09-4

### C10
- **Moritz Seibert (host)** Moritz's math: at about 6 dollars per contract and 8,000 round turns per million, costs are about 10.8 percent a year, a very high hurdle for short-term strategies.  #mech/risk_management
  > when we do these 8 8,000 round turns per million per year you're down about 11% uh 10.8% to be exact in terms of uh expected execution and implementation cost
  indicator: execution cost per contract · asset: multi · horizon: years · conditions: per 6 dollar all-in contract cost · testable: yes · confidence: medium
  **Correction (cross-check):** Faithful to the speaker but the arithmetic does not reconcile: 8,000 round turns x 2 contracts x $6 = 9.6% (and 700 per month x 12 = 8,400 gives about 10.1%); 10.8% would need about 9,000 round turns at $12. Treat 10.8% as the speaker's rough figure, about 10% a year. → Moritz: at roughly 6 dollars all-in per contract and about 8,000-9,000 round turns per million per year, execution cost is roughly 10 percent a year (he states 10.8%), a very high hurdle for the short-term strategy.
  ^MT108-C10-1
- **Vishal (J8, head of trading)** Short-term systems can easily overtrade, so exposure and sensitivity must be controlled.  #mech/risk_management
  > you can easily do overtrading in the short-term space
  asset: multi · horizon: days · testable: yes · confidence: high
  ^MT108-C10-2
- **Vishal (J8, head of trading)** Intraday trading needs 24-hour automated infrastructure (FIX execution, alerts, monitoring desks in India and UK), an operational overhead.  #mech/risk_management
  > we have built our own in-house uh infrastructure for the fix uh execution
  asset: multi · testable: no · confidence: high
  ^MT108-C10-3
- **Moritz Seibert (host)** Cost build-up for a non-HFT futures trader: about 0.75 broker commission, 0.50 exchange fee, 0.50 clearing fee, plus spread, slippage and market impact, which brings the all-in cost to roughly 5-6 dollars per contract.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > there is like an execution Commission of 75 cents and there's always exchange fees whatever like 50 cents and clearing fees 50 cents
  indicator: per-contract execution cost components · asset: multi · conditions: firms without HFT infrastructure or exchange membership · testable: yes - cost components can be audited · confidence: medium
  ^MT108-C10-X1

### C11
- **Tilman** J8's objective with the Global Absolute Return strategy is broad, diversified, holistic access to systematic investing; it only adds outside traders if they offer something it has not considered.  #mech/new _(added by map cross-check, time-bound view)_
  > provide the investor with uh with access to the asset class systematic in a broader Diversified and all-encompassing inclusive holistic way
  indicator: n/a · asset: multi · horizon: n/a · conditions: J8 business plan (managed accounts, hosting, planned fund vehicle) · testable: no · confidence: high
  ^MT108-C11-R2

