---
source_id: MT143
title: "Sharing the Trend Following Pie - Systematic Investor 299"
date: 2024-06-12
channel: "Top Traders Unplugged"
url: 
words: 13338
claims: 60
added_by_crosscheck: 12
corrections: 1
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Niels Kaastrup-Larsen (host, Top Traders Unplugged, trend-following background)", "Andrew Beer (co-manager of DBMF managed futures replication ETF)"]
tags: [source, layer0]
---
# Sharing the Trend Following Pie - Systematic Investor 299

**Speakers:** Niels Kaastrup-Larsen (host, Top Traders Unplugged, trend-following background); Andrew Beer (co-manager of DBMF managed futures replication ETF)

**Summary:** Weekly Systematic Investor episode (June 2024). Beer and Kaastrup-Larsen discuss why short selling stopped paying, why trend followers are the only true shorts, how replication handles lag and reversals, Pivotal Path data showing managed futures are only ~6% of hedge fund assets despite zero equity correlation and 340bp alpha, and why advisors/allocators do not buy them (narrative, anxiety, fees, ETF economics).

**Approach:** trend following, managed futures replication, short selling, hedge fund industry structure, real yields, ETF fees, allocator behavior

**Cross-check completeness estimate of first read:** 0.82 - first reader caught the core arguments on short selling, replication lag, Pivotal Path statistics and the adoption barriers (about 56 of roughly 68 ideas); missed the June 2024 macro views, the trend-window lag mechanics, reversal persistence, fee-differential and data-sample details

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | small talk: US politics, weather, European elections; nothing actionable |
| C02 | 2 | real yields pre/post 2009 and debt-service/bond vigilante risk |
| C03 | 3 | near-term macro forecasts no better than coin toss; macro models crisis; short sellers closing |
| C04 | 4 | trend followers as the only true shorts; asymmetry and timing risk of single-stock shorting |
| C05 | 4 | capacity limits and selection bias in short selling; two dominant investor types |
| C06 | 3 | trend following edge vs value buyers, 2022 alpha, timing CTA entry |
| C07 | 5 | dollar cost averaging into CTAs, trend index performance, replication lag and Nov 2023 reversal |
| C08 | 2 | head fakes and window-based replication; speed of exits trade-off |
| C09 | 4 | faster exit research vs Sharpe, replication adaptivity, skis pointing the same way |
| C10 | 3 | stop prevention is costly; hedge fund fees; Pivotal Path data intro |
| C11 | 4 | managed futures share of hedge fund assets, correlation, beta, alpha, Sharpe |
| C12 | 1 | allocator incentives and why institutions do not adopt replication |
| C13 | 2 | why managed futures has not grown: smoothing and nomenclature (private equity analogy) |
| C14 | 3 | narrative gap vs equity long short, crisis alpha framing, 60/40 to 50/30/20 |
| C15 | 2 | advisor communication, beacon of green, sister anecdote start |
| C16 | 1 | macro as worry-less strategy, advisor emotions, concern about fee race |
| C17 | 2 | low-cost airline analogy, low fees not necessarily good |
| C18 | 2 | ETF cost structure, fees and manager economics, new entrants |
| C19 | 1 | wealth management walled gardens, pricing floor, close |
| C20 | 0 | outro; nothing actionable |

## Claims

### C02
- **Niels Kaastrup-Larsen** Pre-2009 US real yields were about 2% above inflation but since then about 0.25% or less; the past 10-15 years may be the abnormal period, so rates dropping at the long end is not assured and many portfolios are not positioned for normal real yields.  #mech/structural_shift _(time-bound view)_
  > before 2009 so before really the GFC real yields in the US was about 2% above inflation
  indicator: US real yields vs inflation · asset: rates · direction: rates higher for longer at the long end · horizon: years · testable: yes - real yield series are public · confidence: medium
  ^MT143-C02-1
- **Niels Kaastrup-Larsen** With real yields near 2% and 4.5-5.5% on 10- and 30-year bonds, heavily indebted governments risk Truss-style moments where excess stimulus triggers a bond market collapse until the government steps in.  #mech/fiscal_debt _(time-bound view)_
  > then the bond V Vigilantes will come out and basically with their feet and and the bond markets collapse
  indicator: 10y/30y yields, government debt service · asset: rates · direction: bond yields up on fiscal slippage · horizon: months · conditions: when governments run excess stimulus · testable: partly - episodic · confidence: medium
  ^MT143-C02-2
- **Niels Kaastrup-Larsen** June 2024 view: the strong US jobs report is further evidence against the claim that rates will fall sharply and inflation will quickly return to 2%, so he stays cautious on rate cuts.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > the latest us unemployment numbers which are somewhat surprising for those who keep saying that interest rates are going to drop like a stone
  indicator: US monthly employment report · asset: rates · direction: rates do not fall quickly · horizon: months · conditions: labour market stays strong · testable: partly - jobs surprise versus subsequent rate path · confidence: medium
  ^MT143-C02-X1

### C03
- **Andrew Beer** Market expectations for the 2-year yield a year ahead are always wrong (chart of rate forecasts as filaments around the actual line), so near-term macro predictions are no better than a coin toss.  #mech/research_method
  > these near-term macro predictions that have are really no better than a toin than a coin toss
  indicator: consensus 2y Treasury yield forecast · asset: rates · horizon: months · testable: yes - forecast error vs realised yields can be measured · confidence: high
  ^MT143-C03-1
- **Andrew Beer** Macro models failed to anticipate the 2010s (no fiscal restraint yet no inflation in 2014-15), so people have no good replacement.  #mech/research_method
  > I think there is a existential crisis in a lot of macroeconomic modeling
  indicator: macroeconomic models · asset: multi · horizon: years · testable: partly - forecast accuracy of models is testable · confidence: high
  ^MT143-C03-2
- **Andrew Beer** Media rotate commentators depending on the latest print and each commentator is talking his own book, adding noise to macro commentary.  #mech/behavioral
  > who are generally always talking their own books in some way shape or form
  asset: multi · testable: no · confidence: medium
  ^MT143-C03-3
- **Andrew Beer** June 2024 non-quantitative view: the US economy does not feel like it is slowing much or entering recession (only pockets of weakness), held with low conviction.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > it doesn't feel recession let's say um but two months from now I could be wrong
  asset: multi · direction: no recession · horizon: months · testable: no - gut feel · confidence: low
  ^MT143-C03-X1
- **Andrew Beer** Managed-futures and trend managers were positioned in mid-2024 for a stronger-inflation, higher-yield environment (short bonds), so a strong data print helps their performance.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check, time-bound view)_
  > I'm kind of Happy the number came in strong today because it's been you know I mean I think a lot of a lot of us have been positioned for you know a healthier inflationary environment
  indicator: strong US data surprise · asset: rates · direction: short bonds benefits from strong data · horizon: weeks · conditions: CTA positioning short bonds · testable: partly - CTA bond positioning versus data surprises · confidence: medium
  ^MT143-C03-X2

### C04
- **Niels Kaastrup-Larsen** Investors redeem after trend following is declared dead, then it posts a strong run about six months later; short sellers closing (Chanos etc.) after a long bull market may come just before shorts are most needed.  #mech/behavioral
  > every time Trend following is pronounced dead people redeem and then you know hey ho 6 months later they have a great run
  indicator: trend-following returns after drawdowns · asset: multi · horizon: months · conditions: after periods of poor performance · testable: yes - flows vs subsequent CTA returns can be tested · confidence: medium
  ^MT143-C04-1
- **Niels Kaastrup-Larsen** Trend followers have no long bias so they were genuinely short bonds in 2022-2024, whereas bearish macro managers often held other positions instead of shorting bonds; trend followers may be the only true short sellers left.  #mech/structural_shift _(time-bound view)_
  > we can truly go short when markets point in that direction
  indicator: CTA positioning in bonds · asset: rates · direction: short bonds 2022-2024 · horizon: years · conditions: rising yield regimes · testable: partly - compare stated views to actual positions · confidence: medium
  ^MT143-C04-2
- **Andrew Beer** Single-stock short selling has a horribly asymmetric payoff: at best about 50% gain while losses can reach 200%, so the odds are stacked against it.  #mech/risk_premium
  > if you get it unbelievably perfect timing and everything else you make 50% you know if you get the timing wrong or or other things you know you lose 200%
  asset: equities · direction: avoid single-stock shorts · testable: yes - payoff asymmetry is arithmetic · confidence: high
  ^MT143-C04-3
- **Andrew Beer** Even correct fundamental shorts can fail through takeover premiums or prolonged mispricing (Chanos story), so being right on fundamentals does not make a short work.  #mech/risk_management
  > the answer is we just got to take over all like you know 70% premium to the stock
  indicator: takeover premium · asset: equities · testable: partly - anecdote · confidence: medium
  ^MT143-C04-4

### C05
- **Andrew Beer** A hedge fund can run a concentrated long book but a short book must be diversified, so beyond a certain size shorting individual stocks cannot generate alpha (Tesla wiped out shorts; Melvin/GameStop).  #mech/crowding_positioning
  > as you get bigger the the the short constraints or the capacity constraints on the short side um are are are become much much more difficult
  indicator: short book capacity · asset: equities · horizon: years · conditions: as AUM grows · testable: partly - plausible, requires fund data · confidence: medium
  ^MT143-C05-1
- **Andrew Beer** Short-selling alpha seen in selected funds (Einhorn on Lehman, Chanos on Enron) vanished the moment allocators invested, because of selection bias and a halo effect.  #mech/research_method
  > it was just selection bias right you you get 50 guys who are doing it and you're looking around you're GNA there a couple of guys who going to look like like Geniuses
  indicator: short-seller alpha after investing · asset: equities · horizon: years · testable: yes - post-selection performance is testable · confidence: high
  ^MT143-C05-2
- **Niels Kaastrup-Larsen** Trend followers earn from broad bear markets in diversified sectors without needing single-stock shorts, which helps portfolios.  #mech/cycle_persistence
  > we as Trend followers believe that markets move up and down
  asset: multi · direction: short broad bear markets · testable: yes · confidence: medium
  ^MT143-C05-3
- **Andrew Beer** Investing is dominated by slow-moving long-only asset allocation models and by mean-reversion/intrinsic-value stock pickers, so few participants trade momentum.  #mech/crowding_positioning
  > is dominated by two kinds of people
  asset: equities · testable: partly · confidence: medium
  ^MT143-C05-4

### C06
- **Andrew Beer** Fundamental pickers buy after declines (long holding periods, belief the market mispriced) while trend following shorts more as the market goes from 100 to 80, a competitive advantage because it ignores intrinsic value.  #mech/slow_reaction
  > something like Trend following which will short after it's already gone down
  asset: equities · direction: trend following short after decline · horizon: months · conditions: drawdowns · testable: yes - behaviour of trend vs value in declines · confidence: medium
  ^MT143-C06-1
- **Andrew Beer** Trend following alpha comes from being the one group built to exploit large trends: in 2022 hundreds of billions of alpha were available because most of the investing world could not act.  #mech/slow_reaction _(time-bound view)_
  > the magnitude the hundreds of billions of dollars of of Alpha can be generated for a period of time
  asset: multi · horizon: years · conditions: in persistent macro trends such as 2022 · testable: partly - 2022 CTA returns known · confidence: medium
  ^MT143-C06-2
- **Andrew Beer** Do not try to time entry into trend following; most investors set a 3-5% allocation after months of study and timing is too random.  #mech/behavioral
  > if you're trying to time this and you're part you know try to pick the bottom or something honestly don't
  asset: multi · testable: partly - timing evidence for CTA entry could be studied · confidence: medium
  ^MT143-C06-3

### C07
- **Andrew Beer** Phase into a 5% CTA allocation by thirds over three quarters (dollar cost averaging) to avoid entering at the worst point, as many investors did in 2022 before a bad 2023.  #mech/risk_management
  > dial it in over over over three allocations you know do a third each quarter for the next three quarters
  asset: multi · direction: scale in over three quarters · horizon: months · testable: yes - phased vs lump-sum entry is testable · confidence: medium
  ^MT143-C07-1
- **Andrew Beer** Managed futures should be a long-term strategic allocation; as a six-month trade investors will be disappointed and leave.  #mech/behavioral
  > if they're thinking about this as a 6mon trade I honestly say it's I don't think you should
  asset: multi · horizon: years · testable: no · confidence: high
  ^MT143-C07-2
- **Niels Kaastrup-Larsen** June 2024 trend environment: his Trend barometer 41 (neutral to weak), uses short time frames and tracks the short-term traders index (+2.38% YTD) more than the longer-term SG Trend index (+9.21% YTD).  #mech/cycle_persistence _(time-bound view)_
  > my own Trend barometer closed yesterday at 41 so it's kind of neutral to weak
  indicator: Trend barometer; SG CTA, SG Trend, SG Short-term Traders indices · asset: multi · horizon: months · testable: partly - indices are public · confidence: medium
  ^MT143-C07-3
- **Andrew Beer** Replication looks back about four weeks of data and so always lags the funds it tracks.  #mech/slow_reaction
  > replication will always be a little bit slower than the underlying funds
  indicator: replication of managed futures indices (four-week look-back) · asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT143-C07-4
- **Andrew Beer** On 1 Nov 2023 Powell signalled the end of hikes and nearly everyone was short Treasuries; the sharp reversal hit all trend-followers and replicators at once.  #mech/crowding_positioning _(time-bound view)_
  > we've all collectively walked into a propeller
  indicator: Treasury short positioning, SG CTA index · asset: rates · horizon: weeks · conditions: at inflection points after a steady trend · testable: partly - event study · confidence: high
  ^MT143-C07-5
- **Niels Kaastrup-Larsen** Early-June 2024 scoreboard: BTOP50 and SG CTA both +7.2% YTD, SG Trend +9.21%, short-term traders +2.38% versus MSCI World +10.12% and S&P 500 +12.9%, i.e. trend followers lagged a strong equity market while bonds sold off after the jobs number.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > msci world as of last night up 1.3% in June up 10.12 for the year
  indicator: BTOP50, SG CTA, SG Trend, MSCI World, S&P 500 YTD returns · asset: multi · horizon: months · testable: yes - index returns are public · confidence: high
  ^MT143-C07-X1

### C08
- **Andrew Beer** Sharp one- or two-day reversals often reverse; a slower window (17 old data points plus 3 new) therefore avoids some whipsaw even if it misses real reversals.  #mech/slow_reaction
  > empirically though a lot of the times that sharp move is a head fake
  indicator: replication window, sharp reversals · asset: multi · horizon: weeks · conditions: after sudden risk-off events that fade · testable: yes - head fake frequency is testable · confidence: medium
  ^MT143-C08-1
- **Andrew Beer** Managers with fast exits get out earlier on reversals but are likely to underperform in sustained trend years like 2022; the choice depends on loss tolerance vs long-term returns.  #mech/risk_management
  > guys like that also you know in in a period like 2022 they're also likely to underperform
  indicator: exit speed · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT143-C08-2
- **Andrew Beer** Window-return trend signals stay long through the first part of a reversal (10 to 20 then back to 18 still shows +80% over the window), so exits are inherently late; when a steady rise has every short, medium and long horizon long, the whole trend universe is all in and a reversal hits every horizon at once.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > it drops from 20 to 18 right okay so now your now your six-month window of time is 10 to 18 still pretty good
  indicator: six-month window return trend signal · asset: multi · direction: signals flip only after retracement deepens · horizon: weeks · conditions: after a long steady trend with all lookbacks aligned · testable: yes - signal lag after peaks can be simulated · confidence: high
  ^MT143-C08-X1
- **Andrew Beer** The Nov 2023 bond reversal hurt because it continued for about seven weeks, not because it happened; if managers could know a reversal would persist they would all exit within a week, but most sharp one-day moves are head fakes, so exit speed differs by manager (index CTAs with tight trip wires and vol controls de-risk fast, replicators miss it).  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > they would all get out a week after it starts and then avoid the difficulties of the next seven weeks as it continues
  indicator: persistence of a sharp reversal · asset: rates · horizon: weeks · conditions: reversals that continue rather than fake out · testable: partly - fraction of sharp reversals that persist is measurable · confidence: medium
  ^MT143-C08-X2

### C09
- **Andrew Beer** Faster exits and risk reduction in trend following lower drawdowns but add whipsaw risk and probably hurt the Sharpe ratio over time.  #mech/research_method
  > I do see lower draw downs but I see I see also I see you know you're getting lower draw downs but you're adding a different kind of whipsaw risk
  indicator: exit speed, Sharpe ratio, drawdown · asset: multi · horizon: years · testable: yes - testable on CTA index data · confidence: medium
  ^MT143-C09-1
- **Niels Kaastrup-Larsen** We cannot know the counterfactual of unchanged models over 15 years; his own firm's changes did improve Sharpe.  #mech/research_method
  > some of the changes we have made have certainly helped and improved our sharp ratio
  indicator: Sharpe ratio · asset: multi · horizon: years · testable: partly - no counterfactual · confidence: low
  ^MT143-C09-2
- **Andrew Beer** Replication hurts when whipsaw is a market-wide theme across many positions rather than one or two positions going wrong.  #mech/crowding_positioning
  > you've got 11 skis pointing in the same direction
  indicator: number of correlated positions · asset: multi · horizon: weeks · conditions: when a macro theme drives many positions · testable: partly · confidence: medium
  ^MT143-C09-3
- **Andrew Beer** Replication is adaptive because new data is always entering, so a wrong week is corrected the next (model unchanged since 2016).  #mech/slow_reaction
  > what I always liked about replication is when you're when you're wrong you're never that wrong
  indicator: replication model · asset: multi · horizon: weeks · testable: partly · confidence: medium
  ^MT143-C09-4
- **Niels Kaastrup-Larsen** Trend followers have broadly lengthened their lookback periods, and recent manager innovation has focused on reacting faster on the exit side (risk reduction on more than volatility).  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > although Trend followers to a large extent have become longer term in terms of our look back periods and so on and so forth I think that that's I think pretty Universal uh across the space
  indicator: trend lookback length; exit rules · asset: multi · direction: longer entry lookbacks with faster risk-reduction exits · horizon: years · testable: partly - industry-wide evidence is anecdotal · confidence: medium
  ^MT143-C09-X1
- **Niels Kaastrup-Larsen** The common view of trend following Sharpe (about 0.3 as the caption renders it) understates the last ten years of managers' realised Sharpe, which was higher even through the difficult period (caption garbled, treat the exact figure as uncertain).  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > I mean if you look at the manager today the last 10 years it's not3 even though we went through a difficult period of time but it's it's higher than that
  indicator: trend-following Sharpe ratio, last 10 years · asset: multi · horizon: years · testable: yes - manager and index Sharpe ratios are measurable · confidence: low
  ^MT143-C09-X2

### C10
- **Andrew Beer** Predicting drawdowns in advance (stop prevention) is hard and expensive; the space's returns would suffer if everyone tried.  #mech/research_method
  > so the idea that the dream is not that you have a stop loss is you have a stop prevention but but that's really costly and and you end up giving a lot for that
  asset: multi · testable: partly · confidence: medium
  **Correction (cross-check):** Second half misstates the point: Beer says that if the whole space found a way to predict drawdowns and exit early, a slower replication model would capture less of the space's returns (he is skeptical it can be done); he does not say the space's returns would suffer. → Predicting drawdowns in advance ('stop prevention' rather than a stop loss) is very hard and costly; if the space did learn to exit before drawdowns, a replicator that adapts only gradually would capture less of the space's returns, so Beer doubts it can be done.
  ^MT143-C10-1
- **Andrew Beer** Hedge fund fees take about 80% of alpha.  #mech/research_method
  > now hedge fund fees consume 80% of Alpha
  indicator: hedge fund fees · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT143-C10-2
- **Andrew Beer** Hedge fund indices miss large firms (Citadel, Wellington, sometimes Millennium), so Pivotal Path holdings data is the most complete.  #mech/research_method
  > hedge fund databases overall always have this incompleteness issue
  indicator: Pivotal Path, hedge fund databases · asset: multi · testable: yes · confidence: high
  ^MT143-C10-3

### C11
- **Andrew Beer** Pivotal Path shows managed futures are about 6% of hedge fund assets versus equity long/short 37% and multi-strat 20%, so institutions are ridiculously underinvested in managed futures.  #mech/structural_shift
  > Futures represent uh about 6% of the assets
  indicator: Pivotal Path category assets · asset: multi · horizon: years · conditions: data since Sept 2015 · testable: yes · confidence: high
  ^MT143-C11-1
- **Andrew Beer** Correlation to equities: managed futures 0, multi-strat 0.5, equity long/short 0.75; betas 0, 0.1 and 0.3-0.4.  #mech/risk_premium
  > manage Futures is a correlation into two equities of zero
  indicator: correlation and beta to equities by category · asset: multi · horizon: years · conditions: since September 2015 · testable: yes · confidence: high
  ^MT143-C11-2
- **Andrew Beer** Managed futures delivered 340bp per year alpha to an equity allocator, more than multi-strategy funds (280bp), while equity long/short added flat to slightly positive alpha.  #mech/risk_premium
  > manage F has 340 basis points per anom of alpha to an allocator in in stocks
  indicator: alpha vs equities, Pivotal Path categories · asset: multi · horizon: years · conditions: Sept 2015 onward including the long winter · testable: yes · confidence: high
  ^MT143-C11-3
- **Andrew Beer** Managed futures give about 75% of multi-strat returns with double the volatility, hence a lower Sharpe despite the diversification and alpha.  #mech/risk_premium
  > you get 75% of the returns but doubl the all so you end up with a much lower sharp ratio
  indicator: Sharpe ratio, volatility · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT143-C11-4
- **Andrew Beer** Method point: Pivotal Path's managed-futures category covers 58 funds against 20 in the SG CTA index and its data starts in September 2015, so the 340bp alpha estimate spans roughly nine years including the long winter and is a broader sample than a standard CTA index.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > their manage Futures category has 58 funds in it whereas the stock CT index has 20
  indicator: Pivotal Path managed futures category (58 funds) vs SG CTA index (20) · asset: multi · horizon: years · conditions: sample period from Sept 2015 · testable: yes - holdings data is the source · confidence: high
  ^MT143-C11-X1

### C12
- **Andrew Beer** Replication does not help hedge fund allocators because their job and status are tied to evaluating hedge funds, so institutional adoption fails despite lower fees and better drawdowns.  #mech/behavioral
  > we don't make for a typical person in that space whose job is to be a head fund allocator we don't make their life better
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT143-C12-1
- **Niels Kaastrup-Larsen** A low-cost replicator can deliver roughly 300-400bp more net return than a 1.5-and-10 fee structure for similar exposure, which is why it risks taking assets from incumbent managers rather than only growing the pie.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > I can give you a better return 3 to 400 basis points more because we have low cost
  indicator: fee drag versus replication · asset: multi · horizon: years · conditions: similar gross exposure · testable: yes - fee differential versus tracking error · confidence: medium
  ^MT143-C12-X1

### C13
- **Andrew Beer** Private equity grew by selling smoothed marks to pension allocators who prefer a 5% markdown to a true 30-40% loss in front of an unsophisticated committee.  #mech/behavioral
  > would I rather have something that got marked down five in that period of time
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT143-C13-1
- **Andrew Beer** Name matters for adoption: private equity and high yield sound good while managed futures causes anxiety.  #mech/behavioral
  > managed Futures does not have an inherent positive connotation
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT143-C13-2
- **Niels Kaastrup-Larsen** Visible external CTA assets understate trend-following adoption because large pension funds likely run trend following in-house, although the data does not show it.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > I'm sure more more big Pension funds do internal Trend follow I'm I'm pretty sure of that but we don't see the those kind of numbers
  indicator: CTA industry assets · asset: multi · horizon: years · testable: no - in-house assets are not observable · confidence: low
  ^MT143-C13-X1

### C14
- **Andrew Beer** Equity long/short managers can explain drawdowns (cheap stocks got cheaper), whereas managed futures lack a narrative, so allocators fear explaining a drawdown to the investment committee.  #mech/behavioral
  > they are armed with a narrative not just on the initial investment but how to manage it over time
  asset: multi · testable: no · confidence: medium
  ^MT143-C14-1
- **Andrew Beer** Crisis alpha framing pushes investors to time purchases instead of holding managed futures permanently.  #mech/behavioral
  > it gets people focused on the issue that youve described is should I buy it today or next month
  indicator: crisis alpha · asset: multi · testable: no · confidence: medium
  ^MT143-C14-2
- **Andrew Beer** Portfolios are shifting from 60/40 to 50/30/20 and the 20% alternatives bucket is where managed futures compete with gold and TIPS.  #mech/structural_shift
  > the world is going from 60 40 to 50 30 20
  indicator: portfolio allocation · asset: multi · direction: managed futures 3-5% of the 20% · horizon: years · testable: partly · confidence: medium
  ^MT143-C14-3

### C15
- **Andrew Beer** A 5% managed futures allocation will not save a portfolio in a major bear market but helps at the margin as the green in a sea of red.  #mech/risk_premium
  > something's working when nothing else is working
  asset: multi · conditions: bear markets · testable: partly · confidence: medium
  ^MT143-C15-1
- **Andrew Beer** Advisors will not allocate to a product they cannot explain simply to clients.  #mech/behavioral
  > if the adviser doesn't think he can describe that $100,000 in a way that makes the person the other side feel warm and happy
  asset: multi · testable: no · confidence: high
  ^MT143-C15-2

### C16
- **Andrew Beer** Managed futures pitch to retail: macro investors treat world dislocations as opportunities, so a small allocation lets investors worry less.  #mech/behavioral
  > it's a strategy that helps you to worry a little bit less about the world
  asset: multi · testable: no · confidence: medium
  ^MT143-C16-1

### C17
- **Niels Kaastrup-Larsen** Concern that fee cutting turns CTA ETFs into the low-cost airline model, with less experienced and worse products.  #mech/structural_shift
  > if we make this about just getting it cheaper and cheaper and cheaper we're going to introduce we're going to end up with worse products
  indicator: ETF fees · asset: multi · horizon: years · testable: no · confidence: medium
  ^MT143-C17-1
- **Andrew Beer** Low fees are not good if the product is worse; a hedge fund at 10 before / 6 after fees beats a cheap fund at 6 before / 3 after.  #mech/research_method
  > low fees is not necessarily good like lower fees and hedge fundes is not necessarily good
  indicator: net-of-fee returns · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT143-C17-2

### C18
- **Andrew Beer** ETF fees will not fall to zero: running an ETF costs 10-15bp at scale plus marketing and platform costs, and DBMF at 85bp is in line with active ETFs.  #mech/structural_shift
  > it's going to cost 10 to 15 basis points to to to really run it
  indicator: ETF expense ratios · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT143-C18-1
- **Niels Kaastrup-Larsen** If a product charges about 80bp and costs are as high as stated, the manager earns only a few basis points.  #mech/structural_shift
  > the managers certainly are not making more than a few basis points frankly
  indicator: fee levels · asset: multi · horizon: years · testable: no · confidence: medium
  ^MT143-C18-2
- **Andrew Beer** In replication ETFs the market leader's track record is a moat: a pure copycat cannot win, so entrants adapt part of the model, add their own overlay and cut price, which fuels fee competition.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > established it's already there they already have a longer track record so so people are going to come in they're going to say well okay we're kind of try to adapt part of that
  indicator: ETF track record and fees · asset: multi · horizon: years · testable: no - business judgement · confidence: medium
  ^MT143-C18-X1

### C19
- **Andrew Beer** Pricing is held up by distribution gatekeepers (platforms want a cut, hedge fund channels profit from high fees), so ETF fees will not go to zero unless Vanguard decides otherwise.  #mech/structural_shift
  > the US wealth management business is a whole series of Walled Gardens
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT143-C19-1

