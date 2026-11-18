# Digest for playbook card 1.4 (verbatim extracts; their numbers are not ground truth for this card)

# A. Systematic charter (CHARTER_1.2.md)

## 1. Verdict

The notes agree, mostly by assertion, on how to build trend: size by volatility, mix speeds, count price drivers
not markets, never time it. They do not establish why trends exist (four mechanisms conflict). Tests with numbers
come from one paper (U01), one blog (U02) and studies only described on air. Pods: Trend, Economic trend, Carry,
Value (existing book) and Curve carry (new, B1); the notes give no thesis for Carry or Value. Versions to average:
16, 2, 2, 1 and 2, each in four weekly tranches. The one pass has six diagnostics. It decides three Batch A items
(new commodity markets, a no-trade buffer, a faster book scaler) and four lines in pod specs, and adopts nothing;
the other 26 proposals are folded in or dropped. Largest unverified dependency: the one new pod rests on a seller's
unshown claims (U04). Rule 5 is open: no note dates a thesis before 2011; Economic trend's sources are 2017 and 2023.

# B. Thesis note 1.3a rates and curve

## 1. Verdict

Spec one new pod, **Strip reversion**: fade local bends in short-rate futures curves with QP06's two local rules.
Grade weak. Batch B2, behind every stronger candidate, and only if diagnostic R1 passes and daily prices are locked.
Do not spec: QP06's Treasury-bill form, whole-curve reversion (the engine's three built spreads stay untraded),
the QP07 model as a signal, a QP12 commodity forecast pod. Front-end carry is not a pod: short-rate futures
enter existing pods as markets (non-US only) through the charter's breadth check D1.
Established: on estimated Treasury yields 1973-2000 local reversion paid up to about five times the equity benchmark (rule 2-B; 3.3 times for 3-B)
per unit of risk before costs, and faded after the late 1980s. On traded Eurodollar futures a related curve model (QP07: long-run curve plus decaying habitat and date parts, one of 6 chosen by AIC) added
0.03 and 0.30 bp a trade (5- and 250-day holds) to always-long. Weakest link: no test of the local rule on traded prices.

# C. Thesis note 1.3b value / momentum / carry

## 1. Verdict

- **Carry: thesis supplied for currencies and commodities (asserted), not for bonds (pattern, no mechanism in the pack); grade weak on this pack.** Payers: hedgers of commodities (QP08, asserted); for currencies QP08 asserts a risk premium (QP08-C04-5) and the savers who pay it are my reading (reader); borrowers who fix long rates (reader: QP08 names no payer for bonds). Evidence: one sellers' paper, 1990 to April 2015, before costs.
- **Value: thesis supplied with a reservation.** Grade weak: the pattern rests on words in two sellers' papers; the only per-class figure in a quote is the bond leg's 0.18, which fails (QP15-C19-2), and survivorship "will likely favor value and carry" (QP08-C26-4); payer not established. Working reading: investors chase winners until prices overshoot, and Value is paid when prices come back. Two rivals kept apart.
- **Cross-sectional momentum: neither a pod nor a Trend version.** Roughly, it is what is left of Trend once each asset class's average position is removed (QP08-C21-4; exact only for positions proportional to one shared signal, claim text; our Trend uses other lookbacks and sign or capped shapes, reader). No payer of its own; QP08 finds it the weaker form (Sharpe 0.42 against 0.96, QP08-C17-1, over 1990 to April 2015 including 52 sealed months, so not a design-era fact).
- **Registration:** Trend directional only. Carry in both forms: 2 versions, unchanged. Value cross-asset only.
- **Changes to the charter:** Value from 1 version to 2 (a second anchor for bonds and currencies). Carry's grid stays; equities stay out. Two zero-slot diagnostics (X1, X2).
- **Rule 5:** the pack dates neither paper before 2011. Step 1.5 must date older sources for both pods, or the verdict rule makes them Incubator.
- **Weakest link:** nobody establishes who pays Value. The risks the authors test do not explain it; funding-liquidity risk has the wrong sign (QP15-C03-4, C34-2; pooled with individual stocks); and the authors find the cross-asset pattern "difficult to reconcile under existing behavioral theories" (QP15-C53-3), which cuts against the working reading too.
- **Limits on everything:** before costs; both author groups sell these strategies; QP08's sample runs 52 months into our sealed years.

# D. Thesis note 1.3c testing method

## 1. Verdict

1. QP13 firmly establishes one thing: a test of no skill that assumes only a zero expected specific return (the return left after the market's part is taken out) and keeps false alarms at 1 in 20, even against a made-up fund with steady gains and a hidden total loss (SHOWN: stated inequality, constructed example). Its price is not quantified: the tested stream must multiply by 20.
2. The rest is asserted, or shown on dice and four hand-picked assets.
3. Supported in our sheet: whole-month resampling instead of a t table; counting candidates; alpha against what is already held; registered checkpoints; sizing below the growth optimum (consistent, in words only); the holdout read as a screen.
4. Contradicted: citing these slides for the tail test (their own fund passes it until the loss comes) and the name Foster-Stine on a regression t-test. A one-year criterion is cut against.
5. Added: take market exposure out before judging the book; alpha earns a pod some amount, not by itself an equal share; the error budget covers only losses that show on the window.
6. Four protocol items (P1-P4, no new decisive test), one diagnostic (M1). The martingale test is dropped: as held a typical path (about even odds) clears the bar only at a Sharpe gap of about 0.84 on the design window.
7. Weakest link in the source: the scale (leverage) of the tested stream is never discussed, yet it sets the verdict; power is not shown.
8. Weakest link in our sheet as the slides see it: every guard against "many small gains, rare big loss" reads only losses that already happened.

# E. Forecast scorecard 2026-11-12 (descriptive only), lines for the two men

| Stanley Druckenmiller | 16 | 25% | -9 pp (16) |