---
source_id: MT187
title: "Treasury Markets not as “Safe” as You Think - Systematic Investor - Ep.414"
date: 2026-08-23
channel: "Top Traders Unplugged"
url: 
words: 12177
claims: 58
added_by_crosscheck: 13
corrections: 0
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Mark Rzepczynski (co-host, systematic/VUCA-focused quant, caption 'Mark Ramsinski')", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Treasury Markets not as “Safe” as You Think - Systematic Investor - Ep.414

**Speakers:** Mark Rzepczynski (co-host, systematic/VUCA-focused quant, caption 'Mark Ramsinski'); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Top Traders Unplugged Systematic Investor, Aug 2026: Mark and Niels discuss market 'rumblings' (leverage blowups, Korean bubble, yen intervention, stock issuance), commodity buffer stocks, and the Treasury buyback and market plumbing (primary dealer capacity, hedge fund basis trade, repo leverage, March 2020). Also trend-following style taxonomy (LGT paper), blending styles as pods, tick size and short-term trend, and a tribute to Victor Niederhoffer.

**Approach:** trend following, Treasury market plumbing, basis trade, commodity inventories, VUCA, research method, CTA

**Cross-check completeness estimate of first read:** 0.82 - the first reader captured the main Treasury-plumbing chain, index numbers and the trend-style taxonomy; it missed supporting analogies (cocoa, 2000-02 buyback, 1980s dealer failures), the dealer-spread mechanism, CTD switching, Niels's caveats on style labels and costs, and the Niederhoffer ecosystem/Taleb framing.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 3 | intro; 'rumblings' list: leverage blowup, Korean stock bubble, issuance, yen intervention |
| C02 | 3 | concentrated bets at market makers; 177% single stock move and risk; stock vs futures volatility |
| C03 | 4 | market maker correlation risk; copper spread squeeze and commodity buffer stocks |
| C04 | 3 | oil inventories, China stock draw, blowoff risk; trend barometer; VUCA volatility view |
| C05 | 3 | complexity and ambiguity create trends; performance figures; Treasury action at long end |
| C06 | 2 | Treasury auction size, on-the-run vs off-the-run liquidity, buyback programme |
| C07 | 3 | buyback is composition change not QE; timing after 5.34% long bond; debt maturity management |
| C08 | 3 | buybacks as stabiliser; who controls long end; Treasury plumbing and primary dealers |
| C09 | 3 | dealer capital constraints (SLR), hedge funds as marginal Treasury holders, basis trade |
| C10 | 3 | basis trade leverage via repo; repo shocks spill to bonds; HFT liquidity can vanish |
| C11 | 2 | March 2020 Treasuries not safe; trust cycle; agenda for research segment |
| C12 | 2 | Arthur Sepp LGT paper: three trend-following styles |
| C13 | 2 | style differences and how many trend managers to hold; blending styles |
| C14 | 3 | podification of trend following; netting of fees; teaser on short-term trend research |
| C15 | 3 | tick size and short-term trend following; plumbing matters; Niederhoffer introduction |
| C16 | 3 | Niederhoffer research legacy: overreaction, clustering, insider trades, empiricism |
| C17 | 0 | Niederhoffer lineage; wrap-up and plugs |
| C18 | 0 | outro and legal disclaimer, nothing actionable |

## Claims

### C01
- **Mark Rzepczynski** A fund losing 67% in one month is a reminder that leverage can wipe out capital; such episodes are 'rumblings' of fragile markets.  #mech/risk_management _(time-bound view)_
  > someone loses 67% in a single month. Well, we find out once again that uh you know uh leverage hurts or leverage kills.
  asset: multi · horizon: months · conditions: leveraged concentrated positions · testable: no - anecdote · confidence: medium
  ^MT187-C01-1
- **Mark Rzepczynski** Rising equity issuance with new issues reversing is a sign of an overvalued market (late-stage bubble), and a Korean stock bubble just collapsed after a huge run-up.  #mech/overshoot _(time-bound view)_
  > we're seeing some of those new issues sort of uh have big reversals and usually it's a sign of an overvalued market when there's more stock issuance
  indicator: equity issuance volume; new issue performance · asset: equities · direction: caution on equities · horizon: months · testable: yes - issuance vs forward returns is testable · confidence: medium
  ^MT187-C01-2
- **Mark Rzepczynski** Joint Japan MoF and Fed yen intervention signals authorities dislike the market direction, but FX intervention usually fails to reverse trends.  #mech/policy_reaction _(time-bound view)_
  > Intervention usually doesn't work in the foreign exchange markets, but that hasn't stopped the governments to say like we've got to arrest the uh what is going on in the yen market
  indicator: FX intervention (yen) · asset: fx · direction: yen trend likely persists after intervention · horizon: weeks · testable: yes - event study of intervention · confidence: medium
  ^MT187-C01-3

### C02
- **Niels Kaastrup-Larsen** A large multi-strategy/market-maker firm reportedly lost $15bn on a single concentrated bet after earning $40bn, suggesting hidden concentration despite many teams and good risk management.  #mech/crowding_positioning _(time-bound view)_
  > But 15 out of 40 is a big deal
  asset: equities · horizon: months · conditions: multi-strategy pod shops · testable: no - speculation from headlines · confidence: low
  ^MT187-C02-1
- **Niels Kaastrup-Larsen** Trend followers or shorts in single stocks face gap risk of order 177% in a day (Moderna), much more than normal futures, so stock trading needs explicit tail-risk limits.  #mech/risk_management _(time-bound view)_
  > if you were a trend follower having uh trading individual stocks potentially it could have been um you know in a downtrend and suddenly it goes up by 177%. What does that tell you um from a riskmanagement perspective?
  indicator: single-stock daily move · asset: equities · horizon: days · conditions: single-stock futures or individual stocks · testable: partly - gap statistics available · confidence: medium
  ^MT187-C02-2
- **Mark Rzepczynski** Single stocks are generally more volatile than futures markets, though some futures (grains, indices) can still move 20-30% in a month.  #mech/risk_premium
  > there's no question that the individual stock volatility can be much uh greater than what you sort of see in in most futures markets.
  asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT187-C02-3
- **Niels Kaastrup-Larsen** The new listing of single-stock futures may draw more systematic futures managers into single-name trading, which exposes them to gap risk far beyond that of traditional futures markets.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > I think now more recently we've had um single stock equities come out as futures. So there might be even more people from our industry attracted to that area.
  indicator: single-stock futures · asset: equities · conditions: relevant for trend followers adding single stocks to a futures universe · testable: partly - jump-risk statistics of single-stock futures versus index futures · confidence: medium
  ^MT187-C02-X1
- **Mark Rzepczynski** Huge single-stock run-ups in AI names (Micron from under 400 in April to about 1,200) look like excessive speculation; when markets normalize the reversal will hurt late buyers, so such moves are a 'rumbling' of fragility.  #mech/overshoot _(added by sonnet-xhigh cross-check, time-bound view)_
  > It could be excessive speculation which is good for the person who is the buyer but you say that what happens when the markets start to normalize you're
  indicator: AI stock price run-ups (Micron) · asset: equities · direction: reversal risk in speculative AI stocks · horizon: months · conditions: when speculation normalizes · testable: partly - after-the-fact reversals of extreme multi-month run-ups · confidence: medium
  ^MT187-C02-X2

### C03
- **Mark Rzepczynski** Modern market makers take speculative, correlation-based hedge bets across hundreds of stocks, so if historical correlations break they can suffer large losses.  #mech/crowding_positioning _(time-bound view)_
  > the market makers that we have that have been very profitable you know are very different than the market makers of old because they might be taking speculative positions.
  indicator: cross-stock correlations · asset: equities · horizon: weeks · conditions: correlation regime break · testable: partly · confidence: medium
  ^MT187-C03-1
- **Mark Rzepczynski** Low commodity inventories remove the buffer stock, so users pay almost any price and extreme moves and backwardation follow.  #mech/liquidity_flows
  > When inventory goes very low, uh then there's a a decrease in what we call the buffer stock.
  indicator: warehouse inventory levels; futures curve backwardation · asset: commodities · direction: long commodity with extreme backwardation · horizon: weeks · conditions: low inventories · testable: yes - inventory-conditioned returns · confidence: high
  ^MT187-C03-2
- **Mark Rzepczynski** Inventory levels help anticipate curve shape changes (contango to backwardation) and front-end volatility, information not contained in the price trend alone.  #mech/slow_reaction
  > Looking at inventory levels is critical to understand whether there's going to be a change from contango or to backradation or if there's more whippiness in the front end of a lot of these commodity curves.
  indicator: commodity inventories vs curve shape · asset: commodities · horizon: months · testable: yes · confidence: medium
  ^MT187-C03-3
- **Niels Kaastrup-Larsen** A copper spot-to-3-month spread squeeze with the biggest weekly LME inflow since 2020 indicated tight physical supply.  #mech/liquidity_flows _(time-bound view)_
  > copper squeeze draws biggest weekly flow to LME shed since 2020.
  indicator: LME copper spot to 3-month spread · asset: commodities · horizon: days · testable: partly - LME stock and spread data · confidence: low
  ^MT187-C03-4
- **Mark Rzepczynski** Cocoa two years earlier is the analogy for buffer-stock exhaustion: when inventories are too low users bid any price, and the same dynamic is a risk for oil (after Iran-war moves) and metals such as copper.  #mech/overshoot _(added by sonnet-xhigh cross-check)_
  > We saw that in the cocoa market a couple years ago is is that there's just not enough inventory.
  indicator: commodity inventory levels · asset: commodities · direction: extreme price spikes and backwardation when inventory is scarce · horizon: months · conditions: only when production needs continuing physical supply and warehouses are depleted · testable: yes - inventory-to-consumption ratios versus subsequent price spikes · confidence: high
  ^MT187-C03-X1

### C04
- **Mark Rzepczynski** China cut purchases and drew on reserves to smooth oil price spikes, but as buffers (China and US reserves) deplete a blowoff in oil and refined products becomes the risk.  #mech/liquidity_flows _(time-bound view)_
  > the demand for oil by China was significantly reduced. So basically they started to pull from their inventory reserves
  indicator: Chinese and US strategic oil inventories · asset: commodities · direction: long oil / refined products later · horizon: months · conditions: buffer stocks exhausted · testable: partly - reserve data is partially visible · confidence: medium
  ^MT187-C04-1
- **Niels Kaastrup-Larsen** A trend barometer of 43 means a neutral breadth of trending markets in the tracked portfolio.  #mech/slow_reaction _(time-bound view)_
  > my own trend barometer has cooled off a little bit in recent days. We're down to kind of a neutral level of 43.
  indicator: Trend barometer (43) · asset: multi · horizon: weeks · testable: yes - breadth indicator · confidence: medium
  ^MT187-C04-2
- **Mark Rzepczynski** Despite stress signals, VIX was low in Aug 2026 and uncertainty had receded from its Ukraine war high.  #mech/risk_premium _(time-bound view)_
  > VIX index is relatively low. So, so for all of the things we're talking about or all these rumblings, volatility has been relatively low.
  indicator: VIX · asset: equities · horizon: weeks · testable: yes · confidence: medium
  ^MT187-C04-3
- **Niels Kaastrup-Larsen** Commodity analyst Adam Rosenswag argues that roughly a billion barrels of physical oil are unaccounted for, which could eventually produce much higher oil prices, though the timing is uncertain.  #mech/overshoot _(added by sonnet-xhigh cross-check, time-bound view)_
  > what what the missing and his in his view I think like a billion barrels of oil physical oil what that might lead to
  indicator: global physical oil inventories · asset: commodities · direction: higher oil prices · conditions: timing unknown · testable: partly - depends on inventory accounting that is not public in full · confidence: low
  ^MT187-C04-X1

### C05
- **Mark Rzepczynski** Complexity and ambiguity (unwinding yen carry trade with intervention, unclear Fed policy and Treasury financing) force participants to adjust expectations slowly, creating trends in the fall.  #mech/slow_reaction _(time-bound view)_
  > This is that let's look at the yen carry trade, you know, which being unwind.
  indicator: VUCA: complexity and ambiguity · asset: multi · direction: trend opportunities in FX and rates · horizon: months · testable: no - qualitative · confidence: medium
  ^MT187-C05-1
- **Niels Kaastrup-Larsen** As of 18 Aug 2026 trend indices were up roughly 9.7-9.9% YTD (BTOP50 9.87%, SG Trend 9.73%, SG CTA 9.7%), short-term traders 4.6%, vs MSCI World 12.3%, S&P total return 12.6%, US Aggregate 0.39%.  #mech/slow_reaction _(time-bound view)_
  > Btop 50 up 1.78% for the month of August. Uh up 9.87 for the year.
  indicator: BTOP50, SG Trend Index, SG Short-Term Traders Index, S&P 500 TR · asset: multi · horizon: months · testable: yes - index data · confidence: high
  ^MT187-C05-2
- **Mark Rzepczynski** The US Treasury Secretary's role is to ensure buyers for Treasuries as weekly refunding auctions approach $800bn.  #mech/fiscal_debt _(time-bound view)_
  > he has said that he's the uh number one salesman for US bonds around the world.
  indicator: Treasury auction size · asset: rates · horizon: weeks · testable: partly · confidence: medium
  ^MT187-C05-3

### C06
- **Mark Rzepczynski** Many off-the-run bonds with different coupons are less liquid than on-the-run issues, so there is a yield and price gap between them.  #mech/liquidity_flows
  > we have a lot of these different we'll call it orphan bonds that are away from the benchmark on ther run issue.
  indicator: on-the-run vs off-the-run yield spread · asset: rates · horizon: months · testable: yes - spread data · confidence: high
  ^MT187-C06-1
- **Mark Rzepczynski** The Treasury buyback programme (raised from about $2bn to about $4bn a month) swaps off-the-run for new on-the-run issuance, changing composition not total debt, which signals insufficient dealer market-making capacity.  #mech/policy_reaction _(time-bound view)_
  > the Treasury Secretary is basically signaling to the market that we have a liquidity problem with an off therun issues.
  indicator: Treasury buyback size · asset: rates · horizon: months · testable: partly · confidence: medium
  ^MT187-C06-2
- **Mark Rzepczynski** Treasury buybacks have precedent: the first programme (2000-2002) was designed when budget surpluses raised fears of running short of long bonds, was stopped when rates were stable and restarted later, so the current expansion reflects liquidity needs rather than a surplus.  #mech/policy_reaction _(added by sonnet-xhigh cross-check)_
  > the first buyback program was in 2000 2002 and at that particular time if you could believe it is that the US government was running a uh uh a you know surplus
  indicator: US Treasury buyback programme · asset: rates · horizon: years · testable: partly - small number of historical buyback episodes · confidence: medium
  ^MT187-C06-X1

### C07
- **Niels Kaastrup-Larsen** Buyback announced right after the long bond hit 5.34% looks like soft yield curve control for the long end.  #mech/policy_reaction _(time-bound view)_
  > the Treasury long bond hits 5.34% which is like the highest we've seen in god knows how long
  indicator: 30-year Treasury yield 5.34% · asset: rates · direction: lower long-end yields from official action · horizon: weeks · testable: partly - event study · confidence: medium
  ^MT187-C07-1
- **Mark Rzepczynski** Official reassurance should itself be treated as a warning sign of an underlying problem.  #mech/behavioral
  > if the government tells you not to worry that's the time to start
  asset: multi · testable: no · confidence: low
  ^MT187-C07-2
- **Mark Rzepczynski** Shifting issuance toward bills shortens average maturity and holds down long yields without Fed action; a buyback could be a precursor to bills replacing bonds to relieve the long end.  #mech/fiscal_debt
  > during the Yellen period there was a tremendous amount of focus on issuing more Treasury bills as opposed to bonds.
  indicator: Treasury issuance mix (bills vs bonds); average maturity · asset: rates · horizon: years · testable: yes - issuance data · confidence: medium
  ^MT187-C07-3

### C08
- **Mark Rzepczynski** Treasury buybacks can act as a small bond market stabiliser by buying off-the-run bonds that trade cheap to the curve.  #mech/policy_reaction _(time-bound view)_
  > the Treasury could step in and be able to buy those cheap bonds that they think is cheap in an effort as part of this buyback program. So, they're actually act acting as uh bond market stabilizers
  indicator: off-the-run richness/cheapness · asset: rates · horizon: weeks · testable: partly · confidence: medium
  ^MT187-C08-1
- **Niels Kaastrup-Larsen** Trends in short rates follow monetary policy paths and suit trend followers, while the long end can have massive moves if rates truly change.  #mech/cycle_persistence
  > we as trend followers we we don't mind if we have a long-term trend in the short end uh where we can see the path of of um of of interest rates going higher or lower
  indicator: short-rate trends · asset: rates · horizon: months · testable: yes · confidence: medium
  ^MT187-C08-2
- **Mark Rzepczynski** Cash Treasuries trade OTC through primary dealers who also serve as auction conduits.  #mech/structural_shift
  > there is no exchange for treasuries. Now we do have the futures exchange for futures but the rest of the cash market is over the counters driven by a set of primary government security dealers.
  asset: rates · testable: no · confidence: high
  ^MT187-C08-3

### C09
- **Mark Rzepczynski** Regulation like the supplementary leverage ratio limits dealer balance sheets so capital for market making is out of proportion to Treasury volume, reducing liquidity.  #mech/liquidity_flows
  > because of regulations from the Fed so such as the uh supplemental liquidity ratios is is that there may not be enough capital at primary government security dealers for them to do their job to make markets.
  indicator: dealer balance sheet capacity vs Treasury volume · asset: rates · direction: wider bid-ask when liquidity is scarce · horizon: years · conditions: regulatory capital constraints · testable: partly · confidence: medium
  ^MT187-C09-1
- **Mark Rzepczynski** Hedge funds hold over 9% of marketable Treasuries, so the marginal long-end buyer is now levered rather than real money.  #mech/crowding_positioning _(time-bound view)_
  > hedge funds are the people who are hold some of the biggest holders they may uh be larger than mutual funds in terms of their holdings of treasuries. We're looking at 9% plus of the total
  indicator: hedge fund share of Treasuries · asset: rates · horizon: years · testable: yes - Fed/TIC data · confidence: medium
  ^MT187-C09-2
- **Mark Rzepczynski** The Fed finds the basis trade (cash vs futures, anchored on the cheapest to deliver) is the top hedge fund Treasury trade, and it keeps futures aligned with cash.  #mech/crowding_positioning
  > the number one trade is the basis trade. So, so the basis trade between the futures and and and cash
  indicator: Treasury cash-futures basis; cheapest to deliver · asset: rates · horizon: months · testable: yes - basis data · confidence: medium
  ^MT187-C09-3
- **Mark Rzepczynski** When Treasuries become less liquid, balance-sheet-constrained dealers must widen bid-ask spreads and hold inventory longer, which they must finance with scarce capital, so liquidity deteriorates exactly when selling pressure rises.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > you're going to either have to increase your bid spread because it's going to be harder to find that buyer and you're going to have to hold that on your balance sheet longer
  indicator: Treasury bid-ask spreads; dealer inventory · asset: rates · direction: wider spreads and weaker liquidity in stress · horizon: days · conditions: when dealer capital is limited by leverage regulation · testable: yes - dealer inventory and quoted spreads in stress episodes · confidence: high
  ^MT187-C09-X1

### C10
- **Mark Rzepczynski** The Treasury basis trade earns only a few ticks so it is run with extreme repo leverage; any repo market stress would spill into the bond market.  #mech/crowding_positioning
  > you've got to use a tremendous amount of leverage on what you think is a fairly low risk low return trade
  indicator: basis trade leverage; repo financing · asset: rates · direction: Treasury selloff on repo stress · horizon: weeks · conditions: Fed balance-sheet cuts or short-rate rises · testable: partly - repo rates and haircuts · confidence: medium
  ^MT187-C10-1
- **Niels Kaastrup-Larsen** Crowded low-risk levered trades can fail suddenly (SNB removing the franc floor).  #mech/crowding_positioning
  > it certainly reminds me about the the Swiss Frank euro um trade that lots of people loved and felt certain about until the day where the Swiss Frank was let free
  asset: fx · horizon: days · conditions: crowded leveraged carry-like trades · testable: no - analogy · confidence: medium
  ^MT187-C10-2
- **Mark Rzepczynski** High-frequency liquidity providers in Treasuries have no obligation to make markets and can switch off in stress, withdrawing liquidity.  #mech/liquidity_flows
  > the HFT, the high frequency traders like the Citadel and other places that are active in the Treasury market. So, but they're all electronic trading. They're not reporting to the Fed. They don't have specific market making responsibilities.
  asset: rates · horizon: days · conditions: market stress · testable: partly · confidence: medium
  ^MT187-C10-3
- **Mark Rzepczynski** More outstanding Treasury issues raise the chance that the cheapest-to-deliver bond switches, which creates both more basis-trade profit opportunities and more risk for the levered funds running them.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check)_
  > So that that then that means is that there's more opportunities for basis trading profits but also for risk.
  indicator: cheapest-to-deliver switches; Treasury futures basis · asset: rates · horizon: weeks · conditions: when many different coupons and maturities are outstanding · testable: yes - CTD switch frequency versus basis volatility · confidence: medium
  ^MT187-C10-X1
- **Mark Rzepczynski** Because Treasury positions are financed in repo, a Fed balance-sheet reduction or a rise in short rates tightens repo financing and reverberates from the overnight market through the whole bond market, as with the highly financed secondary Treasury dealers that failed in the 1980s.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > if let's say that the Fed wants to sort of cut its balance sheet okay then that's going to have an impact on on repo financing
  indicator: repo rates; Fed balance sheet · asset: rates · direction: funding stress transmits from short end to long end · horizon: weeks · conditions: when dealers and hedge funds are heavily leveraged through repo · testable: yes - repo spikes versus Treasury market dislocations · confidence: medium
  ^MT187-C10-X2

### C11
- **Mark Rzepczynski** In March 2020 Treasuries failed as a safe asset because liquidity vanished, so safety includes the ability to sell at a fair price.  #mech/liquidity_flows
  > when you look at March of 2020, there was a shortage of liquidity in the market. So we expected that treasuries would act as a safe asset and it didn't act like the safe asset.
  indicator: Treasury market liquidity · asset: rates · direction: avoid Treasuries as hedge in liquidity crises · horizon: days · conditions: liquidity shock · testable: yes - March 2020 bond-equity behaviour · confidence: high
  ^MT187-C11-1
- **Niels Kaastrup-Larsen** Loss of trust in institutions is a slow cycle that, once trust breaks in a market, produces disorderly moves; worth monitoring.  #mech/behavioral _(time-bound view)_
  > once you lose the trust of the market uh then uh all hell breaks loose.
  asset: multi · horizon: years · testable: no · confidence: low
  ^MT187-C11-2

### C12
- **Mark Rzepczynski** The LGT paper (Arthur Sepp) classifies trend followers as European (high signal to noise, dynamic position adjustment), American (breakout with digital positions held until exit) and academic time-series momentum (scaled by return).  #mech/research_method
  > he defines European is those people who look for s you know high signal to noise trades and look at constant adjustments in their positioning.
  indicator: trend style classification · asset: multi · horizon: years · testable: yes - styles can be backtested · confidence: medium
  ^MT187-C12-1
- **Mark Rzepczynski** The three trend styles have similar Sharpe ratios and drawdowns and all do well in strongly trending periods, with nuance in timing.  #mech/cycle_persistence
  > they actually are fairly similar in terms of their sharp ratios, their draw downs. There might be differences between each one of these. They all do very well during periods when there's a lot of trends.
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT187-C12-2
- **Niels Kaastrup-Larsen** The European/American trend-follower labels are historical rather than geographic: the digital-position 'American' style reflects the era before dynamic sizing tools existed, and today many US firms use dynamic sizing and hybrid breakout-plus-dynamic approaches, so due diligence must examine actual sizing and signal rules, not the label.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > there's a lot of of firms based in the US today that uh uses dynamic position sizing
  indicator: position-sizing method (digital versus dynamic) · asset: multi · testable: yes - classify managers by return-based sizing behaviour · confidence: high
  ^MT187-C12-X1

### C13
- **Niels Kaastrup-Larsen** When building a portfolio of managers, diversify by structural differences (markets traded, speed) rather than by style labels, because the future path is unknown.  #mech/risk_management
  > probably a good idea to start by looking at people with structural difference now this could one structural difference, right? Could also be the number of markets they trade.
  asset: multi · testable: partly · confidence: medium
  ^MT187-C13-1
- **Mark Rzepczynski** Fewer trend followers are needed to replicate the trend benchmark than managers in other hedge fund styles.  #mech/research_method
  > the number of trend followers you need to be able to replicate a benchmark or replicate is probably less than for some other hedge fund styles.
  asset: multi · testable: yes - number-of-managers replication study · confidence: medium
  ^MT187-C13-2
- **Niels Kaastrup-Larsen** Trend managers tend to stay with the style they started with, but programmes that evolve to blend several methodologies (provided each model is good and remains pure trend) can be stronger than a single style, which is a form of diversification inside one programme.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > where managers start to blend different types of trend following uh as long as it's quote unquote pure trend so you're not deviating from that
  asset: multi · conditions: each component must be a well-built, truly trend-following model · testable: yes - blend versus single-style backtests · confidence: medium
  ^MT187-C13-X1

### C14
- **Mark Rzepczynski** Run American, European and time-series momentum models as internal pods, aggregate signals before execution to cut transaction costs while tracking each pod's performance.  #mech/risk_management
  > I run different trend following models almost as if they're different pods and then what I could do is I can blend those together
  indicator: multi-model trend blending · asset: multi · direction: combine trend styles · testable: yes · confidence: medium
  ^MT187-C14-1
- **Niels Kaastrup-Larsen** Blending styles in one fund nets performance fees across models, unlike paying separate fees to several managers.  #mech/risk_management
  > there is one other big advantage compared to going out finding three or four or five different managers and that is you get netting of the performance fee.
  indicator: performance fee netting · asset: multi · horizon: years · testable: yes - fee calculation · confidence: medium
  ^MT187-C14-2
- **Mark Rzepczynski** Research finds short-term trend following has weakened in practice.  #mech/structural_shift
  > short-term trend following just doesn't really work that well.
  indicator: short-term trend following · asset: multi · direction: avoid short-term trend following · horizon: months · testable: yes · confidence: medium
  ^MT187-C14-3
- **Niels Kaastrup-Larsen** For long-term trend following in exchange-traded futures, transaction costs are low and not the main hurdle, so the cost saving from netting pod signals before execution is modest and the fee-netting benefit matters more.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > transaction cost generally at least in my view is not the biggest hurdle we face uh in in the in the long-term trend following uh trading on exchange futures uh only because transaction cost are low
  asset: multi · horizon: years · conditions: holds for long-horizon trend in liquid futures, not for short-term trend · testable: yes - estimate turnover and cost drag by lookback · confidence: medium
  ^MT187-C14-X1

### C15
- **Mark Rzepczynski** Short-term trend profits remain in futures with large (vol-adjusted) tick size, but are competed away by HFT market makers where tick sizes are small.  #mech/liquidity_flows
  > if you look at contract futures contracts that have large tick size, you can still make money from short-term trend following. those that have very tight or small tick size, it is very hard to make profits in those markets
  indicator: vol-adjusted tick size · asset: multi · direction: short-term trend only in large-tick contracts · horizon: days · conditions: small tick size markets dominated by HFT · testable: yes - cross-sectional by tick size · confidence: medium
  ^MT187-C15-1
- **Niels Kaastrup-Larsen** Short-term 'trend following' is typically volatility breakout with different exit rules, not true trend following, so results are not comparable with longer-term trend.  #mech/research_method
  > It's more like a vault breakout and then they get out at at you know with completely different uh rules not from a reversal of price
  asset: multi · horizon: days · testable: partly · confidence: low
  ^MT187-C15-2
- **Mark Rzepczynski** Market microstructure (tick size, player mix, financing) affects strategy returns as much as model details like breakout length.  #mech/research_method
  > understanding the plumbing of how markets operate and and and plumbing does matter. So those, you know, tick size matters, you know, who are the players in the market in treasuries matters, how who's getting financing
  asset: multi · testable: partly · confidence: high
  ^MT187-C15-3
- **Mark Rzepczynski** Niederhoffer treated markets as an evolving ecosystem of participants rather than as an efficient pricing machine, so understanding who the players are and how they behave (what is now called market plumbing) is a source of edge.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > he viewed it more as an you know evolutionary biology sense an ecosystem that uh so it's not so much markets are efficient but you have to look at what the ecosystem of markets and how they behave
  asset: multi · testable: no - a framework rather than a specific rule · confidence: medium
  ^MT187-C15-X1

### C16
- **Mark Rzepczynski** Niederhoffer research: headline overreaction, round-number price clustering, short-term mean reversion after large moves, and executive insider trades as signals.  #mech/overshoot
  > did some extreme uh good research in short-term mean reversion
  indicator: overreaction; price clustering; insider trading · asset: equities · direction: fade large moves short term; follow insider buying · horizon: days · testable: yes · confidence: medium
  ^MT187-C16-1
- **Mark Rzepczynski** Empiricism: verify with numbers and rigorous backtests; quality of results depends on quality of testing.  #mech/research_method
  > if you cannot count it, you do not know it.
  asset: multi · testable: yes · confidence: high
  ^MT187-C16-2
- **Mark Rzepczynski** Niederhoffer blew up in the late 1990s (and again later) despite empirical rigour, showing tail and leverage risk; he recovered by improving the process.  #mech/risk_management
  > blowups after the uh you know in uh you know in the you know late 90s
  asset: multi · conditions: leverage in short-volatility style positions · testable: no - anecdote · confidence: medium
  ^MT187-C16-3
- **Mark Rzepczynski** The Niederhoffer versus Taleb contrast frames a core research dilemma: the empiricist trusts data and rigorous backtests while the skeptic argues that history and statistical data can mislead, and Niederhoffer's blowups show the cost of over-trusting the numbers while his comebacks show the value of improving process.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > if Victor Netherhoffer was the uh true empiricist say Nin Talab was the skeptic and so uh so so you had the quant who said like let's just look at the data and follow the numbers
  asset: multi · testable: no - a philosophical disagreement · confidence: medium
  ^MT187-C16-X1

