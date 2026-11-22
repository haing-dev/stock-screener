# Digest for playbook card 1.4 #2 (verbatim extracts; numbers are not ground truth for this card)

# A. Systematic charter

## 1. Verdict

The notes agree, mostly by assertion, on how to build trend: size by volatility, mix speeds, count price drivers
not markets, never time it. They do not establish why trends exist (four mechanisms conflict). Tests with numbers
come from one paper (U01), one blog (U02) and studies only described on air. Pods: Trend, Economic trend, Carry,
Value (existing book) and Curve carry (new, B1); the notes give no thesis for Carry or Value. Versions to average:
16, 2, 2, 1 and 2, each in four weekly tranches. The one pass has six diagnostics. It decides three Batch A items
(new commodity markets, a no-trade buffer, a faster book scaler) and four lines in pod specs, and adopts nothing;
the other 26 proposals are folded in or dropped. Largest unverified dependency: the one new pod rests on a seller's
unshown claims (U04). Rule 5 is open: no note dates a thesis before 2011; Economic trend's sources are 2017 and 2023.

# B. Thesis note 1.3a

## 1. Verdict

Spec one new pod, **Strip reversion**: fade local bends in short-rate futures curves with QP06's two local rules.
Grade weak. Batch B2, behind every stronger candidate, and only if diagnostic R1 passes and daily prices are locked.
Do not spec: QP06's Treasury-bill form, whole-curve reversion (the engine's three built spreads stay untraded),
the QP07 model as a signal, a QP12 commodity forecast pod. Front-end carry is not a pod: short-rate futures
enter existing pods as markets (non-US only) through the charter's breadth check D1.
Established: on estimated Treasury yields 1973-2000 local reversion paid up to about five times the equity benchmark (rule 2-B; 3.3 times for 3-B)
per unit of risk before costs, and faded after the late 1980s. On traded Eurodollar futures a related curve model (QP07: long-run curve plus decaying habitat and date parts, one of 6 chosen by AIC) added
0.03 and 0.30 bp a trade (5- and 250-day holds) to always-long. Weakest link: no test of the local rule on traded prices.

# C. Thesis note 1.3b

## 1. Verdict

- **Carry: thesis supplied for currencies and commodities (asserted), not for bonds (pattern, no mechanism in the pack); grade weak on this pack.** Payers: hedgers of commodities (QP08, asserted); for currencies QP08 asserts a risk premium (QP08-C04-5) and the savers who pay it are my reading (reader); borrowers who fix long rates (reader: QP08 names no payer for bonds). Evidence: one sellers' paper, 1990 to April 2015, before costs.
- **Value: thesis supplied with a reservation.** Grade weak: the pattern rests on words in two sellers' papers; the only per-class figure in a quote is the bond leg's 0.18, which fails (QP15-C19-2), and survivorship "will likely favor value and carry" (QP08-C26-4); payer not established. Working reading: investors chase winners until prices overshoot, and Value is paid when prices come back. Two rivals kept apart.
- **Cross-sectional momentum: neither a pod nor a Trend version.** Roughly, it is what is left of Trend once each asset class's average position is removed (QP08-C21-4; exact only for positions proportional to one shared signal, claim text; our Trend uses other lookbacks and sign or capped shapes, reader). No payer of its own; QP08 finds it the weaker form (Sharpe 0.42 against 0.96, QP08-C17-1, over 1990 to April 2015 including 52 sealed months, so not a design-era fact).
- **Registration:** Trend directional only. Carry in both forms: 2 versions, unchanged. Value cross-asset only.
- **Changes to the charter:** Value from 1 version to 2 (a second anchor for bonds and currencies). Carry's grid stays; equities stay out. Two zero-slot diagnostics (X1, X2).
- **Rule 5:** the pack dates neither paper before 2011. Step 1.5 must date older sources for both pods, or the verdict rule makes them Incubator.
- **Weakest link:** nobody establishes who pays Value. The risks the authors test do not explain it; funding-liquidity risk has the wrong sign (QP15-C03-4, C34-2; pooled with individual stocks); and the authors find the cross-asset pattern "difficult to reconcile under existing behavioral theories" (QP15-C53-3), which cuts against the working reading too.
- **Limits on everything:** before costs; both author groups sell these strategies; QP08's sample runs 52 months into our sealed years.

# D. Thesis note 1.3c

## 1. Verdict

1. QP13 firmly establishes one thing: a test of no skill that assumes only a zero expected specific return (the return left after the market's part is taken out) and keeps false alarms at 1 in 20, even against a made-up fund with steady gains and a hidden total loss (SHOWN: stated inequality, constructed example). Its price is not quantified: the tested stream must multiply by 20.
2. The rest is asserted, or shown on dice and four hand-picked assets.
3. Supported in our sheet: whole-month resampling instead of a t table; counting candidates; alpha against what is already held; registered checkpoints; sizing below the growth optimum (consistent, in words only); the holdout read as a screen.
4. Contradicted: citing these slides for the tail test (their own fund passes it until the loss comes) and the name Foster-Stine on a regression t-test. A one-year criterion is cut against.
5. Added: take market exposure out before judging the book; alpha earns a pod some amount, not by itself an equal share; the error budget covers only losses that show on the window.
6. Four protocol items (P1-P4, no new decisive test), one diagnostic (M1). The martingale test is dropped: as held a typical path (about even odds) clears the bar only at a Sharpe gap of about 0.84 on the design window.
7. Weakest link in the source: the scale (leverage) of the tested stream is never discussed, yet it sets the verdict; power is not shown.
8. Weakest link in our sheet as the slides see it: every guard against "many small gains, rare big loss" reads only losses that already happened.

# E. Card 1.4 #1 policy and liquidity (Druckenmiller, Bessent): verdict and rule layer (to avoid duplicate rules)

## 1. Verdict

1. Playbook: find where policy is out of step with the economy, wait for a cheap one-sided bet, size it big, cut it fast. D reads the Fed through the inside of the stock market; B reads the people who make policy.
2. Part of it can be coded: six rules, 30 versions (60 with the two entry versions of section 6), all averaged; R6 fails the premise check (section 4) and is held back, leaving 28 (56) to register. Liquidity itself, peg breaks, policy personnel and conviction sizing cannot; the 1992 and Japan 2012-13 trades came from those, while the 2000 Treasury trade is coded in R1 and R2.
3. Strongest link: the 1992 peg break. Named loser, numbers in the quotes, both men tell it; but it is one trade of one fund (Soros's), so one case, not two. Rare, not codable.
4. Weakest link: the title idea that the quantity of liquidity drives prices. Asserted; D's 2018 stock short on it lost (claim text), and his 2021 short of the 2-year on "money supply growing at 40 percent" gained by his account from 15 to 150 basis points (MT149-C07-1, MT151-C10-4; trade and year are claim text). Central-bank and Treasury series do not cover most design years (reader); M2SL does, and enters R2 only as a warning.
5. Dating: four rules rest on three recalled pre-2011 actions (R1 and R2 on 2000, R3's stock leg on 1999, R5 on 1992), none dated by a year spoken in the quote; R3's bond leg, R4 and R6 are hindsight-flagged; nothing was recorded before 2018, so all six are hindsight under rule 5.
6. Record (ledger, machine-coded): D 4 of 16 forecasts right, 9 points below base rate, three recession calls missed; B one resolved row.
7. D says bond buying suppressed this playbook and macro was dead for 10 to 15 years: most of the holdout window.
8. Counts: 6 rules, 10 analyst questions, 11 open forecasts, 2 diagnostics.

## 4. Rule layer

Common to all rules. Checked at each month-end with data as known then (lags above); series marked first-published on the data sheet (CPILFESL, M2SL) are used as first published where vintages exist, else latest values, flagged. Markets are the book's panel, as excess returns. A position runs from the first month the condition holds until 12 months after the last such month, unless stated. Reason: "it looks one year forward" (MT151-C12-2), and 12 months is the short end of D's stated horizons (MT046-C05-3). Legs and rules are held at equal risk and opposite positions net; nothing is sized by conviction. Four weekly tranches. Two entry versions for every rule (section 6); every version of a rule is run and averaged. Each formula is the reader's wording.

**R1. Squeeze.** If WTISPLC, the dollar index (TWEXMMTH to its last month, DTWEXBGS after; each L-month change is taken inside one series, reader) and a rate are all above their level L months earlier: long US 2-year note and US 10-year bond. Versions: L 6 or 12; rate FEDFUNDS or GS10; R4 gate on or off (8). The men give only a direction; 6 is the Compass window, 12 the model's horizon. No position while R4's state at 5.0 is on. That gate is the reader's link, made knowing 2022-23, from MT149-C07-3 to the 5% test of MT148-C02-2; the quote of MT149-C07-3 gives only his usual Treasury playbook and the "10-year yielding 350", and that he declined it for inflation is claim text, so the gate is a version, not a fixed part of the rule. Claims: MT153-C10-5, MT153-C11-1, MT148-C11-1, MT151-C12-1, MT151-C12-2, MT151-C12-4. Hindsight: action in 2000, recalled in 2018, 2022 and 2024; one case. Not in the pods: Trend sells bonds when yields rise; this buys them (reader).

**R2. Tightening into warnings.** If FEDFUNDS is at least 0.25 above its level T months earlier, and at least k of three warnings hold: (a) GS5 minus GS2 below zero ("we've inverted", MT152-C02-2); (b) BAA minus GS10 above its level 6 months earlier (MT152-C02-3; the Compass window); (c) 12-month growth of M2SL below its level 24 months earlier ("over the last couple years", MT152-C04-3). Then long US 2-year note and US 10-year bond. Versions: T 6 or 12 (as R1); k 2 or 3; R4 gate on or off (8). The 0.25 is one standard move (reader). Same gate as R1. Claims: MT148-C11-2, MT153-C11-2, MT152-C08-1, MT152-C07-6. Hindsight: 2000 recalled; December 2018 stated live (ledger: the stance scored right, the 50 to 60 basis-point level wrong). Not in the pods: he bought when "there was no price movement" (MT153-C11-2), so before Trend; Carry leans against bonds when the curve is inverted (reader).

**R3. Easing into strength.** If FEDFUNDS is at least 0.25 below its level 3 months earlier, BAA minus GS10 is below its expanding-window median (window from the first month both series exist), and the S&P 500 price level is above its 10-month average (panel index; Compass spx_trend live): short US 10-year bond, long S&P 500. Versions: spread below the median or in the lowest third ("tight" is only a direction); gold (panel gold; GC=F live) at a 12-month high required or not, since gold is in the 2024 quote only (4). The 3 months are one quarter (reader). Source: "to cut 50 basis points with credit spreads tight gold at new highs" (MT151-C01-5). Claims: MT151-C03-3 ("I shorted them literally the day the FED cut"), MT069-C03-6, MT069-C03-X2, MT151-C11-2, MT153-C07-5. Hindsight: the stock leg has a recalled 1999 action ("Everyone knows how I played the Nasdaq melt up in '99", MT069-C06-3; its link to the Fed's easing is claim text of MT151-C11-2), and that episode ended when he "bought the exact top" and lost "two or three billion" (MT069-C06-3, MT148-C11-X1); the bond leg is 2024 only, flagged, and the ledger scores it wrong at 12 months. Not in the pods: after a cut Trend and Carry tend to hold bonds, so the bond leg is opposite; the stock leg probably repeats Trend (diagnostic D2).

**R4. Behind on inflation.** State on while the 12-month change of CPILFESL is above 5.0% and FEDFUNDS is below that change; off otherwise, with no 12-month tail. Action A: short US 10-year bond and 2-year note. Action B: A plus short S&P 500 and long the panel's commodities at equal risk (he names none: "some of the key commodities"; reader) ("a matrix of short fixed income short stocks", MT148-C05-2). Versions: threshold 5.0 or 4.5 (MT148-C02-2, MT148-C02-1, both in quote); action A or B (4). Claims: MT148-C02-3, MT148-C02-X2. Hindsight: stated June 2022; the only related action in a quote is after 2010, a short of the 2-year from 15 to 150 basis points (MT151-C10-4, MT149-C07-1; trade and year are claim text); flagged. Not in the pods: Trend and Economic trend probably hold the same positions while inflation rises (D2); the level test and the exit are new.

**R5. After the fall.** For each G10 currency in the panel other than the dollar whose stock index (and, for the bond version, 10-year bond) is in the panel; the mark and then the euro map to the German index and Bund (reader): trigger when its 6-month return against the dollar is at least 15 points below the median of those currencies. Then long that country's stock index. Versions: 15 or 10 points; stocks only, or stocks plus its 10-year bond (4). The 15 is the size D gives for a break; 10 is an earlier entry and 6 months the Compass window (reader). Claims: "I bought guilts I bought British stocks" (MT151-C09-6); MT141-C10-2. The bond version follows D in 1992; the other follows B, who stayed out: "I don't really need to mess around in the jgb market" (MT203-C10-1). Hindsight: 1992 purchase recalled, one case; B's case is 2012-13. Not in the pods: Trend sells the falling currency; no pod buys the local stocks on the fall. Economic trend may: check at step 3.2.

**R6. Gold that ignores yields.** If over L months GS10 rose, the real 10-year yield (GS10 minus the 12-month change of CPILFESL) rose, and gold rose (panel gold; GC=F live): long gold. Versions: L 3 or 6, short because he speaks of a pullback (2). Claim: MT203-C08-2 ("real rates started going up in the US nominal rates started going up", which he calls normally "a signal that you're going to get a 5 10 could be 15% pullback"). Premise check fails: the long direction and the rise in gold are claim text; on its words the quote points to a pullback. R6 is held back from registration until a quote supports the direction; question 8 covers gold meanwhile. B, 2024. Hindsight: flagged. Not in the pods: Trend is already long rising gold; D2 decides.

Not a rule: liquidity quantity (section 11). It goes to the analyst layer.

# F. Forecast scorecard 2026-11-12, lines for these speakers

