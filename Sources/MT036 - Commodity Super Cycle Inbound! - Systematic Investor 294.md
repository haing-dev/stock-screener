---
source_id: MT036
title: "Commodity Super Cycle Inbound! - Systematic Investor 294"
date: 2024-05-09
channel: "Top Traders Unplugged"
url: 
words: 9114
claims: 80
added_by_crosscheck: 13
corrections: 1
crosscheck: "opus cross-check"
speakers: ["Harry Krishnan (guest, volatility/options manager)", "Niels Kaastro Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Commodity Super Cycle Inbound! - Systematic Investor 294

**Speakers:** Harry Krishnan (guest, volatility/options manager); Niels Kaastro Larsen (host, Top Traders Unplugged)

**Summary:** Niels Kaastro Larsen and Harry Krishnan discuss zero-day options crowding, April CTA performance and the cocoa spike, then Krishnan's 'virtual warehousing' of cheap commodities. The approach buys futures at cheap curve points and pays the roll cost by selling overpriced moderately out-of-the-money calls (hedged with far calls), then converts to trend following once prices rise. Conclusions: commercial hedgers make moderate call options rich across storable commodities, and the structure caps losses at ~25% of down moves while capturing ~2/3 of rallies.

**Approach:** options volatility, commodity carry / virtual warehousing, trend following, regime-based participation, commodity super cycle

**Cross-check completeness estimate of first read:** 0.87 - first reader caught all core mechanisms (roll vs theta, hedger-driven rich calls, payoff profile, regimes); missed the host's challenges (Ukraine spike reversal, negative oil storage, timing risk), the trend barometer reading and some caveats on margins/flows.

## Argument map

**Episode thesis:** Harry Krishnan argues that commodity option markets are structurally mispriced because commercial hedgers and credit-constrained end users make moderately out-of-the-money calls rich, so a long futures position at cheap curve points can have its roll cost paid by selling those calls (bounded by far calls), giving a 'virtual warehouse' that loses about a quarter of further declines and captures about two thirds of rallies, then converts to trend following once prices rise. The episode opens with his warning that the popular 0DTE short-straddle trade is a crowded, short-sample, untested-through-a-vol-spike strategy, and the host adds the trend-following view of April 2024 CTA performance and the cocoa spike.

### Harry Krishnan (Guest; volatility/options manager and author, now building commodity 'virtual warehousing' structures)
Fingerprint: #approach/volatility_options #approach/value_mean_reversion #approach/positioning_crowding #approach/commodity_fundamentals #approach/structural_themes #approach/carry #approach/regime_detection #approach/crisis_alpha_convexity
_Speaker note: Caption attribution is clear for the long answers; the ledger assigns the COT 'blurred' question in C04 to the host._

**Worldview premises**
- Option prices are set partly by hedging necessity, not only by arbitrage, so insurance demanded by institutions or hedgers is systematically overpriced at certain strikes (moderately OTM S&P puts, moderately OTM commodity calls) while extreme strikes are not. _[institutional, stated; support: Backtests across markets; institutional product flows (collars) and commercial hedging behaviour]_ ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C05-4|C05-4]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C05-5|C05-5]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C08-1|C08-1]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C09-3|C09-3]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C10-1|C10-1]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C09-R1|C09-R1]])
- Commercial hedgers (farmers, elevators, miners) sell futures into rallies because they want to stay in business, not capture the right tail, so moderate uptrends rarely accelerate. _[behavioural, stated; support: Research on corn and copper; stylised fact tested with backtests and statistics]_ ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C07-4|C07-4]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C07-5|C07-5]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C07-6|C07-6]])
- Non-storable markets (VIX, natural gas, electricity) share the same structure: severe contango, heavy roll-down, sporadic mega spikes, so structures transfer between them. _[theoretical, stated; support: Analogy then backtest in his engine]_ ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C04-5|C04-5]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C05-1|C05-1]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C05-2|C05-2]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C05-3|C05-3]])
- Roll cost of a long futures position rises sharply as the price falls (curve effects), unlike physical storage cost, so cheap commodities are costly to hold via standard futures. _[empirical, stated; support: Corn 2000-present: about $1 to buy and roll at a $3 price]_ ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C07-1|C07-1]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C11-3|C11-3]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C11-2|C11-2]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C06-3|C06-3]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C07-2|C07-2]])
- Volatility is cyclical while prices trend, so paying for insurance when vol is high is worse than selling into the decline (trend following). _[theoretical, stated; support: Experience in the hedging business]_ ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C10-5|C10-5]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C10-6|C10-6]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C10-7|C10-7]])
- Every option structure encodes a regime bet; there is no structure that works in all cases, so participation should be regime-based. _[experience, stated; support: Options practitioner experience]_ ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C10-8|C10-8]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C10-2|C10-2]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C10-3|C10-3]])
- Crowded, popular trades distort markets, and short-vol records in a sample with no vol spike prove little. _[experience, stated; support: Own backtests of 0DTE (Sharpe above 1 to 1.5 since 2022, only 2-3 years of data)]_ ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C01-1|C01-1]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C01-3|C01-3]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C01-4|C01-4]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C02-1|C02-1]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C02-X1|C02-X1]])
- Commodity prices should rise over the medium term because of deglobalisation, green-transition metal demand, remilitarisation and weather volatility. _[theoretical, stated; support: Qualitative; wheat tripled in both world wars as analogy; admits technology limits grain upside]_ ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C05-6|C05-6]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C05-7|C05-7]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C05-8|C05-8]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C05-9|C05-9]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C06-1|C06-1]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C06-2|C06-2]])
- Demand for long-vol and trend-following strategies is cyclical: flows arrive after bad markets and dry up in long calm periods. _[experience, stated; support: Own business experience]_ ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C04-X1|C04-X1]])

**Chain: Why moderately OTM commodity calls are overpriced and how that pays for carry**
1. Producers, storage and elevator operators want to lock in gains as prices rise → They sell futures into rallies: Staying in business matters more than the right tail ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C07-4|C07-4]])
2. Selling into rallies → Moderate uptrends rarely go ballistic: Commercial supply of futures dampens moves ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C07-5|C07-5]])
3. Moderate moves are more likely than expected from option pricing, and end users (airlines) buy simple calls for protection → Moderately OTM calls are rich while far OTM calls are not: Hedging demand is for moderate outcomes; credit-constrained end users avoid open-ended structures ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C07-6|C07-6]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C10-1|C10-1]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C08-1|C08-1]])
4. Sell moderate OTM calls, buy far OTM and at-the-money calls → Premium theta pays for futures roll-down; flat-market cost near zero, bounded risk: Reverses the hedging case where roll-down pays for theta ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C07-3|C07-3]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C07-7|C07-7]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C07-8|C07-8]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C10-4|C10-4]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C09-2|C09-2]])
- Evidence: Backtests for nearly all storable commodities, stable cross-sectionally; no live track record cited.
- Fails when: Prices spike in a day (captures only ~50% of the upside), prices drop sharply (loses ~25% of the decline), options illiquid beyond the ~10-15 biggest markets, non-storable underlyings.

**Chain: Virtual warehousing then trend conversion**
1. Commodity price is depressed → Skew is asymmetric to the upside and a trend follower would be short with roll costs: Gas at $1.50 has more upside than downside; at $6-7 risk is symmetric ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C08-5|C08-5]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C08-3|C08-3]])
2. Hold futures at cheap curve points plus the option overlay → Wait cheaply for a rise: Holder is implicitly paid to wait and break-even falls from about 30% to a hoped-for 5-10% ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C06-4|C06-4]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C11-3|C11-3]])
3. Price rises significantly → Convert to trend following: Relative-value edge fades as hedging is monetised; trend following captures the full move and has built-in exit ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C10-3|C10-3]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C08-4|C08-4]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C08-2|C08-2]])
- Evidence: Backtest rule of thumb; the host challenges the switch as regime timing.
- Fails when: Storage is scarce and full (2020 oil went negative, host challenge); structural narrative does not produce a lasting rally (post-2022 commodity sell-off).

**Chain: 0DTE short-straddle crowding**
1. Portfolio managers with end-of-day risk limits buy zero-day options → Short-dated vol is rich versus 2-3 days out: Cheap fixed-cost tail patch ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C01-2|C01-2]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C02-2|C02-2]])
2. Rich short-dated vol and a record without vol spikes → Selling straddles looks like Sharpe above 1: Sample 2022-2024 contains no major spike ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C01-4|C01-4]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C02-1|C02-1]])
3. Idea goes viral → Market distortions and a fragile trade: Crowding ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C01-1|C01-1]])
- Evidence: Own backtests, with admitted short data.
- Fails when: A volatility event arrives; he says he sees 'something brewing' but gives no timing.

**Chain: Cocoa as a crowded technical trade**
1. Poor West African production → Price rise: Fundamental trigger ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C03-X3|C03-X3]])
2. Managed money as large as commercials in open interest in an illiquid market → Technical, positioning-driven extension: Managed money correlates with trend ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C03-4|C03-4]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C03-5|C03-5]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C03-6|C03-6]])
3. Margin increases and a better Nigerian harvest → 35% fall in two weeks: Crowded long unwinds; he doubts margin forces exits on profitable longs ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C03-X2|C03-X2]])
- Evidence: COT report reading (host notes it is incomplete).
- Fails when: COT misses other funds' buying.

**Decision process**
- [research] Run unconditional backtests across markets, check stability, identify the reason for the mispricing, then find trend- or vol-based regimes where the structure is attractive.. Why: Avoid data-mined structures; need a causal reason for the edge ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C12-1|C12-1]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C09-4|C09-4]])
- [signal] A template maps the regime to one standard trade structure applied identically across markets; trend piece is systematic.. Why: No discretionary choice between put or put spread ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C12-2|C12-2]])
- [execution] Manual execution: legging in, time of day, sourcing liquidity.. Why: Options liquidity is sourced by hand ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C12-3|C12-3]])
- [universe] Only the ~10-15 most liquid commodity options markets with a storable underlying (copper, silver, gold, oil, some gas, grains; 7-8 live); cocoa, milling wheat, soybean oil excluded.. Why: Option liquidity falls sharply beyond the biggest markets; storability needed for the physical analogy ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C10-9|C10-9]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C11-1|C11-1]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C13-2|C13-2]])
- [portfolio] Enter cheap commodities with low-carry structure; convert to trend following after a significant rise.. Why: Capture early-rally skew at low cost, then full move with built-in exit ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C08-3|C08-3]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C08-2|C08-2]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C10-3|C10-3]])
- [risk] Bounded structure: sell moderate OTM options, buy deep OTM and ATM options; accepts losing about 25% of further declines.. Why: Upside covered, downside is a fraction ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C10-4|C10-4]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C09-1|C09-1]])
- [other] Target users: those with a long-term commodity bull view or business exposure who want pure commodity exposure at low cost, without the noise of commodity equities.. Why: Commodity equities carry hedging, diversification, passive-flow and equity-beta noise ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C13-1|C13-1]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C11-2|C11-2]])

**Evidence style:** Backtests across markets and cross-sectional stability, mechanism stories about who is on the other side of the trade (hedgers, institutions), analogies from VIX to commodities, historical anecdote (wheat in world wars); no live track record is given for the commodity structure.

**Views at the time**
- (2024-05-09) 0DTE option selling is a crowded trade with a hidden volatility-spike risk.. Reasoning: Popularity causes distortions; record covers only 2-3 calm years ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C01-1|C01-1]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C02-1|C02-1]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C02-X1|C02-X1]])
- (2024-05-09) Commodities, especially cheap ones such as Henry Hub natural gas, are attractive to hold long-term via the low-carry warehousing structure.. Reasoning: Structural demand themes plus low prices give upside asymmetry ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C08-X1|C08-X1]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C08-5|C08-5]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C05-6|C05-6]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C05-7|C05-7]])
- (2024-05-09) Cocoa's run was technical and positioning-driven and has reversed.. Reasoning: Managed money as large as commercials; margin hikes and better Nigerian supply ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C03-4|C03-4]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C03-X3|C03-X3]])

### Niels Kaastro Larsen (Host; veteran hedge fund manager and trend-following advocate)
Fingerprint: #approach/trend_following #approach/policy_reaction_central_banks #approach/position_sizing_vol_target #approach/positioning_crowding #approach/diversification_risk_parity
_Speaker note: Host; views stated mainly in the opening market commentary and in challenges to the guest._

**Worldview premises**
- Trend followers use volatility-scaled sizing and equal risk across a broad, fixed universe because they cannot predict where the next trend will be. _[institutional, stated; support: Own practice]_ ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C04-2|C04-2]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C10-X1|C10-X1]])
- The Fed commits to a narrative and may not follow data, as with 'transitory'. _[experience, stated; support: Observation of Fed communication]_ ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C02-3|C02-3]])
- Diverging central bank policy creates currency trends, from which trend followers benefit. _[empirical, stated; support: April 2024 yen and peso moves]_ ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C03-1|C03-1]])
- Trend following diversified stock and bond losses in April 2024. _[empirical, stated; support: Index returns for the month]_ ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C03-3|C03-3]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C03-2|C03-2]])

**Chain: Why trend followers were not the cocoa buyers**
1. Long-term signals began January 2023 and positions built slowly → Trend followers largely did not hold the parabolic phase: Time scale of the trend follower ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C04-1|C04-1]])
2. Vol rose in 2024 → Vol-scaled sizing cut positions, so they were net sellers: Risk targeting ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C04-2|C04-2]])
- Evidence: Reasoning from model rules; he does not follow COT.
- Fails when: Shorter-term trend followers behave differently.

**Decision process**
- [sizing] Same risk to all markets in a defined universe; scale down as volatility rises.. Why: Cannot predict where the next big trend is ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C10-X1|C10-X1]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C04-2|C04-2]])

**Evidence style:** Index data and model signal readings (trend barometer), general market commentary; challenges the guest with counterexamples (2020 oil, Russia/Ukraine).

**Views at the time**
- (2024-05-09) Trend models remained risk-on going into summer, though some managers trimmed after April reversals.. Reasoning: Signals still long; reversals in yen, cocoa, equities ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C02-5|C02-5]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C02-X2|C02-X2]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C03-X1|C03-X1]])
- (2024-05-09) Fed is boxed in by its rate-cut narrative; Powell sees no stagflation.. Reasoning: Hot inflation prints versus stated expectations ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C02-3|C02-3]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C02-4|C02-4]])
- (2024-05-09) Short-term CTAs led April (+2.4%), trend index +1.65%, SocGen CTA +1.82%, while MSCI World fell 3.85%.. Reasoning: Volatility helped short-term traders ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C03-2|C03-2]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C03-3|C03-3]])

### Disagreements
- **Who drove the cocoa spike and whether margin hikes mattered**: Harry Krishnan: Managed money as large as commercials suggests heavy trend-following piling in; margin effect debatable ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C03-4|C03-4]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C03-5|C03-5]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C03-X2|C03-X2]]); Niels Kaastro Larsen: Longer-term trend followers entered in January 2023 and were sellers in 2024; speculators, not trend followers, drove the end; margin hikes and Nigerian harvest plausible causes of the fall ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C04-1|C04-1]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C04-2|C04-2]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C04-4|C04-4]])
- **Does cheaper storage at low prices make warehousing attractive?**: Harry Krishnan: Storage and insurance costs fall and holders are implicitly paid to wait when prices are low ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C06-4|C06-4]]); Niels Kaastro Larsen: 2020 oil went negative because storage was scarce and costly, so the argument fails when storage is full ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C06-X2|C06-X2]])
- **Is the commodity super-cycle thesis reliable given the post-2022 sell-off?**: Harry Krishnan: Structural reasons (deglobalisation, green metals, weather, remilitarisation) plus wartime history support rallies; own the cheap ones cheaply ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C05-6|C05-6]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C06-1|C06-1]]); Niels Kaastro Larsen: The same reasons were cited after the Ukraine invasion and prices fully reverted for two years ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C06-X1|C06-X1]])
- **Is switching between value-style warehousing and trend following a timing problem?**: Niels Kaastro Larsen: Choosing the right investor type at the right time makes timing important ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C08-X2|C08-X2]]); Harry Krishnan: Not important; the switch is a rule: warehouse at low prices, trend follow after a significant rise ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C08-3|C08-3]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C08-2|C08-2]])

### Gaps and conflicts
- The 25% down-capture / 2/3 up-capture / 50% spike-capture figures are rules of thumb with no stated sample, costs or period. ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C09-1|C09-1]])
- The corn break-even figure refers to futures-only holding; the 5-10% break-even for the structure is an aim stated hypothetically, not a result (ledger correction applied). ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C11-3|C11-3]])
- The switch point to trend following ('significant rise') is not defined. ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C08-3|C08-3]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C08-X2|C08-X2]])
- The 0DTE claim that 'something is brewing' has no stated mechanism or timing; the guest also admits his own Sharpe above 1 is unreliable. ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C02-1|C02-1]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C01-4|C01-4]])
- Tension: the claim that moderate OTM calls are rich because hedgers sell futures into rallies mixes two different channels (futures selling versus option buying by end users). ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C07-6|C07-6]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C10-1|C10-1]])
- Uranium vehicles may not give true storage-equivalent exposure; hedging 'necessity' claim relies on backtests only. ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C11-X1|C11-X1]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C09-3|C09-3]])
- Execution is manual and the universe is only 7-8 markets, limiting scale and replicability. ([[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C12-3|C12-3]], [[MT036 - Commodity Super Cycle Inbound! - Systematic Investor 294#^MT036-C13-2|C13-2]])

### Forward-looking inputs (reader synthesis)
(reader) Guest's inputs: commodity price level (cheap vs history), shape of the futures curve (roll cost), call-versus-put skew and richness of moderate OTM calls, commercial hedger positioning, option liquidity, and for vol, the term-structure kink at the short end and open interest in 0DTE. Horizon is medium to long term (months to years) for commodities; 0DTE risk is unspecified. Host inputs: trend signals and the trend barometer, central bank divergence for FX trends.

### Reader inferences (not stated by the speakers)
- (reader) The structure is effectively a short-call-spread overlay on a long futures position, so its edge depends on moderate calls being rich relative to realized outcomes; if hedging demand shrinks, the edge goes with it.
- (reader) The hybrid (value then trend) approach inherits both strategies' regime risk; the claimed 'regime-conditional' templates were fitted on historical data without disclosed out-of-sample tests.
- (reader) The guest's own caution on 0DTE (short sample, no vol event) applies equally to commodity backtests that include few spike episodes.
- (reader) The host's disagreement on cocoa positioning shows that COT categories cannot reliably separate trend followers from other speculators.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 4 | intro/disclaimer; 0DTE options crowding, short-dated vol term structure, short sample backtests |
| C02 | 5 | no vol spike since 2022; 0DTE as hedge; Fed boxed in; Powell on stagflation; April trend positioning |
| C03 | 6 | central bank divergence and FX trends; April CTA index returns; cocoa managed money vs commercial positioning |
| C04 | 5 | cocoa: trend followers vol-scaling, COT limits, margin/harvest news; VIX/natgas analogy |
| C05 | 9 | contango and roll-down; rich OTM puts (S&P) and OTM calls (commodities); super-cycle drivers |
| C06 | 4 | history of wheat in wars; improved supply chains; case for owning cheap commodities; cost of physical carry |
| C07 | 8 | futures roll cost vs fixed warehouse cost; theta vs roll-down; hedgers sell rallies; virtual warehousing recipe |
| C08 | 5 | moderately vs extremely OTM options; warehousing plus trend following; natgas example; skewness at low prices |
| C09 | 4 | payoff profile rule of thumb; options driven by necessity; cross-commodity stability |
| C10 | 9 | airline hedging; regimes favouring the structure; vol cyclical vs price; equity index choppiness; universe limits |
| C11 | 3 | liquidity and storability drivers; ETF storage issues; corn break-even example |
| C12 | 3 | degree of systematization; backtest workflow; manual execution |
| C13 | 2 | target investors; commodity equities as noisy proxies; markets covered; outro |
| C14 | 0 | outro and rating plug; nothing actionable |

## Claims

### C01
- **Harry Krishnan** Selling zero-day-to-expiration straddles looks very attractive in recent backtests, but once such a trade becomes popular it tends to distort the market, so the strategy is vulnerable to crowding.  #mech/crowding_positioning _(time-bound view)_
  > I would be worried about this because as soon as this sort of idea catches catches fire or wildfire, uh there tend to be distortions in the market.
  indicator: 0DTE straddle selling · asset: equities · direction: short 0DTE straddles (caution) · conditions: Fragile once the idea is widely adopted · testable: partly - 0DTE data only exists for 2-3 years · confidence: medium
  ^MT036-C01-1
- **Harry Krishnan** Very short-dated equity protection is expensive relative to options 2-3 days out because portfolio managers with end-of-day risk limits buy zero-day options to block out risk, creating a spike at the short end of the vol term structure.  #mech/liquidity_flows
  > a strangely shaped term structure volatility where very short dated protection was quite expensive.
  indicator: implied vol term structure (0-3 days) · asset: equities · direction: short-dated vol rich versus 2-3 day vol · horizon: days · testable: yes - compare 0DTE implied vol with 2-3 day vol · confidence: medium
  ^MT036-C01-2
- **Harry Krishnan** 0DTE backtests rest on only two or three years of data, and interpolating the surface before then is unreliable because the dynamics were different, so conclusions are weak.  #mech/research_method
  > a lot of the data is restricted. It only goes back two or three years.
  asset: equities · horizon: years · conditions: Short sample, regime-specific · testable: yes - sample length is observable · confidence: high
  ^MT036-C01-3
- **Harry Krishnan** Selling 0DTE straddles every day produced a Sharpe ratio well above 1 to 1.5 in the 2022-2024 sample.  #mech/risk_premium _(time-bound view)_
  > You can generate a sharp ratio well over one or one and a half doing this.
  indicator: daily 0DTE straddle selling · asset: equities · direction: short straddles · horizon: days · conditions: Sample contains no major vol spike · testable: yes - Sharpe quoted from a short backtest · confidence: medium
  ^MT036-C01-4

### C02
- **Harry Krishnan** The good record of short-vol 0DTE strategies reflects a period without any major volatility spike; a spike would be the real test and he sees something brewing.  #mech/risk_management _(time-bound view)_
  > But we haven't seen a major event or major volatility spike in equity land or in equity index land since 2022.
  asset: equities · conditions: Strategy untested through a vol event · testable: partly - depends on future vol spike · confidence: medium
  ^MT036-C02-1
- **Harry Krishnan** Zero-day options are useful as a fixed-cost patch for tail risk in a portfolio, which is why demand and open interest at the short end soared.  #mech/risk_management
  > You could fill the holes in your portfolio by buying these things a fixed cost and blocking out extreme downside scenarios for a short time.
  indicator: 0DTE options open interest · asset: equities · direction: long 0DTE options as hedge · horizon: days · testable: partly - open interest data observable · confidence: medium
  ^MT036-C02-2
- **Niels Kaastro Larsen** The Fed has committed to a rate-cut-hope narrative and is struggling when each inflation print comes in hot, as it did with the transitory narrative, so policy may not follow the data.  #mech/policy_reaction _(time-bound view)_
  > they're putting themselves a little bit into a corner like they did with this transitory narrative
  indicator: Fed communication / inflation prints · asset: rates · horizon: months · testable: no - qualitative judgement · confidence: medium
  ^MT036-C02-3
- **Niels Kaastro Larsen** Powell argued there is no stagflation because growth is at least 3% and inflation below 3%.  #mech/policy_reaction _(time-bound view)_
  > by some measures at least the economy is growing at least 3% and inflation is below 3% so he didn't see stagflation anywhere.
  indicator: growth above 3%, inflation below 3% · asset: multi · horizon: months · testable: partly - thresholds are stated · confidence: medium
  ^MT036-C02-4
- **Niels Kaastro Larsen** In early May 2024 trend-following models were still risk-on despite April reversals, entering the summer months when decent moves sometimes occur.  #mech/cycle_persistence _(time-bound view)_
  > Trend following models still positioned kind of risk on when you look at the signals we have on at the moment.
  indicator: trend signals · asset: multi · direction: risk-on · horizon: months · conditions: Some trend followers cut risk after April reversals · testable: partly - positions observable but a point-in-time view · confidence: medium
  ^MT036-C02-5
- **Harry Krishnan** An equity bear market can unfold without a volatility spike (2022 was a down year but not very volatile), so long-volatility protection need not pay in a slow grinding decline and short-vol records since 2022 are untested.  #mech/risk_management _(added by opus cross-check)_
  > I know 2022 was a fairly bad year for international stocks but or international indices but um it wasn't a very volatile year.
  indicator: realized/implied equity index volatility in 2022 · asset: equities · direction: bear market with low vol: long vol underperforms · horizon: months · conditions: slow grinding declines · testable: yes - compare drawdown vs vol spike across bear markets · confidence: medium
  ^MT036-C02-X1
- **Niels Kaastro Larsen** The April 2024 reversals (yen intervention, sharp cocoa sell-off, equity weakness) led some trend followers to cut risk.  #mech/risk_management _(added by opus cross-check, time-bound view)_
  > April may also been a month where some trend followers took a little bit of risk off the table given
  indicator: trend follower exposure · asset: multi · direction: reduce gross exposure after reversals · horizon: weeks · conditions: sharp reversals in trending markets · testable: partly - exposure data of CTAs · confidence: low
  ^MT036-C02-X2

### C03
- **Niels Kaastro Larsen** Diverging central bank policies create trends in currencies, a sector that had not moved for a while, from which trend followers benefited (yen, Mexican peso).  #mech/policy_reaction _(time-bound view)_
  > Now the other thing that's happening at the moment of course which is interesting from a trend following perspective is this divergence in central bank policy.
  indicator: central bank policy divergence · asset: fx · direction: trend in FX (yen, MXN) · horizon: months · conditions: Fed vs ECB/BoJ differing paths · testable: yes - rate differentials and FX trend returns · confidence: medium
  ^MT036-C03-1
- **Niels Kaastro Larsen** Short-term CTAs gained most in April 2024 (+2.4%) from the volatility, ahead of the trend index (+1.65%) and SocGen CTA index (+1.82%).  #mech/cycle_persistence _(time-bound view)_
  > the winner this uh this month was uh the Short-Term Traders Index. They enjoyed some of that volatility
  indicator: SG Short-Term Traders Index · asset: multi · horizon: weeks · conditions: Volatile months · testable: yes - index returns · confidence: high
  ^MT036-C03-2
- **Niels Kaastro Larsen** In April 2024 CTA indices rose while MSCI World fell 3.85% and world government bonds fell 1.77%, showing trend following diversified stock and bond losses.  #mech/risk_management _(time-bound view)_
  > uh MSCI World down 3.85% still up 4 and 1/4 for the year.
  indicator: SocGen CTA Index, MSCI World, world govt bonds · asset: multi · horizon: weeks · conditions: Single month · testable: yes - monthly returns · confidence: high
  ^MT036-C03-3
- **Harry Krishnan** In cocoa managed-money open interest was as large as commercial hedging, which is unusual and suggests a major piling into the trend trade.  #mech/crowding_positioning _(time-bound view)_
  > cocoa seemed to be one of the markets where managed money was as large in terms of open interest um as commercial hedging activity was, both for producers and end users.
  indicator: CFTC Commitments of Traders: managed money vs commercial open interest · asset: commodities · horizon: months · conditions: Illiquid market with small open interest · testable: yes - COT data · confidence: medium
  ^MT036-C03-4
- **Harry Krishnan** Managed-money positioning in the COT report typically correlates with trend, so it can be used as a proxy for trend-following crowding.  #mech/crowding_positioning
  > because managed money typically correlates to trend in most markets.
  indicator: COT managed money · asset: commodities · horizon: months · testable: yes - correlate managed-money positions with trend signals · confidence: medium
  ^MT036-C03-5
- **Harry Krishnan** Cocoa had long untrended periods and is not very liquid, so some trend followers may not have included it in their basket and missed the later trend.  #mech/structural_shift
  > And cocoa was a phenomenal market in so many ways. One is that it had long periods where it hadn't trended.
  indicator: cocoa · asset: commodities · horizon: years · conditions: Illiquid, low-open-interest markets · testable: partly - depends on each manager's universe · confidence: medium
  ^MT036-C03-6
- **Niels Kaastro Larsen** The host's trend barometer (share of markets trending) read 45 at end-April 2024, a neutral reading for trend-following conditions.  #mech/slow_reaction _(added by opus cross-check, time-bound view)_
  > at the end of April my trend barometer finished at 45 which is a neutral level
  indicator: Niels' trend barometer (0-100) · asset: multi · direction: neutral trend environment · horizon: weeks · testable: partly - barometer definition not given · confidence: medium
  ^MT036-C03-X1
- **Harry Krishnan** Exchange margin hikes may matter less for forcing liquidation than assumed, because holders of heavily profitable positions are not desperate to exit quickly.  #mech/liquidity_flows _(added by opus cross-check)_
  > One can debate to what extent this is a factor because if you have a trade that's heavily on side you're not desperate to get out too quickly
  indicator: exchange margin requirements · asset: commodities · direction: margin hikes have limited forced-selling effect on winning longs · horizon: weeks · conditions: positions deep in profit · testable: partly - margin changes vs subsequent price/positioning · confidence: low
  ^MT036-C03-X2
- **Harry Krishnan** The cocoa rally began with a fundamental trigger (poor West African production) and then became largely a technical, positioning-driven move.  #mech/overshoot _(added by opus cross-check, time-bound view)_
  > I presume it was very to a very large extent a technical affair once the production poor production numbers came out from Africa
  indicator: cocoa price, production data · asset: commodities · direction: fundamental shock then technical extension · horizon: months · testable: partly - positioning vs fundamentals timing · confidence: low
  ^MT036-C03-X3

### C04
- **Niels Kaastro Larsen** Longer-term trend followers got their cocoa entry signals in January 2023 and built positions slowly, so the parabolic phase in 2024 was driven by other speculators rather than by trend followers.  #mech/crowding_positioning _(time-bound view)_
  > I don't think the trend followers interestingly enough really had much to do with with cocoa once it became a parabolic trade.
  indicator: cocoa trend signals (started Jan 2023) · asset: commodities · horizon: months · conditions: Depends on time scale of the trend follower · testable: partly - requires CTA position data · confidence: medium
  ^MT036-C04-1
- **Niels Kaastro Larsen** Volatility-scaled position sizing makes trend followers reduce positions as volatility rises, so they were net sellers of cocoa during its 2024 spike.  #mech/risk_management
  > trend followers in general who uses dynamic position sizing will have been selling cocoa all of this year because of the increased volatility.
  indicator: volatility-scaled position size · asset: commodities · direction: reduce size as vol rises · horizon: weeks · conditions: Dynamic (vol-targeted) sizing · testable: yes - rule is mechanical · confidence: high
  ^MT036-C04-2
- **Niels Kaastro Larsen** The COT managed-money category misses other funds' buying (it is blurred), so it is an incomplete measure of who is long.  #mech/research_method
  > if another hedge fund bought those contracts, you wouldn't see it, right?
  indicator: COT managed money · asset: commodities · testable: yes - known data limitation · confidence: medium
  ^MT036-C04-3
- **Niels Kaastro Larsen** Cocoa fell 35% in two weeks after exchange margin increases and news of a better Nigerian harvest, ending the parabolic run.  #mech/liquidity_flows _(time-bound view)_
  > there was also news out that Nigeria actually has is going to come out out with a better harvest.
  indicator: cocoa price, exchange margins · asset: commodities · direction: cocoa down · horizon: weeks · conditions: Crowded long positioning · testable: partly - margin changes and supply news are datable · confidence: low
  ^MT036-C04-4
- **Harry Krishnan** VIX and natural gas/electricity are analogous because neither can be easily stored or replicated, giving futures term structures and option dynamics that look alike.  #mech/structural_shift
  > It's hard to replicate the VIX. It's very hard to store natural gas unless you liquefy it.
  indicator: VIX, natural gas, electricity futures · asset: multi · conditions: Non-storable underlyings · testable: yes - compare term structures and option behaviour · confidence: medium
  ^MT036-C04-5
- **Harry Krishnan** Investor demand for long-volatility (and similarly trend-following) strategies is highly cyclical: inflows surge after bad markets and dry up in long calm periods.  #mech/behavioral _(added by opus cross-check)_
  > it's just that that's a highly cyclical business in terms of interest. When things are going very bad, I tend to get tons of requests
  indicator: fund flows / allocation requests to long vol · asset: multi · direction: inflows after crises, outflows in calm · horizon: years · testable: partly - flows into tail-risk/CTA funds vs prior drawdowns · confidence: medium
  ^MT036-C04-X1

### C05
- **Harry Krishnan** Non-storable markets (VIX, natural gas, electricity) show severe contango, so long positions face heavy roll-down costs.  #mech/risk_premium
  > So, you get severe contango in the term structure where the front month trades at a significant discount to the further out months.
  indicator: futures term structure / roll yield · asset: commodities · direction: long futures bleed · horizon: months · conditions: Storage-constrained markets · testable: yes - roll yield measurable · confidence: high
  ^MT036-C05-1
- **Harry Krishnan** Because of contango, longer-term trend followers are short most of the time in these markets and then get hurt by sporadic mega spikes from supply shortages or risk-off events.  #mech/cycle_persistence
  > So, trend longer-term trend followers, let's say, are typically short most of the time these markets.
  indicator: trend signal in VIX / natural gas · asset: multi · direction: short most of the time, losses in spikes · horizon: months · testable: yes - backtest trend on these markets · confidence: medium
  ^MT036-C05-2
- **Harry Krishnan** The same option trades that work in VIX also work in the storage-constrained commodities, found by transferring structures across analogous markets in a backtest.  #mech/research_method
  > And so, I put all of this stuff into into my backtesting engine. And I found that the same sorts of trades seem to be working.
  asset: multi · testable: yes - backtest · confidence: medium
  ^MT036-C05-3
- **Harry Krishnan** Three-month 10%-out-of-the-money S&P puts are expensive because institutions buy them for hedging and collared products, so hedging strategies can be built around selling them.  #mech/liquidity_flows
  > So, let's say 3-month to maturity S&P puts that are 10% out of the money tend to be quite pricey because institutions like to buy them.
  indicator: 3-month 10% OTM S&P put implied vol · asset: equities · direction: sell moderately OTM puts, buy far OTM · horizon: months · testable: yes - option price vs realised · confidence: high
  ^MT036-C05-4
- **Harry Krishnan** In oil, corn and soybeans, out-of-the-money calls are rich, the mirror image of equity puts, probably because hedgers buy them.  #mech/liquidity_flows
  > I found that in the commodities markets such as oil, or corn, soybeans, and so on, out of the money call options, which are trading on the other side of the distribution, tend to be expensive.
  indicator: OTM call implied vol in oil, corn, soybeans · asset: commodities · direction: sell moderately OTM calls · horizon: months · testable: yes - backtest of call selling · confidence: high
  ^MT036-C05-5
- **Harry Krishnan** Deglobalization and food and energy security concerns require more domestic infrastructure and add frictions to commodity trade, which could push prices higher.  #mech/structural_shift _(time-bound view)_
  > uh deglobalization seems to be coming into vogue. Where countries are worried about food security, about energy security, about being able to produce what they need internally.
  asset: commodities · direction: commodities up · horizon: years · testable: no - narrative · confidence: medium
  ^MT036-C05-6
- **Harry Krishnan** The green transition requires large amounts of industrial metals such as copper (e.g. rebuilding the grid), supporting copper demand.  #mech/structural_shift _(time-bound view)_
  > Which, as it progresses at whatever pace, will require large amounts industrial metals such as copper.
  indicator: copper · asset: commodities · direction: copper up · horizon: years · testable: no - narrative · confidence: medium
  ^MT036-C05-7
- **Harry Krishnan** Greater extremes in temperature and precipitation (e.g. Brazil deforestation) destabilise grain and other commodity prices and should raise price volatility.  #mech/structural_shift _(time-bound view)_
  > Uh we're also in an environment where weather volatility seems to be picking up.
  indicator: weather volatility · asset: commodities · direction: higher commodity volatility · horizon: years · testable: partly - weather extremes observable · confidence: low
  ^MT036-C05-8
- **Harry Krishnan** Remilitarization raises demand for metals and energy.  #mech/structural_shift _(time-bound view)_
  > Where countries are trying to, God forbid, remilitarize, which requires a lot more metal and energy uh inputs, or requires a lot more of those.
  asset: commodities · direction: metals and energy up · horizon: years · testable: no - narrative · confidence: low
  ^MT036-C05-9

### C06
- **Harry Krishnan** In both world wars wheat prices rose three to four times in sustained moves, an analogy for a geopolitically driven commodity rally.  #mech/structural_shift
  > in World War I and World War II, the price of wheat trebled.
  indicator: wheat price · asset: commodities · direction: wheat up in wartime · horizon: years · testable: partly - historical data · confidence: medium
  ^MT036-C06-1
- **Harry Krishnan** Better technology and supply chains limit how far grains can rally compared with the wars, putting downward pressure on grain prices at the top.  #mech/structural_shift
  > I do accept that technology and sort of the improved supply chains from 50 years ago or 75 years ago are creating a bit of a downward pressure on grains, at least at the top for the time being.
  indicator: grain prices · asset: commodities · horizon: years · testable: no - qualitative · confidence: medium
  ^MT036-C06-2
- **Harry Krishnan** Owning depressed commodities with low carry and high participation if prices rise is valuable; virtual warehousing means buying and holding cheap commodities through financial instruments with low bleed.  #mech/risk_premium
  > being able to own stuff that's cheap seems to be immensely valuable.
  asset: commodities · direction: long cheap commodities · horizon: years · conditions: Commodity prices depressed · testable: partly - define cheap and test · confidence: medium
  ^MT036-C06-3
- **Harry Krishnan** Physical storage costs (insurance, depreciation) fall and sellers have less incentive to sell when prices are low, so holders are implicitly paid to wait.  #mech/behavioral
  > there's less incentive for me, let's say if I'm a farmer and corn's at $3 to sell corn into the market to pay off my loan
  asset: commodities · horizon: months · conditions: Low commodity prices · testable: partly - storage cost proxies · confidence: medium
  ^MT036-C06-4
- **Niels Kaastro Larsen** Caveat to the super-cycle thesis: the commodity spike after Russia's invasion of Ukraine fully reverted and prices sold off for two years even though the cited structural reasons were unchanged.  #mech/overshoot _(added by opus cross-check, time-bound view)_
  > But, to many people's surprise, actually They came right back down. They They've been selling off for 2 years.
  indicator: commodity prices after 2022 spike · asset: commodities · direction: geopolitical spikes can fully reverse · horizon: years · conditions: structural narrative present but no lasting rally · testable: yes - post-shock commodity returns · confidence: medium
  ^MT036-C06-X1
- **Niels Kaastro Larsen** Challenge to the claim that storage gets cheaper as prices fall: in 2020 oil went negative because storage became scarce and costly, so the argument fails when storage capacity is full.  #mech/new _(added by opus cross-check)_
  > We saw a couple of years ago that prices moved down in oil. They actually went negative. But, that was not a time where storage became cheaper, so to speak.
  indicator: WTI front-month price, storage capacity · asset: commodities · direction: low prices with full storage: carry cost rises, not falls · horizon: days · conditions: storage capacity constrained · testable: yes - storage utilisation vs curve contango · confidence: medium
  ^MT036-C06-X2

### C07
- **Harry Krishnan** In commodity futures the cost of buying and rolling a long position rises sharply as price falls because of curve effects, unlike fixed warehouse rental, so a physical holder and a futures holder are treated asymmetrically.  #mech/risk_premium
  > on average the cost of buying and rolling a long position goes up quite dramatically as the price goes down.
  indicator: futures curve roll cost vs price level · asset: commodities · direction: long futures bleed more at low prices · horizon: months · testable: yes - roll yield vs price level · confidence: high
  ^MT036-C07-1
- **Harry Krishnan** In hedging, forward-curve roll-down can pay for option time decay (rho pays for theta) when rates are below the dividend yield.  #mech/risk_management
  > for long dated options you can sometimes pay for time decay using forward curve dynamics.
  indicator: forward curve roll vs theta · asset: equities · horizon: months · conditions: Rates below S&P dividend yield · testable: yes - carry arithmetic · confidence: high
  ^MT036-C07-2
- **Harry Krishnan** In commodities the structure is reversed: option time decay (theta) earned from selling rich options pays for the futures roll-down.  #mech/risk_management
  > In the virtual warehousing world, it's the problem is similar, but almost the other way around. You pay for roll down with theta.
  indicator: option theta vs futures roll-down · asset: commodities · horizon: months · testable: yes - carry arithmetic · confidence: high
  ^MT036-C07-3
- **Harry Krishnan** When corn rises, producers, storage and elevator operators sell futures to lock in gains; the same holds in copper, because commercial hedgers care about staying in business more than the right tail.  #mech/crowding_positioning
  > are highly incentivized to sell futures to lock in gains.
  indicator: commercial hedger net short futures · asset: commodities · direction: commercial selling into rallies · horizon: months · conditions: Rising prices · testable: yes - COT hedger positions · confidence: high
  ^MT036-C07-4
- **Harry Krishnan** Commercial hedging dampens rallies so moderate uptrends rarely go ballistic.  #mech/liquidity_flows
  > most uptrends do not accelerate in markets where commercial hedgers are selling into rallies.
  asset: commodities · horizon: months · conditions: Markets with active commercial hedging · testable: yes - trend acceleration frequency · confidence: medium
  ^MT036-C07-5
- **Harry Krishnan** Moderately out-of-the-money calls are overpriced because hedgers sell futures into rallies, which can be shown by backtests.  #mech/risk_premium
  > somewhat out of the money call options which are providing insurance against moderate outcomes moderate increases tend to be overpriced.
  indicator: moderately OTM call options · asset: commodities · direction: sell moderately OTM calls · horizon: months · testable: yes - backtest · confidence: high
  ^MT036-C07-6
- **Harry Krishnan** Selling moderately OTM calls while buying further OTM calls and covering the extreme is attractive and funds the carry of long futures.  #mech/risk_management
  > being a seller of these moderately out of the money options can be very profitable if you can buy other options around it.
  indicator: call spread / call overwriting structure · asset: commodities · direction: short moderate OTM calls, long far OTM calls · horizon: months · conditions: Need liquid options · testable: yes - backtest · confidence: high
  ^MT036-C07-7
- **Harry Krishnan** Virtual warehousing buys futures at the cheapest curve points and funds roll costs from rich option premium so that holding a flat market costs close to zero.  #mech/risk_management
  > So, the virtual warehousing idea is basically a combination of buying futures, targeting cheaper points on the curve to manage roll costs
  indicator: futures + option combination · asset: commodities · direction: long commodity with low carry · horizon: years · conditions: Depressed commodity prices · testable: yes - backtest · confidence: medium
  ^MT036-C07-8

### C08
- **Harry Krishnan** Moderately OTM options are rich while extremely OTM options are not, which allows selling the former and buying the latter.  #mech/risk_premium
  > There are a number of reasons why out of the money options are expensive but but extremely out of the money options are not
  indicator: OTM option skew by strike distance · asset: commodities · horizon: months · testable: yes - strike-level option pricing · confidence: medium
  ^MT036-C08-1
- **Harry Krishnan** Virtual warehousing complements trend following: warehouse early in the move while the price is low, then switch to trend following.  #mech/cycle_persistence
  > Yes. Yes. And to be fair, the warehousing works well in conjunction with trend following.
  asset: commodities · horizon: months · testable: partly - requires a switching rule · confidence: medium
  ^MT036-C08-2
- **Harry Krishnan** Use warehousing at low prices (avoiding a short trend position and roll costs), then convert to trend following once price rises to capture the full move.  #mech/policy_reaction
  > Until the price did go up significantly, at which point I would turn into more of a trend follower.
  indicator: price rise from a cheap level · asset: commodities · direction: long, converting to trend following · horizon: months · conditions: Natural gas example, as of May 2024 · testable: partly - rule for switch not specified · confidence: medium
  ^MT036-C08-3
- **Harry Krishnan** Trend following has built-in risk control: the position is held while the trend lasts and exits when it breaks.  #mech/risk_management
  > trend following has the marvelous quality of having a risk control mechanism built into it.
  indicator: trend break exit · asset: multi · testable: yes · confidence: high
  ^MT036-C08-4
- **Harry Krishnan** At very low prices (e.g. gas at $1.50) the payoff is asymmetric to the upside, while at $6-7 the risk becomes symmetric, so the early part of a rally has the best skew.  #mech/risk_premium _(time-bound view)_
  > gas is at a buck 50 uh the the risk of it's going down a dollar are far lower than the odds of it's going up by an equivalent amount.
  indicator: price level vs history · asset: commodities · direction: long at low prices · horizon: months · conditions: Price near multi-year lows · testable: yes - conditional return distribution by price level · confidence: medium
  ^MT036-C08-5
- **Harry Krishnan** As of May 2024 Henry Hub natural gas was cheap; a trend follower would be short, but a long-term bull should warehouse it via the futures-plus-options structure rather than pay roll costs or be short.  #mech/structural_shift _(added by opus cross-check, time-bound view)_
  > Henry Hub natural gas is quite cheap. I would want to be a virtual warehouser in the early stages because I don't want to be short.
  indicator: Henry Hub natural gas price · asset: commodities · direction: long gas via low-carry structure · horizon: months · conditions: cheap price, long-term bullish view · testable: partly - single view · confidence: medium
  ^MT036-C08-X1
- **Niels Kaastro Larsen** Host challenge: switching from value-style warehousing to trend following implies regime timing risk, and every option structure has a cost somewhere (Harry agrees there is always a cost).  #mech/research_method _(added by opus cross-check)_
  > it sounds like you want to be a value uh investor when it's good to be a value investor and a trend follower when it's good to be a trend follower.
  asset: commodities · conditions: switch rule must be specified ex ante · testable: yes - test switching rule out of sample · confidence: medium
  ^MT036-C08-X2

### C09
- **Harry Krishnan** The warehousing structure loses ~25% of further declines and captures ~2/3 of rallies (only ~50% of a one-day spike), a rule-of-thumb payoff.  #mech/risk_management
  > if the price of a commodity is low and it drops further, I'll lose about 25% of the down move. If the price rallies, I'll capture about 2/3 of the upside.
  indicator: structure payoff profile · asset: commodities · horizon: months · conditions: Low-price starting point · testable: yes - backtest payoff ratios · confidence: medium
  ^MT036-C09-1
- **Harry Krishnan** If spot is flat the long futures drift down but the combined structure stays flat because option premium offsets roll costs.  #mech/risk_management
  > So, if the spot price flatlines, the futures will typically drift down, but I won't drift down.
  asset: commodities · horizon: months · conditions: Flat market · testable: yes · confidence: medium
  ^MT036-C09-2
- **Harry Krishnan** Commodity option prices reflect hedging necessity, creating systematic mispricing that arbitrageurs do not fully remove.  #mech/liquidity_flows
  > commodity options markets are driven by necessity as much as they are by arbitrage type ideas.
  asset: commodities · testable: partly · confidence: medium
  ^MT036-C09-3
- **Harry Krishnan** The same structures work across nearly all storable commodities, giving cross-sectional stability.  #mech/research_method
  > for all storable commodities or for nearly all storable commodities, the um same structures work.
  asset: commodities · conditions: Storable commodities only · testable: yes - cross-sectional backtest · confidence: high
  ^MT036-C09-4
- **Harry Krishnan** Option arbitrageurs in commodities are unpredictable in which side they take (short, long, or relative value), so their presence does not reliably remove the hedging-driven mispricing.  #mech/new _(added by map cross-check)_
  > you don't know which side of the game they're going to be on at any given point in time.
  indicator: commodity option mispricing · asset: commodities · direction: none · conditions: Commodity option markets driven by hedging necessity · testable: partly - arbitrageur positioning not observable · confidence: medium
  ^MT036-C09-R1

### C10
- **Harry Krishnan** End users such as airlines are credit-constrained and hedge simply by buying call options, which creates structural demand for OTM calls.  #mech/liquidity_flows
  > Airlines are not that solvent some of the time. It's not been the greatest business to run. So, they're not going to be doing complicated structures that have open-ended risk.
  indicator: airline hedging in oil · asset: commodities · testable: partly - hedger behaviour · confidence: medium
  ^MT036-C10-1
- **Harry Krishnan** The structure works best when commodity prices are low but demand for OTM insurance is high.  #mech/crowding_positioning
  > markets where the price is low, but the demand for out-of-the-money insurance is high. That's a good regime for me.
  indicator: price level and OTM call demand · asset: commodities · horizon: months · testable: yes - regime backtest · confidence: medium
  ^MT036-C10-2
- **Harry Krishnan** As prices rise and hedging is monetised, the relative-value structures become less attractive, which is where trend following takes over.  #mech/cycle_persistence
  > And the attractiveness of some of these structures decreases as prices rise and the hedging has already occurred or is being monetized.
  asset: commodities · horizon: months · conditions: Rising prices · testable: yes · confidence: medium
  ^MT036-C10-3
- **Harry Krishnan** The structure is bounded: sell moderate OTM options, buy deep OTM and at-the-money options so all upside is covered.  #mech/risk_management
  > Uh please remember, though, that I'm covering all the upside. I'm not just selling out-of-the-money options.
  asset: commodities · testable: yes · confidence: high
  ^MT036-C10-4
- **Harry Krishnan** In hedging, buy volatility when cheap and switch to trend following for downside protection once vol is expensive.  #mech/risk_management
  > As a hedger, my idea is to buy volatility when it's cheap, and then turn it into a trend follower if I have to provide protection on the way down once volatility has become rich.
  indicator: implied volatility level · asset: equities · direction: long vol when cheap, then trend following · horizon: months · testable: partly · confidence: medium
  ^MT036-C10-5
- **Harry Krishnan** Volatility is cyclical (mean-reverting) while prices trend, so insurance is overpaid when vol is high and selling into the decline gives the same protection.  #mech/cycle_persistence
  > volatility tends to be more cyclical than price. Prices tend to trend a lot more.
  indicator: volatility vs price · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT036-C10-6
- **Harry Krishnan** Pure momentum is harder in equity indices because declines are choppy and rallies more stable.  #mech/cycle_persistence
  > the signal-to-noise ratio in bear markets tends to be lower than in bull markets because declining markets for equities tend to be choppy.
  indicator: S&P, Nasdaq trend · asset: equities · horizon: months · conditions: Bear markets · testable: yes · confidence: medium
  ^MT036-C10-7
- **Harry Krishnan** Every option structure encodes a regime bet, so participation should be regime-based.  #mech/risk_management
  > And as soon as you put an options trade on, you've already decided what regime you're hoping for and what you don't want because there's no structure that will do well in every case.
  asset: multi · testable: partly · confidence: high
  ^MT036-C10-8
- **Harry Krishnan** Option liquidity drops sharply beyond the ten biggest commodity markets (cocoa unplayable), restricting the universe to about 10-15 markets.  #mech/liquidity_flows
  > the options liquidity is sharply decreasing once you go beyond biggest 10 commodities markets, let's say.
  indicator: option liquidity · asset: commodities · testable: yes · confidence: high
  ^MT036-C10-9
- **Niels Kaastro Larsen** Trend followers allocate equal risk across a fixed, broad universe because they cannot predict where the next big trend will appear.  #mech/risk_management _(added by opus cross-check)_
  > We apply the same risk to all markets. We're we don't know where the next big trend is going to be.
  asset: multi · direction: equal risk per market · testable: yes - equal-risk vs concentrated universes · confidence: high
  ^MT036-C10-X1

### C11
- **Harry Krishnan** The edge relies on liquid options and storable underlyings, so it does not extend to weather derivatives.  #mech/structural_shift
  > liquidity and the ability to store the commodity are two drivers in this whole thing.
  asset: commodities · conditions: Storable, liquid markets · testable: yes · confidence: high
  ^MT036-C11-1
- **Harry Krishnan** Physically backed ETFs (gold) give real storage but blended futures ETFs lose it through roll costs, leaving a gap the strategy fills.  #mech/structural_shift
  > things like the two cream ETFs, which are blends of futures, and you've lost the virtual storage concept immediately.
  indicator: commodity ETFs · asset: commodities · testable: partly · confidence: medium
  ^MT036-C11-2
- **Harry Krishnan** Holding $3 corn via futures needs about $4 to break even over 12 months (30% roll cost), versus 5-10% for virtual warehousing.  #mech/risk_premium
  > your break-even for corn has historically been $4 over 12-month horizon. It costs a dollar to buy and roll the futures at least from 2000 to the present.
  indicator: corn futures roll cost · asset: commodities · horizon: years · conditions: Low price · testable: yes - 2000 to present roll cost · confidence: high
  **Correction (cross-check):** Overstates: the speaker did not say virtual warehousing achieves a 5-10% break-even; he said it would be desirable 'if you can turn that into a 5% break-even, 10% break-even'. → Holding $3 corn via futures has historically needed about $4 to break even over 12 months (about $1 or ~30% roll cost, 2000-present); the aim of virtual warehousing is to cut that break-even to something like 5-10% so a position can be held far longer.
  ^MT036-C11-3
- **Harry Krishnan** Physically backed uranium vehicles may not give true storage-equivalent exposure because there may be no free open market in which to sell the units.  #mech/liquidity_flows _(added by opus cross-check)_
  > one can argue as to whether there is any freely available open market in which to sell these claims
  indicator: physically backed uranium trusts/ETFs · asset: commodities · conditions: illiquid secondary market for units · testable: partly - premium/discount and liquidity of units · confidence: low
  ^MT036-C11-X1

### C12
- **Harry Krishnan** The research process is: unconditional backtests across markets, check stability, identify the reason for the mispricing, then find regimes that favour the structure.  #mech/research_method
  > come up with unconditional back tests across markets, see how stable the ideas are, identify the possible reasons for the mispricings in the structures that work
  asset: multi · testable: yes · confidence: high
  ^MT036-C12-1
- **Harry Krishnan** The strategy is systematic: each regime (trend- or vol-based) maps onto a standard trade structure.  #mech/risk_management
  > templates which maps a state of the world onto a trade.
  indicator: trend and volatility regime · asset: multi · testable: yes · confidence: high
  ^MT036-C12-2
- **Harry Krishnan** Execution is manual: legging into trades, choosing time of day and sourcing liquidity.  #mech/risk_management
  > there is discretion in terms of legging up the trade.
  asset: multi · horizon: days · testable: no - discretionary · confidence: high
  ^MT036-C12-3

### C13
- **Harry Krishnan** Commodity equities are noisy proxies for commodity prices (hedging, diversification, passive flows, equity beta).  #mech/structural_shift
  > the sensitivity of commodity shares to say the S&P 500, or the level of diversification of certain businesses that cloud the issue of whether they're really gaining exposure to what they want.
  indicator: commodity company shares · asset: equities · testable: partly · confidence: medium
  ^MT036-C13-1
- **Harry Krishnan** Applied to copper, silver, gold, oil, some gas and grains; gas is limited because of poor storability (seven or eight markets running).  #mech/structural_shift
  > Uh oil and to a lesser extent gas because of its lack of storage.
  asset: commodities · testable: yes · confidence: high
  ^MT036-C13-2

