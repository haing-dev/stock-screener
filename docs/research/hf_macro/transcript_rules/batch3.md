# Batch 3: testable rules from macro transcripts

Files (9): Luke Gromen (petrodollar, Jan 2022); Kenneth Rogoff (NBIM); Scott Nations (financial crises); Scott Bessent (Treasury); Kenneth Tropin (Graham Capital); Margrethe Vestager (NBIM); Paul Krugman; Jeff Yass (Susquehanna); Karen Karniol-Tambour (Sohn 2022, Bridgewater).

Notes: quotes are verbatim from transcripts (some are auto-captions without punctuation). "(proposed)" marks thresholds I added.

---

## File 1: Luke Gromen — What if the Saudis Break the Petrodollar System (recorded 12 Jan 2022)

### Sovereign-debt deleveraging needs sustained negative real rates -> own real assets
- Source: Luke Gromen — What if the Saudis Break the Petrodollar System (quote: "we think you're going to need negative real rates on a sustained basis increasingly negative to make Global sovereign debt and fiscal positions and entitlement obligations in the West in particular sustainable")
- Type: regime map
- Rule as testable logic: IF federal debt/GDP > 100% AND real 10y yield (or fed funds minus core CPI) < 0 THEN overweight gold (GLD), commodities (DBC/GSG), TIPS (TIP) vs nominal long Treasuries (TLT); hold while real policy rate < 0 (proposed: re-check monthly; exit when real fed funds > +1%).
- Data needed: Federal debt/GDP (FRED GFDEGDQ188S, 1966); real fed funds = FEDFUNDS - CPILFESL y/y (1958); real 10y (DFII10, 2003; pre-2003 proxy 10y minus 12m core CPI). Real 10y already in tool; debt/GDP and real fed funds NOT.
- Confidence: high

### WWII financial-repression playbook (yield caps + inflation run hot)
- Source: Luke Gromen — same file (quote: "they let inflation on hot they cap yields uh from 46 to 51 U.S that the GDP went from 110 to 55 percent U.S real rates went as low as negative 14")
- Type: regime map
- Rule as testable logic: IF central bank caps long yields (yield curve control / large QE absorbing >50% of net issuance) while CPI y/y > 4% THEN underweight nominal Treasuries and cash, overweight gold, commodities and equities with pricing power; horizon: duration of the cap. Test on 1942-1951 US data (Shiller/GFD) and 2020-21.
- Data needed: Fed Treasury holdings (FRED TREAST, 2002; WALCL), Treasury net issuance (FRED FYGFDPUN / Treasury MSPD), CPI (CPIAUCSL, 1947; Shiller CPI 1871). Partly in tool (net liquidity); QE share of issuance NOT.
- Confidence: medium

### Peak cheap energy and metals -> sustained commodity inflation impulse
- Source: Luke Gromen — same file (quote: "you're going to have a real sort of sustained inflationary impulse from uh from commodity and metals markets in a way that we probably haven't seen in some time")
- Type: signal
- Rule as testable logic: IF broad commodity index 12m change > 0 AND above its 10-month average (proposed trend filter) THEN overweight commodities (DBC/GSG, copper CPER, energy XLE) vs bonds; exit when below 10-month average.
- Data needed: S&P GSCI / BCOM total return (Yahoo ^SPGSCI 1970 via SPGSCI index; DBC 2006; World Bank Pink Sheet monthly 1960). Oil and copper 6m changes in tool; broad commodity index trend NOT.
- Confidence: medium (thematic, not a stated threshold)

### China water/power constraint -> supply-chain inflation
- Source: Luke Gromen — same file (quote: "if China has a water problem China has a power problem and if China has a power problem the world has a power problem and the world has an inflation problem")
- Type: signal
- Rule as testable logic: IF China industrial power output y/y falls below 0 (proposed) or China PPI rises > 5% y/y (proposed) THEN expect higher US import prices/core goods inflation over 6-12 months: overweight commodities/TIPS, underweight long Treasuries.
- Data needed: China PPI y/y (FRED CHNPIEATI01GYM? OECD MEI via FRED "PIEATI01CNM661N", ~1996), China electricity output (NBS; no easy free FRED series), US import prices from China (FRED CHNTOT / IR import price index EIUIR, 1989). NOT in tool.
- Confidence: low (narrative)

### Sticky supply-chain inflation -> inventory hoarding mindset (1970s analogue)
- Source: Luke Gromen — same file (quote: "companies are going to go from running jit to doing what they did in the 70s I'm told which is you order as much as you can")
- Type: signal
- Rule as testable logic: IF ISM manufacturing supplier deliveries index > 60 AND ISM prices paid > 70 (proposed) THEN inflation regime: overweight commodities, underweight long nominal bonds for 6-12 months.
- Data needed: ISM supplier deliveries, ISM prices paid (ISM, not on FRED since 2016; proxy NY Fed Global Supply Chain Pressure Index GSCPI, 1997, free). NOT in tool.
- Confidence: medium

### Fed tightening into a sovereign debt bubble = policy mistake -> markets "throw a fit"
- Source: Luke Gromen — same file (quote: "the FED can't tighten enough to fight this without blowing up the bond market with the dollar where it is")
- Type: signal / conflict
- Rule as testable logic: IF Fed hiking (fed funds 12m change > +1 pt) AND dollar index (DXY) >= 96-100 (his level) or dollar within 5% of 12m high (proposed) THEN expect a "deflationary fit": cut equities and commodities, hold cash/short T-bills; IF Fed hiking AND dollar falling (DXY 3m change < -3%, proposed) THEN tightening is tolerable — stay invested. Conflicts with the tool's "cut stocks while Fed tightening" (adds dollar as the conditioner).
- Data needed: DXY (Yahoo DX-Y.NYB, 1971; FRED DTWEXBGS 2006, DTWEXM 1973-2019). Fed funds 12m change and dollar vs 12m high already in tool; the interaction is NOT.
- Confidence: high (he repeats "it depends on where the dollar is")

### Tolerable yield level depends on the dollar
- Source: Luke Gromen — same file (quote: "it's I think it's the answer is is that it depends on where the dollar is so if if the dollar is here or higher you're probably getting close to the levels")
- Type: signal
- Rule as testable logic: IF 10y yield 3m change > +50bp (proposed) AND DXY 3m change > 0 THEN risk-off (equities and credit down); IF 10y rises while DXY falls THEN rising yields are benign (reflation), hold equities/commodities.
- Data needed: DGS10 (1962), DXY. Both in tool individually; combination NOT. Related to existing oil+rates+dollar squeeze.
- Confidence: high

### Druckenmiller capital-flow thesis: rotation out of US tech -> weaker dollar
- Source: Luke Gromen citing Stan Druckenmiller — same file (quote: "if they start moving money out of tech that means Capital flows that are helping Finance these deficits sterilize these deficits start flowing Elsewhere on the margin and the release valve turns into the dollar")
- Type: signal
- Rule as testable logic: IF Nasdaq-100 (QQQ) underperforms equal-weight/value (RSP or IWD) by > 10% over 6 months (proposed) THEN expect dollar weakness over next 6-12 months: overweight EM equities (EEM), commodities, gold; underweight US growth.
- Data needed: QQQ (1999), ^NDX (1985), value vs growth (Ken French HML, 1926; IWD/IWF 2000), DXY. NOT in tool (narrow leadership/cyclical vs defensive are related but not this).
- Confidence: medium

### Reopening/cyclical recovery playbook: sell growth, buy value, commodities, EM; sell US and the dollar
- Source: Luke Gromen — same file (quote: "you sell growth you buy value you buy Commodities you buy Emerging Markets you sell the United States and the dollar Falls")
- Type: action/instrument
- Rule as testable logic: IF recovery state (unemployment falling 6m, ISM rising, proposed) AND dollar 6m change < 0 THEN overweight EM (EEM, EWZ, EWY), commodities (DBC), value (IWD) vs US large growth; hold until dollar 6m change turns positive.
- Data needed: EEM (2003; MSCI EM index from 1988), EWZ/EWY (2000; MSCI Brazil/Korea 1988), DXY, UNRATE. EM/country data NOT in tool.
- Confidence: high

### Foreign official Treasury buying is inverse to the dollar level
- Source: Luke Gromen — same file (quote: "there's an inverse relationship between the level of a dollar and and how many treasuries they buy and once it gets too high they sell a whole lot")
- Type: signal
- Rule as testable logic: IF dollar index > 12m high (or top 20% of 5y range, proposed) THEN foreign official net Treasury sales -> term premium up: underweight long Treasuries; IF dollar in bottom 20% of 5y range THEN foreigners buy -> overweight long Treasuries.
- Data needed: TIC foreign official holdings (Treasury TIC, monthly 1977; FRED FDHBFIN quarterly 1970), Fed custody holdings for foreign officials (FRED WMTSECL1, 2002 weekly). NOT in tool.
- Confidence: medium

### Fed balance-sheet run-off (aggressive QT) -> rates up, dollar up, stocks down
- Source: Luke Gromen — same file (quote: "it's going to be back to 800 billion like it was in 08 pre-liemann by the Fourth of July well that was probably gonna go up ... rates are gonna go up Dollar's gonna go up markets are going to go down")
- Type: signal
- Rule as testable logic: IF Fed total assets 3m change < -2% (proposed) THEN underweight equities and long Treasuries, overweight dollar/cash.
- Data needed: WALCL (2002), net liquidity (WALCL - WTREGEN - RRPONTSYD). Net liquidity 3m change in tool; gross balance sheet change NOT (minor).
- Confidence: medium

### Fed buying 60-100% of issuance -> dollar down
- Source: Luke Gromen — same file (quote: "we know empirically when the FED buys 60 to 100 issuance the dollar goes down we know that because we saw it last year")
- Type: signal
- Rule as testable logic: IF Fed Treasury purchases over 12m / net Treasury issuance over 12m > 60% THEN underweight dollar (UUP short / overweight FXE, gold, EM) for 12m.
- Data needed: Fed Treasury holdings (FRED TREAST 2002), marketable debt outstanding (FRED MTSDS133FMS / GFDEBTN 1966). NOT in tool.
- Confidence: high (he calls it empirical)

### Reverse repo balance is not free liquidity unless SLR is relaxed
- Source: Luke Gromen — same file (quote: "if the SLR rules for treasuries are not suspended again ... then what Zero Hedge said is I don't think correct in terms of no net flow implication")
- Type: conflict/caveat
- Rule as testable logic: Caveat on the net-liquidity indicator: IF RRP drawdown occurs while SLR exemption is not in place THEN do not count RRP decline as fully stimulative (test: weight RRP component at 0.5 vs 1.0 in net liquidity and compare predictive power for S&P 3m return).
- Data needed: RRPONTSYD (2013), WALCL, WTREGEN; SLR exemption dates (Apr 2020-Mar 2021, manual dummy). Net liquidity in tool; split NOT.
- Confidence: medium

### Repo spikes are hitting the balance-sheet constraint (Fed reacts within 24-48h)
- Source: Luke Gromen — same file (quote: "how quickly they hop to it when the repo rates spiked right that took them 24 to 48 hours")
- Type: re-entry/exit
- Rule as testable logic: IF SOFR (or general collateral repo) minus IORB > +10bp (proposed) THEN expect Fed liquidity injection within weeks: treat funding-stress dip as buy (re-enter equities after 1 month, proposed) rather than sell.
- Data needed: SOFR (FRED SOFR, 2018), IORB (FRED IORB 2021; IOER 2008-2021), pre-2018 GC repo proxy (DTB3 vs fed funds). NOT in tool.
- Confidence: low

### "Deflationary fits" will be met by massive QE and eventually yield curve control
- Source: Luke Gromen — same file (quote: "yield curve control is the Hotel California right once they check in they can never leave")
- Type: regime map
- Rule as testable logic: IF crisis drawdown (S&P -20% from high) occurs with debt/GDP > 100% THEN expect QE: buy long Treasuries into the fit, then rotate to gold/commodities once Fed balance sheet 3m change > +10% (proposed).
- Data needed: S&P, WALCL, GFDEGDQ188S. Partly in tool.
- Confidence: medium

### Expected inflation range if supply constraints persist: CPI 7-10% for 2-4 years
- Source: Luke Gromen — same file (quote: "you're going to be talking about uh CPI that's probably going to run seven to ten for the next two three four years")
- Type: conflict/caveat (forecast, can be scored)
- Rule as testable logic: Forecast check only: CPI y/y averaged ~4% in 2023-2025, so the forecast failed; lowers weight on supply-constraint-only inflation signals. IF CPI y/y > 5% THEN track whether next 24m average stays > 5% (base rate test, 1950-2025).
- Data needed: CPIAUCSL (1947). In tool (core CPI).
- Confidence: low as a rule

### Fed hikes slow the dollar's fall (hikes possible when dollar falls)
- Source: Luke Gromen — same file (quote: "the more the dollar Falls the more ability they will have to actually raise rates")
- Type: signal
- Rule as testable logic: IF DXY 3m change < -3% (proposed) THEN Fed hikes less damaging: keep equities even if Fed tightening flag is on (override of tool's Fed-tightening gate).
- Data needed: DXY, fed funds. In tool individually.
- Confidence: medium

### Gold rising with rising real rates = dollar-debasement signal
- Source: Luke Gromen — same file (quote: "I've been watching gold rise with real rates Rising sharply in the U.S uh off the lows um and neither of these things should be happening")
- Type: signal
- Rule as testable logic: IF gold 3m change > 0 AND real 10y 3m change > +25bp (proposed) THEN regime of structural dollar weakness: overweight gold and EM, underweight dollar for 6-12m.
- Data needed: Gold (LBMA via FRED GOLDAMGBD228NLBM until 2022; Yahoo GC=F 2000; GLD 2004; World Bank monthly 1960), DFII10 (2003). Gold NOT in tool.
- Confidence: medium

### Petrodollar break (Saudi selling oil in yuan) -> structurally bad dollar, short-run bad oil
- Source: Luke Gromen — same file (quote: "structurally it'd be really bad for the dollar it might actually be good for the dollar in the short run it might be bad for oil in the short run")
- Type: action/instrument (event)
- Rule as testable logic: IF event: major oil exporter announces non-dollar oil pricing THEN short horizon (0-3m): long dollar, underweight oil; long horizon (12-36m): underweight dollar, overweight gold. Event study only.
- Data needed: Event dates (manual), DXY, Brent (FRED DCOILBRENTEU 1987), gold.
- Confidence: medium

### Central-bank/ESF gold buying as a dollar-weakening tool -> gold strength foreshadows dollar weakness
- Source: Luke Gromen — same file (quote: "if I wanted the dollar down one way I would consider doing that I would you know get someone like the bis bid in Gold every day")
- Type: signal
- Rule as testable logic: IF gold makes a 12m high while DXY 6m change < 0 THEN overweight gold, short dollar (UUP short/FXE) for 6m. Also: IF official-sector gold purchases (WGC quarterly) > 5y average THEN overweight gold (proposed).
- Data needed: Gold price, DXY, World Gold Council central-bank demand (quarterly, 2010, free with registration). NOT in tool.
- Confidence: low

### Bitcoin/gold as "Fed is trapped" end-game hedge; manage leverage
- Source: Luke Gromen — same file (quote: "the path was the path yeah be careful with leverage be careful with leverage")
- Type: position sizing/risk
- Rule as testable logic: IF holding debasement hedges (gold, bitcoin) THEN no leverage; size so a 30-40% drawdown is tolerable (proposed: max 10% portfolio in gold+BTC, unlevered). Weimar example: repeated sharp dips in gold during a debasement trend — do not use tight stops.
- Data needed: Gold, BTC-USD (Yahoo 2014). NOT in tool.
- Confidence: medium

### Weimar analogy: tightening announcements cause temporary gold sell-offs in a debasement trend
- Source: Luke Gromen — same file (quote: "there were four or five instances as the currency was hyperinflating ... where people were selling gold and buying German race marks")
- Type: re-entry/exit
- Rule as testable logic: IF in debasement regime (debt/GDP > 100%, real policy rate < 0) AND gold falls > 10% from high on a hawkish Fed shift THEN buy gold (re-entry), hold 12m (proposed).
- Data needed: Gold, real fed funds, debt/GDP. NOT in tool.
- Confidence: low

### Flat/flattening curve while hiking = markets near breaking point
- Source: Luke Gromen — same file (quote: "I think the yield curve where it's you know flat and you know flattening out um is probably telling you that that we're getting close")
- Type: signal
- Rule as testable logic: IF 10y-2y < 50bp AND falling over 3m while Fed hikes THEN reduce equities (proposed 50%). Already similar to existing yield-curve indicator.
- Data needed: T10Y2Y (1976). In tool.
- Confidence: medium

### Foreign holdings of US equities rose from $2tn to $12tn (deficits financed with stocks)
- Source: Luke Gromen — same file (quote: "corn Holdings of equities has gone from like 2 trillion in 2009 to 12 trillion in 2020")
- Type: signal
- Rule as testable logic: IF foreign net purchases of US equities (TIC) turn negative on a 12m sum THEN dollar weakness and US underperformance vs ex-US over next 12m: overweight EFA/EEM vs SPY (proposed).
- Data needed: TIC net foreign purchases of US equities (Treasury TIC, monthly 1977); FRED Z.1 rest-of-world corporate equities (BOGZ1LM263064105Q, 1945). NOT in tool.
- Confidence: medium

---

## File 2: Kenneth Rogoff — In Good Company, NBIM (Apr 2025)

### 1970s/Nixon analogue: tariffs + pressure on the Fed -> inflation regime
- Source: Kenneth Rogoff — Kenneth Rogoff - Podcast - In Good Company (quote: "I think it feels a little like the 70s to me. Trump actually feels a little like Nixon to me")
- Type: regime map
- Rule as testable logic: IF effective US tariff rate rises > 5 pts in 12m (proposed) AND political pressure on Fed (proxy: fed funds cut while core CPI y/y > 3%) THEN 1970s playbook: overweight gold, commodities, TIPS, short-duration; underweight long nominal Treasuries and the dollar for 12-24m.
- Data needed: Effective tariff rate = customs duties / imports (FRED B235RC1Q027SBEA customs duties 1947 / IMPGS imports 1947); core CPI (in tool); fed funds. Tariff rate NOT in tool.
- Confidence: medium

### Tariffs: short-term price level effect, long-term growth drag (not a big inflation driver alone)
- Source: Kenneth Rogoff — same file (quote: "what will be the impact on inflation from the tariffs? So that is not a big deal ... the problem is more uh innovation slowing growth over the longer run")
- Type: conflict/caveat
- Rule as testable logic: IF tariff shock THEN expect one-off core goods inflation (3-12m) but lower real GDP growth over 2-5 years: do not treat tariff-driven CPI spike as persistent (no long-duration sell on tariff alone); tilt toward lower equity expected return. Contrasts with the 1970s regime call above (inflation comes from the Fed's response, not tariffs).
- Data needed: Effective tariff rate, core goods CPI (FRED CUSR0000SACL1E, 1956). NOT in tool.
- Confidence: medium

### Policy randomness/uncertainty is the main risk -> recession via confidence loss
- Source: Kenneth Rogoff — same file (quote: "the nature of the recession we might get is a loss of confidence, not an oil shock, not a pandemic, not a global financial crisis")
- Type: signal
- Rule as testable logic: IF consumer sentiment (UMich) falls > 20% in 6m (proposed) OR trade-policy uncertainty index > 2x its 5y average (proposed) THEN raise recession probability: reduce equities 50%, add long Treasuries (if not inflation regime).
- Data needed: UMich sentiment (FRED UMCSENT, 1952 monthly from 1978); Economic Policy Uncertainty index (FRED USEPUINDXM, 1985) and Trade Policy Uncertainty (policyuncertainty.com, 1985). NOT in tool.
- Confidence: medium

### Partisan split in sentiment distorts surveys
- Source: Kenneth Rogoff — same file (quote: "they're looking at the same data and just drawing completely different conclusions")
- Type: conflict/caveat
- Rule as testable logic: Caveat: IF using consumer sentiment/inflation expectations surveys THEN prefer hard data or market-based inflation expectations (breakevens) since ~2016 because partisan bias inflates swings; test: predictive power of UMich vs real consumption pre/post 2016.
- Data needed: UMCSENT, UMich 1y inflation expectations (MICH, 1978), T5YIE (2003). Breakevens partially in tool.
- Confidence: medium

### No Trump put
- Source: Kenneth Rogoff — same file (quote: "So, I don't I don't believe in a Trump put put. Uh I think he has conviction")
- Type: conflict/caveat
- Rule as testable logic: Caveat: do not assume policy reversal after equity drops in tariff shocks (no automatic buy-the-dip on policy-driven selloffs). Test: S&P 3m forward return after -10% policy-driven drawdowns vs other drawdowns.
- Data needed: S&P daily, event dates (manual).
- Confidence: medium

### Dollar footprint peaked ~2015; gradual decline (late middle-aged)
- Source: Kenneth Rogoff — same file (quote: "we sort of reached the peak 10 years ago in terms of the dollar's footprint and dominance in the global economy")
- Type: regime map
- Rule as testable logic: IF dollar share of global FX reserves (IMF COFER) falls > 1 pt over 4 quarters (proposed) THEN structural underweight dollar: tilt to ex-US equities (EFA, EEM) and gold over 3-5y; slow-moving, use as a tilt not a switch.
- Data needed: IMF COFER dollar share (quarterly, 1995, free); DXY. NOT in tool.
- Confidence: medium (structural, he says gradual)

### Dollar decline from inside: debt unwillingness + Fed independence concerns
- Source: Kenneth Rogoff — same file (quote: "a lot of the big problems are inside the unwillingness to confront debt, concerns about the independence of the central bank")
- Type: signal
- Rule as testable logic: IF 10y term premium rises while dollar falls (both 6m changes, term premium > +50bp and DXY < -5%, proposed) THEN "sell America" regime: underweight long Treasuries and USD, overweight gold, ex-US equities (EFA, EWJ, EWG), foreign bonds hedged? (unhedged for dollar view).
- Data needed: ACM term premium (NY Fed, 1961; FRED THREEFYTP10 Kim-Wright 1990), DXY. Term premium and dollar in tool; combination NOT.
- Confidence: medium

### China slowdown hurts energy/commodity exporters (Norway, Brazil, Argentina)
- Source: Kenneth Rogoff — same file (quote: "it's very big on uh energy exporters and commodity exporters ... good for Brazil and good for Argentina")
- Type: action/instrument (country/EM)
- Rule as testable logic: IF China growth proxy (China Li Keqiang proxy / China credit impulse / OECD China CLI) falls below its 12m average THEN underweight commodity exporters (EWZ Brazil, ENOR Norway, EWA Australia, EWC Canada, ECH Chile) and copper/oil; IF rising THEN overweight them, 6-12m.
- Data needed: OECD CLI China (FRED CHNLOLITONOSTSAM, 1980s), China credit impulse (no free FRED; proxy China total social financing from PBoC), MSCI Brazil/Norway (EWZ 2000, ENOR 2012; MSCI indices from 1988). NOT in tool.
- Confidence: high

### China japanification: deflation + falling rates while world rates rise
- Source: Kenneth Rogoff — same file (quote: "do we have a some kind of japanification in China now then? Yes, we do. The question is a matter of degree")
- Type: regime map (country)
- Rule as testable logic: IF China CPI y/y < 0.5% AND China 10y yield falling 12m AND property prices falling THEN underweight China equities (FXI/MCHI) and favor China bonds (CBON); "China's Sweden time is over" -> expect multi-year (proposed: until China CPI > 1.5% for 6m).
- Data needed: China CPI (FRED CHNCPIALLMINMEI, 1993), China 10y (investing.com; FRED none; proxy via OECD long-term rate IRLTLT01CNM156N if available), China house prices (BIS QCNN628BIS, 2005). NOT in tool.
- Confidence: medium

### China deflation + claimed 5% growth = don't trust official data
- Source: Kenneth Rogoff — same file (quote: "if your prices are going down continually and you're telling me you have 5% growth, I don't believe you")
- Type: conflict/caveat
- Rule as testable logic: Caveat: use market or alternative China data (copper, iron ore, Korea exports to China, electricity) rather than official GDP for China/EM signals.
- Data needed: Korea exports to China (Korea customs; FRED XTEXVA01KRM667S total Korea exports 1960), iron ore (World Bank Pink Sheet 1960). NOT in tool.
- Confidence: high

### China+1 manufacturing shift benefits Japan, Korea, Singapore, Malaysia, Indonesia, India
- Source: Kenneth Rogoff — same file (quote: "it's been great for Japan, for Korea, for Singapore, Malaysia, even Indonesia and India")
- Type: action/instrument (country)
- Rule as testable logic: IF China FDI inflows falling y/y (proposed) THEN overweight EWJ, EWY, EWS, EWM, EIDO, INDA vs FXI/MCHI (relative pair) for 12-36m.
- Data needed: China FDI (World Bank BX.KLT.DINV.CD.WD annual 1982; SAFE quarterly), MSCI country indices (ETFs from 1996-2012). NOT in tool.
- Confidence: medium

### India: positive growth story, but hard to be euphoric
- Source: Kenneth Rogoff — same file (quote: "I'm optimistic but it's hard to get euphoric about India because it's just so hard to govern a country of 1.4 billion people")
- Type: action/instrument (country)
- Rule as testable logic: IF India real GDP growth > China real GDP growth (IMF WEO) THEN overweight INDA vs MCHI (proposed, 12m rebalance); no strong conviction, small tilt.
- Data needed: IMF WEO GDP growth (annual, 1980), INDA (2012; MSCI India 1993). NOT in tool.
- Confidence: low

### Inflation in remission not dead; another burst within ~5-7 years after a big shock
- Source: Kenneth Rogoff — same file (quote: "there's going to be another big burst of inflation similar to what we saw in the uh after the pandemic")
- Type: regime map
- Rule as testable logic: IF large negative growth shock (pandemic, cyber war, climate disaster; proxy: unemployment +2 pts in 6m) AND fiscal response (deficit/GDP widens > 3 pts) AND Fed independence questioned THEN expect inflation surge within 12-24m: after the initial deflationary phase, rotate from long Treasuries to TIPS/commodities/gold.
- Data needed: UNRATE (in tool), federal deficit/GDP (FRED FYFSGDA188S annual 1929; quarterly surplus M318501Q027NBEA / GDP), CPI. Deficit NOT in tool.
- Confidence: medium

### Debt resolves through inflation or higher rates; this time rates rise more
- Source: Kenneth Rogoff — same file (quote: "debt doesn't just mechanically turn into inflation. That's wrong. It either turns into higher interest rates or inflation")
- Type: regime map
- Rule as testable logic: IF debt/GDP > 100% AND deficit > 5% of GDP outside recession THEN underweight long nominal Treasuries (TLT) vs T-bills/short TIPS; expect term premium to rise (test 10y term premium 12m forward change conditional on deficit).
- Data needed: GFDEGDQ188S, deficit/GDP, ACM term premium. Term premium in tool; fiscal series NOT.
- Confidence: high

### Investors will demand more compensation next inflation ("fool me once")
- Source: Kenneth Rogoff — same file (quote: "this time interest rates are going to go up a lot more. uh investors were forgiving last time")
- Type: signal
- Rule as testable logic: IF core CPI y/y > 4% for second time within 10 years THEN expect larger rise in 10y yield per point of inflation than prior episode: underweight duration earlier (rule: cut TLT when core CPI 3m annualized > 3.5%, proposed).
- Data needed: CPILFESL, DGS10. In tool.
- Confidence: low

### Next financial crisis more likely from crypto than AI valuations
- Source: Kenneth Rogoff — same file (quote: "if we get a financial crisis, look for it coming out of crypto rather than necessarily high valuations of AI firms")
- Type: signal
- Rule as testable logic: IF bitcoin falls > 50% from 12m high (proposed) AND stablecoin market cap shrinks > 10% in 3m (proposed) THEN raise financial-stress flag: reduce equity exposure 25%, monitor credit spreads.
- Data needed: BTC-USD (Yahoo 2014), stablecoin supply (DefiLlama, 2018). NOT in tool.
- Confidence: low

### New-technology booms create volatility and sudden valuation collapses
- Source: Kenneth Rogoff — same file (quote: "a lot of financial crises have come because there's a new technology and everybody gets all excited about it")
- Type: signal
- Rule as testable logic: IF tech sector share of S&P market cap > 30% (proposed) AND tech 12m return > 50% (proposed) THEN bubble flag: reduce tech/ Nasdaq weight, buy puts or hold equal weight (RSP) instead of cap weight.
- Data needed: XLK vs SPY, sector weights (S&P; proxy Ken French industry portfolios, 1926). Narrow leadership/rally speed in tool; tech share NOT.
- Confidence: low

### Nixon-style price controls and financial repression coming
- Source: Kenneth Rogoff — same file (quote: "I think we're going to see Nixon like price controls like we saw in the 1970s. Maybe, you know, other kinds of controls")
- Type: regime map
- Rule as testable logic: IF financial repression (real 10y < 0 with CPI > 3%, or regulation forcing banks to hold Treasuries) THEN hold real assets and gold vs nominal bonds; price controls -> later inflation release (1971-74 pattern: CPI jumps after controls lifted). Event test on 1971-1974.
- Data needed: CPI, real yields, manual event dummies. Partly in tool.
- Confidence: medium

### Fed left alone will hike if inflation rises with strong jobs
- Source: Kenneth Rogoff — same file (quote: "if left to its own devices, it will raise interest rates. I don't think there's any doubt about it")
- Type: signal
- Rule as testable logic: IF core CPI 3m annualized > 3% AND unemployment < 12m average THEN expect hikes: underweight 2y Treasuries (SHY) vs bills, underweight long duration.
- Data needed: CPILFESL, UNRATE. In tool.
- Confidence: medium

### Supply-shock inflation that didn't reverse was a central bank mistake
- Source: Kenneth Rogoff — same file (quote: "the supply chain problems went away. Why didn't the price of paper towels come down?")
- Type: conflict/caveat
- Rule as testable logic: Caveat vs "transitory" view: IF supply-chain pressure (NY Fed GSCPI) normalizes but core CPI 3m annualized still > 3% THEN inflation is demand/expectations-driven: keep underweight duration.
- Data needed: NY Fed GSCPI (1997), core CPI. GSCPI NOT in tool.
- Confidence: medium

### Real 10y TIPS swing from -1% to +2% raised US interest burden to ~$1tn
- Source: Kenneth Rogoff — same file (quote: "That got to minus one. Now it's around two. You know, it's a 3% swing. And US uh interest payments have gone up")
- Type: signal (fiscal)
- Rule as testable logic: IF federal interest outlays / GDP > 3% (proposed) or interest/revenue > 15% (proposed) THEN fiscal-dominance risk: overweight gold and short-duration, underweight long nominal Treasuries.
- Data needed: Federal interest payments (FRED A091RC1Q027SBEA, 1947), federal receipts (FGRECPT), GDP. NOT in tool.
- Confidence: medium

### Low-debt countries could stimulate more after GFC and did better (Germany now)
- Source: Kenneth Rogoff — same file (quote: "look at the low debt countries and how much they were able to stimulate their economies, they did better")
- Type: action/instrument (country)
- Rule as testable logic: IF global recession signal (e.g., OECD CLI below 100 and falling) THEN overweight equities of low-debt countries (gov debt/GDP < 60%: e.g., Germany EWG, Australia EWA, Korea EWY, Switzerland EWL) vs high-debt (Japan, Italy EWI, France EWQ, US) for 12-24m.
- Data needed: IMF gov debt/GDP by country (annual, 1980s), MSCI country indices. NOT in tool.
- Confidence: medium

### Europe must rearm: decades of underinvestment
- Source: Kenneth Rogoff — same file (quote: "Europe's going to end up having to put a lot more in than uh leaders are beginning to talk about yet")
- Type: action/instrument (geopolitics)
- Rule as testable logic: IF NATO Europe defense spending/GDP rising (annual) THEN overweight European defense/industrials (EUAD, ITA as US proxy) and European equities (VGK); also higher Bund yields (underweight German bonds).
- Data needed: NATO/SIPRI defense spending (annual, 1949), VGK (2005), EUAD (2023). NOT in tool. (Sector-level; borderline vs no-single-stocks rule, ETF ok.)
- Confidence: medium

### US cannot restructure or default; uses inflation/repression card (EM borrowing in dollars can break suddenly)
- Source: Kenneth Rogoff — same file (quote: "when you go to an emerging market uh that borrows in dollars, it can happen very suddenly that Greece was an example")
- Type: regime map (EM)
- Rule as testable logic: IF EM country has high foreign-currency debt (external debt/GDP > 40%, proposed) AND dollar rising (DXY 6m > +5%) THEN underweight that EM country ETF and EM USD sovereign debt (EMB); US debt risk shows up gradually in yields, not as default.
- Data needed: World Bank external debt (annual 1970), EMB (2007; JPM EMBI from 1993 via proxies), DXY. NOT in tool.
- Confidence: medium

---

## File 3: Scott Nations — How to Act Rationally During a Financial Crisis (2022 bear market)

### Do not get scared out: keep investing in bear markets (anti-timing)
- Source: Scott Nations — How to Act Rationally During a Financial Crisis (quote: "Invest, continue to invest. Don't stop investing.")
- Type: conflict/caveat (re-entry)
- Rule as testable logic: Benchmark/contradiction to the tool's de-risking: IF S&P closes > 20% below its high THEN buy (or at least do not sell) and hold 10y. Test: forward 1/3/5/10y S&P returns after first close at -20% vs unconditional; compare tool's rule to "never sell" at 10y horizon.
- Data needed: S&P 500 total return (Shiller 1871; ^GSPC 1927). In tool.
- Confidence: high

### Capitulation flows mark the bottom (Feb-Mar 2009 record equity fund outflows)
- Source: Scott Nations — same file (quote: "the biggest net mutual fund, equity mutual fund outflows in decades happened in February and March of 2009, which was the absolute bottom of the market")
- Type: re-entry/exit
- Rule as testable logic: IF monthly net equity mutual fund + ETF outflows are the largest in 24m (proposed: bottom 5% of history, as % of assets) AND S&P > 20% below high THEN re-enter equities (overweight) for 12m.
- Data needed: ICI monthly equity fund flows (ICI, 1984; weekly from 2007, free summaries); proxy: AAII bull-bear spread (1987, free), Investors Intelligence. NOT in tool.
- Confidence: medium

### Sellers at the bottom don't get back in until after a big rally
- Source: Scott Nations — same file (quote: "The problem is, they don't get back in until it's rallied a bunch")
- Type: re-entry/exit
- Rule as testable logic: Re-entry rule test: after a de-risk, compare re-entering when S&P crosses back above its 10-month average vs re-entering at -30% from high vs fixed 6m later; measure missed return. Supports a fast mechanical re-entry.
- Data needed: S&P monthly. In tool.
- Confidence: medium

### No autocorrelation in daily index returns since 1896
- Source: Scott Nations — same file (quote: "since the creation of the Dow Jones Industrial Average in 1896, that what happened today has no impact on what's going to happen in the stock market tomorrow")
- Type: conflict/caveat
- Rule as testable logic: Caveat: daily returns not predictive; any short-horizon momentum/trend signal should be tested at monthly horizon (10-month average, 12m momentum) not daily. Contradicts trend-followers (Tropin, file 5) at longer horizons only partially.
- Data needed: DJIA daily (1896, FRED DJIA only 10y; Stooq ^DJI long history). Partly.
- Confidence: high

### Availability/recency: crash memories are not the base case
- Source: Scott Nations — same file (quote: "if you're always invested with the idea that a stock market crash is just around the corner, then you're never going to be in the stock market")
- Type: position sizing/risk
- Rule as testable logic: Constraint: de-risking signals must have a cost check — require that the average time out of equities be < 20% of months (proposed) and that rule beats buy-and-hold net of missed upside.
- Data needed: tool backtest output.
- Confidence: medium

### Hindsight bias: only ~3% acted before 1987 crash
- Source: Scott Nations — same file (quote: "it turns out that 3% of them, 3%, which would be about the random number you would expect for a group, about 3% had actually done something in advance")
- Type: conflict/caveat
- Rule as testable logic: Caveat against discretionary crash calls; require pre-registered rules (supports tool's registry approach). No trading rule.
- Data needed: none.
- Confidence: high

### 30-day waiting rule for new trades
- Source: Scott Nations — same file (quote: "Wait 30 days. Just wait 30 days. If it's a real trade, if it's an investment, 30 days is going to be meaningless in the long term")
- Type: position sizing/risk
- Rule as testable logic: IF a new discretionary (non-signal) position is proposed THEN delay 30 days; test whether delaying signal execution by 1 month changes strategy return (signal decay test for each macro rule).
- Data needed: tool signals with 1-month lag.
- Confidence: medium

### Disposition effect: sold winners outperform what investors keep/buy (Odean)
- Source: Scott Nations — same file (quote: "the stocks that they sell ultimately outperform whatever they end up buying")
- Type: position sizing/risk
- Rule as testable logic: Rebalancing rule: do not trim instruments only because they have gained; IF an asset is in uptrend (12m momentum > 0) THEN let it run within max weight cap; consistent with time-series momentum across ETFs (test 12m TSMOM on country ETFs, commodities).
- Data needed: ETF prices.
- Confidence: medium

### Loss aversion: losses hurt 2-2.5x gains -> panic sells at bottom
- Source: Scott Nations — same file (quote: "we hate losses about two times to two and a half times more than we like the exact same gain")
- Type: position sizing/risk
- Rule as testable logic: Size total equity so that a 50% equity drawdown (proposed stress) produces a portfolio loss the user can hold through (e.g. max 25% portfolio drawdown -> max 50% equity weight without de-risk rule). Design input, not a signal.
- Data needed: none.
- Confidence: medium

### Overreaction to bad news is exploitable (value/reversal funds)
- Source: Scott Nations — same file (quote: "There are actually a number of funds out there that work to take advantage of your overreaction")
- Type: signal
- Rule as testable logic: Index-level analogue: IF a country ETF or sector ETF falls > 30% in 12m (proposed) AND is in bottom decile of 5y-relative valuation (CAPE) THEN buy and hold 3-5y (long-horizon reversal across countries).
- Data needed: Country CAPE (Barclays/Star Capital, research-affiliates; free partial), MSCI country returns (1970 for developed via MSCI, 1988 EM). NOT in tool.
- Confidence: low (he talks about stocks)

### Antitrust/government breakup risk adds market uncertainty (1907, 1911/1929, 2000)
- Source: Scott Nations — same file (quote: "That helped fuel the stock market crash of 1929. Really, the same thing happened in 1907")
- Type: signal
- Rule as testable logic: IF top-10 stock concentration > 30% of S&P (proposed) AND major antitrust action against the largest company is announced THEN reduce cap-weighted index exposure in favor of equal-weight (RSP) for 12m. Event test: 2000 Microsoft ruling, 2020-2024 big tech cases.
- Data needed: Concentration (S&P top-10 share; proxy CRSP), event dates. Narrow leadership in tool; event NOT.
- Confidence: low (historical fact is shaky: Standard Oil breakup was 1911)

### Bubble markers: name changes to hot theme, profits ignored, 'phantastic objects'
- Source: Scott Nations — same file (quote: "If Joe's Diner was publicly listed and changed its name to JoesDiner.com in 1999, its stock price would rally")
- Type: signal
- Rule as testable logic: IF share of unprofitable companies in Russell 2000 > 40% (proposed) AND IPO first-day returns average > 30% (proposed) THEN bubble flag: underweight small/growth (IWO, ARKK-like) vs value/quality.
- Data needed: Jay Ritter IPO data (1980, free), Russell 2000 unprofitable share (no free series; proxy from SEC data). NOT in tool.
- Confidence: low

### Expect 7-8%/yr long-run equity return with risk; don't short-circuit risk
- Source: Scott Nations — same file (quote: "If you expect to earn 7 to 8% a year, sometimes you're just going to be along for the ride")
- Type: conflict/caveat
- Rule as testable logic: Benchmark: strategy must beat a static allocation with similar long-run return; note his 7-8% is nominal approx. (real ~6.5-7%).
- Data needed: Shiller.
- Confidence: medium

### Housing: national prices hadn't fallen in unison -> overconfidence; recency in leverage
- Source: Scott Nations — same file (quote: "across the entire country, housing prices had not fallen in tandem, and so a lot of people were overconfident about that")
- Type: signal
- Rule as testable logic: IF national real house prices y/y > 10% (proposed) and house price/rent ratio > 1.2x its 30y average (proposed) THEN underweight homebuilders (ITB/XHB) and banks (KBE), raise credit-risk flag for 24m.
- Data needed: Case-Shiller national (FRED CSUSHPINSA, 1987; Shiller from 1890), OER rent CPI (CUSR0000SEHC, 1983). Homebuilders vs market in tool; house price/rent NOT.
- Confidence: low

---

## File 4: Scott Bessent — Inside Trump's Treasury; War Costs; Why Bond Market is King (Mar 2026, during Iran conflict)

### Crowd is right 85-90% of the time (momentum), money is made at turns
- Source: Scott Bessent — Scott Bessent- Inside Trump's Treasury (quote: "the crowd is right 85 or 90% of the time and that's the momentum, but it's really that when things turn ... is when you can really make a lot of money")
- Type: regime map / position sizing
- Rule as testable logic: Default to trend/momentum: IF asset 12m return > 0 AND price > 10-month average THEN hold/overweight (country ETFs, currencies, commodities, bonds). Contrarian only on a catalyst: IF consensus extreme (e.g., CFTC net positioning in top/bottom 5% of 3y range) AND policy catalyst (new government/central bank leadership) THEN take the other side.
- Data needed: ETF/futures prices (Yahoo), CFTC Commitments of Traders (1986, free). COT NOT in tool.
- Confidence: high

### Policy-regime catalyst trade: Abenomics short yen (current account flip + new BoJ board)
- Source: Scott Bessent — same file (quote: "when the Japanese switched off the nuclear reactors, they had to start importing more fossil fuels, and it took the current account to a deficit. But, nothing really happened")
- Type: signal (currency/country)
- Rule as testable logic: IF a country's current account balance swings by > 2 pts of GDP toward deficit (proposed) AND a reflationary government/central-bank change is elected/appointed THEN short its currency (FXY short / USDJPY long) and long its equity index hedged (DXJ / EWJ hedged) for 1-3 years. Note: current-account flip alone did not move the yen; catalyst needed.
- Data needed: Japan current account % GDP (IMF/OECD; FRED JPNB6BLTT02STSAQ, 1996), USDJPY (FRED DEXJPUS, 1971), EWJ (1996), DXJ (2006). NOT in tool.
- Confidence: high (his signature trade)

### Long yen-weakness = long Japan equity ("market ride of a lifetime")
- Source: Scott Bessent — same file (quote: "I have no idea, but it will be the market ride of a lifetime")
- Type: action/instrument (Japan)
- Rule as testable logic: IF yen 6m change < -10% vs USD (proposed) THEN overweight Japanese equities in yen terms (currency-hedged DXJ/HEWJ) vs unhedged; test correlation USDJPY vs Nikkei since 2012.
- Data needed: Nikkei 225 (FRED NIKKEI225, 1949), USDJPY. NOT in tool.
- Confidence: medium

### Japan structural reform (shareholder rights, ROE) supports Japan equities
- Source: Scott Bessent — same file (quote: "restructure the investment environment in terms of you know, the bringing up shareholders' rights, return on capital")
- Type: action/instrument (Japan)
- Rule as testable logic: IF Japan market-wide ROE rising and buybacks rising y/y (proposed) THEN overweight EWJ vs ACWI over 3y.
- Data needed: Japan ROE (TSE/MSCI; no free series; proxy MSCI Japan earnings). NOT in tool.
- Confidence: low

### Endowment bias: be able to put a trade "back on the shelf" until a catalyst appears
- Source: Scott Bessent — same file (quote: "Do a immense amount of work, and then just say now now's not the time")
- Type: re-entry/exit
- Rule as testable logic: IF fundamental signal says buy/sell an asset BUT price trend disagrees (12m momentum opposite sign) THEN wait; enter only when trend confirms (fundamental AND trend). Test combining each macro signal with a 10-month average filter.
- Data needed: prices.
- Confidence: medium

### Oil shock damage is about duration, not level
- Source: Scott Bessent — same file (quote: "I I I don't think it it it's the the level. I think it's probably the duration")
- Type: signal
- Rule as testable logic: IF oil (WTI) > 50% above its 12m average for > 3 consecutive months (proposed) THEN recession/stagflation risk: cut equities, underweight consumer discretionary (XLY), overweight energy (XLE), T-bills; a spike lasting < 1 month: no action.
- Data needed: WTI (FRED DCOILWTICO, 1986; WTISPLC monthly 1946). Oil 6m change in tool; duration measure NOT.
- Confidence: high

### US energy independence insulates the US economy from oil spikes
- Source: Scott Bessent — same file (quote: "President Trump's energy policies have insulated the US quite a bit. We're we're record liquids production")
- Type: conflict/caveat
- Rule as testable logic: Caveat: weight on oil-shock warning should decline as US net petroleum imports fall; IF US net petroleum imports < 0 (net exporter, since ~2020) THEN halve the oil-shock indicator's weight in equity de-risking; oil shock now hits oil-importing countries harder (underweight EWJ, EWY, INDA, Europe VGK vs US).
- Data needed: EIA US net petroleum imports (weekly/monthly, 1973, FRED? EIA API free). NOT in tool.
- Confidence: medium

### Strategic reserve release (record 400m bbl) and "market lives in the future"
- Source: Scott Bessent — same file (quote: "The market lives in the future ... then we had the biggest single reversal in one-day history the that day, so it was already priced in")
- Type: re-entry/exit
- Rule as testable logic: IF coordinated SPR/IEA release announced during an oil spike THEN oil's peak likely in (fade the spike): reduce long oil, re-add equities within 1 month (proposed). Event study on 1991, 2005, 2011, 2022, 2026 releases.
- Data needed: Event dates (IEA collective actions), WTI/Brent daily. NOT in tool.
- Confidence: medium

### After a Middle-East war resolved in US favor, lower oil regime
- Source: Scott Bessent — same file (quote: "once this conflict is over and resolved in favor of the US, I think there's a chance we can move to a substantially lower oil price regime")
- Type: action/instrument (geopolitics)
- Rule as testable logic: IF geopolitical oil-supply conflict ends (event) THEN underweight oil/energy (XLE, USO), overweight oil importers (EWJ, INDA, EWY), consumer discretionary for 6-12m. Test after 1991 Gulf War, 2003 Iraq invasion.
- Data needed: Brent/WTI, event dates. NOT in tool. (Speaker is a policy official: talking his book.)
- Confidence: low

### Fed reacting to energy-driven inflation expectations vs growth slowdown
- Source: Scott Bessent — same file (quote: "I think the Fed is worried about maybe the energy component triggering inflationary expectations")
- Type: signal
- Rule as testable logic: IF oil 3m change > +30% AND 5y breakeven 3m change > +30bp (proposed) THEN Fed likely delays cuts: underweight 2y Treasuries, stay short duration; IF breakevens don't move THEN Fed looks through: duration OK.
- Data needed: T5YIE (2003), WTI. Both in tool.
- Confidence: medium

### Extended QE caused the 2022-23 inflation; QE only in extraordinary times
- Source: Scott Bessent — same file (quote: "The the Fed continued buying the for years afterwards and I I believe that that's one of the things that got us the great inflation 22 and 23")
- Type: signal
- Rule as testable logic: IF Fed balance sheet still growing (WALCL 6m change > 0) more than 12 months after crisis low in unemployment/after S&P regains prior high (proposed) THEN inflation risk ahead: underweight long Treasuries, overweight TIPS/commodities 12-24m.
- Data needed: WALCL, UNRATE, S&P. Partly in tool.
- Confidence: medium

### Treasury shifting issuance to short end (bills) to keep long yields down
- Source: Wilfred Frost question, Bessent response — same file (quote: "your debt management has been down to that more short term issuance")
- Type: signal (fiscal/debt management)
- Rule as testable logic: IF bill share of marketable debt rising (> 22%, proposed) THEN term premium suppressed: favour long Treasuries short-term; IF Treasury announces larger coupon (long) issuance (quarterly refunding) THEN underweight TLT for 3m.
- Data needed: Treasury MSPD bill share (monthly, 1996; FRED MTSDS? use Treasury Fiscal Data API), quarterly refunding sizes (manual). NOT in tool.
- Confidence: medium

### Foreign demand for Treasuries rising; US 10y fell while other G7 yields rose
- Source: Scott Bessent — same file (quote: "what what we've seen last year was continued and increasing foreign interest in US Treasuries")
- Type: conflict/caveat
- Rule as testable logic: Counter to Gromen/Rogoff "sell America": test TIC foreign net Treasury purchases 12m sum as a signal for 10y yield 12m change (IF foreign buying > 0 and rising THEN overweight TLT).
- Data needed: TIC (1977). NOT in tool.
- Confidence: low (official spin)

### Private credit "wobbles": monitor shadow-bank links to banks and insurers
- Source: Scott Bessent — same file (quote: "there's nothing that tells me that shadow shadow banking is having a systemic problem. But we we are monitoring any relationships between the regulated entities")
- Type: signal (credit)
- Rule as testable logic: IF BDC/private credit index (BIZD) falls > 15% from high (proposed) or BDC discount to NAV widens > 15% THEN credit warning: reduce high yield (HYG) and bank exposure; add to warning count.
- Data needed: BIZD (2013), Cliffwater/BDC indices (no free long series; proxy: listed BDC ETF, alt. KBW), bank loans to nondepository financial institutions (FRED H.8 series LNFACBW027SBOG? "Loans to nondepository financial institutions" 2015). NOT in tool.
- Confidence: low

### Markets must stay continuous; panics happen when price discovery stops (gating, closures)
- Source: Scott Bessent — same file (quote: "when people panic is when they're you're not able to have price discovery, when markets close, when there's the threat of gating")
- Type: signal
- Rule as testable logic: IF fund gating/redemption limits announced (private credit, real estate funds) or Treasury market liquidity index (Bloomberg) spikes > 2 SD THEN systemic-stress flag: move to T-bills, raise cash.
- Data needed: Treasury market liquidity proxy (NY Fed? free proxy: MOVE index ^MOVE 2003 on Yahoo), event dates. MOVE NOT in tool.
- Confidence: medium

### Don't get out over your skis; never be forced to sell at the bottom
- Source: Scott Bessent — same file (quote: "You never want to have to sell at the bottom. You never want to find yourself like chasing at the top")
- Type: position sizing/risk
- Rule as testable logic: Leverage cap: no leverage on any position whose 1-month 99% loss could force liquidation; keep cash/bills buffer (proposed >= 10%) so no forced selling in drawdowns.
- Data needed: none.
- Confidence: medium

### Earn the right to take risk; size by "chip stack" (Druckenmiller/Buffett don't lose money)
- Source: Wilfred Frost paraphrase of Bessent — same file (quote: "spoken about how you have to earn the right to be able to take risk. You have to stay in the game")
- Type: position sizing/risk
- Rule as testable logic: IF strategy year-to-date return > 0 THEN allow risk budget up to full; IF YTD drawdown > 10% (proposed) THEN halve active bets (house-money sizing). Test on tool's tactical overlays.
- Data needed: strategy P&L.
- Confidence: medium

### Tariff regime: global 10% tariff baseline; Section 301/122 reconstruction after Supreme Court IEEPA ruling
- Source: Scott Bessent — same file (quote: "we're operating now with a global 10% tariff")
- Type: regime map (trade)
- Rule as testable logic: Input to tariff regime: effective tariff rate ~10%+; IF effective tariff rate > 8% (proposed) THEN apply "tariff regime" rules (see Rogoff file): higher core goods inflation, lower trade-exposed EM (EWY, EWT, EWW Mexico) performance.
- Data needed: effective tariff rate (customs duties / imports, FRED). NOT in tool.
- Confidence: medium

### US AI compute share 70-80% + energy dominance -> relative US strength
- Source: Scott Bessent — same file (quote: "we're going to have over 70 or 80% of all the compute in the world up from 40 or 50 a few years ago is going to be in the US")
- Type: conflict/caveat
- Rule as testable logic: Opposing view to "sell America": overweight US vs Europe while US real GDP growth - Euro area growth > 1.5 pts (proposed); test SPY vs VGK relative return conditional on growth gap.
- Data needed: US and Euro area real GDP (FRED GDPC1; CLVMNACSCAB1GQEA19 1995). NOT in tool.
- Confidence: low (policy official)

### Latin America shift to market-friendly governments (Argentina, Chile, Bolivia)
- Source: Scott Bessent — same file (quote: "this is a generational opportunity in the Western Hemisphere to show the benefits of being allies with the US")
- Type: action/instrument (country/EM)
- Rule as testable logic: IF a Latin American country elects a market-friendly government (event) THEN overweight its index ETF (ARGT, ECH Chile, EPU Peru) for 12m; event study.
- Data needed: Election dates, ARGT (2011), ECH (2007), MSCI country indices. NOT in tool.
- Confidence: low

### Sanctions waivers: Russian barrels flow to India/China anyway
- Source: Scott Bessent — same file (quote: "those barrels are going to end up in China anyway")
- Type: conflict/caveat (geopolitics)
- Rule as testable logic: Caveat: sanctions on oil exporters have smaller sustained effect on global oil price than headline (barrels re-route); do not hold long-oil on sanctions news beyond 1 month (proposed).
- Data needed: Brent, sanction event dates.
- Confidence: low

---

## File 5: Kenneth Tropin (Graham Capital) — Risk and Return Podcast (Aug 2025)

### Rate-change frequency = macro opportunity set (9x since 2022)
- Source: Kenneth Tropin — Kenneth Tropin ... Risk and Return Podcast (quote: "there's something like nine times the opportunity set on an annual basis in the last four years compared to the previous decade")
- Type: regime map
- Rule as testable logic: IF count of 25bp-equivalent policy rate changes across Fed/ECB/BoE over trailing 12m > 6 (proposed) THEN allocate more to trend/macro sleeve (managed futures DBMF/KMLM, SG CTA index) and active duration/currency tilts; IF < 2 THEN favor carry/static allocation.
- Data needed: FEDFUNDS target (FRED DFEDTARU 2008, DFEDTAR 1982), ECB deposit rate (FRED ECBDFR 1999), BoE Bank Rate (BoE database 1694; FRED IUDSOIA? use BoE), managed futures index (SG CTA from 2000; BarclayHedge CTA 1980; DBMF 2019). NOT in tool.
- Confidence: medium

### Low term premium: 2s10s at 40bp vs ~100bp average since 1990 -> duration poorly paid
- Source: Kenneth Tropin — same file (quote: "It's currently about 40 basis points, twos 10 ... The historical average since 1990 is about 100 basis points. It's been as high as 300")
- Type: signal
- Rule as testable logic: IF 10y-2y < 50bp (below its 1990+ average of ~100bp) AND federal deficit/GDP > 5% THEN underweight 10y+ Treasuries vs 2y/T-bills (you are not paid for duration); IF 10y-2y > 200bp THEN overweight long duration.
- Data needed: T10Y2Y (1976), deficit/GDP (FRED FYFSGDA188S). Curve in tool; deficit NOT.
- Confidence: high

### Combined vulnerability: record prices + record valuations + positive stock-bond correlation + geopolitics + Fed constrained
- Source: Kenneth Tropin — same file (quote: "I can't really recall a set of circumstances that make me feel uh that is you know you're more vulnerable than you are today")
- Type: signal (composite)
- Rule as testable logic: IF S&P at/near all-time high (within 3%) AND forward P/E > 22 (or CAPE top 5%) AND 1y stock-bond correlation > +0.3 AND core CPI > 2.5% (Fed constrained) THEN reduce equity weight (proposed 25%) and replace bonds with diversifiers (gold, managed futures, T-bills) rather than long Treasuries.
- Data needed: S&P, forward P/E (no free long series; proxy CAPE from Shiller 1881), stock-bond corr (in tool), core CPI (in tool). Gold/managed futures NOT in tool.
- Confidence: high

### Stock-bond correlation +0.4 -> bonds won't diversify; normal is zero or slightly negative
- Source: Kenneth Tropin — same file (quote: "stocks and bonds are correlated roughly to point4 normal would be zero or slightly negative")
- Type: hedge
- Rule as testable logic: IF 12m rolling stock-bond correlation > +0.3 THEN hedge equity drawdown with gold/T-bills/trend (managed futures) or puts rather than long Treasuries. (Tool already uses this for TLT vs T-bills; extend to gold and managed futures as alternatives.)
- Data needed: SPY/TLT returns (in tool), GLD, SG CTA/DBMF. Partly in tool.
- Confidence: high

### Macro/trend is one of few hedge styles that performs in equity corrections
- Source: Kenneth Tropin — same file (quote: "that's usually not good for the majority of hedge fund styles macro is one of the few tends to perform in that environment")
- Type: hedge
- Rule as testable logic: IF tool de-risks equities THEN allocate part of freed capital (proposed 1/3) to a time-series momentum sleeve (12m trend across bond, FX, commodity, equity index futures/ETFs) instead of only T-bills/TLT. Test crisis alpha 1990-2025 (Moskowitz-Ooi-Pedersen TSMOM data AQR, 1985).
- Data needed: AQR TSMOM factor (free, 1985), SG CTA Index (2000), ETF universe. NOT in tool.
- Confidence: high

### Bond market panics with illiquidity (April 2025 Liberation Day) produce exaggerated moves
- Source: Kenneth Tropin — same file (quote: "This was one of those scenarios where it was got really really illquid and uh therefore the moves are really really exaggerated")
- Type: signal
- Rule as testable logic: IF 10y yield rises > 40bp in 5 trading days while S&P falls > 5% (stocks and bonds sold together, proposed) THEN liquidity-panic flag: hold cash/T-bills, avoid duration; expect partial reversal within 1-3 months (re-entry rule to test).
- Data needed: DGS10 daily, S&P daily, MOVE (Yahoo ^MOVE). MOVE NOT in tool.
- Confidence: medium

### Markets habituate to repeated policy shocks (reactions get muted)
- Source: Kenneth Tropin — same file (quote: "the market reaction is beginning to get a little more muted each time. And that's because we're getting used to this")
- Type: re-entry/exit
- Rule as testable logic: IF successive policy-shock events produce smaller VIX spikes (each spike < 60% of the prior, proposed) THEN fade later shocks: re-risk sooner (shorter de-risk holding period).
- Data needed: VIX daily (in tool), event dates.
- Confidence: low

### Low VIX may understate risk
- Source: Kenneth Tropin — same file (quote: "if you look at the VIX, it's telling us, right, that risk is perceived of to be low, which I I'm not sure I agree with")
- Type: hedge
- Rule as testable logic: IF VIX < 15 (proposed) AND composite vulnerability (valuation top decile) THEN buy cheap protection: 3-6 month 10% OTM SPY puts with ~0.5-1% of portfolio per year (proposed), or VIX calls.
- Data needed: VIX (in tool), CBOE put-write/put index (PPUT 1986, free), option prices (CBOE). Put index NOT in tool.
- Confidence: medium

### Tariffs: Fed split between growth-cut and inflation-hold camps (stagflation possible)
- Source: Kenneth Tropin — same file (quote: "are the tariffs inflationary or are we getting a recession because of them?")
- Type: regime map
- Rule as testable logic: IF core CPI 3m annualized > 3% AND unemployment 3m change > +0.2 pts (stagflation lite, proposed) THEN underweight equities and long nominal Treasuries, overweight T-bills, gold, commodities, TIPS.
- Data needed: CPILFESL, UNRATE (in tool), gold (NOT).
- Confidence: medium

### Equity valuations only justified if AI delivers earnings with low inflation
- Source: Kenneth Tropin — same file (quote: "there's no reason for equities to be at record highs unless you believe AI is going to create a lot of uh earnings momentum and growth")
- Type: conflict/caveat
- Rule as testable logic: IF forward EPS revisions for S&P turn negative (3m) while P/E > 22 THEN de-rate risk: underweight Nasdaq/semis (SMH, QQQ) vs equal-weight (RSP). Also: AI job creation -> wage pressure -> higher rates (IF ECI wages y/y > 4.5%, proposed, underweight duration).
- Data needed: EPS revisions (no free; proxy S&P operating EPS quarterly from S&P website), ECI (FRED ECIWAG, 2001). NOT in tool.
- Confidence: low

### Deficit inflection: market psychology turns suddenly; VIX not yet worried
- Source: Kenneth Tropin — same file (quote: "I don't know when the market psychology is going to focus on the deficit")
- Type: signal
- Rule as testable logic: IF 30y Treasury yield rises > 50bp in 3m without a rise in breakevens (real-yield driven) AND term premium 3m change > +30bp (proposed) THEN fiscal-scare regime: underweight long Treasuries, overweight T-bills, gold.
- Data needed: DGS30 (1977), T10YIE, ACM term premium. Partly in tool.
- Confidence: medium

### 1980s bond losses: rates 6% -> 18%, bonds fell ~45%
- Source: Kenneth Tropin — same file (quote: "I had clients that own bonds that went down 45% in value")
- Type: position sizing/risk
- Rule as testable logic: Stress test: long-duration allocation (TLT-like) must survive a 1977-1981 replay (~-45%); cap TLT weight so portfolio loss < 15% in that scenario (proposed max ~30% in long Treasuries when inflation regime is on).
- Data needed: Long Treasury returns (Ibbotson/FRED long yields 1953; synthetic from DGS30).
- Confidence: medium

### Illiquid private equity / multistrat lockups amplify an equity correction
- Source: Kenneth Tropin — same file (quote: "if you were to have uh some sort of relatively normal correction in equity prices and you have a lot of money tied up in illquid private equity ... that could be pretty provocative")
- Type: signal
- Rule as testable logic: IF listed private equity ETF (PSP) underperforms S&P by > 15% over 6m (proposed) THEN illiquidity-stress flag; add to warning count.
- Data needed: PSP (2006), listed PE index (LPX50, 1993). NOT in tool.
- Confidence: low

### Fed independence pressure -> small, temporary corrections; expect a dovish successor
- Source: Kenneth Tropin — same file (quote: "it it upsets the market and and people don't, you know, usually get uh nervous and and and then you see a little bit of a tiny correction in in prices. But uh I think this is all going to go away")
- Type: conflict/caveat
- Rule as testable logic: Contradicts Rogoff (file 2): Fed-independence headlines = short-lived dips; test: S&P/10y/gold 1m and 6m forward moves after Fed-pressure events (Trump tweets on Powell 2018-19, 2025).
- Data needed: event dates, prices.
- Confidence: medium

### Dollar decline overdone; EURUSD fair value ~1.10-1.14; trading range; 5% 10y draws a huge bid
- Source: Kenneth Tropin — same file (quote: "every time the tenure gets to 5% there's a huge bid")
- Type: signal (currency, rates)
- Rule as testable logic: IF 10y yield >= 5% THEN buy 10y/long Treasuries (mean reversion), hold 3-6m; IF EURUSD > 1.15 (above his 1.10-1.14 fair band) THEN underweight euro vs dollar (range trade). Contradicts Rogoff/Gromen structural dollar decline.
- Data needed: DGS10 (1962), EURUSD (FRED DEXUSEU 1999; synthetic DM pre-1999). EURUSD NOT in tool.
- Confidence: medium

### Diversify some portfolio outside US and outside traditional assets (gold, crypto, EM)
- Source: Kenneth Tropin — same file (quote: "it makes sense for investors to have some of their portfolio not just invested in the the United States and and not just in, uh, traditional investments")
- Type: position sizing/risk
- Rule as testable logic: Strategic allocation: hold permanent small sleeves (proposed 5% gold, 2% bitcoin, 10% ex-US equity) and test whether adding them to tool's SPY/TLT/T-bill mix raises Sharpe and lowers max drawdown.
- Data needed: GLD/gold (1968 LBMA), BTC (2014), ACWX/EFA (2001; MSCI EAFE 1970). NOT in tool.
- Confidence: medium

### EM sovereign spreads very tight (caution)
- Source: Kenneth Tropin — same file (quote: "credit spreads on emerging market bonds for example are you know really tight")
- Type: signal (credit/EM)
- Rule as testable logic: IF EM sovereign spread (EMBI) in bottom 10% of history THEN underweight EM USD bonds (EMB) vs Treasuries; IF top 10% THEN overweight.
- Data needed: ICE BofA EM corporate OAS (FRED BAMLEMCBPIOAS, 1998), EMB (2007). NOT in tool.
- Confidence: medium

### Expected Fed cut late-2025; Europe delivered cuts, US disappointed (rate expectations swing)
- Source: Kenneth Tropin — same file (quote: "We started the year before the uh trade announcement the tariff announcements expecting four cuts this year. Now maybe we'll get one")
- Type: signal
- Rule as testable logic: IF market-implied cuts over next 12m (2y yield minus fed funds < -50bp) fall by > 50bp within 3m (hawkish repricing, proposed) THEN underweight 2y/duration and growth equities; relative: IF ECB cuts more than Fed THEN long USD vs EUR.
- Data needed: DGS2, FEDFUNDS, ECB rate, German 2y (FRED IRLTLT01DEM156N is 10y; 2y from Bundesbank). Partly in tool.
- Confidence: low

---

## File 6: Margrethe Vestager — EU Competition Commissioner, NBIM (Sep 2024)

(Mostly regulatory/policy; few macro rules. Extracted what can be turned into index/sector tests.)

### EU regulation of big tech (DMA/DSA, Google adtech breakup as last resort) -> regulatory overhang on mega-cap tech
- Source: Margrethe Vestager — Margrethe Vestager - Commissioner for Competition (quote: "we have the competence to ask for a breakup of a company but it would be a meure of L Resort")
- Type: signal (event)
- Rule as testable logic: IF EU/US antitrust escalation (statement of objections or breakup request against a top-5 S&P company) THEN short-term underweight cap-weighted tech (XLK/QQQ) vs equal-weight (RSP) for 3m (event study). Consistent with Scott Nations (file 3).
- Data needed: Event dates (EC press releases), QQQ, RSP (2003). NOT in tool.
- Confidence: low

### European defense consolidation as budgets rise
- Source: Margrethe Vestager — same file (quote: "since uh defense budgets are increasing and we spent most of that today outside of Europe there is indeed room for consolidation of a European Defense industry")
- Type: action/instrument (sector/geopolitics)
- Rule as testable logic: IF European defense spending/GDP rising (NATO annual) THEN overweight European defense ETF (EUAD/ Stoxx Europe Aerospace & Defense) vs Stoxx 600; corroborates Rogoff (file 2).
- Data needed: NATO defense expenditure (annual 2014+; SIPRI 1949), Stoxx A&D index. NOT in tool.
- Confidence: low

### Fragmented EU capital/telco/banking markets restrain scale and bank recovery
- Source: Margrethe Vestager — same file (quote: "we really miss a European Capital Market we really miss a European Telco market")
- Type: regime map (country/region)
- Rule as testable logic: Structural caveat: European banks recovered slower than US post-GFC; IF Capital Markets Union / banking-union progress (event) THEN overweight European banks (EUFN) vs US banks (KBE) 12m. Test: EUFN vs KBE relative return around 2014 banking union, 2024-25 consolidation news.
- Data needed: EUFN (2010), Stoxx Europe 600 Banks (SX7E, 1987), KBE (2005). NOT in tool.
- Confidence: low

### Europe cheap-energy dependence (Gazprom) = hidden security cost; gas supply now diversified (10-12 suppliers, LNG)
- Source: Margrethe Vestager — same file (quote: "we didn't realize that there was the price to pay uh to get cheap energy and the price that we paid was uh our security")
- Type: signal (commodity/geopolitics)
- Rule as testable logic: IF European gas price (TTF) 3m change > +100% (proposed) THEN underweight European equities (VGK, EWG) vs US; IF TTF back below its 12m average THEN re-enter. Diversified LNG reduces future sensitivity (test pre/post 2023).
- Data needed: Dutch TTF gas (World Bank Pink Sheet "Natural gas, Europe" monthly 1960 free; ICE daily), VGK (2005), MSCI Europe (1970). NOT in tool.
- Confidence: medium

### China industrial playbook (solar, now wind, batteries) -> Western producers uncompetitive
- Source: Margrethe Vestager — same file (quote: "the Chinese market working as a as a building ground uh for a solar panel industry now with a huge uh production at very low cost")
- Type: action/instrument (sector)
- Rule as testable logic: IF China capacity share in a clean-tech industry > 70% (proposed; IEA) THEN avoid Western clean-tech ETFs (TAN, ICLN) unless trade protection (tariffs/foreign subsidies regulation) is enacted; event test on 2012-13 EU/US solar tariffs.
- Data needed: IEA manufacturing capacity shares (annual), TAN (2008), ICLN (2008). NOT in tool.
- Confidence: low

### Economic security: export controls on AI, semiconductors, biotech as geopolitics hardens
- Source: Margrethe Vestager — same file (quote: "economic competition and systemic rivalry which has made us be much more focusing on economic security")
- Type: signal (geopolitics)
- Rule as testable logic: IF new export-control round on semiconductors to China (event) THEN underweight semis (SMH) for 1-3m and China tech (KWEB); test event returns (Oct 2022, Oct 2023, Dec 2024).
- Data needed: Event dates (BIS rules), SMH (2000; SOX index 1994), KWEB (2013). Chips vs 12m high in tool; events NOT.
- Confidence: low

### Europe's competitiveness crisis is slow; crises of life and death get fast responses
- Source: Margrethe Vestager — same file (quote: "the crisis of uh com U competitiv is a slow one competitiveness being eroded over years it will take time to to rebuild")
- Type: regime map
- Rule as testable logic: Structural: do not expect quick European outperformance from reform announcements; Europe overweight only on cyclical/valuation signals (e.g., Europe CAPE discount to US > 40%, proposed, AND Euro area PMI rising).
- Data needed: Country CAPE (Research Affiliates/Barclays), Euro area PMI (S&P Global; proxy OECD CLI euro area FRED EA19LOLITONOSTSAM 1960s). NOT in tool.
- Confidence: low

---

## File 7: Paul Krugman — Generating Alpha Podcast Ep. 28 (Jul 2025)

### Stable wealthy countries can carry very high debt without crisis (US post-WWII ~106%, UK 250%)
- Source: Paul Krugman — Episode 28- Paul Krugman (quote: "stable wealthy countries uh have historically been able to run up very large debts without a crisis")
- Type: conflict/caveat
- Rule as testable logic: Contradicts Gromen/Rogoff fiscal-dominance rules: test whether debt/GDP level alone predicts 10y yield or term premium changes over 1-5y in advanced economies (1950-2025, JST macrohistory data). IF no predictive power THEN do not use debt level as a standalone underweight-Treasuries signal; use only credibility/market signals.
- Data needed: Jorda-Schularick-Taylor Macrohistory database (17 countries, 1870-2020, free), GFDEGDQ188S. NOT in tool.
- Confidence: high

### The real US debt risk is credibility, not arithmetic
- Source: Paul Krugman — same file (quote: "the biggest reason to worry about a US debt crisis is that uh are we still uh that are we still a credible country?")
- Type: signal
- Rule as testable logic: IF US 10y yield rises while dollar falls AND gold rises (all over 1-3m: 10y +30bp, DXY -3%, gold +5%, proposed) THEN credibility-loss regime: underweight long Treasuries and USD, overweight gold and non-US assets; IF yields rise with dollar up THEN normal tightening.
- Data needed: DGS10, DXY, gold. Gold NOT in tool.
- Confidence: high

### Rates persistently higher than expected ("some mystery") -> interest burden rising
- Source: Paul Krugman — same file (quote: "interest payments are up and there's some mystery about why interest rates are higher than than persistently higher than they were")
- Type: signal
- Rule as testable logic: IF 10y yield minus (Fed funds + term premium model) residual rises (proposed) — simpler: IF 10y term premium > 0.5% and rising 12m THEN underweight duration. (Term premium 12m change already in tool.)
- Data needed: ACM term premium (in tool).
- Confidence: low

### Tariffs in violation of trade agreements (Korea FTA hit with 25%) -> US untrustworthy; China looks more credible
- Source: Paul Krugman — same file (quote: "we have a free trade agreement with South Korea, and we've just hit them with uh 25% tariffs")
- Type: action/instrument (country)
- Rule as testable logic: IF US tariff rate on a trade partner rises > 10 pts (event) THEN underweight that country's equity ETF (EWY Korea, EWJ Japan, EWW Mexico, EWC Canada) for 3m vs ACWI; long-run: underweight USD (credibility). Event study around Apr 2, 2025 and 2018-19.
- Data needed: Country tariff announcements (manual; Peterson Institute tracker), MSCI country ETFs. NOT in tool.
- Confidence: medium

### Restoring credibility takes decades (Latin America 'original sin'; Brazil now borrows in reais)
- Source: Paul Krugman — same file (quote: "Brazil can now borrow and reage um and um um but it took decades of reasonably responsible policy to get there")
- Type: regime map (EM)
- Rule as testable logic: IF EM country issues most debt in local currency (local-currency share > 80%, proposed) THEN it is less vulnerable to dollar spikes: prefer such countries (Brazil, Mexico, Indonesia) in EM local bond exposure (EMLC) vs dollar-debt-heavy issuers when DXY rising.
- Data needed: BIS debt securities statistics by currency (quarterly, 1990s), EMLC (2010). NOT in tool.
- Confidence: medium

### US credibility loss opens room for China and big developing countries (Brazil); EU third superpower
- Source: Paul Krugman — same file (quote: "there are three superpowers in the world economically which is US, China and the EU")
- Type: action/instrument (country)
- Rule as testable logic: IF US credibility-loss regime (see above) THEN tilt equity sleeve from US to EU (VGK), China (MCHI), Brazil (EWZ) by 10-20 pts (proposed) for 12m.
- Data needed: ETFs, regime flag.
- Confidence: low

### Underpowered fiscal response after a financial crisis = slow recovery; European austerity destructive
- Source: Paul Krugman — same file (quote: "it was just obvious to me uh that that the Obama stimulus was way too small and that it would take years to recover")
- Type: regime map
- Rule as testable logic: IF post-crisis fiscal impulse is small (structural deficit narrows while output gap < -2%, proposed) THEN expect prolonged low rates/low inflation: overweight long government bonds of that country (e.g., Bunds/BTPs 2011-2014, TLT 2010-2012), underweight its equities vs countries with larger stimulus.
- Data needed: IMF WEO output gap and structural balance (annual 1980), OECD Economic Outlook. NOT in tool.
- Confidence: medium

### Macro policy is mostly made by the Fed; fiscal usually not that consequential
- Source: Paul Krugman — same file (quote: "under normal circumstances or what used to be normal circumstances, what the federal government does is usually not that consequential for the economy as a whole")
- Type: conflict/caveat
- Rule as testable logic: Weighting caveat: give Fed-policy indicators (fed funds change, real rates) more weight than fiscal indicators in normal times; fiscal signals only in crises/zero-bound regimes (fed funds < 0.5%).
- Data needed: FEDFUNDS (in tool).
- Confidence: medium

### Inequality at Gilded Age levels and populism -> policy risk
- Source: Paul Krugman — same file (quote: "inequality of both income and wealth is now at at levels that are really back to guil back to the guilded age")
- Type: regime map (low testability)
- Rule as testable logic: IF top-1% wealth share > 30% (proposed) THEN higher probability of populist policy shocks (tariffs, Fed pressure, taxes); use as a slow-moving tilt toward real assets and away from long nominal bonds. Weak/long-horizon; test with WID data vs subsequent inflation.
- Data needed: Fed DFA top 1% wealth share (FRED WFRBST01134, 1989), WID.world (1913). NOT in tool.
- Confidence: low

### Zero/negative immigration -> lower future US living standards (growth)
- Source: Paul Krugman — same file (quote: "if we're going to have zero or negative immigration from here on in, that's going to be a real blow to the uh future living standards")
- Type: signal
- Rule as testable logic: IF labor force growth y/y < 0.3% (proposed) THEN lower trend GDP: lower long-run equity earnings growth and tighter labor market -> wage inflation; tilt toward short duration and away from domestic cyclicals.
- Data needed: CLF16OV (FRED, 1948). NOT in tool.
- Confidence: low

### Skeptical of AI job displacement; nobody knows AI's economic impact
- Source: Paul Krugman — same file (quote: "if it really leads to huge job displacement which I'm always skeptical about but you know there could be a first time")
- Type: conflict/caveat
- Rule as testable logic: Caveat: do not build AI-unemployment signals until data show it; monitor youth/college-grad unemployment vs overall (youth jobless already in tool).
- Data needed: youth unemployment (in tool), recent-grad unemployment (NY Fed, 1990).
- Confidence: medium

### Financialization: finance ~3 extra points of GDP, innovations (subprime, CDOs, crypto) mostly costs
- Source: Paul Krugman — same file (quote: "there was a lot of financial innovation, subprime lending, CDOS's, all of that stuff uh which all helped pave the way for the financial crisis")
- Type: signal
- Rule as testable logic: IF fast growth in a new credit product (e.g., private credit AUM, non-bank lending, or crypto market cap > 20% y/y for 2y, proposed) THEN raise financial-crisis risk weight; combine with credit spreads.
- Data needed: Fed Z.1 nonbank credit (quarterly 1945), crypto market cap (CoinGecko 2013). NOT in tool.
- Confidence: low

---

## File 8: Jeff Yass (Susquehanna) — Economic Myths, Generating Alpha Ep. 55 (Jun 2026)

### Measure US debt against national wealth, not GDP (debt ~13-14% of wealth = historic low)
- Source: Jeff Yass — Episode 55- Economic Myths with Jeff Yass (quote: "if you measure it to wealth, which is really the only thing that matters, it's at a very low uh a very low number")
- Type: signal / conflict
- Rule as testable logic: Alternative fiscal indicator: federal debt / household net worth. IF debt/net worth < 15% THEN no fiscal-stress underweight of Treasuries; IF > 20% (proposed) or rising > 2 pts in 2y THEN fiscal-stress flag. Test vs debt/GDP for predicting term premium and 10y real yield changes. Contradicts Rogoff/Gromen debt/GDP framing.
- Data needed: Federal debt (FRED GFDEBTN, 1966), household net worth (FRED TNWBSHNO / BOGZ1FL192090005Q, 1945). NOT in tool.
- Confidence: high

### US goes broke only if wealth gets annihilated (e.g., $230tn -> $100tn)
- Source: Jeff Yass — same file (quote: "The way we go broke is if that $230 trillion wealth gets annihilated and goes down to 100 trillion")
- Type: signal
- Rule as testable logic: IF household net worth falls > 15% y/y (proposed; happened 2008-09) THEN fiscal capacity concern + recession: overweight long Treasuries (flight to quality) short-term, then watch for fiscal stress. Also implies market cap/GDP is a wealth buffer, not just a valuation warning (contrast with existing market cap/GDP indicator).
- Data needed: TNWBSHNO (quarterly 1945). NOT in tool.
- Confidence: medium

### US stock market ~2.5x GDP vs ~1x in Europe/China -> different situation
- Source: Jeff Yass — same file (quote: "our stock market is worth $80 trillion, or or two and more than two and a half times our GDP, while other countries, particularly Europe, China, their stock market value and their GDPs are roughly one to one")
- Type: conflict/caveat
- Rule as testable logic: Caveat to the tool's market cap/GDP valuation warning: test whether US market cap/GDP still predicts 10y returns after 2010 (structural break from global revenues/intangibles); and cross-country: IF a country's market cap/GDP is in bottom third of its own history THEN overweight (country valuation rule).
- Data needed: World Bank market cap/GDP by country (CM.MKT.LCAP.GD.ZS, annual 1975-2020s), Wilshire 5000/GDP (FRED). Market cap/GDP in tool (US only).
- Confidence: medium

### Wasteful spending (~$2tn/yr) is the problem, not the debt itself
- Source: Jeff Yass — same file (quote: "we're spending 7 trillion when 5 trillion could have gotten the same job done")
- Type: conflict/caveat
- Rule as testable logic: No direct trade; supports using growth/productivity indicators over fiscal ratios.
- Data needed: none.
- Confidence: low

### Bad policy (regulation, very high taxes) could make US "become Europe" — possible 2029 risk
- Source: Jeff Yass — same file (quote: "we might well see this in 2029, uh regulation that makes it impossible for business to get started, uh super high taxes")
- Type: signal (political event)
- Rule as testable logic: IF top marginal capital gains/corporate tax rate increases legislated (> 5 pts, proposed) THEN underweight US small caps/new-business-sensitive (IWM) and US vs Europe for 12m; event study 1987, 1993, 2013 tax hikes.
- Data needed: Tax rate history (Tax Policy Center, 1913), IWM (2000; Russell 2000 1979). NOT in tool.
- Confidence: low

### US 50% richer than Europe with similar population (growth engine)
- Source: Jeff Yass — same file (quote: "we're roughly the same, you know, population as as most of Europe, and we're 50% richer")
- Type: conflict/caveat
- Rule as testable logic: Supports default US-equity overweight vs Europe unless valuation gap extreme; test SPY vs VGK when US/Europe CAPE ratio > 2 (proposed) -> Europe outperforms next 5y?
- Data needed: Country CAPE (Research Affiliates/Barclays), MSCI USA/Europe (1970). NOT in tool.
- Confidence: low

### Consumer surplus: firms capture ~2-10% of the value they create
- Source: Jeff Yass — same file (quote: "I say the typical number somewhere around 10%. So, most of the money most of the wealth created is just given to the consumer")
- Type: conflict/caveat
- Rule as testable logic: Not testable as a trading rule; implies anti-business policy (taxes, vilification) hurts long-run growth. No instrument mapping.
- Data needed: none.
- Confidence: low

---

## File 9: Karen Karniol-Tambour (Bridgewater) — Sohn 2022, A Macro Approach (May 2022)

### Corporate profits at multi-decade highs vs GDP -> mean reversion risk
- Source: Karen Karniol-Tambour — Sohn 2022 - A Macro Approach (quote: "u.s corporate profits are currently at the highest level they've really ever been um so you can see here multi multi-decade highs relative to the size of the economy")
- Type: signal
- Rule as testable logic: IF corporate profits/GDP in top 10% of post-1947 history AND turning down (4-quarter change < 0) THEN underweight US equities (proposed 25% cut) for 12-24m; IF profits/GDP in bottom quintile and rising THEN overweight.
- Data needed: Corporate profits after tax with IVA/CCAdj (FRED CPATAX 1947 / A446RC1Q027SBEA) / GDP. NOT in tool.
- Confidence: high

### Kalecki profit logic: profits come from spending not paid as wages (household borrowing, capex borrowing, government deficits)
- Source: Karen Karniol-Tambour — same file (quote: "you need to find a way for basically all the workers in the economy to pay for your goods without actually earning that money and income")
- Type: signal
- Rule as testable logic: Profit-source indicator = (government deficit + net private borrowing + household dissaving) / GDP. IF this sum's 4-quarter change < -2 pts of GDP (fiscal pullback, falling credit growth, rising savings) THEN expect profit margin compression: underweight equities, overweight Treasuries 12m.
- Data needed: Federal deficit (FRED FGDEF? use M318501Q027NBEA, 1947), household credit growth (FRED CMDEBT, 1945), personal saving rate (PSAVERT, 1959), nonfinancial business debt (BCNSDODNS, 1945). NOT in tool.
- Confidence: high

### Fiscal checks ending + households dissaving via credit cards = unsustainable spending
- Source: Karen Karniol-Tambour — same file (quote: "the last couple months not many months but two three months of spending have been totally totally funded by households basically dis saving")
- Type: signal
- Rule as testable logic: IF personal saving rate falls > 3 pts below its 5y average (proposed) AND revolving credit y/y > 10% (proposed) AND real disposable income y/y < 0 THEN consumer spending slowdown ahead: underweight consumer discretionary (XLY) vs staples (XLP), cut equities 6-12m.
- Data needed: PSAVERT, REVOLSL (1968), DSPIC96 (1959). NOT in tool (staples vs discretionary price ratio is in tool, but these drivers are not).
- Confidence: high

### Biggest rise in mortgage rates in decades + falling asset prices -> households won't re-lever
- Source: Karen Karniol-Tambour — same file (quote: "we already have the biggest rise in mortgage rates in decades very very fast very very rapid falling asset prices this isn't going to be the time that households choose now i wanted to")
- Type: signal
- Rule as testable logic: IF 30y mortgage rate 12m change > +1.5 pts (proposed) THEN household borrowing will slow with a lag (6-12m): underweight homebuilders and consumer discretionary; overweight long Treasuries later. (Mortgage rate 12m change already in tool.)
- Data needed: MORTGAGE30US (1971). In tool.
- Confidence: high

### Labor bargaining power shift (tightest labor market, lower-income wages rising) squeezes margins
- Source: Karen Karniol-Tambour — same file (quote: "we now have the tightest labor market in decades companies everywhere are raising wages")
- Type: signal
- Rule as testable logic: IF unit labor costs y/y > productivity-adjusted price growth (ULC y/y minus GDP deflator y/y > +1 pt, proposed) OR labor share of income rising 4 quarters THEN profit margin squeeze: underweight equities (esp. labor-intensive: retail XRT, restaurants), overweight T-bills.
- Data needed: Nonfarm business unit labor cost (FRED ULCNFB, 1947), GDP deflator (GDPDEF), labor share (PRS85006173, 1947), Atlanta Fed wage tracker (1997). NOT in tool.
- Confidence: high

### Peak pro-corporate environment: globalization done, corporate taxes lowest in decades, antitrust rising
- Source: Karen Karniol-Tambour — same file (quote: "we were kind of at the peak pro corporate environment and now we see lots of pressures the other way")
- Type: regime map
- Rule as testable logic: IF effective corporate tax rate (taxes on corporate income / pre-tax profits) at multi-decade low AND rising (proposed) THEN lower expected equity returns: reduce strategic equity weight; favour real assets.
- Data needed: Taxes on corporate income (FRED B075RC1Q027SBEA? / W025RC1Q027SBEA, 1947) / profits before tax (A053RC1Q027SBEA). NOT in tool.
- Confidence: medium

### Inelastic inflation (fuel, food) hits bottom 40-60% and non-commodity margins
- Source: Karen Karniol-Tambour — same file (quote: "there are particular areas like fuel and oil and gas and food that are specifically inelastic and specifically have inflation")
- Type: signal / action
- Rule as testable logic: IF food+energy CPI y/y minus core CPI y/y > +3 pts (proposed) THEN overweight commodity producers (XLE, XME, MOO agriculture, DBA) vs consumer discretionary and broad market; underweight non-commodity equities, 6-12m.
- Data needed: CPI energy (CPIENGSL 1957), food (CPIUFDSL 1947), core (CPILFESL). Oil 6m change in tool; food/energy-vs-core gap NOT; DBA (2007), World Bank agriculture index (1960).
- Confidence: high

### 1970s: stock market had ~30% commodity producers, today ~3% -> fewer inflation winners
- Source: Karen Karniol-Tambour — same file (quote: "back then about 30 of the stock market was commodity producers today it's more like 3")
- Type: action/instrument
- Rule as testable logic: IF inflation regime (core CPI > 4% and rising, or food+energy shock above) THEN hold commodities directly (DBC/GSG, gold) rather than relying on broad equity index as inflation hedge; equity index inflation beta is lower than in the 1970s.
- Data needed: Ken French industry portfolios (energy/mining weights, 1926), S&P GSCI TR (1970). NOT in tool.
- Confidence: high

### Inflationary environments raise the equity risk premium (1970s worst decade despite good profits)
- Source: Karen Karniol-Tambour — same file (quote: "equities actually did terribly in 1970s worst decade ever even though profits were good ... people demanded a higher risk free to be in stocks in an inflationary environment")
- Type: regime map
- Rule as testable logic: IF CPI y/y > 5% (proposed) THEN expect P/E compression: underweight equities vs commodities/T-bills until CPI y/y < 4% and falling. Test valuation (CAPE) changes conditional on inflation level 1900-2025.
- Data needed: Shiller CAPE and CPI (1871). CAPE and CPI in tool; conditional rule NOT.
- Confidence: high

### Resilience/decarbonization capex less profitable than past capex
- Source: Karen Karniol-Tambour — same file (quote: "these are big areas of spend that at least unless like not likely to boost profits the way that prior investments work")
- Type: signal
- Rule as testable logic: IF nonresidential investment share of GDP rising while return on capital (profits / capital stock) falling (proposed) THEN lower equity margin outlook; low testability.
- Data needed: FRED B008RC1Q027SBEA nonres investment (1947), BEA fixed assets. NOT in tool.
- Confidence: low

### Rule of thumb: +1.5 pts on 10y yield ≈ -15% equities (duration of a 10y earnings stream)
- Source: Karen Karniol-Tambour — same file (quote: "if interest rates rose one and a half percent on a 10-year bond and maybe you have a 10-year stream of earnings that's a 15 equity decline")
- Type: signal
- Rule as testable logic: Priced-in check: expected equity move = -10 x (10y yield change). IF actual S&P 6m return ≈ -10 x Δ10y (within 5%) THEN market has priced only rates, not an earnings slowdown: if slowdown indicators are on (warnings), cut further. IF actual drop >> rate-implied THEN slowdown already priced (consider re-entry).
- Data needed: DGS10, S&P (in tool).
- Confidence: medium

### Market priced Goldilocks; did not price slowdown or 1970s-style higher risk premium
- Source: Karen Karniol-Tambour — same file (quote: "the market is not really reflecting a significant economic slowdown it's kind of reflecting a beautiful goldilocks scenario")
- Type: signal
- Rule as testable logic: IF consensus forward EPS growth > 5% (proposed) WHILE recession indicators (tool warnings share > 25%) THEN underweight equities further (earnings downgrade not priced).
- Data needed: Forward EPS (no free series; proxy: S&P EPS estimates from S&P website, 1988). NOT in tool.
- Confidence: medium

### US exceptionalism priced in: after a decade of one country leading, disappointment more likely (rotate to rest of world)
- Source: Karen Karniol-Tambour — same file (quote: "once you have one decade where one country is really successful in this case the united states these things tend to get priced into the price")
- Type: action/instrument (country)
- Rule as testable logic: IF US equity 10y return minus ex-US (MSCI EAFE+EM) 10y return > +5%/yr (proposed) THEN overweight ex-US equities (EFA, EEM, VEU) vs US for next 5-10y. Test 1970-2025 (MSCI USA vs EAFE; Japan 1989 analogue).
- Data needed: MSCI USA, EAFE (1970), EM (1988) total return (MSCI end-of-day free); ETFs EFA (2001), VEU (2007). NOT in tool.
- Confidence: high

### QE inflates financial assets, boosts inequality, low spending multiplier; direct fiscal transfers have high multiplier
- Source: Karen Karniol-Tambour — same file (quote: "lots of money is printed lots of people get that money but really drives up financial assets and wealthy people own financial assets disproportionately")
- Type: regime map
- Rule as testable logic: IF policy easing is via QE (Fed assets up, deficit stable) THEN favour financial assets (equities, long bonds) over goods inflation hedges; IF easing is via direct transfers (deficit/GDP widens > 5 pts with transfers) THEN favour goods inflation hedges (commodities, TIPS) and expect profit surge then inflation (2020-22 pattern).
- Data needed: WALCL, federal deficit, personal current transfer receipts (FRED PCTR, 1959). NOT in tool (deficit, transfers).
- Confidence: high

### Pre-GFC: EM/oil-exporter dollar saving drove rates down and fueled leverage
- Source: Karen Karniol-Tambour — same file (quote: "there was a lot of desire from emerging markets particularly china and oil producers they wanted to save in dollars ... drove interest rates down")
- Type: signal
- Rule as testable logic: IF global FX reserves (IMF COFER total) growing > 10% y/y (proposed) THEN downward pressure on US long yields: overweight long Treasuries; IF reserves shrinking THEN underweight. Consistent with Gromen's foreign Treasury buying rule.
- Data needed: IMF COFER total reserves (1995 quarterly), TIC foreign official holdings. NOT in tool.
- Confidence: medium

---

## Cross-speaker conflicts in this batch

1. **US debt danger**: Gromen (needs sustained negative real rates, fiscal dominance), Rogoff (resolves via inflation or higher rates; Fed independence risk) vs Krugman (wealthy stable countries can carry very high debt; only credibility matters) vs Yass (debt vs wealth at historic low; not a problem). Test: does debt/GDP vs debt/net worth vs a market-based credibility signal (yields up + dollar down + gold up) predict bond returns?
2. **Dollar**: Rogoff and Gromen (structural decline; footprint peaked 2015) vs Tropin (decline overdone; trading range; 5% 10y draws buyers) vs Bessent (rising foreign demand for Treasuries).
3. **Fed tightening effect**: tool cuts stocks on Fed tightening; Gromen says it depends on the dollar (hikes OK when dollar falling); Rogoff says Fed will hike if left alone.
4. **Market timing**: Scott Nations (never sell in bear markets; don't get scared out) vs Tropin/Karniol-Tambour/Gromen (de-risk on macro vulnerability). Tool must beat buy-and-hold over full cycles.
5. **Fed independence headlines**: Rogoff (serious, leads to inflation, Nixon-style controls) vs Tropin (small temporary dips; will "go away").
6. **Tariffs and inflation**: Rogoff (tariff inflation "not a big deal", growth is the problem) vs Tropin (Fed constrained by tariff inflation) vs Karniol-Tambour (deglobalization ends the pro-corporate era).
7. **US exceptionalism**: Karniol-Tambour (priced in, rotate abroad), Krugman (US no longer credible) vs Bessent (US AI compute and energy dominance, 3% growth) and Yass (US 50% richer than Europe, wealth engine).
8. **Supply-chain inflation**: Gromen (CPI 7-10% for years from China water/energy limits; forecast missed) vs Rogoff (supply chain problems went away; inflation stayed because of central bank mistake).
9. **Oil shocks**: Bessent (duration matters, US insulated by production) vs Karniol-Tambour (inelastic energy inflation squeezes margins for 97% of non-commodity market).

---

## Batch summary (10 most important testable ideas)

1. **Profit-margin mean reversion via Kalecki sources** (Karniol-Tambour): corporate profits/GDP in top decile and turning down, plus a falling "profit source" sum (deficit + private borrowing - saving), predicts equity weakness. New FRED series, 1947+.
2. **Fed tightening conditioned on the dollar** (Gromen): hikes + strong/rising dollar = "deflationary fit" (cut risk); hikes + falling dollar = tolerable. Direct refinement of the tool's Fed-tightening gate.
3. **Diversifier choice by stock-bond correlation and inflation** (Tropin, Karniol-Tambour): when correlation > +0.3 or CPI > 5%, hedge with gold, commodities, managed futures (time-series momentum) or T-bills instead of long Treasuries. Extends the tool's TLT/T-bill switch to gold and a TSMOM sleeve.
4. **Inelastic food+energy inflation playbook** (Karniol-Tambour): when food+energy CPI y/y beats core by 3+ pts, own commodities directly (DBC, XLE, DBA, gold) and underweight discretionary; equity index is a weak inflation hedge now (~3% commodity producers vs ~30% in the 1970s).
5. **Inflation raises equity risk premium** (Karniol-Tambour): CPI > 5% means P/E compression; underweight equities vs commodities/T-bills until inflation falls (Shiller data back to 1871).
6. **US vs rest of world rotation** (Karniol-Tambour, Gromen, Rogoff, Krugman): after a decade of US outperformance > 5%/yr, or when "sell America" signal is on (yields up + dollar down + gold up), tilt to EFA/EEM/EWJ/EWZ etc.
7. **Fiscal-dominance / credibility signal, tested against alternatives** (Gromen/Rogoff vs Krugman/Yass): compare debt/GDP, debt/household net worth, interest/GDP and market-based credibility signals as predictors of term premium and long-bond returns.
8. **China/commodity-exporter link** (Rogoff): China growth proxy (OECD CLI, copper, Korea exports) drives Brazil, Norway, Australia, Canada, Chile ETFs and industrial metals; China japanification -> underweight China equities.
9. **Oil shock duration rule + SPR fade** (Bessent): de-risk only if oil stays > 50% above its 12m average for 3+ months; coordinated reserve releases mark peaks; oil importers (Japan, Korea, India, Europe) hurt more than the US.
10. **Capitulation re-entry** (Nations): record equity fund outflows and/or -20% drawdowns are buy points; compare the tool's re-entry rule with "never sell" and with flow-based re-entry, and require de-risk signals to beat buy-and-hold net of time out.

Also notable: Bessent's current-account + policy-regime-change currency trade (Abenomics template: short currency, long hedged equities); Gromen's Fed-buys-60%+-of-issuance -> dollar down; consumer dissaving (saving rate below 5y avg, revolving credit > 10% y/y) -> spending slowdown; cheap tail hedges (OTM puts) when VIX < 15 and valuations are high (Tropin).

---

## Data requests (series NOT in the existing tool list)

Fiscal/debt
- Federal debt/GDP: FRED GFDEGDQ188S (1966); federal debt GFDEBTN (1966)
- Federal deficit/GDP: FRED FYFSGDA188S (annual 1929); quarterly M318501Q027NBEA (1947)
- Federal interest outlays: FRED A091RC1Q027SBEA (1947); federal receipts FGRECPT
- Household net worth: FRED TNWBSHNO (1945) -> debt/net worth
- Treasury bill share of marketable debt and refunding sizes: Treasury Fiscal Data MSPD (1996)
- Effective tariff rate: customs duties FRED B235RC1Q027SBEA / imports IMPGS (1947)
- Personal current transfer receipts: FRED PCTR (1959)
- Effective corporate tax rate: taxes on corporate income / profits before tax (FRED, 1947)
- Advanced-economy long history: Jorda-Schularick-Taylor Macrohistory database (1870-2020)
- IMF gov debt/GDP by country, output gap, structural balance (WEO, 1980)

Profits/labor/households
- Corporate profits after tax / GDP: FRED CPATAX or A446RC1Q027SBEA (1947)
- Unit labor costs ULCNFB (1947), labor share PRS85006173 (1947), GDP deflator GDPDEF, ECI wages ECIWAG (2001), Atlanta Fed wage tracker (1997)
- Personal saving rate PSAVERT (1959), revolving credit REVOLSL (1968), real disposable income DSPIC96 (1959), household credit CMDEBT (1945), nonfinancial business debt BCNSDODNS
- Consumer sentiment UMCSENT (1952/1978), UMich inflation expectations MICH (1978)
- Economic Policy Uncertainty USEPUINDXM (1985), Trade Policy Uncertainty (policyuncertainty.com)
- Labor force CLF16OV (1948); top-1% wealth share WFRBST01134 (1989)
- Case-Shiller national CSUSHPINSA (1987) and OER rent CPI (1983) -> price/rent
- Nonresidential investment share (BEA)

Inflation detail
- CPI energy CPIENGSL (1957), CPI food CPIUFDSL (1947), core goods CUSR0000SACL1E (1956)
- Real fed funds = FEDFUNDS - core CPI y/y
- NY Fed Global Supply Chain Pressure Index (1997); ISM prices paid / supplier deliveries
- China PPI and CPI (OECD MEI via FRED, 1993-96), US import prices

Liquidity/plumbing/flows
- Fed Treasury holdings TREAST (2002) vs net Treasury issuance -> Fed share of issuance
- Fed total assets WALCL (gross; partly in tool via net liquidity), RRP split, SLR-exemption dummy
- SOFR (2018), IORB/IOER (2008) -> repo stress spread
- TIC: foreign official/private net purchases of Treasuries and US equities (1977); FRED FDHBFIN; Fed custody WMTSECL1 (2002)
- Z.1 rest-of-world holdings of US equities (1945)
- IMF COFER dollar reserve share and total reserves (1995)
- ICI equity fund flows (1984); AAII sentiment (1987)
- CFTC Commitments of Traders positioning (1986)
- World Gold Council central-bank gold demand (2010)
- BIS debt securities by currency (EM local-currency share)

Markets/instruments
- Gold (LBMA/World Bank 1960; GLD 2004), silver, BTC-USD (2014), stablecoin supply (2018)
- Broad commodity indices: S&P GSCI TR (1970), BCOM, DBC (2006), World Bank Pink Sheet (agriculture, metals, iron ore, European gas TTF; 1960), DBA (2007)
- Brent DCOILBRENTEU (1987), WTI monthly history WTISPLC (1946)
- EIA US net petroleum imports (1973); IEA collective-action/SPR event dates
- DXY (Yahoo DX-Y.NYB 1971) and FX: USDJPY DEXJPUS (1971), EURUSD DEXUSEU (1999)
- MSCI country/region total returns (USA, EAFE 1970; EM 1988) and ETFs: EEM, EFA, VEU, VGK, EWJ, DXJ/HEWJ, EWY, EWZ, EWT, EWW, EWC, EWA, ENOR, ECH, EPU, ARGT, INDA, MCHI/FXI, KWEB, EWG, EWI, EWQ, EWS, EWM, EIDO
- Nikkei 225 FRED NIKKEI225 (1949); country CAPE (Research Affiliates/Barclays)
- World Bank market cap/GDP by country (1975)
- Japan current account % GDP (OECD/IMF, 1996); country current accounts
- China growth proxies: OECD CLI China (FRED), Korea exports (FRED XTEXVA01KRM667S), China house prices (BIS), China FDI (World Bank)
- Euro area OECD CLI, Euro area GDP; ECB deposit rate ECBDFR (1999); BoE Bank Rate; Bund yields
- Term premium ACM (already in tool) plus 30y yield DGS30 (1977)
- MOVE index (^MOVE, 2003); CBOE PPUT put index (1986); option prices for OTM SPY puts
- Managed futures / TSMOM: AQR TSMOM factor (1985), SG CTA Index (2000), BarclayHedge CTA (1980), DBMF (2019)
- EM credit: ICE BofA EM corporate OAS BAMLEMCBPIOAS (1998), EMB (2007), EMLC (2010)
- Listed private equity PSP (2006)/LPX50 (1993); BDC ETF BIZD (2013); bank loans to nondepository financials (H.8, 2015)
- Value vs growth: Ken French HML (1926), IWD/IWF (2000); QQQ/NDX (1985); RSP equal weight (2003)
- Sector/thematic ETFs: XLE, XME, MOO, XLY, XLP, XRT, ITB/XHB, KBE, EUFN, SMH, XLK, TAN, ICLN, ITA, EUAD
- IPO first-day returns (Jay Ritter, 1980); NATO/SIPRI defense spending (1949)
- Election/policy event dates (tariff announcements, antitrust actions, export controls, LatAm elections, SPR releases)
