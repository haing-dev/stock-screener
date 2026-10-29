# Batch 7 hypotheses: notes

Code: `hyp_b7.py`. Results: `out_b7.txt` from `python3 harness.py hyp_b7`. 127 hypotheses, 0 errors.
Note: `harness_results.csv` is shared with other batches running in parallel and gets overwritten, so the
batch-7 table to use is `out_b7.txt`.

## 1. Counts

| | count |
|---|---|
| Batch 7 rule blocks read (`### ` headings, 9 files) | 159 |
| Galt (X) rules in `macro/registry.py` (14 indicators cited with X(): staples_disc, breakdowns, transports, homebuilders, vix, spx_trend, junk, banks, dollar_break, chips_break, dollar, mcap_gdp, hh_equity, cape; plus 4 sector playbooks citing X(): late, overheating, recovery, STRESS) | 18 |
| Batch 7 rules coded (after merging duplicates; some only partly, see below) | 93 |
| Batch 7 rules skipped | 66 |
| Hypotheses D001-D106 (batch 7: speaker threshold plus at most one alternative) | 106 |
| Hypotheses G001-G021 (Galt: worst-fifth score >= 80 for every indicator, the stated level where one exists: VIX > 30, dollar at a new 12m high, chips -20% from their 12m high, S&P below its 10m average; 4 sector overlays) | 21 |
| Total hypotheses | 127 |

Merges: Gerstner and Tropin on policy uncertainty (D001/D002). Gerstner and Tropin on tariffs feeding into TIPS (D004/D005).
Druckenmiller 2024, Tropin 2025 "incurable deficit" and Sokoloff on deficits at full employment (D026/D027).
Druckenmiller's two drawdown rules and Law's drawdown rule (D049). The "lighten high flyers" froth rule and the
rally-speed rule (D080).

**Skipped (66)**
- **Sizing or process, not a monthly macro condition (19).** Concentrate on the top ideas; start with a third of the
  position; trade liquid markets only; cold streak means halving the tilts; per-position stop-losses; invest first,
  investigate later; buy back higher; sell when the thesis breaks; the "one-way bet" sizing; capping shorts; Rogers'
  stops vs holding the pain; ignore hot tips; low conviction means staying close to home; be tactical; liquid
  markets 2022; sterling after a big move (needs trend-sleeve internals); close positions before holidays; "never
  invest in the present"; "bond market reacts late".
- **Caveats or meta-tests, with no rule to trade (8).** Algo-era signal decay; debt vs terminal rate; student-loan
  distortion; same management again; market is not the economy; ESG; reserve-currency caveat; the "two-thirds ex-AI"
  rule (duplicates the GDP ex-AI rule).
- **Data missing (33).** TPU; GPR (twice); trade openness; NFIB; FX regime factors (G10 2y yields, current accounts);
  peg reserves; central-bank gold buying; GDP ex-AI capex; mega-cap capex and free cash flow; quality factor; auto
  delinquency (twice); statutory tariff rate; funding stress (SOFR-IORB, TED); EM central-bank claims; refinancing
  wall; Philly Fed future activity; peg divergence; mining and farm employment; frontier markets; NIIP; G10 hawkish
  ranking; BDC and private credit (three rules); TTF gas (twice); S&P sector weights (twice); put/call and retail
  calls; homebuilder P/B; GSCPI; crude inventories.
- **Event dates or intraday/daily data (5).** Chip tariffs; tariffs on inputs; S&P -3% day with low VIX; overnight
  political gap; OPEC cut announcements.
- **Not expressible in the harness (1).** "Banks well capitalised, so cap the cut at 50%" needs a floor on exposure.
  The harness offers only caps (cut) and a full override (block).

**Coded only in part (a leg is missing or proxied)**
- D033: no top-1% share.
- D039: no capex-boom precondition.
- D061: no "economy needed lower rates" test, no local bonds.
- D090: no OPEC leg.
- D094: openings per unemployed only. Unemployed persons are approximated from payrolls and the unemployment rate;
  no wage tracker.
- D106: NFIB leg missing, so all 3 available signals are required.
- D076: top-10 weight and tech P/E replaced by the narrow-leadership score >= 80 and CAPE > 30.
- D028-D030, D037, D051: Baa-10y spread instead of HY OAS. The panel has HY OAS only from 2023-10. D028, D037 and
  D051 use a trailing 20-year percentile because the Baa spread drifts upward over time.
- D003-D005, D040: tariff rate = customs duties / imports of goods and services. This understates the goods-only rate.
- D085: transports instead of airlines.
- D060: drilling industrial production instead of the rig count.
- D018: Philly Fed instead of ISM (the rule's own proxy).
- D015: BRL/MXN/KRW/INR instead of BRL/ZAR/TRY/ARS.
- D016: Brazil only.
- D012/D019/D070: monetary base stands in for the Fed balance sheet before 2002.

**Panel workarounds (no look-ahead)**
- Core CPI in `F` starts in 1997. Before 1998 it is 0.35 x core goods + 0.65 x services less energy, lag 1. This
  matches official core CPI within a few tenths: 1975 11.3%, 1990 4.4%.
- Nominal GDP in `F` starts in 1992. Before that it is real GDP x deflator (quarterly, lag 4).
- Deficit = 12-month sum of the Monthly Treasury Statement (lag 1) / nominal GDP.
- G3 central-bank flow: the ECB and BoJ balance-sheet changes are converted at the current exchange rate. The rates
  are EXUSEU and EXJPUS monthly averages, read from the repo cache `cache/macro/raw/` (read only).
- BoJ rate: the call rate from the same cache (lag 1); before 1985 the discount rate.
- Derived assets added to `R` at import: `b7_real` (equal-weight commodities, gold and TIPS, net of fees),
  `b7_trend3` and `b7_trend_blend` (built with `trend_sleeve`), `b7_deval` and `b7_domino`. The last two are
  equal-weight baskets chosen at t, earned at t+1, with inner turnover costs.

**Never or almost never true**
- D106: 1 month, 2022-03.
- D096: 2 months.
- D023: 3 months.
- D051: one episode, 2024-09.
- D050: one episode, 2009-05.
- D028: 13 months.
- D055: 17 months.
- D005/D040: 2025-11 on only.
- D038: youth data start in 2013.
- D010/D011: the G3 flow starts in 2003.
- `on_share` overstates activity wherever the traded asset starts late, because the fallback sets those weights to
  0: TIPS from 2004, HY 2007, EUR/JPY 2006-07, TAIL 2017, equal-weight S&P 2003, bitcoin 2014.

## 2. Data needed (missing series -> best proxy, source, start)

| Needed | Best proxy / workaround | Source | Start |
|---|---|---|---|
| Trade Policy Uncertainty | TPU newspaper index; or the EPU "trade policy" category | policyuncertainty.com (Caldara et al.; Baker-Bloom-Davis categorical EPU) | 1960 (historical TPU) / 1985 |
| Geopolitical Risk, China/Taiwan/Russia sub-indices | GPR country indices; second best: oil 1m spikes + gold vs S&P | matteoiacoviello.com | 1985 (1900 historical) |
| Trade openness by country | World Bank NE.TRD.GNFS.ZS | WDI | 1960 annual |
| NFIB optimism / expected conditions | Philly Fed future general activity (FRED NOFDFSA066MSFRBPHI) + Empire State future + Korean exports y/y (already in S) | NFIB / FRED | NFIB 1986 monthly (1974 quarterly); Philly 1968 |
| ISM manufacturing / new orders | Average of regional Fed surveys (Philly 1968, Richmond 1993, Kansas City 2001, Dallas 2004, Empire 2001) + Korea and Taiwan exports y/y | regional Feds / OECD MEI | 1968 |
| Philly Fed future activity (bottom-up rule) | NOFDFSA066MSFRBPHI | FRED | 1968 |
| ZAR, TRY, ARS spot | DEXSFUS (ZAR); TRY=X and ARS=X; BIS daily FX | FRED / Yahoo / BIS | ZAR 1971, TRY 1990s (Yahoo 2003), ARS 1990s |
| MSCI EM before 2003 | MSCI EM gross USD; or equal weight of eq_korea, eq_brazil, eq_mexico, eq_hongkong, eq_india | msci.com end-of-day history | 1988 |
| South Africa equity and policy rate | MSCI South Africa; SARB repo rate (FRED IRSTCI01ZAM156N) | MSCI / FRED-OECD | 1988 / 1960s |
| Daily S&P, VIX, ES futures (algo days, VIX 5-day falls, overnight gaps) | Daily ^GSPC open/close, ^VIX, ES=F | Yahoo | 1950 / 1990 / 2000 |
| G10 2y government yields (hawkish ranking, FX regime) | OECD 3m interbank rates already cached (IR3TIB01xxM156N) as policy-path proxy; 2y from Bundesbank, BoE, MoF Japan | repo cache / central banks | 1960s-1970s |
| Current accounts | FRED BOPBCA (US), OECD current account % GDP | FRED/OECD | 1960 |
| FX reserves of pegged currencies | IMF IFS total reserves ex gold | IMF | 1950s |
| CFTC positioning (USD, EUR, JPY) | CFTC COT legacy futures-only; proxy: 12m FX momentum in top decile | cftc.gov | 1986 |
| BoE Bank Rate; full BoJ policy rate | BoE database IUMABEDR; BoJ policy rate | BoE / BoJ | 1694 / 1883 |
| HY OAS full history (panel has 2023+ only) | ICE BofA H0A0 (licensed; FRED serves 3 years); proxy: Baa-10y (used), Baa-Aaa, HYG/JNK total return vs IEF (2007), Moody's spec-grade yields | ICE / FRED / Moody's | 1996-12 (OAS) / 1919 (Baa) |
| GDP ex AI capex | Real GDP minus real info-processing equipment (A679RX1Q020SBEA), software (B985RC1Q027SBEA), data-center construction (Census C30) | BEA via FRED / Census | 1947 / 1959 / 2014 |
| Mega-cap capex and FCF margin | Sum of PaymentsToAcquirePropertyPlantAndEquipment and operating cash flow for MSFT, GOOGL, AMZN, META, ORCL from the repo's own SEC companyfacts bulk data | SEC XBRL (already in repo) | 2009 |
| Quality / low-leverage factor | Ken French RMW (5-factor file the repo already downloads); AQR QMJ; QUAL ETF | French / AQR / Yahoo | 1963 / 1957 / 2013 |
| Auto-loan 90+ delinquency | NY Fed HHDC auto 90+; FRED DROCLACBS (other consumer loans, banks) | NY Fed / FRED | 2003 / 1987 |
| Student-loan delinquency | NY Fed HHDC | NY Fed | 2003 |
| Statutory tariff rate | Yale Budget Lab tracker; USITC DataWeb duties by HTS line / dutiable value | Yale / USITC | 2025 / 1989 |
| Goods-only imports (better denominator) | FRED IEAMGSN or BOPGTB goods imports | FRED | 1960 (quarterly) / 1992 (monthly) |
| Funding stress (SOFR-IORB, TED, FRA-OIS) | TEDRATE to 2022 then SOFR-IORB; 3m CP minus T-bill (CPF3M-DTB3); STLFSI4 (already in S) | FRED | 1986 / 1997 / 1993 |
| BDC / private credit stress | BIZD; before 2013 a basket of ARCC, PSEC, MAIN, GBDC total returns vs HYG; Cliffwater CDLI (quarterly) | Yahoo / Cliffwater | 2004 basket / 2013 ETF |
| Leveraged loans | BKLN; S&P/LSTA LLI | Yahoo / S&P | 2011 / 1997 |
| Central-bank gold purchases | WGC quarterly demand trends; IMF IFS official gold holdings (tonnes) change | WGC / IMF | 2010 / 1950s |
| Top-1% income share | WID.world | WID | 1913 annual |
| Effective rate on outstanding mortgages / corporate debt | BEA mortgage interest paid / Z.1 mortgage debt; NIPA net interest / Z.1 nonfinancial corporate debt | BEA / Fed Z.1 | 1960 |
| Rig count | Baker Hughes US rotary rigs (used drilling IP IPN213111N instead) | Baker Hughes | 1944 monthly / 1987 weekly |
| Crude inventories vs 5y average | EIA US crude ex-SPR stocks | EIA | 1920 monthly / 1982 weekly |
| Europe natural gas (TTF) | World Bank Pink Sheet "Natural gas, Europe": the same pink-sheet file that gives wb_*; just add the column | World Bank | 1960 monthly |
| Mining and farm employment | FRED CES1000000001 (mining and logging); USDA farm sector income | FRED / USDA | 1939 / 1910 |
| Frontier markets | MSCI Frontier; FM ETF | MSCI / Yahoo | 2002 / 2012 |
| US net international investment position | FRED IIPUSNETIQ (quarterly), IIPUSNETIA (annual) | BEA via FRED | 2006 / 1976 |
| Put/call ratio, retail call share, AAII | CBOE equity P/C, total P/C; AAII bull-bear | CBOE / AAII | 2003 / 1995 / 1987 |
| S&P sector weights (semis share, defensive share) | Ken French 49-industry files: average firm size x number of firms = industry market cap, a value-weighted share of the total (repo already downloads the industry zip) | Ken French | 1926 |
| Homebuilder price-to-book | Ken French industry B/M (annual), or book equity of DHI, LEN, PHM, NVR from SEC XBRL vs their market caps | French / SEC | 1926 / 2009 |
| Airlines / travel | JETS; Dow Jones US Airlines; Ken French "Trans" is a weak proxy (used IYT) | Yahoo / S&P | 2015 / 1990s |
| NY Fed GSCPI | GSCPI | NY Fed | 1997 |
| Wage Growth Tracker; unemployed persons | Atlanta Fed WGT; FRED UNEMPLOY (D094 approximates it from payrolls) | Atlanta Fed / FRED | 1983 / 1948 |
| OPEC production cuts | EIA OPEC crude production; event = 3m change <= -1 mb/d | EIA | 1973 |
| Fed funds futures (cuts priced) | CME 30-day FF futures; 2y minus Fed funds used | CME / FRED | 1988 |
| Treasury auction tails | TreasuryDirect auction results (high yield vs when-issued, needs WI data) | TreasuryDirect | 1980s-2000s |
| Longer history of series cut short in the panel | CPILFESL (1957), PPIACO (1913), PCEPILFE (1959), LNS14024887 (1948), ACM term premium (1961 from the NY Fed site), GDP (1947): all are just download limits in `cache/macro/raw` | FRED / NY Fed | as listed |

## 3. Results that look too good (or too clean) to trust

No batch-7 hypothesis is a big winner. The largest full-period Sharpe gains against candidate 5.0 are about 0.05.
The ones to treat with suspicion:

- **D099, D045, D102 (cross-asset trend sleeves).** Sharpe gain +0.04 to +0.05, worst drawdown 3-4 pts better,
  but CAGR 1-1.5 pts lower.
  - The pre-1985 legs use AQR's back-constructed equity index series (`intl_eq`) and spliced index proxies (the
    synthetic 30-year bond, the commodity index). They were not tradeable as built.
  - Shorting total-return series ignores borrow and roll costs. The only cost charged is 0.1% per unit of turnover.
  - The gain is mostly 1975-2000. D045 is about 0 in 2012-2026, consistent with the post-2010 decay in trend returns.
- **D024 (July-August cut).** +0.10 Sharpe in 1975-2000, but -0.04 in 2001-2026 and -0.10 in 2012-2026. This is the
  pattern of a data-mined calendar effect.
- **D079 (no cuts in midterm Q4).** Same flip: +0.06 in 1997-2011, -0.16 in 2012-2026.
- **D103 (bitcoin 2% above its 10m average).** All of the gain is 2015+ and comes from one asset's exceptional run.
  Bitcoin was picked with hindsight.
- **D021 and D022 (Nasdaq after a Fed cut into a strong economy).** D022 is Druckenmiller's own 1998-99 story turned
  into a rule. It fires in 5.5% of months and the 1999 Nasdaq gain dominates.
- **D051, D050, D106, D055.** One- or two-episode rules written after the episode they describe (Sep-2024 cut,
  2009 bottom, Mar-2022, the late-1960s). Any gain is anecdotal, not evidence.
- **D076 (TAIL hedge when leadership is narrow and CAPE > 30).** TAIL only trades from 2017, so the measured effect
  is 2017-2026 alone.
- **D105 (short EUR/JPY when those central banks ease against a non-easing Fed).** The currency ETFs start in
  2006-07, so the gain comes from the 2013-15 and 2021-24 yen and euro slides, against a reported 43% on-share.
- **D003-D005 and D040 (tariffs).** The customs ratio jumps in 1975-76 (2.8% to 5.6%) because of Ford's oil-import
  fees, not consumer tariffs. Apart from that, the tariff rules fire mainly before 1977 and in 2025-26.
- **The same +1.25 pt change in c5's worst drawdown shows up in about 10 unrelated hypotheses** (D021, D022, D076,
  G005, G006, G007, G014, G015, D002). c5's worst drawdown is a single episode, so any small exposure change in
  those months moves it. Not a sign of robustness.
- **Clear rejections, not artifacts.** D057/D058 (Druckenmiller's narrow-leadership precondition used as a "no cuts
  otherwise" block) cost about 0.32 Sharpe and 30 pts of drawdown, because they switch off the cuts in 70% of months.
  D071 (Rogers' no shorts after a crash and a 10% rebound) costs 16 pts of drawdown: the block lands on bear-market
  rallies and keeps the book invested through the second leg down (2008-09).
