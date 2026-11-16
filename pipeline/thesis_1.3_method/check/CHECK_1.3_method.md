# Independent check of THESIS_1.3_method.md (testing method, QP13), Opus 5.5, 2026-11-16

Checked against pack/QP13_slides_text.md (all 45 slides), the quote field of all 72 claims in pack/QP13.json, pack/WORKFLOW_sections_1-6.md, pack/TESTING_PROTOCOL.md, pack/BRIEF_V2_RULES.md, pack/CHARTER_DIGEST.md and pack/BOOK_FACTS_design_era.md. Every claim id (37 distinct) and slide cited exists and was looked up with tools/lookup.py. All arithmetic was recomputed independently in opus_work/recompute.py (output reproduced in the tables). No author scratch file was read.

## 1. Verdict

**PASS WITH CORRECTIONS.**
- Numbers: 87 checked. 8 in quote, 20 on slide, 22 repo or pack values (all match the pack), 37 computed: 36 confirmed, 1 contradicted (the 15% target figure 0.019 is 0.021: the note scaled log wealth by 1.5 and left the larger variance drag out). No summary-only number is used; none not found.
- Statements (8 rows of section 2): 7 supported, 1 partly (row 1 is labelled SHOWN although the slides only cite the inequality), 0 not supported, 0 contradicted; one row (3) lacks a limit (beta estimated on the same data).
- Elements (10 rows of section 3): our own rule quoted correctly in 10 of 10; verdict supported in 8, partly in 2 (multiplicity leaves out the slides' "Bonferroni does fine"; sizing reads a remark as support).
- Proposals: 0 status changes (P1-P4 and M1 stand, D1-D9 stand); precision fixes to P1, P2, P3 and P4; 22 required corrections; 10 open judgement points, none for the user.

## 2. Findings

### Table A: numbers

| # | Number in note | Note's status | Check | Recomputed / source words |
|---|---|---|---|---|
| 1 | 20 (bar) | in quote C39-4 | in quote | "have to exceed 20 during observed period" |
| 2 | 710 months, Feb 2009 | in quote C06-1 | in quote | "Jan 1950 - Feb 2009, 710 months" |
| 3 | t 3.12 | in quote C31-2 | in quote | "alpha= 0.01 with t= 3.12" |
| 4 | 2008 (FSY), 2006 (Amer Statistician) | in quote C45-2, C16-2 | in quote | as quoted |
| 5 | 2% (Bob Fund) | used, no status | in quote | C03-1 "Guarantees 2% excess annual returns"; C44-1b "those 2% above" |
| 6 | 1/20 | on slide C44 | on slide C44, and in quote C43-1 ("A p-value of 1/20") | fine |
| 7 | level 0.05 | on slide C39 | on slide | "To reject H 0 at 0.05 level" |
| 8 | k = 19; "for any choice of k ... = 1/20" | on slide C44 | on slide | as printed |
| 9 | t 2.7, 3.1, 5.5, -2.6 | on slide C36, rows by order | on slide; order is fixed by consistency, not guessed: 2.68 belongs to Exxon (C31, C35: alpha 0.0062, t 2.68), 3.12 to Berkshire (C31 "alpha= 0.01", C36 0.0103), the negative t to the only negative alpha (TEAM -0.0008), leaving 5.5 for Bob | confirmed |
| 10 | alpha 0.0016 (Bob) | on slide C36 | on slide | "Bob 0.0016" |
| 11 | 2.68 | on slide C35 | on slide C31 and C35 | fine |
| 12 | beta 0.56 | on slide C35 | on slide | "beta = 0.56" |
| 13 | 7.5%, 20%, 71% | on slide C15 | on slide | table of C15 |
| 14 | -0.16 (Red) | on slide C20 | on slide | 0.71 - 1.32^2/2 = -0.161 |
| 15 | 0.14 (Pink) | on slide C21 | on slide | 0.355 - 0.435/2 = 0.1375 |
| 16 | 1.75, 0.075/0.040 | on slide C25 | on slide | printed so |
| 17 | (0.06)^2 = 0.003; "a bit more than 2%"; "more than 4" | on slide C20, C44, C43 | on slide | fine |
| 18 | 432, 189 months | pack parameters | pack | 1975-01..2010-12 = 432; BOOK_FACTS "189 months, 2011-01..2026-09" |
| 19 | 10% target; 0.05 (dSR); 0.025; 0.05 Holm; 0, 0.2, 0.4 | pack | pack | TESTING_PROTOCOL 1, 2; WORKFLOW 6 "2.5%"; WORKFLOW 3.3 |
| 20 | holdout criteria 0.3, -25%, 0.3, 2022; tail 2 and 1 points; 6 lags; 62 markets; 61 markets | pack | pack | WORKFLOW 6; TESTING_PROTOCOL 2; BOOK_FACTS header |
| 21 | +0.118, Holm p 0.0036 | repo result | matches | BOOK_FACTS batch0 row B0.1 (window 1975-01..2010-12) |
| 22 | 11.6%, 17.1% | repo result | matches | protocol_diagnostics "compound growth 11.6%/yr", "17.1%/yr" |
| 23 | 32 variants; 1.46; 0.23 | repo result | matches | stats audit section 2; "full book: 1.46"; "about 0.23" |
| 24 | 0.46, 0.67 | repo result | matches, but they are P(2022 > 0), not a pass chance of the holdout (that is 0.04 and 0.41): correction 7 | BOOK_FACTS audit section 4 |
| 25 | 0.0485 at k = 19 | computed | confirmed | 59 gains needed ((20/19)^59 >= 20); (19/20)^59 = 0.0485 |
| 26 | -0.17, 0.17 ("exact") | computed | confirmed as exact geometric growth per round of the C16 dice | Red (0.06*0.2*1*27)^(1/6) - 1 = -0.171; Pink over 36 equally likely pairs = 0.168 |
| 27 | 1.875 | computed | confirmed | 0.075/0.04 |
| 28 | 0.0036, 5.3% | computed | confirmed | 0.06^2; 1/19 = 0.0526 |
| 29 | 0.89, 1.27, 1.86, 1.97 | computed | confirmed: 0.885, 1.273, 1.858, 1.967 | (1 + m - v/2)^n = 20 x count, v = 0.01/12, Sharpe = 12m/0.10 |
| 30 | 0.41, 0.49, 0.60 | computed | confirmed: 0.408, 0.493, 0.599 | monthly growth S^2/24 over 432 months = ln(20 x count) |
| 31 | 8.4 points, 0.84 | computed | confirmed: 8.35, 0.835 (difference variance ignored) | exp(ln 20/432) - 1 = 0.00696 a month |
| 32 | about 1.5 | computed | confirmed: 1.53 | (1 + 0.0118/12)^432 |
| 33 | 143, 0.007, 0.22 | computed | confirmed: 142.8, 0.0070, 0.224 | 1.116^15 x 1.171^21 |
| 34 | 0.019 (15% target) | computed | **contradicted**: 0.0215 | slide C20: means x1.5, variance x2.25: ln W = 1.5 x (4.962 + 36 x 0.005) - 36 x 0.01125 = 7.307, W = 1491, 32/1491 = 0.021; the note's 0.019 = 32/exp(1.5 x 4.962), drag left out |
| 35 | 1.75 for Bob over about 350 months | computed (reader) | confirmed: 1.750; 1980-01..2009-02 = 350 months | 1.0016^350 (residual variance and beta error ignored) |
| 36 | 32 years | computed | confirmed: 31.5 | ln 20/(0.10 - 0.005) |
| 37 | 0.10, 0.05 | computed | confirmed | growth S v - v^2/2 at v = 0.10 is zero at S = 0.05; best v = S |
| 38 | 0.236, 0.29, 0.12, 0.34, 0.025, a tenth | computed | confirmed: 0.2361, 0.290, 0.118, 0.345, 0.0247, 0.106 | (2 S_B + s)/sqrt 5 > S_B iff s > (sqrt 5 - 2) S_B; needs all five pods independent |
| 39 | 1.23 | computed | confirmed | 1.46 - 0.23 |
| 40 | 0.37 | computed | confirmed: 0.3675 | (1 - 1/432)^432; the loss in the row is 1.44 times the pod's capital at 10% volatility (about 50 monthly standard deviations) |
| 41 | 0.375, 0.11 | computed | confirmed | 7.5/20; 0.3 x 0.375 = 0.1125 |
| 42 | 5% and 10% over two batches | computed | confirmed | 2 x 0.025; 2 x 0.05 |
| 43 | month 37 = 1978-01 | P4 | confirmed | 36 months from 1975-01 |

Not used by the note but checked as context: 1.71^20 = 45,700 (C18, correct); the C24 "long run return" column equals mean - SD^2/2 for all four assets (0.0076, 0.0112, 0.0053, 0.0012).

### Table B: statements (section 2 of the note)

| Row | Verdict | Reason |
|---|---|---|
| 1 Doob bound, 1 in 20 | partly | The slides state the inequality (C39 "CERT p-value from Doob's inequality", formula on slide) and do not derive it; by the brief's labels that is ASSERTED on the slides, though the theorem itself is standard (checker's knowledge). "Ever" goes beyond "during observed period" but is true by Ville's inequality (checker's knowledge). Limits honest. Correction 2. |
| 2 Bob Fund reaches the bound | supported | C44 construction and "For any choice of k" on slide; the note correctly shows the slide's "= 1/20" is only near-exact (0.0485 at k = 19). |
| 3 Four assets: t vs martingale | supported | C36 table, C41-1 quote; row order fixed by consistency (Table A #9). Missing limit: the residuals use b estimated on the same data (C40 "(R t - r f ) - b (M t - r f )"). Correction 3. |
| 4 t-test p-value doubtful | supported | C38-1, C38-2 quotes; ASSERTED with charts is right. |
| 5 Bonferroni | supported | C43-2, C45-2b quotes; ASSERTED is right. |
| 6 Growth = mean - var/2; dice | supported | C20-1 quote, C19-1, C21-1; numbers on slides; exact values confirmed. The slides also apply the formula to the four real assets (C24, on slide), which the row does not mention (harmless). |
| 7 Hold excess mean over variance | supported | C25-1; formula on slide, no derivation; 1.875 confirmed. |
| 8 Take market out; alpha -> some amount | supported | C04-2, C27-2, C30-2 quotes; "Buy (or sell) some amount of it" on slide C30; C25-3 adds "for which we know μ ≠ 0". |

### C. Element table and what the note leaves out

(i) Own rules. All ten rows quote the pack correctly: TESTING_PROTOCOL test 1 ("Paired stationary bootstrap of the Sharpe difference"), section 3 ("Holm's step-down correction is applied over every challenger in the batch"), test 5 ("max fall not worse by more than 2 points and worst month not worse by more than 1 point"), test 4 ("dSR at twice the costs on the window"), section 6 ("it does not prove skill"), section 1 ("10% vol target"), the reported list ("the Foster-Stine value-add test"); WORKFLOW section 5 test 3 (placebo), 3.3, section 6 criteria, 5.1, section 5 test 1 ("alpha against the Core book"), Q ("promotions only at registered checkpoints with stated sample sizes"). Pack problem 5's "family shares 45/25/15/15" is BOOK_FACTS' wording (verbatim).

(ii) Verdicts.
- Bootstrap: supported. QP13-C28-2 is about dependence across 1,500 funds in one year, which is exactly the reason TESTING_PROTOCOL gives for resampling whole months; apt.
- Multiplicity: partly. "Silent on Holm" is literally true, but the slides endorse Bonferroni ("Bonferroni does fine, particularly since it's hard to “count” the considered alternatives", QP13-C45-2b), while TESTING_PROTOCOL section 4 calls it "overly strict". The row should say so (D5 covers the proposal). Correction 4.
- Tail: supported (balanced: supports the worry, contradicts the citation as support for a fall statistic).
- Placebo, double costs, power check: supported ("cost", "drawdown", "fall", "Sharpe", "bootstrap", "Holm" occur on no slide).
- Holdout: supported; the 0.46 and 0.67 are the chance that 2022 is positive, not a pass chance (correction 7).
- Sizing: partly. QP13-C25-2 ("Example suggests we’re more risk averse…") is a remark that the formula asks for more than investors hold; it is not an argument for holding less. Corrections 5 and 6.
- Adds to the book: supported (QP13-C45-2 names the martingale test).
- Live promotion: supported (C22-2; the max in the C39 formula covers every look).

(iii) Slide content bearing on our sheet that the note does not mention:
1. The slides' own martingale results use a beta estimated on the same data: slide C40 writes the residual as "(R t - r f ) - b (M t - r f )" and says finely spaced data "essentially reveal β (if you believe it's fixed!)". An estimated beta that is too low leaves part of the market premium in w, which then has a positive mean without skill (reader). So C41's one rejection carries the look-ahead the note's own rule forbids, and the slides show nothing about the test with a beta from past data only.
2. The Bob Fund "Guarantees 2% excess annual returns above any benchmark you want" (QP13-C03-1). The hidden-loss overlay can sit on top of any incumbent, so the scope warning of P3 applies to every challenger-minus-incumbent comparison in TESTING_PROTOCOL, not only to new pods (P3 goes into TESTING_PROTOCOL section 3, which is about challengers). Correction 17.
3. Correlation: "correlation remains between assets" (QP13-C10-1); "Messy problem of portfolio analysis is to anticipate correlations going forward" (QP13-C27-1); independence is the first caution (QP13-C23-1). The 0.236 break-even, "a tenth", the 0.34 of D4 and P2's power check all assume independent pods. Correction 14; open point 3.
4. Stability caution (QP13-C23-2, "The properties of the dice stay the same throughout the simulation"): real records change; bears on the power check's constant true Sharpe and on expanding-window estimates. Not mentioned.
5. Frequency: "Much simpler structure, almost iid..." (QP13-C08-1) and "Fat tails more apparent in daily data" (QP13-C09-2) support monthly design tests and the use of slide C20's formula on monthly data; the note picks monthly without a reason (correction 10).
6. "Focus on returns, not cumulative value or prices" (QP13-C04-1) and "Too easy to be deceived..." (QP13-C07-1): the worst-fall statistics (tail test, holdout criterion) are cumulative-value measures; the slides warn against judging on cumulative value, though not about falls as such. The note says "silent on falls"; a weak "cuts against" would be as defensible.
7. Slide C29 ("Mixing the “tangent” portfolio with cash obtains better performance"; lend/borrow) treats leverage as moving along a line at constant Sharpe: support for judging at a fixed volatility target by a scale-free statistic (P4's "a Sharpe has none"). Not cited.
8. Bob's alpha, 0.0016 a month (C36), is about 1.9% a year, the Bob Fund's promised 2% (C03). Reader: "Bob" in the challenge may be a constructed series; QP13-C41-2's machine field says Bob and TEAM are "nearly exact functions of the market" (summary only, on no slide). If so, the note's "The slides' own case: Bob" is a constructed case. Cannot verify.
9. C41-1/C43-1: with Bonferroni over four assets the bar is 80; whether Berkshire reaches it is only in the chart (summary says about 25). On the slides' own logic probably no asset survives; the note says "then we have to consider multiplicity" and leaves it there. Cannot verify from text.

(iv) What weakens a proposal of the note: item 1 weakens the martingale lesson of section 4 (beta), item 2 widens P3, item 3 weakens section 5 and P2's power check, item 4 weakens P2's power check.

### D. Proposals

- P1 (wording). Precise; no test changes; pass chance unchanged is right. The reported-list sentence says slide 38 "doubts its p-value" for a Newey-West t; slide 38 doubts the plain t-statistic ("Test H 0 : α = 0 using t-statistic ... Doubts about standard test"). Newey-West corrects the standard error for dependence and ARCH, not for fat tails (checker's knowledge). Correction 15.
- P2 (test 1 for new pods, decisive). Statistic, resampling, multiplicity and gate are fixed; the p-value is indeed scale-free (intercept and its resampled values scale together). It names what 3.3 must simulate. Weak points: (a) "the market is the Core book" is a reader extension of C27-2 (correction 16); (b) the power check leaves the correlation between pod and book unset (open point 3); (c) it implies that protocol tests 2 and 3 are reported only for pods without saying so (open point 2); (d) it fixes now what WORKFLOW 3.3 says is fixed at the power check (open point 1); (e) the excess-of-cash treatment of pod and book changes alpha by beta times the cash rate when only one includes cash (open point 7). Not redundant; respects the budget (no added test, Holm 2.5% per batch as in WORKFLOW 6).
- P3 (reported-only). The identity is right ((1 - 1/n)^n = 0.37 at n = 432) if the loss is independent of the other returns, which the text should say (correction 19). "Every test here then reads the pod as a good one" overstates: the tests see the same returns as if the loss did not exist; they may still reject (correction 18). Scope should include challengers (correction 17). Naming each pod's worst-loss event is a judgement without a gate (open point 5). No effect on pass chance: right.
- P4 (reported-only). Fixed window (expanding, first value month 37 = 1978-01), no look-ahead, no scale. With two markets the slope is a vector (correction 20). The S&P series and whether r is in excess of cash are named but not verifiable from the pack (open point 7). Not redundant (the correlation criterion caps exposure, does not remove its return).
- M1 (zero-slot). Gate fixed (0.05 in either era 1978-89, 1990-2010), data named (engine pair of charter D3), logged as a design-data run, outcome only selects a reported line. The 0.05 is borrowed from cost-error reasoning (note admits; open point 8).
- D1-D9: reasons hold. D1's 0.84 is the difference-stream figure; for a pod at 10% volatility with a count of 4 the typical path needs Sharpe 1.27, so the drop is stronger than stated (correction 21). D2 is a judgement (open point 6). D5's "Holm guards the same error" is flagged as the author's knowledge and is right (checker's knowledge: Holm controls the familywise error under any dependence and rejects whatever Bonferroni rejects).

### E. Rules of the shop

- No decision handed to the user: confirmed. Every proposal is exactly one of protocol item, zero-slot diagnostic or dropped: confirmed. Nothing is claimed as registered or run: confirmed. No 2011-2026 result: confirmed (0.46/0.67 are a design-era simulation; 1.97 on 189 months is hypothetical arithmetic).
- Author's knowledge is flagged where used (D5). One reader extension is unlabelled ("the slides take out what is already held", twice; corrections 9 and 16).
- Attribution "Stine 2009" for the tail test: the slides support the worry (QP13-C04-3, C44) and offer a different remedy ("Watch for unseen volatility using robust test / Martingale test (CERT)", slide C45); no fall statistic is on any slide, and the slides' own fund passes a fall test until "busted!". The note's verdict (contradicted as support for the statistic, kept for the worry in P1) is right.
- Attribution "Foster-Stine value-add test" for the Newey-West alpha t: not supported by the pack. The only Foster-Stine(-Young) test on the slides is "A martingale test for alpha" (QP13-C45-2). Checker's knowledge, certain: the paper's authors are Dean Foster, Robert Stine and H. Peyton Young, and it is the source of the CERT test; the HAC standard error is Newey and West (1987). I do not know with certainty whether a separately named Foster-Stine value-add test exists; the note's own hedge (section 12, P1) is appropriate.
- Checker's knowledge on the inequality: for a nonnegative martingale or supermartingale C with C_0 = 1, P(max over t <= n of C_t >= γ) <= 1/γ (Doob); Ville's inequality extends it to all t, so unbounded monitoring and the one-sided null α <= 0 are covered. It needs 1 + w_t >= 0 surely. A scale chosen from past data only, and an average of compounded values over scales fixed in advance, are again nonnegative martingales under the null if every scale keeps 1 + c w_t >= 0; so the scale can be closed by a registered rule, at the price of a bound on the worst month at the largest scale. This is why the note's "it cannot be" is too strong (correction 11), while its drop of the test stands on power (even the best scale needs Sharpe 0.41 to 0.60).

### F. Martingale-test section

- Assumptions: (1) is QP13-C39-1, (2) QP13-C39-2, (3) C40 ("if you believe it's fixed!"): all on the slides. But the sentence "Our streams meet (1) and (2)" treats the null as a property of the stream; (1) means no skill only after every premium the stream holds is removed, and the whole-book figures (143, p 0.007) keep the market in (correction 8).
- Open choices: market and beta closed by a rule with a reason (reader extension unlabelled, correction 9); look-ahead closed by the expanding-window rule (WORKFLOW 5) and "a wrong beta" correctly listed as not controlled; count closed by a rule; frequency chosen without a reason (correction 10); scale reported as unanswered, correctly, but "cannot be" closed is too strong (correction 11).
- Detectable-effect arithmetic: all right except 0.019 (correction 12, 13). The figures are the effect at which a typical (median) path ends at the bar, so about even odds of detection, not high power; the verdict line and D1 should say so (corrections 1, 21).
- Status: "dropped" as decisive is consistent with the arithmetic (a 0.4 pod at 10% volatility needs log growth of 4.38 against an expected 1.26 with standard deviation 0.60: z about 5) and with the slides' own remarks ("A p-value of 1/20 does not overcome adjustments for multiplicity", QP13-C43-1; only one of four rejects before multiplicity). Dropping the reported line is a judgement (open point 6).

## 3. Required corrections

1. Verdict line 6 overstates detection: the computed figure is the gap at which a typical path ends at the bar.
- Find: `as held it could detect only a Sharpe gap of about 0.84 on the design window.`
- Replace: `as held a typical path (about even odds) clears the bar only at a Sharpe gap of about 0.84 on the design window.`
Reason: section 4 of the note itself, "a typical path reaches 20 only at"; recompute.py (median path, 0.835).

2. Row 1 label: the slides cite the inequality without derivation, example or numbers for it.
- Find: `SHOWN (inequality stated, not derived)`
- Replace: `ASSERTED on the slides (Doob's inequality cited, not derived; a standard theorem, checker's knowledge)`
Reason: slide C39, "CERT p-value from Doob’s inequality" (QP13-C39-3), formula only; brief: SHOWN needs a derivation, a constructed example or a result with numbers.

3. Row 3 omits that the slides' residuals use a beta estimated on the same data.
- Find: `Four hand-picked series, two unexplained (Bob, TEAM): it can happen; nothing on how often`
- Replace: `Four hand-picked series, two unexplained (Bob, TEAM); residuals use a beta estimated on the same data (slide C40, b): it can happen; nothing on how often`
Reason: slide C40, "“Residual” returns for Exxon, (R t - r f ) - b (M t - r f )" and QP13-C40-1 "essentially reveal β (if you believe it’s fixed!)".

4. Multiplicity row leaves out the slides' endorsement of Bonferroni against the protocol's wording.
- Find: `Silent on Holm, selection inflation, deflated Sharpe`
- Replace: `Silent on Holm, selection inflation, deflated Sharpe; calls Bonferroni adequate (QP13-C45-2b, "Bonferroni does fine") where TESTING_PROTOCOL 4 calls it "overly strict" (D5)`
Reason: QP13-C45-2b "Bonferroni does fine, particularly since it’s hard to “count” the considered alternatives"; TESTING_PROTOCOL 4 "without the overly strict Bonferroni".

5. Sizing row reads a remark as support.
- Find: `Supports holding less than the growth optimum (QP13-C25-2).`
- Replace: `Consistent with holding less than the growth optimum, in words only: QP13-C25-2 remarks that investors hold less than the formula asks; it gives no argument for holding less.`
Reason: QP13-C25-2 "Example suggests we’re more risk averse…" (a remark after p = 1.75, slide C25).

6. Same point in the verdict list.
- Find: `sizing below the growth optimum;`
- Replace: `sizing below the growth optimum (consistent, in words only);`
Reason: QP13-C25-2 as in item 5.

7. The 0.46 and 0.67 are the chance that 2022 is positive, not the holdout pass chance (0.04 and 0.41).
- Find: `pass chance 0.46 at true Sharpe 0, 0.67 at 0.5, repo result`
- Replace: `chance that 2022 is positive 0.46 at true Sharpe 0, 0.67 at 0.5, repo result`
Reason: BOOK_FACTS audit section 4, column "P(2022 > 0)": 0.46 and 0.67; "P(pass all)": 0.04 and 0.41.

8. Assumption (1) is the null, and means no skill only after every premium is removed; a whole book with market exposure has a positive mean without skill.
- Find: `Our streams meet (1) and (2) at the scale held, and (3) only where beta is fixed by construction.`
- Replace: `(1) is the null itself; it means no skill only after every premium the stream holds is removed (3), so a whole book that keeps market exposure can be rejected without skill (the 143 below keeps the market in). Our streams meet (2) at the scale held, and (3) only where beta is fixed by construction.`
Reason: slide C39, "Specific returns after removing market w t = (R t - r f ) - β (M t - r f ) = α + ε t"; QP13-C04-2 "Remove market performance (CAPM)".

9. Reader extension unlabelled (market and beta rule).
- Find: `Reason: the slides take out what is already held (QP13-C27-2).`
- Replace: `Reason (reader): the slides take out the whole market (QP13-C27-2), which their theory calls the tangent portfolio (slide C29); for us the held book plays that role.`
Reason: QP13-C27-2 "Invest first in the market as a whole"; slide C29 "The tangent portfolio is the market portfolio."

10. Frequency chosen without a reason.
- Find: `(QP13-C40-2): monthly here.`
- Replace: `(QP13-C40-2): monthly here, because the design tests are monthly (WORKFLOW 5) and finer data help only a fixed beta (QP13-C40-1), which ours is not (D8).`
Reason: QP13-C40-1 "we can use finely spaced data that essentially reveal β (if you believe it’s fixed!)"; WORKFLOW 5 "Design tests are monthly on 1975-2010".

11. "It cannot be" is too strong: the slides leave the scale open; a registered rule could close it at the price of a worst-month bound.
- Find: `Not closed, and it cannot be.`
- Replace: `Not closed by the slides.`
Reason: slides C39-C41 never mention leverage ("leverage" only on C04 and C29); checker's knowledge: a scale chosen from past data, or an average over scales fixed in advance, keeps the bound if no scale can lose more than 100% in a month.

12. Arithmetic: at a 15% target the variance drag grows by 2.25, not 1.5.
- Find: `At a 15% target the same record gives 0.019.`
- Replace: `At a 15% target the same record gives 0.021 (means times 1.5, variance times 2.25, slide C20).`
Reason: slide C20 "W t ≈ W 0 (1 + E(r t ) - Var(r t )/2) t"; recompute.py: ln W = 1.5 x (4.962 + 0.18) - 0.405 = 7.307, 32/1491 = 0.0215.

13. Same number in the list of section 9.
- Find: `143, 0.007, 0.22, 0.019`
- Replace: `143, 0.007, 0.22, 0.021`
Reason: as item 12.

14. The break-even assumes five independent pods, which the slides warn against.
- Find: `With four independent pods, a fifth raises the book's Sharpe`
- Replace: `With five mutually independent pods (an assumption the slides warn against: QP13-C10-1, C27-1), a fifth raises the book's Sharpe`
Reason: QP13-C10-1 "correlation remains between assets"; QP13-C27-1 "Messy problem of portfolio analysis is to anticipate correlations going forward."

15. P1: slide 38 doubts the plain t-test, not a Newey-West t.
- Find: `Stine 2009, slide 38, doubts its p-value`
- Replace: `Stine 2009, slide 38, doubts the p-value of the plain t-test; Newey-West is on no slide`
Reason: slide C38 "Test H 0 : α = 0 using t-statistic ... Doubts about standard test."

16. P2: same reader extension unlabelled.
- Find: `The market is the Core book: the slides take out what is already held.`
- Replace: `The market is the Core book (reader: the slides take out the whole market, QP13-C27-2, which their theory calls the tangent portfolio, slide C29).`
Reason: QP13-C27-2 "Invest first in the market as a whole"; slide C29.

17. P3 goes into TESTING_PROTOCOL section 3, which governs challengers; the Bob Fund overlay sits on any benchmark.
- Find: `They do not cover a pod with steady gains`
- Replace: `They do not cover a pod or a challenger with steady gains`
Reason: QP13-C03-1 "Guarantees 2% excess annual returns above any benchmark you want."

18. P3 overstates: with no loss on the window the tests see the same returns as without the loss; they may still reject.
- Find: `and every test here then reads the pod as a good one.`
- Replace: `and every test here then sees the same returns as if the loss did not exist.`
Reason: slide C44 "busted!" (the record is unchanged until the loss); the identity in P3's own next sentence.

19. P3's computed row needs the loss independent of the other returns.
- Find: `(true mean zero) is adopted at least`
- Replace: `(true mean zero; the loss independent of all other returns) is adopted at least`
Reason: (1 - 1/n)^n times the 0.4 pod's pass rate holds only if the loss is independent of the pod's and the book's returns (recompute.py: 0.3675); QP13-C23-1 "The dice fluctuate independently of one another."

20. P4: with two markets the slope is one per market.
- Find: `b is the least-squares slope of r on m, with intercept`
- Replace: `b is the least-squares slope (one per market, fitted jointly) of r on m, with intercept`
Reason: P4's own "(and of the US 10-year bond if diagnostic M1 says so)"; slide C30 single-market form "R t - r f = α + β (M t - r f ) + ε t".

21. D1: same overstatement as item 1, and the relevant pod figure is stronger.
- Find: `as held it detects a Sharpe gap of 0.84; every simulated pod would fail.`
- Replace: `as held a typical path clears the bar only at a Sharpe gap of 0.84 (a pod at 10% volatility: Sharpe 1.27 with a count of 4); every simulated pod would fail.`
Reason: section 4 of the note, "1.27 with a count of 4"; recompute.py 1.273.

22. Pack problems: three more machine statements are on no slide.
- Find: `drops slide C39's conditions.`
- Replace: `drops slide C39's conditions; QP13-C41-2's 'Bob and TEAM returns are nearly exact functions of the market', QP13-C27-2's rule 'test other assets for alpha relative to it' and the map thesis 'even it is marginal after multiplicity' are on no slide.`
Reason: slide C41 says only "Only Berkshire Hathaway rejects the null, and then we have to consider multiplicity."; slide C27 says "Then consider other assets."

## 4. Open judgement points

1. P2 fixes the decisive statistic of test 1 now, while WORKFLOW 3.3 says the decisive statistic is fixed at the power check; 3.3 should measure P2's alpha form and the Sharpe-difference form side by side before 3.4 registers one (closed at 3.3-3.4).
2. P2 makes protocol tests 2 (dSR >= 0.05) and 3 (era non-inferiority) reported-only for pods by implication; the registration must state the decisive set for pods (WORKFLOW section 5's four) explicitly (pack problem 11.3b; closed at 3.4).
3. P2's power check does not set the correlation between simulated pods and the Core book; alpha, pass rates and the break-even depend on it (closed at 3.3).
4. P2's Core book at true Sharpe 1.23 subtracts a selection inflation measured on 1990-2010 variants from a 1975-2010 Sharpe; a reader choice (closed at 3.3).
5. P3's "event in which its mechanism loses most" is a judgement with no gate; the spec check (3.2, fresh Opus) could verify it (closed at 3.1-3.2).
6. D2: whether the martingale number earns a reported line, at the held scale or as a registered average over a fixed grid of scales (the only hidden-loss-robust number in the sheet), or stays dropped as nearly always uninformative, like the deflated Sharpe BOOK_FACTS no longer cites (closed at 3.4).
7. Whether the book's monthly return is in excess of cash: P4, M1, P2's alpha and the 143 depend on it; BOOK_FACTS gives Sharpe = mean/vol (14.33/9.78 = 1.465) with no cash term, which suggests an excess-return series, but the pack does not say (closed by Opus at 3.4 from the engine).
8. M1's gate 0.05 is borrowed from cost-estimate error, not estimation noise (closed at 3.4).
9. Holm's count: the slides' reason for Bonferroni is that the count is uncertain ("I bet that you have considered more than 4"); whether a batch's count should include logged design-data variants and diagnostics (research log, 7.1), not only registered challengers (closed at 3.4).
10. Whether "Stine 2009" should stay on test 5 at all; P1 keeps it for the worry with a scope sentence, which is defensible (closed at 3.4).

## 5. What I could not verify

- Whether a test called the "Foster-Stine value-add test" exists outside the pack (only the martingale test of Foster, Stine and Young is on the slides).
- Whether the book's return series is in excess of cash (open point 7).
- Chart-only values: the CERT maxima of slide C41, the mutual-fund regression of slide C28 (summary only; the note correctly does not use them); whether Berkshire's path reaches 80 (Bonferroni over four).
- Whether "Bob" and "TEAM" are constructed series (Bob's alpha 0.0016 a month is about the Bob Fund's 2% a year; reader observation only).
- The content of the Foster, Stine and Young paper beyond what the slides show (how it treats scale and power).
- Whether the engine's S&P 500 and US 10-year series for P4/M1 are excess returns (named in the charter digest only as "US equity and 10-year bond returns").
