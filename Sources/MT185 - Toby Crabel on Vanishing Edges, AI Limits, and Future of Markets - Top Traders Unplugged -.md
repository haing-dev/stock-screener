---
source_id: MT185
title: "Toby Crabel on Vanishing Edges, AI Limits, and Future of Markets - Top Traders Unplugged - Ep.152"
date: 2026-04-16
channel: "Top Traders Unplugged"
url: 
words: 10410
claims: 48
added_by_crosscheck: 14
corrections: 4
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Toby Crabel (founder, Crabel Capital Management, short-term systematic futures)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)", "Alan Dunne (co-host)"]
tags: [source, layer0]
---
# Toby Crabel on Vanishing Edges, AI Limits, and Future of Markets - Top Traders Unplugged - Ep.152

**Speakers:** Toby Crabel (founder, Crabel Capital Management, short-term systematic futures); Niels Kaastrup-Larsen (host, Top Traders Unplugged); Alan Dunne (co-host)

**Summary:** April 2026 interview with Crabel on how edges vanish: opening range breakout decayed as 24-hour trading removed the open, markets show more reversals and big-trader liquidity taking, and the firm responds with 10% annual portfolio turnover, generalized balanced mean-reversion/momentum strategies, execution investment and volume-price (effort vs result) research.

**Approach:** short-term trading, opening range breakout, edge decay, execution, volume analysis

**Cross-check completeness estimate of first read:** 0.8 - the first reader caught the core edge-decay, execution, generalised-strategy, volume-effort and replication ideas; misses are supporting caveats and data points (zero-commission origin, session-structure test of ORB, publication persistence, volume comparability, debasement anecdote) and four speaker or direction misreads.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | cold open (humbling markets), intro and sponsor text, tennis to futures biography |
| C02 | 2 | early career, opening range breakout origins |
| C03 | 4 | ORB decay, 24-hour sessions, adding mean reversion, new reference points |
| C04 | 2 | reversals, liquidity moved to the close, Monroe Trout anecdote |
| C05 | 3 | evolving portfolios, market makers, 23 March 2026 gold and silver reversal |
| C06 | 3 | liquidity-taking by big traders, follow-through probability, volume |
| C07 | 2 | quantifying chart patterns, AI vs charts, high-frequency traders |
| C08 | 2 | order book depth, momentum decay and allocation response |
| C09 | 5 | shorter holds, generalized versus optimized strategies, execution as edge |
| C10 | 2 | slippage, AI coding, markets as non-linear, volume watch |
| C11 | 3 | replication, capacity, AI pattern recognition competition |
| C12 | 2 | volume-price research, effort versus result |
| C13 | 2 | philosophy of technical analysis, 1970s analogy, gold and trend |
| C14 | 2 | personal style, S&P pit edge decay, short-term preference |
| C15 | 0 | closing remarks, Substack plug (nothing actionable) |

## Claims

### C02
- **Toby Crabel** Opening range breakout, from Chicago bond floor traders who faded an 8-tick move off the open but followed beyond it, was the foundational short-term momentum edge the speaker built strategies on in the late 1980s.  #mech/slow_reaction
  > if the market moved eight ticks above or below the open, they would actually fade that and if it went beyond that, they would start to to go with it.
  indicator: opening range breakout · asset: multi · direction: buy/sell break of opening range · horizon: days · testable: yes: ORB rule is precise · confidence: high
  ^MT185-C02-1
- **Toby Crabel** Opening range breakout is a measure of intraday momentum, a large factor; the speaker learned the opposing mean-reversion view from Niederhoffer and kept both.  #mech/slow_reaction
  > opening range breakout is a great measure of momentum in markets which is a huge factor.
  indicator: opening range breakout · asset: multi · horizon: days · testable: yes: backtest on intraday data · confidence: high
  ^MT185-C02-2
- **Toby Crabel** Very short-term trading is only viable when transaction costs are near zero: the speaker moved from trend following to shorter-term trading because his partner's account paid no commissions, and the firm's short-term time frame harks back to zero-commission days.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > he had no commissions in his account um as because he was an owner of a brokerage firm. So I then started gradually going towards shorter term trading
  indicator: commission and execution cost per trade · asset: multi · horizon: days · conditions: low or zero transaction costs · testable: yes - net edge per trade vs cost per contract · confidence: high
  ^MT185-C02-X1

### C03
- **Toby Crabel** Trend days are less frequent than before because liquidity is positioned against momentum, pushing strategies toward mean reversion.  #mech/crowding_positioning _(time-bound view)_
  > trend days. Uh generally they're not as frequent it doesn't look like as they used to be. There seem there seem to be there seems to be uh a lot of liquidity against momentum
  indicator: frequency of trend days · asset: multi · direction: fewer trend days, more reversion · horizon: days · testable: yes: count trend days over time · confidence: medium
  ^MT185-C03-1
- **Toby Crabel** Opening range breakout deteriorated (worst in decades in the last 2-3 years) because 24-hour trading removed the meaningful open as a reference point, a dissipation first seen in the 1980s with US Treasury night sessions.  #mech/structural_shift
  > where is the open? I For God's sake, I mean you there's so much volume in the 24-hour sessions, it's impossible to determine what the open is.
  indicator: opening range breakout, 24-hour sessions · asset: multi · horizon: years · conditions: markets with a clear primary session still work (palm oil, Brazil) · testable: yes: compare ORB in 24h versus session markets · confidence: high
  **Correction (cross-check):** Imprecise: Crabel says that apart from an earlier period (caption garbled as '60 to 1962') which was one of the worst for this strategy, the last two or three years have been equally as bad; this is not simply 'worst in decades'. → Opening range breakout has deteriorated: the last two or three years have been as bad as one earlier worst period (year garbled in the captions), because 24-hour sessions make the open impossible to determine, a dissipation first seen in the 1980s with US Treasury night sessions.
  ^MT185-C03-2
- **Toby Crabel** After working with Niederhoffer, the speaker added mean-reversion strategies in the 1990s to offset the expected decay of opening range breakout; the decay took 8-10 more years and is glacial.  #mech/research_method
  > the one thing that you know, I did in the '90s also with my portfolio after working with Victor was to add mean reversion to sort of offset
  indicator: mean reversion added to momentum book · asset: multi · horizon: years · testable: yes: combine mean-reversion and breakout books · confidence: high
  ^MT185-C03-3
- **Toby Crabel** Replacement reference points for the open include the previous close and overnight movement, previous-day highs and lows and the 24-hour session range; they work, though less strongly than the old opening range.  #mech/research_method
  > Uh one is the close of the previous day and the movement off of that.
  indicator: previous close, overnight move, previous-day high/low · asset: multi · horizon: days · testable: yes: test each reference level · confidence: medium
  ^MT185-C03-4
- **Toby Crabel** Publishing the opening-range-breakout edge in 1989 did not kill it: the following decade was among the best ever for the strategy, so a known edge can persist for years and decay came from structural change (24-hour trading) rather than from publicity.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > when I published the book the next 10 years was one of the best periods in history for open opening range breakout
  indicator: opening range breakout returns after publication · asset: multi · horizon: years · conditions: defined primary trading sessions · testable: yes - ORB strategy returns 1989-1999 vs later · confidence: high
  ^MT185-C03-X1

### C04
- **Toby Crabel** There are many more intraday reversals (new overnight lows followed by large rallies) and fewer follow-through days than in a long time.  #mech/crowding_positioning _(time-bound view)_
  > many more reversals uh instead of follow-through days now than there have been in quite a while.
  indicator: reversal frequency vs follow-through · asset: multi · horizon: days · testable: yes: count reversals versus follow-through days · confidence: medium
  ^MT185-C04-1
- **Niels Kaastrup-Larsen** Liquidity has migrated from the open to the close (stock index closing volume is high), making the close a more significant reference point than the open.  #mech/liquidity_flows
  > nowadays it's actually around the close.
  indicator: closing volume in S&P futures · asset: equities · horizon: days · testable: yes: intraday volume profile · confidence: medium
  ^MT185-C04-2
- **Toby Crabel** Markets that still trade a defined primary session (the examples named are palm oil and Brazilian markets) show much better opening-range-breakout results, supporting the explanation that 24-hour trading destroyed the open as a reference point; in stock indices momentum is strong but crossover around an obscured open widens the path.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > When that is happening, those markets have much better results for the open the opening range breakout concept
  indicator: opening range breakout performance by market trading-hours structure · asset: multi · direction: ORB works where a primary session exists · horizon: days · conditions: single primary session vs 24-hour trading · testable: yes - cross-section of ORB results by market session structure · confidence: medium
  ^MT185-C04-X1

### C05
- **Toby Crabel** Old portfolios do not work as well as current ones, and the firm changes 10% or more of its portfolio every year because markets evolve; without changes the 5-10 year old portfolio would have gone out of business.  #mech/research_method
  > there's probably a 10% or more shift in our portfolios every year because of the the amount of work we're doing now.
  indicator: annual portfolio turnover of strategies about 10% · asset: multi · horizon: years · testable: yes: rolling comparison of old versus current portfolio · confidence: high
  ^MT185-C05-1
- **Toby Crabel** Large algorithmic market makers and big traders use activity beyond prior-day highs and lows to enter and exit, so volatile liquidity events are an opportunity for big traders and reversals are more common.  #mech/liquidity_flows
  > the market makers now, they're all, you know, algorithmic um and they're huge. And um most of them are very profitable. And we work against them.
  indicator: previous-day highs and lows, volume spikes · asset: multi · horizon: days · testable: partly: needs volume data by participant · confidence: medium
  ^MT185-C05-2
- **Toby Crabel** On 23 March 2026 gold and silver fell and reversed on 5-10 times normal volume, with large contracts trading ten minutes before Iran-talk headlines; the speaker sees this as big players using fear-driven liquidation to buy.  #mech/liquidity_flows _(time-bound view)_
  > five, 10 times more volume than typically.
  indicator: volume spike at lows in gold and silver · asset: commodities · direction: buy after high-volume low in a bull market · horizon: days · testable: partly: single episode · confidence: medium
  ^MT185-C05-3
- **Toby Crabel** Uncertainty has grown, especially in the last few years, so outlier moves catch portfolios more easily and do more damage, although the basic concepts remain valid and there is room for new ones.  #mech/risk_management _(added by sonnet-xhigh cross-check, time-bound view)_
  > that means that sort of outlier movements can catch you uh I think a little bit easier than they used to be
  indicator: outlier move frequency and damage · asset: multi · horizon: years · conditions: recent years · testable: yes - tail event frequency and drawdown contribution over time · confidence: medium
  ^MT185-C05-X1
- **Toby Crabel** Daily percentage moves in gold and silver on 23 March 2026 look larger than ever before, a claim the speaker says can be verified from price history.  #mech/overshoot _(added by sonnet-xhigh cross-check, time-bound view)_
  > damn it, they seem much larger than they've ever been and I think we could probably verify that
  indicator: gold and silver daily percentage change · asset: commodities · horizon: days · conditions: March 2026 Iran-related volatility · testable: yes - price history · confidence: medium
  ^MT185-C05-X2

### C06
- **Toby Crabel** Big traders need liquidity, and markets trading through highs and lows provide it from fearful traders liquidating, so breaks of obvious levels are often traps.  #mech/liquidity_flows
  > Big traders need liquidity. They need they need they need to get fed, so to speak, and the markets by trading through highs and lows provide that liquidity
  indicator: breaks of prior highs and lows with volume · asset: multi · horizon: days · testable: yes: study stop-run reversals · confidence: medium
  ^MT185-C06-1
- **Toby Crabel** The probability of follow-through after a higher low was taken out fell from about 62% to 58%; a few percentage points of edge decay change the behaviour of markets materially.  #mech/cycle_persistence
  > let's say that it used to be, you know, 62% of the time the market would follow through after it took out a higher low. Well, now it's only 58% of the time.
  indicator: follow-through probability 62% to 58% · asset: multi · horizon: days · testable: yes: measurable rate · confidence: medium
  ^MT185-C06-2
- **Toby Crabel** Large volume outside prior ranges signals opportunity for big players; volume is more important now than the speaker recalls, as seen in Wyckoff's 1930s study of the New York Times index in a volatile bear market.  #mech/liquidity_flows
  > there's huge interests that are taking advantage of liquidity pockets. Wherever that wherever that volume comes in, they that's, you know, their eyes open wide.
  indicator: volume outside prior range · asset: multi · horizon: days · testable: yes: volume-conditioned signals · confidence: medium
  ^MT185-C06-3
- **Toby Crabel** If gold and silver hold after the 23 March reversal and this is only a pullback in a bull market (there is precedent), the next three to six months could be sharply higher; the speaker cannot hold a position that long himself.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > Then I hate to see what the next three to six months are to the upside
  indicator: gold and silver price after pullback · asset: commodities · direction: gold and silver higher · horizon: months · conditions: price holds after the March 2026 reversal · testable: yes - outcome observable · confidence: low
  ^MT185-C06-X1
- **Toby Crabel** Momentum makes money even though the speaker does not like it personally, but it is very hard to trade on a discretionary basis because the market moves slowly during the process, which makes it better suited to systematic rules.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > it's very hard to do it uh on a discretionary basis because the market moves much slower in that process
  asset: multi · conditions: discretionary execution of momentum · testable: partly - discretionary vs systematic momentum performance · confidence: medium
  ^MT185-C06-X2

### C07
- **Toby Crabel** Charts show what is going on; the firm quantifies visual observations to detect market changes, and the human mind still extracts information from charts better than a computer, so we still must tell the computer what to do.  #mech/research_method
  > The charts aren't really look I it's not like you there's a there's a a premise that we we have to hold to all the time.
  asset: multi · testable: partly: visual features can be quantified · confidence: medium
  ^MT185-C07-1
- **Toby Crabel** High-frequency firms act like the old floor traders as the liquidity backbone and do not take alpha from short-term managers; they pay heavily for microsecond speed, while the firm invests in execution instead.  #mech/liquidity_flows
  > the high frequency groups, you know, they really are the liquidity uh backbone of the markets.
  indicator: high-frequency traders · asset: multi · horizon: days · testable: no: opinion · confidence: medium
  **Correction (cross-check):** Overstated: Crabel says high-frequency groups are the liquidity backbone, like the old floor traders, make money and need to spend millions for microseconds, and he does not begrudge them; he does not say they leave short-term managers' alpha untouched (he notes some nuances are a little frustrating). → Toby Crabel: high-frequency firms are the liquidity backbone, comparable to floor traders, and will make money; they spend millions of dollars for a few microseconds of speed, whereas the firm prefers to invest in cheaper execution edge, while acknowledging some frustrating nuances.
  ^MT185-C07-2
- **Alan Dunne** Candidate causes of edge decay over three to four decades include new products, more retail participation, prop shops, zero-DTE options and structured products; Crabel does not isolate one cause but detects change by looking at charts and then quantifying it.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > maybe increased retail participation. You've got prop shops. You've got, you know, new options activity, zero DTEs. You got a lot of structure products
  asset: multi · horizon: years · testable: partly - each driver could be tested against edge decay · confidence: medium
  ^MT185-C07-X1

### C08
- **Toby Crabel** S&P futures book depth fell from about 500 contracts to about 20 at the touch while volume rose, so execution is more cagey and splitting orders is needed.  #mech/liquidity_flows
  > Well, you're lucky to get 20 now uh showing on the in the book.
  indicator: S&P futures displayed depth · asset: equities · horizon: days · testable: yes: order-book depth data · confidence: medium
  ^MT185-C08-1
- **Toby Crabel** Basic momentum strategies have deteriorated by 4-5 points of hit rate (still above 50%) because options traders and pod groups compress volatility; the firm shifts allocation, front-loads adjustments and monitors each portfolio section by market.  #mech/crowding_positioning
  > there's been a deterioration in the momentum basic momentum strategies of 4 or 5% say say they're still successful uh above 50% or something like that
  indicator: momentum hit rate · asset: multi · horizon: years · testable: yes: track hit rate decay by strategy · confidence: medium
  ^MT185-C08-2

### C09
- **Toby Crabel** Markets are news-prone and jumpy, so the short-term program's average hold has shortened from about 36 hours to less.  #mech/structural_shift _(time-bound view)_
  > Our portfolio has gone from probably an average of 36-hour hold to something less than
  indicator: average holding period · asset: multi · horizon: days · testable: yes: holding period measurable · confidence: medium
  ^MT185-C09-1
- **Toby Crabel** Portfolio of six uncorrelated mean-reversion and six momentum general strategies with balanced weight; four of the top five performers that year were the generalized ones even though optimized strategies looked better on paper.  #mech/research_method
  > late in the late '90s I decided to generalize uh the strategies into a portfolio of six primary mean reversion strategies and six primary uh momentum strategies
  indicator: 6 mean reversion + 6 momentum strategies · asset: multi · horizon: years · testable: yes: compare general versus optimized versions · confidence: high
  ^MT185-C09-2
- **Toby Crabel** Over-optimization is self-deception; generalized strategies hold up (some 1990s strategies still run), and the speaker looks for strategies that could last 50 years.  #mech/research_method
  > if you optimize too much, you're fooling yourself in this in this systematic area.
  asset: multi · testable: yes: out-of-sample decay of optimized vs general · confidence: high
  ^MT185-C09-3
- **Toby Crabel** Markets are as tough as in 40-50 years; there is a '70s-like environment but with an unidentified further factor causing challenges.  #mech/structural_shift _(time-bound view)_
  > I think we're kind of in a '70s environment.
  asset: multi · horizon: years · testable: no: vague · confidence: low
  ^MT185-C09-4
- **Toby Crabel** Execution is a main source of edge: execution quality has improved by multiples in 20-25 years and slippage is at the best level in the firm's history.  #mech/risk_management
  > you have to get better at execution. Find ways of doing something that don't cost you
  indicator: slippage · asset: multi · testable: yes: slippage reports measurable · confidence: high
  ^MT185-C09-5
- **Toby Crabel** Although conditions are the toughest for systematic traders in 40-50 years, the speaker expects them to improve, with something beyond the 1970s analogy still unidentified.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > And you would think it I I think they're going to get better
  asset: multi · horizon: years · conditions: after the current hard period · testable: no - forecast · confidence: low
  ^MT185-C09-X1

### C10
- **Toby Crabel** Extraordinary volume at any point of the day, especially at the start of a regional session, is a signal worth watching.  #mech/liquidity_flows
  > Watch out for extraordinary volume. At any point of the day.
  indicator: intraday volume spikes · asset: multi · horizon: days · testable: yes: volume-spike event study · confidence: medium
  ^MT185-C10-1
- **Toby Crabel** Markets are non-linear and only probabilistic, so AI cannot give a reliable 5-minute forecast and anything can happen; the mood among systematic and discretionary traders is humility.  #mech/research_method
  > you've got to expect that anything can happen. Anything can happen in the markets.
  asset: multi · testable: no: philosophy · confidence: high
  ^MT185-C10-2
- **Toby Crabel** AI coding tools (Codex and others) let staff build and program verbally, the CEO pushes a firm-wide mandate including back office, and the speaker sees this as the next major change, cutting development and operating cost.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > pretty much everybody in the firm is coding. But now, coding is different than it's ever been
  asset: multi · horizon: years · testable: no - qualitative management practice · confidence: high
  ^MT185-C10-X1

### C11
- **Toby Crabel** Capacity is assessed by net dollars per contract against execution cost; if the margin is thin there is a problem, and this matters far more for very short-term than 5-10 day holds.  #mech/risk_management
  > we look at our dollars per contract net and we look at what it's costing us to actually execute. And if there's not a fair margin there
  indicator: net dollars per contract, execution cost · asset: multi · horizon: days · testable: yes: define margin threshold · confidence: high
  ^MT185-C11-1
- **Toby Crabel** Short-term strategies are hard to replicate because of nuance and heavy execution investment; trend following products are easier to replicate but the firm's version has done slightly better.  #mech/research_method
  > there's enough nuance and interesting elements about it that it's going to be very it's going to be hard to replicate. That's why it's a higher cost product.
  indicator: replication of short-term vs trend · asset: multi · testable: partly: replicate and compare · confidence: medium
  ^MT185-C11-2
- **Toby Crabel** AI and genetic algorithms accelerate quantification, so short-term trading becomes more competitive as everyone uses every tool.  #mech/crowding_positioning
  > speed and uh ability to quantify data is really what what what it's all about.
  asset: multi · horizon: years · testable: no: assertion · confidence: medium
  ^MT185-C11-3

### C12
- **Toby Crabel** The relationship between volume and price is under-researched; many stick to price alone and miss nuance, and a deep database remains unexplored.  #mech/research_method
  > volume itself and the relationships of volume to price is a subject that I think a lot of people have overlooked.
  indicator: volume-price relationship · asset: multi · testable: yes: add volume features to price models · confidence: medium
  ^MT185-C12-1
- **Toby Crabel** Wyckoff's effort versus result: high volume with a narrow range or a dead stop in a rally or decline signals large players absorbing and standing in front of the move, so do not buy there.  #mech/liquidity_flows
  > Effort is volume and the result is the position of the price range, the size of the price range
  indicator: volume versus range (effort/result) · asset: multi · direction: avoid buying a rally stopped dead on high volume · horizon: days · testable: yes: define effort/result ratio · confidence: medium
  **Correction (cross-check):** Direction is incomplete: for the rally case Crabel says large traders stopping a rally dead with high volume is not a place to buy, but for the decline case (market goes down, dead stops, narrow range, high volume) he says someone is standing in front of the move, which means selling into that stall is unattractive, not that one should not buy. → Wyckoff effort versus result (effort = volume, result = price range): high volume with a narrow range at a dead stop shows a large trader absorbing flow; after a rally it is a poor place to buy, and at a low it signals someone standing in front of the move (do not chase the decline).
  ^MT185-C12-2
- **Toby Crabel** Quantifying price behaviour is an endless and slow process: databases are so deep that each answered question raises about 50 more, so research has barely scratched the surface even with AI tools.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > there's one question that's being answered and some development around that, there's going to be another 50 to be asked right after that
  asset: multi · horizon: years · testable: no - qualitative · confidence: medium
  ^MT185-C12-X1
- **Toby Crabel** Volume is hard to use consistently because its scale has changed enormously (15 million NYSE shares a day was huge in the 1970s), so tracking volume per market across eras requires care, one reason the volume-price relation is under-researched.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > So, tracking volume in individual markets is not an easy thing.
  indicator: volume series comparability over time · asset: equities · horizon: years · conditions: long-history volume research · testable: yes - volume normalisation methods can be compared · confidence: medium
  ^MT185-C12-X2

### C13
- **Toby Crabel** Technical analysis lacks a philosophical justification; charts (bars and candles) hold dense information through a cognitive element, which is the topic of the speaker's next book.  #mech/research_method
  > there's a cognitive element here that has to be considered. It seems to me to be really one of the best ways to pick up this information
  asset: multi · testable: no: philosophy · confidence: low
  ^MT185-C13-1
- **Toby Crabel** The current environment resembles the 1970s (debasement, gold and silver, trend following profitable, large abrupt moves) but is bigger and global; the 200-day moving average has become more important.  #mech/structural_shift _(time-bound view)_
  > Now, of course, it's different. It's so much bigger, it seems like and it's it permeates globally.
  indicator: 200-day moving average; gold and silver · asset: multi · direction: long gold and silver, trend following up · horizon: years · testable: partly: analogy · confidence: medium
  **Correction (cross-check):** Wrong speaker for one element: the remark that the 200-day moving average has become much more important is a host's inference ('I guess') after Crabel said the short-term moves are generally with the trend; Crabel did not say it. → Toby Crabel: the current environment resembles the 1970s (debasement, gold and silver, profitable trend following, large abrupt moves) but is bigger and global. Host (inference): the 200-day moving average may have become more important.
  ^MT185-C13-2
- **Toby Crabel** In the March 2026 environment the firm's trend-following products did very well, while the short-term program was less spectacular because moves are so abrupt, though they generally go with the trend.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > the short-term's a little interesting though. I I have to say it's not quite as quite as spectacular, but the movements are so abrupt
  indicator: short-term program vs trend products · asset: multi · direction: trend following outperforms short-term in large abrupt moves · horizon: months · conditions: 1970s-like environment with large abrupt moves · testable: yes - compare firm and index returns of short-term vs trend CTAs · confidence: medium
  ^MT185-C13-X1
- **Toby Crabel** Currency debasement is illustrated by a $100 life insurance policy in the speaker's trust that has lost 95% of its value against gold, which he cites as why gold and silver (he buys physical coins) and stocks have made such tremendous moves.  #mech/fiscal_debt _(added by sonnet-xhigh cross-check, time-bound view)_
  > it's lost 95% of its value value against gold for my kids
  indicator: purchasing power of dollar vs gold · asset: commodities · direction: gold and silver higher vs currency · horizon: years · conditions: debasement regime · testable: yes - dollar price of gold over the policy's life · confidence: medium
  ^MT185-C13-X2

### C14
- **Toby Crabel** An early S&P pit pattern (straight runs of 5-10 five-minute bars) quadrupled an account in two months until institutions entered and compressed the market, showing how quickly an edge disappears when participants change.  #mech/crowding_positioning
  > Essentially the market would at the beginning would go straight up and straight down for five, six, even 10 bars in a row without taking out a low or or taking out a high
  indicator: 5-minute bar runs in S&P futures · asset: equities · horizon: days · testable: yes: historical edge decay example · confidence: high
  ^MT185-C14-1
- **Toby Crabel** Short-term trading gave better risk-adjusted returns and diversification versus trend following, which the speaker had done in the early 80s.  #mech/risk_premium
  > I just thought there was a better risk-adjusted return there.
  asset: multi · horizon: years · testable: partly: compare Sharpe of short-term vs trend · confidence: low
  ^MT185-C14-2

