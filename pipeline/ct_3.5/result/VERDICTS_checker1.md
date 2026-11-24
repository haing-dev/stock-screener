# Checker verdicts, check_1 (brief v1, 2026-11-24)

Every case was run as given and reproduced the report's figures exactly. Two generic tests run on all ten
(work/lookahead_test.py: scramble every input dated after 1995-06 -> net up to 1995-06 unchanged in all ten;
work/samebar_test.py: net(T) linear in R(T) at five dates -> no position reads its own month's return in any case).
Publication lags and costs were checked line by line against each spec.

C04 | verdict: CLEAN | defect type(s): none | evidence: momentum = R.shift(1).rolling(12).sum() = months t-12..t-1
(backtest.py:24); held = pos.shift(1), cost on held.diff() at 1 bp (:38-40); window 1975-01..2010-12. Reproduced net
0.32 / gross 0.35 / 2x 0.29 / eras -0.02, 0.71 / costs 0.30%. The report's "weak, not stable" reading matches. | confidence: high

C05 | verdict: DEFECT | defect type(s): period-selection (market subset), report-mismatch | evidence: spec s5 says the
headline is the net Sharpe of all three classes (FI+FX+CM). The report leads with "core carry (FX+CM)" net 0.53
(backtest.py:58-62), a subset that drops the losing bond block (FI only -0.23) after seeing it. Registered headline
reproduced: net 0.22, gross 0.24, 2x 0.21, eras 0.26 / 0.20, DD -51.7%. These are given only lower down in the report. | confidence: high

C06 | verdict: CLEAN | defect type(s): none | evidence: u uses vol(t-1) (backtest.py:33), gap = L - 3-month mean of L
(:35), k = -z/2 x 0.10/(su sqrt12) (:38), legs k/va, -k/vb, 1/sqrt(live pairs), held = shift(1), costs per leg on
held.diff() with the class bp (:49-52). Reproduced net 0.89 / gross 1.09 / 2x 0.67 / eras 0.87, 0.92 / costs 1.12%.
Costs are 0.196 of the gross (the report says "a fifth"). | confidence: high

C07 | verdict: CLEAN | defect type(s): none | evidence: the expanding mean and std include t with min 60 (backtest.py:24-26),
as registered ("up to and including t"). Vol 36/24, per-class 1/sqrt(live), held = shift(1), costs EQ/FX 2, CM 4 bp.
Reproduced net 0.10 / gross 0.11 / 2x 0.09 / eras 0.47, -0.25 / EQ 0.18, FX 0.07, CM -0.07 / costs 0.13%.
The report's "fails" is honest. | confidence: high

C08 | verdict: DEFECT | defect type(s): look-ahead (publication lag ignored) | evidence: backtest.py:30 reads
MACRO["us_cpi"] at t, which is the value for reference month t. Spec s2.1 says only t-1 is known at the close of t,
because the month-t CPI is published during month t+1, the month the position is held. With the lag fixed
(`.shift(1)`, work/C08/fixed.py), net Sharpe goes from 0.23 to -0.18, gross from 0.24 to -0.17, and the eras from 0.41 / 0.07
to 0.16 / -0.48. Mean on-months goes from +0.44% to -0.35% and positive months from 54% to 47%. The reported edge is all look-ahead. | confidence: high

C10 | verdict: DEFECT | defect type(s): costs | evidence: backtest.py:18 sets ONE_WAY = 1.0e-5, which is 0.1 bp. The spec
registers 1 bp for trades and for rolls (|notional| x 2 x 4/12 x 1 bp), so both charges are 10x too small. With 1.0e-4
(work/C10/fixed.py): costs go from 0.13% to 1.31%/yr, net Sharpe from 0.41 to 0.11, 2x costs from 0.38 to -0.21, and the eras from 0.40 / 0.42
to 0.22 / 0.04 (gross 0.45 unchanged). The report's "costs take little of it" is false. | confidence: high

C11 | verdict: CLEAN | defect type(s): none | evidence: sign of the 1/3/12-month sums up to t (backtest.py:24); EWMA of
squared returns, half-life 6, min 12 (:20); per-class 1/sqrt(live); gross = pos.shift(1) x R; cost = trade.shift(1)
x class bp (:43-45). Reproduced net 0.66 / gross 0.72 / 2x 0.60 / eras 0.45, 0.86 / costs 0.93% / turnover 55.4x. | confidence: high

C16 | verdict: CLEAN | defect type(s): none | evidence: the sign and rank versions match the spec (the rank version
sums to n, and there is no position under 3 markets, backtest.py:26-31). The pod is the mean of the two versions,
with a missing one counted as 0 (:42-43). The cost is charged on the pod's netted position (:47-51). Reproduced
net -0.15 / gross -0.13 / 2x -0.17 / eras 0.03, -0.31 / sign -0.23, rank 0.20 / costs 0.12%. The report keeps the pod
as registered and does not switch to the ranked version. | confidence: high

C19 | verdict: DEFECT | defect type(s): sample, report-mismatch | evidence: backtest.py:21 `R.dropna(how="any")` deletes
every month before the last market starts (natgas 1990-04), against spec s2.1 ("each market enters when its own data
allow"). The run has 249 months from 1990-04 and positions only from 1992-04, so the "1975-1992" era is 9 live months
(vol 3.21%, DD -1.9%), not the registered 432-month window the report claims. Without the dropna (work/C19/probe.py):
net 0.39 (not 0.94), gross 0.40, 2x 0.38, eras -0.05 / 0.99, DD -58.1%. | confidence: high

C20 | verdict: DEFECT | defect type(s): tuned-knob | evidence: the spec does not fix the look-back ("as set in
backtest.py (LOOK)"), and LOOK = 2 (backtest.py:15) is the best value. Moving it on the registered window
(work/C20/l*.py) gives net Sharpe 0.10 at LOOK=1, 0.34 at 2, 0.24 at 3, 0.22 at 4 and 0.24 at 6. The headline is the peak and
falls by 0.24 one step down. The report's "robust" covers costs only. Otherwise the code is sound (timing, costs, window). | confidence: medium-high
