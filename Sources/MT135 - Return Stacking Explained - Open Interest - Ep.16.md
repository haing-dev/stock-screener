---
source_id: MT135
title: "Return Stacking Explained - Open Interest - Ep.16"
date: 2025-06-07
channel: "Top Traders Unplugged"
url: 
words: 11510
claims: 37
added_by_opus: 0
corrections: 0
crosscheck: "pending"
speakers: ["Cory Hoffstein (Newfound Research / Return Stacked)", "Adam Butler (Resolve Asset Management / Return Stacked)", "Moritz (Open Interest host)", "Moritz (co-host, Takahi Capital partner)"]
tags: [source, layer0]
---
# Return Stacking Explained - Open Interest - Ep.16

**Speakers:** Cory Hoffstein (Newfound Research / Return Stacked); Adam Butler (Resolve Asset Management / Return Stacked); Moritz (Open Interest host); Moritz (co-host, Takahi Capital partner)

**Summary:** Open Interest ep.16 (Apr-Jun 2025): return stacking and portable alpha ETFs; top-down and bottom-up replication of the SG Trend Index; ETF capacity and liquidity; stacking limits; merger arbitrage and gold/Bitcoin overlays.

**Approach:** return stacking, replication, trend following, portable alpha, merger arbitrage

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | preview of later point (30/70 blend), intro, guest background |
| C02 | 2 | portable alpha and return stacking concept |
| C03 | 2 | ETF vs mutual fund; ETF liquidity |
| C04 | 1 | bid-ask spreads and ETF trading |
| C05 | 3 | capacity, CFTC limits, universe size, no closing |
| C06 | 1 | bottom-up replication method |
| C07 | 3 | bottom-up fit, resulting weights, recalibration |
| C08 | 2 | stability of fitted weights; market set limits |
| C09 | 3 | dispersion, fat-tail markets, top-down method |
| C10 | 3 | top-down pros/cons; blend |
| C11 | 2 | rationale for blend; CTA index replication |
| C12 | 4 | feature families, ETFs as benchmark, crisis offset |
| C13 | 3 | vol levels, high-vol trend, client vol tolerance |
| C14 | 3 | stacking limits, 18f-4, margin |
| C15 | 2 | April drawdown ops; merger arbitrage |
| C16 | 2 | merger arb index; gold/Bitcoin product |
| C17 | 1 | gold plus Bitcoin overlay; outro |

## Claims

### C02
- **Cory Hoffstein** Portable alpha / return stacking keeps core stock and bond beta and uses futures, swaps and capital efficiency to free capital for other alpha sources (trend, carry, merger arb).  #mech/risk_management
  > how can you keep your beta in your portfolio, the core stocks and bonds that institutions are building their strategic asset allocation around, but search for alpha in more fruitful places
  indicator: return stacking · asset: multi · direction: long stocks/bonds plus overlay · horizon: years · testable: yes - backtest overlay on 60/40 · confidence: high
  ^MT135-C02-1
- **Cory Hoffstein** Selling alternatives by asking investors to cut stocks and bonds failed in the 2010s; a capital-efficient stacked product avoids that behavioural obstacle.  #mech/behavioral
  > struggled against the non-stop outperformance particularly here in the US of a core US6040
  asset: multi · horizon: years · conditions: strong US 60/40 period · testable: no · confidence: medium
  ^MT135-C02-2

### C03
- **Adam Butler** Mutual fund wrappers can trade a wider futures set than ETFs because ETF market makers need liquid hedges for creations and redemptions.  #mech/liquidity_flows
  > the mutual fund strategies are able to trade a a slightly wider and more diverse group of futures markets
  asset: multi · testable: no · confidence: high
  ^MT135-C03-1
- **Cory Hoffstein** Futures-based ETF trend products use a subset of the most liquid US and European markets versus the full set in their mutual fund and hedge fund versions.  #mech/structural_shift
  > most of the futures based products that are coming out from Alpha Simplex and ManHL and Invesco and Black Rockck tend to be subset a
  asset: multi · testable: no · confidence: high
  ^MT135-C03-2

### C04
- **Adam Butler** Small-size ETF trades in less liquid futures baskets face bid-ask spreads of 20-30 bp on average and wider in stress; large trades via institutional desks can be done near NAV, and holding long term smooths cost.  #mech/risk_management
  > badass spreads of 20 30 [L160] basis points on average I don't think are unusual
  indicator: ETF bid-ask spread · asset: multi · horizon: days · conditions: small trade size, chaotic markets · testable: yes - observe spreads · confidence: medium
  ^MT135-C04-1

### C05
- **Adam Butler** CFTC limits on front-month positions can be bypassed by trading back-month contracts, giving 10x or more capacity.  #mech/risk_management
  > CFTC limits that limit the number of contracts that can be held in the front month
  asset: multi · testable: yes · confidence: high
  ^MT135-C05-1
- **Adam Butler** A 26-27 market universe covering equities, bonds, commodities and currencies (70-80% of global futures liquidity) replicates the full CTA universe closely because all players trade in proportion to liquidity.  #mech/research_method
  > you can get pretty darn close in replication space with a much more finite universe of markets as long as you're spanning the equity index, bond index, commodity, and currencies
  indicator: replication with ~26 markets · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT135-C05-2
- **Cory Hoffstein** An ETF cannot be closed to inflows, so the strategy must be run identically at all sizes; at extreme scale performance would degrade and self-correct.  #mech/liquidity_flows
  > you can't close the ETF. So, we have to be able to run it at in theory infinite scale.
  indicator: capacity · asset: multi · conditions: very large AUM · testable: no · confidence: medium
  ^MT135-C05-3

### C06
- **Adam Butler** Bottom-up replication: for each market build time-series trend strategies with lookbacks from 5 to 300 days and regress them on the SG Trend Index (daily since 2000) to pick the weights that best fit.  #mech/research_method
  > we regressed all of these individual market individual trend length strategies on the societ general trend index over the very long term
  indicator: SG Trend Index regression · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT135-C06-1

### C07
- **Adam Butler** The bottom-up replication achieves about 0.8 daily correlation to the SG Trend Index, which is an average of 10 funds with differing styles.  #mech/research_method
  > the bottomup strategy actually does just a really good job with an average correlation daily correlation in the neighborhood of kind of 0.8
  indicator: SG Trend Index replication correlation · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT135-C07-1
- **Cory Hoffstein** Fitting to the SG Trend Index gives intermediate trend speeds and about equal 25% risk weights in equities, bonds, commodities and currencies, with commodity risk split evenly between metals and energies.  #mech/structural_shift
  > You get intermediate term trend speeds and you get 25% of your risk weight pretty much in equity indices, in bonds, in commodities, in currencies.
  indicator: fitted sector risk weights · asset: multi · direction: equal risk across four sectors · horizon: years · testable: yes · confidence: high
  ^MT135-C07-2
- **Adam Butler** Fitting trend weights needs 15-20 years of data because a market that produced no P&L in a decade cannot be distinguished from one managers did not trade.  #mech/research_method
  > for all the markets you're trading to have gone through meaningful periods of contributing positive or negative P&L
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT135-C07-3

### C08
- **Adam Butler** Fitted market weights change by decade (S&P trendless in 2000-10, trendy 2010-20) but sector weights and trend speeds stay stable under cross-validation, and there is no evidence that trend length rose systematically 2000-2020.  #mech/research_method
  > the sector weight was still very consistent
  indicator: fitted weights over time · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT135-C08-1
- **Cory Hoffstein** The trend index consists of the largest managers, whose less liquid markets matter little to P&L, so a limited-market replication tracks them well.  #mech/liquidity_flows
  > as you grow in AUM the less liquid markets that you trade end up having a smaller impact on total portfolio P&L
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT135-C08-2

### C09
- **Cory Hoffstein** Idiosyncratic bets such as coffee in 2023-24 created manager dispersion that later reversed, and on average dispersion balances out.  #mech/cycle_persistence _(time-bound view)_
  > coffee was a big one, uh, in 2024, uh, and 2023
  indicator: coffee · asset: commodities · horizon: years · testable: yes · confidence: medium
  ^MT135-C09-1
- **Adam Butler** Large trend managers put about 80% of risk in the same ~20 markets, and averaging the fat-tail weights across managers attenuates toward zero, so the beta can be captured with a handful of common markets.  #mech/research_method
  > 80% of their risk weights probably in the same 20 markets we could all rattle off the top of our head
  indicator: risk weight concentration · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT135-C09-2
- **Cory Hoffstein** Top-down replication: run a robust regression of recent index returns on futures markets to find the long/short basket that mimics it, assuming weights hold one day ahead.  #mech/research_method
  > is a regressionbased approach, right? Where we're going to look at the most recent performance of something like the sock gen trend index
  indicator: robust regression of SG Trend Index on futures · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT135-C09-3

### C10
- **Cory Hoffstein** Top-down regression is flexible and can approximate untraded markets (e.g. Swiss franc via gold and euro) and capture manager innovation.  #mech/research_method
  > it can capture the return of markets that we're not necessarily trading because of the way regression works
  asset: multi · horizon: days · testable: yes · confidence: high
  ^MT135-C10-1
- **Cory Hoffstein** Top-down weights lag by the 20-40 day lookback (regional bank crisis 2023 shift missed) and cannot see positions in markets with no recent P&L.  #mech/research_method
  > it is by definition rearward facing
  asset: multi · horizon: days · conditions: after sudden manager repositioning, flat markets · testable: yes · confidence: high
  ^MT135-C10-2
- **Cory Hoffstein** Top-down and bottom-up replicate the trend index equally well, but their tracking errors are weakly correlated, so a 30% top-down / 70% bottom-up blend lowers tracking error.  #mech/research_method
  > the two systems are almost identical, they're statistically indistinguishable
  indicator: blend of top-down and bottom-up replication · asset: multi · direction: blend 30/70 · horizon: years · testable: yes · confidence: high
  ^MT135-C10-3

### C11
- **Adam Butler** Top-down is kept because managers constantly innovate; it captures idiosyncratic methods the continuous bottom-up misses, even though bottom-up has better average fit.  #mech/research_method
  > the top down is an expression of epistemological humility
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT135-C11-1
- **Cory Hoffstein** Replicating the broader CTA index (with mean reversion, VIX trading, carry) is harder bottom-up; Andrew Beer's CTA fund uses only top-down.  #mech/research_method
  > I'll say it makes it harder to do the bottom up for sure.
  indicator: SG CTA index replication · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT135-C11-2

### C12
- **Adam Butler** Adding carry, skewness, seasonality and relative-value features improves fit to the CTA index much more than to the trend index, where the gain is marginal.  #mech/research_method
  > They improve the explanatory fit against the CTA index to a larger extent than they improve it relative to the trend index
  indicator: explanatory fit · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT135-C12-1
- **Moritz (co-host)** Replication ETFs form a cheap benchmark that performance-fee hedge funds must beat over the long run.  #mech/research_method
  > you better beat these ETFs who replicate, as you say, or who give access, costefficient access to the beta of our industry
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT135-C12-2
- **Cory Hoffstein** Per Quantica, a longer tail of markets raises Sharpe but diverts risk from markets tied to big macro factors, reducing crisis offset.  #mech/risk_management
  > because you're putting so much of your risk budget in this longer tale of markets, you don't necessarily get the same crisis offset
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT135-C12-3
- **Cory Hoffstein** Generic trend beta is available in QIS at 10-15 bp, so managers must differentiate through spreads, breakout, speed, or fat-tail markets.  #mech/structural_shift
  > those hedge funds that are doing very generic trend, uh, I think you're right, are just going to get squeezed out by lower cost
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT135-C12-4

### C13
- **Moritz (co-host)** Trend funds now run 8-12% volatility, so returns lack the punch of 1980s-90s CTAs, trading off stress payoff.  #mech/structural_shift
  > most of the funds in our space have lowered their volatility profiles in recent years
  indicator: CTA target vol · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT135-C13-1
- **Adam Butler** A high-vol trend strategy is a capital-efficient version of a low-vol one (50 vol with a fifth of capital equals 10 vol) and at the limit a portable alpha overlay.  #mech/risk_management
  > a very high ball [L520] trend strategy
  asset: multi · testable: yes · confidence: medium
  ^MT135-C13-2
- **Adam Butler** Most clients cannot tolerate more than about 10% vol and line-item risk, so products shifted to 10-12% vol.  #mech/behavioral
  > most clients can't tolerate more than 10 ball
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT135-C13-3

### C14
- **Cory Hoffstein** Stack only low-correlation components such as equity plus trend, which diversify each other.  #mech/risk_management
  > you would not combine things that are closely correlated
  asset: multi · direction: stock plus trend · testable: yes · confidence: medium
  ^MT135-C14-1
- **Cory Hoffstein** SEC Rule 18f-4 caps fund VaR at 20% or two times the benchmark, limiting how far stacking can be pushed.  #mech/risk_management
  > you can only have a 20day 99 percentile VAR of either 20% or two times your relevant benchmark
  indicator: 20-day 99% VaR · asset: multi · conditions: US ETFs and mutual funds · testable: yes · confidence: high
  ^MT135-C14-2
- **Adam Butler** Nightly rebalancing keeps the beta/trend ratio fixed after losses; trend collateral needs only 25-30% of NAV with 40-50% cash buffer, so ruin risk is negligible, as seen in the April 2025 drawdown.  #mech/risk_management
  > the risk of ruin is is fairly negligible and also I mean we only need at maximum kind of 25 or 30% uh of the of the total portfolio value to collateralize
  indicator: margin usage · asset: multi · horizon: days · conditions: drawdown in both stocks and trend · testable: yes · confidence: high
  ^MT135-C14-3

### C15
- **Cory Hoffstein** Merger arbitrage earns a spread equal to time value of money plus deal-break risk premium; generic strategies earned about 200-250 bp over SOFR over 20 years.  #mech/risk_premium
  > it typically doesn't get all the way to the buyout price
  indicator: merger arbitrage spread · asset: equities · direction: long deal targets · horizon: years · testable: yes · confidence: high
  ^MT135-C15-1
- **Cory Hoffstein** Merger arbitrage has low correlation to equity, bond and credit premia (about 0.5 to credit), making it a diversifying stack.  #mech/risk_premium
  > correlation of just 0.5 to the credit risk premium
  indicator: merger arbitrage correlation · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT135-C15-2

### C16
- **Cory Hoffstein** The Alpha Beta merger arbitrage index uses machine learning on spread, acquirer and industry to estimate deal-close probability and includes only deals that clear a return hurdle; stock-deal acquirers are hedged short or via swaps.  #mech/risk_premium
  > they're using a machine learning model to look at effectively the quality of the deal
  indicator: Alpha Beta merger arbitrage index · asset: equities · horizon: months · conditions: US-listed deals above size threshold · testable: partly · confidence: medium
  ^MT135-C16-1
- **Cory Hoffstein** Stacked suite distinguishes diversifying strategies (trend, carry, merger) from diversifying assets (gold, Bitcoin) as overlays on equities and bonds.  #mech/risk_management
  > There's diversifying strategies and there's diversifying assets.
  asset: multi · testable: no · confidence: medium
  ^MT135-C16-2

### C17
- **Cory Hoffstein** A risk-balanced gold plus Bitcoin overlay on US equity offers a store-of-value diversifier to a stock-bond portfolio.  #mech/structural_shift
  > gold in particular, and I think Bitcoin is proving some of these features, uh, can be a very interesting long-term diversifier for a stock bond portfolio
  indicator: gold, Bitcoin · asset: multi · direction: long gold and Bitcoin overlay · horizon: years · testable: partly · confidence: low
  ^MT135-C17-1

