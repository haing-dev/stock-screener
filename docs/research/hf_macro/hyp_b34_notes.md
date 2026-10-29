# Hypotheses from transcript batches 3 and 4 (hyp_b34.py)

Code: `hyp_b34.py` (163 hypotheses, B001-B163). Run: `python3 harness.py hyp_b34 > out_b34.txt`. No errors.

## 1. Counts

| | batch 3 | batch 4 | total |
|---|---|---|---|
| rule blocks read | 142 | 148 | **290** |
| rule blocks coded (own hypothesis or merged into one) | 74 | 74 | **148** |
| hypotheses (incl. alternatives / second branches) | 86 (B001-B086) | 77 (B087-B163) | **163** |
| rule blocks skipped | 68 | 74 | **142** |

Skipped, by reason:

| reason | count |
|---|---|
| data not available (list in section 2) | 72 |
| caveat, benchmark, forecast or meta-test, not a trading rule | 35 |
| needs event dates (elections, tariff announcements, SPR releases, antitrust, IMF programmes, export controls) | 21 |
| position sizing / execution constraint, not a signal | 13 |
| not expressible with the harness kinds (Oppenheimer "limit de-risking to 50%" needs a floor on the cut) | 1 |

Merged duplicates: "Fed hikes slow the dollar's fall" into B007; Nations' disposition effect and Bessent's "big trend" into B044 (trend sleeve); Bessent's "trend confirms" into B040; Bessent's gold-despite-real-rates as the alternative B019 to Gromen's B018; Bessent's "interest > defence" as the alternative B036 to Rogoff's B035; Citrone's headline caveat as the alternative B096 to B095; Oppenheimer's scale-in at -30% into B041; Lagarde's "Europe most exposed" into B123; Eisman's relative rate level (Weekly Wrap) into B118; Eisman's Brent spike as the alternative B150 to Lagarde's B149.

Never true in the sample (fine, but uninformative): B023 (tariff +5 pts with Fed cutting and core > 3%), B073 (household net worth -15% y/y; 2009 reached about -13%), B087 (customs > 1.5% of GDP), B115 (foreign holdings falling while JGB yields rise), B134 (Oppenheimer structural-bear setup, all four legs). B046 (oil 50% above its 12m average for 3 months) fires only in 1974, before the test windows.

Partly coded (one leg missing or replaced by a stated proxy): B011 (ISM replaced by Philly Fed), B020 (WGC buying leg dropped), B026 (China CLI replaced by Korean exports: the OECD CLI is revised with a two-sided filter, so it is not point in time), B027 (no China 10y), B028 (Fed-independence leg not measurable), B031 (no stablecoin data), B032 (no tech share of the S&P), B037 (the speaker's static list of low-debt countries; global recession = ex-US stocks below their 10m average plus Korean exports y/y < 0), B038 (no EM external debt), B042 (no country CAPE), B043 (no rent index), B044 (no CFTC positioning), B052 (no BoE rate), B055 (CAPE top 5% in place of forward P/E > 22), B062/B063 (euro leg skipped, no EURUSD level), B065 (bitcoin leg left out), B089 (fiscal impulse = realised deficit change while unemployment is not rising), B100 (FX only, no CDS), B106 (no Japan CPI after 2021), B126 (narrow-leadership score in place of top-10 weight), B128 (Baa spread in place of BB OAS), B131 (iron ore only, no China PMI), B142 (energy and materials only, no quality factor), B144 (10y differentials in place of 2y), B161 (semis crash only, no capex share).

Series built for these hypotheses (only in `hyp_b34.py`; no existing file changed):
- **Core CPI before 1997**: the tool's CPILFESL starts in 1997. Earlier values are rebuilt from core goods (CUSR0000SACL1E) and services less energy (CUSR0000SASLE), weighted by BLS relative importance (40% falling to 25%). Against the real series in 1998-2026: correlation 0.998, mean error 0.06 pt.
- **Nominal GDP before 1992**: GDPC1 x GDPDEF.
- **Deficit/GDP**: 12-month sum of the monthly Treasury statement from 1981, the annual fiscal-year ratio before that.
- **Credit gap**: household plus business debt / GDP minus its trailing 10-year mean, one-sided.
- **Dollar**: DXY, spliced by returns onto the Fed's trade-weighted index before 1985.

### Coded rule -> hypothesis map

Batch 3:
- Gromen: sovereign debt / negative real rates B001-B002; WWII repression B003; commodity impulse B004; Fed tightening + dollar B005-B007; yield vs dollar B008-B009; Druckenmiller rotation B010; recovery playbook B011; foreign official buying vs dollar B012-B013; QT B014; Fed share of issuance B015; deflationary fits B016-B017; gold with rising real rates B018 (+B019); central-bank gold B020; Weimar dips B021; flat curve while hiking B022.
- Rogoff: B023-B038.
- Nations: B039-B043.
- Bessent 2026: B044-B051.
- Tropin: B052-B067.
- Krugman: B068-B071.
- Yass: B072-B073.
- Karniol-Tambour: B074-B086.

Batch 4:
- Gerstner: B087-B091.
- Citrone: B092-B107.
- Bessent (Real Vision): B108-B115, plus B019 and B036.
- Eisman Ep 73: B116-B133.
- Oppenheimer: B134-B147, plus B041.
- Lagarde: B148-B154, plus B123.
- Georgieva: B155-B159.
- Eisman Weekly Wrap: B160-B163, plus B118 and B150.

### Skipped rules (reason)

Batch 3:
- **Gromen**
  - Data: China water/power (China PPI, power output), ISM hoarding (ISM indices), repo spikes (SOFR/IORB), foreign holdings of US equities (TIC).
  - Not a rule: RRP/SLR caveat (indicator-design test), CPI 7-10% forecast (forecast scoring).
  - Event: petrodollar break.
  - Sizing: bitcoin/gold leverage.
- **Rogoff**
  - Data: dollar footprint (COFER), China+1 (China FDI), India vs China (IMF WEO growth), supply-shock caveat (GSCPI), Europe rearm (NATO spending).
  - Not a rule: tariff caveat, partisan surveys, "don't trust China data" (a data choice, applied in B026).
  - Event: no Trump put.
- **Nations**
  - Data: capitulation flows (ICI), bubble markers (IPO returns, unprofitable share).
  - Not a rule: no autocorrelation, availability/time-out constraint, hindsight bias, 30-day wait (a 1-month execution-lag meta test), 7-8% benchmark.
  - Sizing: loss aversion.
  - Event: antitrust.
- **Bessent 2026**
  - Data: current-account catalyst trade (Japan current account plus regime event), Japan ROE, energy independence (EIA net imports), bill share (MSPD), private credit (BDC data), US vs Europe growth (euro area GDP).
  - Event: SPR release, post-war oil, LatAm elections.
  - Sizing: over your skis, chip stack (needs strategy P&L).
  - Not a rule: sanctions caveat.
- **Tropin**
  - Data: AI EPS revisions / ECI, listed private equity (PSP/LPX50), EM spreads (the panel's EM OAS starts in 2023).
  - Event: habituation to shocks, Fed-independence episodes.
  - Sizing: 1980s bond stress cap.
- **Vestager** (all 7)
  - Event: EU tech antitrust, banking union, export controls.
  - Data: defence consolidation, European gas, clean-tech capacity, Europe CAPE/PMI.
- **Krugman**
  - Event: tariffs on partners.
  - Data: EM local-currency debt share, post-crisis fiscal impulse (output gap), inequality, immigration (labour force), financialisation (nonbank credit, crypto market cap).
  - Not a rule: Fed vs fiscal weighting, AI jobs.
- **Yass**
  - Data: country market cap/GDP, US/Europe CAPE ratio.
  - Event: tax hikes.
  - Not a rule: wasteful spending, consumer surplus.
- **Karniol-Tambour**
  - Data: corporate tax rate, capex returns, Goldilocks (forward EPS), EM reserve accumulation (COFER).

Batch 4:
- **Gerstner**
  - Data: stablecoins, US-China tariff de-escalation (bilateral tariff rate).
  - Event: chip export controls.
- **Citrone**
  - Data: EM reserves crisis, Japan 1990s bubble (country CAPE), Turkey (CDS/reserves), China CNH (China EPU, China 2y), EM ex-China, deglobalisation (GPR, world trade), DAX vs gas, Italy spread.
  - Event: regime change, Argentina election.
  - Sizing: asymmetric shorts, short sizing, net exposure, position cap.
  - Not a rule: exit fully, Africa, travel, 2022 bottom call, replace ideas.
- **Bessent (Real Vision)**
  - Sizing: asymmetry.
  - Event: peg breaks.
  - Data: CFTC positioning, central-bank/retail gold, bill share, Japan governance, BoJ hikes (BoJ rate in the panel ends 2023, no yen spot), USDJPY 160, China FDI, China export prices, China yields, card bifurcation (no discretionary/luxury series).
  - Not a rule: currency valuation, populism, gold vs S&P.
- **Eisman Ep 73**
  - Data: China crude imports, hyperscaler issuance/FCF, Japan CPI after 2021 / country CAPE, Japanese banks, PE illiquidity.
  - Not a rule: OpenAI/Anthropic single point of failure, populism.
  - Sizing: leveraged pairs, failed-rally exit for sector holdings the book does not hold.
  - Event: deregulation.
- **Oppenheimer**
  - Not expressible: healthy balance sheets.
  - Not a rule: PPP.
  - Data: FTSE/GBP, domestic equities vs gas, Italy, deglobalisation capex (PNFIC1).
  - Event: UK fiscal clash.
- **Lagarde**
  - Sizing: oil volatility.
  - Not a rule: policy lags, AI-cuts caveat, stablecoins.
  - Data: euro reserve share, European defence, euro productivity.
- **Georgieva**
  - Event: currency board, Bulgaria convergence.
  - Data: announced vs collected tariffs, AI preparedness index, Nasdaq forward P/E.
  - Not a rule: climate.
- **Eisman Weekly Wrap**
  - Data: AI debt supply (SIFMA), ARKK.
  - Not a rule: Treasury jawboning, two-company chain, AI-beta sector cuts (needs a factor model on top of B162), Nvidia receivables, vendor financing.

## 2. Data needed (missing series, best proxy, source, start)

| needed for | missing series | best proxy (creative where needed) | likely source | start |
|---|---|---|---|---|
| Gromen ISM hoarding; Rogoff supply shock; Peter O. checklist | ISM supplier deliveries, prices paid, new orders; NY Fed GSCPI | Philly Fed delivery times (DTCDFSA066MSFRBPHI) and prices paid (PPCDFSA066MSFRBPHI), with Korean exports y/y for new orders; Empire State prices paid | FRED; NY Fed site (GSCPI) | 1968 (Philly), 1997 (GSCPI) |
| Gromen China power/PPI; Bessent China deflation export | China PPI, electricity output, export prices | OECD MEI China PPI (FRED PIEAMP01CNM661N); US import prices from China (BLS); Korean+Taiwanese exports to China; Australian coal price (World Bank pink sheet) | FRED / BLS / World Bank | 1996 / 2003 / 1960 |
| Gromen foreign equity flows; Bessent foreign Treasury demand (official) | TIC net purchases (equities, Treasuries, official) | Fed custody holdings for foreign officials (WMTSECL1); Z.1 rest-of-world equities (BOGZ1LM263064105Q); FDHBFIN (used, total foreign, quarterly) | Treasury TIC; FRED | 1977 / 2002 / 1945 |
| Gromen repo stress | SOFR, IORB/IOER, GC repo | TED spread (TEDRATE) or 3m financial CP minus T-bill (DCPF3M - DTB3) | FRED | 2018 / 1986 / 1997 |
| Fed balance-sheet rules before 2002 (B014-B017, B048, B086, B094, B112, B159) | Fed total assets pre-2002 | Monetary base BOGMBASE (in panel, but its Y2K spike and fall gives a fake "QT" in early 2000, so it was not spliced in); H.4.1 history on FRASER | FRED / FRASER | 1959 / 1914 |
| Bessent bills share | T-bills / marketable debt | Treasury MSPD; earlier Treasury Bulletin tables | Fiscal Data API | 1996 (1950s in bulletins) |
| Rogoff/Bessent interest burden at 3% (B035) | CBO net interest outlays | FRED FYOINT (annual) or MTS net interest line (monthly). The NIPA series used (A091) includes imputed pension interest and sits 1-1.5 pts higher, so B035 is on 78% of months | FRED / Treasury | 1940 / 1980 |
| Rogoff COFER; KT reserves; Lagarde euro share | IMF COFER shares and totals | Dollar share of official gold+FX reserves from IMF IFS; foreign official custody holdings (above) | IMF data portal | 1995 |
| Rogoff China+1; Bessent China FDI | China FDI | IMF BOP direct investment liabilities; SAFE BoP | IMF / SAFE | 1982 annual, 1998 quarterly |
| Rogoff India vs China; Peter O. 2y differentials | IMF WEO GDP growth; G10 2-year yields | OECD MEI industrial production by country; Bundesbank/MoF/BoE 2y yields | IMF / OECD / central banks | 1980 / 1960s |
| Rogoff low-debt countries; Citrone EM crises; Georgieva convergence | country government debt/GDP, external debt, FX reserves in months of imports | IMF Historical Public Debt Database; World Bank IDS; World Bank FI.RES.TOTL.MO | IMF / World Bank | 1800s / 1970 / 1960 |
| country valuation (Nations reversal B042, Citrone Japan bubble, Yass, Trennert, Vestager) | country CAPE | Dividend yields from iShares country ETF distributions (12m trailing); MSCI country dividend yields; World Bank market cap/GDP (CM.MKT.LCAP.GD.ZS) | iShares / MSCI / World Bank | 1996 / 1970 / 1975 |
| pre-ETF country returns | actual MSCI total returns | MSCI end-of-day net-return indices in place of the panel's local index + 2%/yr dividend splice | MSCI | 1970 (DM), 1988 (EM) |
| Nations capitulation | ICI equity fund flows | AAII bull-bear spread; VIX/VIX3M inversion (px_^VIX3M, in panel); CBOE put/call | ICI / AAII / CBOE | 1984 / 1987 / 1995 |
| Nations bubble markers | IPO first-day returns, unprofitable share | Jay Ritter monthly IPO stats; Ken French small-growth vs small-value | Ritter site / French library | 1960 / 1926 |
| Nations housing (B043) | rent index for price/rent | CPI rent of primary residence CUSR0000SEHA, OER CUSR0000SEHC | FRED | 1914 / 1983 |
| Rogoff tech booms; Trennert concentration (B032, B126) | tech share of S&P, top-10 weight | Nasdaq-100/S&P price ratio; RSP/SPY; CRSP top-decile share from French ME breakpoints | Yahoo / French library | 1985 / 2003 / 1926 |
| Rogoff crypto (B031) | stablecoin supply | USDT+USDC market cap | DefiLlama / CoinGecko | 2015-2018 |
| Bessent momentum, Bessent positioning | CFTC Commitments of Traders | none good; ETF share-count changes as a flow proxy | CFTC | 1986 |
| Bessent Abenomics; Japan rules | Japan current account, BoJ rate after 2023, USDJPY spot, Japan CPI after 2021 | FRED JPNB6BLTT02STSAQ, DEXJPUS; e-Stat CPI; BoJ site; JGB 10y (in panel) as the reflation gauge | FRED / e-Stat / BoJ | 1971-1996 |
| Bessent energy independence | US net petroleum imports | EIA API; or US crude production (FRED IPG211111CN) | EIA | 1973 |
| Bessent private credit; Tropin/Trennert PE illiquidity | BDC discounts, listed PE | BIZD, PSP prices; LPX50; H.8 loans to nondepository financials | Yahoo / LPX / FRED | 2013 / 2006 / 1993 / 2015 |
| Bessent US vs Europe; Lagarde productivity | euro area GDP and productivity | FRED CLVMNACSCAB1GQEA19; Eurostat productivity | FRED / Eurostat | 1995 |
| Tropin 5% bid euro leg; Tropin ECB cut | EURUSD spot, BoE Bank Rate | DEXUSEU (synthetic via DEXGEUS before 1999); BoE database | FRED / BoE | 1971 / 1694 |
| EM spreads (Tropin; Citrone EM lag) | EMBI / EM OAS full history (the panel's BAML EM OAS starts in 2023) | EMB vs IEF relative price; Baa-10y spread for the US | JPM (paid), ICE via Bloomberg; Yahoo | 1993 / 2008 |
| Vestager, Citrone DAX, Oppenheimer domestic Europe | European gas price (TTF) | FRED PNGASEUUSDM (IMF); World Bank pink sheet "Natural gas, Europe" | FRED / World Bank | 1985 / 1960 |
| Citrone and Oppenheimer Italy | Italy 10y | FRED IRLTLT01ITM156N | FRED | 1991 |
| Oppenheimer FTSE/GBP | GBPUSD, UK mid caps | DEXUSUK; EWUS (2014) or FTSE 250 | FRED / Yahoo | 1971 |
| Krugman inequality | top-1% wealth share | WFRBST01134 | FRED (DFA) | 1989 |
| Krugman immigration | labour force | CLF16OV | FRED | 1948 |
| Krugman post-crisis fiscal | output gap, structural balance | CBO potential GDP (GDPPOT) and the cyclically adjusted deficit | FRED / CBO | 1949 |
| KT corporate tax rate | taxes on corporate income / pretax profits | A054RC1Q027SBEA / A053RC1Q027SBEA | FRED | 1947 |
| KT capex returns; Oppenheimer deglobalisation capex | nonres investment, capital stock | PNFIC1, BEA fixed-asset tables | FRED / BEA | 1947 |
| KT Goldilocks; Tropin AI EPS; Georgieva Nasdaq P/E | forward EPS, revisions, Nasdaq P/E | S&P operating EPS estimates (S&P DJI xls); Shiller trailing EPS (used) | S&P DJI | 1988 |
| Citrone China CNH; Gerstner China tariffs | China EPU, China 2y/10y, US-China tariff rate | policyuncertainty.com; ChinaBond / Investing.com; PIIE tariff tracker | various | 1995 / 2002 / 2018 |
| Citrone deglobalisation; Lagarde fragmentation | GPR index, world trade volume | Caldara-Iacoviello GPR; CPB World Trade Monitor. The B148 proxy (US imports/GDP) is a recession detector, not fragmentation | Fed / CPB | 1900 / 1991 |
| Eisman oil oversupply | China crude imports | JODI oil database | JODI | 2002 |
| Eisman AI capex | info-processing + software investment contributions; SIFMA issuance; hyperscaler capex | FRED Y033RC1Q027SBEA, B985RC1Q027SBEA; SIFMA monthly issuance | FRED / SIFMA | 1947 / 1996 |
| Eisman ARKK; Oppenheimer quality | non-profitable tech basket; quality factor | French small-growth vs large-growth; French RMW (profitability) | French library | 1926 / 1963 |
| Trennert Japan banks | TOPIX banks | 1615.T ETF, 8306.T | Yahoo / JPX | 2008 |
| event rules (21) | event dates | hand-built tables: IEA collective actions, BIS export-control rules, PIIE tariff announcements, IMF MONA, election calendars, SLR exemption, YCC dates (used in B106) | various | - |
| revision bias (see section 3) | real-time vintages for GDP, profits, imports, Z.1, NROU, BIS house prices | ALFRED vintages | ALFRED | 1990s+ |

## 3. Results that look too good, or are likely artifacts

The table is the full-sample change vs the base books (Sharpe change in the 1975-2000 | 2001-2026 windows). Most hypotheses move Sharpe by less than 0.03. The few larger gains:

- **B101 (Citrone top-down: dollar and 10y both down over 12m -> half of equities in EM)**: +0.06 live and +0.045 c5 Sharpe in 2001-26, +1.1%/yr CAGR, but drawdown 2.7 pts worse. The gain is all in 1997-2011 (S1 +0.115, S2 -0.002), mostly the 2002-03 and 2007-08 EM boom. Country returns before each ETF launch are local indices + an assumed 2%/yr dividend, which flatters EM in the 1990s. It is effectively one regime.
- **B050 (Bessent: MOVE > 36m mean + 2 SD -> stocks to 0)**: on only 18 months. Half are 2007-08 and the rest 2020-02 and 2022. The 2001-26 gain (+0.084 live, S2 +0.125) comes from two or three crashes. It is too few events to separate skill from luck, and MOVE starts in 2002.
- **B148 (Lagarde: CAPE > 30 and imports/GDP below 3y ago -> stocks to 50%)**: +0.05 live / +0.034 c5 in 2001-26, drawdown 2.8 pts better. The gain sits almost entirely in cuts that happened to cover December 2018 and March 2020 (the signal was on 2019-12..2020-02). The "fragmentation" proxy is really a trade-recession detector, and NIPA imports are latest-vintage (revised) data. Treat it as luck plus revision bias.
- **B022 (Gromen: flat and flattening curve while hiking -> stocks 50%)** and **B020 (gold at a 12m high with the dollar falling -> 10% gold)**: modest gains in both halves (+0.02 to +0.07). They look plausible, not artifacts. B020's gold history before 1975 is a fixed price, but that is outside the windows.
- **B081 (Karniol-Tambour: CPI > 5% -> stocks 50%)** and **B135 (Oppenheimer cyclical setup)**: +0.07 in 1975-2000 for the live book, mostly the 1970s-80s inflation. They lose or are flat after 2000. This is regime-specific, not a timing edge.

Other artifact risks to keep in mind when reading the table:
- **Revised data used as if known at the time.**
  - Quarterly series from the panel's S block are latest vintage: profits (B074), real GDP (B141 stagflation), imports and customs (B148, B087), Z.1 debt and net worth (B072, B075, B134-B136 credit gap), BIS house prices (B043, B134) and CBO NROU (B110, B127).
  - Lags are applied, but revisions are not. This most likely flatters cuts that fire in recessions (B075, B141, B148).
- **Thresholds that do not match the speaker's variable.**
  - B035 (NIPA gross interest vs CBO net interest) is on 78% of months, so it is effectively "always gold vs long Treasuries".
  - B117 (10y > 4.5%) is on 58% of months: almost all of 1968-2008.
  - B062 (10y >= 5%) is on 52%.
  - These measure the level of rates in that era, not the speaker's idea.
- **Short-history assets.** Overlays on tips (2004), usd/jpy/eur (2006-07), em_fx (2009), em_local (2010), tail (2017) and value/eqw (2000/2003) are zero before their start. Their 1975-2000 columns are 0 by construction.
- **intl_eq** before 2001 is the AQR global equity-index futures series, which may include the US. That understates US-vs-ex-US differences in B084 and B065.
- **Monthly approximations of daily rules** (B058 liquidity panic, B091 and B150 oil spikes, B088 policy-shock rebound) lose the speakers' timing.
- **Series that end early**, so signals stop: China and Brazil CPI end 2025-04 (B027, B103), Shiller E/P ends 2024 (B118 E/P leg, B122), R['trend'] ends 2026-05.
