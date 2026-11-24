# Global Macro Book: rule changes and trial log

Every rule change gets a new VERSION in gm/run.py and a line here. Every variant tested on the design period
(1990-2010; extra check 1975-89) is logged so the deflated Sharpe can count the trials. The holdout (2011-2026) is run
once, after the rules are frozen, by gm/holdout.py.

## gm-2.1.0 feature version (registered 2026-11-24, BEFORE the code): E6-E11, E14
Feature version (no change to BASE or CANDIDATE at k = 0). Registered in docs/research/global_macro/TESTING_PROTOCOL.md
section 7.4 rows E6-E11 and E14 with 7.3 items 1-3, 5, 6 and 7.7 (step 3.4, 2026-11-23); this is entry 2 of
docs/research/registration/REGISTRATION_3.4.md part (c). The fix version gm-1.2.3 (E1-E5, entry 1) is done (afca6b2,
d68c0d6, c27d9d2). Each item below is the registered text (quoted where possible); none is chosen from results, and none
is revisited after them. Not in this version: E12, E13, E15, the LSEG source, the pod builds (Curve carry, Strip
reversion, the card rule-layer engine of part (c) item 6), and every diagnostic run (7.5).
1. E6 "k = 1 return form of 7.3 item 2 with flags" (7.3 item 1: decisive timing is k = 1). 7.3 item 1: "a position
   decided at the close of month-end t is traded at the close of the first trading day after t and held to the close of
   the first trading day after month-end t+1. Reported beside it: k = 0 (the engine's same-close form, book.py run,
   timing.py k = 0) and the one-period (one-month) delay of WORKFLOW s5." 7.3 item 2: "k = 1 return of market m for the
   holding decided at t: the panel's monthly excess return of month t+1, plus the price return of m on the first trading
   day of month t+2, minus the price return of m on the first trading day of month t+1 (carry and dividends accrue
   monthly, as timing.py assumes). It applies where a daily price of m exists on both days. Where it does not, the k = 0
   monthly return is used and the market-month is flagged; the result sheet reports, by year, the share of gross position
   flagged. Costs are charged as today."
2. E7 "Version-grid machinery: each version computed as a complete pod, pod position = equal-weight mean of version
   positions at the unscaled stage, a missing version counted as 0 (SPEC_Trend s3 step 6); Trend 16, Economic trend sign
   shape, Carry versions 1/2 as separate signals, Value version 2". Grids as the approved specs fix them (section 6 of
   each): Trend v1-v4 lookback 1/3/6/12 months, sign, hybrid volatility; v5-v8 the same with m36; v9-v12 graded (cap 2),
   hybrid; v13-v16 graded, m36 (SPEC_Trend s3 steps 1-6). Economic trend v1 f(z) = tanh(z / 2) (today), v2 f(z) =
   sign(z) (SPEC_Economic_trend s3 step 8). Carry v1 directional w = sign(carry), v2 cross-asset w = rank in class
   (SPEC_Carry s3; "this reproduces today's half-and-half exactly"). Value v1 as coded; v2 bonds yield(t) - yield(t-60
   month-ends), currencies minus the deviation of q(t) = ln USD value(t) + cumulative (local CPI yoy - US CPI yoy) / 100
   / 12 from its expanding mean (at least 60 months of q), equities as v1 (SPEC_Value s3). Each version: position = w x
   0.40 / vol, divided by the count of markets in the class with a position that month; Trend versions use their own
   volatility (vol_v), every other pod the CANDIDATE hybrid estimate. 7.6 step 3 defines the A2 challenger ("CANDIDATE
   with Trend 16 versions, Economic trend 2, Carry 2, Value 2"): its config is written here; it is not run.
3. E8 "Weekly tranche engine of 7.3 item 6" (registration part (c): "NYSE calendar, offsets 0/5/10/15, k = 1 trades,
   cut"). 7.3 item 6: "tranche j = 0, 1, 2, 3 decides on trading day 5 x j after the month's last trading day. Trading
   days = days the New York Stock Exchange is open; a market without a price that day uses its last price ... Each
   tranche holds a quarter of the pod from the close of the trading day after its decision day (k = 1) to the same point
   after its next decision day. Decisions dated after 2010-12-31 do not exist (tranches 1-3 of month-end 2010-12 decide
   in January 2011); holdings of tranches 1-3 decided in December 2010 end at the 2010-12-31 close. Monthly design runs
   use tranche 0 only. The tranche form runs only in the weekly-implementation check (1990-2010, reported). In it, a
   market without daily data holds its tranche-0 position all month and is flagged ... coverage is reported." Card 4
   R1-R4 and Curve carry have no tranches (registered exceptions).
4. E9 "Component masks (pod x class x version) so that the Core book holds only Core parts and the shadow book the
   rest; Core book at equal risk: each Core part's summed scaled-block return is rescaled to unit volatility (trailing
   36-month realised volatility, lagged one month, as the block scaler) and weighted 1/n before the book scaler (book.py
   family weights alone give a 4-block part up to about twice the risk of a 1-block part)". Core parts (7.2 item 5, 7.6
   step 6): Trend (all classes and versions); Carry currencies version 2 plus energy versions 1 and 2; Value equities
   (both versions). Shadow: Economic trend; Carry currencies version 1 and bonds (both versions); Value bonds and
   currencies (both versions). "Core book v1 = the Core parts at equal risk as defined in 7.4 E9, 10% target, the
   engine's caps."
5. E10 "Test code: alpha bootstrap (7.7 T1) in gm/stats.py; placebo engine (7.7 T3) for monthly signals, rule states
   and date rules; non-inferiority decision for hygiene (7.7 H1-H4)". T1: "Intercept of the least-squares regression of
   the pod's monthly net return on the Core book's monthly net return over the window. One-sided p for H0 alpha <= 0
   from the centred stationary bootstrap: whole months, mean block 6, 10,000 resamples, seed 20261101, the regression
   re-fitted in every resample; p = share of resamples with (alpha_b - alpha_hat) >= alpha_hat"; Holm-adjusted p < 0.025
   over the Core-eligible systematic pods. T2: alpha of T1 with every cost doubled > 0. T3: "1,000 placebos, seed
   20261101. Monthly pods and state rules: the score array (before division by volatility) of all markets moved jointly
   in 12-month blocks in random order (blocks aligned to the window's first month, the last part-block kept), then
   re-sized with each month's own volatility, scalers and caps, same costs. Card 4 R1-R4: each window moved to a random
   start in the same calendar year (R1, R3) or month (R2, R4), same length in trading days, gates re-read at the new
   dates"; pass: "share of placebos with net Sharpe >= the pod's < 0.05". T4: test 5 on the combined book (Core book +
   pod at lambda 0.5, rescaled to 10% by its trailing 36-month realised volatility, lagged one month) against the Core
   book alone. H1 "one-sided 95% lower bound of dSR (paired stationary bootstrap of section 2, pooled design window) >
   -0.10; H2 dSR at twice the costs, reported; H3 tail test 5 between the two books; H4 (A3 only) the item's own target,
   point estimate ... Pass = H1, H3 and, in A3, H4."
6. E11 "Spread pods: joint caps (a currency's whole Strip contract vector multiplied by the smallest ratio cap_j /
   abs(x_j); Curve carry's two legs share one cap from the front leg's hybrid volatility); per-instrument gross weight
   (3-month contracts at 0.25/1.9 of notional)". Why (7.4): "book.py clips each column alone, which breaks level
   neutrality (SPEC_Strip_reversion s5; SPEC_Curve_carry s5; CHECK_3.2_B s4)". Machinery only: no spread pod is built.
7. E14 "Daily S&P excess return for card 4 (spec s3: ^GSPC daily price return + the panel's monthly carry part spread
   over trading days)". SPEC_Card4 s3: "e(d) = ^GSPC price return of day d + c(m) / N(m), where c(m) = panel eq_us_spx
   monthly excess return minus the ^GSPC monthly price return ... and N(m) = trading days in m. So a rule held all month
   earns exactly the panel's monthly excess return."
8. E5 in every new path (part (c) item 2: "E5's seal and holding cut are built into each new path in this entry"):
   7.3 item 5, every holding of the k = 1, tranche and daily paths ends at the close of 2010-12-31 at the latest; no
   price or statistic dated after 2010-12-31 is read; "under k = 1 the decision at month-end 2010-12 is never traded; the
   holding decided at month-end 2010-11 ends at the 2010-12-31 close (the move to 2011-01-03 is not read)"; card 4
   windows that would run into 2011 end at the last trading day of 2010. Each new path's output passes gm/seal.py
   check_output.
Version names: the engine version is gm-2.1.0 (gm/config.py ENGINE_VERSION). BASE stays gm-1.2.3 and CANDIDATE
gm-2.0.3-candidate (nothing changes at k = 0; gm/run.py VERSION stays the BASE name gm-1.2.3). The A2 challenger config
is named gm-2.1.0-a2-challenger. No rule, weight, threshold or cost of BASE or CANDIDATE changes.
Gate (7.4 "Gate for E6-E14", part (c) item 2): BASE and CANDIDATE at k = 0 reproduce the gm-1.2.3 reference
(tools/bbgq/engine_ref.json) exactly, 24 of 24 items, difference 0; the truncation test passes at all 8 cut dates,
including the k = 1, tranche and daily paths (and the grid, Core and shadow positions) cut at each date; tests pass
(tests/run_tests.py with a new synthetic-data test of every item). NO PERFORMANCE STATISTIC OF ANY NEW PATH IS COMPUTED
IN THIS VERSION: no return, Sharpe, drawdown, hit rate, alpha, p-value or placebo result of any k = 1 form, version,
grid, tranche, Core or shadow book or pod, on real data, in any period. On real data only the k = 0 reproduction and
the truncation test (positions, signals and value differences across cut dates) are run. Every test of the new
statistics runs on synthetic data with known answers. No gm/trials.csv row (nothing is a trial). The live paper ledger
and the holdout are untouched.
Closed here, before the code (details the registered text leaves open; simplest reading consistent with the specs):
1. NYSE calendar (E6, E8, E14): the NYSE open days are the dates of the daily ^GSPC closes in the free daily file
   (gm/daily.py EQ_DAILY, from 1970-01-02), the engine's only record of NYSE days; it includes the special closures
   (e.g. 2001-09-11 to 09-14). "Month-end" = the month's last NYSE day; "first trading day" = its first NYSE day.
2. E6 price return of m on a day = gm/daily.py build()'s daily return of m on that day turned into a price return
   (bonds and notes: -duration x yield change, already a price return; every other market: exp(log return) - 1); a day
   without a value (no price, or removed by daily.py's 25% filter) has no price, so the market-month is flagged and
   earns the k = 0 return. Positions, signals, scalers, caps and costs are the same under k = 0 and k = 1: only the
   return a holding earns changes (the block and book scalers keep reading the k = 0 returns, which are known at the
   decision close; the k = 1 return of the last holding is not). Cost timing as today (the same cost series, same
   lag). Holding cut: where the first trading day of t+2 lies after the seal (or after the last day of a truncated run),
   the holding ends at the close of month-end t+1: return = R(t+1) - price return of the first trading day of t+1, not
   flagged. Months whose first trading day is missing from the calendar (before 1970) are flagged.
3. E7 configs: a config key "grid" ({pod: versions}); absent = today's single form, so BASE and CANDIDATE are unchanged.
   A missing version adds 0; a market-month where no version has a position holds no position (missing, as today), so
   block starts are unchanged. Each version counts its own markets with a position (n_v). The alternative-commodity
   30% cap (inactive while E1 is off) applies to the averaged pod. Trend vol_v: "hybrid" = CANDIDATE's vol parameters,
   "m36" = vol.py m36; the per-market cap uses the config's engine volatility (SPEC_Trend s5: CANDIDATE hybrid). Economic
   trend sign shape: f is applied where tanh(z / 2) is applied today (FX: to local minus US theme; commodities: to the
   four-country mean); both shapes come from one pass over the themes. Value v2 currencies: CPI as v1 (carried at most
   18 months, lagged 1 month); the cumulative inflation gap starts at the first month both CPIs exist and a month
   without a gap adds nothing; q is missing where the USD value is missing; the expanding mean is over all q values up
   to and including t. Carry: v1 = sign of carry through the "dir" form, v2 = cs_rank; whenever components or a grid are
   used, Carry is computed as these two versions (equal to the half-and-half form; checked on synthetic data, and on
   real positions in the result commit).
4. E8: decision day d_j(t) = the (5j)-th NYSE day after month-end t (j = 0: month-end t); the holding runs from the
   close of the NYSE day after d_j(t) to the same point after d_j(t+1). Tranche j's decision panel X_j(t) = R(t) - pr(m,
   month-end t-1 -> d_j(t-1)) + pr(m, month-end t -> d_j(t)) and its earned return Y_j(t+1) = R(t+1) - pr(month-end t ->
   d_j(t)+1 day) + pr(month-end t+1 -> d_j(t+1)+1 day), where pr(a -> b) = the ratio of m's last daily price at or before
   b to its last daily price at or before a, minus 1 ("uses its last price"); carry accrues monthly, as for k = 1.
   Tranche 0 is exactly the E6 monthly k = 1 path (its flags included), so the monthly design run is tranche 0. Price
   trend, cross-sectional momentum and every volatility estimate of tranche j read X_j and the daily EWMA at d_j(t)
   (the last daily value at or before it); Economic trend, Carry and Value use their month-end t values (all published
   by d_j(t)). A market has daily data for label t if its first daily price is at or before month-end t-1 (decided by
   the past only, so the rule is truncation-safe); a market without daily data uses R(t) in X_j, earns tranche 0's k = 1
   return and holds tranche 0's final position (overwritten after the caps), flagged. Each tranche is a full book run
   with its own costs; the tranche form's return = one quarter of the sum of the four tranche returns (a tranche without
   a return that month adds 0). Decision days after the seal do not exist (no position); holding ends are capped at the
   seal close.
5. E9: a component = (pod, class, version), versions numbered as the grids (a config without a grid has one version per
   pod, except Carry, always split into v1 and v2 for masks). Component position = its term p_v / V in the pod average,
   so the Core and shadow components partition the pod. Masked block = the sum of a class's masked components, scaled
   by the block scaler (36 months, at least 24, lagged, multiplier capped at 50). Part return = the sum over its blocks
   of the scaled block position's return r_b(t) x k_b(t-1) (book.py's blocks table records r_b(t) x k_b(t); the part
   scaler needs the return of the position it scales); part scaler = the block scaler's convention (36 months, at least
   24, lagged one month, capped at 50); weight 1/n with n = the number of parts in the book (3 for the Core book),
   constant. Then the book scaler, the per-market cap, the gross cap and costs exactly as book.run; family shares are not
   used. Shadow book: the same construction over the shadow parts (Economic trend; Carry shadow; Value shadow). BASE's
   cross-sectional momentum is not a component.
6. E10: the bootstrap index matrix is gm.stats._stationary_idx(T, 10000, 6, 20261101) (the registered section 2
   bootstrap); p = (number of resamples with alpha_b - alpha_hat >= alpha_hat) / 10,000, as registered ("share"); the
   count is returned too (tools/power used (count + 1) / 10,001, as paired_sr_test does; the test checks the counts
   agree). A zero Core book (7.6 step 6: "alpha against a zero book (the pod's own mean)"): beta 0, alpha = mean. The
   window is the common months of the two series. Placebo: the window's months are cut into 12-month blocks from its
   first month (the last part-block kept), the blocks are put in random order by numpy default_rng(20261101).permutation,
   drawn in sequence, 1,000 placebos; the permuted array is every version's score or rank weight (before x 0.40 / vol),
   rows inside the window only, all markets jointly; p = (placebos with net Sharpe >= the pod's) / 1,000 on the window;
   pass p < 0.05. Date rules: each window's entry is redrawn uniformly among the NYSE days of its calendar year (R1, R3)
   or month (R2, R4), length kept in trading days, cut at the seal close; the caller re-reads the gates. H1-H3: H1 = the
   lb95 of gm.stats.paired_sr_test on the common pooled window > -0.10; H3 = check 5 of gm.protocol.decide (max fall not
   more than 2 points worse, worst month not more than 1 point worse); identical books pass. T4: the combined book is
   rescaled; the Core book is taken as run (its own book scaler is the same convention); common months.
7. E11: config key "cap_groups" = list of {"members": [...], "cap_from": None or a member}; a group's ratio = min(1,
   min over members with a position of cap_j / abs(x_j)), cap_j = the per-market cap of j (or of cap_from for every
   member); all members are multiplied by it; columns outside a group clip as today; no group = today. Gross weight:
   config.STRIP_GROSS_WEIGHT = 0.25 / 1.9 through the existing "gross_weights" config key.
8. E14: price return of day d = ratio of consecutive ^GSPC closes minus 1; c(m) = panel eq_us_spx(m) minus the SUM of
   the daily price returns of m (the reading that makes "a rule held all month earns exactly the panel's monthly
   excess return" true); N(m) = number of ^GSPC days in m; no value in a month without a panel return or without daily
   closes; no day after 2010-12-31.
9. Truncation horizons for the new stages: positions and signals compare months <= T; a k = 1 or tranche return or a
   tranche position whose holding or decision day falls after T in the full run is cut at T in the cut run (the holding
   cut rule), so these compare months <= T - 1 (all months at T = 2010-12-31, the seal); daily e(d) compares days <= T.

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
