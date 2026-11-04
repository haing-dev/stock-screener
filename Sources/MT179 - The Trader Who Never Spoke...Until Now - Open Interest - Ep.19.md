---
source_id: MT179
title: "The Trader Who Never Spoke...Until Now - Open Interest - Ep.19"
date: 2025-11-04
channel: "Top Traders Unplugged"
url: 
words: 15459
claims: 40
added_by_crosscheck: 12
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Dave Drew (founder, Tactical Investment Management)", "Moritz Seibert (host, Open Interest series)"]
tags: [source, layer0]
---
# The Trader Who Never Spoke...Until Now - Open Interest - Ep.19

**Speakers:** Dave Drew (founder, Tactical Investment Management); Moritz Seibert (host, Open Interest series)

**Summary:** Open Interest ep.19: Drew describes Tactical's systematic futures method designed to sit opposite commercial hedgers (risk premium capture, price-based algorithms from COT patterns), not trend following, though it correlates with trend followers. Stresses timing, money management and portfolio selection, with portfolio construction by orthogonal sectors/markets most important. Also small-fund capacity advantage in small markets and investor alignment; Seykota is discretionary pattern trader.

**Approach:** hedger risk premium, commitments of traders, portfolio construction, systematic futures, position sizing, fund capacity

**Cross-check completeness estimate of first read:** 0.80 - first reader caught the central hedger-premium method, three-part system framework, portfolio orthogonality and business-model points; missed several supporting reasoning steps and two speaker attributions were wrong.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro; zero-sum game; background |
| C02 | 0 | how Drew got into trading |
| C03 | 2 | scared money advice, starting a fund, ER career |
| C04 | 0 | Commodities Corp experience (no method content) |
| C05 | 1 | Seykota's actual style; apprenticeship |
| C06 | 1 | Tactical edge: hedger risk premia; not a trend trader |
| C07 | 2 | zero-sum, who wins and loses (COT groups), hedger transfer |
| C08 | 2 | COT patterns used to design timing algorithm |
| C09 | 2 | algorithm used for 40 years; hedging in currencies, rates, equities |
| C10 | 2 | equity futures excluded; timing vs money management; sizing and stops |
| C11 | 1 | expecting drawdowns; insurer analogy |
| C12 | 2 | psychology, heat, extensive testing |
| C13 | 1 | programming; portfolio is most important |
| C14 | 2 | multi-timeframe, dynamic markets list |
| C15 | 2 | orthogonality, sector weights |
| C16 | 2 | correlated market sizing, robustness tests, goals of portfolio |
| C17 | 1 | business model, marketing costs |
| C18 | 1 | investors first; small markets and capacity |
| C19 | 1 | fund size cap, capacity, new markets |
| C20 | 1 | organisation size, investor fit |
| C21 | 0 | investor fit; fund closure reason |
| C22 | 1 | closure and investor reaction; wrap-up |
| C23 | 0 | nothing actionable: outro |

## Claims

### C01
- **Dave Drew** Futures profits come from someone else's losses, so a trader should know who is losing money for them to make it.  #mech/crowding_positioning
  > Futures trading is a zero sum game. That is got to be understood by anyone who is trying to to, you know, be successful in the markets.
  asset: multi · testable: no - framing principle · confidence: high
  ^MT179-C01-1

### C03
- **Dave Drew** Trade with money you can afford to lose from an independent income source; scared money forces poor decisions.  #mech/behavioral
  > if you take this job, you're going to trade with your own money. I know it. And it's going to be scared money.
  asset: multi · testable: no - anecdote · confidence: medium
  ^MT179-C03-1
- **Dave Drew** Proper diversification across many futures markets requires more capital than an individual typically has, which motivated starting a fund.  #mech/risk_management
  > to do this right, you really need a lot of money to diversify properly. So, why not start a fund?
  asset: multi · testable: no - motivation · confidence: medium
  ^MT179-C03-2

### C04
- **Dave Drew** Commodities Corp recruited independent traders and gave each a staff contact who counselled and encouraged them through drawdowns, an institutional practice to keep skilled traders trading through losing periods.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > they were a psychological support in addition to the person that found you
  asset: multi · conditions: when a trader is in a drawdown · testable: no - organisational practice · confidence: medium
  ^MT179-C04-X1

### C05
- **Dave Drew** Ed Seykota's style is computer-assisted technical discretionary pattern-based trading, not algorithmic trend following; he knows system strengths and weaknesses from backtests but uses computers for data display and cleaning.  #mech/research_method
  > Ed has uh of course certain very um welldefined rules in his mind for trading.
  asset: multi · testable: no - correction of a misconception · confidence: high
  ^MT179-C05-1

### C06
- **Dave Drew** Tactical's edge was capturing risk premia from commercial hedgers; because that profit appears mainly when markets trend, returns correlate highly with trend followers.  #mech/risk_premium
  > We always felt that our edge was capturing risk premia from hedggers and we designed our system specifically to do that.
  indicator: commercial hedger positioning · asset: commodities · direction: long/short opposite hedgers · horizon: months · conditions: works in futures with true hedging flows; not in equity futures · testable: partly - COT-based hedger position strategies are testable · confidence: high
  ^MT179-C06-1
- **Dave Drew** Seykota believed technical discretionary pattern trading is more profitable over the long run than algorithmic systematic trading, although Drew never adopted it for his investors.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > he always encouraged me to try to trade in a style more similar to his because he felt it was more profitable over the long run
  asset: multi · horizon: years · testable: no - opinion of one trader · confidence: medium
  ^MT179-C06-X1

### C07
- **Dave Drew** Academic studies show that only large speculators earn profits over time while commercial hedgers and small speculators lose, so a professional must take money from hedgers.  #mech/risk_premium
  > only the big speculators over time take money out of the markets. The commercial hedgers lose money in the futures markets and the small speculators lose money in the futures markets.
  indicator: COT trader groups: large speculators, small speculators, commercial hedgers · asset: commodities · direction: long large speculators, short hedgers · horizon: years · conditions: size makes small speculators irrelevant as a source · testable: yes - COT group P&L studies · confidence: medium
  ^MT179-C07-1
- **Dave Drew** A trend follower implicitly takes money from hedgers: a farmer hedges when price is high enough, then loses on futures as the trend continues while locking in profit on physical crops.  #mech/risk_premium
  > those hedggers have traded opposite you at some point. The price got high enough for them to
  indicator: hedger behaviour · asset: commodities · horizon: months · testable: no - explanatory · confidence: medium
  ^MT179-C07-2
- **Dave Drew** A professional running funds cannot rely on small speculators as the source of profits because their size is too small for the capital deployed, so the large-capital edge has to come from commercial hedgers.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > small speculators are going to become irrelevant because the size that they trade is tiny compared to the size you might want to trade
  indicator: small speculator positions (COT) · asset: multi · conditions: when trading size is large · testable: partly - COT groups can be tested · confidence: medium
  ^MT179-C07-X1

### C08
- **Dave Drew** In the 1980s, COT data (two-week lag) was used to find chart patterns that precede shifts in hedger net positions, and price-based algorithms were built from these patterns rather than using COT data in the live system.  #mech/slow_reaction
  > and you could see where the big the big specs and the hedggers shifted from net long to net short and vice versa.
  indicator: CFTC Commitments of Traders, price patterns · asset: commodities · horizon: weeks · conditions: only worked when futures were the main hedging venue · testable: partly - derived rules reproducible only with price patterns · confidence: high
  ^MT179-C08-1
- **Dave Drew** The hedger-opposite method stopped being reproducible because hedgers now have OTC and options routes to lay off risk, so futures positions no longer capture their flows.  #mech/structural_shift
  > the futures markets were really the only vehicles that big commercial hedgers had that were liquid enough for them to hedge their positions.
  indicator: commercial hedging venues · asset: commodities · horizon: years · conditions: method no longer works · testable: no - structural claim, hard to test · confidence: medium
  ^MT179-C08-2
- **Dave Drew** Drew admits he never verified that hedgers actually shifted at the points his patterns flagged; the hedger-shift hypothesis was a better design basis for entry timing than guessing when a trend begins, so the edge was inferred rather than observed.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > Now do I know that they actually did? No, I have no idea. But it's a it's a better basis for determining timing than just trying to guess that a trend is starting
  indicator: pattern-implied hedger shifts · asset: multi · testable: no - cannot observe hedger intent · confidence: high
  ^MT179-C08-X1

### C09
- **Dave Drew** Systematic trading involves discretion at design (choice of rules) and none afterwards; the same timing algorithms from 1984 were used until the fund closed in 2023, without overriding.  #mech/research_method
  > systematic trading is also discretionary, but the discretion it goes in at the front.
  asset: multi · horizon: years · testable: no - principle · confidence: high
  ^MT179-C09-1
- **Dave Drew** The hedger model applies to currencies (institutions laying off risk) and to interest rate futures but breaks down at the short end of the curve where central bank arbitrage dominates; equity futures excluded because tied to index arbitrage so no genuine price discovery by hedgers.  #mech/risk_premium
  > it's absolutely a valid model in those
  indicator: hedging flows in currencies, rates, equities · asset: multi · horizon: years · conditions: excluded in equity index futures · testable: no - judgment · confidence: medium
  ^MT179-C09-2

### C10
- **Dave Drew** A trading system has three separable parts (timing, money management, portfolio selection); entries came from opposite-hedger timing, exits from money-management rules, and the system was not always in the market.  #mech/risk_management
  > in a system of trading there are three main aspects. There's timing, there's money management and there's portfolio selection
  asset: multi · testable: partly - components can be tested separately · confidence: high
  ^MT179-C10-1
- **Dave Drew** Positions were sized by volatility so that a trailing stop is not triggered by random price noise (ATR-like), giving the market enough room but not too much.  #mech/risk_management
  > we sized our positions based on the uh uh likelihood that that position would get stopped out with just a random movement of price
  indicator: volatility-based position size, trailing stop · asset: multi · horizon: days · testable: yes - ATR sizing and trailing stop backtest · confidence: high
  ^MT179-C10-2

### C11
- **Dave Drew** Taking risk hedgers want to shed gives a volatile equity stream with frequent small losses and occasional large wins, the opposite of an insurer's income profile; drawdowns must be expected.  #mech/risk_premium
  > I felt that this style of trading was inherently going to have a swingy uh type of equity stream because I'm taking what the hedgers don't want.
  indicator: strategy return profile · asset: commodities · horizon: years · testable: yes - return distribution · confidence: high
  ^MT179-C11-1
- **Dave Drew** A volatile risk-premium strategy needs a decision at the outset to have faith in the method and never abandon it, because knocked-down-and-stand-up-again is how the hedger premium is earned and drawdowns of years are expected.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > just being able to never quit you know that's the thing you're you make a decision at the beginning I have faith in this method I'm not going to abandon the method
  asset: multi · horizon: years · conditions: long drawdowns without new equity highs · testable: no - behavioural discipline · confidence: high
  ^MT179-C11-X1

### C12
- **Dave Drew** The original timing algorithm proved robust for 40 years after extensive testing of alternatives, which Drew programmed himself so he could ask complex portfolio-level questions.  #mech/research_method
  > I tested absolutely every single thing under the sun. I had computers going 247 for years testing every possible system
  asset: multi · horizon: years · testable: yes - robustness over 40 years · confidence: high
  ^MT179-C12-1
- **Dave Drew** There was no maximum portfolio heat rule; large open equity did not trigger cutting positions, and the computer helps follow trades during long drawdowns though psychological pain remains.  #mech/risk_management
  > we did not have such a um a a rule in the uh system.
  indicator: portfolio heat · asset: multi · testable: yes - test heat caps · confidence: high
  ^MT179-C12-2

### C13
- **Dave Drew** Portfolio selection matters more than timing or money management; the same system on cocoa versus crude oil gives very different outcomes, so portfolio construction deserves the most attention.  #mech/risk_management
  > the portfolio is an order of magnitude at least 10 times more important than either of the other two.
  indicator: portfolio selection, market weights · asset: multi · horizon: years · testable: partly - compare portfolio choices on the same system · confidence: high
  ^MT179-C13-1

### C14
- **Dave Drew** The same hedger-shift pattern was applied across multiple time frames because markets are self-similar over a range, and backtests confirmed it.  #mech/slow_reaction
  > markets are fractal over a wide range. If you get too short or you get too long, the fractal nature of markets breaks down.
  indicator: multi-timeframe pattern · asset: multi · conditions: breaks down at extreme short or long time frames · testable: yes - multi-timeframe backtest · confidence: medium
  ^MT179-C14-1
- **Dave Drew** Portfolios need rules for adding new markets (e.g. heating oil before crude futures) and removing dying ones (potato futures), including how long to wait before trusting a new market.  #mech/research_method
  > You have to have some rule to tell you when to stop trading a certain market.
  indicator: market inclusion and exit rules · asset: multi · testable: yes - survivorship in market universe · confidence: high
  ^MT179-C14-2
- **Dave Drew** Systematic strategies should be tested on the longest possible history (Drew obtained 1970s Board of Trade charts and typed in the data by hand) to see markets and regimes such as 1970s potato trends.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > you always want to look back as far as you can if you're doing systematic trading
  indicator: long history of futures data · asset: multi · horizon: years · testable: yes - longer samples · confidence: high
  ^MT179-C14-X1
- **Dave Drew** A portfolio should include a feedback mechanism that checks whether it still delivers its stated goal (such as smoother equity growth), not only a static basket of markets.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > you want to have something in your portfolio that looks at what your portfolio is trying to achieve for you and make sure that you have some feedback on it
  indicator: portfolio goal feedback · asset: multi · testable: partly - requires defined goal metrics · confidence: medium
  ^MT179-C14-X2

### C15
- **Dave Drew** If the portfolio goal is smooth equity growth, choose orthogonal markets; 25 interest-rate futures give almost no smoothing, so weights by sector and sub-sector should reflect correlations.  #mech/risk_management
  > you have to construct it with this goal in mind. And you have to say, I want orthogonal markets
  indicator: correlation-based sector weights · asset: multi · testable: yes - diversification measure · confidence: high
  ^MT179-C15-1
- **Dave Drew** Weights are set top-down by sectors and sub-sectors using orthogonality and slowly updated if correlations change.  #mech/risk_management
  > ever so slowly make adjustments over time if markets no longer were behaving in the way that we had initially assessed them
  indicator: portfolio weights, correlation drift · asset: multi · horizon: years · testable: yes - slow-moving weights backtest · confidence: high
  ^MT179-C15-2

### C16
- **Dave Drew** Design questions (e.g. half weights for correlated petroleum markets versus full weight on first signal) should be tested over rolling 5- and 10-year blocks to see if the answer is robust.  #mech/research_method
  > look back as far as I could over time or write a program, analyze the results, and then break it up in little segments of of yearly intervals, rolling intervals
  indicator: rolling-window robustness test · asset: commodities · horizon: years · testable: yes - rolling-window evaluation · confidence: high
  ^MT179-C16-1
- **Dave Drew** Alternative portfolio goal: hold only the best markets by relative strength (e.g. top five), requiring an algorithm that changes weights as strength changes; Tactical instead sought smoothness.  #mech/slow_reaction
  > I want a portfolio that has the markets in it that have the best potential to make money in the near term. And so then you have to have some type of an algorithm that gives a relative strength weight
  indicator: relative strength market selection · asset: multi · direction: long strongest markets · horizon: months · testable: yes - relative-strength selection backtest · confidence: medium
  ^MT179-C16-2

### C17
- **Dave Drew** Marketing costs of large funds are paid by investors via commissions or fees, creating misalignment; smaller funds with investors-first philosophy avoided this.  #mech/behavioral
  > the people who got really big, they spent a significant amount of money on marketing and the investors paid for it uh one way or another
  asset: other · horizon: years · testable: no - business opinion · confidence: medium
  ^MT179-C17-1

### C18
- **Moritz Seibert** Smaller funds can trade small orthogonal markets (lumber, orange juice, cotton, cocoa, sugar) that a $10bn fund cannot, giving more diversification and less noise than large funds concentrated in rates and equities.  #mech/structural_shift
  > If you are smaller, you can operate in some of these smaller markets. And some of these smaller markets are the really diversifying ones.
  indicator: capacity of small markets · asset: commodities · direction: diversification benefit up for smaller funds · horizon: years · conditions: capacity-limited · testable: yes - compare small-market contribution · confidence: high
  ^MT179-C18-1
- **Moritz Seibert** A client base of private investors and family offices, rather than large institutions, lets the manager explain the volatility and the required holding period, reducing short-term redemptions.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > it gives us an opportunity to also explain in more detail what it is that we do, how we trade, why the volatility exists, and that they need to be there for a period of time
  indicator: investor base composition · asset: multi · horizon: years · conditions: smaller funds without large marketing · testable: partly - redemption data by investor type · confidence: medium
  ^MT179-C18-X1

### C19
- **Dave Drew** Capping fund size keeps access to small markets; individual trades lose 70% of the time, but adding canola to the 10-year note helps the portfolio much more than adding the five-year note.  #mech/risk_management
  > We've even put language in our legal offering documents that will limit the size of the fund
  indicator: fund capacity cap, marginal diversification · asset: commodities · horizon: years · testable: yes - marginal contribution by market · confidence: high
  **Correction (cross-check):** Wrong speaker: the legal offering-document cap, the 70% losing trades statement and the canola versus 5-year note comparison are Moritz Seibert describing his own fund (Drew's Tactical had already closed). → Seibert caps his fund's size in the offering documents so it can keep trading small markets such as lumber, oats and canola; individual trades in these markets lose about 70% of the time, but adding canola to the 10-year note helps the portfolio much more than adding the 5-year note.
  ^MT179-C19-1
- **Moritz Seibert** Large funds concentrated in interest-rate and equity markets (where it is risk-on/risk-off) are forced to dial positions down and control volatility to avoid drawdowns because investors will fire them, misaligning incentives and degrading the trend edge.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check)_
  > then they have to dial their positions down and they have to respond to these investors and smooth the returns and v control stuff and avoid getting into a draw down otherwise they get fired
  asset: multi · conditions: when assets are very large and risk is concentrated in rates and equities · testable: partly - fund size versus performance · confidence: medium
  ^MT179-C19-X1
- **Moritz Seibert** Chinese futures markets are very liquid, large and offer portfolio qualities (different contracts) not found on CME, but are difficult for US persons to reach; there are legitimate routes, making them a source of diversification.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > Some of these markets we can find in in China where they have markets that are very liquid, very large, markets that are difficult to access for say US persons and institutions
  indicator: Chinese futures · asset: commodities · horizon: years · conditions: access routes available · testable: no - implementation point · confidence: medium
  ^MT179-C19-X2

### C20
- **Moritz Seibert** Large AUM brings institutional staffing and due-diligence burdens that pull focus from trading; investors in drawdown tend to redeem at lows, so screening for the right investors improves outcomes.  #mech/behavioral
  > If you have a billion, 2 billion, three billion of assets under management, the investors demand you to have that.
  asset: other · horizon: years · testable: no - business opinion · confidence: medium
  ^MT179-C20-1

### C21
- **Dave Drew** Blowing up is the number one reason a long-lived commodity trading firm disappears, followed by ageing or death of the principals; Tactical closed instead because two key employees retired in 2023.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > most most people most commodity traders stop trading because they blow up
  asset: commodities · horizon: years · testable: no - anecdotal base rate · confidence: medium
  ^MT179-C21-X1

### C22
- **Dave Drew** Liquid futures strategies can return capital within about 30 days, so key-person risk is less costly than for illiquid strategies; Tactical closed in 2023 when two key employees retired.  #mech/risk_management
  > need 3 years to get out of an interest rate, you know, credit derivative swap contract
  indicator: fund liquidity · asset: multi · testable: no - business fact · confidence: medium
  **Correction (cross-check):** Wrong speaker and claim: the liquidity and key-person argument (monthly liquidity, no 3-year swap exit) is Moritz Seibert's reasoning in his question; Drew's own answer was that investors were understanding when Tactical closed in early 2023 after two long-time key employees retired. → Seibert argues that a liquid futures manager can return capital within 30 days, so a closure is a small event compared with illiquid strategies; Drew replies that Tactical closed in 2023 when two key employees retired, and that investors understood.
  ^MT179-C22-1
- **Dave Drew** Investors chosen for fit and informed about risks accept a closure or key-person event with understanding, while mismatched investors are likely to redeem at the low, so investor selection is itself risk management.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > your investors if you've selected them according to the criteria you've mentioned they will understand
  indicator: investor fit and redemption behaviour · asset: multi · conditions: investors screened for fit · testable: partly - anecdotal · confidence: medium
  ^MT179-C22-X1

