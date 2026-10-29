# Batch 2: testable rules from macro transcripts

Files: 9 (all read in full). Quotes are verbatim from the transcripts (auto-captions, so wording/spelling as in source).

---

## File 1: Ep14. Public Market Volatility, AI Air Pocket, $GOOG Ruling - BG2 w- Bill Gurley & Brad Gerstner (Aug 2024)

### Units of risk scaled to skew (price, earnings revisions, rates)
- Source: Brad Gerstner — Ep14 BG2 (quote: "when the skew gets more negative when cards get turned over when our probabilities of winning uh dissipate we got to we got to reduce the BET size")
- Type: position sizing/risk
- Rule as testable logic: Net equity exposure = function of a skew score built from (a) price vs recent drawdown (low price = good), (b) earnings-revision direction (consensus beaten down / revisions up = good), (c) Fed cutting vs hiking (cuts ahead = good). IF all three favorable (S&P >= 15% below 12m high, 3m net EPS revisions rising, Fed expected to cut) THEN net exposure 90% ("nine units"); IF all three unfavorable (S&P at all-time high after parabolic run, revisions flat/negative, recession signs) THEN 30% ("three units"); intermediate linearly (proposed). Rebalance monthly.
- Data needed: S&P 500 price (Yahoo ^GSPC, 1950; in tool), S&P forward EPS revisions (no free long series; proxy: Yardeni/FactSet not free; alternative: trailing EPS growth from Shiller data 1871), fed funds (FRED FEDFUNDS; in tool).
- Confidence: high (he describes it as how they run the book).

### Positive skew example: 80% x +50% vs 20% x -10% -> 9 units; negative skew -> 3 units
- Source: Brad Gerstner — Ep14 BG2 (quote: "we think there's an 80% chance that the names that we like in technology can be up a lot ... 20% chance the market can be down ... 5 to one or 4 to1 risk reward we put on nine nine units of risk")
- Type: position sizing/risk
- Rule as testable logic: Expected-payoff sizing: exposure proportional to (p_up*up - p_down*down)/|down| capped at 90%; floor 30%. Proxy for p/up/down: use the tool's state-conditional historical 12m return distribution (walk-forward) — IF upside/downside ratio of conditional forward returns >= 4 THEN 90% equity; IF ratio <= 1 THEN 30% equity (proposed).
- Data needed: tool's own state history + S&P returns (in tool).
- Confidence: medium.

### Reduce risk at all-time highs after parabolic run
- Source: Brad Gerstner — Ep14 BG2 (quote: "prices had just gone up a Lot bill right we were at all-time highs um and the moves had been fairly parabolic")
- Type: signal
- Rule as testable logic: IF S&P (or Nasdaq-100) at a 12m high AND 6m return >= +25% (Nasdaq +33% in 6 months cited) THEN cut equity exposure by 1/3 for 3 months (proposed thresholds).
- Data needed: ^GSPC, ^NDX / QQQ (1985 / 1999), Yahoo. Related to tool's "rally speed" (in tool).
- Confidence: medium.

### "High prices always make for big drops" in crowded markets
- Source: Brad Gerstner — Ep14 BG2 (quote: "the Japanese markets were really crowded bill um they hit an all-time high just three weeks ago high prices always make for big drops")
- Type: signal / conflict/caveat
- Rule as testable logic: IF a country index (e.g. Nikkei/EWJ) is within 3% of an all-time high AND its funding currency is at a multi-year low (JPY near 10y low vs USD) THEN expected drawdown risk elevated: underweight/hedge that index for 3 months (proposed). Test: forward 3m max drawdown conditional on ATH + weak-currency carry.
- Data needed: Nikkei 225 (^N225, 1965 Yahoo; FRED NIKKEI225 1949), USDJPY (FRED DEXJPUS 1971). Not in tool.
- Confidence: low.

### Fiscal cliff / personal tax increase as market headwind
- Source: Brad Gerstner — Ep14 BG2 (quote: "if taxes were to go up by 150 billion bucks a year this is a big risk to the market")
- Type: signal (fiscal)
- Rule as testable logic: IF scheduled fiscal tightening (tax expiry / deficit shrink) >= 0.5% of GDP within the next 12m THEN reduce equity by 1 unit (proposed). Testable proxy: IF change in federal deficit/GDP over next 4 quarters (CBO baseline or realized) <= -0.5 pp THEN underweight S&P.
- Data needed: Federal surplus/deficit % GDP (FRED FYFSGDA188S, annual 1929; quarterly FGDEF/GDP). Not in tool.
- Confidence: medium.

### Earnings beat rate as slowing signal
- Source: Brad Gerstner — Ep14 BG2 (quote: "48% of them had a positive Revenue beat now that sounds like a lot but it's the lowest level since the third quarter of 2019")
- Type: signal
- Rule as testable logic: IF share of S&P companies beating revenue estimates falls to its lowest in >= 4 years (or below 55%, proposed) THEN growth-slowing flag; combine with other recession signals to cut equity.
- Data needed: FactSet/LSEG revenue beat rate (not free). Free proxy: none long-history; could use S&P 500 quarterly sales growth from Shiller/S&P (S&P sales per share, spglobal xls, ~2001). Not in tool.
- Confidence: medium.

### Consumer deferral sequence: furniture -> travel = consumer under pressure
- Source: Brad Gerstner — Ep14 BG2 (quote: "the first thing they do is you know when things are starting to get tight is you defer your couch ... when Airbnb and Disney and the cruise lines and the airlines start seeing down ticks")
- Type: signal
- Rule as testable logic: IF real spending on furnishings y/y < 0 AND real spending on recreation/transport services (air travel, hotels) y/y turns negative THEN consumer-recession flag; underweight consumer discretionary (XLY) vs staples (XLP) for 6m; cut equity 1 unit.
- Data needed: BEA PCE by type: furnishings (FRED DFDHRX1A020NBEA annual / monthly real PCE furnishings "DFXARX1M020SBEA" proposed), air transportation services, accommodations (BEA NIPA table 2.4.6U monthly, 1959). Not in tool (tool has car sales, staples vs discretionary stocks).
- Confidence: medium.

### Sahm rule (confirmation)
- Source: Brad Gerstner — Ep14 BG2 (quote: "a recession is almost always underway if the three-month average unemployment rate Rises by half a percentage point from its low of the past year")
- Type: signal
- Rule as testable logic: IF 3m avg unemployment - min(3m avg, prior 12m) >= 0.5 pp THEN recession flag (cut equity / add duration).
- Data needed: FRED UNRATE / SAHMREALTIME (1948). Already in tool.
- Confidence: high.

### JOLTS openings below trend
- Source: Brad Gerstner — Ep14 BG2 (quote: "the jolts which is the job openings are below Trend um and that trend has been in place for quite a while")
- Type: signal
- Rule as testable logic: IF job openings < their 12m moving average for >= 6 consecutive months (proposed) THEN labour-softening flag (add to warning count).
- Data needed: FRED JTSJOL (Dec 2000). Not in tool.
- Confidence: medium.

### Restrictiveness gauge: 10y TIPS real yield vs 0.5% neutral
- Source: Brad Gerstner — Ep14 BG2 (quote: "the 10year tips right ... it's currently at 1.8% and 50 basis points is viewed as neutral so this is kind of Highly restrictive")
- Type: signal / regime map
- Rule as testable logic: IF 10y TIPS real yield >= 1.5% (>= 100 bp above a 0.5% "neutral") AND labour data weakening (Sahm >= 0.3 pp, proposed) THEN expect Fed cuts: overweight 2y-10y Treasuries (IEF/SHY) and steepeners for 6-12m.
- Data needed: FRED DFII10 (2003). Real 10y yield already in tool; the 0.5% neutral threshold is new.
- Confidence: medium.

### Fed funds vs 10y gap = market says rates too high
- Source: Brad Gerstner — Ep14 BG2 (quote: "the FED funds rate is at 55% right the 10year is at 4% so the the market-based mechanism for saying where rates are going to be is 150 basis low points lower")
- Type: signal
- Rule as testable logic: IF fed funds - 10y yield >= 1.0 pp (inverted vs policy) THEN Fed is restrictive; overweight intermediate Treasuries (IEF) 12m; equities face growth risk. Variant of 10y-3m curve.
- Data needed: FRED FEDFUNDS, DGS10 (1962). Partly in tool (10y-2y curve, not 10y-FF).
- Confidence: medium.

### Real fed funds at cycle peak + weakening data -> cuts coming
- Source: Austan Goolsbee quoted by Brad Gerstner — Ep14 BG2 (quote: "the real fed funds rate is at its peak for this cycle and we should only have that restrictiveness in place if there's a fear of overheating")
- Type: signal
- Rule as testable logic: IF real fed funds (FF - core PCE y/y) is at its 24m high AND core inflation 3m annualized < 12m (disinflation) AND unemployment rising THEN Fed cutting within 6m: overweight 2y Treasuries (SHY/IEI); steepener (long 2y vs 10y).
- Data needed: FRED FEDFUNDS, PCEPILFE (1959), UNRATE. Real FF not explicitly in tool.
- Confidence: medium.

### Rate cuts that precede recession are sold (bad for stocks)
- Source: Brad Gerstner — Ep14 BG2 (quote: "historically rate cuts that are preceding a recession or fears about a recession are often times sold right it doesn't cause the market to go up actually causes the market to go down")
- Type: regime map / conflict/caveat
- Rule as testable logic: IF Fed starts cutting (first cut after hikes) AND recession flag on (Sahm >= 0.5 or yield curve recently un-inverted) THEN do NOT buy stocks on the cut; hold underweight equity / long Treasuries for 6-12m. IF first cut with no recession flag ("insurance cut") THEN stocks overweight. Test 1990, 1995, 1998, 2001, 2007, 2019, 2024.
- Data needed: FEDFUNDS / DFEDTAR (1982), UNRATE (in tool).
- Confidence: high.

### Emergency/large cut = negative signal
- Source: Brad Gerstner — Ep14 BG2 (quote: "that would probably spook the market uh worse than if they just stay the course here um because that would suggest the economy is falling off a cliff")
- Type: signal
- Rule as testable logic: IF Fed cuts >= 50 bp at one meeting or intermeeting THEN treat as recession confirmation: equity underweight, long Treasuries for 6m (proposed).
- Data needed: FRED DFEDTAR/DFEDTARU (1982). Not in tool (tool has FF 12m change).
- Confidence: medium.

### Growth/unemployment/CPI matter more than the cut
- Source: Brad Gerstner — Ep14 BG2 (quote: "what's far more important about whether we end the year higher or lower is not whether the FED Cuts rates it's what is the economic growth what is the unemployment what is the CPI")
- Type: conflict/caveat
- Rule as testable logic: Test whether Fed-funds-change signals add value once unemployment trend and CPI trend are included (nested regression on 12m S&P excess returns). Expectation: FF change adds little.
- Data needed: in tool.
- Confidence: medium.

### Yen carry unwind: BoJ hike + crowded carry -> global risk-off
- Source: Brad Gerstner — Ep14 BG2 (quote: "the bank of Japan raises rates and all of the sudden these people who were effectively borrowing in Japanese Yen ... had to unwind these trades")
- Type: signal / hedge
- Rule as testable logic: IF USDJPY falls >= 7% in 1 month (yen surge) after a >= 2y uptrend (proposed) OR BoJ raises policy rate THEN cut equity 1 unit and Nikkei (EWJ) exposure for 1-2 months; long yen (FXY) as hedge. Test 1998 (LTCM yen spike), 2008, Aug 2024.
- Data needed: FRED DEXJPUS (1971), BoJ policy rate (FRED IRSTCI01JPM156N or IRLTLT01JPM156N; BoJ site), FXY (2007). Not in tool.
- Confidence: medium.

### US-Japan rate gap drives carry (wider gap -> more crowding)
- Source: Brad Gerstner — Ep14 BG2 (quote: "the US has kept rates higher for longer so it increases the spread there at zero or negative ... LED even more people to Pig pile into this carry trade")
- Type: signal
- Rule as testable logic: IF US 2y minus Japan 2y >= 4 pp AND starts narrowing (3m change <= -0.5 pp) THEN yen-strength / carry-unwind risk: long FXY, underweight EWJ (unhedged view) 3m (proposed).
- Data needed: FRED DGS2; Japan 2y yield (investing.com; FRED IRLTLT01JPM156N is 10y, 1989). Not in tool.
- Confidence: low.

### Middle East flare-ups usually a buying opportunity
- Source: Brad Gerstner — Ep14 BG2 (quote: "when the market Market get concerned about it it's generally a buying opportunity because they are generally shortlived right they keep each other in check")
- Type: re-entry/exit (geopolitics)
- Rule as testable logic: IF S&P falls >= 5% within 1 month coinciding with a Middle East conflict escalation (event list) AND oil does not rise >= 30% (no oil shock) THEN buy back equity to full weight; hold 6m. Event data: Caldara-Iacoviello Geopolitical Risk index spike (GPR >= 2 std above 12m mean, proposed).
- Data needed: Geopolitical Risk Index (matteoiacoviello.com/gpr.htm, monthly 1900/1985), WTI (FRED DCOILWTICO 1986 / WTISPLC 1946). Not in tool.
- Confidence: medium.

### Tail case: oil shock from war is the exception
- Source: Brad Gerstner / Bill Gurley — Ep14 BG2 (quote: "if the geopolitical events caused the price of oil to spike rate all of those risks have to be taken into account")
- Type: conflict/caveat / hedge
- Rule as testable logic: IF geopolitical risk spike AND oil 1m change >= +20% (proposed) THEN do not buy the dip: underweight S&P, overweight energy (XLE) / oil (USO) for 3-6m.
- Data needed: GPR index, WTI. Oil 6m change in tool; 1m spike + GPR not.
- Confidence: medium.

### Give back YTD gains test
- Source: Brad Gerstner — Ep14 BG2 (quote: "is the world so much better than it was on January 1 right that it has to be priced 10 to 15% higher and the answer to that is no")
- Type: conflict/caveat
- Rule as testable logic: Not a standalone rule (judgment). Could test: IF S&P YTD >= +15% AND macro warning count rose since start of year THEN expect mean-reversion of YTD gain (low confidence).
- Data needed: in tool.
- Confidence: low.

### Capex-ahead-of-revenue in tech phase shifts (AI air pocket)
- Source: Brad Gerstner / Bill Gurley — Ep14 BG2 (quote: "in the case of the internet capex got way out ahead of early revenues in the case of cloud capex ahead of early revenues mobile same thing")
- Type: signal (sector)
- Rule as testable logic: IF semiconductor index (SOXX/SMH) 12m return >= +80% AND hyperscaler capex growth >= 2x revenue growth (proposed) THEN expect "air pocket": underweight semis vs S&P for 6m. Simpler: IF SOX 12m return >= 100% THEN reduce semis weight (test 2000, 2021, 2024).
- Data needed: PHLX SOX (^SOX 1994 Yahoo), SMH (2000). Chips vs 12m high in tool; 12m-return extreme not.
- Confidence: low.

### Commodity-cycle stocks: buy at highest P/E, sell at lowest P/E
- Source: Bill Gurley — Ep14 BG2 (quote: "you had to buy hard drive compy companies when their PE was the highest ... then you literally sold it when when the the P was the lowest")
- Type: signal (cyclical sector)
- Rule as testable logic: For cyclical sectors (semis, memory, materials, energy, homebuilders): IF sector trailing P/E in top 20% of its 10y range (earnings trough) THEN overweight sector 12m; IF in bottom 20% (peak earnings) THEN underweight. Long-capacity-lead industries mis-forecast supply/demand.
- Data needed: sector P/E (no long free series; proxy: Ken French industry portfolios E/P breakpoints, or sector ETF trailing P/E from 2000s). Not in tool.
- Confidence: medium (stated as general pattern of cyclical industries).

### Cyclical capacity lead -> boom/bust shortages
- Source: Bill Gurley — Ep14 BG2 (quote: "whenever you have this kind of really long cycle time to actually bring up incremental capacity it's easier to miss supply and demand")
- Type: regime map
- Rule as testable logic: Supporting rationale for commodity-cycle rules: industries with long capacity lead times (memory, oil, copper, shipping) show mean-reverting earnings; test contrarian-on-P/E rule above in those groups.
- Data needed: as above.
- Confidence: low.

### Crypto correlates with equities in sell-offs (not a hedge)
- Source: Bill Gurley — Ep14 BG2 (quote: "crypto which you kind of would have thought maybe would have rallied with what's going on didn't it traded down in sympathy")
- Type: conflict/caveat (hedge)
- Rule as testable logic: Test: correlation of BTC with S&P during S&P drawdowns >= 5%; IF positive (>0.3) THEN exclude crypto as a hedge asset.
- Data needed: BTC-USD (Yahoo 2014; FRED CBBTCUSD 2014). Not in tool.
- Confidence: medium.

### Election binary + tax risk -> lower exposure into event
- Source: Brad Gerstner — Ep14 BG2 (quote: "we've got an upcoming election where there's going to be you know some some real binary things at play including higher taxes")
- Type: position sizing/risk
- Rule as testable logic: IF within 3 months of a US presidential election AND equities at 12m high THEN reduce equity 1 unit until election resolved (proposed). Test 1928-2024 election-year Aug-Nov returns.
- Data needed: S&P (in tool), election calendar.
- Confidence: low.

### Rising consumer delinquencies and small-business defaults
- Source: Austan Goolsbee quoted by Brad Gerstner — Ep14 BG2 (quote: "consumer delinquencies are rising small business defaults are rising they are at worrisome levels")
- Type: signal
- Rule as testable logic: IF credit-card delinquency rate rises >= 1 pp over 12m OR small business loan delinquency rate at 5y high THEN credit-stress flag; add to warnings.
- Data needed: FRED DRCCLACBS (card, 1991; in tool), small business: FRED DRBLACBS (business loans 1987) / NFIB credit conditions. Business-loan delinquency not in tool.
- Confidence: medium.

---
## File 2: Optimizing Investment Alpha with Customized Completion Portfolios Featuring Chris Jones, Ph.D. (Graham Capital webinar, Nov 2021 content; uploaded 2025)

Mostly about managed accounts / allocator structure; macro-testable content below.

### Stock-bond correlation regime: positive when Fed hawkish + inflation shock
- Source: Chris Jones (citing Pablo Calderini's paper) — Completion Portfolios (quote: "this period of positive correlation between equities and bonds could be identified by hawkish fed policy and uh inflation shock essentially")
- Type: regime map
- Rule as testable logic: IF Fed hiking (fed funds 12m change >= +1 pp) AND core CPI y/y >= 3% (or rising 12m) THEN expect stock-bond correlation > 0 over next 12m: replace long Treasuries as the de-risking asset with T-bills / gold / trend-following / commodities. ELSE (disinflation, Fed easing) long Treasuries hedge equities. Test predicted vs realized 36m rolling correlation from 1960.
- Data needed: fed funds (FRED FEDFUNDS 1954), core CPI (CPILFESL 1957), stock-bond correlation (in tool). Mostly in tool; the conditional switch is a new test (tool already uses corr<0 for TLT).
- Confidence: high.

### Positive stock-bond correlation lasted ~30 years (1970s-1990s); negative was a ~20-year "free lunch"
- Source: Chris Jones — Completion Portfolios (quote: "this was just a a 20-year free lunch we've had and in fact kind of equities and bonds can be positively correlated")
- Type: conflict/caveat
- Rule as testable logic: Backtest caveat: do not assume Treasuries hedge equities; evaluate de-risk sleeve separately 1965-1999 vs 2000-present. IF realized 24m stock-bond correlation > +0.2 THEN bonds weight in de-risk sleeve = 0 (proposed).
- Data needed: S&P total return, 10y Treasury total return (Shiller / Damodaran annual 1928; FRED DGS10 to build returns 1962). In tool (correlation).
- Confidence: high.

### Equities do poorly in inflationary periods
- Source: Judy Posnikoff — Completion Portfolios (quote: "if you go back to the academic papers um and they are quite old now they find that equities do very poorly in an inflationary period")
- Type: regime map
- Rule as testable logic: IF CPI y/y >= 4% and rising (3m annualized > 12m) THEN underweight S&P (e.g. 50%), overweight commodities / TIPS / gold for 12m (proposed thresholds).
- Data needed: CPIAUCSL (1947; in tool as core CPI y/y), commodity index (S&P GSCI total return from 1970 — not free; free proxy: World Bank Pink Sheet commodity price indices 1960 monthly; ETF DBC 2006), gold (LBMA via FRED GOLDAMGBD228NLBM 1968 — discontinued; use Yahoo GC=F / GLD 2004 or World Bank gold monthly 1960).
- Confidence: medium.

### Inflation hedges: commodities, trend following, linkers (TIPS), gold, infrastructure
- Source: Judy Posnikoff / Ella (allocator) — Completion Portfolios (quote: "obviously linkers and uh gold if you prefer a more blunt object")
- Type: action/instrument
- Rule as testable logic: IF tool state = Overheating or Stagflation THEN hold sleeve of TIPS (TIP/SCHP; 10y breakeven-based return) + gold (GLD) + broad commodities (DBC) + trend-following (proxy: SG Trend / time-series momentum on futures) instead of nominal Treasuries; hold while state persists.
- Data needed: TIPS returns (TIP 2003; FRED DFII10 from 2003 to synthesize; pre-1997 none), gold (World Bank 1960), commodities (World Bank indices 1960), trend proxy: AQR "Time Series Momentum" factor data (aqr.com datasets, monthly from 1985) or Ken French UMD (equity only). Not in tool.
- Confidence: medium.

### Trend following should do well in inflationary periods (AQR)
- Source: Judy Posnikoff — Completion Portfolios (quote: "aqr just came out with a a paper on Trend following should do well in inflationary periods and we'll we'll just have to see")
- Type: action/instrument / hedge
- Rule as testable logic: IF CPI y/y > 3% (proposed) THEN allocate 20% to a multi-asset trend sleeve (12m time-series momentum across equity indexes, bonds, commodities, currencies; long if 12m excess return > 0 else short/cash). Test vs Treasuries as diversifier.
- Data needed: AQR TSMOM dataset (1985) or build from ETFs (SPY, EFA, EEM, TLT, IEF, DBC, GLD, UUP, 2006+) / futures-like long histories (Ken French international indexes, World Bank commodities). Not in tool.
- Confidence: low (speaker is sceptical: "we'll just have to see").

### Cap portfolio beta, not just equity upside
- Source: Chris Jones — Completion Portfolios (quote: "we found the much more effective way to do this than just removing upside Equity exposure was to cap the beta overall in the portfolio so that Equity uh exposure doesn't pop up in Commodities or or elsewhere")
- Type: position sizing/risk
- Rule as testable logic: When adding commodity/EM/credit sleeves to the tool, compute rolling 12m beta of the whole portfolio to the S&P; IF de-risk signal active THEN constrain total portfolio beta <= 0.3 (cap can be 0, 0.3, 0.5), not just S&P weight = 0. Prevents hidden equity beta in EM, copper, high yield.
- Data needed: returns of all sleeves (as added). Not in tool (tool only has one risky asset).
- Confidence: high (described as their standard method).

### Seek downside (conditional) correlation, not plain correlation
- Source: Chris Jones — Completion Portfolios (quote: "people are looking from Cor corelation to conditional correlation correlation uh in down markets")
- Type: hedge
- Rule as testable logic: Rank candidate hedge assets (TLT, IEF, gold, yen, CHF, VIX futures, trend, puts) by their beta to S&P in months when S&P < -5% (or S&P drawdown > 10%); select hedges with negative downside beta in the current inflation regime (split by CPI >/< 3%).
- Data needed: monthly returns of hedge candidates (FXY 2007/DEXJPUS 1971; GLD/World Bank gold 1960; VIX index ^VIX 1990; VIXY 2011; Treasury returns 1962). Not in tool.
- Confidence: high.

### Risk-mitigation sleeve targets the biggest portfolio risk (equity drawdown), adds dry powder
- Source: Ella (ex-BCI) — Completion Portfolios (quote: "its main role is to mitigate the draw down triggered by whatever the biggest risk in the total portfolio is ... it reduces the conditional beta of that risk it increases uh liquidity and dry powder")
- Type: hedge / position sizing/risk
- Rule as testable logic: Design: a permanent 10-20% sleeve of passive (T-bills, TIPS, gold) + active (trend) assets whose objective is minimum downside capture vs S&P; rebalance into equities after drawdowns >= 20% (dry powder). Proposed parameters.
- Data needed: as above.
- Confidence: medium.

### Bonds may join equities on the downside in inflation; lower bond insurance
- Source: Ella (ex-BCI) — Completion Portfolios (quote: "there's a decent chance that bonds may join equities on the downside in an inflationary environment")
- Type: conflict/caveat
- Rule as testable logic: Same as stock-bond regime rule: IF core CPI y/y > 3% THEN do not use long Treasuries (TLT) as de-risk destination; use T-bills.
- Data needed: in tool.
- Confidence: high.

### Inflation-focused risk parity as an inflation play
- Source: Ella (ex-BCI) — Completion Portfolios (quote: "risk parity managers that actually have um an inflation Focus inflation protection Zeno risk parity could actually use that could have a focus on on inflation")
- Type: action/instrument
- Rule as testable logic: Test a risk-parity mix (equal risk across S&P, 10y Treasuries, TIPS, commodities, gold; inverse 36m vol weights) vs the tool during inflation regimes (CPI y/y > 4%).
- Data needed: as above (TIPS from 1997/2003 limits history; pre-1997 synthesize with real-yield models — low quality).
- Confidence: low.

### Excluding energy drives ESG performance: sector exclusion cuts both ways
- Source: Judy Posnikoff — Completion Portfolios (quote: "a lot of the um environmental portfolios really outperformed but that was because they didn't include energy and that's obviously changed this year")
- Type: conflict/caveat
- Rule as testable logic: Caveat for sector calls: energy (XLE) relative performance flips with the inflation regime; IF inflation rising (core CPI 3m > 12m) THEN overweight energy vs S&P (test).
- Data needed: XLE (1998), Ken French 49 industry portfolios "Oil" (1926). Tool has sector ETFs; Ken French history not.
- Confidence: low.

---
## File 3: The Market's Biggest Warning Signs Right Now with Todd Sohn - The Real Eisman Playbook Ep 66 (June 2026)

### 200-day moving average slope as trend filter
- Source: Todd Sohn — Eisman Ep 66 (quote: "we really like to work off of the slopes of moving averages ... When you start to see it flatten out and roll over, that's usually a tell")
- Type: signal / re-entry/exit
- Rule as testable logic: For any index/sector/country ETF: IF slope of 200-day MA (200dma today vs 20 trading days ago) > 0 THEN eligible to hold; IF slope <= 0 (flat/rolling over) THEN exit/underweight. Monthly version: 10-month MA slope over last 1 month. Apply to S&P, sector ETFs, country ETFs (EWY, EWZ, EWJ, FXI, INDA, EEM), commodities.
- Data needed: daily prices (Yahoo; ^GSPC 1950, sector ETFs 1998, country ETFs 1996/2000s; MSCI country indexes monthly 1970 via msci.com). Tool has S&P vs 10m average (level), not slope; not for other assets.
- Confidence: high (his core method).

### Laggard not making new highs while index does = weak / short candidate
- Source: Todd Sohn — Eisman Ep 66 (quote: "you have a market that is making a new high. S&P 500, equal S&P 500, small caps are making new highs. This is not made a new high in months")
- Type: signal (relative strength)
- Rule as testable logic: Cross-asset/sector rotation: IF S&P at 12m high AND a sector/country ETF is >= 10% below its own 12m high with 200dma slope <= 0 THEN underweight it (relative short) for 3m. Test on 11 sector ETFs and ~20 country ETFs.
- Data needed: as above. Tool has "industries 20%+ below high" (breadth), not as a per-asset allocation rule.
- Confidence: medium.

### RSI divergence: new high without overbought = warning; new low without oversold = trend change
- Source: Todd Sohn — Eisman Ep 66 (quote: "something reaching a new high without being as overbought, that can be a little bit of a warning sign. Or something making a new low without being as oversold")
- Type: signal
- Rule as testable logic: IF index makes 52-week high AND 14-day RSI < its value at the previous 52-week high by >= 10 points (bearish divergence) THEN cut exposure 1/3 for 1m (proposed); IF new 52-week low with RSI higher than at prior low (bullish divergence) THEN re-enter.
- Data needed: daily prices (Yahoo). Not in tool.
- Confidence: low ("It is a guideline. It's not a rule").

### Overbought-then-consolidate in uptrend = buyable
- Source: Todd Sohn — Eisman Ep 66 (quote: "You have a great trend, you got very overbought. Uh and now you're just consolidating ... it's going to be a buy pretty soon")
- Type: re-entry/exit
- Rule as testable logic: IF 200dma slope > 0 AND RSI(14) exceeded 70 in last 2 months AND now 40-55 (pullback) THEN buy/add for 3m (proposed). Apply to sector/country/commodity ETFs.
- Data needed: daily ETF prices. Not in tool.
- Confidence: medium.

### Use options (defined risk) for messy, mean-reverting charts
- Source: Todd Sohn — Eisman Ep 66 (quote: "it's a great use of the options market where I can structure a trade and I'm going to pay my premium, however it is, and that's my risk")
- Type: position sizing/risk / action/instrument
- Rule as testable logic: IF asset is oversold but 200dma slope still negative ("messy") THEN express rebound only through calls sized to premium budget (e.g. 0.5% of portfolio per trade, proposed) instead of buying outright; else respect stop-loss. For the tool: when re-entering after a de-risk while trend still down, use 3-6m at-the-money call spreads on SPY with <= 1% budget (requires option-price model: Black-Scholes with VIX as implied vol).
- Data needed: VIX (^VIX 1990; FRED VIXCLS), SPY; CBOE option-strategy indexes (BXM, PUT, 1986) as proxies. Not in tool.
- Confidence: medium.

### Respect stop-loss levels on counter-trend rebounds
- Source: Todd Sohn — Eisman Ep 66 (quote: "If you want to take a flyer on them, you got to respect your stop loss levels")
- Type: position sizing/risk
- Rule as testable logic: IF entering an asset whose 200dma slope <= 0 THEN stop-loss at prior swing low or -8% from entry (proposed); exit on breach.
- Data needed: daily prices. Not in tool.
- Confidence: medium.

### Sector concentration > 15% of S&P has preceded poor results
- Source: Todd Sohn — Eisman Ep 66 (quote: "since 1990, only tech hardware back in the tech bubble ... climbed way above 15, got to like 30. Uh energy in the mid-2000s got right above 15 ... Two out of three of those times have ended up with not so great results")
- Type: signal (concentration)
- Rule as testable logic: IF any single industry group > 15% of S&P 500 market cap (or top sector > 35%) THEN reduce S&P weight 1 unit and/or shift part to equal-weight S&P (RSP) and underweight that group for 12m. Test 1990-2026 (few episodes; weak statistics).
- Data needed: sector/industry weights — Ken French 49 industry portfolios with market caps (1926, free) as proxy for industry share of US market. Tool has "narrow leadership" (related), not sector weight share.
- Confidence: medium (speaker says it's a road map, not a prediction).

### Tech ~40% of S&P: index is not diversified; "no place to hide" if tech reverses
- Source: Todd Sohn / Steve Eisman — Eisman Ep 66 (quote: "if you own an index and you think therefore you're diversified, you're actually no longer diversified because tech so dominates")
- Type: hedge / position sizing/risk
- Rule as testable logic: IF tech (+ comm. services mega-caps) share of S&P > 40% THEN hold the equity sleeve partly in equal-weight S&P (RSP) or ex-tech sectors, or hedge with QQQ/XLK puts; reduce effective equity risk by sizing on tech beta.
- Data needed: Ken French industry market caps (1926); RSP (2003), equal-weight S&P index (1990). Not in tool.
- Confidence: medium.

### High beta vs low vol at historic extreme -> beware (mean reversion risk)
- Source: Todd Sohn — Eisman Ep 66 (quote: "the point of this chart is not to say, 'Hey, sell everything.' cuz it's Listen, it's still a bull market. But be aware that beta is getting extreme")
- Type: signal
- Rule as testable logic: IF rolling 12m return of high-beta decile minus low-vol decile is in its top 5% since 1963 THEN expect low-vol outperformance next 12m: tilt equities to low-vol (USMV/SPLV) and staples; cut 1 unit of equity (proposed).
- Data needed: Ken French portfolios formed on beta / variance (1963, free); ETFs SPHB/SPLV (2011). Tool has cyclical vs defensive 6m and staples vs discretionary (related).
- Confidence: medium.

### Semis vs staples relative performance at historic extreme
- Source: Todd Sohn — Eisman Ep 66 (quote: "the performance of say semis versus staples has gotten to historically extreme territory")
- Type: signal
- Rule as testable logic: IF SOX/XLP 12m relative return in top 5% of history (proposed) THEN overweight staples vs semis for 6-12m (contrarian), conditional on 200dma slope of SOX turning down (to avoid fighting trend).
- Data needed: ^SOX (1994), XLP (1998), Ken French "Chips" vs "Food/Smoke" industries (1926). Partly in tool (chips vs 12m high).
- Confidence: low.

### Hedge tech with healthcare, discretionary, financials (6m relative performance)
- Source: Todd Sohn — Eisman Ep 66 (quote: "if you're looking for stuff to hedge tech, look in healthcare, discretionary, financial")
- Type: hedge
- Rule as testable logic: Diversify tech concentration by holding the 3 sectors with lowest correlation to XLK whose 6m relative-to-S&P performance has started improving (6m rel. return rising over last 1m, proposed).
- Data needed: sector ETFs XLV/XLY/XLF/XLK (1998). Tool has 20 industry ETFs.
- Confidence: low.

### Sector ETF flow concentration (one-game market) = fragility
- Source: Todd Sohn — Eisman Ep 66 (quote: "27 billion into tech ETFs, give or take, since the March 30th low ... and negative 4.4 billion into every other sector combined")
- Type: signal (sentiment/flows)
- Rule as testable logic: IF cumulative 3m flows into one sector's ETFs exceed the sum of all others' and that sector > 30% of S&P THEN fragility flag; reduce that sector weight. Flow data not free (ETF.com / ICI); proxy: shares-outstanding changes of XLK/SMH (from issuer files) — hard.
- Data needed: sector ETF flows (not free; ICI monthly ETF net issuance aggregate is free from 2000s). Not in tool.
- Confidence: low.

### Equity ETF flow percentile (1y) as temperature, not a signal
- Source: Todd Sohn — Eisman Ep 66 (quote: "Flows are just a it's a temperature barometer. They're not necessarily a signal")
- Type: conflict/caveat
- Rule as testable logic: Test only: IF equity fund flows in top decile of trailing 1y THEN forward 3m S&P returns lower? Speaker says not a signal; low prior.
- Data needed: ICI weekly/monthly fund flows (ici.org, 2007+). Not in tool.
- Confidence: low.

### Cyclical minus defensive sector flows = risk appetite
- Source: Todd Sohn — Eisman Ep 66 (quote: "Add those flows up and then subtract them from defensives, energy, staples, utilities, health ... Just a measure of risk risk appetite")
- Type: signal
- Rule as testable logic: Price-based proxy (flows not free): cyclicals ex-tech (XLF, XLI, XLB, XLY) vs defensives (XLE, XLP, XLU, XLV) 3m relative performance; IF in bottom quintile THEN risk appetite subdued (contrarian bullish?) — direction ambiguous; test both.
- Data needed: sector ETFs (1998). Tool already has cyclical vs defensive 6m (note his defensive set includes energy).
- Confidence: low.

### Equal-weight consumer discretionary as consumer-health barometer ("looks like recession")
- Source: Todd Sohn — Eisman Ep 66 (quote: "This chart look on consumer discretionary, looks like we're we're in a recession ... Discretionary is is a a barometer of the health of the consumer")
- Type: signal
- Rule as testable logic: IF equal-weight consumer discretionary (RSPD / equal-weight S&P discretionary) 6m relative to equal-weight S&P in bottom decile THEN consumer-recession warning (+1 warning). Use equal-weight to avoid Amazon/Tesla skew.
- Data needed: RSPD (2006), Ken French "Rtail"/"Cnsum" equal-weighted industry returns (1926 — French provides equal-weighted versions). Tool has staples vs discretionary (cap-weighted) — new: equal-weighted version.
- Confidence: medium.

### Use equal-weight sector series for backtests (cap-weight skewed)
- Source: Todd Sohn — Eisman Ep 66 (quote: "whenever you backtest anything from that sector, it's just going to get Amazon type results")
- Type: conflict/caveat
- Rule as testable logic: Methodology: re-run tool's sector indicators (staples vs discretionary, cyclical vs defensive) on equal-weighted Ken French industries; keep the version with better walk-forward record.
- Data needed: Ken French 49 industries equal-weighted (1926). Not in tool.
- Confidence: high (methodological).

### Healthcare share halved (16% -> 8%): mean reversion setup
- Source: Todd Sohn — Eisman Ep 66 (quote: "Health care has has gone from 16% to 8%. It's unbelievable ... the performance is so bad you could make the case it's good")
- Type: signal (sector contrarian)
- Rule as testable logic: IF a defensive sector's share of S&P falls to <= 50% of its 10y high AND its 200dma slope turns positive THEN overweight that sector 12m (proposed). Speaker admits it hasn't worked for a year.
- Data needed: Ken French industry market caps; XLV (1998). Not in tool.
- Confidence: low.

### Small-cap ETF outflows (first since 2011) = capitulation
- Source: Todd Sohn — Eisman Ep 66 (quote: "last year small cap ETFs had outflows. That was the first time since 2011")
- Type: signal (contrarian)
- Rule as testable logic: IF annual net flows into small-cap ETFs < 0 (proposed) THEN overweight small caps (IWM) vs S&P next 12m. Flow data hard; price proxy: IWM/SPY 3y relative return in bottom decile.
- Data needed: Ken French size portfolios (1926), IWM (2000). Not in tool.
- Confidence: low.

### Energy flow "sugar rush" on war start, then oil peaks
- Source: Todd Sohn — Eisman Ep 66 (quote: "Big rush as energy got some momentum. Money flooded in ... Coincidental that all of a sudden oil started to peak too? Perhaps")
- Type: signal (geopolitics-to-asset)
- Rule as testable logic: IF oil rises >= 25% within 2 months after a geopolitical shock AND energy ETF flows/volume spike (proxy: XLE volume 3x 1y avg) THEN expect oil peak within 3 months: take profits on energy/oil longs (proposed). Peace/deal headline -> oil collapse risk.
- Data needed: WTI (FRED DCOILWTICO), XLE volume (Yahoo), GPR index. Not in tool (oil 6m change only).
- Confidence: low.

### Record leveraged-ETF usage = froth / added volatility
- Source: Todd Sohn — Eisman Ep 66 (quote: "the volume of this, called the usage rate, is huge. It is huge. It is It is stair-stepping higher. And this is So this this is I this would make me nervous")
- Type: signal (sentiment)
- Rule as testable logic: IF leveraged ETF AUM or share of volume at record and rising >= 50% y/y (proposed) THEN froth flag: tighten trailing stops / cut equity 1 unit if trend breaks. Proxy series: total AUM of TQQQ+SOXL+SPXL (shares x price, 2010+).
- Data needed: leveraged ETF AUM (issuer data; partial). Not in tool.
- Confidence: low.

### Daily rebalancing of leveraged ETFs adds volatility
- Source: Todd Sohn — Eisman Ep 66 (quote: "because these funds rebalance at the end of every day to reset that to a daily exposure, it's adding more volatility into the market")
- Type: conflict/caveat
- Rule as testable logic: Caveat for instrument choice: leveraged/inverse ETFs (SH, SDS, SQQQ, TBT) decay; tool should model daily-reset returns (not 2x monthly) when testing inverse/levered exposure.
- Data needed: daily index returns to simulate daily reset. Methodological.
- Confidence: high.

### Thematic ETFs: avg 3-year drawdown 32%, 70% have Sharpe < 1
- Source: Todd Sohn — Eisman Ep 66 (quote: "this says the average 3-year drawdown is is 32% ... 70% have a sharp ratio less less than one from thematic ETFs")
- Type: conflict/caveat (instrument)
- Rule as testable logic: Exclude thematic ETFs from the instrument universe; use broad sector/country/commodity ETFs only.
- Data needed: none.
- Confidence: high.

### Quality and momentum factor ETFs ~ S&P (R-squared near 1) -> not diversifiers
- Source: Todd Sohn — Eisman Ep 66 (quote: "the R squared of this ETF ... is near perfect to the S&P 500")
- Type: conflict/caveat (hedge)
- Rule as testable logic: When choosing a defensive equity sleeve, require 36m R-squared vs S&P < 0.8 (proposed); quality/momentum ETFs fail when mega-cap tech dominates.
- Data needed: QUAL (2013), MTUM (2013), Ken French factors. Not in tool.
- Confidence: medium.

### REITs diversified in the 2000 tech-bust
- Source: Todd Sohn — Eisman Ep 66 (quote: "if you ever had to have another 2000 environment, the REITs actually went up during it ... They were the diversifier")
- Type: hedge
- Rule as testable logic: IF tech share of market > 35% AND tech 200dma slope turns negative THEN overweight REITs (VNQ / FTSE NAREIT) vs S&P for 12m (proposed). Test 2000-02 vs 2022.
- Data needed: FTSE Nareit All Equity REITs index (reit.com, monthly 1972, free), VNQ (2004). Not in tool.
- Confidence: medium.

### Money-market funds 25% of bond aggregate = sidelined cash
- Source: Todd Sohn — Eisman Ep 66 (quote: "there's 8 trillion of money market funds and as a percentage of the bond agg, that's very elevated. It's about 25%")
- Type: signal (liquidity)
- Rule as testable logic: IF money-market fund assets / (bond market size or S&P market cap) in top quintile THEN potential fuel when rates change; test as contrarian bullish for equities/bonds over 12m (weak prior).
- Data needed: FRED MMMFFAQ027S (money market fund assets, quarterly 1974) or WRMFNS (retail MMF, weekly 1980); US market cap (Wilshire 5000 FRED WILL5000PRFC, discontinued 2024 — or tool's market cap/GDP data). Not in tool.
- Confidence: low.

### Gold failing to rally on war/inflation fears = "pay attention when stuff does not behave"
- Source: Todd Sohn — Eisman Ep 66 (quote: "Chris always likes to say pay attention when stuff that is supposed to behave one way does not")
- Type: signal
- Rule as testable logic: IF geopolitical risk index spikes AND gold 1m return < 0 THEN gold-weakness signal: avoid adding gold for 3m (test whether "failure to respond" predicts further gold underperformance).
- Data needed: gold (World Bank 1960 / GLD 2004), GPR index (1985). Not in tool.
- Confidence: low.

### Gold drivers: higher rates and stronger dollar are headwinds; blow-off after "metal mania"
- Source: Todd Sohn — Eisman Ep 66 (quote: "Whether it's higher rates, uh modestly higher dollar maybe's been a headwind. I look at it as more so what is a was a blow off from metal mania")
- Type: signal
- Rule as testable logic: IF real 10y yield 3m change > +0.3 pp AND dollar index 3m change > +2% THEN underweight gold 3m; IF gold 12m return > +40% with record ETF volume THEN blow-off risk, trim (proposed).
- Data needed: DFII10 (2003; in tool as real 10y), DTWEXBGS (2006)/DTWEXM (1973) (dollar in tool), gold. Gold not in tool.
- Confidence: medium.

### Outflows from gold and Bitcoin ETFs = "bar is low" (contrarian bottoming)
- Source: Todd Sohn — Eisman Ep 66 (quote: "I've seen a lot of money coming out coming out of gold ETFs. So, that kind of perks my interest of well, maybe this thing will start to bottom out")
- Type: re-entry/exit (contrarian)
- Rule as testable logic: IF GLD shares outstanding fall >= 5% over 3m (proposed) AND gold 200dma slope still positive THEN buy gold for 6m. Data: GLD tonnes held (spdrgoldshares.com history 2004, free).
- Data needed: GLD holdings (2004). Not in tool.
- Confidence: low.

### Cap-weighted index exposure: check what you own (concentration risk)
- Source: Todd Sohn — Eisman Ep 66 (quote: "Pay attention to what you own ... it's a bull market, but you might be loaded up on more exposure than you think in certain areas")
- Type: position sizing/risk
- Rule as testable logic: Portfolio rule: compute look-through exposure to top-10 S&P stocks across all equity sleeves (S&P, QQQ, quality, momentum, sector ETFs); cap top-10 look-through at 30% of equity sleeve (proposed).
- Data needed: ETF holdings (issuer files). Not in tool.
- Confidence: medium.

### Staples only bought by algorithms in a market freak-out
- Source: Todd Sohn — Eisman Ep 66 (quote: "It will take a market freak out for algorithms to buy consumer staples again")
- Type: signal
- Rule as testable logic: IF VIX > 30 (proposed) THEN staples outperform S&P during the next 1-3m; test as hedge sleeve rotation (XLP overweight on VIX spike).
- Data needed: VIX (in tool), XLP / Ken French Food (1926).
- Confidence: low.

---
## File 4: Stanley Druckenmiller on Economy, Stocks, Bonds, Trump, Fed- Full Interview (Bloomberg, recorded Dec 2018)

### "Inside the stock market": early cyclicals down far more than the S&P = recession warning
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "auto stocks are down 30% they're not down 10 or 11 they're down 30 building stocks are down 35 banks ... are down 25% the Russell 2000 is down over 20 percent")
- Type: signal (regime map)
- Rule as testable logic: IF average drawdown from 12m high of early-cyclical groups (autos, homebuilders/building, banks, retail, small caps) minus S&P drawdown >= 15 pp AND defensives (utilities, staples, pharma) are up/flat THEN recession-risk "amber": cut equity 1-2 units and go long Treasuries (2y/5y/10y). He says he used this "cycle after cycle" and predicted the last four recessions.
- Data needed: Ken French 49 industries (Autos, BldMt/Cnstr, Banks, Rtail, Util, Food, Drugs; 1926), Russell 2000 (^RUT 1987; Ken French small-size 1926), XHB/KBE/XRT ETFs (2006). Tool has cyclical vs defensive 6m, homebuilders vs market, bank stocks vs market — the composite drawdown-gap formulation is new.
- Confidence: high.

### Yield curve flattening/partial inversion (2s5s) = amber
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "the segment would be the yield curve again amber not red but we've inverted as you know from fives and to is just slightly")
- Type: signal
- Rule as testable logic: IF 5y - 2y <= 0 (first inversion segment) THEN amber (+1 warning); IF 10y - 2y / 10y - 3m <= 0 THEN red. Also "bull flattening" (curve flattening while yields fall and Fed guiding hikes) = market disbelieves Fed -> go long 2y-10y Treasuries.
- Data needed: FRED DGS2, DGS5 (1976), DGS10, DTB3. Tool has 10y-2y; 5y-2y and bull-flattening are new.
- Confidence: high.

### Market disagrees with Fed dots (curve prices fewer hikes than guided) = buy Treasuries
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "the Fed is you know told us that there's going to be three to four hikes next year after this hike and the market is just saying no no no")
- Type: signal
- Rule as testable logic: IF 2y yield - fed funds <= 0 while Fed is still hiking (FF 6m change > 0) THEN market expects end of hikes: long 2y/5y Treasuries (SHY/IEI) for 12m.
- Data needed: DGS2, FEDFUNDS (1976). Not in tool.
- Confidence: medium.

### Credit leads the economy: CDS/high-yield widening, leveraged loans falling
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "the other thing we've looked at historically is credit tends to lead the economy")
- Type: signal
- Rule as testable logic: IF high-yield OAS widens >= 150 bp from its 6m low (proposed) OR leveraged loan index falls >= 3% from high (proposed) THEN credit warning: cut equity, short credit (HYG) vs long Treasuries; it doesn't matter whether bad credit sits in banks or non-banks.
- Data needed: ICE BofA HY OAS (FRED BAMLH0A0HYM2, 1996), Baa spread (FRED BAA10Y 1986/BAA 1919; in tool), leveraged loan index (S&P/LSTA not free; proxy BKLN 2011). Tool has junk vs Treasuries 3m and Baa spread; leveraged loans not.
- Confidence: high.

### Credit-dependent financials (AIG, Blackstone) falling = warning light
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "AIG is down from 65 to 35 and it's the number one what I would call closed on credit fund on the planet ... how can you look at that ... and not see that's at least a warning light")
- Type: signal
- Rule as testable logic: IF insurers + alternative asset managers + banks (KIE, PSP or BDC index, KBE) are >= 25% below 12m high while S&P is <= 15% below THEN credit-stress warning (+1). Proxy: Ken French "Insur" and "Fin" industries.
- Data needed: Ken French industries (1926), KIE (2005), PSP (2006). Bank stocks vs market in tool; insurers/alt managers new.
- Confidence: medium.

### Pair trade: short credit + long Treasuries in late cycle
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "it's easy to short credit for long Treasuries because again if rates are going up I don't want to be short credit because their interest rate instrument")
- Type: hedge / action/instrument
- Rule as testable logic: IF late-cycle state (curve flat/inverted + credit warning) THEN hold short HY (HYG or SJB) duration-hedged with long Treasuries (IEF), i.e. long IEF / short HYG equal duration, for 12m or until HY OAS > 800 bp (proposed exit).
- Data needed: HY total return index (FRED BAMLHYH0A0HYM2TRIV, 1986), Treasury index (ICE BofA FRED BAMLCC0A0CMTRIV is corporate; use synthetic from DGS7/DGS10). Not in tool (tool doesn't short credit).
- Confidence: high.

### Credit yields too low for late-cycle risk (5-6% vs normal 8-9%)
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "five or six percent absolute nominal yields for stuff that normally would be eight or nine an environment like this the risk award is just terrible in credit")
- Type: signal
- Rule as testable logic: IF HY effective yield < its 20-year median minus 2 pp (proposed) AND late-cycle state THEN underweight/short HY for 12m.
- Data needed: FRED BAMLH0A0HYM2EY (1996). Not in tool.
- Confidence: medium.

### Make money in bear markets via Treasuries (2y especially), not stock shorts
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "I always made it in Treasuries because Treasury yields will go down dramatically ... one of my biggest hit was in two years")
- Type: action/instrument
- Rule as testable logic: IF recession/bear signals on (inside-market + curve + credit) THEN overweight 2y/5y/10y Treasuries (barbell across curve; 2y gains most when Fed cuts from high FF). Prefer Treasuries over shorting stocks ("vicious rallies"). Hold until Fed cutting is priced (2y yield <= FF - 1.5 pp, proposed).
- Data needed: DGS2/DGS5/DGS10 to build constant-maturity total returns (1976). Partly in tool (TLT / T-bills); 2y/5y not.
- Confidence: high.

### Shorting equities in bear markets is hard (vicious rallies)
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "in a bear market they don't trade with rhythm you get these vicious rallies you get squeezed out of shorts")
- Type: conflict/caveat
- Rule as testable logic: When de-risking, prefer 0% equity + Treasuries over inverse equity (SH); test whether adding a -20% S&P short to the de-risk state improves Sharpe; expectation: little gain, worse drawdowns.
- Data needed: S&P (in tool).
- Confidence: high.

### M2 growth slowdown (7.5% -> 4%) = liquidity tightening
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "m-2 growth has gone from about seven and a half percent to four percent over the last couple years it doesn't take a genius to figure out why liquidity is tightening")
- Type: signal (liquidity)
- Rule as testable logic: IF M2 y/y growth falls >= 3 pp over 24m (proposed) or to < 4% THEN liquidity-tightening warning (+1).
- Data needed: FRED M2SL (1959). M2 growth in tool; the 24m change formulation is new.
- Confidence: medium.

### QT + deficit financing = tightening even without hikes; global QT (Fed+ECB)
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "if you have a budget deficit and you need to raise money every month you know that creates government bonds selling every month and it tightens liquidity")
- Type: signal (liquidity)
- Rule as testable logic: IF combined Fed + ECB (+BoJ) balance sheet 12m change (in USD) < 0 ("global QT") THEN underweight global equities and EM; IF turning positive THEN overweight. Also IF Fed balance sheet shrinking AND federal deficit > 4% of GDP THEN extra tightening flag.
- Data needed: FRED WALCL (2002), ECB total assets (FRED ECBASSETSW 1999), BoJ (FRED JPNASSETS 1998), EURUSD/JPY (DEXUSEU 1999). Tool has Fed net liquidity 3m change; global CB balance sheet and deficit not.
- Confidence: high.

### Fed hiking into a market meltdown = policy mistake risk; rate of change matters
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "we in the US have never hiked into a meltdown like this since Volcker ... it's not even the level it's the rate of change")
- Type: signal
- Rule as testable logic: IF Fed hikes while S&P is >= 10% below 12m high AND cyclicals are >= 25% below THEN "policy mistake" regime: go long 2y Treasuries, underweight equities 6m; IF Fed then pauses/pivots within 3m THEN re-enter equities (Jan 2019 analog).
- Data needed: DFEDTAR (1982), S&P (in tool), Ken French cyclicals. Partly in tool (Fed tightening condition).
- Confidence: medium.

### Unemployment is lagging; recessions preceded by very low unemployment
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "employment is in the lagging indicators ... most recessions were preceded by a very low unemployment rate")
- Type: regime map / conflict/caveat
- Rule as testable logic: IF unemployment at 10y low (or <= its 5y min + 0.2 pp) AND Fed tightening THEN late-cycle flag (capacity exhausted): begin de-risk prep. Use leading (markets, credit, housing, autos), not coincident data. Contradiction with tool's Sahm usage: Sahm fires late; test lead/lag.
- Data needed: UNRATE (in tool).
- Confidence: high.

### Leading housing and autos weakening at low rates = malinvestment/debt drag
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "some of this leading stuff like autos and housing being this week with 2% rates has got to give them pause")
- Type: signal
- Rule as testable logic: IF housing starts/permits 6m change < -10% AND auto sales 6m change < -5% while policy rate is low (< 3%) THEN warning (+1). (Tool already has permits and car sales 6m.)
- Data needed: FRED PERMIT, TOTALSA (in tool).
- Confidence: medium.

### Corporate debt growth >> earnings growth (buybacks/M&A financed by debt) = bubble
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "since 2010 corporate non-financial debt has grown from six trillion to nine point six trillion ... during that time corporate earnings increased 27%")
- Type: signal (credit/debt)
- Rule as testable logic: IF nonfinancial corporate debt 5y growth minus corporate profits 5y growth >= 25 pp (proposed) THEN fragile-credit regime: lower equity max weight (e.g. 70%) and favour Treasuries in de-risk. Test vs subsequent 3-5y equity returns.
- Data needed: FRED BCNSDODNS (nonfin corp debt, quarterly 1945), CP (corporate profits after tax, 1947). Not in tool.
- Confidence: medium.

### After QE-driven debt build-up: expect 0-5% S&P returns for 5 years
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "I could see the SP returning between 0 and 5 percent annually the next five years")
- Type: regime map
- Rule as testable logic: Forecast test: IF (Fed balance sheet/GDP rose >= 10 pp in prior 5y) AND (corp debt/GDP at record) THEN expected 5y S&P return low. (Realized 2019-2023 was ~15%/yr: forecast failed — caveat.)
- Data needed: WALCL/GDP, BCNSDODNS/GDP. Not in tool.
- Confidence: low (he hedges heavily; ex-post wrong).

### Global bear market: DAX and China peaked first (international leads)
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "the Dax and the China market peaked in January and I don't know that anybody's seen their economic data lately")
- Type: signal (country/EM)
- Rule as testable logic: IF share of major country indexes (MSCI ACWI constituents: Germany, China, Japan, UK, Korea, EM) below their 10m MA >= 60% (proposed) while S&P still above THEN global-breadth warning for US equities (+1); underweight EM/Europe.
- Data needed: MSCI country index monthly (msci.com end-of-day data, 1970; EM 1988), Yahoo ^GDAXI (1987), 000001.SS (1997), EWG/FXI/EWY ETFs. Not in tool.
- Confidence: medium.

### Bear market that follows free money/debt build-up takes 3-5 years (sideways or big down)
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "this could take three to five years either sideways or a big down with something else")
- Type: regime map
- Rule as testable logic: Not directly testable beyond the low-return regime above. Low confidence.
- Data needed: n/a.
- Confidence: low.

### After large price adjustment + broad de-risking, favorable period possible (policy-dependent)
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "with this adjustment in prices and with this D risking that's been done by a lot of investors we could certainly have a favorable period ahead")
- Type: re-entry/exit
- Rule as testable logic: IF S&P drawdown >= 15-20% AND positioning washed out (AAII bull-bear < -20 or equity fund outflows, proposed) AND Fed pauses hikes THEN re-enter equities to full weight.
- Data needed: AAII sentiment survey (aaii.com xls, weekly 1987, free), S&P, DFEDTAR. AAII not in tool.
- Confidence: medium.

### Short financials when they need rising rates to work
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "why in the world would you buy a group that needs rates to go up to own it because the last time I checked banks our equities and equities don't do well with with rates going up")
- Type: action/instrument (sector)
- Rule as testable logic: IF Fed tightening late-cycle (FF 12m change > +1 pp AND curve flattening) THEN underweight financials (XLF/KBE) vs S&P for 12m.
- Data needed: XLF (1998), Ken French Banks/Fin (1926). Tool has bank stocks vs market as indicator; sector call is new.
- Confidence: medium.

### Long-duration secular growers (high-growth stocks) win in slow-growth, low-rate world
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "in a period of slow muted growth if you can find a 20 to 30 percent grower it's really like a long-term cashflow in some ways it's almost better than a bond")
- Type: regime map (sector/factor)
- Rule as testable logic: IF real GDP growth trend <= 2% AND 10y yield falling (12m change < 0) THEN overweight growth (IWF/QQQ/software) vs value (IWD) for 12m; IF cyclical earnings boom with rising yields THEN value wins (his 2018 interruption).
- Data needed: Ken French HML (1926, monthly), GDPC1 (1947), DGS10 (in tool). HML not in tool.
- Confidence: medium.

### Long disruptors / short disrupted (tech)
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "in tech we've been long the disruptors and short the disrupted which has worked beautifully over in two years")
- Type: action/instrument
- Rule as testable logic: Single-stock theme; not testable with indexes except as long growth / short value (HML short) — see growth rule. Caveat: fails in sharp sell-offs when value buyers rotate.
- Data needed: Ken French HML/UMD.
- Confidence: low (single-stock theme).

### Commodity indexes down sharply = disinflation the Fed should heed
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "not just oil but all the commodity indexes are down dramatically in the last four or five months and it's inconceivable that that doesn't float through")
- Type: signal (inflation)
- Rule as testable logic: IF broad commodity index 6m change <= -15% (proposed) THEN expect lower headline inflation within 6-12m: Fed less hawkish; overweight Treasuries (IEF/TLT), underweight TIPS vs nominals (breakevens fall).
- Data needed: World Bank commodity price index (monthly 1960), S&P GSCI / BCOM (not free; DBC 2006). Tool has oil and copper 6m; broad commodity index new.
- Confidence: medium.

### Volatility is only good when part of a trend
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "volatility is only good if it's part of a trend and it's giving you entry points within a trend we're getting volatility ... with no trend so ... that's a nightmare")
- Type: position sizing/risk
- Rule as testable logic: IF VIX > 25 AND trend indicators conflicting (S&P 10m MA slope ~ 0, |12m return| < 5%) THEN reduce gross exposure / position sizes by half (trendless high-vol regime) for 1-3m (proposed).
- Data needed: VIX (in tool), S&P (in tool).
- Confidence: medium.

### Price-vs-news signals are noisier now (short-horizon); 8-9 month message still reliable
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "the message over eight or nine months is still great ... I just think over a week or two you're getting noise that used to mean something and now it doesn't mean anything")
- Type: conflict/caveat
- Rule as testable logic: Use market-based signals on 6-9 month horizons (e.g. 6-9m relative performance of cyclicals), not 1-2 week reactions. Test signal decay by horizon pre/post 2010.
- Data needed: in tool.
- Confidence: high.

### Market reaction to big events is predictive (Trump 2016: stocks reversed up, bonds sold off)
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "the night Trump was elected bonds got murdered ... stock market was down like some crazy amount overnight ended up that day ... the market was predicting a big economic recovery")
- Type: signal
- Rule as testable logic: IF after a major event cyclicals outperform defensives by >= 5% over 1 month AND 10y yield rises >= 30 bp THEN reflation regime: overweight cyclicals/value/small caps, underweight long Treasuries 6-12m.
- Data needed: Ken French industries, DGS10. Tool partly (cyclical vs defensive 6m).
- Confidence: medium.

### Asymmetric one-way bets only (pound 1992 vs Brexit)
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "the beauty of the pound trade that you mentioned was a one-way bet it was either going to be flat or we're gonna make fifteen or twenty percent this is not so appealing you can either make 10 percent or lose 10 percent")
- Type: position sizing/risk
- Rule as testable logic: Only take currency/country positions when the downside is bounded (pegs/bands under pressure, e.g. reserves falling, rate defence) — size big when payoff skew >= 3:1, skip symmetric 1:1 binaries (elections, referendums).
- Data needed: FX reserves (IMF IFS; FRED TRESEGxxx series), pegged FX rates. Not in tool.
- Confidence: high.

### Courage to bet big and concentrated when conviction is high; buy lows feel terrible
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "you need the courage a bit big and a bit concentrated but also the courage to fight your own emotions I've never made a buy at a low that I didn't just feel terrible")
- Type: position sizing/risk
- Rule as testable logic: Sizing: when multiple independent signals align (e.g. >= 3 of inside-market, curve, credit, liquidity), go to maximum position (0% equity / 100% Treasuries or 100% equity), not partial. Test full-swing vs graded allocations.
- Data needed: in tool.
- Confidence: medium.

### Fed should pause when markets warn; forward guidance ties hands
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "I would sneak one in every time I could under booming financial conditions")
- Type: regime map
- Rule as testable logic: Fed hikes are benign when financial conditions are booming (S&P at highs, credit tight) and harmful when markets are falling. Test: S&P 12m return after hikes conditional on S&P drawdown at time of hike (< 5% vs > 10%).
- Data needed: DFEDTAR (1982), S&P (in tool), NFCI (FRED NFCI 1971).
- Confidence: medium.

### Cutting too late in 2007 caused crisis; cut 6-9 months earlier would have avoided it
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "had he cut six to nine months earlier we would have had a recession but I don't know whether we've had a financial crisis")
- Type: conflict/caveat
- Rule as testable logic: Narrative; supports treating "Fed hiking/holding while credit + housing collapse" as max-risk regime (overweight Treasuries, 0% equity).
- Data needed: in tool.
- Confidence: low.

### Trade wars hit business confidence (Smoot-Hawley analog)
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "we all know about smoot-hawley we know a way you all know about trade wars and we all know what all this nonsense is doing to business confidence")
- Type: signal (geopolitics)
- Rule as testable logic: IF trade policy uncertainty index (Baker-Bloom-Davis TPU) >= 2 std above its 5y mean THEN cut equity 1 unit, underweight China/EM exporters (FXI, EWY, EWT) for 6m (proposed).
- Data needed: Trade Policy Uncertainty index (policyuncertainty.com, monthly 1985 newspaper-based; Caldara et al TPU 1960), EPU (FRED USEPUINDXM 1985). Not in tool.
- Confidence: medium.

### Government shutdowns don't matter
- Source: Stanley Druckenmiller — Druckenmiller Bloomberg Dec 2018 (quote: "does it matter if the government shuts down I don't think so that's that's a lot of nonsense")
- Type: conflict/caveat
- Rule as testable logic: Ignore shutdown events (test: S&P returns around 1976-2025 shutdowns ~ unconditional).
- Data needed: shutdown dates list.
- Confidence: high.

---
## File 5: #133 - Jan van Eck- Macro Forces Shape Markets (Insightful Investor, July 2026)

### Four macro forces framework: deregulation, fiscal, monetary, technology
- Source: Jan van Eck — #133 van Eck (quote: "there are forces in the world government policy, government spending policy, fiscal policy, monetary policy, how much money is being printed, technology, war, these outside forces will shape financial markets")
- Type: regime map
- Rule as testable logic: Country allocation score = deregulation (+1 if improving) + fiscal impulse (+1 if deficit >= 5% GDP / widening) + monetary (−2 if central bank hiking >= 2 pp in 12m, +1 if easing) ; overweight top-ranked country ETFs. Each component tested separately below.
- Data needed: see components.
- Confidence: medium.

### Country deregulation / pro-business reform -> rising profits -> buy that country's stocks
- Source: Jan van Eck — #133 van Eck (quote: "If a if a government central government in a country is creating a pro business environment with by deregulating by the rule of law that is a great a great signal that they're probably going to be increasing corporate profits")
- Type: signal (country/EM)
- Rule as testable logic: IF a country's Economic Freedom score (Fraser / Heritage) or World Bank "ease of doing business"/regulatory quality improves by >= 1 std over 3-5y (proposed) THEN overweight that country index (MSCI country ETF) for 3-5y. Examples cited: China 1990s, India now (INDA).
- Data needed: Fraser Economic Freedom of the World (annual 1970/2000, free), Heritage Index (1995), World Bank Worldwide Governance Indicators "Regulatory Quality" (1996, free), MSCI country indexes (1970/1988), INDA (2012), FXI (2004). Not in tool.
- Confidence: high (he calls it "a clear pattern").

### Fiscal deficit 6% of GDP = "two feet on the gas pedal"
- Source: Jan van Eck — #133 van Eck (quote: "if they're running 6% of of uh GDP fiscal deficits, then they're, as I like to say, putting two feet on the gas pedal")
- Type: signal (fiscal)
- Rule as testable logic: IF federal deficit >= 5% of GDP outside a recession (unemployment not rising) THEN stimulus regime: overweight equities/real assets, underweight long Treasuries (inflation/term-premium risk) for 12m; IF budget balanced/surplus THEN no stimulus signal. Apply cross-country (IMF WEO deficits) to country ETFs.
- Data needed: FRED FYFSGDA188S (annual 1929), quarterly MTSDS133FMS (monthly deficit 1980) / GDP; IMF WEO general government net lending (1980, free). Not in tool.
- Confidence: high.

### Fed "slamming the brakes" (1% -> 4% in a year) = worry about equity exposure
- Source: Jan van Eck — #133 van Eck (quote: "they're jacking interest rates up from 1% to 4%. Like that's when you really want to worry about your equity exposure, right? Whenever the Fed is slamming the brakes on")
- Type: signal
- Rule as testable logic: IF fed funds 12m change >= +2.5 pp (proposed from 1%->4%) THEN cut equity to 50% (or apply the tool's warning cut with lower threshold). Otherwise stay fully invested ("very strong equity bias ... unless the Fed is jamming up interest rates").
- Data needed: FEDFUNDS (in tool as 12m change; tool uses >= 1 pt above 24m low).
- Confidence: high.

### Default: fully invested in equities except during aggressive Fed tightening
- Source: Jan van Eck — #133 van Eck (quote: "you just really want to be fully invested in equities as much as you can throughout cycles because it's pretty hard to time again unless the Fed is jamming up um interest rates")
- Type: position sizing/risk / regime map
- Rule as testable logic: Benchmark strategy: 100% equity unless FF 12m change >= +2 pp, then 50% equity / 50% T-bills. Compare to tool (which is close to this already).
- Data needed: in tool.
- Confidence: high.

### Monetary signal is muted when inflation leaves no room to cut
- Source: Jan van Eck — #133 van Eck (quote: "the likelihood was inflation was kind of in a in an area that didn't give the Fed a big budget to cut")
- Type: conflict/caveat
- Rule as testable logic: IF core inflation >= 3% THEN do not expect Fed easing in response to weakness; de-risk destination = T-bills not long Treasuries.
- Data needed: core CPI (in tool).
- Confidence: medium.

### 40-year falling-rate backtests are biased; regime has changed
- Source: Jan van Eck — #133 van Eck (quote: "whatever charts you're looking at over the last 40 years have this big bias to them of a falling interest rate and falling inflationary environment")
- Type: conflict/caveat
- Rule as testable logic: Backtest robustness: split results into rising-rate (1950-1981) and falling-rate (1982-2020) secular regimes; require rules to work (or at least not fail) in both. Use pre-1982 data (Shiller S&P 1871, GS10 1953, FF 1954).
- Data needed: Shiller data (1871), FRED GS10 (1953). Partly in tool.
- Confidence: high.

### 60/40 out; 60-70% equities + 10% real assets + rest bonds
- Source: Jan van Eck — #133 van Eck (quote: "we would be more like 60 70% equities and then 10% maybe real assets and then you know the balance in in bonds")
- Type: action/instrument / position sizing/risk
- Rule as testable logic: Strategic baseline to test: 65% equity / 10% real assets (gold + commodities, e.g. 5% GLD + 5% DBC) / 25% Treasuries vs 60/40 in post-2021 regime and in 1965-1981. He admits "very very little science".
- Data needed: gold & commodity series (World Bank 1960). Not in tool.
- Confidence: medium.

### Rebalance on schedule or price trigger: harvest winners (gold) into laggards (oil)
- Source: Jan van Eck — #133 van Eck (quote: "when gold was going up, you're just constantly harvesting some of those profits and reinvesting in in oil ... didn't know why you were buying oil at 60 or $55 still it made no sense but ... that paid off")
- Type: position sizing/risk
- Rule as testable logic: In a real-asset sleeve (gold, oil, copper, agriculture), rebalance quarterly or when any asset drifts >= 25% relative from target weight (proposed band); measure rebalancing premium vs buy-and-hold.
- Data needed: World Bank monthly commodity prices (gold, Brent/WTI, copper, agriculture index; 1960). Not in tool.
- Confidence: medium.

### In a liquidity crisis / bond-confidence shock, even gold falls (sell what you can)
- Source: Jan van Eck — #133 van Eck (quote: "if 10-year interest rates go up 200 basis points and we have a loss of confidence I can tell you nothing's going up even gold doesn't go up")
- Type: conflict/caveat (hedge)
- Rule as testable logic: IF 10y yield rises >= 1.0 pp in 3 months (proposed) or a dash-for-cash event (VIX > 40 with Treasuries also falling) THEN expect gold to fall short term: hedge sleeve = T-bills/cash, not gold; buy gold after the liquidation (e.g. 1 month after VIX peak).
- Data needed: DGS10, VIX, gold. Not in tool (gold).
- Confidence: medium.

### War-driven liquidation: Middle East sellers sold Treasuries and gold for cash
- Source: Jan van Eck — #133 van Eck (quote: "people in the in the Middle East were just liquidating. They were selling Treasury bonds and they were selling gold. They just needed cash")
- Type: conflict/caveat (geopolitics)
- Rule as testable logic: IF geopolitical shock (GPR spike) THEN do not assume Treasuries/gold rise in first month; test 1m returns of TLT and gold after GPR spikes.
- Data needed: GPR index (1985), gold, Treasury returns. Not in tool.
- Confidence: medium.

### Diversification by underlying exposure, not labels (Mag7 in growth/value/quality ETFs)
- Source: Jan van Eck — #133 van Eck (quote: "If it's a similar risk, then you can't be fooled by the number of line items and different labels that you have")
- Type: position sizing/risk
- Rule as testable logic: Same as Sohn: measure correlation/beta of each sleeve vs S&P; treat sleeves with corr > 0.8 as the same risk bucket. Private marks follow public marks with a lag.
- Data needed: sleeve returns.
- Confidence: high.

### Bitcoin: halving cycle predicts weak year after peak
- Source: Jan van Eck — #133 van Eck (quote: "Bitcoin, you know, we predicted it would fall this year because of the happening cycle")
- Type: signal
- Rule as testable logic: IF 12-24 months after a Bitcoin halving (Apr 2024 -> 2025 peak; 2026 weak) THEN underweight BTC; IF 0-12 months after halving THEN overweight. Very few cycles (2012, 2016, 2020, 2024).
- Data needed: BTC-USD (2010/2014). Not in tool; crypto may be outside scope.
- Confidence: medium (stated as their prediction method), statistical power very low.

### Gold and Bitcoin as one family (precious-metals-like); both peaked together
- Source: Jan van Eck — #133 van Eck (quote: "it's like platinum and palladium and silver like the family of precious metals that are related to gold but they certainly don't uh necessarily behave you know, kind of on top of each other")
- Type: conflict/caveat
- Rule as testable logic: Treat BTC, silver, platinum as satellites of a gold sleeve; test correlation regimes. No rule.
- Data needed: silver (World Bank 1960; SLV 2006), platinum (World Bank), BTC.
- Confidence: low.

### EM not one bloc; diversify across countries with different cycles/currencies (India)
- Source: Jan van Eck — #133 van Eck (quote: "I'm really starting to think of them less as one coherent group in a portfolio ... these countries are very as you know very well know very different from each other")
- Type: action/instrument (country/EM)
- Rule as testable logic: Allocate EM by country (India, China, Korea, Taiwan, Brazil, Mexico, Saudi) using country-level signals (trend, fiscal, deregulation, commodity linkage), not EEM as a block. Prefer countries with low correlation to US cycle and own non-dollarized currency (India) for diversification.
- Data needed: MSCI country indexes (1988 EM), country ETFs (EWZ 2000, EWY 2000, EWT 2000, EWW 1996, INDA 2012, FXI 2004, KSA 2015). Not in tool.
- Confidence: medium.

### Commodity cyclical upswing benefits Latin America / Middle East
- Source: Jan van Eck — #133 van Eck (quote: "maybe Latin America with the cyclical improvement in commodity prices that you know that's probably be with here with us for a while")
- Type: signal (commodity-country linkage)
- Rule as testable logic: IF broad commodity index 12m change > +15% AND above its 10m MA THEN overweight commodity-exporter equities (EWZ, EWW, ILF, Chile ECH, Saudi KSA, Australia EWA, Canada EWC) vs ACWI for 6-12m.
- Data needed: World Bank commodity indices (1960), MSCI country indexes. Not in tool.
- Confidence: medium.

### Higher returns possible outside the US now; time to diversify internationally
- Source: Jan van Eck — #133 van Eck (quote: "you can potentially do that without giving up returns because that you may actually have higher returns outside of the US")
- Type: signal
- Rule as testable logic: IF dollar 12m change < 0 (dollar falling) AND ex-US equities (EFA/ACWX) relative to S&P 10m MA slope > 0 THEN overweight international equities vs US (e.g. 40% of equity sleeve), else 20%. Dollar in tool.
- Data needed: MSCI EAFE / ACWI ex US (1970/1988), EFA (2001), dollar index (in tool).
- Confidence: medium.

### India underweighted in indexes; post-shock (war + tariffs) entry point
- Source: Jan van Eck — #133 van Eck (quote: "India suffered a lot because of the Iran war and the US tariffs. So, in a way, I think it's especially good time ... to kind of look at that market")
- Type: re-entry/exit (country)
- Rule as testable logic: IF a structurally favoured country (growth leader + deregulation) underperforms ACWI by >= 15% over 12m due to external shocks (oil, tariffs) THEN buy that country ETF (INDA) for 12-24m (proposed). Also: India is an oil importer -> oil spikes hurt it.
- Data needed: MSCI India (1993), INDA (2012), Brent. Not in tool.
- Confidence: medium.

### Oil importers hurt by oil shocks (India) — country-oil linkage
- Source: Jan van Eck — #133 van Eck (quote: "India suffered a lot because of the Iran war")
- Type: signal (country/commodity)
- Rule as testable logic: IF oil 3m change >= +30% THEN underweight oil-importing EM (India, Korea, Taiwan, Turkey) vs oil exporters (Saudi, Brazil, Norway, Canada) for 3-6m; reverse when oil falls.
- Data needed: Brent (FRED DCOILBRENTEU 1987; World Bank 1960), MSCI country indexes. Not in tool.
- Confidence: medium.

### Valuation only at extremes, within a trend (not as market timing)
- Source: Jan van Eck — #133 van Eck (quote: "I don't use valuation at the at the market or industry level, but then sometimes like within a trend, it can give you some kind of guidance one way or the other at extremes")
- Type: conflict/caveat
- Rule as testable logic: Use valuation (CAPE, P/S) only as a filter at extremes (top/bottom 5%) combined with trend; e.g. IF CAPE in top 5% AND 10m MA slope negative THEN cut equity. Supports tool's existing secondary use of CAPE.
- Data needed: CAPE (in tool).
- Confidence: medium.

### Cheap international markets need a catalyst, not just valuation
- Source: Jan van Eck — #133 van Eck (quote: "international markets are cheap on a valuation basis. Yes. But I want something a little bit more to be going for them")
- Type: conflict/caveat (country)
- Rule as testable logic: Country value (low CAPE) only counts when combined with momentum/trend or policy catalyst: overweight country IF CAPE in bottom tercile AND 12m return > 0 (or 10m MA slope > 0).
- Data needed: country CAPE (Research Affiliates / Barclays / Star Capital free snapshots; Norbert Keimling papers 1979; or MSCI country P/E), MSCI country indexes. Not in tool.
- Confidence: medium.

### Copper/metals: supply constraints + AI/power demand -> multi-year profitability
- Source: Jan van Eck — #133 van Eck (quote: "the demand for copper and other kind of metals with the kind of supply constraints and the inability to turn you know get a mine going in the short term should lead to good you know visible profitability several years out")
- Type: regime map (commodity cycle)
- Rule as testable logic: IF copper above 10m MA AND global mine supply growth < demand growth (ICSG deficit) THEN overweight copper (CPER) / copper miners (COPX) for 12m (proposed).
- Data needed: copper (FRED PCOPPUSDM 1990 / World Bank 1960; in tool as 6m change), ICSG supply-demand balance (monthly press releases, not easy). Partly in tool.
- Confidence: medium.

### Speculative-theme froth tell: price-to-sales instead of P/E in headlines; size small
- Source: Jan van Eck — #133 van Eck (quote: "they're not showing price to earnings ratios are price to sales that right there is kind of a signal like they're not profitable ... the solutions just don't size it too much like you know dip your toe")
- Type: position sizing/risk
- Rule as testable logic: Cap any thematic/speculative sleeve at <= 5% (proposed). Not a macro signal.
- Data needed: none.
- Confidence: medium.

### Avoid leveraged/inverse ETFs (tracking surprises)
- Source: Jan van Eck — #133 van Eck (quote: "Van has stayed away from like leveraged ETFs and inverse ETFs ... funds that are so sort of dislocated or super expensive or are generally things that we stay away from")
- Type: conflict/caveat (instrument)
- Rule as testable logic: For short exposure prefer cash/T-bills or puts over inverse ETFs; if inverse ETFs are used, simulate daily-reset decay. Also: commodity futures ETFs (USO) may not track spot oil — test roll yield.
- Data needed: USO vs WTI spot (2006). Not in tool.
- Confidence: medium.

### Bond ETFs add liquidity; fixed income is first to become illiquid
- Source: Jan van Eck — #133 van Eck (quote: "fixed income markets are the first markets to become less liquid and and having anything that adds liquidity to that ecosystem I think is fabulous")
- Type: conflict/caveat
- Rule as testable logic: Use liquid ETFs (HYG/LQD/TLT) for credit instruments; watch ETF discounts to NAV (HYG/LQD discount > 2%, proposed) as a stress signal (as in March 2020).
- Data needed: HYG/LQD price vs NAV (iShares history, 2007). Not in tool.
- Confidence: low.

### Low down-payment mortgages = unsustainable risk-taking (housing credit standards)
- Source: Jan van Eck — #133 van Eck (quote: "the fact that you could mortgage a house with almost no money down is like if someone asked me what is the one thing that, you know, the Fed got wrong")
- Type: signal (credit)
- Rule as testable logic: IF mortgage credit loosening extreme (MBA Mortgage Credit Availability Index at 10y high, or average LTV of new mortgages > 90%) THEN housing-credit bubble flag; underweight homebuilders/banks over 2-3y.
- Data needed: MBA MCAI (2004, partially free), FHFA LTV data (Monthly Interest Rate Survey, 1973), Senior Loan Officer survey mortgage standards (FRED SUBLPDHMSNQ, 2007). Not in tool.
- Confidence: low.

### Sovereign bond pricing disconnects (Greece < Germany; Japan low despite debt) are unreliable to trade
- Source: Jan van Eck — #133 van Eck (quote: "How did Greek bonds before the European financial crisis have lower interest rates than the German bond market ... I put that almost in a separate category of stuff that I just don't understand")
- Type: conflict/caveat
- Rule as testable logic: Do not build rules shorting sovereign bonds on debt levels alone (Japan widow-maker). Test: debt/GDP vs subsequent 5y yield change across G10 — expect weak relationship.
- Data needed: IMF debt/GDP, OECD 10y yields (FRED IRLTLT01xxM156N, 1950s-). Not in tool.
- Confidence: medium.

### Currency pegs break (ERM 1992) — hard to forecast
- Source: Jan van Eck — #133 van Eck (quote: "in the early 90s European currencies were all linked and then they broke. I just completely did not see that coming")
- Type: conflict/caveat
- Rule as testable logic: Pairs with Druckenmiller's one-way bet: IF a pegged currency's country has policy rate >> anchor and falling reserves THEN asymmetric short-currency bet. Low testability (few events).
- Data needed: FX reserves (IMF). Not in tool.
- Confidence: low.

### Nuclear/power demand driven by bipartisan policy shift (multi-year)
- Source: Jan van Eck — #133 van Eck (quote: "Nuclear is more influenced by public policy. There's been a bipartisan shift ... it's global")
- Type: regime map (sector)
- Rule as testable logic: Thematic; uranium (URA/URNM, Cameco proxy) price trend rule: IF uranium spot above 10m MA THEN hold uranium ETF sleeve <= 3%. Low priority.
- Data needed: uranium spot (Cameco/UxC monthly; IMF uranium price PURANUSDM on FRED, 1980). Not in tool.
- Confidence: low.

### Demographics: long trends (China shrinking, India rising)
- Source: Jan van Eck — #133 van Eck (quote: "China is going to shrink you know we know for sure almost from you know 1.5 4 billion to about 700 750 million in a 100 years")
- Type: regime map (country)
- Rule as testable logic: Structural tilt: working-age population growth by country as slow-moving input; overweight countries with rising working-age share (India, Indonesia, Mexico) vs shrinking (China, Korea, Japan) — 5y horizon test across MSCI countries.
- Data needed: UN World Population Prospects (1950, free), World Bank working-age population (SP.POP.1564.TO, 1960). Not in tool.
- Confidence: low (he says implications are "something different").

---
## File 6: Børge Brende - Podcast - In Good Company - Norges Bank Investment Management (June 2025)

Mostly geopolitical narrative; few explicit rules. All low-medium confidence.

### Record global debt limits fiscal response in the next recession
- Source: Børge Brende — In Good Company (quote: "the fact that we have the highest global debt since 1945 also gives nation states um a harder time if we're going to see a recession. There is not that much of fiscal muscles")
- Type: regime map (fiscal/debt)
- Rule as testable logic: IF government debt/GDP >= 100% (US) AND recession flag fires THEN expect smaller fiscal offset: hold de-risk longer (re-entry only after Fed easing >= 2 pp or S&P back above 10m MA), and prefer Treasuries/gold over credit. Cross-country: countries with debt/GDP > 100% get smaller post-recession equity rebounds (test, IMF data).
- Data needed: FRED GFDEGDQ188S (US federal debt % GDP, 1966), IMF Global Debt Database / WEO (1950s, free). Not in tool.
- Confidence: low.

### Geopolitical fragmentation (friend-shoring) -> slower growth, not full decoupling
- Source: Børge Brende — In Good Company (quote: "if you go too far in n shoring, friend shoring and only trade with people uh you like ... will also come with um economic cost and you will see more sluggish uh growth")
- Type: regime map (geopolitics)
- Rule as testable logic: IF world trade volume growth (CPB World Trade Monitor) < world industrial production growth for 12m (trade intensity falling, proposed) THEN underweight export-heavy markets (Korea EWY, Taiwan EWT, Germany EWG, China FXI) vs US for 12m.
- Data needed: CPB World Trade Monitor (monthly 2000, free; cpb.nl), MSCI country indexes. Not in tool.
- Confidence: low.

### Between world orders = "unruly times" (soft power -> hard power)
- Source: Børge Brende — In Good Company (quote: "between world orders, it's always uh unruly times. We know that from history")
- Type: regime map (geopolitics)
- Rule as testable logic: IF Geopolitical Risk Index 12m average in top quintile since 1985 THEN raise strategic allocation to real assets (gold, energy) by 5 pp and defence sector (ITA) tilt (proposed). Test 1985-2026.
- Data needed: Caldara-Iacoviello GPR (1900 historical / 1985 recent), gold, ITA (2006) / Ken French "Guns" industry (1926... actually 1963 in 49-industry set). Not in tool.
- Confidence: low.

### Tariffs + tighter labour (immigration curbs) = higher US inflation risk
- Source: Børge Brende — In Good Company (quote: "if you are paying more for imports and you're creating also a tougher uh market at home when it comes to access to labor can lead to higher inflation")
- Type: signal (inflation)
- Rule as testable logic: IF effective US tariff rate rises >= 3 pp in 12m (proposed) AND labour force growth < 0.5% y/y THEN inflation-up regime: overweight TIPS vs nominals (long breakevens), underweight long Treasuries for 12m.
- Data needed: effective tariff rate = customs duties / goods imports (FRED B235RC1Q027SBEA customs duties, 1947; IMPGS imports), labour force CLF16OV (1948), 10y breakeven T10YIE (2003). Not in tool.
- Confidence: medium.

### US soft landing more likely than hard landing (2025 view)
- Source: Børge Brende — In Good Company (quote: "I do think still that the US economy is uh very solid. I think it's going to continue to uh grow I believe more in the soft landing")
- Type: conflict/caveat (view, not a rule)
- Rule as testable logic: Not a rule; record as a 2025 view for later scoring.
- Data needed: n/a.
- Confidence: low.

### Europe turnaround: periphery (Spain, Greece) growing fastest in OECD
- Source: Børge Brende — In Good Company (quote: "look at the fastest growing of all the OCD economies including American economy is Spain and Spain was almost written off ... Another very fast growing economy is Greece")
- Type: signal (country)
- Rule as testable logic: Country rotation: IF a written-off country (equity index >= 50% below its prior peak in USD) moves to top quartile of OECD real GDP growth THEN overweight its index (EWP Spain, GREK Greece) for 2-3y. Generalisable "recovery from crisis" rule.
- Data needed: OECD quarterly GDP (FRED NAEXKP01xxQ657S, 1960s), MSCI country indexes. Not in tool.
- Confidence: low.

### European red tape holds back; mood shifts quickly (Davos gloom -> optimism)
- Source: Børge Brende — In Good Company (quote: "in Davos there was like gloom and doom uh when it came to Europe. I think uh things are not as bad in Europe")
- Type: signal (sentiment contrarian, country)
- Rule as testable logic: IF consensus pessimism on a region (e.g. Euro area Sentix / ZEW expectations in bottom decile) THEN overweight that region's equities (EZU/VGK) vs US for 12m (contrarian). Test with ZEW (1991) / EC economic sentiment indicator (1985).
- Data needed: ZEW economic sentiment (monthly 1991, free summary), EC ESI (Eurostat, 1985), MSCI EMU (1988). Not in tool.
- Confidence: low.

### China less dependent on US exports (20% -> 11-12%); structural headwinds (property, workforce)
- Source: Børge Brende — In Good Company (quote: "Chinese export to the US, it's gone down from 20% of their export in 2013 to now I think is around 11 12%. So they're more resilient")
- Type: regime map (country/EM)
- Rule as testable logic: Caveat for tariff shocks: China equity sensitivity to US tariff news should decline over time; test beta of FXI/MCHI to US trade-policy-uncertainty index pre/post 2018. China structural headwinds: property prices falling -> underweight China banks/property; no explicit threshold.
- Data needed: China exports by destination (IMF DOTS, free), China house prices (BIS residential property prices, FRED QCNN628BIS, 2005), TPU index. Not in tool.
- Confidence: low.

### Global trend growth slowed from ~4% to ~3%; AI may lift productivity ~10% over a decade
- Source: Børge Brende — In Good Company (quote: "for decades we had a global trend growth of close to 4%. We are no more than we're closer to 3%")
- Type: regime map
- Rule as testable logic: Long-run context only. Possible test: IF US productivity growth (5y avg) rises above 2% (proposed) THEN favour equities over bonds structurally (higher equity weight cap).
- Data needed: FRED OPHNFB (nonfarm productivity, 1947). Not in tool.
- Confidence: low.

### Energy security: over-dependence on one supplier is a risk (Europe/Russia gas)
- Source: Børge Brende — In Good Company (quote: "We have seen in Europe uh how bad an idea it was to base uh almost half of our natural gas um from Russia")
- Type: geopolitics-to-asset mapping
- Rule as testable logic: IF European natural gas price (TTF) 3m change >= +100% (supply shock, proposed) THEN underweight European equities (VGK/EWG) vs US and overweight US LNG/energy (XLE) for 6m.
- Data needed: TTF / EU natural gas (World Bank Pink Sheet "Natural gas, Europe", monthly 1960; FRED PNGASEUUSDM 1990), MSCI Europe. Not in tool.
- Confidence: low.

### AI cost collapse (DeepSeek) -> shift from hardware phase to software/applications phase
- Source: Børge Brende — In Good Company (quote: "the deepseek uh experience ... shows that we're maybe a little bit closer to the software phase where we can do applications")
- Type: regime map (sector)
- Rule as testable logic: Sector rotation: IF semis (SOXX) underperform software (IGV) by >= 10% over 3m (proposed) THEN rotate tech sleeve toward software for 6m. Weak, thematic.
- Data needed: SOXX (2001), IGV (2001). Not in tool.
- Confidence: low.

### Young, digital EMs (India, Indonesia, Vietnam, Nigeria, Bangladesh) have growth opportunity
- Source: Børge Brende — In Good Company (quote: "this open up also huge opportunities for the countries with a lot of young people. Look at Nigeria. Uh look at Indonesia, India, Bangladesh, Vietnam")
- Type: regime map (country/EM)
- Rule as testable logic: Same as demographics rule (van Eck): working-age population growth tilt across EM country ETFs (INDA, EIDO, VNM, NGE); 5y horizon.
- Data needed: World Bank population 15-64 (1960). Not in tool.
- Confidence: low.

---
## File 7: Global Macro- Discretionary vs. Systematic - Who Wins- - Global Alts 2025 - Pablo Calderini (Graham panel, Feb 2025)

Mostly process discussion; testable content:

### Systematic macro signal families: fiscal, monetary, growth, inflation + value, mean reversion, carry, momentum
- Source: Pablo Calderini — Global Alts 2025 (quote: "you look at things like fiscal monetary policy huge huge amount of focus on monetary policy central banks fiscal Dynamics growth inflation and then some some some signals that you can classify more as factors like value or mean reversion or carry")
- Type: regime map / action/instrument
- Rule as testable logic: Build cross-asset sleeves (equity indexes, 10y bonds, currencies, commodities) with four standard factors, monthly rebalance: (1) time-series momentum (12m return > 0 -> long), (2) carry (currencies: rate differential; bonds: term spread; commodities: futures roll yield), (3) value (equity CAPE / real yield / PPP deviation), (4) macro fundamentals momentum (growth and inflation surprises: 6m change in PMI/CPI). Rank and go long top / short bottom tercile.
- Data needed: country 10y yields (FRED IRLTLT01xxM156N, 1960s), policy rates (FRED/BIS), FX (FRED DEX* 1971), commodity futures (not free; World Bank spot), MSCI country indexes, OECD CLI (FRED, 1955). Not in tool.
- Confidence: high (described as their method).

### Systematic horizon 1-3 months; discretionary week-to-week
- Source: Pablo Calderini — Global Alts 2025 (quote: "our Quant programs typically run one to two month Horizon maybe three months")
- Type: conflict/caveat
- Rule as testable logic: Design choice: macro signals rebalanced monthly with 1-3m forecast horizon are the industry norm; test the tool's signals at 1m, 3m, 6m horizons and pick the best-decaying horizon.
- Data needed: in tool.
- Confidence: high.

### Trend-following convexity is mechanical; new signals that correlate with trend cluster add nothing
- Source: Christian (CFM) — Global Alts 2025 (quote: "this idea of convexity that was brought up I it's interesting because it's really just a mechanical effect so when you Trend follow that's going to emerge")
- Type: hedge / conflict/caveat
- Rule as testable logic: (a) Use a trend sleeve as convex hedge (positively skewed in large moves). (b) Methodology: reject any new macro indicator whose signal correlation with a 12m trend signal on the same asset > 0.7 (proposed) — it's not new information.
- Data needed: asset prices.
- Confidence: high.

### Macro/trend strategies are "positively convex", capture the right tails
- Source: Jackie Rosner — Global Alts 2025 (quote: "these strategies tend to be positively convex and EV friendly and and tend to capture the right Tales appropriately")
- Type: hedge
- Rule as testable logic: Test a 10-20% allocation to diversified trend (multi-asset TSMOM) as permanent tail hedge vs the tool's binary de-risking; measure returns in S&P months < -5%.
- Data needed: AQR TSMOM (1985) or SG Trend index; build from ETFs/futures proxies. Not in tool.
- Confidence: medium.

### Sharpe benchmarks: discretionary macro ~1; average futures strategy ~0.5 at ~2x vol
- Source: Jackie Rosner — Global Alts 2025 (quote: "an average uh good discretionary macr Trader might have a sharp that's uh just under one ... the average future strategy whether it's a trend or non- trend has a sharp much lower maybe something like 0.5")
- Type: conflict/caveat
- Rule as testable logic: Realistic expectation: a systematic macro overlay should target Sharpe ~0.5; distrust backtests showing > 1.0 (overfitting check).
- Data needed: n/a.
- Confidence: high.

### Don't over-diversify managers/strategies ("water down the soup")
- Source: Jackie Rosner — Global Alts 2025 (quote: "you need definitely you know more than one or two managers for sure but definitely less than 10 because you put too many people too much diversification and you just water down the soup")
- Type: position sizing/risk
- Rule as testable logic: For signal combination: use 3-8 distinct signal families rather than dozens of overlapping indicators (relevant to tool's 43 indicators; test whether a 5-8 indicator subset matches the full set).
- Data needed: in tool.
- Confidence: medium.

### Never override systematic signals; constrain risk models for non-model risks (elections, regulation)
- Source: Christian (CFM) — Global Alts 2025 (quote: "we never override signals but on rare occasions we'll put constraints on our risk models and ideally that'll feed back into the system you know you codify the logic")
- Type: position sizing/risk
- Rule as testable logic: Event-risk overlay: around pre-identified binary events (elections, major central bank meetings), cap gross exposure / volatility target (e.g. reduce vol target by 25%, proposed) without changing signals.
- Data needed: event calendar.
- Confidence: medium.

### Unsupervised ML overfits; prefer supervised, interpretable methods
- Source: Pablo Calderini — Global Alts 2025 (quote: "we don't like to use unsupervised machine learning I think it has a huge today it's super prone to over Feit so to perform incredibly well in Sample but terrible out of sample")
- Type: conflict/caveat
- Rule as testable logic: Methodology: keep the tool's pre-registered, interpretable rules; walk-forward only.
- Data needed: n/a.
- Confidence: high.

### "Don't fight the Fed" -> "don't fight Trump"; policy "beta dependent" (watches equity market)
- Source: Jackie Rosner — Global Alts 2025 (quote: "for for decades uh Traders have talked about things like uh uh don't fight the FED uh but now with the new Administration there's another Mantra people could say don't fight Trump")
- Type: regime map
- Rule as testable logic: "Trump put" test: after S&P drawdowns >= 10% in 2017-2020 and 2025-2026, did policy reversals (tariff pauses) follow within 1-2 months? IF administration historically reacts to equity declines THEN buy S&P after a 10-15% policy-induced drawdown (2025 April analog). Very small sample.
- Data needed: S&P (in tool), event list.
- Confidence: low.

### Geopolitical risk cuts both ways for inflation
- Source: Jackie Rosner — Global Alts 2025 (quote: "geopolitical risk goes both ways elevated risk could be inflationary uh if if geopolitical risk goes away it could be deflationary")
- Type: regime map
- Rule as testable logic: IF GPR index rises AND oil rises THEN inflationary geopolitics (favour commodities, short duration); IF GPR falls and oil falls THEN disinflation (favour long duration). Map via oil reaction, not GPR alone.
- Data needed: GPR, WTI. Not in tool (GPR).
- Confidence: medium.

### China exporting deflation; strong dollar bid
- Source: Jackie Rosner — Global Alts 2025 (quote: "there's massive debts out there mounting deficits a strong dollar bid there's a fear of uh China exporting deflation")
- Type: signal (inflation/country)
- Rule as testable logic: IF China PPI y/y < 0 for >= 6 months (proposed) THEN expect lower US goods inflation: favour long Treasuries vs TIPS, underweight commodity exporters (EWZ, EWA) for 12m.
- Data needed: China PPI (FRED CHNPIEATI01GYM / NBS, 1996). Not in tool.
- Confidence: low.

### Biggest macro risks (panel): unsustainable fiscal trajectory; AI disruption; inflation/higher rates
- Source: Pablo Calderini / panel — Global Alts 2025 (quote: "biggest macro risk fiscal trajectory unsustainable good I agree definitely artificial intelligence just shaking things up uh inflation higher rates")
- Type: signal (fiscal/debt)
- Rule as testable logic: IF federal interest outlays / GDP rising AND term premium 12m change > +0.5 pp THEN fiscal-stress regime: shorten duration (no TLT), overweight gold/real assets.
- Data needed: FRED A091RC1Q027SBEA (federal interest payments, 1947), GDP; term premium (in tool, ACM/KW). Interest outlays not in tool.
- Confidence: medium.

### Expected hedge-fund/macro returns: cash + 3-5% with no beta
- Source: Nicholas Cormier (CPP) — Global Alts 2025 (quote: "probably somewhere in like the cash plus three to five range and that's with with no exposure to Beta")
- Type: conflict/caveat
- Rule as testable logic: Benchmark for any macro overlay the tool adds: target excess return 3-5% p.a. over T-bills with zero beta.
- Data needed: T-bill (in tool).
- Confidence: medium.

### Fundamental dispersion across regions (China weak, US exceptional, DM in between) = macro opportunity
- Source: Nicholas Cormier (CPP) — Global Alts 2025 (quote: "there's a lot of fundamental dispersion for macro strategies to take advantage of and capture")
- Type: signal
- Rule as testable logic: IF cross-country dispersion of 12m GDP growth forecasts / PMIs (std across G10+China) in top quintile THEN increase allocation to cross-country relative-value sleeve (long top, short bottom country indexes/currencies) (proposed).
- Data needed: OECD CLI by country (FRED, 1955-), PMIs (not free long history). Not in tool.
- Confidence: low.

---
## File 8: Rob Citrone and Karen Karniol-Tambour at Sohn 2025 (May 2025)

### Regime shift: from deflationary globalization to "modern mercantilism" -> US-only portfolios vulnerable
- Source: Karen Karniol-Tambour — Sohn 2025 (quote: "the last 15 years made the United States such a winner that pretty much the best thing you could have held is a simple S&P 500 ... it's hard not to feel that we're fundamentally in a different place")
- Type: regime map
- Rule as testable logic: Strategic: when the regime flags "inflationary/fragmented" (core CPI > 3% AND trade intensity falling AND dollar 12m change < 0), cap US share of equity sleeve at 60% (vs ~75% market cap) and spread rest across regions/countries. Test with MSCI regional indexes 1970-2026 (1970s inflationary regime: ex-US outperformed).
- Data needed: MSCI World ex-US / EAFE / EM (1970/1988), dollar index (in tool), CPB world trade (2000). Not in tool.
- Confidence: medium.

### Take geographic diversification seriously; different growth/inflation/monetary cycles
- Source: Karen Karniol-Tambour — Sohn 2025 (quote: "the most fundamental form of diversification is to be in countries that actually have a different system, that actually have a different beat of the drum, different growth, different inflation, different monetary policy")
- Type: position sizing/risk (country)
- Rule as testable logic: Allocate equity risk across countries by low correlation of their macro cycles to the US (e.g. inverse-correlation weighting of country index returns over 36m), with country-level trend filter (10m MA). Compare drawdowns vs S&P-only.
- Data needed: MSCI country indexes (1970/1988), country ETFs. Not in tool.
- Confidence: high.

### Global investors over-concentrated in US assets; slow repatriation weighs on dollar for years
- Source: Rob Citrone / Karen Karniol-Tambour — Sohn 2025 (quote: "the flip side of a massive trade deficit is a huge amount of current account inflows that people are buying all of our things and that doesn't go away in a day")
- Type: signal (currency)
- Rule as testable logic: IF US net international investment position (NIIP) / GDP at record low (more negative) AND dollar real effective exchange rate in top decile of 30y range THEN short USD vs EUR and JPY for 1-3y (slow-moving); confirm with dollar 12m change < 0 (trend).
- Data needed: BEA NIIP (FRED IIPUSNETIQ, quarterly 2006; annual 1976), BIS real effective dollar (FRED RBUSBIS, 1994; Fed broad real TWEXBPA 1973), EURUSD (DEXUSEU 1999; synthetic DEM pre-1999), USDJPY (1971). Dollar 12m change in tool; NIIP/REER not.
- Confidence: medium.

### Short the dollar vs euro and yen (big crosses), not vs everything
- Source: Karen Karniol-Tambour — Sohn 2025 (quote: "I like shorting the dollar, not against everything, but euro, yen, kind of the big crosses")
- Type: action/instrument (currency)
- Rule as testable logic: IF dollar overvalued (REER top quintile) AND rate differentials (US 2y - Germany/Japan 2y) narrowing over 6m THEN long FXE + FXY (or UDN) for 12m.
- Data needed: FRED DGS2, Germany 2y (Bundesbank, 1972), Japan 2y (MoF), REER, FXE/FXY (2005/2007). Not in tool.
- Confidence: medium.

### Currency moves driven by slow governance-bound flows take time; early moves are speculative/hedges
- Source: Karen Karniol-Tambour — Sohn 2025 (quote: "the dollar move so far has been primarily people are either speculative or are able to do things really quickly like I can just put on a hedge ... lots of the big currency drivers don't work that way")
- Type: re-entry/exit
- Rule as testable logic: Currency trends persist: use 12m time-series momentum on USD vs EUR/JPY with long holding periods (rebalance quarterly).
- Data needed: FX rates (FRED 1971). Not in tool.
- Confidence: medium.

### Latin America: political/management change + high rates + cheap currencies = big returns across equities, FX, credit, rates
- Source: Rob Citrone — Sohn 2025 (quote: "the great thing about Latin America is you can make huge returns uh in equities but also in currencies, credit rates because rates are high, currencies are cheap")
- Type: signal (country/EM)
- Rule as testable logic: IF an EM country has (a) real policy rate >= 4% (policy rate - CPI y/y, proposed), (b) currency REER in bottom quintile of its 10y range, (c) market-friendly political change (election win of reform candidate; proxy: sovereign spread tightening >= 100 bp in 6m) THEN overweight its equity ETF (EWZ, EWW, ARGT, ECH, EPU, GXG) and local-currency bonds/FX for 12-24m.
- Data needed: EM policy rates (BIS policy rates, monthly, free), EM CPI (IMF IFS / FRED), BIS REER (1994), EMBI spreads (not free; proxy EMB price 2007, or FRED BAMLEMCBPIOAS EM corporate OAS 1998), MSCI country indexes. Not in tool.
- Confidence: medium-high (central to his process).

### Judge countries like companies: management and policies first
- Source: Rob Citrone — Sohn 2025 (quote: "we look at countries like we look at companies you we first thing we look at is management and how good is management and what are the policies")
- Type: signal (country)
- Rule as testable logic: Country quality score from World Bank governance indicators (government effectiveness, regulatory quality) change; IF score improving 2y in a row THEN overweight. Overlaps with van Eck deregulation rule.
- Data needed: World Bank WGI (annual 1996). Not in tool.
- Confidence: medium.

### Elections as catalysts for EM re-rating (Peru, Colombia, Chile, Brazil 2025-26)
- Source: Rob Citrone — Sohn 2025 (quote: "we have big four big elections in the next few months uh next 18 months in in Peru, Colombia, Chile, and Brazil. And we think that's going to usher in substantial change")
- Type: signal (country)
- Rule as testable logic: Event rule: buy EM country ETF 6 months before a national election IF polls favour the market-friendly candidate (proxy: currency strengthening >= 5% over prior 3m); sell if outcome adverse. Test historically on LatAm elections 2000-2024.
- Data needed: election dates, FX, country ETFs. Not in tool.
- Confidence: low (needs polling data).

### Brazil risk: 500 bp of hikes "will have some consequences"
- Source: Rob Citrone — Sohn 2025 (quote: "a little worried about the fact they've had to hike rates 500 basis points in the last few months, which will have some consequences")
- Type: signal (country/EM monetary)
- Rule as testable logic: IF an EM central bank hikes >= 400 bp in 12m THEN near-term equity headwind (underweight that country 6m); once hiking stops and inflation peaks THEN rates can fall "hundreds of basis points": go long local bonds / equities (12-24m).
- Data needed: BIS policy rates (EM, 1990s), country ETFs. Not in tool.
- Confidence: medium.

### Post-devaluation, very-high-yield currencies (Nigeria 30%, Turkey 45%) = carry opportunity
- Source: Rob Citrone — Sohn 2025 (quote: "I like currencies like a place like Nigeria and Turkey where they've had big devaluations and interest rates are incredibly high 30% in Nigeria 45% in Turkey")
- Type: action/instrument (FX carry)
- Rule as testable logic: IF a currency has fallen >= 40% vs USD in prior 24m (devaluation done) AND real policy rate > 5% THEN long that currency (carry) for 6-12m, with stop-loss -10% (proposed).
- Data needed: FX (FRED/BIS), policy rates (BIS), CPI. Retail instruments limited (TUR equity ETF, no FX ETF) — mostly not tradable retail. Not in tool.
- Confidence: medium.

### Treasuries need a risk premium; US 10y to 5-5.25% (fiscal stimulus, no Fed cuts)
- Source: Rob Citrone — Sohn 2025 (quote: "I think rates in the US are going to back up particularly in the in the 10-year sector and I'm kind of thinking that we're going to hit five to five and a quarter this year")
- Type: signal (rates/fiscal)
- Rule as testable logic: IF fiscal stimulus ahead (tax cuts; deficit/GDP widening >= 1 pp) AND Fed on hold AND term premium near zero (ACM 10y TP < 0.5%, proposed) THEN underweight 10y/long Treasuries (short TLT or hold T-bills) for 12m. (Outcome 2025: 10y peaked ~4.6-4.8% — not reached.)
- Data needed: ACM term premium (NY Fed, daily 1961; in tool as 12m change), deficit/GDP. Partly in tool.
- Confidence: medium.

### Treasury vs cash: little risk premium -> backup in yields reasonable
- Source: Karen Karniol-Tambour — Sohn 2025 (quote: "you kind of started this environment with nothing really looking like a big risk premium on treasuries. If you said, 'What am I getting for Treasury versus cash?' Probably not much")
- Type: signal
- Rule as testable logic: IF 10y yield - 3m T-bill <= 0.5 pp AND term premium <= 0.5% THEN prefer T-bills over long Treasuries in the de-risk sleeve; IF 10y - 3m >= 2 pp THEN long Treasuries pay for duration.
- Data needed: DGS10, DTB3 (1954/1962), ACM TP. Partly in tool.
- Confidence: high.

### Prefer non-US government bonds where central banks can ease (deflationary tariff shock abroad)
- Source: Karen Karniol-Tambour — Sohn 2025 (quote: "I like fixed income a lot more in other countries in the United States because I think that other central banks. For them, easing is just more straightforward")
- Type: signal (rates, country)
- Rule as testable logic: IF foreign inflation (core CPI) below target AND their currency weakened / energy prices falling AND US inflation >= 3% THEN overweight foreign government bonds (currency-hedged: BWX/BNDX; UK gilts IGLT) vs Treasuries for 12m. Rank countries by (10y yield - core CPI) and (policy rate - neutral).
- Data needed: OECD 10y yields (FRED IRLTLT01xxM156N, 1950s+), OECD CPI (FRED), BNDX (2013), BWX (2007). Not in tool.
- Confidence: high.

### Tariff inflation is one-off like a VAT unless supply problems (then COVID-like)
- Source: Karen Karniol-Tambour — Sohn 2025 (quote: "an inflationary impulse from the tariffs is a one-off. It kind of goes through like a VAT tax increase and fades. But you don't know for sure. And the more it comes with supply problems, the more it looks more like a co")
- Type: regime map (inflation)
- Rule as testable logic: IF tariffs raise goods inflation AND supply-chain pressure (NY Fed GSCPI) > 1 std THEN persistent inflation: underweight duration, overweight TIPS/commodities; IF GSCPI < 0 THEN treat tariff inflation as transitory.
- Data needed: NY Fed Global Supply Chain Pressure Index (monthly 1997, free), core goods CPI (FRED CUSR0000SACL1E, 1957). Not in tool.
- Confidence: medium.

### Fixed-income pressure "once every 10-15 years" in some markets — measure pressure vs history
- Source: Karen Karniol-Tambour — Sohn 2025 (quote: "we can kind of measure the strength of the pressure relative to history and I think in some of these fixed income markets it's like a once every 101 15 year type size")
- Type: signal / position sizing/risk
- Rule as testable logic: Size positions by z-score of the macro pressure (e.g. (policy rate - inflation - growth) z-score vs 30y history); IF |z| >= 2 THEN double normal position size (proposed).
- Data needed: country rates/inflation/growth (OECD via FRED). Not in tool.
- Confidence: medium.

### Japan and US yields go higher (shorts); Brazil, Mexico, Argentina, Turkey yields fall a lot; UK most attractive DM
- Source: Rob Citrone — Sohn 2025 (quote: "I think Japan goes higher and the US goes higher. I think those are the two clear shorts. I think something like a Brazil or a Mexico, Argentina, um Turkey are places where rates can come down a lot")
- Type: action/instrument (rates)
- Rule as testable logic: Cross-country bond rule: long bonds where real policy rate is highest and inflation falling (EM high yielders: EMLC ETF 2010 as retail proxy); short (avoid) bonds where inflation is rising and policy rate is below inflation (Japan). Test as rank on (policy rate - CPI) with 12m holding.
- Data needed: BIS policy rates, CPI, EMLC (2010), local bond indexes (JPM GBI-EM not free). Not in tool.
- Confidence: medium.

### Not the best time to take risk in the US; take it outside (70% risk ex-US, half in EM)
- Source: Rob Citrone — Sohn 2025 (quote: "we have, you know, probably 70% of our risk outside the US and probably half our risk in EM")
- Type: position sizing/risk
- Rule as testable logic: Variant to test: risky sleeve 30% US / 35% DM ex-US / 35% EM when dollar 12m change < 0 and US CAPE > 30 (proposed); else market-cap weights.
- Data needed: MSCI indexes, CAPE (in tool), dollar (in tool).
- Confidence: medium.

### Make money in a country via bonds and currency, not just stocks (China: weak economy -> long bonds, short CNY)
- Source: Karen Karniol-Tambour — Sohn 2025 (quote: "being in China, being able to also profit from the fact the economy has actually been weak, the bonds have been a good buy, that the currency have devalued")
- Type: action/instrument (country)
- Rule as testable logic: Country regime mapping: IF country growth weak (OECD CLI < 100 and falling) AND inflation < 2% THEN long that country's government bonds (CBON for China, 2014) and short its currency vs USD; IF growth strong THEN long equities. Applies across countries.
- Data needed: OECD CLI (FRED, incl. China 1990s), China 10y yield, CNY (DEXCHUS 1981). Not in tool.
- Confidence: high.

### Ignored asset classes: commodities/oil and duration+currency "alpha spaces" are back
- Source: Karen Karniol-Tambour — Sohn 2025 (quote: "duration and currency are great alpha spaces that have seemed uninteresting for a while where rates were zero and are kind of coming back in a big way")
- Type: regime map
- Rule as testable logic: IF policy rates > 2% across G10 (non-ZIRP) THEN enable bond-curve and FX sleeves (their alpha is higher when rate dispersion is high); IF ZIRP THEN disable. Test cross-country bond momentum/value returns vs rate dispersion.
- Data needed: G10 policy rates (BIS). Not in tool.
- Confidence: medium.

### Private credit = equity-like risk, not a bond diversifier
- Source: Karen Karniol-Tambour — Sohn 2025 (quote: "The issue with private credit is that you tend to get depending where you are in the risk spectrum something much more similar to equity-like risk")
- Type: conflict/caveat (hedge)
- Rule as testable logic: Exclude BDCs/private credit (BIZD) and high-yield from the de-risk sleeve; treat them as equity beta (beta to S&P ~0.6-0.9; test).
- Data needed: BIZD (2013), HYG (2007). Not in tool.
- Confidence: high.

### Oil: buy at $55-58 given Iran/Israel tail risk (near-term asymmetric)
- Source: Rob Citrone — Sohn 2025 (quote: "oil when it got down to 55 was a very interesting buy ... I think the risk award in oil prices is phenomenal right here. Long-term, I'm not sure, but near-term, I like it a lot")
- Type: action/instrument (geopolitics/commodity)
- Rule as testable logic: IF WTI in bottom quintile of its 5y range (or <= real 10y median -25%, proposed) AND Geopolitical Risk index in Middle East elevated (GPR > 12m mean) AND positioning short (CFTC managed money net short or low) THEN long oil (USO/BNO) for 3-6m with defined risk.
- Data needed: WTI (FRED 1986), GPR (1985), CFTC COT crude managed money (free, 2006; legacy non-commercial 1986). Not in tool (oil 6m change only).
- Confidence: medium.

### Gold vs oil positioning: everybody long gold, people short oil -> oil spike risk
- Source: Karen Karniol-Tambour — Sohn 2025 (quote: "gold's had a big run and it everybody's long and oil I think people are short. So I think technically in the near term you could see a big spike in in oil with gold not not performing as well")
- Type: signal (positioning, commodity)
- Rule as testable logic: Contrarian positioning: IF CFTC net speculative position (as % of open interest) in top decile of 3y range THEN underweight that commodity next 3m; IF bottom decile THEN overweight. Apply to gold, crude, copper, silver, grains.
- Data needed: CFTC Commitments of Traders (weekly, 1986 legacy / 2006 disaggregated, free). Not in tool.
- Confidence: medium.

### Commodities as inflation-risk assets for a world with more inflation risk
- Source: Karen Karniol-Tambour — Sohn 2025 (quote: "the entire commodity complex, gold of course being a unique commodity within that, these are useful assets. You're clearly looking at a world that has more inflation risk than it used to")
- Type: hedge (inflation)
- Rule as testable logic: Strategic 5-10% commodity + gold allocation when inflation regime flag on (core CPI > 3% or 5y breakeven > 2.5%); 0-5% otherwise.
- Data needed: World Bank commodity / gold (1960), T5YIE (2003; in tool as 5y expectations 6m change).
- Confidence: medium.

### Need shorts/protection and liquidity in a fractured world
- Source: Rob Citrone / Karen Karniol-Tambour — Sohn 2025 (quote: "We think it's a very tricky world. We think you have to have shorts. We like we like the fact you have to protect your portfolio at certain points here. Uh and you have to be dynamic")
- Type: hedge / position sizing/risk
- Rule as testable logic: Keep >= 20% of the portfolio in liquid instruments able to move monthly; add tactical index puts (SPY 3m 10% OTM, <= 1% of portfolio per quarter, proposed) when the warning share is between the tool's thresholds (partial-warning zone).
- Data needed: VIX for option pricing (in tool), CBOE PPUT index (1986) as proxy.
- Confidence: medium.

### Regional siloing: Americas / Europe / Asia blocs; capital stays home (Germany defence & infrastructure)
- Source: Rob Citrone / Karen Karniol-Tambour — Sohn 2025 (quote: "look at what Germany did they said we should make our own defense make our own infrastructure so there'll be more opportunities to actually have capital stay at home")
- Type: regime map (fiscal/country)
- Rule as testable logic: IF a country announces fiscal expansion >= 1% of GDP (defence/infrastructure) THEN overweight its equities (EWG) and underweight its long bonds (Bunds) for 12m — "fiscal impulse -> equities up, bond yields up" (test across G10 fiscal impulses, IMF Fiscal Monitor).
- Data needed: IMF Fiscal Monitor structural balance changes (annual 1980s), MSCI country indexes, OECD 10y yields. Not in tool.
- Confidence: medium.

### US fiscal stimulus + reshoring -> 2026 boom; Fed won't cut in 2025
- Source: Rob Citrone — Sohn 2025 (quote: "I think next year's a boom in the economy in the US on the back of significant fiscal uh tax cuts ... I don't think the Fed's going to cut any rates this year")
- Type: conflict/caveat (view)
- Rule as testable logic: View (Fed did cut in late 2025 — partly wrong); supports fiscal-impulse rule: IF deficit/GDP widens >= 1 pp outside recession THEN overweight equities 12m.
- Data needed: deficit/GDP.
- Confidence: low (forecast, not a rule).

### Contradiction: Citrone (US rates up, US growth boom 2026) vs Karniol-Tambour (slowdown + inflation ahead; prefers foreign bonds)
- Source: Karen Karniol-Tambour — Sohn 2025 (quote: "I think there's very clearly some degree of economic slowdown ahead of us and some inflation ahead of us because of the set of policies")
- Type: conflict/caveat
- Rule as testable logic: Both agree US Treasuries are unattractive; disagree on US growth. Shared testable: stagflation-lite (growth slowing + inflation >= 3%) -> avoid US duration, prefer foreign bonds and gold.
- Data needed: in tool (state machine).
- Confidence: medium.

---
## File 9: Steve Cohen and Jawad Mian at Sohn 2025 (May 2025)

Mostly personal/psychology; macro content in first third.

### Tariff stack (effective rate 14-17%) -> significant slowing; ~45% recession odds
- Source: Steve Cohen — Sohn 2025 (quote: "When you add up the tariffs, you add up the 10% rate, the sectoral tariffs, and whatever happens with China, you're probably going to end up ... 14 to 17% rate perhaps")
- Type: signal (trade policy)
- Rule as testable logic: IF effective US tariff rate (customs duties / goods imports) rises >= 5 pp within 12m THEN growth-slowdown flag: cut equity 1 unit, favour defensives, for 12m.
- Data needed: FRED customs duties (B235RC1Q027SBEA, quarterly 1947) / goods imports (BOPGTB or IMPGS). Not in tool.
- Confidence: medium.

### Fed won't cut quickly on tariff slowdown (tariff inflation fear)
- Source: Steve Cohen — Sohn 2025 (quote: "we don't think the Fed's going to act right away because they're still going to be worried about inflation from tariffs")
- Type: regime map
- Rule as testable logic: IF growth slowing AND inflation >= 3% due to tariffs THEN expect delayed Fed easing: equities lack the "Fed put"; de-risk to T-bills rather than long bonds. (Same as stagflation rule.)
- Data needed: in tool.
- Confidence: medium.

### Slowing growth + high multiples = little upside -> sideways/trading-range market
- Source: Steve Cohen — Sohn 2025 (quote: "with slowing growth and like I'll say it again multiples you know being on the higher side I think that's kind of a a mix that doesn't give you much upside")
- Type: regime map / position sizing/risk
- Rule as testable logic: IF forward P/E (or CAPE) in top quintile AND real GDP growth forecast/OECD CLI falling THEN expect range-bound market: lower equity to ~60-70% and/or sell covered calls (BXM-like overlay) for 6-12m; buy near range lows (-10 to -15% from high), trim near highs.
- Data needed: CAPE (in tool), OECD CLI US (FRED USALOLITONOSTSAM, 1955), CBOE BXM index (1986) for covered-call overlay. CLI/BXM not in tool.
- Confidence: medium.

### Watch market reaction when data turns down (priced-in test)
- Source: Steve Cohen — Sohn 2025 (quote: "I want to see when the data turns down how the market's going to react and that'll tell me a lot about whether we're priced correctly or not")
- Type: signal
- Rule as testable logic: IF macro surprise index negative (Citi Economic Surprise Index < -30, or tool warnings rising) AND S&P 1m return >= 0 THEN market resilient -> stay invested/raise equity; IF S&P falls >= 3% on bad data THEN not priced -> de-risk. Price-vs-news test.
- Data needed: Citi Economic Surprise Index (not free; proxy: own surprise from ISM vs prior consensus not available; alternative: change in tool warning count). Not in tool.
- Confidence: medium.

### Policy capitulation (tariff deal) "raises the floor": drawdown limited to retest of lows (10-15%)
- Source: Steve Cohen — Sohn 2025 (quote: "it's possible we can go back toward the lows which is 10 15%. So it's not a calamity and and what Trump done you know did recently actually raises the floor")
- Type: re-entry/exit
- Rule as testable logic: IF a policy reversal removes the tail scenario after a >= 15% drawdown THEN hold equities at neutral (not max) and treat retest of prior low as buy zone (buy if S&P within 5% of the prior low, proposed).
- Data needed: S&P (in tool).
- Confidence: low.

### Sharp V-shaped drop-and-recovery is unusual (pandemic-like)
- Source: Steve Cohen — Sohn 2025 (quote: "this is unusual for something like this to happen where you you you drop significantly and rally back as quickly. I mean, the closest thing might might have been a pandemic")
- Type: conflict/caveat
- Rule as testable logic: Re-entry rule design: test whether fast re-entry (S&P back above 10m MA within 2 months of a >= 15% drop) beats waiting for macro confirmation; relevant to 1987, 1998, 2020, 2025.
- Data needed: S&P (in tool).
- Confidence: medium.

### Regime change: what worked last year (multiple expansion) won't work; raise the bar, lower expectations
- Source: Steve Cohen — Sohn 2025 (quote: "I was trying to get them to to think that we're in a different regime and what worked in the past is not going to work this year")
- Type: position sizing/risk
- Rule as testable logic: After a year with S&P return >= 20% and P/E expansion >= 15% (proposed), cap equity at 80% next year unless earnings revisions positive. Weak.
- Data needed: Shiller P/E (in tool), S&P (in tool).
- Confidence: low.

### "Market feels toppy" (May 2025)
- Source: Steve Cohen — Sohn 2025 (quote: "Right now the market feels toppy")
- Type: conflict/caveat (view)
- Rule as testable logic: View only (S&P rose ~15% after) — record for scoring.
- Data needed: n/a.
- Confidence: low.

### Drawdowns are normal; stick to process
- Source: Steve Cohen — Sohn 2025 (quote: "if your process is consistent and you believe in your process, um you can always have self-doubt")
- Type: position sizing/risk
- Rule as testable logic: Don't change rules after short-term losses; evaluate the tool only on pre-registered walk-forward record (already tool policy).
- Data needed: n/a.
- Confidence: high.

---

## Batch summary

Total rules extracted: 191 (File 1: 26, File 2: 11, File 3: 30, File 4: 32, File 5: 30, File 6: 12, File 7: 14, File 8: 27, File 9: 9).

Ten most important testable ideas in this batch:

1. **Druckenmiller's "inside the stock market" composite** (File 4): early cyclicals (autos, homebuilders, banks, retail, small caps) falling >= 15 pp more than the S&P while defensives hold up = amber recession warning. He says it called the last four recessions. Pair it with credit (HY OAS widening, credit-sensitive financials) and the 2s5s curve. Action: no equities, long 2y/5y/10y Treasuries. Can be tested back to 1926 with Ken French industries.
2. **Short-credit / long-Treasury pair in late cycle** (File 4): long IEF / short HYG with matched duration, used when the curve is flat and credit is warning, plus "HY yields too low for the risk". This is a new de-risking instrument beyond cash/TLT.
3. **Inflation decides which de-risk asset to hold** (Files 2, 5, 8, 9): stocks and bonds move together under a hawkish Fed plus an inflation shock. When core CPI > 3% or the Fed is hiking fast, de-risk into T-bills/gold/commodities/trend, not long Treasuries. When term premium and the 10y-3m gap are near zero, prefer T-bills over duration. The tool already uses stock-bond corr < 0; this adds a forward-looking switch based on the inflation regime.
4. **Country selection by policy and value** (Files 5, 8): overweight a country when there is (a) deregulation / better governance, (b) real policy rate >= 4% with a cheap currency (bottom-quintile REER), (c) market-friendly political change, and (d) a 10-month trend filter. Applies to Brazil, Mexico, Argentina, India and others. Value alone is not enough without a catalyst.
5. **Commodity-to-country links** (Files 5, 8): rising broad commodities (12m > +15%, above 10m MA) -> overweight exporters (EWZ, EWW, ECH, KSA, EWA, EWC); an oil spike (3m > +30%) -> underweight importers (India, Korea, Taiwan, Turkey). China PPI < 0 -> deflation is exported.
6. **Foreign government bonds vs Treasuries** (File 8): when US inflation is >= 3% and foreign inflation is below target and their currency/energy prices are weaker, prefer hedged non-US bonds (BNDX/BWX, gilts) and EM local bonds where real rates are high and inflation is falling. Avoid JGBs/USTs.
7. **Dollar short vs EUR/JPY** (File 8): record-negative NIIP, top-decile REER and narrowing 2y rate gaps -> long FXE/FXY, held with slow-moving currency trend (12m momentum, quarterly rebalance). Yen-carry unwind trigger: USDJPY down >= 7% in 1m -> cut risk (File 1).
8. **Rate cuts before a recession are sold** (File 1): a first cut with a recession flag on, or an emergency/50 bp cut, is NOT a buy signal. Stay underweight equities and long Treasuries for 6-12m. A first "insurance" cut with no recession flag is a buy.
9. **Trend / 200-day slope filter and contrarian CFTC positioning on every new asset** (Files 3, 8): require the 200-day (10-month) MA slope to be > 0 to hold any sector, country or commodity. Fade top/bottom-decile speculative net positioning in gold, crude, copper and silver.
10. **Fiscal impulse rules** (Files 1, 5, 8): deficit >= 5-6% of GDP outside recession = "two feet on the gas" (equities and real assets up, long bonds down). Scheduled fiscal tightening >= 0.5% of GDP is a headwind. Country fiscal expansion (Germany defence) -> long that country's equities, short its bonds. Effective tariff rate up >= 3-5 pp -> slower growth plus inflation.

Also notable: Gerstner's "units of risk" skew sizing (9 vs 3 units); the concentration rule (any industry > 15% of S&P, tech > 40% -> equal-weight or REIT hedge); "cap whole-portfolio beta, not just equity weight" (Graham), needed once EM/commodity/credit sleeves are added; and trendless high-VIX regimes -> halve position size (Druckenmiller).

Contradictions / caveats found:
- Gerstner (Middle East flare-ups are buying opportunities) vs. van Eck and Sohn (in a war or liquidation even gold and Treasuries get sold; gold did not rally in 2026). Treat Treasuries/gold as hedges only after the first month.
- Druckenmiller (Treasuries are the bear-market money-maker) vs. Calderini, Jones and Karniol-Tambour (bonds may fall with stocks in inflation regimes; Treasuries carry little risk premium).
- Citrone (US growth booms in 2026, 10y to 5%+) vs. Karniol-Tambour (slowdown plus inflation). Both agree US duration is unattractive.
- Druckenmiller's "0-5%/yr for 5 years" (Dec 2018) and Cohen's "toppy" (May 2025) were wrong ex post. They are forecasts, not rules.
- Sohn: flows are "a temperature barometer, not a signal". Van Eck: valuation is useful only at extremes and inside a trend. Both argue against stand-alone valuation/flow timing.
- Instrument caveats: leveraged/inverse ETFs decay with daily reset (Sohn, van Eck), so use T-bills or puts for shorts. Quality/momentum ETFs are not diversifiers (R² ≈ 1 to the S&P). Private credit and BDCs carry equity-like risk.

## Data requests

Series needed that are NOT in the existing tool list (free source, approximate start):

Equity: sectors, countries, factors
- Ken French 49 industry portfolios, value- and equal-weighted, with market caps (1926): autos, building, banks, insurance, retail, utilities, food, drugs, chips, oil, guns. Needed for the inside-the-market composite, sector-weight concentration and equal-weight sector indicators.
- Ken French factors: HML, UMD, size; portfolios sorted on beta and variance (1926/1963).
- Russell 2000 (^RUT 1987) / IWM (2000).
- Equal-weight S&P (RSP 2003; S&P EW index 1990); equal-weight consumer discretionary (RSPD 2006).
- Sector ETFs XLK, XLF, XLY, XLP, XLV, XLE, XLU, XLI, XLB, XHB, KBE, KIE, PSP, SOXX/SMH, IGV, XRT, ITA, VNQ (1998-2006); FTSE Nareit All Equity REITs (1972).
- Nasdaq-100 (^NDX 1985) / QQQ (1999); PHLX SOX (1994).
- MSCI country indexes, monthly in USD (developed 1970, EM 1988, msci.com), plus country ETFs: EWY, EWZ, EWJ, FXI/MCHI, INDA, EWT, EWW, ECH, EPU, ARGT, KSA, EWA, EWC, EWG, EWP, GREK, EIDO, VNM, TUR, EEM, EFA, VGK, EZU, ACWX.
- Nikkei 225 (FRED NIKKEI225 1949), DAX (^GDAXI 1987), Shanghai Composite (1997).
- Country CAPE / P/E (Research Affiliates / Star Capital snapshots; MSCI P/E).
- S&P 500 sales per share and forward EPS revisions (S&P xls 2001; revisions not free).

Rates, credit, FX
- 2y and 5y Treasury (FRED DGS2, DGS5, 1976); 3m bill (DTB3); fed funds target (DFEDTAR/DFEDTARU 1982).
- 10y TIPS real yield at the 0.5% neutral level (DFII10 2003; already in tool as real 10y); 10y breakeven (T10YIE 2003).
- HY OAS (BAMLH0A0HYM2 1996), HY effective yield (BAMLH0A0HYM2EY), HY total return (BAMLHYH0A0HYM2TRIV 1986), EM corporate OAS (BAMLEMCBPIOAS 1998); leveraged loans (BKLN 2011).
- Business-loan delinquency (FRED DRBLACBS 1987).
- Foreign 10y yields (FRED IRLTLT01xxM156N, 1950s-), Germany/Japan 2y (Bundesbank/MoF), BoJ policy rate; BIS central bank policy rates for EM (monthly, free).
- FX: USDJPY (DEXJPUS 1971), EURUSD (DEXUSEU 1999), CNY (DEXCHUS 1981), EM currencies (FRED/BIS); BIS real effective exchange rates (RBUSBIS 1994; Fed TWEXBPA 1973).
- US net international investment position (FRED IIPUSNETIQ 2006; BEA annual 1976).
- ETF instruments: FXY, FXE, UDN, BNDX, BWX, IGLT, EMLC, EMB, CBON, HYG, LQD, BIZD, SHY, IEI, IEF, TIP/SCHP; HYG/LQD discount to NAV (iShares 2007).

Commodities, volatility, hedges
- World Bank Pink Sheet monthly prices and indices (1960): broad commodity, energy, metals, agriculture, gold, silver, platinum, Brent, natural gas Europe (TTF), copper.
- WTI daily (DCOILWTICO 1986), Brent (DCOILBRENTEU 1987), uranium (FRED PURANUSDM 1980).
- ETFs: GLD (+ GLD tonnes held, 2004), SLV, DBC, USO, BNO, CPER, COPX, URA.
- CFTC Commitments of Traders, speculative net positions for gold, crude, copper, silver, grains (1986 legacy / 2006 disaggregated).
- CBOE strategy indexes: BXM (covered call, 1986), PUT/PPUT (put-write/protective put, 1986); VIX futures ETF VIXY (2011).
- Trend-following returns: AQR Time Series Momentum dataset (1985) or SG Trend index.
- Bitcoin (BTC-USD 2014; FRED CBBTCUSD).

Macro, fiscal, liquidity, sentiment, geopolitics
- Federal deficit % GDP (FRED FYFSGDA188S 1929; monthly MTSDS133FMS 1980); federal debt % GDP (GFDEGDQ188S 1966); federal interest outlays (A091RC1Q027SBEA 1947).
- IMF WEO / Fiscal Monitor deficits, structural balances and debt by country (1980); IMF Global Debt Database.
- Effective US tariff rate = customs duties (B235RC1Q027SBEA 1947) / goods imports (IMPGS).
- Nonfinancial corporate debt (BCNSDODNS 1945) vs corporate profits (CP 1947).
- ECB total assets (ECBASSETSW 1999), BoJ total assets (JPNASSETS 1998), for global QT.
- Money-market fund assets (MMMFFAQ027S 1974 / WRMFNS 1980).
- JOLTS openings (JTSJOL 2000).
- Real PCE detail for furnishings, air travel and accommodation (BEA NIPA 2.4.6U, 1959).
- Labor force (CLF16OV 1948), nonfarm productivity (OPHNFB 1947).
- OECD Composite Leading Indicators by country incl. US and China (FRED, 1955-); OECD GDP by country.
- China PPI (FRED CHNPIEATI01GYM 1996), China house prices (BIS QCNN628BIS 2005), China exports by destination (IMF DOTS).
- NY Fed Global Supply Chain Pressure Index (1997); core goods CPI (CUSR0000SACL1E 1957).
- CPB World Trade Monitor (2000).
- Caldara-Iacoviello Geopolitical Risk Index (1985 / historical 1900); Baker-Bloom-Davis Economic Policy Uncertainty (USEPUINDXM 1985) and Trade Policy Uncertainty (1985/1960).
- AAII sentiment survey (1987); ICI fund and ETF flows (2007); Citi Economic Surprise Index (not free).
- Governance/reform: Fraser Economic Freedom (1970/2000), Heritage Index (1995), World Bank Worldwide Governance Indicators (1996).
- Demographics: World Bank population aged 15-64 (SP.POP.1564.TO, 1960) / UN WPP (1950).
- Housing credit: MBA Mortgage Credit Availability Index (2004), FHFA LTV (1973), SLOOS mortgage standards (SUBLPDHMSNQ 2007).
- Euro area sentiment: ZEW (1991), EC Economic Sentiment Indicator (1985).
- Leveraged-ETF AUM and usage; sector ETF flows (issuer/ETF.com; mostly not free).
- Event lists: US presidential elections, government shutdowns, EM national elections, BoJ/Fed emergency or 50 bp moves.
