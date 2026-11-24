# Global Macro Book: rule changes and trial log

Every rule change gets a new VERSION in gm/run.py and a line here. Every variant tested on the design period
(1990-2010; extra check 1975-89) is logged so the deflated Sharpe can count the trials. The holdout (2011-2026) is run
once, after the rules are frozen, by gm/holdout.py.

## gm-1.2.3 and gm-2.0.3 candidate (registered 2026-11-24, BEFORE the code change): E1-E5
Fix version (may change design numbers). Registered in docs/research/global_macro/TESTING_PROTOCOL.md section 7.4 rows
E1-E5 and 7.3 item 5 (step 3.4, 2026-11-23); this is entry 1 of docs/research/registration/REGISTRATION_3.4.md part (c).
Each item is the registered text; none is chosen from results, and none is revisited after them.
1. E1 gm/config.py (flags), read by gm/signals.py and gm/panel.py: Bloomberg switches OFF by default, by registered
   config flags: Value's Bloomberg equity composite; Carry's farthest-contract commodity curve carry; the alternative
   commodity columns (until charter D1 admits a market through A3); Bloomberg growth surprise. Why: different measures
   on different markets, switched on by which tickers load (register D4-D6, D16); a Bloomberg-only input cannot run
   live (rule 7). With no Bloomberg file present (the cloud and free-data case) E1 alone changes no number; this is
   shown before the other items are coded.
2. E2 gm/bloomberg.py EQ_INDEX: remove the mappings eq_eu_stoxx50 -> "MXEM Index", eq_us_ndx -> MSCI USA, eq_us_r2k ->
   MSCI USA; every remaining mapping (a local index to the MSCI index of the same country) is used only if the A1 rule
   of 7.6 step 2 admits the series. Why: code defect (NOTES_3.1_agent_A item 3; CHECK_3.2_A s4 item 12). Inactive on
   free data.
3. E3 gm/signals.py: CPI as-of rule: a country whose OECD CPI series is quarterly enters a quarter's value at the end
   of the month after the quarter ends; oecd_sdmx raises an error instead of returning an empty table when the csv
   cannot be parsed; a metadata job lists, per country, monthly or quarterly and the first date (metadata only, design
   rows only). Why: look-ahead (SPEC_Economic_trend s3; CHECK_3.2_A s4 item 7: a parse error silently moves every
   country to FRED). Found while reading the code before this entry: the current parser reads a quarterly period
   "YYYY-Qn" as the FIRST month of the quarter (pandas), so a quarterly value would enter before its quarter ends.
4. E4 gm/signals.py, Value, the 7 non-US equity markets (Germany, UK, France, Japan, Canada, Australia, Hong Kong; Ken
   French country files): the trailing 12-month dividend yield used at month t is the one ending at t-12 (design and
   live alike); US (SPY) unchanged. Why: the live Ken French file can be up to 12 months stale (ffill limit 12) while
   the design run used month t (CHECK_3.2_A s4 item 5); using the bound means live is never staler than the backtest.
   Reported: the lag-0 form, kept as a flag (default = the registered lag-12 form).
5. E5 seal and holding cut (7.3 item 5): every holding period of every pod, tranche, rule and diagnostic ends at the
   close of 2010-12-31 at the latest. No price, settlement or statistic dated after 2010-12-31 is read, printed or used
   before the holdout. Under k = 1 the decision at month-end 2010-12 is never traded; the holding decided at month-end
   2010-11 ends at the 2010-12-31 close (the move to 2011-01-03 is not read). Why: sealed days were reachable through
   k = 1, tranches and forward windows (checks A item 9, C item 3; register D15). This entry covers the paths that exist
   now: the monthly k = 0 book (gm/book.py), the existing trade-delay diagnostic (gm/timing.py) and the engine runner
   (tools/bbgq/lib/gm_engine.py); the k = 1, tranche and daily paths are built in entry 2 with the cut built in. A guard
   and a test fail if any design output has a date after 2010-12 or uses an input dated later. The live run
   (gm/run.py) and the one-shot holdout run (gm/holdout.py) are not design runs and say so explicitly.
VERSION gm-1.2.3 in gm/run.py; config names gm-1.2.3 (BASE) and gm-2.0.3-candidate (CANDIDATE). No other rule, weight,
threshold or cost changes.
Gate: the truncation test passes at all 8 cut dates for BASE and CANDIDATE on free data; tests pass
(tests/run_tests.py, tests/bbgq_engine_smoke.py, tests/gm_bloomberg_smoke.py); the current reference (gm-1.2.2) is
reproduced 24/24 before the change. Reported once: design-period statistics before and after (net Sharpe, mean, vol,
worst drawdown; BASE and CANDIDATE; 1975-2010 and 1990-2010). Logged in gm/trials.csv as family "fix" (one row per
config, not a selection trial). New reference tools/bbgq/engine_ref.json (old one kept as engine_ref_gm-1.2.2.json).
Live paper ledgers: untouched (workflow disabled); the next live run restates under the new version name. Holdout not
run. The PC engine is redeployed when PC jobs that import pandas run again (7.4 precondition).

Result (2026-11-24, free data, design months only; inputs = the repo cache, the same 239 files as the gm-1.2.2
reference, which the cloud reproduced 24/24 before the change; code commit d68c0d6): truncation test PASS at all 8 cut dates
(1980-06 ... 2010-12), every stage (21 of 21), BASE and CANDIDATE, 0 differing market-months
(tools/bbgq/results/engine_trunc_cloud_2026-11-24_gm-1.2.3.txt). Which item moves numbers (engine fingerprint, 24
items, vs the gm-1.2.2 reference): E1 + E2 + E3 with E4 at lag 0, unsealed engine 24/24 identical (E1 alone changes no
number on free data, nor do E2 and E3); the same sealed (E5) 24/24 identical; gm-1.2.3 sealed vs unsealed 24/24
identical. Only E4 changes numbers: Value's signal for the 7 non-US equity markets and everything that follows from
it (other signals, volatility estimates and market months identical). So the reported lag-0 form of E4 has exactly
the gm-1.2.2 statistics (the "old" column). Net of costs, old -> new:
| Config | Period | Sharpe | Mean %/yr | Vol %/yr | Worst drawdown % |
|---|---|---|---|---|---|
| BASE gm-1.2.2 -> gm-1.2.3 | 1975-2010 | 1.222 -> 1.226 | 12.34 -> 12.46 | 10.10 -> 10.17 | -19.9 -> -21.0 |
| BASE gm-1.2.2 -> gm-1.2.3 | 1990-2010 | 1.452 -> 1.469 | 14.27 -> 14.47 | 9.83 -> 9.86 | -12.5 -> -12.3 |
| CANDIDATE gm-2.0.2 -> gm-2.0.3 | 1975-2010 | 1.456 -> 1.461 | 14.27 -> 14.38 | 9.81 -> 9.84 | -16.9 -> -16.8 |
| CANDIDATE gm-2.0.2 -> gm-2.0.3 | 1990-2010 | 1.608 -> 1.620 | 16.23 -> 16.38 | 10.09 -> 10.11 | -16.9 -> -16.8 |
E3 metadata (tools/bbgq/cpi_freq_meta.py -> tools/bbgq/results/cpi_freq_meta_2026-11-24.txt): the cached
oecd_cpi_yoy.csv holds monthly rows only (19 countries, 0 quarterly; macro/fetch_research.py requests frequency M), so
the quarterly as-of rule is built and tested on synthetic rows but INACTIVE on this file; it acts if quarterly rows ever
arrive. Australia has OECD rows only after 2010-12 and New Zealand none, and neither has a FRED fallback file, so
neither has CPI in design months (unchanged; a new CPI source would be a data entry). Every other country: OECD monthly
from 1990-01, FRED monthly before.
Closed here (details the registered text leaves open; simplest reading, not chosen from results):
1. E1: the four switches are module-level registered constants (gm/config.py BBG_SWITCHES), not keys of the BASE /
   CANDIDATE dicts, because the panel and the signals are shared by both configs. Growth surprise off = an empty series
   (the theme is unused anyway: ECON_THEMES has no growth and GROWTH_SOURCE stays 'off'). The Bloomberg excess-return
   indexes of the 16 panel commodities are not an E1 switch: they are the A1 data swap (7.6 A1, E15).
2. E3: a quarterly value sits on the quarter's last month and is carried two more months; with the callers' existing
   one-month publication lag (Economic trend lag 1, Value shift 1) it enters at the end of the month after the quarter
   ends and stays until the next quarter enters. Where a country has both, its monthly value wins month by month. A
   period that is neither YYYY-MM nor YYYY-Qn, or any read error, raises OECDParseError; a MISSING file still gives an
   empty table (the registered text names the parse error only). The metadata listing counts rows up to 2010-12 only
   and shows a first date only if it is in the design period; it also lists the FRED fallback's spacing.
3. E4: the lag-12 value at t is exactly the 12-month sum ending at t-12, with no carry-forward (the old 12-month
   carry-forward stays only in the lag-0 form), so a file that does not reach t-12 gives no value. Only Value changes:
   equity carry (not in the book) keeps the lag-0 form; the Bloomberg-composite path (switched off) ranks the same
   lagged yield. Flag: gm/config.py VALUE_DY_LAG (12); value_values(dy_lag=0) gives the reported form.
4. E5: a design run is every run except gm/run.py (live) and gm/holdout.py (the one-shot holdout), which pass
   seal=None; gm.book.run seals by default (inputs after 2010-12-31 are dropped, not masked; outputs end at 2010-12 and
   are checked by gm/seal.py check_output). Under k = 0 the decision at month-end 2010-12 is computed but earns
   nothing, and its trading cost (charged in 2011-01) is not charged. The engine runner (gm_engine 1.1.0) cuts every
   loader at 2010-12-31 in a design run and stops if an input dated later reached the engine; the truncation test's
   full run is therefore sealed and its 2010-12-31 cut passes by construction (the unsealed comparison above, 24/24,
   stands in for that cut's old meaning). gm/timing.py (delay diagnostic, an existing path): days after 2010-12-31 are
   dropped and a delayed holding ends at the 2010-12-31 close at the latest; this changes only that diagnostic's
   2010-12 month for delays k > 0 (it used to read k days of January 2011).
5. gm/trials.csv rows: from the sealed engine books with gm.stats.summary, as for the gm-1.2.2 rows.
Tests: tests/run_tests.py ALL TESTS PASSED (incl. the new tests/gm_seal_smoke.py);
tests/gm_bloomberg_smoke.py PASSED; tests/bbgq_engine_smoke.py OK (packaged engine reproduces the new reference
24/24, truncation at 1995-12 PASS, curve carry only with its switch on). Logged in gm/trials.csv as family "fix" (two rows). Reference: tools/bbgq/engine_ref.json (old
one kept as engine_ref_gm-1.2.2.json). Not built here (registered for entry 2): the k = 1, tranche and daily paths and
their cut. PC engine not redeployed (pandas blocked on the PC).

## gm-1.2.2 and gm-2.0.2 candidate (registered 2026-11-22, BEFORE the code change): doubled US 2-year market removed
Found by code reading in the systematic charter (docs/research/fable/CHARTER_1.2.md section 9 item 2; confirmed by its
independent Opus check): `st_us_2y` and `bd_us_2y` are the same series (the 2-year par note priced from DGS2, less the
same US 3-month rate) wherever DGS2 exists, in monthly returns, daily volatility and every signal; `bd_us_2y` also
carries any stooq months before DGS2. So the book has 61 distinct markets, not 62, and the US 2-year note holds 2/15 of
the fixed-income block instead of 1/14 and can reach twice the per-market cap. The charter fixed the remedy before any
number: drop `st_us_2y` (the subset), keep `bd_us_2y`; registered as a design change before the run.
1. D1 gm/panel.py: "st_us_2y" leaves SHORT (the other short-end notes stay).
2. D1 gm/signals.py: "st_us_2y" leaves BD.
3. gm/variants.py, archived batch-1 variant S1 (US 3-month rate market): its signs are taken from `bd_us_2y` (the same
   series), so S1 is unchanged wherever it can be rebuilt.
No other rule, weight, threshold or cost changes. Which id goes is set by the data (the superset stays), not by results,
and is not revisited after them. Batch A1 (data swap) therefore stays a pure data swap.
Gate: the truncation test passes at all 8 cut dates for BASE and CANDIDATE on free data; tests pass; the PC engine is
redeployed and reproduces the new reference. Reported once: design-period statistics before and after (1975-2010,
1990-2010), as for C1-C4. Logged in gm/trials.csv as family "fix" (one row per config, not a selection trial). Live
paper ledger: untouched (workflow disabled); the next live run restates under the new version name. Holdout not run.
Texts that still say 62 markets (TESTING_PROTOCOL.md) are corrected at registration step 3.4.

Result (2026-11-22, free data, design months only; inputs = the PC's gm_free_inputs.zip, the same 239 files as the
gm-1.2.1 reference, which the cloud first reproduced 24/24 before the change): truncation test PASS at all 8 cut dates
(1980-06 ... 2010-12), every stage, BASE and CANDIDATE (tools/bbgq/results/engine_trunc_cloud_2026-11-22_gm-1.2.2.txt).
Net of costs, old -> new:
| Config | Period | Sharpe | Mean %/yr | Vol %/yr | Worst drawdown % |
|---|---|---|---|---|---|
| BASE gm-1.2.1 -> gm-1.2.2 | 1975-2010 | 1.236 -> 1.222 | 12.49 -> 12.34 | 10.11 -> 10.10 | -20.5 -> -19.9 |
| BASE gm-1.2.1 -> gm-1.2.2 | 1990-2010 | 1.474 -> 1.452 | 14.41 -> 14.27 | 9.77 -> 9.83 | -12.3 -> -12.5 |
| CANDIDATE gm-2.0.1 -> gm-2.0.2 | 1975-2010 | 1.464 -> 1.456 | 14.33 -> 14.27 | 9.78 -> 9.81 | -16.8 -> -16.9 |
| CANDIDATE gm-2.0.1 -> gm-2.0.2 | 1990-2010 | 1.629 -> 1.608 | 16.34 -> 16.23 | 10.03 -> 10.09 | -16.8 -> -16.9 |
Logged in gm/trials.csv as family "fix" (two rows). Reference: tools/bbgq/engine_ref.json (old one kept as
engine_ref_gm-1.2.1.json).

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

## 2026-11-02: statistical audit (gm/audit.py -> docs/research/global_macro/stats_audit_2026-11-02.md)
- Bootstrap: gm-2.0 1975-2010 SR 1.46, 90% interval 1.17-1.79, stable for mean blocks 3-24 months; batch-0 p-values
  stable across block lengths.
- Selection inflation among 32 logged variants (sd 0.11): about 0.23 Sharpe (0.28-0.31 if 100-300 variants).
  Deflated Sharpe is 1.000 at every trial count, so it is uninformative here and is no longer cited as evidence.
- CSCV over 20 rebuildable variants: PBO 0.04 (in-sample winner 1.50 -> 1.45 out of sample).
- Holdout power (block bootstrap, 189 months): pass-all probability 0.04 if true SR 0, 0.22 at 0.3, 0.41 at 0.5,
  0.66 at 0.8; the -25% max-fall criterion is the binding one (61% at SR 0.5).
- EM currencies and equities removed before 2000: 1990-2010 SR 1.63 -> 1.51; 1975-2010 1.46 -> 1.43.
- Trial log fix: batch rows had the pooled 1975-2010 SR in the 1990-2010 column and signal-only challengers
  shared the incumbent's hash; corrected (era columns recomputed, fingerprint includes the challenger name).
