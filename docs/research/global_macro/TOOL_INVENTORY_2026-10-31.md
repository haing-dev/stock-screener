# Global Macro Book: complete inventory for review (2026-10-31, version gm-1.2.0)

Purpose of this document: give a reviewer (another chat) everything the tool currently contains, every source read so
far, and every gap, so that a new batch of transcripts can be checked for additions. Paper research only (no money).
Repo: `haing-dev/stock-screener` (private), code in `gm/`, plan and results in project doc
`claude/global_macro_book_plan_2026-10-29.md`, change and trial log in `gm/CHANGES.md`.

---

## 1. What the tool is

- A systematic, slow-frequency, long/short, multi-asset, multi-country macro book, in the style of AQR and Man AHL
  macro funds. Its target is the middle ground: about 10% volatility, net Sharpe 0.5-0.8 live, correlation with stocks
  near zero, worst fall 15-20%.
- Monthly rebalance, at month-end close, from month-end data only. Daily data exists but is not used yet.
- All signals give continuous scores (no on/off switches). Positions are sized by volatility, and the whole book is
  scaled to 10% annual volatility.
- It runs on GitHub Actions on the 3rd of each month.
  - Branch `gm-status`: status page with positions, family breakdown, factor exposure, stress tests and data flags.
  - Branch `gm-record`: append-only paper ledger. Restatements are appended, never overwritten.
- Validation design:
  - design period 1990-2010; extra check 1975-89;
  - holdout 2011-2026, never looked at, to be run once after the Bloomberg data and version freeze (gm-2.0);
  - live paper record from Sep 2026.

### Results so far (design periods only)
| Version gm-1.2.0 | Net Sharpe | Net Sharpe at 2x costs | Max drawdown | Correlation with S&P 500 |
|---|---|---|---|---|
| 1990-2010 | 1.47 | 1.36 | -12% | -0.06 |
| 1975-89 | 0.93 | 0.87 | -21% | 0.21 |

Crisis months, 1990-2010 design: 1987 crash -19% (S&P -29%); 1994 +2%; 1998 LTCM +8%; 2000-02 bear market +32%;
2008 +57%.

Expected live Sharpe is 0.4-0.8. Published styles weakened after 2010, and about 0.3-0.4 of the design Sharpe depends
on trading within days of month end.

---

## 2. Universe (62 traded markets + 3 untraded spreads)

| Class | Markets (start of usable data) | Return construction |
|---|---|---|
| Equity indexes (18) | US S&P 500 (1963), Nasdaq 100 (1985), Russell 2000 (1987), Euro Stoxx 50 (2000), Germany DAX (1988), UK FTSE (1975), France CAC (1990), Japan (1975), Canada (1977), Australia (1975), Hong Kong (1981), China (1997), Korea (1997), Taiwan (1997), India (1997), Brazil (1996), Mexico (1997), South Africa (2001) | Local-currency total return minus local 3m rate known at the start of the month. Sources in priority order: MSCI gross local (2001+; manual download, kept out of git), country ETF converted to local currency, Ken French country market portfolio (1975+), price index plus a dividend estimate (estimated on data up to 2010 only) |
| Government bonds (9) | US 2/5/10/30y (1962-77); Germany (1972), UK (1993), Japan (1986), Canada (2001), Australia (1995) 10y | Par-bond return from month-end yields minus local 3m rate. Sources: FRED daily, Bundesbank, MoF Japan, Bank of Canada, RBA, BoE |
| Short end (6) | US 2y, Germany 2y, UK 5y, Canada 2y, Australia 2y, Japan 2y | Stand-in for short-rate futures (2y par notes) |
| Currencies vs USD (13) | EUR (1999), JPY, GBP, CHF, AUD, NZD, CAD, SEK, NOK (1970s-82), MXN, BRL (1996-97), KRW (1991), ZAR (1980) | Month-end spot change plus the 3m rate differential. Sources: Fed H.10 daily first, then Yahoo |
| Commodities (16) | WTI (1985), natural gas (1994), heating oil (1994), gasoline (2000), Brent (2007), gold, silver, copper (2000), platinum (1997), corn, wheat, soybeans, sugar, coffee, cotton (2000), live cattle (2001) | Energy: EIA NYMEX contract-2-to-1 roll (true futures excess return). Others: ETF or Yahoo front future (not roll-adjusted). Before 2001 the class is represented by the AQR long-run equal-weight index |
| Spreads (3, built, not traded) | US 2s10s steepener (1976), German 2s10s (1972), US 10y breakeven (2003) | Duration-neutral pairs; breakeven change x 8 |

Data check against AQR's published trend factor, 1985-2026, monthly correlation:
- whole book 0.83;
- equity 0.80, bonds 0.85, FX 0.65, commodities 0.81 since 2001.

---

## 3. Signal families (what is live, what was tested, what failed)

### Live in gm-1.2.0 (fixed risk shares)
| Family | Share | Definition | Design 1990-2010 Sharpe (alone) |
|---|---|---|---|
| Price trend | 30% | Per market, the average sign of 1-, 3- and 12-month excess return, held directionally (time-series momentum) | 1.20 (EQ 0.55, FI 0.87, FX 0.96, CM 0.56) |
| Economic trend | 30% | Four themes, each a 12-month change scaled by its own 10-year volatility (capped at 3), combined as tanh, signed per asset class (AQR table): **inflation** (CPI y/y change, lag 1); **trade** (BIS nominal effective FX, weakening = +, lag 1); **monetary** (2y yield, or the 3m rate lagged 1 where no 2y exists); **risk appetite** (12-month local equity excess return plus narrowing of the Moody's Baa spread, lag 1). FX uses local minus US themes. Commodities use the average of US, Germany, Japan and China themes. The growth theme is OFF | 0.59 (EQ 0.66, FI 0.29, FX 0.47, CM -0.12) |
| Carry | 20% | Half directional, half cross-sectional within class. Bonds: yield minus local 3m rate (lag 1). FX: local minus US 3m rate (lag 1). Energy: annualised F1/F2 - 1 from EIA curves | 0.92 (FI 0.75, FX 0.76, CM 0.36) |
| Value | 15% | Cross-sectional within class. Equities: dividend yield (Ken French with minus without dividends; US from SPY minus S&P price), developed markets only. Bonds: 10y yield minus trailing 3-year CPI inflation. FX: 5-year real depreciation (PPP gap) | 0.15 (EQ 0.29, FI 0.06, FX 0.39) |
| Cross-sectional momentum | 5% | 12-1 month return rank within class | 0.53 |

### Signal sign table (economic trend, from AQR "Economic Trend")
| Theme | Stocks | Bonds | Currency | Commodities |
|---|---|---|---|---|
| Growth (off) | + | - | + | + |
| Inflation | - | - | + | + |
| Trade (currency weakening) | + | - | - | - |
| Monetary policy (rates rising) | - | - | + | - |
| Risk aversion falling | + | - | + | + |

### Tested and rejected (all logged in `gm/CHANGES.md`, about 37 variants)
| Idea | Result (design period) |
|---|---|
| Equity value by 5-year reversal | -0.46 |
| Commodity value by 5-year reversal | -0.62 |
| Equity carry (dividend yield minus 3m rate) | 0.02 |
| Growth theme from revised OECD leading indicator | 0.42 alone, but mostly hindsight (commodities 0.68 -> 0.05 point in time) |
| Growth theme point in time (Dallas Fed and OECD vintages: IP growth change, unemployment change, CLI) | 0.29 alone; no gain for the book; worse in 1975-89 |
| IMF WEO forecast revisions (2006+) | Cross-section nothing (t < 1); bonds directional t 1.8 |
| Early-warning risk scalers (credit-spread jump, cross-asset correlation jump, drawdown brake) | None improves Sharpe; correlation scaler cuts max drawdown -12% -> -9% but lowers return; none helps in 1975-89 |
| Trend lookbacks 3/6/12, 6/12, 12 | Lower Sharpe (1.27-1.35 vs 1.48); with a 1-month delay all land at about 1.1 gross |
| Value + momentum 50/50 pairing | 0.23 |

### Research-only signals (WRDS; cannot be used live under the WRDS licence)
| Signal (25 countries, cross-sectional, after 10 bp costs) | 1990-2025 Sharpe |
|---|---|
| Value composite (B/M, E/P, D/P) + I/B/E/S analyst revisions | 0.69 (t 4.1); 0.55 acting one month late |
| Value alone | 0.55 gross |
| Revisions alone | 0.42 gross; 0.58 since 2008 |

---

## 4. Portfolio construction and risk engine

- **Per family and asset class:** score x 40% / trailing 36-month volatility per market, equal weight within the
  class. Each family-class block is scaled to unit ex-ante volatility (trailing 36-month realised, lagged).
- **Across families and classes:** family shares are fixed (30/30/20/15/5). Asset classes get equal risk.
- **Whole book:** 10% volatility target (trailing 36-month realised volatility of the unscaled book, lagged).
- **Caps:**
  - per-market risk cap;
  - gross notional at most 5x (binds in calm years, mostly through bond notional).
- **Costs (one-way, bp):** US equity 1, other developed equity 2, EM equity ETFs 5, bonds 1, G10 FX 2, EM FX 8,
  energy 4-6, other commodities 4. Futures rolls are charged per year. EM equity shorts pay 1%/yr borrow. Turnover is
  about 22x notional a year, costing about 1.2%/yr.
- **Status page diagnostics:**
  - betas of today's positions to equity, US 10y bonds, the US dollar and commodities, and the residual share;
  - stress P&L of today's positions in the 2008, 2020, 2022 and 1994 windows.
  - 2026-09 positions: 82% of risk explained by those factors (short bonds, long USD, long commodities). Stress:
    2022 +22%, 1994 +6%, 2020 -2%, 2008 -8%.
- **Not built (in the plan):**
  - the equity-beta cap of -0.5 to +0.5;
  - an EWMA covariance with shrinkage (today volatility is scaled per block, not with a full covariance matrix);
  - covariance that adapts to the stock-bond correlation regime;
  - weekly trading with a 15% no-trade band;
  - a margin or liquidity reserve rule.

---

## 5. Validation done

- **Data check against AQR:** trend factor correlation 0.83 (whole book).
- **Independent look-ahead audit** by a separate agent: rebuilt with data cut at 4 dates; signals and positions were
  identical up to each cut. It found 6 issues, all fixed in gm-1.2.0:
  - dividend estimate using later data;
  - same-month rates;
  - an unlagged rate fallback;
  - an outcome-based outlier filter (bad KRW prints from Yahoo replaced by Fed H.10);
  - SPY not being read;
  - report month.
- **Documented, not fixed:**
  - the universe was hand-picked from survivors;
  - EM FX is only MXN/BRL/KRW/ZAR (no TRY, RUB, THB, IDR, ARS), which flatters carry;
  - families were dropped after seeing design results;
  - CPI and BIS data are latest vintage.
- **Holdout script** `gm/holdout.py` refuses to run twice per version. Pass criteria: net Sharpe at least 0.5, worst
  fall above -20%, correlation with the S&P 500 at most 0.3, 2020 and 2022 not negative.

---

## 6. The sibling tool: Macro Compass (US stocks, `macro/`, public page)

This is where the transcript theories currently live. Family 3.8 of the macro book is meant to rerun them long/short
across countries.

- **Indicators (43, six pillars), each cited to transcripts.** By pillar:

  | Pillar | Indicators |
  |---|---|
  | Growth | Sahm-style unemployment rise, truck freight, home permits, car sales, 10y-2y curve, youth joblessness, credit-card delinquencies |
  | Market health | cyclicals vs defensives, staples vs discretionary, industry breadth, industries 20% below high, transports vs industrials, homebuilders |
  | Inflation | core PCE 3m vs 12m, core CPI, PPI, 5y inflation expectations, oil, copper, stock-bond correlation |
  | Stress | VIX, S&P vs 10-month average, junk vs Treasuries, Baa spread level and change, banks vs market, dollar vs 12m high, chips vs 12m high |
  | Money and rates | Fed funds change, 10y change, 10y minus nominal GDP growth, M2 growth, dollar change, oil+rates+dollar squeeze, real 10y yield, mortgage rate change, term premium change, Fed net liquidity |
  | Froth | market cap/GDP, household equity share, CAPE, rally speed, narrow leadership |

- **States:** Expansion, Late, Overheating, Contraction, Stagflation, Recovery, plus a stress overlay, with an
  investor playbook per state.
- **Live rule P1 (5.0):**
  - Track-record-weighted warnings (28 core indicators) cut stocks 100% -> 0% as their share goes 15% -> 35%, only
    while the Fed is tightening.
  - S&P below its 10-month average AND unemployment above its 12-month average -> 0% stocks.
  - TLT when growth is weak and the stock-bond correlation is below 0, else T-bills.
  - 10% commodities in a commodity uptrend.
  - Sector-momentum tilt.
- **Transcript hypothesis test:**
  - 1,062 rules from the 61 transcripts below were coded into 731 hypotheses; 690 were usable.
  - 7 passed the screen, 5 the placebo, 1 FDR (Gromen: commodities sleeve in a commodity uptrend).
  - The presidential cycle (Hirsch) passed placebo but not FDR.
  - A long-only US book could not express most macro theses (shorts, other countries). That is why the macro book
    exists.

---

## 7. Sources read in this build

### 7a. Quant papers (folder `Macro Transcripts/Quant`)
1. AQR, *Economic Trend* (Brooks, Feilbogen, Ooi, Akant 2023): `Economic Trend_.pdf`
2. AQR, *Certainly Uncertain* (Brooks 2023): `AQR_Certainly Uncertain.pdf`
3. Man AHL, *Dissecting Investment Strategies in the Cross Section and Time Series* (Baz, Granger, Harvey, Le Roux,
   Rattray 2015): `dissecting-investment-strategies-in-the-cross-section-and-time-series.pdf`
4. Asness, Moskowitz, Pedersen, *Value and Momentum Everywhere* (2013): `ValMomEverywhere.pdf`

### 7b. Manager research supplied in chat
5. Graham Capital, *Imbalances, Consolidation and Choke Points* (Foehrenbach, May 2026)
6. Graham Capital, *From Suppressed to Structural* (Politi, Jun 2026)
7. Graham Capital, *Trend-Following Primer* (May 2026)
8. Graham Capital, *Q4 2026 CIO Outlook* (Foehrenbach, Oct 2026)
9. Man Group, *The Quant Renaissance II: Winter's Thaw?* (Xiang, Ben-Akiva)
10. Cliff Asness with Tyler Cowen (Conversations with Tyler, 2015)

### 7c. Solovis insights (10 relevant of 26)
Momentum vs Trend Following; How to Identify Independent Sources of Risk; Five Safe-Haven Assets in 2022; Risk Without
Return; Is Your Total Portfolio at Risk?; Factor Investing & Analysis Guide; The Bacon Factor; How Do Sector Bets
Translate into Factor Bets; Incorporating a Total Portfolio Approach; The Science of Finance.

### 7d. AQR data sets used as references
TSMOM factors; Value and Momentum Everywhere factors; Century of Factor Premia; Commodities for the Long Run.

### 7e. X posts
Galt (@AtlasShrug1): only the rules already coded in `macro/registry.py`. Raw posts are not available.

### 7f. Macro transcripts read in full (61 files, `Processed Transcripts/Macro Transcripts`)
These became the 1,062 rules / 731 hypotheses (`docs/research/hf_macro/transcript_rules/batch1-7.md`).

1. Cullen Roche, "Macro Investing - Understanding How And Why w- Cullen Roche (TIP486)" (Oct 2022)
2. Kyle Bass, "Global Macro Investing And Geoeconomics With Hedge Fund Investor Kyle Bass - Hoover Institution" (Jun 2025)
3. Jeffrey Hirsch (with Steve Eisman), "Market Patterns Work and Jeffrey Hirsch Explains Why - The Real Eisman Playbook Ep 56" (Apr 2026)
4. Stanley Druckenmiller (with Kiril Sokoloff), "Sohn 2023 - Kiril Sokoloff in conversation with Stanley Druckenmiller" (May 2023)
5. Mike Pompeo, "Mike Pompeo, Former US Secretary of State & CIA Director, on Geopolitics, Leadership & the Economy" (Money Maze, Jul 2023)
6. Ajay Banga, "Ajay Banga - President of World Bank - Podcast - In Good Company - Norges Bank Investment Management" (Oct 2023)
7. Pablo Calderini (Graham Capital), "Navigating a New World Order- Macro Strategies for Uncertain Times" (posted Jan 2025; content recorded ~Mar 2023, during SVB / debt-ceiling period)
8. Pablo Calderini (Graham Capital), "Resilient Strategies- Tailwinds in Left-Tail Scenarios" (Jun 2024)
9. "What is the fiscal rule-" (NBIM, Oct 2024; speaker is a former Norwegian finance minister and prime minister in 2000 who designed the rule, interviewed by NBIM; name not stated in transcript)
10. Ep14. Public Market Volatility, AI Air Pocket, $GOOG Ruling - BG2 w- Bill Gurley & Brad Gerstner (Aug 2024)
11. Optimizing Investment Alpha with Customized Completion Portfolios Featuring Chris Jones, Ph.D. (Graham Capital webinar, Nov 2021 content; uploaded 2025)
12. The Market's Biggest Warning Signs Right Now with Todd Sohn - The Real Eisman Playbook Ep 66 (June 2026)
13. Stanley Druckenmiller on Economy, Stocks, Bonds, Trump, Fed- Full Interview (Bloomberg, recorded Dec 2018)
14. #133 - Jan van Eck- Macro Forces Shape Markets (Insightful Investor, July 2026)
15. Børge Brende - Podcast - In Good Company - Norges Bank Investment Management (June 2025)
16. Global Macro- Discretionary vs. Systematic - Who Wins- - Global Alts 2025 - Pablo Calderini (Graham panel, Feb 2025)
17. Rob Citrone and Karen Karniol-Tambour at Sohn 2025 (May 2025)
18. Steve Cohen and Jawad Mian at Sohn 2025 (May 2025)
19. Luke Gromen — What if the Saudis Break the Petrodollar System (recorded 12 Jan 2022)
20. Kenneth Rogoff — In Good Company, NBIM (Apr 2025)
21. Scott Nations — How to Act Rationally During a Financial Crisis (2022 bear market)
22. Scott Bessent — Inside Trump's Treasury; War Costs; Why Bond Market is King (Mar 2026, during Iran conflict)
23. Kenneth Tropin (Graham Capital) — Risk and Return Podcast (Aug 2025)
24. Margrethe Vestager — EU Competition Commissioner, NBIM (Sep 2024)
25. Paul Krugman — Generating Alpha Podcast Ep. 28 (Jul 2025)
26. Jeff Yass (Susquehanna) — Economic Myths, Generating Alpha Ep. 55 (Jun 2026)
27. Karen Karniol-Tambour (Bridgewater) — Sohn 2022, A Macro Approach (May 2022)
28. AI, Middle East, China, Tariffs, Recon Bill, Invest America (BG2, Bill Gurley & Brad Gerstner, May 2025)
29. Rob Citrone, Discovery Capital (Capital Allocators EP.261, July 2022)
30. Scott Bessent on Real Vision (recorded ~late April/May 2024; uploaded Nov 2024), "Trump's NEW Treasury Secretary on Macro Strategy"
31. The Real Eisman Playbook Ep 73: The AI Trade, Rising Rates (Steve Eisman with Jason Trennert and Chris Verrone, Strategas; Aug 2026)
32. Peter Oppenheimer, Goldman Sachs (Money Maze Podcast, Oct 2022)
33. Christine Lagarde, ECB President (NBIM In Good Company, March 2026)
34. Kristalina Georgieva, IMF Managing Director (NBIM In Good Company, Dec 2025)
35. Is OpenAI the Achilles' Heel of the US Economy? (Steve Eisman, The Weekly Wrap, Sept 2026)
36. Greg Jensen — Co-CIO of Bridgewater (NBIM In Good Company, upload 2025-11-26)
37. Stanley Druckenmiller — Sohn 2022 (conversation with John Collison)
38. Ray Dalio — Five Forces Shaping the Global Economy (Money Maze Podcast, 2023-11-02)
39. Bob Prince — Co-CIO of Bridgewater (Generating Alpha Podcast Ep. 12, 2025-03-20)
40. BG2 Thanksgiving Roundtable — Brad Gerstner & Bill Gurley (Bg2 Pod, 2024-11-27)
41. Graham Capital 2022 Virtual Investment Symposium — Discretionary Strategies Panel (Pablo Calderini, Kelly (Katie) Dropping Woodridge, Peter Chapson, David Keelan, Chris McCann; recorded Sept 2022)
42. Kenneth Tropin — Graham Capital (iConnections, 2025-06-17)
43. Felix Zulauf — Zulauf Consulting (Generating Alpha Podcast Ep. 15, 2025-04-10)
44. General David Petraeus — "The War in Ukraine, Relations With China & Wider Geopolitics" (Money Maze, 2023-01-19)
45. Bill Gurley & Brad Gerstner — "Tariffs, Free Trade, Export Controls, H20 & Rare Earth Ban" (BG2, 2025-04-24)
46. Scott Bessent — "Macro Maven" (Capital Allocators EP.415, 2024-11-04)
47. Krishna Guha (Evercore), host Steve Eisman — "5% Rates, Bessent's Failed Gamble & What Comes Next" (Real Eisman Playbook Ep 78, uploaded 2026-10-05)
48. Geoffrey Garrett (USC Marshall dean) with Nicolai Tangen — NBIM "In Good Company" (2025-05-07)
49. Ken Tropin (Graham Capital) — Macro Hive with Bilal Hafeez (uploaded 2025-02-14; content recorded ~spring 2023, "two weeks" after SVB)
50. Stanley Druckenmiller — "Druckenmiller on How AI is Dominating His Long Portfolio" (Bloomberg Live, 2023-06-07)
51. Stanley Druckenmiller — "Hard Lessons: Invest, then investigate" (Morgan Stanley, 2026-02-27)
52. Crescat Capital (Kevin Smith presenting; Quinton Hennigh referenced) — "A Brief World Economic History For Gold, Silver, and Fiat Money" (2024-05-06)
53. DeepSeek, Open Source, Tariffs, DOGE, Market Impact (BG2: Bill Gurley & Brad Gerstner, 2025-02-05)
54. Stanley F. Druckenmiller: Monetary Policy & Markets (Real Vision, 2018-11-13)
55. Inside America's Economic Divide: AI, Tariffs, & The Fed (Real Eisman Playbook Ep. 29; Steve Eisman with Steve Liesman, 2025-10-13)
56. The Boardroom Masterclass: Andrew Law (Caxton Associates; University of Sheffield, 2020-09-17)
57. Stan Druckenmiller, In Good Company (Norges Bank Investment Management, 2024-11-06)
58. Episode 5: Jim Rogers (Generating Alpha Podcast, 2025-01-04)
59. Ken Tropin on Macro Hive Podcast: Markets, Risk, AI-Driven Technology (Graham Capital, 2025-12-15)
60. Why This Market "Melt-Up" is Making Me Nervous (Steve Eisman, The Weekly Wrap, 2026-05-15)
61. Graham Capital Management's Tropin on Why Macro is Killing It (Bloomberg Live, 2022-10-12)

Folder status (2026-10-31): `Macro Transcripts` now holds about 216 transcripts. The 61 above were read; about 155
(many *Systematic Investor* / *Top Traders Unplugged* episodes and others) have NOT been read for this build. They are
the obvious "new batch".

---

## 8. What is missing

### 8a. Macro mechanisms the book does not model yet (the real blanks)
| # | Mechanism | What it would add | Status / nearest data |
|---|---|---|---|
| 1 | Growth vs expectations (data surprise) | Growth theme as actual minus consensus, the way markets trade data | Bloomberg Economics sheet (first release + consensus, 35 series), Citi surprise indexes; UBC visit next week |
| 2 | Liquidity and plumbing: central-bank balance sheets (QE/QT), reserves, TGA, reverse repo, dollar funding (cross-currency basis), repo stress | A liquidity theme for risk assets and bonds; Druckenmiller, Citrone and Gromen all lean on it | US net liquidity exists in Macro Compass only; no non-US balance sheets, no basis data |
| 3 | Term premium and bond supply (deficits, issuance, auction tails) | A bond-specific driver beyond the policy rate; Graham's "long end held up by deficits" | ACM term premium is in Macro Compass (US only); no issuance or auction data |
| 4 | Market-implied policy path (OIS / fed funds futures) and central-bank surprises | The monetary theme today uses realised 2y changes, not expectations or surprises | Not available free with history; Bloomberg could provide |
| 5 | Real-rate differentials for FX and gold | Graham: FX is driven by real-yield differentials. A pre-registered FX variant exists but is not tested | Needs inflation expectations or breakevens outside the US (only US TIPS) |
| 6 | Credit cycle as its own theme (spreads, lending standards, defaults) | Today only the Baa spread inside "risk appetite" | SLOOS, HY OAS (1996+), EBP available free (US); nothing outside the US |
| 7 | Positioning and flows (CFTC, CTA crowding, fund flows) | Family 3.7 planned at 0% until tested; crowding diagnostic in the plan | CFTC COT selected markets downloaded, unused |
| 8 | Volatility as an asset and signal (VIX term structure, vol risk premium, options carry) | No vol markets or vol carry in the universe | VIX and VIX3M daily downloaded; no options data (no OptionMetrics) |
| 9 | Stock-bond correlation regime inside the risk model | Cap bond diversification credit when the correlation is positive (2022) | In the plan, not built; correlation is used only in Macro Compass |
| 10 | EM sovereign and external risk: current account, reserves, external debt, EMBI spreads, balance-of-payments crises | EM FX carry is crash-prone; no crisis currencies in the universe flatters it | Not built; EMBI not free |
| 11 | Commodity fundamentals: inventories, futures curves outside energy, OPEC supply, seasonality, consumer-weighted demand | Commodity carry beyond energy, better commodity econ theme (today a US/DE/JP/CN average) | Bloomberg curves (next week); EIA inventories free but not fetched |
| 12 | Terms of trade for commodity currencies (AUD, CAD, NOK, BRL, ZAR) | A direct FX driver | Not built; could use the panel's commodity returns weighted by export mix |
| 13 | China credit impulse / Chinese policy cycle | A major global-cycle driver cited by several speakers | Not built; free data is patchy |
| 14 | Fiscal dominance and debt sustainability (r - g, deficits, interest/GDP) | Long-end and currency risk; Bass, Druckenmiller, Dalio themes | Only "10y minus nominal GDP" in Macro Compass (US) |
| 15 | Geopolitics and event risk (GPR index, sanctions, tariffs, war) | Risk overlay, oil and defence moves | GPR and trade-policy-uncertainty indexes downloaded, unused in the book |
| 16 | Regime-dependent behaviour (growth/inflation quadrant, crisis vs mid-cycle) | Report results by regime; any regime weighting only as a pre-registered variant | Quadrant book failed in Macro Compass; regime reporting not built |
| 17 | Cross-asset lead-lag (copper/gold -> yields, credit -> equities, dollar -> EM) | Possible inputs to econ trend under the same-sign rule | Not tested in the book |
| 18 | Transcript theories long/short across countries (family 3.8) | The only route to an edge beyond published premia | Not run yet in the book; 731 coded hypotheses exist for the long-only US setting |
| 19 | Same-sign rule test | A theme or theory may trade an asset only with the sign its news moves that asset in the same month | In the plan, not yet run |

### 8b. Data gaps
| Gap | Effect | Alternative |
|---|---|---|
| Commodity returns before 2000 (except energy) and curves (except energy) | No per-commodity history 1985-99; no non-energy carry | Bloomberg (UBC), Pinnacle CLC (~$100) |
| Consensus forecasts, first releases for most countries after 1998 with release dates | Growth theme limited | Bloomberg Economics sheet |
| Euro before 1999 (DEM) | Germany and France equity start 1988-90 in local terms | Bundesbank DEM/USD series (code still to find) |
| Bond history: Canada from 2001, UK 1993, Australia 1995 | Shorter design sample | Global Financial Data (paid) |
| EM equity valuations (value signal) | Value covers developed markets + US only | MSCI P/E, P/B, D/Y; WRDS (research only) |
| Inflation-linked yields outside the US | No real-rate FX variant, no non-US breakevens | Bloomberg; national debt offices |
| Australian / NZ monthly CPI (quarterly only) | FX value for AUD/NZD missing | Quarterly CPI interpolated |
| Short-rate futures history (SOFR, Euribor, SONIA...) | Front end proxied by 2y notes | None free |
| Daily data in the book | Monthly decisions only; fast-trend execution risk | Free daily already downloaded (FRED, H.10, Yahoo, EIA); not wired in |

### 8c. Method and engineering gaps
- Full covariance risk model (EWMA + shrinkage), equity-beta cap, and correlation-regime adaptation.
- Weekly signal check with a no-trade band. About 0.3-0.4 Sharpe depends on prompt month-end execution.
- Deflated Sharpe with the full trial count (about 37 in the book; 300+ in Macro Compass history).
- Results by regime and a crowding diagnostic (correlation with CTA ETFs DBMF/KMLM, AQR trend).
- Independent rebuild of the book from the written rules (Macro Compass had one; the book had a look-ahead audit only).
- Private web page for the book (status is a markdown file on a branch today).

---

## 9. How to propose additions from new transcripts (for the reviewing chat)

For each idea, give:
1. **Claim** (quote plus speaker, file and date).
2. **Mechanism**: why it should move which asset.
3. **Signal definition**: exact series, transformation, lookback, publication lag.
4. **Sign per asset class**: stocks, bonds, short end, FX vs USD, commodities. Same-sign rule: state how the news
   moves each asset in the same month.
5. **Universe**: which of the 62 markets, directional or cross-sectional.
6. **Data**: free source with history from 1990 (or say what is missing).
7. **Which gap in section 8 it fills**, or which existing family it changes.

Rules the reviewer must keep:
- Ideas are tested only on 1990-2010 (and 1975-89). The 2011-2026 holdout must not be looked at.
- Every variant counts as a trial.
- Prefer ideas that fill section 8a (mechanisms) over re-tunings of trend or carry.
- Prefer continuous scores over on/off switches.
- WRDS data may be used for research statistics only, never for live positions or copied into chat.
