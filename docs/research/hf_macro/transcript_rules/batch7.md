# Batch 7 — testable macro rules

Files read in full (9): BG2 Gurley & Gerstner (DeepSeek/Tariffs/DOGE); Druckenmiller "Monetary Policy & Markets"; Real Eisman Playbook Ep. 29; Andrew Law Sheffield Boardroom Masterclass; Druckenmiller NBIM In Good Company; Jim Rogers Episode 5; Ken Tropin Macro Hive; "Melt-Up making me nervous" Weekly Wrap; Ken Tropin "Why Macro is Killing It" (Graham Capital).

Note: the BG2 transcript has no punctuation (auto-captions); quotes are verbatim caption text.

---

## File 1 — DeepSeek, Open Source, Tariffs, DOGE, Market Impact (BG2: Bill Gurley & Brad Gerstner, 2025-02-05)

Mostly a tech/AI-policy discussion; few macro rules. Extracted:

### Policy-uncertainty spike -> raise discount rate, cut gross risk
- Source: Brad Gerstner — DeepSeek, Open Source, Tariffs, DOGE, Market Impact - BG2 (quote: "we have to take the discount rate up why because we're a lot less certain about technology politics and and and and economics so to me that means multiples come down")
- Type: signal / position sizing/risk
- Rule as testable logic: IF economic policy uncertainty rises sharply (EPU index 3m average > its 80th percentile of trailing 10y, proposed) THEN reduce equity exposure (e.g., S&P 500 weight -25%, proposed) and expect lower P/E multiples over the next 6 months; also expect higher realized volatility.
- Data needed: Baker-Bloom-Davis Economic Policy Uncertainty index (FRED USEPUINDXM, from 1985; daily USEPUINDXD from 1985) and Trade Policy Uncertainty index (policyuncertainty.com, from 1985); S&P 500 forward P/E (proxy: Shiller CAPE, in tool). NOT in tool (EPU).
- Confidence: medium.

### Uncertainty -> concentrate, drop marginal ideas
- Source: Brad Gerstner — BG2 (quote: "as a risk manager what I have to say to my team is okay we've got a downsize risk right ... you don't do the 10th best idea right or the 11th best idea")
- Type: position sizing/risk
- Rule as testable logic: IF policy uncertainty high (as above) THEN reduce number of active tilts/positions to the top-ranked few and cut gross exposure; for an ETF tool: hold only the highest-conviction 1–3 sleeves instead of spreading across many tilts.
- Data needed: EPU (not in tool); internal signal ranks.
- Confidence: medium.

### Expect higher volatility for ~6 months after a policy-regime shock
- Source: Brad Gerstner — BG2 (quote: "expect way more volatility I think the next 6 months all of this uncertainty means that you're going to have a lot of volatility")
- Type: signal (volatility regime)
- Rule as testable logic: IF tariff/trade-policy uncertainty index jumps (TPU > 2x its 3y median, proposed) THEN expect S&P realized vol over next 6 months above its trailing median; size equity by inverse vol (target-vol sleeve) and/or hold VIX calls / SPY puts.
- Data needed: Trade Policy Uncertainty index (policyuncertainty.com, 1985); realized vol of SPY (Yahoo ^GSPC, 1950); VIX (in tool). TPU NOT in tool.
- Confidence: medium.

### Tariffs: market consensus "loaded gun rarely discharged" vs real intent (caveat)
- Source: Brad Gerstner — BG2 (quote: "don't be lazy in believing the best consensus don't think that this is just about um you know a negotiating tactic")
- Type: conflict/caveat
- Rule as testable logic: Not directly testable; caveat that tariff threats may become permanent — IF effective US tariff rate rises above 5% (proposed) and stays there 3+ months THEN treat as persistent: underweight import-heavy sectors (retail XRT, autos CARZ) and expect higher goods inflation.
- Data needed: US effective tariff rate (customs duties / goods imports: FRED B235RC1Q027SBEA customs duties, and imports of goods BOPGSTB; from 1947/1992). NOT in tool.
- Confidence: low.

### Tariffs raise domestic prices (umbrella pricing), create few jobs
- Source: Brad Gerstner citing a Fed study on 2018 washing-machine tariffs — BG2 (quote: "even the domestic producers rais prices because now the competitive market had raised prices so they now had a price an umbrella")
- Type: signal (inflation)
- Rule as testable logic: IF effective tariff rate rises by >= 2 pts in 12 months (proposed) THEN expect core goods CPI y/y to rise over the next 6–12 months; tilt to TIPS (TIP) over nominal Treasuries.
- Data needed: customs duties (FRED B235RC1Q027SBEA), core goods CPI (FRED CUSR0000SACL1E, 1956). Neither in tool.
- Confidence: medium.

### Chip tariffs = tax on chip buyers/AI capex
- Source: Brad Gerstner — BG2 (quote: "that's really just a a tax on chip manufacturers and on the end buyers ... which which likely means that you get less chips purchased")
- Type: signal (sector)
- Rule as testable logic: IF semiconductor-specific tariffs announced THEN underweight semis (SOXX/SMH) vs market for 3 months (proposed). Event-study only.
- Data needed: event dates (manual); SOXX (2001), SMH (2000). Chips vs 12m high is in tool.
- Confidence: low.

### Credible deficit-cut plan -> lower long rates
- Source: Brad Gerstner — BG2 (quote: "we put together a believable plan where you're going to cut a trillion dollars and balance the budget in in the next few years I'll tell you what's going to happen right interest rates are going to come down")
- Type: signal (fiscal -> rates)
- Rule as testable logic: IF federal deficit as % GDP (12m rolling) falls by >= 1 pt over 12 months (proposed) THEN overweight long Treasuries (TLT/IEF) for next 12 months; IF deficit widens >= 1 pt outside recession THEN underweight long duration (bond vigilantes).
- Data needed: monthly federal surplus/deficit (FRED MTSDS133FMS, 1980), nominal GDP (FRED GDP). Not in tool (only 10y minus nominal GDP growth, term premium).
- Confidence: medium.

### Fiscal stimulus + no spending cuts -> bond vigilantes short Treasuries
- Source: Brad Gerstner — BG2 (quote: "the whole reason Bond vigilantes moved into the bond market and started shorting it is they thought okay here we go Trump's going to stimulate the hell out of the economy")
- Type: signal
- Rule as testable logic: IF term premium rises 12m AND deficit widening (above) THEN avoid long duration; prefer T-bills/short Treasuries (SHV/SHY).
- Data needed: term premium (ACM, in tool), deficit (not in tool).
- Confidence: medium.

### Sovereign wealth fund hurdle = government borrowing cost (~5%)
- Source: Brad Gerstner — BG2 (quote: "we're paying 5% on all that debt so the hurdle rate to our return that is needed on The Sovereign wealth fund right is 5%")
- Type: conflict/caveat (general principle: compare expected equity return vs risk-free/borrow cost)
- Rule as testable logic: IF equity earnings yield (1/CAPE) minus 10y yield < 0 (proposed) THEN equities do not beat the borrowing hurdle: underweight stocks vs Treasuries. (Generalisation of the speaker's hurdle logic.)
- Data needed: CAPE (in tool), 10y yield (in tool).
- Confidence: low.

### Geopolitics: pushing China harder raises Taiwan risk
- Source: Bill Gurley — BG2 (quote: "if you just poke China enough if you keep poking and you keep raising the constraints you increase the odds that they make a run at Taiwan")
- Type: regime map (geopolitics -> asset)
- Rule as testable logic: IF US-China tension index rises (proposed: Caldara-Iacoviello Geopolitical Risk index China/Taiwan sub-index > 90th pct) THEN underweight Taiwan (EWT), semis (SMH) and China (FXI/MCHI); hedge with gold (GLD).
- Data needed: GPR index (matteoiacoviello.com, 1985 monthly; country-specific series); EWT (2000), FXI (2004), MCHI (2011). NOT in tool.
- Confidence: low.

### Protectionism hurts long-run competitiveness (caveat on "fortress" economies)
- Source: Bill Gurley — BG2 (quote: "I don't know of a long-term success uccessful High tariff program")
- Type: conflict/caveat
- Rule as testable logic: IF a country's trade openness (trade/GDP) falls >= 5 pts over 5 years (proposed) THEN underweight that country's index over the next 5 years. Cross-country test.
- Data needed: World Bank trade % GDP (NE.TRD.GNFS.ZS, 1960); MSCI country indexes. NOT in tool.
- Confidence: low.

---

## File 2 — Stanley F. Druckenmiller: Monetary Policy & Markets (Real Vision, 2018-11-13)

### Central-bank balance-sheet rate of change drives equities
- Source: Stanley Druckenmiller — Stanley F. Druckenmiller- Monetary Policy & Markets (quote: "if you go from a trillion in central bank buying a year to zero and you get that rate of change all happening within a 12-month period does that not matter")
- Type: signal (liquidity)
- Rule as testable logic: IF the 12-month change in combined G3 central-bank balance sheets (Fed + ECB + BoJ, USD) falls by >= USD 1 trillion vs its level 12 months earlier (i.e., second derivative sharply negative), proposed: 12m flow turns from > +USD 500bn/yr to <= 0, THEN underweight equities (S&P 500, especially Nasdaq/high-multiple) and EM over next 6–12 months.
- Data needed: Fed total assets (FRED WALCL, 2002; pre-2002 FRED WRESBAL/H.4.1), ECB total assets (FRED ECBASSETSW, 1999), BoJ total assets (FRED JPNASSETS, 1998), EUR/USD and USD/JPY (FRED DEXUSEU, DEXJPUS). Only Fed net liquidity 3m change is in tool; global CB balance-sheet flow NOT in tool.
- Confidence: high (repeated core belief: "it's always about liquidity").

### "Never about earnings, always about liquidity"
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "everything for me has never been about earnings it's never been about politics it's always about liquidity")
- Type: regime map
- Rule as testable logic: IF liquidity composite (Fed balance sheet 6m change + M2 growth, proposed z-score average) is falling AND the Fed is hiking THEN equity weight low regardless of earnings revisions; test whether liquidity composite beats earnings-revision signal for 6–12m S&P returns.
- Data needed: WALCL, M2 (FRED M2SL; in tool), Fed funds (in tool); earnings revisions (no free series; proxy: S&P trailing EPS change, Shiller data 1871).
- Confidence: high.

### Tightening hits EM first; EM stress is the early warning
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "some of the things that tend to happen early in a monetary tightening are responding to the QE shrinkage and that's obviously as you've cited emerging markets")
- Type: signal (lead indicator)
- Rule as testable logic: IF Fed is tightening (funds rate up >= 1 pt in 12m or balance sheet shrinking) AND EM equities (EEM) underperform S&P by >= 10% over 6 months (proposed) THEN treat as early warning for US equities: raise cash/Treasuries share over next 6–12 months.
- Data needed: EEM (2003) or MSCI EM index (1988, msci.com); EMB EM bond ETF (2007); Fed funds (in tool). EM relative strength NOT in tool.
- Confidence: high.

### "Bombs going off" in EM -> tightening continues -> more bombs (until the Fed stops)
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "until the bombs go off in the development markets you would think the tightening will continue and if the tightening continues the bombs will keep going off")
- Type: regime map
- Rule as testable logic: IF Fed hiking AND an EM currency crisis occurs (any of Brazil BRL, South Africa ZAR, Turkey TRY, Argentina ARS falls >= 20% vs USD in 6 months, proposed) THEN stay underweight EM (EEM/EWZ/EZA) and US equities until Fed pauses (no hike for 3+ months).
- Data needed: FX rates (FRED DEXBZUS 1995, DEXSFUS 1971; TRY/ARS from BIS or Yahoo); Fed funds. NOT in tool.
- Confidence: medium.

### EM "lottery ticket": buy Brazil / South Africa after tightening-driven collapse
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "we have a lottery ticket in in Brazil and in South Africa because as we've seen back in the 90s and again now these things can move 5060 percent and your risk is probably not much more than the carry")
- Type: action/instrument (country/EM, asymmetric)
- Rule as testable logic: IF Brazil (EWZ) or South Africa (EZA) index in USD is down >= 40% from 2-year high AND local short rates give positive carry vs USD (policy rate - Fed funds > 4 pts, proposed) THEN buy a small (e.g., 2–5% of portfolio, proposed) position in EWZ/EZA or long BRL/ZAR, hold until +50% or 12 months; exit if Fed keeps tightening and the drawdown deepens by a further 15% (proposed).
- Data needed: EWZ (2000), EZA (2003), MSCI Brazil/SA (1988), Brazil Selic and SA repo rate (BIS policy rates, 1990s; FRED INTDSRBRM193N), BRL/ZAR spot (FRED). NOT in tool.
- Confidence: medium (stated as a current position, framed via 1990s analogue).

### Oil up + dollar up + rates up = earnings recession -> buy 2y/5y Treasuries
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "the price of oil has gone up the dollars going way up and it's rates going up ... I knew that normally this particular cocktail had always been negative for earnings and the US economy")
- Type: signal + action/instrument
- Rule as testable logic: IF oil 12m change > +30% AND trade-weighted dollar 12m change > +5% AND 2y Treasury yield 12m change > +1 pt (proposed thresholds) THEN buy 2y and 5y Treasuries (SHY/IEI; futures-like) and underweight S&P 500 for next 12 months; expect S&P EPS to fall over 12 months (his regression: -25% vs street +18% in 2000).
- Data needed: WTI (FRED DCOILWTICO, 1986; WTISPLC 1946), broad dollar (FRED DTWEXBGS 2006; DTWEXM 1973), 2y yield (FRED DGS2, 1976), 5y (DGS5). Tool has "oil+rates+dollar squeeze" — this confirms it and adds the instrument (2y/5y Treasuries rather than TLT).
- Confidence: high.

### Short-duration Treasuries when 2y yield is below Fed funds and the economy is rolling over
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "the two-year is yielding 6:04 ... and Fed Funds were six and a half so I start buying very large positions in two and five year US Treasuries")
- Type: action/instrument
- Rule as testable logic: IF 2y yield < Fed funds (curve inverted at front end) AND anecdotal/survey business conditions weaken (proposed proxy: NFIB small-business optimism or ISM manufacturing < 50 and falling 3m) THEN overweight 2y/5y Treasuries for 12 months, keep adding on hawkish Fed rhetoric.
- Data needed: DGS2, FEDFUNDS (in tool), NFIB SBOI (nfib.com, 1974 quarterly/1986 monthly), ISM PMI (FRED NAPM discontinued; proxy: Philly Fed FRED GACDFSA066MSFRBPHI 1968). ISM/NFIB NOT in tool.
- Confidence: high.

### Talk to small businesses: survey of operators as recession signal
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "I then went about calling 50 of my clients ... who were all small business men ... and every one of them said their business was terrible")
- Type: signal
- Rule as testable logic: IF NFIB small-business optimism falls >= 5 points over 6 months (proposed) THEN raise recession probability: shift to Treasuries.
- Data needed: NFIB Small Business Optimism Index (1974). NOT in tool.
- Confidence: medium.

### Late-cycle valuation with record margins -> vulnerable to liquidity withdrawal
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "margins are an all-time record we're at the top of the valuation round any measure you look except against interest rates")
- Type: signal (valuation conditional on liquidity)
- Rule as testable logic: IF CAPE > 80th pct AND corporate profit margin (profits/GDP) > 80th pct AND CB liquidity flow turning negative THEN underweight equities. Interaction test.
- Data needed: CAPE (in tool), corporate profits after tax / GDP (FRED CP / GDP, 1947). Profit margin NOT in tool.
- Confidence: medium.

### Fed should hike until financial conditions tighten dramatically (reaction function)
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "they're gonna go every opportunity they have until you have a dramatic tightening and financial conditions")
- Type: regime map / re-entry
- Rule as testable logic: IF Fed hiking THEN expect hikes to continue until a financial-conditions index tightens sharply (proposed: Chicago Fed NFCI rises >= 0.5 sd in 3 months); re-enter equities after a Fed pause that follows such tightening.
- Data needed: Chicago Fed NFCI (FRED NFCI, 1971 weekly). NOT in tool.
- Confidence: medium.

### Fed easing into a strong economy fuels a bubble ("original sin")
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "we cut in September of 98 ... we don't need to be easing there's nothing at all wrong with the American economy and this this money is probably going to flow into the US")
- Type: signal (blow-off)
- Rule as testable logic: IF Fed cuts while unemployment is at/near cycle low (unemployment within 0.3 pt of 24m low) AND S&P at new high THEN expect an equity melt-up over next 6–18 months: stay long equities/Nasdaq (QQQ) but set trailing stop (proposed 15% from peak).
- Data needed: FEDFUNDS, UNRATE (FRED, 1948), S&P (in tool), Nasdaq-100 (^NDX 1985; QQQ 1999).
- Confidence: medium.

### Algo / risk-parity selling: markets down 3% trigger program selling (tail risk)
- Source: Karl (Carol) Sokoloff (interviewer) with Druckenmiller response — Monetary Policy & Markets (quote: "their program to sell if the markets down 3% machines are running can't be stopped")
- Type: conflict/caveat (tail risk)
- Rule as testable logic: IF S&P falls >= 3% in a day while VIX < 15 the prior week (proposed) THEN expect elevated follow-through risk over 5 days; small long-vol hedge (VIX calls / SPY puts) is warranted ahead when VIX very low. Druckenmiller: price signals now less reliable.
- Data needed: S&P daily (1950), VIX (in tool).
- Confidence: low.

### Industry relative strength as economic signal is less reliable in the algo era (caveat)
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "the challenge for me is these groups that used to send me signals it doesn't mean anything anymore")
- Type: conflict/caveat
- Rule as testable logic: Test whether the predictive power of intra-market group signals (cyclicals vs defensives, transports, homebuilders — all in tool) for 6–12m S&P returns / recessions has decayed after ~2010 (split-sample test pre/post 2010).
- Data needed: existing tool indicators.
- Confidence: high (that he believes signal decayed); test is a validation of existing signals.

### Currency regime changes every 15–20 years (what drives FX)
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "currencies traded on current account until Reagan came in and then they traded on interest differentials and about five years ten years ago they started trading on risk-on risk-off")
- Type: regime map / caveat
- Rule as testable logic: For currency sleeves, test rolling (10y) correlation of FX returns with (a) current-account balance, (b) 2y rate differential, (c) VIX/risk-on. Use the factor with the highest trailing correlation (proposed) to set FX positions (e.g., long USD when US-foreign 2y differential widening and that factor dominant).
- Data needed: 2y yields US/Germany/Japan (FRED IRLTLT01 for 10y; 2y from OECD/Bundesbank), current accounts (FRED BOPBCA / OECD), DXY/UUP (2007), FXE (2005), FXY (2007). NOT in tool.
- Confidence: medium.

### Pyramid: start with one-third, add on price confirmation; enter by the 2nd inning
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "normally I'll wait for I'll go in with say a third of a position and then wait for price come from and when I get that when I get a technical signal I go")
- Type: position sizing/risk
- Rule as testable logic: IF a macro signal fires THEN take 1/3 of target position; add remaining 2/3 when price confirms (proposed: instrument breaks its 3-month high/low in the signal direction, or crosses 10m average); do not initiate after the trend is mature (proposed: skip if instrument already moved > 2 sd of 12m returns in signal direction).
- Data needed: price of each instrument (Yahoo).
- Confidence: high.

### Size up only in liquid, 24-hour markets (bonds, currencies)
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "if you're gonna make a bet like that it has to be in a very liquid market even better if it's a liquid market that trades 24 hours a day")
- Type: position sizing/risk
- Rule as testable logic: Concentrated (largest) positions only in highly liquid instruments (Treasury futures/ETFs, major FX, S&P futures); cap single-country EM ETF or commodity ETF weight lower (proposed max 10%) than Treasury/S&P/major-FX positions (max 50%+).
- Data needed: ETF volume (Yahoo).
- Confidence: high.

### Conviction exception: fundamental certainty can override price confirmation
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "sometimes it's price sometimes it's just such a belief from the fundamentals")
- Type: position sizing/risk
- Rule as testable logic: IF multiple independent signals agree (proposed: >= 3 of oil/dollar/rates squeeze, EM stress, liquidity drop, NFIB fall) THEN take full position immediately without waiting for price confirmation.
- Data needed: as above.
- Confidence: medium.

### When cold (in drawdown), bet small until rhythm returns
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "if I was down I had not earned the right to play big and the little bets you're talking about were simply on to tell me had I reestablished a rhythm")
- Type: position sizing/risk
- Rule as testable logic: IF strategy's own year-to-date (or trailing 6m) P&L is negative THEN cut active tilt size by 50% (proposed) until trailing 3m P&L of tilts turns positive. (Strategy-level drawdown control.)
- Data needed: strategy equity curve (internal).
- Confidence: high.

### Fixed-currency regimes: no momentum needed — bet on the break
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "we were dealing in those instances with fixed currencies so you don't there's no price momentum you're betting that something's gonna break")
- Type: action/instrument (FX)
- Rule as testable logic: IF a currency is pegged AND the central bank's policy conflicts with peg (e.g., reserves falling >= 20% in 12m, proposed) THEN short the pegged currency at full size immediately (asymmetric: limited downside). Not retail-easy; reference only.
- Data needed: FX reserves (IMF IFS), peg list. NOT in tool.
- Confidence: medium.

### Central bank goes negative rates while world is long -> short that currency (EUR 2014)
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "they went to negative interest rates it was very clear they were in a trash at currency and the whole world was long")
- Type: signal + action/instrument (FX)
- Rule as testable logic: IF a major central bank (ECB/BoJ/SNB) cuts policy rate below zero or launches QE while US is not easing (rate differential vs Fed widening >= 0.5 pt in 6 months, proposed) THEN short that currency vs USD (FXE/FXY short or UUP long) for 12 months; add when price breaks a round level / 3m low.
- Data needed: ECB deposit rate (FRED ECBDFR, 1999), BoJ rate (FRED IRSTCI01JPM156N), EUR/USD (DEXUSEU), JPY (DEXJPUS); CFTC positioning (CFTC COT, 1986) for "whole world long". NOT in tool.
- Confidence: high.

### Bundesbank-type inflation-hawk central bank -> currency strengthens on fiscal shock
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "the Bundesbank is the most powerful institution in germany the public's is obsessed with inflation and they will do whatever it takes on the right side to keep that currency strong")
- Type: regime map (FX)
- Rule as testable logic: IF a fiscal expansion shock hits a country whose central bank is hawkish (real policy rate rising) THEN go long that currency (the policy-mix rule: loose fiscal + tight money = strong currency). Test on USD 1981–85, DEM 1990, USD 2018, 2022.
- Data needed: structural deficit (IMF WEO / FRED FYFSGDA188S, 1929 annual), real policy rate (policy rate - CPI y/y), FX. Not in tool.
- Confidence: medium.

### Japan breaking yield cap = global liquidity reckoning piece
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "now it looks like yields are breaking out of the jgb ... it's an important all these pieces fit together for reckoning")
- Type: signal (global rates/liquidity)
- Rule as testable logic: IF Japanese 10y yield rises >= 0.3 pt in 6 months (proposed) or makes a 12m high, AND ECB QE ending AND Fed QT THEN underweight global duration (long Treasuries) and equities; long JPY (FXY) as beneficiary.
- Data needed: Japan 10y (FRED IRLTLT01JPM156N, 1989), FXY. NOT in tool.
- Confidence: medium.

### Credit has priced no risk: zombie companies + covenant-lite = next crisis trigger
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "what happens when interest rates start to reflect credit risk")
- Type: signal (credit)
- Rule as testable logic: IF high-yield spread is in bottom 10% of history (proposed: ICE BofA HY OAS < 3.5%) AND Fed tightening (funds up >= 1 pt in 12m) THEN underweight high yield (HYG/JNK) vs Treasuries, prepare to cut equities when HY spread rises >= 1 pt from low (trigger).
- Data needed: ICE BofA HY OAS (FRED BAMLH0A0HYM2, 1996-12), HYG (2007). Junk vs Treasuries 3m and Baa spread are in tool; spread level percentile NOT exactly in tool.
- Confidence: medium.

### Buybacks + leverage + low rates = malinvestment (excess credit growth)
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "corporation's buying back their stock to the tune of five trillion running down their balance sheets")
- Type: signal (credit cycle)
- Rule as testable logic: IF nonfinancial corporate debt / GDP rises >= 3 pts over 3 years (proposed) at a cycle high THEN raise weight of credit-spread warnings; underweight HY.
- Data needed: FRED NCBDBIQ027S (nonfinancial corporate debt, 1945 quarterly) / GDP. NOT in tool.
- Confidence: low.

### Rates too low vs nominal growth = malinvestment seeds (2003-04 analogue)
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "we had nine percent nominal growth in the fourth quarter and we had one percent rate which wasn't even enough")
- Type: signal (policy too loose)
- Rule as testable logic: IF nominal GDP growth y/y minus Fed funds > 4 pts (proposed) for 4+ quarters THEN expect asset bubble/inflation build-up: overweight real assets (commodities DBC, gold GLD, TIPS) and later (when Fed starts hiking from that level) prepare to cut credit/housing exposure.
- Data needed: GDP (FRED GDP, 1947), FEDFUNDS. Tool has 10y minus nominal GDP; Fed funds minus NGDP NOT in tool.
- Confidence: medium.

### Debt cannot handle normal rates (caveat on how far the Fed can hike)
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "now the debt is so much higher particularly in emerging markets than it was five years ago you're not going to be able to raise that much more")
- Type: conflict/caveat
- Rule as testable logic: IF total debt/GDP (US nonfinancial or global) higher than prior cycle THEN expect lower terminal Fed funds; earlier pause; Treasuries rally sooner after first equity stress. Test: terminal rate vs debt/GDP across cycles.
- Data needed: FRED TCMDO (total credit market debt, 1945) / GDP; BIS total credit. NOT in tool.
- Confidence: low.

### Seasonality: Q4 blow-off (esp. Nasdaq) then short around year-end
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "if we get a blow off in the fourth quarter which seasonally tends to happen particularly in Nasdaq ... I could see myself taking a big shot somewhere around year-end")
- Type: signal (seasonal)
- Rule as testable logic: IF Nasdaq-100 rallies >= 10% in Q4 (proposed) AND liquidity flow negative THEN reduce Nasdaq/S&P exposure at year-end for Q1; also test July–August seasonal weakness (he used it for a short).
- Data needed: ^NDX (1985), ^IXIC (1971). Seasonality NOT in tool.
- Confidence: low.

### Bear markets ignore fundamentals: high-growth stocks fall despite beats
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "if and when we get in a bear market it doesn't matter what your fundamental learning is our fight")
- Type: conflict/caveat
- Rule as testable logic: IF S&P below 10-month average (in tool) THEN cut growth/high-multiple sleeves (QQQ, ARKK-like, KWEB China internet) regardless of earnings momentum.
- Data needed: S&P vs 10m (in tool), KWEB (2013), QQQ.
- Confidence: medium.

### Fiscal deficit at full employment -> explodes in recession; foreign holders = trade-war targets
- Source: Karl Sokoloff (interviewer) — Monetary Policy & Markets (quote: "running fiscal deficits that are close to what they were in 2009 I think we have full employment")
- Type: signal (fiscal/debt) — interviewer view, Druckenmiller agreeing
- Rule as testable logic: IF federal deficit > 4% GDP while unemployment < 4.5% (proposed) THEN expect term premium to rise; underweight long Treasuries (TLT) vs short (SHY) outside recessions.
- Data needed: FRED FYFSGDA188S (annual) / MTSDS133FMS (monthly), UNRATE, term premium (in tool). Deficit NOT in tool.
- Confidence: low (interviewer).

### Sanctions overuse erodes trust in USD system (long-run dollar risk)
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "the biggest danger I see is we lose that trust that America is good")
- Type: regime map (geopolitics -> dollar/gold)
- Rule as testable logic: IF central-bank gold purchases rise to >= 2x 5y average (proposed) and US sanctions used broadly THEN overweight gold (GLD) and underweight USD over multi-year horizon.
- Data needed: World Gold Council central-bank purchases (quarterly, 2010; annual 1950), gold (LBMA via FRED GOLDAMGBD228NLBM discontinued; GLD 2004; Yahoo GC=F). NOT in tool.
- Confidence: low.

### Wealth disparity -> populism -> creditor vs debtor conflict (inflationary long run)
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "you're going to have a battle between creditors and debtors at some point up to now the creditors have been winning but they're starting to lose")
- Type: regime map
- Rule as testable logic: IF populist policy regime (proposed proxy: wage share rising + deficit widening + top-1% share high) THEN long-run underweight nominal bonds, overweight TIPS/real assets. Weak testability.
- Data needed: labor share (FRED PRS85006173, 1947), WID top 1% share. NOT in tool.
- Confidence: low.

### Odd correlations (e.g., RMB and gold) signal regime distortion (caveat)
- Source: Stanley Druckenmiller — Monetary Policy & Markets (quote: "the R&B and gold are trading very closely I mean it makes no sense you know and that's very dangerous")
- Type: conflict/caveat
- Rule as testable logic: Not a rule; caveat to avoid trusting short-window cross-asset correlations; use longer windows (proposed 3y) for correlation-based switches (e.g., the tool's stock-bond correlation).
- Data needed: CNY (FRED DEXCHUS 1981), gold.
- Confidence: low.

---

## File 3 — Inside America's Economic Divide: AI, Tariffs, & The Fed (Real Eisman Playbook Ep. 29; Steve Eisman with Steve Liesman, 2025-10-13)

### GDP ex-AI capex flat = narrow economy (K-shape) warning
- Source: Steve Eisman — Inside America's Economic Divide (quote: "If you take all the money that Meta, Google, Amazon, right, Oracle, etc., etc., are spending on AI, it's over 400 billion. So, what's left the the economy X what's being spent on AI is really flat.")
- Type: signal
- Rule as testable logic: IF real GDP growth excluding information-processing equipment + software + data-center structures investment is <= 0.5% y/y (proposed) while headline GDP > 1.5% THEN treat economy as narrow/fragile: underweight cyclicals ex-tech (equal-weight RSP, small caps IWM) vs cash; raise weight of recession indicators.
- Data needed: real GDP (FRED GDPC1, 1947), private fixed investment in information processing equipment (FRED Y033RC1Q027SBEA / real A679RX1Q020SBEA, 1947) and software (B985RC1Q027SBEA, 1959). NOT in tool.
- Confidence: medium.

### "Momentum will continue as long as the momentum continues" — capex rewarded by stock price
- Source: Steve Liesman (citing Josh Brown) — Inside America's Economic Divide (quote: "as long as the market is rewarding companies for increasing their investment in AI, AI investment will continue")
- Type: re-entry/exit (bubble timing)
- Rule as testable logic: IF hyperscaler/AI-leader stocks stop rising on capex increases (proposed proxy: semis SOXX fall below 10-month average OR SOXX/SPY 6m relative < 0) THEN expect capex cycle to roll over: underweight semis/tech (SMH/XLK) and the S&P for 6–12 months.
- Data needed: SOXX (2001) / ^SOX (1994), XLK (1998); chips vs 12m high is in tool.
- Confidence: medium.

### Market shifts from rewarding investment to demanding return (capex cycle top)
- Source: Steve Eisman / Steve Liesman — Inside America's Economic Divide (quote: "Does the market wake up one morning ... and say you know what I don't want to see more investment. I want to see more return. That's coming. I just don't know when.")
- Type: regime map
- Rule as testable logic: IF tech capex growth y/y is > 30% (proposed) AND tech free-cash-flow margins falling for 2 quarters THEN raise risk of tech de-rating; cut XLK/QQQ overweight. Exit trigger = price breaks (see above).
- Data needed: aggregate capex of mega-caps (no free macro series; proxy: BEA info-processing investment growth, FRED A679RX1Q020SBEA). NOT in tool.
- Confidence: medium.

### Equity-funded (not debt-funded) bubble = equity loss, not systemic
- Source: Steve Eisman — Inside America's Economic Divide (quote: "if it falls apart, right, nobody's going back equity loss, not a leverage loss, not a systemic risk")
- Type: conflict/caveat (bubble type)
- Rule as testable logic: IF an equity bubble bursts while credit spreads remain tight (HY OAS < 5%) and bank stocks vs market not falling THEN expect equity-only bear (sell growth, buy Treasuries) but no credit crisis — keep credit exposure, do not short banks. Compare 2000–02 vs 2007–09.
- Data needed: HY OAS (FRED BAMLH0A0HYM2), bank stocks vs market (in tool).
- Confidence: medium.

### Good times: stories; bad times: balance sheets
- Source: Steve Liesman — Inside America's Economic Divide (quote: "in good times, right? People care about stories and in bad times they care about balance sheets")
- Type: regime map (factor rotation)
- Rule as testable logic: IF S&P below 10-month average OR Baa spread widening 6m THEN rotate from growth/momentum to quality (QUAL, from 2013; MSCI Quality index 1975) / low-leverage factor; ELSE allow growth.
- Data needed: QUAL, Ken French profitability factor RMW (1963), Baa spread (in tool).
- Confidence: medium.

### Used-car loan losses = canary for the consumer
- Source: Steve Eisman — Inside America's Economic Divide (quote: "used cars is kind of a a nice sort of what I call a canary in the coal mine kind of view into what's happening in the consumer")
- Type: signal (consumer credit)
- Rule as testable logic: IF auto-loan 90+ day delinquency rate rises >= 1 pt y/y (proposed) or hits a 10y high THEN underweight consumer discretionary (XLY) vs staples (XLP) for 12 months; add to recession composite.
- Data needed: NY Fed Household Debt and Credit auto 90+ delinquency (quarterly, 2003); Fed consumer loan delinquency (FRED DRCLACBS, 1987). Card delinquencies in tool; AUTO delinquency NOT.
- Confidence: medium.

### Car loan is paid first (payment hierarchy) -> auto delinquency is a late, serious signal
- Source: Steve Liesman — Inside America's Economic Divide (quote: "when all the bills come due and you can't pay one, the first thing you pay is your car loan, right?")
- Type: signal
- Rule as testable logic: IF auto delinquencies rise while card delinquencies also rising THEN treat consumer stress as severe (more weight than cards alone): cut equity by one notch.
- Data needed: as above.
- Confidence: medium.

### Student-loan repayment restart may distort auto delinquencies (caveat)
- Source: Steve Liesman — Inside America's Economic Divide (quote: "the extent to which the student loan repayments may be stressing the car data")
- Type: conflict/caveat
- Rule as testable logic: Flag auto/card delinquency signals in 2024–25 as possibly policy-distorted; test signal robustness excluding 2023Q4–2025.
- Data needed: NY Fed student-loan delinquency (2003).
- Confidence: low.

### Youth unemployment vs overall (AI displacing entry-level jobs)
- Source: Steve Eisman — Inside America's Economic Divide (quote: "the current unemployment rate in the United States is four and a half percent. Youth unemployment's around 11.")
- Type: signal
- Rule as testable logic: IF youth (16–24 or 20–24) unemployment minus overall rises >= 1 pt in 12 months (proposed) THEN early labor-market weakening: add to recession composite. (Already in tool.)
- Data needed: FRED LNS14024887 (16–24, 1948), UNRATE. In tool ("youth jobless vs overall").
- Confidence: medium.

### Profits accrue to technology users, not providers, or the cycle dead-ends
- Source: Steve Liesman — Inside America's Economic Divide (quote: "if the profit does not acrue to the users of technology then you're going to hit a dead end")
- Type: signal (sector rotation)
- Rule as testable logic: IF non-tech S&P earnings growth (S&P 500 ex-IT) and nonfarm productivity growth stay below trend (productivity < 1.5% y/y, proposed) 2 years into a capex boom THEN underweight the AI-provider sector (semis) vs market. IF productivity accelerates (> 2.5% y/y) THEN overweight equal-weight/AI-user sectors.
- Data needed: nonfarm productivity (FRED OPHNFB, 1947), sector EPS (no free history; proxy: sector ETF price relatives). NOT in tool.
- Confidence: low.

### Tariffs absorbed in margins first; small business hit hardest
- Source: Steve Liesman — Inside America's Economic Divide (quote: "they're sucking up tariffs in margin and how long that continues is what's unclear to me. I'm also concerned ... about the impact of tariffs on smaller businesses")
- Type: signal
- Rule as testable logic: IF effective tariff rate rises >= 5 pts in 12 months (proposed) THEN underweight small caps (IWM) vs large caps (SPY) and underweight import-input manufacturers; expect corporate margin compression over 4 quarters.
- Data needed: effective tariff rate (customs duties FRED B235RC1Q027SBEA / goods imports FRED IEAMGSN), IWM (2000) / Russell 2000 (1979), NFIB. NOT in tool.
- Confidence: medium.

### Tariffs on inputs hurt domestic manufacturers
- Source: Steve Liesman — Inside America's Economic Divide (quote: "economists would say is a bad idea, which is don't put tariffs on inputs. That's what we did.")
- Type: signal (sector)
- Rule as testable logic: IF tariffs on intermediate goods / metals raised THEN underweight industrials using imported inputs (XLI, autos) vs market for 6–12 months. Event study (2018 steel tariffs, 2025).
- Data needed: event dates; XLI (1998), CARZ.
- Confidence: low.

### Effective vs statutory tariff gap: only half passed through so far
- Source: Steve Liesman — Inside America's Economic Divide (quote: "the effective tariff on goods being imported is 10%. They believe the actual tariff rate is 18%. Ergo, we've only seen half of the tariffs.")
- Type: signal (inflation pipeline)
- Rule as testable logic: IF statutory tariff rate minus effective (collected) rate > 5 pts (proposed) THEN expect further goods inflation over 6–12 months: prefer TIPS over nominal Treasuries; caveat: avoidance (transfer pricing, mislabeling) may keep effective rate down.
- Data needed: Yale Budget Lab statutory rate (2025 only); customs duties (FRED). NOT in tool.
- Confidence: low.

### Funding-market stress (repo/Fed funds traders) as crisis gauge; policy reversal when markets near seizure
- Source: Steve Liesman — Inside America's Economic Divide (quote: "the market, the iners of the market were fairly close to seizing up at that time ... We were very close to a a real seizure in in markets")
- Type: signal + re-entry ("policy put")
- Rule as testable logic: IF funding stress spikes (proposed: SOFR minus IORB > 10 bp, or FRA-OIS/ TED-type spread > 50 bp, or Treasury 10y yield rising while stocks fall >= 10% in a week) THEN expect policy reversal (Treasury/Fed/White House) within ~1–2 weeks: buy equities after the reversal announcement (re-entry), hold 3 months. Test April 2025, March 2020, 2019 repo.
- Data needed: SOFR (FRED SOFR, 2018), IORB (FRED IORB, 2021; IOER before), TED spread (FRED TEDRATE 1986–2022), FRA-OIS (Bloomberg; no free). NOT in tool.
- Confidence: medium.

### Fed follows path of least political resistance
- Source: Steve Liesman — Inside America's Economic Divide (quote: "it's a bit like the way ... that they think a hurricane moves. It follows the path of least resistance.")
- Type: regime map / caveat
- Rule as testable logic: IF political pressure for cuts is high AND long-end yields not rising THEN expect further cuts; IF long end rises on cuts ("resistance") THEN cuts slow. Testable piece: IF the Fed cuts and the 10y yield rises >= 0.4 pt within 3 months of the first cut (proposed) THEN underweight long Treasuries (TLT) — market doubts the Fed.
- Data needed: FEDFUNDS, DGS10 (in tool).
- Confidence: low.

### Fed cutting while inflation above target (3% vs 2%) — Volcker would not
- Source: Steve Liesman — Inside America's Economic Divide (quote: "I don't think Vulker would step forward and say, 'I got a 2% target. I'm at 3% and rise.'")
- Type: signal (inflation regime)
- Rule as testable logic: IF Fed cuts while core PCE/CPI y/y >= 3% and rising (3m annualised > 12m) THEN overweight inflation hedges (TIPS, gold GLD, commodities DBC) and steepeners (short TLT vs long SHY) for 12 months.
- Data needed: core CPI (in tool), core PCE (FRED PCEPILFE, 1959), FEDFUNDS.
- Confidence: medium.

### Credit excess: "done lending to everybody creditworthy and still had money left over"
- Source: Steve Liesman quoting a Deutsche Bank derivatives head — Inside America's Economic Divide (quote: "We got done lending lending to everybody who was creditworthy and we still had money left over.")
- Type: signal (credit cycle)
- Rule as testable logic: IF lending standards loosen for 4+ consecutive quarters (Fed SLOOS net % tightening < 0) AND private credit/GDP rising >= 2 pts/yr (proposed) THEN late credit cycle: reduce HY/financials; prepare for credit-spread triggers.
- Data needed: SLOOS (FRED DRTSCILM C&I, 1990; DRTSCLCC cards), credit-to-GDP (BIS, FRED QUSPAM770A). NOT in tool.
- Confidence: medium.

### Same management reappears = repeat blow-up (pattern in subprime lenders)
- Source: Steve Eisman — Inside America's Economic Divide (quote: "the people who were running them were the same guys who were running them in '98. They just changed the names.")
- Type: conflict/caveat (qualitative)
- Rule as testable logic: Not testable at index level; implication: when a lending sub-sector that blew up re-emerges within 5 years with rapid issuance growth (> 40%/yr, proposed: e.g., CLO/subprime auto ABS issuance), underweight related credit.
- Data needed: SIFMA ABS/CLO issuance (annual, 1990s). NOT in tool.
- Confidence: low.

### Budget deficit -> next-month inflation (monetised deficit, EM case)
- Source: Steve Liesman — Inside America's Economic Divide (quote: "You learn inflation when the government comes out with a budget which is X over it has X deficit and it turns into inflation the next month.")
- Type: signal (EM / fiscal dominance)
- Rule as testable logic: IF a country's deficit is financed by its central bank (central-bank claims on government rising > 20% y/y, proposed) THEN underweight its bonds and currency; country equity in USD underperforms. (Russia 1990s, Turkey, Argentina.)
- Data needed: IMF IFS central-bank claims on government; country FX. NOT in tool.
- Confidence: low.

### Market not the economy (caveat)
- Source: Steve Liesman — Inside America's Economic Divide (quote: "I think you're conflating something in your question, okay, that I try to separate, which is the market and the economy")
- Type: conflict/caveat
- Rule as testable logic: Caveat: economic weakness ex-AI may not translate into index declines while index concentration in AI winners is high; test economic-signal hit rate conditional on top-10 concentration (narrow leadership, in tool).
- Data needed: narrow leadership (in tool).
- Confidence: medium.

---

## File 4 — The Boardroom Masterclass: Andrew Law (Caxton Associates; University of Sheffield, 2020-09-17)

Mostly career advice; few macro rules. Extracted:

### Trend following at weeks-to-months horizon (buy rising, sell falling)
- Source: Andrew Law — The Boardroom Masterclass - Andrew Law (quote: "if we think something is going up in price we will buy it and if we think it's going down we will sell it and our investment horizon is several weeks to several months")
- Type: action/instrument (trend/momentum across asset classes)
- Rule as testable logic: For each instrument (equity indexes, Treasuries, FX, commodities): IF 3-month (proposed; also test 1–12m) total return > 0 THEN long, ELSE short/flat; hold 1 month, rebalance monthly (time-series momentum).
- Data needed: futures/ETF prices (Yahoo: SPY, EWJ, EWZ, EWY, FXI, TLT, IEF, GLD, DBC, USO, UUP, FXE, FXY, from 1990s–2000s; longer: MSCI indexes 1970, Ken French? no; AQR TSMOM factor data free from 1985). Trend on S&P only (10m average) in tool; cross-asset trend NOT.
- Confidence: medium (description of Caxton style, not a specific rule).

### Cut losers, keep winners; right only half the time
- Source: Andrew Law — The Boardroom Masterclass (quote: "i probably get half of the things wrong that i forecast my skill set is not to let it bother me to sell the things that aren't working to keep the things which are working")
- Type: position sizing/risk (stop-loss)
- Rule as testable logic: IF a position loses >= 1 x its 3-month volatility-scaled stop (proposed: -8% for equity ETF, -4% for 10y Treasury, -10% for commodity) from entry THEN close it; let winners run with a trailing stop at 2x that distance (proposed). Measure win rate ~50% with payoff ratio > 1.
- Data needed: instrument prices.
- Confidence: high (general principle).

### Greed and fear: crowd joins trends, panics on losses
- Source: Andrew Law — The Boardroom Masterclass (quote: "people don't want to miss out on trends and the people have a deep fear of losing too much money when it goes wrong")
- Type: regime map (behavioural basis for momentum and capitulation)
- Rule as testable logic: Supports both trend-following (above) and contrarian buying at panic extremes: IF VIX > 40 (proposed) THEN buy S&P after the first 5-day decline in VIX of >= 20%.
- Data needed: VIX (in tool).
- Confidence: low.

### Real-time alternative data (web-scraped case counts) front-runs policy by a month
- Source: Andrew Law — The Boardroom Masterclass (quote: "by sunday morning we knew the game was up the virus had spread outside of china ... that was a month before the government actually chose to do it")
- Type: signal (event / alternative data)
- Rule as testable logic: IF a high-frequency real-time indicator (e.g., Google Trends, mobility, case counts, weekly jobless claims) breaks out (proposed: initial claims 4-week average up >= 20% vs 26-week low) THEN de-risk equities before official monthly data confirms.
- Data needed: weekly initial claims (FRED ICSA, 1967); Google Trends (2004). Claims NOT in tool (tool uses monthly Sahm).
- Confidence: medium.

### Markets ignore a building crisis then "flip a switch" to panic
- Source: Andrew Law — The Boardroom Masterclass (quote: "the markets literally flip a switch one day from ignoring events to panicking about them")
- Type: conflict/caveat (regime change speed)
- Rule as testable logic: Implies holding cheap tail hedges continuously rather than timing: maintain a small budget (proposed 0.5–1%/yr of portfolio) of 3-month 10%-OTM SPY puts or VIX calls, larger when VIX < 15.
- Data needed: VIX (in tool); CBOE PPUT put-write / CBOE tail-hedge indexes (CBOE VXTH from 2006; PPUT from 1986) as backtest proxy. NOT in tool.
- Confidence: medium.

### Crises are recurrent; cannot be timed (sizing implication)
- Source: Andrew Law — The Boardroom Masterclass (quote: "although it's hard to forecast the timing of crises history suggests that crises always happen um they happen when nobody really expects them")
- Type: position sizing/risk
- Rule as testable logic: Never run max leverage; keep portfolio drawdown limit (proposed: cut gross exposure by half if portfolio is -10% from peak; restore after new 3-month high).
- Data needed: strategy equity curve.
- Confidence: medium.

### Political shock: market's prior assumption reverses within hours (2016 election)
- Source: Andrew Law — The Boardroom Masterclass (quote: "the u.s stock market fell by six seven eight percent during asian hours ... the markets reversed actually within 12 hours of the election results")
- Type: re-entry/exit (event)
- Rule as testable logic: IF an overnight political-shock gap down in S&P futures >= 4% (proposed) THEN do not sell at the open; buy if the cash session recovers above the prior close; test event reversals (Brexit, 2016, April 2025).
- Data needed: S&P futures (ES=F Yahoo, 2000) intraday — limited free; daily open/close (^GSPC open from 1982).
- Confidence: low.

### Fiscal + monetary bazooka after a crash (avert 1930s) -> buy risk
- Source: Andrew Law — The Boardroom Masterclass (quote: "the massive government stimulus the furloughing of workers paying people's bills mortgage holidays business loans and so forth all designed to avert what would have been a repeat of history from the 1930s")
- Type: re-entry/exit
- Rule as testable logic: IF Fed cuts to zero AND starts QE AND fiscal deficit expands >= 5% GDP within 6 months of an equity drawdown >= 30% THEN re-enter equities fully (override bearish macro warnings) for 12 months.
- Data needed: FEDFUNDS, WALCL, deficit (FRED MTSDS133FMS), S&P drawdown.
- Confidence: medium.

### Close positions before holidays (risk discipline)
- Source: Andrew Law — The Boardroom Masterclass (quote: "most of the people in my company close down nearly all their positions their investment positions before they go on holiday")
- Type: position sizing/risk
- Rule as testable logic: Not relevant for a systematic tool (operational). Skip testing.
- Data needed: none.
- Confidence: low.

### ESG becomes central to investing (flows thesis)
- Source: Andrew Law — The Boardroom Masterclass (quote: "esg environment social and governance i think is is of a whole different order and it's going to become a really central part of all investing")
- Type: signal (structural flows)
- Rule as testable logic: Long clean-energy ETF (ICLN, 2008) vs energy (XLE) when ESG fund flows rising? Weak; proposed: no rule, note as thematic.
- Data needed: ICLN, XLE; ESG flow data (Morningstar, paid). NOT in tool.
- Confidence: low.

---

## File 5 — Stan Druckenmiller, In Good Company (Norges Bank Investment Management, 2024-11-06)

### Financial conditions: Fed easing into loose conditions -> inflation re-acceleration risk
- Source: Stanley Druckenmiller — Stan Druckenmiller - Podcast - In Good Company (quote: "to cut 50 basis points with credit spreads tight gold at new highs equity's roaring no sign of weakness ... that just makes me nervous that this thing could turn up again")
- Type: signal (inflation)
- Rule as testable logic: IF Fed cuts AND HY spread in bottom quintile AND gold at a 12m high AND S&P within 5% of its high (all proposed thresholds) THEN expect inflation second wave: short long Treasuries (TLT short / underweight duration), overweight TIPS, gold, commodities for 12 months.
- Data needed: FEDFUNDS, HY OAS (FRED BAMLH0A0HYM2), gold (GLD / Yahoo GC=F / LBMA), S&P (in tool), Chicago Fed NFCI (FRED NFCI). Gold and NFCI NOT in tool.
- Confidence: high (his live position: 25% NAV short 10y-equivalent from the day of the cut).

### 1970s double-hump inflation template
- Source: Stanley Druckenmiller — In Good Company (quote: "inflation came down I think from about 8 to 3 and then went back up again ... and the number of months um would correlate to the bottom being right about now")
- Type: regime map (inflation)
- Rule as testable logic: IF core CPI y/y fell >= 4 pts from a peak > 6% AND the Fed starts cutting while core inflation still > 2.5% THEN raise probability of a second inflation wave over the next 12–24 months: tilt to short duration (SHY), TIPS, commodities (DBC), energy (XLE), underweight long nominal bonds.
- Data needed: core CPI (in tool), FEDFUNDS. Combined state NOT in tool.
- Confidence: medium.

### Money supply growth 40% -> inflation conviction (2021)
- Source: Stanley Druckenmiller — In Good Company (quote: "I don't have conviction like I had in 21 that inflation was going going to go up that's when the money supply was growing 40% and all sorts of things were happening")
- Type: signal (inflation)
- Rule as testable logic: IF M2 growth y/y > 15% (proposed) THEN expect core CPI to rise over 12–24 months: short long Treasuries, long TIPS/commodities/gold. (Tool has M2 growth; this adds threshold and instrument.)
- Data needed: M2SL (in tool).
- Confidence: high.

### Short bonds when the Fed makes a policy mistake (ease into strength)
- Source: Stanley Druckenmiller — In Good Company (quote: "I'm short ponds ... I shorted them literally the day the FED cut ... I'm like 25% naav short uh 10e equivalent")
- Type: action/instrument
- Rule as testable logic: IF first Fed cut occurs while unemployment < 4.5%, core CPI > 2.5%, and S&P within 5% of high (proposed) THEN short 10y Treasury (TBF / short IEF / TBT) sized ~25% NAV duration-equivalent (his size), hold until core inflation peaks or 10y reaches nominal GDP growth.
- Data needed: UNRATE, core CPI, DGS10, TBF (2009), TBT (2008).
- Confidence: high.

### 10-year yield can rise to nominal GDP growth
- Source: Stanley Druckenmiller — In Good Company (quote: "the 10 year I guess it's around 4 and a half it can go to nominal GDP")
- Type: signal (rates fair value) / exit
- Rule as testable logic: IF 10y yield < nominal GDP growth y/y by >= 1 pt AND inflation re-accelerating THEN short/underweight long Treasuries; target/exit when 10y >= nominal GDP growth. (Tool has 10y minus nominal GDP; adds trading rule.)
- Data needed: DGS10, GDP (in tool).
- Confidence: high.

### Bond market reacts late in inflationary second waves (1970s)
- Source: Stanley Druckenmiller — In Good Company (quote: "the bond market didn't really respond until we went back up from like 3 to 12 and then it it responded in Spades")
- Type: conflict/caveat
- Rule as testable logic: In second inflation waves, short-bond signal should be based on inflation trend (core 3m > 12m and rising), not on bond price momentum; test lag between CPI re-acceleration and 10y yield breakout (1976–80).
- Data needed: CPI, 10y from 1953 (FRED GS10).
- Confidence: medium.

### Fiscal deficit 7% of GDP at full employment: "bankrupt slowly then suddenly"
- Source: Stanley Druckenmiller — In Good Company (quote: "running deficits with full employment at basically at 7% of GDP is a recipe that can't last forever")
- Type: signal (fiscal/debt)
- Rule as testable logic: IF federal deficit > 5% GDP while unemployment < 5% (proposed) THEN structural underweight long Treasuries vs T-bills; gold overweight. Trigger for acute action: failed/weak Treasury auction (tail >= 3 bp, proposed) -> short TLT 3 months.
- Data needed: deficit (FRED FYFSGDA188S annual; MTSDS133FMS monthly), UNRATE; auction tails (TreasuryDirect auction results, 1990s+; derived). NOT in tool.
- Confidence: medium (timing explicitly unknown).

### Refinancing wall: private sector termed out debt; rollover 2025–26 is when rates bite
- Source: Stanley Druckenmiller — In Good Company (quote: "80% of individuals refinance their mortgages so the average mortgage rate is still under 4% ... corporations termed out their debt that stuff rolls over in 25 and 26")
- Type: signal (lagged rate transmission)
- Rule as testable logic: IF effective interest rate on outstanding debt (household mortgage effective rate or corporate interest/debt) is >= 2 pts below the marginal market rate (proposed) THEN tightening impact is delayed; time recession/credit warnings by the rollover schedule; expect lagged hit when gap closes.
- Data needed: average outstanding mortgage rate (BEA mortgage interest / mortgage debt; FHFA), 30y mortgage (FRED MORTGAGE30US, 1971). Gap NOT in tool (mortgage rate 12m change is in tool).
- Confidence: medium.

### Reserve currency status lets the US run deficits others cannot (caveat)
- Source: Stanley Druckenmiller — In Good Company (quote: "because the reserve currency we've been permitted to engage in behavior that say the Brits couldn't have behaved in")
- Type: conflict/caveat
- Rule as testable logic: Fiscal-stress signals should be weighted less for USD/Treasuries than for non-reserve countries (UK gilts 2022): apply deficit rules to UK, Italy, EM bonds with higher weight.
- Data needed: country deficits (IMF WEO), 10y yields (FRED IRLTLT01GBM156N etc.).
- Confidence: medium.

### Narrow leadership is a necessary (not sufficient) condition for a bear market — yellow light
- Source: Stanley Druckenmiller — In Good Company (quote: "we've never had a bare Market start without the leadership narrowing ... it's a yellow light it's not a red light")
- Type: signal (breadth)
- Rule as testable logic: IF narrow leadership (in tool: e.g., equal-weight S&P vs cap-weight 6m < -5%, or % of stocks above 200d < 50% while S&P near high) THEN only "yellow": do not cut on its own, but require it as a precondition for other bearish signals to cut equities. Test as an AND-gate.
- Data needed: RSP vs SPY (2003; S&P equal weight index 1990), narrow leadership (in tool).
- Confidence: high.

### Financials improving = broadening (bullish offset)
- Source: Stanley Druckenmiller — In Good Company (quote: "you're starting to get some broadening out the financials are doing better")
- Type: signal
- Rule as testable logic: IF bank/financial stocks outperform S&P over 3 months THEN breadth improving: reduce weight of narrow-leadership warning. (Bank stocks vs market in tool.)
- Data needed: XLF/KBE vs SPY (in tool).
- Confidence: medium.

### Fed's job is to avoid the big mistakes; fine-tuning soft landings -> error (caveat on Fed)
- Source: Stanley Druckenmiller — In Good Company (quote: "the fed's job is to avoid the big big mistakes yeah like the 70s like the great financial crisis like the big inflation we just had but all this fine tuning")
- Type: conflict/caveat
- Rule as testable logic: Forward guidance reduces Fed optionality -> when the Fed has guided a series of cuts and inflation surprises upward (CPI above consensus 2 months in a row, proposed), expect a sharp rise in long yields: underweight TLT.
- Data needed: CPI surprises (no free consensus series; proxy: core CPI 3m annualised rising above 12m).
- Confidence: medium.

### Bottom-up company data as the macro read
- Source: Stanley Druckenmiller — In Good Company (quote: "I do a macro from the bottom up so we're listening primarily to companies and we're not seeing any material signs of weakness other than maybe in the housing market")
- Type: signal
- Rule as testable logic: Proxy for company commentary: IF aggregate earnings revisions / corporate guidance negative (proxy: Philly Fed future activity index < 0, or NFIB expected business conditions falling) THEN recession risk in 3–6 months: de-risk. 
- Data needed: Philly Fed future general activity (FRED, 1968), NFIB. NOT in tool.
- Confidence: medium.

### Invest first, investigate later (starter position), then add or cut
- Source: Stanley Druckenmiller — In Good Company (quote: "we will buy something a meaningful position but not Earth shaking and then really do the work and if I think we made a mistake I'll sell it")
- Type: position sizing/risk
- Rule as testable logic: When a new signal first fires, take a partial position immediately (proposed 1/3 of target) instead of waiting for full confirmation; scale up if signal persists and price confirms over 1–3 months; exit if signal reverses.
- Data needed: signal history.
- Confidence: high.

### Look 18–24 months ahead; cyclical capacity shutdowns -> future profits
- Source: Stanley Druckenmiller — In Good Company (quote: "if you're dealing with a psychical company and they're losing money ... and everybody in their industry is shutting capacity down it doesn't take a rocket scientist to try and envision 18 to 24 months out")
- Type: signal (commodity/cyclical cycle)
- Rule as testable logic: IF a commodity/cyclical sector is in a deep drawdown (sector ETF >= 50% below 5y high, proposed) AND capacity is being cut (proxy: Baker Hughes rig count down >= 40% y/y for energy; capex falling) THEN buy the sector/commodity (XLE, XOP, XME, COPX, URA) and hold 18–24 months.
- Data needed: Baker Hughes rig count (1987 weekly, free), XLE (1998), XOP (2006), XME (2006), sector industrial production / capacity utilisation (FRED CAPUTLG211S oil & gas, 1967). NOT in tool.
- Confidence: high (stated as general principle).

### Never invest in the present
- Source: Stanley Druckenmiller — In Good Company (quote: "the biggest mistake investors make is they invest in the present rather than forward looking and looking where the Puck's going")
- Type: regime map (use leading not coincident indicators)
- Rule as testable logic: Weight leading indicators (curve, permits, credit spreads, liquidity, market-based signals) over coincident data (GDP, earnings) in signal composite; test that leading-only composite beats coincident composite.
- Data needed: existing tool indicators.
- Confidence: high.

### Tops = rate of change of the rise flattens (technical)
- Source: Stanley Druckenmiller — In Good Company (quote: "a top is something the rate of change of it's going up changes and it tends to flatten out for quite some time")
- Type: re-entry/exit
- Rule as testable logic: IF an instrument's 3m momentum falls below its 12m momentum/4 (proposed: deceleration) after a > 50% 12m rise THEN take partial profits (cut 1/3); full exit on break of 10-month average. Caveat: may be a bull flag.
- Data needed: instrument prices.
- Confidence: medium.

### Willing to buy back higher (no anchoring to own exit)
- Source: Stanley Druckenmiller — In Good Company (quote: "I'm perfectly willing to buy something back higher than I sold it some people can't get themselves do it")
- Type: re-entry/exit
- Rule as testable logic: Re-entry rules must be signal-based, not price-anchored: re-enter when signals turn back positive regardless of exit price.
- Data needed: none.
- Confidence: high.

### Sell when the thesis breaks, regardless of entry price
- Source: Stanley Druckenmiller — In Good Company (quote: "if the reason I bought a stock is no longer the case I don't care what I paid for it")
- Type: re-entry/exit
- Rule as testable logic: Exit as soon as the triggering macro condition no longer holds (no hold-to-breakeven); test exit-on-signal-off vs fixed holding period.
- Data needed: signal history.
- Confidence: high.

### Concentrate when conviction is high; "one-way bet" -> 100–200% of NAV
- Source: Stanley Druckenmiller (recounting Soros) — In Good Company (quote: "this is a one-way bet they come along very very rarely it's ridiculous doing 100% we should put 200% of the fund in this trade")
- Type: position sizing/risk
- Rule as testable logic: IF downside is capped (e.g., carry cost small: pegged currency forward cost 0.5% for 6 months) AND upside large THEN size up to max allowed; generally: size proportional to estimated payoff ratio (Kelly-like), cap e.g. 1.5x NAV for Treasuries/FX. "It's not whether you're right or wrong, it's how much you make when right vs lose when wrong."
- Data needed: implied carry (FX forwards; proxy: rate differential).
- Confidence: high.

### Peg under economic divergence -> short the weak-economy currency (ERM 1992)
- Source: Stanley Druckenmiller — In Good Company (quote: "this one economy is booming and they need higher rates this other economy is falling apart they need lower rates that's these two currencies shouldn't be linked")
- Type: signal + action/instrument (FX)
- Rule as testable logic: IF two currencies are pegged AND growth/housing divergence (GDP growth gap >= 2 pts, or one country's house prices falling) AND anchor central bank signals hawkishness THEN short weaker currency vs anchor at large size (cost = carry). Modern analogues: HKD, DKK, CNY band, Gulf pegs, EM managed pegs.
- Data needed: GDP growth (OECD), policy rates, FX. Not in tool.
- Confidence: high.

### After a devaluation: buy that country's bonds and stocks (concentric circles)
- Source: Stanley Druckenmiller — In Good Company (quote: "the guilts were down two points which I thought was ridiculous British needed lower rates ... so I bought guilts I bought British stocks")
- Type: action/instrument (country)
- Rule as testable logic: IF a currency breaks a peg / falls >= 10% in a month AND the country's economy needed lower rates (inflation low, unemployment rising) THEN buy that country's government bonds and equities (EWU, IGLT-like; local index in local currency) for 6–12 months.
- Data needed: FX, country 10y yields (FRED IRLTLT01xxM156N), MSCI country indexes (EWU 1996).
- Confidence: high (for the pattern), medium (general).

### Trade themes through "dominoes": second-order beneficiaries (AI -> power, uranium)
- Source: Stanley Druckenmiller — In Good Company (quote: "we knew it would affect power we knew it would affect uranium we just went through the whole chain")
- Type: action/instrument (thematic chain)
- Rule as testable logic: IF a theme ETF leads (e.g., SMH +50% 12m) THEN overweight second-order sectors (utilities XLU, uranium URA, copper COPX, grid/industrials) when they begin to outperform (3m relative > 0). Test lead-lag between SMH and URA/XLU/COPX.
- Data needed: SMH, URA (2010), XLU (1998), COPX (2010).
- Confidence: medium.

### Multiple asset buckets; bonds and currencies move most in equity bear markets
- Source: Stanley Druckenmiller — In Good Company (quote: "the most action in bonds and currencies tends to happen in bare markets and Equity markets so you can put the put the equities in the drawer for a while")
- Type: action/instrument / regime map
- Rule as testable logic: IF equity bear-market regime (S&P below 10m average and unemployment rising — already the tool's trigger) THEN shift risk budget from equities to bond/FX trend positions (long Treasuries 2–10y, long USD or JPY, short EM FX), not just to cash.
- Data needed: Treasury ETFs/futures, UUP, FXY, CEW (EM FX ETF, 2009) or JP Morgan EM FX index.
- Confidence: high.

### Drawdowns: avoid big drawdowns to reduce stress (risk mgmt)
- Source: Stanley Druckenmiller — In Good Company (quote: "there's less stress if you don't have big draw Downs")
- Type: position sizing/risk
- Rule as testable logic: Portfolio-level drawdown control: IF strategy drawdown >= 10% from peak (proposed) THEN halve active tilt sizes (consistent with "cold streak" rule in File 2).
- Data needed: strategy equity curve.
- Confidence: medium.

### Late-1990s: Fed easing during EM crisis with strong US economy -> ride Nasdaq melt-up, then exit
- Source: Stanley Druckenmiller — In Good Company (quote: "green span e because of the agent financial crisis while our economy was strong and we had the internet and all this behind it")
- Type: regime map (bubble)
- Rule as testable logic: IF Fed eases because of foreign (EM) crisis while US unemployment at low THEN overweight Nasdaq (QQQ) for up to 12–18 months; exit on 10-month average break. Warns that chasing after exiting (re-buying near top) was his worst mistake.
- Data needed: ^NDX, FEDFUNDS, UNRATE, EM index.
- Confidence: medium.

### Dollar 50% / oil 25% / rates 25% regression for next-year S&P earnings
- Source: Stanley Druckenmiller citing Ed Hyman — In Good Company (quote: "it's 50% I think currency 25% oil and 25% interest rates and it looks one year forward and it predicts earnings")
- Type: signal
- Rule as testable logic: Build composite = 0.5*z(dollar 12m change) + 0.25*z(oil 12m change) + 0.25*z(10y or 2y yield 12m change); IF composite > +1.5 sd (proposed) THEN expect S&P EPS decline over next 12 months: cut equities, long 2–10y Treasuries (he went to 350% 10y-equivalent). Refines the tool's oil+rates+dollar squeeze with weights.
- Data needed: broad dollar (FRED DTWEXBGS / TWEXB 1973), WTI, DGS10/DGS2. Existing squeeze indicator in tool; weights new.
- Confidence: high.

---

## File 6 — Episode 5: Jim Rogers (Generating Alpha Podcast, 2025-01-04)

Mostly life advice; macro content is thin. Extracted:

### Buy the disaster that the world needs (agriculture contrarian)
- Source: Jim Rogers — Episode 5- Jim Rogers (quote: "agriculture has been a disaster of course and whenever you find a dis disaster especially if it's something the world needs and it changes you'll probably be very successful")
- Type: signal + action/instrument (commodity cycle)
- Rule as testable logic: IF an essential commodity group (agriculture, energy, metals) index is >= 50% below its 10-year high (proposed) or its real (CPI-deflated) price is in the bottom quintile of 50 years, AND a catalyst of change appears (proposed: index above its 10-month average, or 12m momentum > 0) THEN buy that commodity index (DBA agriculture; RICI/BCOM sub-indexes; DBC) and hold 3–5 years.
- Data needed: World Bank Pink Sheet agriculture/energy/metals price indexes (monthly, 1960), BCOM sub-indexes (1991; S&P GSCI 1970), DBA (2007), CPI. NOT in tool.
- Confidence: medium.

### Nobody wants the job -> supply shortage (labor/capacity contrarian signal)
- Source: Jim Rogers — Episode 5 (quote: "I doubt if any of your classmates want to be Farmers which means they probably should be farmers")
- Type: signal (supply cycle)
- Rule as testable logic: IF investment/capacity in a commodity sector falls for 5+ years (proposed proxy: farm employment or mining capex declining; ag land under-invested) THEN overweight that commodity over 5–10 years. Weakly testable.
- Data needed: BLS mining/logging employment (FRED CES1000000001, 1939), farm income (USDA). NOT in tool.
- Confidence: low.

### China rises again (long-run overweight China)
- Source: Jim Rogers — Episode 5 (quote: "China is the only country in world history that's been on top three or four times ... China's Rising again yeah whether we like it or not")
- Type: regime map (country)
- Rule as testable logic: Structural: hold China (MCHI/FXI) at >= its MSCI ACWI weight; tactical (proposed) only when China index above its 10-month average. Caveat: China MSCI returns 2007–2024 were poor — test explicitly.
- Data needed: MSCI China (1992), FXI (2004), MCHI (2011).
- Confidence: medium (as belief), low (as timing rule).

### Frontier markets on long-run reform stories (Uzbekistan)
- Source: Jim Rogers — Episode 5 (quote: "I am extremely bullish on usbekistan these days ... if I'm right it's a place where you can invest now")
- Type: action/instrument (frontier)
- Rule as testable logic: IF a frontier country opens up (reforms, currency liberalisation; proposed proxy: currency unpegged + IMF program completed) THEN buy frontier ETF (FM, 2012) or country fund early; hold 5+ years. Not retail-tradeable for Uzbekistan directly.
- Data needed: FM ETF; MSCI Frontier index (2002). NOT in tool.
- Confidence: low.

### Money printing debases currency -> long run bad; own real assets
- Source: Jim Rogers — Episode 5 (quote: "money printing may be a temporary solution to something but it's in the end it's not good debasing currency there are very few countries that have become successful by debasing the currency")
- Type: regime map (inflation/currency)
- Rule as testable logic: IF central-bank balance sheet / GDP rises >= 5 pts in 12 months (proposed) THEN overweight gold and commodities vs cash and long nominal bonds over the next 3 years; underweight that currency.
- Data needed: WALCL / GDP; gold; DBC; DXY. Fed net liquidity in tool (3m change only).
- Confidence: medium.

### Largest debtor nation -> long-run US decline (Britain analogue)
- Source: Jim Rogers — Episode 5 (quote: "the US has become the largest debtor nation in the history of the world ... 100 years ago Britain was the richest most powerful country in the world 50 years later they were bankrupt")
- Type: regime map (fiscal/debt -> dollar)
- Rule as testable logic: IF US net international investment position worsens (NIIP/GDP falls >= 5 pts in 3 years, proposed) and federal debt/GDP rising THEN long-run underweight USD vs gold/foreign assets; overweight non-US equities (VXUS/EFA). Test 1985–2025.
- Data needed: NIIP (FRED IIPUSNETIQ, 1976 annual/2006 quarterly), federal debt/GDP (FRED GFDEGDQ188S, 1966). NOT in tool.
- Confidence: medium.

### Bought puts before a crash, sold at the bottom, then lost all shorting a rally
- Source: Jim Rogers — Episode 5 (quote: "I bought a lot of puts because I thought the market was going to collapse ... I sold my puts on the day the market hit his bottom ... four or five months later I lost everything")
- Type: hedge / position sizing (caveat on shorting)
- Rule as testable logic: Puts are a good hedge ahead of predicted collapse; but after a crash, do not go short again into the rebound: IF S&P has fallen >= 25% and then rallies >= 10% off the low THEN close all shorts/puts and stop new shorts for 6 months (proposed).
- Data needed: S&P (in tool).
- Confidence: medium.

### Market can stay irrational longer than you stay solvent — shorts need limited size
- Source: interviewer, with Jim Rogers agreeing — Episode 5 (quote: "the companies all went bankrupt and I was selling them short but unfortunately ... the market went through the roof my shorts went through the roof")
- Type: position sizing/risk
- Rule as testable logic: Cap any short/inverse position (SH, PSQ, short commodity) at a small share (proposed 10–20% of NAV) and use a stop (e.g., +15% against) since being right on fundamentals does not prevent ruin.
- Data needed: none.
- Confidence: high.

### Stop-loss vs hold the pain (conflict)
- Source: Jim Rogers — Episode 5 (quote: "many people I know you stop losses you know they will say if it goes down 12% I'm out ... my pathetic answer usually is I just take the pain until I realize oh I made a bad mistake")
- Type: conflict/caveat (contradicts Law and Druckenmiller fast-loss-cutting)
- Rule as testable logic: Test fixed 12% stop-loss vs no stop (thesis-based exit) on each sleeve; Rogers uses no mechanical stop.
- Data needed: instrument prices.
- Confidence: medium.

### Know copper, wheat, oil: commodities as economic inputs
- Source: Jim Rogers — Episode 5 (quote: "if you don't know the price of copper you're going to suffer somewhere if you don't know the price of wheat you're going to suffer somewhere")
- Type: signal (general)
- Rule as testable logic: Add agricultural (wheat/grains) price change to inflation dial: IF World Bank grains index 6m change > +25% (proposed) THEN raise inflation reading; overweight DBA/commodities. (Oil and copper 6m change already in tool.)
- Data needed: World Bank grains index (1960), wheat futures (ZW=F Yahoo; WEAT 2011). NOT in tool.
- Confidence: low.

### Ignore hot tips; invest only in what you understand
- Source: Jim Rogers — Episode 5 (quote: "please ignore Hot Tips stay away from Hot Tips Hot Tips will ruin you")
- Type: conflict/caveat
- Rule as testable logic: Not testable; process rule (every position must have a documented signal/thesis).
- Data needed: none.
- Confidence: high (as advice).

---

## File 7 — Ken Tropin on Macro Hive Podcast: Markets, Risk, AI-Driven Technology (Graham Capital, 2025-12-15)

### Term premium underpriced -> curve steepener (2s10s / 5s30s)
- Source: Ken Tropin — Ken Tropin on Macro Hive Podcast (quote: "I think term premium is underpriced. And so I like the steep nerve as a general statement. Obviously you got to know when to put it on and take it off.")
- Type: action/instrument (yield curve)
- Rule as testable logic: IF ACM 10y term premium < its 20-year median (proposed) AND federal deficit > 5% GDP AND Fed in cutting cycle (funds rate down >= 0.5 pt in 12m) THEN hold curve steepener: long 2y (SHY) / short 10y–30y (TLT) duration-neutral, or overweight short Treasuries vs long; exit when 2s10s > +150 bp or term premium > its 80th pct (proposed).
- Data needed: ACM term premium (NY Fed, 1961; in tool as 12m change), 2s10s (FRED T10Y2Y, 1976; in tool), deficit (FRED MTSDS133FMS). Steepener instrument and deficit NOT in tool.
- Confidence: high (his single highest-probability macro trade).

### Large, "incurable" deficit = duration risk the market has forgotten
- Source: Ken Tropin — Macro Hive (quote: "our deficit is so extraordinarily large and so incurable from my perspective ... duration risk uh has for so many years been a non-event and a non-factor")
- Type: signal (fiscal -> rates)
- Rule as testable logic: IF deficit/GDP > 5% outside recession (unemployment < 5%) THEN structural underweight long-duration Treasuries (TLT, EDV) vs T-bills/short Treasuries; expect term premium rises over 1–2 years.
- Data needed: deficit, UNRATE, term premium (in tool).
- Confidence: high.

### Low conviction / policy fluidity -> use less risk ("stay close to home")
- Source: Ken Tropin — Macro Hive (quote: "when you don't have conviction, stay close to home")
- Type: position sizing/risk
- Rule as testable logic: IF signals conflict (proposed: dials disagree, or policy-uncertainty index > 80th pct) THEN cut active tilt sizes by 50% and stay near the strategic benchmark; full size only when several signals agree.
- Data needed: internal signal agreement; EPU (FRED USEPUINDXM).
- Confidence: high.

### Most traders using less of risk limits when disruptive policy/geopolitical events are likely
- Source: Ken Tropin — Macro Hive (quote: "most traders I know are you is using less of their risk limits than normal")
- Type: position sizing/risk
- Rule as testable logic: IF geopolitical risk index (GPR) or EPU > 80th pct THEN scale gross exposure to 50–75% of normal (proposed).
- Data needed: GPR index (Caldara-Iacoviello, 1985), EPU. NOT in tool.
- Confidence: medium.

### Most hawkish central bank -> strongest currency; all hawkish -> dollar range-bound
- Source: Ken Tropin — Macro Hive (quote: "usually in forex uh you know the the country that has the most hawkish central bank has the strongest currency but when you have an environment where everybody's a little on the hawkish side right now the dollar's in a trading range")
- Type: signal + action/instrument (FX)
- Rule as testable logic: Rank G10 currencies by 6-month change in 2y government yield (proxy for policy expectations, proposed); go long the top 2, short the bottom 2 (or long USD vs basket if US ranks top). IF dispersion of 6m 2y-yield changes across G10 < 25 bp (proposed) THEN no FX position (trading range).
- Data needed: 2y yields US/Japan/Germany/UK/Canada/Australia (FRED DGS2; OECD/central-bank series; investing.com), FX (FRED DEXUSEU, DEXJPUS, DEXUSUK, DEXCAUS, DEXUSAL), FX ETFs FXE, FXY, FXB, FXC, FXA (2005–2006), UUP (2007). NOT in tool.
- Confidence: high.

### Japan hawkish (BoJ hiking) is driving global rates
- Source: Ken Tropin — Macro Hive (quote: "Japan is the most hawkish that I can remember ... they are driving uh you know uh rates globally right now")
- Type: signal (global rates)
- Rule as testable logic: IF BoJ policy rate up >= 0.25 pt in 6m OR JGB 10y yield at a 10-year high THEN underweight long Treasuries (global term-premium spillover) and expect JPY strength / carry-unwind risk: hedge with long JPY (FXY) and lower equity beta.
- Data needed: BoJ rate, JGB 10y (FRED IRLTLT01JPM156N), USD/JPY (DEXJPUS). NOT in tool.
- Confidence: medium.

### AI equity concentration: not a bubble but expensive; correction normal (risk antenna)
- Source: Ken Tropin — Macro Hive (quote: "it's a very concentrated bet in the equity markets right ... I think AI is so for real ... but having said that it's expensive")
- Type: signal (concentration)
- Rule as testable logic: IF top-10 S&P weight > 35% (proposed) AND forward P/E of tech > 30 (proposed) THEN expect a correction (>= 10%) is likely within 12 months: hold a modest put hedge (e.g., 1% of NAV per year in 3m 10% OTM SPY/QQQ puts) rather than cutting exposure.
- Data needed: narrow leadership (in tool), CAPE (in tool); QQQ options (no free history; use CBOE index data).
- Confidence: medium.

### Markets can get away from central banks (no reliable Fed put short-term)
- Source: Ken Tropin — Macro Hive (quote: "sometimes the market can get away from any central bank and we've seen that over and over again right so in the long run the central banks usually can get their arms around problems but sometimes it doesn't happen overnight")
- Type: conflict/caveat
- Rule as testable logic: Do not assume immediate Fed support: after the Fed's first emergency action, wait for price confirmation (S&P back above 50-day / 10-month average, proposed) before re-entering.
- Data needed: S&P.
- Confidence: medium.

### Tariffs are a consumer tax, passed through (inflation persistence)
- Source: Ken Tropin — Macro Hive (quote: "if you buy something from Europe ... whether you're paying the 15% tariff or 20% tariff, companies are passing that on. Car manufacturers are passing that on.")
- Type: signal (inflation) — contrasts with Liesman (File 3) "sucking up tariffs in margin"
- Rule as testable logic: IF effective tariff rate up >= 5 pts THEN expect core goods CPI 6m annualised > 3% within 12 months; hedge with TIPS, avoid long nominal bonds.
- Data needed: customs duties, core goods CPI (FRED CUSR0000SACL1E). NOT in tool.
- Confidence: medium.

### Two-thirds of the economy ex-AI slowing (deflationary offset)
- Source: Ken Tropin — Macro Hive (quote: "you've got twothirds of the economy slowing outside of AI, right? So, that's slightly deflationary")
- Type: signal (same K-shape concept as Eisman, File 3)
- Rule as testable logic: See "GDP ex-AI capex" rule; agreement across two speakers.
- Data needed: as File 3.
- Confidence: medium.

### Private credit: liquidity shock -> redemptions suspended (gating risk)
- Source: Ken Tropin — Macro Hive (quote: "when there's a liquidity shock all bets are off right ... even well-managed funds can all of a sudden have to you know uh suspend redemptions")
- Type: signal (credit/liquidity)
- Rule as testable logic: IF BDC index (BIZD, 2013) falls >= 15% in 3 months OR trades at >= 20% discount to NAV (proposed) THEN credit stress: underweight HY/leveraged loans (BKLN, 2011), cut equity one notch.
- Data needed: BIZD, BKLN, HY OAS. NOT in tool.
- Confidence: medium.

### Pre-midterm fiscal stimulus pressure (US politics -> rates)
- Source: Ken Tropin — Macro Hive (quote: "there's going to be an enormous pressure on the new chair to to really stimulate the economy")
- Type: regime map (political cycle)
- Rule as testable logic: Test presidential/midterm cycle: IF year before midterm/presidential election AND deficit widening THEN steeper curve, weaker long bonds; also test S&P midterm-year seasonality (Q4 of midterm year strong, proposed).
- Data needed: election calendar; S&P from 1928; 10y.
- Confidence: low.

### Geopolitics: US–China need each other (Taiwan tail risk); Russia–Ukraine not easily solved
- Source: Ken Tropin — Macro Hive (quote: "there's always going to be that risk of something in Taiwan ... but we need each other too badly uh you know uh for things to get too ugly")
- Type: regime map (geopolitics -> asset) — contrasts with Gurley (File 1) on escalation risk
- Rule as testable logic: Keep a small tail hedge vs Taiwan escalation (e.g., underweight EWT/SMH, long gold) rather than a large position; Russia/Ukraine: persistent European energy risk premium -> keep European equity (VGK) underweight when natural gas (TTF) > 2x 5y average (proposed).
- Data needed: GPR index; TTF gas (World Bank Pink Sheet Europe natural gas, 1960 monthly); VGK (2005). NOT in tool.
- Confidence: low.

### Be tactical, low risk in policy-fluid environments
- Source: Ken Tropin — Macro Hive (quote: "our traders have have uh done very well by being very tactical, opportunistic and not having really high levels of risk")
- Type: position sizing/risk
- Rule as testable logic: In high-uncertainty regimes use shorter holding periods (proposed: 1-month re-evaluation instead of 3–6) and smaller sizes.
- Data needed: EPU.
- Confidence: medium.

---

## File 8 — Why This Market "Melt-Up" is Making Me Nervous (Steve Eisman, The Weekly Wrap, 2026-05-15)

### Rally speed: from -4% YTD to +9% in ~6 weeks = froth
- Source: Steve Eisman — Why This Market "Melt-Up" is Making Me Nervous (quote: "At its bottom at the end of March, the S&P was down 4% and Nasdaq was down 7% for the year. The market is now up 9% and Nasdaq is up 15%. It's feeling frothy.")
- Type: signal (rally speed / froth)
- Rule as testable logic: IF S&P rises >= 12% (Nasdaq >= 20%) within 8 weeks from a low (proposed) AND other froth signals (below) present THEN lighten high-beta/growth exposure (cut QQQ/semis overweight by half) for 3 months. (Rally speed is in tool; adds instrument choice.)
- Data needed: ^GSPC, ^NDX. Rally speed in tool.
- Confidence: medium.

### Semis share of S&P > 18% (from 14%) = concentration froth
- Source: Steve Eisman — Melt-Up (quote: "The semiconductor sector is now over 18% of the S&P. It was 14% at the start of 2026. Nvidia is now larger than the entire healthcare sector.")
- Type: signal (sector concentration)
- Rule as testable logic: IF a single sector's S&P weight rises >= 4 pts within 6 months OR exceeds its prior all-time high share (proposed) THEN underweight that sector vs market over next 12 months (test: tech 2000, energy 1980/2008, financials 2007).
- Data needed: S&P sector weights (S&P Dow Jones factsheets, monthly; free history limited; proxy: sector ETF market cap or Ken French 12-industry value-weighted market caps, 1926). NOT in tool (narrow leadership is).
- Confidence: medium.

### Defensive sectors' share of S&P collapsing (19% vs 31%)
- Source: Steve Eisman — Melt-Up (quote: "The sum of the four defensive sectors, healthcare, consumer staples, energy, and utilities represents only 19% of the S&P 500. That number was 31% at the end of 2022.")
- Type: signal (froth / contrarian)
- Rule as testable logic: IF combined weight of healthcare+staples+energy+utilities in S&P < 20% (proposed) or falls >= 8 pts in 3 years THEN overweight defensives (XLV, XLP, XLE, XLU equal-weight basket) vs S&P for 12–24 months (mean reversion).
- Data needed: sector weights (Ken French industry portfolios market cap 1926 as proxy). NOT in tool (cyclical vs defensive 6m is).
- Confidence: medium.

### Retail call buying at 2021 highs = euphoria
- Source: Steve Eisman — Melt-Up (quote: "Retail traders are buying calls in Cboe's Mag 10 stocks ... at the heaviest 10-day clip since 2021 ... 52% were call buying and 17% were call selling.")
- Type: signal (sentiment, contrarian)
- Rule as testable logic: IF equity put/call ratio (10-day average) falls to bottom 5% of 3-year range (proposed) OR retail call volume share at 3y high THEN reduce equity/high-beta exposure for 1–3 months; buy cheap SPY/QQQ puts as hedge.
- Data needed: CBOE equity put/call ratio (CBOE daily, 2003; total P/C 1995), AAII sentiment (1987, weekly). NOT in tool.
- Confidence: medium.

### Market assumes geopolitical risk is over (war) — caveat
- Source: Steve Eisman — Melt-Up (quote: "part of the rally is an assumption by the market that the war is over. And I'm just not sure that is right.")
- Type: conflict/caveat (geopolitics)
- Rule as testable logic: IF oil remains > 30% above its pre-war level (proposed) while S&P makes new highs (equity pricing peace, oil not) THEN keep energy (XLE) / oil (USO) hedge and lighten equities.
- Data needed: WTI/Brent (FRED DCOILBRENTEU, 1987), S&P.
- Confidence: low.

### Lighten high flyers on froth, without a recession call
- Source: Steve Eisman — Melt-Up (quote: "I am not calling for a recession because there is no evidence that there is one on the horizon ... This week, I lightened up, especially on my high flyers")
- Type: position sizing/risk
- Rule as testable logic: Separate froth signals (rally speed, concentration, call buying) from recession signals: froth -> trim high-beta (QQQ, SMH, ARKK) by a fraction (proposed 25–50%) but keep core S&P; recession signals -> cut S&P. Test whether froth-only trims improve risk-adjusted return.
- Data needed: as above.
- Confidence: medium.

### PPI surge (1.4% m/m, 6% y/y) = inflation rearing its head
- Source: Steve Eisman — Melt-Up (quote: "the producer price index rose a seasonally adjusted 1.4% for the month ... On an annual basis, the index was up 6%, the biggest gain since December 2022")
- Type: signal (inflation)
- Rule as testable logic: IF PPI final demand m/m >= 1.0% OR y/y >= 5% (proposed) THEN raise inflation dial; underweight long Treasuries, overweight TIPS/commodities over 6 months. (PPI y/y in tool; adds m/m surprise.)
- Data needed: PPI final demand (FRED PPIFIS, 2009; PPIACO 1913). In tool (y/y).
- Confidence: medium.

### 10-year at 4.5% = "Rubicon" for equities
- Source: Steve Eisman — Melt-Up (quote: "The 10-year yield is now flirting with 4 and 1/2%, which in the past has been a Rubicon for markets.")
- Type: signal (rates threshold)
- Rule as testable logic: IF 10y yield crosses above 4.5% (2023–26 regime; generalise as: 10y above its 3-year high, proposed) THEN expect equity multiple pressure: underweight long-duration equities (growth, small caps, homebuilders) for 3 months.
- Data needed: DGS10 (in tool as 12m change, level threshold NOT).
- Confidence: low (regime-specific level).

### Credit lines cut to a lender = really bad (private credit stress)
- Source: Steve Eisman — Melt-Up (quote: "When a financial services company has its credit lines cut, that is always really, really bad.")
- Type: signal (credit)
- Rule as testable logic: IF BDC index (BIZD) underperforms HY bonds (HYG) by >= 10% over 6 months (proposed; proxy for lender stress / bank line cuts) THEN credit cycle turning: underweight HY/leveraged loans and financials; add to warnings.
- Data needed: BIZD (2013), HYG (2007); Cliffwater Direct Lending Index (quarterly, 2004, free summary). NOT in tool.
- Confidence: medium.

### Private credit marks: >1/10 of loans marked down >= 50%
- Source: Steve Eisman citing MSCI — Melt-Up (quote: "private credit funds have marked down more than 1/10 of their loans by at least 50%")
- Type: signal (credit cycle)
- Rule as testable logic: First credit cycle since GFC is in private credit: IF private-credit distress (proxy BDC non-accruals rising / BIZD drawdown >= 20%) THEN expect "losses and perhaps a recession, but not a total disaster" because banks well capitalised: modest equity cut (one notch), no bank short.
- Data needed: BIZD; bank capital (FRED, Tier-1 ratios). NOT in tool.
- Confidence: medium.

### Banks well capitalised -> private credit losses will not be GFC-scale (caveat)
- Source: Steve Eisman — Melt-Up (quote: "why this is a difficult situation, but will probably not cause the same level of chaos because the banks are in fact well capitalized. There will be losses and perhaps a recession, but not a total disaster.")
- Type: conflict/caveat (severity)
- Rule as testable logic: Scale de-risking by bank health: IF bank stocks vs market not falling (in tool) during a credit-spread warning THEN cap equity cut at 50% rather than 100%.
- Data needed: bank stocks vs market (in tool).
- Confidence: medium.

### Homebuilder below tangible book while growing book usually works — but wait while long rates rise
- Source: Steve Eisman — Melt-Up (quote: "buying a home builder below tangible book value ... when the builder is growing book value, usually works out. It's just a question of time. But right now with long-term rates going up, I will have to continue to wait.")
- Type: signal + re-entry (sector)
- Rule as testable logic: IF homebuilder ETF (ITB/XHB) price-to-book < 1.2 (proposed proxy) THEN accumulate homebuilders, but only after 10y yield / mortgage rate 3m change turns negative (re-entry trigger).
- Data needed: ITB (2006), XHB (2006); mortgage rate (in tool); sector P/B (no free series; proxy: Ken French B/M for construction industry). Homebuilders vs market in tool.
- Confidence: medium.

### Travel guidance cuts on geopolitical uncertainty
- Source: Steve Eisman — Melt-Up (quote: "Airlines and bookings have all cut guidance ... the company forecast weak bookings for the second quarter because of geopolitical uncertainty")
- Type: signal (sector, geopolitics -> asset)
- Rule as testable logic: IF oil price spike >= 30% in 3 months on war (proposed) THEN underweight airlines/travel (JETS, 2015; PEJ 2005) vs market for 6 months; overweight energy.
- Data needed: JETS, PEJ, Brent.
- Confidence: low.

---

## File 9 — Graham Capital Management's Tropin on Why Macro is Killing It (Bloomberg Live, 2022-10-12)

### Central-bank activity = macro opportunity (FX and equity volatility)
- Source: Ken Tropin — Graham Capital Management's Tropin on Why Macro is Killing It (quote: "Central Bank movement is going to equate to FX volatility it's very often going to equate to equity volatility")
- Type: regime map / position sizing
- Rule as testable logic: IF count of 25bp-equivalent policy moves across Fed+ECB+BoE (and BoJ) over trailing 12 months >= 10 (proposed) THEN expect high cross-asset trend returns: raise allocation to trend/macro sleeves (cross-asset time-series momentum in bonds, FX, commodities) and cut static equity beta; IF policy on hold (count <= 2) THEN favour static equity beta.
- Data needed: policy rates FEDFUNDS / FRED ECBDFR / BoE Bank Rate (FRED BOERUKM, or BoE database 1694) / BoJ; SG CTA index or AQR TSMOM (1985) as validation. NOT in tool.
- Confidence: high.

### Policy divergence (US hiking, Japan pinned) -> long USD/JPY; watch for band release
- Source: Ken Tropin — Why Macro is Killing It (quote: "Japan's not raising rates they're they're holding their upper band at 25 basis points ... if they were to release that band there'd be a lot of opportunity on the downside in dollar Yen")
- Type: signal + action/instrument (FX)
- Rule as testable logic: IF Fed funds 12m change - BoJ rate 12m change > +2 pts (proposed) THEN long USD vs JPY (short FXY / long UUP); EXIT/REVERSE when BoJ loosens yield cap or hikes, or after Japanese MoF intervention (USD/JPY falls >= 3% in a day).
- Data needed: FEDFUNDS, BoJ policy rate (FRED IRSTCI01JPM156N), USD/JPY (DEXJPUS, 1971), FXY (2007). NOT in tool.
- Confidence: high.

### Long dollar in a synchronized tightening led by the Fed; crowded -> cautious
- Source: Ken Tropin — Why Macro is Killing It (quote: "the dollar has been at profitable trade it's a crowded trade too ... it's definitely expensive uh and I think the path of least resistance is the dollar goes a little higher but we're pretty cautious")
- Type: position sizing/risk (FX)
- Rule as testable logic: Long USD while Fed most hawkish (see File 7 FX rule); reduce size by half when USD is expensive (real broad dollar > 90th pct of 30y, proposed) or CFTC net long USD positioning > 80th pct.
- Data needed: real broad dollar (FRED RTWEXBGS, 2006; RBUSBIS BIS real effective, 1994), CFTC COT (1986). Dollar vs 12m high and 12m change in tool; valuation/positioning NOT.
- Confidence: medium.

### Short bonds across durations/geographies in an inflation-hiking regime
- Source: Ken Tropin — Why Macro is Killing It (quote: "in fixed income we've done quite well uh you know being short bonds of various durations and various different uh geographies")
- Type: action/instrument
- Rule as testable logic: IF core CPI y/y > 4% AND rising (3m annualised > 12m) AND central banks hiking THEN short/underweight government bonds (US IEF/TLT, Bunds, gilts) across maturities; hold T-bills. (Tool currently switches to T-bills; adds explicit short.)
- Data needed: core CPI (in tool), FEDFUNDS; IEF, TLT, BWX (international Treasuries, 2007).
- Confidence: high.

### Energy most profitable commodity in supply-driven inflation
- Source: Ken Tropin — Why Macro is Killing It (quote: "in energy it's been a you know over the commodity sector that's been the most probable for us")
- Type: action/instrument (commodity)
- Rule as testable logic: IF headline inflation driven by energy (energy CPI y/y > 20%, proposed) AND OPEC+ cutting supply THEN long energy futures/ETF (USO, DBE, XLE) with trend confirmation (price above 10m average).
- Data needed: energy CPI (FRED CPIENGSL, 1957), WTI, DBE (2007), XLE. Energy CPI NOT in tool (oil 6m change is).
- Confidence: medium.

### Inflation takes years to kill; Fed easing too early -> re-hike (Volcker lesson)
- Source: Ken Tropin — Why Macro is Killing It (quote: "if I recall correctly the Central Bank started easing because they thought they had it under control and then they had to raise rates again")
- Type: regime map (inflation) — agrees with Druckenmiller File 5
- Rule as testable logic: IF Fed starts easing within 18 months of core CPI peak > 5% AND core still > 3% THEN expect inflation rebound; stay underweight long duration, overweight commodities/TIPS. Market pricing of early cuts should be faded (sell SHY / short-rate futures when market prices >= 4 cuts within 12 months while core > 3%, proposed).
- Data needed: core CPI, FEDFUNDS, 2y yield minus Fed funds as proxy for cut pricing (DGS2 - FEDFUNDS).
- Confidence: high.

### Inflation sticky: back to 2% only years later
- Source: Ken Tropin — Why Macro is Killing It (quote: "I think inflation will come down for sure next year but I don't think we're getting anywhere close to a target of two percent I think I think it may be 2025 before we get to Target if then")
- Type: signal (inflation persistence)
- Rule as testable logic: IF core CPI peaked > 6% THEN assume >= 3 years to return to 2.5%; inflation dial stays "hot" until core 12m < 3% for 6 months (proposed).
- Data needed: core CPI (in tool).
- Confidence: medium.

### Supply-side inflation (energy, supply chains) is outside Fed control
- Source: Ken Tropin — Why Macro is Killing It (quote: "the supply chain disruption the FED really can't manage that right and so the FED really can't manage what energy prices are")
- Type: signal
- Rule as testable logic: IF NY Fed Global Supply Chain Pressure Index > 1.5 sd (proposed) THEN goods inflation persists 6–12 months: overweight commodities, TIPS; underweight nominal bonds.
- Data needed: NY Fed GSCPI (monthly, 1997, free). NOT in tool.
- Confidence: medium.

### Tight labor market / workers never saw a recession -> wage inflation sticky
- Source: Ken Tropin — Why Macro is Killing It (quote: "the inflation problem in the United States is partially Supply driven but partially driven by higher labor")
- Type: signal (wage inflation)
- Rule as testable logic: IF Atlanta Fed wage growth tracker > 5% (proposed) OR job openings / unemployed > 1.5 THEN inflation sticky: same tilt as above.
- Data needed: Atlanta Fed Wage Growth Tracker (1997), JOLTS openings (FRED JTSJOL, 2000) / UNEMPLOY. NOT in tool.
- Confidence: medium.

### Re-anchor inflation expectations even at cost of recession (Summers camp) -> recession follows
- Source: Ken Tropin — Why Macro is Killing It (quote: "it's going to be uh painful from for the economy Powell's conceded that uh I think that's another way of saying we're going to have a recession")
- Type: regime map
- Rule as testable logic: IF Fed funds rises >= 3 pts in 12 months (proposed) THEN recession probability over 24 months high: plan shift from short-bonds to long-bonds once unemployment starts rising (Sahm trigger, in tool).
- Data needed: FEDFUNDS 12m change (in tool), Sahm (in tool).
- Confidence: medium.

### Duration risk premium missing -> 10y should be 50–100 bp higher; curve re-steepens
- Source: Ken Tropin — Why Macro is Killing It (quote: "most of them there were something called duration risk for being in longer dated bonds and that's completely missing at the moment ... it should get steeper")
- Type: signal + action/instrument (curve)
- Rule as testable logic: IF 2s10s inverted AND inflation expected > 3% for several years AND term premium < 0 THEN short 10y–20y (TLT) and position for re-steepening (long 2y vs short 10y) over 12–24 months.
- Data needed: T10Y2Y (in tool), ACM term premium (in tool), DGS10.
- Confidence: high (same view three years later in File 7).

### Equities in a trading range for years after a 12-year straight rise
- Source: Ken Tropin — Why Macro is Killing It (quote: "a straight shot up in equity prices for 12 years and now we're getting a more normal Market where you know they go up they go down and we may be in a trading range for equities for some number of years")
- Type: regime map
- Rule as testable logic: IF inflation regime "hot" (core > 3%) after a decade of low inflation THEN expect lower equity trend persistence: favour mean-reversion (buy S&P at -15% from high, trim at new highs) over trend; prefer diversified macro (trend in bonds/FX/commodities). Test 1966–1982 analogue.
- Data needed: S&P (1871 Shiller), CPI.
- Confidence: medium.

### Trade only liquid markets; exit early and cheaply
- Source: Ken Tropin — Why Macro is Killing It (quote: "I want to always be the the guy who gets out of the market sooner than later not later at greater expense")
- Type: position sizing/risk
- Rule as testable logic: Restrict instruments to liquid ETFs/futures (proposed: average daily value traded > $50m); exit on first signal deterioration rather than waiting for confirmation.
- Data needed: ETF volume.
- Confidence: high.

### Fast discretionary vs slow systematic horizons
- Source: Ken Tropin — Why Macro is Killing It (quote: "our quantitative systems are somewhat longer term in nature they would tend to move around say over a period of weeks and months")
- Type: action/instrument (trend horizon)
- Rule as testable logic: Trend sleeve signals on weeks-to-months lookbacks (proposed: blend 1m, 3m, 12m momentum) across liquid futures-like ETFs.
- Data needed: ETF prices.
- Confidence: medium.

### Gold failed as an inflation hedge in a rate-hiking year; quant models short gold
- Source: Ken Tropin — Why Macro is Killing It (quote: "if there was ever a year people wanted gold to perform and uh you know be an inflation hedge it's down ... our quantitative models have tended to be shorted")
- Type: conflict/caveat (gold vs real rates) — contrasts with Rogers/Druckenmiller gold-as-debasement-hedge
- Rule as testable logic: IF real 10y yield rising >= 1 pt in 12 months (in tool) AND dollar rising THEN underweight/short gold (GLD) regardless of inflation; gold only as hedge when real yields falling or dollar falling. Trend filter: hold gold only above its 10-month average.
- Data needed: real 10y (FRED DFII10, 2003; in tool), gold (GLD 2004; LBMA via FRED discontinued; Yahoo GC=F 2000; World Bank gold monthly 1960).
- Confidence: high.

### Green energy transition = less energy today = longer inflation
- Source: Ken Tropin — Why Macro is Killing It (quote: "our energy policies are green ... however that comes at a cost of not having a lot of energy to use today")
- Type: regime map (commodity supply)
- Rule as testable logic: IF oil & gas capex (proxy: rig count) stays >= 40% below prior peak while demand recovers (oil inventories below 5y average, proposed) THEN structural overweight energy (XLE) and oil over 2–3 years.
- Data needed: Baker Hughes rig count, EIA crude inventories (weekly, 1982). NOT in tool.
- Confidence: medium.

### OPEC cuts -> oil back up -> inflationary
- Source: Ken Tropin — Why Macro is Killing It (quote: "with Saudi Arabia essentially sort of flipping us off a week or two ago right um you know Energy's back ... that's pretty inflationary")
- Type: signal (geopolitics -> oil -> inflation)
- Rule as testable logic: IF OPEC+ announces production cut >= 1 mb/d (event, proposed) THEN long oil (USO/BNO) for 3 months and raise inflation dial.
- Data needed: OPEC decision dates (manual), Brent.
- Confidence: low.

### Europe: supply-side energy inflation (power prices hundreds of % higher)
- Source: Ken Tropin — Why Macro is Killing It (quote: "the cost of power in Europe ... hundreds of percent higher than the previous year so they have a very dramatic uh inflation problem that's very supply side driven")
- Type: signal (country)
- Rule as testable logic: IF European natural gas (TTF) y/y > +100% (proposed) THEN underweight European equities (VGK/EZU) and EUR vs USD; overweight US.
- Data needed: World Bank Europe natural gas price (monthly, 1960), VGK, EZU (2000), EUR/USD. NOT in tool.
- Confidence: medium.

### Sterling after a big move: neutral (avoid chasing extremes)
- Source: Ken Tropin — Why Macro is Killing It (quote: "it's already made a big move so I don't know how much weaker it really gets ... I would be kind of neutral at these levels")
- Type: re-entry/exit (FX)
- Rule as testable logic: IF a currency has moved >= 15% in 12 months (proposed) THEN cut trend position to neutral/half (take profits after extreme moves).
- Data needed: GBP/USD (FRED DEXUSUK, 1971).
- Confidence: low.

### Macro/trend as diversifier; beta rewarded only in low-inflation, on-hold regimes
- Source: Ken Tropin — Why Macro is Killing It (quote: "our investors had the luxury in the previous decade of being very heavily weighted towards beta and you got rewarded for that it was as benign and environment probate as you could possibly want with inflation close to zero and Central Bank policy on hold")
- Type: regime map
- Rule as testable logic: IF core CPI < 2.5% AND Fed on hold (|Fed funds 12m change| < 0.5 pt) THEN max equity beta; ELSE allocate a share (proposed 25–50%) to cross-asset trend sleeve. Test stock-bond 60/40 vs 60/40 + trend by regime.
- Data needed: core CPI, FEDFUNDS (in tool); trend sleeve prices.
- Confidence: high.

### Crypto: tiny positions only (outside expertise)
- Source: Ken Tropin — Why Macro is Killing It (quote: "our Traders can trade it our trading systems can trade it our positions there are very very very small")
- Type: position sizing/risk
- Rule as testable logic: If crypto included (IBIT/BTC trend), cap at <= 2% of NAV (proposed) and trade only with trend filter.
- Data needed: BTC-USD (Yahoo, 2014).
- Confidence: low.

---

## Cross-speaker conflicts and agreements (batch 7)

- **Tariff pass-through:** Tropin (File 7): companies pass tariffs on ("tax on consumers"). Liesman (File 3): companies "sucking up tariffs in margin", effective rate only ~half of statutory and may stay there; Gerstner (File 1) cites Fed study showing umbrella price rises. Test: effective tariff change vs core goods CPI and vs S&P margins.
- **Stop-losses:** Andrew Law and Druckenmiller (sell losers fast, thesis-based exits) vs Jim Rogers ("I just take the pain until I realize oh I made a bad mistake"; no mechanical 12% stop).
- **Gold:** Rogers / Druckenmiller (debasement, central-bank trust erosion, gold at highs as sign of loose conditions) vs Tropin 2022 (gold "ineffective as a hedge" during hiking; quant models short). Resolution to test: gold conditional on real yields and dollar trend.
- **US–China geopolitics:** Gurley (pushing China raises Taiwan-invasion odds) vs Tropin ("we need each other too badly ... for things to get too ugly").
- **AI bubble:** Eisman (froth: semis 18% of S&P, defensives 19%, call buying; lightened high flyers) and Liesman ("fervor") vs Tropin ("I don't think this is some imaginary bubble ... but it's expensive") and Druckenmiller 2024 (neither long nor short; narrow leadership only a yellow light). Gerstner: fundamentals "on fire", but uncertainty -> lower multiples.
- **Algos and price signals:** Druckenmiller 2018 (algos destroyed group-rotation signals) vs Law (systematic + human best; 2016 election showed machines wrong). Validation test: split-sample decay of the tool's intra-market signals.
- **Agreement — inflation second wave / early Fed easing:** Druckenmiller 2024 (1970s double hump, short bonds the day the Fed cut), Tropin 2022 (Volcker-era easing too early then re-hike) and Liesman (Volcker would not cut at 3%).
- **Agreement — term premium / long-end short:** Druckenmiller (10y can go to nominal GDP; fiscal 7% deficit at full employment), Tropin 2022 and 2025 (duration risk missing; steepener), Gerstner (bond vigilantes / credible deficit cut would lower rates).
- **Agreement — oil+dollar+rates squeeze:** Druckenmiller twice (2018 and 2024 accounts of 2000; Hyman regression 50/25/25).

---

## Batch summary — 10 most important testable ideas

1. **Oil + dollar + rates squeeze with explicit weights and instrument** (Druckenmiller/Hyman): composite = 50% dollar 12m change, 25% oil, 25% rates; when extreme, cut equities and buy 2y–5y (then 10y) Treasuries; predicts next-12m S&P EPS falls. Tool has the squeeze; add the weights and the Treasury long.
2. **Fed easing into loose financial conditions -> short long bonds / inflation second wave** (Druckenmiller 2024, Tropin 2022, Liesman): first cut with tight credit spreads, gold at highs, stocks near highs, core > 2.5% -> underweight TLT, overweight TIPS/commodities; 10y target = nominal GDP growth.
3. **Term premium underpriced + large deficit at full employment -> curve steepener** (Tropin 2022/2025, Druckenmiller): deficit > 5% GDP with unemployment < 5% and low term premium -> long 2y / short 10–30y, or T-bills over TLT. Needs deficit series.
4. **Global central-bank balance-sheet flow (Fed+ECB+BoJ) as an equity liquidity signal** (Druckenmiller 2018): a 12-month swing of about −$1tn in G3 CB purchases -> underweight equities and EM; EM stress is the first domino.
5. **Policy-divergence FX rule** (Tropin 2022/2025, Druckenmiller): long the currency of the most hawkish central bank (rank by 6m change in 2y yields); USD/JPY long when Fed−BoJ divergence is wide, exit when BoJ turns hawkish; no FX position when everyone is equally hawkish.
6. **EM "lottery ticket" after tightening-driven collapse** (Druckenmiller): small EWZ/EZA (or BRL/ZAR) position after a >= 40% USD drawdown with positive carry; stay out while the Fed keeps tightening and EM currency crises spread.
7. **Cross-asset trend sleeve with regime-dependent weight** (Law, Tropin, Druckenmiller "five buckets"): weeks-to-months time-series momentum in bonds, FX, commodities and equity indexes; give it more weight when central banks move a lot or inflation is > 2.5%, and when the tool cuts stocks (bear-market regime), instead of only holding cash.
8. **Narrow leadership as a necessary AND-gate (yellow light), plus froth set** (Druckenmiller, Eisman): use narrowing breadth as a precondition, not a trigger. Froth signals (rally speed, sector weight >= 4 pts higher in 6m, defensive share < 20%, call buying at a 3y high) -> trim high-beta (QQQ/SMH) only, not core S&P.
9. **Commodity/cyclical contrarian with capacity cuts** (Druckenmiller "18–24 months out", Rogers "buy the disaster the world needs"): commodity or sector index >= 50% below its 5–10y high and capacity cut (rig count −40% y/y) -> buy (XLE/XOP/DBA/XME) once price is back above its 10m average; hold 18–36 months.
10. **Position sizing package**: start at 1/3 size and add on price confirmation ("invest then investigate"); halve tilts after a 10% drawdown or in a cold streak; stay close to benchmark when signals conflict or policy uncertainty (EPU/GPR) is > 80th pct; size up only in liquid instruments and on asymmetric "one-way bets"; cap shorts/inverse at 10–20% NAV; stop new shorts after a 25% crash plus a 10% rebound.

Also notable: gold held only when real yields are falling or the dollar is weak (Tropin vs Rogers); after a currency peg breaks, buy that country's bonds and stocks (UK 1992); auto-loan delinquencies as a consumer canary; BDC/private-credit stress (BIZD vs HYG) as a credit-cycle warning, with the size of the cut scaled by bank health; funding-stress spike -> policy reversal -> re-entry.

---

## Data requests (series not in the existing tool list)

Liquidity / central banks
- ECB total assets (FRED ECBASSETSW, 1999); BoJ total assets (FRED JPNASSETS, 1998); Fed total assets level (FRED WALCL) for the G3 combined 12m flow
- ECB deposit rate (FRED ECBDFR); BoJ policy rate (FRED IRSTCI01JPM156N); BoE Bank Rate (BoE database / FRED BOERUKM); count of G3/G4 policy moves
- Chicago Fed NFCI (FRED NFCI, 1971)
- SOFR (FRED SOFR, 2018), IORB/IOER, TED spread (FRED TEDRATE 1986–2022)

Rates / fiscal
- Federal surplus/deficit monthly (FRED MTSDS133FMS, 1980) and % GDP (FRED FYFSGDA188S); federal debt/GDP (FRED GFDEGDQ188S)
- 2y and 5y Treasury yields (FRED DGS2, DGS5); 2y minus Fed funds (market-implied cuts proxy)
- Japan 10y (FRED IRLTLT01JPM156N); UK/Germany/other 10y (FRED IRLTLT01xxM156N); G10 2y yields (OECD / central banks)
- Treasury auction results / tails (TreasuryDirect)
- US net international investment position (FRED IIPUSNETIQ)
- Average outstanding mortgage rate vs marginal (BEA mortgage interest / mortgage debt)

Credit
- ICE BofA HY OAS level and percentile (FRED BAMLH0A0HYM2, 1996)
- Fed SLOOS lending standards (FRED DRTSCILM, 1990)
- Nonfinancial corporate debt/GDP (FRED NCBDBIQ027S); total credit/GDP (FRED TCMDO; BIS)
- BDC index BIZD (2013), leveraged loans BKLN (2011), Cliffwater Direct Lending Index
- Auto-loan delinquency (NY Fed HHDC 2003; FRED DRCLACBS 1987); student-loan delinquency (NY Fed)

Inflation / labour / activity
- Core PCE (FRED PCEPILFE); core goods CPI (FRED CUSR0000SACL1E); energy CPI (FRED CPIENGSL)
- NY Fed Global Supply Chain Pressure Index (1997)
- Atlanta Fed Wage Growth Tracker (1997); JOLTS openings (FRED JTSJOL) / unemployed (FRED UNEMPLOY)
- Weekly initial jobless claims (FRED ICSA, 1967)
- NFIB Small Business Optimism (1974/1986); Philly Fed current and future activity (1968); ISM PMI
- Corporate profits/GDP (FRED CP / GDP); nonfarm productivity (FRED OPHNFB)
- GDP ex information-processing equipment and software investment (FRED A679RX1Q020SBEA, B985RC1Q027SBEA, GDPC1)
- Effective tariff rate: customs duties (FRED B235RC1Q027SBEA) / goods imports; Yale Budget Lab statutory rate

Uncertainty / geopolitics / sentiment
- Economic Policy Uncertainty (FRED USEPUINDXM/USEPUINDXD, 1985); Trade Policy Uncertainty (policyuncertainty.com)
- Caldara-Iacoviello Geopolitical Risk index, with country sub-indexes (1985)
- CBOE equity put/call ratio (2003); AAII sentiment (1987); CFTC COT positioning for USD/JPY/EUR (1986)
- Central-bank gold purchases (World Gold Council)

Markets / instruments
- EM: EEM (2003) / MSCI EM (1988); EWZ, EZA, EWT, EWU, FXI/MCHI, KWEB, FM (frontier), CEW (EM FX); EMB
- FX: broad dollar (FRED DTWEXBGS/TWEXB), real broad dollar (FRED RTWEXBGS; BIS), EUR/USD, USD/JPY, GBP/USD, BRL, ZAR, TRY, CNY (FRED DEX*); UUP, FXE, FXY, FXB, FXC, FXA
- Commodities: gold (GLD, GC=F, World Bank monthly 1960); World Bank Pink Sheet agriculture/grains/energy/metals indexes (1960); BCOM/GSCI sub-indexes; DBA, DBC, DBE, USO, BNO; Europe natural gas (World Bank / TTF); Baker Hughes rig count (1987); EIA crude inventories; uranium URA; copper miners COPX
- Equity sectors/factors: sector weights in the S&P (S&P DJI; Ken French industry market caps as proxy); RSP vs SPY; QUAL / Ken French RMW; SOXX/SMH; XLE/XOP/XME; ITB/XHB; JETS/PEJ; XLU; VGK/EZU; IWM / Russell 2000; ^NDX/QQQ
- Treasuries/hedges: SHY, IEI, IEF, TLT, EDV, TIP, TBF/TBT, BWX; SPY/QQQ put proxies (CBOE PPUT, VXTH); SG CTA / AQR TSMOM index for trend validation
- Crypto: BTC-USD (2014), IBIT
