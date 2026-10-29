# Batch 5 — testable rules from macro transcripts

Files (8): Greg Jensen (NBIM In Good Company, 2025-11); Stanley Druckenmiller (Sohn 2022); Ray Dalio (Five Forces); Bob Prince (Episode 12); BG2 Thanksgiving Roundtable (Gerstner/Gurley); Graham 2022 Discretionary Strategies Panel; Kenneth Tropin (Graham Capital); Felix Zulauf (Episode 15).

Notation: "In tool" = already among the 43 Macro Compass indicators. Thresholds marked "(proposed)" are not from the speaker.

---

## File 1: Greg Jensen — Co-CIO of Bridgewater (NBIM In Good Company, upload 2025-11-26)

### US vs rest-of-world equity rotation under "modern mercantilism"
- Source: Greg Jensen — Greg Jensen - Co-CIO of Bridgewater ... NBIM.txt (quote: "you've had the worst performance of US equities relative to the rest of the world equities in common currency terms that you've had over that 15-ear period")
- Type: signal | regime map
- Rule as testable logic: IF US equities (SPY) underperform world ex-US (ACWX/VEU, common currency USD) by more than 10 pts over 12 months (proposed) THEN overweight ex-US equities (VEU/EFA) vs SPY for the next 12 months (relative-momentum persistence test); test also as a regime flag "US exceptionalism unwinding" (tariffs/trade policy shock + USD falling).
- Data needed: MSCI ACWI ex-US / EAFE total return (Yahoo EFA 2001, VEU 2007, ACWX 2008; MSCI EAFE index from 1970 via MSCI site / Ken French international). Not in tool.
- Confidence: medium (stated as observation of regime shift, implies action).

### Look beneath the averages: US ex-AI vs world
- Source: Greg Jensen — same file (quote: "How is the US equity market X the AI names doing relative to investments in the rest of the world?")
- Type: signal
- Rule as testable logic: IF equal-weight S&P 500 (RSP) / cap-weight (SPY) falls >5% over 6 months (proposed) while SPY is flat-up AND world ex-US beats RSP THEN treat headline US strength as narrow; tilt to ex-US and equal-weight / reduce US cap-weight concentration. Overlaps with tool's "narrow leadership".
- Data needed: RSP (2003), SPY, VEU. Narrow leadership is in tool; RSP vs VEU not.
- Confidence: medium.

### Gold as the geopolitics / institutional-trust gauge
- Source: Greg Jensen — same file (quote: "If you look at gold as another example where you're seeing the geopolitics play out.")
- Type: signal | hedge
- Rule as testable logic: IF gold (GLD/LBMA) 12m return > SPY 12m return AND USD falling (proposed) THEN regime = "geopolitical/trust erosion": hold gold allocation (e.g. 10%, proposed) and global diversification instead of US-only equities.
- Data needed: LBMA gold PM fix (FRED GOLDPMGBD228NLBM discontinued; use World Bank Pink Sheet monthly gold 1960, or Yahoo GC=F / GLD 2004). Not in tool.
- Confidence: medium.

### Mercantilism is inflationary (tariffs + military + infrastructure)
- Source: Greg Jensen — same file (quote: "there's nothing more inflationary really than military spending because it creates demand for labor and demand for goods with no supply into the real economy")
- Type: regime map
- Rule as testable logic: IF tariff rate (customs duties / imports) rises >2 pts y/y (proposed) OR defense spending growth (real) > 5% y/y across US+EU (proposed) THEN raise inflation-dial weight: overweight TIPS (TIP) vs nominal Treasuries (IEF), overweight commodities (DBC) for 12 months.
- Data needed: US customs duties (FRED B235RC1Q027SBEA, 1947) / imports of goods (FRED IMPGS); US national defense consumption (FRED FDEFX, 1947); Europe defense spending (SIPRI annual, 1949). Not in tool.
- Confidence: medium.

### AI capex boom is low labor intensity: weak jobs with OK GDP
- Source: Greg Jensen — same file (quote: "you have a disinflationary weak labor market because so much of the growth ... without AI it would be 1%")
- Type: conflict/caveat
- Rule as testable logic: IF unemployment rises (Sahm trigger) BUT real GDP growth ex-information-processing-equipment investment remains > 1% and nominal GDP > 4% (proposed) THEN downgrade the unemployment warning (do not cut stocks on Sahm alone). Caveat to tool's Sahm/unemployment rule.
- Data needed: unemployment (in tool); real private investment in information processing equipment + software (FRED Y033RC1Q027SBEA / B985RC1Q027SBEA), real GDP (GDPC1). Investment split not in tool.
- Confidence: medium (stated for current cycle).

### Inflation base case ~3%; Fed tolerates above 2.5%
- Source: Greg Jensen — same file (quote: "break even inflation is around 2 and a2 we think the fed is very comfortable above two and a half and probably we're in the three range as a base")
- Type: signal
- Rule as testable logic: IF core PCE (or core CPI) 3m annualized > 5y breakeven + 0.5 pt (proposed) THEN breakevens are underpricing inflation: overweight TIPS vs nominals (long TIP / short IEF) for 6 months.
- Data needed: FRED T5YIE (2003), T10YIE; core PCE PCEPILFE (1959). Core inflation and 5y expectations change in tool; the gap is not.
- Confidence: medium.

### Lowering real rates into a boom (political Fed) = inflationary
- Source: Greg Jensen — same file (quote: "lowering real rates into a boom like this is particularly inflationary if it ends up going down that path")
- Type: signal | regime map
- Rule as testable logic: IF Fed funds 12m change < 0 (cuts) WHILE unemployment ≤ its 12m average AND core inflation > 2.5% (proposed) THEN overweight gold + TIPS + commodities, underweight long nominal Treasuries for 12 months.
- Data needed: Fed funds (in tool), unemployment (in tool), core CPI (in tool). Combination not in tool. Gold not in tool.
- Confidence: medium.

### Fiscal-space asymmetry ("we're all Brazil now")
- Source: Greg Jensen — same file (quote: "if the UK said, 'I'm going to do what Germany's going to do. I'm going to write a big fiscal check.' Currency would go down. The equity market would probably go down")
- Type: regime map | signal
- Rule as testable logic: IF a country announces large fiscal expansion (deficit up >2% of GDP, proposed) AND it has fiscal room (debt/GDP low, current-account surplus, high domestic savings) THEN long its currency and equities (e.g. Germany EWG/FXE). IF it lacks room (high debt, current-account deficit, low savings; UK/Brazil-type) THEN short currency (FXB/BZF) and long-dated bonds, equities neutral-negative. Test: monthly panel of G10+EM: change in IMF deficit forecast vs subsequent 6m FX, 10y yield, equity.
- Data needed: IMF WEO general government debt & primary balance (1980), current account % GDP (IMF/World Bank 1980), gross national savings; FX (FRED DEXUSUK etc., 1971); 10y yields (FRED IRLTLT01GBM156N OECD, 1960); MSCI country indexes. None in tool.
- Confidence: high (explicitly framed as general mechanism).

### Fiscal-constrained country: spending becomes counterproductive; US drifting there
- Source: Greg Jensen — same file (quote: "when you get constrained spending money becomes counterproductive rather than productive that's the case in the UK and Brazil today um and the US is drifting towards that line")
- Type: signal | conflict/caveat
- Rule as testable logic: IF on US deficit-widening news (or rising deficit % GDP) the 10y yield rises AND the dollar falls in the same month (bond-down, currency-down, "EM-style" reaction) (proposed: 10y +25bp and DXY −2% in a month) THEN flag "fiscal constraint regime": reduce long Treasury duration (switch TLT → T-bills/short TIPS), add gold.
- Data needed: 10y yield (in tool as 12m change), dollar (in tool); monthly joint sign test new. Deficit: FRED FYFSGDA188S (1929), MTSDS133FMS monthly.
- Confidence: medium.

### Bonds hedge less when fiscal is the lever; correlation shift at fiscal limits
- Source: Greg Jensen — same file (quote: "the big thing bonds diversify against our major deflations and disinflations. But if you believe there if there's a disinflation, they're going to just push on fiscal. They don't they don't hedge as well.")
- Type: hedge | conflict/caveat
- Rule as testable logic: IF stock-bond correlation (in tool) > 0 OR debt/GDP > 100% and deficit > 5% GDP (proposed) THEN cap long-Treasury hedge weight (e.g. ≤ 20%, proposed) and substitute gold / T-bills / managed-futures trend as the hedge. Supports tool's existing TLT-only-when-corr<0 logic.
- Data needed: stock-bond correlation (in tool); FRED GFDEGDQ188S (1966), FYFSGDA188S. Debt ratio not in tool.
- Confidence: high.

### Competition for capital (fiscal + AI capex) pushes real rates up
- Source: Greg Jensen — same file (quote: "you're going to have this big competition for capital between fiscal and AI ... problems for real rates")
- Type: regime map
- Rule as testable logic: IF federal deficit % GDP > 5% AND hyperscaler/info-processing capex growth > 20% y/y (proposed) THEN expect rising real 10y (TIPS) yields; underweight long duration (TLT, TIP long) and favor T-bills/short duration.
- Data needed: FRED DFII10 (2003; in tool as real 10y level), FYFSGDA188S; BEA info-processing investment (Y033RC1Q027SBEA). Capex series not in tool.
- Confidence: medium.

### Private credit absorbing AI financing — credit risk watch
- Source: Greg Jensen — same file (quote: "they need a lot of money you're seeing that in private credit and that's going to be sucking in money")
- Type: signal (low specificity)
- Rule as testable logic: IF BDC/private-credit index (BIZD) underperforms HY bonds (HYG) by >10% over 6 months (proposed) THEN treat as credit stress early warning; trim equities / high-yield.
- Data needed: BIZD (2013), HYG (2007). Not in tool (tool has junk vs Treasuries, Baa spread).
- Confidence: low.

### Global diversification to survive many worlds (anti-US-concentration)
- Source: Greg Jensen — same file (quote: "how do we survive in the wide range of possible worlds rather than try to pick the best thing"; "Most people have moved away from diversification because it hasn't worked for 15 years... I think it's mostly a trap.")
- Type: position sizing/risk
- Rule as testable logic: Baseline portfolio = globally diversified (US + ex-US equities + bonds + gold + commodities, risk-balanced) rather than US-only; IF US share of world market cap > 60% (proposed) THEN cap US equity at world-cap weight minus 10 pts. Test vs SPY-only on max drawdown and Sharpe.
- Data needed: US share of MSCI ACWI (MSCI factsheets; proxy SPY/ACWI cap ratio), world equity indexes. Not in tool.
- Confidence: high.

### Capital concentration in US equity and illiquid assets = risky setup
- Source: Greg Jensen — same file (quote: "capital is more concentrated in the US than ever, more concentrated in equity and illquid assets. Um so a kind of risky setup")
- Type: signal
- Rule as testable logic: IF household equity share (in tool) in top decile AND foreign holdings of US equities / US market cap at record (proposed) THEN lower expected US equity return; overweight ex-US.
- Data needed: household equity share (in tool); Fed Z.1 rest-of-world holdings of US corporate equities (FRED BOGZ1LM263064105Q, 1945). Foreign holdings not in tool.
- Confidence: medium.

### Europe: fiscal turn favors domestic-company profits; shareholder-friendlier; cheap vs US peers
- Source: Greg Jensen — same file (quote: "fiscal policy works in the profits of domestic companies ... if you look at companies that directly compete between Europe and the US, they're generally priced cheap")
- Type: action/instrument
- Rule as testable logic: IF Euro-area structural deficit expands >1% GDP y/y (proposed) AND Europe forward P/E discount to US > 30% (proposed) THEN overweight Europe (VGK/EZU; Germany EWG) vs SPY for 12–24 months.
- Data needed: MSCI Europe vs US P/E (MSCI; proxy Shiller CAPE by country from Research Affiliates/Barclays, or Star Capital), Eurostat/IMF deficit; VGK (2005), EZU (2000), EWG (1996). Not in tool.
- Confidence: medium.

### China: policy pivot to private sector/AI → own for diversification
- Source: Greg Jensen — same file (quote: "Look, I think China is really important to global diversification... they need the equity market to function to do it they know it and you've seen the shift there")
- Type: action/instrument | conflict/caveat
- Rule as testable logic: IF China policy turns pro-private-sector (proxy: China tech KWEB/MCHI 6m return > 0 and above 10-month average, proposed) THEN hold a strategic China weight (MCHI/FXI at ≥ MSCI ACWI weight); caveat: biggest risk is home-government restriction (US investor ban), so size small.
- Data needed: MSCI China (MCHI 2011, FXI 2004; MSCI China index 1993). Not in tool.
- Confidence: medium.

### Bonds have a place again because real yields rose
- Source: Greg Jensen — same file (quote: "interest rates have risen and real interest rates have risen such that there is a place for bonds in portfolios")
- Type: action/instrument
- Rule as testable logic: IF real 10y yield (in tool) > 1.5% (proposed) THEN allow a strategic allocation to Treasuries/TIPS (e.g. 20–30%); IF < 0.5% THEN minimal duration.
- Data needed: DFII10 (in tool, 2003; pre-2003 proxy 10y minus 12m core CPI).
- Confidence: medium.

### Bitcoin as partial gold substitute (low conviction)
- Source: Greg Jensen — same file (quote: "if you don't trust governments and such having a way to move money around the world, Bitcoin is obviously the best choice. It is a replacement in some ways to gold although in many ways it's not")
- Type: conflict/caveat
- Rule as testable logic: No standalone rule; IF trust-erosion regime (gold rule above) THEN small optional BTC sleeve ≤ 2% (proposed). Note: he calls crypto a magnet for corruption/bubble — low allocation.
- Data needed: BTC-USD (2014 Yahoo; 2010 CoinMetrics). Not in tool.
- Confidence: low.

### AI is not yet a bubble but in a "more dangerous" resource-grab phase
- Source: Greg Jensen — same file (quote: "I still don't think we're in a bubble, but we are in a more dangerous phase ... we're in the resource grab phase now")
- Type: regime map | conflict/caveat
- Rule as testable logic: IF chips vs 12m high (in tool) strong AND power/utilities (XLU) and semis (SMH) both outperform SPY over 12 months while hyperscaler free cash flow turns negative/near zero (proposed proxy: tech sector debt issuance surge) THEN "resource-grab phase": keep sector exposure but tighten risk (smaller weight, trend stop). Contrast with tool's rally-speed/narrow-leadership warnings.
- Data needed: SMH (2000), XLU (1998), chips vs 12m high (in tool). Tech capex/FCF not in tool.
- Confidence: low.

### Divided Fed/new chair outvoted → policy uncertainty
- Source: Greg Jensen — same file (quote: "for a while you're going to have this very divided Fed and where the chairman may be in the minority")
- Type: conflict/caveat
- Rule as testable logic: IF FOMC dissents ≥ 2 per meeting for 2+ meetings (proposed) THEN raise term-premium expectation: underweight long Treasuries vs bills.
- Data needed: FOMC dissent counts (Fed website; St. Louis Fed has history from 1936). Term premium change in tool.
- Confidence: low.

### Home bias everywhere as reaction to US bullying
- Source: Greg Jensen — same file (quote: "You're seeing home bias everywhere as a reaction to this. I think you will see more of that.")
- Type: regime map
- Rule as testable logic: IF foreign net purchases of US long-term securities (TIC) turn negative over 6 months (proposed) THEN expect USD weakness and US underperformance vs ex-US: underweight USD (long FXE/FXY/UDN), overweight ex-US equities.
- Data needed: Treasury TIC net foreign purchases (monthly, 1977; FRED has partial). Not in tool.
- Confidence: medium.

---

## File 2: Stanley Druckenmiller — Sohn 2022 (conversation with John Collison)

### Inflation >5% never tamed without Fed funds above CPI
- Source: Stanley Druckenmiller — Sohn 2022 ... Druckenmiller.txt (quote: "once inflation gets above 5%, it's never come down unless uh Fed funds have gotten above the CPI")
- Type: signal | regime map
- Rule as testable logic: IF CPI y/y > 5% AND Fed funds < CPI y/y THEN inflation regime persists: underweight long nominal Treasuries and equities, overweight commodities/short duration; exit when Fed funds ≥ CPI y/y. (He himself expected the first rule to be violated in 2022-23 — test it.)
- Data needed: CPIAUCSL (1947), FEDFUNDS (1954). Both in tool separately; real policy rate (FF − CPI) not.
- Confidence: high.

### Inflation >5% → recession follows
- Source: Stanley Druckenmiller — same file (quote: "once inflation's got above 5%, to use your word, it's never been tamed without a recession")
- Type: signal
- Rule as testable logic: IF CPI y/y crosses above 5% THEN probability of NBER recession within 24 months high; reduce equities (e.g. 50% cap, proposed) once a growth warning (unemployment rise or S&P below 10m avg) confirms, for up to 24 months.
- Data needed: CPIAUCSL, USREC (NBER 1854). CPI in tool.
- Confidence: high.

### No soft landing after inflation above 4.5%
- Source: Stanley Druckenmiller — same file (quote: "we've never had a soft landing after inflation's gotten above 4 and 1/2%")
- Type: signal
- Rule as testable logic: IF CPI y/y peak in cycle > 4.5% AND Fed is hiking THEN do not treat the first equity rebound as all-clear; keep stock cap until unemployment peaks or Fed starts cutting (proposed).
- Data needed: CPI, Fed funds (in tool).
- Confidence: high.

### Bear markets after asset bubbles last longer than 6 months; fade 15–20% rallies
- Source: Stanley Druckenmiller — same file (quote: "if the market were to rally 15 to 20% from here over the intermediate term, I'm going to take a shot because 6-month bear markets preceded by asset bubbles don't exist historically")
- Type: re-entry/exit | signal
- Rule as testable logic: IF S&P 500 in drawdown >20% from peak within the last 6 months AND prior valuation extreme (CAPE or market cap/GDP top decile, in tool) THEN a 15–20% rally from the low is a re-short / de-risk point, not a re-entry, until the bear is ≥ 12 months old (proposed) or the Fed eases.
- Data needed: S&P 500 (Shiller 1871), CAPE (in tool), market cap/GDP (in tool).
- Confidence: high.

### Leading industries lead the economy by 6–12 months (housing, trucking, retail)
- Source: Stanley Druckenmiller — same file (quote: "stocks tend to lead the fundamentals by somewhere between 6 and 12 months ... if the leading industries are turning up or turning down, that's a signal")
- Type: signal
- Rule as testable logic: IF homebuilders (ITB/XHB) AND trucking (IYT or truckers sub-index) AND retail (XRT) are each > 40% below 52-week high (his examples: 50%, 40%) OR all three underperform SPY over 6 months THEN growth slowdown expected in 6–12 months: cut cyclicals, lower equity weight. Reverse (all three turning up from lows) = early-cycle buy signal. Tool has homebuilders vs market, transports vs industrials; retail missing.
- Data needed: ITB (2006), XHB (2006), XRT (2006), IYT (2003); Ken French 49-industry portfolios (housing-related Constr/BldMt, Trans, Rtail) from 1926. Retail not in tool.
- Confidence: high.

### Retail weaker than GDP = early warning
- Source: Stanley Druckenmiller — same file (quote: "retail appears to be much weaker than it should be given what the so-called GDP numbers are printing")
- Type: signal
- Rule as testable logic: IF retail stocks (XRT / French Rtail) 6m relative to SPY < −10% (proposed) WHILE real GDP growth > 2% THEN early recession warning (6–12m lead): reduce equities 25% (proposed).
- Data needed: XRT, French Rtail industry; GDPC1. Not in tool.
- Confidence: medium.

### Bond market as signal only when not manipulated by QE
- Source: Stanley Druckenmiller — same file (quote: "the bond market has not signaled anything because the central banks took it upon themselves to manipulate bond prices")
- Type: conflict/caveat
- Rule as testable logic: IF Fed balance sheet growth > 10% y/y (QE active, proposed) THEN down-weight bond-based signals (yield curve, 10y change) in the warning count; up-weight equity-industry signals.
- Data needed: FRED WALCL (2002), pre-2002 BOGMBASE/total reserves. Fed net liquidity in tool (3m change) but not as a signal-weighting switch.
- Confidence: high.

### "Price action vs news" (weakened)
- Source: Stanley Druckenmiller — same file (quote: "if the economy looked great and bonds were rallying that meant the economy was not going to look so great. We used to call it price action versus news")
- Type: signal | conflict/caveat
- Rule as testable logic: IF macro surprise index positive (strong data) AND 10y yield falls over 1 month (proposed) THEN growth slowdown ahead (overweight duration). He says this tool has weakened since the 2000s — test by sub-period (pre/post 2008).
- Data needed: Citi Economic Surprise Index (not free; proxy: change in ISM/payrolls vs consensus — no free consensus; proxy ISM new orders change), 10y (in tool). Not in tool.
- Confidence: medium.

### Oil up + rates up + dollar up → earnings fall ~35%; buy Treasuries
- Source: Stanley Druckenmiller — same file (quote: "if you have oil, interest rates, he he plugged in the percentages, and the dollar up this amount, earnings the next year forward based on history go down 35%")
- Type: signal | action/instrument
- Rule as testable logic: IF oil 12m change, 10y yield 12m change and dollar 12m change are all strongly positive (tool's "oil+rates+dollar squeeze") THEN expect forward EPS decline; long 10y Treasuries (he went 350% of fund in 10y equivalents) and underweight equities for 6–12 months, especially when Fed has a tightening bias that should reverse.
- Data needed: in tool (squeeze). Add S&P forward EPS (Shiller earnings 1871) for validation.
- Confidence: high.

### Bear market playbook: take equities off, buy Treasuries — except when inflation high and yields low
- Source: Stanley Druckenmiller — same file (quote: "I've never present been presented a cocktail where you have 8% inflation, you think the economy might weaken and bond yields 3%")
- Type: hedge | conflict/caveat
- Rule as testable logic: IF bear market AND CPI y/y > 10y yield (negative real yield) THEN Treasuries are NOT the hedge: use T-bills/short duration + commodities; IF CPI < 10y yield (positive real) THEN Treasuries are the bear-market hedge. Directly testable alongside tool's stock-bond correlation switch.
- Data needed: CPI, 10y yield (DGS10/GS10 1953), both in tool.
- Confidence: high.

### Inflationary bear matrix: short fixed income, short stocks, long oil/copper
- Source: Stanley Druckenmiller — same file (quote: "a matrix of short fixed income short stocks and not doing a whole lot in currencies and owning some of the key commodities particularly oil and mistakenly gold but copper")
- Type: action/instrument | regime map
- Rule as testable logic: IF stagflation-early regime (CPI y/y > 5% and rising, Fed behind curve: FF < CPI) THEN short long Treasuries (TBF/TBT or underweight TLT), underweight equities (SH), long oil (USO/DBO) and copper (CPER); gold did not work in 2022 ("mistakenly gold").
- Data needed: oil (WTI FRED DCOILWTICO 1986; MCOILWTICO 1946), copper (World Bank 1960; FRED PCOPPUSDM 1990), gold. Oil/copper changes in tool; instruments not.
- Confidence: medium.

### Reduce shorts once front-end data weakens
- Source: Stanley Druckenmiller — same file (quote: "we're now getting definitive signals that the economy may be weakening particularly at the front end ... much less comfortable being short fixed income")
- Type: re-entry/exit
- Rule as testable logic: IF in short-duration position AND leading growth indicators turn down (e.g. 3+ of tool's growth warnings fire) THEN cover duration shorts (go neutral, not long, until inflation falls).
- Data needed: in tool (growth warnings).
- Confidence: medium.

### Short the dollar after the "first to tighten" inflow peaks
- Source: Stanley Druckenmiller — same file (quote: "I will be surprised if sometime in the next 6 months I'm not short the dollar. 14 trillion dollars has come in here because we were the first to tighten")
- Type: signal | action/instrument
- Rule as testable logic: IF dollar index at/near 12m high (in tool) AND Fed hiking cycle mature (FF 12m change > 2 pts) AND other central banks start catching up (G10 ex-US policy rates rising faster than US over 6m, proposed) THEN short USD (UDN, long FXE/FXY) and overweight ex-US/EM equities for 6–12 months.
- Data needed: DXY/broad dollar (FRED DTWEXBGS 2006, TWEXB 1973), foreign policy rates (BIS policy rates, 1946+). Dollar vs 12m high in tool; foreign rates not.
- Confidence: medium.

### Energy long for 5–10 years (ESG underinvestment); exit on demand destruction
- Source: Stanley Druckenmiller — same file (quote: "the energy, because of the transition to ESG, we look to be short energy for 5 or 10 years" and "we're looking for demand destruction in energy, but so far we don't see it")
- Type: action/instrument | re-entry/exit
- Rule as testable logic: IF energy capex/upstream investment depressed (proposed: oil rig count < 10y average) AND oil above 10-month average THEN overweight energy (XLE/XOP) and oil; EXIT when demand destruction appears (US gasoline/petroleum product supplied y/y < −3%, proposed) or worldwide recession signal.
- Data needed: Baker Hughes rig count (1987 weekly; free), EIA product supplied (WRPUPUS2, 1990s weekly), XLE (1998). Not in tool.
- Confidence: medium.

### Bitcoin in inflationary bull; gold in inflationary bear/stagflation
- Source: Stanley Druckenmiller — same file (quote: "if it's in a bull phase, you want to own Bitcoin. But if it's in a bear phase for other assets, you want to own gold")
- Type: regime map | action/instrument
- Rule as testable logic: IF inflation regime (CPI y/y > 3%, proposed) AND S&P above 10-month average THEN inflation hedge = BTC; IF inflation regime AND S&P below 10-month average (stagflation bear) THEN inflation hedge = gold.
- Data needed: BTC (2010/2014), gold, S&P 10m avg (in tool).
- Confidence: medium (explicitly "85% what I've observed").

### Crypto as Nasdaq-correlated risk indicator
- Source: Stanley Druckenmiller — same file (quote: "there certainly seems to be a strong correlation between crypto and the Nasdaq ... I'm looking at it as an indicator that way")
- Type: signal
- Rule as testable logic: IF BTC falls > 40% from 6m high (proposed) THEN speculative-liquidity warning: reduce growth/Nasdaq exposure (QQQ) for 3 months. Test lead/lag BTC vs QQQ.
- Data needed: BTC-USD, QQQ (1999). Not in tool.
- Confidence: low.

### Position sizing: concentrate on conviction; hot/cold streak scaling
- Source: Stanley Druckenmiller — same file (quote: "sizing is probably 70 to 80% of the equation ... when I'm hot, I'm supposed to turn the dial way up ... when you're cold ... you should tone yourself down")
- Type: position sizing/risk
- Rule as testable logic: Scale gross exposure by the strategy's own trailing performance: IF strategy trailing 6m return > its long-run median (proposed) THEN size up (e.g. 1.25×); IF trailing 6m drawdown > 10% (proposed) THEN size down (0.5×) — "don't trade a lot when you're down". Also: only take large positions when multiple signals align ("fat pitch"); otherwise stay small/flat.
- Data needed: the tool's own return series. N/A.
- Confidence: high (core stated principle).

### Take a break after a large drawdown
- Source: Stanley Druckenmiller — same file (quote: "one of my trading rules is you don't trade a lot when you're down")
- Type: position sizing/risk
- Rule as testable logic: IF strategy drawdown > 15% (proposed; his were 16–18%) THEN cut to minimum risk for 1–3 months before re-engaging.
- Data needed: own P&L.
- Confidence: medium.

### Invest the change, 18–24 months ahead, not the present
- Source: Stanley Druckenmiller — same file (quote: "Do not invest in the present. The present is not what moves stock prices. Change moves them.")
- Type: signal (general)
- Rule as testable logic: Use rates of change (6–12m changes, accelerations) rather than levels for all signals; test level vs change versions of each tool indicator.
- Data needed: existing series.
- Confidence: high.

### Countercyclical: buy cyclicals when losing money, sell when over-earning
- Source: Stanley Druckenmiller — same file (quote: "when companies are losing money, capacity is always going to shrink and their margins going to look better in 3 years. When companies are over earning, their margins are going to come down")
- Type: signal | action/instrument
- Rule as testable logic: IF a cyclical sector's (chemicals, shipping, trucking, retail, energy) earnings margin is in the bottom quintile of its 20y history THEN overweight that sector ETF for 2–3 years; top quintile (over-earning) THEN underweight. Sector-ETF version (XLB, XLE, IYT, XRT).
- Data needed: sector earnings/margins (Ken French industry book-to-market as proxy; S&P sector EPS not free). Not in tool.
- Confidence: medium.

### Post-bubble outcome range: 1966–82 sideways or Japan 1989 deflation
- Source: Stanley Druckenmiller — same file (quote: "it could be just no growth and sideways for 15 or 20 years, like '66 to '82 in terms of the markets, or it could be something more pernicious like we had in Japan")
- Type: regime map | conflict/caveat
- Rule as testable logic: IF market cap/GDP or CAPE top 5% historically AND central-bank balance sheet expansion then reversal (QT) THEN lower equity long-run expected return; favor trend-following overlay and real assets. Every deflation followed an asset bubble — keep some long-duration hedge ("70% inflation / 30% deflation").
- Data needed: CAPE, market cap/GDP (in tool); Japan Nikkei (Yahoo ^N225 1965).
- Confidence: medium.

### Ignore 13F as timing data
- Source: Stanley Druckenmiller — same file (quote: "People looking at 13 Fs, by the way, which I would caution against because that's old data")
- Type: conflict/caveat
- Rule as testable logic: N/A for the macro tool (relevant to triage owner cells: 13F lag).
- Data needed: N/A.
- Confidence: high.

### Never bet against America (long term)
- Source: Stanley Druckenmiller — same file (quote: "Warren Buffett and Ken Langone ... say never bet against America ... that has always been true over the long term")
- Type: conflict/caveat
- Rule as testable logic: Default long US equities over long horizons; bearish overlays should be time-limited (re-entry rules mandatory).
- Data needed: N/A.
- Confidence: medium.

---

## File 3: Ray Dalio — Five Forces Shaping the Global Economy (Money Maze Podcast, 2023-11-02)

### Currency devaluation (break from hard money) → stocks up
- Source: Ray Dalio — Five Forces Shaping the Global Economy ... Ray Dalio.txt (quote: "I thought that everything was going to collapse because money as we knew it was ending it was exact opposite the stock market went up a lot")
- Type: signal | regime map
- Rule as testable logic: IF a country devalues / abandons a peg or its trade-weighted currency falls > 15% in 6 months via policy (proposed) THEN its domestic-currency equity index rises in the following 6–12 months (buy local equities in local currency, hedge FX) and gold rises. Test on events: US 1933, 1971; UK 1992; Mexico 1994; Asia 1997; Brazil 1999; Argentina 2002; Japan 2013 (Abenomics); Egypt 2016/2024.
- Data needed: FX (FRED DEX* 1971; BIS effective exchange rates 1964), MSCI country indexes in local currency (MSCI 1970/1988), gold. Not in tool.
- Confidence: medium (stated as mechanism he learned: "I understood the mechanic").

### Devaluation plus inflation shock → stocks down (1973)
- Source: Ray Dalio — same file (quote: "they devalue the dollar and stocks go down we have this inflationary and I came out in 1973 ... same year as the oil crisis")
- Type: conflict/caveat
- Rule as testable logic: The devaluation-is-bullish rule fails when followed by an inflation/oil shock: IF devaluation AND oil 6m change > +50% or CPI accelerating > 2 pts in 12m (proposed) THEN equities underperform; prefer commodities/gold.
- Data needed: oil 6m change (in tool), CPI (in tool).
- Confidence: medium.

### Tight US money + EM dollar debt → EM default; but the default marked the equity bottom
- Source: Ray Dalio — same file (quote: "with the tightness of monetary policy that existed that those countries would not be able to pay back those debts" ... "August 1982 um was the exact bottom in the stock market")
- Type: signal | conflict/caveat
- Rule as testable logic: (a) IF US real policy rate > 2% (FF − CPI, proposed) AND dollar rising (12m change > 10%, proposed) THEN underweight EM equities/EM dollar bonds (EEM/EMB) — EM debt-service squeeze. (b) Caveat: once the crisis/default event occurs AND the Fed begins easing, the equity bottom is near — re-enter US equities (do not extrapolate the crisis).
- Data needed: FEDFUNDS, CPI (in tool), dollar 12m change (in tool); EEM (2003), EMB (2007), MSCI EM (1988), JPM EMBI (not free; proxy EMB). EM not in tool.
- Confidence: medium.

### Diversify across ~15 uncorrelated return streams (cuts risk up to 80%)
- Source: Ray Dalio — same file (quote: "if I could take good bets winning bets that were uncorrelated and diversify well that I could eliminate up to 80% of my risk without diminishing my expected returns")
- Type: position sizing/risk
- Rule as testable logic: Build the tool's portfolio as risk-balanced sleeves (US equities, ex-US equities, nominal Treasuries, TIPS, gold, commodities, trend) with inverse-volatility weights; test vs 100/0 stock/cash switching on Sharpe and max drawdown. Keep pairwise correlations < 0.3 (proposed) as a design check.
- Data needed: ETF/index returns for each sleeve. Not in tool.
- Confidence: high.

### Debt service squeezes spending; holders sell debt when real return < inflation
- Source: Ray Dalio — same file (quote: "if you don't have a return in relation to inflation that is High Enough by holding that debt you won't hold that debt")
- Type: signal | regime map
- Rule as testable logic: IF real 10y yield (in tool) < 0 AND federal interest outlays / receipts rising (> 15%, proposed) THEN bonds are unattractive to holders: underweight long Treasuries, overweight gold/TIPS/T-bills, for 12 months.
- Data needed: real 10y (in tool), FRED A091RC1Q027SBEA (federal interest payments, 1947) / W006RC1Q027SBEA (federal receipts). Interest/receipts not in tool.
- Confidence: high.

### Debt-supply imbalance forces central bank choice: rates up a lot OR print
- Source: Ray Dalio — same file (quote: "what the central bank is forced to choose between is interest rates Rising a lot that curtail SS everything has very bad implications or coming in and printing a lot more money")
- Type: regime map
- Rule as testable logic: IF Treasury supply (deficit % GDP > 5%, proposed) exceeds demand (foreign + Fed holdings share of Treasuries falling, proposed) THEN two branches: (a) Fed not buying (QT) → yields rise: short duration, underweight equities; (b) Fed restarts QE → long gold/commodities/equities, short dollar. Switch on Fed balance sheet 3m change sign.
- Data needed: deficit (FRED FYFSGDA188S), Fed holdings of Treasuries (FRED TREAST 2002), foreign holdings (FRED FDHBFIN 1970). Fed net liquidity 3m change in tool; holdings shares not.
- Confidence: high.

### Central bank losses and QT add upward pressure on yields
- Source: Ray Dalio — same file (quote: "the central banks now inclination particularly like the FED to have the balance sheet roll off ... is going to exert upward pressure on rates")
- Type: signal
- Rule as testable logic: IF Fed balance sheet 12m change < −5% (QT, proposed) THEN underweight long Treasuries (TLT) vs T-bills; also tool's term premium 12m change should rise. Test TLT excess return conditional on QT periods (2018–19, 2022–25).
- Data needed: WALCL (2002); term premium (in tool, ACM/Kim-Wright).
- Confidence: high.

### Sanctions risk reduces foreign demand for US Treasuries
- Source: Ray Dalio — same file (quote: "there are sanctions and those sanctions means that it some countries believe it's risky to own particular us bonds because maybe they can get sanctioned")
- Type: regime map
- Rule as testable logic: IF foreign official holdings of Treasuries (custody holdings at NY Fed) fall y/y AND central-bank gold buying rises (proposed) THEN overweight gold vs Treasuries.
- Data needed: FRED WMTSECL1 (foreign official custody, 2002), WGC central-bank gold demand (quarterly, 2000). Not in tool.
- Confidence: medium.

### "Dollar cash" preferred when real cash yields are high
- Source: Ray Dalio — same file (interviewer quote: "explain exactly why it is you like dollar cash right now")
- Type: action/instrument
- Rule as testable logic: IF 3m T-bill yield − core CPI y/y > 1.5% (proposed) AND bond supply pressure high THEN hold T-bills (BIL/SGOV) in place of long Treasuries as the defensive asset.
- Data needed: FRED TB3MS (1934), core CPI (in tool).
- Confidence: low (attributed by interviewer).

### Country health screen: income vs spending, balance sheet, internal conflict, external war risk
- Source: Ray Dalio — same file (quote: "are you earning more than you are spending so that your income statement is good and your balance sheet is good places that have good savings and good financials will be better off")
- Type: regime map | action/instrument
- Rule as testable logic: Country allocation score = z(current account % GDP) + z(−govt debt % GDP) + z(national savings % GDP) − z(internal conflict/polarization) − z(external war risk). Overweight top-tercile countries' ETFs, underweight bottom tercile; rebalance annually; test 1990–present on MSCI country indexes in USD.
- Data needed: IMF WEO (current account, debt, savings; 1980), World Bank WGI political stability (1996), Geopolitical Risk Index by country (Caldara-Iacoviello, 1985 monthly, free), MSCI country indexes/iShares country ETFs (EWJ, EWY, EWZ, INDA, EWS, KSA, UAE, MCHI...). Not in tool.
- Confidence: high.

### Avoid places with big internal (left-right, wealth-gap) conflict
- Source: Ray Dalio — same file (quote: "history shows that you could lose more money money not just in price movements but you could be confiscated from you or taken from you")
- Type: signal | position sizing/risk
- Rule as testable logic: IF a country's political polarization/conflict index in top quintile (proposed) THEN cap that country's equity weight at half of benchmark. For US: IF partisan conflict index (Philadelphia Fed Partisan Conflict Index) rising strongly, raise risk premium / lower US weight.
- Data needed: Philadelphia Fed Partisan Conflict Index (1981 monthly, free; discontinued updates?); V-Dem polarization (annual); Gini (World Bank). Not in tool.
- Confidence: medium.

### Neutral countries outperform winners in great-power wars
- Source: Ray Dalio — same file (quote: "history has shown that that the neutral countries have done better than even the winning countries in Wars economically")
- Type: regime map | action/instrument
- Rule as testable logic: IF Geopolitical Risk Index (GPR) > 90th percentile (proposed) THEN overweight neutral/non-aligned markets (India INDA, Singapore EWS, Gulf UAE/KSA, ASEAN ASEA, Switzerland EWL) vs combatant-bloc markets (US, China, Taiwan EWT, Korea EWY near conflict). Dalio's stated favorites: ASEAN, Singapore, India, Gulf states.
- Data needed: Caldara-Iacoviello GPR (1900 annual / 1985 monthly, free), country ETFs (INDA 2012, EWS 1996, UAE 2014, KSA 2015, ASEA 2011, EWL 1996). Not in tool.
- Confidence: medium.

### US–China conflict near red lines (Taiwan, chips, sanctions on Chinese assets)
- Source: Ray Dalio — same file (quote: "we're also seeing the possibility of sanctioning their debt in other words like Russia" ; "the winner of a technology war is going to be the winner of this Global World Order war")
- Type: position sizing/risk | conflict/caveat
- Rule as testable logic: IF US–China tension index (GPR China-specific or tariff/export-control events) spikes THEN cap China (MCHI/FXI) and Taiwan (EWT) exposure (sanction/confiscation risk); favor neutral Asia. Contrasts with Jensen (China needed for diversification).
- Data needed: GPR country index (China, Taiwan), MCHI, EWT (2000). Not in tool.
- Confidence: medium.

### Climate/energy transition = 5–10% of GDP cost; underinvestment in old energy shrinks supply
- Source: Ray Dalio — same file (quote: "you don't invest in um the um old Technologies the old energy sources so you have less Supply in that period of time before it's uh replaced")
- Type: regime map
- Rule as testable logic: IF global upstream oil & gas capex / revenue in bottom quartile of its 20y range (proposed; proxy rig count) THEN expect structurally higher energy prices: overweight energy (XLE) and oil (DBO) in inflation regimes. Agrees with Druckenmiller's ESG-energy thesis.
- Data needed: Baker Hughes rig counts (1987), IEA upstream investment (annual). Not in tool.
- Confidence: medium.

### Deficit pressures structurally up (climate, infrastructure, education, defense)
- Source: Ray Dalio — same file (quote: "we're now in a world where they say well we have to spend money we have to spend money on climate we have to spend money on infrastructure")
- Type: regime map
- Rule as testable logic: IF projected deficit (CBO 10y baseline) rises between vintages (proposed) THEN term premium rises → underweight long Treasuries vs bills.
- Data needed: CBO baseline projections (annual, 1990s), term premium (in tool).
- Confidence: medium.

### Big debt cycle analog 1930–45 (debt monetization + internal conflict + great-power conflict)
- Source: Ray Dalio — same file (quote: "the amounts of debt creation and debt monetization that whole dynamic and last time that happened was in 1930 to 45 period")
- Type: regime map
- Rule as testable logic: Regime flag "late big debt cycle" IF govt debt/GDP > 100% AND central bank holds > 20% of govt debt (proposed) AND policy rates near zero or real rates negative THEN strategic allocation: gold ≥ 10%, TIPS over nominals, real assets, diversify geographically.
- Data needed: FRED GFDEGDQ188S, FDHBFRBN (Fed holdings of federal debt, 1970), real rates. Not in tool.
- Confidence: medium.

---

## File 4: Bob Prince — Co-CIO of Bridgewater (Generating Alpha Podcast Ep. 12, 2025-03-20)

### Strong dollar hurts US manufacturers / cyclicals
- Source: Bob Prince — Episode 12- Bob Prince ... .txt (quote: "growing up in Illinois near a caterpillar factory uh when the dollar was super strong like they were doing layoffs and they were getting hurt because the Japanese could undercut them")
- Type: signal
- Rule as testable logic: IF trade-weighted dollar 12m change > +10% (proposed) THEN underweight US industrials/exporters (XLI) vs domestic sectors / vs ex-US equities for 12 months. Tool already has dollar 12m change; the sector mapping is new.
- Data needed: dollar 12m change (in tool), XLI (1998) / French "Mach"/"Manuf" industries (1926).
- Confidence: medium (anecdotal).

### Oil-price swings whip oil-region economies
- Source: Bob Prince — same file (quote: "oil prices are high and to Tulsa had was like one of the top places ... 3% unemployment when Boston had an 18% ... all of a sudden oil prices go down and that everything flip-flops")
- Type: signal | action/instrument
- Rule as testable logic: Country/region version: IF oil 6m change < −30% (proposed) THEN underweight oil-exporter equity markets & currencies (Norway ENOR/NOK, Canada EWC/CAD, Brazil EWZ, Saudi KSA, Mexico EWW) vs oil importers (India INDA, Japan EWJ, Korea EWY); reverse when oil 6m change > +30%.
- Data needed: oil 6m change (in tool); country ETFs (EWC 1996, EWZ 2000, EWW 1996, ENOR 2012, EWJ 1996, EWY 2000, INDA 2012); MSCI country indexes 1988; FX (FRED). Country mapping not in tool.
- Confidence: medium.

### Hidden market bets: separate operating margin from market exposure
- Source: Bob Prince — same file (quote: "businesses are really comprised of two things. One is like an operating margin and the other is a bet on the markets")
- Type: position sizing/risk
- Rule as testable logic: For every sleeve, decompose return into beta to equities, rates, dollar, oil, gold (rolling 36m regression) and cap unintended exposure (e.g. country ETF's oil beta) at a set level (proposed |beta| ≤ 0.5). Design check, not a signal.
- Data needed: returns of sleeves and factor series.
- Confidence: medium.

### Very long duration as capital-efficient deflationary-depression hedge (Kodak mandate)
- Source: Bob Prince — same file (quote: "if we have a deflationary depression it everything's going to go down together ... a hund00 million in bonds with a 25-y year duration that I'll get the price action of $500 million")
- Type: hedge | position sizing/risk
- Rule as testable logic: Hedge sleeve = small weight in ultra-long duration (EDV/ZROZ, ~25y duration, or 2–2.5× levered 10y futures) instead of a large weight in intermediate bonds; hold it when deflation risk high (core CPI 3m < 12m and falling, unemployment rising — tool signals) and when stock-bond corr < 0; scale duration 0–40y by signal. Test EDV (2007) / 30y zero (Treasury STRIPS proxy from FRED DGS30 1977) vs TLT/IEF as hedge per unit capital.
- Data needed: FRED DGS30 (1977), GS20; EDV (2007), ZROZ (2009), TLT (2002). Ultra-long not in tool (tool uses TLT).
- Confidence: high.

### Duration and currency as active overlays (duration 0–40y, currency ±100%)
- Source: Bob Prince — same file (quote: "we could shift the duration from uh 40 years all the way down to zero ... We could move the currency plus or minus 100%. And we could do that in any at any point in the yield curve in any country")
- Type: action/instrument
- Rule as testable logic: Treat duration as a continuous dial driven by the tool's state (e.g. Contraction → 25–40y, Overheating/Stagflation → 0–2y) and currency hedge ratio of foreign holdings as a dial driven by dollar trend (dollar above 12m avg → hedge 100%; below → unhedged). Test on ex-US equity sleeve: hedged (HEFA) vs unhedged (EFA).
- Data needed: Treasury yield curve (FRED DGS1..DGS30), EFA/HEFA (2014), dollar (in tool).
- Confidence: medium.

### Interest-rate, stock and gold "systems" (systematic timing per asset)
- Source: Bob Prince — same file (quote: "Rey had built the first couple of, uh, he built an interest rate system, a stock system, and a gold system")
- Type: action/instrument
- Rule as testable logic: Add a dedicated gold timing model to the tool (e.g. long gold when real 10y yield 6m change < 0 OR dollar below 12m average; proposed) alongside stock and bond models.
- Data needed: gold, real yield (in tool), dollar (in tool).
- Confidence: low (no rule given, only existence).

### German defense spending → unintended European fiscal stimulus
- Source: Bob Prince — same file (quote: "Germany has come through with a big defense uh u initiative which is primarily for defense ... that that's now turning into a very positive for the European economy because it's fiscal stimulation")
- Type: signal | action/instrument
- Rule as testable logic: IF German/EU fiscal impulse (change in structural primary balance) > +1% GDP (proposed) THEN overweight European equities (EWG, EZU, VGK) and European defense/industrials for 12–24 months. Agrees with Jensen.
- Data needed: IMF/Eurostat fiscal balance, EWG (1996), EZU (2000), defense ETF (EUAD 2024; ITA US 2006). Not in tool.
- Confidence: medium.

### Stability vs geopolitical chaos: balance achieved, now threatened by modern mercantilism
- Source: Bob Prince — same file (quote: "policy makers have managed to finally kind of bring things into a reasonable balance. And just as they're achieving this reasonable balance ... you now have this geopolitical chaos")
- Type: regime map
- Rule as testable logic: IF the macro state is "balanced" (inflation near 2–3%, unemployment stable, Fed neutral) BUT GPR or trade-policy uncertainty index > 90th percentile (proposed) THEN keep equity exposure but add tail hedges (gold, long-dated puts, see Graham panel) rather than cutting.
- Data needed: Baker-Bloom-Davis Trade Policy Uncertainty (1985 monthly, free), GPR. Not in tool.
- Confidence: low.

### Modern mercantilism: China has done it successfully; Europe lags (no central government)
- Source: Bob Prince — same file (quote: "if you look at China, China's been doing that for a while actually pretty successfully ... Europe is really sort of left behind because they don't really have a central government")
- Type: regime map | conflict/caveat
- Rule as testable logic: No direct trading rule; qualitative support for a "mercantilist regime" flag (tariffs rising, industrial policy) → favour countries with strong state capacity; partially conflicts with his own Europe-positive fiscal point.
- Data needed: tariff rates (WTO/World Bank), N/A.
- Confidence: low.

---

## File 5: BG2 Thanksgiving Roundtable — Brad Gerstner & Bill Gurley (Bg2 Pod, 2024-11-27)

Note: mostly policy/venture talk; few market rules. Extracted what is testable.

### Fiscal-reform rally in EM (Argentina/Milei)
- Source: Bill Gurley — BG2 Thanksgiving Roundtable ... .txt (quote: "if you look at the Argentinian ETF argt it's up 60% year-to date 65 which suggests the optimism around Argentina's economy has has has reversed")
- Type: signal | action/instrument
- Rule as testable logic: IF an EM country with a fiscal/inflation crisis delivers a credible fiscal adjustment (primary balance improves > 3% GDP within 12 months, proposed) THEN overweight that country's equity ETF (ARGT, EWZ, TUR, EGPT...) for the next 12 months. Event-study test on IMF primary-balance improvements 1990–present.
- Data needed: IMF WEO primary balance (1980), MSCI country indexes / ETFs (ARGT 2011, EWZ 2000, TUR 2008). Not in tool.
- Confidence: low (single anecdote).

### US fiscal consolidation path (spending back to trend) as bond-positive scenario
- Source: Brad Gerstner — same file (quote: "if you reduced spending for the next four years bill at 3% it simply gets us back to 6 trillion which is exactly the trend line")
- Type: regime map
- Rule as testable logic: IF federal outlays y/y growth < revenue growth for 4+ quarters (deficit shrinking, proposed) THEN term premium falls: overweight long Treasuries vs bills; reverse when deficit widens outside recessions. Counterpart to Jensen/Dalio/Tropin deficit-risk rules.
- Data needed: FRED FGEXPND (federal expenditures, 1947), FGRECPT (receipts, 1947), term premium (in tool).
- Confidence: low (advocacy, not a trading rule).

### Tariffs as negotiating anchor: "loaded but rarely discharged"
- Source: Brad Gerstner — same file (quote: "the Tariff gun will be loaded but rarely discharged" (quoting Bessent); "treat them as effective negotiating tactics not as literary flourishes")
- Type: conflict/caveat | re-entry/exit
- Rule as testable logic: IF equities sell off > 10% on a tariff announcement (proposed) AND the announced tariff has a negotiation condition/deadline THEN treat as re-entry opportunity once the effective tariff rate (customs duties/imports) fails to rise as much as announced within 3 months. Contrast with Jensen/Zulauf (tariffs = durable regime change).
- Data needed: effective tariff rate (customs duties FRED B235RC1Q027SBEA / imports), Trade Policy Uncertainty Index (Baker-Bloom-Davis, 1985). Not in tool.
- Confidence: low.

### China tech catching up despite export controls
- Source: Bill Gurley — same file (quote: "I don't think blocking asml or blocking AI technology or blocking anything is working it's just not working")
- Type: conflict/caveat
- Rule as testable logic: Caveat against a permanent China underweight: IF China tech (KWEB/CQQQ) outperforms SOXX over 6 months (proposed) THEN allow China tech exposure in the country sleeve. Conflicts with Dalio's sanction/containment caution.
- Data needed: KWEB (2013), CQQQ (2009), SOXX (2001). Not in tool.
- Confidence: low.

### Gas-price spike kills big-vehicle sales
- Source: Bill Gurley — same file (quote: "when gas prices spiked in 2009 uh uh big SUV sales went in the tank")
- Type: signal
- Rule as testable logic: IF retail gasoline price 6m change > +30% (proposed) THEN expect auto sales (in tool: car sales 6m) to fall; underweight autos/consumer discretionary (XLY, CARZ) vs staples for 6 months. (Spike was 2008.)
- Data needed: FRED GASREGW (1990), car sales (in tool), XLY (1998).
- Confidence: low.

### Oligopoly margins in US payments threatened by public instant-payment rails
- Source: Bill Gurley — same file (quote: "Visa and MasterCard have the two highest operating margin percentages in our markets total like they're over 60%")
- Type: conflict/caveat
- Rule as testable logic: Not a macro index rule (single-stock/sector); note only. Possible sector test: payments sector ETF (IPAY) relative performance after FedNow consumer rollout. Out of scope (no single stocks).
- Data needed: IPAY (2015). Not in tool.
- Confidence: low.

---

## File 6: Graham Capital 2022 Virtual Investment Symposium — Discretionary Strategies Panel (Pablo Calderini, Kelly (Katie) Dropping Woodridge, Peter Chapson, David Keelan, Chris McCann; recorded Sept 2022)

### Fed reaction function regime: low inflation = quick to ease/slow to tighten (Fed put); high inflation = put struck far lower
- Source: Kelly (Graham chief economist) and David Keelan — Graham's 2022 ... Discretionary Strategies Panel.txt (quotes: "made them really kind of slow to ease quick uh sorry quick to ease low to tighten and kind of made that fed put a feature of monetary policy"; "there is a fed put but it's it struck so far down that we're not quite sure where that is yet")
- Type: regime map | re-entry/exit
- Rule as testable logic: IF core inflation (core PCE/CPI y/y) < 2.5% THEN "Fed put on": buy equity dips (drawdown > 10%) with 6m horizon; IF core inflation > 3.5% (proposed) THEN "Fed put off": do not buy dips on pivot hopes; require trend confirmation (S&P back above 10-month average) before re-entry. Test dip-buying returns conditional on inflation regime.
- Data needed: core CPI (in tool), S&P 10m average (in tool). Regime-conditional dip rule not in tool.
- Confidence: high.

### Stock-bond correlation turned positive; 60/40 and risk parity broken in inflation
- Source: Peter Chapson — same file (quote: "the 64 60 40 portfolio the death of that you know the you know the negative correlation between stocks and bonds ... that's gone")
- Type: hedge | regime map
- Rule as testable logic: IF stock-bond correlation (in tool) > 0 AND core inflation > 3% THEN bonds are not a hedge; replace with USD cash / long dollar / trend-following. Confirms tool's TLT-only-if-corr<0 rule.
- Data needed: in tool.
- Confidence: high.

### 2022 tightening playbook: long dollar, short rates, short equities ("short risk parity")
- Source: David Keelan / Peter Chapson — same file (quote: "it's obviously this year long the dollar short rates short equities um has been the trade to be in")
- Type: action/instrument | regime map
- Rule as testable logic: IF core inflation > 4% AND Fed funds 12m change > +2 pts (aggressive tightening) AND stock-bond corr > 0 THEN: long USD (UUP), short/underweight Treasuries (TBF or T-bills only), underweight equities (SH) until Fed funds 3m change ≤ 0 or core inflation 3m < 12m.
- Data needed: UUP (2007; DXY futures earlier, FRED DTWEXB 1973), Fed funds (in tool), core inflation 3m vs 12m (in tool).
- Confidence: medium.

### Bear-market rallies are vicious when sentiment is dire
- Source: David Keelan — same file (quote: "the bear Market rallies are so vicious and we did see a summer rally where stocks had a 20 bounce off the lows and at the same time 10-year notes rally I think 75 basis points")
- Type: re-entry/exit | position sizing/risk
- Rule as testable logic: IF in a de-risked state AND sentiment extreme bearish (AAII bull-bear spread < −30, proposed, or VIX > 35) THEN do not add new shorts; cut short exposure by half (snapback risk) — not a re-entry by itself. Agrees with Druckenmiller ("short side ... head ripped off in rallies").
- Data needed: AAII sentiment (weekly, 1987, free download), VIX (in tool, 1990; VXO 1986).
- Confidence: medium.

### Reshoring/nearshoring supports Mexican peso despite high carry
- Source: David Keelan — same file (quote: "Mexican peso even with tremendous carries appreciated as as um you had like I guess they call it kind of reshoring type stuff from you know out of the East back to North America")
- Type: action/instrument
- Rule as testable logic: IF MXN carry (Banxico rate − Fed funds) > 4 pts (proposed) AND USD/MXN below its 12m average THEN long MXN (FXM discontinued; proxy: long Mexico EWW unhedged or MXN futures) for 6 months. General EM carry rule: long high-carry EM FX when trend agrees and VIX < 25 (proposed).
- Data needed: FRED DEXMXUS (1993), Banxico policy rate (BIS, 2008), Fed funds; EWW (1996). Not in tool.
- Confidence: medium.

### Japan: inflation rising under yield-curve control → JGB yields/yen pressure
- Source: David Keelan / Peter Chapson — same file (quote: "Japan for instance they just put up 30-year High inflation last night ... why are they doing yield curve control and you can see the markets trying to test them")
- Type: signal | action/instrument
- Rule as testable logic: IF Japan core CPI y/y > 2% AND BoJ policy rate ≤ 0 / YCC binding (10y JGB at the cap) THEN expect JGB yield rise and later yen rebound: short JGBs (via JGB futures; no retail ETF), or long yen (FXY) once BoJ shifts; meanwhile yen weak (short FXY) while US–Japan rate gap widens. Test: FXY 6m return vs change in US–Japan 2y spread.
- Data needed: Japan CPI (FRED JPNCPIALLMINMEI, 1955), JGB 10y (FRED IRLTLT01JPM156N, 1989), USD/JPY (FRED DEXJPUS, 1971), FXY (2007), EWJ (1996). Not in tool.
- Confidence: medium.

### Europe tightening into recession because of energy shock
- Source: Kelly (Graham economist) — same file (quote: "we're seeing those central banks having to tighten into recessions which is something you know again going back to this idea of central banks previously being able to accommodate downside risks")
- Type: regime map
- Rule as testable logic: IF European natural gas price 6m change > +100% (proposed) AND ECB hiking THEN underweight European equities (VGK/EZU) and EUR (FXE) vs US for 6 months; IF gas falls > 50% from peak THEN reverse (cold-winter risk resolved).
- Data needed: TTF gas (World Bank Pink Sheet "Natural gas, Europe", monthly 1960s), ECB rate (FRED ECBDFR 1999), VGK, FXE (2005). Not in tool.
- Confidence: medium.

### Terminal rate surprises up when inflation entrenched (services, core goods sticky)
- Source: Kelly (Graham economist) — same file (quote: "if we start with the Baseline view that we think inflation is going to remain entrenched we think that that means that the FED has a lot more work to do")
- Type: signal
- Rule as testable logic: IF core services inflation 3m annualized > 12m rate AND > 4% (proposed) THEN market-implied terminal rate too low: short front-end (hold T-bills / short 2y via SHV vs SHY), avoid duration for 3–6 months.
- Data needed: CPI services less energy (FRED CUSR0000SASLE, 1957), 2y yield (DGS2, 1976). Core inflation 3m vs 12m in tool; services split not.
- Confidence: medium.

### Global liquidity tightening (QT) is bad for risk assets; both stocks and bonds fall
- Source: Peter Chapson — same file (quote: "I think liquidity is going to keep tightening globally I think it's bad for risk assets ... I think stocks and bonds sell off")
- Type: signal
- Rule as testable logic: IF combined central-bank balance sheets (Fed + ECB + BoJ, USD) 6m change < 0 (proposed) THEN underweight equities AND long bonds simultaneously; hold T-bills/USD. Extends tool's Fed net liquidity to global.
- Data needed: FRED WALCL (2002), ECBASSETSW (1999), JPNASSETS (1998), FX rates. Fed net liquidity in tool; global not.
- Confidence: medium.

### QT and real yields: at what level do central banks flinch?
- Source: David Keelan — same file (quote: "does do real yields keep going because we're uh shrinking our balance sheet larger than we really ever have ... at what point do do yields maybe get too high where central banks you know might Flinch")
- Type: re-entry/exit | conflict/caveat
- Rule as testable logic: IF real 10y yield (in tool) rises > 1.5 pts in 12 months (proposed) AND financial stress (Baa spread 6m change > +1 pt, in tool) THEN expect central-bank flinch (pause/QT end): start adding duration (TLT) and reduce dollar longs.
- Data needed: real 10y and Baa spread (both in tool).
- Confidence: low.

### Size positions in volatility units; smaller when vol is high
- Source: Peter Chapson — same file (quote: "you size or positions and ball units so and and Chris said this earlier you know and higher it falls higher your emotional size is smaller")
- Type: position sizing/risk
- Rule as testable logic: Position weight = target risk / trailing 60-day realized volatility (proposed target 10% annualized per sleeve); cap leverage at 1.5× (proposed). Test vs fixed weights.
- Data needed: daily returns of each instrument.
- Confidence: high.

### Stress tests > VaR when correlations are unstable; watch gap risk
- Source: Chris McCann — same file (quote: "unstable correlations so that makes sort of the value of a statistic like VAR a little bit less valuable it makes statistics like stress tests more valuable")
- Type: position sizing/risk
- Rule as testable logic: Risk budget check: portfolio loss in historical stress scenarios (1987, 2008, 2020, 2022) must be < 20% (proposed) — overrides vol-based sizing when correlations spike (cross-asset corr > 0.5, proposed).
- Data needed: historical returns of sleeves.
- Confidence: high.

### Cross-asset "one trade" risk: shrink the book into central-bank events
- Source: David Keelan / Chris McCann — same file (quote: "you could be in the dollar rates and equities but it's all the same trade ... the idea of shrinking the book so you are still making a big bet but you're not making a triple size bet on an outcome of a meeting")
- Type: position sizing/risk
- Rule as testable logic: IF rolling 3m correlation among the tool's active positions (e.g. long USD, short bonds, short equities) > 0.6 (proposed) THEN scale total risk so the combined position counts as one bet (divide by sqrt of effective number of bets); reduce gross by 30% (proposed) in the week of FOMC meetings when positions are event-driven.
- Data needed: FOMC calendar (Fed website, 1936), position returns.
- Confidence: medium.

### Prefer liquid instruments; liquidity is poor in high-vol regimes
- Source: Peter Chapson — same file (quote: "I'm more liquid things because liquidity in the markets are terrible and so some trades you just might not take")
- Type: position sizing/risk
- Rule as testable logic: Universe filter: only instruments with average daily dollar volume > $50m (proposed) (e.g. SPY, TLT, GLD, EEM, EWZ, EWY, FXI, USO, UUP); in VIX > 30 regimes, restrict to the top-liquidity tier.
- Data needed: ETF volumes (Yahoo).
- Confidence: medium.

### Sentiment factor: overbought sold together, oversold bought together
- Source: Peter Chapson — same file (quote: "there is a factor that's I would call a sentiment Factor so sometimes things get correlated everything that's overbought gets sold and everything that's open sold gets bought")
- Type: signal | position sizing/risk
- Rule as testable logic: IF an asset's 1m return > +2 s.d. (overbought) during a de-risking episode (VIX up > 30% in a week, proposed) THEN expect mean reversion; avoid adding to recent winners during risk-off shocks. Cross-asset short-term reversal test.
- Data needed: daily ETF prices.
- Confidence: low.

### Scale down into events, react afterwards
- Source: Chris McCann — same file (quote: "portfolio managers especially this year where there are a lot of opportunities to react have been tending to scale down into events and then reacting to what happens")
- Type: position sizing/risk
- Rule as testable logic: Rebalance timing: do not change tool allocations on FOMC/CPI release days; implement signals the day after the event (test 1-day delay vs same-day execution).
- Data needed: event calendar.
- Confidence: medium.

### Conviction-based sizing: high theme clarity → higher risk; PM correlation up = higher information ratio
- Source: Pablo Calderini / Chris McCann — same file (quote: "in times of the higher correlation we actually have a higher information ratio among our PMS however they also tend to be times of higher volatility")
- Type: position sizing/risk
- Rule as testable logic: IF most of the tool's independent indicator families agree (e.g. ≥ 70% of warnings in same direction, proposed) THEN allow larger tilts (full 0/100 switch); IF mixed THEN partial tilts (e.g. 50/50). Mirrors Druckenmiller "fat pitch".
- Data needed: tool's indicators.
- Confidence: medium.

### Post-2010 suppressed volatility was the anomaly; expect pre-2010 vol norms
- Source: Pablo Calderini — same file (quote: "I think it's time that we start seeing the 2010-20 period as an anomaly a period that will very unlikely come back")
- Type: regime map | conflict/caveat
- Rule as testable logic: Backtests should weight pre-2010 data at least equally; calibrate thresholds on 1970–2009 and check 2010–20 separately (overfitting guard). QE brings down vol: IF Fed balance sheet growing > 10% y/y THEN expect lower VIX — signals based on VIX levels must be regime-adjusted.
- Data needed: VIX (in tool), WALCL.
- Confidence: medium.

### Fed responds to University of Michigan inflation expectations
- Source: Peter Chapson — same file (quote: "the FED height texture in response to a higher than expected Universe University of Michigan uh um inflation expectations survey")
- Type: signal
- Rule as testable logic: IF UMich 5–10y inflation expectations rise > 0.3 pt in 3 months (proposed) THEN Fed hawkish surprise risk: underweight 2y Treasuries/duration for 3 months.
- Data needed: UMich 5-10y expectations (FRED MICH is 1y, 1978; 5–10y from UMich site, 1990). Tool has 5y market expectations (breakevens), not survey.
- Confidence: low.

### Governments subsidize prices (fiscal offsets) while central banks tighten
- Source: Peter Chapson — same file (quote: "then you have governments that what are they doing they're actually spending more money to help people afford higher prices so it's kind of like a Back to the Future moment")
- Type: regime map
- Rule as testable logic: IF fiscal impulse positive (deficit widening outside recession) WHILE central bank is hiking THEN inflation more persistent; extend underweight duration/overweight commodities.
- Data needed: deficit (FRED FYFSGDA188S/MTSDS133FMS), Fed funds (in tool).
- Confidence: medium.

---

## File 7: Kenneth Tropin — Graham Capital (iConnections, 2025-06-17)

### Central-bank activity count as macro opportunity gauge
- Source: Kenneth Tropin — Why Macro Investing Matters More Than Ever ... .txt (quote: "There were only 13, 25 basis point rate moves between those three central banks and 11 years and in the subsequent 36 months there have been 60")
- Type: regime map
- Rule as testable logic: IF number of 25bp policy-rate moves by Fed+ECB+BoE over the past 12 months > 8 (proposed) THEN allocate to macro/trend sleeve (DBMF/KMLM or a simple time-series momentum model on futures-proxy ETFs) and widen the tool's tilt sizes; IF < 3 THEN favor buy-and-hold beta.
- Data needed: FRED FEDFUNDS/DFEDTARU, ECBDFR, BoE Bank Rate (BoE database, 1694); trend sleeve proxy: SG Trend Index (not free), DBMF (2019), or own TSMOM on ETFs (1990s). Not in tool.
- Confidence: medium.

### Stocks expensive + bonds scary (record deficit) → diversify into macro/trend
- Source: Kenneth Tropin — same file (quote: "we're in an environment where stocks are really expensive and bonds are kind of scary")
- Type: hedge | regime map
- Rule as testable logic: IF CAPE (in tool) top decile AND deficit % GDP > 5% outside recession (proposed) THEN replace part of the bond hedge with a trend-following sleeve (e.g. 20%, proposed). Test trend sleeve vs TLT as equity hedge in 1970s/2022-type regimes.
- Data needed: CAPE (in tool), deficit (FRED FYFSGDA188S), trend returns (own TSMOM on futures-proxy series; AQR TSMOM factor data 1985 free, Hurst-Ooi-Pedersen century data 1880).
- Confidence: medium.

### Macro/trend went short in extended declines (crisis alpha 1987, 2000–03, 2008, 2022)
- Source: Kenneth Tropin — same file (quote: "If markets have some kind of extended decline, we're going to go short")
- Type: hedge
- Rule as testable logic: Add a 12-month time-series momentum rule per asset (long if 12m excess return > 0, else short/flat) across equity indexes, bonds, FX, commodities; evaluate as hedge: correlation to SPY in SPY's worst 10% of quarters should be negative.
- Data needed: AQR TSMOM factor (1985), ETF/futures proxies.
- Confidence: high.

### Trend-following suffers in fast policy reversals; short-horizon models do better
- Source: Kenneth Tropin — same file (quote: "in an environment such as we've seen in the last 6 or 8 weeks, where the policies of the current administration have been really volatile ... It's tough for a medium term time horizon")
- Type: conflict/caveat | position sizing/risk
- Rule as testable logic: IF policy-uncertainty index (Economic Policy Uncertainty or Trade Policy Uncertainty) > 95th percentile (proposed) THEN shorten trend lookbacks (e.g. 1–3 months instead of 12) or cut trend sleeve weight by half; restore when uncertainty normalizes.
- Data needed: Baker-Bloom-Davis EPU (1985 monthly; FRED USEPUINDXM) and TPU. Not in tool.
- Confidence: medium.

### Combine price trend with carry, value/yield and relative value
- Source: Kenneth Tropin — same file (quote: "quant strategies that are not just based on price, but also that are based on fundamentals, things that look at, yield and carry, relative value, all of these things are complementary")
- Type: action/instrument
- Rule as testable logic: Cross-asset sleeve ranks instruments (country equity indexes, bonds, FX, commodities) on trend (12m momentum) + carry (dividend yield/earnings yield minus cash; bond yield minus cash; FX rate differential; commodity futures roll yield) + value (5y reversal / CAPE); long top third, underweight bottom third. Test vs trend alone.
- Data needed: country CAPE/dividend yields (MSCI / Research Affiliates), yields (FRED/OECD), FX rates, commodity roll (futures curves; Bloomberg not free — proxy ETF vs spot gap). Not in tool.
- Confidence: medium.

### Tariffs are inflationary → Fed cannot be dovish; new chair (Warsh) not a dove
- Source: Kenneth Tropin — same file (quote: "The fed, right, knows that these tariffs are inflationary. So they can't really be as dovish as they'd like to be")
- Type: signal | conflict/caveat
- Rule as testable logic: IF effective tariff rate up > 3 pts y/y (proposed) THEN discount market-priced rate cuts: underweight 2y Treasuries vs bills, avoid long duration for 6–12 months. Conflicts with Jensen (political Fed lowering real rates).
- Data needed: customs duties / imports (FRED), 2y yield (DGS2).
- Confidence: medium.

### Bond-market "canary": no term premium for 25 years; deficit + foreign holders may spook bonds
- Source: Kenneth Tropin — same file (quote: "for 25 years, there's been no premium for taking duration, risk ... the canary in the room to watch is, is the bond market")
- Type: signal | hedge
- Rule as testable logic: IF term premium (ACM 10y, in tool as 12m change) rises > 1 pt in 12 months OR 10y yield rises while Fed is cutting (proposed) THEN "bond scare": underweight long Treasuries (TLT) AND equities (bond scare spills to stocks), hold T-bills/gold/trend. Analog 1980 (yields 8% → 20%).
- Data needed: ACM term premium (NY Fed, 1961), Fed funds (in tool), foreign holdings of Treasuries (FRED FDHBFIN).
- Confidence: high.

### Record valuations + unstable geopolitics = asymmetric downside
- Source: Kenneth Tropin — same file (quote: "valuations in equities or record highs as we sit here today ... if you look at the geopolitical situation, it's never been more unstable in my opinion")
- Type: signal
- Rule as testable logic: IF CAPE top decile AND GPR > 80th percentile (proposed) THEN hold a tail hedge (e.g. 1–2% annual budget for 3-month 10% OTM SPY puts, or long VIX calls) rather than cutting equities outright.
- Data needed: CAPE (in tool), GPR (1985), option prices (CBOE PUT index 1986 as proxy for put-writing; SPY options data not free — proxy via CBOE PPUT 5% put protection index, 1986). Not in tool.
- Confidence: low.

### Policy chaos will calm before midterms
- Source: Kenneth Tropin — same file (quote: "you got the midterm elections coming up in a year. It's inconceivable to me that we're going to have the administration ignore everything")
- Type: regime map
- Rule as testable logic: IF within 12 months before US midterm elections THEN expect policy volatility (EPU) to decline; restore medium-term trend lookbacks. Presidential-cycle test: S&P and EPU in midterm year vs others.
- Data needed: EPU (1985), election calendar.
- Confidence: low.

### Macro is negatively correlated to equities "two thirds to three quarters" of bad equity periods — not always
- Source: Kenneth Tropin — same file (quote: "We have about two thirds of three quarters of the time. But definitely there's some times where we've been exposed")
- Type: conflict/caveat | hedge
- Rule as testable logic: Hedge sleeve design should not assume trend always hedges; size it so that a failure (trend loses while equities fall) costs < 5% of portfolio (proposed).
- Data needed: trend sleeve returns.
- Confidence: high.

---

## File 8: Felix Zulauf — Zulauf Consulting (Generating Alpha Podcast Ep. 15, 2025-04-10)

### Top-down chain: zeitgeist pendulum → business cycle (with intervention distortions) → rates, currencies, capital flows → bonds/equities/sectors/FX hedge/commodities
- Source: Felix Zulauf — Episode 15- Felix Zulauf ... .txt (quote: "you analyze the business cycle, a classic business cycle um analysis ... you deviate what it means for interest rates for currencies for capital flows ... whether you want to be uh in more defensive groups or ... deep cyclical groups")
- Type: regime map
- Rule as testable logic: Map tool state → sector tilt (defensives vs deep cyclicals), currency hedge decision, commodity weight: Expansion → deep cyclicals (XLB, XLI, XLE) + commodities, unhedged foreign; Contraction → defensives (XLP, XLU, XLV) + bonds, hedge foreign FX. Already partly in tool (sector calls); add currency-hedge and commodity dials.
- Data needed: sector ETFs (1998), Ken French industries (1926), FX.
- Confidence: medium.

### End of globalization / WTO → trade then capital flows are the key variable; reserve-currency role of USD and US rates change
- Source: Felix Zulauf — same file (quote: "the next one issue will probably be capital flows ... it is changing uh the importance and relevance of uh the US dollar as a reserve currency and uh this is changing capital flows and this capital flow will change in principle the level of interest rates in the US")
- Type: regime map | signal
- Rule as testable logic: IF foreign net purchases of US long-term securities (TIC) 12m sum falls > 50% from its 3y average (proposed) OR USD share of global FX reserves (IMF COFER) falls > 1 pt y/y THEN expect higher US long yields and weaker USD: underweight TLT, overweight gold and ex-US (unhedged) assets for 12 months. Agrees with Jensen (home bias), Dalio (sanctions).
- Data needed: Treasury TIC (1977 monthly), IMF COFER (quarterly 1995/1999). Not in tool.
- Confidence: medium.

### Sold commodity equities at 1980 commodity peak: 70% cash, 30% bonds
- Source: Felix Zulauf — same file (quote: "I took over a fund for commodity related investments ... at the peak of the commodity boom in 1980 ... So I went to 70% cash and 30% in bonds of um commodity companies")
- Type: re-entry/exit | action/instrument
- Rule as testable logic: IF commodity index 12m change > +50% (proposed) AND real policy rate turns positive / Fed tightening hard (Volcker-type: FF 12m change > +3 pts) THEN exit commodities and commodity equities (DBC, XLE, GDX, XME) to cash/short bonds of the sector; i.e., commodity booms end when real rates spike.
- Data needed: World Bank commodity price index (1960 monthly), CRB/BCOM (BCOM 1960 back-filled; free proxy DBC 2006, GSG 2006), Fed funds (in tool), CPI.
- Confidence: medium (single episode but clearly a call based on cycle).

### Sold all institutional equity before the 1987 crash
- Source: Felix Zulauf — same file (quote: "after 87 uh which was the crash of 87 where I sold all the institutional accounts down to zero equities before it happened")
- Type: signal (no mechanism stated)
- Rule as testable logic: No explicit indicator given; test 1987 setup as candidate rule: IF 10y yield 6m change > +1.5 pts AND equity earnings yield − 10y yield < −2 pts (Fed model gap, proposed) AND dollar falling THEN cut equities to 0. (Rule proposed from the known 1987 setup, not stated by him.)
- Data needed: DGS10 (1962), S&P earnings yield (Shiller 1871), dollar (in tool).
- Confidence: low.

### Weekly multi-timeframe technical review of ~1000 charts to confirm/falsify the thesis
- Source: Felix Zulauf — same file (quote: "I use technical analysis to support my analysis or to tell me whether I'm wrong or not ... on a long-term, medium-term and short-term basis")
- Type: re-entry/exit | conflict/caveat
- Rule as testable logic: Fundamental (macro-state) signal acts only when the instrument's own trend agrees on at least 2 of 3 horizons (e.g. price above 40-week, 13-week, 4-week averages; proposed); where the market "does not agree", stay neutral and re-examine. Test macro signal alone vs macro + trend confirmation.
- Data needed: price series of each instrument.
- Confidence: high.

### Market breadth / "health of the trend"
- Source: Felix Zulauf — same file (quote: "analyzing the health of the market, the health of a trend etc.")
- Type: signal
- Rule as testable logic: IF index makes a new 12m high while % of constituent sectors/countries above their 10-month average < 50% (proposed) THEN unhealthy trend: reduce exposure 25%. Tool has industries-in-uptrend breadth; extend to world country breadth (share of MSCI country indexes above 10m average).
- Data needed: country ETFs / MSCI country indexes (1970/1988). Industry breadth in tool; country breadth not.
- Confidence: medium.

### Mandatory fail-safe stop-loss
- Source: Felix Zulauf — same file (quote: "You have to have stop losses in place ... there is a fail-safe stop-loss that you have to have in place otherwise you know when you lose big it kills you psychologically")
- Type: position sizing/risk
- Rule as testable logic: Every directional tilt (e.g. country, commodity, short) has a hard stop: exit if position loses > 15% from entry (proposed) or the instrument closes below its 10-month average for longs (above for shorts); re-entry only on a fresh signal. His worst loss without a stop: −50%.
- Data needed: price series.
- Confidence: high.

### Only trade when odds turn in your favor (high-conviction-only)
- Source: Felix Zulauf — same file (quote: "I do only enter a position when I have a strong conviction ... I only play when I see that the odds are turning in my favor. Uh other than that, I leave it")
- Type: position sizing/risk
- Rule as testable logic: Default = neutral benchmark; active tilts only when composite score exceeds a high threshold (e.g. top/bottom 20% of its history, proposed). Agrees with Druckenmiller fat-pitch and Graham conviction sizing.
- Data needed: tool composite score.
- Confidence: high.

### Long cycles: bull markets favor young bulls; structural bear conditioning
- Source: Felix Zulauf — same file (quote: "when you have a bull market you should not use a 60 or 55 year old portfolio manager because they are conditioned by the previous structural bare market")
- Type: conflict/caveat
- Rule as testable logic: Guard against bear bias: in secular bull regimes (S&P above its 10-year moving average and 10y yield trending down, proposed) require stronger evidence (more warnings) before cutting equities. Echoes Druckenmiller's self-declared bearish bias.
- Data needed: S&P (Shiller), 10y yield.
- Confidence: medium.

### Contrarian at extremes: bearish at the top is lonely
- Source: Felix Zulauf — same file (quote: "at the top with a bearish view, you are very lonely ... you have virtually nobody to speak to")
- Type: signal
- Rule as testable logic: IF investor sentiment extreme bullish (AAII bull-bear spread > +30, or household equity share top decile — in tool) THEN contrarian lean bearish, but act only with technical confirmation (see multi-timeframe rule).
- Data needed: AAII (1987), household equity share (in tool).
- Confidence: medium.

### Currency-hedge decision is part of every allocation
- Source: Felix Zulauf — same file (quote: "and in what currency you want you want to be whether you have to hedge the currency or or not")
- Type: action/instrument
- Rule as testable logic: For ex-US holdings: hedge FX (HEFA, DBEF, HEWJ) when USD is above its 12m average and rate differential favors USD; unhedged otherwise. Test EFA vs HEFA switching.
- Data needed: EFA (2001), HEFA (2014), DBEF (2011), DXY.
- Confidence: medium.

---

## Cross-speaker contradictions and agreements

- **China exposure**: Jensen (China "really important to global diversification", policy now pro-private-sector) and Gurley (export controls not working, China out-innovating) vs Dalio (sanction/confiscation risk near red lines; prefer neutral countries). Testable: China weight conditional on GPR-China and on China's own trend.
- **Fed direction under political pressure**: Jensen (populist control of the Fed → lower real rates into a boom → inflation) vs Tropin (tariffs make the Fed unable to be dovish; Warsh "no dove"). Both imply underweight long duration, but differ on front end (Jensen: cuts; Tropin: fewer cuts).
- **Tariffs**: Jensen, Prince, Zulauf: durable regime change (modern mercantilism, end of WTO globalization) vs Gerstner: negotiating anchor, "loaded but rarely discharged" (fade tariff-shock sell-offs).
- **Bonds as hedge**: Druckenmiller (Treasuries were always his bear-market tool, not in 2022), Graham panel (60/40 dead while inflation high), Jensen (bonds hedge less when fiscal is the lever; though real yields now give them "a place"), Tropin (bond market is the canary) vs Prince (ultra-long duration is the capital-efficient deflationary-depression hedge). Reconciliation to test: duration as hedge only when inflation low/stock-bond corr < 0 (tool already does this) and use ultra-long rather than more TLT.
- **Fiscal consolidation**: Gerstner (balanced budget by 2029 doable, positive) vs Dalio/Jensen (spending pressures structural: defense, climate, AI capital competition).
- **Inflation forecast**: Druckenmiller 2022 (once >5%, recession inevitable; expected Fed funds rule to be violated) vs Graham panel 2022 (entrenched inflation, terminal rate surprises up). Outcome (2023–24: no NBER recession) is a test of the ">5% → recession" rule.
- **Bitcoin**: Druckenmiller (own BTC in inflationary bull, gold in inflationary bear) vs Jensen (BTC partly a gold substitute but corruption-heavy, not helpful technology).
- **Energy**: Druckenmiller and Dalio agree — underinvestment (ESG/transition) supports energy for years.
- **Europe**: Jensen and Prince agree — German/European defense-fiscal turn is positive for European domestic earnings.
- **Sizing**: Druckenmiller (concentrate, hot/cold streaks, cut when down), Zulauf (only high-conviction, mandatory stops), Graham (vol-unit sizing, shrink into events, correlation = one trade), Dalio/Jensen (diversify across many uncorrelated bets, survive). Dalio/Jensen diversification vs Druckenmiller concentration is the core contrast.
- **Bear-market behavior**: Druckenmiller (fade 15–20% rallies in post-bubble bear < 6 months old) and Graham (rallies vicious when sentiment dire → don't add shorts) agree on caution with shorts; Dalio's 1982 lesson (crisis/default = bottom) warns against extrapolating the bear.

---

## Batch summary

Top 10 testable ideas from this batch:

1. **Inflation regime switch for the hedge asset** (Druckenmiller, Graham panel, Jensen): IF CPI y/y > 10y yield or stock-bond corr > 0 → hedge with T-bills/USD/commodities/trend, not Treasuries; IF real yields positive and corr < 0 → Treasuries (ultra-long per Prince). Extends the tool's current TLT-vs-bills switch with USD, trend and EDV options.
2. **"Inflation > 5% persists until Fed funds > CPI"** and **"> 5% → recession within 24m"** (Druckenmiller): real policy rate (FF − CPI) as a regime variable for duration, equities and commodities.
3. **Leading-industry composite** (Druckenmiller): homebuilders + trucking + retail each ≥ 40% off highs or all lagging SPY over 6m → slowdown in 6–12 months; reverse on joint upturn. Adds retail (missing from tool).
4. **Fiscal-space asymmetry for countries** (Jensen, Dalio): big fiscal expansion in countries with room (surplus, low debt, high savings) → long currency + equities; in constrained countries (UK/Brazil-type) → short currency and long bonds. Plus a "US fiscal constraint" flag: 10y up and USD down in the same month on deficit news → cut duration, add gold.
5. **Country health/neutrality screen** (Dalio): current account, debt, savings, internal conflict, war risk → overweight healthy/neutral countries (India, Singapore, ASEAN, Gulf, Switzerland), especially when GPR is high.
6. **Bond-scare canary** (Tropin, Dalio, Graham): term premium +1 pt in 12m, QT, or 10y rising while Fed cuts → underweight both TLT and equities; hold T-bills/gold/trend. Flinch point: real 10y +1.5 pts plus credit stress → add duration back.
7. **Time-series trend + carry + value cross-asset sleeve** (Tropin, Zulauf technical confirmation): add a TSMOM sleeve as crisis hedge; require instrument's own trend to agree with macro signals; shorten lookbacks when policy uncertainty is extreme.
8. **Oil-exporter vs oil-importer country rotation** (Prince; Druckenmiller energy thesis): oil 6m ±30% → rotate EWC/EWZ/ENOR/KSA/EWW vs INDA/EWJ/EWY; energy overweight while rig counts depressed, exit on demand destruction.
9. **Fed-put regime for dip-buying** (Graham panel, Druckenmiller): buy 10% drawdowns only when core inflation < 2.5%; when > 3.5%, wait for trend confirmation; in post-bubble bears < 6m old, treat 15–20% rallies as de-risk points.
10. **Risk/sizing rules** (Druckenmiller, Zulauf, Graham, Dalio): vol-unit sizing; conviction-scaled tilts only when indicator families agree; hard stop (15%/trend break) on every tilt; cut risk after a strategy drawdown > 15%; treat correlated positions as one bet; implement the day after FOMC/CPI events; diversify across uncorrelated sleeves (inverse-vol).

Also notable: devaluation → local equities up unless followed by oil/inflation shock (Dalio); USD short after the "first to tighten" inflow peaks (Druckenmiller); BTC vs gold as inflation hedge by bull/bear regime (Druckenmiller); global QT (Fed+ECB+BoJ) as risk-asset warning (Graham); Europe overweight on fiscal impulse + valuation discount (Jensen, Prince); US vs ex-US relative-momentum rotation and capital-flow/TIC signals (Jensen, Zulauf); Japan inflation under YCC → yen/JGB trades (Graham); MXN nearshoring carry (Graham); commodity booms end when real rates spike (Zulauf 1980).

---

## Data requests (series NOT in the existing tool list)

Equities / countries / sectors
- MSCI ACWI ex-US / EAFE / EM total return (EFA 2001, VEU 2007, ACWX 2008, EEM 2003; MSCI history 1970/1988); US share of ACWI market cap.
- Equal-weight S&P 500 (RSP 2003).
- MSCI country indexes / iShares country ETFs: EWG, EZU, VGK, EWJ, EWY, EWZ, EWW, EWC, ENOR, EWS, EWL, EWT, INDA, MCHI, FXI, KWEB/CQQQ, KSA, UAE, ASEA, ARGT, TUR (1996–2015 starts; MSCI 1970/1988).
- Currency-hedged ex-US equity (HEFA 2014, DBEF 2011, HEWJ).
- Retail stocks (XRT 2006; Ken French 49-industry "Rtail" 1926); homebuilders ITB/XHB; trucking/transport IYT; industrials XLI; energy XLE/XOP; utilities XLU; semis SMH/SOXX; consumer discretionary XLY; defense ITA; payments IPAY.
- Country CAPE / dividend yield / forward P/E (Research Affiliates, Star Capital, MSCI factsheets).
- Shiller S&P earnings (1871) for EPS validation; Fed-model gap.
- World country breadth (share of country indexes above 10-month average).
- BDC/private-credit index (BIZD 2013) vs HYG.

Rates / fiscal / central banks
- 3m T-bill (TB3MS 1934), 2y (DGS2 1976), 30y (DGS30 1977), ultra-long duration ETFs (EDV 2007, ZROZ 2009), TIPS (TIP 2003), short-duration (SHV/SHY/BIL/SGOV), inverse Treasury (TBF/TBT).
- Real policy rate FF − CPI (computed).
- Federal deficit % GDP (FYFSGDA188S 1929; monthly MTSDS133FMS), outlays/receipts (FGEXPND, FGRECPT 1947), federal interest payments (A091RC1Q027SBEA 1947), debt/GDP (GFDEGDQ188S 1966), Fed holdings of federal debt (FDHBFRBN 1970; TREAST 2002), CBO baseline vintages.
- Foreign holdings of Treasuries (FDHBFIN 1970), foreign official custody (WMTSECL1 2002), Treasury TIC net foreign purchases (1977), IMF COFER USD reserve share (1995/1999), rest-of-world holdings of US equities (Z.1 BOGZ1LM263064105Q 1945).
- Central-bank balance sheets: WALCL (2002, pre-2002 proxies), ECB (ECBASSETSW 1999), BoJ (JPNASSETS 1998).
- Policy rates abroad: ECB (ECBDFR 1999), BoE Bank Rate (BoE), BoJ, Banxico (BIS policy-rate database 1946+); count of 25bp moves by Fed+ECB+BoE.
- FOMC dissent counts and meeting calendar.
- ACM term premium (in tool as 12m change; need level, 1961).
- Foreign 10y yields (OECD IRLTLT01xxM156N, e.g. UK, Japan, Germany, Brazil; 1960/1989).
- IMF WEO: general government debt, primary balance, current account % GDP, gross national savings (1980); Eurostat/IMF structural balance (fiscal impulse).

Inflation / growth
- Core PCE (PCEPILFE 1959), CPI services less energy (CUSR0000SASLE 1957), Japan CPI (JPNCPIALLMINMEI 1955).
- UMich 5–10y inflation expectations (1990; MICH 1y 1978).
- 10y breakeven (T10YIE 2003) — gap vs realized core inflation.
- Real GDP (GDPC1), info-processing equipment + software investment (Y033RC1Q027SBEA, B985RC1Q027SBEA).
- Defense spending (FDEFX 1947; SIPRI 1949 for Europe).
- Effective tariff rate: customs duties (B235RC1Q027SBEA 1947) / goods imports (IMPGS).
- NBER recession dates (USREC 1854).
- Retail gasoline (GASREGW 1990).
- EIA petroleum product supplied (demand destruction, WRPUPUS2 1990s); Baker Hughes rig count (1987).

Commodities / FX / alternatives
- Gold (World Bank Pink Sheet 1960 / LBMA; GLD 2004), central-bank gold demand (WGC 2000).
- WTI (MCOILWTICO 1946), copper (PCOPPUSDM 1990 / World Bank 1960), European natural gas TTF (World Bank Pink Sheet), broad commodity index (World Bank index 1960; DBC/GSG 2006), oil ETFs (USO/DBO), copper ETF (CPER 2011), gold miners (GDX), metals (XME).
- FX: DXY/broad dollar (DTWEXBGS 2006, TWEXB 1973), UUP (2007), UDN, FXE (2005), FXY (2007), FXB, BZF, USD/MXN (DEXMXUS 1993), USD/JPY (DEXJPUS 1971), USD/GBP (DEXUSUK 1971), BIS effective exchange rates (1964).
- Bitcoin (BTC-USD 2010/2014).
- Trend-following / managed-futures returns: AQR TSMOM factor (1985), Hurst-Ooi-Pedersen century data, DBMF (2019), KMLM (2020).
- CBOE put-protection index PPUT (1986) / option data for tail hedges.

Sentiment / uncertainty / geopolitics
- AAII bull-bear sentiment (1987).
- Economic Policy Uncertainty (USEPUINDXM 1985) and Trade Policy Uncertainty (Baker-Bloom-Davis, 1985).
- Caldara-Iacoviello Geopolitical Risk Index, global and by country (1900 annual / 1985 monthly).
- Philadelphia Fed Partisan Conflict Index (1981); V-Dem polarization; World Bank WGI political stability (1996).
- Macro surprise proxy (Citi ESI not free; proxy ISM new orders change).
