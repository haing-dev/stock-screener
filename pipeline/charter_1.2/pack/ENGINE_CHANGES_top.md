# Global Macro Book: rule changes and trial log

Every rule change gets a new VERSION in gm/run.py and a line here. Every variant tested on the design period
(1990-2010; extra check 1975-89) is logged so the deflated Sharpe can count the trials. The holdout (2011-2026) is run
once, after the rules are frozen, by gm/holdout.py.

## gm-1.2.1 and gm-2.0.1 candidate (registered 2026-11-11, BEFORE the code change): input-layer look-ahead removed
Found by the block 3 truncation test (docs/research/bbg/BLOCK3_engine_2026-11-11.md; 8 cut dates 1980-2010, loader-level
cuts, stricter than the gm-1.2.0 audit). Signals, volatility, positions and book code are clean; four places in the
input layer read the whole sample. The fixes below are the point-in-time form of each existing rule. They were fixed
here before any number was produced and are not to be tuned after the results.
1. C1 gm/panel.py, pre-total-return dividend proxy: the yield added in month t is the mean gap between total-return
   and price-index returns over overlap months up to t only, used when more than 60 such months exist (same
   threshold), otherwise the registered constant per market. (Before total-return data exist this is the constant.)
2. C2 gm/panel.py, local-rate stand-in for equity excess returns: `gap = rl.isna() & (GRID >= 1990-01) &
   rl.notna().cummax()` (the stand-in is used only after the local rate has first appeared, decided month by month).
3. C3 gm/daily.py: the whole-sample "more than 500 days" gate is dropped (the volatility estimate already needs its
   own minimum of observations).
4. C4 Bloomberg paths (gm/panel.py commodity_return, gm/signals.py carry_values and growth_surprise, gm/bloomberg.py
   index choice): "more than 24 / 36 observations" is counted on observations up to each month; a choice between two
   series is a fixed preference order written in gm/config.py, not a comparison of sample lengths. Inactive on free data.
Gate: the truncation test passes at all 8 cut dates for BASE and CANDIDATE on free data (and the Bloomberg-input cut
on mock data). Reported once: design-period statistics before and after (1975-2010, 1990-2010). Logged in
gm/trials.csv as one fix run per config (not a selection trial). Live paper ledger: untouched; the next live run
restates under the new version name. Holdout not run.

Result (2026-11-12, gm-1.2.1 / gm-2.0.1-candidate, free data, design months only): truncation test PASS at all 8 cut
dates (1980-06 ... 2010-12), every stage (panel, daily, the four signal families, volatility, family positions,
positions, book returns) for BASE and CANDIDATE, 0 differing market-months; with Bloomberg inputs from mock workbooks
(245 tickers through the adapter) PASS at 1984-12, 1995-12 and 2007-06. Only C1 changes design numbers: 631 equity
market-months in 8 markets (eq_us_ndx 170, eq_us_r2k 152, eq_fr_cac 106, eq_br_ibov 45, eq_cn 41, eq_kr_kospi 41,
eq_in 41, eq_tw 35; 1985-02 to 2000-12), largest monthly return change 0.33 percentage points (eq_cn); C2 and C3, run
alone, change no design number; C4 is inactive on free data. Net of costs, old -> new:
| Config | Period | Sharpe | Mean %/yr | Vol %/yr | Worst drawdown % |
|---|---|---|---|---|---|
| BASE gm-1.2.0 -> gm-1.2.1 | 1975-2010 | 1.235 -> 1.236 | 12.48 -> 12.49 | 10.10 -> 10.11 | -20.5 -> -20.5 |
| BASE gm-1.2.0 -> gm-1.2.1 | 1990-2010 | 1.475 -> 1.474 | 14.40 -> 14.41 | 9.77 -> 9.77 | -12.3 -> -12.3 |
| CANDIDATE gm-2.0 -> gm-2.0.1 | 1975-2010 | 1.464 -> 1.464 | 14.32 -> 14.33 | 9.78 -> 9.78 | -16.8 -> -16.8 |
| CANDIDATE gm-2.0 -> gm-2.0.1 | 1990-2010 | 1.630 -> 1.629 | 16.34 -> 16.34 | 10.03 -> 10.03 | -16.8 -> -16.8 |
C4 preference order (gm/config.py BBG_ER_PREFERENCE): S&P GSCI before BCOM, decided by the ticker's index family only.
Logged in gm/trials.csv as family "fix" (two rows, not counted as book trials). Reference: tools/bbgq/engine_ref.json
(old one kept as engine_ref_gm-1.2.0.json).

