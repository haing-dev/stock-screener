# Independent review of eq_recall 1.0.0 (2026-11-27, Opus, read only)

Verdict: pull() safe; run() safe, no blocker. No look-ahead, no forward return, no recipe criterion wrong, no
arithmetic error against RECALL_SPEC_v1 found; code hash matched the registration; smoke test passed.
Findings: 1 should-fix (Treasury gaps silently fail P1 at a quarter-end -> fixed in 1.0.1: stop); notes: 2 single
R2 version not flagged (fixed); 3 revision measure's last split factor taken from the truncated price file (fixed);
4 AAPL factor printed (fixed: direction only); 5 universe-rejection column must be stripped from the writer's
feedback by hand, masked ids as strong as the name hash; 6 no rollback after a failed SQL in a pull step (worst case a
pull rerun); 7 full-form bootstrap may rest on few draws (count printed); 8 per-criterion shares use the decisive
missing-data rules (as specified).
Checked correct: availability lags (rdq + 1 day / +45 days, 270-day staleness; fiscal year +90 days, 550-day
staleness; GICS by validity dates; Treasury on or before t; IBES within 35 days); monthly data cut at 2025-09;
B1-B6, P1-P3, A1-A5 and every GICS code as RECIPE_v1; median over the eligible set before exclusions; 108 full-form
versions; cells, lift, bootstrap and gate as specified; gvkey normalised.
