---
source_id: MT180
title: "The Trend Following ETF Revolution - Systematic Investor 298"
date: 2024-06-06
channel: "Top Traders Unplugged"
url: 
words: 10284
claims: 38
added_by_crosscheck: 15
corrections: 3
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Katie Kaminski (co-host, Alpha Simplex)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# The Trend Following ETF Revolution - Systematic Investor 298

**Speakers:** Katie Kaminski (co-host, Alpha Simplex); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Systematic Investor 298: May 2024 trend update (long equities, short bonds, long dollar and metals) and Kaminski's paper on managed futures ETFs: regulation, growth, use cases and replication versus direct implementation. ETFs widen access (model portfolios, institutional liquidity buffer), will probably converge toward index-like products, and use fewer liquid markets. Trend following is behavioural and non-predictive, so AI is unlikely to change it.

**Approach:** trend following, managed futures ETFs, CTA replication, model portfolios, 60/40 diversification, AI

**Cross-check completeness estimate of first read:** 0.70 - first reader caught the main ETF structure, use-cases, replication trade-offs and AI view; it missed several secondary points (route taxonomy, hybrid, fee incentives, AUM caveats) and three speaker attributions in the AI section.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro; small talk on Nvidia and Musk pay |
| C02 | 4 | May 2024 trend positioning and index numbers |
| C03 | 1 | traditional markets numbers; ETF paper intro; ETF regulation and growth |
| C04 | 3 | institutional use of ETFs as liquidity buffer; retail share of managed futures; strategic allocation |
| C05 | 2 | model portfolios; bond-stock correlation changes |
| C06 | 2 | changing regime and alternatives; three ETF use cases |
| C07 | 2 | due diligence and know-your-client question; mutual fund convergence |
| C08 | 1 | convergence to institutional correlation; bad to okay; ETF market set |
| C09 | 0 | investor visibility; three ETF routes: full strategy, watered down, replicator |
| C10 | 1 | replication vs direct implementation pros and cons |
| C11 | 2 | single replicator risk; ETF vs classic managed futures |
| C12 | 1 | incentive fees and research focus; many replicators question |
| C13 | 1 | convergence of replicator products; AI intro |
| C14 | 2 | AI and trend following; Nvidia example |
| C15 | 1 | trend following does not predict; outro |

## Claims

### C02
- **Katie Kaminski** Trend positioning in 2024 was polarised: long equities, short fixed income (higher for longer) and long dollar, with a February pivot to long energies and precious and base metals and a May reversal of agricultural short signals.  #mech/slow_reaction _(time-bound view)_
  > you've seen sort of long Equity signals being paired with short fixed income signals as well as long dollar
  indicator: trend positions by sector in 2024 · asset: multi · direction: long equities, long dollar, short bonds, long energy and metals · horizon: months · testable: partly - one year · confidence: high
  ^MT180-C02-1
- **Katie Kaminski** Short fixed income worked as a hedge against the April equity drawdown within the trend portfolio even though it was noisy.  #mech/risk_management _(time-bound view)_
  > short fixed income that's higher for longer and that's been a noisy trade but it has kind of worked and it definitely was a a good position against the equity draw down we saw in April
  indicator: short bond trend position · asset: rates · direction: short bonds gain when inflation and rate fears hit equities · horizon: weeks · conditions: regime of higher-for-longer · testable: partly - single episode · confidence: medium
  ^MT180-C02-2
- **Niels Kaastrup-Larsen** Trend reversals were rolling across sectors rather than simultaneous, so index performance looked calm while manager performance differed depending on sector risk allocation.  #mech/slow_reaction _(time-bound view)_
  > it's almost like kind of a rolling reversals we're kind of seeing different sectors different markets um getting into a little bit of trouble from a trend following perspective but they don't happen all at the same time
  indicator: trend index vs manager dispersion · asset: multi · horizon: months · testable: partly - dispersion data · confidence: medium
  ^MT180-C02-3
- **Niels Kaastrup-Larsen** CTA indices at end of May 2024: BTOP50 -1.14% month and +10.25% YTD, SG CTA -0.62% and +11.18%, SG Trend -0.79% and +13.41%, short-term traders flat and +3.6%; MSCI World +3.5% in May.  #mech/slow_reaction _(time-bound view)_
  > btp 50 was down 1.14% for the month of May still up 10 and a quarter for the year
  indicator: BTOP50, SG CTA, SG Trend, SG Short-Term Traders · asset: multi · horizon: months · testable: yes - index data · confidence: high
  ^MT180-C02-4
- **Niels Kaastrup-Larsen** Large intra-month swings (cocoa 25% off its high, natural gas up 40%) imply performance dispersion between trend managers even in a month when benchmark indices look calm.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > I seem to have seen Coco being off by like 25% from its high I think I've seen natural gas being up by 40% from its end of last month
  indicator: cocoa and natural gas intra-month moves · asset: commodities · direction: dispersion across managers · horizon: weeks · conditions: when large moves reverse within the month · testable: partly - manager-level returns needed · confidence: medium
  ^MT180-C02-X1
- **Niels Kaastrup-Larsen** The host's own trend barometer at 45 (neutral) led the host to expect trend indices to be flat or slightly down for May 2024; the barometer is used as a quick read of the trend environment.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > my own Trend barometer finished uh yesterday at 45 that's pretty neutral
  indicator: Trend barometer (Top Traders Unplugged) · asset: multi · horizon: weeks · testable: partly - definition not stated · confidence: medium
  ^MT180-C02-X2

### C03
- **Katie Kaminski** US regulatory changes (the ETF Rule and the derivatives rule) in 2020 opened the door to futures-based ETFs; systematic trend ETF assets grew from about $220m to $1.45bn and non-traditional ETFs from $20bn to $150bn since 2020.  #mech/structural_shift _(time-bound view)_
  > until 2020 the regulatory framework in the United States was very um opaque and it wasn't as clear
  indicator: ETF assets in systematic trend, non-traditional ETFs · asset: multi · direction: ETF assets up · horizon: years · testable: yes - Morningstar fund flow data · confidence: high
  ^MT180-C03-1

### C04
- **Katie Kaminski** Institutions use trend ETFs as a liquidity buffer next to their CTA allocations to adjust exposure without redemption paperwork.  #mech/liquidity_flows
  > they like the liquidity profile of an ETF they thought of it as a liquidity buffer something that they could use as sort of a buffer to their existing uh CTA exposures
  indicator: trend ETF usage · asset: multi · testable: no - anecdote · confidence: medium
  ^MT180-C04-1
- **Katie Kaminski** Of about $350bn in managed futures only about 5% is retail, so ETFs and model portfolios could broaden access to diversifying return streams.  #mech/structural_shift _(time-bound view)_
  > it's about three 350 through 45 billion only 5% of that allocation is actually in the retail space
  indicator: managed futures AUM by investor type · asset: multi · direction: retail share up · horizon: years · testable: yes - AUM data · confidence: medium
  ^MT180-C04-2
- **Katie Kaminski** Managed futures should be a strategic allocation rebalanced to target rather than timed; if adding at all, add during drawdowns since managed futures tend to recover on average.  #mech/risk_management
  > if you're going to rebalance it should be based on sort of things have done well and see equities have underperformed
  indicator: strategic allocation, drawdown recovery · asset: multi · direction: allocate in drawdowns · horizon: years · testable: partly - allocation timing study · confidence: medium
  ^MT180-C04-3
- **Niels Kaastrup-Larsen** Daily liquidity in ETFs may hurt investors in a crisis-alpha strategy that requires patience, because ease of exit encourages timing and abandonment, an argument for lock-up-like discipline.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > to give people even more how should I say liquidity in a strategy where maybe sometimes it would be be better for them not to be almost like private Equity
  indicator: ETF liquidity and investor behaviour · asset: multi · horizon: years · conditions: strategies where payoff is unpredictable and needs holding through drawdowns · testable: partly - flows versus returns for ETFs and funds · confidence: medium
  ^MT180-C04-X1

### C05
- **Katie Kaminski** US model portfolio assets grew from $286bn (2021) to $424bn (June 2023); holding managed futures via ETFs in model portfolios builds in strategic allocation and reduces line-item picking and timing of trend.  #mech/liquidity_flows _(time-bound view)_
  > roughly 286 billion in Assets in two 2021 were in model portfolios um in the United States in June 2023 it's 424
  indicator: US model portfolio AUM (Morningstar) · asset: multi · direction: model portfolio assets up · horizon: years · testable: yes - Morningstar data · confidence: high
  ^MT180-C05-1
- **Katie Kaminski** In the last three years, with higher rates and inflation, bond volatility is higher and the stock-bond correlation is positive, so 60/40 provides less diversification than in the prior 40 years.  #mech/structural_shift
  > look for the last three years in fact in a higher rate environment with some inflation Bond volatility is
  indicator: stock-bond correlation, bond volatility · asset: multi · direction: 60/40 diversification down · horizon: years · conditions: higher-rate, inflationary regime · testable: yes - rolling stock-bond correlation · confidence: high
  ^MT180-C05-2
- **Niels Kaastrup-Larsen** Recommended managed-futures allocation sizes vary widely: a Man paper suggested about 40% of a portfolio while the replication-ETF issuer targets model portfolios at only 3-5%, so ETF-based adoption assumes small weights.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > I think this was based on a man paper that they where they said 40% and he said well I'm only going for three or 5% whatever it was
  indicator: managed futures allocation size · asset: multi · conditions: model portfolio construction · testable: partly - optimisation studies · confidence: low
  ^MT180-C05-X1
- **Niels Kaastrup-Larsen** The roughly $350bn managed futures AUM figure has been flat for a very long time and about half of it is Bridgewater, so the industry has not penetrated institutional portfolios as much as the headline implies.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > about half of that number is Bridgewater which I don't really myself consider a CTA or manage Futures product
  indicator: managed futures AUM · asset: multi · horizon: years · testable: partly - AUM series differ by provider · confidence: medium
  ^MT180-C05-X2

### C06
- **Katie Kaminski** A return to zero interest rates, where buying stocks and bonds suffices, is unlikely, so alternatives are a natural choice, and ETF innovation can make them available to retail investors.  #mech/structural_shift
  > it's very unlikely I think that we're going to go back to this zerp world where interest rates are really low and then all you have to do is buy bonds and stocks
  indicator: interest rate regime · asset: multi · direction: alternatives allocation up · horizon: years · testable: no - regime view · confidence: medium
  ^MT180-C06-1
- **Katie Kaminski** ETF use cases: direct investment, model portfolios and institutional access as a liquid sleeve to adjust total managed futures exposure without redeeming from individual managers.  #mech/liquidity_flows
  > if you have an ETF you can use that as a liquidity buffer and if you have cash management issues or you want to come in or out of it you can just use that to get to your target
  indicator: trend ETF use cases · asset: multi · testable: no - product use · confidence: medium
  ^MT180-C06-2

### C07
- **Niels Kaastrup-Larsen** ETF buyers may do less manager due diligence and rely on the ticker's return stream, and managers will not know their investors, limiting education during drawdowns.  #mech/behavioral
  > maybe they just more focus on the return stream they see from the ticker then all the other stuff that we normally have to answer for uh when it comes to due diligence
  asset: multi · testable: no - speculation · confidence: low
  ^MT180-C07-1
- **Katie Kaminski** In mutual funds, product proliferation first, then consolidation: surviving managed futures mutual funds became about 95% correlated to institutional products, suggesting ETF markets will converge similarly.  #mech/crowding_positioning
  > the correlation of the funds that existed started to move much closer to the actual index of institutional funds
  indicator: correlation of mutual funds to institutional index · asset: multi · direction: convergence to index · horizon: years · testable: yes - correlation to benchmark by fund · confidence: medium
  ^MT180-C07-2

### C08
- **Katie Kaminski** The goal is to move investors from bad to okay: even a modest managed futures allocation via ETF improves diversification versus none; ETFs use fewer, liquid markets (copper, bonds, maybe no cocoa).  #mech/risk_management
  > if we actually think about the best interests of the investors a lot of it that's why we talk about education is is trying to get people to go from bad to
  indicator: managed futures ETF beta exposure · asset: multi · direction: portfolio diversification up · horizon: years · testable: partly - ETF vs no allocation simulation · confidence: medium
  ^MT180-C08-1
- **Katie Kaminski** Excluding Bridgewater the managed futures space is roughly 80% institutional (about 95% including it), so retail penetration is larger than the 5% headline but ETF-style product governance is still unfamiliar to the industry.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > given that we're 95% institutional um take out Bridgewater then you maybe you know 80% um institutional as a as a space
  indicator: institutional share of managed futures AUM · asset: multi · horizon: years · testable: partly - AUM data · confidence: medium
  ^MT180-C08-X1

### C09
- **Niels Kaastrup-Larsen** Managers entering the ETF space have three routes: replicate their full strategy in the wrapper, offer a watered-down version trading fewer, more liquid markets, or use a replication approach that infers exposure from historical manager data.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > they can try and recreate their full strategy with an within an ETF like Jerry has they can do and and I I say in quotation a water down uh version of the strategy
  indicator: ETF design routes · asset: multi · testable: no - taxonomy · confidence: medium
  ^MT180-C09-X1
- **Katie Kaminski** When ETFs hide the end investor, education must run through adviser networks because the manager cannot talk to the clients directly, while institutions will still do full due diligence.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > you're going to rely more on networks of advisers to educate their clients um as your conduits
  indicator: distribution through advisers · asset: multi · conditions: when investors access via ETF tickers · testable: no - qualitative · confidence: medium
  ^MT180-C09-X2

### C10
- **Katie Kaminski** Replication-based ETFs have lower manager-specific risk and look like industry beta but are backward-looking, slower, and inherit managers' risk management; direct implementation uses actual signals and risk rules but reflects one manager's parameters and can deviate from the index.  #mech/research_method
  > replication is backward-looking um it can be slower to react um and it's not necessarily directly implementing risk management
  indicator: index replication vs mechanical replication · asset: multi · horizon: months · testable: yes - compare replicators vs trend indices · confidence: high
  ^MT180-C10-1
- **Katie Kaminski** A hybrid between index replication and direct implementation is sensible: it keeps CTA insight in signals and risk management while tracking the industry beta that ETF buyers expect (as with an S&P 500 ETF).  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > so I think a combination of the to make sense right so you have some CTI insights but also if you want to follow the bait of the industry
  indicator: hybrid replication plus direct signals · asset: multi · testable: yes - compare tracking error and returns · confidence: medium
  ^MT180-C10-X1

### C11
- **Niels Kaastrup-Larsen** A replicator carries single-replicator model risk; the correlation to the target may be less than expected.  #mech/research_method
  > you could have a single replicator risk because of course there is no guarantee that the model that's being used to
  indicator: replication model risk · asset: multi · testable: yes - tracking error · confidence: medium
  ^MT180-C11-1
- **Katie Kaminski** ETF constraints (fewer markets, slow signals because of creation-redemption) give industry-like exposure but performance diverges from classic CTAs depending on whether trends are in big markets (gold, yen, equities) or idiosyncratic ones.  #mech/structural_shift _(time-bound view)_
  > you can't trade as many markets um and perhaps you know might not want to use really really fast signals because of you know the the sort of create Redemption process
  indicator: ETF market set vs classic CTA 100+ markets · asset: multi · direction: ETFs do well when trends in large markets · horizon: months · conditions: trends concentrated in large liquid markets · testable: yes - compare ETF vs index by market set · confidence: high
  ^MT180-C11-2
- **Katie Kaminski** A classic managed futures fund can trade 100+ markets with many model types (including machine learning), making it a best-ideas product, whereas an ETF is limited to fewer liquid markets and slower signals but still captures the main macro themes.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > when you think about a classic manag Futures product it's it's a best ideas product it's really sort of putting all these different ideas together
  indicator: classic CTA vs ETF market set · asset: multi · testable: partly - compare ETF vs fund returns · confidence: medium
  ^MT180-C11-X1

### C12
- **Katie Kaminski** Flat-fee ETFs still require research focused on extended markets and differentiated techniques that justify performance fees, because the mutual fund shift pushed managers toward scale versus return.  #mech/research_method
  > research needs to drive performance um and thus you need to be putting Research into areas where you can actually provide an edge
  indicator: research allocation, fee structure · asset: multi · horizon: years · testable: no - management principle · confidence: medium
  ^MT180-C12-1
- **Niels Kaastrup-Larsen** Without incentive fees a manager's revenue depends only on AUM, which pushes research toward scalable (liquid, slower) models and more markets rather than the highest possible return.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > when you have no incentive fee the only way you can do well is to grow that uh AUM as much as possible
  indicator: fee structure and incentives · asset: multi · horizon: years · conditions: flat-fee products · testable: no - incentive argument · confidence: medium
  ^MT180-C12-X1

### C13
- **Katie Kaminski** Managed futures replicator ETFs will probably converge to higher correlation with the index as in mutual funds, though the CTA index is time-varying, so noise is larger.  #mech/crowding_positioning
  > products that were more similar to the index that people liked and that have worked have been the persistent products
  indicator: product correlation to CTA index · asset: multi · horizon: years · testable: partly - need fund history · confidence: medium
  ^MT180-C13-1
- **Niels Kaastrup-Larsen** If replicator ETFs grow large enough to be included in the CTA indices they replicate, the benchmark becomes circular (replicators replicating themselves); Kaminski thinks this is a long way off.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check)_
  > just wonder what would happen if these products became so successful that they actually become The Benchmark so they replicating themselves
  indicator: CTA index replication · asset: multi · horizon: years · conditions: if replicator AUM becomes large relative to the industry · testable: no - speculative · confidence: low
  ^MT180-C13-X1
- **Katie Kaminski** Using AI to hunt for the best new signal (for example to trade cocoa) will not improve outcomes for the marginal investor; AI's value is helping investors access better portfolios and make better decisions.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > that is one area of application but that's not going to make the marginal investor that much better off
  indicator: AI in systematic investing · asset: multi · testable: no - opinion · confidence: medium
  ^MT180-C13-X2

### C14
- **Niels Kaastrup-Larsen** Classical trend following based on price history will survive AI because it follows human behaviour (over- and under-reaction) rather than predicting; the internet-era claim that equal data kills trend turned out wrong.  #mech/behavioral
  > a normal classical way of doing Trend following will will do well because it's based on human behavior
  indicator: trend following price-based signals · asset: multi · horizon: years · testable: no - opinion · confidence: medium
  **Correction (cross-check):** The over- and under-reaction mechanism was stated by Kaminski, not the host; the host's point was that classical trend following using old price-history techniques will keep working despite AI, as it did after the internet. → Kaastrup-Larsen expects classical trend following to do well despite AI because it is based on human behaviour and survived the internet-era claim that equal data kills it; the over/under-reaction mechanism was added by Kaminski.
  ^MT180-C14-1
- **Niels Kaastrup-Larsen** A simple trend model would have captured Nvidia's rise because any price move from 100 to 200 passes through intermediate levels, so prediction by AI is not needed.  #mech/slow_reaction _(time-bound view)_
  > for a market to go from 100 to 200 it still has to go to 105 110 and that's all the stuff that all we need to to know to pick up
  indicator: price path continuity · asset: equities · direction: long during sustained rise · horizon: months · conditions: asset must be in the portfolio · testable: partly - example only · confidence: medium
  **Correction (cross-check):** Wrong speaker: the Nvidia 100-to-200 example is Kaminski circling back to her own opening Nvidia remark after saying she has been fascinated with trend following 'my entire career'; the host made the classical-trend-following-survives-AI point. → Kaminski: even if an AI had predicted Nvidia's rise two years ago, a simple trend model would have captured it because a price moving from 100 to 200 must pass through 105 and 110, which is all the information trend followers need.
  ^MT180-C14-2
- **Katie Kaminski** AI adds new tools for managers' research processes but also raises barriers to entry because the research is expensive, favouring larger managers.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > it does add barriers to entry like you said as well it's not always cheap to do that type of research
  indicator: AI research cost · asset: multi · horizon: years · testable: no - opinion · confidence: medium
  ^MT180-C14-X1
- **Katie Kaminski** Trends exist because market participants remain human with overreaction, underreaction and repeating behaviour, so AI does not remove the source of trends.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > trading in financial markets we have overreaction underreaction and we have behavior um and this Behavior tends to repeat and change over time which provides Trends in markets
  asset: multi · testable: no - behavioural explanation · confidence: high
  ^MT180-C14-X2

### C15
- **Katie Kaminski** Trend following does not predict and follows whatever themes move, so AI as a predictive tool for the next word or price gives no advantage to a strategy built on not predicting.  #mech/slow_reaction
  > it's following the themes of what is moving and ask the why later and that strategy's worked for decades
  indicator: trend following vs prediction · asset: multi · horizon: years · testable: no - philosophical · confidence: medium
  **Correction (cross-check):** Two speakers are blended: Kaminski's statement is that trend following does not predict and follows whatever themes move, asking why later; the large-language-model point (LLMs aim at prediction, so prediction is a 'red card' to AI in trend following) is the host's. → Kaminski: trend following does not get hung up on predicting and follows the themes (Nvidia or cocoa), asking why later; the host adds that LLMs are built to predict, so a strategy built on not predicting gains nothing from them.
  ^MT180-C15-1

