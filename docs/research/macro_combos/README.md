# Macro Compass: combination tests (2026-10-28, research only, live rule unchanged)

Grid: 5,637 distinct rules = warning signal (none / weighted / equal-weight) x confirmation of the cut (none, S&P trend,
half-then-full, unemployment, trend or unemployment, Fed tightening, narrowing market) x extra cut (none, growth-trend,
trend, hot inflation + Fed) x re-entry (immediate, 3-month hold, bear-rally guard, 25-pt ramp) x floor (50/25/0%)
x defensive asset (T-bills, Treasuries if stock-bond corr < 0, Treasuries always) x sector momentum (none, when fully
invested, always). Fit half 1975-2000, check half 2001-2026, untouched 1966-1974. Run: `python3 build_data.py`, then
`combos.py`, `robust.py`, `early.py` (needs the cached raw data in cache/macro).

## Leading rule ("Fed-gated")
1. Macro warnings (live weighted share, same 15%->35% band) cut stocks only while the Fed is tightening: funds rate
   >= 1 pt above its 24-month low (on 36% of months).
2. Whatever the Fed does: S&P 500 below its 10-month average AND unemployment above its 12-month average -> cut.
3. Floor 0% stocks; non-stock share in 7-10y Treasuries while the 12-month stock-bond correlation < 0, else T-bills;
   12-1 sector momentum tilt (top/bottom 5, 1.5x/0.5x) only while 100% invested.

| | 1975-2000 | 2001-2026 | 1975-2026 | 1966-1974 (untouched) |
|---|---|---|---|---|
| S&P 500 | 15.9% / -30% / 0.62 | 9.0% / -51% / 0.53 | 12.4% / -51% / 0.58 | -0.6% / -47% |
| Live rule 3.2 | 14.5% / -21% / 0.61 | 8.4% / -29% / 0.63 | 11.4% / -29% / 0.62 | 1.5% / -34% |
| Fed-gated | 17.4% / -15% / 0.76 | 11.8% / -19% / 0.89 | 14.6% / -19% / 0.81 | 8.0% / -15% |
| Fed-gated, T-bills, no tilt | 16.1% / -15% / 0.72 | 10.2% / -20% / 0.77 | 13.1% / -20% / 0.74 | 7.8% / -16% |

Cells: CAGR / worst fall / Sharpe. 2.6 exposure changes a year, average 81% stocks, 0% stocks in 15% of months.
IEF instead of the synthetic bond since 2002: same result (12.3%/yr, Sharpe 0.91 vs 0.92).

## Checks
- Plateau: Fed-gate lookback 12-36 months x rise 0.25-1.0 pt all give Sharpe 0.62-0.79 (fit) / 0.86-0.94 (check);
  breaks at >= 1.5 pt (1987 missed). Alternatives (funds rate above 12 months ago, 12m change >= 1 pt) work as well.
- Placebo: the Fed gate replaced by 1,000 random schedules with the same on/off runs: real beats 96.6% (p 0.034).
- Single-test bootstrap vs the live rule: Sharpe gain <= 0 in 1.6% of draws. After searching all 5,637 rules (White
  reality check): p 0.25; CSCV probability of overfitting 0.39. => the family is real, the exact best setting is not
  proven; expect about half the backtest gain live.
- Weak spots: 2020-2026 (9.4%/yr vs S&P 15.1%: whipsaw exits Apr-May 2020, Jul 2022-Jan 2023, Apr-May 2025,
  Apr 2026 each cost 5-10 pts); sudden crashes (1987 -10%, 2020 -18%) need a daily signal.
- Average effect of each layer, all else equal (Sharpe pts, fit / check half): Treasuries if corr < 0 +0.03 / +0.10;
  Treasuries always +0.07 / +0.08 (but -22% in 2022); momentum when fully invested +0.03 / +0.04; trend
  half-then-full confirmation +0.03 / +0.00; equal-weight indicators -0.03 / -0.02; re-entry rules ~0 or negative;
  narrowing-market gate and unemployment gate negative.

## Reading 2026-10
Fed gate off (funds 3.75%, 24m low 3.63%), S&P above trend, unemployment 4.2% vs 4.30% average -> 100% stocks
(live rule 68%).

## Non-stock share (assets.py, 2026-10-29)
Same 4.0.0 stock exposure; CAGR / worst / Sharpe 1975-2000 | 2001-2026 | 1966-74: bills 16.1/-15/0.72 | 10.2/-20/0.77 |
7.8; 10y if corr<0 16.5/-15/0.73 | 11.4/-20/0.84 | 7.7; by cause (growth cut -> long if corr<0, else bills, ADOPTED
4.1.0) 16.9/-15/0.74 | 11.6/-20/0.83 | 7.8; gold instead of bills when hot 16.2/-18/0.70 | 11.5/-27/0.83 | 15.2;
gold whenever bonds don't hedge 13.7/-27/0.51 | 13.0/-27/0.91 | 15.8; defensive sectors 18.6/-26/0.81 | 8.6/-36/0.56;
walk-forward pick 15.2/-17/0.64 | 10.1/-27/0.72. Gold before 2000 = monthly average price (smoothed, autocorr 0.17).

## Dollar / currencies (dollar.py, dollar2.py, 2026-10-29)
Holding (instead of bills): dollar (UUP; synthetic DXY carry before 2007), yen, franc, half long-T/half dollar: none
beats the live 4.1 mix (14.2%/yr; alternatives 13.6-14.1%). Signal: warnings also acted on when the dollar-oil-rates
squeeze score >= 80 (not only when the Fed tightens): 14.7%/yr, worst -19%, Sharpe 0.83 (live 0.78); 1975-2000 equal,
2001-2026 12.6% vs 11.6%; plateau 70-85; shuffled-timing placebo 0/500 better; gain mostly 2021-10..2022-05 (+12.5 pts),
1999-2000 cost -4.7 pts. Not adopted (pending user decision): it would cut stocks most months of mid-2026.
