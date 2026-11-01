# Global Macro Book: rule changes and trial log

Every rule change gets a new VERSION in gm/run.py and a line here. Every variant tested on the design period
(1990-2010; extra check 1975-89) is logged so the deflated Sharpe can count the trials. The holdout (2011-2026) is run
once, after the rules are frozen, by gm/holdout.py.

## gm-2.0 candidate (2026-11-01, NOT frozen: waits for the Bloomberg data)
Framework rebuilt to be config-driven and statistics-driven: gm/config.py (every rule), gm/vol.py, gm/daily.py,
gm/timing.py, gm/stats.py (decade table, bootstrap, deflated Sharpe, marginal alpha), gm/trials.py (every trial
logged to gm/trials.csv with its config hash), gm/bloomberg.py (adapter; synthetic smoke test passes).
Decision rule fixed before the tests: adopt a component only if it raises net Sharpe in BOTH 1990-2010 and 1975-89.
| Trial (logged) | SR 1990-2010 | SR 1975-89 | Verdict |
|---|---|---|---|
| gm-1.2 base | 1.48 | 0.93 | reference |
| continuous vol-normalised trend | 1.43 | 0.76 | rejected |
| hybrid volatility (daily EWMA 35d + 10y, floor) | 1.58 | 1.06 | ADOPTED |
| cluster weights within class | 1.48 | 0.94 | rejected (no gain, deeper drawdown) |
| trend on spot moves only | 1.39 | 0.92 | rejected (carry inside trend helps) |
| scenario limit 3% | 1.32 | 0.93 | rejected as a rule; diagnostic |
| family shares 45/25/15/15 (trend/carry/value/econ) | 1.56 | 1.09 | ADOPTED |
| hybrid + shares = candidate | 1.63 | 1.22 | candidate |
| candidate with slow trend 6/12 / 12 | 1.43 / 1.40 | 1.03 / 1.10 | rejected |
| candidate + scenario limit 5% / 3% | 1.56 / 1.41 | 1.22 / 1.20 | rejected (drawdown/vol 1.55 vs 1.68 only) |
| risk theme credit-only (removes trend overlap) | 1.57 | 1.20 | rejected |
Trade timing (daily, price moves only, 1990-2010): 1/3/12 trend Sharpe 0.95 at k=0, 0.85 at 1 day late, 0.64 at 5,
0.61 at 10; slow 6/12 0.57 / 0.52 / 0.42 / 0.42. The fast blend beats the slow one at every delay. Rule: trade on the
first trading day after month end.
Candidate statistics 1990-2010: net SR 1.63, bootstrap 90% interval 1.26-2.02, deflated-Sharpe probability ~1.00
with 32 logged book trials (expected best of unskilled trials 0.21); every family adds (marginal alpha t: carry 4.9,
trend 3.3, value 3.1, econ 2.8); family correlations -0.16 to 0.26.
WRDS (statistics only): our yield-built US bond returns vs CRSP Treasury indexes: corr 0.985 (2y), 0.989 (5y),
0.965 (10y), 0.990 (30y); tracking error 0.6-2.1%/yr. Daily-vol study on 20 MSCI country indexes 1990-2010: daily
EWMA R2 0.46 vs 0.07 for the 36-month estimate (QLIKE 0.29 vs 0.60); blend keeps vol-scaled returns at 1.05 x target.
Holdout pass criteria changed BEFORE any holdout run (user decision 2026-11-01): net SR >= 0.3, worst fall > -25%,
corr S&P <= 0.3, 2022 positive.

## gm-1.2.0 (2026-10-31): independent look-ahead audit fixes
Audit by a separate agent (truncation test: rebuilding with data cut at 1998-06, 2003-11, 2008-09, 2010-12 gives
identical signals and positions up to each cut, apart from item 1). Verdict: no material look-ahead. Fixes:
1. Pre-ETF dividend proxy estimated on design data only (overlap up to 2010-12), not the full sample.
2. Excess returns subtract the 3m rate known at the start of the month (rate3m.shift(1)), for equities, bonds,
   notes and FX.
3. Monetary theme lags the OECD 3m-rate fallback by one month.
4. The |r| >= 60% filter was outcome-based; replaced by an explicit BAD_POINTS list plus a warning. The only large
   moves left are real (RBOB 2020-03, WTI roll 2020-05). The KRW spikes 2015-17 came from Yahoo, so FX now uses Fed
   H.10 daily first.
5. Yahoo files in cache/macro/raw are now read too, so the US equity uses SPY (1993+) and the US dividend yield exists.
6. book.main reports positions at the last complete month.
Known and documented (not fixed): hand-picked surviving universe; EM FX limited to MXN/BRL/KRW/ZAR (no TRY, RUB, THB,
IDR, ARS), which flatters carry; families dropped after design-period results; latest-vintage CPI and BIS data.
Design 1990-2010 net SR 1.47 (2x costs 1.36), maxDD -12%; 1975-89 net SR 0.93.

## gm-1.1.0 (2026-10-31)
- Econ trend: growth theme (OECD CLI, latest vintage, heavily revised) left out until first-release vintages exist.
  Themes now inflation (CPI, rarely revised), trade (BIS FX), monetary (yields), risk appetite (markets, credit spread).
  Design net effect: econ family SR 0.71 -> 0.60.
- Equity value: dividend yield (Ken French country market with minus without dividends, 1975+; US from SPY minus
  S&P 500 price, 1993+) replaces the 5-year reversal (which failed: -0.46). Design SR 0.28, corr with AQR equity-index
  value 0.51. Emerging-market equities have no value signal yet.
- Equity carry (dividend yield minus 3m rate, half directional / half cross-sectional): design SR 0.02; left out.
- Book design 1990-2010: net SR 1.55, maxDD -13%; 1975-89 net SR 0.95.

## gm-1.0.0 (2026-10-30)
- First combined book. Families: trend 30, econ 30, carry 20, value 15 (FX PPP + bond real yield), xs-momentum 5.
- Design 1990-2010 net SR 1.50; 1975-89 0.96.

## Trial log (design-period variants, all seen)
1. Price trend 1/3/12 blend and 12-month only (plumbing vs AQR).
2. Econ: five themes (v1); four themes without growth (v1.1); each theme alone (diagnostic, 5 runs).
3. Carry: half/half (chosen), directional only, cross-sectional only; equity carry half/half.
4. Value: 5-year reversal + real yield + PPP (v1); equity dividend yield (v1.1).
5. Cross-sectional momentum 12-1; value + momentum 50/50 pairing.
6. Risk scaler: credit-spread jump, cross-asset correlation jump, drawdown brake (none adopted).
7. IMF WEO forecast revisions: cross-sectional and directional, equities and bonds (exploratory, not adopted).
8. Family ablations of the book (diagnostic, 5 runs).
9. Trend lookbacks (2026-10-31, after reading Solovis "Momentum vs trend following": 6/12 months explain CTA returns
   best): 1/3/12 (kept), 3/6/12, 6/12, 12. Design 1990-2010 book net SR 1.48 / 1.35 / 1.28 / 1.27. With positions
   applied one month late, gross SR is 1.10-1.16 for every variant: the extra Sharpe of 1/3/12 is the fast part,
   which needs trading within days of month end. Rule unchanged; noted as an execution dependency.
10. Point-in-time growth theme (2026-10-31): industrial-production growth change and unemployment change as first
    published (Dallas Fed vintages 1962-98, OECD revisions editions 1999+; plus CLI editions from 2001). Design
    1990-2010, growth theme alone: PIT 0.29 vs revised CLI 0.42 (commodities 0.05 vs 0.68: the revised CLI's commodity
    result was mostly hindsight). Econ with PIT growth 0.64 vs 0.59 without; 1975-89 0.24 vs 0.37. Book net SR
    1990-2010 1.47 either way; 1975-89 0.84 vs 0.93. Not adopted (GROWTH_PIT stays False).
Total: about 37 variants before the trial log; 32 book-level trials in gm/trials.csv since (2026-11-01).

## 2026-11-01: statistical adoption protocol (docs/research/global_macro/TESTING_PROTOCOL.md)
Replaces "raise net Sharpe in both eras" with a pre-registered test: paired stationary bootstrap of the Sharpe
difference (Holm across each batch, p < 0.05), dSR >= 0.05, non-inferiority per era (95% lower bound > -0.10;
eras without new data identical), dSR > 0 at 2x costs, tail checks. Code gm/protocol.py, gm/variants.py, gm/stats.py.
- Batch 0 (re-test of gm-2.0 adoptions): hybrid vol dSR +0.12 (Holm p 0.004) PASS; family shares 45/25/15/15
  dSR +0.11 (p 0.037) PASS. gm-2.0 candidate unchanged.
- Batch 1 (free data): all rejected. Econ theme x class blocks -0.01; US 3m short-rate market -0.02; bond value
  composite +0.00; FX value skip 12m +0.01 (p 0.17); bond carry per duration +0.00.
- Diagnostics (protocol_diagnostics.md): trend family SR 1.22 vs AQR TSMOM 1.34 (corr 0.66) on 1990-2010, so the
  trend leg is not inflated; book Lo-adjusted SR 1.49 / 1.32; no single market or 2008 drives the result
  (1.35-1.48 with any top market removed; 1.44 without 2008). 1987 loss came from trend long equities (-6.4%) and
  short bonds (-2.1%).
