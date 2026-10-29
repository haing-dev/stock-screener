# Independent audit: candidate 5.0 backtest (hf/ research), 2026-10-29

Scope: rpanel.py, lab.py, base.py, exp_combo.py, robust5.py, exp_loc.py, exp_exp.py; macro/engine.py (calc_all,
scores/expanding_pct, derisk, fred_monthly, build_returns, portfolio, tilt_weights); macro/registry.py (FRED lags).
The existing files were not modified. Test code: `audit_lib.py`, `audit_1_bonds_gold.py`, `audit_2_decompose.py`,
`audit_3_selection.py`, `audit_4_costs_data.py`, `audit_5_combined.py`. Run them with `python3 audit_N_*.py` from this folder.

Reproduced first (audit_1): S&P 500 12.4%, live 4.1 14.1% (Sharpe 0.77), candidate 5.0 16.2% (Sharpe 0.99), 1975-02..2026-10.
The numbers match the claim exactly.

## Bottom line

| 1975-2026, CAGR / worst fall / Sharpe | live 4.1 | candidate 5.0 | gap |
|---|---|---|---|
| As published (0.1% cost) | 14.1% / -20% / 0.77 | 16.2% / -18% / 0.99 | +2.1 |
| Exact month-end Treasury returns | 13.9% / 0.77 | 16.0% / 0.99 | +2.1 |
| + gold signal known at t + 0.3% cost | 13.6% / -20% / 0.75 | 15.2% / -18% / 0.93 | +1.6 |
| Same, without melt-up and squeeze cuts | 13.6% | 13.9% / 0.78 | +0.3 |

The mechanical fixes (timing, data, costs) cut about 1 point from the candidate and 0.5 from live. The larger problem
is inference. The two layers that produce most of the remaining gain are each active in only one half of the
sample, and each rests on two or three episodes. The candidate was picked from a 300-variant grid scored on the full sample.
After correcting for that many trials, the gain over live is not significant at the 95% level (deflated Sharpe probability 0.87).

---

## HIGH severity

### H1. Selection on the full sample. The "both halves" check does not test the new cuts.
Files: exp_combo.py:1-9 (grid "pre-registered 2026-10-29 *after* Exp 1-3", layer options kept because they "did not
lose in either half"), exp_combo.py:111-113 (ranking), exp_exp.py:27 and :31 (squeeze, melt-up), robust5.py:1-5.

- **Squeeze cut:** the squeeze score first exists in 1988-11, because DXY starts in 1985 and the score needs 60 months for
  the z-score plus 120 for the percentile. It is first on in 1997-01. It is on for 60 months, and 2000 (10 months) and
  2021-23 (21 months) dominate. It therefore cannot lose in 1975-2000. In 1975-2000 the "squeeze cut0" variant differs
  from live only through 1997-2000.
- **Melt-up cut:** on for 10 months in total: 1980-01/02, 1980-11/12, 1981-04/05/06, 1987-08/09 and 1999-10. Sharpe in
  2001-2026 is 0.81, the same as live. So it cannot lose there either. Its gain comes from two episodes, the Volcker
  1980-81 period and the 1987 crash.
- **Which layer does what** (audit_2): melt-up alone gives +0.8 pts CAGR, all of it before 2001. Squeeze alone gives
  +0.7 pts, almost all after 1997. The sector tilt gives +0.5. D7 and the inflation sleeve give about 0 each. Removing the
  sleeve from the candidate *raises* CAGR to 16.3%.
- **Concentration:** the 10 best months of candidate minus live supply 79% of the total log gain, and the top 20 months
  supply 120%. The best months are 1980-03 (+10.3 pts), 1987-10 (+9.8), 2022-04 (+9.1), 2022-06, 2018-10, 2015-08,
  2022-01, 1997-08, 2000-01 and 2010-06. Swapping just those 10 months for live's returns leaves 14.5% against live's 14.1%.
- **Rank:** the candidate is #2 of 200 on the author's own selection criterion (the worse half's Sharpe gain), #15 by
  full-period CAGR and #34 by Sharpe. It was picked from the top of the grid, and its Exp 3 modes (cut0 rather than cut50 or gate) were
  also the best full-sample modes (audit_3 section c).
- **Deflated Sharpe** of the active return (candidate minus live): the annualised information ratio is 0.37, with skew
  2.65 and kurtosis 21, so a few big months drive it. The naive p-value is 0.9986. With N = 299 trials the deflated
  probability is 0.878; with N ≈ 360 (Exp 2-4) it is 0.871. With an "effective N" of 2.9 from the eigenvalue
  participation ratio it is 0.993. The eigenvalue figure is a lower bound on the true number of trials, because Exp 1-3
  and the earlier macro_combos rounds are not in the grid.
- **Walk-forward choice inside the grid** (re-picked each January by Sharpe since 1975): 15.0% in 1985-2026 against
  13.8% for live, so some gain survives. But the grid's menu was itself built from full-sample Exp 1-3 results, so this
  is an upper bound.
- The author's CSCV and PBO (0.08), the placebo and the bootstrap in robust5.py:41-84 all run *within* the final
  grid, or on the candidate *after* it was chosen. None of them accounts for the earlier selection rounds.

**Fix:** treat 16.2% as an in-sample figure. Report the deflated Sharpe with the full trial count. The squeeze and
melt-up rules each have one regime of evidence, so either adopt them only on prior reasoning or keep them in paper
tracking. If they are kept, state that squeeze is unvalidated before 1997 and melt-up unvalidated after 2000.
Re-select on a split where both rules can be active, or freeze the candidate today and score it forward in
`macro-record`.

### H2. The "untouched" 1966-1974 window does not test the candidate.
File: robust5.py:21-26. Evidence from audit_2, last section.
- In 1966-1974 the squeeze score exists in 0 of 108 months and melt-up is on in 0 months. The window cannot test either
  new cut.
- The candidate's 10.5% against live's 7.6% comes almost entirely from the gold sleeve, which is on in 65 of the 108
  months. Without the sleeve the candidate earns 7.8%.
- Gold was pegged at $35 until 1968 and ran a two-tier market after that. US individuals could not legally own bullion
  until 31 Dec 1974. The gold returns used for this period are the look-ahead month-end estimate (M3).

**Fix:** drop the claim that 1966-1974 validates the candidate. If the window is kept, exclude gold before 1975 and
report that the new cuts are inactive there.

### H3. One-month dating error in non-US index and Yahoo FX files, which feed the country proxies.
Files: rpanel.py:34-52 (`csvm`/`y`: date to period with no time-zone handling), rpanel.py:146-157 (FX, `local_usd`).
- Yahoo stamps each monthly bar at local midnight on the 1st, which falls on the previous day in UTC. Every bar of
  ^N225, ^KS11, ^HSI, ^TWII, ^BSESN, ^AXJO, ^GDAXI, ^FCHI, ^STOXX50E and 000001.SS is dated at the previous month's end.
  So each value sits one month early: the 1996-12 KOSPI value in the panel is 685.84, the Jan-1997 close; the
  true Dec-1996 close is 651.22. The 1985-01 Nikkei value is 12,322; the true close is 11,992.
- In the FX files (KRW=X, JPY=X, INR=X, BRL=X, MXN=X, CNY=X, EURUSD=X, AUDUSD=X) and in ^FTSE, the shift happens only
  in summer-time months. That gives a one-month lead for about 7 months a year and leaves **every October missing**
  (21 missing months since 2005).
- The India proxy (^BSESN / INR, used for 1997-2012) correlates 0.15 with correctly dated data in the same month, and
  0.70 with the next month.
- Effect (audit_4): Exp 2 "L3 country momentum top 3", fully invested, 1997-2011, falls from 15.4% to **12.3%**
  (Sharpe 0.59 to 0.49). Over 1997-2026 it falls from 13.2% to 11.7%.
- Candidate 5.0 is **not** affected, because L4 uses US sector ETFs and French industries, and US-listed Yahoo files are
  dated correctly. The error does contaminate Exp 2, the L1-L3 cells of the 300-variant grid (and so the CSCV, the layer
  averages and the walk-forward, which picked L2/L3 in some years), robust5.py:38 ("China cycle instead of sector
  tilt"), and the `px_^N225`, `px_^KS11` and `*=X` signals in S.

**Fix:** in `csvm`, map each date to `(date + 2 days).to_period("M")` for all Yahoo bars except the trailing live
quote, or keep the timestamps in exchange time. Add assertions against known closes. Rebuild rpanel.pkl and re-run
Exp 2 and Exp 4.

## MEDIUM severity

### M1. Costs are low for a strategy that trades 2.3 times as much as live.
Files: lab.py:14 (COST = 0.10% per 100% traded), lab.py:32.
- One-way turnover is 311% of the book per year for the candidate against 133% for live. Of the candidate's turnover,
  112% a year is the sector tilt. Before 2006, 356 of the 621 months have 10 or more of the 20 sectors on French
  industry proxies, which cannot be traded as baskets at 0.1%.
- CAGR at 0.1%, 0.3% and 0.5% per trade: candidate 16.18%, 15.46% and 14.75%; live 14.08%, 13.78% and 13.47%.
  The gap shrinks from 2.1 to 1.7 to 1.3.
- Drift rebalancing is ignored, which matters little (16.18% becomes 16.17%).
- The live engine's published backtest has no costs at all (engine.py:494).

**Fix:** use 0.2-0.3% before about 2000 (S&P futures only from 1982; no sector ETFs) and report the sensitivity.

### M2. Synthetic Treasury returns are built from monthly-average yields with a fixed duration.
Files: rpanel.py:104-110 (`syn`, GS10 with d=7, GS30 with d=15); live engine engine.py:487-489 (same construction).
- A change between two monthly averages measures roughly mid-month to mid-month. So half of the "month t+1" price move
  actually happened in the second half of month t, before the end-of-month decision. The series is also smoothed.
- Against TLT over 2006-2026, the average-yield synthetic correlates 0.72 in the same month and **0.54 with TLT one
  month earlier**, with volatility of 10.0% against 13.9%. Exact par-bond pricing on month-end DGS30/DGS10 yields
  correlates 0.99, with 0.06 to the month before.
- A duration of 15 is also too high when yields are 12-14%: the true modified duration of a 30-year bond then is about
  8. In the single 1980 month the candidate held, the author's return is +21.2% against an exact +12.1%.
- Effect: over the 31 months the candidate holds t30y, the bonds earn +82% under the author's construction against
  +70% exact. Candidate CAGR goes from 16.2% to 16.0%; live from 14.1% to 13.9%.
- The effect is small here only because the bond switch is rare. The same series drives the live engine's
  published 4.1 track record and all bond-sleeve research.

**Fix:** use month-end DGS10/DGS30 (daily, last value) with exact par-bond pricing (`audit_lib.par_bond_ret`) in
both rpanel.py and engine.derisk. The stock-bond *correlation signal* (engine.py:226-229) uses data known at t, so it
can keep monthly averages.

### M3. The gold estimate before 2000 uses next month's average, and that estimate feeds the signal.
Files: rpanel.py:119-125 (`end_est = sqrt(avg_t * avg_{t+1})`); exp_combo.py:18 `gold_up = above_ma("gold")`, via
lab.py:76-78, which builds the level from those returns.
- The level at t contains avg_{t+1}, which includes prices up to the end of month t+1, so `gold_up` at t is not known
  at t. Using the estimate for *returns* is acceptable; using it in the *signal* is look-ahead.
- In 1975-2000/08, next-month gold returns average 17.5%/yr when the author's signal is on, against 14.0% when a
  signal built from the known monthly average is on. The two signals disagree in 11 of the sleeve's months.
- Effect: candidate CAGR goes from 16.2% to 16.1%. Most of the impact is on the 1966-74 claim (H2).
- Also, 8 GC=F months between 2000-10 and 2004-08 are missing and fall back to the same estimate.

**Fix:** build the signal from `g_avg_t > mean(g_avg_{t-9..t})`, or lag the estimated level by one month. Get a
month-end London PM fix for returns.

### M4. The baseline is also in-sample, and the "S&P 500" label is wrong before 1993.
- Live 4.1's parameters (15/35% band, worst fifth, Fed gate of 1 pt over 24 months, growth-trend cut, bonds when the
  correlation is below 0) were chosen on the same 1975-2026 data in the macro_combos rounds. Both 14.1% and 16.2% are
  therefore in-sample.
- `mkt` before SPY (1993) is the French all-CRSP value-weighted market (engine.py:109-112), not the S&P 500.

**Fix:** label the series correctly, and report forward results from the `macro-record` ledger as the only
out-of-sample evidence.

## LOW severity

- **L1. Duplicate sector proxies.** KBE and KRE are both French "Banks" for 551 months (to 2005-11), so they tie in the
  momentum rank and banks get twice the tilt. The XBI proxy (Drugs) is also part of XLV. Registry INDUSTRIES; exp_combo.py:43-52.
  Fix: exclude KRE before its ETF exists.
- **L2. Next-month availability used as an input.** `avail = rets.shift(-1).notna()` (exp_combo.py:49; same pattern in
  engine.backtest:632), `have()` (exp_combo.py:32-33) and `W_top` (exp_loc.py:44) all check whether next month's data
  exists. This has no effect on sectors after 1975 (no gaps). It is small for countries, but combined with H3's missing
  Octobers it decides which countries can be held. Fix: use data availability at t.
- **L3. Rows with missing data.** 100 D6 variants (2-year Treasuries, 1976+) have one NaN month. They drop silently
  out of the full-period ranking, and CSCV's `np.nansum` treats the NaN as a zero excess return (exp_combo.py:137).
  There are no NaN months in any asset the candidate holds after 1975, and nothing is silently filled with 0 in
  `run()`: a held NaN voids the month (lab.py:27-31).
- **L4. Partial final month.** The last month, 2026-10, runs only to the 29th (Yahoo trailing quote) but sits inside
  every window.
- **L5. Sharpe formula.** lab.stats divides mean excess return by the standard deviation of *total* return. Immaterial.
- **L6. Japan FX.** The JPY rate before Yahoo coverage is EXJPUS, a monthly *average*, divided into a month-end index
  (rpanel.py:147). It affects the Japan proxy only.
- **L7. Shiller earnings.** E/P is lagged 3 months (exp_exp.py:39), but Shiller's latest E values are estimates, and
  the series is interpolated from quarterly data. It is used only in Exp 3's erp1, not in the candidate.
- **L8. Bad-tick clip.** `R[R.abs() > 3] = NaN` (rpanel.py:185) only removes bad ticks. No asset in the candidate has
  a monthly move above 50%.

## Checked and found correct

- lab.run: weights decided at t earn t+1 (`W.shift(1)`, lab.py:26), and turnover is charged in the month it occurs.
  engine.portfolio and engine.derisk shift the same way.
- `cpi_yy` (base.py:30): the CPIAUCNS value for month m is used from the end of m+1; the release comes mid-month.
- FRED lags (registry.py:59-71): UNRATE and other first releases have lag 1, PCE lag 2, quarterly series lag 2-3 after
  the quarter's last month. FEDFUNDS, GS10 and GS2 are monthly averages with lag 0, which are known by month-end.
  WTISPLC has lag 1, which is conservative. The manifest shows `fred_key: true` and first-release vintages.
- Squeeze score (engine.py:230-235): DXY is the Yahoo month-end value, dated correctly for a US-listed index; TWEX
  is lagged 0; oil is lagged 1. The z-scores use an expanding standard deviation and the score is an expanding
  percentile. Everything used is known at t.
- Warning share (engine.derisk:461-475): the outcome of month s (a fall within s+1..s+12) enters only from s+12
  (`cumsum().shift(hz)`). This is walk-forward and correct.
- Growth-trend cut: the S&P month-end close against its 10-month average at t; unemployment lagged 1.
- Sector momentum: `cumret(rets, 12).shift(1)` is 12-1 momentum known at t. The tilt applies only when e = 1 at t.
- Stock-bond correlation: a 12-month window ending at t.
- AQR commodities are month-end dated and correlate 0.92 with DBC over 2006-2025, with no lead or lag (0.20 / 0.13).
  The rf is added correctly to the excess returns. The DBC splice starts at 2006-03.
- No duplicated months. The French industry parser takes the value-weighted monthly block and filters out -99.99.
  Yahoo ETF data are adjusted closes (dividends included).
