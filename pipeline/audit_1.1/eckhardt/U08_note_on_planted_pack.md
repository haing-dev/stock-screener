# U08: Eckhardt Trading (Bill Eckhardt, Rob Santino; host Moritz Seibert) - judgement brief (Fable, 2026-11-12)

Inputs: foundation/packs/U08.json (one transcript map, MT020, Open Interest 10, dated 2024-10 in the map; 55 claims by
speaker field: Eckhardt 41, Santino 6, Seibert 8; 52 quotes script-checked "exact", three R-claims with no check; one
ledger correction, C13-1), the notes U01-U07 and BRIEF_ADDENDUM.md. Claim ids are written without the MT020- prefix.
Per the addendum: (a) every pack statement was checked against its verbatim quote and is used in sections 1-8 only
where the quote carries it; the quotes are one line each, so most of the map is unusable (section 9, 83 items); (b)
the repo was not read: what our book does is taken second-hand from U01-U07 and cited to them, and every status tag in
section 4 reads "not checked". SHOW = a test with numbers; ASSERT = stated, no test; (reader) = my inference. Nothing in
this pack is SHOWN. No backtest was run, no returns were loaded (pack checks and plain arithmetic only, scripts in
tmp_u08/); the 2011-2026 holdout was not touched. Which ETC speaker gives the sizing answers is uncertain by the pack's
own note, so C06-2 to C06-4 are cited as ETC's.

## 1. Verdict

1. Core logic: the direction of a market can almost never be known better than 51-52% (C13-4) and the loss tail is
   very heavy (C13-2, C11-4), so the edge lies in what can be known and controlled: risk first, as a risk-averse agent
   (C04-1, C04-2, C05-1); losses cut and profits left to run (C14-1); increased volatility not restrained and size not
   readjusted to it inside a trend (C06-3; C06-4, a quote cut short); payoffs that win 70-90% of the time distrusted
   (C13-3); inference by distribution-free statistics at 10-30 times the data (C12-1, C12-2); systems torn apart as
   hard as they are built (C09-3, C09-2, C10-1).
2. Grounding: assertion throughout. One interview, one-line quotes, no return, drawdown, cost, sample or test
   statistic, methods withheld; the only quantities in the quotes are 51-52%, four or five days, five or six, 70-90%,
   10-30 times and two to four months. The premises are common ground with U02-U07 (returns hardly forecastable, risk
   forecastable; volatility rises with winning trends; a high win rate marks a sold tail). The one operating
   conclusion that differs, do not re-size to volatility, is contradicted on Sharpe by what Carver SHOWS (1.18 against
   0.88; 0.92 against 0.57: U02 section 3, digest numbers) and agrees with Quantica's convexity trade-off (U03
   section 2): a difference of objective, since he reasons in utility functions (C04-2, C04-4), not in Sharpe.
3. The pack is thin and unreliable: 83 problems (section 9). The map contradicts its quotes five times (robust
   statistics need 2-3 times the data where the quote says 10-30; resizing is "always" a hidden reversion trade where
   the quote says "not always"; a strong run lasts years where the quote says months; prices mean-revert where the
   quote says volatility does; the Turtle rules decayed before their release where the quote says since) and itself
   three times (70 or 120 markets, 40% or 60% winners, a portfolio volatility target or none); two speaker fields are
   wrong or contested; and the specifics a reader would most want (market count, trend share, win-rate target, sample
   length, out-of-sample hold-back, stop rule, the case against moving averages on price) are in no quote and are not
   used.
4. For our book (as U02-U07 describe it; not re-checked): we stand at the opposite end of the one live dispute.
   Positions are re-sized monthly on a 70%-fast volatility estimate adopted for +0.12 Sharpe (U03 row 3) where ETC
   does not readjust; 40% of risk sits in convergent families (U02 row 11), where his warning about frequent small
   wins would apply if T2 finds them; and the bar is a moment statistic tested by a distribution-free bootstrap (U07
   section 5). His line that fear of overfitting ends in underfitting (C09-1) is the case for the registry over one
   slot per change. The unit carries no number that could move a prior, so nothing earns a Holm slot.
5. Action: four zero-slot diagnostics. T1 within-trend volatility audit and the P&L of the re-sizing overlay; T2 sign
   accuracy and payoff profile by family, the mark of a sold tail before its loss; T3 distribution-free re-read of
   the paired tests, with time concentration; T4 planted-error test of the engine gates. Open choices are expressed as
   levels of C (static-at-entry; a mean-absolute estimate, conditional), D (fixed gearing) and U07's S (a rank
   statistic, conditional); no new dimension.

## 2. Logical foundation

| Premise | Type | Source |
|---|---|---|
| P1 Money flows from the many to the few; one has to be among the few | institutional/behavioural, ASSERT | C01-1 |
| P2 Direction is almost never known better than 51-52%; prediction cannot be very successful | empirical, ASSERT (no sample, horizon or market) | C13-4, C03-2 |
| P3 Risk can be known, changed and controlled | institutional | C04-1 |
| P4 Each dollar gained is worth a little less, each dollar lost a little more; risk-loving preferences are "financially suicidal"; only risk aversion works | theoretical (concave utility) | C04-2, C04-4, C05-1 |
| P5 Price changes and the trades of a futures system are not normally distributed; the loss tail is very heavy | empirical, ASSERT here | C11-4, C13-2; Seibert C12-X2 |
| P6 Volatility mean-reverts, futures prices do not; volatility often increases with a trend | empirical, ASSERT | C07-2; C06-4 |
| P7 Futures carry a robust trend component, stocks do not; futures are exactly balanced between longs and shorts | empirical/institutional, ASSERT | C11-2, C11-3 |
| P8 What was revealed when the Turtles were let go has been heavily degraded; one has to keep researching to stay ahead; yet "the death of trend following has been highly exaggerated" | institutional, testimony | C05-4, C06-1, C05-5 |
| P9 Fit the permanent features of a series, not the transitory; fear of overfitting leads to underfitting; a system can run strongly for two to four months, then go flat or degrade | statistical | C08-3, C09-1, C09-4 |

Chains (each arrow is a step a quote carries; where the pack completes a quote, that is said):

- Source of the edge: futures are balanced, one long for every short (P7), and money flows from the many to the few
  (P1) -> (reader) an edge is the mirror of what the many do, so a rule the many adopt loses it: the decay of the
  revealed rules and the need to keep researching (P8) follow from the first premise. No quote says who the losing
  many are or why they persist.
- Risk first: P2 -> prediction cannot carry the result -> "instead" put the effort where knowledge exists (P3) ->
  size as a risk-averse agent (P4), not with risk control grafted on "as an afterthought" (C04-3) -> get out of
  losses, let profits run (C14-1). (reader) At 51-52% accuracy only gains larger than losses close the arithmetic:
  the exit is the edge.
- Tails to payoff: P5 -> a strategy that makes money 70-90% of the time is "subject to large freakish losses" (C13-3)
  -> take the opposite payoff (C14-1) -> in Seibert's words controlled risk and a "long optionality profile"
  (C07-1), paid for by the "pain arbitrage" of holding to the system in bad times (C14-2).
- Volatility: P6 -> estimate it with moving averages (C08-2); it enters the system in five or six ways (C06-2) ->
  but increased volatility often helps, "we don't want to restrain it" (C06-3) -> it rises with trends, so ETC does
  not readjust to it (C06-4: the quote stops at "if we were readjusting to volatility we would"; the claim field
  adds "cut the position along with the trend") -> Seibert: that would be "a hidden Mar reversion trade against the
  direction of the trend" (the caption's spelling of mean reversion), "not always true by definition" but true
  "more often than not" (C07-X1). (reader) The two halves of P6 point one way: if volatility mean-reverts, a rise
  inside a trend overstates future risk, so sizing on current volatility over-cuts. ETC's practice is the limit of a
  slow estimator, the dimension on which Kaminski put us at the fast end (U03 row 3).
- Statistics: P5 -> avoid normal techniques, use robust or distribution-free statistics (C12-1) -> these are "data
  hogs" that need 10, 20, 30 times as much data for a reliable inference (C12-2) -> long samples only; someone
  unnamed "busted out spectacularly" on normal theory (C12-3); Seibert: a standard-deviation volatility estimate
  brings normality back (C12-X3).
- Research: formalise parts of trading rigorously, oversimplifying at first (C02-2, C03-1); P9 + P8 -> keep some
  of the structure rather than boil it all down into one number, though much of it must go (C07-3, C08-1; structure
  of what is claim text only) -> an E-score ("escore" in the captions) with elements that test for money made over
  too short a period (C09-2) -> as much time tearing systems apart as building them (C09-3), by a process that also
  tests the program for subtle glitches (C10-1) -> keep researching (C06-1).
- Universe: more markets, more independent bets (Seibert, C10-2) -> liquidity and slippage measured for every market
  traded or considered (C10-3) -> alternative markets look better on paper and "I think" are worse in practice
  (C11-1) -> no chasing of the few hot markets (C10-X1) -> futures, not stocks (P7).

Decision process, as far as the quotes go: short, medium and long-term systems, some trades averaging four or five
days (C05-2); volatility in five or six places (C06-2), not restrained, not readjusted to (C06-3, C06-4); losses cut
(C14-1); liquidity and slippage measured (C10-3); an E-score and destructive testing of systems (C09-2, C09-3,
C10-1). No quote gives a position formula, an exit distance, a volatility estimator, a market count, a trend share, a
sample length or an out-of-sample rule.

## 3. Evidence grading

| Claim | Grade | Reason |
|---|---|---|
| Direction is almost never known better than 51-52% (C13-4, C03-2) | ASSERT; consistent with other units | No sample, horizon or market; a ceiling, not a measured hit rate. (reader) Under normal returns it equals a per-market Sharpe of 0.09-0.17 at a monthly horizon and 0.19-0.38 at his four-to-five-day trade length: the order of Robertson's 0.1 and Git's 0.2-0.25 (U06 section 3; U05 P4). |
| Concave utility makes risk aversion necessary; risk-loving sizing ends in ruin (C04-2, C04-4, C05-1) | strong as logic; nothing shown | No utility function, leverage or loss figure. (reader) At a 10% target the skew term of log utility is about -0.006% a year; even at a risk aversion of 10 a skew difference of 0.3 between two books is worth about 0.16% a year, against a bar of 0.5% (U07 section 5). The argument bites at high leverage or with drawdown-type preferences, hardly in ranking books at ours. |
| Price changes and system trades are not normal; the loss tail is very heavy (C11-4, C13-2; Seibert C12-X2) | ASSERT here; (reader) well documented for daily futures returns | Nothing on monthly, diversified, vol-scaled returns, the series our tests use. |
| Distribution-free statistics need 10-30 times the data (C12-1, C12-2) | direction sound; size ASSERT | Times what is not said. (reader) Textbook rank tests need about 1.05 (signed rank) to 1.57 (sign test) times the data of a t-test under normality, so the figure can only describe inference on tails or dependence. Carver agrees that 2-3 years say far less than 20-50 (U02 section 2). |
| A strategy that wins 70-90% of the time is subject to large freakish losses (C13-3) | moderate as logic | No example; matches the third-party results Harding cites (U07 section 3). |
| Volatility often increases with a trend (C06-4) | moderate | "We have found", no numbers; Quantica's entry-to-exit ratio of 1.2 for winners against 1.05 for losers agrees (U03 section 2). |
| Readjusting size to volatility works against the trend (C06-4 as the claim field completes it; Seibert C07-X1) | ASSERT; contradicted on Sharpe | The quote stops before its conclusion; Seibert hedges. Carver SHOWS vol-scaled sizing ahead of static three times (U02 section 3); Quantica: Sharpe with scaling, convexity without (U03 section 2); on our panel the faster estimate won +0.12 (U03 row 3). |
| Increased volatility often helps; do not restrain it (C06-3) | ASSERT; disputed | Baltas's theory agrees, Carver's B24 finds momentum weaker in high volatility (U04 section 5). Carver's B03 does support not forcing risk back to target (U02 section 3). |
| Volatility mean-reverts; futures prices do not (C07-2) | first half standard (reader); second ASSERT | No horizon. Carver has reversion beyond a year (U02 P1); our value family includes a 5-year commodity reversal (U04 row 5). |
| Revealed rules were heavily degraded, yet trend's death is exaggerated (C05-4, C05-5); shorter-term edges decayed while long time frames still work (Seibert, C05-3, C05-X1) | testimony, moderate; the split by speed ASSERT | The originator on his own rules, no figure; Winton says the same of simple rules (U07 P4). No performance by horizon, and ETC itself still has four-to-five-day trades (C05-2). |
| Alternative markets are worse in practice than on paper (C11-1) | ASSERT ("I think") | Against AHL's 0.8-0.9 versus 0.5-0.6 (U06 section 3); each side sells its universe. The checkable part, measured slippage (C10-3), is not shown. |
| Stocks lack the trend component of futures (C11-2) | ASSERT | Winton reports the same for single stocks (U07 section 3); the long-short balance of futures (C11-3) is a fact with no shown link to trend. |
| An E-score tests for profit made in too short a time; systems are torn apart; the process finds program glitches (C09-2, C09-3, C10-1) | process description, unverifiable | No criterion, threshold or result; C09-3's speaker is doubtful (section 9, row 9). |
| Track record | none | The pack holds no ETC return, asset or drawdown figure. |

## 4. Rules worth keeping

Status is "not checked" throughout (addendum). Each rule is my coding of what the quote says; where the quote gives no
parameter none is invented. The last column is what earlier notes say of our book, second-hand.

| # | Rule (codable) | Source | Status | Earlier notes (second-hand) |
|---|---|---|---|---|
| 1 | Fix the risk budget and the loss bound before any return estimate; rank ideas by a risk-averse objective | C04-1, C04-2, C05-1 | not checked | 10% target, -25% holdout bound (U02 rows 6, 20) |
| 2 | Cut losses, let profits run: an exit that bounds each position's loss, no profit target | C14-1; C13-1 (speaker contested) | not checked | no stops (U02 row 6); (reader) the 1-month sign leg is the only fast exit |
| 3 | Do not restrain risk when volatility rises | C06-3 | not checked | slow 36-month book scaler lets risk float (U02 row 5) |
| 4 | Do not readjust size to volatility while a trend runs | C06-4 (cut short); Seibert C07-X1 | not checked | re-sized monthly on the hybrid estimate (U03 row 3) |
| 5 | Estimate volatility with moving averages; expect it to mean-revert | C08-2, C07-2 | not checked | 70/30 fast/slow blend with a slow floor (U02 row 2) |
| 6 | Flag any system that wins 70-90% of the time | C13-3 | not checked | none; (reader) meaningful per market or trade only. T2 |
| 7 | Inference by distribution-free statistics; no conclusion from short samples | C12-1, C12-2 | not checked | paired bootstrap of a Sharpe difference (U07 section 5). T3 |
| 8 | Test whether a system made too much of its money in too short a period | C09-2 | not checked | two-era bound only (U07 section 5). T3 |
| 9 | Do not act on a two-to-four-month run | C09-4 | not checked | long windows only (U05 row 13) |
| 10 | Fit permanent features, not transitory ones; do not escape overfitting by underfitting | C08-3, C09-1 | not checked | no criterion given; section 5, our protocol |
| 11 | Spend as much effort breaking a system as building it; the battery must test the program | C09-3, C10-1 | not checked | negative-lag and noise tests missing (U05 row 12). T4 |
| 12 | Measure liquidity and slippage for every market traded or considered; discount paper results of alternative markets | C10-3, C11-1 | not checked | alternatives costed at 8 bp in U06-T2 |
| 13 | Do not concentrate in what is currently hot | C10-X1 | not checked | no screening on past contribution (U04 row 6) |
| 14 | Assume a revealed rule degrades; keep researching | C05-4, C06-1 | not checked | our families are published premia (U07 section 1) |

Not codable as stated: keep enough structure, more than one summary number (C07-3, C08-1; the pack's 20-day example
is in no quote); several horizons from short to long (C05-2; ours is the 1/3/12 sign blend, U03 row 1).

## 5. Conflicts

With other speakers in the pack. (a) Breadth: Seibert, more markets give more independent bets (C10-2); Eckhardt,
alternative markets are worse in practice (C11-1), yet chasing a few hot markets is anti-diversifying (C10-X1).
Reconciled by his criterion, measured liquidity and slippage (C10-3); the size of the haircut is unresolved. (b) Speed:
Seibert says alpha decayed in shorter-term systems while long time frames still work (C05-3, C05-X1); ETC still has
trades averaging four or five days (C05-2). Unresolved: no performance by horizon. (c) Volatility: the map files a
disagreement, but at quote level Seibert and ETC agree (C07-X1, C06-3); Seibert's objection that a standard-deviation
estimate brings normality back (C12-X3) is answered in no ETC quote. The map's fourth disagreement, with Dennis as
reported, rests on claim text and an unchecked quote (section 9, rows 31, 32, 81) and is not used.

With earlier notes:

- Vol sizing: ETC is the first unit against re-sizing. Carver, Baltas, Git and AHL scale continuously (U02 row 2; U04
  row 1; U05 row 3; U06 section 5); Kaminski and Harding name the cost ETC names, the right tail (U03 section 2; U07
  section 5). Evidence favours dynamic sizing on Sharpe (Carver, SHOWN) and ETC on convexity (Quantica, described): a
  choice of objective. T1.
- High volatility: "often helps" (C06-3) sides with Baltas's theory against Carver's B24 (U04 section 5): favours
  Carver, who has a test; T1 puts both in one table.
- Exits: "get out of your losses" (C14-1) against Carver's no stops (U02 row 6). (reader) In a sign-blend book the fast
  leg is the exit; unresolved for trade-based systems, which ours is not.
- Speed and decay: ETC's short trades stand against Winton and AHL (fast decayed first; slow has the higher Sharpe: U07
  P5; U06 section 3) and with our design panel (U06 section 5). His account of one revealed rule decaying (C05-4) is
  Winton's P4; trend's death "highly exaggerated" (C05-5) fits the no-aggregate-crowding view of U03-U05. (reader)
  His first premise makes every widely known rule decay; Baltas lets risk-sharing premia survive crowding (U04 P6) and
  Carver calls them premia anyone can harvest (U02 P2). Unresolved until the holdout, and it matters for a book of
  four published families (U07 section 1).
- Reversion: futures prices do not mean-revert (C07-2) against Carver's reversion beyond a year (U02 P1) and the
  commodity reversal in our value family (U04 row 5): favours Carver at multi-year horizons; Eckhardt gives no
  horizon.
- Alternative markets: against AHL, Judes and Baltas (U06 section 3; U07 section 3; U04 row 6), with Carver's cost
  limits and Git's view that 50 markets do as well as 200 (U02 row 8; U05 section 5). All assertion; unresolved; it
  supports the 8 bp charge in U06-T2.
- Statistics: with Harding against normal-theory moments (U07 section 3) and with Carver on long samples; Carver's
  bootstrap makes the size second order when leverage is free (U02 section 3). Favours Carver on size.
- Loss bound: Carver and Moore say a drawdown is only what Sharpe and length predict (U02 row 20; U06 section 5);
  Eckhardt's order, risk before prediction (C04-1), like Harding's return under a risk constraint (U07 section 5),
  keeps a stated loss bound. Unresolved; the holdout criteria stand as registered.
- Replication (C12-X1): U05's public example, a crossover 80% correlated with the SG CTA index that earned 0.43% a
  year (U05 section 3), shows the correlation can be had without the return.
- Common ground with every unit: risk can be forecast, returns hardly (C04-1, C13-4; U02 P3; U04 P4; U07 P6); no
  choice of markets by recent performance (C10-X1; U04 row 6; U06 row 6).
- Our protocol (reader): the trial log holds two adoptions against ten failed variants (U04 section 1), and under one
  bar for every change, dSR >= 0.05 with Holm, gains of 0.02-0.04, the size a registry level is expected to carry
  (U07 section 6), cannot pass one at a time (U02 section 1). "If you're afraid of overfitting one way is to
  underfit" (C09-1) names that risk; the registry's walk-forward selection, tested once, is the answer already
  chosen. The unit supplies the reason, no parameter.

Inside the unit. (a) The E-score tests for money made in too short a time (C09-2), yet a book that holds size seeks a
payoff concentrated in few episodes (C06-3; Seibert's "long optionality", C07-1): no threshold is given; unresolved,
and the reason T3 reports concentration but never bars on it. (b) Robust statistics (C12-1) beside volatility
estimated by moving averages (C08-2): of what is not said. (c) Rules degrade once revealed (C05-4), so the methods are
withheld, and the claims that matter most (control of overfitting) cannot be examined. (d) Prediction "can't be very
successful" (C03-2) beside systems that take direction: consistent, 51-52% plus asymmetric exits. (e) Volatility
mean-reverts (C07-2) and rises with trends (C06-4): consistent, and jointly Carver's reason for the slow 30% in the
estimate (U02 section 2).

## 6. Test proposals (ranked)

Earlier tests, no new slot: U03-T1 gains T1's overlay rows (same runs); U02-T4 (level E2) shares T1's table; U07-T1's
table gains T2's columns; U06-T2's admission rule gains a liquidity floor from file 5 volume and open interest, fixed
before any P&L is seen (C10-3; U05 row 6).

T1. Within-trend volatility audit and the re-sizing overlay (zero slot; run with U03-T1). Hypothesis (C06-4, C07-X1,
C06-3 against Carver's B22, B31, B24): (a) volatility rises as a trend extends; (b) cutting size on that rise forfeits
return, so the book as sized minus the same book with size held is a losing trade against the trend. Rule: design
months, trend family, gross unit-risk P&L as U05-T1 defines it. Episode = a run of months in which the sign of a
market's 12-month return is unchanged (U03-T1's static-at-entry); R = current vol over vol in the episode's first
month. Report by era (1975-89, 1990-2010): (i) the share of episode-months with R > 1 by age (1-3, 4-6, 7-12, over 12
months) and the entry-to-exit ratio for winning and losing episodes; (ii) next-month return in the trend's direction
by tercile of R within age band, divided in turn by entry vol, current vol and, where daily data exist, next month's
realised vol; top minus bottom tercile with a month-clustered t; (iii) overlay = family P&L as sized minus P&L with
vol frozen at entry: mean, Sharpe, skew, correlation with the frozen book, and its mean in the frozen book's best and
worst 5% of months; (iv) (i)-(ii) again with a mean-absolute-return estimate (C12-X3) and with U02-T4's percentile Q
in place of R. Data: free; Bloomberg file 6 later for daily commodity vol (U02-T2). Expected (reader): (a) holds for
winners (1.2 against 1.05, U03); return per unit of current vol flat to falling in R, per unit of entry vol rising;
the overlay earns a positive mean and gives up the best months: each side right on its own objective. Fails for ETC
if the overlay's mean is positive in both eras and nothing is given up in the best months; fails for our hybrid if
return per unit of realised vol (current vol where there is no daily data) rises with R at |t| > 2 in both eras.
Registry, fixed now: the open choice is dimension C, level static-at-entry (on the menu or not: not checked). It is
removed by rule only in the first case; otherwise the walk-forward procedure decides, under S1 as well if U07-T1
registers it. A mean-absolute level of C is admitted only if (iv) reverses the sign of (ii). At book level C06-3 is
dimension D, level fixed gearing, with Carver's B03 behind it (U02 section 3); U03-T3 is its diagnostic. Cost: none
against Holm; logged.

T2. Sign accuracy and payoff profile by family (zero slot). Hypothesis (C13-4, C14-1, C13-3): a trend rule is right
about direction barely more than half the time and earns from gains larger than losses; a convergent rule shows the
reverse, many small gains, before any tail loss is realised: the profile the realised-loss guards cannot see (U07
section 5). Rule: design months; gross unit-risk P&L per family, market and month. Report by family, class and era: (i)
accuracy = share of market-months with positive P&L, month-clustered standard error (a sign test); (ii) payoff ratio =
mean gain over mean loss; (iii) the same per trade, a trade being a run of months with one sign of the family's score
in one market: win rate, payoff ratio, share of P&L from the best tenth of trades, the worst 1% of trades in
entry-risk units; (iv) the book's share of winning months, for reference. Flag, for families now and registry levels
later: trade-level win rate above 70% with a payoff ratio below 1 (C13-3's band). Data: free. Expected (reader): trend
accuracy 52-54%, the normal-return equivalent of a per-market Sharpe of 0.2-0.35 (U05 P4; U06 section 5), at or just
above his ceiling; trend trades win less than half the time at a ratio above 1; carry and value win more often at a
ratio below 1; no family reaches 70% per trade, while a book at the design Sharpe of 1.63 (U02 section 7) wins 68%
of months by diversification alone, which is why the flag is never read at book level. Fails usefully if trend
accuracy is 55% or more (about 0.44 per market, richer than any practitioner's figure; Git's haircut applies, U05
section 2) or a convergent family sits in the 70-90% band. Consequence, fixed now: the table goes into the holdout
report; a tail loss in a flagged family is read as the profile realised, not as breakdown; U07-T1's bar on S1 gains
the flag as a second trigger. Cost: none; logged.

T3. Distribution-free re-read of the paired tests, with time concentration (zero slot). Hypothesis (C12-1, C12-2,
C09-2): a verdict on a Sharpe difference can rest on a few months; rank statistics and a concentration count would show
it. Rule: for each paired comparison on record (B0.1, B0.2, the five batch-1 challengers: U07-T1's list) and each later
main-effect run, d = monthly net return of challenger minus incumbent at the common 10% target, design months. Beside
dSR report: (i) share of months with d > 0, stationary-bootstrap interval; (ii) Wilcoxon signed-rank p; (iii)
Hodges-Lehmann location x 12 beside mean x 12; (iv) mean with the 2.5% largest and smallest months trimmed; (v) mean
with each calendar year left out in turn (minimum, maximum) and the number of best years whose removal brings it to
zero; (vi) share of the cumulative difference earned in the best 5% of months (about 22 of 432, U07 section 8). Data:
stored runs. Expected (reader): differences of two diversified monthly books are near symmetric, so (i)-(iv) agree
with dSR; B0.2 (p 0.037, U07 section 6) is the adoption most likely to lose significance; a shift of share to trend is
more concentrated in time than a change of vol estimate. Fails usefully if an adoption changes sign under two of
(ii)-(iv) or reaches zero with two or fewer years removed. Consequence, fixed now: nothing adopted is reopened; the
main-effects table carries (iii) and (v); concentration is reported, never a bar, because a convex level earns in few
months by design (about 20 months carry trend's return, U03 section 1). Level S2 of dimension S (U07's proposal;
adoption not checked), the shrunk Hodges-Lehmann location of d with the same guard as S0, is registered only if it
ranks the levels of some dimension differently from S0; S1 and S2 then compete for the single extra chain, the one
that differs from S0 in more dimensions; otherwise the null is recorded. Cost: none.

T4. Planted-error test of the engine gates (zero slot; engineering, no market hypothesis). Hypothesis (C10-1, C09-3):
a destructive battery finds program glitches that a normal run does not. Ours found look-ahead paths in the input
layer at block 3 (CLAUDE.md, status of 2026-11-11, as given in this session's context; the repo was not read), so
its power against other classes is unmeasured. Rule: on a copy of the engine, never the registered version,
plant one defect at a time from a list fixed in advance: a signal reading month t+1; a centred vol window; a scaling
constant fitted on the full sample; a start gate set by full-sample length; a market list filtered by later existence;
a roll adjusted with later prices; costs dropped for one class. Run the reproduction and truncation gates with the cut
inside the design period. On the clean engine add the two profiles U05 lists as missing (U05 row 12): positions
applied a month early must raise the Sharpe sharply, one to three months late lower it smoothly; price noise of 0.25,
0.5 and 1 daily standard deviations must lower it monotonically. Data: free inputs; no holdout month is produced.
Expected (reader): hard look-ahead is caught; the full-sample constant and the survivor list pass unless the truncated
run recomputes them. Fails usefully if a planted defect passes: the gate is extended before the registered engine
version that fixes the block-3 findings is built. Cost: none.

T5. No test, not worth a slot. A per-position stop (C14-1): redundant with the 1-month sign leg (reader) and against
Carver's rule and his static-sizing comparison (U02 row 6, section 3). A breakout or range-position estimator in
dimension E (C07-3): the quotes name no form, the rules he does speak of are the ones he says degraded (C05-4), and
Baltas and Git call signal form secondary (U04 section 1; U05 P4); the spread report of U07-T5 suffices. Expected
utility as the selection statistic (C04-2): close to Sharpe at a 10% target (section 3), and U07's S1 already carries
the downside view. Short-horizon systems (C05-2): U06-T3 covers the question. Stocks (C11-2) and replication
(C12-X1): not our instruments. The alternative-market haircut (C11-1): an admission rule (above), not a test.

## 7. Forward-looking logic

The unit names no input that leads price direction; that is its premise (C13-4, C03-2). What its logic says leads, and
what it leads:

1. A market's own persistence, in futures and not in stocks (C11-2), with no pull back to a mean (C07-2); horizon from
   trades of four or five days to long-term systems (C05-2; Seibert: long time frames still work, C05-X1). Step: the
   payoff chain; what turns persistence into profit is the exit (C14-1).
2. Volatility leads volatility: it mean-reverts and is estimated by moving averages (C07-2, C08-2); it leads the right
   size, not direction.
3. A trend leads volatility: vol often increases with a trend (C06-4), and increased vol often helps the systems
   (C06-3). (reader) Within-trend vol is read as confirmation, not as risk to cut; Git says an extended trend makes
   historical vol under-forecast (U05 section 7, claim text). Horizon: the life of the trend.
4. Disclosure leads decay: rules degraded after they were revealed (C05-4); horizon years; hence C06-1.
5. A payoff's win rate leads its tail: 70-90% winners, then "large freakish losses" (C13-3); undated.
6. A system's last two to four months lead nothing (C09-4); measured liquidity and slippage lead the gap between
   paper and practice (C10-3, C11-1).

It stops working, by its own logic (no failure condition is stated in any quote; reader throughout): when prices do
revert at the horizon traded, the V-shapes of U03 and U04; when volatility rises without a trend, so that held size
carries more risk for nothing; when a move gaps through the exit and the loss is not the one planned; once a rule is
public (C05-4); and, for inference, whenever the sample is short (C12-2).

## 8. Self-check

Numbers re-verified. From the pack, all in the verbatim quote (check_note.py: every cited id resolves): 51 or 52%
(C13-4); four or five day (C05-2); five or six (C06-2); 70, 80, 90% (C13-3); 10, 20, 30 times (C12-2); two, three, four
month (C09-4); 55 claims, 52 exact, 3 unchecked, 41/6/8 by speaker (check_pack.py). From earlier notes, second-hand,
not re-checked against the repo or their packs: 1.18/0.88, 0.92/0.57 (U02 section 3); 1.2/1.05 (U03 section 2); +0.12
(U03 row 3); about 20 months (U03 section 1); 0.1 per market (U06 section 3); 0.2-0.25 (U05 P4); 0.35 (U06 section 5,
derived there); 0.8-0.9 and 0.5-0.6 (U06 section 3); 8 bp (U06-T2); 80%, 0.43% (U05 section 3); 1.63 (U02 section 7);
p 0.037 (U07 section 6); 432 months (U07 section 8); 45/15/25/15, hence 40% convergent (U02 row 11); 10% and -25% (U02
rows 6, 20); 20-50 against 2-3 years (U02 section 2); two adoptions, ten failed variants (U04 section 1); 0.02-0.04
per level (U07 section 6); 0.5% a year = dSR 0.05 at a 10% target, and skew -0.65 (U07 section 5); 70/30 and the
36-month scaler (U02 rows 2, 5); 1/3/12 (U03 row 1); 50 against 200 markets (U05 section 5). Derived (reader,
derive.py; normal returns where stated): 51-52% accuracy = annual Sharpe 0.09-0.17 at a monthly horizon and 0.19-0.38
at 4.5 days; Sharpe 0.2, 0.35 and 0.44 = 52.3%, 54.0% and 55% of months; a book at 1.63 wins 68% of months; skew term
of utility at 10% vol = -0.006% a year for log utility at skew -0.65, 0.16% a year at risk aversion 10 for a skew
difference of 0.3; data ratios 1.05 and 1.57 from the textbook efficiencies 3/pi and 2/pi (not from the pack); about
22 = 5% of 432; 83 = rows of section 9 (5 + 3 + 8 + 1 + 12 + 54).

Corrections made during the check. The first draft took from claim text and map "ten times the emphasis on risk
control", "about 70 markets", "80% trend", "about 40% winners", "10-20 years of data" and "constant size from entry to
exit"; none is in a quote and all were removed. C13-4 was first read as a measured hit rate; it is a ceiling on knowing
direction, with no horizon. C06-4 was first cited for "resizing cuts the position with the trend"; the quote stops
before that. "55% non-trend" became 40% convergent, since the econ family is trend-like in U02's split. "Expected
utility ranks like Sharpe" was too strong: it holds for log utility, less at high risk aversion. The names Gauntlet,
Mandelbrot and LTCM are in no quote and are not used as the speakers' words. C13-1 is followed as corrected (Seibert);
C09-3 is cited with its speaker doubt. Quotes are given in the captions' spelling ("Mar reversion", "escore").

Strongest counter-argument to the verdict: Eckhardt co-wrote the Turtle rules (the map's role field; no quote) and a
"we have found" from a firm that says it spends as much time breaking systems as building them may be worth more than
blog backtests of a different kind of system (Carver's comparison is his own continuous system against a static one,
U02 section 3); and a Sharpe bar is a normal-theory yardstick of the kind he says to avoid (C12-1). The quote-only
rule of this run also throws away claim text that is probably faithful to the transcript: under the practice of
U02-U07 (claim text used, marked) the unit would look far more specific. Conversely, a unit with no number,
undisclosed methods and a map this unreliable cannot move a prior, whatever the speaker's standing.

Strongest counter-argument to T1: our book has no entries. An "episode" defined by the 12-month sign is my construct;
ETC speaks of trades (C05-2), which the pack describes as sized once and stopped out (not in a quote), so a null on
a book without entries says little about them. R is mechanically tied to recent absolute returns, which also drive
the signal, and after a spike current vol overstates next month's (C07-2), so "return per unit of current vol" is
biased down; the realised-vol column mends that only ex post. And it is one more look at design-period returns that
shapes how a registry level is read: logged, but a mild selection step.

## 9. Pack problems

Kinds: Q = contradicts its own verbatim quote; P = contradicts another pack statement (no quote decides); S = speaker
or attribution; R = record; U = not in the quote: it may be in the transcript, cannot be verified here and is not used
in sections 1-8. 83 rows: Q 5, P 3, S 8, R 1, U 66 (12 map statements or tags, 54 claim fields). Rows 30-83 are one
per claim; with row 2, every one of the 55 claim fields says more than its quote or contradicts it. Whether or not
any were planted, rows 1-16 are of the three kinds U06's reader test names (an altered number, an inverted
mechanism, a swapped speaker; U06 section 6).

Contradictions, speakers and record (rows 1-17):

| # | Kind | Location | The pack says | The quote (or the other pack statement) says |
|---|---|---|---|---|
| 1 | Q | C12-2 claim; Eckhardt premise 8; chain "Heavy tails" step 2 | robust statistics need "2-3 times" ("two to three times") more data | "you need 10 20 time 30 times as much data" |
| 2 | Q | C07-X1 claim and conditions | resizing is "always" a hidden mean-reversion trade; "holds by definition for any open trend position" | "that is not always true by definition but ... true in my experience more often than not" (Seibert premise 3 in the map has it right) |
| 3 | Q | Santino premise 4 | systems can have "a strong 2-4 year run" | C09-4: "a two three four month really strong run"; the claim field says month |
| 4 | Q | Eckhardt premise 12 | futures prices mean-revert over short horizons, volatility does not; the non-trend methods are mean-reversion trades on price | C07-2: "it's volatility that mean reverts uh price doesn't doesn't mean revert at least Futures prices"; the claim field, disagreement 3 and gap 5 follow the quote |
| 5 | Q | Eckhardt chain "Why published rules decay" step 1 | breakout systems had already degraded, then the rules were released because little edge was left | C05-4: "heavily degraded since we let the turtles go and ... this information got revealed": order reversed, motive in no quote |
| 6 | P | Eckhardt decision process, universe | "about 120 futures markets" | "about 70" in the C10-3 claim, episode thesis, premise 16, disagreement 2, current view 2; the quote has no number |
| 7 | P | Eckhardt premise 13 | "prefers a roughly 60% success rate" | about 40% in the C13-3 claim, chain 3, decision process (risk), gap 1, reader inference 2; the quote has neither |
| 8 | P | Eckhardt decision process, sizing | "scale the whole portfolio to a volatility target" | no portfolio volatility target in the C06-3 claim, episode thesis, chain 4 step 3, Santino premise 2 and decision process, disagreement 1, gap 3; quote: "we don't want to restrain it" |
| 9 | S | C09-3 speaker field | Bill Eckhardt | the quote speaks of him in the third person ("bill has spent as much time ... as we do"): another ETC speaker; the map cites it under both men |
| 10 | S | C13-1 speaker field | Rob Santino | its own correction, gap 6 and Seibert's speaker note ("applied correction") say Moritz Seibert; the field was not changed; the correction's evidence ('and Rob maybe to your point') is in no quote |
| 11 | S | Eckhardt chain 4 step 1 | the hidden mean-reversion trade is "Eckhardt's point" | the claims cited are Santino's (C06-4) and Seibert's (C07-X1, "in my experience"); no Eckhardt claim states it |
| 12 | S | Episode thesis; Eckhardt premise 1 (cites C14-2) | Eckhardt treats discomfort as the real edge ('pain arbitrage') | C14-2: speaker Seibert |
| 13 | S | C12-1 claim; Eckhardt premise 7 support; chain 2 evidence; C12-X2 | Mandelbrot's cotton work is Eckhardt's evidence (C12-1, premise 7) and "cited by the host" (chain 2, C12-X2) | no quote names Mandelbrot, cotton or a missing variance |
| 14 | S | Gap 3 | "He ... says volatility enters ETC's systems five or six ways and that range-based measures exist" | C06-2 is Santino's; the ATR remark is Seibert's claim text (C12-X3) and in no quote |
| 15 | S | Gap 4 | "He says ETC moves from short-term systems for alpha decay"; Eckhardt calls 4-5-day trades 'short only relative to other traders' | C05-3 is Seibert about "they", not ETC; C05-2: "we have shortterm ... systems"; the phrase is in no quote |
| 16 | S | Eckhardt speaker note; Santino role | which ETC speaker answers the sizing questions is unclear (kept as Santino); Santino is "president and CEO" or "COO" | self-flagged and unresolved in the pack |
| 17 | R | C03-R1, C08-R3, C10-R2 | listed among the claims | no quote_check field: the three quotes were not script-checked |

Map statements and tags that no quote supports (rows 18-29):

| # | Kind | Location | The pack says | The quote (or the other pack statement) says |
|---|---|---|---|---|
| 18 | U | Eckhardt decision process, research | "hold back the most recent three years as an untouched out-of-sample test" | the cited C12-1, C12-2, C08-3 say nothing of it; it also sits against current view 4 (nothing can be inferred from two or three years) |
| 19 | U | Eckhardt decision process, sizing; chain 4 step 2 | "stop-loss for each trade"; "exit with a stop loss" | no ETC quote names a stop; C14-1: "get out of your losses"; C07-1 (Seibert): "controlled risk" |
| 20 | U | Eckhardt premise 4 support; episode thesis | 51-52% is "ETC's measured hit rate across its systems and markets over decades" | C13-4: "you almost never know better than about 51 or 52% which way the Market's going": a ceiling, no measurement, no horizon; the map's own evidence_style says he gives no performance data |
| 21 | U | Gap 2 | "Eckhardt says he knows of no one who does curve fitting" | the cited C08-3, C09-1, C08-R3 do not say it; C08-R3 (unchecked): "curve fitting is simply the wrong term" |
| 22 | U | Eckhardt chain 5 step 2 | the long-term edge persists "where it is harder to arbitrage" | C05-3, C05-X1 give no reason |
| 23 | U | Eckhardt chain 6 step 1 and fails_when; Santino premise 5 | replication "fits index returns with 10-20 markets"; Santino: 'it will end badly', 'I'll go on record' | C12-X1: "that's probably not going to have a good ending"; no number, neither phrase |
| 24 | U | Eckhardt decision process, portfolio; episode thesis | ETC does not replicate CTA indices | no quote on ETC's practice, only C12-X1's opinion |
| 25 | U | Forward-looking inputs | replication products will end badly "in a tail event" | C12-X1 gives no mechanism |
| 26 | U | Santino premise 4 support; Santino decision process | the Gauntlet is "offered to outside ideas and University of Chicago students"; the E-score matters "especially when blending systems" | C09-3, C09-4 say neither |
| 27 | U | Seibert decision process | initial sizing and many small positions are the main risk control; correlations, volatility and VaR; "overtrading is the main risk" | the cited C07-1, C07-X1 say none of it |
| 28 | U | Disagreements 1 and 3 | Seibert "asks whether markets are normalised to a common volatility target" and "whether ETC's non-trend add-on is mean reversion or carry" | no quote holds either question; disagreement 3 cites only C07-2, an Eckhardt claim; in neither entry do the positions conflict |
| 29 | U | Mechanism tags | C05-2, C05-3, C05-X1 "slow_reaction"; C05-5, C07-2 "cycle_persistence"; C11-2, C11-3 "structural_shift"; C13-3 "risk_premium" | the quotes state no such mechanism (trade length; decay; a denial of reversion; a standing difference, not a shift) |

Claim fields that say more than their quote, with the map statements that repeat them (rows 30-83):

| # | Kind | Location | The pack says | The quote (or the other pack statement) says |
|---|---|---|---|---|
| 30 | U | C01-1 | normal reflexes put you among the many; trading requires suffering; premise 1 support: a party anecdote | "money flows from the many to the few so you have to be among the few" |
| 31 | U | C01-2 | "entry" rules; attitudes to profit and loss; Dennis ran risk control, Eckhardt developed rules (also disagreement 4) | "there's more to trading than Simply Having rules you have risk management" |
| 32 | U | C02-1 | Dennis's 'weighted rules' view | "it was much harder to mechanize what is needed for trading" |
| 33 | U | C02-2 | a theory built "from the philosophy of science" | "I have formalized certain parts of trading in a mathematically rigorous fashion" |
| 34 | U | C03-1 | ballistics; factors added as research proves them | "you have to oversimplify a problem sometimes in the beginning" |
| 35 | U | C03-2 | markets "are not random"; too close "to random"; "simple" predictions | the quote stops at "it's too close" |
| 36 | U | C04-1 | decide what to do wherever the market goes; profit follows from risk control | "focus on risk control because ... you can know your risk ... change your risk ... control your risk" |
| 37 | U | C04-2 | ETC uses a small class of utility functions suited to commodity trading and clients | only the shrinking gain and growing loss per dollar |
| 38 | U | C04-3 | "most traders"; ETC brings expected utility in at the ground floor and judges every idea by it; premise 6: 'Island of Dr Moreau', 'all other traders that I know of' | "they graft risk control almost as an afterthought on ... their profitability system" |
| 39 | U | C04-4 | risk-neutral utilities too; the St Petersburg paradox | only "the risk loving ones ... financially suicidal" |
| 40 | U | C05-1 | leverage; risk-loving traders repeatedly lose everything | "one has to be risk averse that's the only thing that ... can work in this business" |
| 41 | U | C05-2 | average trade lengths up "to 50-60 days" (also decision process, forward-looking inputs) | "trades that ... have a ... four or five day average length" |
| 42 | U | C05-3 | the movers are "many Turtle students" (premise: and "systematic diversified trend followers") | "they have moved over to longer term hold periods" |
| 43 | U | C05-4 | the rules are breakout systems; degraded "by competition"; Eckhardt changed systems before the release; premise 14: a Turtle published the manual | "they've been heavily degraded since we let the turtles go and ... this information got revealed" |
| 44 | U | C05-5 | declared dead every few years; most of ETC's work is still trend (thesis, decision process, current view 1: "about 80%") | "the death of trend following has been highly exaggerated" |
| 45 | U | C05-X1 | "around 200-day look-backs" | "two and a day time frames" (a caption garble; 200 is a reconstruction) |
| 46 | U | C06-1 | Red Queen effect; competition and technical-analysis knowledge; premise 15: 'Alice in Wonderland' | "one has to keep researching to stay ahead of it" |
| 47 | U | C06-2 | the ways are sizing, measuring price change and risk control, "alongside price" | "about five or six different ways" |
| 48 | U | C06-3 | no portfolio volatility target; no wish to "juice up when volatility is low"; each future's vol tracked for risk | "increased volatility often helps us we don't want to restrain it" |
| 49 | U | C06-4 | size kept roughly constant from entry to exit; readjusting would cut the position with the trend; "counterproductive"; chain 4 evidence: "tested"; Santino: "small technical adjustments" | the quote ends "if we were readjusting to volatility we would" |
| 50 | U | C07-1 | the subject is constant sizing with a stop-loss; "volatility-seeking" | "which means controlled risk and therefore a sythetic long optionality profile" |
| 51 | U | C07-2 | "non-trend methods (about 20% of work) are not mean reversion" | only that volatility mean-reverts and futures prices do not |
| 52 | U | C07-3 | a moving average as the poor summary; the 20-day high and low; position within the range; premise 10: 20 closes into 1 or 2 numbers | "instead of boiling all the structure down into one number you're keeping some of the structure" |
| 53 | U | C08-1 | keeping all structure is "combinatorially impossible" | "eliminate a lot of the structure but ... keep enough of it" |
| 54 | U | C08-2 | volatility is a moving-average process, price is not; moving averages and crossovers on price are counterproductive; premise 11: "no theoretical support", a gold-and-silver quip | "it's appropriate to estimate volatility using moving averages" |
| 55 | U | C08-3 | some overfitting is inevitable; in-house techniques estimate and minimise it | "fit to the permanent features ... ignore the transitory features" |
| 56 | U | C09-1 | underfitting ignores worthwhile information; good traders lost everything to overfitting | "if you're afraid of overfitting one way is to underfit" |
| 57 | U | C09-2 | the E-score combines many measures (a 'Super Value'); "2 of 20 years"; it "discounts" | "a system might make too much of its money over too short a period ... elements of the escore ... will test for that" |
| 58 | U | C09-3 | "the Gauntlet", a barrage of tests; where a system fails matters as much as why it works; removes emotion | "tearing systems apart as we do putting them together"; the name Gauntlet is in no quote |
| 59 | U | C09-4 | "so scientific testing and emotion removal are needed" | the run, "and then they just go flat or degrade" |
| 60 | U | C10-1 | "it" is the Gauntlet; glitches "nearly impossible to find" otherwise | "it actually tests the program too it can find very subtle glitches" |
| 61 | U | C10-2 | less noise in any run; smaller portfolios can outperform for periods; premise support: diversification is 'free'; disagreement 2: alternative markets are "just markets" | "the more markets we trade the more independent bets we can place" |
| 62 | U | C10-3 | "about 70 markets"; diversification the greatest financial idea of the 20th century; illiquid markets avoided | "we measure the liquidity and the trade slippage for all markets that we trade whether we're considering trading" |
| 63 | U | C10-X1 | "despite its proven value" | the quote carries the rest |
| 64 | U | C11-1 | the reasons: slippage and difficulty exiting in a hurry | "on paper ... might appear better but in practice I I think they're actually worse" |
| 65 | U | C11-2 | "single" stocks; splits, dividends; relative advantage; premise 18: 'no claim of expertise' | "stocks don't really have the kind of robust Trend component that Futures tend to have" |
| 66 | U | C11-3 | stock markets are dominated by longs; "different processes" | only the futures half: "exactly one long for every short" |
| 67 | U | C11-4 | replication by regression 'sounds like an invitation to really overfit' (given in quotation marks); "radically" | only that price changes and system trades "are not normally distributed" |
| 68 | U | C12-1 | Mandelbrot, possibly no variance; small-sample normal statistics wrong; standard deviation and least-squares correlation unreliable | "avoid normal techniques ... use ... robust or distribution free statistics" |
| 69 | U | C12-2 | ETC needs 10-20 years of data; nothing can be concluded from two or three years (also decision process, current view 4, forward-looking inputs) | the quote has only the 10-30 times |
| 70 | U | C12-3 | the firm is LTCM; "despite fat tails" | "they" are not named |
| 71 | U | C12-X1 | "regression-based CTA-index" products; indicator "ETFs" | "on the replication question" |
| 72 | U | C12-X2 | Mandelbrot's cotton work; stable Paretian; no defined variance; premise support: 'Misbehavior of Markets' | "it is definitely tailed in both directions it is prone to jumps" |
| 73 | U | C12-X3 | "for sizing"; range-based measures such as ATR are not standard deviations | "many people would calculate volatility as a function of standard deviation under the assumption of normal distribution ... you're back" |
| 74 | U | C13-1 | replication portfolios lack predefined exits; discontinuity and gap events; gap 6: "Eckhardt agrees wholeheartedly" | "keeping these losses small is what keeps you in business" |
| 75 | U | C13-2 | "all futures markets"; trading rules must intervene | "the left hand tail the one that represents losses is very heavy" |
| 76 | U | C13-3 | the strategies sell cheap options; ETC rejects any new system at 70-80% and prefers about 40% with larger winners | "they make money 70 80 90% of the time but then they're subject to large freakish losses" |
| 77 | U | C13-4 | "ten times" the emphasis on risk control (also chain 1, decision process) | only the 51 or 52% |
| 78 | U | C14-1 | normal human attitudes are "dead wrong" | "get out of your losses ... let your profits run" |
| 79 | U | C14-2 | "the trend follower's edge"; individual losses kept small | "this pain Arbitrage of sticking to your system during bad times" |
| 80 | U | C15-1 | the drop-outs were Turtle trainees; some "could not get along" | "there were some who dropped out ... fairly soon" |
| 81 | U | C03-R1 | the other party is Dennis; they disagreed throughout the Turtle years; 1980s | (unchecked) "between the two of us I was the more risk averse Trader" |
| 82 | U | C08-R3 | a nonlinear-regression term; 'overfitting' preferred; so underfitting exists | (unchecked) "curve fitting is simply the wrong term" |
| 83 | U | C10-R2 | would like to publish parts of the Gauntlet; has published nothing specific | (unchecked) "this is an industry where we have to keep secrets" |
