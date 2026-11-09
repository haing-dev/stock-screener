# U04: Nick Baltas (Goldman Sachs QIS; Imperial) - judgement brief (Fable, 2026-11-09)

Inputs: foundation/packs/U04.json (synthesis over 18 Systematic Investor transcripts, 2024-05-10 to 2026-09-24; 553
claims, 536 quotes script-checked "exact", 17 reader/R claims unchecked; 22 corrections, six moving a claim from Baltas
to Niels: MT087-C04-1, MT116-C04-1, MT116-C07-2, MT116-C11-1, MT117-C05-2, MT216-C05-3, one the other way,
MT204-C15-2). Caption names vary ("Balters", "Bolters", "Palus"); MT009 ("Palus") carries the most identity doubt.
Repo /home/claude/stock-screener read only. SHOW = a test with numbers (his own or a paper's, described, exhibits never
shown on air); ASSERT = stated, no test; (reader) = my inference. Most numbers sit in the extracted claim text, not in
the short quote (section 8). No code was run; the 2011-2026 holdout was not touched.

## 1. Verdict

1. Core logic: trend is a permanent, never-timed harvest of slow information digestion and volatility clustering,
   taken on 50-100 markets chosen for diversification and cost rather than past contribution, every exposure scaled by
   volatility and correlation; its known cost is the V-shaped reversal, which no speed escapes and which hits the
   middle speeds twice; that cost is diversified with beta-neutral carry, skew reversion and vol selling, not repaired
   by refitting; and whether a return survives crowding depends on its type: risk-sharing premia persist, behavioural
   premia may gain from early crowding, flow imbalances erode (MT116-C02-1, MT116-C14-2, MT173-C03-3, MT009-C07-4,
   MT087-C05-1, MT200-C05-1, MT131-C09-1, MT204-C14-3, MT204-C15-X1).
2. Grounding: almost entirely assertion plus close readings of other people's papers (Quantica, Man Group, ATP, AQR,
   Graham, Harvey et al.); his own evidence is desk material (25-year speed-by-universe rankings, attribution, a trend
   barometer) described, never shown, without the top-bottom spread he himself asks for (MT116-C08-X2). He flags
   hindsight and data mining in his own suggestions (MT087-C08-X1, MT116-C06-R1, MT200-C07-1): directions credible,
   sizes unknown. He sells QIS indices in trend, carry, curve carry and vol selling: a conflict on crowding and curve
   carry.
3. Our book already holds his core: vol-scaled multi-speed trend, breadth without performance screening, no timing,
   no refit after an episode, carry half cross-sectional, fixed shares (config.py:19, 22, 62; book.py:131-132;
   TESTING_PROTOCOL.md:29-32). We differ in static equal class risk, sign rather than sigmoid signals, raw rather than
   z-scored carry, no calendar-spread curve carry, and in executing at the month-end turn he says to avoid.
4. Our own trial log confirms his central research claim: signal forms are transformations of each other and the
   gains sit in construction and risk (MT131-C07-4); our two adoptions were construction (hybrid vol +0.12, shares
   +0.11, CHANGES.md:91-92), while all eight signal variants failed (continuous, spot-only and two slower trends, a
   credit-only risk theme, bond value composite, FX value skip, duration-scaled carry: CHANGES.md:15, 18, 22, 24;
   protocol_batch1.md:9-11), as did one structure (E1) and one market (S1) variant (protocol_batch1.md:7-8).
5. Action: no new Holm slot. Two zero-slot diagnostics (turn-of-month decomposition of our one-day delay loss, which
   his rebalancing-flow mechanism may explain; aggregate trendiness against forward return and realised risk), one
   sharpening of the already-planned Batch 2 commodity-carry challenger into his calendar-spread form, one skew
   conditioning folded into U02-T1, and a "no test" list.

## 2. Logical foundation

| Premise | Type | Source |
|---|---|---|
| P1 Information is digested slowly, so a continued move is the signal; it now arrives in bursts, making V-shapes more frequent (open whether this is a regime) | behavioural, ASSERT | MT116-C02-1, MT039-C04-2, MT087-C05-2 |
| P2 Trend can pay without return autocorrelation: volatility clusters, big moves follow big moves with skew; conditional on a drawdown past a threshold the trend payoff is positive even for iid returns (ATP) | theoretical, SHOWN as mathematics | MT116-C14-2, MT117-C12-1, MT116-C15-1 |
| P3 Disputed fundamentals make price moves informative and trends continue; certainty (a Fed put, consensus valuation) makes shocks revert | behavioural, ASSERT | MT117-C11-2, MT216-C13-2, MT167-C17-1 |
| P4 Risk is forecastable, returns are not; even the current state is hard to identify; any fixed weight embeds a return forecast and a value bet | statistical | MT200-C09-2, MT009-C03-1, MT117-C08-2, C08-3 |
| P5 Allocations are set by constraints (tracking error, career risk, leverage limits); many premia exist because of them | institutional | MT087-C11-1, C12-1, MT200-C15-1, MT174-C11-1 |
| P6 Premium taxonomy: risk-sharing premia (vol selling, curve carry) survive crowding; behavioural premia (trend) may gain from early crowding; allocation imbalances (roll congestion) erode | economic, ASSERT | MT204-C14-3, C15-1, MT130-C07-1, C07-3, MT204-C15-2 as corrected |
| P7 Loss aversion drives allocators; paying for downside protection can be rational; short-term loss mitigation lifts compounding | behavioural | MT087-C09-1, MT173-C12-1, MT131-C13-2, C14-4 |

Chains (each arrow a step he states):

- Payoff and the V: P1 + P2 -> hold the trend, vol-scaled -> sustained moves (2002, 2008, 2022) pay through whichever
  class trends (MT039-C17-1, MT200-C08-2 as corrected) -> nothing is earned in the three months before an equity peak
  or the first weeks after (MT039-C17-3, C17-4) -> in a sharp fall and rebound signals need days to flip: short near
  the trough, re-added into the recovery; fast loses less down but recovers less, slow rides the whole V, the middle
  (3-6 months) is caught both ways (MT039-C08-3, MT087-C07-3, MT200-C05-1, MT134-C03-3) -> no speed escapes; the
  result depends on whether the break was a true or false positive (MT099-C10-3) -> so choose speed and universe by
  objective, core liquid markets for crisis alpha, a broad set for Sharpe (MT130-C12-2, MT167-C12-1, MT167-C11-3),
  never by the last episode (MT116-C08-1, MT002-C02-5b).
- Sizing: P4 -> scale each exposure by volatility continuously, never by VIX triggers (MT009-C07-4, C07-2) -> and by
  correlation, since vol-only scaling over-represents clusters and correlation spikes change the dollars a vol target
  needs (MT117-C09-2, MT009-C07-5, MT200-C11-1) -> let risk flow to trending classes rather than force equal budgets
  (MT117-C09-1, MT099-C08-1) -> but leverage carried into an unpredictable turning point sets the loss (MT087-C08-1),
  so a lower or time-varying vol target is floated, hindsight caveat stated (MT087-C08-2, C09-2, C06-4); static and
  dynamic converge in the long run (MT200-C10-2).
- Signal shape: size linearly in strength, cap the extremes, keep the sign (MT116-C12-1, C12-2, C13-2); binary signals
  flip full positions near zero and accrue costs (MT116-C12-3); yet thresholding weak signals lagged a rates sell-off
  that began from weak signals (MT174-C04-2); signals are transformations of each other, so effort belongs in
  construction and risk (MT131-C07-4).
- Diversifiers: trend carries equity beta and loses in V-shapes -> add beta-neutral carry, skew-based cross-sectional
  reversion, vol selling (MT131-C09-1, MT173-C02-3, MT216-C06-1, C06-2) -> carry z-scored against 1-5 years of its own
  history, cross-sectional within class, built to minimise spot contribution so trend is not paid for twice
  (MT173-C15-3, C15-X2, C17-2) -> reversion as a separate engine, not a sign flip inside trend (MT116-C13-2,
  MT173-C03-1) -> non-trend sleeves also keep loss-averse investors invested (MT116-C10-3).
- Flows and crowding: P6 -> judge a premium by its driver, aggregate flow and overlap (MT130-C06-1) -> congestion
  (pre-positioning before index rolls) flattened 2015-18 when passive roll demand shrank, returned 2022 (MT204-C14-1,
  C14-2, MT134-C19-1) -> scheduled 60/40 rebalancing is mechanically contrarian and front-run, about 8bp a year on
  $20tn (MT216-C14-X2, C14-1) -> avoid month- and quarter-end schedules, use thresholds, check the trend before buying
  falling equities (MT216-C15-2, C15-1) -> the systemic risk is synchronous deleveraging, unquantifiable, so design
  more conservatively than history suggests (MT216-C03-3, C03-4, MT099-C15-2).
- Allocation: P5 + P7 -> an optimiser gives 70% (mean-variance) or 52% (downside) in trend, unusable (MT200-C15-1) ->
  size by scenario analysis of 2/5/10/15% sleeves against tracking error, ideally 5-20% inside the strategic benchmark
  (MT200-C16-1, C16-2) -> never time it, never exit after losses (MT087-C14-1, C14-2, MT216-C07-2).

Decision process: medium-term trend around a 3-month exponential half-life (the SG Trend fit; Quantica's 66 business
days), speeds about 3-12 months by "heuristics and experience" (MT099-C10-2, MT131-C07-1, MT173-C05-1, C05-R2); 50-100
markets, 40-150 look alike at constant vol (MT174-C07-2, MT173-C04-1); beyond 70-80 liquid macro markets nothing new,
exotic commodities still add (MT174-C07-1); commodities clustered into energy, metals, ags (MT167-C07-1); 10-15% vol
alone, about 20% beside a strategic allocation, drawdowns checked against Dunne's twice-vol rule (MT173-C07-1, C07-X1);
expected shortfall over VaR (MT099-C15-1); retire only when the premise changed, not on statistics (MT134-C18-3); data
mining controlled by culture, changes justified by explanation not repair (MT204-C12-1, C12-2); QIS execution passive
at guaranteed close or TWAP prices, no execution alpha for the client (MT130-C13-2).

## 3. Evidence grading

| Claim | Grade | Reason |
|---|---|---|
| V-shapes hit every speed, middle worst (MT200-C05-1, MT134-C03-3, MT087-C07-3) | moderate for direction, weak for "3-6 months" | consistent across Aug 2024, Apr 2025, Mar 2026 in his own books (described); Kaminski puts the worst window at 4-9 months (U03 section 3); March 2026 reversed the fast/slow order (MT167-C06-1). |
| 2023-25 the only three consecutive years in 25 where the slowest speed won; small universe first or second (MT134-C03-4, MT116-C06-2, C06-3) | moderate as description, weak as a rule | own 25-year grid, never shown; no top-bottom spread (MT116-C08-X2); he reads it as a V-shape artefact (MT116-C08-2). |
| No earnings in the 3 months before a peak or the first weeks after (MT039-C17-3, C17-4, C18-1) | moderate | Man Group and Kaminski papers described; few peaks; same finding as U03's second responder. |
| Quantica equity caps: worst-16-quarter average +4.1% unconstrained vs S&P -9.5%, 3.7% no equities, 4.5-4.6% capped; long run 5.9% -> about 4% (MT173-C10-1, C09-1) | moderate, SHOWN by Quantica | 2000-2024 (conditions text); his own caveats: constant beta within a quarter (MT173-C09-X2), vol not equalised across variants (MT173-C11-X1), ex-post conditioning (MT173-C09-X1). |
| Trend without autocorrelation via vol clustering; iid conditional payoff (MT116-C14-2, C15-1, MT117-C12-1) | strong as mathematics, weak as an account of realised returns | no magnitude; sits beside his "today's volatility has no short-term forecasting power for returns" (MT200-C09-2). |
| Fixed budgets embed equal-Sharpe forecasts; dynamic class budgets are prudent (MT117-C08-3, C10-1, C09-1) | algebra strong, empirics ASSERT | no backtest; his own counter-example: equities 60% of the Aug 2024 loss under dynamic allocation (MT099-C09-1); convergence long run (MT200-C10-2). |
| Sigmoid beats binary after costs (MT116-C12-1..C12-3) | weak-moderate | ASSERT; Man AHL's neural-network paper agrees in shape (MT116-C14-1); Carver's B22 gives +0.03 over binary (U02 section 3); our continuous variant lost 0.05/0.17 (CHANGES.md:15). |
| Time-series bond carry 67% correlated with bond beta; cross-sectional more neutral; optimised carry Sharpe near one (MT173-C16-1, C15-X2, C17-1 as corrected) | moderate for the beta fact, weak for the Sharpe | Resolve paper described; small universe (MT173-C16-2); the Sharpe belongs to optimised time-series carry, not the blend. |
| Curve carry: oldest QIS strategy, 15 years live, strong long-run return with no visible decay; 2026 drawdown about 10%, worst in 40 years, twice 2018 (MT130-C08-X1, C10-X2, C09-1) | weak-moderate | his bank's product, no Sharpe or cost given, "40 years" is a backtest; the risk-sharing mechanism (MT167-C02-X1) is plausible; (reader) term-structure premia are documented in the literature, outside this pack. |
| Congestion premium flattened 2015-18 from lost passive demand, not crowding; back 2022 (MT204-C14-2, MT134-C19-1) | weak-moderate | ASSERT with a mechanism that distinguishes "flat" from "negative"; no data. |
| Rebalancing front-running 8bp a year, $16bn (MT216-C14-1) | moderate, third-party SHOWN | Harvey et al. read from Bloomberg on air; the avoid-month-end rule is his inference, untested. |
| Barometer does not predict trend returns except very high -> weak (MT087-C09-3) | weak, ASSERT | own data, not shown; conflicts with Carver's B03 at market level (U02 row 5). |
| Crowding taxonomy; "crowding overstated" (MT204-C15-X1, MT002-C06-4) | strong as framework, untested | QIS seller; he concedes shared-signal externalities cannot be quantified (MT216-C03-3). |
| Track record | none | fragments: Jan 2026 +4-6% at 15% vol (MT116-C06-X1); five of seven 2026 months positive (MT174-C05-X2); index levels (MT087-C05-5, MT167-C07-2 as corrected). |

## 4. Rules worth keeping

Tags: ALREADY (file:line) / DIFFERS (how) / MISSING.

| # | Rule (codable) | Source | Status |
|---|---|---|---|
| 1 | Scale every exposure by volatility continuously; no vol or VIX triggers; judge timing indicators by false positives | MT009-C07-4, C07-2, C09-1 | ALREADY: score x 0.40 / vol (book.py:132); hybrid vol (vol.py:4-10, 48-51); risk scalers rejected (CHANGES.md:73). |
| 2 | Use correlation as well as vol: clusters inside a class, top-level leverage under a vol target | MT117-C09-2, MT200-C11-1, MT009-C07-5 | PARTLY: correlation enters only through 36-month realised vol of block and book P&L (book.py:191, 198); cluster weights rejected (CHANGES.md:17); realised book vol 4.9-14.2% vs 10% (protocol_diagnostics:4, 6). His own warning: a correlation-aware budget re-added equity risk just before Aug 2024 (MT200-C04-X1). |
| 3 | Let class risk flow to where trends exist instead of equal budgets | MT117-C09-1, MT099-C08-1, C08-2 | DIFFERS: equal class risk (book.py:9, 191-193); the slow block scaler lets signal agreement float risk inside a class (Carver B03, U02 row 5), not between classes. |
| 4 | Multi-speed 3-12 months around a 3-month EWMA half-life | MT099-C10-2, MT173-C05-1 | DIFFERS in form: 1/3/12-month sign blend, monthly (config.py:19); the 1-month leg is faster than his range; slower rejected (CHANGES.md:22, 26). |
| 5 | Linear in signal strength, capped (sigmoid), sign kept; reversion as a separate engine | MT116-C12-1, C12-2, C13-2 | DIFFERS: sign blend, four levels (book.py:71-72); continuous rejected (CHANGES.md:15); U02-T1/T5 cover it. Separate reversion: ALREADY in spirit (value = 5-year commodity reversal, signals.py:354-356). |
| 6 | 50-100 markets for diversification and cost, no screening on past contribution; alternative commodities for Sharpe, core for defence | MT173-C03-3, MT117-C01-2, MT174-C07-2, MT130-C12-2 | PARTLY: 62 hand-picked survivors (TESTING_PROTOCOL.md:25; CHANGES.md:49), a documented survivorship issue; alternative commodities capped at 30% of commodity risk (book.py:140-148). |
| 7 | Carry z-scored against 1-5 years of own history, cross-sectional within class, minimal spot contribution | MT173-C15-3, C15-X2, C17-2 | DIFFERS: raw carry level, half directional / half cross-sectional (signals.py:329-347; book.py:131); the directional half carries the bond beta he puts at 67% (MT173-C16-1). |
| 8 | Commodity curve carry: long deferred, short front; close or beta-hedge in backwardation | MT130-C08-1, C10-4, MT216-C08-3 | MISSING: our commodity carry is a front-contract position signed by ln(F1/F12) (bloomberg.py:119-133) or the EIA F1/F2 slope (signals.py:336-337); three EIA spreads exist but are not traded (gap_review_crosscheck:42). |
| 9 | Cross-sectional reversion on realised skew ("exacerbated trend") | MT173-C02-3, MT216-C06-2 | MISSING; skew is on the free "do now" list (gap_review_crosscheck:41); Carver's skew rule judged weak (U02 row 17). |
| 10 | Avoid month-end and quarter-end execution; thresholds; partial rebalancing | MT216-C15-2, C15-X1 | DIFFERS: we trade at the month-end turn by design (config.py:43; timing.py:3-5) because the fast leg loses 0.10 Sharpe per day (CHANGES.md:25); no buffer (U02-T3). |
| 11 | No model change after one episode; retire only when the premise changed; call tweaks data-mined | MT116-C08-1, MT134-C18-3, MT204-C12-1 | ALREADY: pre-registration, trial log, no in-batch re-runs (TESTING_PROTOCOL.md:29-32). DIFFERS in trigger: ours is statistical (dSR, Holm, :17-18), which he calls the wrong reason to retire. |
| 12 | Expected shortfall; design more conservatively than history; stress scenarios | MT099-C15-1, MT216-C03-3 | PARTLY: scenario limit tested, rejected as a rule, kept as a diagnostic (CHANGES.md:19, 23; config.py:30, 66-73). |
| 13 | Standalone trend unconstrained in equities; cap the position-weighted beta only when stacked | MT173-C08-3, C11-X3, MT174-C10-X1 | ALREADY: no cap; same as U03 row 12; planned variant (gap_review_crosscheck:20). |
| 14 | Vol 10-15% standalone; drawdowns under about twice vol | MT173-C07-1, C07-X1 | ALREADY: 10% (config.py:27); design max fall -12% to -17% (CHANGES.md:51; protocol_batch1.md:7). |
| 15 | Costs are limits to arbitrage; speed-cost trade-off; capacity-aware design | MT039-C14-2, MT200-C06-2, MT204-C11-2 | ALREADY: costs and 2x costs inside the test (book.py:210-215; TESTING_PROTOCOL.md:20). |
| 16 | Size the allocation by tracking-error scenarios, 5-20% | MT200-C16-1, C16-2 | not a book rule (allocator). |

## 5. Conflicts

- With Niels (pure trend vs trend-plus, MT117-C07-X1): our book is 55% non-trend (config.py:62) and every family adds
  (marginal alpha t 2.8-4.9, CHANGES.md:29-30); design evidence favours Baltas. Niels's overfit warning on
  carry-filtered trend (MT200-C13-2) stands (section 6).
- With U02 (Carver). Agreements: continuous vol scaling, breadth, no timing, costs inside the test, no refits.
  Conflicts: (a) speed: his 3-12 months with a 3-month centre vs Carver's momentum from an hour to a year; our 1-month
  leg sits outside his range and carries the delay cost (timing_grid row 3); design data keep it (CHANGES.md:26);
  unresolved. (b) Vol regime: trend should do better in a high-vol regime for a given asset because big moves follow
  big moves (MT117-C11-3) vs Carver's attenuation in high vol (U02-T4, B24); Baltas also says vol spikes carry a
  negative association with subsequent returns (MT200-C10-2), separating level from spike (reader). Carver has a test,
  Baltas a theory: favours Carver; U02-T4 should report level and spike separately. (c) Forecast strength: Carver lets
  book risk float with aggregate strength because it predicts return (B03); Baltas says aggregate trendiness does not
  predict, except very high readings precede weakness (MT087-C09-3): T2. (d) Sign vs sigmoid: both prefer continuous;
  Carver's number is +0.03, ours -0.05; agreed in direction, unresolved in size.
- With U03 (Kaminski). Agreements: second responder (he cites her work, MT039-C16-4, C17-4), objective decides design,
  no timing, risk not notional. Conflicts: (a) carry share: she says carry waters down crisis alpha; he says
  beta-neutral carry and reversion diversified the V-shape years and had one of their best years (MT131-C03-5,
  MT087-C10-1). His condition is beta neutrality, which answers her objection; our carry is only half cross-sectional
  (book.py:131), so half of it is exposed to her point; unresolved until U03-T2 reports carry's P&L in equity
  drawdowns. (b) Vol-sizing speed: she names 2022 as the year slow vol won; he names the March 2026 oil spike, where
  scaling cut risk automatically (MT167-C04-1), and the March 2026 V, where dynamic scaling added value (MT174-C05-2):
  opposite episodes, same path dependence, both call it an objective choice; our hybrid stands with U03-T1 as the
  reading. (c) Which speeds a V hits: her 4-9 months vs his 3-6 (MT200-C05-1), same episodes; immaterial for a book
  that will not switch.
- With U01 (AQR economic trend): economic trend is slow and complements price trend, but with negative growth it would
  have missed the equity trends and sizing beyond risk is the hard part (MT039-C15-1, C15-5, C15-3): supports econ at
  15% with growth off (config.py:62; signals.py:230).
- Inside the unit: (1) prefers dynamic vol scaling and class budgets (MT099-C08-R3) yet calls trend a never-timed
  allocation and static sizing after Aug 2024 data mining (MT087-C14-1, MT200-C07-1); resolved by horizon
  (MT200-C10-2), empirically open. (2) "Do not change after an episode" vs a floated lower vol target after four
  V-shapes in four years (MT087-C08-2, MT009-C09-2): hindsight flagged by him. (3) Crowding overstated vs design
  conservatively because externalities cannot be quantified (MT002-C06-4, MT216-C03-3): consistent as "no erosion, but
  a systemic tail". (4) No forecasting vs a 2025 regime read (gold, bonds, no equities) that played out but was missed
  by fast signals (MT087-C16-2): a view he does not trade. (5) 2022 "fastest best" is Niels reading his data; he says
  all speeds won, a month's entry shifting +40% to +35% (MT116-C07-2 as corrected, MT116-C08-X1).

## 6. Test proposals (ranked)

T1. Turn-of-month decomposition of the one-day delay loss (zero slot). Hypothesis (MT216-C14-1, C14-X2, C15-2;
reader link): the trend leg's loss from trading one day late (0.95 -> 0.85; book 1.01 -> 0.96, timing_grid rows 2-3)
is by construction the sum over markets of (position change) x (first-day return) (timing.py:3-5, 25-41). Signal
decay predicts a loss spread over all classes in proportion to the 1-month leg's trading; the rebalancing-flow story
predicts it concentrated in equities and bonds, the assets calendar rebalancers sell after an up-month, in trades whose
direction matches the prior month's return, with first-day class returns reversing the prior month's sign on average.
Econ, carry and value lost nothing at k = 1 (0.73 -> 0.74, -0.36 -> -0.33, 0.58 -> 0.56), as both stories predict.
Rule: on the daily grid of gm/timing.py (free daily data, daily.py:1-9), per month and market d = dpos x r(day 1) for
the trend family; sum by class and by sign(dpos x prior-month return); k = 0 and k = 1 Sharpe by class; day 2 as a
control; the regression of day-1 class returns on prior-month class returns, 1990-2010 and 2000-2010. Data: free;
Bloomberg files 6-7 later (BLOOMBERG_PULL_GUIDE.md:14-15). Expected (reader): mixed, a material equity and bond day-1
share with a negative reversal coefficient plus genuine decay in FX and commodities. Fails usefully if the loss is even
across classes and the coefficient near zero: signal decay, execution rule stands. Consequences, fixed before the
holdout: (i) live execution sits between k = 0 (the close that produced the signal) and k = 1, so the live trend leg
should be expected between 0.85 and 0.95 gross on design-era terms; (ii) if the flow story holds, part of the fast-leg
edge is a flow premium that Harvey et al.'s trend-conditional rebalancing would shrink if adopted, a holdout-era decay
risk; (iii) a no-trade buffer (U02-T3) would forgo flow captures, so T1 runs before T3 is registered. Cost: none;
logged as a diagnostic on design-period daily returns.

T2. Aggregate trendiness against forward return and realised risk (zero slot). Hypothesis (MT087-C09-3, C07-1;
MT131-C07-X6; against Carver's B03): mean absolute trend score across markets does not predict next-month trend-family
return, except that the top decile is followed by weaker risk-adjusted return and realised vol above the ex-ante
estimate, because a high barometer means concentrated exposure on few principal components that the 36-month scalers
(book.py:191, 198) under-measure. Rule: design months; B = mean |trend score| (book.py:72), C =
Herfindahl of ex-ante class risk shares; decile sort on B; next-month trend-family and book net return, Sharpe,
realised-to-ex-ante vol ratio; Newey-West t of top decile vs rest; same by C. Data: free. Expected (reader): flat to
mildly positive through the deciles, top decile with realised vol 10-30% above ex-ante and a lower Sharpe. Fails if
monotone positive with no vol excess (B03 holds, the slow scaler is right) or flat throughout. Consequence: a material
top-decile risk excess defines U03-T3's challenger (a faster, position-aware book scaler) and answers his floated lower
vol target (MT087-C08-2): no case unless low-barometer months underperform. Cost: none.

T3. Calendar-spread curve carry as the form of the planned Batch 2 commodity-carry challenger (the slot registered at
TESTING_PROTOCOL.md:82-83; no new slot). Hypothesis (MT130-C08-1, C09-2, C10-4, C10-X2; MT167-C02-X1, C11-X9;
MT216-C08-3): per commodity, long the roughly 12-month contract and short the front earns the roll-yield differential
as a risk-sharing premium with small spot beta, positive in non-inflationary recessions; its loss is the supply-shock
backwardation, avoided by closing the spread when the front is backwardated. Rule: a synthetic market per commodity,
return = deferred minus front generic-contract return (Bloomberg file 5 curves 1-12, monthly from 1969,
BLOOMBERG_PULL_GUIDE.md:13, 18; file 1 curves, :9), vol-scaled, weight 1 while ln(F1/F12) < 0 (bloomberg.py:120) and 0
otherwise, taking half of the carry family's CM block risk from the directional half (book.py:131); window = months
with at least ten commodities with curves. Expected (reader): spread Sharpe 0.5-0.8 gross, near-zero correlation with
trend; at about 4% of book risk (a quarter of the 25% carry share is CM, half of it) even that adds about 0.03, under
the 0.05 bar, hence inside the registered challenger rather than a slot of its own. Fails if the spread's net Sharpe
is under 0.3 after two legs of costs and twelve energy rolls a year (book.py:55-56), or if the 1990 oil spike
(config.py:67), the design era's supply-shock backwardation, breaches test 5 (TESTING_PROTOCOL.md:21). The 1975-89 era
will be thin and may pass test 3 only by having no new data.

T4. Skew-conditioned tail audit, folded into U02-T1 (zero slot). Hypothesis (MT173-C02-3; MT116-C12-2, C13-1):
extreme trend forecasts revert mainly when the move came with high positive realised skew in the trend's direction.
Rule: in U02-T1's bucket table, split the top |z| bucket by sign(trailing 3-month daily skew x z) where daily data
exist (daily.py), 12-month monthly skew elsewhere; next-month vol-normalised return per cell, pooled, Newey-West.
Expected (reader): weak (Carver's skew rule is +7bp, U02 row 17). Fails usefully if the cells do not differ: both
Carver's and Baltas's skew items close without a slot.

T5. No test, not worth a slot: dynamic class budgets (no backtest, his own Aug 2024 counter-example MT099-C09-1,
convergence MT200-C10-2, Kaminski's equal-risk evidence in U03); the carry filter on trend (MT200-C13-1; Niels's
1998-2023 overfit point MT200-C13-2; (reader) shorting positive-carry bonds in 1975-81 was right, so our era test would
punish it); VIX look-back switching (he rejects it, MT009-C06-3, C07-2); a standalone equity-beta cap (200bp a year for
50bp, MT173-C10-1); sigmoid vs sign (U02-T1/T5); a lower vol target (hindsight by his account, MT087-C09-2; T2
informs); roll congestion (intra-month, MT204-C14-1); dealer gamma and 0DTE (short-term only, MT167-C09-X6); narrative
data (second-hand, MT174-C16-1); option skew as a trend filter (hypothesis, MT167-C10-2); V-shape speed profiles, which
U03-T1's window split can report per trend leg at no cost.

## 7. Forward-looking logic

Inputs he says lead prices: (1) price itself over 3-12 months, timing skill at one to six months, a coin toss over a
day (MT173-C13-X1), continuing while fundamentals are disputed, reverting under certainty (MT216-C13-2, MT167-C17-1);
(2) volatility, which forecasts next-period volatility and so the right size, not next-period return (MT200-C09-2,
C10-2); lower-vol assets such as duration have delivered the stronger trend Sharpe (MT117-C12-2); (3) correlation
spikes, which change the dollars a vol target needs and mark synchronous deleveraging (MT009-C07-5, MT216-C03-2); (4)
the curve: a supply shock pushes the front into backwardation and reverts unless permanent (MT167-C02-2); curve carry
pays in non-inflationary recessions (MT167-C11-X9); (5) scheduled flows: rebalancing dates and index roll windows
create predictable pressure that fast money front-runs (MT216-C14-1, MT204-C14-1); forced liquidations and stop-loss
rules generate trends endogenously (MT216-C14-X1); (6) slow growth and inflation regimes mapped to assets (falling
growth, undecided inflation: gold, bonds, no equities, MT039-C15-4), which would have missed the equity trends of
2024-25 (MT039-C15-5); (7) crowding gauges: prime-brokerage net and gross exposure, trend positions across managers, a
trendiness measure near its 20th percentile meaning reshuffling rather than crowding (MT039-C03-1, C13-1, C13-4 as
corrected). It stops working in V-shaped spike-and-revert events, one a year for four years (MT009-C09-2),
synchronous across classes (MT087-C05-X1); under a central-bank put (MT216-C13-2); in trendless rates, 2022 to Q2 2026
(MT009-C04-2); for curve carry in a persistent supply shock (MT167-C02-2); for flow premia when passive demand
disappears or QIS crowds a pure imbalance (MT204-C14-2); and systemically when similar portfolios deleverage together,
which no backtest shows (MT216-C03-1, C03-2, MT134-C08-1).

## 8. Self-check

Numbers re-verified against the pack by script (foundation/tmp_u04/check_numbers.py; "claim" = in the extracted claim
text, "quote" = in the verbatim quote, "cond" = conditions field): 3-6 months (MT200-C05-1, quote); 3-month half-life,
66 days, 15 years (MT099-C10-2, MT131-C07-1, claim); 3-12 months (MT173-C05-1, claim); 50-100 (MT174-C07-2, quote);
70-80 (MT174-C07-1, quote); 40/50/100/150, ten (MT173-C04-1, claim); 10-15%, 20% (MT173-C07-1, claim); 4.1 / -9.5 /
3.7 / 4.5-4.6 / 5.9 / about 4 / 50bp / 200bp (MT173-C10-1, claim; 2000-2024 cond); 12 of 16 (MT173-C09-1, claim); 67%
(MT173-C16-1, claim); 1-5 years (MT173-C15-3, quote "one year or three years or five years"); 70% / 52%
(MT200-C15-1, claim); 2/5/10/15%, 5-20% (MT200-C16-1, C16-2, claim and quote); 60% of the loss (MT099-C09-1, claim);
8bp / $20tn / $16bn (MT216-C14-1, claim); about 10%, 40 years, twice 2018 (MT130-C09-1, claim); 15 years
(MT130-C08-X1, claim); three consecutive years in 25 (MT134-C03-4, claim); +40% to +35% (MT116-C08-X1, claim); 4-6% at
15% vol (MT116-C06-X1, quote); five of seven (MT174-C05-X2, claim); one a year for four years (MT009-C09-2, quote);
beta 0.4 (MT173-C08-2, quote "point4"); 20th percentile (MT039-C13-4, quote); 3 of 33 (MT009-C09-1, claim). Against
the repo: (1, 3, 12), cap 2.0 (config.py:19); 35 days, 0.7, 0.75 (config.py:22); 10% (config.py:27); 45/15/25/15
(config.py:62); execution rule (config.py:43); 1990 oil window (config.py:67); equal class risk (book.py:9); sign blend
(book.py:71-72); half carry (book.py:131); 0.40 (book.py:132); 30% cap (book.py:140-148); 36 months (book.py:191, 198);
costs 4-6 bp, 12 rolls (book.py:55-56); ln(F1/F12) (bloomberg.py:120); 1.43/0.76 vs 1.48/0.93 (CHANGES.md:14-15);
cluster, spot, slow (CHANGES.md:17-18, 22); 0.95/0.85/0.64/0.61 (CHANGES.md:25); t 4.9, 3.3, 3.1, 2.8
(CHANGES.md:29-30); +0.12, +0.11 (CHANGES.md:91-92); timing grid 1.01/0.96, 0.95/0.85, 0.73/0.74, -0.36/-0.33,
0.58/0.56 (timing_grid rows 2-6); 4.9-14.2% (protocol_diagnostics:4, 6); dSR >= 0.05, test 5 (TESTING_PROTOCOL.md:18,
21); 62 markets (:25); batch 2 commodity carry (:82-83); files 1, 5, 6-7, "monthly from 1969" (BLOOMBERG_PULL_GUIDE.md:9,
13, 14-15, 18). Derived (reader): about 4% of book risk = 0.25 x 1/3 x 1/2; about +0.03 from an uncorrelated Sharpe
0.8 stream at that share. Corrections made during the check: MT200-C08-2 and MT039-C13-4 are cited as corrected;
MT116-C07-2 (2022 fastest best) is Niels's reading; MT173-C17-1's Sharpe near one belongs to optimised time-series carry only; MT167-C06-2's
"10-40 commodities, quarter of risk" is claim text whose quote says "15 to 20", so only the clustering is cited;
MT173-C07-X1's twice-vol rule is Dunne's, cited as his check of it; the six claims re-attributed to Niels are not used
as his.

Strongest counter-argument to the verdict: he is the one unit so far whose job is building and selling exactly the
objects we are building (trend, carry, curve, reversion indices on 50-100 markets), and he is candid about the limits
of his evidence; discounting him for not showing exhibits on a podcast may undervalue desk experience that agrees with
our own log on where the gains are (construction, not signals). Conversely the agreement may be shared industry
folklore rather than independent confirmation: our construction choices were made after reading the same literature.

Strongest counter-argument to T1: the decomposition cannot separate the two stories cleanly, because the 1-month leg's
trades are aligned with the prior month's return by construction, so "with-trend trades in equities and bonds on day
1" is also where pure signal decay would show; the class split (FX and commodities carry no 60/40 rebalancing flow) is
the only discriminator, and FX has its own month-end fixing flows (reader). A turn-of-the-month effect in equities is
also a known calendar anomaly independent of rebalancing (reader), so a positive result supports "flow", not
specifically Harvey et al.'s rebalancing. And it is a look at design-period daily returns that shapes how a later
buffer challenger is read: logged, but a mild selection step.
