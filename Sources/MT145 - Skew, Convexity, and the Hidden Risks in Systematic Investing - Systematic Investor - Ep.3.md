---
source_id: MT145
title: "Skew, Convexity, and the Hidden Risks in Systematic Investing - Systematic Investor - Ep.370"
date: 2025-10-24
channel: "Top Traders Unplugged"
url: 
words: 10276
claims: 91
added_by_crosscheck: 27
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Nicole Kajin (founder, Alpha Quest, short-term CTA)", "Alan Dunn (systematic investor co-host)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Skew, Convexity, and the Hidden Risks in Systematic Investing - Systematic Investor - Ep.370

**Speakers:** Nicole Kajin (founder, Alpha Quest, short-term CTA); Alan Dunn (systematic investor co-host); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Nicole Kajin (Alpha Quest) argues Fed/political support and a Buffett ratio above 200% pushed platforms and CTAs toward hidden negative-skew and levered positioning. She treats skew and convexity, not Sharpe, as the true risk metric. Her approach trades short-term breakouts in vol-compressed markets and plans to short crowded high-Sharpe single-stock factors.

**Approach:** short-term breakouts, skew/convexity, CTA analysis, multi-manager platforms, trend following

**Cross-check completeness estimate of first read:** 0.72 - first reader (64 claims) caught the main thesis chain (Fed put, pod leverage, skew/Sharpe, CTA style drift, signal design); 27 additions are mostly supporting mechanisms, numbers, Niels counterpoints and caveats, plus 2 corrections (speaker of C13-4, caption number in C03-4).

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | intro/sponsor; Nicole on history of intervention since 1987; CTA index October gains |
| C02 | 5 | Buffett ratio, stock market as risk-free asset, concentration, trend follower headwind, debasement |
| C03 | 5 | platform alpha = tail risk, correlation, mean reversion bubble, Sharpe thresholds |
| C04 | 5 | inflation certainty, Sharpe-chasing drives hedged books, leverage, LTCM analogy |
| C05 | 7 | liquidity, Covid, reflexivity, Fed put, why pods survived 2022-25 |
| C06 | 3 | endgame, commodities/S&P ratio, AI energy demand, nuclear |
| C07 | 5 | volatility vs risk, leverage, S&P skew, alpha vs negative skew |
| C08 | 3 | breakouts in vol compression, CTA horizon dispersion |
| C09 | 5 | CTA style drift, skew and Sharpe, government pinning of markets |
| C10 | 4 | CTA long-side returns, skew over cycles, rolling CTA skew, trend follower reply |
| C11 | 5 | time horizon of optimisation, Sharpe predicts flows, factor breakouts |
| C12 | 4 | short-term trend degradation, long-cycle allocation, daily options, S&P mean reversion |
| C13 | 5 | call overwriting, CTA ex fixed income, platforms as LTCM |
| C14 | 5 | trading against platform factor crowding, behavioral and research cautions |
| C15 | 1 | crowd psychology; outro and plugs |

## Claims

### C01
- **Niels Kaastrup-Larsen** SG CTA indices were all positive in October 2025, a data point on trend-following health.  #mech/slow_reaction _(time-bound view)_
  > all is well in trend following land with all the stock gen CTA indices posting gains so far in October
  indicator: SG CTA indices · asset: multi · direction: CTA/trend indices up · horizon: months · testable: partly - single-month datapoint · confidence: medium
  ^MT145-C01-1
- **Nicole Kajin** Since 1987 (then 2001-03 and the GFC) US political and Fed intervention in markets has grown after each crisis, changing how markets behave.  #mech/policy_reaction
  > it became clear for the political system the governance in governance in America that uh markets needed uh more support and uh more guidelines
  asset: equities · horizon: years · testable: no - narrative, no measure · confidence: medium
  ^MT145-C01-2

### C02
- **Nicole Kajin** With market cap/GDP (Buffett ratio) over 200% vs a 70% norm, the stock market drives the economy, so Fed and politicians act whenever it corrects (a Fed put).  #mech/policy_reaction
  > the stock market is about 70% of the size of GDP. Today we we're over 200%.
  indicator: Buffett ratio (market cap / GDP) · asset: equities · direction: equity drawdowns get supported by liquidity · horizon: years · testable: yes - ratio and Fed reaction to drawdowns can be measured · confidence: high
  ^MT145-C02-1
- **Nicole Kajin** Because policy supports every dip, investors treat equities as risk-free fixed income, so equity risk is under-priced and positioning is crowded.  #mech/crowding_positioning
  > the stock market has gone from being the risky asset with high returns to effectively becoming a new fixed income
  asset: equities · horizon: years · testable: partly - risk perception hard to measure · confidence: medium
  ^MT145-C02-2
- **Nicole Kajin** US weight (about 60% of global equities, with the top 7 tech stocks about 40% of US cap) shows extreme concentration of the market in one country and a few names.  #mech/structural_shift _(time-bound view)_
  > The US is about 60% of global stocks today.
  indicator: US share of global market cap; top-7 share of S&P · asset: equities · horizon: years · testable: yes - market-cap shares are observable · confidence: high
  ^MT145-C02-3
- **Nicole Kajin** Political suppression of volatility, inflation and drawdowns shortens and reverses trends, which has been a headwind for trend followers.  #mech/policy_reaction
  > In that context, trend followers have been the have had a headwind.
  asset: multi · direction: trend following weaker · horizon: years · conditions: when policy suppresses trends · testable: partly - needs a policy-suppression proxy · confidence: medium
  ^MT145-C02-4
- **Nicole Kajin** Looking only at 40 years of data suggests money can be printed without consequence, but longer history shows consequences, and a dollar debasement trade is emerging.  #mech/fiscal_debt _(time-bound view)_
  > you see you start to hear that there's a debasing trade going on
  asset: fx · direction: short USD / long hard assets (debasement) · horizon: years · testable: partly - trade is defined loosely · confidence: medium
  ^MT145-C02-5
- **Nicole Kajin** With the stock market above 200% of GDP, each 1% equity return adds about 2% of GDP in new liquidity (a wealth effect), so equity prices drive the economy and policy leans against every equity drawdown.  #mech/policy_reaction _(added by sonnet-xhigh cross-check)_
  > So 1% return in the stock market is giving you 2% of GDP in in new liquidity and that's very very very influential.
  indicator: Buffett ratio (equity market cap / GDP); equity return to GDP liquidity ratio · asset: equities · direction: equity falls trigger Fed/political easing; equity rallies add liquidity · conditions: market cap far above its ~70% of GDP norm · testable: partly - wealth-effect elasticity is estimable but the 2:1 figure is asserted, not shown · confidence: medium
  ^MT145-C02-X1
- **Nicole Kajin** A buy-and-hold narrative plus much higher retail ownership reinforces the view that equities carry no real risk, so corrections are ignored and dips are bought.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > Warren Buffett uh I would say is the main cheerleader for the stock market and if you're wise and you have a long-term perspective you can be rich by just holding the market
  indicator: retail equity ownership share · asset: equities · direction: dips bought, equity risk under-priced · horizon: years · conditions: rising retail participation and a popular buy-and-hold message · testable: partly - retail ownership and flow data exist, the narrative effect is hard to isolate · confidence: medium
  ^MT145-C02-X2

### C03
- **Nicole Kajin** The high Sharpe of large multi-manager platforms is explained by tail-risk (negative skew) exposure, not manager skill.  #mech/risk_premium
  > the surrogate factor that explains all these alphas is not skill but tail risk exposure
  asset: equities · horizon: years · testable: yes - test Sharpe against skew/tail exposure · confidence: high
  ^MT145-C03-1
- **Nicole Kajin** PM alphas look uncorrelated locally, but in stress they are highly correlated to each other and to the market because they share the same tail exposure.  #mech/crowding_positioning
  > they're actually all highly correlated to each other and to the market
  indicator: correlation of pod PM returns in stress · asset: equities · conditions: in market stress · testable: yes - measurable on return series · confidence: high
  ^MT145-C03-2
- **Nicole Kajin** The real bubble is confidence that everything mean reverts and converges (buy the dips, long-short equity), so markets are priced as if equilibrium is stable forever.  #mech/behavioral _(time-bound view)_
  > that mean reversion is the the real bubble that would say that there's a the confidence to buy the dips
  asset: equities · horizon: years · testable: no - narrative · confidence: medium
  ^MT145-C03-3
- **Alan Dunn** Allocators now demand Sharpe of 1 or more regardless of correlation, so a diversifying 0.7 Sharpe macro strategy is rejected, rewarding hidden tail risk.  #mech/behavioral
  > they say yeah that's not that interesting we we typically look for one sharp and above as a minimum
  indicator: Sharpe ratio threshold · asset: multi · testable: partly - anecdotal · confidence: medium
  **Correction (cross-check):** Number was silently changed: the caption reads 'a quad macro strategy with a 6.7 sharp', an obvious transcription error; the claim states 0.7 without flagging that it is an inference. → Allocators now look for a Sharpe of 1 or more as a minimum regardless of correlation profile, so a respectable macro strategy (caption '6.7', probably 0.7 or 0.67) is dismissed as uninteresting, which rewards hidden tail risk.
  ^MT145-C03-4
- **Niels Kaastrup-Larsen** Political involvement in central banking may not be unprecedented but part of a longer cycle that will clear at some point.  #mech/cycle_persistence
  > I wonder if it's just part of a bigger cycle
  asset: other · horizon: years · testable: no - opinion · confidence: low
  ^MT145-C03-5
- **Nicole Kajin** The S&P has returned about 16% a year over 16 years and 25% a year over the last 3, a run she reads as confidence in mean reversion and Fed support rather than normal returns, so extrapolating it overstates what to expect.  #mech/overshoot _(added by sonnet-xhigh cross-check, time-bound view)_
  > Uh so the S&P has analyzed 16% a year over 16 years and uh 25% over the last 3 years.
  indicator: S&P 500 annualised return (16 years, 3 years) · asset: equities · horizon: years · conditions: recent-window returns far above the ~7% long-run norm · testable: yes - rolling return statistic · confidence: high
  ^MT145-C03-X1
- **Nicole Kajin** Growth with heavy money creation and no visible CPI inflation is only possible through effective currency devaluation, a hidden tax on wealth, so the cost appears as debasement against hard assets rather than as consumer inflation.  #mech/fiscal_debt _(added by sonnet-xhigh cross-check, time-bound view)_
  > you cannot create this type of environment without uh an effective devaluation or effectively a mass massive tax on wealth uh which is what's going on
  indicator: USD versus hard assets / gold (debasement trade) · asset: fx · direction: dollar down versus real assets · horizon: years · conditions: persistent deficits financed by money creation · testable: partly - debasement can be measured versus gold and commodities, causality is argued · confidence: medium
  ^MT145-C03-X2

### C04
- **Nicole Kajin** Current debt levels with continued money printing mean an inflationary cycle is certain, as one of the cycle's normal phases.  #mech/fiscal_debt _(time-bound view)_
  > There's no way you can have this amount of debt and not end up uh and continuing to print money without uh without inflation as a stabilizer.
  asset: multi · direction: inflation up · horizon: years · testable: no - not falsifiable in short run · confidence: high
  ^MT145-C04-1
- **Nicole Kajin** Because investors reward high Sharpe, managers hedge out principal components of risk, producing less trending, more mean-reverting, less liquid books that need more leverage.  #mech/crowding_positioning
  > if you take the delta 1 markets and you hedge more and more principal components of risk, you will end up with things that have less trends but are more mean reverting in nature
  asset: multi · testable: partly · confidence: medium
  ^MT145-C04-2
- **Nicole Kajin** Delta-1 trend following has a Sharpe of about 0.3-0.4; hedged spread trading removes the trend component, which is the most macro one, to raise Sharpe.  #mech/research_method
  > if delta 1 markets on trend following gives you a sharp ratio of.3 or 04
  indicator: trend-following Sharpe · asset: multi · horizon: years · testable: yes - compare Sharpe and skew of outright vs spread books · confidence: medium
  ^MT145-C04-3
- **Nicole Kajin** Single-stock pods hedge 70-90% of book volatility and are levered 20-30x, the same pattern as LTCM in fixed income, with risk looking near zero.  #mech/crowding_positioning _(time-bound view)_
  > PMS that are required or are being encouraged to achieve high sharp ratios are designing strategies where they're hedging 70 80 90% of the volatility
  indicator: gross leverage of pod books · asset: equities · testable: partly - leverage data is private · confidence: high
  ^MT145-C04-4
- **Nicole Kajin** In highly levered hedged books, a small rise in volatility or correlation forces deleveraging and liquidity disappears quickly.  #mech/liquidity_flows
  > the slightest change in volatility, the slightest change in correlation will lead to very quick changes in liquidity
  indicator: volatility and correlation changes · asset: equities · horizon: days · testable: partly · confidence: high
  ^MT145-C04-5

### C05
- **Nicole Kajin** With banks no longer committed liquidity providers, equity liquidity is supplied by other PMs and withdraws simultaneously in stress.  #mech/liquidity_flows
  > The liquidity is provided by other PMs and the liquidity all comes in at once and all leaves at once.
  asset: equities · horizon: days · conditions: in stress · testable: partly · confidence: high
  ^MT145-C05-1
- **Nicole Kajin** In Covid (March 2020) multi-manager platforms that looked uncorrelated fell 20-35% intra-month, showing the sensitivity of leverage to a fast shock.  #mech/crowding_positioning _(time-bound view)_
  > you have a situation such as co and all of them are down 20 30 35% intra months although they're uncorrelated
  indicator: platform returns Mar 2020 · asset: equities · horizon: weeks · conditions: fast shocks · testable: partly - private return data · confidence: medium
  ^MT145-C05-2
- **Nicole Kajin** High Sharpe attracts capital which is added to the same positions, a reflexive loop that sustains convergence trades until it breaks.  #mech/crowding_positioning
  > creating a self reinforcing cycle in mean reversion or in convergence
  asset: equities · horizon: months · testable: partly · confidence: high
  ^MT145-C05-3
- **Nicole Kajin** With a Fed put the tail hedge is free, so convergence/short-vol trades earn steady profit for a long time while risk builds unseen.  #mech/policy_reaction
  > if the Fed is there to provide uh the safety net, the market put you don't have to pay for that hedge, then you're convergence trade is highly profitable for a long period of time
  asset: equities · horizon: years · conditions: while the Fed backstop holds · testable: partly · confidence: high
  ^MT145-C05-4
- **Nicole Kajin** The 2022, SVB, yen-carry and tariff drawdowns were gradual so pods coped; only the fast Covid shock broke them, so speed of drawdown matters.  #mech/liquidity_flows
  > Those were more organized like and gentle corrections that happened over time co happened almost too quickly for these firms to adapt.
  asset: equities · horizon: weeks · testable: partly · confidence: medium
  ^MT145-C05-5
- **Nicole Kajin** In 2022 pods were hedged by their momentum sleeves, so they needed less liquidity than in 2020.  #mech/risk_management _(time-bound view)_
  > remember in 2022 all these partops also have trend following momentum components and momentum did very well in 2022
  asset: equities · horizon: months · testable: partly · confidence: medium
  ^MT145-C05-6
- **Nicole Kajin** Absence of a crisis lets leverage, platform allocations and investor confidence grow, so latent vulnerability rises over time.  #mech/cycle_persistence _(time-bound view)_
  > the fact that there's been no crisis means the risk is steadily increasing
  asset: equities · horizon: years · testable: no - not testable until a crisis · confidence: medium
  ^MT145-C05-7
- **Nicole Kajin** With the Fed put and equities seen as risk-free, speculation (long bitcoin, buying hedge funds, shorting options) pays more than productive work, so capital flows into financial risk-taking and money seems to come from nowhere, feeding the leverage cycle.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check, time-bound view)_
  > you can make more money playing the markets than trying to be productive in the economy
  asset: multi · direction: capital into speculative and short-vol strategies · horizon: years · conditions: persistent policy backstop and no crisis · testable: no - broad narrative with no stated metric · confidence: medium
  ^MT145-C05-X1
- **Alan Dunn** The economy has shifted from demand-constrained to supply-constrained with fiscal dominance, so a debasement trade now exists that did not a few years ago.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > Now it's more supply constrained and you know fiscal dominance you mentioned the debasement trade
  indicator: supply-constrained versus demand-constrained regime; fiscal dominance · asset: multi · horizon: years · conditions: post-pandemic regime · testable: partly - regime can be proxied with inflation and output-gap data · confidence: medium
  ^MT145-C05-X2

### C06
- **Nicole Kajin** The GSCI/S&P ratio is at a record low, suggesting reversion in favour of commodities against equities.  #mech/overshoot _(time-bound view)_
  > the Goldman Sachs commodity index relative to the S&P it's at the lowest level it's ever been
  indicator: GSCI / S&P 500 ratio · asset: commodities · direction: long commodities vs equities · horizon: years · testable: yes - ratio is measurable · confidence: medium
  ^MT145-C06-1
- **Nicole Kajin** AI buildout needs real energy that cannot be printed, so energy, nuclear and uranium assets (and gold, which nearly doubled) will see price inflation.  #mech/structural_shift _(time-bound view)_
  > the AI demand for energy will trig will trigger a massive inflation in certain limited assets
  indicator: energy and uranium prices; nuclear stocks · asset: commodities · direction: long energy / nuclear / uranium · horizon: years · testable: partly - thesis, early evidence · confidence: medium
  ^MT145-C06-2
- **Nicole Kajin** AI valuations depend on new energy supply (small nuclear); if it falls short, AI stocks must fall 70-80%.  #mech/risk_premium _(time-bound view)_
  > If these small nuclear reactors are not what we expect, then AI has to basically collapse 70 80%.
  asset: equities · direction: AI equities down · horizon: years · conditions: if energy supply disappoints · testable: no - scenario · confidence: low
  ^MT145-C06-3
- **Alan Dunn** Because financialisation means a 20% equity fall hits GDP, the Fed must ease into it, and with fiscal dominance already present this points to inflation as the endgame rather than a clean deflationary bust.  #mech/policy_reaction _(added by sonnet-xhigh cross-check)_
  > if the stock market falls 20% now as you say it has a huge impact on GDP so the the Fed has to react to that at the same time you've got fiscal dominance
  indicator: equity drawdown to Fed response · asset: multi · direction: easing after equity drops; inflation risk up · conditions: high financialisation and fiscal dominance · testable: partly - Fed reaction function to equity drawdowns can be tested · confidence: medium
  ^MT145-C06-X1
- **Nicole Kajin** Historical analogy: late-cycle empires hand out paper claims in exchange for real assets and keep the commodities; the US cannot expand territorially to sell paper to new populations, so debasement shows up as paper losing value against physical commodities.  #mech/fiscal_debt _(added by sonnet-xhigh cross-check)_
  > the endgame is always to try to give people paper in exchange for physical things
  indicator: commodities versus equities / paper assets · asset: commodities · direction: long physical commodities versus paper · horizon: years · conditions: empire late cycle with no room for expansion · testable: no - historical analogy · confidence: medium
  ^MT145-C06-X2
- **Nicole Kajin** Once investors see returns in nuclear and energy, large flows follow because these assets are a diversified return source away from crowded equity themes, amplifying price moves in a limited set of assets.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check, time-bound view)_
  > once investors see that you can have returns by investing in nuclear energy or in certain energy sectors, you're going to have a massive flow because it's a diversified return source
  indicator: nuclear and uranium equities, energy sector flows · asset: commodities · direction: long energy, nuclear and uranium · horizon: months · conditions: AI energy demand narrative takes hold · testable: partly - flows and returns of energy/nuclear baskets are measurable · confidence: medium
  ^MT145-C06-X3
- **Nicole Kajin** Markets price AI (40-50% of the economy and about half of equity market cap in her words) as a projection; the real-world buildout and its energy and infrastructure cost are not fully taken into account.  #mech/overshoot _(added by sonnet-xhigh cross-check, time-bound view)_
  > today today AI is more of an idea uh and of a projection
  indicator: AI share of market cap; energy supply for AI · asset: equities · direction: AI stocks exposed if buildout is constrained · horizon: years · conditions: projected earnings must become real earnings · testable: no - projection and valuation view · confidence: medium
  ^MT145-C06-X4

### C07
- **Nicole Kajin** Standard deviation misses risk: a stock rising 5% a day and one rising 1% a day both have zero volatility, so vol budgets are blind to some risk.  #mech/risk_management
  > Volatility today does not measure risk.
  indicator: standard deviation of returns · asset: multi · testable: yes · confidence: high
  ^MT145-C07-1
- **Nicole Kajin** PMs size leverage from standard deviation and long-short correlation, so low vol plus high correlation allows 30x leverage.  #mech/risk_management
  > low low volatility and high correlation between your longs and your shorts creates an opportunity to basically leverage
  indicator: realised vol and long-short correlation · asset: equities · direction: more leverage · testable: yes · confidence: high
  ^MT145-C07-2
- **Nicole Kajin** Rolling S&P option skew is most negative on record, meaning options price a faster liquidity drain and vol rise on a decline, a signal ignored by hedge funds.  #mech/risk_premium _(time-bound view)_
  > If you look at the skew, the rolling skew of the S&P today, it's the most negative ever.
  indicator: rolling skew of S&P options · asset: equities · direction: downside risk higher · testable: yes - skew is observable · confidence: high
  ^MT145-C07-3
- **Nicole Kajin** Reported alpha and high Sharpe are 80-90% correlated to negative skew, so negative skew mostly explains strong Sharpe ratios.  #mech/risk_premium
  > alpha and high sharp ratio are 80 90% correlated to negative skew
  indicator: skew of strategy returns · asset: multi · horizon: years · testable: yes - correlate Sharpe with skew across managers · confidence: high
  ^MT145-C07-4
- **Nicole Kajin** If everyone sells tail risk for Sharpe, one can arbitrage different volatility measures to hold long-vol exposure and still earn returns.  #mech/risk_premium
  > be able to be long volatility while actually generating returns
  asset: multi · direction: long convexity · testable: partly · confidence: medium
  ^MT145-C07-5
- **Nicole Kajin** A high equity-market-to-GDP ratio makes S&P option skew very negative, because a fall would hit the economy and liquidity, so the options market prices downside volatility rising faster than upside.  #mech/risk_premium _(added by sonnet-xhigh cross-check)_
  > when the stock market is large as a percentage of the economy, the skew of the S&P becomes very negative
  indicator: S&P rolling option skew versus Buffett ratio · asset: equities · direction: downside protection priced richly; skew more negative · conditions: equity market large relative to GDP · testable: yes - regress option skew on market cap to GDP · confidence: medium
  ^MT145-C07-X1
- **Nicole Kajin** Definition used throughout: skew is the gap between upside and downside volatility, and convexity is nonlinear risk in both directions (being long or short options-like payoffs), i.e. an asymmetry in how volatility rises; these describe risk that standard deviation misses.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > Convexity is effectively volatility is going to go up faster on the downside versus upside or upside versus it's an asymmetry in volatility.
  indicator: return skew and convexity of a strategy · asset: multi · testable: yes - skew and convexity can be computed on any return series · confidence: high
  ^MT145-C07-X2
- **Nicole Kajin** She sees the mispricing of skew and convexity, with risk measured only by standard deviation, as a larger opportunity than the pre-GFC mortgage mispricing.  #mech/risk_premium _(added by sonnet-xhigh cross-check, time-bound view)_
  > There's an incredible opportunity in the market today bigger than the market and mortgage crisis of uh the GFC.
  indicator: skew and convexity versus standard deviation · asset: multi · direction: long convexity / long insurance · horizon: years · conditions: tail risk widely sold for Sharpe while risk is delayed · testable: no - opinion on size of opportunity · confidence: medium
  ^MT145-C07-X3

### C08
- **Nicole Kajin** When standard-deviation volatility is low relative to other risk measures (ATR, price range), trade short-term breakouts in delta-1 markets, a way to buy insurance via momentum.  #mech/slow_reaction
  > when volatility is low relative to the other other measures of risk effectively trade short-term breakouts
  indicator: ATR vs standard deviation; vol behavior at highs and lows · asset: multi · direction: long breakouts · horizon: days · conditions: when vol measures disagree · testable: yes · confidence: high
  ^MT145-C08-1
- **Nicole Kajin** Trading momentum in vol-compressed markets produced alpha vs the S&P and the CTA index over 25 years while keeping positive convexity.  #mech/slow_reaction
  > trading momentum in all compressed uh regimes or in all compressed markets
  indicator: volatility compression · asset: multi · direction: long momentum in compressed markets · horizon: days · conditions: vol compression · testable: yes · confidence: high
  ^MT145-C08-2
- **Nicole Kajin** The short-term CTA index has lost money since inception while long-term (12-month momentum) strategies made money, so CTA returns differ sharply by horizon.  #mech/slow_reaction
  > It's been losing money effectively since it was uh created.
  indicator: short-term CTA index vs long-term trend indices · asset: multi · direction: long-term trend over short-term · horizon: years · testable: yes - index data · confidence: high
  ^MT145-C08-3
- **Nicole Kajin** A further vol-divergence signal: whether a market's volatility expands or compresses as it makes new highs and lows, differing across markets; such differences in risk measures show where to trade short-term breakouts.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > you can see that a market volatility increases when the market is making new highs and new lows versus another market the vault compresses when it's making new highs and new lows
  indicator: volatility behaviour at new highs and new lows · asset: multi · direction: breakouts where vol compresses relative to other risk measures · horizon: days · conditions: risk measures disagree · testable: yes - vol conditioned on breakout events · confidence: medium
  ^MT145-C08-X1
- **Nicole Kajin** If the Buffett ratio, volatility and the frequency of tail events revert to long-run means, the resulting shock and rebalancing would pay strongly to the long-convexity breakout strategy, which meanwhile earns alpha without a correction.  #mech/overshoot _(added by sonnet-xhigh cross-check, time-bound view)_
  > if markets were to go back to their long-term means in terms of uh buffet ratio, in terms of uh volatility
  indicator: Buffett ratio, volatility, tail versus everyday event frequency · asset: multi · direction: long-convexity breakout strategy gains in a reversion · horizon: years · conditions: mean reversion of valuation and volatility toward long-run norms · testable: partly - conditional payoff of the strategy in past valuation unwinds · confidence: medium
  ^MT145-C08-X2

### C09
- **Nicole Kajin** CTA assets sit in long-horizon, risk-parity-like funds with long bond/equity bias, so the industry gives less protection in equity corrections.  #mech/crowding_positioning
  > the majority of the assets in the CTA industry are allocated to very very long-term CTAs with biases that reduce their ability to make returns during equity corrections.
  asset: multi · horizon: years · testable: yes - replicate with long-bias benchmarks · confidence: high
  ^MT145-C09-1
- **Nicole Kajin** CTAs that did well in the last 15 years added long equity or vol-selling to momentum, i.e. rewarded style drift, which hurts the diversifier role.  #mech/behavioral
  > supplemented their momentum strategies with long equity positions
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT145-C09-2
- **Nicole Kajin** In the last 15 years a more positively skewed (long convexity) strategy had a lower Sharpe, so skew is the main differentiator of CTA Sharpe and portfolio fit.  #mech/risk_premium
  > more positively skewed the strategy is the lower the sharp ratio in the last 15 years
  indicator: skew of CTA returns · asset: multi · horizon: years · conditions: last 15 years · testable: yes · confidence: high
  ^MT145-C09-3
- **Nicole Kajin** Long-vol and short-horizon (long-convexity) exposure has performed poorly since the GFC, which drove capital away from them.  #mech/risk_premium
  > being long volatility has been a horrible strategy in the last 15 years
  indicator: long volatility returns · asset: multi · horizon: years · conditions: last 15 years · testable: yes · confidence: high
  ^MT145-C09-4
- **Nicole Kajin** Governments successively suppressed volatility in commodities, then FX, then fixed income, with inflation now limiting rates and stocks the last pinned asset, which pushed CTAs to drift.  #mech/policy_reaction
  > first commodities got pinned, second FX got pinned in the 80s, fixed income got pinned in the '9s and early 2000s
  asset: multi · horizon: years · testable: no - historical narrative · confidence: medium
  ^MT145-C09-5

### C10
- **Nicole Kajin** 80-90% of CTA returns come from the long side; shorts rarely pay, so CTAs have become long-only-like and can be replicated.  #mech/structural_shift
  > from long the long side effectively the short the short side uh doesn't make money very often
  indicator: long/short split of CTA returns · asset: multi · horizon: years · testable: yes - decompose returns · confidence: medium
  ^MT145-C10-1
- **Nicole Kajin** Negative skew predicts returns only in the short recent cycle, not over the full cycle, a research trap.  #mech/research_method
  > In the full cycle, a skew is not a predictor of returns in the full cycle. In the short-term cycle, it seems that negative skew is a predictor of returns.
  indicator: skew · asset: multi · horizon: years · conditions: regime dependent · testable: yes · confidence: high
  ^MT145-C10-2
- **Nicole Kajin** CTAs moved from long to short tails, so the rolling skew of the CTA index is flat and it no longer diversifies portfolios.  #mech/structural_shift
  > if you look at the rolling skew of the CTA index, it's actually flat.
  indicator: rolling skew of CTA index · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT145-C10-3
- **Niels Kaastrup-Larsen** Modern trend followers choose horizons by data rather than committee, so a drift to longer horizons reflects what data supports.  #mech/research_method
  > We want to use the data to tell us where to select the parameters
  indicator: trend lookback selection · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT145-C10-4
- **Nicole Kajin** CTA return dispersion is explained by style-drift dimensions: long versus short side, time frame, asset-class mix, long versus short volatility, and mixing mean reversion with momentum; these can be replicated to see which CTAs drifted.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > long versus short long-term time frame the asset class style drift u and then the long volatility versus short volat voltility style drift
  indicator: CTA style-drift factors (side, horizon, asset mix, vol exposure, mean-reversion mix) · asset: multi · horizon: years · testable: yes - factor decomposition of CTA returns · confidence: high
  ^MT145-C10-X1
- **Nicole Kajin** Greater data, alternative markets and optimisation power have been used to justify moving CTAs into negatively skewed strategies in the name of diversification, which explains why CTAs went from long tails to short tails.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > all the new data sources, the alternative markets, um the ability to optimize way more than ever before have all been a justifications for CTAs to drift into negatively skewed strategies in the name of diversification
  indicator: CTA index rolling skew · asset: multi · horizon: years · conditions: optimisation on a recent sample with negative skew paying · testable: partly - CTA skew history is measurable · confidence: medium
  ^MT145-C10-X2
- **Niels Kaastrup-Larsen** Index-level critiques (flat skew, style drift) blend diversified CTAs with a small group of pure trend followers, so the analysis should separate the two groups.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > there is a small minority now which I would call kind of pure trend followers who are kind of living uh the way uh we did back in the 70s and the 80s and in the '90s
  indicator: pure trend followers versus diversified CTAs · asset: multi · testable: yes - split an index into pure trend and diversified managers · confidence: high
  ^MT145-C10-X3
- **Niels Kaastrup-Larsen** Niels argues a trend follower has no reason to trade short-term because the short-term CTA index has not made money in 15-20 years, and he would shift horizon only if data showed shorter horizons paying; he does not see Nicole's approach as short-term trend following.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > profitable as you rightly pointed out the short-term traders index has not made money for 15 20 years or however long it's been around
  indicator: short-term traders index · asset: multi · direction: avoid short-term trend following · horizon: years · conditions: unless shorter horizons start to pay in the data · testable: yes - index return history · confidence: medium
  ^MT145-C10-X4

### C11
- **Nicole Kajin** The CTA index earned only the risk-free rate from September 2003 until 2022, so the 15-year view reflects a long weak period too.  #mech/cycle_persistence
  > had not made money since September 2003 other than the risk-free rate
  indicator: CTA index returns 2003-2022 · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT145-C11-1
- **Nicole Kajin** Optimising on the last 15 years (market up 16% a year vs 7% normal) is a short-term optimisation; long-cycle factor exposure is the alternative.  #mech/research_method
  > should you optimize based on the factors are working now or should you optimize on the 100year cycle or the 50ear cycle
  asset: multi · horizon: years · testable: yes - compare sample windows · confidence: high
  ^MT145-C11-2
- **Nicole Kajin** Sharpe ratio predicts asset flows and regime shifts because investors chase recent Sharpe, so factors and PMs that did well get reallocated to.  #mech/crowding_positioning
  > we use sharp ratio as a pred predictor of asset flows
  indicator: trailing Sharpe · asset: multi · horizon: months · testable: yes - flows vs trailing Sharpe · confidence: medium
  ^MT145-C11-3
- **Niels Kaastrup-Larsen** Pure price-based trend followers will adapt to a regime change as data shifts without needing to predict it.  #mech/slow_reaction
  > we will pick up a change in market regime at some point if we are data driven
  asset: multi · testable: partly · confidence: medium
  ^MT145-C11-4
- **Nicole Kajin** Buy the breakout in a factor (e.g. value) when a long-underperforming factor begins to do well, as an adaptive way to catch turns.  #mech/slow_reaction
  > if value hasn't done well and value starts to do well again we're going to buy the breakout in value
  indicator: factor breakouts · asset: equities · direction: long factor on breakout · horizon: months · testable: yes · confidence: medium
  ^MT145-C11-5
- **Niels Kaastrup-Larsen** Niels suggests the flat or negative skew of the trend-following index may be an artefact of 20 years of rising equities, so skew should be measured over a much longer horizon.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > maybe you say okay trend following skew has to be measured against a much longer term horizon today than otherwise
  indicator: trend-following index skew over long samples · asset: multi · horizon: years · conditions: equity bull market in the sample · testable: yes - compute skew over longer or regime-split samples · confidence: low
  ^MT145-C11-X1

### C12
- **Alan Dunn** CTAs argue fast breakouts worked in the 70s-80s but degraded after costs as markets became more efficient and respond faster to news.  #mech/slow_reaction
  > markets have become more efficient back in the 80s you know people didn't respond as quickly to the news
  indicator: short-term breakout returns net of cost · asset: multi · horizon: years · conditions: after costs · testable: yes · confidence: medium
  ^MT145-C12-1
- **Nicole Kajin** The firm kept equal risk allocation across sectors (long-cycle factor exposure) rather than dropping sectors that did poorly in recent years, avoiding recency optimisation.  #mech/risk_management
  > we're still trading commodities, we're still trading FX, we're still trading fixed income and equities all the same way with the same risk allocation
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT145-C12-2
- **Nicole Kajin** Selling daily options gives very high Sharpe in this regime (Jane Street India case), a short-term distortion that creates short-term volatility and mean reversion.  #mech/risk_premium _(time-bound view)_
  > daily options has created the opportunity for people who are not convexity conscious to make a lot of money
  indicator: daily options · asset: equities · direction: short daily options earns carry · horizon: days · conditions: until a vol shock · testable: partly · confidence: medium
  ^MT145-C12-3
- **Nicole Kajin** In the very short term the S&P mean reverts: fading large daily moves works, unlike in other markets.  #mech/overshoot _(time-bound view)_
  > if you trade the inverse of a volatility breakout, if the market is up a lot, sell it.
  indicator: S&P daily returns · asset: equities · direction: sell large up days, buy large down days · horizon: days · conditions: short-term · testable: yes · confidence: medium
  ^MT145-C12-4
- **Nicole Kajin** The Indian case as alleged: retail buys leveraged daily options after daily moves, and the market maker allegedly induced cash-market moves to trigger them and sold the options into it, illustrating retail option demand as a source of short-term distortion.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check, time-bound view)_
  > Jane Street was selling daily options to the retail market that was buying whenever there were daily moves
  indicator: retail daily-option demand · asset: equities · direction: short daily options, mean reversion of daily moves · horizon: days · conditions: retail leveraged option demand after moves · testable: no - an accusation, not demonstrated here · confidence: low
  ^MT145-C12-X1

### C13
- **Nicole Kajin** Heavy covered call selling for yield pins the S&P and suppresses upside volatility.  #mech/crowding_positioning _(time-bound view)_
  > the S&P cannot go up as fast as it wants. It has like a massive price pinning mechanism
  indicator: call writing / call implied vol · asset: equities · direction: S&P upside capped · horizon: days · testable: partly · confidence: medium
  ^MT145-C13-1
- **Nicole Kajin** Because call implied vol is too low from call overwriting, buying calls is cheap insurance that mean reverts if the distortion unwinds.  #mech/crowding_positioning _(time-bound view)_
  > you can go long insurance and actually get paid because the call implied volatility at this point is too
  indicator: call implied volatility · asset: equities · direction: long S&P calls · horizon: months · testable: yes · confidence: medium
  ^MT145-C13-2
- **Nicole Kajin** Fixed income gave long-term CTAs positive skew; in a large inflation regime that contribution may vanish, so CTA convexity should be tested ex fixed income.  #mech/research_method
  > Um one very important thing to to understand the real vulnerability of long-term CTAs is to look at the returns without fixed income.
  indicator: CTA returns excluding fixed income · asset: rates · horizon: years · conditions: inflation regime · testable: yes · confidence: medium
  ^MT145-C13-3
- **Alan Dunn** Trend followers can profit in inflation regimes via short bond positions as in 2022.  #mech/slow_reaction
  > it can also be a nice contributor like in 2022 on the short side
  asset: rates · direction: short bonds in inflation · horizon: months · conditions: inflation regime · testable: yes · confidence: high
  **Correction (cross-check):** Speaker attribution looks wrong: the person who says 'as a trend follow I have to just raise my hand' is the self-described trend follower Niels (who earlier described 'pure trend followers' as 'we'), not Alan Dunn, who speaks about presenting strategies to investors and reports what CTAs say. → Niels Kaastrup-Larsen (probable speaker) notes that trend followers can also profit in an inflation regime from short bond positions, as in 2022.
  ^MT145-C13-4
- **Nicole Kajin** Multi-manager platforms resemble LTCM: they underwrite large tail risk with large leverage for short-term high Sharpe.  #mech/crowding_positioning _(time-bound view)_
  > I think of them as the LTC LTCMs of 2025.
  asset: equities · testable: no - analogy · confidence: high
  ^MT145-C13-5
- **Nicole Kajin** Two short-term systems with the same time frame and the same skew can have opposite results, so horizon and skew do not fully explain performance; she says the firm is researching what separates them.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > shortterm with the same time frame with the same skew one is losing a lot of money and one is making a lot of money
  asset: multi · horizon: days · testable: yes - pairwise comparison of similar systems · confidence: medium
  ^MT145-C13-X1
- **Nicole Kajin** Market regime shifts are harder to detect than assumed, and vulnerabilities from adaptations to a regime can take years to show up.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > The market regime shifts are harder to catch than uh we think the the adaptations uh the vulnerabilities are sometimes take years to show up.
  asset: multi · horizon: years · testable: no - qualitative caveat · confidence: medium
  ^MT145-C13-X2
- **Nicole Kajin** Long-term CTAs are long-biased, and she links long positions to a bottom-picking bias (dip buying), adding to their lack of protection in equity corrections.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check)_
  > these long-term CTS have long bias, right? That's and longs have bottom picking bias
  indicator: long versus short contribution of CTAs · asset: multi · horizon: years · testable: partly - split returns by side · confidence: low
  ^MT145-C13-X3
- **Niels Kaastrup-Larsen** Allocator money is flowing into multi-manager platforms rather than CTAs, the flow imbalance behind the platform crowding argument.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check, time-bound view)_
  > all the money flowing into these pot shops. Uh and they're certainly not flowing into to the CTA space at the same degree
  indicator: asset flows into multi-manager platforms versus CTAs · asset: multi · horizon: years · testable: partly - AUM flow data · confidence: medium
  ^MT145-C13-X4

### C14
- **Nicole Kajin** Short single-stock factors whose Sharpe is abnormally high once the turn begins, as platforms feed self-reinforcing vol compression in them.  #mech/crowding_positioning
  > What we will do is look for high sharp ratios on a time series perspective or cross-sectionally and try to short the high sharp ratios once the turnaround happens
  indicator: factor Sharpe (time series or cross-sectional) · asset: equities · direction: short crowded high-Sharpe factors · horizon: weeks · conditions: after turnaround · testable: yes · confidence: medium
  ^MT145-C14-1
- **Nicole Kajin** Platforms cut losing PMs and add to winners, so factors that performed well get reallocated to, creating distortions in single-stock factors.  #mech/liquidity_flows
  > the platforms have a very specific mandate and it's to cut off PMs that are losing money and to add to PMs that I have made money
  asset: equities · horizon: months · testable: partly · confidence: high
  ^MT145-C14-2
- **Nicole Kajin** Smaller capital ($2bn) can trade short horizons unavailable to large platforms, allowing trading against them.  #mech/crowding_positioning
  > we're relatively small at 2 billion. We can actually uh trade in a time frame which is not available to the large platforms
  asset: equities · horizon: days · conditions: capacity constraint · testable: no · confidence: medium
  ^MT145-C14-3
- **Nicole Kajin** Short memory and chasing recent rewarded behavior create market inefficiencies; avoiding them needs long-term data and self-awareness.  #mech/behavioral
  > Our brains are not designed to uh to have a long-term perspective.
  asset: multi · testable: no · confidence: medium
  ^MT145-C14-4
- **Nicole Kajin** Quant researchers should use long cycles in their data, not only the last 15 years that dominate the available data.  #mech/research_method
  > every quant researcher has the ability to uh look at the long-term cycles and take those into account
  asset: multi · horizon: years · testable: yes - test across longer samples · confidence: medium
  ^MT145-C14-5
- **Nicole Kajin** Shorting abnormally high-Sharpe single-stock factors is meant to earn in normal times as platform-driven distortions revert and to pay strongly if the regime shifts.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check)_
  > that's the opportunity to make money even when nothing is going on, but also to make a lot of money when in case the market regime shifts
  indicator: single-stock factor Sharpe (time series or cross-section) · asset: equities · direction: short crowded high-Sharpe factors after turn · horizon: weeks · conditions: after the turn begins; small size so short horizon is accessible · testable: yes - backtest factor-Sharpe reversal · confidence: medium
  ^MT145-C14-X1
- **Nicole Kajin** Career incentives push PMs to chase short-term gains to raise capital now, which produces less optimal decisions and the crowded positioning that creates inefficiencies.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > you're ambitious and you want to prove that you're the best PM ever and you want to raise money like right now, you're gonna make uh decisions uh which are less optimal uh for the sake of a short-term gain
  asset: multi · testable: no - incentive argument · confidence: medium
  ^MT145-C14-X2

### C15
- **Nicole Kajin** Being with the crowd feels safe but is dangerous; investors must neutralise this bias.  #mech/behavioral
  > the crowd is a very safe place to be emotionally for humans
  asset: multi · testable: no · confidence: medium
  ^MT145-C15-1

