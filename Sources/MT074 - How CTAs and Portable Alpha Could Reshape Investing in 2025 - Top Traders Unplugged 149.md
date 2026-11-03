---
source_id: MT074
title: "How CTAs and Portable Alpha Could Reshape Investing in 2025 - Top Traders Unplugged 149"
date: 2025-04-19
channel: "Top Traders Unplugged"
url: 
words: 10990
claims: 57
added_by_opus: 0
corrections: 0
crosscheck: "pending"
speakers: ["Niels Kaastrup-Larsen (host, Top Traders Unplugged)", "Alan Dunne (co-host, allocator/researcher)", "Rasvan, captioned 'Raswan Reming' (director of investment solutions, Aspect Capital)"]
tags: [source, layer0]
---
# How CTAs and Portable Alpha Could Reshape Investing in 2025 - Top Traders Unplugged 149

**Speakers:** Niels Kaastrup-Larsen (host, Top Traders Unplugged); Alan Dunne (co-host, allocator/researcher); Rasvan, captioned 'Raswan Reming' (director of investment solutions, Aspect Capital)

**Summary:** Top Traders Unplugged 149 (April 2025): Aspect's investment solutions director discusses portable alpha with CTAs as the alpha source on equity beta (Aspect paper 'Finding the Right Match'), behavioral fit, total portfolio approach, the 2025 macro divergence for trend following, CTA replication, and tailored solutions. Main conclusion: CTAs paired with equity beta give cash-efficient, adaptive, tail-resilient exposure that sits better than equity market neutral on shared tail risk.

**Approach:** portable alpha, trend following, total portfolio approach, CTA replication, asset allocation, behavioral finance, macro regime

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | nothing actionable: intro, guest background |
| C02 | 0 | nothing actionable: career background and introduction of portable alpha topic |
| C03 | 5 | portable alpha definition, GFC failures, 2022 private markets liquidity squeeze |
| C04 | 5 | career risk, CTA as shock absorber, cash efficiency, sizing of PA structure |
| C05 | 5 | static equity beta, cyclical vs structural reasons, return stacking, tail behavior |
| C06 | 2 | CTA bucket problem, equity sleeve overlay, hedging strategies bleed |
| C07 | 5 | trend as long-term yet crisis relief, behavioral hold, ripples after equity corrections |
| C08 | 5 | hidden skew in packaging, trend allows owning equities, equity market neutral comparison |
| C09 | 5 | antifragile caveat, shared tail risk, macro shift to volatility |
| C10 | 7 | policy divergence, currency trends, fixed income decoupling, stagflation whiffs |
| C11 | 4 | outlook of divergence; total portfolio approach definition |
| C12 | 3 | TPA implementation hurdles, portable alpha as bridge, CTA bucket fit, replication intro |
| C13 | 5 | CTA replication critique and views |
| C14 | 2 | tailored solutions vs finished products, manager relationships |
| C15 | 3 | investor utility, limits of customization, building blocks |
| C16 | 1 | managed accounts, combos of strategies; outro |

## Claims

### C03
- **Rasvan (captioned Raswan Reming)** Portable alpha packages chosen beta exposures with an overlay of uncorrelated alpha, making the portfolio more efficient per dollar of capital.  #mech/risk_premium
  > The principle being that when you do that you get a more efficient portfolio. It works harder for you.
  indicator: portable alpha structure · asset: multi · direction: long beta plus alpha overlay · horizon: years · testable: partly - efficient frontier simulation · confidence: high
  ^MT074-C03-1
- **Rasvan (captioned Raswan Reming)** Original portable alpha products (GFC era) used extreme leverage and shared a common left tail, so simulation of uncorrelated streams looked good but live structures broke in a crisis.  #mech/risk_management
  > a lot of the original portable alpha implementations shared a a common left tail
  indicator: portable alpha tail dependence · asset: multi · horizon: years · conditions: extreme leverage and shared left tail · testable: partly - tail correlation observable · confidence: high
  ^MT074-C03-2
- **Rasvan (captioned Raswan Reming)** Insufficient cash buffers forced portable alpha structures to unwind at the worst time, so cash-efficiency and margin buffers determine survival.  #mech/risk_management
  > not enough cash buffers left to to finance the the the um ongoing structure. It meant that they had to be unwound at the worst time possible.
  indicator: cash buffer in leveraged overlay · asset: multi · direction: keep cash buffer · horizon: weeks · conditions: aggressive structures · testable: yes · confidence: high
  ^MT074-C03-3
- **Rasvan (captioned Raswan Reming)** After 2022, allocators heavy in private markets want their liquid portfolio to work harder.  #mech/liquidity_flows _(time-bound view)_
  > they want to make their liquid part of their portfolio work harder
  indicator: liquid portfolio efficiency · asset: multi · horizon: years · conditions: private-market-heavy portfolios · testable: no - motivation · confidence: high
  ^MT074-C03-4
- **Rasvan (captioned Raswan Reming)** In 2022 stocks and bonds fell while private market cash flows dried up, forcing endowments and liability-driven investors to meet liabilities from a diminished liquid portfolio.  #mech/liquidity_flows _(time-bound view)_
  > you now have to source those meet those liabilities from a diminished liquid as uh sort of portion of your portfolio
  indicator: liquid portfolio vs liabilities · asset: multi · horizon: years · conditions: private markets illiquid, capital calls · testable: partly · confidence: high
  ^MT074-C03-5

### C04
- **Rasvan (captioned Raswan Reming)** Allocators need diversification but face career risk from underweighting a strongly performing equity market, so they want to diversify equities while staying fully invested.  #mech/behavioral _(time-bound view)_
  > you couple that experience of needing to make your liquid portion work harder with the career risk of selling down your equity
  indicator: equity underweight career risk · asset: equities · horizon: years · conditions: strong equity bull market · testable: no - behavioral · confidence: high
  ^MT074-C04-1
- **Rasvan (captioned Raswan Reming)** Portable alpha lets investors add CTAs without changing strategic asset allocation.  #mech/risk_management
  > portable alpha is just a mechanism, another mechanism of allowing people to access these strategies without having to make big wholesale changes to their strategic allocations
  indicator: portable alpha overlay · asset: multi · horizon: years · testable: no - structural · confidence: high
  ^MT074-C04-2
- **Rasvan (captioned Raswan Reming)** CTAs are margin-traded and so leave most capital unencumbered, enabling cash-efficient overlays.  #mech/risk_management
  > by being margin traded, there's a lot of unencumbered cash floating around in your portfolio
  indicator: margin-to-equity of CTA · asset: multi · testable: yes · confidence: high
  ^MT074-C04-3
- **Rasvan (captioned Raswan Reming)** In stress, CTAs reduce risk and move to cash (volatility targeting), a self-healing property that helps overlay structures survive shocks.  #mech/risk_management
  > the worse market gets, the more volatile, the more stressed the markets get, the general tendency for CTAs is to to take cover or to or to or to become more and more cashri.
  indicator: CTA exposure in stress · asset: multi · direction: reduce risk as volatility rises · horizon: weeks · conditions: sharp gap moves can still hurt · testable: yes · confidence: high
  ^MT074-C04-4
- **Rasvan (captioned Raswan Reming)** Per 100 of capital, about 15-25 can fund a diversified CTA and 15-20 can fund 100 notional of equity exposure, leaving ample cash for variation margin.  #mech/risk_management
  > with 15 to $25 in a 100, you can get access to a decent uh well diversified CTA strategy. with another $ 15 to $20, you could replicate $100 notion of equity exposure
  indicator: capital split in equity+CTA overlay · asset: multi · conditions: conservative structure needed for 1-2 day drops · testable: yes - can be simulated · confidence: high
  ^MT074-C04-5

### C05
- **Rasvan (captioned Raswan Reming)** Mid-size allocators with static equity beta can host a CTA via portable alpha without portfolio disruption.  #mech/liquidity_flows _(time-bound view)_
  > suddenly you've got a home for a CTA without having to disrupt the portfolio
  indicator: equity beta overlay · asset: multi · horizon: years · conditions: mid-size allocators · testable: no · confidence: high
  ^MT074-C05-1
- **Alan Dunne** A strong S&P makes standalone CTAs look unattractive, so blending with equity beta (return stacking) makes them more acceptable.  #mech/behavioral _(time-bound view)_
  > the S&P's done, you know, 14 and a half% for the last 5 years and probably done that for the last 15 years
  indicator: S&P 500 trailing return · asset: equities · horizon: years · testable: partly · confidence: medium
  ^MT074-C05-2
- **Alan Dunne** Return stacking is now more widely understood and embraced by a broader investor base such as RIAs.  #mech/liquidity_flows _(time-bound view)_
  > The idea of using derivatives to have a portfolio that's more than 100% in in in the kind of simplest terms is been to my mind more widely understood and been embraced by a broader set of investors
  indicator: return stacking adoption · asset: multi · horizon: years · testable: no · confidence: medium
  ^MT074-C05-3
- **Rasvan (captioned Raswan Reming)** Viability of a portable alpha structure depends on the tail behavior of the alpha and beta together, not any alpha with any beta.  #mech/risk_management
  > it's the tail behavior that decides how viable the structure will be
  indicator: tail dependence of alpha and beta · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT074-C05-4
- **Rasvan (captioned Raswan Reming)** Portable alpha brings in new investors who had no slot for CTAs.  #mech/liquidity_flows _(time-bound view)_
  > there's a group of investors that traditionally just wouldn't have had allocations to CTAs
  indicator: CTA investor base · asset: multi · horizon: years · testable: no · confidence: medium
  ^MT074-C05-5

### C06
- **Rasvan (captioned Raswan Reming)** A CTA is both defensive and growth; its value is adaptability, though a pure growth or pure defensive asset would do better in those single roles.  #mech/risk_premium
  > The things that we add as a as a strategy is how adaptive we are. How you know that we are not fitted to being defensive or growth.
  asset: multi · testable: no · confidence: medium
  ^MT074-C06-1
- **Rasvan (captioned Raswan Reming)** Equity beta is the best base for a CTA overlay, and equity sleeves or a CIO completion portfolio set the overlay size as a tracking error choice.  #mech/risk_management _(time-bound view)_
  > there's a lot of interest from the equity sleeves. Think of it, you can decide how much overlay you put on top and then it becomes a tracking error question and a risk appetite question
  indicator: tracking error budget · asset: equities · horizon: years · testable: no · confidence: medium
  ^MT074-C06-2

### C07
- **Niels Kaastrup-Larsen** Pure hedging or tail-risk strategies bleed returns over time unless timed perfectly, so they suit only short-term mindsets.  #mech/risk_management
  > By default, hedging strategies are only successful if you have a short-term mindset because uh it you it's simply the returns bleed or or you lose money over time
  indicator: tail hedge carry cost · asset: multi · horizon: years · conditions: unless timed, as in COVID · testable: yes · confidence: high
  ^MT074-C07-1
- **Niels Kaastrup-Larsen** Trend following needs a long-term holding mindset yet adapts quickly enough to deliver relief in many crises, making it a good match for long-term equity investors.  #mech/slow_reaction
  > It has the ability to deliver uh some relief uh in terms of positive performance uh during time frames um where it's most needed
  indicator: trend following in equity drawdowns · asset: multi · horizon: months · conditions: not guaranteed · testable: yes · confidence: medium
  ^MT074-C07-2
- **Rasvan (captioned Raswan Reming)** The main difficulty of holding a CTA is behavioral: it is uncorrelated and zigzags at different times to the widely held equity market.  #mech/behavioral
  > the trend being like a medicine that requires time to work
  indicator: CTA drawdown timing · asset: multi · horizon: years · testable: no · confidence: high
  ^MT074-C07-3
- **Rasvan (captioned Raswan Reming)** Equities have positive months about two-thirds of the time while a CTA is closer to 50/50, and with loss aversion (3x) separate line items make the CTA harder to hold.  #mech/behavioral
  > Twothirds of the time it's an up month. Uh in a CTA you closer to 50/50.
  indicator: hit rate of months · asset: multi · horizon: months · testable: yes - monthly win rates · confidence: high
  ^MT074-C07-4
- **Rasvan (captioned Raswan Reming)** A big equity correction propagates to currencies, bonds and commodities; trend followers earn from those ripples rather than from equity shorts alone.  #mech/slow_reaction
  > It starts to, you know, cause ripples in currencies, in bonds, as central banks react, commodity markets react. It's those ripples that trend followers capture.
  indicator: cross-asset reaction to equity correction · asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT074-C07-5

### C08
- **Rasvan (captioned Raswan Reming)** Combined with equity beta, trend's frequent small losses are hidden behind the widely held equity asset class while positive skew remains, making it behaviorally easier to hold.  #mech/behavioral
  > positive skeess that you get with trend with more frequent but smaller negative months, they can get hidden in inverted commas behind this widely held asset class
  indicator: trend skew · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT074-C08-1
- **Rasvan (captioned Raswan Reming)** The alpha source should remain independent of equities; packaging with beta is a behavioral accommodation, not a logical construct.  #mech/behavioral
  > it's the packaging that really talks to behavioral need rather than a a a logical construct
  asset: multi · testable: no · confidence: high
  ^MT074-C08-2
- **Niels Kaastrup-Larsen** Trend following lets investors own equities.  #mech/risk_management
  > trend following is what allows you to own equities
  asset: equities · testable: partly · confidence: medium
  ^MT074-C08-3
- **Niels Kaastrup-Larsen** Making trend portfolios 50% single-stock equities weakens diversification since equities struggle most when diversification is needed; prefer classically diversified portfolios.  #mech/risk_management
  > it's going to be harder and harder to be that diversifier if you do that because we know equities is the part of the portfolio that's going to um struggle the most
  indicator: equity weight in trend portfolio · asset: equities · direction: avoid equity-heavy trend · testable: partly · confidence: medium
  ^MT074-C08-4
- **Rasvan (captioned Raswan Reming)** Equity market neutral is overwhelmingly the alpha used in portable alpha; managed futures is the novel alternative Aspect proposes.  #mech/crowding_positioning _(time-bound view)_
  > I think it's overwhelmingly equity market neutral strategies that are being utilized.
  indicator: portable alpha alpha source · asset: multi · horizon: years · testable: no · confidence: high
  ^MT074-C08-5

### C09
- **Rasvan (captioned Raswan Reming)** CTAs are only almost antifragile: a sharp gap against a long position gives no protection, so a cash buffer is needed.  #mech/risk_management
  > if it's a sharp drop and I'm long that market and it gaps against me, guess what? I'm not going to be providing protection.
  indicator: gap risk · asset: multi · horizon: days · conditions: sudden drop while long · testable: yes · confidence: high
  ^MT074-C09-1
- **Rasvan (captioned Raswan Reming)** Equity market neutral keeps shared equity tail risk, while a CTA overlay gives greater tracking error but a mechanical cross-asset response when equities shock.  #mech/risk_management
  > what they can't really sidestep is the shared tail risk that hits equity markets
  indicator: tail dependence with equities · asset: multi · direction: CTA over EMN for equity tail · horizon: weeks · testable: yes · confidence: high
  ^MT074-C09-2
- **Rasvan (captioned Raswan Reming)** In the GFC, pandemic crash and tech wreck, CTA gains came mainly from other asset classes reacting, with only a small contribution from stock indices.  #mech/slow_reaction
  > it's all the other asset classes that drove performance with a little bit of a contribution eventually from stock indices
  indicator: CTA attribution in equity crashes · asset: multi · horizon: weeks · testable: yes - attribution · confidence: high
  ^MT074-C09-3
- **Alan Dunne** The 2010s of secular stagnation and low macro volatility gave way to higher macro volatility, favoring CTAs.  #mech/structural_shift _(time-bound view)_
  > now we've gone into this decade and we've had, you know, much more volatility in GDP, much more volatility in inflation, uh, higher interest rates
  indicator: volatility of GDP and inflation · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT074-C09-4
- **Alan Dunne** Uncertainty indices at multi-year highs suggest more dislocations, a favorable backdrop for CTAs (uncertainty alpha), though returns were muted since 2022.  #mech/slow_reaction _(time-bound view)_
  > indices that actually quantitatively track uncertainty are at multi-year highs and, um, all of that would seem to be a favorable backdrop for for CTAs
  indicator: economic uncertainty indices · asset: multi · direction: long trend following · horizon: months · testable: yes · confidence: medium
  ^MT074-C09-5

### C10
- **Rasvan (captioned Raswan Reming)** In early 2025 German fiscal expansion, US policy shifts and DeepSeek changed the outlook for Europe, US tech and Asia, creating sources of big macro trends.  #mech/policy_reaction _(time-bound view)_
  > the sheer amount of potential policy changes and also potential policy mishaps on the US has actually really put a question mark on this US
  indicator: US exceptionalism · asset: equities · horizon: months · testable: no · confidence: medium
  ^MT074-C10-1
- **Rasvan (captioned Raswan Reming)** CTAs have no prior, fair-value view or geographic bias, so can follow whichever divergence emerges.  #mech/risk_management
  > we're not fitted. I have no prior. I have no sense of the fair value
  asset: multi · testable: partly · confidence: high
  ^MT074-C10-2
- **Rasvan (captioned Raswan Reming)** During the zero-rate QE era currencies gave little trend following return because coordinated policy suppressed risk appetite.  #mech/policy_reaction
  > currency markets currencies were pretty uninteresting asset class from a trend following point of view during this this this QE era
  indicator: FX trend returns in QE era · asset: fx · horizon: years · conditions: coordinated zero rates · testable: yes · confidence: high
  ^MT074-C10-3
- **Rasvan (captioned Raswan Reming)** When inflation built and monetary policies diverged across regions in 2021-22, currencies became the main driver of CTA returns for two to three years.  #mech/policy_reaction
  > the currency asset class was the one that picked up that divergence and drove returns and dispersion for the next two to three years
  indicator: currency trends from policy divergence · asset: fx · direction: long trend following in FX · horizon: years · conditions: policy divergence · testable: yes · confidence: high
  ^MT074-C10-4
- **Rasvan (captioned Raswan Reming)** In 2025 fixed income markets decoupled (Treasuries, Bunds, JGBs) and China shifted to risk-on, creating breeding grounds for sustained macro divergence.  #mech/policy_reaction _(time-bound view)_
  > I think right now we've seen a very big decoupling of fixed income markets between US treasuries buns bank of Japan is sort of still a little bit different
  indicator: bond market decoupling · asset: rates · horizon: months · testable: yes · confidence: medium
  ^MT074-C10-5
- **Rasvan (captioned Raswan Reming)** Uncertainty leads to short-term inactivity and choppiness, but clear divergence later creates trend opportunities.  #mech/slow_reaction _(time-bound view)_
  > once there is a little bit of clarity of this divergence, we should see opportunities open up
  asset: multi · horizon: months · conditions: after clarity emerges · testable: partly · confidence: medium
  ^MT074-C10-6
- **Rasvan (captioned Raswan Reming)** The March 2025 FOMC revised growth down with inflation still elevated, hinting at stagflation.  #mech/policy_reaction _(time-bound view)_
  > I definitely got some whiffs of stagflation from the Fed's sort of results last night
  indicator: FOMC dot plot · asset: multi · horizon: months · testable: no · confidence: low
  ^MT074-C10-7

### C11
- **Rasvan (captioned Raswan Reming)** Aspect expects divergence over the next 6-12 months, being optimistic medium-term while cautious on liquidity, risk management and sensible model choices in the short term.  #mech/slow_reaction _(time-bound view)_
  > And so what I would like to see happen over the next six month 12 months is divergence.
  asset: multi · direction: long trend following · horizon: months · testable: no · confidence: medium
  ^MT074-C11-1
- **Alan Dunne** Strategic allocation silos optimize within asset classes while ignoring portfolio-wide interactions.  #mech/risk_management
  > you're optimizing within a category without being cognizant of what everybody else in the portfolio is doing
  asset: multi · horizon: years · testable: partly · confidence: high
  ^MT074-C11-2
- **Alan Dunne** The total portfolio approach looks through to risk factors and allocates risk rather than buckets, used by larger endowments, SWFs and pensions.  #mech/risk_management
  > taking the portfolio and looking through to the underlying risk factors uh and then optimizing and deciding how to allocate risk based on that
  indicator: risk factor allocation · asset: multi · horizon: years · testable: partly · confidence: high
  ^MT074-C11-3
- **Rasvan (captioned Raswan Reming)** Organizations using the total portfolio approach find CTAs more useful because CTAs are best judged at portfolio level.  #mech/risk_management
  > Organizations that have adopted this approach tend to find greater utility and a greater applicability of of CTAs
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT074-C11-4

### C12
- **Rasvan (captioned Raswan Reming)** Organizations unable to adopt TPA use portable alpha within existing sleeves to move toward the same result without restructuring.  #mech/structural_shift
  > but are still siloed in the asset classes are trying to make those individual asset classes become sort of work harder
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT074-C12-1
- **Rasvan (captioned Raswan Reming)** A CTA does not fit a single asset-class bucket (hedge fund team wants low beta, equity team wants equities), hence the bucket problem.  #mech/structural_shift
  > the hedge fund team says to you, you've got too much variable beta.
  asset: multi · testable: no · confidence: high
  ^MT074-C12-2
- **Rasvan (captioned Raswan Reming)** Consultants estimate TPA outperforms strategic asset allocation by 1.5-2% per year.  #mech/risk_premium
  > it's at least one and a half to 2% perom you could outperform by having a a total portfolio approach versus an SAA approach
  indicator: TPA vs SAA outperformance · asset: multi · horizon: years · testable: partly - unverified claim · confidence: low
  ^MT074-C12-3

### C13
- **Niels Kaastrup-Larsen** CTA replication products do not replicate closely, and their correlation to CTA indices breaks down at critical times.  #mech/risk_management
  > doesn't it doesn't replicate that closely um and correlation to the indices tend to break down at critical times
  indicator: replication vs CTA index correlation · asset: multi · horizon: weeks · conditions: at critical times · testable: yes · confidence: medium
  ^MT074-C13-1
- **Rasvan (captioned Raswan Reming)** Replication products trade few markets and take manager risk, so they may not capture trend following properties.  #mech/risk_management
  > they're quite narrow very few markets you're taking a manager risk
  asset: multi · testable: yes · confidence: medium
  ^MT074-C13-2
- **Rasvan (captioned Raswan Reming)** A blow-up in a replicated strategy could harm the whole CTA industry's reputation.  #mech/risk_management
  > as long as we don't have a spectacular unwind or or or big riskmanagement mishap from one of these replicated strategies that will taint the space
  asset: multi · testable: no · confidence: medium
  ^MT074-C13-3
- **Rasvan (captioned Raswan Reming)** ETF-based model portfolios with managed futures slices broaden CTA awareness and adoption.  #mech/liquidity_flows _(time-bound view)_
  > model portfolios have the ability to create investable ETFbased portfolios that have a slice allocate to manage futures
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT074-C13-4
- **Niels Kaastrup-Larsen** Industry labels all futures-trading products as CTA, so definitional standards may be needed.  #mech/research_method
  > shouldn't there be some quote unquote, you know, rules about what a product should contain in order to be called a CTA product
  asset: multi · testable: no · confidence: low
  ^MT074-C13-5

### C14
- **Alan Dunne** Allocators benefit from deep relationships with a few managers: they understand drawdowns better and can net fees across products.  #mech/behavioral
  > there is a merit in really understanding the manager's approach so that when they have their their draw down you understand that
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT074-C14-1
- **Alan Dunne** Best-in-class selection per bucket argues for individual manager selection instead of one provider.  #mech/research_method
  > you might want to say well we want to have bestin-class in every bucket and that's where it might make sense to do it individually
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT074-C14-2

### C15
- **Alan Dunne** Investors value consistency and avoiding sharp drawdowns over maximum compound growth, as seen in multistrat growth.  #mech/behavioral _(time-bound view)_
  > it seems that investors value that given the growth of the multistrats which are all based on delivering consistent returns
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT074-C15-1
- **Rasvan (captioned Raswan Reming)** Allocators with an existing portfolio want sleeves of a CTA program (commodities only, non-trend only) to complete the portfolio.  #mech/risk_management
  > Maybe they want to just do the commodities part of it. That's what's missing. Or maybe they just want to do the non-trend part of it.
  indicator: CTA program components · asset: multi · horizon: years · testable: no · confidence: medium
  ^MT074-C15-2
- **Rasvan (captioned Raswan Reming)** Customization should keep the strategy pure: do not speed up the portfolio or overweight carry on request.  #mech/research_method
  > You want to preserve the integrity of the investment thesis.
  asset: multi · testable: no · confidence: high
  ^MT074-C15-3

### C16
- **Rasvan (captioned Raswan Reming)** Allocators increasingly combine several strategies in their own proportions rather than tuning each strategy.  #mech/liquidity_flows _(time-bound view)_
  > a greater um sort of growth area has been in allocators combining a number of our strategies
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT074-C16-1

