---
source_id: MT038
title: "Crisis Alpha Is Not What Most Investors Think - Systematic Investor - Ep.400"
date: 2026-05-18
channel: "Top Traders Unplugged"
url: 
words: 11932
claims: 81
added_by_crosscheck: 4
corrections: 2
crosscheck: "opus cross-check"
speakers: ["Rob (guest; captioned 'Rob Carver', portfolio manager, Fidelity Investments quantitative research)", "Yuval (co-host, Cambridge-based; trades commodities and JGBs)", "Niels Kaastro Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Crisis Alpha Is Not What Most Investors Think - Systematic Investor - Ep.400

**Speakers:** Rob (guest; captioned 'Rob Carver', portfolio manager, Fidelity Investments quantitative research); Yuval (co-host, Cambridge-based; trades commodities and JGBs); Niels Kaastro Larsen (host, Top Traders Unplugged)

**Summary:** Niels Kaastro Larsen, co-host Yuval and Fidelity's Rob discuss out-of-sample testing, May 2026 trend-following results, AQR's Betting Against Beta, and Rob's paper on where trend-following crisis alpha comes from. Main findings: most crisis alpha comes from beta timing (about 75% of trend risk); the relative-value tilt can be replaced by carry-over-vol if it stays volatility-neutral without losing defensiveness. The last topic is multi-asset execution: reduce risk early, watch correlations that spike and turn stale in crises.

**Approach:** trend following, crisis alpha, betting against beta, carry, execution, research methodology

**Cross-check completeness estimate of first read:** 0.94 - first reader was very thorough on testing, BAB, the crisis-alpha paper and execution; missed only a few market-context remarks and one critique of the leverage explanation; two speaker attributions wrong.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro; guests' backgrounds; no actionable content |
| C02 | 3 | off-topic (maths); out-of-sample testing problem and full-sample inference idea |
| C03 | 7 | inference from commodity spreads, physicality, forward-looking tests; Powell exit; JGB yields |
| C04 | 4 | global yields and fiscal issues; bonds vs equities after ceasefire; momentum at highs; May trend update |
| C05 | 5 | trend barometer breadth, May 2026 index returns, gold vs dollar and India, trend in rates; BAB paper introduced |
| C06 | 6 | BAB definition, evidence across asset classes, 13 years out-of-sample, quality explanation |
| C07 | 6 | BAB construction ($2 vs $1), leverage-constraint explanation and its critiques |
| C08 | 4 | private equity/Buffett idiosyncratic risk, leverage aversion, equity drift, pre-1945 sample |
| C09 | 4 | BAB formula; speculative 'betting against trend beta'; origin of Fidelity paper |
| C10 | 6 | paper method: decompose trend into beta timing and tilt; findings; carry replacement |
| C11 | 5 | market-neutral tilt condition; Yuval on 75% beta timing, correlation with equity, straddle analogy |
| C12 | 5 | relative value trend still useful; leverage and costs; carry's crisis risk |
| C13 | 4 | carry in EM FX; regime-adaptive essence of trend; portable alpha rationale |
| C14 | 5 | execution: passive vs risk, benchmarks, CTAs' passive-first approach versus front-loading |
| C15 | 4 | multi-asset execution: correlation, trading hours; Rob on conviction |
| C16 | 6 | closed markets, OTC execution, correlation spikes in crisis, discretionary macro practice |
| C17 | 3 | stale correlations, transaction costs, intraday correlation as risk-off signal; outro |
| C18 | 0 | legal disclaimer; nothing actionable |

## Claims

### C01
- **Rob** Rob found empirically, against his efficient-markets training, that buying assets that have been rising works, i.e. time-series momentum is visible in raw data before any theory.  #mech/slow_reaction _(added by opus cross-check)_
  > Look at this. Buying things that go have been going up seems to work.
  indicator: past returns (time-series momentum) · asset: multi · direction: long rising, short falling assets · horizon: months · testable: yes - time-series momentum backtest · confidence: medium
  ^MT038-C01-X1

### C02
- **Rob** Because researchers have run so many backtests, a pure out-of-sample test is impossible, so full-sample information should be used carefully, without polluting the strategy.  #mech/research_method
  > we've also run many many back tests in our in our in our lifetime. And as a result, it's very hard to run a true out of sample test.
  asset: multi · testable: partly - conceptual · confidence: high
  ^MT038-C02-1
- **Rob** Extreme full-sample regularities (like a coin showing 20 heads) can support inference about a market structure even without a clean out-of-sample period.  #mech/research_method
  > if I flip a coin 20 times and it comes up heads every time, can I infer that there's something about that coin
  asset: multi · conditions: Needs a prior reason such as physical mechanism · testable: partly · confidence: medium
  ^MT038-C02-2
- **Rob** A calendar spread (e.g. natural gas November vs March contract) with a 100% hit rate over 20-30 years may reveal a structural pattern.  #mech/risk_premium
  > some commodity spread, for example, is has been up uh has a hit rate of 100% over the last 20 or 30 years
  indicator: natural gas November vs March calendar spread · asset: commodities · horizon: years · testable: yes - historical spread · confidence: medium
  ^MT038-C02-3

### C03
- **Rob** Natural gas carries a stock-out risk premium in winter, so a persistent spread pattern has a fundamental reason; the information might be used for risk management rather than alpha.  #mech/risk_premium
  > natural gas is a natural example because we know that there's a stock out risk premium there.
  indicator: natural gas spread / stock-out risk · asset: commodities · horizon: months · conditions: Winter · testable: partly · confidence: medium
  ^MT038-C03-1
- **Yuval** When a market has a physical or institutional structure (storage, government auctions such as California carbon), full-sample information can legitimately inform strategy design.  #mech/research_method
  > in the situation where there is a physicality to the market, it is fair enough to use that information
  asset: commodities · conditions: Physical or structurally constrained markets · testable: partly · confidence: medium
  ^MT038-C03-2
- **Yuval** One way to detect a too-good result is a forward-looking test: if the effect is real, using future information should earn more money.  #mech/research_method
  > You actually use the system to say look forward and say if if the effect is there, should I make more money by actually looking forward?
  indicator: forward-looking sanity test · asset: multi · testable: yes · confidence: medium
  ^MT038-C03-3
- **Yuval** Test design should follow the essence of what the strategy captures; this may be market physicality or a mathematical trick, not necessarily a backtest.  #mech/research_method
  > think about what makes my strategy work work and then try to design the test around what is the essence of what the strategy is meant to capture.
  asset: multi · testable: partly · confidence: medium
  ^MT038-C03-4
- **Rob** Trend and momentum were found in the data before being explained, so let the data guide with conviction in a way that avoids overfitting.  #mech/research_method
  > I think momentum and trend were detected in the data first uh and then explained.
  asset: multi · testable: no · confidence: medium
  ^MT038-C03-5
- **Niels Kaastro Larsen** Powell stepping down as Fed chair is flagged as a rate-relevant event, with some expecting lower rates.  #mech/policy_reaction _(time-bound view)_
  > J. Powell is going to step down as chairman of the Fed after 8 years.
  indicator: Fed chair change · asset: rates · direction: lower rates (expected by some) · horizon: months · testable: no - political · confidence: low
  ^MT038-C03-6
- **Niels Kaastro Larsen** The 10-year JGB yield hit a 29-year high in May 2026.  #mech/policy_reaction _(time-bound view)_
  > the 10-year JGBs are hitting 29-year highs.
  indicator: 10-year JGB yield · asset: rates · horizon: months · testable: yes · confidence: high
  ^MT038-C03-7

### C04
- **Yuval** US Treasury 5% coupons (not seen since 2008) and high yields elsewhere reflect fiscal issues everywhere.  #mech/fiscal_debt _(time-bound view)_
  > I think you can buy US Treasury. There was another headline. You can buy US Treasury with 5% coupon.
  indicator: US Treasury yields · asset: rates · direction: yields up · horizon: months · testable: yes · confidence: medium
  ^MT038-C04-1
- **Yuval** After the April ceasefire equities and credit recovered to highs while bonds kept falling, so bonds were the laggard.  #mech/cycle_persistence _(time-bound view)_
  > Whereas in the bond market, we've seen a nice bounce when the ceasefire was announced. But then since then, we've seen the Treasury being dragged down.
  indicator: bonds vs equities after ceasefire · asset: multi · direction: bonds down, equities up · horizon: weeks · testable: yes · confidence: medium
  ^MT038-C04-2
- **Niels Kaastro Larsen** In momentum/trend strategies new all-time highs are a buy signal, unlike conventional thinking that highs are a bad time to buy.  #mech/cycle_persistence
  > it probably is a good buy to buy a time to buy when we see new all-time highs
  indicator: new all-time highs · asset: equities · direction: long at all-time highs · horizon: months · conditions: Momentum approach · testable: yes · confidence: medium
  ^MT038-C04-3
- **Niels Kaastro Larsen** Trend followers are short fixed income after years of it being their hardest sector since 2022; follow-through is uncertain.  #mech/cycle_persistence _(time-bound view)_
  > they're shorting fixed income the last few months so that would be interesting to see whether there's going to be any follow through because that has been perhaps the most difficult sector for many trend followers
  indicator: trend positioning in fixed income · asset: rates · direction: short bonds · horizon: months · testable: yes - CTA positions and sector returns · confidence: medium
  ^MT038-C04-4
- **Niels Kaastro Larsen** Large asset managers (Fidelity, BlackRock) entering trend following and Ritholtz launching a concentrated single-stock momentum product show growing mainstream adoption of momentum strategies.  #mech/crowding_positioning _(added by opus cross-check, time-bound view)_
  > here's another firm moving in the direction of momentum
  indicator: new momentum/trend product launches · asset: multi · direction: more capital in momentum · horizon: years · testable: partly - AUM in momentum/trend products vs factor returns · confidence: low
  ^MT038-C04-X1
- **Niels Kaastro Larsen** In May 2026 trend leadership shifted: metals and equities (US and Japan at new highs) and some currencies were trending, while energies were net slightly down for the month.  #mech/slow_reaction _(added by opus cross-check, time-bound view)_
  > we see a lot more in the metals as far as I can tell in terms of trends not so much in energies right now
  indicator: sector trend strength (metals, energy, equities, FX) · asset: multi · direction: long metals and equities; energy flat/down · horizon: weeks · testable: partly - sector P&L attribution · confidence: low
  ^MT038-C04-X2

### C05
- **Niels Kaastro Larsen** A trend barometer reading of 64 signals breadth (more markets trending) rather than stronger individual trends, which benefits trend followers.  #mech/cycle_persistence _(time-bound view)_
  > there's a lot of breath. It's not about that that trends are any, you know, stronger, but there are more of them in the 44 market portfolio that it tracks.
  indicator: trend barometer (44-market portfolio) · asset: multi · horizon: months · testable: yes - barometer is defined · confidence: medium
  ^MT038-C05-1
- **Niels Kaastro Larsen** May 2026 mid-month returns: Beta50 +1.41% (YTD 11.10%), SG CTA +1.45%, SG Trend +1.84%, Short-Term Traders +1.15%, MSCI World +2.61%, S&P 500 +3.31%, US Agg bond -0.12%.  #mech/cycle_persistence _(time-bound view)_
  > Beta 50 so far in May up 1.41% uh up 11.10 for the uh for the year.
  indicator: CTA indices and equity/bond indices · asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT038-C05-2
- **Yuval** Gold has not recovered with the weaker dollar, so the standard dollar-gold explanation fails currently.  #mech/liquidity_flows _(time-bound view)_
  > although we have seen the dollar uh slumping back and a lot of EM currencies performing very well uh um quite recently. The gold hasn't tracked it.
  indicator: gold vs dollar · asset: commodities · horizon: months · testable: yes · confidence: medium
  ^MT038-C05-3
- **Yuval** India, a large gold buyer, is cutting gold imports because of FX reserve strain from the energy crisis and a 15% tariff on gold and silver imports, weighing on gold.  #mech/liquidity_flows _(time-bound view)_
  > India is a big consumer of gold. They have because of the energy crisis, they are looking they are having trouble with FX reserves.
  indicator: Indian gold imports, tariff · asset: commodities · direction: gold down · horizon: months · conditions: Energy crisis · testable: partly · confidence: medium
  ^MT038-C05-4
- **Rob** Trend followers are very bearish in rates, counterintuitive to the average investor.  #mech/crowding_positioning _(time-bound view)_
  > bearish trend followers might be in rates today just given what we've seen in the data recently.
  indicator: trend positioning in rates · asset: rates · direction: short rates · horizon: months · testable: partly · confidence: medium
  ^MT038-C05-5

### C06
- **Yuval** The Betting Against Beta factor: high-beta assets underperform low-beta ones on a risk-adjusted basis.  #mech/risk_premium
  > why it seems to be that assets with equities with high beta will underperform equities with low beta to the to the sort of the S&P.
  indicator: beta-sorted portfolios · asset: equities · direction: long low beta, short high beta · horizon: years · testable: yes - factor is defined · confidence: high
  ^MT038-C06-1
- **Yuval** The BAB effect appears in US equities since the 1920s, international equities, bonds and credit, and only weakly in commodities.  #mech/risk_premium
  > It's been prevalent in international markets, international equity markets, but also in the bond markets, in the credit markets, and a little bit in commodities
  indicator: BAB factor · asset: multi · horizon: years · conditions: Weak in commodities · testable: yes · confidence: high
  ^MT038-C06-2
- **Yuval** BAB is built by going long low-beta and short high-beta assets, scaled to be beta neutral, which makes it zero beta by construction.  #mech/risk_management
  > I would marry it with a short in equities which have got high beta on them.
  indicator: BAB construction · asset: equities · horizon: years · testable: yes · confidence: high
  ^MT038-C06-3
- **Yuval** AQR's published BAB factor has 13 years of out-of-sample data and remains strong.  #mech/research_method
  > we now have 13 years of out of sample on the beta factor and long made continue it is actually very strong.
  indicator: AQR BAB factor · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT038-C06-4
- **Yuval** Rob's explanation: the low-beta long portfolio has high idiosyncratic risk and low correlation among its stocks, so it is a better diversified portfolio with a higher Sharpe, as trend followers prefer uncorrelated bets.  #mech/risk_premium
  > The portfolio that you are long is a much higher quality portfolio.
  indicator: portfolio diversification of low beta stocks · asset: equities · horizon: years · testable: yes - test with quality control · confidence: medium
  **Correction (cross-check):** Misattributes the idea: the diversification/quality explanation of BAB is Yuval's own interpretation ('I'm going to try and explain why I think this is making money'), not Rob's. → Yuval's explanation: the low-beta long portfolio has high idiosyncratic risk and low correlation among its stocks, so it is a better diversified, higher-Sharpe portfolio, just as trend followers prefer many uncorrelated bets.
  ^MT038-C06-5
- **Yuval** The low-volatility anomaly is consistent with BAB: low volatility stocks outperform high volatility stocks.  #mech/risk_premium
  > low volatility stocks tend to outperform high volatility stocks.
  indicator: low volatility factor · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT038-C06-6

### C07
- **Yuval** To be beta neutral BAB needs about $2 of low-beta stock per $1 of short high-beta, so it is net long notional.  #mech/risk_management
  > you have to be to buy essentially $2 of um of low beta stocks for $1 of high beta stocks.
  indicator: BAB hedge ratio · asset: equities · direction: net long · horizon: years · testable: yes · confidence: high
  ^MT038-C07-1
- **Yuval** Frazzini-Pedersen explanation: leverage-constrained investors overpay for high-beta stocks, so they underperform.  #mech/risk_premium
  > high beta stocks are more wanted by uh investors who have capital constraints
  indicator: financing constraints, TED spread · asset: equities · horizon: years · conditions: Tight leverage and financing · testable: yes - correlate BAB with TED spread · confidence: medium
  ^MT038-C07-2
- **Yuval** The paper shows BAB is more profitable when leverage constraints are tight, but this could be coincident rather than causal.  #mech/risk_premium
  > periods where there is more constraint on um on leverage and on finance, the betting [clears throat] against beta factor is more profitable.
  indicator: TED spread vs BAB returns · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT038-C07-3
- **Rob** BAB also appears in Treasuries (2-year beats 10-year risk-adjusted), where a quality difference cannot explain it.  #mech/risk_premium
  > if you were to look at US two-year versus 10-year, it seems like the two-year probably has better risk-adjusted returns in the long run.
  indicator: 2-year vs 10-year Treasury risk-adjusted return · asset: rates · horizon: years · testable: yes · confidence: medium
  ^MT038-C07-4
- **Rob** The BAB paper may not control for quality as a factor; the quality explanation is untested.  #mech/research_method
  > I don't recall whether they ran a control uh with quality as a factor on the right-hand side.
  indicator: quality factor control · asset: equities · horizon: years · testable: yes · confidence: low
  ^MT038-C07-5
- **Yuval** If financing constraints explained BAB, it should be stronger in markets with tighter finance than the US, but it is not.  #mech/risk_premium
  > you don't see that effect even even stronger.
  indicator: BAB across countries · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT038-C07-6
- **Yuval** Yuval doubts the leverage-constraint explanation for BAB because investors wanting more risk can get it through leveraged ETFs or futures rather than by overpaying for high-beta stocks.  #mech/research_method _(added by opus cross-check)_
  > if you really want to risk, um there's plenty of risk in the ETFs, plenty of risk in um in futures to actually get yourself exposed to that.
  asset: equities · conditions: leverage available via ETFs/futures · testable: partly - BAB returns before/after leveraged ETF availability · confidence: medium
  ^MT038-C07-X1

### C08
- **Yuval** Private equity and Berkshire Hathaway also invest in idiosyncratic risk with leverage, resembling BAB.  #mech/risk_premium
  > invest in idiosyncratic risk and leverage it up, which is exactly what this betting against beta factor does.
  asset: equities · horizon: years · testable: partly · confidence: medium
  ^MT038-C08-1
- **Rob** Institutions avoid leverage and take more duration for more risk, which is a plausible demand for long-end bonds.  #mech/behavioral
  > if I think about how large bond portfolios are likely managed, um they probably use more duration when they want more risk
  asset: rates · horizon: years · testable: partly · confidence: medium
  ^MT038-C08-2
- **Yuval** BAB is always net long notional so it earns the equity drift from a long equity bull market, while having low correlation to equity.  #mech/risk_management
  > notionally you're always long because the beta, in order to balance the the beta exposure, you will always be long more the the high quality the low beta portfolio
  indicator: BAB net notional exposure · asset: equities · horizon: years · conditions: Sample dominated by equity upswings · testable: yes · confidence: medium
  ^MT038-C08-3
- **Yuval** The BAB effect is weaker before 1945 and stronger afterwards.  #mech/research_method
  > actually the fact is not that strong before the 1945.
  indicator: BAB by sub-period · asset: equities · horizon: years · conditions: Pre-1945 · testable: yes · confidence: medium
  ^MT038-C08-4

### C09
- **Yuval** In the paper's model BAB's expected return is proportional to (beta high - beta low) over residual volatility, which is proportional to beta high times beta low.  #mech/research_method
  > it's got beta high minus beta low uh divided by the residual uh volatility that remains, which is really proportional to beta high times beta low.
  indicator: BAB formula · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT038-C09-1
- **Yuval** A 'betting against trend beta' (long trend in diversified portfolios, short trend in less diversified ones) might do well, but no evidence.  #mech/risk_premium
  > I'm going to make the assertion without having a shred of evidence on it that that will actually do do very well as a relative value trend portfolio.
  indicator: relative value trend · asset: multi · horizon: years · testable: yes - testable · confidence: low
  ^MT038-C09-2
- **Rob** Trend followers' crisis alpha occurred when all positions within an asset class were aligned (all long or all short equity indices), motivating decomposition into beta timing and cross-sectional tilt.  #mech/cycle_persistence
  > the trend following sort of crisis alpha, you know, delivering on crisis alpha seemed to occur when uh all of the positions within an asset class were pretty aligned.
  indicator: position alignment within asset class · asset: multi · horizon: months · conditions: Crisis periods · testable: yes · confidence: medium
  ^MT038-C09-3
- **Rob** A trend portfolio can be tilted and still defensive if the tilts are beta-neutral within each asset class.  #mech/risk_management
  > if you're going to tilt the trend portfolio and keep the defensiveness of it, one way to do that might be to have beta neutral tilts within each asset class.
  indicator: beta-neutral tilts · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT038-C09-4

### C10
- **Rob** Paper method: regress trend positions to split into the asset-class beta component and a residual volatility-neutral tilt.  #mech/research_method
  > we can actually use a formula that looks like a linear regression formula to decompose those exposures into the beta component um and then the residual
  indicator: trend position decomposition · asset: multi · testable: yes · confidence: high
  ^MT038-C10-1
- **Rob** Crisis alpha in a simple trend model comes mainly from beta timing, which is also most of its volatility.  #mech/cycle_persistence
  > the stereotypical crisis alpha, uh, returns seem to have come from the beta timing.
  indicator: beta-timing return · asset: multi · horizon: years · conditions: Crisis periods · testable: yes · confidence: high
  ^MT038-C10-2
- **Rob** Conditional correlation with equities is more negative for beta timing than for the relative-value tilt.  #mech/cycle_persistence
  > the conditional, uh, equity correlations were more negative for the beta timing than they were for, uh, the relative value.
  indicator: conditional correlation to equities · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT038-C10-3
- **Rob** Replace trend's relative-value component with carry divided by volatility in each asset class, producing largely beta-neutral portfolios that behave independently of trend.  #mech/risk_premium
  > carry over vol is likely the signal and it's the signal we use in the paper to build these carry portfolios within each
  indicator: carry over vol · asset: multi · direction: long high carry-to-vol, short low · horizon: years · conditions: Within asset classes · testable: yes · confidence: medium
  ^MT038-C10-4
- **Rob** Carry-over-vol tilts historically did slightly better than trend and better than trend's relative-value component.  #mech/risk_premium
  > actually carry seems historically to have done a little bit better than trend.
  indicator: carry vs trend returns · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT038-C10-5
- **Rob** Trend is episodic and tolerated poorly during long equity bull runs, so adding carry could help in such periods.  #mech/behavioral
  > when stocks or the SPY are up a huge amount every year for for five or more years, it's hard to remember why you have an alternative in your portfolio.
  asset: multi · horizon: years · conditions: Strong equity bull markets · testable: partly · confidence: medium
  ^MT038-C10-6

### C11
- **Rob** Swapping carry for trend's relative value preserves defensiveness only if the tilt is market neutral in volatility space.  #mech/risk_management
  > The condition for that being true is that the the portfolio that you use to tilt has to be market neutral in volatility space.
  indicator: vol-neutral tilt · asset: multi · horizon: years · conditions: Tilt portfolio must be volatility neutral · testable: yes · confidence: high
  ^MT038-C11-1
- **Yuval** About 75% of trend's risk is beta timing, which explains the skew and crisis alpha; trend is largely macro-level trend across assets.  #mech/cycle_persistence
  > about 75% of the risk is um is in sort of essentially beta timing
  indicator: beta-timing risk share · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT038-C11-2
- **Yuval** Commodity or bond trend alone has negative correlation to equities, so the crisis alpha is not just mechanical shorting of equities.  #mech/cycle_persistence
  > If I look at commodity trend, okay, or bond trend, okay, which has got no explicit exposure to equity. Overall, it has negative correlation to equity.
  indicator: trend correlation to equity by asset class · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT038-C11-3
- **Yuval** Trend behaves like long straddles that gain when volatility rises, and equities are negatively correlated with volatility, giving trend a structural negative equity correlation.  #mech/cycle_persistence
  > trend following is a little bit like buying straddles in each of the assets that you trend.
  indicator: trend as straddle, equity-volatility correlation · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT038-C11-4
- **Yuval** Bond markets differ in risk-on/risk-off behaviour, so building one beta per asset class is a simplification.  #mech/research_method
  > you can think of Italian bonds are actually risk on, whereas Japanese bonds are risk off, for example.
  indicator: bond beta construction · asset: rates · horizon: years · testable: partly · confidence: medium
  ^MT038-C11-5

### C12
- **Yuval** Relative-value trend is valuable and keeps negative equity correlation, so discarding it entirely is questionable.  #mech/cycle_persistence
  > signal is strong on one asset within the asset class, it is likely to perform better than an asset with a weaker trend.
  indicator: relative-value trend within asset class · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT038-C12-1
- **Rob** In practice one can keep native relative-value trend and overlay carry or resize it; the paper's replacement was illustrative.  #mech/risk_management
  > You could choose to keep the sort of native amount of relative value trend in the portfolio and just overlay something else over it.
  asset: multi · testable: partly · confidence: medium
  ^MT038-C12-2
- **Yuval** Trend portfolios typically run about 3.5-4x risk leverage, and adding more relative-value could increase leverage and trading costs.  #mech/risk_management
  > if I think about the leverage of a trend portfolio, it's normally something like three and a half to 4x um in terms of the risk.
  indicator: trend portfolio leverage · asset: multi · testable: yes · confidence: medium
  ^MT038-C12-3
- **Rob** Tilting within asset classes reduces diversification, which could lower the leverage needed, so the net effect is ambiguous.  #mech/risk_management
  > on average you're actually reducing diversification by tilting within each asset class.
  asset: multi · testable: partly · confidence: low
  ^MT038-C12-4
- **Niels Kaastro Larsen** Carry looks good most of the time and then suffers horrific periods, so adding it to trend risks hurting crisis protection.  #mech/risk_premium
  > carry is also known for looking great most of the time and then suddenly it has a really horrific period
  indicator: carry crash risk · asset: multi · horizon: years · conditions: Risk-off periods · testable: yes · confidence: medium
  ^MT038-C12-5

### C13
- **Rob** Carry built long/short with equal volatility within an asset class avoids the usual poor crisis performance.  #mech/risk_management
  > if you do EM carry uh EM FX carry just in EM and you go equal vol long and short, we don't see a lot as much of this uh sort of bad crisis performance
  indicator: EM FX carry vol-neutral · asset: fx · horizon: years · conditions: Equal vol long/short · testable: yes · confidence: medium
  ^MT038-C13-1
- **Rob** The essence of trend's benefit is adaptability across regimes; you don't need pure trend to get it.  #mech/cycle_persistence
  > It's really these regime-changing adaptable sort of properties that trend following has that really is sort of the essence of the benefit
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT038-C13-2
- **Rob** The paper did not optimise the carry/trend mix (no tipping point analysis), using round numbers.  #mech/research_method
  > We wanted to just pick nice round numbers and put them in there.
  asset: multi · testable: yes · confidence: high
  ^MT038-C13-3
- **Yuval** Investors like layering another strategy on top of 100% trend (portable alpha) because it gives more risk for fees, especially when they cannot lever.  #mech/risk_management
  > I can have 100% of trend, but also on top of it another 30% of another strategy
  indicator: portable alpha overlay · asset: multi · conditions: Investors unable to use leverage · testable: partly · confidence: medium
  ^MT038-C13-4

### C14
- **Yuval** In the March crisis execution reduced longs and shorts separately, when the right action was to cut the dominant duration factor immediately.  #mech/risk_management _(time-bound view)_
  > both the long and the short were trying to reduce size, whereas actually what you were trying to do is to reduce the first factor, the like the your duration straight away during the crisis.
  indicator: fixed income execution in crisis · asset: rates · direction: reduce duration first · horizon: days · conditions: Crisis · testable: partly · confidence: medium
  ^MT038-C14-1
- **Yuval** Execution trades off passivity (lower spread cost) against accumulated risk of holding the order.  #mech/risk_management
  > the more you hold on to the order, the more sort of risk you're accumulating in the sense that you're increasing your volatility of your tracking error to some benchmark.
  indicator: order execution trade-off · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT038-C14-2
- **Yuval** Execution quality is measured against arrival price or VWAP/TWAP.  #mech/research_method
  > most execution algorithms are benchmarked against either the price that they were given when the order was first received.
  indicator: arrival price, VWAP, TWAP · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT038-C14-3
- **Yuval** CTAs typically start passive and become aggressive as the deadline nears, leaving risk when the order is largest.  #mech/risk_management
  > we would receive an order and we start by being passive. And we are passive and we are passive until we run out of time, at which point we become less passive
  indicator: CTA execution schedule · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT038-C14-4
- **Yuval** Almgren's finding: be aggressive first and passive later, since risk is highest at the start.  #mech/risk_management
  > what you should do is you should start immediately cut the risk that you're holding in the order very quickly.
  indicator: front-loaded execution · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT038-C14-5

### C15
- **Yuval** In pair orders, low-correlation legs (soybean vs oil) can be executed independently, but highly correlated legs (2y/10y) must be coordinated to avoid beta risk.  #mech/risk_management
  > But as the correlation between the markets you have a higher correlation, you have to start thinking about about the spreads.
  indicator: correlation of order legs · asset: multi · horizon: days · conditions: Correlated legs · testable: yes · confidence: medium
  ^MT038-C15-1
- **Yuval** Different trading hours (Asia vs US bonds) create hedge mismatch in pair orders.  #mech/risk_management
  > sometimes those markets will be open at different times or they will be the trading hours that you have will be at different times.
  indicator: trading hours · asset: rates · horizon: days · testable: yes · confidence: medium
  ^MT038-C15-2
- **Rob** Because trend's information coefficient is low, routine rebalances should not be traded aggressively.  #mech/risk_management
  > trend doesn't have a super high information coefficient. So, how strong is this view? Um and if it's not that strong, do we really want to be aggressive ever?
  indicator: information coefficient · asset: multi · horizon: days · conditions: Modest rebalances · testable: partly · confidence: medium
  ^MT038-C15-3
- **Rob** Crisis risk reduction should be handled separately from alpha execution.  #mech/risk_management
  > in cases where um we're thinking about risk management uh in in a crisis environment, I think those could be handled separately.
  asset: multi · horizon: days · conditions: Crisis · testable: partly · confidence: medium
  ^MT038-C15-4

### C16
- **Rob** When one market is closed and correlation is high, hedge with the cheapest available asset then rebalance.  #mech/risk_management
  > you can reduce risk uh sort of by by uh intentionally choosing the most available and cheapest to trade asset and then rebalancing around that position.
  asset: multi · horizon: days · conditions: High conviction in correlation · testable: partly · confidence: medium
  ^MT038-C16-1
- **Rob** In alternative markets trade passively over multiple days.  #mech/risk_management
  > I talked about multi-day execution and saying you want to be passive as long as possible, right?
  indicator: multi-day execution · asset: multi · horizon: days · conditions: Alternative markets · testable: partly · confidence: medium
  **Correction (cross-check):** Wrong speaker: the preference for passive multi-day execution in alternative markets is Yuval's (he refers to his first appearance on the podcast; it is Rob's first time on the show). → Yuval: in alternative (less liquid) markets stay passive as long as possible and execute over multiple days.
  ^MT038-C16-2
- **Yuval** OTC and commodity markets (freight) need broker execution that cannot be fully automated.  #mech/risk_management
  > A lot of the markets that we trade are OTC and they're not they don't they don't necessarily trade on the exchange and you can't really automate it.
  asset: multi · horizon: days · conditions: OTC markets · testable: partly · confidence: high
  ^MT038-C16-3
- **Yuval** In crises correlations spike and the first factor dominates, so liquid markets become substitutes for less liquid ones.  #mech/liquidity_flows
  > exactly during the time of crisis what we observe is that the first factor actually becomes very dominant
  indicator: cross-asset correlation · asset: multi · horizon: days · conditions: Crisis · testable: yes · confidence: high
  ^MT038-C16-4
- **Yuval** A static correlation assumption is a flaw in execution models, since correlations change in crises.  #mech/risk_management
  > your correlation estimation, the fact that you're kind of assuming the correlation is static, I think is an issue.
  asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT038-C16-5
- **Yuval** Discretionary macro traders in crises first cut risk in the most liquid assets (S&P, crude, Treasuries), then refine by view.  #mech/risk_management
  > It would pick the first most liquid assets, you know, be it the S&P, be it crude, be it uh US Treasuries to reduce its overall duration or its overall beta to equities.
  asset: multi · horizon: days · conditions: Crisis · testable: partly · confidence: medium
  ^MT038-C16-6

### C17
- **Rob** The correlation estimate used to execute may be stale exactly when it is needed in a crisis.  #mech/risk_management
  > that correlation estimate we're using to execute could potentially be stale at the exact time when we need it
  indicator: correlation estimates · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT038-C17-1
- **Rob** Transaction costs rise sharply when volatility spikes, complicating crisis execution.  #mech/risk_management
  > the other thing is transaction costs go up a lot. And when volatility goes up a lot
  indicator: transaction cost vs volatility · asset: multi · horizon: days · conditions: High volatility · testable: yes · confidence: medium
  ^MT038-C17-2
- **Yuval** Intraday correlation spikes (Shephard) signal risk-off because markets are becoming dysfunctional.  #mech/risk_management
  > when there is a spike in correlation, that's generally a a risk off signal because it's an indication that the market is becoming dysfunctional
  indicator: intraday correlation · asset: multi · direction: risk-off · horizon: days · testable: yes · confidence: medium
  ^MT038-C17-3

