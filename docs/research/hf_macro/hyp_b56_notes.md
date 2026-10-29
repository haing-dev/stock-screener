# hyp_b56: transcript rules from batches 5 and 6 as hypotheses

Code: `hyp_b56.py` (192 hypotheses, C001 to C192). Run: `python3 harness.py hyp_b56`. The table is in `out_b56.txt`. No hypothesis errors.

## 1. Counts

| | Batch 5 | Batch 6 | Total |
|---|---|---|---|
| Rule blocks read | 116 | 143 | **259** |
| Rules coded (at least one hypothesis) | 72 | 77 | **149** |
| Rules skipped | 44 | 66 | **110** |
| Hypotheses | C001-C102 | C103-C192 | **192** |

Some rules have more than one hypothesis. This happens when a rule names several actions (for example "stocks 50%", "10% commodities" and "short long Treasuries"), or when I added one alternative threshold.

Merged duplicates:
- b5 #96 and b6 #74 (count of policy-rate moves): C084 / C085.
- b5 #98 and b6 #75 (permanent trend sleeve): C087 / C088.
- b5 #100 and b6 #86 (trend + carry + value): C090.
- b6 #32 and #118 (expensive US real dollar): C123 / C124.
- b6 #42 and #91 (pro-cyclical deficit): C130 / C131.
- b6 #40 and #112 (VIX re-entry): C127 / C128.
- b6 #134 and #141 (miners vs gold): C187 / C188.
- b5 #4 and b6 #16 (tariff jump, TIPS vs nominals): C005 at 2 pts, C113 at 3 pts.
- b5 #32 and #33 (inflationary short, covered when growth weakens): C036 / C037.
- b6 #10 is covered by C104 / C116. Its daily "add on big down days" part cannot be tested.

### Never true since 1975 (no effect, kept as coded)
- **C024** (post-bubble 15% rally): the 2022 rally reached 14%.
- **C026 / C027** (all three leading industries 40%+ off their highs at once).
- **C038** (dollar near its high while the ECB out-hikes the Fed).
- **C048** (dollar down 15% in 6 months with an oil or CPI shock).
- **C077** (Japan CPI ends 2021-06; the BoJ rate was never <= 0 while CPI was > 2%).
- **C096**: on only in 1973-74.
- **C109 / C110** (the "sell America" month never had all three legs together at month-end).
- **C111**: customs duties / imports of goods *and services* never reach 10%. See the data list.
- **C117** (no tariff walk-back of 5 points).

### Coding conventions
- **Exposure cuts:**
  - "Cut / exit / sell" is level 0.0. "Reduce / underweight" is level 0.5.
  - Gerstner's "bottom third" (C104) is coded at 0.5, as are the "25%" reductions in C028 and C099. The lab uses 0.0 or 0.5.
- **"Underweight long Treasuries"** is a return bet: an overlay that shorts 20% of `t30y` against T-bills.
- **"Treasuries are not the hedge"** is a hedge choice: an overlay that removes the base book's TLT holding. That holding is computed exactly for the c5 book.
- **Pair overlays** only switch on in months where every leg has data. A sleeve only switches on once its asset has data, so before inception the sleeve share is not left in cash.
- **Signal horizons:** a stated horizon is applied with `hold(n)`. With no stated horizon, the signal applies while it is true. Re-entry blocks with no horizon are held 3 months, which is my choice.
- **Assets added to `R` (in memory only):**
  - Baskets: `x56_real` (gold, commodities, TIPS), `x56_metals`, `x56_oilcu`, `x56_goldmin`, `x56_emproxy`.
  - Dynamic baskets: `x56_deval`, `x56_cheapfx`, `x56_strong`, `x56_secular`, `x56_turn`. They select at month t and earn in month t+1.
- **Publication lags:**

| Data | Lag |
|---|---|
| FRED monthly macro | +1 month |
| OECD CLI, Japan CPI | +2 months |
| GDP | +4 months from quarter start |
| NIPA fiscal detail | +5 months from quarter start |
| Treasury Bulletin ownership (FDHBFIN, FDHBFRBN) | +6 months from quarter start |
| BIS house prices | +6 months from quarter start |
| Annual fiscal-year deficit | +10 months |
| Shiller EPS | +6 months |

### Proxies used in the code (related data, flagged in each `desc`)
- **Core inflation:** headline CPI before 1998 for core CPI; headline PCE before 2001 for core PCE.
- **Real 10y before 1998:** 10y minus lagged headline CPI.
- **Fed balance sheet before 2002:** monetary base.
- **Rig count:** industrial production of oil and gas drilling (IPN213111N, 1972-).
- **Macro surprise:** Philly Fed current activity, positive and rising (C029).
- **Trade-policy uncertainty:** economic policy uncertainty, EPU (C067).
- **ACM term premium:** Kim-Wright (THREEFYTP10, 1990-) (C160, C161).
- **German 2y:** German 10y (C157).
- **Forward P/E:** Shiller trailing P/E (C154). The TINA rule (C155, C156) also uses the trailing earnings yield.
- **Foreign official custody:** total foreign holdings, FDHBFIN (C055).
- **Policy-rate activity:** Fed + ECB only, because BoE is missing (C084, C085, C163).
- **Trade-weighted currencies:** BIS real broad indices (C046, C125).
- **Consumer discretionary:** retail (XRT).
- **Daily 60-day correlations:** monthly 12-month correlations (C148).
- **Weekly crash:** a monthly -10% fall (C152).
- **AI-capex split:** total GDP, without the AI split (C007). C018 is coded without hyperscaler free cash flow.
- **Short histories:** truck freight starts only in 2015 (C118, C170) and the household equity share in 2013 (C102, C147).

### Skipped rules and why

**Data not available.** Each is in the list in section 2.
- **Batch 5:**
  - #8, #54, #70: IMF fiscal, current-account and savings data.
  - #11: info-processing capex.
  - #12: BIZD.
  - #13: US share of ACWI.
  - #14: foreign holdings of US equities.
  - #15, #67: European deficits and P/E.
  - #20: FOMC dissents.
  - #21, #107: TIC flows and COFER.
  - #41: sector margins.
  - #55: polarization indices.
  - #56, #57, #103: geopolitical risk (GPR).
  - #59: CBO vintages.
  - #73: KWEB.
  - #82: TTF gas.
  - #94: UMich 5-10y expectations.
  - #116: hedged ex-US ETFs.
- **Batch 6:**
  - #3, #108, #122: GPR.
  - #6: GSCPI.
  - #11: EPS revisions.
  - #21: uranium.
  - #24: oil futures curve.
  - #44: central-bank gold buying.
  - #47: TTF gas and China imports.
  - #51: CRE prices.
  - #55: diesel.
  - #56: issuance and nonresidential investment.
  - #59, #60: bill share and refunding sizes.
  - #67: HY OAS history.
  - #71: China EV exports.
  - #96: FDIC unrealised losses.
  - #107: China credit impulse.
  - #110: country CAPE.
  - #119: TIC flows and current account.
  - #126: COT positioning.
  - #128: surprise index.
  - #133, #140: mining capex.
  - #142: silver price level for the gold/silver ratio.

**Event lists needed.**
- Batch 5: #72.
- Batch 6: #1, #2, #4, #7, #17, #33, #45, #49, #52, #61, #88, #89, #101, #138.

**Sizing, process or portfolio-design rules with no market condition, or not expressible in the harness.**
- **Batch 5:**
  - #28: re-weighting inside the warning count.
  - #38's 1.25x up-sizing: no leverage allowed.
  - #40, #44: principles.
  - #48: static risk parity.
  - #63: design check.
  - #86-#93: vol-unit sizing, stress tests, event sizing, liquidity filter, daily reversal, event-day execution, conviction scaling, VIX regime.
  - #104: trend lookback switch.
  - #105: design.
  - #112: stop-losses on tilts.
  - #113: composite threshold.
- **Batch 6:**
  - #26, #27, #34, #36, #37, #38, #85, #95, #113, #116, #127, #131: design or process.
  - #35: a Dec 15 to Jan 1 window cannot be shown in monthly data.
  - #39: covered as C126.
  - #106: the book holds no index shorts.
  - #125: daily entries.
  - #130: the book has no gain-based exits.

**Narrative or caveats with no standalone rule.** Several only modify a rule the tool already has.
- Batch 5: #43, #69, #75, #79 (applies to short positions; AAII missing).
- Batch 6: #8, #28, #31, #54, #68, #73, #80, #90, #93, #137, #139.

## 2. Data needed (missing series, best proxy, source, start)

| Series needed | Best proxy (with what we have, or a cheap substitute) | Source | Start |
|---|---|---|---|
| Geopolitical Risk index (global, China, Taiwan) | Defence stocks (ITA) vs S&P 3m + gold/S&P 1m jump + oil 1m spike | matteoiacoviello.com | 1900 annual / 1985 monthly |
| Trade Policy Uncertainty | EPU (have; USEPUINDXM); tariff-rate change | policyuncertainty.com | 1985 (Caldara TPU 1960) |
| HY OAS full history (FRED only serves 3 years) | Moody's Baa−Aaa (FRED DBAA/DAAA), Baa−10y (have), HYG−IEF 3m (2007) | ICE via Bloomberg; FRED BAMLH0A0HYM2 | 1996 (Baa 1919) |
| ACM term premium (level) | Kim-Wright THREEFYTP10 (have, 1990); 10y−2y minus a 5y average | NY Fed | 1961 |
| AAII bull-bear spread | VIX, S&P 6m return z-score, put/call ratio (CBOE 1995) | aaii.com | 1987 |
| TIC net foreign purchases of US long-term securities | FDHBFIN y/y (have); dollar vs rate gap | US Treasury TIC | 1977 |
| Foreign official custody holdings | FDHBFIN (have, quarterly) | FRED WMTSECL1 / H.4.1 | 2002 |
| Central-bank gold purchases | IMF IFS official gold tonnes; gold minus real-yield model residual | World Gold Council / IMF IFS | 2000 / 1950s |
| IMF COFER USD reserve share | Dollar REER (have) | IMF | 1995 |
| US NIIP | Cumulated current-account deficits (FRED NETFI / IEABC) | FRED IIPUSNETIQ / BEA | 2006 / 1976 |
| IMF WEO: country debt, primary balance, current account, savings | OECD Economic Outlook (annual); for EM, the FX reserve change | IMF WEO | 1980 |
| Country CAPE / valuation | Dividend yields from ETF distributions (Yahoo dividends, 1996), MSCI factsheets, Shiller-style CAPE from country index + local EPS | StarCapital, Research Affiliates | ~1980 |
| US share of world equity cap | SPY vs ACWI market cap ratio; cumulative spx vs ACWX return anchored to an MSCI factsheet | MSCI factsheets | 1970 |
| Rest-of-world holdings of US equities | Foreign holdings of Treasuries as an appetite proxy | Fed Z.1 BOGZ1LM263064105Q | 1945 |
| Info-processing equipment + software investment; private nonresidential investment | Tech-sector capex from 10-Ks of hyperscalers; semis vs S&P (have) | FRED Y033RC1Q027SBEA, B985RC1Q027SBEA, PNFI | 1947 |
| BoE Bank Rate | UK 10y (have, IRLTLT01GBM156N) as a weak stand-in | FRED BOERUKM / BoE IUDBEDR | 1694 |
| German 2y yield | German 10y (have); ECB deposit rate (have, 1999) | Bundesbank / ECB curve | 1972 / 2004 |
| Banxico policy rate (MXN carry) | Mexico 3m interbank (FRED IR3TIB01MXM156N) | BIS policy rates | 1990s / 2008 |
| Japan CPI after 2021-06; BoJ rate after 2023 | OECD CPALTT01JPM659N; BoJ website | e-Stat, BoJ | 1970 |
| Japan 2y yield | Japan 10y (have) | MoF Japan | 1974 |
| UMich 5-10y inflation expectations | T5YIFR 5y5y (have, 2003); UMich 1y (have) | UMich survey site | 1990 |
| European natural gas (TTF) | World Bank Pink Sheet "Natural gas, Europe" (monthly, free) | World Bank / ICE | 1960 / 2004 |
| Diesel, ULSD, jet fuel, crack spread | Gasoline (have) vs WTI; World Bank energy index | EIA, FRED GASDESW, DDFUELNYH, DJFUELUSGULF | 1986-1994 |
| WTI futures curve (front vs 12th) | XLE / WTI ratio (have) | EIA RCLC1-4 | 1983 |
| Baker Hughes rig count | IP oil and gas drilling (have; used) | Baker Hughes | 1987 |
| Petroleum product supplied (demand destruction) | Gasoline price vs vehicle miles (FRED TRFVOLUSM227NFWA) | EIA WRPUPUS2 | 1991 |
| EIA US petroleum net exports | Oil vs dollar correlation | EIA | 1973 |
| Silver spot price (gold/silver ratio) | World Bank silver price (monthly) or LBMA; anchoring the SLV level is not enough | World Bank Pink Sheet | 1960 |
| Mining capex, exploration budgets, copper mine supply | Miners' capex from 10-K (FCX, NEM, BHP ADRs); USGS annual output | S&P Global, ICSG, USGS | 1990s / 1900 |
| S&P forward EPS, revision ratio, forward P/E | Shiller trailing EPS (have; used); y/y change of trailing EPS | S&P Global EPS file, I/B/E/S | 1988 / 1976 |
| Macro surprise index | Philly Fed (have; used) + Korean exports (have) + first-release payrolls vs a 3m average (ALFRED) | Citi (paid) | 2003 |
| NY Fed GSCPI | Philly Fed delivery times (FRED DTDFSA066MSFRBPHI) | NY Fed | 1997 / 1968 |
| SLOOS CRE; CRE delinquency; CRE prices | SLOOS C&I (have; used); REITs vs S&P | FRED SUBLPDRCSC, DRCRELEXFACBS; BIS COMREPUSQ159N | 1990-1991 |
| FDIC unrealised securities losses | 10y yield change × bank duration estimate | FDIC QBP | 2008 |
| Treasury bill share of marketable debt, refunding sizes | Fed bill holdings share | Treasury MSPD | 1950s |
| Treasury and IG issuance | Change in GFDEBTN (have) | SIFMA | 1996 |
| HLW r* | Real 10y (have) | NY Fed | 1961 |
| China credit impulse (TSF) / M1 | Korean exports (have, XTEXVA01KRM667S), copper, China OECD CLI (have to 2024) | PBoC, FRED MYAGM1CNM189N | 2002 / 1996 |
| China imports | China exports (have) | FRED XTIMVA01CNM667S | 1992 |
| China EV exports | Lithium / battery ETF (LIT) | CAAM | 2010 |
| FOMC dissent counts | None (manual list) | Fed / Thornton-Wheelock | 1936 |
| CBO baseline vintages | Deficit (have) | CBO | 1990s |
| CFTC Commitments of Traders | None (free download) | CFTC | 1986 |
| Fed Distributional Financial Accounts | Household equity share (have, 2013) | Fed DFA | 1989 |
| SPF Anxious Index | Curve + OECD CLI | Philly Fed | 1968 |
| Missing instruments: XLY, XHB, SOXX, KWEB, MCHI, INDA (have India proxy), EWS, EWL, EWQ, KSA, UAE, ASEA, ARGT, VNM, EMXC, HEFA/DBEF, BIZD, REMX, URA, SH, PPUT | Ken French 49 industries (1926) for sectors; MSCI country index history (1970/1988) for countries | Yahoo, MSCI, Ken French | various |
| European defence spending | US FDEFX (have) | SIPRI | 1949 |
| Partisan conflict, WGI | None | Philly Fed (1981), World Bank (1996) | 1981 / 1996 |
| Event lists (sanctions, export bans, China stimulus, central-bank governors, debt-ceiling dates, wars, tariff announcements, transfer restarts) | None; hand-built CSV | news archives | n/a |

Note on C111: the rule needs customs / imports of **goods**. FRED BOPGSTB or NIPA goods imports (A253RC1Q027SBEA) would fix the denominator.

## 3. Results that look too good, and possible data artifacts

- **Trend and multi-style sleeves (C087, C088, C089, C090; also C084, C085, C163, C126, C175).** Only five hypotheses add more than 0.01 Sharpe in both halves for both books: C087, C088, C089, C161 and C021. Of these, C087-C089 are the largest. C090 helps mainly in 1975-2000.
  - The AQR TSMOM and AQR Century-premia series are hypothetical backtests. They were built after publication, with a futures universe chosen with hindsight. C087's out-of-sample gain after 2012 (S2 +0.07) is about half its 1985-2000 gain.
  - The harness charges 1.5%/yr on `trend` but no fee on `aqr_all_macro_multi_style`, so C090 is gross of costs.
  - C089 (trend off when EPU is above its 95th percentile) beats the always-on version in 2001-2026 (+0.116 vs +0.075). Its "off" months are about 60, clustered in 2008-12, 2020-21 and 2025-26: few independent episodes.
  - C089 also misses 1985-89, because the EPU percentile needs 60 months of history. Treat the gate as weakly supported.
  - C088 (own 6-asset trend) is the more honest estimate: about +0.07 and +0.03.
- **Term-premium rules (C160, C161).** The Kim-Wright term premium is re-estimated on the full sample. Its history is not what was known in real time, so C161's +0.02/+0.04 carries look-ahead in the signal itself.
- **One-episode wins (C130, C131, C185, C021, C036, C037, C153, C010).** Most of their gain is the 2022 bond crash. C130 is only on from 2021-10. C185 is on 2.6% of months, all in 2022.
- **C103 (long India+Mexico, short China).** CAGR is +0.6 but the worst drawdown is 5.6 points worse.
  - The "tariff rate rising y/y" signal is noisy quarterly data. With the 24-month hold it is on 88% of months, so this is effectively a permanent pair.
  - India and Mexico before their ETFs are local index prices in USD plus a flat 2%/yr dividend: a proxy with no costs.
- **C125 and C046 (cheap-currency and devaluation country baskets).** Pre-ETF country returns are index proxies. BIS real effective rates are revised. The baskets hold 1-3 countries, so the CAGR gain (+0.47, +0.37) rests on a few names. C046 loses in 1975-2000 (Sharpe -0.07).
- **C069 (gasoline spike: long staples, short retail).** The gain is in 2012-2026 only (S2 +0.08) and comes from 2-3 gasoline spikes. Before 2006 the retail series is the tool's spliced sector proxy.
- **C063 (EDV-type instead of TLT).** Before 2007 ultra-long returns are synthetic, from the 30y yield at duration 22 with no convexity or roll. The +0.3 CAGR mainly reflects more duration in the 2008 and 2020 cuts.
- **All short-Treasury overlays.**
  - Before 2002, `t30y` is synthetic from yields with no borrowing or financing cost for the short.
  - Synthetic bond returns ignore convexity. Short-bond gains in the 1970s may be overstated.
- **Fiscal, GDP and tariff rules.** These include C005, C006, C013, C014, C051-C053, C059, C068, C083, C086, C130, C131, C134, C164, C182, C186 and C191.
  - The series are final revised vintages. The publication lag is applied, but the first-release values are not used.
  - The deficit before 1980 is the annual fiscal-year figure, so it changes once a year.
- **C016 (real 10y > 1.5% gives 20% 10y Treasuries).** On 60% of months; the CAGR is -0.7. The gain is a volatility reduction rather than an edge. Before 1998 the real yield is 10y minus lagged headline CPI.
- **Large losers are informative, not artifacts.**
  - C070 ("Fed put" no-cut) blocks the 2008 cuts: core CPI was 2.3% then.
  - C098 (cuts only when the trend agrees) removes most protective cuts.
  - C172 (hold strong industries in cuts): the momentum industries crash with the market.
