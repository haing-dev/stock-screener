# Batch 6 — testable macro rules

Files read in full (9): Petraeus (Money Maze, 2023-01); BG2 Gurley & Gerstner on tariffs (2025-04); Scott Bessent (Capital Allocators, 2024-11); Krishna Guha (Real Eisman Playbook Ep 78); Geoffrey Garrett (NBIM In Good Company); Ken Tropin (Macro Hive); Druckenmiller on AI; Druckenmiller "Invest, then investigate"; "A Brief World Economic History for Gold, Silver and Fiat Money".

Note on quotes: transcripts are auto-captions; quotes are verbatim from the caption text (caption spelling errors kept, e.g. "Navaro", "Bessant").

---

## File 1 — General David Petraeus — "The War in Ukraine, Relations With China & Wider Geopolitics" (Money Maze, 2023-01-19)

Mostly geopolitical commentary; few direct market rules. Extracted what can be mapped to assets.

### Commodity-producer resilience to sanctions (Russia)
- Source: David Petraeus — The War in Ukraine, Relations With China & Wider Geopolitics (quote: "Russia is sent from Central Casting when it comes to resisting sanctions because they have you know they're one of the top three gas oil and coal producers")
- Type: conflict/caveat
- Rule as testable logic: IF a major commodity exporter is put under broad Western sanctions THEN do not expect a rapid GDP collapse (he estimates ~5% not 10% in year 1); commodity prices (energy/coal/grains) stay elevated while the world still needs its supply. Test: energy (XLE/USO, DBC) 12m return after sanction events (Iran 2012, Russia 2014, Russia 2022) vs unconditional (proposed: overweight energy 6m after a G7 sanction event on a top-3 producer).
- Data needed: event dates (manual list); WTI (FRED DCOILWTICO, 1986), Brent (FRED DCOILBRENTEU, 1987), natural gas (FRED DHHNGSP, 1997), coal (World Bank Pink Sheet, 1960). Oil 6m change is in the tool; event flags are not.
- Confidence: low (descriptive, not an investment rule).

### Dollar weaponisation does not displace the dollar
- Source: David Petraeus — same file (quote: "there's no sign I don't think of true displacement of the dollar as the currency through which much of trade uh is done")
- Type: conflict/caveat
- Rule as testable logic: IF the US freezes a sovereign's reserves (e.g., Russia Feb-2022) THEN do NOT assume a dollar bear market; expect only a "tactical shift" into other currencies/gold. Test: DXY 12m change after asset-freeze events vs gold/USD 12m change (gold reserve accumulation is the channel Bessent cites, see File 3). Contrasts with the "debasement/de-dollarisation -> gold" thesis in File 9 and Bessent's gold view.
- Data needed: broad dollar (FRED DTWEXBGS 2006; DTWEXM 1973-2019), gold (LBMA via FRED was discontinued; use Yahoo GC=F 2000 / GLD 2004, or World Bank Pink Sheet monthly 1960), central-bank gold purchases (World Gold Council, quarterly ~2000). Dollar 12m change is in the tool.
- Confidence: medium.

### Geopolitics now determines economics (regime flag)
- Source: David Petraeus — same file (quote: "we've gone from an era of benign globalization in which economics determined geopolitics ... to a world of renewed great power rivalries where geopolitics now determines what's possible")
- Type: regime map
- Rule as testable logic: IF a geopolitical-risk index is in its top quintile of the last 10 years (proposed) THEN reduce weight in China/EM Asia equity (MCHI/FXI, EEM) relative to US and India (INDA), overweight defence (ITA) and gold. Horizon 12m (proposed).
- Data needed: Caldara-Iacoviello Geopolitical Risk index (GPR, matteoiacoviello.com, monthly from 1900/1985) — NOT in tool; MSCI China (MCHI 2011, FXI 2004), India (INDA 2012; MSCI India index 1993), EEM (2003), ITA (2006), gold.
- Confidence: low (worldview, no threshold).

### Selective decoupling: higher fences around fewer items
- Source: David Petraeus — same file (quote: "there will be additional restrictions but it will be higher fences around fewer items rather than Many Many Items surrounded by less high fences")
- Type: regime map
- Rule as testable logic: IF US export controls tighten on advanced chips/tools THEN underweight China tech/semis relative to US semis is NOT automatically right (selective decoupling, not full); expect relative losses concentrated in China tech and chip-equipment makers with China sales; broad trade continues. Test: SOXX vs KWEB/MCHI and vs SMH around control dates (2022-10-07, 2023-10-17, 2025-04-15) — 3m relative return.
- Data needed: export-control event dates (manual), SOXX (2001), SMH (2000), KWEB (2013), MCHI. Chips vs 12m high is in the tool.
- Confidence: low.

### Supply-chain shift: China -> India / Southeast Asia / Mexico (near-shoring)
- Source: David Petraeus — same file (quote: "you're seeing a migration in some cases from China Vietnam to India to other Southeast Asian countries Philippines and so forth none of which obviously has the capacity of China")
- Type: action/instrument
- Rule as testable logic: Long-horizon tilt: overweight India (INDA/MSCI India), Mexico (EWW), Vietnam (VNM), versus China (MCHI) for multi-year periods while trade/export restrictions on China are rising (proposed trigger: US effective tariff rate on China rising y/y, or rising count of entity-list additions). Hold 24m+.
- Data needed: US effective tariff rate (customs duties / imports; FRED B235RC1Q027SBEA customs duties and IMPGS imports, 1947); INDA, EWW (1996), VNM (2009), MCHI. Not in tool.
- Confidence: low-medium (structural observation, not a timing rule).

### "Just in case" logistics = inventory build (inflationary/capex tailwind)
- Source: David Petraeus — same file (quote: "we've gone from just in time Logistics to just in case Logistics again which means that you're back in the business of warehouses")
- Type: regime map
- Rule as testable logic: IF supply-chain pressure is high (NY Fed GSCPI > +1 sd, proposed) THEN expect higher goods inflation and inventory build; overweight industrials/materials/commodities (XLI, XLB, DBC) vs consumer discretionary for 6-12m; when GSCPI falls back below 0, reverse.
- Data needed: NY Fed Global Supply Chain Pressure Index (monthly from 1997) — NOT in tool; XLI/XLB (1998), DBC (2006; or S&P GSCI from 1970).
- Confidence: low.

### Iran regime-change indicator: security forces stand down / oil workers strike
- Source: David Petraeus — same file (quote: "say the Oil Workers go on strike as they did back in the final days of the shaw this kind of indicator is just not there yet")
- Type: signal
- Rule as testable logic: IF Iranian oil workers strike or security forces defect (event flag) THEN expect an Iranian supply shock: overweight oil (USO/BNO, XLE) for 3-6m (proposed). Otherwise protests alone are not an oil signal.
- Data needed: event flag (manual/news), Brent. Not in tool.
- Confidence: low.

### Cyber deterrence untested (tail risk)
- Source: David Petraeus — same file (quote: "we do fear certain actions certain capabilities they fear certain actions and capabilities and it does have somewhat of a deterrent effect I believe but no one would really know until they try it")
- Type: conflict/caveat
- Rule as testable logic: Not a market rule; a reminder that tail hedges (puts/long Treasuries/gold) are needed for unknown-severity shocks. No direct test.
- Data needed: none.
- Confidence: low.

---

## File 2 — Bill Gurley & Brad Gerstner — "Tariffs, Free Trade, Export Controls, H20 & Rare Earth Ban" (BG2, 2025-04-24)

### Multiple simultaneous policy shocks -> higher discount rate, cut risk units
- Source: Brad Gerstner — Tariffs, Free Trade, Export Controls... BG2 (quote: "I said I was worried about the markets. Discount rates had to go up. There was more uncertainty in the world.")
- Type: position sizing/risk
- Rule as testable logic: IF economic policy uncertainty is high (Baker-Bloom-Davis EPU index or trade-policy-uncertainty index above its 90th percentile of the last 10y, proposed) THEN cut equity exposure to the bottom third of normal (he says "bottom third ... of whatever your normal exposures are"), i.e. ~33% of target stocks; restore when the index falls back below the 75th percentile (proposed). Horizon until reset.
- Data needed: US EPU index (FRED USEPUINDXD daily 1985 / USEPUINDXM monthly 1985), Trade Policy Uncertainty index (Caldara et al., matteoiacoviello.com, 1960). NOT in tool.
- Confidence: medium.

### Units of risk in bottom third under uncertainty; buy big risk-off days only if policy reversal expected
- Source: Brad Gerstner — same file (quote: "if you're thinking about units of risk, you know, it still feels to me like you're in that bottom third, right, of whatever your normal exposures are")
- Type: position sizing/risk
- Rule as testable logic: IF S&P drawdown from high is 10-20% AND EPU high THEN hold ~1/3 normal equity, add only on single-day falls > 3% ("leaning back into markets on some of these down days where it's big risk off") (proposed threshold), betting on policy reversal. Test vs simple trend rule.
- Data needed: S&P 500 daily (Yahoo ^GSPC 1950), EPU. Partly in tool (S&P vs 10m avg).
- Confidence: medium.

### Earnings estimates lag the shock: market falls further when estimates catch down
- Source: Brad Gerstner — same file (quote: "consensus earnings expectations for the S&P have barely moved down ... I think the next move down if we have it is going to be around growth")
- Type: signal
- Rule as testable logic: IF market has fallen >10% on a macro shock BUT forward EPS revisions have fallen < 3% (proposed) THEN expect a second leg down; stay underweight until 3m EPS revisions breadth turns up (proposed: net revisions ratio > 0). 
- Data needed: S&P 500 forward EPS / revision ratio (I/B/E/S — not free; free proxy: S&P quarterly operating EPS estimates from spglobal.com "S&P 500 EPS" spreadsheet ~1988; or Yardeni charts). NOT in tool.
- Confidence: medium.

### Uncertainty becomes reflexive after ~8-16 weeks (capex decommitment)
- Source: Brad Gerstner / Bill Gurley — same file (quote: "if we're still having this conversation in 8, 12, 16 weeks with this level of uncertainty around tariffs, I think it's going to have a much bigger headwind to those S&P earnings")
- Type: signal
- Rule as testable logic: IF EPU (or trade-policy uncertainty) stays above its 90th percentile for > 12 consecutive weeks (proposed) THEN expect earnings downgrades and a growth slowdown; underweight cyclicals vs defensives and stocks vs Treasuries for the next 6m. Gurley: "the fear of it starts to become the reality" — decommitting capacity also raises prices (stagflationary).
- Data needed: EPU daily/monthly (FRED USEPUINDXD), cyclicals vs defensives (in tool), capex intentions (Philly Fed future capex index, FRED? CEFDFSA066MSFRBPHI 1968; regional Fed surveys). Capex survey NOT in tool.
- Confidence: medium.

### Gold outperforming S&P = safe-haven flight signal
- Source: Brad Gerstner — same file (quote: "gold's outperforming uh the S&P so far this year by about 40%. Right? What does that tell you? People are moving into safe havens.")
- Type: signal
- Rule as testable logic: IF gold/S&P ratio YTD or 6m change > +20% (proposed) THEN risk-off regime: underweight stocks, overweight gold for next 3-6m (test whether it is a continuation or contrarian signal).
- Data needed: gold (GLD 2004; World Bank monthly 1960; FRED discontinued LBMA series GOLDAMGBD228NLBM to 2022), S&P. Gold NOT in tool.
- Confidence: medium (observational).

### VIX > 30 + dollar under assault + 10y demand doubts = "sell America" regime
- Source: Brad Gerstner — same file (quote: "The VIX is still over 30. There are fears and rumors out there about is our 10-year, you know, do we have demand for it on a global basis? The dollar is is under assault here.")
- Type: regime map
- Rule as testable logic: IF VIX > 30 AND dollar 1m change < -2% AND 10y yield 1m change > +20bp (stocks, bonds and dollar falling together; proposed thresholds) THEN do NOT use long Treasuries as the hedge; hold gold and T-bills (and non-US equities/currencies e.g. EUR, JPY, CHF) instead until the condition clears.
- Data needed: VIX (in tool), dollar (in tool, DTWEXBGS), 10y (FRED DGS10, in tool), gold, FXE/FXY/FXF (2005-2007) or FRED DEXUSEU (1999), DEXJPUS (1971), DEXSZUS (1971). Combined condition NOT in tool (tool has oil+rates+dollar squeeze, which is the opposite sign for dollar).
- Confidence: medium.

### Tariff policy type determines whether to be in the market
- Source: Brad Gerstner — same file (quote: "your decision as to whether be in the market comes down to whether you think the president is more ... tactical free trader ... or whether you really think he wants to reorient the world in the way Navaro discusses it")
- Type: regime map
- Rule as testable logic: IF US effective tariff rate rises above ~10% and continues rising (structural "Navarro" regime; proposed threshold) THEN underweight US equities vs cash/gold and underweight import-heavy sectors (retail XRT, autos CARZ, consumer discretionary XLY); IF tariffs are narrow/targeted (effective rate rises < 2pp) THEN stay invested. Horizon 12m.
- Data needed: US effective tariff rate (customs duties / goods imports: FRED B235RC1Q027SBEA and BOPGSTB/IMPGS, quarterly 1947); Yale Budget Lab series (2025). NOT in tool.
- Confidence: medium.

### Tariffs are inflationary and invite retaliation (stagflation channel)
- Source: Bill Gurley (citing Reagan) — same file (quote: "tariffs lead to increased inflation. They lead to reduced innovation ... and then fourth ... it leads to retaliation")
- Type: regime map
- Rule as testable logic: IF effective tariff rate jumps > 3pp in 12m (proposed) THEN expect core goods inflation up and growth down over 12m -> stagflation playbook (underweight long nominal Treasuries, overweight TIPS vs nominal, overweight gold/commodities, underweight discretionary). Test: 1930 Smoot-Hawley, 2018-19, 2025 episodes.
- Data needed: effective tariff rate (above), core goods CPI (FRED CUSR0000SACL1E, 1956), TIPS (TIP ETF 2003; FRED DFII10 2003), breakevens (FRED T10YIE 2003). Core CPI is in tool; tariff rate and core goods CPI NOT.
- Confidence: medium.

### Export bans (rare earths, chips) are more dangerous than tariffs
- Source: Brad Gerstner — same file (quote: "these export bans are really dangerous, Bill. ... 90% of them are refined in China")
- Type: signal
- Rule as testable logic: IF China imposes a rare-earth/critical-mineral export ban (event flag) THEN overweight non-China rare-earth/strategic-metals ETF (REMX) and industrial-metal producers ex-China for 3-6m; underweight autos/EV makers (CARZ, DRIV) on input shortage. Test events: 2010-09 Japan embargo, 2023-08 gallium/germanium, 2025-04-04 rare earths.
- Data needed: event list (manual), REMX (2010), CARZ (2011), DRIV (2018). NOT in tool.
- Confidence: low-medium.

### Export controls fail / backfire (porous borders)
- Source: Bill Gurley — same file (quote: "borders are porous, money finds a home ... internet arbitrage is undefeated ... spectacular failure of Russian sanctions")
- Type: conflict/caveat
- Rule as testable logic: Do NOT build rules that assume sanctions/export controls durably cut a target economy's output or a commodity's supply; fade price spikes caused by sanctions after 3-6m (proposed: if oil rises > 20% in 1m on a sanction event, test mean-reversion over the next 6m). Contrasts with Petraeus ("it will bite more and more ... over time").
- Data needed: Brent/WTI, event dates.
- Confidence: medium.

### Political risk to a single dominant firm = macro risk you cannot forecast (avoid concentration)
- Source: Brad Gerstner — same file (quote: "if you wake up one morning and 12 billion of their sales are gone because they can no longer sell ... chips in China, that's something again that ... is the macro that is hard for you to forecast")
- Type: position sizing/risk
- Rule as testable logic: IF top-10 S&P weight is very high (narrow leadership, in tool) AND US-China tension is rising (tariff rate / GPR up) THEN prefer equal-weight S&P (RSP) over cap-weight (SPY) for 12m (proposed).
- Data needed: RSP (2003; S&P 500 equal-weight index 1990), narrow leadership (in tool), GPR (not in tool).
- Confidence: low.

### Nasdaq down 20% / S&P down 10% peak-to-trough is "air out of balloon", not capitulation
- Source: Brad Gerstner — same file (quote: "the S&P's down 10%, NASDAQ, I think as of yesterday was down 20%, peaked to trough ... that feels to me like just the air coming out of the balloon")
- Type: re-entry/exit
- Rule as testable logic: IF S&P drawdown is only ~10% while a policy shock is unresolved THEN do not buy the dip "all in"; require resolution (EPU falling below 75th percentile, proposed) before restoring full exposure.
- Data needed: S&P, Nasdaq (^IXIC 1971 / QQQ 1999), EPU.
- Confidence: medium.

### China's cheap nuclear/power capacity: power is not their constraint
- Source: Brad Gerstner — same file (quote: "there are 100 nuclear power plants under construction in China. Power is not their limit.")
- Type: action/instrument
- Rule as testable logic: Long-horizon: uranium demand rises with global nuclear builds; overweight uranium (URA 2010, URNM 2019) when reactor construction starts rise y/y (proposed). Gurley: Korea/China build nuclear at 1/4 US cost -> Korea industrials (EWY) benefit from export of nuclear builds.
- Data needed: IAEA PRIS reactor construction starts (annual, 1954), uranium spot (Cameco/UxC monthly; IMF PURANUSDM 1980), URA, EWY (2000). NOT in tool.
- Confidence: low.

### Expected tariff end-state (5-10% RoW, 25-30% China) = market floor case
- Source: Brad Gerstner — same file (quote: "we're going to probably land somewhere in this kind of 5 to 10% tariffs for the rest of the world ... and you're not going to end up at 140 on China")
- Type: re-entry/exit
- Rule as testable logic: IF announced tariffs are walked back toward ~10% RoW / ~30% China (effective rate falls from peak by > 5pp, proposed) THEN re-risk equities to normal weight.
- Data needed: effective tariff rate (monthly customs receipts: Treasury Monthly Statement, FRED MTSR133FMS? — customs duties via Daily Treasury Statement 2005).
- Confidence: low (forecast).

---

## File 3 — Scott Bessent — "Macro Maven" (Capital Allocators EP.415, 2024-11-04)

### Micro drives macro: company signals before data
- Source: Scott Bessent — Scott Bessent - Macro Maven (quote: "if trucking companies are telling you the business is taking off then that's very interesting ... if you are hearing from Bank CEOs that credit cards are getting sour")
- Type: signal
- Rule as testable logic: IF truck freight volumes accelerate (y/y up > 3%, proposed) THEN overweight cyclicals for 6m; IF card delinquencies rise > 0.5pp y/y (proposed) THEN underweight consumer discretionary/banks and cut stocks. (Validates existing tool indicators.) Also Home Depot inventory shortages -> goods inflation signal.
- Data needed: truck freight (in tool; FRED TRUCKD11 2000), card delinquencies (in tool; FRED DRCCLACBS 1991), retail inventories/sales ratio (FRED RETAILIRSA, 1992) NOT in tool.
- Confidence: high (core method).

### Best instrument for a view: "where can you get the most bang for the buck"
- Source: Scott Bessent — same file (quote: "if you think oil's going up if drilling stocks are really beaten down then maybe it's stuck if the forward curve is predicting that oil is going to drop over the next 3 years than it could be through the Futures curve")
- Type: action/instrument
- Rule as testable logic: For a bullish oil view: IF oil futures curve is in steep backwardation (12m-ahead futures > 5% below front, proposed) THEN express via long-dated futures (or USL/12-month strip) rather than front month; IF energy equities (XLE/XOP) are cheap vs crude (XLE/WTI ratio in bottom quintile of 10y, proposed) THEN use equities. Choose the cheaper expression. Same logic for any theme: compare spot, curve, equity proxy, options.
- Data needed: WTI front and 12th contract (EIA futures prices RCLC1-RCLC4 1983; CME CL12), XLE (1998), XOP (2006), USO (2006), USL (2007). Oil curve NOT in tool.
- Confidence: high.

### Equity proxy lags commodity: own the commodity directly
- Source: Scott Bessent — same file (quote: "if I had a bullish view on oil okay I'd probably be better off owning crude because I remember at a point I did have a bullish view on oil and the oil stocks didn't move")
- Type: action/instrument
- Rule as testable logic: IF oil-price signal is bullish THEN prefer crude futures (USO/BNO or GSCI energy) over XLE when energy stocks discount the mid-curve rather than spot. Test: compare 6m return of WTI vs XLE following oil momentum signals.
- Data needed: WTI, XLE, GSCI energy (S&P GSCI Energy 1983; via Yahoo ^SPGSEN?). NOT in tool beyond oil 6m change.
- Confidence: medium.

### Correlation check: a "new" idea that is just S&P beta
- Source: Scott Bessent — same file (quote: "someone would say I've got this great idea in Australia and then the risk manager would do a correlation and it had a 98% r squared with the S&P what else is it giving you")
- Type: position sizing/risk
- Rule as testable logic: When adding any country/sector/commodity sleeve, compute 1y rolling correlation/R² with S&P; IF R² > 0.8 (proposed) THEN treat it as S&P exposure for sizing and do not count it as diversification.
- Data needed: daily returns of candidate ETFs (Yahoo) and SPY.
- Confidence: high.

### Size up with confidence; it is fine to be in cash
- Source: Scott Bessent — same file (quote: "if you want conviction and you want to be concentrated there are times when you might not have a big portfolio you could end up in cash")
- Type: position sizing/risk
- Rule as testable logic: IF no signal exceeds a conviction threshold (e.g., composite score in the middle 3 quintiles, proposed) THEN hold T-bills; only take large positions when signals are extreme ("only swing at strikes"). Test: performance of extreme-only rules vs always-on.
- Data needed: tool composite scores; T-bill (FRED DTB3 1954).
- Confidence: high.

### Asymmetric bets on pegged/defended currencies
- Source: Scott Bessent — same file (quote: "if it was an asymmetric bet we could push them up against the wall and the most they could push us back was 2 and a half% and if the corridor broke we can make whatever in a day")
- Type: action/instrument
- Rule as testable logic: IF a currency is pegged/banded AND the domestic economy needs lower rates than the anchor (e.g., housing weak with floating-rate mortgages, policy rate differential under strain) THEN short the pegged currency (max loss = band width). Retail-tradeable analogues: HKD (rare), CNY band (CYB ETF discontinued), DKK, SAR — limited; more general: buy options when implied vol is suppressed by a peg.
- Data needed: FX spot (FRED DEX* series), policy rates (BIS policy rate database 1946), mortgage-rate type (manual).
- Confidence: medium (historically important, few retail instruments).

### Floating-rate mortgages make rate hikes self-defeating
- Source: Scott Bessent — same file (quote: "mortgages there floated with the base rate ... if they were trying to protect the pound strengthen it by raising rates the higher they took rates they would be bankrupting the voting public")
- Type: signal
- Rule as testable logic: IF a country with mostly floating-rate mortgages (UK, Australia, Canada, Sweden, Korea) is hiking rates while house prices are falling (y/y < 0, proposed) THEN expect the central bank to reverse within 12m: short that currency vs USD and long its 2y government bond / overweight its rate-sensitive equities after the pause. Applicable to EWU, EWA, EWC, EWD, EWY.
- Data needed: BIS residential property prices (quarterly, 1970s), BIS policy rates, FX (FRED DEXUSUK 1971, DEXUSAL 1971, DEXCAUS 1971, DEXSDUS 1971, DEXKOUS 1981), MSCI country ETFs (1996-2000). NOT in tool.
- Confidence: medium.

### Low volatility leads to volatility: buy cheap options before regime change
- Source: Scott Bessent — same file (quote: "lack of volatility leads to volatility ... the Yen had been very stable so ball was low maybe the V on the screen was four")
- Type: hedge
- Rule as testable logic: IF 3m implied (or realized) vol of an asset is in its bottom decile of 5y (proposed) AND a fundamental catalyst exists (policy change) THEN buy options (calls/puts) instead of spot. For tool: IF VIX < 12 (proposed, bottom decile) THEN buy SPY puts as a hedge (cheap) rather than selling stocks.
- Data needed: VIX (in tool), CBOE currency vol indexes (EVZ euro vol 2008), realized vol from FX spot; CBOE VXEEM (EM vol, 2011), GVZ gold vol (2008), OVX oil vol (2007). Only VIX in tool.
- Confidence: high.

### Currency is the ultimate expression; equities are the derivative (Abenomics template)
- Source: Scott Bessent — same file (quote: "it was very clear to me that the Yen was the ultimate expression and that equities would be a good derivative of that")
- Type: action/instrument
- Rule as testable logic: IF a country's new government commits to reflation (credible central-bank regime change) AND its currency is the most expensive on PPP THEN short the currency (long USD/JPY via FXY short or YCS) and long its equities hedged (DXJ) for 12-24m. Don't short its bonds (JGB yields "might go lower before they go higher").
- Data needed: PPP valuation (OECD PPP 1960; Big Mac index 1986), JPY (FRED DEXJPUS 1971), DXJ (2006), EWJ (1996), MSCI Japan. NOT in tool.
- Confidence: high (his signature trade), but rule generality medium.

### Currency valuation reference points (PPP, current account)
- Source: Scott Bessent — same file (quote: "this is what could happen to the current account this is how cheap the currency is if it just got back to the historical level so you actually have a framework and reference points")
- Type: signal
- Rule as testable logic: IF a currency's real effective exchange rate is > 1.5 sd above its 20y mean (proposed) AND current account surplus is shrinking THEN expect depreciation over 2-3 years; underweight unhedged exposure / short the currency; reverse for cheap currencies (own unhedged EM equity when EM REERs > 1 sd cheap).
- Data needed: BIS real effective exchange rates (monthly, broad 1994, narrow 1964), IMF current account (WEO, annual 1980). NOT in tool.
- Confidence: medium.

### Policy change doesn't have to work to move prices
- Source: Scott Bessent — same file (quote: "the polic decision doesn't have to work but it can cause a lot of price gation")
- Type: signal
- Rule as testable logic: IF a major regime shift in a country's policy is announced (new central-bank governor / framework change / election of reflation government) THEN trade the first 12m move in the currency/equity direction implied, regardless of the long-run outcome.
- Data needed: event list (manual), FX, country ETF.
- Confidence: medium.

### Trade in thirds; size by P&L cushion ("earn the right to take risk")
- Source: Scott Bessent — same file (quote: "I tend to trade in thirds ... a lot of times we'll keep adding if the p&l is good ... the size of your p&l in a given year will determine your position")
- Type: position sizing/risk
- Rule as testable logic: Enter any new position in three equal tranches (e.g., 1/3 at signal, 1/3 after +X% or 1 month confirmation, 1/3 after another; proposed). Overall risk budget scales with year-to-date P&L: IF YTD return > +5% THEN allow 1.5x risk; IF YTD < 0 THEN 0.5x (proposed). Reset chip stack each January.
- Data needed: strategy's own P&L.
- Confidence: high.

### Take risk down in December
- Source: Scott Bessent — same file (quote: "it's December 15th we got to start taking this down ... when I look back almost every time that I've taken it down it's been the right thing to do because there's always a counter Trend")
- Type: position sizing/risk
- Rule as testable logic: IF a position (esp. currency) has large YTD gains THEN halve it from Dec 15 to Jan 1 (proposed size); test year-end counter-trend in FX/commodity trends (Dec15-Jan15 returns of trailing 12m momentum winners).
- Data needed: FX/commodity daily returns.
- Confidence: medium.

### Risk = probability x severity; Russia-style 95% day
- Source: Scott Bessent — same file (quote: "what's the probability that you're going to lose all your money one day that you were going to have a Russia Ukraine kind of day ... Russian equities would go down 95% in a day")
- Type: position sizing/risk
- Rule as testable logic: Cap any single country with authoritarian/sanction risk (China, Russia-type) at a small weight (proposed ≤ 5% of portfolio) regardless of signal; cap EM single-country sleeve at 10% (proposed).
- Data needed: none (portfolio constraint); optional: political risk index (ICRG, paid; free: World Bank WGI 1996).
- Confidence: high.

### Be concentrated OR illiquid OR leveraged, never all three; exit within 24-72h
- Source: Scott Bessent — same file (quote: "you can't be concentrated illiquid and leveraged I prefer to be liquid and then to use leverage ... I want to be able to get out within 24 72 hours on part of the portfolio")
- Type: position sizing/risk
- Rule as testable logic: Only use instruments with daily volume such that the position can be exited in ≤ 3 days (proposed: position ≤ 10% of ADV); if leverage is used, keep to liquid futures/large ETFs.
- Data needed: ETF volumes (Yahoo).
- Confidence: high.

### Correlations break when you think you're hedged
- Source: Scott Bessent — same file (quote: "how are you measuring liquidity because correlations go to zero when you may think you're hedged")
- Type: hedge
- Rule as testable logic: Do not rely on historical correlation for hedges in stress; test hedges (TLT, gold, JPY, USD, puts) conditional on VIX > 30. Matches tool's stock-bond-correlation switch.
- Data needed: in tool (stock-bond correlation, VIX).
- Confidence: high.

### Add to good managers/strategies after a slump, trim after big years
- Source: Scott Bessent (citing Commonfund study) — same file (quote: "when a manager has one two three blow it out of the park years you pull in some Capital ... and when they are in a slump you add")
- Type: position sizing/risk
- Rule as testable logic: For a multi-strategy allocation (e.g., trend, carry, value sleeves), rebalance toward sleeves with negative 3y returns and away from those with top 3y returns (3-year mean reversion in strategy returns).
- Data needed: sleeve returns.
- Confidence: medium.

### Detect the policy U-turn: "driving 90 mph at a brick wall"
- Source: Scott Bessent — same file (quote: "when a policy when a government when a management is driving 90 M an hour at a brick wall you assume that they are going to hit the brakes so that's how you get the big policy changes")
- Type: re-entry/exit
- Rule as testable logic: IF a policy is pushing an indicator to an extreme (e.g., stocks -20%, 10y yield +100bp in 3m, currency -10% in 3m, credit spread > 2 sd wide; proposed) THEN expect a policy reversal and buy the affected asset (good entry point "because something has gone so far out of equilibrium"). Test: buy S&P after VIX > 40 / HY spread > 7% (proposed).
- Data needed: VIX, HY spread (FRED BAMLH0A0HYM2, 1996), 10y, FX.
- Confidence: high (core method), thresholds proposed.

### Post-election growth shock risk: Fed may have to re-hike
- Source: Scott Bessent — same file (quote: "if Republicans ... get the trifecta I think there could be a growth shock and animal Spirits are back and maybe the fed's jumbo rate cut was a mistake")
- Type: signal
- Rule as testable logic: IF the Fed cuts while nominal GDP growth > 5% and core inflation 3m > 3% (proposed) THEN expect long yields to rise (10y up) — underweight long Treasuries (TLT), prefer T-bills/short TIPS for 6-12m.
- Data needed: Fed funds (in tool), nominal GDP (FRED GDP), core inflation 3m (in tool), 10y.
- Confidence: medium.

### 7% budget deficit in an expansion -> rates up (and yet tech bubble)
- Source: Scott Bessent — same file (quote: "if you were going to say that we were going to have a 7 % budget deficit that rates would go way up but there'd be a MAG seven that there'd be a tech bubble")
- Type: regime map
- Rule as testable logic: IF federal deficit > 6% of GDP while unemployment < 5% (proposed) THEN underweight long-duration Treasuries (10y+), prefer bills/short duration; equities not necessarily hurt (rates up and tech up can coexist).
- Data needed: federal deficit % GDP (FRED FYFSGDA188S annual 1929; monthly Treasury statement MTSDS133FMS 1980), unemployment (FRED UNRATE). Deficit NOT in tool.
- Confidence: medium.

### China under Xi: no clearing function -> structural underweight China
- Source: Scott Bessent — same file (quote: "he's a leninist so he's not going to allow a clearing function in the market that would allow for a sustainable Chinese economy")
- Type: regime map
- Rule as testable logic: Structural: treat China equity (MCHI/FXI) stimulus rallies as tactical only — IF China stimulus announcement causes > 20% rally in 1m (proposed) THEN fade after 1-3m; long-term underweight China vs EM ex-China (EMXC).
- Data needed: MCHI, FXI, EMXC (2017; MSCI EM ex China index 1990s). NOT in tool.
- Confidence: medium.

### Long-term bull market in gold driven by central-bank reserve accumulation
- Source: Scott Bessent — same file (quote: "I think we are in a long-term bull market in Gold I think we're seeing Reserve accumulation by central banks ... it's my biggest position")
- Type: signal
- Rule as testable logic: IF central-bank net gold purchases (4-quarter sum) are above their 10y average (proposed) THEN hold a strategic gold allocation (e.g., 5-10% proposed) and overweight gold vs Treasuries. Trigger example: Poland targeting 20% of reserves in gold.
- Data needed: World Gold Council central-bank demand (quarterly, 2000; IMF IFS gold reserves monthly 1950s), gold price. NOT in tool.
- Confidence: high.

### Policy is personnel: watch who is appointed
- Source: Scott Bessent — same file (quote: "policy is personnel and Personnel is policy so you always look at whether it's the management or the policy makers")
- Type: signal
- Rule as testable logic: IF a central-bank board/governor change shifts the board's stance (e.g., BoJ 2013), THEN the policy shift is credible; trade currency/bonds in that direction. Test with event dates of governor changes (BoJ, Fed chair, BoE, ECB).
- Data needed: event list (manual).
- Confidence: medium.

### Japan: one of the few secular bull markets
- Source: Scott Bessent — same file (quote: "Japan I believe that this could be a secular bull market one of the few in the world")
- Type: action/instrument
- Rule as testable logic: Strategic overweight Japanese equities (EWJ unhedged; DXJ hedged when yen strengthening is unlikely) while Japan core inflation > 1% and governance reforms continue; risk = PM "musical chairs" instability (IF PM changes > 1 per 12m, reduce).
- Data needed: Japan CPI (FRED JPNCPIALLMINMEI 1955), EWJ (1996), MSCI Japan (1970).
- Confidence: medium.

### Europe: populism and de-industrialization; German export model at risk
- Source: Scott Bessent — same file (quote: "German industrial policy we're going to sell into China we're going to use Russian energy ... we're going to turn off our nukes")
- Type: regime map
- Rule as testable logic: IF European natural gas price (TTF) > 2x its 5y average (proposed) OR China import growth < 0 THEN underweight Germany (EWG) vs US; IF far-right/populist poll lead in France, widen-spread trade (French-German 10y spread) — underweight EWQ.
- Data needed: TTF gas (World Bank Pink Sheet "Natural gas, Europe" monthly 1960; ICE TTF futures), China imports (FRED XTIMVA01CNM667S 1990s), EWG/EWQ (1996), OAT-Bund spread (FRED IRLTLT01FRM156N and IRLTLT01DEM156N, 1960s). NOT in tool.
- Confidence: low-medium.

### Grow out of debt via deregulation and energy dominance
- Source: Scott Bessent — same file (quote: "we are going to decide whether we are going to grow our way out of this debt burden and I think we can through deregulation energy Independence")
- Type: regime map
- Rule as testable logic: Fiscal regime: IF real GDP growth > real 10y yield (r < g) THEN debt is sustainable — no fiscal-risk penalty on Treasuries; IF r > g with deficit > 5% GDP THEN fiscal-risk penalty: underweight long bonds, overweight gold. (Tool has 10y minus nominal GDP growth.)
- Data needed: in tool (10y minus nominal GDP), deficit % GDP (not in tool).
- Confidence: medium.

### "Bretton Woods" style realignment coming (global trade/currency regime)
- Source: Scott Bessent — same file (quote: "we're in the midst of a great realignment and of a Britain Woods realignments coming in terms of global policy global trade")
- Type: regime map
- Rule as testable logic: IF US policy explicitly targets dollar weakness / trade realignment (event flag) THEN overweight non-US equities and gold vs US for 12-24m; underweight USD.
- Data needed: dollar (in tool), ACWX (2008)/EFA (2001)/VEU; event flags.
- Confidence: low.

### Bad policy creates good opportunities: overreaction to the last crisis
- Source: Scott Bessent — same file (quote: "a lot of times when there is a bad reaction you get an equal and opposite misguided reaction on the other side ... my first go with seeing how bad policy creates good investment opportunities")
- Type: signal
- Rule as testable logic: IF regulators tighten bank lending standards sharply after a crisis (Fed SLOOS net % tightening C&I > 40%, proposed) THEN short/underweight banks (KBE/XLF) and credit-sensitive sectors for 6-12m; later buy when tightening peaks and starts falling.
- Data needed: Fed Senior Loan Officer Survey (FRED DRTSCILM, quarterly 1990). NOT in tool (bank stocks vs market is).
- Confidence: medium.

### Short-selling works in financial-engineering busts (S&L, Drexel)
- Source: Scott Bessent — same file (quote: "89 and 90 were fantastic years to be short financials so it was the end of this financial engineering")
- Type: action/instrument
- Rule as testable logic: IF commercial real estate prices fall y/y AND credit spreads widen (Baa spread 6m change > +50bp, in tool) THEN short/underweight financials (XLF, KRE) vs S&P for 12m.
- Data needed: CRE prices (FRED COMREPUSQ159N BIS CRE 1990s; Green Street CPPI paid), XLF (1998), KRE (2006), S&P financials sector index (1989). Baa spread in tool.
- Confidence: medium.

### Election/war events: obvious headline does not give obvious trade
- Source: Scott Bessent — same file (quote: "if You would said okay there's going to be this war in Israel it is going to go on for a year but oil prices are going to be lower that's not obvious")
- Type: conflict/caveat
- Rule as testable logic: Do not hard-code geopolitics-to-oil mappings (Middle East war -> long oil); test them: oil 6m/12m return after war onsets (1973, 1990, 2003, 2014, 2022, 2023). Expect weak or negative average.
- Data needed: event list, oil.
- Confidence: high (as caveat).

---

## File 4 — Krishna Guha (Evercore), host Steve Eisman — "5% Rates, Bessent's Failed Gamble & What Comes Next" (Real Eisman Playbook Ep 78, uploaded 2026-10-05)

Context stated in the file: new Fed chair (Warsh) has just hiked; 10y went from ~4.5% (July) to ~5.25%; deficit ~6% of GDP; US-Iran war, diesel doubled; Treasury buyback "operation twist"; mortgage rates ~7%.

### Fed hikes as "insurance" when inflation above target > 5 years
- Source: Krishna Guha — 5% Rates, Bessent's Failed Gamble... (quote: "His judgment is that inflation has been above the Fed's 2% target for too long. It's more than 5 years.")
- Type: signal
- Rule as testable logic: IF core PCE has been above 2% for ≥ 36 consecutive months (proposed; speaker says >5 years) AND unemployment is low/stable THEN raise probability of Fed hikes even into supply shocks (oil) -> underweight long Treasuries and rate-sensitive sectors (homebuilders, utilities) for 6-12m; prefer T-bills/floating rate (USFR, TFLO).
- Data needed: core PCE (FRED PCEPILFE, 1959) — months-above-target counter NOT in tool; Fed funds 12m change in tool; USFR (2014), TFLO (2014).
- Confidence: medium.

### Tariff inflation drops out of the data after ~12 months; oil does not create lasting inflation
- Source: Krishna Guha — same file (quote: "I do think that the tariff inflation is going to drop into, you know, drop out of the numbers fairly soon ... I don't see any evidence that oil is going to create some kind of lasting inflation impulse")
- Type: conflict/caveat
- Rule as testable logic: IF an inflation rise is driven by a one-off level shock (tariffs, oil spike) THEN expect y/y inflation to fall back after 12m (base effect) — do not stay underweight duration beyond 12m on a level shock unless core 3m annualised stays > 12m rate (tool already has core 3m vs 12m). Test: core CPI 12-24m after oil spikes > 50% y/y.
- Data needed: in tool (core 3m vs 12m, oil 6m change).
- Confidence: medium.

### Diesel/refined products signal more inflation than crude
- Source: Krishna Guha / Steve Eisman — same file (quote: "if you just look at the price of WTI or Brent oil or even you just look at the pump price of gasoline, you're not getting the full picture because refined product like diesel and jet fuel has actually increased a lot more")
- Type: signal
- Rule as testable logic: IF diesel price 6m change > crude 6m change by > 25pp (crack spread blowout; proposed) THEN treat as a stronger inflation/growth shock than the oil indicator suggests: add to the oil+rates+dollar squeeze warning; underweight transports (IYT) and airlines (JETS), overweight refiners (CRAK) / energy.
- Data needed: US No.2 diesel retail (EIA, weekly 1994; FRED GASDESW 1994), NY Harbor ULSD spot (EIA 1986), jet fuel (FRED DJFUELUSGULF 1990), 3-2-1 crack spread; IYT (2004), JETS (2015), CRAK (2015). NOT in tool (tool has crude 6m).
- Confidence: medium.

### 10y yield surge from 4.5% to 5.25%: three causes (supply, AI investment demand / higher r*, oil)
- Source: Krishna Guha — same file (quote: "you have a ton of debt issuance by the AI hyperscalers ... the government's running a massive deficit already 6% of GDP ... more borrowers competing for savings")
- Type: regime map
- Rule as testable logic: IF (corporate IG issuance + Treasury net issuance) rises y/y AND deficit > 5% GDP AND capex boom (business investment growth > 5% real y/y, proposed) THEN expect higher neutral rate: underweight long Treasuries (TLT) vs bills; expect curve steepening (long 2s10s steepener via short TLT/long SHY).
- Data needed: Treasury net issuance (SIFMA, monthly 1996; Treasury quarterly refunding), IG corporate issuance (SIFMA), private nonresidential fixed investment (FRED PNFI 1947), deficit (FRED MTSDS133FMS). NOT in tool (term premium 12m change and 10y-GDP are).
- Confidence: medium.

### Neutral rate higher in an investment boom ("too few savings chasing investment")
- Source: Krishna Guha — same file (quote: "we've moved from a world where there was too much saving chasing too few investment opportunities to a world in which there's a huge demand to invest chasing a limited pool of savings")
- Type: regime map
- Rule as testable logic: IF Laubach-Williams / Holston-Laubach-Williams r* estimate rises y/y (or real 10y yield > 2%, proposed) THEN lower the expected return of long nominal bonds as a hedge; cap TLT weight in de-risk sleeve and prefer T-bills.
- Data needed: NY Fed HLW r* (quarterly 1961), real 10y yield (in tool, FRED DFII10 2003 / estimated pre-2003).
- Confidence: medium.

### Removal of Fed forward guidance -> higher rate volatility and overshooting
- Source: Krishna Guha — same file (quote: "Worshes removed those guard rails and that has contributed in my view to rates markets running rampant over recent weeks because of uncertainty")
- Type: regime map
- Rule as testable logic: IF Fed provides no reaction-function guidance (regime flag) or MOVE index > 120 (proposed) THEN expect bond-yield overshoots: reduce duration size (half-weight TLT) and use mean reversion: buy TLT only after 10y yield rises > 75bp in 3m (proposed), not before.
- Data needed: ICE BofA MOVE index (Yahoo ^MOVE, 1988), 10y (DGS10). MOVE NOT in tool.
- Confidence: medium.

### Treasury buybacks / sovereign intervention in own bond market = credibility negative
- Source: Krishna Guha — same file (quote: "serious governments like the US government tend not to intervene in their own debt market. That's the sort of thing you find more often in struggling emerging markets")
- Type: signal
- Rule as testable logic: IF the Treasury announces buybacks aimed at capping long yields, or shifts issuance strongly to bills to suppress long rates (bill share of issuance > 25%, proposed) THEN expect term premium to rise further (counter-intuitive): underweight long Treasuries, overweight gold (fiscal-dominance hedge) for 6m.
- Data needed: Treasury buyback schedule (TreasuryDirect, 2024+), bill share of marketable debt (Treasury Monthly Statement of the Public Debt, 1950s), term premium (in tool, ACM). Bill share NOT in tool.
- Confidence: medium.

### Shifting issuance to bills signals lower long-end supply (signal channel)
- Source: Krishna Guha — same file (quote: "he's also sending a signal that future government debt issuance may be shifted from these longerterm bonds to the shorter duration bonds")
- Type: conflict/caveat
- Rule as testable logic: Opposite to the rule above: IF quarterly refunding cuts coupon sizes THEN 10y term premium falls over next 3m. Test both directions on refunding announcement dates (2023-11-01 example: coupon slowdown -> yields fell).
- Data needed: refunding dates and coupon sizes (Treasury, 1970s), ACM term premium (NY Fed, daily 1961).
- Confidence: medium.

### Bank liquidity rules (LCR/SLR) loosened -> banks absorb Treasuries (mostly bills)
- Source: Krishna Guha / Steve Eisman — same file (quote: "encourages banks to hold fewer Fed reserves, which would help Kevin Walsh in his goal of bringing down the Fed balance sheet ... and potentially hold more treasuries")
- Type: signal
- Rule as testable logic: IF SLR/LCR easing is finalised (event) THEN expect swap spreads to widen (Treasuries outperform swaps) and front-end yields to fall vs long end; favour 2-5y Treasuries (SHY/IEI) over long (TLT).
- Data needed: event dates; bank Treasury holdings (FRED TASACBW027SBOG, weekly 1973), swap spreads (FRED discontinued; Bloomberg). NOT in tool.
- Confidence: low.

### Fed balance-sheet reduction resumes when bond markets stabilise
- Source: Krishna Guha — same file (quote: "he's going to look for a window of opportunity when bond market conditions stabilize, when yields come down some, where he can start to reintroduce a plan to gradually reduce")
- Type: signal
- Rule as testable logic: IF 10y yield falls ≥ 50bp from its peak (proposed) under a balance-sheet-hawk Fed THEN expect QT announcement -> cap upside for bonds; Fed net liquidity 3m change (in tool) turns negative -> reduce equities. 
- Data needed: Fed assets (FRED WALCL 2002), net liquidity (in tool).
- Confidence: low-medium.

### 10y with a "5 handle" hurts non-AI economy; 6% threatens AI capex and stock wealth effect
- Source: Krishna Guha — same file (quote: "we're already clearly in territory you know with a five handle which is putting strain on the nonAI uh parts of the economy ... that might require ... say six handle")
- Type: signal
- Rule as testable logic: IF 10y yield > 5% THEN underweight rate-sensitive "old economy" (small caps IWM, homebuilders ITB/XHB, REITs VNQ, regional banks KRE) vs mega-cap tech for 6m; IF 10y > 6% (proposed) THEN cut equities overall (AI capex and wealth effect at risk).
- Data needed: DGS10 (in tool as 12m change, add level thresholds); IWM (2000), ITB (2006), VNQ (2004), KRE (2006).
- Confidence: medium.

### Housing is ground zero at 7% mortgage rates
- Source: Krishna Guha — same file (quote: "Ground zero for this is the housing market. Right? Housing is completely bombed out because mortgage rates are 7%.")
- Type: signal
- Rule as testable logic: IF 30y mortgage rate > 7% (proposed level; tool has 12m change) THEN underweight homebuilders (ITB/XHB) and home-improvement retail; expect housing starts down. Reverse when mortgage rate falls > 100bp from peak (homebuilders lead).
- Data needed: FRED MORTGAGE30US (1971; in tool as 12m change), housing starts (FRED HOUST 1959), ITB/XHB.
- Confidence: high.

### Wealth-effect economy: the stock market is the key variable
- Source: Krishna Guha — same file (quote: "the one thing to watch right now is whether the stock market can withstand, you know, 10-year yields in this zip code because if the stock market sells off, then you have a wealth problem")
- Type: signal
- Rule as testable logic: IF household equity share is high (in tool) AND consumer spending is driven by top-income cohort AND S&P falls > 15% from high (proposed) THEN expect consumer-spending slowdown 2-3 quarters later; underweight consumer discretionary (XLY) vs staples (XLP).
- Data needed: household equity share (in tool), Fed Distributional Financial Accounts (top 10% spending share, quarterly 1989), XLY/XLP (1998; staples vs discretionary in tool).
- Confidence: medium.

### Markets move with oil and the 10-year
- Source: Steve Eisman — same file (quote: "if you look at the markets on a daily basis, they simply move with oil prices and the yield on the 10-year")
- Type: regime map
- Rule as testable logic: IF 60-day correlation of S&P daily returns with oil and with 10y-yield changes is strongly negative (both < -0.3, proposed) THEN supply-shock regime: stocks and bonds fall together -> TLT is not a hedge; use T-bills/gold/energy as the de-risk asset. (Extends tool's stock-bond correlation switch to oil.)
- Data needed: S&P, WTI, DGS10 daily (in tool partly).
- Confidence: medium.

### QE works in seized markets; Warsh accepts QE only in market seizures
- Source: Krishna Guha — same file (quote: "He actually agrees that there is a role for QE when markets seize up ... what he doesn't like is ... to continue to do QE to try to strengthen growth")
- Type: re-entry/exit
- Rule as testable logic: IF credit markets seize (HY spread > 8% or rising > 300bp in 1m, proposed) THEN expect Fed emergency QE/backstops -> buy credit (HYG/LQD) and equities within 1-3m of the backstop announcement. In non-crisis slowdowns, do NOT expect QE under a balance-sheet-hawk Fed (lower odds of a liquidity-driven rally).
- Data needed: FRED BAMLH0A0HYM2 (1996), Moody's Baa spread (in tool), HYG (2007), LQD (2002).
- Confidence: medium.

### Fed was slow to see inflation persistence, then caught up fast (soft landing possible)
- Source: Krishna Guha — same file (quote: "Jay Powell achieved something that most economists thought was unreachable which was to bring inflation down without pushing unemployment up")
- Type: conflict/caveat
- Rule as testable logic: Caveat for yield-curve/hiking-cycle recession rules: fast hiking cycles do not always cause recession (2022-24); require a labour-market confirmation (Sahm rule, in tool) before cutting stocks on curve inversion alone.
- Data needed: in tool.
- Confidence: medium.

---

## File 5 — Geoffrey Garrett (USC Marshall dean) with Nicolai Tangen — NBIM "In Good Company" (2025-05-07)

Mostly leadership/education content; only a few macro statements.

### Deglobalisation raises prices and interest rates
- Source: Geoffrey Garrett — Geoffrey Garrett - Podcast - In Good Company (quote: "globalization reduced prices and reduced interest rates in America for decades")
- Type: regime map
- Rule as testable logic: IF trade openness falls (US imports/GDP or world trade volume y/y < 0 for 4 quarters, proposed) THEN expect structurally higher inflation and higher long yields: lower long-duration bond weight; tilt to TIPS, commodities.
- Data needed: world trade volume (CPB World Trade Monitor, monthly 1991), US imports/GDP (FRED IMPGSC1 / GDPC1, 1947). NOT in tool.
- Confidence: medium.

### Reshoring has a cost: prices higher
- Source: Geoffrey Garrett — same file (quote: "there's a real cost to reshoring stuff which is prices go higher")
- Type: regime map
- Rule as testable logic: Same mapping as tariffs: rising tariff/reshoring regime -> higher core goods inflation -> favour TIPS over nominals (proposed: hold TIP vs IEF while effective tariff rate is rising y/y).
- Data needed: effective tariff rate (FRED customs duties B235RC1Q027SBEA / imports), TIP vs IEF (2003). NOT in tool.
- Confidence: medium.

### Chinese EVs are a transformative force (pressure on legacy autos, Germany)
- Source: Geoffrey Garrett — same file (quote: "the rise of the Chinese electric vehicle and the question in Europe in the US is what are we going to do about that")
- Type: action/instrument
- Rule as testable logic: Structural underweight Germany (EWG) / European autos vs China EV/battery supply chain (KARS, LIT) while China EV export volumes grow > 20% y/y (proposed).
- Data needed: China auto exports (CAAM monthly, ~2010; China customs), EWG, KARS (2018), LIT (2010). NOT in tool.
- Confidence: low.

### Green-energy supply chain dominated by China; nickel (Indonesia)
- Source: Geoffrey Garrett — same file (quote: "the entire green energy supply chain now is dominated by China ... Indonesia thinks that nickel mining is their future")
- Type: action/instrument
- Rule as testable logic: Commodity-country link: Indonesia equity (EIDO) tracks nickel price; IF nickel 6m change > +20% (proposed) THEN overweight EIDO vs EEM for 6m. Test correlation first.
- Data needed: nickel (World Bank Pink Sheet monthly 1960; LME), EIDO (2010). NOT in tool.
- Confidence: low.

### Cheap US gasoline (energy exporter) slows EV adoption
- Source: Geoffrey Garrett — same file (quote: "the US is now a fossil fuel exporter and as you know uh petrol is cheaper in the US than anywhere else in the world")
- Type: conflict/caveat
- Rule as testable logic: US is a net petroleum exporter since 2019/2020 -> oil price rises now improve US terms of trade (dollar may rise with oil rather than fall). Test: correlation of dollar 12m change with oil 12m change before vs after 2019 (tool's oil+rates+dollar squeeze may behave differently post-2019).
- Data needed: US petroleum net exports (EIA, monthly 1973), dollar, oil (in tool).
- Confidence: medium (structural fact).

---

## File 6 — Ken Tropin (Graham Capital) — Macro Hive with Bilal Hafeez (uploaded 2025-02-14; content recorded ~spring 2023, "two weeks" after SVB)

### Macro/CTA returns come from central-bank activity: count rate moves
- Source: Ken Tropin — Ken Tropin on How to Run a Successful Macro Hedge Fund (quote: "there were just under 50 raid hikes of 25 basis points equivalent by those same three central banks ... there was 30 times the amount of uh action to work with")
- Type: regime map
- Rule as testable logic: IF the sum of absolute policy-rate changes of Fed+ECB+BoE over the last 12m > 200bp (proposed; 2010-21 average was ~120bp per year in total) THEN allocate to trend-following/managed futures (DBMF, KMLM, or a simple time-series momentum sleeve on bonds, FX, commodities, equity indexes) — opportunity set rich; IF < 50bp (zero-rate forward-guidance regime) THEN reduce trend allocation.
- Data needed: Fed funds (FRED FEDFUNDS 1954), ECB deposit rate (FRED ECBDFR 1999), BoE Bank Rate (BoE database 1694; FRED BOERUKM), BIS policy rates; SG Trend index / managed futures proxy (Ken French–style TSMOM from AQR data library "Time Series Momentum" 1985); DBMF (2019), KMLM (2020). NOT in tool.
- Confidence: high.

### Trend/macro diversifies in crises (1987, 2000-02, 2008)
- Source: Ken Tropin — same file (quote: "uh the second half of 2008 was a great period for macro and for GTA ... it was an uncorrelated way of investing")
- Type: hedge
- Rule as testable logic: Hold a permanent time-series-momentum sleeve (e.g., 10-20% of portfolio, proposed) as crisis hedge; test its return when S&P drawdown > 20% (1987, 2000-02, 2008, 2022) vs long Treasuries and gold.
- Data needed: AQR TSMOM factor (monthly 1985), SG CTA index (2000), or build own on futures/ETFs (Yahoo). NOT in tool.
- Confidence: high.

### Bonds rally hard on equity crash days (1987)
- Source: Ken Tropin — same file (quote: "bonds really crater yields really cratered bonds rallied a lot uh on the Monday following the market crash and our CTA got long fixed income")
- Type: hedge
- Rule as testable logic: IF S&P falls > 10% in a week AND inflation is not the cause (core CPI 3m < 4%, proposed) THEN long Treasuries (10y+ futures / TLT) are the hedge. Consistent with tool's stock-bond-correlation switch.
- Data needed: in tool.
- Confidence: medium.

### Inflation is an ocean liner: slow to return to 2%
- Source: Ken Tropin — same file (quote: "I think inflation is kind of like an ocean liner it's hard to move around it was really hard for them to create it I think it's going to be not so easy")
- Type: regime map
- Rule as testable logic: IF core CPI y/y > 4% (proposed) THEN expect it to stay above 3% for ≥ 12m; do not front-run rate cuts (market cut-pricing too optimistic): underweight long duration until core 3m annualised < 3% (proposed).
- Data needed: core CPI (in tool), fed funds futures-implied cuts (CME FedWatch; free proxy: 2y yield minus fed funds, FRED DGS2 - DFF, 1976). 2y-FF spread NOT in tool.
- Confidence: medium.

### Expensive equities into a likely recession: fair forward P/E 16-17 not 19
- Source: Ken Tropin — same file (quote: "with forward pees onee PE now just under 19 that seems high to me uh should we normalize at 16 or 17 I would think so")
- Type: signal
- Rule as testable logic: IF S&P forward P/E > 18 AND recession probability high (curve inverted + leading indicators down) THEN lean short/underweight equities for 6-12m.
- Data needed: S&P forward P/E (not free long history; proxy: trailing P/E Shiller data 1871 — CAPE in tool), yield curve (in tool). Forward P/E NOT in tool.
- Confidence: medium.

### TINA is over when cash pays 4-5% (equity risk premium vs T-bill)
- Source: Ken Tropin — same file (quote: "there is no alternative and now there is an alternative now you can make four or five% in RIS stre rates")
- Type: signal
- Rule as testable logic: IF S&P earnings yield minus 3m T-bill yield < 1pp (proposed) THEN underweight equities vs T-bills for 12m; IF > 4pp overweight.
- Data needed: S&P earnings yield (Shiller data monthly 1871; or 1/forward PE), T-bill (FRED TB3MS 1934). Earnings-yield-minus-bill gap NOT in tool (CAPE is).
- Confidence: medium-high.

### Buy-the-dip psychology persists until the economy actually contracts
- Source: Ken Tropin — same file (quote: "the psychology of investor for the last 15 years is buy every dip and you were rewarded for doing so ... that psychology probably hasn't changed yet")
- Type: conflict/caveat
- Rule as testable logic: Do not cut equities on valuation alone; wait for a macro confirmation (Sahm rule trigger / earnings contraction). Supports tool design (warnings only bite with Fed tightening / trend break).
- Data needed: in tool.
- Confidence: medium.

### Dollar weakens when the ECB is more hawkish than the Fed
- Source: Ken Tropin — same file (quote: "the perception is the ECB is now more hawkish than the Fed and uh so you know the dollar looks slightly weak")
- Type: signal
- Rule as testable logic: IF (US 2y yield minus German 2y yield) falls > 50bp over 6m (proposed) THEN short USD vs EUR (long FXE) / overweight unhedged European equities (VGK, EZU) for 6m; EUR breaking above a round level (1.10) adds confirmation.
- Data needed: US 2y (FRED DGS2 1976), German 2y (Bundesbank daily 1972; FRED IRLTLT01 is 10y only — use Bundesbank or ECB yield curve 2004), EURUSD (FRED DEXUSEU 1999; DM pre-1999 DEXGEUS 1971), FXE (2005), VGK (2005). NOT in tool.
- Confidence: medium.

### Yield curve steepens as the economy goes into recession (bull steepener)
- Source: Ken Tropin — same file (quote: "it was inverted as much as two1 were 100 basis points inverted now it's about 60 uh I would look for that to steepen as the economy indeed goes into a recession")
- Type: signal
- Rule as testable logic: IF 2s10s has been inverted (< 0) and starts steepening by > 50bp from its trough (proposed) THEN recession is near: cut equities, own 2y Treasuries (SHY) / steepener (long SHY, short TLT duration-neutral) for 6-12m.
- Data needed: FRED T10Y2Y (1976; in tool as level). Steepening-from-trough NOT in tool.
- Confidence: medium-high.

### No term premium: duration risk unpriced (SVB lesson)
- Source: Ken Tropin — same file (quote: "people totally forgot about something called duration risk uh and that you should get paid more you should have term premium for taking duration risk and and there is no premium right now")
- Type: signal
- Rule as testable logic: IF ACM 10y term premium < 0 (proposed) THEN underweight long-duration Treasuries vs bills (poor compensation); IF > +1% overweight duration.
- Data needed: ACM term premium (NY Fed, 1961; tool has 12m change only — add level).
- Confidence: medium.

### Market too optimistic on cuts
- Source: Ken Tropin — same file (quote: "I think the Market's slightly optimistic on Cuts particularly in the US happening in this third and fourth quarter uh I'm not convinced")
- Type: signal
- Rule as testable logic: IF market prices > 50bp cuts within 6m (2y yield < fed funds by > 50bp, proposed) BUT core inflation 3m > 3.5% THEN fade the cuts: underweight 2y Treasuries / underweight duration for 3-6m.
- Data needed: DGS2, DFF (1954), core CPI.
- Confidence: low-medium.

### Daily risk meeting; risk management from 2007 counterparty crisis
- Source: Ken Tropin — same file (quote: "we started having a daily risk meeting at 9:30 every morning to look at um every Traders positions liquidity and counterparty risks and stress tests")
- Type: position sizing/risk
- Rule as testable logic: Process rule: daily stress test of portfolio vs historical scenarios (1987, 2008, 2020, 2022); cap portfolio stress loss (proposed ≤ 20% in worst scenario).
- Data needed: historical returns of instruments.
- Confidence: high (process).

### Diversify sources of return: momentum and value
- Source: Ken Tropin — same file (quote: "I don't want to only make money when it's good for momentum and quantitative trading I want to be able to make uh a return uh when uh you know maybe value is a more attractive Factor than momentum")
- Type: position sizing/risk
- Rule as testable logic: Combine trend (time-series momentum) with value (e.g., cross-country CAPE value, currency PPP value, commodity 5y reversal) sleeves; test that the combo has lower drawdown than either alone.
- Data needed: country CAPE (Barclays/Research Affiliates/ StarCapital, ~1980s), PPP (OECD), commodity prices (World Bank). NOT in tool.
- Confidence: high.

### Volatility persists 36-60 months after an inflation shock (supply chains, war, Asia tension, elections, green policy)
- Source: Ken Tropin — same file (quote: "for macro maybe the next 36 to 60 months continue to look really favorable")
- Type: regime map
- Rule as testable logic: IF inflation regime (core CPI > 3%) and policy rate volatility high THEN expect elevated FX/rates/commodity volatility for 3-5 years -> keep trend sleeve at higher weight; stock-bond correlation likely positive (tool switch to T-bills over TLT).
- Data needed: in tool (core CPI, stock-bond correlation); FX vol (realized from FRED FX).
- Confidence: medium.

### Debt ceiling: "always ugly until it isn't"
- Source: Ken Tropin — same file (quote: "we got the debt cealing uh you know negotiation that it's always ugly until it isn't right so uh we'll have to keep an eye on that")
- Type: conflict/caveat
- Rule as testable logic: Do not de-risk on debt-ceiling headlines alone; test: S&P and T-bill spread around X-dates (2011, 2013, 2023) — expect brief stress, then reversal. (Optional rule: avoid T-bills maturing near X-date.)
- Data needed: event dates, 1m T-bill (FRED DTB4WK 2001).
- Confidence: medium.

### No 08-style crisis after SVB: Fed response contained it
- Source: Ken Tropin — same file (quote: "I don't I don't think we'll see an' 08 style crisis uh although we came pretty close two weeks ago ... I think the FED response was pretty good")
- Type: re-entry/exit
- Rule as testable logic: IF a bank run triggers a rapid Fed facility (BTFP-type) within 1 week THEN do not extend de-risking beyond 3m unless credit spreads keep widening (Baa spread 6m change > +100bp, proposed).
- Data needed: Baa spread (in tool), KRE.
- Confidence: medium.

---

## File 7 — Stanley Druckenmiller — "Druckenmiller on How AI is Dominating His Long Portfolio" (Bloomberg Live, 2023-06-07)

### Fiscal/entitlement problem is not a 3-6 month trade
- Source: Stanley Druckenmiller — Druckenmiller on How AI is Dominating His Long Portfolio (quote: "I don't think the entitlement situation is something you should be trading on in the next three to six months")
- Type: conflict/caveat
- Rule as testable logic: Do NOT use debt/GDP or fiscal-gap levels as short-horizon (≤ 6m) timing signals for Treasuries or stocks; at most as a slow regime weight (5-10y). Test: predictive power of debt/GDP level for 6m vs 5y bond returns.
- Data needed: federal debt/GDP (FRED GFDEGDQ188S, 1966), CBO projections.
- Confidence: high.

### Pro-cyclical deficits: trillion-dollar deficit at 3.5% unemployment
- Source: Stanley Druckenmiller — same file (quote: "with three and a half percent unemployment we had something unprecedented we had a trillion dollar deficit usually when the economy is roaring tax revenues go up in the deficit shrinks")
- Type: signal
- Rule as testable logic: IF deficit/GDP > 5% while unemployment < 4.5% (pro-cyclical fiscal; proposed) THEN expect higher inflation and higher term premium over 1-3 years: structurally lower long-Treasury weight, tilt to TIPS/gold/commodities.
- Data needed: deficit (FRED FYFSGDA188S annual 1929; MTSDS133FMS monthly 1980), UNRATE (1948). Deficit NOT in tool.
- Confidence: medium.

### Interest expense crowding out (CBO path) — long-term fiscal dominance risk
- Source: Stanley Druckenmiller — same file (quote: "interest expense is 27 percent of outlays by 2050 and just entitlements and interest expense ... will be 117 percent of taxes by 2050")
- Type: regime map
- Rule as testable logic: IF federal net interest/receipts > 20% (proposed; was ~14% 2023) and rising THEN fiscal-dominance regime: prefer gold and short-duration TIPS over long nominal Treasuries as the defensive asset; Fed may tolerate higher inflation.
- Data needed: federal interest outlays (FRED A091RC1Q027SBEA, 1947), federal receipts (FRED W006RC1Q027SBEA, 1947). NOT in tool.
- Confidence: medium.

### Taxes must rise (or 30-40% inflation) — long-run
- Source: Stanley Druckenmiller — same file (quote: "taxes are going to be much higher in 20 years ... it's either that or you know 30 or 40 inflation which I don't think is going to happen")
- Type: regime map
- Rule as testable logic: Long-run valuation adjustment: expected equity returns lower (higher future taxes); not a trading rule. Optional: overweight non-US equities when US fiscal gap widens.
- Data needed: CBO fiscal gap (annual).
- Confidence: low.

### After the biggest asset bubble + 500bp hikes in a year, expect "more shoes to drop"
- Source: Stanley Druckenmiller — same file (quote: "when you go from this kind of environment the biggest broadest asset bubble ever and then your jack rates up 500 basis points in a year I think the probabilities would suggest that Silicon Valley Banks Bed Bath and Beyond they're probably the tip of the iceberg")
- Type: signal
- Rule as testable logic: IF Fed funds 12m change > +300bp (proposed; tool has the variable) AND preceding valuation was extreme (CAPE > 30 or market cap/GDP top decile; in tool) THEN expect credit events within 6-24m: underweight equities and HY credit, overweight T-bills; keep until Fed funds 12m change turns negative AND credit spreads have peaked.
- Data needed: in tool (Fed funds 12m change, CAPE, market cap/GDP); HY spread (FRED BAMLH0A0HYM2) — add if missing.
- Confidence: high (matches existing tool design).

### Hard-landing earnings drop: 20-30% (40-50% if unanticipated)
- Source: Stanley Druckenmiller — same file (quote: "I could see corporate profits down 20 to 30 percent normally I would say 40 or 50 in a hard Landing but this recession is so anticipated")
- Type: position sizing/risk
- Rule as testable logic: Recession-scenario sizing: assume EPS -25% in an anticipated recession, -45% in an unanticipated one; use to set equity stress loss. Test: measure EPS declines in recessions vs consensus recession probability (SPF anxious index) before them.
- Data needed: S&P EPS (Shiller 1871), SPF probability of decline (Philadelphia Fed Anxious Index, quarterly 1968). SPF NOT in tool.
- Confidence: medium.

### Banks impaired by duration losses; recession losses come from cards and CRE
- Source: Stanley Druckenmiller — same file (quote: "they bought a bunch of treasuries yielding one or two percent and now they're carrying them at five so so their balance sheets are impaired but if we get in a recession then the real losses comes which is stuff like credit cards commercial real estate")
- Type: signal
- Rule as testable logic: IF bank unrealised securities losses / equity > 25% (FDIC; proposed) AND credit-card delinquencies rising (in tool) THEN underweight banks (KRE/KBE) vs market for 12m; credit tightening over next 6-9 months -> cut cyclicals.
- Data needed: FDIC Quarterly Banking Profile unrealised losses (2008+), card delinquencies (in tool), CRE delinquency (FRED DRCRELEXFACBS 1991), SLOOS (FRED DRTSCILM 1990). Unrealised losses, CRE delinquencies, SLOOS NOT in tool.
- Confidence: medium.

### Office CRE stress + credit tightening next 6-9 months
- Source: Stanley Druckenmiller — same file (quote: "commercial real estate ... office is a problem ... financing rates going up ... I'm worried about credit tightening the next six to nine months")
- Type: signal
- Rule as testable logic: IF SLOOS net % tightening for CRE/C&I > 30% (proposed) THEN underweight REITs (VNQ), regional banks (KRE), small caps (IWM) for 6-9m.
- Data needed: SLOOS (FRED SUBLPDRCSC 1990 CRE; DRTSCILM C&I), VNQ, KRE, IWM.
- Confidence: medium.

### Delayed recession does not lower its probability; longer delay -> higher terminal rate -> higher hard-landing odds
- Source: Stanley Druckenmiller — same file (quote: "the fact that it hasn't started yet change the probability of whether it's going to be hard or soft I would actually argue since it's taken so long the FED has ended up with a higher terminal rate")
- Type: conflict/caveat
- Rule as testable logic: Do not decay recession warnings with time since yield-curve inversion; hold the warning until the curve has re-steepened and labour market confirms or clears (proposed: keep warning active up to 24m after inversion). Contrast: Guha (File 4) points to the 2022-24 soft landing.
- Data needed: in tool (T10Y2Y, Sahm rule).
- Confidence: medium.

### Liquidity drivers: TGA drawdown, BoJ YCC defence, QT, TGA rebuild
- Source: Stanley Druckenmiller — same file (quote: "secretary Yellen Drew down the TGA that's basically the treasury savings account from 700 billion to practically nothing ... actually the TJ is going to go the other way ... about 800 billion in treasuries issued between now and Year End")
- Type: signal
- Rule as testable logic: Net liquidity = Fed assets - TGA - reverse repo (tool has 3m change). Add forward-looking rule: IF Treasury announces TGA rebuild > $500bn within 6m (post debt-ceiling; proposed) THEN expect liquidity drain -> reduce equities/risk assets over the rebuild window; IF TGA drawdown (debt-ceiling period) THEN liquidity tailwind. Also foreign CB interventions (BoJ bond buying) add dollar liquidity.
- Data needed: TGA (FRED WTREGEN weekly 2002; daily DTS 2005), RRP (FRED RRPONTSYD 2013), WALCL (2002), BoJ JGB holdings (BoJ monthly). Net liquidity in tool; TGA projections (Treasury quarterly refunding) NOT.
- Confidence: medium-high.

### Excess demand deposits / COVID liquidity stock delays recession
- Source: Stanley Druckenmiller — same file (quote: "10 trillion dollars 5 trillion monetary 5 trillion fiscal was put in during covid what has happened is that created this giant giant stock of liquidity")
- Type: regime map
- Rule as testable logic: IF M2 level is above its pre-shock trend (e.g., M2 vs 2010-2019 log trend > +5%, proposed) THEN recession signals have longer lags (add 6-12m); IF M2 falls back to trend, warnings become live. (Tool has M2 growth; add M2 gap vs trend.)
- Data needed: FRED M2SL (1959); excess savings (SF Fed estimate). Gap vs trend NOT in tool.
- Confidence: medium.

### Student-loan payment restart = consumption headwind
- Source: Stanley Druckenmiller — same file (quote: "you've got the student loan thing which I think has kept consumption up that's all changing in September")
- Type: signal
- Rule as testable logic: IF a policy ends a consumer transfer/moratorium (student loans, stimulus checks, child tax credit) worth > 0.3% of disposable income (proposed) THEN underweight consumer discretionary vs staples for 6m after the restart.
- Data needed: event list; staples vs discretionary (in tool).
- Confidence: low.

### Trucks and retail anecdotes lead recession
- Source: Stanley Druckenmiller — same file (quote: "got anecdotals and stuff that is traditionally LED like trucks and Retail move that up")
- Type: signal
- Rule as testable logic: IF truck freight y/y < 0 (in tool) AND real retail sales 6m change < 0 (proposed) THEN bring forward recession warning (cut equities). Validates truck freight indicator; adds real retail sales.
- Data needed: truck freight (in tool), real retail sales (FRED RRSFS 1992; RSXFS nominal 1992 / RETAIL 1947 deflated by CPI). Retail sales NOT in tool.
- Confidence: medium.

### In hard landings some sectors still win (1974-75 chemicals and oils)
- Source: Stanley Druckenmiller — same file (quote: "there's always stuff to do we had a hard Landing in 74.75 and chemicals and oils and that stuff did great")
- Type: regime map
- Rule as testable logic: IF stagflation state (inflation hot + growth falling; tool state) THEN overweight energy (XLE) and materials (XLB) vs S&P rather than cash only. Test with Ken French 49-industry data 1926+ (Oil, Chems) in stagflation months.
- Data needed: Ken French industry portfolios (1926), XLE/XLB (1998). Sector calls exist in tool; stagflation-specific energy tilt test needed.
- Confidence: medium.

### Earnings growth in a recession beats valuation (secular-growth exception)
- Source: Stanley Druckenmiller — same file (quote: "if you have very good earnings in a recession and they're sustainable ... those stocks will do just fine")
- Type: conflict/caveat
- Rule as testable logic: When cutting equities in recession warnings, keep sectors whose earnings revisions are positive (e.g., semis SOXX in 2023) — test a "keep positive-revision sectors" exception vs blanket cut. Proxy without revisions: keep sectors with 6m relative strength > +10% vs S&P (proposed).
- Data needed: sector ETFs (Select Sector SPDRs 1998; SOXX 2001), sector earnings (not free).
- Confidence: medium.

### Secular moves don't end in 10 months: hold 2-3 years
- Source: Stanley Druckenmiller — same file (quote: "if this is a secular move if this is if this thing is real you just don't have 10 month moves that's not how it works even the dot Tom bubble lasts in the two two and a half years")
- Type: re-entry/exit
- Rule as testable logic: IF a sector/theme ETF rallies > 100% in < 12m on a structural change (proposed) THEN do not exit on overbought alone; hold ≥ 24m unless trend breaks (price < 10-month MA). Test on sector/theme ETFs (tech 1995-2000, energy 2003-08, semis 2023-25).
- Data needed: sector/theme ETF prices.
- Confidence: medium.

### Shorts asymmetric: index shorts a disaster; can lose 10x
- Source: Stanley Druckenmiller — same file (quote: "our shorts have been fine this year except my index shorts which have been a disaster ... if you're dead wrong on a short you can lose 10 times your money")
- Type: position sizing/risk
- Rule as testable logic: Prefer cutting to cash/bonds over outright index shorts (SH/SDS/SPXU); if inverse exposure is used, cap at -20% of portfolio (proposed) and only when trend is down (S&P < 10m MA) and macro warnings are on. Test inverse vs cash in the tool's de-risk states.
- Data needed: SH (2006)/ synthetic short S&P.
- Confidence: high.

### China: stimulus sugar high (6-9 months), long-term undynamic under Xi
- Source: Stanley Druckenmiller — same file (quote: "what they're doing now is very stimulative we're expecting a sugar high and some kind of robust growth there maybe for six or nine months but looking out ... I do not look at them as a big challenge")
- Type: regime map
- Rule as testable logic: IF China announces major stimulus (credit impulse turns up > 2pp of GDP, proposed) THEN tactical overweight China (MCHI/FXI) and China-sensitive commodities (copper) for ≤ 9m, then return to structural underweight. Agrees with Bessent (File 3).
- Data needed: China credit impulse (total social financing; PBoC monthly 2002; free proxies via CEIC not free — use China M1 y/y from FRED MYAGM1CNM189N 1996), MCHI/FXI, copper.
- Confidence: medium.

### Dictators under economic stress more dangerous (Taiwan risk)
- Source: Stanley Druckenmiller — same file (quote: "if I'm right it makes me more fearful of military action because that's when dictators become more dangerous is when they've got a divert attention")
- Type: hedge
- Rule as testable logic: IF China growth slows (China GDP or M1 below trend) AND tension indicators rise (GPR Asia, Taiwan Strait events) THEN hedge with semis puts / underweight Taiwan (EWT) and Korea semis; overweight gold/defence.
- Data needed: GPR country indices (Caldara-Iacoviello, 1985), EWT (2000).
- Confidence: low.

### Japan: deflation ending + shareholder-value reform + dovish BoJ = broad bull market
- Source: Stanley Druckenmiller — same file (quote: "they look like they're solving deflation plus so you're getting nominal growth they've also it's more than just talk they're really into the whole shareholder value thing")
- Type: signal
- Rule as testable logic: IF Japan core CPI > 2% AND BoJ policy rate still ≤ 0.5% (behind the curve) AND breadth strong THEN overweight Japan equities (EWJ/DXJ) vs ACWI for 12-24m; currency weakness supports hedged version (DXJ). Agrees with Bessent.
- Data needed: Japan CPI ex fresh food (FRED JPNCPIALLMINMEI / Statistics Bureau 1970), BoJ policy rate (FRED IRSTCB01JPM156N 1955), EWJ/DXJ, MSCI Japan.
- Confidence: medium-high.

### Japan "biggest value trap in history" (caveat for value rules)
- Source: Stanley Druckenmiller — same file (quote: "every trade I made like five years later on I've lost money in Japan it's been the biggest value trap in history")
- Type: conflict/caveat
- Rule as testable logic: Cheap country CAPE alone is not enough; require nominal-growth/inflation confirmation (Japan 1990-2012). Test country-value rules with and without a nominal GDP growth > 2% filter.
- Data needed: country CAPE (StarCapital / Research Affiliates), nominal GDP by country (OECD/IMF).
- Confidence: medium.

### Uncertain equities -> trade bonds and currencies ("know when not to play")
- Source: Stanley Druckenmiller — same file (quote: "if there's uncertainty inequities usually that's a good time for bonds and currencies they're doing crazy things when the world's blowing up")
- Type: action/instrument
- Rule as testable logic: IF equity regime is unclear (signals mixed; composite in middle) AND rate/FX volatility high (MOVE > 100 or FX realized vol top quartile, proposed) THEN shift risk budget from equities to bond/FX trend positions.
- Data needed: MOVE (Yahoo ^MOVE 1988), FX vol (CBOE EVZ 2008 / realized), tool composite.
- Confidence: medium.

### No fat pitch: preserve cash for the 8-24 month opportunities after a liquidity shift
- Source: Stanley Druckenmiller — same file (quote: "I don't want to blow my cash and being being a horrible mental state being down eight percent making a big bet on something that I didn't have amazing conviction on")
- Type: position sizing/risk
- Rule as testable logic: IF liquidity is turning negative (net liquidity 3m change < 0 and QT ongoing; in tool) AND no extreme signal THEN keep low gross exposure (T-bills) and wait; deploy when extremes appear (e.g., VIX > 35, HY spread > 7%, proposed). Limit drawdown before big bets (if YTD < -8%, cut risk; proposed from quote).
- Data needed: in tool (net liquidity, VIX), HY spread.
- Confidence: medium-high.

---

## File 8 — Stanley Druckenmiller — "Hard Lessons: Invest, then investigate" (Morgan Stanley, 2026-02-27)

### Look ahead 18 months to 3 years, not at today
- Source: Stanley Druckenmiller — Hard Lessons- Stan Druckenmiller- Invest, then investigate (quote: "If you look at today, you're not going to make any money. If you try and look ahead and what might change")
- Type: regime map
- Rule as testable logic: Signals should be forecasting changes over 18-36 months; evaluate rules on 12-36m forward returns, use volatility only for entry points.
- Data needed: none (evaluation design).
- Confidence: high.

### Leadership change: biotech after 4 years of underperformance + momentum turn
- Source: Stanley Druckenmiller — same file (quote: "biotech had been on its butt for like 4 years. I also grew up with technical analysis, and you could see the momentum changing")
- Type: signal
- Rule as testable logic: Sector rotation: IF a sector ETF has underperformed S&P for ≥ 3 years (36m relative return < -30%, proposed) AND its 6m relative momentum turns positive (price > 10m MA and relative 6m > 0) THEN overweight for 12-24m. Test on XBI/IBB, XLE, XME, etc.
- Data needed: XBI (2006), IBB (2001), sector ETFs; Ken French industries 1926.
- Confidence: medium.

### Hot theme rhyming with 1999-2000: rotate into cheap "boring" value with change
- Source: Stanley Druckenmiller — same file (quote: "the AI stuff started to get let me say disturbingly heated and started to at least have some rhyme with what I went through in '99, 2000, and we were looking for other areas")
- Type: signal
- Rule as testable logic: IF narrow leadership/rally speed signals are extreme (in tool) THEN rotate part of equity exposure from cap-weight/tech (QQQ) into equal weight (RSP), value (IWD/VTV), healthcare (XLV), Japan/Korea.
- Data needed: in tool (narrow leadership, rally speed); RSP, VTV (2004), XLV.
- Confidence: medium.

### Sizing is everything (Soros lesson)
- Source: Stanley Druckenmiller — same file (quote: "What I learned from him was sizing. It's not whether you're right or wrong, it's how much you make when you're right and how much you lose when you're wrong.")
- Type: position sizing/risk
- Rule as testable logic: Scale position size with signal strength (e.g., weight ∝ signal z-score, capped), not equal weights; test convex sizing (large on extreme signals, small otherwise) vs linear.
- Data needed: tool signals.
- Confidence: high.

### Current macro portfolio (early 2026): long eclectic equities incl. Japan and Korea
- Source: Stanley Druckenmiller — same file (quote: "we still have big positions in Japan and Korea. Some of them are AI, some of them are not.")
- Type: action/instrument
- Rule as testable logic: IF US equities are at top of valuation range (CAPE top decile; in tool) AND US growth strong THEN hold equity beta preferentially via cheaper markets (Japan EWJ, Korea EWY) rather than S&P. Test: CAPE-relative country allocation (US vs Japan vs Korea).
- Data needed: country CAPE (StarCapital/Barclays), EWY (2000), EWJ (1996), MSCI Korea (1988).
- Confidence: medium.

### Bearish US dollar: top of PPP range + foreigners overloaded in dollars
- Source: Stanley Druckenmiller — same file (quote: "We're bearish on the US dollar, mainly because sort of the top of the historic range in terms of purchasing power. And foreigners are way, way overloaded in dollars.")
- Type: signal
- Rule as testable logic: IF US dollar real effective exchange rate in top decile of its 50y range (proposed) AND US net international investment position < -50% of GDP (foreign holdings heavy; proposed) THEN short USD (UDN, or long FXE/FXY/FXA) and favour unhedged non-US equities/EM for 18-36m.
- Data needed: BIS REER USA (1964 narrow / 1994 broad), Fed real broad dollar (FRED RTWEXBGS 2006; TWEXMPA 1973-2019), NIIP (FRED IIPUSNETIQ 2006 quarterly; BEA annual 1976). Dollar vs 12m high and dollar 12m change in tool; REER level and NIIP NOT.
- Confidence: high.

### Dollar falls "on its own" if foreigners stop net buying (trade balance)
- Source: Stanley Druckenmiller — same file (quote: "it's more like if they don't buy American assets on a net basis because of the trade balance and because the position the dollar will go down on its own")
- Type: signal
- Rule as testable logic: IF net foreign purchases of US long-term securities (TIC) 12m sum < current account deficit (i.e., financing gap; proposed) THEN dollar weakens over next 12m.
- Data needed: TIC net long-term flows (Treasury TIC, monthly 1977), current account (FRED IEABC quarterly 1960). NOT in tool.
- Confidence: medium.

### Long copper futures: consensus, tight supply 8 years, AI/data-centre demand
- Source: Stanley Druckenmiller — same file (quote: "we own copper. It's not a genius trade. It's a big consensus trade. Uh there's no supply coming on meaningful supply very tight for the next 8 years")
- Type: action/instrument
- Rule as testable logic: IF copper is in an uptrend (price > 10m MA; tool has 6m change) AND supply growth is low (mine supply growth < 2% y/y, proposed) THEN hold long copper via rolling front futures (CPER ETF / HG=F) rather than miners (COPX) for 12-36m.
- Data needed: copper (FRED PCOPPUSDM 1990; World Bank 1960; HG=F 2000), CPER (2011), COPX (2010), ICSG mine supply (monthly, paid; USGS annual free). Copper 6m change in tool; trend and supply NOT.
- Confidence: medium-high.

### Commodity exposure via futures, not equities
- Source: Stanley Druckenmiller — same file (quote: "We're not long copper equities as much as we are the till we just keep rolling the front end.")
- Type: action/instrument
- Rule as testable logic: Same as Bessent's oil point: when commodity signal is on, prefer futures/commodity ETFs (front-month roll) over miners; test copper futures vs COPX and FCX-type equity basket after signals, also roll yield (backwardation adds return).
- Data needed: copper futures curve (CME), CPER, COPX.
- Confidence: medium.

### Gold as a geopolitical trade (not monetary)
- Source: Stanley Druckenmiller — same file (quote: "We have some gold. that's mainly a geopolitical trade. It's not so much a monetary trade.")
- Type: hedge
- Rule as testable logic: IF geopolitical risk index (GPR) 3m average is above its 80th percentile (proposed) THEN hold gold (GLD/IAU) 5-10% (proposed) as the hedge; test gold returns conditional on GPR vs conditional on real yields. Contrasts with Crescat (File 9: gold = fiat debasement/monetary) and Bessent (central-bank buying).
- Data needed: GPR (matteoiacoviello.com, 1985 daily/1900 monthly), gold. NOT in tool.
- Confidence: medium.

### Short bonds as the hedge to a long risk portfolio in a growth boom
- Source: Stanley Druckenmiller — same file (quote: "because we're long all these risk assets I just mentioned, we're short bonds. I don't necessarily expect to make money short bonds, but I think we might make a lot if I'm right on the economy")
- Type: hedge
- Rule as testable logic: IF growth is strong and accelerating (economy-stage dial = Expansion/Overheating) AND Fed is cutting or on hold while fiscal stimulus is large (deficit > 5% GDP) THEN pair long risk assets with a short long-duration Treasury position (TBF/TBT or underweight TLT); this hedges the "Fed cuts into a boom -> inflation" scenario.
- Data needed: tool dials; TBF (2009), TBT (2008); deficit.
- Confidence: high (explicit portfolio construction).

### Fed cutting into a booming economy can ignite inflation (esp. with commodities rising)
- Source: Stanley Druckenmiller — same file (quote: "it wouldn't be that unusual if the Fed were to cut into a booming economy for inflation to take off, particularly with what's going on in commodities")
- Type: signal
- Rule as testable logic: IF Fed funds 6m change < 0 AND real GDP growth > 2.5% (or unemployment at/below 12m average) AND commodity index 6m change > +10% (proposed) THEN expect inflation acceleration: underweight long nominals, overweight TIPS/commodities/gold over 12m.
- Data needed: Fed funds (in tool), GDP (FRED GDPC1), commodity index (S&P GSCI / BCOM via Yahoo ^SPGSCI 1970 / DBC 2006; tool has oil and copper 6m).
- Confidence: medium-high.

### Horizon: 18 months to 3 years; volatility is for entry points
- Source: Stanley Druckenmiller — same file (quote: "Most trades I put on, I think in terms of 18 months to 3 years ... The violence that creates is more useful for entry points")
- Type: re-entry/exit
- Rule as testable logic: Once a 12-36m regime signal is on, add on short-term pullbacks (e.g., buy after a 5% 2-week drop within an uptrend, proposed) rather than at signal day; test entry improvement.
- Data needed: daily prices.
- Confidence: medium.

### Crowd right 80% of the time; crowded is fine if trend agrees
- Source: Stanley Druckenmiller — same file (quote: "Soros used to say the crowd's right 80% of the time ... I don't care if a trade is crowded if I think the thesis is right and the trend is with me")
- Type: conflict/caveat
- Rule as testable logic: Do not use positioning/crowding (CFTC COT extremes) as a standalone contrarian signal; use only to time entries. Test: COT net-speculative extremes as contrarian signal vs with-trend filter.
- Data needed: CFTC Commitments of Traders (weekly 1986) — NOT in tool.
- Confidence: medium.

### Technical analysis and "price vs news" have decayed (crowded signals stop working)
- Source: Stanley Druckenmiller — same file (quote: "technical analysis is about 20% as effective today as it was then because no one was using it. But when everybody's using it, it doesn't work anymore")
- Type: conflict/caveat
- Rule as testable logic: Test signal decay: split sample pre/post 2000 for trend and "bad news, price up" rules; downweight rules whose post-2000 Sharpe < 50% of pre-2000.
- Data needed: long price histories (Shiller, Ken French).
- Confidence: high (as caveat).

### Price vs news: bad news + price up = bullish (historically)
- Source: Stanley Druckenmiller — same file (quote: "the company reported horrible earnings, opened down in the after market, and then was up 10% the next day, almost guaranteed to be higher 6 months later")
- Type: signal
- Rule as testable logic: Macro analogue: IF a major negative macro data surprise (e.g., payrolls miss > 1 sd) and S&P closes up that day THEN bullish for 6m. (He says this decayed after 2000.)
- Data needed: economic surprise (Citi index paid; free proxy: payrolls vs consensus — not free; use ALFRED first releases), S&P daily.
- Confidence: low (decayed per speaker).

### US backdrop early 2026: strong economy, fiscal stimulus, Fed cutting, valuations high
- Source: Stanley Druckenmiller — same file (quote: "the US economy is already strong, and it's going to get much stronger cuz we're looking at the big beautiful bill ... We're not undervalued. We're toward the top of the valuation range")
- Type: regime map
- Rule as testable logic: IF strong growth + fiscal stimulus + Fed easing + top-decile valuation THEN be long equities but diversified across countries/sectors (not cap-weight US concentration), short duration, long commodities (copper), short USD.
- Data needed: tool dials, CAPE (in tool), deficit.
- Confidence: medium.

### Don't sell a secular winner on a big gain (Nvidia regret)
- Source: Stanley Druckenmiller — same file (quote: "It had gone from 150 to 800. I was long-term on it. I couldn't deal with it. And I sold it and then it was 1400 like 5 weeks later")
- Type: re-entry/exit
- Rule as testable logic: Exit secular-trend positions only on a trend break (e.g., close < 10-month MA), not on gain size. Test on sector/country trends.
- Data needed: prices.
- Confidence: medium.

### Emotional drawdown control: move on after mistakes
- Source: Stanley Druckenmiller — same file (quote: "when you have these drawdowns ... just get over it and move on")
- Type: position sizing/risk
- Rule as testable logic: Systematic rule follows signals after drawdowns (no discretionary override); optional test: cooling-off — after a -10% strategy drawdown, keep exposure rules unchanged rather than cutting.
- Data needed: strategy P&L.
- Confidence: low.

---

## File 9 — Crescat Capital (Kevin Smith presenting; Quinton Hennigh referenced) — "A Brief World Economic History For Gold, Silver, and Fiat Money" (2024-05-06)

### Unsustainable deficits -> intractable inflation -> fiat debasement -> gold/silver/copper
- Source: Crescat Capital (Kevin Smith) — A Brief World Economic History For Gold, Silver, and Fiat Money (quote: "unsustainable debt and government deficits in developed economies that make inflation AR pressures intractable and Fiat currencies more susceptible to the basement")
- Type: regime map
- Rule as testable logic: IF developed-market deficits > 5% of GDP AND real policy rate < 1% (proposed; fiscal dominance) THEN overweight gold (GLD), silver (SLV) and copper (CPER) vs Treasuries for 24-36m.
- Data needed: deficit (FRED), real fed funds (FEDFUNDS - core PCE), gold (World Bank 1960), silver (World Bank 1960; SLV 2006), copper. Deficit and precious metals NOT in tool.
- Confidence: medium.

### Metals supply constraints vs rising demand (infrastructure, reshoring, green energy)
- Source: Crescat Capital — same file (quote: "there are critical Metal Supply constraints under Rising demand given us government's spending initiatives geared towards commodity hungry infrastructure projects reshoring")
- Type: signal
- Rule as testable logic: IF mining capex has been falling for ≥ 5 years (underinvestment; proposed) AND metal prices are in uptrend THEN overweight industrial metals (DBB, CPER) for multi-year horizon.
- Data needed: global mining capex (S&P Global Market Intelligence, paid; free proxy: miners' capex from annual reports / USGS), DBB (2007), LMEX index; World Bank metals index (1960).
- Confidence: medium.

### Gold breaks to new all-time high while miners lag -> miners catch-up (operating leverage)
- Source: Crescat Capital — same file (quote: "gold Has Broken out to new all-time Highs but the exploration index ... it has about 7x performance to get back to its prior all-time high back in in 2007")
- Type: signal
- Rule as testable logic: IF gold makes a new all-time high (or > 12m high) AND gold-miners/gold ratio (GDX/GLD or GDXJ/GLD) is in bottom decile of 10y range (proposed) THEN overweight miners (GDX/GDXJ) vs gold for 12-24m. Test 2001-2011, 2019-2020, 2024-2026.
- Data needed: GDX (2006), GDXJ (2009), GLD, Barron's Gold Mining Index (BGMI, 1938 weekly; via Barron's/ Nasdaq data), XAU index (1983), TSX Venture composite (^JX / 2001+). NOT in tool.
- Confidence: medium.

### Gold/miners boom when nifty-fifty-style growth bubble ends with rising inflation and rates (1973-74)
- Source: Crescat Capital — same file (quote: "in 7374 The Baron's gold mining index would go up 5x ... the S&P 500 was down 50% in those same two years ... Rising inflation Rising interest rates")
- Type: regime map
- Rule as testable logic: IF (a) concentrated mega-cap growth leadership (narrow leadership in tool) AND (b) core CPI y/y rising and 10y yield 12m change > +100bp THEN underweight S&P/growth, overweight gold and gold miners for 24m (stagflation playbook).
- Data needed: in tool (narrow leadership, core CPI, 10y change); gold miners index (BGMI 1938 / XAU 1983 / GDX 2006).
- Confidence: medium.

### Fiat money printing to fund wars -> hyperinflation (Yuan dynasty)
- Source: Crescat Capital — same file (quote: "would go on to suffer from hyperinflation after issuances of excessive amounts of paper currency to fund their Wars and expansionism while depleting all of their silver")
- Type: regime map
- Rule as testable logic: IF central-bank financing of government (Fed Treasury holdings growth > nominal GDP growth by > 10pp y/y, proposed) during war/fiscal expansion THEN overweight real assets (gold, commodities, TIPS) vs nominal bonds for 24m+.
- Data needed: Fed Treasury holdings (FRED TREAST 2002; Fed H.4.1 history 1914 via FRASER), nominal GDP (FRED GDP).
- Confidence: low (historical narrative).

### Metal-backed money underpinned prosperity (Song); silver standard (Ming)
- Source: Crescat Capital — same file (quote: "these Bank notes were exchangeable for metal coins the money was backed by metal and that was a key uh element of the prosperity")
- Type: conflict/caveat
- Rule as testable logic: Narrative only; no direct test. Implies gold's value rises with loss of confidence in unbacked money — proxy test: gold vs 12m change in central-bank balance sheets/GDP.
- Data needed: Fed assets/GDP (WALCL/GDP 2002; FRASER for earlier).
- Confidence: low.

### Nixon de-peg (1971) -> gold took off
- Source: Crescat Capital — same file (quote: "the dollar had been deeg from gold at this point by Nixon and it would take off")
- Type: regime map
- Rule as testable logic: IF a monetary-regime break weakens the reserve currency's anchor (event: de-peg, explicit dollar-weakening policy, reserve freeze) THEN overweight gold for 24-36m. Test on 1971, 2008 (QE), 2022 (Russia reserve freeze) — links Petraeus/Bessent.
- Data needed: gold (World Bank 1960), event list.
- Confidence: medium.

### Mining-equity fraud risk: Comstock, Bre-X — prefer diversified ETFs
- Source: Crescat Capital (citing Mark Twain) — same file (quote: "a gold mine is a hole in the ground with a liar standing on top of it")
- Type: position sizing/risk
- Rule as testable logic: For the tool (no single stocks), express miners via diversified ETFs (GDX/GDXJ/SIL/COPX) and cap junior-miner exposure (GDXJ) at ≤ 1/3 of the metals sleeve (proposed) because of fraud/dilution risk.
- Data needed: GDX, GDXJ, SIL (2010), SILJ (2012).
- Confidence: medium.

### M&A cycle as majors underinvested in exploration -> juniors re-rate
- Source: Crescat Capital — same file (quote: "there is an m&a cycle coming because the majors have underinvested in Exploration for so long ... they're going to have to come to the Juniors")
- Type: signal
- Rule as testable logic: IF gold price high AND gold-miner exploration budgets low (S&P Global exploration budget falling, proposed) THEN overweight junior miners (GDXJ) vs majors (GDX) for 12-24m.
- Data needed: S&P Global Market Intelligence exploration budgets (annual, paid summary free), GDXJ/GDX ratio.
- Confidence: low (sales pitch).

### Mining stocks lag metals because of sector reputation (persistent discount)
- Source: Crescat Capital — same file (quote: "the reputation that the mining industry has ... it's an extra hurdle that that really explains why this industry is still still so depressed")
- Type: conflict/caveat
- Rule as testable logic: Caveat to the miners catch-up rule: miners may stay cheap vs metal for years (2011-2023). Require miners' relative momentum (GDX/GLD 6m change > 0) before overweighting miners.
- Data needed: GDX, GLD.
- Confidence: medium.

### Silver-rich economies / silver inflows fuel growth (historical); silver as monetary metal
- Source: Crescat Capital — same file (quote: "silver was in high demand during the Ming period as became the standard currency replacing paper money")
- Type: action/instrument
- Rule as testable logic: Include silver alongside gold in the debasement sleeve; test gold/silver ratio rule: IF gold/silver ratio > 80 (proposed) AND copper/industrial metals rising THEN overweight silver vs gold for 12m.
- Data needed: silver (World Bank 1960; SLV 2006; SI=F 2000), gold. NOT in tool.
- Confidence: low-medium.

### Speculation in megacap tech/AI/crypto is a product of fiat printing
- Source: Crescat Capital — same file (quote: "Mega cap Tech Stock Investing and and the excitement over Ai and cryptocurrencies is ... we think highly speculative world because of of all the the Fiat money printing")
- Type: signal
- Rule as testable logic: IF M2 growth or Fed balance-sheet growth is high (top quartile) AND narrow leadership extreme THEN expect later reversal in favour of hard assets once money growth slows (M2 y/y turns < 0). Contrasts with Druckenmiller ("AI is real ... unlike crypto").
- Data needed: in tool (M2 growth, narrow leadership, net liquidity).
- Confidence: low.

---

## Cross-speaker themes in this batch

### Country / EM rules
- Japan secular bull (Bessent, Druckenmiller): deflation ending + governance reform + BoJ behind the curve -> long Japan equities (DXJ hedged when yen weak). Caveat: Japan was a 20-year value trap (Druckenmiller).
- Japan/Korea as the cheaper way to hold equity beta when US valuations are top-decile (Druckenmiller 2026).
- China: stimulus = 6-9m sugar high only; structurally underweight under Xi (Bessent, Druckenmiller); concentration/sanction-risk cap (Bessent "Russia day").
- India / SE Asia / Mexico gain from supply-chain migration (Petraeus); Indonesia–nickel link (Garrett).
- Floating-rate-mortgage countries (UK, Australia, Canada, Sweden, Korea) cannot sustain hikes into falling house prices (Bessent, ERM 1992).
- Dollar: bearish when REER at top of range and foreigners overloaded (Druckenmiller); weakens when ECB more hawkish than Fed (Tropin); not displaced by sanctions (Petraeus).

### Commodity cycle
- Copper long via rolling futures: no new supply for ~8 years + AI/data-centre demand (Druckenmiller); metals supply constraints + reshoring/infrastructure (Crescat).
- Prefer commodity futures over producer equities when equities price the mid-curve (Bessent oil; Druckenmiller copper). Contrast: Crescat argues miners will catch up with gold (operating leverage).
- Diesel/refined products as a sharper inflation/growth shock gauge than crude (Guha).
- Sanction-driven commodity spikes may fade (Gurley) vs sanctions bite over time (Petraeus).

### Inflation / stagflation playbooks
- Stagflation (rising inflation + rising rates after a growth bubble): gold and gold miners up 5x, S&P -50% (1973-74, Crescat); energy and chemicals win in hard landings (Druckenmiller 1974-75).
- Fed cutting into a boom with rising commodities -> inflation risk -> short long bonds (Druckenmiller 2026; Bessent 2024 on "jumbo cut").
- Tariffs are a one-off level shock that drops out after ~12 months (Guha) vs tariffs inflationary and retaliatory (Gurley/Reagan, Garrett).
- Inflation is an ocean liner; cuts are over-priced (Tropin).

### Liquidity
- Net liquidity components: TGA drawdown during debt ceiling = tailwind; TGA rebuild + QT = drain (Druckenmiller 2023). Foreign CB intervention (BoJ YCC defence) can add liquidity.
- COVID liquidity stock (M2 above trend) delays recessions (Druckenmiller).
- Warsh-era Fed: QE only in seizures; no forward guidance -> more rate volatility (Guha).

### Credit / banks
- Banks' duration losses + card/CRE losses in a recession; credit tightening 6-9m after shock (Druckenmiller); SLOOS-based bank short after regulatory overreaction (Bessent 1990).
- HY spread blowout -> expect backstop -> buy credit (Guha on Warsh QE in seizures).

### Yield curve / rates
- Steepening from deep inversion signals recession arrival (Tropin).
- Zero/negative term premium = duration risk unpriced (Tropin); 10y > 5% hurts non-AI economy, > 6% threatens AI capex (Guha); mortgage > 7% = housing ground zero.
- Treasury buybacks / bill-heavy issuance aimed at capping yields hurt credibility (Guha).

### Fiscal / debt
- Pro-cyclical deficits (deficit > 5% GDP at low unemployment) -> rates up (Bessent 7% deficit, Druckenmiller trillion-dollar deficit at 3.5% unemployment, Guha 6% deficit + AI issuance).
- Not a 3-6 month trade (Druckenmiller); fiscal dominance -> gold (Crescat).

### Geopolitics-to-asset mappings
- Geopolitics now determines economics (Petraeus) -> GPR index regime flag.
- Gold as a geopolitical hedge (Druckenmiller) vs monetary hedge (Crescat) vs central-bank reserve diversification (Bessent).
- Export bans (rare earths) more dangerous than tariffs (Gerstner); export controls leak (Gurley).
- Middle East war does not imply higher oil (Bessent caveat).
- Economic stress makes dictators more dangerous (Druckenmiller, Taiwan risk).

### Hedging methods actually used
- Short bonds as the hedge for a long-risk book in a growth/inflation boom (Druckenmiller 2026).
- Buy cheap options when implied vol is suppressed (Bessent yen puts at 4-6 vol).
- Futures hedges on equity books (Bessent at Soros).
- Trend-following / CTA sleeve as crisis diversifier (Tropin: 1987, 2000-02, 2008).
- Long bonds on equity crash days when inflation is not the issue (Tropin 1987).
- Avoid outright index shorts (Druckenmiller: "index shorts have been a disaster").
- Gold (Gerstner: safe-haven flight 2025; Druckenmiller geopolitics; Bessent central-bank buying).

### Position sizing
- Trade in thirds; size by YTD P&L ("earn the right"); reset each January; take down risk mid-December (Bessent).
- Never concentrated + illiquid + leveraged; exit part within 24-72h (Bessent).
- Cut to the "bottom third" of normal risk under policy uncertainty (Gerstner).
- Sizing > being right (Druckenmiller/Soros); don't bet big without "amazing conviction"; don't be down 8% on a mediocre bet.
- Daily risk meeting + stress tests (Tropin).
- Add to strategies after slumps, trim after big years (Bessent/Commonfund).

### Contradictions / tensions inside this batch
1. Gold driver: geopolitical (Druckenmiller) vs fiat debasement (Crescat) vs CB reserve accumulation (Bessent) — test each conditioning variable.
2. Dollar: weaponisation won't displace it (Petraeus) vs bearish dollar from overvaluation and foreign over-allocation (Druckenmiller 2026) vs Bretton-Woods-style realignment (Bessent).
3. Sanctions/export controls: bite more over time (Petraeus) vs porous, spectacular failure (Gurley).
4. Tariff inflation: transitory level effect (Guha) vs durable inflation + retaliation (Gurley, Garrett).
5. Recession timing: delay raises hard-landing odds (Druckenmiller 2023) vs soft landing achieved (Guha on Powell).
6. Commodity expression: futures over equities (Bessent, Druckenmiller) vs junior miners' leverage (Crescat).
7. AI: real, secular, hold 2-3 years (Druckenmiller 2023) vs AI "disturbingly heated, rhymes with 1999" (Druckenmiller 2026) vs fiat-fuelled speculation (Crescat).
8. Contrarianism: overrated, crowd right 80% (Druckenmiller) vs Bessent "imagine what never happened" / buy when policy hits the wall.
9. QE efficacy: did support demand (Guha) vs only inflated asset prices (Eisman); Warsh: only in seizures.
10. Treasury buybacks: signal of less long supply (lower term premium) vs EM-style credibility loss (higher term premium) — both from Guha.

---

## Batch summary — 10 most important testable ideas

1. **Supply-shock regime switch for the de-risk asset** (Guha, Gerstner, Druckenmiller): when stocks, bonds and oil/yields move against stocks together (60d corr of S&P with oil and with 10y-yield changes < -0.3, or VIX > 30 with dollar falling and 10y rising), use T-bills/gold instead of long Treasuries; when inflation is not the cause, long Treasuries remain the crash hedge (Tropin 1987).
2. **Fed cutting into a boom + rising commodities -> short/underweight long bonds, own TIPS/commodities/gold** (Druckenmiller 2026, Bessent 2024). Testable with Fed funds 6m change < 0, GDP > 2.5%, commodity index 6m > +10%.
3. **Pro-cyclical deficit rule** (Bessent, Druckenmiller, Guha, Crescat): deficit > 5% GDP with unemployment < 4.5-5% -> lower long-duration weight, higher gold/real-asset weight; explicitly not a ≤ 6-month signal.
4. **Trend-following sleeve sized by central-bank activity** (Tropin): allocate more to time-series momentum across bonds, FX, commodities, equity indexes when the sum of |policy-rate changes| of Fed+ECB+BoE over 12m is large; it is the crisis diversifier of 1987/2000-02/2008/2022.
5. **Dollar valuation + foreign over-allocation -> short USD, own non-US (Japan, Korea, EM) unhedged** (Druckenmiller; Bessent PPP framework; Tropin rate-differential trigger). Inputs: REER percentile, NIIP, TIC flows, US-German 2y spread change.
6. **Japan reflation rule** (Bessent, Druckenmiller): core CPI > 2% with BoJ still ≤ 0.5% and breadth strong -> overweight Japan (hedged DXJ if yen weakening); require nominal-growth filter for any country-value rule (Japan value-trap caveat).
7. **Copper via rolling futures when in uptrend with constrained supply** (Druckenmiller, Crescat); generalised: express commodity views via futures, not producer equities (Bessent oil), unless miners/metal ratio is extreme and turning (Crescat).
8. **Gold conditioning test** (Druckenmiller GPR, Bessent central-bank buying, Crescat fiscal dominance, Gerstner safe-haven flow): hold gold when GPR high, CB net purchases above 10y average, or deficit > 5% with real rate < 1%; test which driver carries the edge.
9. **Policy-uncertainty sizing** (Gerstner): EPU / trade-policy-uncertainty above 90th percentile -> cut equity risk to ~1/3 of normal; > 12 weeks of high uncertainty -> expect earnings downgrades; restore after EPU falls below 75th percentile.
10. **Post-tightening credit-event window** (Druckenmiller 2023, Bessent "brick wall"): after Fed funds +300bp in 12m from extreme valuations, expect credit events for 6-24m (cut equities/HY, underweight banks/CRE/REITs); then buy when policy reverses at extremes (HY > 7-8%, VIX > 35-40, backstop announced).

Also notable: 10y > 5% / mortgage > 7% level thresholds for small caps, homebuilders, REITs (Guha); 2s10s steepening ≥ 50bp from inversion trough as recession-arrival signal (Tropin); equity earnings yield minus T-bill < 1pp -> underweight stocks (Tropin TINA); cheap-vol rule: buy puts/options when implied vol is bottom-decile (Bessent); sizing in thirds with YTD-P&L scaling and mid-December risk reduction (Bessent); avoid outright index shorts, prefer cash (Druckenmiller).

---

## Data requests (series needed that are NOT in the existing tool list)

Rates / Fed / fiscal
- ACM 10y term premium LEVEL (tool has 12m change) — NY Fed, daily 1961.
- 2y Treasury minus fed funds (market-implied cuts) — FRED DGS2 (1976), DFF (1954).
- 2s10s change from trailing 12m trough (steepening) — FRED T10Y2Y (1976).
- 10y yield and 30y mortgage LEVEL thresholds — FRED DGS10 (1962), MORTGAGE30US (1971).
- ICE BofA MOVE index — Yahoo ^MOVE (1988).
- NY Fed HLW r* — quarterly 1961.
- Core PCE months-above-2% counter — FRED PCEPILFE (1959).
- Federal deficit % GDP — FRED FYFSGDA188S (annual 1929), MTSDS133FMS (monthly 1980).
- Federal debt/GDP — FRED GFDEGDQ188S (1966).
- Federal net interest / receipts — FRED A091RC1Q027SBEA, W006RC1Q027SBEA (1947).
- Treasury bill share of marketable debt, refunding coupon sizes, buyback schedule — Treasury MSPD (1950s), Treasury refunding archive.
- Treasury General Account — FRED WTREGEN (2002), Daily Treasury Statement (2005); TGA rebuild projections (quarterly refunding).
- Fed Treasury holdings — FRED TREAST (2002); FRASER H.4.1 (1914).
- M2 gap vs 2010-19 log trend — FRED M2SL (1959).
- Policy rates: ECB deposit rate FRED ECBDFR (1999), BoE Bank Rate (BoE/FRED BOERUKM), BoJ FRED IRSTCB01JPM156N (1955), BIS policy rate database (1946).
- German 2y yield — Bundesbank (1972) / ECB yield curve (2004); OAT-Bund 10y spread FRED IRLTLT01FRM156N / IRLTLT01DEM156N (1960s).
- Bank Treasury holdings — FRED TASACBW027SBOG (1973).
- TIPS real yield/breakevens and ETFs — FRED DFII10, T10YIE (2003); TIP (2003), IEF (2002), USFR/TFLO (2014), SHY/IEI (2002/2007), TBF (2009).

Credit / banks
- HY OAS — FRED BAMLH0A0HYM2 (1996); HYG (2007), LQD (2002).
- Fed Senior Loan Officer Survey C&I and CRE — FRED DRTSCILM, SUBLPDRCSC (1990).
- CRE delinquency rate — FRED DRCRELEXFACBS (1991); CRE prices (FRED BIS COMREPUSQ159N / Green Street CPPI paid).
- FDIC unrealised securities losses — FDIC QBP (2008).
- Regional banks/financials ETFs — KRE (2006), KBE (2005), XLF (1998).

Growth / uncertainty / earnings
- Economic Policy Uncertainty index — FRED USEPUINDXD (daily 1985), USEPUINDXM.
- Trade Policy Uncertainty index — Caldara et al. (1960).
- Geopolitical Risk index (global + country) — Caldara-Iacoviello (1900 monthly / 1985 daily).
- NY Fed Global Supply Chain Pressure Index (1997).
- US effective tariff rate — FRED customs duties B235RC1Q027SBEA / imports IMPGS (1947); Yale Budget Lab (2025).
- S&P forward EPS, revisions ratio, forward P/E — S&P Global EPS spreadsheet (~1988)/I/B/E/S (paid); Shiller earnings (1871) for earnings-yield-minus-bill gap; T-bill FRED TB3MS (1934).
- SPF Anxious Index (Philly Fed, 1968).
- Philly Fed future capex index — FRED CEFDFSA066MSFRBPHI (1968).
- Real retail sales — FRED RRSFS (1992); retail inventories/sales FRED RETAILIRSA (1992).
- Private nonresidential fixed investment — FRED PNFI (1947); Treasury and IG corporate issuance — SIFMA (1996).
- Housing starts — FRED HOUST (1959).
- Fed Distributional Financial Accounts (1989).
- Core goods CPI — FRED CUSR0000SACL1E (1956).
- CFTC Commitments of Traders (1986).

FX / external
- BIS real effective exchange rates (narrow 1964, broad 1994); Fed real broad dollar FRED RTWEXBGS (2006) / TWEXMPA (1973-2019).
- US NIIP — FRED IIPUSNETIQ (2006) / BEA annual (1976); current account FRED IEABC (1960).
- TIC net long-term flows (1977).
- OECD PPP (1960); Big Mac index (1986).
- FX spot: FRED DEXUSEU (1999), DEXGEUS (1971-2001), DEXJPUS, DEXUSUK, DEXUSAL, DEXCAUS, DEXSDUS (1971), DEXKOUS (1981), DEXSZUS (1971); FX ETFs FXE/FXY/FXF/FXA (2005-2007), UDN (2007).
- FX implied vol — CBOE EVZ (2008); OVX (2007), GVZ (2008), VXEEM (2011).
- BIS residential property prices (1970s).
- US petroleum net exports — EIA (1973).
- China M1 / credit impulse — FRED MYAGM1CNM189N (1996), PBoC TSF (2002); China imports FRED XTIMVA01CNM667S; China auto exports (CAAM ~2010).
- Japan CPI — FRED JPNCPIALLMINMEI (1955).

Commodities
- Gold — World Bank Pink Sheet monthly (1960), GLD (2004), GC=F (2000); central-bank gold purchases — World Gold Council (2000), IMF IFS reserves.
- Silver — World Bank (1960), SLV (2006); gold/silver ratio.
- Copper level/trend and futures — FRED PCOPPUSDM (1990), World Bank (1960), HG=F (2000), CPER (2011), COPX (2010); mine supply (ICSG paid / USGS annual).
- Nickel — World Bank (1960).
- Broad commodity index — S&P GSCI (^SPGSCI 1970), BCOM, DBC (2006), DBB (2007).
- WTI futures curve (front vs 12th) — EIA RCLC1-4 (1983), CME; USO (2006), USL (2007), BNO (2010).
- Diesel / ULSD / jet fuel — EIA (1986/1994), FRED GASDESW (1994), DJFUELUSGULF (1990); crack spread.
- Natural gas Henry Hub FRED DHHNGSP (1997); TTF / Europe gas — World Bank (1960).
- Coal — World Bank (1960).
- Uranium — IMF PURANUSDM (1980); URA (2010), URNM (2019); IAEA PRIS construction starts.
- Rare earths — REMX (2010).
- Gold miners — GDX (2006), GDXJ (2009), XAU (1983), Barron's Gold Mining Index (1938), TSX Venture (^JX); SIL/SILJ (2010/2012).
- Mining exploration budgets (S&P Global, annual).

Equity country / sector instruments
- MSCI country ETFs: EWJ (1996), DXJ (2006), EWY (2000), EWT (2000), MCHI (2011), FXI (2004), KWEB (2013), INDA (2012), EWW (1996), VNM (2009), EIDO (2010), EWG/EWQ/EWU/EWA/EWC/EWD (1996), VGK/EZU (2005/2000), EEM (2003), EMXC (2017), EFA (2001), ACWX (2008); underlying MSCI country indices (1970/1988).
- Country CAPE (StarCapital / Research Affiliates / Barclays, ~1980s).
- Sectors/themes: XLE, XLB, XLI, XLY, XLP, XLV (1998); XOP (2006); ITB (2006), XHB (2006); VNQ (2004); IWM (2000); RSP (2003); VTV (2004); IYT (2004); JETS (2015); CRAK (2015); ITA (2006); XBI (2006), IBB (2001); SOXX (2001), SMH (2000); CARZ (2011), DRIV (2018), KARS (2018), LIT (2010); XRT (2006); Ken French 49 industries (1926).
- Trend/managed futures: AQR Time Series Momentum factor (1985), SG CTA/Trend index (2000), DBMF (2019), KMLM (2020).
- Inverse equity: SH (2006) (for testing inverse vs cash).
- World trade volume — CPB World Trade Monitor (1991).
- World Bank Worldwide Governance Indicators (1996) for country political-risk caps.
- Event lists (manual): sanctions/reserve freezes, export controls/bans, China stimulus announcements, central-bank governor changes, debt-ceiling X-dates, war onsets, consumer transfer restarts.
