# hyp_b12: transcript rules from batch 1 and batch 2, coded as hypotheses

Files: `hyp_b12.py` (249 hypotheses, ids A001-A249), `out_b12.txt` (harness table, no errors).
A private copy of the full results is in the scratchpad (`b12_results.csv`). `harness_results.csv` in this folder is shared: other batches (b34, b56, b7) were running at the same time and overwrite it.

## 1. Counts

| | Batch 1 (9 files) | Batch 2 (9 files) | Total |
|---|---|---|---|
| Rules read | 152 | 191 | **343** |
| Rules coded | 100 | 101 | **201**, in **249** hypotheses |
| Merged into another hypothesis (duplicates) | 7 | 8 | **15** |
| Skipped | 45 | 82 | **127** |

Hypotheses by kind: cut 75, overlay 41, sleeve 40, block 36, location 32, defensive 15, gate 10.

**Where some rules have two hypotheses:** this happens when the speaker's threshold had one alternative (A001/A002, A021/A022, A035/A036, A190/A191 ...), or when the rule names two actions (cut + location, sleeve gold + sleeve commodities).

**Merged duplicates (15).** These rules repeat another rule and share its hypothesis:
- Bass "US best place" -> A013.
- Hirsch "Aronson out-of-sample" -> A035, judged in the S1/S2 windows.
- Druckenmiller 2023 "bear rallies" -> A170.
- Pompeo "China reciprocity" -> A237.
- Calderini "macro returns in drawdowns", "macro is not a put" and "60/40+20% macro" -> A097.
- Jones/Ella "bonds join equities" -> A088; "risk-mitigation sleeve" -> A097/A087.
- van Eck "monetary signal muted" -> A088.
- Brende "record debt" -> A080.
- Calderini (Global Alts) "signal families" -> A106; "trend convexity" and "positively convex" -> A097.
- Cohen "Fed won't cut" -> A088.

**Data beyond R/S.** The read-only raw store `/home/claude/stock-screener/cache/macro/raw/research` holds series that are not in R/S. I used them for conditions only, never as assets:
- GPR geopolitical risk index
- Trade-policy uncertainty
- AAII sentiment
- CFTC COT positioning
- NY Fed GSCPI
- Daily S&P from 1970 (Santa Claus rally, first five days, trifecta, MACD, RSI)
- BIZD, BKLN, PSP, SPHB, SPLV

Lags: GPR, trade-policy uncertainty, GSCPI and COT are shifted 1 month. AAII and daily prices use the month-end value.

**Partial implementations.** Each of these drops one leg of the rule or uses a proxy, and says so in its `desc`:
- A024: the bank-leverage leg is missing.
- A025: Japan debt/GDP is assumed above 200% for the whole period.
- A058: the months'-supply leg is missing.
- A060: the 5y yield is approximated as (2y+10y)/2.
- A023: the Fed balance sheet stands in for emergency facilities.
- A102, A135, A206: 10y yield gaps stand in for 2y gaps.
- A125: fiscal tightening is trailing, not scheduled.
- A133: a 50bp move is read from the monthly-average Fed funds rate.
- A155: XRT stands in for equal-weight discretionary.
- A156: price stands in for small-cap flows.
- A157: NDX/S&P relative strength stands in for tech share.
- A166: Baa spread stands in for HY OAS (plus BKLN).
- A172: central-bank balance sheets use constant FX.
- A199, A204, A205, A208: the labour-force, trade-intensity, NIIP and political legs are missing.
- Core CPI before 1998 is a spliced proxy: 0.7 × services-less-energy y/y + 0.3 × core goods y/y, lagged 1 month.

**Size conventions where the speaker gave none:**
- cut: 0.0 when the speaker says "cut", 0.5 for "reduce", "trim" or "underweight".
- Speaker-stated caps are kept: 0.3, 0.6, 0.65, 0.7, 0.8, 0.9.
- sleeve 10%; location 50% for a country, region, small caps or Nasdaq, 20% for a single sector; overlay ±10%.
- "Long Treasuries -> bills" rules are overlays that remove the t30y leg in months when both books hold it (g_l & curve_ok). In the live book a residual xs5 share and the g_l & ~curve_ok months stay as they are.
- A sleeve switches on only once its asset has data. Without this, sleeves left cash drag before 1985 for the trend sleeve.

**Never true (4):**
- A063: deflation bust (S&P 30%+ off a top-decile-CAPE peak with Baa +1 pt).
- A119: equal weight lags by 10% and chips 25%+ off their high.
- A141: card delinquencies up 1 pt in 12 months; not seen in the 2012+ data.
- A152: semis/staples in the top 5% with the semis trend turning down.

**On but no effect (10).** Each is switched on in some months but never changes the books:
- A029, A069, A211: they only remove long Treasuries, but they never coincide with months the book holds them.
- A094, A198, A136, A137, A167, A186: the base book is already cut in those months, or the hypothesis is on for only 1-2 months.
- A135: the yen data start in 2007, after the signal months.

### Skipped rules (127), by reason

Counts: missing data 49, asset not in R 4, no matching position 6, events 8, execution or intraday 3, trade-level stops 3, not a trading rule 54.

**Missing data (see section 2).**
- Batch 1:
  - Roche: the bond-ladder benchmark (needs the 1-10y curve) and home bias.
  - Bass: loose lending, bank-sovereign contagion, the asset prices/wages rule, China price/income and the China current account.
  - Druckenmiller 2023: copper inventories.
  - Banga: opaque sovereign debt.
  - Calderini: the hawkish-central-bank currency rank (needs G10 2y yields).
- Batch 2:
  - Gerstner: revenue beat rate, consumer deferral and sector P/E.
  - Sohn: sector >15%, tech 40%, healthcare share, sector and equity flows, MMF assets, GLD holdings, leveraged-ETF usage, look-through holdings and hedging tech with healthcare/discretionary/financials (needs XLY and correlations).
  - Druckenmiller 2018: HY effective yield.
  - van Eck: four forces, deregulation, country CAPE, the ICSG copper balance, bond-ETF NAV discounts, MBA credit availability, uranium and demographics.
  - Brende: CPB trade, Europe periphery GDP, ZEW, China exports by destination, TTF gas and young-EM demographics.
  - Global Alts: China PPI and country PMI dispersion.
  - Citrone/Karniol-Tambour: WGI, election polls, EM FX carry, hedged foreign bonds, local bond ranks, China bonds/CNY, G10 policy rates, Germany fiscal impulse and the multi-country optimiser.

**Needs an asset that is not in R** (options and puts, NOK, REMX):
- Bass: option barbell.
- Sohn: options with defined risk.
- Karniol-Tambour: shorts and puts in the partial-warning zone.
- Norway fiscal rule: the NOK link.

**No matching position in the base book** (the book holds no China, Europe, Japan, energy, BTC or crypto):
- Bass: avoid China, Europe fragile.
- Hirsch: bitcoin in midterm years.
- Gerstner: crowded Japan, crypto.
- Sohn: energy "sugar rush".

**One-off events without a usable event list, or not backtestable:**
- Bass: Taiwan, amphibious window, rare earths.
- Druckenmiller 2023: debt ceiling, Fed independence.
- Pompeo: Russia, Iran strike.
- Calderini: Taiwan.

**Execution or intraday:** Hirsch's October fund window, turn-of-month and intraday rules.

**Trade-level stops:** Hirsch, Calderini and Sohn.

**Not a trading rule** (a prior, an evaluation criterion, a method, a constraint or a view): 54 rules:
- Roche: real returns, costs.
- Bass: the 55% hit rate.
- Druckenmiller 2023: hard-landing definition, reserve-currency curse, energy bridge. The M2-gap rule is also skipped, because it would mean discounting one indicator inside the warning share, which the harness cannot do.
- Pompeo (inflation erodes property), Banga (4) and the Norway fiscal rule (2).
- Calderini: skewness, fundamentals non-linear, climate softs.
- Gerstner: positive-skew sizing (needs state-conditional forward distributions), growth matters more, capacity lead.
- Jones: beta cap, downside-beta ranking, risk parity.
- Sohn: equal-weight methodology, daily reset, thematic ETFs, quality/momentum.
- Druckenmiller 2018: 3-5y bear, disruptors, 8-9 month horizon, one-way bets, the 2007 narrative, shutdowns.
- van Eck: 40-year bias, 65/10/25, rebalancing, exposure labels, gold/BTC family, EM bloc, thematic cap, leveraged ETFs, sovereign disconnects, pegs.
- Brende: soft-landing view.
- Global Alts: horizons, Sharpe benchmarks, over-diversification, event-risk caps, ML, cash+3-5.
- Citrone/Karniol-Tambour: pressure z-score sizing, private credit.
- Cohen: "toppy", process.

## 2. Data needed (missing series, best proxy, source, start)

| Needed for | Missing series | Best proxy / idea | Source, start |
|---|---|---|---|
| Ladder, 2s5s amber, bank duration mismatch (A060 uses a proxy) | 1y, 5y, 7y Treasury yields | FRED DGS1, DGS5, DGS7; build constant-maturity total returns from yields | FRED, 1953/1962/1969 |
| Druckenmiller credit leads, "HY yields too low" | ICE HY OAS and effective yield, full history (store has 2023+ only) | Gilchrist-Zakrajsek excess bond premium (Fed, 1973); Moody's Baa-Aaa; HYG/JNK 30-day SEC yield | Fed/FRED, 1973 / 1919 / 2007 |
| Bass bank leverage x house prices | Broker-dealer and bank assets/equity | Z.1 broker-dealer assets/equity (BOGZ1FL664090005Q family); FDIC EQTA; or KBE/KIE price-to-book from ETF factsheets | FRED Z.1, 1952 / FDIC, 1984 |
| Bass loose lending, van Eck low down-payment | SLOOS mortgage standards; price/income; MBA credit availability; FHFA LTV | SUBLPDHMSNQ (2007), spliced with DRTSLM (1990); Case-Shiller / median household income (MEHOINUSA672N); FHFA MIRS LTV | FRED, 1990 / 1984 / 1973 |
| Druckenmiller housing re-entry (A058 partial) | Months' supply of new homes | FRED MSACSR | FRED, 1963 |
| Bass asset prices vs wages | Real hourly earnings | AHETPI deflated by CPI; LES1252881600Q | FRED, 1964/1979 |
| Roche home bias, van Eck cheap international, Citrone country value | Country weights in world cap, country CAPE | World Bank CM.MKT.LCAP.CD; country CAPE (Research Affiliates, StarCapital); country dividend yield from iShares ETF distributions (Y_EW* are already in the raw store) | World Bank, 1975; ETF distributions, 1996 |
| Bass contagion | Bank assets/GDP by country; peripheral sovereigns and equities | World Bank GFDD; FRED IRLTLT01ITM156N / ESM / IEM; EWI/EWP from the raw store (Y_EWI, Y_EWP) | World Bank, 1960; OECD, 1991 |
| Bass short yen (A025 assumption) | Japan government debt/GDP | IMF WEO GGXWDG / FRED GGGDTAJPA188N | IMF, 1980 |
| Bass China current account | China current account | SAFE/IMF BOP quarterly; proxy: China exports (XTEXVA01CNM667S, in S) minus imports, or CNY 12m change | IMF, 1998 |
| Calderini, Gerstner, Karniol-Tambour currency rules (10y proxies used) | German and Japanese 2y yields, G10 2y yields | Bundesbank BBK01.WT3211 (1972), MoF JGB 2y (1974), BoE; or AQR currency-carry factor (in R) as a carry proxy | National central banks, 1970s |
| Karniol-Tambour NIIP (A205 partial) | US net international investment position | FRED IIPUSNETIQ (quarterly); BEA annual | FRED 2006 / BEA 1976 |
| Brende tariffs + labour (A199 partial) | Labour force | FRED CLF16OV | FRED, 1948 |
| Citrone EM carry, EM hikes beyond Brazil | EM policy rates, EM FX (TRY, NGN, MXN carry) | BIS central-bank policy rates; FRED DEX* / em_fx basket (in R from 2009) | BIS, 1990s |
| Karniol-Tambour foreign bonds | Hedged non-US government bonds | Y_BWX/Y_BNDX are in the raw store but not in R; longer history: AQR fixed-income market factor (aqr_fixed_income_market, 1960) as a global bond-futures proxy | 2007/2013; 1960 |
| Option-hedge rules (Bass barbell, Sohn options, Karniol-Tambour puts) | A put-protection or covered-call asset in R | CBOE PPUT/PUT/BXM are in the raw store as CSV; add R["pput"], R["bxm"] | Cboe, 1986 |
| Roche, Druckenmiller 2018, Gerstner: value/growth before 2000 | Value/growth returns | Ken French HML in the raw store (french_5f.zip): build value = market + 0.5·HML | Ken French, 1963 |
| Sohn sector concentration, tech 40%, healthcare share | Sector or industry market-cap shares | Ken French 49 industries with market caps (not in the store; free); proxy: relative cumulative returns times starting weights | Ken French, 1926 |
| Sohn high beta vs low vol before 2011 (A233 is short) | Beta-sorted portfolios | Ken French portfolios formed on beta/variance | Ken French, 1963 |
| Sohn flows, GLD outflows, small-cap outflows, leveraged-ETF usage | ETF/fund flows, GLD tonnes, leveraged-ETF AUM | ICI monthly flows (2007); SPDR GLD holdings history (2004); shares outstanding × price of TQQQ/SOXL/SPXL; proxy for flows: issuer shares-outstanding changes | ICI, 2007; issuers |
| Sohn money-market funds | MMF assets | FRED MMMFFAQ027S (quarterly), WRMFNS | FRED, 1974/1980 |
| Gerstner revenue beat rate / EPS revisions | Beat rate, revisions | S&P sales per share (spglobal xls, 2001); proxy: 3m change of Shiller EPS (used); Philly Fed ASPP profits forecasts (1968) as an expectations proxy | S&P, 2001; Philly Fed, 1968 |
| Gerstner consumer deferral | Real PCE: furnishings, air travel, accommodation | BEA NIPA table 2.4.6U; proxy: XRT and airline stocks vs S&P | BEA, 1959 |
| van Eck deregulation, Citrone governance | Country reform scores | Fraser Economic Freedom (1970, 5-yearly then annual), Heritage (1995), WGI (1996) | free, 1970/1995/1996 |
| van Eck, Brende demographics | Working-age population by country | World Bank SP.POP.1564.TO; UN WPP | World Bank, 1960 |
| van Eck copper supply | Copper market balance | ICSG monthly balance (press releases); proxy: LME stocks / HG futures curve spread (front vs 3rd); COMEX inventories | ICSG, 1990s; CME |
| van Eck nuclear | Uranium price | FRED PURANUSDM (IMF) | FRED, 1980 |
| Brende TTF gas | European gas price | World Bank pink sheet "Natural gas, Europe" (wb_pinksheet_monthly.xlsx is in the raw store; add to S) | World Bank, 1960 |
| Brende trade intensity | World trade volume vs world IP | CPB World Trade Monitor; proxy: Korea + Germany + Japan + China exports (XTEXVA01*, in S) vs INDPRO | CPB, 2000; OECD, 1957 |
| Brende Europe sentiment | ZEW, EC ESI | OECD euro-area CLI or business confidence (BSCICP03EZM665S) | ZEW 1991; EC 1985 |
| Rosner China deflation | China PPI | FRED CHNPIEATI01GYM; proxy: China CPI y/y (CPALTT01CNM659N, in S) or US import prices from China (CHNTOT) | FRED, 1996 |
| Global Alts dispersion, Citrone country growth | Country PMIs / CLIs for G10 + China | OECD CLIs by country (FRED *LOLITONOSTSAM; store has US, China, Korea, Brazil only, to 2024) | OECD, 1955 |
| Banga opaque debt | Creditor composition, EMBI spreads | World Bank IDS; AidData; proxy: EMB price drawdown (em_debt in R, 2008) | World Bank, 1970 |
| Goolsbee small-business leg (A141) | Business-loan delinquency | FRED DRBLACBS | FRED, 1987 |
| Bass Taiwan, rare earths, debt ceiling, shutdowns, Fed emergency moves, EM elections | Event lists | Hand-built date lists; Taiwan ADIZ counts (PLATracker, 2020); FRED DFEDTAR/DFEDTARU for intermeeting moves (1982); REMX (2010) | manual |
| Hirsch turn-of-month, intraday | Intraday / daily-execution returns | Daily S&P is in the raw store (D__GSPC); intraday SPY needs a paid feed | 1970 / paid |
| Druckenmiller M2 gap, Calderini "inflation warnings only above 2.5%" | Per-indicator access inside the warning share | Not a data gap: the harness would need a "drop indicator X" kind | n/a |

## 3. Results that look too good, and why they may be data artifacts

- **A097: 20% trend-following always** (Sharpe +0.08 to +0.15 in every window and both books). Related: A148 and A089 (trend when CPI or core CPI is above 3%).
  - `R["trend"]` is the AQR TSMOM factor plus T-bills: 15.4%/yr total return from 1985.
  - It is a gross paper factor, scaled to constant volatility. The harness charges 1.5%/yr plus 0.10% per rebalance, but not the factor's own futures turnover.
  - Live CTA indexes (SG Trend, BTOP50) earned roughly half this after 2009. Expect the real gain to be well below the table.
  - The series ends in 2026-05, so the last months are bills.
  - Note that A114 (trend as the de-risk asset) loses. The gain comes from the permanent diversifier, not from timing.
- **A106: 20% AQR multi-style macro.** Sharpe goes up while CAGR goes down (-1.8 pts). This is also a gross academic factor, with value and carry definitions published after much of the sample.
- **A041: utilities Mar-Oct** (+0.05 to +0.08 in all four book/half cells).
  - It is on 67% of months, so it is mostly a permanent 25% utilities tilt that lowers volatility.
  - Sector returns before XLU (1998) are a spliced proxy series.
  - Hirsch found the seasonal pattern on this same history, so it is in-sample.
- **A033: midterm weak spot, 50% cap.** This is the same calendar rule as the E4 layer already tried in `exp_combo.py` on the same data, so it is not a fresh test. c5 S2 (2012+) is negative.
- **A208: Brazil real rate plus cheap REER** (+1.3 to +1.8 pts CAGR in the full period).
  - Most of it is one episode, the 2003-07 commodity/EM boom (12% of months).
  - Brazil CPI is the OECD MEI latest vintage and stops in 2025-04. BIS REERs are revised.
- **A193: 5% bitcoin for 12 months after halvings** (+0.04 to +0.08 Sharpe after 2012). Only three post-halving windows have BTC data, and they contain returns of several hundred percent. Sample of three.
- **A022, A023: bank credit falling / Fed-liquidity re-entry.** The whole effect is 2009-11.
  - TOTBKCR is the latest vintage and includes the 2010 FAS 166/167 consolidation break.
  - A023's trigger (bank stocks -20% plus a jump in the Fed balance sheet) was written with 2008 in mind.
- **A242: no long Treasuries in a GPR-spike month** (+0.03 to +0.04 Sharpe after 2001). About 4% of months, a handful of events (2001-09, 2003-03, 2022-02). A small sample that looks like an effect.
- **General revision caveat.** P["F"] and P["ind"] are point in time. Everything I lagged myself from S is the latest vintage, so revisions leak some information despite the publication lags:
  - GDP and the deficit/GDP denominator, profits, corporate debt, Case-Shiller, bank credit
  - OECD CLI and country series
  - Shiller EPS (lagged 6 months because Shiller interpolates quarterly earnings)
- **Big losers that are not artifacts:** A200 productivity block, A221 retest buy-zone, A228/A035 Best Six Months, A058, A109, A126 (Sahm cut). They lose because they suspend or add cuts at the wrong time, which is a real finding.
