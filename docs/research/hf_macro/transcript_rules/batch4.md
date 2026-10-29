# Batch 4 — testable rules from macro transcripts

Files (8): BG2 Gurley & Gerstner (AI, Middle East, China, Tariffs, Recon Bill); Rob Citrone (Capital Allocators EP.261, Jul 2022); Scott Bessent (Trump's new Treasury Secretary on macro strategy); Real Eisman Playbook Ep 73 (AI trade, rising rates); Peter Oppenheimer (Goldman); Christine Lagarde (In Good Company); Kristalina Georgieva (IMF); The Weekly Wrap (Is OpenAI the Achilles' heel).

Notes: auto-captions; quotes copied verbatim from the caption text (including caption spelling errors). "(proposed)" = threshold not given by the speaker.

---

## File 1 — AI, Middle East, China, Tariffs, Recon Bill, Invest America (BG2, Bill Gurley & Brad Gerstner, May 2025)

Mostly policy/tech commentary; few general macro rules.

### Tariff-shock size vs GDP (tariff revenue as headwind)
- Source: Brad Gerstner — AI, Middle East, China, Tariffs, Recon Bill, Invest America - BG2 (quote: "$2 trillion in tariffs is probably a 600 to 700 basis point headwind to GDP")
- Type: signal
- Rule as testable logic: IF announced/effective customs-duty revenue (annualized) rises above 1.5% of GDP (proposed) THEN underweight US equities (SPY) vs T-bills until the effective tariff rate falls back by at least one third (proposed). Gerstner's mapping: ~$300bn on a $28tn economy (~1%) is "not that big a headwind"; $800bn–$2tn is severe.
- Data needed: US customs duties (Treasury Monthly Statement / FRED B235RC1Q027SBEA, quarterly from 1947) / nominal GDP (FRED GDP); effective tariff rate (Yale Budget Lab, ad hoc). Not in tool.
- Confidence: medium.

### Policy-path resolution rally ("landing the plane")
- Source: Brad Gerstner — BG2 (quote: "chaos is very difficult both for investors but also for executives like committing to hiring programs committing to capex")
- Type: re-entry/exit
- Rule as testable logic: IF S&P 500 fell ≥15% from its high on a policy shock (tariffs) AND a policy-uncertainty measure drops ≥30% from its peak within 1 month (proposed) THEN re-enter equities (SPY) fully; hold 6–12 months. (Market fell 20% then bounced 20% in 20 trading days once tariffs were walked back.)
- Data needed: Economic Policy Uncertainty index / Trade Policy Uncertainty index (policyuncertainty.com, FRED USEPUINDXD daily from 1985; trade EPU monthly from 1985); S&P 500. Not in tool.
- Confidence: medium.

### Fiscal stimulus from tax cuts / immediate expensing
- Source: Brad Gerstner — BG2 (quote: "you add those things up, that's probably a four or$500 billion annual stimulus to the economy")
- Type: signal
- Rule as testable logic: IF enacted fiscal impulse (change in structural deficit) > +1% of GDP for the coming year (proposed) THEN overweight cyclicals/capex beneficiaries (industrials XLI, equal-weight RSP) vs defensives for 12 months; and treat as a mild negative for long Treasuries (TLT) if deficit already > 5% of GDP.
- Data needed: CBO/IMF fiscal impulse; FRED FYFSGDA188S (federal surplus/deficit % GDP, annual from 1929). Not in tool.
- Confidence: low.

### Deficit size caveat (no quick fiscal fix)
- Source: Brad Gerstner — BG2 (quote: "people should not get their hopes up that they're going to wake up next year and that our our our budget deficit is going to magically be, you know, cut by 50%")
- Type: conflict/caveat
- Rule as testable logic: IF federal deficit > 6% of GDP outside recession (proposed) THEN expect persistent supply pressure on long bonds: prefer short Treasuries (SHY/BIL) over long (TLT) when term premium is also rising (combine with existing "term premium 12m change"). 
- Data needed: FRED FYFSGDA188S / MTSDS133FMS (monthly deficit from 1980); term premium (in tool).
- Confidence: low.

### Stablecoin demand for T-bills
- Source: Brad Gerstner — BG2 (quote: "in 5 to 10 years, stable coin issuers will become the biggest holders of US debt on the planet")
- Type: conflict/caveat (structural)
- Rule as testable logic: IF stablecoin market cap growth y/y > 50% (proposed) THEN expect extra demand for short Treasuries (bills) — test whether bill-OIS / 3m bill minus fed funds falls. Not a trading rule yet; monitoring variable.
- Data needed: stablecoin supply (DefiLlama, from 2018); FRED DTB3 and DFF. Not in tool.
- Confidence: low.

### Geopolitical fork (Iran) as oil risk
- Source: Brad Gerstner — BG2 (quote: "either signed the the nuclear non-prololiferation uh deal on the table or, you know, we could have a a hot war situation with Iran")
- Type: hedge
- Rule as testable logic: IF a Middle East escalation event (proposed: Brent +10% in 5 days) THEN hold a small oil/energy hedge (USO/XLE 5% of portfolio, proposed) for 1–3 months; remove when Brent retraces half the spike.
- Data needed: Brent (FRED DCOILBRENTEU daily from 1987); geopolitical risk index (Caldara–Iacoviello GPR, monthly from 1900, daily from 1985). GPR not in tool.
- Confidence: low.

### China tariff de-escalation = biggest catalyst
- Source: Brad Gerstner — BG2 (quote: "the markets appropriately recognize that the China tariff agreement is the biggest one and the most important")
- Type: signal
- Rule as testable logic: IF US–China effective tariff rate falls by ≥10 pts (proposed) THEN overweight China equities (MCHI/FXI) and US importers/retail (XRT) vs SPY for 3–6 months.
- Data needed: US–China effective tariff (PIIE chart; ad hoc); MCHI (2011), FXI (2004). Not in tool.
- Confidence: low.

### AI capex beneficiary (semis) from export-control easing
- Source: Brad Gerstner — BG2 (quote: "This is going to be in a ton of business for companies like Nvidia, companies like AMD, folks who are suppliers to those companies.")
- Type: action/instrument
- Rule as testable logic: IF export controls on AI chips are loosened (event) THEN overweight semiconductor ETF (SMH/SOXX) vs SPY for 6 months; IF tightened (e.g. H20 ban) THEN underweight. Event study.
- Data needed: event dates (BIS rules); SMH (2000), SOXX (2001). Sector ETF not in tool (tool has "chips vs 12m high").
- Confidence: low.

---

## File 2 — Rob Citrone, Discovery Capital (Capital Allocators EP.261, July 2022)

### Fed put absent when inflation is high
- Source: Rob Citrone — Rob Citrone – Emerging Markets, Hedge Funds (quote: "even if the market will crash there's not much the fed can do because of the inflation issue")
- Type: regime map
- Rule as testable logic: IF S&P 500 drawdown ≥ 20% AND core CPI y/y ≤ 3% THEN buy the crash (Fed will ease, 1987 template; hold 12 months). IF drawdown ≥ 20% AND core CPI y/y > 4% (proposed) THEN do not buy the dip; stay underweight until Fed funds 3m change ≤ 0.
- Data needed: S&P 500; core CPI (in tool); Fed funds (in tool).
- Confidence: high.

### QT = second phase of the bear market
- Source: Rob Citrone — Citrone EP.261 (quote: "if qe had a major impact on asset prices rising we've done six trillion of it ... as we take three trillion out it has to have a significant impact on asset prices")
- Type: signal
- Rule as testable logic: IF Fed total assets 6m change < −3% (proposed) (balance-sheet shrinking) AND Fed funds rising THEN underweight equities and long-duration growth (QQQ) vs T-bills; exit when balance sheet 3m change ≥ 0.
- Data needed: FRED WALCL (weekly from 2002); tool has "Fed net liquidity 3m change" (close; add raw WALCL change).
- Confidence: high.

### Core inflation peak = 3 months of declining y/y
- Source: Rob Citrone — Citrone EP.261 (quote: "it's already three months in a row year over year it's come down and even month over month come down so we think core inflation's peaked")
- Type: signal
- Rule as testable logic: IF core CPI y/y has fallen 3 consecutive months AND core m/m is below its 6m average THEN declare inflation peak: start adding duration (IEF/TLT) and EM local bonds (EMLC) over 3–6 months; but don't expect Fed to stop until core y/y is within 1pt of target.
- Data needed: FRED CPILFESL (1957); tool has core inflation 3m vs 12m and core CPI y/y.
- Confidence: high.

### Headline inflation risk = energy and food
- Source: Rob Citrone — Citrone EP.261 (quote: "the real risk on the headline is energy prices and maybe food prices")
- Type: conflict/caveat
- Rule as testable logic: IF core CPI y/y falling BUT oil 6m change > +20% or food CPI y/y > 8% (proposed) THEN delay duration add until energy/food momentum turns negative.
- Data needed: oil 6m change (in tool); FRED CPIUFDSL food CPI (1947) — not in tool.
- Confidence: medium.

### Reserve currency cushions US in crises
- Source: Rob Citrone — Citrone EP.261 (quote: "we're the reserve currency of the world even during times of crisis we have strengthening in our currency as a result our interest rates don't have to go as high")
- Type: regime map
- Rule as testable logic: IF global risk-off (VIX > 30) THEN expect dollar (UUP/DXY) to rise: hold dollar long (UUP) as crisis hedge; EM currencies (CEW) underweight until VIX < 25.
- Data needed: DXY/UUP (2007; DXY from 1971 via FRED DTWEXBGS 2006 / DTWEXM 1973); VIX (in tool); CEW (2009).
- Confidence: medium.

### EM currency crisis -> debt crisis (FX-denominated debt)
- Source: Rob Citrone — Citrone EP.261 (quote: "a lot of these currency crisis then would lead to debt crisis because the currency would devalue so much they then couldn't pay their debt it was denominated another currency")
- Type: signal (country)
- Rule as testable logic: IF a country's FX reserves (net of swaps) fall below 3 months of imports (proposed) AND currency is pegged/managed AND inflation > 20% THEN short its currency/equity ETF (e.g., TUR) for 6–12 months.
- Data needed: IMF IFS reserves, World Bank reserves in months of imports (FI.RES.TOTL.MO, annual from 1960); country CPI; country ETFs (TUR 2008). Not in tool.
- Confidence: high.

### US can inflate its debt away (debt not the issue)
- Source: Rob Citrone — Citrone EP.261 (quote: "we have all our debt in our own currency so we can actually print the money ... we're actually inflating our debt away right now")
- Type: regime map
- Rule as testable logic: IF nominal GDP growth − 10y yield > +3 pts (financial repression) THEN underweight long nominal Treasuries vs TIPS (TIP) and real assets (gold GLD, commodities DBC) for 12 months.
- Data needed: tool has 10y minus nominal GDP growth (reverse sign); TIP (2003), GLD (2004), DBC (2006); longer: gold FRED / LBMA from 1968.
- Confidence: medium.

### Exit fully when conviction lost
- Source: Rob Citrone (citing Robertson and Soros) — Citrone EP.261 (quote: "when they lost conviction and idea they got out they didn't wait around they didn't get half the position out they just got out")
- Type: re-entry/exit
- Rule as testable logic: IF the signal that justified a position flips (e.g., indicator returns to neutral zone) THEN exit 100% at next open (no partial scaling, no limit waiting). Test vs gradual exit.
- Data needed: none (rule design).
- Confidence: high.

### Asymmetric shorts: pegged currency with unsustainable rates
- Source: Rob Citrone — Citrone EP.261 (quote: "if you're long you lose 10 or 15 if you're right you make 75 or 80. and those were the best shorts")
- Type: position sizing/risk
- Rule as testable logic: Only take short positions when estimated downside (loss if wrong) ≤ 1/5 of upside (proposed 5:1 skew), e.g., shorting a pegged currency whose central bank is losing reserves and holds very high rates; size initial short ≤ 3% NAV; let winning shorts run (don't cover after −40%; best shorts fall 90%).
- Data needed: none / reserves data.
- Confidence: high.

### Short-position sizing: max 3% initial, let it shrink
- Source: Rob Citrone (Robertson) — Citrone EP.261 (quote: "let's say you start with a three percent short it has it's only one half percent now so julian would always say well the best shorts go down ninety percent")
- Type: position sizing/risk
- Rule as testable logic: Inverse/short sleeves start at ≤3% NAV each; do not re-size up as they win; cut if thesis (not price) breaks.
- Data needed: none.
- Confidence: high.

### Japan short in the 1990s (bubble country short vs US long)
- Source: Rob Citrone — Citrone EP.261 (quote: "we were short japan along the us and that was a massive macro trade ... the nikkei was over 40 000. it went down to like 9 000")
- Type: action/instrument
- Rule as testable logic: IF a country's equity market cap/GDP or CAPE is in the top 5% of its own and global history (proposed: CAPE > 50) THEN underweight that country vs US/World for 5+ years (pair: short EWJ-like / long SPY).
- Data needed: country CAPE (Research Affiliates / Barclays CAPE, Star Capital; Shiller for US); MSCI country indexes (from 1970). Not in tool.
- Confidence: medium.

### Seasonal: Japanese equities ramped into March fiscal year end
- Source: Rob Citrone — Citrone EP.261 (quote: "they would always ramp the equities into the end of the quarter at their fiscal year end of march ... he would lighten up in the first quarter on the short side")
- Type: signal (seasonal)
- Rule as testable logic: IF holding a Japan underweight/short THEN reduce it during Feb–March and re-establish in April. Test: EWJ excess return in March vs other months.
- Data needed: EWJ (1996), MSCI Japan (1970). Not in tool.
- Confidence: medium.

### EM equities slower than EM FX/debt
- Source: Rob Citrone — Citrone EP.261 (quote: "in emerging markets the equity markets are really the most inefficient markets they tend not to react as quickly as the currency or the debt")
- Type: signal (lead-lag)
- Rule as testable logic: IF a country's currency (vs USD) 3m change < −10% OR its sovereign CDS/EMBI spread 3m change > +150bp (proposed) THEN underweight that country's equity ETF for next 3 months (equity lags FX/credit). Conversely FX/credit rally -> buy equity.
- Data needed: FX rates (FRED H.10 daily from 1971 for major EM: BRL DEXBZUS 1995, KRW DEXKOUS 1981, MXN DEXMXUS 1993, INR DEXINUS 1973, CNY DEXCHUS 1981); EMBI spread (FRED BAMLEMCBPIOAS EM corp OAS from 1998); country ETFs (EWZ 2000, EWY 2000, EWW 1996, INDA 2012). Not in tool.
- Confidence: high.

### Portfolio construction top-down order
- Source: Rob Citrone — Citrone EP.261 (quote: "what do i think direction of equity markets is what i think directing the dollars what's the direction of interest rates from there i begin to populate the positions")
- Type: regime map
- Rule as testable logic: Model structure: three top-level dials — equity direction, dollar direction, rate direction — then pick country/asset positions conditional on those (e.g., dollar falling + rates falling -> EM local bonds and EM equities; dollar rising + rates rising -> short EM FX, short duration).
- Data needed: dollar 12m change (in tool), 10y yield 12m change (in tool), S&P vs 10m avg (in tool).
- Confidence: high.

### Turkey-type currency/credit crisis signal (CDS, reserves, inflation, intervention)
- Source: Rob Citrone — Citrone EP.261 (quote: "turkey cds has gone from about 400 overnight to 800 over we think it's going well over a thousand the country is gonna experience a traditional currency and credit crisis")
- Type: signal (country)
- Rule as testable logic: IF country inflation > 50% AND net reserves negative AND central bank intervening in FX AND CDS doubled in 12 months THEN short that country's ETF/currency (TUR) for 12 months.
- Data needed: CDS (not free; proxy: country USD bond spread or local 10y yield via Investing.com/FRED), IMF reserves, country CPI (World Bank/OECD). TUR (2008). Not in tool.
- Confidence: high.

### China: political-regime risk -> short CNH
- Source: Rob Citrone — Citrone EP.261 (quote: "we think the currency in china is a great short so it's one of our larger positions we're short the cnh")
- Type: action/instrument
- Rule as testable logic: IF China policy turns state-control (no proxy; use: China economic policy uncertainty index above its 80th percentile, proposed) AND US-China rate differential (US 2y − China 2y) > 0 THEN short CNY/CNH (long UUP vs CYB/CNYB) and underweight MCHI vs EM ex-China (EMXC).
- Data needed: China EPU (policyuncertainty.com, 1995); USDCNY (FRED DEXCHUS 1981); China 10y yield (Investing.com, 2002); MCHI (2011), EMXC (2017). Not in tool.
- Confidence: medium.

### China weight in EM index = concentration risk
- Source: Rob Citrone — Citrone EP.261 (quote: "they're the largest component of the em emerging market equity index over 30 so there's tons of foreign money in china and i think this is a big big risk")
- Type: action/instrument
- Rule as testable logic: IF bearish on China (rule above) THEN hold EM via EM ex-China (EMXC) instead of EEM/VWO.
- Data needed: EMXC (2017), EEM (2003); MSCI EM ex China index (back to 2000s).
- Confidence: medium.

### Deglobalization / cold war = lower growth, higher inflation
- Source: Rob Citrone — Citrone EP.261 (quote: "this globalization which was so prosperous ... is now unfortunately going to reverse and i think this is going to be lower growth higher inflation")
- Type: regime map
- Rule as testable logic: IF geopolitical risk index above its 80th percentile (proposed) for 6 months AND trade/GDP falling THEN stagflation tilt: overweight commodities (DBC), gold (GLD), TIPS; underweight long nominal bonds and EM Asia exporters.
- Data needed: GPR index (Caldara-Iacoviello, 1985 daily/1900 monthly); world trade volume (CPB World Trade Monitor, 2000/1991). Not in tool.
- Confidence: medium.

### Regime change in a sanctioned/depressed country = lifetime opportunity
- Source: Rob Citrone — Citrone EP.261 (quote: "if something were to change in russia if there would be a regime change ... there's an opportunity investment of a lifetime in russian assets")
- Type: action/instrument
- Rule as testable logic: IF a country's equity index is down ≥80% from its high in USD AND a political regime change toward market policy occurs THEN buy country ETF (small, 2–5% NAV) and hold 2–3 years. (Also 1998 Russia template.) Not testable for Russia (ETF delisted); test on Argentina (ARGT 2011) 2015/2023 elections, Brazil 2002–03.
- Data needed: MSCI country indexes; election dates. Not in tool.
- Confidence: medium.

### India = long-term structural long
- Source: Rob Citrone — Citrone EP.261 (quote: "we're bullish on india we think india will be the new growth country of the world they've done a lot of reforms")
- Type: action/instrument
- Rule as testable logic: Strategic allocation: hold India (INDA/EPI) as core EM position; underweight only on short-term macro warnings (e.g., oil 6m > +30%, since India imports oil — proposed).
- Data needed: INDA (2012), EPI (2008), MSCI India (1993). Not in tool.
- Confidence: medium (view, not rule).

### Brazil: high real rates + commodity tailwind + inflation peak -> long local bonds, FX, equities
- Source: Rob Citrone — Citrone EP.261 (quote: "you can try in the u.s at three and a half percent rates or you can go to brazil where they're 14 instead of 100 basis points you can make 800 basis points")
- Type: action/instrument
- Rule as testable logic: IF EM policy rate − EM inflation (real rate) > 5% AND EM inflation y/y has peaked (3 months falling) AND commodity index 12m change > 0 THEN overweight Brazil local bonds/BRL carry and EWZ for 12 months.
- Data needed: Brazil Selic and IPCA (BCB SGS API, from 1990s; FRED IRSTCI01BRM156N, BRACPIALLMINMEI); USDBRL (FRED DEXBZUS 1995); EWZ (2000); commodity index (BCOM/DBC; World Bank pink sheet from 1960). Not in tool.
- Confidence: high.

### EM carry: currency "competitive" + 12% net yield
- Source: Rob Citrone — Citrone EP.261 (quote: "the currency is incredibly competitive and you get 12 net yield down the brazilian currency")
- Type: signal
- Rule as testable logic: IF a currency's real effective exchange rate is ≥15% below its 10-year average (proposed) AND carry (local short rate − US short rate) > 6 pts THEN go long that currency (proxy: CEW or BRL via FXB-type; or EM local bond ETF EMLC) for 12 months.
- Data needed: BIS REER (monthly from 1994; FRED RBBRBIS for Brazil); policy rates. Not in tool.
- Confidence: high.

### Election-driven turnaround (Argentina)
- Source: Rob Citrone — Citrone EP.261 (quote: "argentina which is a basket case right now gonna have an election next year we think they get a real significant change to market-oriented policies")
- Type: signal (event)
- Rule as testable logic: IF a distressed EM (sovereign spread > 1500bp, proposed) has an election where a market-oriented candidate leads polls 3 months before THEN buy country ETF (ARGT) 3 months before the vote; hold 12 months after. Event study.
- Data needed: ARGT (2011), MSCI Argentina (1993); EMBI Argentina (JPM; free proxy: bond prices). Not in tool.
- Confidence: medium.

### Africa: avoid; play via Western companies
- Source: Rob Citrone — Citrone EP.261 (quote: "you would think with commodities strong in that there would be some great opportunities there but it's just very difficult")
- Type: conflict/caveat
- Rule as testable logic: Commodity booms do not automatically justify owning frontier/African country ETFs (EZA, AFK); test EZA/AFK excess return vs commodity index changes.
- Data needed: EZA (2003), AFK (2008). Not in tool.
- Confidence: low.

### Short developed sovereign bonds when yields are suppressed and inflation high
- Source: Rob Citrone — Citrone EP.261 (quote: "any developed bond market didn't make any sense in fact they were generally good shorts and we were short most of them")
- Type: signal
- Rule as testable logic: IF 10y yield − core CPI y/y < −2 pts (deeply negative real yield) AND core CPI y/y > 3% THEN short/underweight long developed bonds (TLT, BWX) — hold short duration/TBT; exit when real yield > 0.
- Data needed: real 10y (in tool; TIPS-based), core CPI (in tool); TBT (2008), BWX (2007).
- Confidence: high.

### Japan yield-curve-control break
- Source: Rob Citrone — Citrone EP.261 (quote: "japan where they have the ycc program where they have 10-year rates pegged to 25 basis points ... there's no way that's going to hold in this environment")
- Type: signal
- Rule as testable logic: IF a central bank caps yields (YCC) while global yields and inflation rise (US 10y 12m change > +1pt, Japan core CPI > 2%) THEN short that country's long bonds / short the yen (FXY) until the cap is lifted.
- Data needed: Japan 10y (FRED IRLTLT01JPM156N, 1989); JPY (FRED DEXJPUS 1971); FXY (2007). Not in tool.
- Confidence: medium.

### Tech: avoid price-to-sales stories in tightening
- Source: Rob Citrone — Citrone EP.261 (quote: "anytime a company's still being priced to sales or they're talking about the tam i want nothing to do with that company probably a short")
- Type: signal
- Rule as testable logic: IF Fed tightening (funds 12m change > +1pt) AND QT THEN underweight long-duration growth (ARKK/QQQ) vs value (VTV) for 12 months.
- Data needed: QQQ (1999), VTV (2004), Ken French HML (1926). Not in tool (tool has Fed funds).
- Confidence: medium.

### Mild services-light recession: travel holds up
- Source: Rob Citrone — Citrone EP.261 (quote: "it's not a service recession actually things like trial will do very well usually travel is terrible in a recession")
- Type: conflict/caveat
- Rule as testable logic: Post-shock recessions with pent-up demand: don't apply standard defensive rotation to services/travel (JETS, PEJ). Not generalizable (2022 specific).
- Data needed: JETS (2015), PEJ (2005).
- Confidence: low.

### Europe energy shock: short DAX
- Source: Rob Citrone — Citrone EP.261 (quote: "their natural gas prices are six times what they are in the united states ... the dax we think is the best way to play the situation in europe")
- Type: action/instrument
- Rule as testable logic: IF European natural gas price / US Henry Hub > 3x (proposed) AND rising THEN underweight Germany equities (EWG) vs US (SPY) for 6–12 months.
- Data needed: TTF (World Bank pink sheet Europe natural gas monthly from 1960s / 1985); Henry Hub (FRED MHHNGSP 1997); EWG (1996). Not in tool.
- Confidence: medium.

### Italian spread blowout risk
- Source: Rob Citrone — Citrone EP.261 (quote: "there's gonna be a fantastic short in italian debt ... you could have a real blow out and spreads there and something could crack in europe")
- Type: signal
- Rule as testable logic: IF ECB hiking (ECB depo 6m change > 0) AND Italy-Germany 10y spread 3m change > +75bp (proposed) THEN underweight eurozone equities (EZU) and banks; long Bund vs BTP not retail-available — use EZU underweight / UUP.
- Data needed: Italy/Germany 10y (FRED IRLTLT01ITM156N, IRLTLT01DEM156N, monthly from 1991/1957); ECB rate (FRED ECBDFR 1999). Not in tool.
- Confidence: medium.

### Net exposure range and volatility budget
- Source: Rob Citrone — Citrone EP.261 (quote: "we'll get to 20 25 net short if we really get incredibly concerned ... equities of all is the highest and then credit is about half of that and the currency is about a third")
- Type: position sizing/risk
- Rule as testable logic: Maximum bearish stance: equity net −20–25% (i.e., inverse up to 25% of NAV, e.g., SH); size credit and currency positions at 2x and 3x the equity notional for equal risk (vol parity: credit vol ≈ ½ equity, FX vol ≈ ⅓).
- Data needed: realized vol of SPY, HYG/LQD, UUP.
- Confidence: high.

### Max position size 10–15% too big (liquidity, regulatory bets)
- Source: Rob Citrone — Citrone EP.261 (quote: "how big was too big in terms of position size between 10 and 15")
- Type: position sizing/risk
- Rule as testable logic: Cap any single non-core position (country, commodity, sector) at < 10% NAV; event/regulatory bets at ≤ 5% (proposed).
- Data needed: none.
- Confidence: high.

### Bear market bottom: lower levels, 6–7 months out (2022)
- Source: Rob Citrone — Citrone EP.261 (quote: "it's possible the markets may bottom the next six or seven months but probably much lower levels than here")
- Type: conflict/caveat
- Rule as testable logic: Not general. Note: his 2022 call (inflation peaked, QT bearish) — markets bottomed Oct 2022, ~3–4 months later.
- Data needed: none.
- Confidence: low.

### Cross-reference / avoid groupthink; replace good ideas with better
- Source: Rob Citrone — Citrone EP.261 (quote: "we have good ideas but we want to replace the good ideas and better ideas")
- Type: position sizing/risk
- Rule as testable logic: Rank-based allocation: hold top-N signals only; replace a holding when a new candidate's score exceeds the weakest held score by a margin (proposed 10%).
- Data needed: none.
- Confidence: medium.

---

## File 3 — Scott Bessent on Real Vision (recorded ~late April/May 2024; uploaded Nov 2024), "Trump's NEW Treasury Secretary on Macro Strategy"

### Asymmetry first: only trade when payoff ≥ 5–10x risk
- Source: Scott Bessent — Trump's NEW Treasury Secretary on Macro Strategy (quote: "it was a five-year fund you could lose 25% and that if the housing market cracked which it did then you could make 250 350%")
- Type: position sizing/risk
- Rule as testable logic: Prefer instruments with capped downside and large upside (long options/puts, CDS-like) when the thesis is a regime break; require modeled payoff/loss ≥ 5:1 (proposed) before taking a tail position; budget negative carry ≤ 5% NAV/yr (from Paulson example).
- Data needed: option prices (CBOE; free proxy: VIX/SKEW, Cboe PUT index from 1986).
- Confidence: high.

### Fixed-band / peg regimes break when defending them hurts the economy
- Source: Scott Bessent — Bessent Real Vision (quote: "as the bank of England can raise R to stabilize the currency they were actually destroying the British housing market")
- Type: signal
- Rule as testable logic: IF a central bank is defending a currency level (peg/band/YCC) AND the defense (rate hikes) hits the most rate-sensitive sector (floating-rate mortgages share high) THEN bet on the peg breaking (short the defended currency or the capped bond) with options; hold until cap/peg is abandoned.
- Data needed: event list of pegs/caps; floating-rate mortgage share (BIS/ECB). Not in tool.
- Confidence: high.

### Check positioning/option skew last; skip if crowded
- Source: Scott Bessent — Bessent Real Vision (quote: "it may show you know in opt option skew that the you know it's already priced in and we're very happy to put our work up on the shelf")
- Type: conflict/caveat
- Rule as testable logic: IF a macro signal fires BUT positioning is already extreme in the same direction (CFTC net speculative position in top/bottom decile of 3-year range, proposed) THEN skip or halve the trade.
- Data needed: CFTC Commitments of Traders (weekly from 1986; free, cftc.gov) for S&P, Treasuries, currencies, gold, oil. Not in tool.
- Confidence: high.

### Fade event panics when the market prices an outcome too cheaply (Brexit, Trump 2016, Macron 2017)
- Source: Scott Bessent — Bessent Real Vision (quote: "the market was paying me to take the risk then even on the night when he won the the Euro only went from 105 to 107")
- Type: re-entry/exit
- Rule as testable logic: IF a political event causes a sharp drop (S&P −5% in ≤ 3 days, or option implied vol for the event in top 5% of history) AND polling/fundamentals point to a benign outcome THEN buy the dip (SPY/country ETF/currency) or buy cheap out-of-the-money calls; hold 1–3 months.
- Data needed: S&P daily (Yahoo ^GSPC 1950); VIX (in tool); currency vol (CVIX not free; proxy: FXE realized vol). Event dates.
- Confidence: medium.

### Gold rising despite rising real rates = accumulation signal
- Source: Scott Bessent — Bessent Real Vision (quote: "real rates started going up in the US nominal rates started going up which is normally ... a signal that you're going to get a 5 10 could be 15% pullback instead gold went up 15%")
- Type: signal
- Rule as testable logic: IF real 10y yield 6m change > +0.25 pt AND gold 6m return > +10% (decoupling) THEN overweight gold (GLD/IAU) 10% (proposed) for 12 months (central bank accumulation regime). Normal regime: IF real yield rising and gold not rising -> expect 5–15% pullback, underweight.
- Data needed: real 10y (in tool, FRED DFII10 from 2003); gold (FRED GOLDAMGBD228NLBM discontinued 2022 → LBMA / Yahoo GC=F, GLD 2004); central-bank gold purchases (World Gold Council quarterly from 2000). Gold not in tool.
- Confidence: high.

### Central bank + retail gold buying (vox populi)
- Source: Scott Bessent — Bessent Real Vision (quote: "you've got the second biggest Central Bank in the world pboc buying and you've got Mom Moms and Pops going into Costco and buying")
- Type: signal
- Rule as testable logic: IF official sector net gold purchases (4-quarter sum) > 800 tonnes (proposed; ~2x pre-2022 average) THEN keep a strategic gold allocation (≥5%).
- Data needed: World Gold Council central-bank demand (quarterly from 2010; annual from 1950); gold ETF holdings. Not in tool.
- Confidence: medium.

### Fiscal dominance endgame: release valve is the dollar (then rates)
- Source: Scott Bessent — Bessent Real Vision (quote: "we have to figure out what the release valve will be my my guess is that it's going to eventually be the dollar it could initially be rates")
- Type: regime map
- Rule as testable logic: IF federal deficit > 6% GDP with unemployment < 5% (no recession) AND interest outlays/GDP rising AND gold/USD 12m change > +15% THEN underweight long Treasuries (TLT) and the dollar; overweight gold, non-US equities (VEU/EFA), and commodities.
- Data needed: deficit (FRED FYFSGDA188S, MTSDS133FMS); interest outlays (FRED A091RC1Q027SBEA, quarterly from 1947); gold; dollar (in tool). Partly in tool.
- Confidence: medium.

### Deficit at 7% with no recession/war is a red flag
- Source: Scott Bessent — Bessent Real Vision (quote: "we are running a 7% budget deficit with the no financial crisis no recession and no war this has never happened before")
- Type: signal
- Rule as testable logic: IF deficit/GDP − (cyclical norm: proposed 2× unemployment gap) > 4 pts THEN tilt fixed income to short maturities (SHY/BIL) and TIPS vs long nominals (TLT).
- Data needed: deficit/GDP; CBO cyclically adjusted deficit (annual). Not in tool.
- Confidence: medium.

### Interest cost > defense spending
- Source: Scott Bessent — Bessent Real Vision (quote: "this year just just see interest on the US debt will be $1.1 trillion to to put that into perspective the defense budget is about 900 billion")
- Type: signal
- Rule as testable logic: IF federal net interest outlays / GDP > 3% (proposed) or > defense spending THEN fiscal-stress regime: underweight TLT; overweight gold.
- Data needed: FRED A091RC1Q027SBEA (interest payments) and FDEFX (defense, quarterly from 1947). Not in tool.
- Confidence: medium.

### Treasury shortening maturity (more bills) = stealth easing
- Source: Scott Bessent — Bessent Real Vision (quote: "Yellen through the quarterly refunding announcement announced that there's going to be fewer coupon bonds issued and more bills issued which you know again Goose The Market")
- Type: signal
- Rule as testable logic: IF bills' share of marketable Treasury debt rises > 2 pts in 12 months (proposed) THEN treat as liquidity easing: overweight equities/high yield for 6 months; but long-run negative for dollar/fiscal credibility.
- Data needed: Treasury Monthly Statement of the Public Debt (bills outstanding vs total marketable, from 1950s; FRED via MSPD; TreasuryDirect). Not in tool (relates to "Fed net liquidity" which uses TGA).
- Confidence: medium.

### Fed pivot talk loosens financial conditions -> stocks +25%, spreads tighter, re-acceleration
- Source: Scott Bessent — Bessent Real Vision (quote: "you ended up with this massive easing of financial conditions that it sent the stock market up 25% the tightened high yield spreads")
- Type: signal
- Rule as testable logic: IF financial conditions index eases by > 1 std dev over 6 months (proposed) while core inflation > 3% THEN expect inflation re-acceleration within 6–12 months: reduce long duration (TLT) and hold equities.
- Data needed: Chicago Fed NFCI (FRED NFCI weekly from 1971); core CPI (in tool). NFCI not in tool.
- Confidence: medium.

### Fed was late: QE until month before first hike
- Source: Scott Bessent — Bessent Real Vision (quote: "they were doing QE right up until the month before the First Rate hike")
- Type: conflict/caveat
- Rule as testable logic: IF Fed balance sheet still growing while core CPI y/y > 4% THEN behind-the-curve regime: underweight long bonds (TLT) — expect aggressive catch-up hikes.
- Data needed: WALCL; core CPI. Partly in tool.
- Confidence: medium.

### Abenomics trade: short yen + long Japanese equities, keep it simple
- Source: Scott Bessent — Bessent Real Vision (quote: "we're going have a gigantic short position the Y and stocks are probably going to go up too and I don't really need to mess around in the jgb market")
- Type: action/instrument
- Rule as testable logic: IF Japan announces reflation regime (BoJ QE expansion; proposed signal: BoJ balance sheet 6m change > +10%) THEN short JPY (long USD/JPY via YCS or short FXY) and long Japanese equities (DXJ hedged / EWJ) for 2+ years.
- Data needed: BoJ total assets (FRED JPNASSETS, monthly from 1998); USDJPY (DEXJPUS 1971); EWJ (1996), DXJ (2006). Not in tool.
- Confidence: medium.

### Japan equity re-rating via corporate governance (lag 8–10 years)
- Source: Scott Bessent — Bessent Real Vision (quote: "Japan's replating there was a 10year lag in or eight nyear lag in corporate governance and the Nik is going to go to new High")
- Type: action/instrument
- Rule as testable logic: Structural overweight Japan equities (EWJ/DXJ) when Japan ROE trend rising (TOPIX ROE 3y change > +2 pts, proposed) and buybacks rising.
- Data needed: TOPIX ROE (JPX; not easy free); MSCI Japan (1970). Not in tool.
- Confidence: low.

### Currency valuation doesn't matter for timing
- Source: Scott Bessent — Bessent Real Vision (quote: "I would say it it's 40% undervalued but as you know in currencies valuation never matters")
- Type: conflict/caveat
- Rule as testable logic: Do not use REER/PPP undervaluation alone as an entry signal for currencies; require momentum or policy catalyst. (Contrasts with Citrone's "currency incredibly competitive" Brazil case — test REER-only vs REER+momentum.)
- Data needed: BIS REER; currency momentum.
- Confidence: high.

### Yen: BoJ hikes are stimulative in Japan (savers)
- Source: Scott Bessent — Bessent Real Vision (quote: "interest rate hikes are actually stimulative to Japan so huge amount of personal savings large corporate savings")
- Type: regime map
- Rule as testable logic: IF BoJ starts a hiking cycle THEN long JPY (FXY) and stay long Japanese domestic equities; don't read hikes as bearish for Japan growth.
- Data needed: BoJ policy rate (FRED IRSTCB01JPM156N); FXY.
- Confidence: medium.

### Currency moves track political popularity; intervention near 160
- Source: Scott Bessent — Bessent Real Vision (quote: "they intervened two nights ago uh in in the currency when it went through 160")
- Type: signal
- Rule as testable logic: IF USDJPY > 155 (proposed; 2022 intervention 145–152, 2024 at 160) THEN expect Japanese MoF intervention: reduce short-yen positions / buy short-dated yen calls.
- Data needed: USDJPY daily; MoF intervention record (mof.go.jp, from 1991). Not in tool.
- Confidence: medium.

### Fiscal dominance definition (US flirting)
- Source: Scott Bessent — Bessent Real Vision (quote: "fiscal dominance is just the government is unable to raise rates because the size of the debt is so large which it which we're which we're flirting with here in the US")
- Type: regime map
- Rule as testable logic: IF federal debt/GDP > 100% AND Fed cuts while core inflation > 3% (proposed) THEN fiscal-dominance regime: overweight gold, TIPS, commodities; underweight long nominal Treasuries and USD.
- Data needed: FRED GFDEGDQ188S (debt/GDP, from 1966); fed funds; core CPI. Debt/GDP not in tool.
- Confidence: medium.

### Reliance on foreign financing (kindness of strangers)
- Source: Scott Bessent — Bessent Real Vision (quote: "it's being funded from overseas so we've got to rely on the kindness of strangers uh the Japanese could always bring a lot of money home")
- Type: signal
- Rule as testable logic: IF foreign official holdings of Treasuries 12m change < 0 AND Japan 10y yield 12m change > +0.5pt (repatriation incentive) THEN underweight long Treasuries (TLT) for 6 months.
- Data needed: TIC data (Treasury, monthly from 1970s; FRED FDHBFIN foreign holdings, quarterly); Japan 10y (FRED IRLTLT01JPM156N). Not in tool.
- Confidence: medium.

### China: FDI collapse + asset-freeze tail risk -> avoid long-term China exposure
- Source: Scott Bessent — Bessent Real Vision (quote: "is there a 5 10 20% chance that if if you have R&B that your assets will be frozen or that you have the equivalent in Chinese equities of a day like you had in Russian equities")
- Type: conflict/caveat
- Rule as testable logic: IF China inward FDI (BoP direct investment liabilities, 4Q sum) turns negative (proposed) THEN underweight China (MCHI/FXI/KWEB) in EM allocation; trade bounces only short term (≤ 3 months).
- Data needed: SAFE China BoP FDI (quarterly from 1998); MCHI/FXI. Not in tool.
- Confidence: medium.

### China exporting deflation hurts Korea and Germany
- Source: Scott Bessent — Bessent Real Vision (quote: "what's the business model for Korea at that point if there's a big overlap with a a giant manufacturer that's exporting deflation what's the business model for Germany")
- Type: signal (country)
- Rule as testable logic: IF China export price index y/y < 0 (proposed) AND China export volumes rising THEN underweight Korea (EWY) and Germany (EWG) vs US for 12 months.
- Data needed: China export prices (China customs / Bloomberg; proxy: US import prices from China, FRED CHNTOT? — BLS import price index from China, series EIUIRCHN? (BLS COCHNTOT from 2003)); EWY (2000), EWG (1996). Not in tool.
- Confidence: medium.

### China gauges: trade balances, PBoC, yield curve, fund flows
- Source: Scott Bessent — Bessent Real Vision (quote: "we're looking at internal stress external indicators and then fund flows")
- Type: signal
- Rule as testable logic: IF China 10y government yield 12m change < −0.5 pt (deflation priced) AND CNY weakening THEN underweight China equities and commodities linked to China (copper — tool has copper 6m change).
- Data needed: China 10y yield (Investing.com from 2002; ChinaBond); USDCNY. Not in tool.
- Confidence: low.

### Bifurcated economy: rising card delinquencies at the bottom
- Source: Scott Bessent — Bessent Real Vision (quote: "credit card delinquencies are the highest that they've been since they've been started measuring them in 2012")
- Type: signal
- Rule as testable logic: Already in tool (card delinquencies). Add: IF card delinquencies at multi-year high BUT equities rising on top-20% consumption THEN overweight luxury/high-income consumer vs discount/low-income (proxy: XLY vs XRT); low confidence.
- Data needed: Philly Fed large-bank card data (from 2012); NY Fed CCP (from 2003); FRED DRCCLACBS (from 1991). In tool.
- Confidence: low.

### Populism risk to buybacks (2028)
- Source: Scott Bessent — Bessent Real Vision (quote: "I could imagine in 2028 that the candidates are AOC and JD Vents and they are you know to to your notion on this left right agreeing you they are both quite populist")
- Type: conflict/caveat
- Rule as testable logic: Not testable as rule; note political tail risk to equity valuations (CAPE) after a populist election.
- Data needed: none.
- Confidence: low.

### Big trend covers mistakes (trend-following bias)
- Source: Scott Bessent — Bessent Real Vision (quote: "if you're in a big Trend the the big Trend covers up a lot of the mistakes")
- Type: position sizing/risk
- Rule as testable logic: Size up only when the instrument is in a long-term uptrend (price > 10-month average, as in tool) — apply the same trend filter to every new instrument (country ETFs, commodities, gold).
- Data needed: monthly prices for each instrument.
- Confidence: medium.

### Gold vs S&P since 1967 (price only) equal
- Source: Scott Bessent — Bessent Real Vision (quote: "if you take out dividends the price appreciation of gold in the S&P since 1967 are are the same")
- Type: conflict/caveat
- Rule as testable logic: Benchmark check: gold as a long-run diversifier — test gold/SPX price ratio regimes (gold outperforms when real yields fall and deficits widen).
- Data needed: gold monthly from 1968 (LBMA; FRED discontinued; Yahoo GC=F from 2000; World Bank pink sheet from 1960); S&P (Shiller).
- Confidence: medium.

---

## File 4 — The Real Eisman Playbook Ep 73: The AI Trade, Rising Rates (Steve Eisman with Jason Trennert and Chris Verrone, Strategas; Aug 2026)

### Breadth improving while leaders correct = healthy rotation (stay long)
- Source: Chris Verrone — The AI Trade, Rising Rates, Eisman Ep 73 (quote: "You only had about 50% of the S&P above the 200-day average on June 2nd. Today, we sit here today with 75% of the S&P above")
- Type: signal
- Rule as testable logic: IF % of S&P 500 members above 200-day average rises ≥ 15 pts over 2 months while the index is flat/down AND leading group (semis SMH) falls ≥ 20% THEN stay long equities (rotation, not top); prefer equal-weight (RSP) over cap-weight for 6 months.
- Data needed: % of S&P above 200dma (free: compute from constituents; StockCharts $SPXA200R not free history; proxy: tool's "industries in uptrend (breadth)"); RSP (2003). Partly in tool.
- Confidence: medium.

### Equity-competitive rate level: 10y 4.5% then higher
- Source: Chris Verrone / Jason Trennert — Eisman Ep 73 (quote: "until we find what level of interest rate is truly competitive to equities, you're going to stay in this highly rotational tape")
- Type: signal
- Rule as testable logic: IF 10y Treasury yield > 4.5% (their old threshold) — or more generally 10y yield − S&P forward earnings yield > 0 (equity risk premium ≤ 0, proposed) — THEN expect corrective periods; reduce equities 25% (proposed). Note: they say the true cycle-ending level is higher (nominal GDP 6.5%), so pair with 10y − nominal GDP growth (in tool).
- Data needed: 10y (FRED DGS10); S&P earnings yield (Shiller/multpl, monthly from 1871; forward EPS not free); 10y minus nominal GDP (in tool).
- Confidence: medium.

### Most dangerous: stocks melt up while long yields jump (1987, 1989 Japan, 1999)
- Source: Jason Trennert — Eisman Ep 73 (quote: "the worst sign when when stocks are going straight up, and they don't care at the same time long-term interest rates are going up")
- Type: signal
- Rule as testable logic: IF S&P 500 12m return > +25% AND 10y yield 12m change > +1.5 pts (examples: 1987 6→9%, 1999 4→7%, Japan 1989 JGB 4→8%) THEN cut equities to 50% (proposed) for 12 months / buy puts.
- Data needed: S&P (Shiller); 10y (FRED GS10 from 1953); Japan 10y and Nikkei (FRED IRLTLT01JPM156N 1989; Nikkei via Yahoo ^N225 1965). Tool has 10y 12m change and rally speed — combine (new interaction).
- Confidence: high.

### Fed tightening because of growth (real rates) vs because of inflation
- Source: Chris Verrone / Jason Trennert — Eisman Ep 73 (quote: "The backup in interest rates has largely been in real rates. It hasn't been in inflation")
- Type: regime map
- Rule as testable logic: IF 10y yield rising mainly via real yield (real 10y 6m change > breakeven 6m change) THEN growth-driven rise: stay overweight cyclicals/banks/equities; IF rise mainly via breakevens THEN inflation-driven: underweight equities and long bonds, overweight commodities/TIPS.
- Data needed: FRED DFII10 (2003), T10YIE (2003); before 2003 use 10y minus trailing core CPI. Real 10y in tool; breakeven decomposition new.
- Confidence: high.

### Earnings-driven market (P/E falling, E rising) favors active/cyclicals
- Source: Chris Verrone — Eisman Ep 73 (quote: "it's been about the E, not the P/E. All right, J so the PE is down maybe two or three turns")
- Type: regime map
- Rule as testable logic: IF S&P P/E 12m change < −2 turns AND S&P EPS 12m growth > 10% THEN favor cyclicals/value and equal weight (RSP) over cap-weight; asset managers/brokers lead.
- Data needed: Shiller P/E and EPS (monthly from 1871); RSP. Not directly in tool.
- Confidence: medium.

### Oil matters more where there is no AI capex (Europe) than in US
- Source: Chris Verrone — Eisman Ep 73 (quote: "There's a lot more reflexivity to higher oil prices in Europe where they don't have this AI capex story underway")
- Type: signal (country)
- Rule as testable logic: IF oil 6m change > +30% (in tool) THEN underweight Europe (VGK/EZU) vs US (SPY) for 6 months; Japan also energy-sensitive but acted better (caveat).
- Data needed: oil 6m (in tool); VGK (2005), EZU (2000), MSCI Europe (1970).
- Confidence: medium.

### Base metals up while iron ore falls = AI/capex demand, not China
- Source: Chris Verrone — Eisman Ep 73 (quote: "copper new high, zinc new high, tin new high, Chinese iron ore is collapsing ... It's AI and CapEx")
- Type: signal
- Rule as testable logic: IF copper 6m change > +10% AND iron ore 6m change < −10% THEN read as non-China (US capex) demand: overweight US industrials/AI build-out (XLI, GRID) and copper miners (COPX); underweight China equities and Australia (EWA)/Brazil (EWZ, iron-ore heavy).
- Data needed: copper (in tool); iron ore (World Bank pink sheet monthly from 1960; FRED PIORECRUSDM from 1980); COPX (2010), EWA (1996). Iron ore not in tool.
- Confidence: medium.

### Oil oversupply: China stopped buying, pipelines bypass the Strait
- Source: Steve Eisman (citing a guest) — Eisman Ep 73 (quote: "China has completely withdrawn from purchasing oil and so that demand is much much lower than people think")
- Type: conflict/caveat
- Rule as testable logic: Geopolitical oil spikes fade fast when demand is weak: IF Brent spikes > 15% on war news while China crude imports 3m y/y < 0 THEN fade spike (no oil hedge / underweight XLE) after 2 weeks. Verrone: crude rally "pretty tepid".
- Data needed: China crude imports (GACC monthly; free proxy: EIA/JODI from 2002); Brent. Not in tool.
- Confidence: low.

### Hyperscaler capex financed by debt/equity issuance = late-cycle risk
- Source: Jason Trennert — Eisman Ep 73 (quote: "it's going to be hard to continue to grow AI investments without further dilution of shareholders")
- Type: signal
- Rule as testable logic: IF large-cap tech net equity + bond issuance turns positive (net issuance > buybacks) AND hyperscaler free cash flow 12m falls > 25% THEN reduce tech overweight (QQQ/XLK) to market weight; prefer semis (SMH) over hyperscalers (they spend).
- Data needed: corporate issuance (SIFMA, monthly from 1996); FCF of top 5 (company filings). Not in tool (narrow leadership is).
- Confidence: medium.

### AI ecosystem concentration: OpenAI + Anthropic as single point of failure
- Source: Steve Eisman — Eisman Ep 73 (quote: "if Open AI and Anthropic ever get in trouble, the ecosystem is in trouble")
- Type: conflict/caveat
- Rule as testable logic: Not directly testable; monitor: IF AI-lab funding round fails/down round or credit spreads of AI-related issuers (Oracle CDS) widen > 100bp in 3 months THEN cut semis/tech overweight.
- Data needed: Oracle CDS (not free); proxy: ORCL bond ETF spreads / IG tech spreads. Not in tool.
- Confidence: low.

### Market concentration (top 10 = 39%) = nervousness
- Source: Jason Trennert — Eisman Ep 73 (quote: "if you look at the top 10 holdings of the S&P 500, I think that's 39%")
- Type: signal
- Rule as testable logic: Already in tool (narrow leadership). Add threshold: IF top-10 weight > 35% (proposed) THEN hold part of equity sleeve in equal-weight RSP.
- Data needed: S&P top 10 weight (S&P DJI; proxy RSP/SPY ratio 2003). In tool (narrow leadership).
- Confidence: medium.

### Leveraged long/short of the same theme blows up on small moves
- Source: Steve Eisman — Eisman Ep 73 (quote: "you're long X and you're short Y, but it's the same thing ... if the trade reverses on you and you're four times levered")
- Type: position sizing/risk
- Rule as testable logic: Avoid pair trades where long and short legs share the same factor (correlation of leg returns > 0.7 in reverse); cap gross leverage at 2x (proposed).
- Data needed: none.
- Confidence: medium.

### Respect price reversals: give leaders benefit of the doubt until a failed rally
- Source: Chris Verrone — Eisman Ep 73 (quote: "you kind of have to give these the benefit of the doubt on until they you know, attempt to rally, don't make new highs, and fail")
- Type: re-entry/exit
- Rule as testable logic: Exit a leading sector only after (a) ≥ 20% drawdown, (b) rebound that fails to make a new high, (c) close below the drawdown low (lower low). Otherwise hold. Test on sector ETFs vs simple 10m MA rule.
- Data needed: sector ETFs (SPDRs from 1998; Ken French 49 industries from 1926).
- Confidence: medium.

### New Fed regime (Warsh): less forward guidance = more volatility, alpha market
- Source: Jason Trennert — Eisman Ep 73 (quote: "the reaction function when you're at full employment is inflation")
- Type: regime map
- Rule as testable logic: IF unemployment ≤ NAIRU (FRED NROU) THEN Fed reacts to inflation: core inflation 3m annualized > 3% -> expect hikes (underweight TLT, long-duration growth). Expect higher VIX baseline; reduce leverage.
- Data needed: FRED UNRATE, NROU (1949); core inflation (in tool).
- Confidence: medium.

### Banks at new highs worldwide + benign credit = no systemic stress
- Source: Chris Verrone — Eisman Ep 73 (quote: "public credit remains very benign. Double B spreads I think made new cycle lows last week")
- Type: signal
- Rule as testable logic: IF bank stocks vs market at 12m high (in tool) AND BB OAS at 12m low THEN no systemic credit problem: stay long equities; overweight banks (KBE, EUFN for Europe, Japanese banks via DXJ financials/proxy) and brokers (IAI). Contrast: Verrone also says it "seems a little out of step" — caveat.
- Data needed: FRED BAMLH0A1HYBB (BB OAS, 1996); bank vs market (in tool); EUFN (2010). BB OAS new.
- Confidence: medium.

### Deregulation needed before Fed can shrink balance sheet
- Source: Chris Verrone (citing Dan Clifton) — Eisman Ep 73 (quote: "you can't really shrink the balance sheet of the Fed until you deregulate the the banks")
- Type: regime map
- Rule as testable logic: IF bank capital rules loosened (eSLR change event) THEN overweight banks (KBE/XLF) 12 months; curve steepeners (short TLT vs SHY) as balance sheet shrinks.
- Data needed: event dates; WALCL. 
- Confidence: low.

### Curve steepening + strong economy = banks
- Source: Jason Trennert — Eisman Ep 73 (quote: "I think the curve is going to steepen ... the economy is strong, so I think ... the credit losses should be pretty minimal")
- Type: signal
- Rule as testable logic: IF 10y−2y 6m change > +0.5 pt (bear steepening) AND unemployment not rising (Sahm < 0.3) THEN overweight banks (KBE/KRE) vs SPY for 6 months.
- Data needed: yield curve (in tool); Sahm (in tool); KBE (2005), Ken French banks industry (1926).
- Confidence: medium.

### Europe cheap for a reason; prefer Japan (ROE reform, reflation)
- Source: Jason Trennert — Eisman Ep 73 (quote: "they're cheap for a reason. They're cheap The reason why it's cheap is that they're not dynamic economies"; "I like Japan a lot better")
- Type: action/instrument
- Rule as testable logic: Country allocation: valuation alone (low CAPE) is not a buy signal for Europe; prefer Japan (EWJ/DXJ) when Japan core CPI y/y > 1.5% (out of deflation) AND TSE governance reform in force (event 2023). Test: low-CAPE country rotation with and without earnings momentum.
- Data needed: country CAPE; Japan CPI (FRED JPNCPIALLMINMEI); EWJ, VGK.
- Confidence: medium.

### Higher JGB yields = reflation, fine for Japanese stocks until Japanese banks/insurers weaken
- Source: Chris Verrone — Eisman Ep 73 (quote: "Until the Japanese insurance stocks or until the Japanese bank stocks start to really weaken here, I'm not concerned about higher JGB yields")
- Type: signal
- Rule as testable logic: IF Japan 10y yield rising AND Japanese bank index relative to TOPIX at/near 12m high THEN stay long Japan equities; IF JGB yields rising AND Japanese banks fall > 15% from high THEN exit Japan.
- Data needed: Japan 10y (FRED); TOPIX banks index (JPX; proxy: Yahoo 1306.T TOPIX ETF, 8306.T MUFG). Not in tool.
- Confidence: medium.

### Japan 10y crossing German 10y (sign of reflation divergence)
- Source: Jason Trennert — Eisman Ep 73 (quote: "Japanese 10-year yields are about to cross German 10-year yields for the first time in decades")
- Type: signal
- Rule as testable logic: Monitoring: IF Japan 10y − Germany 10y > 0 THEN Japan reflation regime: overweight Japan vs Europe (EWJ vs VGK) 12 months (proposed).
- Data needed: FRED IRLTLT01JPM156N, IRLTLT01DEM156N (monthly). Not in tool.
- Confidence: low.

### Europe new highs driven by AI build-out + banks; China-demand groups (autos, luxury) in bear markets
- Source: Chris Verrone — Eisman Ep 73 (quote: "if you look at parts of the economy that rely on Chinese demand, autos and luxury, um you're in prolific bear markets")
- Type: signal
- Rule as testable logic: IF China demand weak (China PMI < 50 for 6 months, or iron ore falling) THEN underweight China-exposed sectors/countries (Europe luxury/autos proxy: Germany EWG; Australia EWA; China MCHI); favor AI build-out (electrical equipment/utilities) instead.
- Data needed: China NBS/Caixin PMI (from 2005; free proxy: OECD CLI China FRED CHNLOLITONOSTSAM from 1993). Not in tool.
- Confidence: medium.

### Defensives ranking: healthcare > staples; regulated utilities weak when politics hits power prices
- Source: Chris Verrone — Eisman Ep 73 (quote: "if I'm going to rate kind of defensives, health care comes at the top of that pile. Staples probably still near the bottom")
- Type: action/instrument
- Rule as testable logic: When de-risking within equities, choose the defensive sector with best 6m relative momentum (XLV, XLP, XLU) rather than a fixed defensive basket. Test vs fixed staples/utilities.
- Data needed: sector SPDRs (1998), Ken French 12 industries (1926). Tool has staples vs discretionary.
- Confidence: medium.

### Populism against "big anything" (pharma, banks, oil) — policy risk
- Source: Jason Trennert — Eisman Ep 73 (quote: "there is a reaction against big anything. Big big media, big academia, big pharma, big banks")
- Type: conflict/caveat
- Rule as testable logic: Not testable as rule; note sector policy risk (XLV pricing, XLE windfall).
- Data needed: none.
- Confidence: low.

### 10y yield range narrow (85bp in 400 days) — not yet disruptive
- Source: Chris Verrone — Eisman Ep 73 (quote: "The range of the 10 years 85 basis points over the last 400 days ... I just don't think this this this move in yield is as explosive yet")
- Type: signal
- Rule as testable logic: Rate shock for equities only when 10y yield 12m range > 150bp (proposed) or 10y 12m change > +1 pt (tool has 10y 12m change; test threshold).
- Data needed: 10y daily (FRED DGS10, 1962). In tool.
- Confidence: medium.

### Private equity/credit illiquidity: endowment stress
- Source: Jason Trennert — Eisman Ep 73 (quote: "the monetization time frame is now like 7 years ... So, now they're sleeping, but they ain't getting their money back")
- Type: conflict/caveat
- Rule as testable logic: IF listed alternative managers (PSP listed private equity ETF) underperform traditional managers for 6 months THEN private-market stress: avoid BDCs (BIZD) and leveraged loans (BKLN); hold IG credit instead.
- Data needed: PSP (2006), BIZD (2013), BKLN (2011). Not in tool.
- Confidence: low.

---

## File 5 — Peter Oppenheimer, Goldman Sachs (Money Maze Podcast, Oct 2022)

### Bear market taxonomy: structural / cyclical / event-driven
- Source: Peter Oppenheimer — Goldman Sachs's Chief Global Equity Strategist, Peter Oppenheimer (quote: "you can distinguish between three types of downturn uh those that we call structural um those that are cyclical and those that are event driven")
- Type: regime map
- Rule as testable logic: Classify each drawdown at onset:
  - Structural (≈ −60%, long recovery): IF prior bubble in equities AND real estate (CAPE top decile AND real house price 5y growth > 30%) AND private-sector credit/GDP gap > 10 pts (BIS) AND bank stress (bank stocks vs market 6m < −20%) THEN hold equities ≤ 25% and long Treasuries for 2+ years.
  - Cyclical (≈ −30%, ~2 years, with bear rallies): IF Fed hiking into late cycle (funds 12m change > +1.5 pts) with inflation high, but healthy private balance sheets THEN reduce equities to 50–60%, re-enter on peak-rates/peak-inflation signals (see re-entry rule).
  - Event-driven (≈ −30%, fast recovery): IF exogenous shock (war, pandemic, commodity shock) with no prior imbalances (credit gap < 5 pts, Fed not tightening) THEN buy after −20% (proposed) and hold 12 months.
- Data needed: CAPE (in tool); real house prices (FRED QUSR628BIS / Case-Shiller CSUSHPINSA from 1987; Shiller from 1890); BIS credit-to-GDP gap (BIS, quarterly from 1960s, US); bank vs market (in tool); Fed funds (in tool). Credit gap and house prices not in tool.
- Confidence: high.

### Typical recession bear market depth ≈ 30%
- Source: Peter Oppenheimer — Oppenheimer (quote: "typically in a bear market around a recession you would see equities falling about 30 percent")
- Type: re-entry/exit
- Rule as testable logic: IF recession signal active (Sahm in tool) AND S&P drawdown < 25% THEN expect further downside: don't re-enter on drawdown alone; IF drawdown ≥ 30% THEN begin scaling in (one third per −5%, proposed).
- Data needed: S&P; Sahm (in tool).
- Confidence: high.

### Bear-market bottom checklist: valuation low, growth deterioration slowing, peak rates, peak inflation
- Source: Peter Oppenheimer — Oppenheimer (quote: "it's usually when interest rates Peak and inflation Peaks that equities start to recover")
- Type: re-entry/exit
- Rule as testable logic: Re-enter equities (from cash/bonds) when ≥ 3 of 4 hold: (1) S&P forward P/E or CAPE ≤ its 20y median; (2) second derivative of growth turns up — ISM/PMI 3m change > 0 while still < 50 (or OECD CLI 3m change > 0); (3) 2y Treasury yield ≥ 0.5pt below its 6m high (rates peaked, proposed); (4) headline CPI y/y ≥ 1pt below its 12m peak (inflation peaked).
- Data needed: CAPE (in tool); ISM PMI (not free on FRED post-2016; proxy: OECD CLI USALOLITONOSTSAM from 1955, or Philly Fed GACDFSA066MSFRBPHI from 1968); FRED DGS2 (1976); CPIAUCSL. CLI/PMI not in tool.
- Confidence: high.

### Rising real yields = near-term downward pressure on equities
- Source: Peter Oppenheimer — Oppenheimer (quote: "the rise in real yields that means interest rates having taken into account inflation means that the near-term pressure on Equity prices is still probably downwards")
- Type: signal
- Rule as testable logic: IF real 10y yield 6m change > +1 pt (proposed) THEN underweight equities, especially long-duration/unprofitable growth (ARKK, IWO), for 6 months.
- Data needed: real 10y (in tool, DFII10 2003; pre-2003 proxy 10y minus 12m core CPI).
- Confidence: high.

### TARA: positive real yields create alternatives — diversify
- Source: Peter Oppenheimer — Oppenheimer (quote: "now people talk about Tara there are alternatives um to equities ... index linked or real yields rising to positive levels")
- Type: action/instrument
- Rule as testable logic: IF 10y TIPS real yield > 1% (proposed) THEN hold a TIPS sleeve (TIP/LTPZ) 10–20% and raise bond weight vs equities; IF real yield < 0 THEN TINA: overweight equities.
- Data needed: DFII10 (2003); TIP (2003). Real yield in tool.
- Confidence: medium.

### Healthy private balance sheets = shallower downturn
- Source: Peter Oppenheimer — Oppenheimer (quote: "the private sector balance sheets are actually quite healthy ... it may not trigger the kind of negative Spirals and Vicious Cycles")
- Type: regime map
- Rule as testable logic: IF household debt service ratio < its 20y median AND corporate debt/GDP not above 10y high AND bank capital strong THEN cap expected drawdown at ~30% (cyclical): limit derisking to 50% equities rather than 0%.
- Data needed: FRED TDSP (household debt service, 1980), BCNSDODNS/GDP (nonfin corp debt, 1945). Not in tool.
- Confidence: medium.

### Stagflation (1970s): financial assets do badly in real terms
- Source: Peter Oppenheimer — Oppenheimer (quote: "higher inflation eroded the value of many Financial assets and in real terms they did very very badly")
- Type: regime map
- Rule as testable logic: IF core CPI y/y > 4% AND real GDP growth < 1.5% (proposed) THEN stagflation playbook: underweight equities and nominal bonds; overweight commodities (DBC/GSG), energy & materials equities (XLE/XLB), TIPS, cash.
- Data needed: CPI; FRED GDPC1 (1947); commodities index (S&P GSCI from 1970 — GSG 2006; World Bank pink sheet 1960). In tool partly (core CPI); GDP growth and commodity index new.
- Confidence: high.

### Within equities in inflationary bear: quality/profitable growth + low-valued commodity producers
- Source: Peter Oppenheimer — Oppenheimer (quote: "to have a bit of a mixture between quality strong balance sheets relatively defensive growth and very low valued um commodity related parts of markets")
- Type: action/instrument
- Rule as testable logic: IF Fed tightening AND inflation high THEN split equity sleeve: 50% quality (QUAL / Ken French RMW profitability factor) + 50% energy/materials (XLE+XLB); avoid unprofitable growth and cyclicals without pricing power.
- Data needed: QUAL (2013), Ken French RMW (1963), sector SPDRs (1998).
- Confidence: high.

### Higher-for-longer rates = factor-agnostic, diversified, more alpha
- Source: Peter Oppenheimer — Oppenheimer (quote: "interest rates won't Trend downwards as they have done for many many years that means less opportunity for valuations to go up it probably means lower returns")
- Type: regime map
- Rule as testable logic: IF 10y yield 5y trend is up (10y > its 60m average) THEN expect lower index returns and higher dispersion: reduce expected-return assumptions; equal-weight sectors/regions rather than cap-weight growth tilt.
- Data needed: FRED GS10 (1953).
- Confidence: medium.

### Dollar strength drivers: safe haven + rate differential; mean-reverts to PPP long-term
- Source: Peter Oppenheimer — Oppenheimer (quote: "the U.S federal reserves the central bank has been raising interest rates more quickly and more aggressively than many other central banks")
- Type: signal
- Rule as testable logic: IF US 2y − G10 average 2y differential rising (6m change > 0) THEN dollar continues up (hold USD, underweight unhedged international). IF differential falls (other central banks catch up) AND dollar REER > 10% above 20y average THEN rotate toward unhedged international equities (EFA/EEM) for 1–3 years.
- Data needed: US 2y (DGS2), Germany/Japan/UK 2y (OECD/FRED IRSTCI or national), BIS USD REER (FRED RBUSBIS from 1994; RNUSBIS narrow from 1964). Dollar 12m change in tool; differential & REER new.
- Confidence: medium.

### Dollar expensive on PPP — but strong short term
- Source: Peter Oppenheimer — Oppenheimer (quote: "on that basis the dollar does look quite expensive quite overvalued ... in the short term I think Simon probably the dollar remains pretty strong")
- Type: conflict/caveat
- Rule as testable logic: PPP valuation used only for multi-year horizon (≥ 3 years); short-term follows momentum/rates. Agrees with Bessent ("valuation never matters" for timing).
- Data needed: OECD PPP (annual from 1960); REER.
- Confidence: medium.

### FTSE 100 is a global/commodity index; weak sterling helps it
- Source: Peter Oppenheimer — Oppenheimer (quote: "about 75 of the revenues of UK ftse 100 companies come from outside of the UK ... about 50 of the dividends ... paid in dollars")
- Type: action/instrument
- Rule as testable logic: IF GBP falls (GBPUSD 6m change < −8%, proposed) AND commodity prices rising THEN overweight UK large caps (EWU) in local-currency terms vs UK domestic (proxy: FTSE 250 / EWUS small caps) and vs Europe. In stagflation, UK large caps (energy/miners, P/E ~9) outperform.
- Data needed: GBPUSD (FRED DEXUSUK 1971); EWU (1996), EWUS (2014); MSCI UK (1970). Not in tool.
- Confidence: medium.

### Domestic-exposed equities suffer in energy squeeze
- Source: Peter Oppenheimer — Oppenheimer (quote: "our domestic basket of companies in the UK is down quite sharply around 40 this year which is very similar to very domestically exposed parts of other markets like the Dax")
- Type: signal
- Rule as testable logic: IF European natural gas price 6m change > +50% THEN underweight European domestic/small caps (proxy: IEUS, EWG) vs global multinationals.
- Data needed: World Bank Europe gas price (monthly from 1960s); IEUS (2007).
- Confidence: medium.

### Fiscal stimulus vs central-bank tightening clash -> bond/currency sell-off (UK 2022)
- Source: Peter Oppenheimer — Oppenheimer (quote: "add a fiscal stimulus through tax cuts to this cocktail ... seems to be at odds with the bank of England's attempt to slow the economy")
- Type: signal
- Rule as testable logic: IF fiscal easing announced (deficit forecast up > 1% GDP) while central bank hiking AND inflation > 5% THEN short that country's long bonds and currency (gilt/GBP) for 1–3 months; also applies to US (Bessent "Fed vs Treasury" theme).
- Data needed: event dates; 10y yields; FX. Not in tool.
- Confidence: medium.

### ECB stuck between inflation and fragmentation (Italy)
- Source: Peter Oppenheimer — Oppenheimer (quote: "it's pushing up the cost of interest for countries within Europe that have a lot of debt Italy being a notable example")
- Type: signal
- Rule as testable logic: Same as Citrone Italy rule: IF ECB hiking AND BTP–Bund spread 3m change > +50bp THEN underweight EZU/EWI. (Agreement between speakers.)
- Data needed: FRED IRLTLT01ITM156N, IRLTLT01DEM156N.
- Confidence: medium.

### Commodities as diversifier when inflation and rates rise
- Source: Peter Oppenheimer — Oppenheimer (quote: "in periods of higher inflation which means higher interest rates which typically would be a negative for gov Bond markets and equities uh Commodities often Thrive")
- Type: hedge
- Rule as testable logic: IF stock-bond correlation (in tool) > 0 AND core CPI y/y > 3% THEN replace part of Treasury hedge with broad commodities (DBC/GSG/PDBC) — e.g., 50% of the defensive sleeve — since bonds stop hedging.
- Data needed: stock-bond correlation (in tool); commodity index (S&P GSCI from 1970; BCOM from 1960 backfilled; DBC 2006).
- Confidence: high.

### Commodity super-cycle from under-investment
- Source: Peter Oppenheimer — Oppenheimer (quote: "we're in a sort of secular super cycle for for many Commodities because you've had long periods of under investment")
- Type: regime map
- Rule as testable logic: IF energy+mining capex/sales at a 10y low (proposed) AND commodity index above its 10-month average THEN strategic overweight commodities/commodity equities (XLE, XME, GNR) for 3–5 years.
- Data needed: sector capex (S&P/Compustat — not free; proxy: Baker Hughes rig count from 1987; FRED IPN213111N oil/gas drilling IP from 1972); GSG. Not in tool.
- Confidence: medium.

### Copper and electrification
- Source: Peter Oppenheimer — Oppenheimer (quote: "you can't do that without having more copper and copper means mining copper")
- Type: action/instrument
- Rule as testable logic: Strategic: hold copper/copper miners (CPER 2011, COPX 2010) as structural commodity long when copper 6m change > 0 (tool has copper 6m change) and global PMI ≥ 50.
- Data needed: copper (in tool); COPX/CPER; global PMI (proxy OECD CLI).
- Confidence: medium.

### Deglobalization/regionalization + defense + decarbonization = physical capex, higher cost of capital
- Source: Peter Oppenheimer — Oppenheimer (quote: "less globalization and a bit more regionalization that means more production more uh um localization of products everything from food to chip manufacturing batteries")
- Type: regime map
- Rule as testable logic: Structural tilt: overweight industrials/infrastructure (PAVE, XLI, ITA defense) vs software/communication when real capex growth (FRED PNFIC1 y/y) > 4% (proposed).
- Data needed: FRED PNFIC1 / PNFI (1947); PAVE (2017), ITA (2006). Not in tool.
- Confidence: low.

---

## File 6 — Christine Lagarde, ECB President (NBIM In Good Company, March 2026)

Policy-maker view; few explicit trading rules, but regime maps and caveats.

### 1920s analogy: tech breakthrough + fragmentation -> financial crisis risk
- Source: Christine Lagarde — Christine Lagarde - President of the European Central Bank - In Good Company (quote: "Technological breakthrough, which I would, you know, associate with the development of AI and the diffusion of AI on the one hand, and fragmentation")
- Type: regime map
- Rule as testable logic: IF tech-driven valuation boom (CAPE > 30 or market cap/GDP top decile — in tool) AND trade fragmentation rising (US effective tariff rate > 10% or world trade/GDP falling 3y, proposed) THEN raise crash-hedge budget (puts/long Treasuries) and cap equities at 60% (proposed).
- Data needed: CAPE, market cap/GDP (in tool); world trade/GDP (World Bank NE.TRD.GNFS.ZS annual from 1960); US effective tariff (customs duties / imports: FRED B235RC1Q027SBEA / IMPGS). Trade data not in tool.
- Confidence: low.

### Europe most exposed to trade and energy shocks (open economy, no fossil resources)
- Source: Christine Lagarde — Lagarde In Good Company (quote: "it's openness on the one hand, rare fossil energy sources on the other hand, and the two combined exposes us um significantly")
- Type: signal (country)
- Rule as testable logic: IF oil 6m change > +30% OR European gas 6m change > +50% OR global tariff shock THEN underweight Europe (VGK/EZU) vs US (SPY) for 6 months; overweight energy exporters (Norway NORW, Canada EWC, Brazil EWZ).
- Data needed: oil (in tool); gas (World Bank); VGK, NORW (2011), EWC (1996). Not in tool (countries).
- Confidence: medium.

### Oil volatility extreme with Hormuz risk (±30% in a day)
- Source: Christine Lagarde — Lagarde In Good Company (quote: "suddenly the price of oil can go up by 30% and go down by 30% in a matter of one day")
- Type: position sizing/risk
- Rule as testable logic: IF oil 20-day realized vol > 60% annualized (proposed) THEN size any oil position by volatility (target 1% NAV daily risk) and prefer options (USO calls) or energy equities (XLE) over futures ETFs; effects on CPI arrive "in a matter of months" — lag headline CPI forecasts 3–6 months.
- Data needed: WTI/Brent daily (FRED DCOILWTICO 1986); OVX (Cboe oil VIX, FRED OVXCLS from 2007). OVX not in tool.
- Confidence: medium.

### Energy shock pass-through lag
- Source: Christine Lagarde — Lagarde In Good Company (quote: "significant increases in the price of energy which as we know is necessary for all economies and has ripple effects in a matter of months")
- Type: signal
- Rule as testable logic: IF oil 3m change > +30% THEN expect headline CPI y/y up within 3–6 months: shift duration to TIPS (TIP) and short-maturity bonds; delay rate-cut bets.
- Data needed: oil, CPI (in tool).
- Confidence: medium.

### Central-bank policy lags 6–12+ months
- Source: Christine Lagarde — Lagarde In Good Company (quote: "It's a matter of 6, 9, 12, sometimes more months")
- Type: regime map
- Rule as testable logic: Model the effect of rate changes with a 6–12 month lag: e.g., Fed funds 12m change (in tool) predicts unemployment change over the following 6–18 months; don't expect immediate economic response to first cut/hike.
- Data needed: Fed funds, ECB rate (FRED ECBDFR), unemployment.
- Confidence: high.

### Forward guidance trap -> central banks late to inflation
- Source: Christine Lagarde — Lagarde In Good Company (quote: "the regret that I have to have felt completely bound by previous forward guidance")
- Type: conflict/caveat
- Rule as testable logic: IF central bank has committed to a path (forward guidance) while core inflation 3m annualized > 4% THEN expect a policy "catch-up": underweight long bonds (TLT; Bunds via BUNL not available — use IGOV/BWX) until hikes begin and core 3m rate peaks.
- Data needed: core inflation 3m vs 12m (in tool).
- Confidence: medium.

### Central-bank independence under political pressure
- Source: Christine Lagarde — Lagarde In Good Company (quote: "somebody uh whom many central bankers around the the world regard as competent, independent, a beacon of integrity uh was being challenged")
- Type: signal
- Rule as testable logic: IF political pressure on the Fed rises (event: attempts to remove governors/chair; proposed proxy: 10y breakeven 3m change > +0.3 pt while Fed cuts) THEN overweight gold (GLD) and TIPS, underweight long nominal Treasuries and USD.
- Data needed: T10YIE (2003); event dates; gold. Partly in tool (5y inflation expectations 6m change).
- Confidence: medium.

### AI-driven front-loaded Fed cuts (Greenspan 1990s) may not apply: energy, debt differ
- Source: Christine Lagarde — Lagarde In Good Company (quote: "if you look at, you know, public debt for instance, we're not in the same situation as in the Greenspan's days")
- Type: conflict/caveat
- Rule as testable logic: Productivity optimism should not override inflation signals when energy prices are rising and debt/GDP > 100%: keep core inflation and oil rules active even if productivity growth > 2% (FRED OPHNFB).
- Data needed: FRED OPHNFB (productivity, 1947); debt/GDP (GFDEGDQ188S).
- Confidence: low.

### Dollar reserve status slowly eroding; still crisis destination
- Source: Christine Lagarde — Lagarde In Good Company (quote: "in times of of high crisis, it is still a destination for capital flows. There's no doubt about that. Are we seeing the level of confidence slightly undermined")
- Type: hedge
- Rule as testable logic: In acute crises (VIX > 35) the dollar still rallies: keep a USD/T-bill hedge in crises; but test whether the dollar's crisis beta (corr. of DXY with VIX changes) is declining over time (structural). IF USD falls during an equity sell-off (DXY 1m < 0 while S&P 1m < −8%) THEN hedge with gold/CHF/JPY instead of USD.
- Data needed: DXY (FRED DTWEXBGS 2006, DTWEXM 1973–2019); VIX (in tool); FXF (2006), FXY; gold. COFER reserve shares (IMF quarterly from 1999). Not in tool.
- Confidence: medium.

### Euro internationalization (ECB repo lines; digital euro)
- Source: Christine Lagarde — Lagarde In Good Company (quote: "we recently changed uh the regime of our uh euro repo lines in order to make it available on a much broader basis")
- Type: conflict/caveat
- Rule as testable logic: Structural: if euro share of FX reserves (COFER) rises 2 pts over 3 years THEN modest long EUR (FXE) vs USD; low conviction.
- Data needed: IMF COFER (1999). Not in tool.
- Confidence: low.

### Stablecoin growth flat since Oct 2025 (contradiction to Gerstner)
- Source: Christine Lagarde — Lagarde In Good Company (quote: "they have significantly increased up until last October. Since last October it's flat")
- Type: conflict/caveat
- Rule as testable logic: Contradicts Gerstner (stablecoins as biggest T-bill holders). Monitor stablecoin supply growth before attributing bill-demand effects.
- Data needed: stablecoin supply (DefiLlama).
- Confidence: medium.

### Demographics/defense vs social spending -> fiscal pressure in Europe
- Source: Christine Lagarde — Lagarde In Good Company (quote: "If we have to referee and trade off between military expenses ... and if we have to have less of those, you know, social benefits")
- Type: regime map
- Rule as testable logic: IF European defense spending/GDP rising (NATO data) THEN overweight European defense/industrials (proxy: EUAD Europe defense ETF 2024, or ITA) vs broad Europe; higher Bund yields (underweight European duration).
- Data needed: NATO defense expenditure (annual from 1949; SIPRI). Not in tool.
- Confidence: low.

### Europe productivity gap since the internet; AI diffusion could help
- Source: Christine Lagarde — Lagarde In Good Company (quote: "we in Europe have missed the internet revolution")
- Type: conflict/caveat
- Rule as testable logic: Structural reason for Europe's valuation discount (agrees with Trennert "cheap for a reason"); don't buy Europe on CAPE alone. Possible trigger: Euro area labor productivity growth > US for 4 quarters -> overweight Europe.
- Data needed: Eurostat/ECB productivity; FRED OPHNFB. Not in tool.
- Confidence: low.

---

## File 7 — Kristalina Georgieva, IMF Managing Director (NBIM In Good Company, Dec 2025)

Policy-maker view; mostly regime/caveat material.

### Currency board + fiscal discipline ends hyperinflation (EM turnaround template)
- Source: Kristalina Georgieva — Why Cooperation Is Essential in Crisis - IMF (quote: "the IMF did for my country was to help us put in place a currency board which really stabilized the uh economy and put fiscal discipline")
- Type: signal (country)
- Rule as testable logic: IF an EM with inflation > 50% adopts an IMF program with a hard anchor (currency board/peg or credible fiscal rule) AND primary fiscal balance turns positive THEN buy that country's equity ETF/bonds (e.g., ARGT, TUR) 3 months after program approval; hold 2 years. Counter-example: Argentina had many programs "none of them got the country completely out of trouble" — require primary surplus.
- Data needed: IMF program dates (IMF MONA database, from 2002); country CPI (World Bank FP.CPI.TOTL.ZG); primary balance (IMF WEO). Country ETFs. Not in tool.
- Confidence: medium.

### Low debt/deficit EM converging (Bulgaria to euro)
- Source: Kristalina Georgieva — IMF (quote: "Bulgaria today has 24% debt to GDP, 3% deficit and as of January 1 would be a member of the Euro zone")
- Type: signal (country)
- Rule as testable logic: IF an EM's government debt/GDP < 40% AND deficit ≤ 3% AND it is joining a currency union/receiving upgrades THEN overweight its bonds (convergence trade) for the 2 years before entry. Retail proxy limited (frontier ETFs).
- Data needed: IMF WEO debt/deficit (annual from 1980). Not in tool.
- Confidence: low.

### Resilience thanks to institutions; trade shock smaller than feared (no tit-for-tat)
- Source: Kristalina Georgieva — IMF (quote: "on April 2nd the total announced tariffs were around 23%. When we look at the level now 17 18%. And when we look at what is being collected as tariffs more like 8 9%")
- Type: signal
- Rule as testable logic: Measure tariff shock by collected (effective) rate, not announced: IF announced tariff rate − collected rate > 8 pts AND no retaliation by major partners THEN fade tariff-driven equity sell-offs (buy SPY/EFA after −10%, hold 6 months). Agrees with Gerstner's tariff math.
- Data needed: customs duties / goods imports (FRED B235RC1Q027SBEA / IMPGS, quarterly); Yale Budget Lab effective rate. Not in tool.
- Confidence: medium.

### Tariff inflation muted by pre-stocking and margins — not yet "victory"
- Source: Kristalina Georgieva — IMF (quote: "tariffs are putting pressure on prices in the United States. So far that was mute. One because there was prepositioning of goods. Two because companies profitable they could eat up some of the tariffs")
- Type: conflict/caveat
- Rule as testable logic: After a tariff increase, expect goods CPI pass-through lagged 6–12 months; IF core goods CPI 3m annualized > 3% (proposed) after a tariff hike THEN delay duration add.
- Data needed: FRED CUSR0000SACL1E (core goods CPI, 1956). Not in tool.
- Confidence: medium.

### High debt = no buffers for the next shock
- Source: Kristalina Georgieva — IMF (quote: "when you have very high level of debt, you really have no buffers. So when the next shock comes, what do you do?")
- Type: regime map
- Rule as testable logic: IF debt/GDP > 100% AND policy rate < 2% (little monetary space) at the start of a recession THEN expect weaker policy response: deeper drawdown; hold more Treasuries/gold during recession signals. Conversely with space (policy rate > 4%), long-duration Treasuries are the best recession hedge (more room to cut).
- Data needed: FRED GFDEGDQ188S; Fed funds (in tool).
- Confidence: medium.

### Interest-rate normalization makes debt service crowd out
- Source: Kristalina Georgieva — IMF (quote: "servicing debt especially when interest rates are no more zero or even negative takes away money from other productive purposes")
- Type: signal
- Rule as testable logic: Same variable as Bessent interest-cost rule: IF federal interest outlays/GDP rising > 0.5 pt in 2 years THEN fiscal-stress tilt (short duration, gold).
- Data needed: FRED A091RC1Q027SBEA / GDP.
- Confidence: low.

### Climate shocks hit vulnerable EM (Philippines, Vietnam)
- Source: Kristalina Georgieva — IMF (quote: "if you live in the Philippines or Vietnam these days very likely you would be hit dramatically")
- Type: conflict/caveat
- Rule as testable logic: Not a tradable rule; possible risk filter: lower weight for climate-vulnerable EMs (EPHE, VNM) in country rotation.
- Data needed: ND-GAIN index (annual from 1995).
- Confidence: low.

### AI preparedness index: AI productivity gains go to US, Singapore, Denmark
- Source: Kristalina Georgieva — IMF (quote: "on the top of this list are three countries um Singapore, Denmark, United States")
- Type: action/instrument
- Rule as testable logic: Structural tilt: overweight AI-ready countries (US SPY, Singapore EWS, Denmark EDEN) vs low-preparedness EMs over multi-year horizon. IMF growth uplift 0.1–0.8 pt/yr.
- Data needed: IMF AI Preparedness Index (2023 one-off); EWS (1996), EDEN (2012). Not in tool.
- Confidence: low.

### AI bubble: correction likely but not systemic (profitable companies)
- Source: Kristalina Georgieva — IMF (quote: "Will there be a correction? Most likely uh some yes, just because enthusiasm has pushed valuations that are now so stretched. Would that take us to a very bad place? I doubt it")
- Type: regime map
- Rule as testable logic: IF tech valuations stretched (Nasdaq 100 forward P/E > 30, proposed) BUT sector earnings growth > 15% and no credit stress (Baa spread in tool not widening) THEN expect cyclical/event-type correction (≈ −20 to −30%, fast recovery) not structural: limit derisking to trimming tech, keep broad equity.
- Data needed: Nasdaq P/E (not free; proxy: QQQ price/earnings from Shiller-type sources); Baa spread (in tool).
- Confidence: low.

### Coordinated global policy response in crisis (COVID template)
- Source: Kristalina Georgieva — IMF (quote: "it makes a huge difference whether individual countries do their individual thing or the world comes together with a strong uh coordinated uh response")
- Type: re-entry/exit
- Rule as testable logic: IF in a crash (S&P −25%) the G7 central banks cut jointly / IMF-SDR-style liquidity injection AND Fed balance sheet 4-week change > +5% THEN re-enter equities and EM (EEM) within 1 month (2009, 2020 templates).
- Data needed: WALCL weekly; event dates (coordinated cuts 2008-10, 2020-03). Fed net liquidity in tool.
- Confidence: medium.

---

## File 8 — Is OpenAI the Achilles' Heel of the US Economy? (Steve Eisman, The Weekly Wrap, Sept 2026)

### Equity-breaking rate level unknown; 4.5% was wrong, 4.8% approaching
- Source: Steve Eisman — Is OpenAI the Achilles' Heel of the US Economy (quote: "I thought that 4 and 1/2% was the Rubicon and I was wrong. Is it 4.8% or even higher? I don't really know")
- Type: conflict/caveat
- Rule as testable logic: Fixed 10y-yield thresholds are unstable; prefer relative measures: IF 10y yield > S&P earnings yield (Fed-model ERP < 0) OR 10y − nominal GDP growth > 0 (in tool) THEN equity correction risk; test 4.5/4.8/5.0% fixed thresholds vs relative.
- Data needed: DGS10; Shiller earnings yield; 10y minus NGDP (in tool).
- Confidence: medium.

### War-driven oil spike -> inflation fears -> higher yields
- Source: Steve Eisman — Weekly Wrap (quote: "the war heated back up and all prices spiked, thereby driving fears of mounting inflation")
- Type: signal
- Rule as testable logic: IF Brent 1m change > +15% on geopolitical news THEN expect 10y yield up and breakevens up over next month: reduce long duration (TLT) and hold short TIPS (VTIP/STIP) instead. (Tool's oil+rates+dollar squeeze captures the combination.)
- Data needed: Brent; T5YIE (in tool as 5y inflation expectations).
- Confidence: medium.

### Corporate (AI) debt supply pushes up Treasury yields
- Source: Steve Eisman — Weekly Wrap (quote: "part of the problem is the enormous amount of AI debt being issued. This supply is putting pressure on rates")
- Type: signal
- Rule as testable logic: IF IG corporate bond issuance 3m sum y/y > +30% (proposed) THEN underweight long duration (TLT) and IG credit (LQD) vs short bills for 3 months; watch IG spread widening.
- Data needed: SIFMA corporate issuance (monthly from 1996); FRED BAMLC0A0CM IG OAS (1996). Not in tool.
- Confidence: low.

### Treasury jawboning of long rates can fail
- Source: Steve Eisman — Weekly Wrap (quote: "Treasury Secretary Besson's recent attempt to reduce long-term rates appears to have already failed")
- Type: conflict/caveat
- Rule as testable logic: Do not assume Treasury (issuance mix, buybacks) caps the 10y; keep term-premium rule (in tool) active regardless of Treasury policy statements. Contrasts with Bessent's view that bill issuance "goosed" markets.
- Data needed: term premium (in tool).
- Confidence: medium.

### Higher rates good for savers, bad for debt issuers
- Source: Steve Eisman — Weekly Wrap (quote: "higher rates put pressure on any company issuing debt. However, higher rates are good for consumers who save")
- Type: regime map
- Rule as testable logic: IF 3m T-bill yield > core CPI y/y + 1 pt (positive real cash) THEN hold more in T-bills (BIL/SGOV) in the defensive sleeve; underweight high-leverage sectors (utilities, REITs VNQ, small caps IWM).
- Data needed: FRED DTB3, core CPI (in tool); VNQ (2004), IWM (2000).
- Confidence: medium.

### AI capex = half of GDP growth; capex stop -> immediate recession
- Source: Steve Eisman — Weekly Wrap (quote: "Hyperscalers are spending about 700 billion in CapEx this year ... that spend accounts for around half of the 2% GDP growth projected for 2026")
- Type: signal
- Rule as testable logic: IF information-processing equipment + software investment contributes > 40% of real GDP growth (4Q average, proposed) THEN the economy is capex-concentrated: treat a > 10% q/q fall in hyperscaler capex guidance or a 3-month fall in semis (SMH −25%) as a recession warning: cut equities 50% and add Treasuries.
- Data needed: BEA NIPA Table 1.1.2 contributions (equipment: information processing; software) quarterly from 1947; FRED Y033RC1Q027SBEA (info processing equipment), B985RC1Q027SBEA (software); SMH. Not in tool (tool has chips vs 12m high).
- Confidence: medium.

### Two-company dependency chain (OpenAI/Anthropic -> hyperscalers -> Nvidia -> GDP)
- Source: Steve Eisman — Weekly Wrap (quote: "the health of the US economy is extremely dependent on hyperscaler CapEx and hyperscaler CapEx is highly dependent on the health of Anthropic and Open AI")
- Type: signal
- Rule as testable logic: Watch-list trigger: IF Oracle (ORCL) falls > 50% from high AND its credit spread widens (rating BBB− -> junk) OR CoreWeave (CRWV) breaks lows THEN pre-emptively rotate from tech/AI-linked industrials/banks into defensive ETFs (see next rule). Event-based; not backtestable pre-2023.
- Data needed: ORCL price; ORCL bond spreads (FINRA TRACE); rating actions. Not in tool.
- Confidence: medium.

### AI-failure reallocation: low-vol/high-dividend, healthcare, staples, P&C insurers
- Source: Steve Eisman — Weekly Wrap (quote: "let me flag three safety ETFs. One, LVHD ... SPLV, the Invesco S&P 500 Low Volatility ETF. And finally, the KBWP")
- Type: hedge
- Rule as testable logic: IF AI-unwind warning (semis SMH −20% from 12m high AND narrow leadership in tool reversing) THEN move equity sleeve to defensive mix: SPLV/USMV, LVHD, XLV, XLP, KBWP (P&C insurers); hold until SMH regains its 10-month average.
- Data needed: SPLV (2011), USMV (2011), LVHD (2015), KBWP (2010), XLV/XLP (1998); Ken French low-vol / industry portfolios for long backtest (1963). Not in tool.
- Confidence: high (explicit instruments).

### Sectors hit in AI unwind: hyperscalers, semis, investment banks, power/electrification industrials
- Source: Steve Eisman — Weekly Wrap (quote: "Investment banks and large banks. These stocks are at peak valuations. Also, the investment banking cycle is super strong right now, partially because of the financing needs of AI")
- Type: action/instrument
- Rule as testable logic: In an AI-unwind regime, underweight XLK/SMH, IAI (brokers/investment banks), and AI-power industrials (GRID, XLU unregulated power names) — i.e., treat AI exposure as one factor across sectors; measure each sector ETF's beta to SMH and cut those with beta > 0.8.
- Data needed: sector ETF returns; SMH.
- Confidence: medium.

### Customer concentration: top 5 = 70% of Nvidia receivables
- Source: Steve Eisman — Weekly Wrap (quote: "five direct customers accounted for 22%, 14%, 13%, 11%, and 10% of our accounts receivable balance ... That adds up to 70%")
- Type: conflict/caveat
- Rule as testable logic: Concentration amplifies downside: size any semis/AI overweight at ≤ half the normal sector-overweight cap (proposed) while top-customer concentration > 50%.
- Data needed: company 10-Q (manual).
- Confidence: low.

### Circular vendor financing (Nvidia -> customers -> chips) as late-cycle marker
- Source: Steve Eisman — Weekly Wrap (quote: "Nvidia is either lending money or making equity investments. The companies then take that cash and buy more Nvidia chips")
- Type: conflict/caveat
- Rule as testable logic: Monitoring only (cf. 1999–2000 telecom vendor financing). Possible proxy: rise in tech-sector receivables/sales; not backtestable from free data.
- Data needed: company filings.
- Confidence: low.

### Don't call the end without data; prepare rather than predict
- Source: Steve Eisman — Weekly Wrap (quote: "It's still early, and I want to emphasize that I'm not making a major call. Not yet. I'm just preparing")
- Type: position sizing/risk
- Rule as testable logic: Two-stage response: stage 1 (watch signals) = shift 10–20% of equity sleeve to defensives; stage 2 (confirmed by price: S&P below 10-month average, in tool) = full de-risk. Test vs one-step switch.
- Data needed: S&P vs 10m average (in tool).
- Confidence: medium.

### Narrative-dependent loss-making companies: appearances matter for capital access
- Source: Steve Eisman — Weekly Wrap (quote: "when a company is not profitable and has an insatiable need for capital, appearances matter more than anything because if the narrative turns negative, raising capital becomes much more difficult")
- Type: signal
- Rule as testable logic: IF unprofitable-tech basket (proxy: ARKK or Goldman non-profitable tech) underperforms QQQ by > 15% over 3 months THEN funding window closing: reduce speculative growth and AI-supplier exposure.
- Data needed: ARKK (2014); QQQ. Not in tool.
- Confidence: medium.

---

## Cross-speaker contradictions and agreements (batch 4)

- **Currency valuation as signal**: Citrone buys "incredibly competitive" BRL with 12% carry (valuation + carry) vs Bessent "in currencies valuation never matters" and Oppenheimer (PPP only long-run). Test: REER-only vs REER + carry + momentum.
- **Treasury issuance mix**: Bessent (2024) says shifting to bills "goosed" markets/loosened conditions; Eisman (2026) says Bessent's own attempt to lower long rates "appears to have already failed". Test bill-share changes vs 10y term premium and equities.
- **Stablecoins**: Gerstner — stablecoin issuers to become largest T-bill holders; Lagarde — "not convinced of the business case", supply flat since Oct 2025.
- **Equity-breaking 10y level**: Strategas (Aug 2026) — not 4.5%, higher, maybe near nominal GDP 6.5%; Eisman (Sep 2026) — 4.8% "getting closer". Both reject fixed 4.5%. Prefer relative measures (10y vs NGDP, ERP).
- **Higher JGB yields**: Verrone — reflation, fine for Japanese stocks until Japanese banks crack; Citrone (2022) — YCC break is a great short of JGBs (consistent: short bonds, but equities fine); Bessent — BoJ hikes stimulative, but was wrong on yen direction in 2024.
- **Europe**: Citrone (short DAX, energy), Trennert ("cheap for a reason"), Lagarde (most exposed to trade/energy, missed internet) all bearish/structural-caveat; Verrone notes Euro Stoxx at new highs via AI build-out + banks (price contradicts narrative).
- **AI bubble severity**: Georgieva — correction likely but not systemic (profitable); Eisman — OpenAI failure could cause "almost immediate recession"; Strategas — rotation, breadth improving, still bullish. Oppenheimer's taxonomy offers the test: structural (needs leverage + bank stress) vs cyclical/event.
- **Fed put**: Citrone (2022) — no Fed put with high inflation; Oppenheimer — buy when rates and inflation peak; Bessent — Fed loosened prematurely (2023) and reignited the economy. Consistent: dip-buying conditional on inflation.
- **China**: Citrone (short CNH, uninvestable unless reformers), Bessent (FDI collapse, asset-freeze tail risk, deflation export hurts Korea/Germany), Gerstner (de-escalation is the biggest catalyst; would sell chips to China), Verrone (China demand weak — iron ore lows). Mostly bearish China, tactical bounces on tariff relief.
- **Dollar**: Citrone/Oppenheimer/Lagarde — crisis safe haven; Bessent — fiscal release valve "is eventually going to be the dollar". Test dollar crisis beta over time and in fiscal-stress regimes.
- **Tariff impact**: Gerstner and Georgieva agree — effective/collected tariffs (~8–10%) far below announced; market overreacted to announced. Use collected rate.

---

## Batch summary — 10 most important testable ideas

1. **Bear-market taxonomy (Oppenheimer)**: classify drawdowns as structural (bubble + private leverage + bank stress, ~−60%), cyclical (Fed tightening into inflation, ~−30% over ~2 years) or event-driven (exogenous shock, ~−30%, fast recovery); de-risk depth and re-entry timing depend on the type. Needs credit-to-GDP gap, house prices, bank stress.
2. **Bottom checklist (Oppenheimer)**: re-enter stocks when ≥3 of 4 hold: valuation ≤ median, growth deterioration slowing (CLI/PMI 3m change > 0), 2y yield off its peak, CPI ≥1pt below peak. A test of the tool's re-entry logic.
3. **No Fed put when inflation is high (Citrone)**: buy ≥20% crashes only when core CPI ≤3%; with core > 4% stay out until Fed funds stop rising. Plus QT (Fed assets shrinking) as a separate equity headwind.
4. **Melt-up + rate spike = top risk (Trennert)**: S&P 12m > +25% AND 10y 12m change > +1.5pt (1987, 1999, Japan 1989) -> cut equities. A new interaction of existing indicators (rally speed × 10y change).
5. **Real-yield vs breakeven decomposition (Strategas, Oppenheimer)**: yields rising via real rates = growth (stay long cyclicals/banks); via breakevens = inflation (underweight stocks and bonds, own commodities/TIPS); fast real-yield rise = pressure on long-duration growth.
6. **Commodities replace Treasuries as hedge when stock-bond correlation > 0 and inflation > 3% (Oppenheimer)**; stagflation playbook (core CPI > 4%, real GDP < 1.5%): commodities, energy/materials, TIPS, cash.
7. **Gold regime (Bessent)**: gold rising despite rising real yields = official-sector accumulation -> strategic gold; combined with fiscal-dominance markers (deficit > 6% outside recession, interest > defense, debt/GDP > 100%, Fed independence under pressure) -> gold/TIPS over long nominals and USD.
8. **EM country rules (Citrone, Georgieva)**: (a) EM equities lag their FX/credit — sell a country ETF after its currency −10% in 3m or spreads +150bp; (b) buy high-real-rate EMs (Brazil) when inflation has peaked and commodities rise; (c) short pegged/managed currencies with falling reserves and runaway inflation (Turkey); (d) buy regime change/IMF hard-anchor programs with primary surplus (Argentina, Bulgaria).
9. **Copper vs iron ore divergence (Verrone)**: copper up + iron ore down = US/AI capex demand, not China -> overweight US industrials/copper miners, underweight China/Australia/Brazil; China deflation exports hurt Korea (EWY) and Germany (EWG) (Bessent).
10. **AI-unwind defensive switch (Eisman)**: AI capex ≈ half of US GDP growth; trigger (SMH −20%/Oracle −50%/credit stress on AI issuers) -> two-stage move to SPLV/USMV, LVHD, XLV, XLP, KBWP; leaders get benefit of the doubt until a failed rally (Verrone). Also energy-exposed Europe underweight on oil/gas spikes (Citrone, Lagarde, Verrone).

Sizing/risk notes worth encoding: net short max 20–25% of equity (Citrone); volatility budget credit ≈ ½ equity, FX ≈ ⅓; single position cap < 10%; full exit when thesis breaks; asymmetric (≥5:1) option-style tail trades with ≤5%/yr carry (Bessent/Citrone); skip crowded trades (CFTC positioning extremes).

---

## Data requests (series not in the existing tool list)

Macro / fiscal (US):
- US customs duties / effective tariff rate: FRED B235RC1Q027SBEA (1947, quarterly) ÷ FRED IMPGS; Yale Budget Lab effective rate.
- Economic / Trade Policy Uncertainty: FRED USEPUINDXD (daily, 1985), policyuncertainty.com trade EPU (1985); China EPU (1995).
- Federal deficit % GDP: FRED FYFSGDA188S (annual 1929), MTSDS133FMS (monthly 1980); CBO cyclically adjusted deficit.
- Federal interest outlays: FRED A091RC1Q027SBEA (1947); defense FRED FDEFX (1947).
- Federal debt % GDP: FRED GFDEGDQ188S (1966).
- Treasury bills share of marketable debt: Monthly Statement of the Public Debt (TreasuryDirect, 1950s+).
- Foreign holdings of Treasuries: TIC data / FRED FDHBFIN.
- Fed total assets raw: FRED WALCL (2002) (tool has net liquidity only).
- Chicago Fed NFCI: FRED NFCI (1971).
- Real GDP growth: FRED GDPC1 (1947); productivity FRED OPHNFB (1947).
- NAIRU: FRED NROU (1949).
- Household debt service ratio: FRED TDSP (1980); nonfinancial corporate debt FRED BCNSDODNS (1945).
- BIS credit-to-GDP gap, US (1960s); real house prices FRED QUSR628BIS / Case-Shiller CSUSHPINSA (1987), Shiller (1890).
- Food CPI FRED CPIUFDSL (1947); core goods CPI FRED CUSR0000SACL1E (1956); headline CPI FRED CPIAUCSL.
- 2y Treasury FRED DGS2 (1976); 3m bill FRED DTB3 (1954).
- Breakeven 10y FRED T10YIE (2003) for real/breakeven decomposition.
- Leading indicator / PMI proxy: OECD CLI USA FRED USALOLITONOSTSAM (1955); Philly Fed GACDFSA066MSFRBPHI (1968).
- BEA investment contributions to GDP: information-processing equipment FRED Y033RC1Q027SBEA, software B985RC1Q027SBEA (1947); private nonres fixed investment PNFI/PNFIC1.
- Corporate bond issuance (SIFMA, monthly 1996); IG OAS FRED BAMLC0A0CM (1996); BB OAS FRED BAMLH0A1HYBB (1996); EM corporate OAS FRED BAMLEMCBPIOAS (1998).
- S&P earnings yield / P/E and EPS (Shiller, 1871) for equity risk premium; % of S&P members above 200dma (compute from constituents).
- CFTC Commitments of Traders positioning (weekly, 1986) for S&P, Treasuries, currencies, gold, oil.
- Cboe option data: SKEW (1990), PUT index (1986), OVX oil vol FRED OVXCLS (2007).
- Stablecoin supply (DefiLlama, 2018).
- Geopolitical Risk index (Caldara–Iacoviello, monthly 1900 / daily 1985).

Global / country:
- FX: FRED H.10 daily — DEXBZUS (BRL 1995), DEXKOUS (KRW 1981), DEXMXUS (MXN 1993), DEXINUS (INR 1973), DEXCHUS (CNY 1981), DEXJPUS (JPY 1971), DEXUSUK (GBP 1971), DEXUSEU (EUR 1999); broad dollar DTWEXBGS (2006) / DTWEXM (1973–2019).
- BIS real effective exchange rates (FRED RBxxBIS, 1994; narrow from 1964), incl. USD RBUSBIS.
- OECD PPP (annual 1960).
- Foreign 10y yields: FRED IRLTLT01JPM156N (Japan 1989), IRLTLT01DEM156N (Germany 1957), IRLTLT01ITM156N (Italy 1991), UK IRLTLT01GBM156N; China 10y (ChinaBond/Investing.com 2002).
- Policy rates: ECB FRED ECBDFR (1999); BoJ IRSTCB01JPM156N; Brazil Selic (BCB SGS) / IRSTCI01BRM156N.
- Country CPI: Brazil IPCA (BCB / FRED BRACPIALLMINMEI), Japan FRED JPNCPIALLMINMEI, Turkey/Argentina (World Bank FP.CPI.TOTL.ZG, OECD).
- FX reserves (IMF IFS; World Bank FI.RES.TOTL.MO reserves in months of imports, 1960).
- BoJ total assets FRED JPNASSETS (1998); Japan MoF intervention record (1991).
- China: inward FDI (SAFE BoP, 1998), export prices / US import prices from China (BLS, 2003), crude imports (JODI/EIA 2002), PMI (NBS 2005) or OECD CLI China (FRED CHNLOLITONOSTSAM 1993).
- IMF program dates (MONA, 2002); IMF WEO debt/deficit/primary balance (1980); COFER reserve currency shares (1999).
- World trade volume (CPB World Trade Monitor, 1991/2000); trade/GDP (World Bank NE.TRD.GNFS.ZS, 1960).
- Country CAPE (Research Affiliates / Star Capital / Barclays); MSCI country indexes (1970) and TOPIX ROE / Japanese bank index (JPX).
- NATO/SIPRI defense spending (annual); ND-GAIN climate vulnerability; IMF AI Preparedness Index.
- Official-sector gold purchases (World Gold Council, quarterly 2000 / annual 1950).

Commodities:
- Gold price monthly from 1968 (LBMA; World Bank pink sheet 1960; Yahoo GC=F 2000; GLD 2004) — not in tool.
- Iron ore (World Bank pink sheet 1960; FRED PIORECRUSDM 1980).
- European natural gas TTF (World Bank pink sheet), Henry Hub FRED MHHNGSP (1997).
- Brent FRED DCOILBRENTEU (1987) / WTI DCOILWTICO (1986) daily (tool has oil 6m change).
- Broad commodity index: S&P GSCI (1970) / BCOM (1960 backfill) / World Bank energy & non-energy indexes (1960); DBC (2006), GSG (2006), PDBC (2014).
- Energy capex proxy: Baker Hughes rig count (1987), FRED IPN213111N drilling IP (1972).

Instruments (Yahoo tickers, start years) referenced in this batch:
- Countries/regions: EWY 2000, EWZ 2000, EWJ 1996, DXJ 2006, MCHI 2011, FXI 2004, KWEB 2013, INDA 2012, EPI 2008, EWW 1996, ARGT 2011, TUR 2008, EZA 2003, AFK 2008, EWG 1996, EWU 1996, EWUS 2014, VGK 2005, EZU 2000, EWI 1996, EWA 1996, EWC 1996, NORW 2011, EWS 1996, EDEN 2012, EPHE 2010, VNM 2009, EEM 2003, VWO 2005, EMXC 2017, EFA 2001, VEU 2007, IEUS 2007, EUFN 2010.
- Bonds/credit: TLT 2002, IEF 2002, SHY 2002, BIL 2007, SGOV 2020, TIP 2003, LTPZ 2009, VTIP 2012, STIP 2010, TBT 2008, BWX 2007, IGOV 2009, EMLC 2010, LQD 2002, HYG 2007, BKLN 2011, BIZD 2013.
- Currencies: UUP 2007, FXY 2007, YCS 2008, FXE 2005, FXF 2006, CEW 2009, CYB (closed).
- Commodities: GLD 2004, IAU 2005, USO 2006, CPER 2011, COPX 2010, XME 2006, GNR 2010.
- Sectors/factors: SMH 2000/2011, SOXX 2001, XLK/XLE/XLB/XLI/XLV/XLP/XLU/XLY/XLF 1998, KBE 2005, KRE 2006, IAI 2006, XRT 2006, JETS 2015, PEJ 2005, PAVE 2017, GRID 2009, ITA 2006, VNQ 2004, IWM 2000, RSP 2003, QQQ 1999, VTV 2004, QUAL 2013, ARKK 2014, IWO 2000, SPLV 2011, USMV 2011, LVHD 2015, KBWP 2010, PSP 2006, SH 2006; Ken French industry/factor portfolios (1926/1963) for long backtests.
