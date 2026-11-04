---
source_id: MT029
title: "CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148"
date: 2025-04-03
channel: "Top Traders Unplugged"
url: 
words: 12726
claims: 50
added_by_crosscheck: 6
corrections: 6
crosscheck: "opus cross-check"
speakers: ["Graham Robertson (Man AHL, CEO of Man AHL)", "Rob Carver (independent systematic trader and author)", "Yav Git (Gresham Research, Safi fixed income CTA)", "Niels Kaastrup-Larsen (host, hedge fund manager)"]
tags: [source, layer0]
---
# CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148

**Speakers:** Graham Robertson (Man AHL, CEO of Man AHL); Rob Carver (independent systematic trader and author); Yav Git (Gresham Research, Safi fixed income CTA); Niels Kaastrup-Larsen (host, hedge fund manager)

**Summary:** Top Traders Unplugged 148 (April 2025): three former AHL colleagues discuss asset-class-specific vs multi-asset CTA design, liquidity and trend, under-allocation to CTAs, execution costs and technology. Conclusions: trend arises from sustained imbalances (Yav) though Rob doubts asset-class differences; execution mostly matters in illiquid markets; large-AUM products risk lowering Sharpe.

**Approach:** trend following, execution and trading costs, fixed income CTA, CTA allocation

**Cross-check completeness estimate of first read:** 0.88 - content coverage is good (missed Rob's rebuttal, Graham's liquidity and allocator points, two execution claims), but speaker attribution in the unlabelled captions was wrong or mixed in 6 of 44 claims.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | nothing actionable: intro, guests and banter (teaser repeated in C18) |
| C02 | 0 | nothing actionable: guest backgrounds and AHL history |
| C03 | 1 | AHL fixed income team; traditional trend struggled in range-bound Fed put era |
| C04 | 1 | alternative markets helped during CTA winter; AHL culture and open research (no method claims) |
| C05 | 2 | asset-class specific CTA building blocks; crypto trends |
| C06 | 5 | Rob's skepticism on asset class differences; Fed factor in bonds |
| C07 | 5 | asset-class risk and execution differences; fixed income share of CTA P&L |
| C08 | 2 | sustained imbalance theory of trend; FX carry and trend; liquidity intro |
| C09 | 5 | liquidity vs performance; equities value traders; commodities supply; execution in bonds; crowding in trend |
| C10 | 3 | participant mix; volume vs open interest |
| C11 | 3 | OTC liquidity; crisis management; CTAs as crude convexity |
| C12 | 3 | absolute return bucket Sharpe problem; high vol; speed vs skew |
| C13 | 4 | skew and no liquidity premium; vol and crisis alpha; bond context |
| C14 | 2 | execution cost; delay cost; patient execution |
| C15 | 2 | signal buffering; execution savings only in OTC markets |
| C16 | 3 | execution desk alpha; research share; technology; open source start |
| C17 | 2 | open source; code quality; chat jokes (no claims) |
| C18 | 1 | BlackRock and Fidelity entry; wrap-up |
| C19 | 0 | nothing actionable: outro |

## Claims

### C03
- **Graham Robertson** Around 2011-2013 traditional liquid trend struggled in range-bound markets with the Fed put emerging, which put pressure on a firm whose earnings depended on the liquid CTA program.  #mech/policy_reaction _(time-bound view)_
  > traditional Trend was struggling you know things were range bound
  indicator: liquid trend program returns, Fed put · asset: multi · horizon: years · conditions: range-bound markets suppressed by central banks · testable: yes - trend returns by period · confidence: medium
  **Correction (cross-check):** Mixes speakers: the pressure on AHL's earnings from the liquid CTA program and the drive for Evolution diversity is Yav's point; Graham adds the range-bound markets and Fed put. → Around 2011-2013 traditional liquid trend struggled in range-bound markets as the Fed put emerged (Graham); because AHL's earnings were tied to the liquid CTA program, this pushed it to diversify the Evolution program (Yav).
  ^MT029-C03-1

### C04
- **Graham Robertson** Alternative and OTC markets less affected by the Fed put (the Evolution program) kept earning during the CTA winter, so researching new markets with different price drivers added genuine value.  #mech/structural_shift
  > diversification in terms of price drivers uh markets was was really helpful to us
  indicator: alternative markets trend program · asset: multi · horizon: years · conditions: liquid trend struggling · testable: yes - alt-market vs liquid trend returns · confidence: medium
  ^MT029-C04-1

### C05
- **Yav Git** Because the utility of a CTA is crisis alpha and convexity relative to what the allocator holds, asset-class-specific trend products (e.g. fixed income only) are better building blocks than one pooled program.  #mech/structural_shift
  > if I'm a bond portfolio holder and I worry about Bond convexity and uh crisis halfa for bonds then what do I care about coffee
  indicator: asset-class-specific CTA building blocks · asset: multi · horizon: years · testable: partly - relates to allocator needs · confidence: medium
  ^MT029-C05-1
- **Yav Git** Crypto trends well because it has no valuation anchor and is in permanent imbalance, so big trends form.  #mech/structural_shift
  > why why crypto currencies actually Trend very well because there is no valuation
  indicator: crypto trend returns · asset: other · horizon: years · testable: partly - short history · confidence: medium
  ^MT029-C05-2
- **Yav Git** Crypto has enormous right skew, so risk control and position management for trend in crypto should differ from other asset classes; a generalist implementation leaves alpha on the table.  #mech/risk_management _(added by opus cross-check)_
  > the way you do the risk anal the risk control on it the way you manage the position um actually needs to be different because it
  asset: other · conditions: assets with strong right skew · testable: yes - compare skew-aware vs standard vol sizing on crypto trend · confidence: medium
  ^MT029-C05-X1

### C06
- **Yav Git** A single market's trend Sharpe is only about 0.25, so tailoring implementation per asset class to raise it to 0.30 adds real value after diversification.  #mech/research_method
  > the average Market sharp Alpha isn't particularly high in Trend it's like you know 25 basis points if we can get it to 30 that really adds value to the investor
  indicator: single-market trend Sharpe about 0.25 · asset: multi · testable: yes - per-market Sharpe · confidence: medium
  ^MT029-C06-1
- **Rob Carver** Rob is skeptical that some asset classes trend better than others; no strong statistically significant difference exists and crypto has too short a history, though equity trend looks weaker than VIX or fixed income, possibly due to higher carry in fixed income.  #mech/research_method
  > I've never really seen a sort of strong statistically significant effect in in performance between different asset classes
  indicator: trend performance by asset class · asset: multi · horizon: years · testable: yes - test asset-class Sharpe differences with error bars · confidence: medium
  ^MT029-C06-2
- **Rob Carver** In Rob's data equity trend does less well than trend in VIX or fixed income, which may relate to carry being naturally higher in fixed income.  #mech/structural_shift
  > Equity trenders is sort of welln doesn't do as well as say I don't know Trend in in vix or Trend in in fxed income
  indicator: trend returns by asset class table · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT029-C06-3
- **Rob Carver** A single universal risk model that includes higher moments can handle assets with different distributions such as crypto, so separate asset-class funds are not needed; a standalone CTA should choose the asset weights itself.  #mech/risk_management
  > that's the sort of thing you can deal with with a kind of universal risk model that just takes higher moments into account
  indicator: risk model with skew and kurtosis · asset: multi · testable: yes - compare universal vs tailored models · confidence: medium
  ^MT029-C06-4
- **Yav Git** Commodity markets diversify naturally (equal weight works), but fixed income has high loading on the Fed as a common factor, so portfolio construction there must be cleverer.  #mech/structural_shift
  > when we come to fixed income we have much bigger issue because there's a very high loading on the FED as a risk factor
  indicator: Fed factor loading across bond markets · asset: rates · testable: yes - factor/PCA analysis of bond returns · confidence: medium
  ^MT029-C06-5

### C07
- **Yav Git** A fixed income trend portfolio has strong left skew, like multi-strat pods, so it needs tighter risk control than naturally diversified commodity portfolios.  #mech/risk_management
  > if you think about uh fixed income portfolio it's got very strong left skew
  indicator: skew of fixed income trend portfolio · asset: rates · testable: yes - measure skew by sector · confidence: medium
  ^MT029-C07-1
- **Yav Git** Bond liquidity is fragmented across many maturities of the same issuer, so execution must tolerate partial fills or substitute bonds, unlike equities.  #mech/risk_management
  > you have multip bonds for the same issuer whereas in equities you have just one one stock for the for a company
  asset: rates · horizon: days · testable: no - practitioner knowledge · confidence: medium
  ^MT029-C07-2
- **Yav Git** About 70-75% of AHL's P&L over the last 25 years came from fixed income, so implementation specific to that sector matters.  #mech/structural_shift
  > about 70 75% of the p&l has come from fixed income
  indicator: sector share of CTA P&L · asset: rates · horizon: years · testable: yes - sector attribution · confidence: medium
  ^MT029-C07-3
- **Rob Carver** Rob argues fixed income dominates CTA P&L because it is the largest and most liquid sector and enjoyed a secular decline in rates for 30-40 years that ended around 2010-2012, and recently made little.  #mech/structural_shift
  > secondly we've had a very nice you know environment overall trend in fixed income for the last 30 40 years
  indicator: secular trend in rates, CTA fixed-income P&L · asset: rates · horizon: years · testable: yes - sector P&L by era · confidence: medium
  **Correction (cross-check):** Wrong speaker: the host (Niels) says 'let me just ask one thing Rob and then I'll let you jump in' and challenges Yav from his CTA vantage point. The dating of the end of the secular rate decline (around 2010) is Yav's reply, not part of this argument. → Niels Kaastrup-Larsen: fixed income dominates CTA P&L because it is the largest, most liquid sector and enjoyed a 30-40 year favourable trend; it has made little recently, so focusing on it risks fitting to the past.
  ^MT029-C07-4
- **Yav Git** Even since 2010 fixed income has been the most consistent asset class for trend across periods and speeds, unlike FX.  #mech/cycle_persistence
  > fixed income has been very consistent not just in terms of um consistency over time so different periods in time also different speeds
  indicator: fixed income trend consistency 2010-2025 · asset: rates · horizon: years · testable: yes - consistency by sector · confidence: medium
  ^MT029-C07-5

### C08
- **Yav Git** Trends arise from sustained imbalances, such as an interest-rate gradient between central banks, which creates sustained carry flows and positive autocorrelation; EURUSD without such gradient shows little trend while EM currencies with high carry trend strongly.  #mech/structural_shift
  > the way I think about what causes trend is sustained imbalance the sustainable imbalance in in the asset class
  indicator: interest rate differential, carry · asset: fx · horizon: years · conditions: large persistent rate gradients · testable: yes - trend strength vs carry/rate differential · confidence: medium
  ^MT029-C08-1
- **Yav Git** Emerging market currencies with strong carry show strong trend, whereas developed-market FX like EURUSD does not trend well.  #mech/structural_shift
  > when you see em currencies where you see very strong carry you see actually very strong Trend as well
  indicator: carry and trend in EM vs DM FX · asset: fx · horizon: years · testable: yes - Sharpe of FX trend by carry bucket · confidence: medium
  ^MT029-C08-2
- **Rob Carver** Rob rejects Yav's case for single-asset-class funds: specialised execution already exists inside a multi-asset CTA, and a generalised optimiser and risk model can handle differing diversification and distributions; he also calls Yav's sustained-imbalance theory of trends unproven.  #mech/research_method _(added by opus cross-check)_
  > you wouldn't have the same person executing cash equities as you would have executing cash Bonds in a CT anyway
  asset: multi · testable: partly - compare generalised vs asset-class-specific implementations · confidence: medium
  ^MT029-C08-X1

### C09
- **Rob Carver** Rob's blog found no correlation between market liquidity and trend performance, though Yav argues the wrong liquidity is measured (the imbalance matters) and liquidity mainly caps diversification and capacity.  #mech/research_method
  > looking at liquidity and seeing if it correlates with performance and it doesn't
  indicator: market liquidity vs trend performance · asset: multi · horizon: years · testable: yes - blog test · confidence: medium
  **Correction (cross-check):** Speaker: Yav Git says this, summarising Rob's blog, and adds his own objection; Rob does not speak here. → Yav Git: Rob's blog found no correlation between market liquidity and trend performance; Yav agrees but argues the wrong liquidity is measured (the imbalance matters), and liquidity mainly limits diversification and capacity.
  ^MT029-C09-1
- **Yav Git** Equity trend is weaker because value traders add negative autocorrelation.  #mech/crowding_positioning
  > the thing that really harms Equity is valuation and the fact that value Traders inject negative autocorrelation which makes it very difficult for Trend followers to harvest Trend inequity
  indicator: equity trend Sharpe, value investor activity · asset: equities · horizon: years · testable: partly - hard to measure value-trader share · confidence: medium
  ^MT029-C09-2
- **Yav Git** In commodities, supply takes time to meet demand shocks (e.g. AI power demand), creating sustained price imbalance and trend; liquidity should be judged by physical versus financial market size.  #mech/structural_shift _(time-bound view)_
  > if energy uh requirements in the US because of AI grows 5% next year it will take time to build power plants and to get to upgrade the electricity grid and price needs to meet that demand
  indicator: supply-demand imbalance, physical vs financial market size · asset: commodities · horizon: years · testable: partly · confidence: medium
  ^MT029-C09-3
- **Yav Git** Liquidity limits how much risk can go into small diversifying markets, so one must either accept small size or cap capacity to keep diversification.  #mech/risk_management
  > but generally we would like to think about liquidity as a way for us to manage diversity and it's a restriction for us
  indicator: market liquidity, capacity · asset: multi · testable: no - qualitative · confidence: medium
  ^MT029-C09-4
- **Yav Git** Better execution in fixed income comes from understanding who holds inventory and using many brokers rather than only big banks; systems should accept partial fills or different bonds on the same curve.  #mech/risk_management
  > is really understanding who is the one who is actually holding the inventory who's the biggest players in that in that market
  indicator: dealer inventory, multiple brokers · asset: rates · horizon: days · testable: partly - execution data · confidence: medium
  ^MT029-C09-5

### C10
- **Rob Carver** Trend following does not suffer the crowding that spread and RV trades do (profits do not reduce future returns), so the liquidity-alpha link differs for momentum versus reversion strategies.  #mech/crowding_positioning
  > the more the market goes up the more opportunity there is for the market to go up more
  indicator: momentum vs reversion trade crowding · asset: multi · testable: partly · confidence: medium
  ^MT029-C10-1
- **Rob Carver** The proportion of reversion players (stat arb in single stocks, curve trades in bonds) versus momentum players in a market may confuse trendiness, compared with gold or crude.  #mech/crowding_positioning
  > I would imagine in like single stock equities there's a lot more people doing you know statar type strategies and playing reversion trades
  indicator: share of reversion traders by market · asset: multi · testable: partly - participant composition hard to measure · confidence: low
  ^MT029-C10-2
- **Rob Carver** Futures liquidity has two measures, volume and open interest (e.g. Korean stocks high volume low open interest, interest rate futures the reverse), which matter differently for position building and liquidation.  #mech/research_method
  > there are two measures of liquidity right there's volume and open interest and you can have markets with incredibly high volume
  indicator: volume vs open interest · asset: multi · testable: yes - liquidity metrics · confidence: high
  ^MT029-C10-3
- **Graham Robertson** Market size is not liquidity: the industry players who dominate a market and its transaction costs shape how it trades and how trend performs there, so a single 'how liquid' measure is misleading.  #mech/research_method _(added by opus cross-check)_
  > liquidity is a term that's often misused you can talk about the size of the market and people will call that liquidity of the market but it's not necessarily the same thing
  indicator: market size vs transaction costs vs participant mix · asset: multi · testable: partly - needs participant-composition data · confidence: medium
  ^MT029-C10-X1

### C11
- **Yav Git** After the GFC transaction reporting and central clearing of swaps improved OTC market liquidity visibility, though broker relationships remain valuable.  #mech/structural_shift
  > I think things after GFC have become a lot better in terms of reporting of transactions
  indicator: OTC transaction reporting, clearing · asset: rates · horizon: years · testable: no - structural · confidence: medium
  ^MT029-C11-1
- **Yav Git** In less liquid OTC markets you cannot exit when vol spikes as futures CTAs do, so a properly diversified portfolio must be built before the crisis.  #mech/risk_management
  > on day one you're just stuck with the position and you have to manage that risk
  indicator: portfolio diversification before crisis · asset: multi · horizon: days · conditions: illiquid OTC markets · testable: partly · confidence: medium
  ^MT029-C11-2
- **Yav Git** CTAs are a crude way to buy convexity or crisis alpha because they may not pay off in a given crisis; a tailored Treasury put replication would be more precise.  #mech/risk_premium
  > then ctas are very crude fuzzy way to get convexity right because it is really not tailored to my underlying portfolio
  indicator: CTA payoff in crises · asset: multi · horizon: years · testable: yes - CTA returns in crisis episodes · confidence: medium
  ^MT029-C11-3

### C12
- **Yav Git** Inside an absolute-return bucket a 0.7 Sharpe CTA beside peers at 1.5 lowers dollar returns, so under-allocation is rational unless leveraged; CTAs need about 1.2-1.3 Sharpe or a tailored crisis role.  #mech/behavioral
  > adding risk adding a CTA is actually very detrimental in terms of dollar terms now it will be great from a sharp point of view and if you could leverage then that will add value
  indicator: Sharpe of CTA vs absolute return peers · asset: multi · horizon: years · testable: yes - portfolio math · confidence: medium
  ^MT029-C12-1
- **Graham Robertson** High-vol share classes give capital efficiency, but many allocators do not value them and prefer low-vol funds, so product design is the lever.  #mech/behavioral
  > the problem is I guess not that many people necessarily understand that the High Vol is a good thing
  indicator: volatility target of share class · asset: multi · testable: no - preference · confidence: medium
  **Correction (cross-check):** Probable wrong speaker: the high-vol share class remark ('I remember back in the day and I'm sure it's still the case AHL was offering High Vol share classes') is by a former AHL person and continues into Rob's 'I like Yav saying...'; it is most likely Rob Carver, not Graham (current AHL CEO). → Rob Carver (probable): high-vol share classes give capital efficiency, but few allocators see high vol as good and many prefer low-vol funds; changing the products may be the lever.
  ^MT029-C12-2
- **Rob Carver** Speeding up a trend program would give more positive skew and tail protection but at the cost of alpha, moving away from where trend works best.  #mech/risk_management
  > something kind of more tail proty would be to speed it up and give it more positive skew um and and then that would be probably at the cost of alpha
  indicator: trend speed, skew · asset: multi · direction: faster models more skew, less alpha · horizon: months · testable: yes - skew and Sharpe by lookback · confidence: medium
  ^MT029-C12-3
- **Graham Robertson** Large institutions keep a steady trend-following allocation through good and bad years, but wealth-segment investors and the media largely ignore it (an FT article on handling volatility did not mention trend following), which is where under-allocation lies.  #mech/behavioral _(added by opus cross-check)_
  > larger investors tend to have an allocation to Trend following thick and thin
  asset: multi · horizon: years · testable: no - anecdotal · confidence: medium
  ^MT029-C12-X1

### C13
- **Yav Git** Trend following has positive skew and does not harvest a liquidity premium, so it deserves a larger allocation if made easier to hold.  #mech/risk_premium
  > it's one of the only strategies which has you know the positive skew and it's not actually harvesting liquidity premium
  indicator: skew of trend following · asset: multi · horizon: years · testable: yes - skewness and premia exposure · confidence: high
  ^MT029-C13-1
- **Niels Kaastrup-Larsen** Higher-vol share classes did not make CTAs institutional before and investors who prefer high vol give smaller allocations, so more vol will not fix under-allocation.  #mech/behavioral
  > I remember the times when we had more V in our industry and that actually didn't make it institutional at all
  indicator: vol targets and allocation size · asset: multi · horizon: years · testable: no - anecdotal · confidence: medium
  ^MT029-C13-2
- **Niels Kaastrup-Larsen** CTAs are not designed to profit from equity crises; good crisis returns result from the strategy and diversification, so selling them as crisis alpha is a mistake and uncorrelated returns are the real value.  #mech/structural_shift
  > generally speaking I don't think we as managers are designing our uh products to make money specifically when there is an equity crisis
  indicator: CTA returns in equity crises · asset: multi · horizon: years · testable: yes - crisis-period returns · confidence: medium
  ^MT029-C13-3
- **Graham Robertson** Heavy fixed income issuance to fund government changes means trend following should be considered as protection for bond portfolios, not just equities.  #mech/fiscal_debt _(time-bound view)_
  > maybe people start need to start thinking about Trend following in the context of a fixed income portfolio not just an equity uh portfolio
  indicator: trend following as bond hedge · asset: rates · horizon: years · testable: partly - bond-trend correlation · confidence: low
  **Correction (cross-check):** Wrong speaker: Niels says this ('that's just my own view here') and moves to the next topic in the same turn. → Niels Kaastrup-Larsen: heavy government bond issuance to fund policy changes means trend following should also be considered as protection for fixed-income portfolios, not just equities.
  ^MT029-C13-4

### C14
- **Yav Git** For liquid CTAs execution costs about 5bp of Sharpe per year, so execution is production work; for illiquid markets it can cost 30-40bp of Sharpe and matters.  #mech/risk_management
  > it cost us a maybe five basis points of sharp per per year
  indicator: execution cost in Sharpe basis points · asset: multi · horizon: years · testable: yes - cost accounting · confidence: high
  ^MT029-C14-1
- **Yav Git** Delaying signals by a day costs only 1-2bp, so execution desks should be given several days to trade patiently, using partial execution to avoid crossing the spread, which is the real cost.  #mech/risk_management
  > if you lag your strategy suppose you say okay I'm going to lag my signals by a day you find that actually your Alpha doesn't Decay that much you will maybe lose one or two basis points
  indicator: alpha decay from lagging signals, spread crossing · asset: multi · direction: slower, patient execution · horizon: days · testable: yes - lag test and execution backtest · confidence: high
  ^MT029-C14-2
- **Yav Git** Due-diligence test: asking whether a CTA pays its execution desk a performance fee reveals whether it treats execution as an alpha source or as a production line.  #mech/research_method _(added by opus cross-check)_
  > do you pay performance fee to your execution desk
  asset: multi · testable: no - due-diligence heuristic · confidence: medium
  ^MT029-C14-X1

### C15
- **Yav Git** Many CTAs smooth signals for days then force execution within hours; better to give the desk the raw signal and tell it to trade slowly, saving costs.  #mech/risk_management
  > you will take a signal and you will sit on it for 5 days because you're buffering it and then ex insist that execution desk execute it within half a day
  indicator: signal buffering vs execution window · asset: multi · horizon: days · testable: yes - compare smoothing vs patient execution · confidence: medium
  ^MT029-C15-1
- **Rob Carver** With trading costs of about 4bp Sharpe (half commissions), only about 2bp can be saved through execution effort on liquid futures, so effort is not worthwhile there; benefit exists mainly in OTC bonds.  #mech/risk_management
  > and half of that's commission which for an institution is negligible right so only only two basis of points of that is Bid ask so I could only save two basis points of shot
  indicator: trading cost 4bp Sharpe · asset: multi · testable: yes - cost decomposition · confidence: high
  ^MT029-C15-2
- **Yav Git** Yav claims patient execution saves more than the alpha lost from delay even in liquid bond futures (e.g. 5-year Bobl), not only in illiquid OTC bonds; Rob disagrees for liquid futures.  #mech/risk_management _(added by opus cross-check)_
  > the benefits of waiting far outweighs the loss of alpha even for those markets
  indicator: execution cost vs signal-delay alpha decay · asset: rates · horizon: days · conditions: disputed for liquid futures · testable: yes - compare spread savings from passive fills vs alpha decay from delay · confidence: high
  ^MT029-C15-X1

### C16
- **Rob Carver** Giving traders discretion over patient execution turns a CTA into CTA plus a short-horizon alpha desk, requiring skills that may not exist; with 30bp costs Rob would slow the signal further or stop trading the market.  #mech/risk_management
  > fund has become a CTA plus a he like like a trading desk with a horizon of a few hours
  indicator: execution desk alpha · asset: multi · horizon: days · testable: partly · confidence: medium
  ^MT029-C16-1
- **Niels Kaastrup-Larsen** Large CTAs spend about 35-40% of research effort on execution.  #mech/research_method
  > we probably spend 35 to 40% of all our research just on execution
  indicator: research allocation to execution · asset: multi · testable: no - interview statement · confidence: medium
  ^MT029-C16-2
- **Yav Git** Technology tightly integrated with research accelerates and cleans implementation and technologists spot issues researchers miss.  #mech/research_method
  > technology um when it is really married to the research when you work side by side um is really uh a great boost to what we do
  asset: multi · testable: no - organisational practice · confidence: medium
  ^MT029-C16-3

### C17
- **Graham Robertson** Open-sourcing foundations (e.g. Arctic DB) attracts top technologists and improved code quality at AHL.  #mech/research_method
  > open source is good uh in fact the we open source a lot of the basic um Foundation of our um of what we do
  asset: multi · testable: no - organisational · confidence: medium
  **Correction (cross-check):** Speaker mostly wrong: Graham only says open source attracts the best technologists; the Arctic DB story and 'we open source a lot of the basic foundation' are Yav Git's (he was the initial sceptic at AHL). → Graham Robertson and Yav Git: open-sourcing core infrastructure (e.g. Arctic DB) attracts top technologists and improved code quality at AHL; Yav says he was first sceptical and was proved wrong.
  ^MT029-C17-1
- **Rob Carver** Open-sourcing a trading system forces better code quality, testing and documentation.  #mech/research_method
  > the discipline of knowing that lots of other people are going to look at your code it makes you more likely to to write good quality code and and you know test and document it properly
  asset: multi · testable: no · confidence: medium
  ^MT029-C17-2

### C18
- **Yav Git** BlackRock and Fidelity's large AUM targets make a high-Sharpe diversified product hard, risking a perception of CTAs as a 0.5 Sharpe strategy.  #mech/crowding_positioning _(time-bound view)_
  > but I think it will be very difficult to create a popular Diversified Pro product um at the AUM that they they will be targeting
  indicator: capacity vs Sharpe of mass-market trend products · asset: multi · horizon: years · testable: partly - capacity curves · confidence: medium
  ^MT029-C18-1

