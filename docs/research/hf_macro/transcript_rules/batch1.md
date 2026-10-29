# Batch 1: testable rules from macro transcripts

Files (9): Cullen Roche (TIP486); Kyle Bass (Hoover); Jeffrey Hirsch (Eisman Playbook Ep 56); Druckenmiller with Sokoloff (Sohn 2023); Mike Pompeo; Ajay Banga (NBIM In Good Company); Pablo Calderini (New World Order); Pablo Calderini (Resilient Strategies / Left-Tail); "What is the fiscal rule?".

Notation: "(proposed)" = threshold not given by speaker. "In tool" = already among the 43 Macro Compass indicators.

---

## File 1: Cullen Roche, "Macro Investing - Understanding How And Why w- Cullen Roche (TIP486)" (Oct 2022)

### Starting bond yield sets forward bond return
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "bonds operate a lot like stocks in the sense that when interest rates rise, the prices fall, their future returns become better")
- Type: signal
- Rule as testable logic: IF the 5y/10y Treasury yield is in the top third of its trailing 20y range or above 4% (proposed) THEN overweight intermediate Treasuries (IEF/5-7y) vs T-bills for the next 3-5 years; IF yield < 1.5% (proposed) THEN underweight duration (hold bills). Test: forward 5y annualized return of a constant-maturity 5y/10y index vs starting yield (expected slope ~1).
- Data needed: 5y and 10y CMT yields (FRED DGS5, DGS10, from 1962); Treasury total-return proxies (IEF from 2002, VFITX from 1991; or build from yields). 10y yield level partly in tool (10y 12m change, real 10y).
- Confidence: high

### Coupon cushion against rate rises (breakeven yield rise)
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "if that bond, let's say you buy it and it's starting at 10% rate, well that bond has to lose the equivalent of two years, basically worth of principle")
- Type: position sizing/risk
- Rule as testable logic: Breakeven = yield / duration. IF breakeven 1-year yield rise (yield/duration) > 0.75 pp (proposed) THEN duration is acceptable as the defensive leg; IF < 0.25 pp (near-zero yields) THEN replace long Treasuries with T-bills in the de-risk sleeve. Test against the current TLT-vs-bills choice.
- Data needed: yields by maturity (FRED DGS2/5/10/30), modified duration (computed from yield and maturity). Not in tool as such.
- Confidence: high

### Zero-rate asymmetry: avoid duration at the zero bound
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "when interest rates are at zero, your interest rate risk is just, it is completely different than when interest rates are starting at four")
- Type: conflict/caveat
- Rule as testable logic: IF Fed funds < 0.5% and 10y < 2% (proposed) THEN long Treasuries are a weak hedge (cap TLT weight in de-risk at 25%, rest bills). Test whether TLT's hedge payoff in stock drawdowns shrinks when starting 10y yield is low.
- Data needed: FEDFUNDS (FRED, 1954), DGS10. Fed funds in tool (12m change).
- Confidence: medium

### Bonds for principal protection only within ~5 years; avoid 30y for that job
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "you should use them inside of like a five year time horizon where you're not exposing yourself to just crazy amounts of like interest rate risk like you would if you owned a 30 year")
- Type: action/instrument
- Rule as testable logic: Test variant of the de-risk sleeve: hold a 1-5y Treasury ladder (SHY/IEI) instead of TLT; compare drawdown and return to TLT/bills switch, especially in inflationary regimes (stock-bond corr > 0).
- Data needed: SHY (2002), IEI (2007), VFISX/VFITX (1991), FRED yields. Not in tool (only TLT and bills).
- Confidence: high

### Bond ladder as systematic fixed-income core
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "you bucket it out from one to 10 year maturities ... you're just systematically rolling them over ... you don't care what's going on with interest rates")
- Type: action/instrument
- Rule as testable logic: Benchmark: equal-weight 1-10y Treasury ladder, rolled annually, regardless of rates. Use as a no-timing benchmark for the bond sleeve.
- Data needed: FRED DGS1..DGS10 (1976+ full curve); build ladder returns. Not in tool.
- Confidence: high

### TIPS are not the inflation answer for the bond sleeve (caveat)
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "I'm not a big fan of tips and inflation protecting its securities in fixed income markets in general, is because bonds, to me, they're principle protection instruments")
- Type: conflict/caveat
- Rule as testable logic: Test whether replacing nominal Treasuries with TIPS (TIP/SCHP) in hot-inflation regimes improves results; Roche predicts little benefit. Conflicts with inflation-hedge playbooks that buy TIPS.
- Data needed: TIP ETF (2003), FRED DFII10 (2003), real yield in tool.
- Confidence: medium

### T-bills when bill yields are meaningfully positive
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "you can buy six and 12 month treasury bills right now for 4% ... that instrument is a no brainer to own. Assuming you have a six month time horizon")
- Type: action/instrument
- Rule as testable logic: IF 6-12m bill yield > core CPI y/y minus 1 pp (proposed) or > 3% THEN bills are the default cash leg (vs zero-yield cash); measure the bills-vs-stocks hurdle (earnings yield minus bill yield) as a signal for stock weight.
- Data needed: FRED DTB6/DTB1YR (1959/1959), TB3MS (1934). Core CPI in tool.
- Confidence: medium

### Drawdown raises forward equity returns (mean reversion)
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "when the stock market falls in value, it actually tends to become a higher return generating instrument in the future")
- Type: re-entry/exit
- Rule as testable logic: IF S&P 500 is 25%+ below its prior peak (proposed) THEN expected 3-5y forward return is higher; test whether re-entering stocks earlier (at -25% drawdown even with warnings on) beats waiting for trend re-entry.
- Data needed: S&P 500 total return (Shiller from 1871; ^GSPC/SPY). S&P vs 10m average in tool; drawdown depth not.
- Confidence: medium

### Avoid forced selling: hold liquidity buckets
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "being a forced seller of stocks into a downturn because you just need the liquidity")
- Type: position sizing/risk
- Rule as testable logic: Portfolio constraint: keep 1-2 years of spending (proposed 10% of portfolio) in bills/short Treasuries at all times; the stock cut should not bring the long-horizon bucket below a floor. Behavioral, test only as a minimum-cash variant.
- Data needed: none beyond bills. Not in tool.
- Confidence: medium

### International vs US leadership cycles
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "international stocks, for instance, they kick the pants off of US stocks in the two thousands and. Then we've, we've been through this long 15, 20 year cycle where the US has")
- Type: regime map
- Rule as testable logic: IF ex-US equities (MSCI ACWI ex-US/EFA) outperform the S&P 500 over the trailing 12 months and the trailing 10-year relative return is in the bottom fifth of history (proposed) THEN overweight ex-US (VEU/EFA/EEM) vs US for 12-36 months; else default global weights. Test relative momentum + long-term reversal.
- Data needed: MSCI EAFE/ACWI ex-US total return (MSCI from 1970; EFA 2001, VEU 2007, VGTSX 1996); dollar 12m change in tool (likely driver).
- Confidence: medium

### Home-bias / single-country concentration risk (Japan 1990)
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "if you were only invested in Japan in 1990, well you suffered through one heck of a big stock market trauma"); Stig Brodersen notes Japan was "45%" of a global index then, "less than 5%" now.
- Type: regime map
- Rule as testable logic: IF one country's share of world market cap exceeds 40% (proposed, cf Japan 1989 ~45%, US now ~60%+) AND its CAPE is in the top decile of its own history THEN underweight that country vs world for 5-10 years. Test on Japan 1989, US 2000, US now.
- Data needed: MSCI country weights / market caps (World Bank CM.MKT.LCAP.CD, 1975+), country CAPE (Research Affiliates/Barclays, StarCapital; MSCI Japan from 1970, EWJ 1996). CAPE (US) in tool; country CAPE not.
- Confidence: medium

### Value vs growth swings; value led in 2022 rate rise
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "value in the last year and a half, has absolutely smoked growth")
- Type: signal
- Rule as testable logic: IF 10y yield 12m change > +1 pp (proposed) THEN overweight value (IWD/VTV) vs growth (IWF/VUG) for 6-12 months; else neutral. Roche himself prefers holding both (no timing), so test as a candidate only.
- Data needed: Ken French HML / Fama-French value and growth portfolios (1926+), IWD/IWF (2000). 10y 12m change in tool.
- Confidence: low (he argues for blending, not timing)

### Commodities and cash as the diversifier when stocks and bonds fall together
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "even though bonds are down, 11% or whatever, and I think gold is down 10%, commodities are up")
- Type: hedge
- Rule as testable logic: IF stock-bond correlation (in tool) > 0 AND core CPI y/y > 4% (proposed) THEN hold the de-risk sleeve in broad commodities (DBC/GSG/BCOM) plus bills rather than long Treasuries. Test 1973-74, 1977-81, 2022.
- Data needed: Bloomberg Commodity Index / S&P GSCI TR (GSCI from 1970; DBC 2006, GSG 2006); World Bank commodity price index (monthly from 1960); stock-bond corr and core CPI in tool.
- Confidence: medium

### Gold return depends on home currency
- Source: Stig Brodersen (host) — Macro Investing (TIP486) (quote: "gold is down 10% here in Europe, people are pretty excited because gold is up. And that's of course because the euro is down 16%")
- Type: conflict/caveat
- Rule as testable logic: Evaluate gold as a hedge in USD terms only for a USD investor; test whether gold's drawdown hedge is stronger when the dollar is falling (dollar 12m change < 0). IF dollar 12m change > +10% THEN gold (USD) hedge expected weak.
- Data needed: gold price (LBMA via FRED discontinued; use World Bank pink sheet monthly from 1960, GLD from 2004, IAU), dollar index (FRED DTWEXBGS 2006, DTWEXM 1973-2019). Dollar 12m change in tool.
- Confidence: low

### Inverted curve = Fed too tight = recession signal
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "with the 10 year yield lower than the two year today, the marketplace is basically saying we are not as worried about inflation ... this is the reason why the yield curve tends to be a pretty good predictor of recessions")
- Type: signal
- Rule as testable logic: IF 10y-2y < 0 THEN raise recession odds over 6-18 months; reduce cyclicals, extend duration. (Already in tool.)
- Data needed: FRED T10Y2Y (1976). In tool.
- Confidence: high

### Fiscal deficits are the real "money printing"; QE is weak (conflict with liquidity views)
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "when the government runs huge deficits ... I would argue that is money printing ... Whereas when a central bank creates reserves, they're not necessarily really printing money")
- Type: conflict/caveat
- Rule as testable logic: IF federal deficit (12m rolling) as % of GDP widens by > 2 pp y/y (proposed) THEN expect higher nominal GDP growth / inflation over 12-24 months (overweight stocks/commodities, underweight long bonds); test this vs the Fed net liquidity indicator to see which predicts better. Contradicts speakers who treat Fed balance sheet / QE as the main liquidity driver.
- Data needed: Monthly Treasury Statement deficit (FRED MTSDS133FMS, 1980), GDP (FRED GDP). Fed net liquidity in tool; deficit not.
- Confidence: medium

### Credit creation is demand-driven (loans create deposits), not reserve-driven
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "The primary function of loan creation is demand for loans and the bank's ability to actually, find credit worthy borrowers")
- Type: conflict/caveat
- Rule as testable logic: Test bank loan growth (C&I + consumer, 6m annualized) as a better growth signal than reserves/QE: IF bank credit growth turns negative (proposed) THEN cut stocks. Caveat on using M2 / reserves alone.
- Data needed: FRED TOTBKCR (1973), BUSLOANS (1947), TOTRESNS. Not in tool (M2 growth is).
- Confidence: medium

### Fed as lender of last resort in banking panics (2008)
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "the Fed could end up having to be involved in this because the banks in Europe are now very interconnected with the banks in the United States"; "that's what they did in 2008. And it actually worked really well")
- Type: re-entry/exit
- Rule as testable logic: IF a bank-stress spike occurs (bank stocks vs market in tool: 3m relative < -20%, proposed) AND the Fed announces emergency liquidity (discount window/facility usage jumps; FRED WLCFLPCL or H.4.1 "loans" > 2x prior) THEN re-enter stocks/credit within 3 months. Test 2008-09, 2020, 2023.
- Data needed: Fed H.4.1 loans/facilities (FRED WLCFLPCL from 2002), bank stocks vs market (in tool), European bank index (EUFN 2010, STOXX Banks).
- Confidence: low

### Real returns are modest: stocks ~4-5%, housing ~1-2% after inflation
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "you should assume that the aggregate stock market after inflation is probably only gonna do like four to 5%"; "real estate historically is only generated about a one, maybe 2% real return")
- Type: conflict/caveat
- Rule as testable logic: Use as a prior for expected-return assumptions (no trading rule). Benchmark hurdle: a de-risk rule must beat buy-and-hold real ~4-5%/yr after costs.
- Data needed: Shiller real returns (1871), Case-Shiller (FRED CSUSHPINSA 1987; Shiller housing from 1890).
- Confidence: medium

### Cost and turnover drag (behavior/costs controllable)
- Source: Cullen Roche — Macro Investing (TIP486) (quote: "the more active you are though, the less control you have because you're incurring higher taxes and fees along the way")
- Type: position sizing/risk
- Rule as testable logic: Constraint for every new rule: count trades per year and charge 10 bp per switch + tax drag (proposed); reject rules whose net edge disappears after costs.
- Data needed: none.
- Confidence: high

---

## File 2: Kyle Bass, "Global Macro Investing And Geoeconomics With Hedge Fund Investor Kyle Bass - Hoover Institution" (Jun 2025)

### Bank leverage x asset loss = system insolvency (pre-crisis leverage screen)
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "you lever yourself 30x and you get and you find and you end up owning assets that lose, you know, 40% of their value and you can do it's just a math problem")
- Type: signal
- Rule as testable logic: IF financial-sector leverage (broker-dealer assets/equity, or bank assets/equity) is in the top fifth of its history AND house prices fall y/y (proposed: Case-Shiller y/y < 0) THEN cut stocks and bank exposure (XLF/KBE) and hold Treasuries for 12-24 months.
- Data needed: Fed Z.1 broker-dealer assets/equity (FRED BOGZ1FL664090005Q etc., 1952), FDIC bank equity/assets (FRED EQTA, 1984), Case-Shiller (FRED CSUSHPISA, 1987; Shiller to 1890). Not in tool (bank stocks vs market and card delinquencies are).
- Confidence: medium

### Loose lending anecdote -> housing credit bubble
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "everyone knew the housing market was overcooked. Everyone knew that it was really easy to borrow money ... bartenders could have two or three loans")
- Type: signal
- Rule as testable logic: IF Senior Loan Officer survey shows mortgage standards net easing for 4+ quarters (proposed) AND home price/income ratio in top decile THEN underweight homebuilders (ITB/XHB) and financials, overweight Treasuries for 2-3 years.
- Data needed: FRED SUBLPDHMSNQ / DRTSCLCC (SLOOS, 1990), house price/income (FRED MSPUS / MEHOINUSA672N, or Shiller), homebuilders vs market (in tool).
- Confidence: medium

### Bank-to-sovereign contagion: bailouts move bad assets onto weak sovereign balance sheets
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "you had to follow the bad private assets to public balance sheets. So then the analysis was which public balance sheets can handle that kind of movement")
- Type: regime map
- Rule as testable logic: IF a systemic banking crisis is under way (bank stocks -40% from high, proposed) THEN rank countries by banking assets/GDP; underweight (or short) equities/sovereign bonds/currency of countries with bank assets > 3x GDP (proposed; Iceland/Ireland were 10x) for 12-36 months. Test 2008-2012 (Ireland EIRL, Greece GREK, Italy EWI, Spain EWP).
- Data needed: World Bank GFDD bank assets/GDP (1960+), BIS; MSCI country indexes (1970+ / iShares country ETFs 1996+); 10y sovereign yields (FRED IRLTLT01xxM156N, OECD, 1960s+). Not in tool.
- Confidence: high

### Very high sovereign debt + capped yields -> currency is the escape valve (short the currency)
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "now they're 265% sovereign debt to GDP. They can never let rates move. They can't. So what does that mean? That means the currency is the is the escape valve")
- Type: action/instrument
- Rule as testable logic: IF government debt/GDP > 200% (proposed, Japan) AND the central bank caps or pegs yields (YCC / policy rate ~0 with large bond buying) THEN short that currency vs USD (long USD/JPY; short FXY) and own that country's equities hedged (DXJ/HEWJ) for 2-5 years. Test yen 2012-2015 and 2021-2024.
- Data needed: IMF WEO / FRED GGGDTAJPA188N debt/GDP, BoJ policy rate (FRED IRSTCI01JPM156N), USD/JPY (FRED DEXJPUS, 1971), FXY (2007), DXJ (2006). Not in tool.
- Confidence: high

### Asymmetric barbell of options on a fork-in-the-road outcome
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "we took twothirds of the money in the fund and we bought bond market optionality right in the in JGBs. I took onethird of the money and I bet with the Bank of Japan")
- Type: position sizing/risk
- Rule as testable logic: When a policy regime must end in one of two outcomes (inflate vs debt crisis), size two option legs so the loss of either leg is capped (premium) and the winner pays a multiple; total premium budget <= 2-3% of portfolio per year (proposed). For the tool: test a small rolling put/call budget (e.g. 1%/yr in SPY puts or TLT calls) instead of outright cuts.
- Data needed: option prices (CBOE PUT index 1986, CBOE PPUT 5% OTM put index, VIX for pricing; Cboe indices free). Not in tool.
- Confidence: medium

### "You only need to be right 55% of the time" (asymmetry over hit rate)
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "on Wall Street you only need to get like 55% of those right")
- Type: position sizing/risk
- Rule as testable logic: Evaluation criterion: accept a signal with hit rate >= 55% if average win/loss >= 1; report hit rate and payoff ratio for every rule.
- Data needed: none.
- Confidence: medium

### Sovereigns rarely default; they print -> inflation/debasement, not default
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "almost no sovereign ever defaults John they get into a crisis they print they print and print money expand a balance sheet but they always pay")
- Type: regime map
- Rule as testable logic: IF government debt/GDP rising fast and deficit > 6% of GDP outside recession (proposed) THEN position for currency weakness and inflation (gold GLD, TIPS, commodities; underweight long nominal bonds) rather than for default.
- Data needed: FRED GFDEGDQ188S (debt/GDP, 1966), FYFSGDA188S (deficit/GDP, 1929), gold, DXY. Not in tool (10y minus nominal GDP is).
- Confidence: medium

### Asset prices outpacing wages -> social tension, more conflict (geopolitical regime)
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "we should expect more and more war uh because there is no answer for for for this equation at the moment")
- Type: regime map
- Rule as testable logic: IF house price/wage ratio is in top decile AND real wages y/y < 0 for 12+ months (proposed) THEN overweight defense (ITA/XAR) and energy vs broad market for 2-5 years. Low testability.
- Data needed: FRED CSUSHPISA, AHETPI or LES1252881600Q (real earnings, 1979), ITA (2006), S&P Aerospace & Defense index. Not in tool.
- Confidence: low

### Home price / income extreme (China 26x) -> property stimulus absent, demographics collapse
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "when home prices in China got to be 26 times median income, um the men couldn't afford homes ... he has not stimulated his real estate market")
- Type: signal
- Rule as testable logic: IF country house price/income ratio > 15x (proposed) AND the government does not stimulate property THEN underweight that country's banks/property and broad equities (China FXI/MCHI) for 3+ years.
- Data needed: Numbeo/national stats price-to-income (patchy); BIS residential property prices (1970+ for many countries); MSCI China (1992), FXI (2004). Not in tool.
- Confidence: low

### Avoid Chinese assets: GDP growth did not reach shareholders
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "if you invested in the Shenen Shanghai 300 ... you've lost a third of your money and they've grown their economy 505%")
- Type: conflict/caveat
- Rule as testable logic: Do NOT use GDP growth as a country-allocation signal. Test: cross-country correlation of 10y GDP growth vs 10y equity return (expected ~0 or negative). Exclude or cap China (FXI/MCHI/ASHR) at index weight or below.
- Data needed: World Bank GDP (1960), MSCI country total returns (1970/1988+), CSI 300 (2005) / ASHR (2013). Not in tool.
- Confidence: high

### Taiwan conflict within 2-3 years -> short China/Taiwan, financial sanctions on Chinese banks
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "I think we're going to see Xi Jinping move in the next two or three years on Taiwan. I think we're going to be kinetically involved"; "we will certainly hobble them financially")
- Type: hedge
- Rule as testable logic: IF Taiwan-strait military activity (ADIZ incursions, proposed: 12m count at record high) or a blockade begins THEN zero China (FXI/MCHI/KWEB) and Taiwan (EWT) and cut semiconductors (SOXX/SMH); overweight US defense (ITA) and gold. Event rule, cannot be backtested (no precedent); keep as a scenario playbook.
- Data needed: Taiwan MND ADIZ incursion counts (2020+, from PLATracker/ChinaPower), EWT (2000), SOXX (2001), ITA (2006). Not in tool (chips vs 12m high is).
- Confidence: medium (as a forecast; low as a testable rule)

### Amphibious invasion window ~3 months/year (Taiwan Strait tides)
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "lends it only to be somewhat amendable to an amphibious invasion three months out of the year")
- Type: conflict/caveat
- Rule as testable logic: Seasonal risk overlay: in April and October windows (commonly cited; months not stated by speaker, proposed) raise Taiwan/semis hedge (e.g. buy SMH/EWT puts). Not backtestable.
- Data needed: none historical.
- Confidence: low

### China current account heading to zero = CCP stress / capital flight
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "The Chinese current account uh call it their net income account was headed towards zero")
- Type: signal
- Rule as testable logic: IF China current account surplus (4q sum) falls below 0.5% of GDP (proposed) THEN expect CNY weakness and tighter capital controls; underweight China equities (FXI) and EM Asia (AAXJ) for 12 months; long USD/CNH.
- Data needed: SAFE / IMF BOP China current account (quarterly, 1998), USD/CNY (FRED DEXCHUS, 1981), FXI. Not in tool.
- Confidence: low

### Rare-earth chokepoint = China's leverage ("hostage negotiation")
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "This is not a trade negotiation. This is a hostage negotiation")
- Type: hedge
- Rule as testable logic: IF China announces export controls on rare earths/critical minerals THEN long rare-earth/strategic metals (REMX) and US defense; underweight autos/EV makers (CARZ/DRIV) for 3-6 months. Event study on 2010, 2019, 2023, 2025 control announcements.
- Data needed: REMX (2010), event dates (manual). Not in tool.
- Confidence: low

### US inflation exported to the world; dollar-dependent countries have "negative convexity" to the US
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "The world's priced in dollars, John. We just pushed 50% dollar inflation to the world in a four-year period. And they have a negative convexity to us")
- Type: regime map
- Rule as testable logic: IF US CPI y/y > 4% AND dollar 12m change > 0 (both in tool) THEN underweight EM non-commodity importers (e.g. EEM ex commodity exporters: India INDA, Turkey TUR, Philippines EPHE, Egypt) vs US for 12 months; prefer self-sufficient commodity exporters (Brazil EWZ, Canada EWC, Australia EWA).
- Data needed: MSCI EM and country indexes (1988+), net commodity exporter list (World Bank/UNCTAD), CPI and dollar (in tool).
- Confidence: medium

### US is the best place for capital (structural overweight US vs Europe) — conflicts with Roche
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "We are 4% of the world's population. We're 26% of the world's GDP. We are 60% of the world's capital markets"; "I can't imagine anywhere better than the US to invest")
- Type: conflict/caveat
- Rule as testable logic: Baseline: hold US equities as the core; Europe only for "branded luxury". Contradicts Roche's "diversify internationally / Japan 1990" warning. Test: US-only vs global-cap-weight vs relative-momentum switch since 1970.
- Data needed: MSCI USA, MSCI Europe, MSCI World (1970). Not in tool.
- Confidence: high (as his view), medium (as a rule)

### Europe fragile in a shock: no fiscal union, no deposit guarantee
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "when the world hits a speed bump, it's it's going to kill Europe because they don't have a real union ... there's no deposit guarantee scheme across Europe")
- Type: regime map
- Rule as testable logic: IF global stress overlay is on (VIX > 30 or junk spreads widening, in tool) THEN underweight Europe (VGK/EZU) vs US and avoid European banks (EUFN); also track Italy-Germany 10y spread > 2.5 pp (proposed) as euro-stress trigger.
- Data needed: Italy and Germany 10y yields (FRED IRLTLT01ITM156N, IRLTLT01DEM156N, 1990s), VGK (2005), EZU (2000), MSCI Europe (1970). VIX and junk spread in tool.
- Confidence: medium

### Middle East realignment (UAE/Saudi with US); Israel-Iran escalation "before de-escalation"
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "I think that things are going to escalate before they deescalate ... I just think there's a lot more kinetic conflict coming")
- Type: hedge
- Rule as testable logic: IF a Middle East military escalation event occurs (manual event list) THEN test 1-3 month response of oil (USO/BNO), gold (GLD), defense (ITA), and Gulf equities (KSA, UAE) — hypothesis: oil/gold up short-term, fade after 3 months (proposed).
- Data needed: Brent (FRED DCOILBRENTEU, 1987), GLD, ITA, KSA (2015), UAE (2014); geopolitical risk index (Caldara-Iacoviello GPR, monthly from 1900, free). Not in tool.
- Confidence: low

### Persistent $1.8T deficits widen inequality (caveat to US-overweight)
- Source: Kyle Bass — Global Macro Investing (Hoover) (quote: "we're going to keep running $1.8 trillion deficits going forward. So, that's the caveat")
- Type: conflict/caveat
- Rule as testable logic: Monitor deficit/GDP; IF deficit > 6% of GDP at full employment (unemployment < 5%) (proposed) THEN term premium and inflation risk up: shorten bond duration in the de-risk sleeve (bills/SHY instead of TLT).
- Data needed: FRED FYFSGDA188S / MTSDS133FMS, UNRATE; term premium (in tool).
- Confidence: medium

---

## File 3: Jeffrey Hirsch (with Steve Eisman), "Market Patterns Work and Jeffrey Hirsch Explains Why - The Real Eisman Playbook Ep 56" (Apr 2026)

### Midterm-year bottom ("bottom picker's paradise")
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "11 of the last 16 bare markets bottomed in the midterm year")
- Type: regime map
- Rule as testable logic: IF calendar year is a US midterm year (1914, 1918 ... 2022, 2026) THEN expect the annual low in Q2-Q3 (late summer to October); allow re-entry into stocks during Aug-Oct of midterm years even if trend is below 10m average (proposed: if drawdown from 12m high > 10%).
- Data needed: Dow (since 1896, FRED/Stooq/Shiller monthly), S&P 500 (1928 daily, Shiller 1871). Not in tool (calendar).
- Confidence: high

### Midterm low to pre-election-year high: Dow +46%, Nasdaq +67% on average
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "The gain from the midterm low to the pre-election year high is 46.3% for the Dow on average going back to 1914")
- Type: signal
- Rule as testable logic: IF in the period from the midterm-year low through the pre-election year THEN overweight equities (S&P 500 / Nasdaq QQQ) vs cash; measure forward 12m return from Oct 1 midterm year vs other years.
- Data needed: Dow, S&P, Nasdaq Composite (1971). Not in tool.
- Confidence: high

### Four-year-cycle sweet spot: Q4 midterm year through Q2 pre-election year
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "the sweet spot of the four-year cycle is Q4 midterm year to Q2 pre-election year ... Sweet spot. 19% Dow, 20% S&P, 29.3 NASDAQ")
- Type: signal
- Rule as testable logic: IF date is between Sep 30 of a midterm year and Jun 30 of the following year THEN hold full stock weight (override soft warnings, proposed: only the Fed-tightening warning cut is suspended); else default rules. Test as an overlay on the existing de-risk logic.
- Data needed: S&P 500 daily/monthly. Not in tool.
- Confidence: high

### Weak spot: Q2-Q3 of midterm year
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "the weakest period what we call the weak spot of the four-year cycle is Q2 Q3 of the midterm year")
- Type: signal
- Rule as testable logic: IF Apr 1 - Sep 30 of a midterm year THEN lower equity weight (proposed: by one third) or require warnings to be at a lower threshold to cut.
- Data needed: S&P 500. Not in tool.
- Confidence: high

### Pre-election year is the best year of the four-year cycle
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "the best year of the four-year cycle has been the pre-election year")
- Type: signal
- Rule as testable logic: IF calendar year is pre-election year (year mod 4 == 3) THEN full equity weight; test average annual return by cycle year since 1928/1914.
- Data needed: S&P 500 / Dow. Not in tool.
- Confidence: high

### Best Six Months switching strategy (Nov-Apr in, May-Oct out)
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "buying, you know, Dow, S&P, NASDAQ on uh October 30th and 31st or the last trading day of the month and selling April 30th um of the following year")
- Type: action/instrument
- Rule as testable logic: IF month in Nov-Apr THEN hold S&P 500/Dow; IF May-Oct THEN hold T-bills or short Treasuries (or reduce, as Hirsch "repositions" rather than exits). Nasdaq: best eight months Nov-Jun. Test vs buy-and-hold and as an overlay to the macro cut (e.g. macro warnings only act in May-Oct).
- Data needed: S&P 500, Dow, Nasdaq daily; T-bill (FRED TB3MS). Not in tool.
- Confidence: high

### MACD timing to refine seasonal entry/exit
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "We use a MACD technical timing indicator ... you use the MACD to sort of confirm an entry or exit")
- Type: re-entry/exit
- Rule as testable logic: Enter the Nov-Apr period when the Dow's MACD (12,26,9, daily; Hirsch uses 8-17-9 for buy and 12-25-9 for sell, parameters not stated here, proposed 12/26/9) turns up on or after Oct 1; exit when MACD turns down on or after Apr 1.
- Data needed: Dow/S&P daily closes. Not in tool.
- Confidence: medium (parameters not stated)

### Claimed out-of-sample validation (Aronson test since 1987)
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "unlike any of the other 6,000 plus different blackbox systems, it was the only one that had predictive power and was not the result of chance")
- Type: conflict/caveat
- Rule as testable logic: Re-run the Best Six Months test out of sample 2008-2026 (after the Aronson check) with White's reality check / bootstrap to confirm it still holds; treat as a candidate overlay only if p < 0.05 after costs.
- Data needed: S&P 500 daily since 1950. Not in tool.
- Confidence: medium

### Mechanism: mutual-fund Oct 31 fiscal year-end and quarter-end window dressing
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "there is that mutual fund deadline um the 40 act uh deadline of October 31st ... This creates sort of a vortex of action")
- Type: signal
- Rule as testable logic: IF last two weeks of September / October (tax-loss and window-dressing selling) THEN avoid adding; buy last trading days of October. Test return of last 5 trading days Oct + first 3 Nov vs average.
- Data needed: S&P daily. Not in tool.
- Confidence: medium

### Best three months: November, December, January
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "the best three months of the year November, December, January")
- Type: signal
- Rule as testable logic: IF month in Nov-Jan THEN full equity weight (do not de-risk on soft warnings, proposed).
- Data needed: S&P monthly. Not in tool.
- Confidence: high

### September is the worst month
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "September historic. That's where things start to to sell off ... the worst month of the year")
- Type: signal
- Rule as testable logic: IF month = September THEN expect below-average return; test September average and hit rate since 1950 (no stand-alone trade, overlay only).
- Data needed: S&P monthly. Not in tool.
- Confidence: medium

### Turn-of-month and mid-month (401k) flow effects
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "most of the market's gains remain on the on the the last day of the month and the first few days of the month ... It doesn't occur so much I mean anymore"; "this midmon spike starts to appear ... the bimonthly or the every two weeks payroll deductions going into 401ks")
- Type: signal
- Rule as testable logic: Execution rule: schedule monthly rebalances/entries on the last trading day of the month (or mid-month) to capture flow days; test turn-of-month (T-1 to T+3) vs other days since 1990 and the decay since 2000.
- Data needed: S&P daily. Not in tool.
- Confidence: medium (he says it has weakened)

### Intraday pattern: weak open, rally into close
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "the opens are weak ... and then you get that end of day rally which is the smart money coming in")
- Type: re-entry/exit
- Rule as testable logic: Execution only: place buy orders as limits for the 2-2:30 pm dip. Not a macro rule. (Note: Eisman's tool uses month-end; no intraday data needed.)
- Data needed: intraday SPY (not free long history). Not in tool.
- Confidence: low (for this tool)

### Utilities seasonal trade during the worst six months
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "weak period trade from March through October is the is utilities ... we're in in utilities for for the the worst months of the year")
- Type: action/instrument
- Rule as testable logic: IF month in Mar-Oct THEN rotate part of the equity sleeve (proposed 25%) into utilities (XLU) vs S&P; Nov-Feb back to broad market. Test relative XLU vs SPY by month since 1999 (S&P Utilities index since 1989; Ken French Utils industry since 1926).
- Data needed: XLU (1998), Ken French 12-industry "Utils" (1926). Not in tool.
- Confidence: medium

### Copper and energy seasonal: December low, April-May high
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "copper tends to make its low in December ... and then top out uh around you know April May. Uh similar with with the energy stocks the XLE")
- Type: action/instrument
- Rule as testable logic: IF date between mid-December and end of April THEN long copper (HG futures / CPER / COPX miners) and energy stocks (XLE) vs S&P; exit by May. Combine with technical entry and macro trend (copper 6m change in tool).
- Data needed: copper price (FRED PCOPPUSDM monthly 1990; World Bank 1960; CPER 2011, COPX 2010), XLE (1998), Ken French Oil industry (1926). Copper 6m change in tool.
- Confidence: medium

### Five-discipline confluence: seasonality + fundamentals + technicals + monetary policy + sentiment
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "we like this to look at things with these five disciplines. Seasonality, fundamentals, technicals, monetary policy, and sentiment")
- Type: position sizing/risk
- Rule as testable logic: Only take a seasonal trade when at least one other discipline agrees (e.g. price above its 50-day average or MACD up, and Fed not tightening). Test seasonal-only vs seasonal+trend filter.
- Data needed: as above; Fed funds 12m change in tool.
- Confidence: medium

### Stop-losses and profit-taking on seasonal trades
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "sell your losers short or fast and hang let your winners ride. I mean, we do like to sell half on a double"; "We've subsequently got stopped out of the miners with a decent gain")
- Type: position sizing/risk
- Rule as testable logic: For tactical (non-core) trades: trailing stop (proposed 10% from peak for ETFs), sell half on +100%. Tighten in May (limit new longs, sell underperformers).
- Data needed: ETF prices. Not in tool.
- Confidence: medium

### Dead indicator: September reverse barometer (indicator graveyard)
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "If September was down, the market would rally after that. If it was up, it would go down. Doesn't work anymore")
- Type: conflict/caveat
- Rule as testable logic: Exclude. Use as a control: any calendar rule must show stability across sub-periods (pre/post 1990, post 2008) or go to the "graveyard".
- Data needed: S&P monthly.
- Confidence: high (that it no longer works)

### January Barometer: as January goes, so goes the year
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "The January barometer, as January goes, so goes the year ... That's all of January based on the S&P 500")
- Type: signal
- Rule as testable logic: IF S&P 500 January return > 0 THEN hold full equity weight Feb-Dec; IF < 0 THEN lower equity weight (proposed by one third) or allow warnings to cut more easily for Feb-Dec.
- Data needed: S&P monthly since 1928/1950. Not in tool.
- Confidence: high

### First Five Days indicator
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "First five days is is um also pretty solid. So in other words, if if the market's up in the first five days of January, chances are it'll be up for the year")
- Type: signal
- Rule as testable logic: IF S&P return over first 5 trading days of January > 0 THEN expect positive year; test hit rate and forward 11m return.
- Data needed: S&P daily (1950). Not in tool.
- Confidence: medium

### Santa Claus Rally (last 5 days of Dec + first 2 of Jan)
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "the last five days of the year in the first two trading days of the new year. Usually up S&P about one and a half%"; "if Santa Claus should fail at the call, bears may come to broaden wall")
- Type: signal
- Rule as testable logic: IF Santa Claus rally return < 0 THEN raise caution for Q1 (proposed: reduce stocks by one third until January barometer confirms).
- Data needed: S&P daily. Not in tool.
- Confidence: medium

### January Indicator Trifecta (all three up -> 90.6% up years)
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "Santa Claus rally, January's first five days, and the full month January barometer. When all three are up, you get the market up 90.6% of the time ... 29 of 32 years")
- Type: signal
- Rule as testable logic: Score = count of (Santa rally > 0, first 5 days > 0, January > 0). IF score = 3 THEN full equity for Feb-Dec and suspend soft warning cuts; IF score <= 1 THEN cap equity at 50% (proposed) unless trend positive. Two of three: "up the next 11 months 87.5% of the time, 12.2%".
- Data needed: S&P daily (1950). Not in tool.
- Confidence: high

### Small caps outperform from mid-December (January effect moved earlier)
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "last two weeks of December seems to be the biggest period of time when like the Russell 2000 outperforms ... tends to start around Halloween as well and then after Thanksiving")
- Type: action/instrument
- Rule as testable logic: IF date between mid-December and end of January (or Nov 1 - Jan 31) THEN overweight small caps (IWM) vs large (SPY). Test Russell 2000 vs Russell 1000 (1979), Ken French size (1926).
- Data needed: IWM (2000), Russell 2000 (1979), Ken French SMB (1926). Not in tool.
- Confidence: medium

### Bitcoin: weak in midterm years; acts like levered Nasdaq
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "It's very weak in midterm election years"; "It's like 4x or 2x the NASDAQ")
- Type: conflict/caveat
- Rule as testable logic: Treat Bitcoin (IBIT/BITO) as high-beta Nasdaq, not a hedge; exclude from the hedge set; if held, cut in midterm years Q1-Q3. Short history (2010+, ETF 2024).
- Data needed: BTC-USD (2014 Yahoo), IBIT (2024). Not in tool.
- Confidence: medium

### Failed seasonal rally = stronger opposing forces (Eddie Gould rule)
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "If the market doesn't rally, you know, during the bullish seasonal period, then there are other forces that are stronger. And when that period ends, you know, those forces will really have their say")
- Type: signal
- Rule as testable logic: IF S&P return over Nov-Jan (best three months) < 0 (proposed) THEN cut equity for the following May-Oct period (or require only one warning to cut). Test forward 6m return after a negative Nov-Jan.
- Data needed: S&P monthly. Not in tool.
- Confidence: medium

### Super Boom: 500% rallies after war + inflation + paradigm-shifting technology
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "the market makes these 500 500% moves following war and inflation, World War I, World War II, and here we were coming out of Vietnam")
- Type: regime map
- Rule as testable logic: IF a secular bear low has occurred (10y real return of S&P < 0, proposed) after a war/inflation episode (CPI y/y peaked > 6%, proposed) THEN expect a secular bull: hold stocks with a more lenient cut rule (e.g. require two warning sets) for 10+ years. Very low sample (1914/21, 1942/49, 1974/82, 2009/11).
- Data needed: Dow/S&P since 1896, CPI since 1913 (FRED CPIAUCNS). CAPE and core CPI in tool.
- Confidence: medium (low sample)

### War endings: market bottoms within a month of the start; oil up like a rocket, down like a feather
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "the market sort of bottom within a month or so of the of the initial outset on average ... the faster it wraps up, um, the market rallies from there. Oil starts to come down"; "tends to go up like a rocket and sort of come down like a a feather")
- Type: re-entry/exit
- Rule as testable logic: IF a geopolitical/war shock event occurs THEN do not sell stocks after the first month; buy stocks ~1 month after the onset if S&P drawdown < 15% (proposed). Oil: after a war spike, expect slow decay; fade oil (underweight energy) 3-6 months after the peak. Event study using the GPR index spikes (top 5% months).
- Data needed: Caldara-Iacoviello GPR index (1900+, monthly; daily 1985+), WTI (FRED WTISPLC 1946), S&P. Oil 6m change in tool; GPR not.
- Confidence: medium

### Trump-era seasonal: Q1 shock, late March-early April low, rally rest of year
- Source: Jeffrey Hirsch — Market Patterns Work (Eisman Ep 56) (quote: "the the Trump presidency years, the the taco trade seasonal cycle, it shows I mean a double bottom in March, late March, and early April ... the average is up about 15%")
- Type: signal
- Rule as testable logic: IF Trump in office THEN buy stocks on a late-March/early-April dip and hold to year-end. Only 5 years of data; keep as watch item, not a rule.
- Data needed: S&P daily 2017-2020, 2025-2026. Not in tool.
- Confidence: low

### Credit cycle tightening (private credit) slows the economy
- Source: Steve Eisman — Market Patterns Work (Eisman Ep 56) (quote: "almost 100% of all the loan growth in the United States since the great financial crisis has been in private credit ... I do think we are entering a credit cycle and there's going to be tightening")
- Type: signal
- Rule as testable logic: IF private-credit/BDC prices fall > 15% from 12m high (proposed; BIZD or BDC index) OR SLOOS C&I standards tighten > 20% net (proposed) THEN reduce stocks/high yield for 6-12 months. Hirsch notes regional-bank fears in 2023 "never did" hit the market (caveat).
- Data needed: BIZD (2013), Cliffwater/BDC index; FRED DRTSCILM (SLOOS C&I, 1990). Not in tool (junk vs Treasuries and Baa spread are).
- Confidence: medium

---

## File 4: Stanley Druckenmiller (with Kiril Sokoloff), "Sohn 2023 - Kiril Sokoloff in conversation with Stanley Druckenmiller" (May 2023)

Note: captions have no punctuation; quotes are verbatim words.

### Worst outcomes follow asset bubbles built on rates below 2%
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "every time you've had interest rates below two percent going back 500 years it's generally been followed um with with difficult Economic Times")
- Type: regime map
- Rule as testable logic: IF policy rate (or 10y yield) has been below 2% for 3+ years (proposed) AND market cap/GDP or CAPE is in the top decile (in tool) THEN cap stock weight (proposed 60%) and expect below-average 5-10y returns; trigger full cut once the Fed starts hiking (rate 12m change > +1 pp, in tool).
- Data needed: FEDFUNDS (1954), Shiller long rate (1871), CAPE and market cap/GDP (in tool). Duration-below-2% counter not in tool.
- Confidence: high

### Don't fight the Fed (500 bp hiking after a bubble -> hard landing odds high)
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "big maximum my business don't fight the Fed"; "we've only had a few soft Landings since 1950 all of them were preceded by what I would call Proactive rather than reactive fed policy")
- Type: signal
- Rule as testable logic: IF Fed funds 12m change > +3 pp (proposed) AND the hikes started after core inflation already exceeded 4% (reactive) THEN hard-landing regime: cut stocks to the de-risk mix for 12-24 months; IF hikes began with core inflation < 2.5% (proactive) THEN soft landing odds higher, keep stocks. Matches the tool's Fed-tightening gate; adds a "reactive vs proactive" classifier.
- Data needed: FEDFUNDS, core CPI/PCE (FRED CPILFESL 1957, PCEPILFE 1959). Both partly in tool.
- Confidence: high

### Trucking as a 6-8 month leading indicator
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "Trucking which has been a Guiding Light for my firms in terms of economic forecasting with a six to eight month lead time")
- Type: signal
- Rule as testable logic: IF truck tonnage/freight y/y < 0 (proposed: 3 consecutive months) THEN expect economic weakness 6-8 months later; reduce cyclicals. (In tool: truck freight y/y; Dow Jones Transports vs industrials also in tool.)
- Data needed: ATA truck tonnage (FRED TRUCKD11, 2000), Cass Freight index; in tool.
- Confidence: high

### Housing leads the cycle (and can lead out of it given structural shortage)
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "housing which has tended to lead historically is actually um fairly fairly robust"; "if things got bad enough I could actually see housing ... could be a big beneficiary on the way out")
- Type: re-entry/exit
- Rule as testable logic: IF in a recession/hard-landing cut AND homebuilders (ITB/XHB) outperform the S&P over 3 months (proposed) while housing inventory/months' supply is below its long-run average (structural shortage) THEN re-enter via homebuilders first (overweight ITB) for 12 months. Homebuilders vs market and permits are in tool.
- Data needed: FRED MSACSR (months' supply, 1963), HOUST, ITB (2006), S&P Homebuilding index. Partly in tool.
- Confidence: medium

### Regional banks + commercial real estate stress = credit contraction
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "the median Regional Bank has 43 percent of their um loans in commercial real estate about 40 percent of that is office ... we have actually a higher vacancy rate than we had in 2008")
- Type: signal
- Rule as testable logic: IF regional bank index (KRE) falls > 25% vs S&P over 3 months (proposed) OR office vacancy above its 2008 peak THEN credit contraction risk: cut stocks/high yield; avoid REITs (VNQ) and CRE-heavy banks for 12 months.
- Data needed: KRE (2006), KBW regional bank index (1991), office vacancy (Moody's/CBRE, not free; proxy: Fed CRE loan delinquency FRED DRCRELEXFACBS, 1991), VNQ (2004). Bank stocks vs market in tool.
- Confidence: medium

### Bank duration mismatch: banks already impaired before loan losses
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "they're basically have stuff yielding two two and a half percent that their cost of funds is five percent on so before we even get into an economic attraction many of the banks already have impaired balance sheets")
- Type: signal
- Rule as testable logic: IF Fed funds minus the 5y Treasury yield of 3 years earlier > 2 pp (proposed proxy for asset-liability mismatch) OR FDIC unrealized securities losses / bank equity > 20% (proposed) THEN underweight banks (KBE/KRE) and cut stocks if bank stocks vs market also falling.
- Data needed: FDIC Quarterly Banking Profile unrealized losses (2008+), FEDFUNDS, DGS5. Not in tool.
- Confidence: medium

### Hard landing definition: profits -20%+, unemployment from 3.4% to above 5%
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "a say a 20 to 20 percent plus with an emphasis on the plus decline in corporate profits um unemployment probably going up from the 3.4 right now to something above five")
- Type: regime map
- Rule as testable logic: Label a "hard landing" ex post when corporate profits fall > 20% peak-to-trough and unemployment rises > 1.5 pp; use as the target variable to evaluate warning signals.
- Data needed: FRED CP (corporate profits, 1947), UNRATE (1948). Unemployment rise in tool; profits not.
- Confidence: high

### Money stock vs money growth: y/y M2 shrinkage overstated by prior 40% surge
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "yes the year to year over change in the money supply is like minus six percent but there's still a lot of liquidity out there")
- Type: conflict/caveat
- Rule as testable logic: Use M2 relative to its pre-shock trend (M2 / 10y log-linear trend, or M2/GDP vs its trend) in addition to M2 y/y: IF M2 y/y < 0 BUT M2 level still > 5% above trend (proposed) THEN discount the M2-contraction warning. M2 growth is in tool.
- Data needed: FRED M2SL (1959), GDP. M2 growth in tool; M2 gap not.
- Confidence: medium

### Inflation path after a hard landing: Arthur Burns stop-go -> stagflation
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "if they act like Arthur burns when it goes down to three or three and a half percent ... I could see a few years out sort of an inflationary probably with an emphasis on the Stag part A stagflationary environment")
- Type: regime map
- Rule as testable logic: IF Fed cuts rates while core inflation is still > 3% (proposed) THEN stagflation regime for 2-4 years: overweight commodities, energy (XLE), materials, gold; underweight long Treasuries and growth stocks.
- Data needed: FEDFUNDS, core CPI (in tool), commodity indexes (GSCI 1970, World Bank 1960), XLE / Ken French Oil (1926). Partly in tool.
- Confidence: high

### After a burst bubble, deflation/bust risk: "can't put Humpty Dumpty back together"
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "the surest way to create deflation is to build an asset bubble and then burst it" (Sokoloff); "if you burst it um there's a possibility that they can't put Humpty Dumpty back together again" (Druckenmiller))
- Type: regime map
- Rule as testable logic: IF S&P falls > 30% from a peak where CAPE was top decile AND credit spreads widen (Baa spread 6m change > +1 pp, in tool) THEN deflation-bust regime: hold long Treasuries (TLT/ZROZ) and cash; avoid commodities.
- Data needed: CAPE, Baa spread (in tool), S&P drawdown. Not in tool (drawdown).
- Confidence: medium

### Commodities can hold up when a stock bubble bursts (1973-74, 2000-02)
- Source: Kiril Sokoloff — Sohn 2023 (quote: "the internet Bubble Burst Commodities and commodity equities especially oil held up well and of course we're the leaders in ensuing decades")
- Type: hedge
- Rule as testable logic: IF S&P breaks down from a top-decile CAPE AND inflation not falling (core CPI 3m vs 12m >= 0, in tool) THEN hold commodity equities (XLE, XME, GNR) and commodities instead of cash. Test 1973-74, 2000-02 vs 2008 (failed).
- Data needed: Ken French industry returns (1926), GSCI (1970), XLE (1998). Partly in tool.
- Confidence: medium

### Don't hold cyclicals (copper) into a hard landing; buy them coming out
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "I'm actually afraid to have a meaningful position in it at this point as we approach the hard Landing um only because I'm not an idiot and I know what what happened to the cyclical factors"; "coming out of it ... it's hard to believe copper won't be a huge beneficiary")
- Type: re-entry/exit
- Rule as testable logic: IF hard-landing warning is on THEN zero copper/miners (CPER, COPX, XME); IF after a recession the Fed is cutting and copper 6m change turns positive (in tool) THEN overweight copper/miners for 12-24 months.
- Data needed: copper (FRED PCOPPUSDM 1990; World Bank 1960), COPX (2010), Fed funds (in tool). Copper 6m change in tool.
- Confidence: high

### Copper structural tightness (EVs, infrastructure)
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "copper is in the tightest position well frankly I've ever even studied")
- Type: signal
- Rule as testable logic: IF LME+COMEX copper inventories (days of consumption) in bottom decile (proposed) THEN long copper on cyclical re-entry signals; size larger.
- Data needed: LME/COMEX inventories (not free long history; proxy: copper futures curve backwardation, CME HG spreads). Not in tool.
- Confidence: medium

### Gold and silver despite history of weak hard-landing performance (de-dollarization)
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "we own gold and silver right now they historically have not done well in hard Landings but given ... other countries have decided particularly autographies not to hold their reserves in dollars um I'm betting for the time being")
- Type: hedge
- Rule as testable logic: IF central-bank gold purchases rise (World Gold Council, proposed > 500t/yr) or foreign official Treasury holdings fall y/y AND fiscal deficit > 5% of GDP THEN hold gold (GLD) and silver (SLV) (proposed 10% combined) even in a hard-landing cut. Test gold in recessions overall vs after 2008.
- Data needed: gold (World Bank 1960; GLD 2004), silver (SLV 2006; World Bank 1960), TIC foreign official holdings (FRED FDHBFIN, 1970), WGC central bank buying (2000+). Not in tool.
- Confidence: medium (he says "could change my mind")

### Treasuries are the bad-outcome playbook, but only when yields offer a fat pitch
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "The Playbook I've always used if I expected a bad economic outcome is to own treasuries well with with 10-year yielding 350 ... and fed funds at five that's not exactly a fat pitch")
- Type: hedge
- Rule as testable logic: IF expecting recession (warnings on) AND 10y yield - Fed funds > 0 (positive curve, rates room to fall) THEN hold long Treasuries in de-risk; IF 10y < Fed funds by > 1 pp (deep inversion) THEN prefer T-bills over TLT (limited upside, inflation risk). Directly testable vs current TLT/bills switch.
- Data needed: DGS10, FEDFUNDS (both in tool via curve/funds). Curve 10y-2y in tool; 10y-funds not.
- Confidence: high

### Fat pitch: asymmetric short of 2-year yields at zero while money grows 40%
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "two years at 15 basis points with a money growing at 40 percent ... if you're dead wrong the two-year yield goes from 15 basis points to 10 basis points I thought at the time if I was right they would go to 200")
- Type: signal
- Rule as testable logic: IF 2y yield < 0.5% AND M2 y/y > 10% (proposed; he cites ~40% peak but money growth was ~25%) THEN short 2y Treasury futures / hold inverse short-duration (or avoid any bonds; hold bills/floating TFLO). Test 1950s-2021: forward 12m change in 2y yield.
- Data needed: FRED DGS2 (1976), M2SL (in tool), TBF/TBT inverse Treasury ETFs (2009), TFLO (2014). M2 growth in tool.
- Confidence: high

### Concentrate on fat pitches, otherwise stand aside; keep gross low in uncertainty
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "I like concentrated bets I like fat pitches and then the swing big and I also like when you don't see a fat pitch stand there and let the pitches go by"; "keep your gross low be open-minded")
- Type: position sizing/risk
- Rule as testable logic: Size by signal agreement: IF 3 of 3 dials agree (e.g. Fed tight + warnings + trend down) THEN full position change (0% or 100% stocks); IF signals mixed THEN reduce gross toward a neutral 50-60% equity with no tactical tilts. Test conviction-scaled vs linear sizing.
- Data needed: existing dials.
- Confidence: high

### Preserve capital before the opportunity: avoid a 20-30% loss
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "I don't want to miss those opportunities by blowing my money now and having some 20 or 30 percent loss where my head is all screwed up")
- Type: position sizing/risk
- Rule as testable logic: Portfolio drawdown limit: IF portfolio drawdown > 15% (proposed) THEN halve risk until drawdown recovers to < 7.5% or a re-entry signal fires. Test effect on max drawdown and recovery time.
- Data needed: portfolio equity curve.
- Confidence: medium

### Bear-market rallies make shorting dangerous
- Source: Kiril Sokoloff / Stanley Druckenmiller — Sohn 2023 (quote: "you've been saying for a year that being short is very dangerous because of these brutal bear Market ballots"; "I wouldn't go crazy on the short side for that reason either")
- Type: conflict/caveat
- Rule as testable logic: In de-risk regimes go to cash/bonds, not net short (no SH/SDS) unless trend AND macro both negative; cap inverse exposure at 20% (proposed). Test cash vs inverse ETFs in 2000-02, 2008, 2022 bear markets.
- Data needed: SH (2006), S&P daily. Not in tool.
- Confidence: high

### Short-dollar position on fiscal/reserve-currency grounds
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "I don't have some massive short dollar position ... but it is a position that will move the needle at my firm"); Sokoloff: "the dollar could certainly fall 25 percent to reach equilibrium"
- Type: action/instrument
- Rule as testable logic: IF deficit/GDP > 5% outside recession AND Fed expected to ease (2y yield < Fed funds by > 0.5 pp, proposed) THEN short USD (UDN, long EUR/JPY/gold) for 6-12 months; equity tilt to ex-US (EFA/EEM). Dollar vs 12m high and dollar 12m change in tool.
- Data needed: DXY/broad dollar (FRED DTWEXBGS 2006; DTWEXM 1973-2019), UDN (2007), FX rates (FRED DEXUSEU etc., 1971+). Dollar measures in tool.
- Confidence: medium

### Curse of the reserve currency: no market check on fiscal recklessness
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "when you're the reserve currency you can continue digging your own grave"; "all this craziness we just talked about went on in 21 and 22 the dollar actually went up any other place the market would have rejected it")
- Type: conflict/caveat
- Rule as testable logic: Don't expect the dollar to fall promptly on fiscal deterioration; require a trigger (Fed easing, foreign official selling). Test: correlation of deficit changes with dollar 12m change (expected weak). Compare UK 2022 gilt shock (non-reserve) as contrast.
- Data needed: deficit (FRED), dollar (in tool), UK gilts (FRED IRLTLT01GBM156N).
- Confidence: medium

### De-dollarization: reserve managers selling Treasuries after the Russia freeze
- Source: Kiril Sokoloff — Sohn 2023 (quote: "after the freezing of Russian foreign exchange Reserves there's been steady liquidation of barn Central Bank holdings")
- Type: signal
- Rule as testable logic: IF foreign official holdings of Treasuries (TIC/H.4.1 custody holdings) fall y/y > 3% (proposed) THEN term premium up / dollar down: shorten duration, overweight gold.
- Data needed: Fed H.4.1 custody holdings for foreign official accounts (FRED WMTSECL1, 2002), TIC. Term premium in tool.
- Confidence: medium

### Fiscal tsunami: entitlements + interest > taxes by 2040 -> interest rates not at 4%
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "in 2040 um entitlements plus centers expense using CBO estimates which I think are ridiculously low on interest rates ... become greater than taxes"; "if you have that situation interest rates aren't going to be four")
- Type: regime map
- Rule as testable logic: IF federal net interest / tax receipts > 20% (proposed; ~18% in 2024) THEN structural underweight long Treasuries (prefer bills/5y) and hold real assets; test interest/revenue vs term premium.
- Data needed: FRED A091RC1Q027SBEA (interest payments, 1947), W006RC1Q027SBEA (federal receipts). Term premium in tool; ratio not.
- Confidence: medium

### Fiscal space determines policy response: crowding out of private investment
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "there's not the room to move in on the monetary or the fiscal front in a reasonable manner that there's been going into other Cycles we basically wasted all our bullets"; "it's going to squeeze out government investment is going to squeeze out private investment")
- Type: regime map
- Rule as testable logic: IF entering a recession with debt/GDP > 100% and deficit > 5% (proposed) THEN expect weaker policy rescue: delay stock re-entry (require trend confirmation: S&P above 10m average for 2 months).
- Data needed: FRED GFDEGDQ188S, FYFSGDA188S. Not in tool.
- Confidence: medium

### Debt ceiling technical default = a market event (small), fiscal path = the tsunami
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "I hope um we don't have a technical default I think it would be stupid I think it would be a market event")
- Type: hedge
- Rule as testable logic: IF debt-ceiling X-date within 4 weeks without deal THEN avoid T-bills maturing near X-date; hold slightly longer bills or govt MMF; stocks: short-term hedge (puts) only. Event dates: 2011, 2013, 2023.
- Data needed: 1m bill yield (FRED DTB4WK 2001), event dates. Not in tool.
- Confidence: low

### Valuation + margins + fiscal => flat stocks over 10 years ("lost decade" but tradeable)
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "when I look at marketed 20 times earnings when I look at margins as high as they are when I look at the fiscal challenges ... it's it's hard for me to Envision stocks being higher in 10 years")
- Type: regime map
- Rule as testable logic: IF forward P/E > 20 (or CAPE top decile, in tool) AND profit margin (corporate profits/GDP) top decile THEN expected 10y real return ~0: favor tactical rotation (sector/commodity rallies like 1970-72, 1975-77) over buy-and-hold; allow more frequent de-risking. Test 10y forward returns conditioned on CAPE x margins.
- Data needed: Shiller CAPE (in tool), FRED CP/GDP (profit margin proxy, 1947). Margins not in tool.
- Confidence: high

### Secular flat markets still have big rallies (1968-82: oil/chemicals 1970-72, 1975-77)
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "you could have made a lot of money um in the 68 to 82 period being long the stock market and being long the right stocks at the right time")
- Type: action/instrument
- Rule as testable logic: In stagflation/flat-market regimes, use sector momentum among industry ETFs (top 3 of 20 by 6m return, proposed) rather than broad index; test on Ken French 30 industries 1966-82, 2000-12.
- Data needed: Ken French 30/49 industry portfolios (1926). Industry breadth in tool.
- Confidence: medium

### Buy the new technology after the burst (AI like internet 2001-02)
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "it could be a beautiful opportunity in a hard Landing just like oh 102 were a beautiful opportunity when the tech Bubble Burst going forward for companies who benefit from the internet")
- Type: re-entry/exit
- Rule as testable logic: IF tech (XLK/QQQ) falls > 40% from high (proposed) AND trend re-turns up (QQQ above 10m average) THEN re-enter tech overweight. Chips vs 12m high in tool.
- Data needed: Nasdaq-100 (1985), QQQ (1999), Ken French BusEq. Chips vs 12m high in tool.
- Confidence: medium

### Biotech: underperformed 3-5 years, candidate for recovery
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "biotech has been a big underperformer in the last three to five years and there are tremendous things going on in cancer")
- Type: signal
- Rule as testable logic: IF a growth sector's 3-5y relative return vs S&P is in its bottom decile (proposed) THEN eligible for overweight after a hard landing when trend turns up. Test long-horizon reversal on sector ETFs (XBI 2006, IBB 2001).
- Data needed: XBI, IBB, NASDAQ Biotech (1993). Not in tool.
- Confidence: low

### Fed independence risk (5-10% chance) in a bad hard landing
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "I think there's a five to ten percent chance if the hard lending got really bad")
- Type: conflict/caveat
- Rule as testable logic: IF political attacks on the Fed intensify (proposed: Fed chair removal attempt or policy rate cut with core CPI > 3.5%) THEN raise inflation regime odds: hold gold/TIPS, shorten duration, underweight dollar. Not backtestable (event).
- Data needed: event list; breakevens (FRED T5YIE 2003). 5y inflation expectations in tool.
- Confidence: low

### Volcker-style cleansing recession -> 20-30 years of prosperity
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "volcker intentionally threw us into a recession he raised rates to 20 percent ... we got 20 to 30 years of prosperios we took the pain")
- Type: regime map
- Rule as testable logic: IF real policy rate (Fed funds - core CPI y/y) > +3 pp during a recession (proposed) THEN after the recession ends, hold stocks and long bonds aggressively (disinflationary bull) for 5+ years; IF policy instead eases with real rate < 0 (Japan route) THEN expect "permanent malaise" (lower equity weights).
- Data needed: FEDFUNDS, core CPI (in tool), NBER recession dates (FRED USREC). Real policy rate not in tool (real 10y is).
- Confidence: medium

### Energy-transition bridge keeps oil relevant 10-15 years; Saudi realignment
- Source: Stanley Druckenmiller — Sohn 2023 (quote: "obviously we have an energy transition no matter what you think about climate there's a bridge of at least 10 to 15 years and we don't want him to be in bed with China")
- Type: regime map
- Rule as testable logic: Keep oil/energy (XLE, USO/BNO) in the investable inflation-hedge set; no rule beyond inclusion. Low.
- Data needed: XLE, Brent. Oil 6m change in tool.
- Confidence: low

---

## File 5: Mike Pompeo, "Mike Pompeo, Former US Secretary of State & CIA Director, on Geopolitics, Leadership & the Economy" (Money Maze, Jul 2023)

Note: mostly political/leadership content; few market statements. Rules below are geopolitics-to-asset mappings inferred from his framing; confidence is low unless stated.

### Perceived US weakness invites aggression (deterrence model)
- Source: Mike Pompeo — Money Maze (quote: "a model that doesn't permit the perception of weakness to creep into the bad guys minds"; "especially in the aftermath of Afghanistan ... this isn't the America I used to fear")
- Type: regime map
- Rule as testable logic: IF a visible US retreat event occurs (e.g. Afghanistan withdrawal Aug 2021) THEN raise geopolitical-risk regime for 12 months: overweight defense (ITA), energy (XLE), gold; underweight Europe/EM near conflict zones (e.g. Eastern Europe, Taiwan EWT, Korea EWY). Test with GPR index rises after such events (small sample).
- Data needed: Caldara-Iacoviello GPR (1900+), ITA (2006), GLD, VGK, EWT, EWY. Not in tool.
- Confidence: low

### Russia war is not over; Putin's goals extend to the Baltics
- Source: Mike Pompeo — Money Maze (quote: "don't think for a moment this is over or is going to be over or that the Russians are intent on capitulating"; "it was a deep play for political control in the Baltic states")
- Type: hedge
- Rule as testable logic: While the Russia-Ukraine war continues, keep a European energy/defense hedge: overweight European defense (EUAD, 2023) and US defense (ITA), natural gas exposure (UNG/TTF) vs European equities. Not backtestable.
- Data needed: ITA, EUAD (2023), Dutch TTF gas (World Bank monthly Europe gas from 1960s), Henry Hub (FRED MHHNGSP 1997). Not in tool.
- Confidence: low

### Regime collapse comes suddenly ("you wake up one morning and the world broke")
- Source: Mike Pompeo — Money Maze (quote: "most time leaders bail like Putin isn't because oh we could see the trajectory ... you wake up one morning and the world broke")
- Type: conflict/caveat
- Rule as testable logic: Geopolitical breaks are not forecastable from trends; use standing hedges (gold, small tail-put budget) rather than event timing. Supports a constant small hedge allocation test (e.g. 5% gold always).
- Data needed: gold, put index (CBOE PPUT). Not in tool.
- Confidence: medium

### China threat is economic; reciprocity => trade/investment restrictions
- Source: Mike Pompeo — Money Maze (quote: "the threat from the Chinese Communist party is centrally an economic threat today"; "economically this looks pretty straightforward with a central thesis of reciprocity")
- Type: regime map
- Rule as testable logic: IF US-China restrictions escalate (tariff rate increases, delisting threats, outbound investment rules; event list or Trade Policy Uncertainty index spike > 2 s.d.) THEN underweight China (FXI/KWEB) vs allied Asia for 6-12 months. Test using Baker-Bloom-Davis Trade Policy Uncertainty index.
- Data needed: EPU Trade Policy Uncertainty (policyuncertainty.com, 1985+), FXI, KWEB (2013). Not in tool.
- Confidence: medium

### Friend-shoring: allied Asian economies (Japan, Korea, India, Australia, Singapore, Malaysia) integrate with the US
- Source: Mike Pompeo — Money Maze (quote: "they had Prime Minister Modi in town they had the president of South Korea ... Australia South Korea Japan Singapore Malaysia these are Big economies and when we get those economies all working together")
- Type: action/instrument
- Rule as testable logic: IF US-China decoupling escalates (as above) THEN overweight allied Asia basket (EWJ, EWY, INDA, EWA, EWS, EWM) vs China (MCHI) for 12-36 months. Test relative return since 2018 tariff start.
- Data needed: iShares country ETFs (EWJ 1996, EWY 2000, INDA 2012, EWA 1996, EWS 1996, EWM 1996), MSCI country indexes (1988+). Not in tool.
- Confidence: low

### Inflation erodes property (savings) — political priority
- Source: Mike Pompeo — Money Maze (quote: "no government's going to come take that away from me or diminish it or worse yet allow inflation to make it worthless")
- Type: conflict/caveat
- Rule as testable logic: None directly; context for inflation-hedge allocation. Skip as a rule.
- Data needed: none.
- Confidence: low

### Iran deterrence (Soleimani strike) did not create "world war three"
- Source: Mike Pompeo — Money Maze (quote: "how we were about to lose deterrence against Iran and we figured out a theory without putting 20 000 of our soldiers at risk without creating world war three")
- Type: hedge
- Rule as testable logic: Event test: targeted US/Israel strikes on Iran (Jan 2020, Apr/Oct 2024, Jun 2025) -> oil spike fades within 1 month (proposed); do not chase oil after strike headlines. Event study on Brent 1-20 days after.
- Data needed: Brent daily (FRED DCOILBRENTEU 1987), event dates. Oil 6m change in tool.
- Confidence: low

---

## File 6: Ajay Banga, "Ajay Banga - President of World Bank - Podcast - In Good Company - Norges Bank Investment Management" (Oct 2023)

Note: almost entirely institutional/leadership content. Few investable statements.

### Opaque sovereign debt (China bilateral loans, undisclosed terms) -> slow, haircut-heavy restructurings
- Source: Ajay Banga — In Good Company (NBIM) (quote: "some countries either have covenants that don't are not similar or in some cases have actually asked the country that received the loan to not disclose the terms so the first real issue is transparency"; Zambia: "people have to take a haircut including the commercial creditors")
- Type: signal
- Rule as testable logic: IF a frontier/EM sovereign has a large share of external debt owed to China/non-Paris-Club bilateral lenders (proposed > 20%) AND its EMBI spread > 1,000 bp (distressed) THEN avoid its hard-currency bonds and equities; the frontier sovereign bond sleeve (EMB/high-yield sovereigns) should exclude such names. Test: recovery values and time-to-resolution after default (Zambia 2020-24, Sri Lanka, Ghana).
- Data needed: World Bank International Debt Statistics (creditor composition, 1970+), JPM EMBI spreads (not free; proxy EMB ETF 2007, EMHY 2012), AidData China lending (2000+). Not in tool.
- Confidence: medium

### Multilateral leverage needs private capital (blended finance)
- Source: Ajay Banga — In Good Company (NBIM) (quote: "there's not enough in these you have to get the private sector involved in a way that makes sense for the private sector")
- Type: conflict/caveat
- Rule as testable logic: No direct rule; context that EM infrastructure financing depends on private flows — EM performance tied to global risk appetite/dollar (use dollar 12m change, in tool, as EM driver).
- Data needed: none new.
- Confidence: low

### Digital ID / payments -> formalization and financial inclusion in EM (India)
- Source: Ajay Banga — In Good Company (NBIM) (quote: "less cash in the economy leads to more transparency in an economy"; "a digital ID is foundational")
- Type: regime map
- Rule as testable logic: Structural tilt only: countries with rapid digital-payment adoption (India UPI) may justify a long-run overweight (INDA) — not testable as a timing rule. Proposed check: India equity premium vs EM since 2016 demonetization/UPI launch.
- Data needed: MSCI India (1993), INDA (2012), EEM. Not in tool.
- Confidence: low

### AI benefits for poorer countries lag (infrastructure gap)
- Source: Ajay Banga — In Good Company (NBIM) (quote: "poorer countries do they have the infrastructure to really benefit in the short term no so not in the short term")
- Type: conflict/caveat
- Rule as testable logic: AI productivity gains accrue first to developed/tech-heavy markets (US, Taiwan, Korea); do not expect a near-term AI growth premium in frontier markets. No trading rule.
- Data needed: none.
- Confidence: low

### No debt/leverage survives a crash; concentrated single-employer stock is risky
- Source: Ajay Banga — In Good Company (NBIM) (quote: "the value of that stockholding went from the tens of millions to the single digit ... fortunately I had no loans and no debt so that is very helpful and and a matter of stability")
- Type: position sizing/risk
- Rule as testable logic: Portfolio rule: no leverage in the strategy (gross exposure <= 100%); avoid concentration in a single sector (financials 2008). Test: max sector weight cap (e.g. 30%) in sector-tilt variants.
- Data needed: none new.
- Confidence: medium

---

## File 7: Pablo Calderini (Graham Capital), "Navigating a New World Order- Macro Strategies for Uncertain Times" (posted Jan 2025; content recorded ~Mar 2023, during SVB / debt-ceiling period)

### Regime shift: from "Fed put" low-inflation decade to inflation-shock regime
- Source: Pablo Calderini — Navigating a New World Order (quote: "there was not one crisis that the FED uh was not able to accommodate"; "now the idea that inflation is a secular low inflation ... and that the risks are only the serial over bound ... are gone")
- Type: regime map
- Rule as testable logic: IF core CPI y/y > 3% (proposed) THEN classify as "no Fed put" regime: shocks are not met with easing, so (a) stock re-entry after drawdowns needs trend confirmation, (b) long Treasuries are not a reliable hedge, (c) raise weight in trend/commodities. IF core CPI < 2.5% THEN "Fed put" regime: buy dips, Treasuries hedge.
- Data needed: core CPI (in tool), S&P, TLT. In tool partly.
- Confidence: high

### Hiking-cycle surprise: actual hikes minus what the curve priced at cycle start
- Source: Pablo Calderini — Navigating a New World Order (quote: "you can see the curve peaking at three percent that means that the FED height 300 basis points more than what the markets were pricing uh that's that is a huge huge shock for for markets")
- Type: signal
- Rule as testable logic: Monetary surprise = (Fed funds now - Fed funds at cycle start) - (rate the futures/2y yield implied at cycle start for now). IF surprise > +100 bp (proposed) THEN fragile market: cut stocks and credit for 6-12 months. Proxy: 2y yield 12m change minus the 1y-forward implied by the curve 12 months earlier (from 1y and 2y yields).
- Data needed: FRED DGS1, DGS2 (1976), FEDFUNDS; fed funds futures (CME, not free long history). Not in tool (Fed funds 12m change is).
- Confidence: high

### Size and speed of hiking cycle (2022: double the average, half the time)
- Source: Pablo Calderini — Navigating a New World Order (quote: "the current height is double the average of the previous four hiking Cycles more importantly in in half the speed")
- Type: signal
- Rule as testable logic: IF cumulative hikes in the cycle > 300 bp within 18 months (proposed) THEN high odds of financial accident (1994 tequila, 2006 GFC, 2023 banks): cut equity, avoid credit, hold bills for 12-24 months.
- Data needed: FEDFUNDS / DFEDTARU (1954). Fed funds 12m change in tool.
- Confidence: medium

### Core inflation drives asset losses; headline/energy inflation is mean-reverting noise
- Source: Pablo Calderini — Navigating a New World Order (quote: "a very clear link between core inflation as always a massive negative shock for us at prices while NRC or headline inflation X score uh being almost unimportant"; "energy inflation ... very mean reversing")
- Type: signal
- Rule as testable logic: Use core-inflation surprises (core CPI 3m annualized minus 12m, in tool) as the inflation warning; do NOT cut stocks on headline/energy-only inflation spikes (headline - core > 2 pp with core stable). Test: equity forward 6m return conditioned on core vs non-core inflation shocks since 1960.
- Data needed: CPIAUCSL, CPILFESL (FRED, 1957). Core inflation in tool.
- Confidence: high

### Inflation-equity link is non-linear (sign flips by regime)
- Source: Pablo Calderini — Navigating a New World Order (quote: "if we are in a deflationary period higher inflation actually can be very positive for asset prices if we're in a in a period of high inflation higher inflation can be terrible")
- Type: regime map
- Rule as testable logic: IF core CPI y/y < 1.5% (proposed) THEN rising inflation is bullish (buy stocks/cyclicals on inflation upticks); IF core CPI > 3% THEN rising inflation bearish. Implement as interaction term in warnings (inflation warnings only active when core > 2.5%).
- Data needed: core CPI (in tool).
- Confidence: high

### Stock-bond correlation positive in high-inflation eras; long-run average ~0
- Source: Pablo Calderini — Navigating a New World Order (quote: "the long run correlation between stocks and bonds is really around zero ... High inflation usually drives correlation up"; "it's hard to think we're going to go back to the the great days of minus 50 correlation")
- Type: hedge
- Rule as testable logic: IF trailing 36m stock-bond correlation > 0 OR core CPI > 3% THEN replace long Treasuries in the de-risk sleeve with trend-following / T-bills / gold. (Tool already uses corr < 0 for TLT; adds inflation condition.)
- Data needed: stock-bond correlation (in tool), core CPI (in tool).
- Confidence: high

### Stocks are riskier in the long run than history suggests (parameter uncertainty) -> hold less equity
- Source: Pablo Calderini — Navigating a New World Order (quote: "when you do proper calculations stocks are a lot more volatile in the long run ... a five percent variance roughly means 22 percent it's a standard deviation"; "you should own a lot less equities")
- Type: position sizing/risk
- Rule as testable logic: Volatility assumption for sizing: use 20-22% long-horizon equity vol (not 15-17%) when computing risk-parity / vol-target weights. Test vol-targeted equity sleeve (target 10% portfolio vol) vs fixed weights.
- Data needed: S&P returns; VIX (in tool).
- Confidence: medium

### Add trend-following / macro: negative conditional correlation, positive skew
- Source: Pablo Calderini — Navigating a New World Order (quote: "our correlation to equities when equities are doing really badly it's negative"; "adding 20 macro ... almost cuts the worst roll down from minus 36 percent to minus 29")
- Type: hedge
- Rule as testable logic: Hold 20% of the portfolio in a cross-asset trend-following sleeve (12m time-series momentum across equity indexes, bonds, FX, commodities; ETF proxies DBMF/KMLM/CTA) alongside the equity/bond mix. Expected: Sharpe/IR 0.66 -> 0.75; max drawdown -36% -> -29% (his numbers, last 20y, 60/40 + 20% macro).
- Data needed: SG Trend Index / Barclay CTA (1980+), AQR Time Series Momentum factor data (free, 1985+, monthly), HFRI Macro (1990), DBMF (2019), KMLM (2020); or build TSMOM from futures-proxy ETFs. Not in tool.
- Confidence: high

### Skewness and conditional correlation matter more than Sharpe in portfolio construction
- Source: Pablo Calderini — Navigating a New World Order (quote: "we as investors uh tend to focus too much on Sharp ratios and returns and standard deviations but really skewness and conditional correlation are super important")
- Type: position sizing/risk
- Rule as testable logic: Evaluation criterion: report each candidate sleeve's return during the worst 10% of S&P months (conditional correlation) and skew; prefer sleeves with positive return in those months even at lower Sharpe.
- Data needed: none new.
- Confidence: high

### Treasury "20-sigma" moves (Mar 2023) -> robust risk limits
- Source: Pablo Calderini — Navigating a New World Order (quote: "what happened in threshold yields was uh really is 20 Sigma event that was very hard to forecast"; "shocks that can seem to happen more frequently and much more violently than before")
- Type: position sizing/risk
- Rule as testable logic: Cap any single bond/rate position by stress loss (e.g. 3-sigma using max historical daily move, not recent vol); when MOVE index > 150 (proposed) halve duration positions.
- Data needed: ICE BofA MOVE index (1988; Yahoo ^MOVE ~2002+), FRED DGS2 daily. Not in tool (VIX is).
- Confidence: medium

### Equities in the "wrong quadrant": falling earnings + high multiples
- Source: Pablo Calderini — Navigating a New World Order (quote: "equities uh are in the complete wrong quadrant right you have earnings that have to come down and you have multiples that are too high for the current context")
- Type: signal
- Rule as testable logic: IF forward EPS revisions negative (or trailing EPS 6m change < 0) AND P/E above its 10y median (or CAPE top third, in tool) AND real 10y yield > 1% (in tool) THEN underweight/short S&P for 3-6 months.
- Data needed: S&P EPS (Shiller monthly 1871; S&P quarterly), CAPE and real 10y (in tool). EPS revisions not free.
- Confidence: medium

### Market pricing cuts vs sticky core inflation: both resolutions are bad for equities
- Source: Pablo Calderini — Navigating a New World Order (quote: "either core inflation will continue to be sticky and the FED will have to hike even more I mean remember the markets are pricing cats"; "core inflation ... will come down if we have a big spike in the unemployment rate")
- Type: signal
- Rule as testable logic: IF 2y yield < Fed funds by > 50 bp (market pricing cuts) AND core CPI 3m annualized > 4% (proposed) THEN underweight equities (either hikes repriced or recession); hold bills.
- Data needed: DGS2, FEDFUNDS, core CPI (in tool partly).
- Confidence: medium

### Long euro on policy divergence (Fed constrained by banks, ECB hawkish)
- Source: Pablo Calderini — Navigating a New World Order (quote: "we actually like the Euro we feel that with the banking issues in the U.S while the FED will not cut they will also be precluded from massively hiking while the ecv ... very hawkish")
- Type: action/instrument
- Rule as testable logic: IF (ECB policy rate expected change - Fed expected change) rises, proxied by German 2y minus US 2y yield 3m change > +30 bp (proposed) THEN long EUR/USD (FXE) for 3 months. Test rate-differential momentum for EUR, JPY, GBP.
- Data needed: German 2y (Bundesbank/ECB SDW, 1990s), US 2y (FRED DGS2), EUR/USD (FRED DEXUSEU 1999), FXE (2005). Not in tool.
- Confidence: medium

### Yen extremely undervalued; BoJ exit from yield-curve control -> long yen (conflicts with Bass's earlier short-yen logic)
- Source: Pablo Calderini — Navigating a New World Order (quote: "where I will not really address yield curve control but eventually that's coming Ian is extremely extremely undervalued so we we like Yen")
- Type: action/instrument
- Rule as testable logic: IF yen real effective exchange rate in its bottom decile (proposed) AND BoJ signals tightening (JGB 10y yield 3m change > +20 bp) THEN long JPY (FXY) vs USD for 6-12 months; also long yen as a crisis hedge. Conflict: Bass (debt 265% -> currency is the escape valve, short yen); resolve by conditioning on BoJ direction (easing -> short yen; tightening from undervalued -> long yen).
- Data needed: BIS real effective exchange rate Japan (FRED RBJPBIS, 1994; RNJPBIS), JGB 10y (FRED IRLTLT01JPM156N, 1989), USD/JPY (FRED DEXJPUS, 1971), FXY (2007). Not in tool.
- Confidence: medium

### Gold: falling real yields via rising breakevens, debt-ceiling fights
- Source: Pablo Calderini — Navigating a New World Order (quote: "real rates eventually will come down we think breakevens are too and it doesn't have it doesn't have to be because the FED cats ... that's normally good for gold"; "debt ceiling negotiation in the U.S that usually is also fairly bullish for gold")
- Type: action/instrument
- Rule as testable logic: IF real 10y yield (in tool) falls over 3 months (proposed < -25 bp) OR 10y breakeven rises > 25 bp while nominal 10y flat THEN long gold (GLD) for 3-6 months. Event: debt-ceiling X-date within 3 months -> overweight gold.
- Data needed: FRED DFII10 (2003), T10YIE (2003), gold (GLD 2004, World Bank 1960). Real 10y in tool; breakeven 10y not (5y expectations is).
- Confidence: high (gold vs real rates), low (debt ceiling)

### Be tactical: cut positions fast when the thesis is not working
- Source: Pablo Calderini — Navigating a New World Order (quote: "we are not shy to cut positions or get off the way if we don't see our thesis working"; "we can talk in a month and have completely different views")
- Type: re-entry/exit
- Rule as testable logic: For tactical overlays (FX, gold, short equity), use a stop: exit if position loses > 1 s.d. of 3m return (proposed) or if 3m trend turns against it; review monthly.
- Data needed: prices.
- Confidence: medium

### Quant macro: four sub-strategies (trend, value/long-run reversion, carry, fundamentals)
- Source: Pablo Calderini — Navigating a New World Order (quote: "one is based on on on Trend the other one is based on value or long-running reversion the other one is based on Curry and and the last one ... is based on what you call macro or fundamentals")
- Type: action/instrument
- Rule as testable logic: Build a cross-asset sleeve across country equity indexes (EWJ, EWG, EWU, EWY, EWZ, FXI, INDA...), 10y bond futures proxies, currencies, commodities: (1) trend = 12m minus 1m return sign; (2) value = 5y reversal; (3) carry = yield/roll differential (bond yield minus cash; FX interest differential; commodity futures basis); (4) fundamentals = growth/inflation momentum. Equal risk-weight. Note: he warns naive carry (long all positive carry) is not used: "we don't like to buy go along ... that has a positive carry but we try to come up with ideas of equilibrium".
- Data needed: AQR "Value and Momentum Everywhere" and "Century of Factor Premia" data (free, 1920s/1970s+), country 10y yields (FRED IRLTLT01 series, OECD 1950s+), FX rates (FRED H.10 1971), interbank rates (FRED IR3TIB01 series). Not in tool.
- Confidence: high

### Fundamental signals are non-linear and regime-dependent
- Source: Pablo Calderini — Navigating a New World Order (quote: "when you're looking at fundamentals and how they affect markets it's highly non-linear it depends on what regime you're on")
- Type: conflict/caveat
- Rule as testable logic: Evaluate every indicator conditional on regime (inflation high/low, Fed tightening/easing) rather than with a single linear beta; the tool's "only while Fed tightening" gate is consistent. Test interactions explicitly.
- Data needed: existing.
- Confidence: high

---

## File 8: Pablo Calderini (Graham Capital), "Resilient Strategies- Tailwinds in Left-Tail Scenarios" (Jun 2024)

### "Bad news is good news" regime (2010-2020) vs inflation regime
- Source: Pablo Calderini — Resilient Strategies (quote: "bad news triggered a reaction, a benign monetary policy reaction by a central bank that then led assets to go up"; 2022: "not only they could not accommodate that shock ... they actually had to tighten policy")
- Type: regime map
- Rule as testable logic: IF core PCE y/y < 2.5% (proposed) THEN buy equity dips on weak data (growth shocks met by easing); IF core PCE > 3% THEN weak data is not rescued: keep cuts until trend repairs. Same as File 7 regime rule; use core PCE as the Fed's target measure.
- Data needed: FRED PCEPILFE (1959). Core CPI in tool; core PCE not.
- Confidence: high

### Dovish pivot with decent growth = very benign for equities
- Source: Pablo Calderini — Resilient Strategies (quote: "the Fed decided to become very dovish ... in a context where equities, where growth was actually quite decent ... that's a really benign backdrop for equities")
- Type: re-entry/exit
- Rule as testable logic: IF the Fed signals/starts cuts (2y yield falls > 50 bp in 3 months, proposed) AND no recession signal (Sahm rule off, in tool; ISM/claims fine) THEN full equity weight for 6-12 months (soft-landing cut cycle: 1995, 1998, 2019, Dec 2023). IF cuts start with Sahm rule triggered THEN recessionary cut (2001, 2007): stay defensive.
- Data needed: DGS2, FEDFUNDS, Sahm rule (FRED SAHMREALTIME, in tool). 
- Confidence: high

### Volatility at lows across assets while geopolitical risk is high -> left tail is cheap to hedge
- Source: Pablo Calderini — Resilient Strategies (quote: "So bottom at 13, right now is at around 16 ... the move index ... also made a low ... FX vol ... it's also at a really low level. So we are, according to this, living in a perfect world")
- Type: hedge
- Rule as testable logic: IF VIX < 14 AND MOVE < 100 (proposed) AND GPR index above its 5y average THEN buy cheap tail hedges (3-6m 10% OTM SPY puts, budget 0.5-1% of portfolio per year, proposed) or VIX calls; do not cut stocks on low vol alone.
- Data needed: VIX (in tool), MOVE (^MOVE Yahoo 2002+; ICE 1988), JPM global FX vol (not free; proxy CBOE EVZ 2008), GPR index (free). Option cost proxy: CBOE PPUT index (1986).
- Confidence: medium

### Fast rallies create the left tail
- Source: Pablo Calderini — Resilient Strategies (quote: "usually when stock prices go up this much, they always create the left tail ... They just went up a thousand points, they can easily move back down that much")
- Type: signal
- Rule as testable logic: IF S&P 6m return > +20% (proposed) with low realized vol THEN expect larger drawdowns on shocks: add hedges rather than cut. Rally speed is already in tool.
- Data needed: S&P (in tool).
- Confidence: medium

### Taiwan blockade/invasion = biggest market shock ever (March 2020-like or worse)
- Source: Pablo Calderini — Resilient Strategies (quote: "China's blockading, invading Taiwan ... I think that that would be the biggest shock financial markets has ever seen ... the level of world that we saw in March 2020. I think maybe even more")
- Type: hedge
- Rule as testable logic: Scenario playbook (agrees with Bass): on a blockade/invasion event, immediately move equity to the de-risk mix; long USD, JPY?, gold, US Treasuries (if inflation low), long VIX; zero EWT/FXI/SMH/EWY. Not backtestable; size hedges by GPR rise.
- Data needed: GPR, event. Not in tool.
- Confidence: medium

### Israel-Iran direct exchanges crossed a Rubicon; accident risk in "war games"
- Source: Pablo Calderini — Resilient Strategies (quote: "having had both Israel and Iran for the first time launch attacks on each other from their own territories, it's a Ruby conduct has been crossed ... there's always the potential for something going wrong")
- Type: hedge
- Rule as testable logic: IF Middle East direct state-on-state exchange occurs THEN hold a small oil call / energy overweight (XLE +5%, proposed) for 3 months as a tail hedge; test Brent and XLE after Apr 2024, Oct 2024, Jun 2025 events.
- Data needed: Brent daily, XLE, event dates. Oil 6m change in tool.
- Confidence: low

### Core PCE re-acceleration (3m annualized > target) -> renewed Fed hike tail risk
- Source: Pablo Calderini — Resilient Strategies (quote: "The 4% core PCE inflation annualizes to 5% ... if we were to stay here, then core inflation, core PCE inflation goes back to 5%. That would actually trigger another Fed hike")
- Type: signal
- Rule as testable logic: IF core PCE 3m annualized > 4% (proposed) after having fallen below 3% THEN reduce duration (bills not TLT) and trim equities by one third for 3-6 months. Core inflation 3m vs 12m in tool (CPI version).
- Data needed: FRED PCEPILFE (1959). Partly in tool.
- Confidence: medium

### AI earnings are real (unlike 2000 internet): valuation alone not a sell
- Source: Pablo Calderini — Resilient Strategies (quote: "earnings are growing strongly in the US. AI is a reality. It's much more of a reality than what the internet was in 2002 when companies made absolutely no money")
- Type: conflict/caveat
- Rule as testable logic: Condition valuation warnings (CAPE, market cap/GDP, in tool) on earnings momentum: IF S&P trailing EPS y/y > +10% THEN suppress valuation-based cuts. Conflicts with Druckenmiller's 20x earnings/margins worry.
- Data needed: S&P EPS (Shiller monthly). Not in tool.
- Confidence: medium

### Climate-driven commodity spikes (cocoa x4): weather volatility in agriculture
- Source: Pablo Calderini — Resilient Strategies (quote: "if you follow the price of cocoa ... prices have moved up four times or more in the last few months ... the patterns are not so much that the planet is warmer is that oil is a lot more volatile")
- Type: regime map
- Rule as testable logic: Include agriculture/softs (DBA, cocoa NIB, coffee) in the commodity trend universe; trend-following, not mean reversion, on weather shocks (12m momentum). Not a stand-alone signal.
- Data needed: World Bank pink sheet monthly cocoa/coffee/grains (1960), DBA (2007). Not in tool.
- Confidence: low

### Stock-bond correlation: growth shocks -> negative; inflation shocks -> positive (bimodal)
- Source: Pablo Calderini — Resilient Strategies (quote: "when the main driver of macroeconomic shocks is growth ... the stock bond correlation tends to be negative ... But when inflation is high, it's the other way around"; "between 1960 and 1995, really stock bond correlation was very, very positive, reaching sometimes level of 60%")
- Type: regime map
- Rule as testable logic: Forecast next-12m stock-bond correlation sign from core inflation level: IF core CPI > 3% THEN expect positive correlation -> de-risk into bills/trend/commodities, not TLT. (Tool uses realized corr; test whether inflation-based ex-ante classification works better.)
- Data needed: core CPI, stock-bond corr (both in tool).
- Confidence: high

### Macro positioning template (2022): short rates, short stocks, short commodities, long dollar
- Source: Pablo Calderini — Resilient Strategies (quote: "in 2022, we were extremely short interest rates globally ... we were also short stocks. We were short commodities at the time. We were long the dollar because we saw the Fed being the most aggressive for central bank")
- Type: action/instrument
- Rule as testable logic: IF core inflation > 4% AND market-implied hikes < required (real policy rate < 0) THEN short duration (TBF/TBT or bills only), underweight equities, long USD (UUP); (commodities short only after the Fed begins aggressive hikes — proposed: Fed funds 6m change > +2 pp).
- Data needed: FEDFUNDS, core CPI (in tool), UUP (2007), TBF (2009). Not in tool (instruments).
- Confidence: medium

### Long the currency of the most hawkish/strongest-growth central bank
- Source: Pablo Calderini — Resilient Strategies (quote: "We are long the dollar because we are seeing this very strong US economy performing really well that will make the Fed less able to cut rates. So Europe ... the European central bank is about to have their independence day when they cut rates independent of the Fed")
- Type: action/instrument
- Rule as testable logic: Rank G10 currencies by 2y yield 3m change (proposed); long top vs bottom (or long USD vs EUR when US 2y - German 2y widening) for 3 months. Consistent with File 7 euro rule (rate-differential momentum).
- Data needed: G10 2y yields (FRED/OECD/national CBs), FX (FRED H.10). Dollar 12m change in tool.
- Confidence: medium

### Short Japanese rates (JGB yields to rise a lot); US curve steepeners
- Source: Pablo Calderini — Resilient Strategies (quote: "We have curve steepeners in the US. We are short rates in Japan where we think Japanese rates will go up a lot")
- Type: action/instrument
- Rule as testable logic: IF BoJ policy rate rising from ~0 and Japan core CPI > 2% (proposed) THEN short JGBs (avoid Japan duration; long yen exposure via hedged/unhedged choice). US: IF Fed expected to cut but fiscal deficit > 5% THEN steepener (long 2y IEI/SHY vs short 10-30y TLT, or just hold short end). Curve 10y-2y in tool.
- Data needed: JGB 10y (FRED IRLTLT01JPM156N), Japan CPI (FRED JPNCPIALLMINMEI), US 2s10s (in tool). Steepener instruments: STPP (discontinued); proxy SHY minus TLT duration-weighted.
- Confidence: medium

### Macro returns in equity drawdowns (1990, 2000-02, 2008, 2022; failed Q1 2020)
- Source: Pablo Calderini — Resilient Strategies (quote: "1990 there was a recession, equities went down 24%, then in macro made 6.7% ... 2000, 2002 ... down as much as 46%. Macro ... up almost 13% ... 2022 ... equities down 25% and macro ... up 10%"; "Q1 2020 ... macro down ... almost 2%")
- Type: hedge
- Rule as testable logic: Validate a macro/trend sleeve by its return in each S&P/MSCI World drawdown > 20%; require positive return in at least 3 of 4 historical drawdowns. Note fast V-shaped crashes (Q1 2020, 1987) are where trend/macro fail -> complement with a small put budget.
- Data needed: HFRI Macro (1990), SG Trend (2000), Barclay CTA (1980), MSCI World (1970). Not in tool.
- Confidence: high

### Macro is not a put: dynamic hedging is not guaranteed
- Source: Pablo Calderini — Resilient Strategies (quote: "We hopefully and expectedly do well in bad equity markets, but we are not guaranteed. It's not the same as buying equity puts that for sure will do well if equities go down")
- Type: conflict/caveat
- Rule as testable logic: Compare hedge types over 1990-2026: (a) 20% trend sleeve, (b) rolling 5% OTM puts (CBOE PPUT), (c) long Treasuries, (d) macro rule cuts (current tool). Measure cost in up years and payoff in crashes (fast vs slow).
- Data needed: CBOE PPUT/BXM (1986), SG Trend, TLT/Treasury TR. Not in tool.
- Confidence: high

### 60/40 + 20% macro (1990-2023): return 6.7% -> 7.2%, vol 10.2% -> 8.7%, IR 0.65 -> 0.83, max DD 36% -> 29%, beta 0.70 -> 0.55
- Source: Pablo Calderini — Resilient Strategies (quote: "the annualized returns on the portfolio go from 6.7 with no macro to 7.2 with 20% macro. Voll interestingly falls a lot, falls from 10.2 to 8.7 ... The information ratio goes up 30% from 0.65 to 0.83")
- Type: position sizing/risk
- Rule as testable logic: Benchmark to replicate: 48% stocks / 32% bonds / 20% trend-or-macro index, monthly rebalance; check the tool's stocks/bonds/bills switching beats this static blend after costs.
- Data needed: HFRI Macro or SG Trend; MSCI World; Bloomberg Agg (AGG 2003; VBMFX 1986). Not in tool.
- Confidence: high

### Macro trades best when central banks are in action
- Source: Pablo Calderini — Resilient Strategies (quote: "We are really, really focused on global central banks, monetary policy, something that we can anticipate well. When central banks are in action, we typically perform really, really well")
- Type: signal
- Rule as testable logic: IF |Fed funds 12m change| > 1.5 pp (proposed; in tool as 12m change) THEN raise the weight of trend/macro sleeve (e.g. 20% -> 30%); in static-policy periods lower it.
- Data needed: Fed funds (in tool), trend index.
- Confidence: medium

### Single stock as macro driver (Nvidia/AI) -> narrow leadership risk
- Source: Pablo Calderini — Resilient Strategies (quote: "NVIDIA became something very relevant because even though it looks like a micro issue, it really became a macro issue, right? Because it was driving markets")
- Type: signal
- Rule as testable logic: IF top-10 stock weight in S&P > 30% (proposed) or equal-weight S&P (RSP) underperforms cap-weight by > 10% over 12m THEN index is driven by a few names: treat AI/semis shock (SMH -25%, proposed) as a market-level warning. Narrow leadership is in tool.
- Data needed: RSP (2003), S&P 500 Equal Weight index (1990), SMH. Narrow leadership in tool.
- Confidence: medium

---

## File 9: "What is the fiscal rule-" (NBIM, Oct 2024; speaker is a former Norwegian finance minister and prime minister in 2000 who designed the rule, interviewed by NBIM; name not stated in transcript)

### Dutch disease: commodity windfalls spent at home overheat the economy
- Source: Former Norwegian PM — What is the fiscal rule (quote: "we were very afraid of uh what we referred to as Dutch disease uh to spend too much"; purpose "to separate earnings from spending and prevent overheating")
- Type: regime map
- Rule as testable logic: For commodity-exporter country ETFs (EWZ Brazil, EWW Mexico, ECH Chile, EWC Canada, EWA Australia, ENOR/NORW Norway, KSA, COLO Colombia, EZA South Africa): IF commodity terms of trade up > 20% y/y (proposed) AND the country has no binding fiscal rule / SWF saving (proposed list: Brazil, South Africa, Colombia) THEN expect boom-bust: overweight during the boom (commodity 12m momentum positive), exit faster (on first 3m commodity decline) than for rule-bound exporters (Norway, Chile).
- Data needed: IMF commodity terms-of-trade index by country (1980+), World Bank commodity prices (1960), MSCI country indexes (1988+), iShares country ETFs (1996-2011+). Not in tool.
- Confidence: low (inference from policy discussion)

### Spend only the expected real return (~3%) of the fund
- Source: Former Norwegian PM — What is the fiscal rule (quote: "the only thing we're going to spend was the financial return uh which we estimate to 3% in yield terms per year as as an average")
- Type: position sizing/risk
- Rule as testable logic: Withdrawal/benchmark assumption: a sustainable real return target ~3% for a global 70/30 portfolio; evaluate tool variants on real return above 3% and on drawdown relative to a 3% spending draw (probability of real capital loss over 10y).
- Data needed: CPI (in tool), portfolio returns.
- Confidence: medium

### Large equity-heavy fund makes the economy exposed to market swings (Norway: ~25% of budget)
- Source: Former Norwegian PM — What is the fiscal rule (quote: "now we have so much our wealth in the stock market then of course there can be big fluctuations uh that can have a impact on the Norwegian economy and that's a new risk")
- Type: conflict/caveat
- Rule as testable logic: Country link: Norway equities/NOK (NORW, ENOR; USD/NOK) are driven by oil AND global equities; test NOK vs (Brent 3m change, MSCI World 3m change) betas. Use NOK as a risk-on/oil proxy currency.
- Data needed: FRED DEXNOUS (1971), Brent (FRED), NORW (2010). Not in tool.
- Confidence: low

### An imperfect but credible rule beats a frequently changed "perfect" rule
- Source: Former Norwegian PM — What is the fiscal rule (quote: "perhaps it's better to have an imperfect rule which is credible than to always try to uh run for a more perfect rule but which is um constantly changed")
- Type: conflict/caveat
- Rule as testable logic: Process rule for Macro Compass itself: pre-register rules and change them rarely (already the practice); penalize strategy variants that require frequent parameter changes (overfitting). Evaluate robustness across parameter ranges, not best-in-sample.
- Data needed: none.
- Confidence: high

---

## Cross-speaker conflicts in this batch

- US-only vs international: Bass ("I can't imagine anywhere better than the US") vs Roche ("it just, it seems like such a no-brainer to diversify internationally", Japan 1990 lesson). Test US-only vs global vs relative-momentum switching.
- Yen: Bass (debt 265% of GDP, "the currency is the is the escape valve", short yen 2012) vs Calderini ("Ian is extremely extremely undervalued so we we like Yen", BoJ exit coming). Resolution to test: condition on BoJ direction and yen valuation (REER).
- Gold in hard landings: Druckenmiller ("historically have not done well in hard Landings" but owns it on de-dollarization) and Calderini (bullish on falling real yields) vs Roche (gold down 10% in 2022 in USD; currency-dependent). Test gold by regime: recession with falling real yields vs rising real yields.
- Treasuries as the bad-outcome hedge: Druckenmiller's playbook ("own treasuries") only if yields offer a fat pitch; Calderini says stock-bond correlation is positive/zero in inflation regimes; Roche says bonds are better value after yields rise. Test TLT vs bills vs trend sleeve by inflation regime and curve shape.
- Liquidity source: Roche (deficits are the real money printing; QE weak; loans create deposits) vs Druckenmiller (M2 surge of ~40% and Fed buying fueled the bubble; M2 stock still high). Test fiscal deficit impulse vs Fed net liquidity vs M2 gap as predictors.
- Valuation: Druckenmiller (20x earnings + record margins + fiscal -> flat decade) vs Calderini (AI earnings are real; valuations "not that much of a complete concern"). Test valuation warnings conditioned on earnings growth.
- Shorting in bears: Druckenmiller/Sokoloff warn of brutal bear-market rallies (don't go net short) vs Calderini (Graham was short equities in 2022 and 2023). For the tool: cash/bonds rather than inverse ETFs unless trend and macro both negative.
- Calendar effects vs macro: Hirsch's seasonal/presidential-cycle rules ignore macro; test as overlays that only modify timing of macro cuts.

## Country / EM rules collected (pointer list)
- Bank-to-sovereign contagion screen: bank assets/GDP > 3x -> avoid that country's equities/bonds/currency after a banking crisis (Bass).
- High-debt + capped yields -> short currency, own hedged equities (Japan; Bass); long yen when undervalued and BoJ tightening (Calderini).
- China: avoid / cap at index weight; GDP growth does not reach shareholders; current account toward zero; Taiwan/decoupling scenarios (Bass, Pompeo, Calderini).
- Allied Asia (Japan, Korea, India, Australia, Singapore, Malaysia) vs China on decoupling escalation (Pompeo).
- US inflation + strong dollar hurts dollar-dependent EM importers; prefer commodity exporters (Bass).
- Europe fragile in global stress (no fiscal union, no deposit guarantee; Italy-Germany spread trigger) (Bass); long EUR on ECB-hawkish divergence (Calderini).
- Frontier sovereign debt with opaque China bilateral loans -> slow haircut-heavy restructurings (Banga).
- Commodity exporters with/without fiscal rules (Dutch disease) (Norway fiscal rule).
- Home-bias/concentration: country > 40% of world cap with top-decile CAPE -> underweight (Roche).

## Batch summary (10 most important testable ideas)

1. Core vs headline inflation as the regime switch (Calderini, both talks): core inflation > ~3% flips stock-bond correlation positive, removes the "Fed put", and makes inflation upticks bearish; below ~1.5-2.5% inflation upticks are benign and Treasuries hedge. Test an ex-ante inflation-regime classifier for the TLT-vs-bills-vs-trend choice and for gating warnings.
2. Add a 20% cross-asset trend-following / macro sleeve (Calderini): claimed 60/40 IR 0.65 -> 0.83, max drawdown 36% -> 29%, positive in 1990, 2000-02, 2008, 2022 drawdowns (fails in fast crashes such as Q1 2020). Build from AQR TSMOM data or ETF proxies and compare with the tool's switching and with rolling puts.
3. Hiking-cycle size, speed and surprise (Calderini, Druckenmiller): cumulative hikes > 300 bp in 18 months, hikes above what the curve priced at cycle start, and "reactive" hikes begun after core inflation > 4% predict hard landings/accidents. Extends the tool's Fed-tightening gate.
4. Druckenmiller's Treasury rule: own long Treasuries for a bad outcome only when the curve leaves room (10y >= Fed funds); in deep inversion with high inflation, hold bills. Directly testable against the current TLT rule.
5. Fat-pitch duration short: 2y yield near zero while money growth surges -> short front-end / hold only bills/floaters (Druckenmiller 2021). Generalize: IF 2y < 0.5% and M2 y/y > 10% THEN zero duration.
6. Presidential/four-year cycle and Best Six Months (Hirsch): midterm-year Q2-Q3 weakness, Q4 midterm to Q2 pre-election "sweet spot" (+20% S&P average), Nov-Apr vs May-Oct switching (with MACD), January Trifecta (up 90.6% of years when all three up). Test as timing overlays on the macro cut (e.g. macro cuts act only in May-Oct, or full weight in the sweet spot).
7. Dovish pivot with no recession signal = strong equity tailwind (Calderini; 1995, 1998, 2019, Dec 2023) vs cuts that start with the Sahm rule triggered (stay defensive). Re-entry rule.
8. Copper/cyclicals: zero exposure into a hard landing, overweight on the way out once the Fed is cutting and copper momentum turns up (Druckenmiller); add Hirsch's December-low / April-May-high seasonal for copper and energy.
9. Currency and gold rules: gold on falling real yields / rising breakevens (Calderini) and on de-dollarization/fiscal stress (Druckenmiller); short the currency of a high-debt country whose central bank caps yields (Bass); long the currency with the most hawkish relative rate momentum (Calderini). Test as a currency/gold sleeve.
10. Banking-system stress screens (Bass, Druckenmiller): bank leverage plus falling house prices, regional-bank/CRE stress, bank securities losses (assets yielding 2-2.5% vs 5% funding), and bank-to-sovereign contagion ranking by bank assets/GDP. Use for cutting stocks/credit and for country underweights.

## Data requests (series needed that are NOT in the existing 43-indicator list)

Rates / curve / policy
- Fed funds level and cycle-start tracking (FRED FEDFUNDS 1954, DFEDTARU/DFEDTARL 2008, DFEDTAR 1982-2008)
- Treasury yields 1y, 2y, 5y, 30y levels (FRED DGS1, DGS2 1976, DGS5 1962, DGS30 1977); full 1-10y curve for ladders
- 6m/12m bills (FRED DTB6, DTB1YR, TB3MS 1934)
- 10y breakeven (FRED T10YIE 2003) and 5y breakeven (T5YIE) levels
- MOVE index (ICE / Yahoo ^MOVE)
- Fed funds futures / implied path (CME; proxy from 1y-2y forward)
- Core PCE (FRED PCEPILFE 1959)
- Real policy rate = Fed funds - core inflation (computed)
- Foreign official Treasury holdings (FRED WMTSECL1 2002; TIC)
- Fed emergency lending (FRED WLCFLPCL 2002)

Fiscal
- Federal deficit monthly/annual (FRED MTSDS133FMS 1980; FYFSGDA188S 1929)
- Federal debt/GDP (FRED GFDEGDQ188S 1966)
- Net interest / federal receipts (FRED A091RC1Q027SBEA, W006RC1Q027SBEA 1947)
- Debt-ceiling event dates (manual)

Credit / banks / money
- Bank credit and C&I loans (FRED TOTBKCR 1973, BUSLOANS 1947)
- Senior Loan Officer survey: C&I and mortgage standards (FRED DRTSCILM, SUBLPDHMSNQ 1990)
- Broker-dealer and bank leverage (Fed Z.1; FDIC EQTA 1984)
- FDIC unrealized securities losses (2008+)
- CRE loan delinquency (FRED DRCRELEXFACBS 1991)
- Regional banks KRE (2006) / KBW regional index
- BDC / private credit proxy (BIZD 2013)
- M2 gap vs trend (computed from M2SL)

Earnings / valuation
- S&P 500 EPS (Shiller monthly 1871) and EPS growth
- Corporate profits and profit margin (FRED CP / GDP 1947)
- S&P 500 drawdown from peak (computed)
- Equal-weight S&P (RSP 2003 / S&P EW index 1990)

Housing
- Case-Shiller home prices (FRED CSUSHPISA 1987; Shiller 1890), months' supply (MSACSR 1963), home price/income

Calendar
- US election cycle year flags; Santa Claus rally, first-five-days, January return (from S&P daily 1950)
- MACD on Dow/S&P daily

Commodities
- Gold (World Bank 1960; GLD 2004), silver (SLV 2006), broad commodity TR (S&P GSCI 1970, BCOM, DBC 2006, GSG 2006), World Bank commodity indexes (1960), Brent/WTI levels (FRED DCOILBRENTEU 1987, WTISPLC 1946), copper inventories / futures curve, cocoa/coffee/grains (World Bank pink sheet), rare earth REMX (2010), Henry Hub / TTF gas, agriculture DBA (2007)

FX
- USD/JPY, EUR/USD, USD/CNY, USD/NOK (FRED DEXJPUS, DEXUSEU, DEXCHUS, DEXNOUS), BIS real effective exchange rates (FRED RBJPBIS etc. 1994), G10 2y yields (OECD/national: German 2y, JGB 2y/10y FRED IRLTLT01JPM156N), UUP/UDN/FXE/FXY ETFs, CNY current account (SAFE/IMF)

International equities and sovereigns
- MSCI World, EAFE, ACWI ex-US, EM, Europe, country indexes (MSCI 1970/1988+); iShares country ETFs EWJ, DXJ/HEWJ, EWY, EWT, FXI, MCHI, KWEB, ASHR, INDA, EWZ, EWW, ECH, EWC, EWA, EWS, EWM, EZA, NORW/ENOR, KSA, UAE, VGK, EZU, EUFN, EWI, EWP, GREK, EIRL
- Country market caps / world share (World Bank CM.MKT.LCAP.CD 1975), country CAPE (StarCapital / Research Affiliates)
- Country 10y yields incl. Italy, Germany, Ireland (FRED IRLTLT01xxM156N)
- Bank assets/GDP by country (World Bank GFDD)
- Sovereign creditor composition (World Bank IDS; AidData), EM sovereign spreads (EMB 2007, EMHY 2012)
- Commodity terms of trade by country (IMF)

Hedging / alternatives / factors
- Trend-following and macro indices (SG Trend, Barclay CTA 1980, HFRI Macro 1990; AQR TSMOM and "Century of Factor Premia" free data; DBMF 2019, KMLM 2020)
- Put-protection indices (CBOE PPUT, PUT 1986), VIX futures/VIX calls, CBOE EVZ
- Inverse ETFs SH, SDS (2006), TBF/TBT (2009), floaters TFLO (2014)
- Short/intermediate Treasury ETFs SHY (2002), IEI (2007), IEF (2002), VFISX/VFITX (1991); TIPS (TIP 2003)
- Value/growth (Ken French HML 1926; IWD/IWF 2000), small vs large (Ken French SMB; IWM 2000; Russell 2000 1979)
- Sector ETFs: XLU, XLE, XME, GNR, COPX, CPER, ITB/XHB, XBI/IBB, SMH/SOXX, ITA/XAR, EUAD, VNQ, KBE, XLF, QQQ, CARZ/DRIV; Ken French industry portfolios (1926)
- Bitcoin (BTC-USD 2014; IBIT 2024)

Geopolitics / uncertainty
- Caldara-Iacoviello Geopolitical Risk index (monthly 1900+, daily 1985+)
- Baker-Bloom-Davis Trade Policy Uncertainty index (1985+)
- Taiwan ADIZ incursion counts (2020+); event lists (wars, strikes, export controls, debt-ceiling X-dates)
