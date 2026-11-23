# Step 3.3 power check (WORKFLOW v2.1), 2026-11-23

> **Status (2026-11-23): step 3.3 done.** One Opus 5.5 run (effort high, ~0.36M tokens) on SYNTHETIC data only, using the
> registered repo test code (gm/stats.py, gm/protocol.py decide, gm/audit.py holdout_power; validation.txt). Script
> tools/power/power_3_3.py (fixed seeds; re-run: python3 tools/power/power_3_3.py), raw tables in csv/. Paths in the
> text that point to the scratch folder now live at tools/power/ and docs/research/power/. Nothing registered:
> the proposal in section 4 goes to step 3.4.

Quant and risk officer (Opus 5.5). Everything below is simulated. No market data, nothing from 2011 or later. The only
real-data facts used are the design-era book facts on record (BOOK_FACTS_design_era.md, 1975-2010), and only to set the
generator. The registered statistics are imported from the repo: `gm/stats.py` (`_stationary_idx`, `paired_sr_test`,
`holm`, `nw_alpha_t`), `gm/protocol.py` (`decide` and its constants) and `gm/audit.py` (`holdout_power`). The vectorised
versions I used were checked against them to the last digit (`validation.txt`: 18 paired tests, 6 alpha bootstraps, 50
Holm vectors and 200 `decide()` calls agree). Nothing is registered here. Registration is step 3.4.

Files: script `work/power_3_3.py`; probes `work/size_probe2.py`, `work/level_probe.py`, `work/tail_probe.py`; raw
tables `csv/*.csv`; all tables as markdown in `work/tables_all.md`. Monte Carlo: 1,000 paths per cell (MC standard error
up to 0.016), 1,500 to 2,000 in the probes, 20,000 for the holdout.

## 1. Summary in ten lines

1. Test 1 (alpha on the Core book, bootstrap p, 2.5%) has fair power only for pods whose residual information ratio (IR) is
   at least 0.4. Pass rate for a lone pod: 0.60 over 432 months and about 0.41 over 250 months. At IR 0.2 it is 0.15 to 0.26.
2. A pod's standalone Sharpe is the wrong yardstick against a book at Sharpe 1.23. At correlation 0.3 with the book, a
   pod with Sharpe 0.4 has a true IR of only 0.03, and one with Sharpe 0.2 has -0.18. The sheet rightly passes them at
   null rates (0.05 and 0.002). Pods with Sharpe 0, 0.2 or 0.4 can be found only if they are close to uncorrelated with
   the book.
3. Given that test 1 passes, double costs and the placebo almost never fail a timing pod. The tail test takes 2 to 7
   points. Making the era test decisive cuts full-sample pods by more than half (0.56 to 0.23).
4. The Sharpe-difference form of test 1 has far less power than alpha: 0.16 against 0.60 for the full-sample pod at IR
   0.4 and correlation 0.3. Alpha is the decisive statistic to register (1.3c P2).
5. Test 1 rejects too often in finite samples when the book's Sharpe is high and the correlation is above zero. At a
   nominal 2.5% the actual rate is 3.3 to 5.7% at correlation 0.3 and 4.5 to 5.8% at 0.6; the Newey-West t does the same.
   B2 false adoption at nominal 2.5% is measured at 3.0 to 3.3%.
6. The placebo works only against standing exposure: it passes a pure standing-exposure pod 5% of the time and a timing
   pod 89%. 12-month blocks wipe out a calendar rule (pass 0.00 with a true on-month Sharpe of 0.8). Date rules need card
   4's within-year shift (pass 0.59).
7. A rule layer with fewer than about 48 on-months or fewer than 3 episodes cannot be judged: even an on-month Sharpe of
   1.2 passes 17% or less.
8. For hygiene, the protocol's superiority test passes a neutral change 5% of the time. Non-inferiority (pooled lower bound
   above -0.10) passes it 44 to 100%, and a change that truly costs -0.1 6 to 9%.
9. Hidden loss (1.3c P3): a zero-mean pod whose loss never showed passes at 0.41 times the rate of the Sharpe-0.4 pod at
   n = 432 (identity bound 0.37). When the loss shows, every reading fails it.
10. Proposal: alpha with bootstrap p, Holm at 2.5% over the systematic pods only; double costs, placebo and tail
    decisive; eras reported; hygiene by non-inferiority; minimum of 48 on-months and 3 episodes per rule layer. Details
    in section 4.

## 2. Generator and calibration

**Book (the Core book stand-in).** Monthly returns at 10% annual volatility from a GARCH(1,1) with Student-t(5) shocks
(alpha 0.05, beta 0.90), filtered by an AR(1) with coefficient 0.10. Mean set by an assumed true Sharpe: 1.23 (1.46 less
0.23 of selection, as 1.3c P2) or 0.5. BOOK_FACTS gives no kurtosis, so df and the GARCH weights were picked from
`work/calib_try.py` (six settings tried) so that every recorded fact falls inside the simulated 10-90% band, near its
middle where the two eras agree:

| Fact on record (design era) | Value | Simulated p10 / p50 / p90 |
|---|---|---|
| Skew 1975-89 / 1990-2010 | -0.65 / +0.26 | -0.67 / -0.01 / 0.66 ; -0.59 / 0.01 / 0.61 |
| Worst month 1975-89 (180 m) / 1990-2010 (252 m) | -14.7% / -9.8% | -15.4 / -9.3 / -6.6 ; -16.1 / -10.2 / -7.3 |
| First-order autocorrelation | 0.09 / 0.12 | median 0.09 ; 0.10 |
| Rolling 36-month vol, min | 4.9% / 6.1% | 5.1 / 6.3 / 7.6 ; 5.0 / 6.0 / 7.1 |
| Rolling 36-month vol, max | 13.3% / 14.2% | 10.2 / 12.8 / 18.0 ; 10.9 / 13.6 / 18.8 |
| Max drawdown 1975-2010: BASE (SR 1.24) / candidate (SR 1.46) | -20.5% / -16.8% | median -20.6% (SR 1.22) / -18.7% (SR 1.46) |

Skew is symmetric in the generator, sitting between the two eras' signs. The 1975-89 worst month is in the 10% tail.

Holdout cross-check: `gm.audit.holdout_power` (the registered code) was run on 10 synthetic 432-month books. Pass-all
probabilities came out at 0.06 / 0.22 / 0.37 / 0.58 at true Sharpe 0 / 0.3 / 0.5 / 0.8. The audit on the real design
returns gave 0.04 / 0.22 / 0.41 / 0.66 (BOOK_FACTS s4). The binding drawdown criterion is a little harsher on synthetic
data (0.73 against 0.84 at Sharpe 0.8). So the generator has slightly deeper falls than the real book, and the power
figures here lean conservative.

**Pods.**
- Systematic pod: K = 8 independent markets. The signal is a Gaussian AR(1) (persistence 0.9 for trend-like and carry
  pods, 0.5 for Strip reversion, re-decided monthly). Market return = m + gamma x signal(t-1) + GARCH-t shock. Pod return
  = mean over markets of signal(t-1) x market return, scaled to 10% volatility. gamma, m and the average exposure b are
  solved in closed form for the target gross Sharpe. Shapes: "timing" (b = 0, all the Sharpe from timing; the default),
  "mixed" (b = 0.5, half from a standing exposure), "static" (all from a standing exposure).
- Rule layer: on/off Markov state with on-share q (5, 10, 25, 50%) and mean spell length L (3, 12, 24 months; card 4 date
  rules are L about 1-3, card 1 rules with a 12-month tail L 12-24). One leg, 10% volatility while on, flat when off,
  no vol rescaling (card 1 s5 convention). Timing skill, optionally plus a market premium earned in on-months. There is
  also a calendar rule (on in 2 of every 12 months).
- "True Sharpe" S is annual, after costs, over all months. It is the brief's 0 / 0.2 / 0.4. Each cell also lists the true
  IR = (S - rho x SR_book) / sqrt(1 - rho^2), computed from the population moments, and IR rows at 0.2 / 0.4. "No skill" =
  gross Sharpe 0, so net = minus costs. "alpha = 0" = S equal to rho x SR_book, the boundary of test 1's null.
- Correlation with the book: book = mean + sigma x (rho x z_pod + sqrt(1 - sum rho^2) x own part), where z_pod is the pod's
  standardised gross return. rho is 0, 0.3 or 0.6; rule layers only 0 and 0.3, because rho 0.6 for a layer that is mostly
  flat would make the book depend on the layer only in on-months.
- Sample: full pod 432 months (1975-2010). Strip reversion 250 months (200 as a sensitivity), ending 2010-12, so all of it
  falls in the 1990-2010 era. Curve carry 260 months (200 and 360 as sensitivities). The spec puts its first month at
  whatever the LSEG lock metadata shows, and grains and metals from 1973 would allow about 360 test months after the
  scalers' 48-month warm-up.
- Costs, in Sharpe units at 10% volatility, as a constant drag, because no spec gives a turnover figure: systematic pod
  0.10, Curve carry 0.20 (two legs, about 12 rolls a year), Strip reversion 0.30 ("turnover is high"), rule layer 0.05
  per on-month unit. Double costs = net minus the same drag again.
- Held size: the pod enters the book at lambda = 0.5 of the book's volatility, i.e. equal risk with one of four equal
  independent pods (WORKFLOW 5.1, 1.3c s5). A rule layer enters at the same size while on. The combined book is rescaled
  to the book's volatility before the tail test ("both books at the same vol target").
- Placebo: the same pod with its signal dates (rule layers: on-states) moved in 12-month blocks in random order. This
  keeps the average exposure exactly and the cross-section intact. 200 shuffles per simulated pod; pass if the share of
  placebos with net Sharpe at least the pod's is below 0.05. Variants: p < 0.10, and pod Sharpe above the placebo mean.
  Calendar rules: 12-month blocks, or a random rotation inside each year.
- Hidden loss (P3): the timing pod at S 0.4, plus a loss of n times its monthly net mean with chance 1/n each month,
  independent of everything else. Its true mean is zero. n = 216, 432, 864.

**Tests on every simulated pod** (the window is the pod's months; the book is cut to the same months):
- T1a: alpha of the least-squares regression of pod on book. One-sided centred stationary bootstrap p, H0 alpha <= 0,
  regression re-fitted in each resample, 10,000 resamples, mean block 6, seed 20261101 (1.3c P2).
- T1d: `paired_sr_test` of book against book + 0.5 x pod (TESTING_PROTOCOL test 1).
- T2: alpha at double costs above 0 (WORKFLOW reading); dSR at double costs above 0 (protocol test 4).
- T3: placebo, as above.
- T4: TESTING_PROTOCOL test 5 as written: max fall of the combined book not more than 2 points worse, worst month not
  more than 1 point worse. Variants 3/1.5 and 4/2.
- ERA: protocol test 3 per era (lower bound above -0.10, at least 60 months, otherwise pass).
- SIZE: dSR at least 0.05.

**Readings:**
- WF_025 = T1a (Holm-adjusted p < 0.025) and T2 (alpha) and T3 and T4. This is WORKFLOW's four decisive tests with test
  1 in the 1.3c P2 form.
- WF_05: the same at 5%.
- WF_era: WF_025 plus ERA.
- WF_dsr: T1d < 0.025 in place of T1a.
- TP_05: TESTING_PROTOCOL tests 1-5 (superiority p < 0.05, size, eras, dSR at double costs, tail), computed with the same
  logic as `gm.protocol.decide`.
- INCUB: mean net return above 0, and T3, and T4 (WORKFLOW s5 Incubator).

## 3. Pass-rate tables

### 3.1 Key table: the four decisive tests together (WF_025, alone in its batch, Holm m = 1), book Sharpe 1.23, rho 0.3

| Shape | no skill | S 0 | S 0.2 | S 0.4 | alpha = 0 (S 0.37) | IR 0.2 | IR 0.4 |
|---|---|---|---|---|---|---|---|
| true IR of the column | -0.49 to -0.70 | -0.39 | -0.18 | +0.03 | 0 | 0.2 | 0.4 |
| Full-sample systematic, 432 m | 0.000 | 0.000 | 0.002 | 0.057 | 0.037 | 0.176 | 0.560 |
| Strip reversion, 250 m | 0.000 | 0.000 | 0.001 | 0.049 | 0.040 | 0.138 | 0.383 |
| Strip reversion, 200 m | 0.000 | 0.004 | 0.011 | 0.052 | 0.037 | 0.114 | 0.342 |
| Curve carry, 260 m | 0.000 | 0.001 | 0.005 | 0.048 | 0.041 | 0.143 | 0.380 |
| Curve carry, 200 m | 0.000 | 0.000 | 0.004 | 0.059 | 0.040 | 0.135 | 0.335 |
| Curve carry, 360 m | 0.000 | 0.000 | 0.001 | 0.042 | 0.029 | 0.177 | 0.470 |
| Rule layer, on 10%, spells 12 m | 0.000 | 0.000 | 0.002 | 0.051 | 0.037 | 0.167 | 0.410 |
| Rule layer, on 25%, spells 12 m | 0.001 | 0.000 | 0.002 | 0.076 | 0.057 | 0.227 | 0.569 |
| Rule layer, on 50%, spells 12 m | 0.000 | 0.001 | 0.003 | 0.075 | 0.051 | 0.236 | 0.517 |

How to read the standalone columns: at rho 0.3 against a 1.23 book, pods with Sharpe 0 to 0.4 truly add nothing (IR at
or below 0.03), so passes near the null rate are correct, not lost power.

The same columns at rho 0 (where S equals IR):
- Full: 0.021 / 0.167 / 0.544 at S 0 / 0.2 / 0.4
- Strip 250: 0.022 / 0.141 / 0.369
- Curve 260: 0.018 / 0.144 / 0.369
- Rule layers: 0.003 / 0.068 / 0.291 (on 10%), 0.008 / 0.131 / 0.481 (on 25%), 0.011 / 0.118 / 0.407 (on 50%)

At rho 0.6 every standalone column is 0.000 to 0.003 (IR -0.42 to -0.92). The IR 0.4 column there: Full 0.408, Strip
0.322, Curve 0.359.

Book Sharpe 0.5, rho 0.3 (IR at S 0.4 = 0.26): Full 0.298 at S 0.4 and 0.580 at IR 0.4; Strip 0.221 / 0.369; Curve
0.188 / 0.418; rule layers 0.21-0.31 / 0.51-0.55.

### 3.2 Each test alone and each conflict reading (book Sharpe 1.23, rho 0.3)

| Shape, truth | T1a 2.5% | T1d 5% | T2 alpha 2x | T3 placebo | T4 tail | ERA | WF_025 | WF_05 | WF_era | WF_dsr | TP_05 | INCUB |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Full, alpha = 0 | 0.041 | 0.006 | 0.246 | 0.859 | 0.733 | 0.007 | 0.037 | 0.062 | 0.004 | 0.002 | 0.002 | 0.648 |
| Full, IR 0.2 | 0.203 | 0.058 | 0.679 | 0.981 | 0.774 | 0.054 | 0.176 | 0.249 | 0.046 | 0.034 | 0.029 | 0.763 |
| Full, IR 0.4 | 0.603 | 0.255 | 0.922 | 0.998 | 0.836 | 0.244 | 0.560 | 0.637 | 0.228 | 0.163 | 0.177 | 0.836 |
| Strip 250, alpha = 0 | 0.041 | 0.014 | 0.089 | 0.900 | 0.694 | 0.083 | 0.040 | 0.064 | 0.039 | 0.007 | 0.014 | 0.644 |
| Strip 250, IR 0.4 | 0.408 | 0.199 | 0.604 | 0.997 | 0.840 | 0.495 | 0.383 | 0.466 | 0.374 | 0.137 | 0.189 | 0.839 |
| Curve 260, alpha = 0 | 0.044 | 0.012 | 0.167 | 0.809 | 0.702 | 0.086 | 0.041 | 0.064 | 0.036 | 0.005 | 0.011 | 0.591 |
| Curve 260, IR 0.4 | 0.408 | 0.172 | 0.753 | 0.990 | 0.831 | 0.489 | 0.380 | 0.487 | 0.352 | 0.105 | 0.165 | 0.826 |
| Curve 360, IR 0.4 | 0.514 | 0.233 | 0.797 | 1.000 | 0.830 | 0.182 | 0.470 | 0.553 | 0.173 | 0.164 | 0.134 | 0.830 |
| Rule 25%, alpha = 0 | 0.057 | 0.047 | 0.465 | 0.640 | 0.763 | 0.268 | 0.057 | 0.089 | 0.054 | 0.029 | 0.030 | 0.532 |
| Rule 25%, IR 0.4 | 0.608 | 0.498 | 0.938 | 0.974 | 0.842 | 0.688 | 0.569 | 0.673 | 0.503 | 0.377 | 0.425 | 0.829 |

What each condition costs on top of T1a (IR 0.4, rho 0.3): with the placebo and double costs added, WF without the tail
equals T1a in every shape (0.603, 0.408, 0.408, 0.608). The tail test takes 0.02 to 0.09. Era decisive takes 0.33 from
full-sample pods and 0.01 to 0.07 from pods that sit in one era. Tail variants: 3/1.5 gives WF 0.579 and 4/2 gives 0.587,
against 0.560 for the full pod.

Sizing (1.3c P2 request): at book Sharpe 1.23 the true held-size dSR is negative for every IR 0.2 pod (-0.017 at rho 0.3,
-0.040 at rho 0). So every IR 0.2 pod the sheet adopts (14 to 24% of them) would lower the book's Sharpe at equal risk.
At rho 0.3 the break-even IR at lambda 0.5 is about 0.24. IR 0.4 pods raise it by +0.05 to +0.06.

### 3.3 Batches: false adoption (B2 = Strip reversion 250 m and a second systematic pod at rho 0.3, plus five rule layers at rho 0.2)

| Book SR | Scenario | Count | T1a alone 2.5% | WF_025 | WF_05 | WF_era | TP_05 |
|---|---|---|---|---|---|---|---|
| 1.23 | all at alpha = 0 | Holm over 7 | 0.033 | 0.032 | 0.053 | 0.028 | 0.010 |
| 1.23 | all at alpha = 0 | Holm over 2 (layers outside) | 0.033 | 0.030 | 0.064 | 0.020 | 0.005 |
| 0.5 | all at alpha = 0 | Holm over 7 | 0.020 | 0.019 | 0.031 | 0.019 | 0.019 |
| 0.5 | all at alpha = 0 | Holm over 2 | 0.028 | 0.027 | 0.048 | 0.023 | 0.019 |
| 1.23 | all at standalone S 0 | either | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

Power in B2 when both systematic pods have IR 0.4 and the layers are null (book Sharpe 1.23):

| Count | Strip reversion (WF_025) | Second systematic pod (WF_025) |
|---|---|---|
| Holm over 7 | 0.193 | 0.322 |
| Holm over 2 | 0.337 | 0.485 |

B1 has one pod (Curve carry), so its rows are the single-pod cells (Curve 260, m = 1).

Incubator rule (no multiplicity), per null layer at standalone S 0: 0.04-0.06. Any of five layers: about 0.2. In the
"alpha = 0" scenario, layers pass Incubator 0.26-0.35 each, because their standalone return is real, only already
held. Incubator asks no question of the book.

### 3.4 Hidden loss (1.3c P3; timing pod, S 0.4 before the loss, rho 0, book Sharpe 1.23)

| n | Loss (share of pod capital at 10% vol) | Share of paths where it shows | WF_025 | Base S 0.4 pod | Ratio | Bound (1 - 1/n)^432 | WF when loss unseen / seen | INCUB (base 0.746) |
|---|---|---|---|---|---|---|---|---|
| 216 | 72% | 0.870 | 0.075 | 0.544 | 0.14 | 0.135 | 0.569 / 0.001 | 0.098 |
| 432 | 144% | 0.618 | 0.222 | 0.544 | 0.41 | 0.367 | 0.581 / 0.000 | 0.289 |
| 864 | 288% | 0.386 | 0.315 | 0.544 | 0.58 | 0.606 | 0.513 / 0.000 | 0.441 |

The 0.58 against the 0.61 bound is within MC error (the hidden-loss pod is drawn independently of the base pod). The P3
row stands: the computed 0.37 is confirmed at n = 432. The losses of n x the mean exceed 100% of pod capital from n = 432
on; at held size 0.5 they are 36-144% of the book.

### 3.5 Placebo forms

| Pod | True S | T3 pass (p < 0.05) | Pod above placebo mean | WF_025 |
|---|---|---|---|---|
| Full, timing (rho 0.3) | 0.4 | 0.890 | 0.998 | 0.045 |
| Full, half standing exposure | 0.4 | 0.367 | 0.914 | 0.045 |
| Full, standing exposure only | 0.4 | 0.052 | 0.506 | 0.018 |
| Full, timing | 0 (gross 0.1) | 0.145 | 0.724 | 0.000 |
| Rule 10% / 25%, market premium only (on-month S 0.3) | | 0.050 / 0.050 | | 0.009 / 0.035 |
| Rule 25%, timing + premium 0.3 (on-month S 0.6) | | 0.223 | | 0.168 |
| Calendar rule, on-month S 0.8, 12-month blocks | | 0.000 | | 0.000 |
| Calendar rule, on-month S 0.8, within-year rotation | | 0.593 | | 0.433 |
| Calendar rule, S 0, rotation | | 0.049 | | 0.014 |

### 3.6 Rule layers: what on-months and episodes allow (rho 0, alpha = on-month timing, all 432 months)

Pass rate of WF_025 (T1a alone in brackets) by realised on-months, pooled over q and L:

| On-month Sharpe | under 24 | 24-47 | 48-95 | 96-143 | 144+ |
|---|---|---|---|---|---|
| 0 (size) | 0.002 (0.002) | 0.005 (0.006) | 0.008 (0.012) | 0.010 (0.019) | 0.015 (0.024) |
| 0.4 | 0.002 (0.002) | 0.019 (0.022) | 0.088 (0.098) | 0.163 (0.199) | 0.202 (0.345) |
| 0.8 | 0.011 (0.011) | 0.091 (0.096) | 0.292 (0.311) | 0.527 (0.610) | 0.673 (0.861) |
| 1.2 | 0.018 (0.019) | 0.173 (0.182) | 0.567 (0.588) | 0.835 (0.888) | 0.882 (0.989) |

Placebo pass by realised episodes:

| On-month Sharpe | 0-2 episodes | 3-5 | 6-9 | 10+ |
|---|---|---|---|---|
| 0.8 | 0.235 | 0.516 | 0.570 | 0.682 |
| 1.2 | 0.383 | 0.708 | 0.790 | 0.889 |
| 0 (size) | 0.043 | 0.062 | 0.062 | 0.067 |

Full grid (q x L x on-month Sharpe): csv/special.csv, block onmonth.

### 3.7 Batch A hygiene (incumbent against a change with true effect delta on book Sharpe, 432 months)

Three tracking levels: the sd of the dSR estimate is 0.016, 0.045 or 0.076, covering batch 0/1's bootstrap SEs of
0.013-0.063. Each cell lists the three levels in that order.

| delta | Superiority (TP 1-5) | NI pooled (lb > -0.10) | NI + era NI | NI against incumbent less 0.23 |
|---|---|---|---|---|
| -0.3 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0.36 / 0.21 / 0.16 |
| -0.2 | 0 / 0 / 0 | 0 / 0 / 0.003 | 0 / 0 / 0 | 0.997 / 0.79 / 0.55 |
| -0.1 | 0 / 0 / 0.001 | 0.087 / 0.061 / 0.092 | 0.004 / 0.005 / 0.003 | 1.0 / 0.99 / 0.90 |
| 0 | 0.001 / 0.048 / 0.053 | 0.998 / 0.750 / 0.442 | 0.940 / 0.265 / 0.106 | 1.0 / 1.0 / 0.98 |
| +0.1 | 0.988 / 0.648 / 0.316 | 1.0 / 0.990 / 0.836 | 0.999 / 0.815 / 0.398 | 1.0 / 1.0 / 1.0 |

The cost difference of a hygiene change is not modelled (dSR at 2x costs taken as dSR).

### 3.8 Holdout (WORKFLOW s6, 189 months; correlation criterion simulated separately)

| True book Sharpe | SR >= 0.3 | Max fall > -25% | 2022 > 0 | All three | All three, Gaussian iid |
|---|---|---|---|---|---|
| 0.0 | 0.142 | 0.154 | 0.489 | 0.052 | 0.052 |
| 0.4 | 0.658 | 0.488 | 0.639 | 0.311 | 0.338 |
| 0.8 | 0.957 | 0.728 | 0.777 | 0.584 | 0.687 |
| 1.2 | 0.997 | 0.858 | 0.874 | 0.763 | 0.860 |

Correlation with the S&P <= 0.3: 1.00 if the true correlation is 0, 0.92 if it is 0.2. The max-fall criterion binds
at every Sharpe, as the audit found.

### 3.9 Robustness of the key cells (rho 0.3, book Sharpe 1.23) to the generator

| Generator | Size of T1a at alpha = 0 (Full / Strip / Curve / Rule 25%) | T4 pass, S 0.4 (Full / Strip / Curve / Rule 25%) | WF_025 at S 0.4 (Full) |
|---|---|---|---|
| Calibrated t5 GARCH | 0.041 / 0.041 / 0.044 / 0.057 | 0.75 / 0.76 / 0.74 / 0.74 | 0.057 |
| t4, GARCH (0.08, 0.90) | 0.043 / 0.040 / 0.027 / 0.039 | 0.79 / 0.76 / 0.77 / 0.74 | 0.043 |
| Gaussian iid | 0.031 / 0.037 / 0.042 / 0.058 | 0.44 / 0.49 / 0.52 / 0.47 | 0.023 |

Tail test detail (csv/tail_probe.csv): for an IR 0.4 pod under the calibrated generator, the combined book's max fall
is worse by more than 2 points in 10-12% of paths. Under Gaussian returns the share is 19-22%, and the worst-month half
fails 19-30%. Under fat tails the book's own extreme month dominates both books. Under thin tails, adding a pod
reshuffles which month is worst. A 1-point margin is about a third of a monthly standard deviation.

### 3.10 Size of test 1 (alpha = 0; csv/size_alpha.csv, 2,000 paths)

| Pod, rho, book SR | Bootstrap p < 0.025 | p < 0.0125 | Newey-West t (normal) < 0.025 |
|---|---|---|---|
| Full, 0, 1.23 | 0.025 | 0.011 | 0.024 |
| Full, 0.3, 0 / 0.5 / 1.23 | 0.019 / 0.026 / 0.034 | 0.012 / 0.015 / 0.021 | 0.019 / 0.024 / 0.030 |
| Full, 0.6, 1.23 | 0.052 | 0.037 | 0.048 |
| Strip 250, 0.3, 1.23 | 0.038 | 0.023 | 0.036 |
| Rule 25%, 0.3, 1.23 | 0.049 | 0.026 | 0.059 |
| Rule 25%, 0, 1.23 | 0.016 | 0.004 | 0.027 |

The excess grows with rho x book Sharpe, and the Newey-West t shares it. This is a finite-sample property of an alpha
measured against a high-Sharpe benchmark (the slope's sampling error times the book's large mean is understated), not a
fault of the bootstrap code. Power at p < 0.0125 against 0.025 (rho 0.3, IR 0.4): Full 0.48 against 0.57, Strip 0.31
against 0.41, Curve 0.32 against 0.40, Rule 25% 0.46 against 0.58.

## 4. Proposal for step 3.4

Each item states its effect on the pass chance. The numbers are at book Sharpe 1.23 and rho 0.3 unless noted.

1. **Decisive statistic of test 1 (new pods and rule layers): alpha with bootstrap p, as 1.3c P2.**
   - Intercept of the least-squares regression of the pod's monthly net return on the Core book's, over the pod's window.
   - One-sided centred stationary bootstrap p, with the registered seed, 10,000 resamples and mean block 6.
   - The Sharpe difference at the held size is reported, not decisive.
   - Effect: power at IR 0.4 is 0.60 (Full), 0.41 (Strip, Curve) and 0.61 (Rule 25%). The dSR form gives 0.26 / 0.20 /
     0.17 / 0.50 at 5%, and 0.16 / 0.14 / 0.11 / 0.38 inside the full sheet.
   - The dSR form also judges the held size, which at a 1.23 book is too large for IR below about 0.24 (section 3.2).
     That belongs to 5.1 sizing, not to the adoption test.
   - Not close; alpha is the reading.

2. **Batch error level: Holm at 2.5% per batch (WORKFLOW s6), counted over the systematic pods of the batch.**
   - Rule layers stay outside the count, because they can only reach Incubator (WORKFLOW s6).
   - Measured false adoption at the null boundary: 0.030-0.033 at book Sharpe 1.23, 0.019-0.027 at 0.5. TESTING_PROTOCOL's
     5% measures 0.053-0.070.
   - 3.4 should write the level as "nominal 2.5%; measured about 3% at correlation <= 0.3 with a 1.23 book, up to about 5%
     for a single pod at correlation 0.6".
   - The alternative that keeps the 2.5% promise is a nominal 1.25% (measured 1.3-2.6%). It costs 8-12 points of power at
     IR 0.4 (section 3.10).
   - Counting the layers in Holm (m = 7) cuts the systematic pods' power from 0.34 / 0.49 to 0.19 / 0.32 while barely
     changing false adoption (0.030 against 0.032).
   - Close call between nominal 2.5% and 1.25%. I propose 2.5% because the excess is about 1 point at the correlations we
     expect, and halving the level costs a fifth to a quarter of the power of a good pod.

3. **Double costs: alpha at twice the costs above 0 (point estimate).** This defines WORKFLOW test 2 for a pod (register
   F5). It binds only when costs in Sharpe units come near the alpha: given that T1a passes, it failed no simulated pod at
   the assumed costs (0.10-0.30). Effect on the pass chance: about 0. It stays decisive, because the costs are guesses
   (no spec gives turnover).

4. **Placebo: permutation test, decisive.**
   - Pass if fewer than 5% of 1,000 placebos (fixed seed; 200 were used here) reach the pod's net Sharpe.
   - Shuffle in 12-month blocks for monthly systematic pods and state rules. For calendar/date rules (card 4), move each
     window to a random start inside its own year (card 4's proposal).
   - Effect: for timing pods, about 0 given T1a. It blocks standing exposures (pass 0.05), which is its purpose. It
     passes half-standing pods 0.37.
   - The point reading ("above the placebo mean") passes a pure standing exposure half the time, so it is not a test.
   - p < 0.10 changes almost nothing (WF 0.560 against 0.560).

5. **Tail test: keep TESTING_PROTOCOL test 5 as registered (2 points / 1 point), decisive, on the combined book at the
   held size, both rescaled to the same volatility.**
   - Effect: -0.02 to -0.07 on good pods (3/1.5 would recover 0.01-0.03).
   - It is the only test that removes a hidden-loss pod whose loss showed (pass 0.000-0.001 when seen).
   - Its false-fail rate depends on the tail shape (section 3.9). 3.4 must fix the held size the test uses for each pod
     and layer (here 0.5 of book volatility).
   - Close between 2/1 and 3/1.5. I keep 2/1 because it is registered and the gain from widening is within 3 points.

6. **Era test: reported, not decisive (WORKFLOW s5; register F2).**
   - Decisive, it cuts full-sample pods at IR 0.4 from 0.56 to 0.23, and Curve carry at 360 months from 0.47 to 0.17. For
     pods that sit in 1990-2010 only, it tests nothing (that era passes by construction).
   - It fails good pods because it tests the held-size combination, which at a 1.23 book barely gains in either era.
   - Not close.

7. **Hygiene (Batch A): non-inferiority, decisive. Pooled one-sided 95% lower bound of dSR above -0.10 (the registered
   margin), plus the tail test; era lower bounds reported.**
   - Effect, at dSR sd 0.016 / 0.045 / 0.076: a truly neutral change passes 1.00 / 0.75 / 0.44. A change costing 0.1
     passes 0.09 / 0.06 / 0.09 (the intended 5%-type level at the margin). A change costing 0.2 passes 0 / 0 / 0.003.
   - Superiority passes a neutral change 0.05 and is the wrong question here.
   - Era NI on top drops the neutral pass to 0.94 / 0.27 / 0.11: too strict, so reported only.
   - "Improves its own target" (rule 3) needs a target per item; 3.4 names it per item, reported.
   - A2 against "incumbent net of 0.23": as a margin shift it passes a change that truly costs 0.2 at 0.55-1.0. The shift
     corrects the selection bias only if 0.23 is right, and its own spread (sd 0.11 over 32 variants) is as large as the
     margin. I propose A2 against the incumbent as run, with the expected averaging cost (about 0.23) printed beside the
     result and not subtracted. It is close only if one trusts 0.23 to within 0.05, which the trial log does not support.

8. **Rule layers: minimum sample to be judged at all.** At least 48 on-months over the window and at least 3 episodes
   (spells of on-months separated by 12 or more off-months, as cards 1 and 2 close it).
   - Below 48 on-months, a layer with on-month Sharpe 1.2 passes 0.17-0.18 and one with 0.8 passes 0.09.
   - With 0-2 episodes the placebo passes 0.24 / 0.38 at on-month Sharpe 0.8 / 1.2, against 0.52 / 0.71 at 3-5.
   - A layer under either floor is "not judgeable": an analyst watch condition, not Shelved, because failing such a test
     carries no information.
   - For an even chance at on-month Sharpe 0.8 a layer needs about 100 on-months.
   - This replaces the cards' differing gates: C1-D1's 6 episodes is stricter on episodes, while C2-D2's 24 on-months and
     3 episodes is too low on months.
   - Effect: removes layers whose expected pass rate is under 0.2 even at implausible skill.

9. **Incubator rule.** Read "positive after costs" as alpha above 0 at single costs, not mean above 0, and keep placebo and
   tail. Standalone, the rule passes 0.26-0.35 of layers that only repeat what the book holds (alpha = 0) and 0.65 of
   systematic pods at alpha = 0. The estimated alpha is above 0 in only about half the paths at alpha = 0, so this reading
   roughly halves those rates. For true no-skill pods it stays near the placebo's 0.04-0.06. This reading was not
   simulated as a separate column; the halving is reasoned from the alpha estimate's symmetry at the null.

10. **Pod-level reading of power for 3.4's one-page summary.**
    - A pod uncorrelated with the book needs a true Sharpe of about 0.4 to have even odds over 432 months, and is passed
      about 0.37 of the time over 250-260 months.
    - A pod correlated 0.3 needs a standalone Sharpe of about 0.75 (IR 0.4).
    - Strip reversion (graded WEAK, 250 months) has about a 1 in 3 chance even if its IR is 0.4, and about 1 in 7 at IR 0.2.
    - A failed test therefore does not refute a weak pod. WORKFLOW 4.6 must say "not shown", not "refuted", for pods
      with these windows.

## 5. What the simulation does not capture, and how big the mistake could be

- **Fat tails and skew.** The book generator is symmetric. The 1975-89 skew of -0.65 lies at its 10% point, and a
  negatively skewed book would make the tail test harsher. Under thin tails the tail test fails good pods 2-3 times as
  often (section 3.9). Test 1's size moves by about 1 point across generators. Power changes are small, 0.02-0.03.
- **Pod shape.** Systematic pods average 8 independent markets, so their own tails are near-Gaussian. A pod with
  short-option-like returns would meet the tail test more often. That is P3's territory: a loss that did not happen is not
  seen (section 3.4).
- **Regime shifts.** Skill is constant over the window. A pod whose edge fades (charter D5, Tropin's "rules decay")
  concentrates its alpha in early years. Test 1 then sees a smaller average IR, and the era test (reported) shows the
  fade. Power for a pod with IR 0.4 in one era and 0 in the other is roughly that of IR 0.2 over the full window: 0.18
  instead of 0.56.
- **Overlap between pods.** In batches the pods are independent given the book. Correlated pods in one batch make Holm
  conservative (false adoption below the figures in 3.3). Netting across cards (B19) is not modelled.
- **The book is fixed.** The Core book is simulated as an exogenous series with known Sharpe. In practice it is itself
  estimated, and the "Core book" for C3-D1 does not exist before B1/B2 (CHECK_3.2_C item 6). If the book's true Sharpe is
  0.5 rather than 1.23, standalone-Sharpe pods pass far more often (S 0.4 at rho 0.3: 0.30 instead of 0.06), because they
  then add something.
- **Costs and sizing are guesses.** The drag assumptions (0.05-0.30 Sharpe) were never binding given T1a. A pod with a
  true cost above its alpha is not represented beyond the "no skill" rows.
- **Held size and caps.** Strip reversion and Curve carry run below target volatility under their caps (CHECK_3.2_B).
  Alpha's p-value does not depend on scale, so test 1 is unaffected. The tail test at held size is affected through
  lambda; at a lower lambda it passes more often.
- **The bootstrap's own error.** The slightly liberal size of test 1 (section 3.10) is measured under this generator. Real
  data with stronger volatility clustering could raise it further. The holdout cross-check suggests the generator is, if
  anything, rougher than the real book.
- **Monte Carlo error.** About +/-0.016 on a pass rate of 0.5 and +/-0.006 on a rate of 0.03 (1,000 paths).

## 6. Runtime and how to re-run

- Main runs, two in parallel, single-threaded BLAS each:
  - `python3 work/power_3_3.py --part validate,calib,cells --reps 1000`: 947 s (168 cells).
  - `python3 work/power_3_3.py --part special,batch,hygiene,holdout,robust --reps 1000`: 934 s.
- Probes: `work/size_probe2.py` (about 6 min), `work/level_probe.py` (about 4 min), `work/tail_probe.py` (about 4 min).
  Tables: `python3 work/make_tables.py`.
- Every draw is seeded from SHA-256(master seed 3303 + cell description), so re-runs reproduce exactly. The bootstrap
  uses the registered seed 20261101 through `gm.stats._stationary_idx`.
- How the speed is achieved: every bootstrap statistic is a linear function of the resample counts. One matrix product
  (10,000 x T counts times the series) gives all 10,000 resamples for 250 paths at once.
- `--quick` runs a 1/7 subset; the environment variable `NPL` sets the number of placebo shuffles.
- Requirements: numpy, pandas, and the repo on the path (read-only).
