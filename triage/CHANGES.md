# Triage rule changes

Rules, weights and thresholds live in `triage/rules.py`. They were written down on 2026-10-22, before any backtest
result was seen. Log every change here (date, what changed, why) before running with it. If a change was prompted
by a backtest result, say so: it then has to be judged on months after the change, not on the backtest that
suggested it.

| Date | Change | Why |
|---|---|---|
| 2026-10-22 | v1.0.0: first version (Hidden Earnings, Emerging Compounders, Core Compounders) | — |
| 2026-10-22 | Scans twice a month (last trading day on or before the 15th, and month-end) instead of month-end only. Same calendar definitions: 12-month high over the past year's scans, own past = 5 years of scans (2 years needed), 6-month cooldown, 12-month holding. Regressions compound the twice-monthly portfolios to calendar months | User asked for bi-weekly calls. Made before any real-data run |
