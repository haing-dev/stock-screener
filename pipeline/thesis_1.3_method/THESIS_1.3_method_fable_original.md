# Thesis note 1.3c: testing method (QP13, Stine 2009)

Ground truth: slide text and claim quotes. Labels: SHOWN, SHOWN (words), ASSERTED, reader. Numbers: in quote, on slide, summary only, repo result (design era), computed. No 2011-2026 figure is used.
Dating: pack header "(slides: Bob Stine, Wharton 2009)"; data end February 2009 (QP13-C06-1); the test is cited as "Foster, Stine, Young (2008)" (QP13-C45-2), the dice game as "Amer Statistician, 2006" (QP13-C16-2). All before 2011.

## 1. Verdict

1. QP13 firmly establishes one thing: a test of no skill that assumes only a zero expected specific return (the return left after the market's part is taken out) and keeps false alarms at 1 in 20, even against a made-up fund with steady gains and a hidden total loss (SHOWN: stated inequality, constructed example). Its price is not quantified: the tested stream must multiply by 20.
2. The rest is asserted, or shown on dice and four hand-picked assets.
3. Supported in our sheet: whole-month resampling instead of a t table; counting candidates; alpha against what is already held; registered checkpoints; sizing below the growth optimum; the holdout read as a screen.
4. Contradicted: citing these slides for the tail test (their own fund passes it until the loss comes) and the name Foster-Stine on a regression t-test. A one-year criterion is cut against.
5. Added: take market exposure out before judging the book; alpha earns a pod some amount, not by itself an equal share; the error budget covers only losses that show on the window.
6. Four protocol items (P1-P4, no new decisive test), one diagnostic (M1). The martingale test is dropped: as held it could detect only a Sharpe gap of about 0.84 on the design window.
7. Weakest link in the source: the scale (leverage) of the tested stream is never discussed, yet it sets the verdict; power is not shown.
8. Weakest link in our sheet as the slides see it: every guard against "many small gains, rare big loss" reads only losses that already happened.

## 2. What the slides establish

| Statement | Label | Ids | Carrying words or numbers | Limits |
|---|---|---|---|---|
| A stream whose specific return has zero mean given its past has at most a 1 in 20 chance of ever multiplying by 20 | SHOWN (inequality stated, not derived) | QP13-C39-1, C39-2, C39-3, C39-4 | "(not nec. iid)"; "Compound returns are non-negative martingale"; "have to exceed 20 during observed period" (20 in quote) | Needs a value that cannot go negative, a known fixed beta, a scale; none tested |
| A fund with steady gains and a rare total loss reaches that bound: it fools the test 1 time in 20 at most | SHOWN (constructed) | QP13-C44-1b, C44-2, C43-3 | "For any choice of k" (on slide C44); "protects against the “until it happens” unobserved volatility" | One made-up process; exact only if 20 can be hit (0.0485 at k = 19, computed) |
| On four assets the t-test calls every alpha significant; the martingale test rejects for one | SHOWN (words); t values on slide | QP13-C36-1, C41-1 | t 2.7, 3.1, 5.5, -2.6 (on slide C36, rows read by order); "Only Berkshire Hathaway rejects the null, and then we have to consider multiplicity." | Four hand-picked series, two unexplained (Bob, TEAM): it can happen; nothing on how often |
| The t-test's p-value is doubtful: fat tails, dependent residuals | ASSERTED, with charts | QP13-C38-1, C38-2, C32-1 | "far from Gaussian, with large outliers (fat tails)"; "Evident lack of independence in CAPM residuals" | No size of the error; residual shapes are summary only |
| Multiply the p-value by the number of candidates considered | ASSERTED | QP13-C43-1, C43-2, C45-2b | "Multiply the p-value from martingale test by number of assets considered."; "hard to “count” the considered alternatives" | No derivation; harsh for near copies (reader) |
| Long-run growth is about mean minus half the variance: a bet with a 71% mean loses almost surely; a mix of two failing bets can grow | SHOWN (constructed dice) | QP13-C20-1, C19-1, C21-1 | "If the r t are independent over time, then"; -0.16 for Red (on slide C20); 0.14 for the mix (on slide C21) | Approximate (exact -0.17 and 0.17, computed); independent bets, fixed odds |
| To maximise long-run wealth, hold excess mean over variance | ASSERTED (no derivation) | QP13-C25-1, C25-2, C23-1b | "p = 0.075/0.040 = 1.75" (on slide C25); "Example suggests we’re more risk averse…" | The division gives 1.875 (computed). The author's cautions: independence, stable odds, known parameters; no rule for real assets |
| Take the market out first; a non-zero alpha (average specific return) means hold some amount | ASSERTED (theory) | QP13-C04-2, C27-2, C30-2 | "Remove market performance (CAPM)"; "Buy (or sell) some amount of it" (on slide C30) | One market, one fixed beta; nothing on a multi-asset long/short book |

An inequality holds under its assumptions; a constructed example shows what can happen; four assets say nothing about how often.

## 3. Element by element

| Element, in the pack's words | What QP13 says | Consequence |
|---|---|---|
| Bootstrap (TESTING_PROTOCOL test 1): "Paired stationary bootstrap of the Sharpe difference" | Silent on the bootstrap and on Sharpe. Supports its reasons: the t table is doubted (QP13-C38-1); dependent observations mislead (QP13-C28-2). Adds a limit: resampled months hold no loss that has not happened (slide C04, "Just because it has not happened") | P3 |
| Multiplicity (TESTING_PROTOCOL 3): "Holm's step-down correction is applied over every challenger in the batch"; WORKFLOW 6: "at most 2.5% probability" | Supports counting (QP13-C43-2), and a wider count than what is shown (slide C43, "I bet that you have considered more than 4"): the research log. Silent on Holm, selection inflation, deflated Sharpe | none (11.3, 11.4) |
| Tail (TESTING_PROTOCOL test 5): "max fall not worse by more than 2 points and worst month not worse by more than 1 point" | Supports the worry (QP13-C04-3). Contradicts the citation: no slide has a fall statistic, and the slides' fund shows no loss until "busted!" (slide C44), so it passes this test until then (reader) | P1, P3 |
| Placebo (WORKFLOW 5): "signal dates shuffled in blocks, keeping the same average long/short exposure" | Silent. Reader: a constant hidden-loss exposure earns the same in its placebo and cannot beat it; a timed one is not covered | none |
| Double costs (TESTING_PROTOCOL test 4): "dSR at twice the costs on the window" | Silent: no slide mentions costs | none |
| Power check (WORKFLOW 3.3): "simulated pods with known true Sharpe (0, 0.2, 0.4)" | Silent on power, beyond calling the test tight for one bad process (QP13-C43-3). Adds a null the simulation lacks: zero mean with a hidden loss (QP13-C44-1b) | P2, P3 |
| Holdout (WORKFLOW 6): "net Sharpe >= 0.3, worst fall > -25%, correlation with the S&P <= 0.3, 2022 positive"; TESTING_PROTOCOL 6: "it does not prove skill" | Supports the screen reading (QP13-C22-2). Adds: take the market out first (QP13-C04-2; P4). Cuts against a one-year criterion (slide C04, "One good year ≠ continuing success"; pass chance 0.46 at true Sharpe 0, 0.67 at 0.5, repo result). Silent on falls | P4, M1; criteria unchanged |
| Sizing (WORKFLOW 5.1): "Core pods at equal risk, volatility target, caps"; TESTING_PROTOCOL 1: "10% vol target" | Supports holding less than the growth optimum (QP13-C25-2). Silent on targets and caps. Contradicts equal risk only if Sharpes are known (QP13-C25-1), which it denies (QP13-C23-3). Section 5 | P2 |
| Adds to the book (WORKFLOW 5): "alpha against the Core book"; TESTING_PROTOCOL: alpha t, "the Foster-Stine value-add test" | Supports the question (QP13-C27-2). Limits the answer: alpha means "Buy (or sell) some amount of it" (slide C30). Doubts a t-table p-value (QP13-C38-1). Contradicts the name: the test of "Foster, Stine, Young (2008)" is the martingale test (QP13-C45-2) | P1, P2 |
| Live promotion (WORKFLOW Q): "promotions only at registered checkpoints with stated sample sizes" | Supports (QP13-C22-2). The bound covers every look (QP13-C39-3) but asks for 20 times: 32 years at Sharpe 1.0 and 10% volatility (computed) | none |

No row for version averaging or economic size (silent); slide C28 ("But the sign changes!") speaks for the era test.

## 4. The martingale test as a check for this shop

**Assumptions.** (1) With no skill the specific return has zero mean given its own past; no normality or independence is needed (QP13-C39-1). (2) The compounded value cannot go negative (QP13-C39-2): no period may lose more than 100% at the scale tested (reader). (3) Beta, the stream's sensitivity to the market, is known and fixed (QP13-C40-1). Our streams meet (1) and (2) at the scale held, and (3) only where beta is fixed by construction.

**Controls.** False alarms: at most 1 in 20, hidden losses included (SHOWN). Not controlled: missed real effects (no power figure on any slide); the size of a tail (a real mean with a ruinous tail passes; reader); a wrong beta; an understated count.

**Open choices.**
- Market and beta. Slides: the whole-market index (slide C12). Rule: for a pod the Core book; for a challenger the incumbent, with beta fixed at one (the plain difference), so nothing is estimated. Reason: the slides take out what is already held (QP13-C27-2).
- Frequency, look-ahead, count. The bound does not depend on the number of observations (QP13-C40-2): monthly here. Rule: any fitted beta uses an expanding window (WORKFLOW 5). Count: pods in the batch; for the whole book, runs in the research log (QP13-C43-2).
- Scale. Not closed, and it cannot be. The slides compound each asset as held; the test slides never mention leverage. For a long/short stream the scale is free, and it sets the result. Only the scale held needs no knowledge of the worst loss (reader, from assumption 2); scaling a small stream up assumes its worst month is known, which unseen volatility denies. A scale fitted to the sample (QP13-C25-1) is look-ahead.

**Detectable size (computed).** Formula: the value after n months is about (1 + mean - variance/2)^n (slide C20). Bar: 20 (QP13-C39-4), times the count. Inputs: 432 design months; 10% yearly volatility, so a monthly variance of 0.01/12.
- A whole stream at 10%: a typical path reaches 20 only at Sharpe 0.89; 1.27 with a count of 4; 1.86 with 32; 1.97 on the 189 holdout months.
- At the best possible scale (QP13-C25-1 put into slide C20: growth is half the squared Sharpe): 0.41, 0.49, 0.60, with the Sharpe known in advance.
- A challenger-minus-incumbent stream as held: a gap of 8.4 points a year, a Sharpe difference of 0.84. The registered minimum is 0.05. The largest on record, +0.118 with Holm p 0.0036 (repo result), compounds to about 1.5.
- The candidate book compounds to about 143 (11.6% a year for 15 years, then 17.1% for 21; repo result): p 0.007, and 0.22 after 32 logged variants. At a 15% target the same record gives 0.019. The volatility convention sets the verdict.
- The slides' own case: Bob has t 5.5 and fails, because 0.0016 a month (on slide C36) over about 350 months is 1.75. The test rewards wealth made, not smoothness.

**Relations.** The bootstrap assumes the window's months stand for the future; the martingale test does not, and pays with power. It measures no tail, so it cannot replace the tail test. The placebo has another null (timing against average exposure): a steady true premium fails it and could pass the martingale test.

**Status: dropped** as a decisive test and as a reported line (D1-D3, section 8). Its lesson is kept in P3.

## 5. How much to hold

**What the slides give.** SHOWN on dice: growth is about mean minus half the variance, and mixing independent bets raises it (QP13-C20-1, C21-1). ASSERTED: the growth-best holding is excess mean over variance (QP13-C25-1), with the remark "Example suggests we’re more risk averse…" and the author's cautions (QP13-C23-1b).

**The 10% target.** Put QP13-C25-1 into slide C20: growth at volatility v is S times v minus half v squared, best when v equals the Sharpe ratio S (computed). So 10% is growth-best only at a true Sharpe of 0.10 and loses wealth only below 0.05. Supports the target as cautious, in words only; no change.

**Equal risk.** The sizing rule gives each bet risk in proportion to its Sharpe (computed). Equal risk treats all Core pods as equally good. The slides say the parameters are not known (QP13-C23-3) and give no rule for that case: silent. One consequence follows. Alpha above zero earns "some amount", not by itself an equal share. With four independent pods, a fifth raises the book's Sharpe at equal risk only if its own Sharpe is above 0.236 (root 5 minus 2) times the book's: 0.29 against a book at 1.23, 0.12 against 0.5 (computed with slide C21's rule for a mix). A pod with no alpha costs the book about a tenth of its Sharpe. P2 reports this number without making it decisive: against the design Sharpe of 1.46 the break-even is 0.34, and a pod at 0.4 adds only 0.025.

**Holdout criteria, caps, switching.** The Sharpe mark is supported as a screen and gets the market line (P4); a correlation cap is not a removal (QP13-C04-2); the one-year criterion is cut against (section 3). Worst fall, caps and no switching: silent, but for the remark "Leverage was good until lately" (slide C04). No criterion changes.

## 6. Protocol items for step 3.4

**P1. Two citations (TESTING_PROTOCOL section 2). Wording only; no test changes.**
> Test 5: Tail (realised falls not materially worse; Harding 2002). The profile "many small gains, rare big loss" is the worry of Stine 2009, slides 4 and 44; this test sees such a loss only if it happened on the window.
> Reported list: Newey-West (6 lags) alpha t-stat of the challenger-minus-incumbent return against the incumbent (the usual regression test of alpha; Stine 2009, slide 38, doubts its p-value).

Reason: QP13-C44-1b, C38-1, C45-2. Pass chance unchanged; nothing to simulate.

**P2. Test 1 for a new pod: alpha with a bootstrap p-value; the Sharpe difference at the size held is reported (TESTING_PROTOCOL section 2, new paragraph). Decisive: it is WORKFLOW test 1 made exact; no test is added.**
> New pods. Test 1 statistic: the intercept (alpha) of the least-squares regression of the pod's monthly net return on the Core book's monthly net return over the window. p-value: one-sided, H0 alpha <= 0, from the centred stationary bootstrap of test 1 (whole months, same blocks, seed and resamples; the regression is re-fitted in every resample). Pass: Holm-adjusted p below 0.025 inside the batch. Reported, not decisive: the Sharpe difference between the Core book with the pod at the risk share of step 5.1 and the Core book without it, with the per-era lower bounds of test 3.

Reason: for a new asset the slides ask the alpha question (QP13-C27-2; slide C30) and doubt a t-table p-value (QP13-C38-1). The market is the Core book: the slides take out what is already held. The p-value does not depend on the pod's scale. 0.025 keeps two batches at 5%. Alpha earns only some amount (QP13-C25-3), so the result at the size held is shown. Existing cover: WORKFLOW names the statistic but no p-value; the tail test already judges the book at the size held. Pass chance: set by this text and measured in the power check. Power check: pods at true Sharpe 0, 0.2 and 0.4 against a Core book at true Sharpe 1.23 (1.46 less 0.23, repo result) and 0.5; pass rates, and the share of adopted pods whose true Sharpe difference at the size held is below zero.

**P3. What the error budget covers (TESTING_PROTOCOL section 3, new paragraph). Reported-only.**
> Scope. Error rates here are computed from the months on the window. They do not cover a pod with steady gains and a loss rarer than the window (Stine 2009, slide 44): if the loss has chance q a month, independently, n months show none with chance (1 - q)^n, and every test here then reads the pod as a good one. Computed row in the step 3.3 table: the true-Sharpe-0.4 pod plus a loss of n times its monthly mean with chance 1/n a month (true mean zero) is adopted at least (1 - 1/n)^n times as often as the 0.4 pod. Each pod spec names the event in which its mechanism loses most and the window months in which such an event occurred; a spec with none is flagged "loss not seen" on the result sheet and in the verdict line. The flag does not change the verdict.

Reason: QP13-C04-3, C44-1b, C44-2. Existing cover: none (this note, section 3: bootstrap, tail, placebo). Pass chance unchanged. Power check: the computed row, 0.37 times the pass rate of the 0.4 pod at n = 432.

**P4. Market-removed Sharpe of the book (TESTING_PROTOCOL section 2 reported list; section 6). Reported-only.**
> Specific return of the book: w = r - b x m. r is the book's monthly net return in excess of cash. m is the monthly excess return of the S&P 500 (and of the US 10-year bond if diagnostic M1 says so). b is the least-squares slope of r on m, with intercept, over all months from 1975-01 to the month before; first value in month 37. Reported: the annualised Sharpe of w next to that of r, on the design window from 1978-01, in the holdout report and in each quarterly review. The holdout verdict quotes both. The registered criteria do not change.

Reason: QP13-C04-2, C30-1; slide C45. At the correlation limit the market part of the Sharpe is 0.3 times the S&P's Sharpe over the same months: 0.11 at the slides' long-run 0.375 (7.5% over 20%, slide C15), the whole 0.3 mark if it were 1.0 (computed). Choices: the S&P 500 because the registered criterion names it (bonds: M1); an expanding window against look-ahead (WORKFLOW 5); no scale, since a Sharpe has none. It takes out the pay of a steady exposure, not of a timed one or of other markets. Existing cover: the correlation criterion caps the exposure without taking its return out. Pass chance unchanged. Power check: nothing.

## 7. Diagnostics

**M1. Which markets must be taken out of the book's return?** Zero slots, design months.
- Computation: build the specific return of P4 twice for the incumbent book of Batch A2, with the S&P 500 alone and with the S&P 500 and the US 10-year bond together. Report the Sharpe of the raw return and of both series for 1978-89 and 1990-2010.
- Data: monthly net returns of the book; monthly excess returns of the S&P 500 and the US 10-year bond from the engine panel (the pair of charter diagnostic D3).
- Gate, fixed now: if in either era the two-market Sharpe is lower than the S&P-only Sharpe by 0.05 or more, P4 uses both markets; otherwise the S&P 500 alone. 0.05 is the smallest Sharpe difference the protocol treats as real ("below this a gain is within cost-estimate error").
- Either outcome only defines a reported line. Logged as a design-data run (step 7.1).

## 8. Dropped

- D1 Martingale test as a fifth decisive test: as held it detects a Sharpe gap of 0.84; every simulated pod would fail.
- D2 Martingale number as a reported line: about 1.5 against a bar of 20 for the best challenger on record; for the whole book the volatility convention sets the verdict.
- D3 Scaling the tested stream up: look-ahead if fitted to the sample; valid from an expanding window, but its rules would be mine and it assumes a known worst month.
- D4 Sharpe difference at the size held as the decisive pod test: against the design Sharpe of 1.46 a pod needs an in-sample Sharpe above 0.34 to show any gain (computed); it would judge the incumbent's record, not the pod.
- D5 Bonferroni for Holm: only asserted ("Bonferroni does fine"); Holm guards the same error (author's knowledge).
- D6 Sizing by estimated excess mean over variance, or a higher target: against the slides' own cautions.
- D7 Demoting the 2022 criterion: registered; a relaxed bar raises false passes.
- D8 Beta from daily data: the slides' own caveat; our exposures change monthly.
- D9 Simulating a hidden-loss pod: the identity in P3 answers it. A decisive flag: it would rest on a judgement.

## 9. Numbers used

- In quote: 20 (QP13-C39-4); 710 months to February 2009 (QP13-C06-1); t 3.12 (QP13-C31-2).
- On slide: level 0.05 (C39); 1/20 and k = 19 (C44); t 2.7, 3.1, 5.5, -2.6 and alpha 0.0016 (C36; loose cells, rows read by order, checked against 2.68 on C35 and 3.12); beta 0.56 (C35); 7.5%, 20%, 71% (C15); -0.16 (C20); 0.14 (C21); 1.75 (C25).
- Summary only, not used: the martingale maxima (QP13-C41-1); the fund slope and t (QP13-C28-1).
- Pack parameters: 432 and 189 months; 10% target; 0.05; 0.025.
- Repo result (design era): +0.118; Holm p 0.0036; growth 11.6% and 17.1%; 32 variants; 1.46; 0.23; 0.46 and 0.67.
- Computed: 0.0485 = (19/20)^59; -0.17, 0.17, 1.875; 0.89, 1.27, 1.86, 1.97; 0.41, 0.49, 0.60; 8.4 and 0.84; 1.5; 143, 0.007, 0.22, 0.019; 1.75 for Bob over about 350 months (reader: 1980 to February 2009); 32 years; 0.10, 0.05; 0.236, 0.29, 0.12, 0.34, 0.025, a tenth, 1.23; 0.37; 0.375, 0.11; 5% and 10%; 5.3%.

## 10. For the Opus check; what the slides leave unanswered

Check first: (1) Is the book's return in excess of cash? P4 and the 143 depend on it. (2) The break-even of section 5 assumes independent pods; does step 5.1's equal risk apply to the four existing pods? (3) The row order of the table on slide C36. (4) Whether a Foster-Stine value-add test exists outside this pack. (5) P3's computed row. (6) M1: the bond series and the 36-month start.

Unanswered by the slides: the scale of the tested stream; its power; the market for a multi-asset book; a beta without look-ahead; costs; counting near copies; sizing with unknown parameters; any test of "does not hurt"; falls.

## 11. Pack problems

1. TESTING_PROTOCOL test 5 cites Stine 2009 for a fall statistic; no slide has one (P1).
2. TESTING_PROTOCOL names the Newey-West alpha t "the Foster-Stine value-add test". On the slides the test of Foster, Stine and Young is the martingale test (QP13-C45-2); the regression t-test is the "Usual Test of Alpha" (slide C35), which slide C38 doubts. Newey-West is on no slide.
3. WORKFLOW against TESTING_PROTOCOL. (a) Error level per batch: 2.5% against "Holm-adjusted p < 0.05"; over two batches 5% against 10% (computed). (b) Decisive sets: adds, double costs, placebo, tail in WORKFLOW; superiority, size, eras, costs, tail in the protocol ("all must pass"); WORKFLOW reports "the two eras". (c) Test 1: an alpha in WORKFLOW, a Sharpe difference in the protocol (P2). (d) Hygiene: "Test = does not hurt" against superiority for every challenger. (e) "Survives double costs" is not defined for a pod.
4. WORKFLOW 5 still reports "deflated Sharpe from the trial log"; BOOK_FACTS: "it is uninformative here and is no longer cited as evidence".
5. Step 5.1 "Core pods at equal risk" against the candidate's "family shares 45/25/15/15".
6. "the 62 markets" (TESTING_PROTOCOL) against "about 61 distinct markets" (BOOK_FACTS).
7. Inside the slides: 0.075/0.040 printed as 1.75 (slide C25); "(0.06) 2 = 0.003" (slide C20; it is 0.0036); k = 19 with "a bit more than 2% growth" (slide C44), though one gain is 1/19 = 5.3%.
8. Summaries beyond their quote: "(capped at 1)" (QP13-C39-3), "conservative for Gaussian-like returns" (QP13-C39-4) and "(e.g. daily)" (QP13-C40-1) are on no slide; QP13-C28-1 and QP13-C41-1 carry chart numbers absent from the text; the map's "regardless of tails or dependence" drops slide C39's conditions.

## 12. Self-check

- P1: the names may rest on sources outside this pack; then only the reference changes.
- P2: alpha lets in a pod that an equal share makes too big; the loss is bounded (a tenth of the book's Sharpe for a pod with no alpha) but real. Against reporting only: the size held is the size that pays.
- P3: a flag without a consequence can be ignored, while Core pods are sized on a volatility that leaves the unseen loss out. Naming the loss event is a judgement.
- P4 and M1: the S&P 500 is not the market of a multi-asset book; a trend book's equity exposure changes sign, so a fitted slope takes out little; 0.05 is borrowed, not derived.
- Dropping the martingale test: it is the only tool here with a guarantee under hidden loss, and a fixed multiple of the held scale would be valid. But the multiple would choose the verdict.
- No change to Holm, the target, equal risk and the criteria: the slides do not test them; silent is not support.

