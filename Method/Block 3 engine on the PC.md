---
tags: [method, spec]
file: /home/claude/stock-screener/docs/research/bbg/BLOCK3_engine_2026-11-11.md
---
# Block 3 (WORKFLOW v2.1 step 0.5): engine on the PC, 2026-11-11

Gate: "must reproduce the current book on free data; truncation test passes".
Result: **reproduction PASS; truncation FAIL with three causes in the input layer** (rules themselves are clean).
Built by Opus (commit 591c54a, ~460k tokens), re-checked by a second Opus that did not see the build (~317k tokens).
Design period only (months up to 2010-12); nothing after 2010 was printed or inspected.

## Reproduction
- Reference (cloud, free data, net of costs, `tools/bbgq/engine_ref.json`, gm commit 2e1b35a5a2):

| config | era | Sharpe | mean %/yr | vol % | worst fall % |
|---|---|---|---|---|---|
| BASE gm-1.2 | 1975-2010 | 1.235 | 12.48 | 10.10 | -20.5 |
| BASE gm-1.2 | 1990-2010 | 1.475 | 14.40 | 9.77 | -12.3 |
| CANDIDATE gm-2.0 | 1975-2010 | 1.464 | 14.32 | 9.78 | -16.8 |
| CANDIDATE gm-2.0 | 1990-2010 | 1.630 | 16.34 | 10.03 | -16.8 |

- PC run (`tools/bbgq/results/gm_repro_v1.txt`; Python 3.15.0, pandas 3.1.1, numpy 2.5.4, no xlrd): 24 of 24 items PASS,
  largest difference 0. gm/ code identical (18 files), 239 free input files identical.
- The checker recomputed the four rows with its own script (not through the helper): max difference 5e-13. Eight
  deliberate errors (one-month lag, sign flip of one market, costs x1.001, one cell changed by 1e-4, ...) all make the
  comparison FAIL, so the fingerprint is strong enough.

## Truncation test (cut every input at T; decisions up to T must not change)
Report: `tools/bbgq/results/engine_trunc_cloud_2026-11-11.txt` (8 cut dates 1980-2010). Each stage run alone on
identical inputs passes at every date (signals, volatility, family positions, positions, book); the checker's poison
test (absurd values after T) agrees. The cut at 2010-12 passes: no data after 2010 moves a design-period number.
Failures all come from three places that read the whole sample:

| id | where | what | fix (new registered engine version; NOT applied) |
|---|---|---|---|
| C1 | gm/panel.py ~455-462 | dividend yield added to early price-index equity returns is one mean up to 2010-12, with whole-sample `>60` gates (eq_us_ndx, eq_us_r2k, eq_fr_cac and EM) | expanding estimate (mostly falls back to the registered constant) or a registered fixed yield; changes numbers |
| C2 | gm/panel.py 428 | local-rate stand-in starts at the first month the local rate exists in the sample (eq_mx, eq_br, eq_kr, eq_cn) | `gap = rl.isna() & (GRID >= 1990-01) & rl.notna().cummax()`: causal, same design numbers |
| C3 | gm/daily.py 130/134/147 | a daily series is kept only if it has more than 500 days in the whole sample (changes CANDIDATE's hybrid volatility) | drop the gate; changes no number on today's data |

Same kind of whole-sample gate (`>24` / `>36` observations) sits in the Bloomberg paths (panel.py 514/565,
signals.py 194/345, bloomberg.py 114): inactive on free data, would fail once Bloomberg inputs are in.
What the test cannot see: revised data vintages (OECD, BIS, MSCI), vendor backfill, publication lags, constants chosen
with hindsight.

## Bloomberg adapter (mocks only)
`tools/bbgq/lib/bbg_panel.py` serves gm.bloomberg's inputs from the locked data as of T. Bloomberg can feed: commodity
excess-return indexes (16 markets), commodity carry from curves, MSCI valuation ratios (15 equity markets), growth
surprises (off in both configs). Everything else stays on free data. Coverage job `gm_bbg_map_v1` runs after lock v2.

## Weekly implementation (not built; Batch A2)
Exists: daily returns for 62 markets (gm/daily.py), a k-day delay test (gm/timing.py). Missing: a weekly decision grid,
four staggered weekly tranches with their own turnover and costs, daily total returns (carry, dividends, rolls), an
as-of path from the Bloomberg daily tables.

## After the re-check (same day)
- Reader bbgdata-1.2.0: copied blocks get status `copy` (identical numbers under 5+ different tickers in one workbook);
  a `_CUT` twin never wins; a shorter re-pull does not replace a longer first pull; sheet names matched loosely;
  the truncation cut also covers Bloomberg inputs (new cause C4: `>24` / `>36`-month gates on Bloomberg series).
- Run on the PC on the first-pull files (`tools/bbgq/results/bbg_build_v2.txt`, `bbg_check_v2.txt`): exactly the 836
  copied blocks are flagged (file 1: 355 in ten sheets; file 3: 481 in eight sheets); nothing else. Provisional lock id
  22f52578... (replaces lock v1 f5a4fb7c... as the working build until lock v2). File 3 keeps only 51 usable blocks,
  file 1's ten sheets almost none: the Friday re-pull (R1-R7) covers all of them.
- PC truncation run (`gm_trunc_v1.txt`): same verdicts as the cloud at all eight cut dates (one displayed count on the
  "daily returns" line differs between pandas versions; no pass/fail changes). Reproduction re-run with the new
  reference: 24 of 24 PASS.
- Coverage map (`gm_bbg_map_v1.txt`), first-pull data: valuation ratios 23 of 23 and economics 35 of 35 served;
  commodity curves 28 of 95; commodity return indexes 0 of 31 (all copies) -> after the re-pull.
- Engine fixes C1-C4 = one new engine version to register before Batch A (not applied).

## 2026-11-12: fixes applied
C1-C4 were registered in gm/CHANGES.md and implemented as gm-1.2.1 / gm-2.0.1-candidate (commit 81fe176). The
truncation test now passes at all eight cut dates, in the cloud and on the PC
(`tools/bbgq/results/gm_trunc_v1_gm-1.2.1.txt`); reproduction of the new reference on the PC: 24 of 24
(`gm_repro_v1_gm-1.2.1.txt`). The Bloomberg-input cut has run on mock data only; it runs on real data after lock v2.
