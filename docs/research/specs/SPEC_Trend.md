# SPEC: Trend (step 3.1, Agent A, 2026-11-23)

Engine read: gm-1.2.2 (BASE) and gm-2.0.2-candidate (CANDIDATE), gm/config.py, book.py, vol.py, daily.py, panel.py,
signals.py, bloomberg.py (read only). Nothing run. Line numbers are today's.

## 0. Header
- Pod: Trend. Type: existing pod.
- Register rows: T01 (pod), T09 (breadth item: alternative commodities, gated market set), T10 (short-rate futures,
  gated market set, shared with Economic trend and Carry), T12 (cross-sectional momentum: not a pod, one reported line here).
- Source notes: CHARTER_1.2 s2 rows 1-10, s3 Trend, s4, s5 D1, D2, D4, D6, s6, s11 and CHARTER_1.2_check (tables B, C,
  D, section 4); THESIS_1.3_xs s3 and s4 (directional only, T12) and its check; THESIS_1.3_rates s4 (T10);
  THESIS_1.3_method P3; foundation U02-U07 through the charter.
- Register status: existing book; grid and tranches in Batch A2 (hygiene: must not hurt, net of about 0.23 selection
  inflation); T09 and T10 only through charter D1 (T10 through a D1 extension to be registered at 3.4).
- Dating class: B (register T01). Fung and Hsieh 2001 document the strategy and its option-like payoff before 2011,
  but "we are not advocating that markets trend" (QP09-C06-4), and their rule form is a lookback straddle, not this
  return-sign rule. Rule 5 then allows: the holdout verdict counts only if step 3.4 reads rule 5 to accept a documented
  strategy without a documented cause; otherwise Trend's holdout result is descriptive and, by WORKFLOW s5, Trend cannot
  be Core. Facts here, reading at 3.4 (charter JP9).

## 1. Economic claim
Investors digest macro change slowly: "slow digestion of information" (MT116-C02-1). So a price move toward a new
level continues for weeks to months: "a journey that takes you from some valuation level to the new valuation level" (MT216-C12-1).
The pod holds each market in the direction of its recent excess return. Who pays is not established
(charter s3): fragments name rebalancers who sell rises and buy falls; rival causes (risk premium, a sustained
imbalance, volatility clustering) imply other payers. The signal holds total excess return, so it also earns carry:
"this will accumulate though the total return and produce a momentum effect" (QP08-C18-4). Written blend, closed here (charter JP4): the pod's claim is about the total excess return a holder
earns; the carry part is measured, not removed.
Evidence grade, as the charter gives it: the chain is "ASSERTED in four notes (row 8), tested in none" (charter s3);
no pod grade; U01-U07 numbers unverified (audit 1.1).

## 2. What is predicted
- Quantity: the sign of each market's next-month excess return (panel.py: futures-style excess return over the local
  3-month rate), over the month after the decision month-end.
- Sign: same as the sign of the trailing 1-, 3-, 6- or 12-month excess return.
- Largest: in long, large moves; in equity falls deeper than 15% from the 24-month high, and late in them:
  "anything less than 15% actually tends to be negative" (MT194-C06-2); the first part of a fall is
  "often a negative environment for trend following" (MT194-C06-4). Smallest or negative: short or V-shaped reversals and markets pinned by policy.

## 3. Signal
Code now (book.py:60-76 trend_signal; book.py:95-151 family_positions; config.py BASE and CANDIDATE):
- BASE: score = mean over h in (1, 3, 12) of sign(compounded h-month excess return); vol model m36. CANDIDATE: same
  score, vol model hybrid. Input X = monthly excess returns R (spot False: carry included, book.py:63-68).
- Compounded return: lvl = cumulative product of (1 + R, gaps as 0) where data exist; h-month return = lvl(t) / lvl(t-h) - 1.
- Position per market = clip(score, -1, 1) x 0.40 / vol, then divided by the number of markets in the class with a
  position that month (equal weight in class, book.py:126-139).

Registered change (charter s4): one version per cell of the grid in section 6. Version v at month-end t:
1. Inputs: R up to t (monthly excess return of month t is known at the close of t).
2. Shape "sign": s = sign(lvl(t) / lvl(t-h) - 1), h = the version's lookback; 0 if exactly 0; no value if lvl(t-h) is missing.
3. Shape "graded": s = clip( sum of ln(1 + R) over months t-h+1..t / (vol_v(t) x sqrt(h / 12)), -2, 2 ) / 2
   (book.py:73-76, cap 2.0 from config.py BASE trend cap). vol_v is the version's own estimate (step 4).
4. Volatility vol_v: "m36" = 36-month standard deviation of monthly R, at least 12 months, x sqrt(12) (vol.py:16-17);
   "hybrid" = max(0.7 x fast + 0.3 x slow, 0.75 x slow), fast = EWMA of daily squared log returns, half-life 35
   days, at least 40 days, where free daily data exist (daily.py), else EWMA of monthly squared returns, half-life
   6 months, at least 12; slow = 120-month standard deviation, at least 36; fast alone until slow exists, m36 where
   neither exists (vol.py:38-52; config.py vol).
5. Version position p_v = clip(s, -1, 1) x 0.40 / vol_v, divided by the count of markets in its class with a p_v that
   month (book.py:126-139).
6. Pod position = sum over the 16 versions of p_v / 16, a missing p_v counted as 0 (closed here: each version is a
   complete pod as the charter says; averaging at the unscaled position keeps today's book arithmetic, book.py:188-195).
7. Rebalancing: decided at the month-end close; traded on the first trading day after month end (config.py comment,
   execution rule); earns month t+1. Weekly tranches (B7, charter s4), closed here: tranche j = 0..3 decides on trading
   day 5 x j after the month's last trading day, holds one quarter of the pod until its next decision day, and uses only
   prices at that day's close and series published by that day; monthly design runs use tranche 0 only; the tranche
   form runs only in the 1990-2010 weekly check.
The SIGN is fixed: long when the trailing excess return is positive. It cannot be flipped after results.

## 4. Markets
61 ids, all distinct (panel.py EQUITY 18, BONDS 9, SHORT 5, FXM 13, COMMOD 16; st_us_2y removed in gm-1.2.2), plus
cm_aqr_ew (trend only, to 2000-12, book.py:121-122). First return month below = 2010-12 minus the design months on record
(tools/bbgq/engine_ref.json market_months, gm-1.2.2 reference; assumes no gaps; the builder confirms with
panel.coverage()). A version's first position = first return month + max(h, 12) months; the class block is scaled
once it has 24 months of its own returns (book.py:191). Design positions start no earlier than 1975-01.

| Class | Markets (first return month) |
|---|---|
| EQ (18) | eq_us_spx 1963-07, eq_gb_ftse 1975-01, eq_jp_nikkei 1975-01, eq_au_asx 1975-01, eq_ca_tsx 1977-01, eq_hk_hsi 1981-02, eq_us_ndx 1985-02, eq_us_r2k 1987-10, eq_de_dax 1988-01, eq_fr_cac 1990-04, eq_br_ibov 1996-11, eq_kr_kospi 1997-01, eq_mx_ipc 1997-02, eq_cn 1997-08, eq_in 1997-08, eq_tw 1997-08, eq_eu_stoxx50 2000-08, eq_za 2001-01 |
| FI (14) | bd_us_5y 1962-02, bd_us_10y 1962-02, bd_de_10y 1972-10, st_de_2y 1972-10, st_jp_2y 1976-01, bd_us_2y 1976-07, bd_us_30y 1977-03, bd_jp_10y 1986-08, bd_gb_10y 1993-12, st_gb_5y 1994-01, bd_au_10y 1995-02, st_au_2y 1995-02, bd_ca_10y 2001-02, st_ca_2y 2001-02 |
| FX (13) | fx_aud, fx_cad, fx_gbp, fx_jpy 1971-02, fx_chf 1972-02, fx_nzd 1974-01, fx_nok 1979-02, fx_zar 1980-02, fx_sek 1982-02, fx_krw 1991-02, fx_brl 1996-11, fx_mxn 1997-02, fx_eur 1999-02 |
| CM (16 + 1) | cm_aqr_ew 1970-01 to 2000-12, cm_wti 1985-02, cm_natgas 1994-02, cm_heatoil 1994-03, cm_cotton 2000-02, cm_gold 2002-01, cm_gasoline 2002-04, cm_silver 2002-05, cm_coffee 2003-01, cm_platinum 2003-01, cm_sugar 2003-03, cm_corn 2003-05, cm_wheat 2003-07, cm_copper 2003-08, cm_soybeans 2003-09, cm_cattle 2004-01, cm_brent 2008-04 |

Markets only through a gate: T09 alternative commodities (charter D1; under the 30% cap of commodity risk,
book.py:140-148; none has a locked history and a live price today); T10 short-rate futures strips (D1 extension at 3.4;
eight contracts locked and a registered live source; today the euro at most, and LSEG is not registered, so none).
Alternative-commodity columns that panel.py:570-575 creates whenever Bloomberg data load stay OFF until D1 admits them
(charter A1, register D4).

## 5. Sizing
- Market: 0.40 / vol_v per unit score (book.py:132); equal weight in class; four classes at equal risk: each class
  block scaled to unit volatility on its trailing 36 months (at least 24), lagged, scale capped at 50 (book.py:188-195).
- Book: family share x block; whole book scaled to 10% volatility on 36 months (at least 24), lagged (book.py:197-199);
  per-market cap 0.10 x 0.10 x 3 / vol (book.py:200-201); gross face value at most 5x (book.py:202-204).
- Pod share: config.py BASE trend 0.30, CANDIDATE 0.45 (family shares 30/30/20/15/5 and 45/15/25/15/0). WORKFLOW 5.1:
  "Core pods at equal risk". They disagree; step 3.4 decides (register F8). The vol estimate of the cap (book.py:200)
  is the engine vol, not a version's: closed here, the cap uses CANDIDATE's hybrid estimate for every version.
- Book-level items that may change Trend's trading, each only through its gate: no-trade buffer (D2), faster book
  scaler (D3) (register B9).

## 6. Version grid
Averaged with equal weight, never picked. 4 x 2 x 2 = 16, each in four weekly tranches (weekly check only).

| v | Lookback h (months) | Shape | Vol |
|---|---|---|---|
| 1-4 | 1 / 3 / 6 / 12 | sign | hybrid |
| 5-8 | 1 / 3 / 6 / 12 | sign | m36 |
| 9-12 | 1 / 3 / 6 / 12 | graded, cap 2 | hybrid |
| 13-16 | 1 / 3 / 6 / 12 | graded, cap 2 | m36 |

Total 16. No version exists only through a diagnostic. Markets added by D1 (T09, T10) enter all 16 versions.

## 7. Sample
Design window 1975-01 to 2010-12 (TESTING_PROTOCOL s1); every input of every version exists for most markets by
then. Months before a market or a version has a position count as flat, not excluded. Eras 1975-89 and 1990-2010
(protocol.py ERAS). Weekly check 1990-2010 only. No month after 2010-12 is read, printed or used, including by the
lookbacks and the vol windows of the last design months (they read only earlier months).

## 8. Data
| Input | History: source, first date | Live: source, delay | Licence |
|---|---|---|---|
| Monthly excess returns, 61 ids + cm_aqr_ew | free panel (panel.py: ETFs, MSCI manual file, Ken French, FRED, central banks, stooq, Yahoo, EIA, AQR); dates in section 4 | same free sources, 1 day | free (MSCI file kept local) |
| Daily returns for hybrid vol and tranches | free (daily.py): FX 1971, US bonds 1962, Japan 1974, Bundesbank 1997, BoE 1993, RBA 1995, BoC 2001, Yahoo equities, EIA energy 1983, other commodities 2000 | free, 1 day | free |
| T09 candidates | LSEG GSCI by commodity 1970-87, LSEG L8 others, LME 1970; not locked | none | LSEG on the user's PC, not registered as live |
| T10 strips | LSEG Euribor 1994; Bloomberg sterling 1-5 1988 (no live); not locked | LSEG only | LSEG not registered |
Rule 7: every input of the 61 ids has a free live source, so Trend can be Core on rule 7. T09 and T10 markets cannot
join a Core Trend until each has a registered live source.

## 9. Costs
book.py:46-57 cost_bp, one-way bp of face value on every change, plus rolls (2 x one-way x rolls per year / 12 on the
held position): US equities 1.0 bp, 4 rolls; other developed equities 2.0, 4; emerging equities (EM_EQ) 5.0, 0, plus
1%/yr borrow on shorts (book.py:214); bonds and notes 1.0, 4; developed currencies 2.0, 4; EM currencies 8.0, 4; WTI,
Brent, heating oil, gasoline 4.0, 12; natural gas 6.0, 12; other commodities 4.0, 5. D1 candidates are costed at 8 bp
(charter D1). Turnover: the notes give no figure. The double-cost test applies (book.py run cost_mult 2.0).

## 10. What would prove it wrong (design window)
- The averaged pod's net return per unit of risk is zero or below in both eras.
- In equity falls deeper than 15% from the 24-month high the Trend return is not positive (the payoff the claim names;
  D4 table, S&P 500 base).
- The profit comes from the carry part, not the price part: the reported split (total vs carry accrual, using the Carry
  pod's carry values of section 3 of SPEC_Carry, bonds and currencies only) shows the price part zero or below.
- The relative part (T12 split, below) carries the profit while the class-average part is zero or below: the claim is
  about each market's own direction, so this would point to cross-sectional momentum instead.
- Loss event (P3): sharp V-shaped reversals and young, shallow equity falls (MT194-C06-4); in the window: 1987-10 to
  1987-11 (config.py STRESS_WINDOWS). Not flagged "loss not seen".

## 11. When it should stop working (live kill and review conditions)
- Markets pinned by policy: "every time equities at least went down somebody popped up and propped up the market" (MT014-C16-1); observable: falls that reverse within days, a lower trend return per unit of market move.
- Short shocks: moves of a few days that a monthly rule cannot hold (MT045-C12-2).
- Capital crowding: "any business that succeeds and isn't a monopoly tends to get too much capital applied to it" (MT070-C01-2).
- If D6 opens it: trend return per unit of market move below the design slope (breakdown check).
- Bands for live against backtest come from W5; their numbers are set at 3.4.

## 12. Knobs that were tuned
| Knob | Value | Origin |
|---|---|---|
| Lookbacks | 1, 3, 6, 12 | grid; 1/3/12 had been chosen over 3/6/12, 6/12, 12 after design results (gm_CHANGES trial log 9; gm_trials.csv rows trend-3/6/12, trend-6/12, trend-12); 6 restored by the charter |
| Shape | sign; graded | grid; graded ("trend cont", gm_trials.csv 2026-11-01 01:09) already seen |
| Cap of graded | 2.0 | engine convention (config.py BASE trend) |
| Vol estimate | hybrid; m36 | grid; hybrid adopted after design results (protocol_batch0.md B0.1) |
| Hybrid parameters | 35 days, 6 months, 0.7, floor 0.75, 120/36 months | engine convention fixed with the one hybrid trial (gm_CHANGES gm-2.0) |
| Sizing constant | 0.40 / vol | engine convention (book.py:132) |
| Equal weight in class | equal | kept after the cluster-weights trial (gm_trials.csv cluster weights) |
| Four classes at equal risk | equal | engine convention; class risk as a version not added (section 15) |
| Total vs spot | total excess return | kept after the spot-only trial (gm_trials.csv trend spot-only) |
| Trade timing | first trading day after month end | chosen from the timing grid (gm_CHANGES gm-2.0) |
| Market list | 61 ids + cm_aqr_ew, hand-picked survivors | gm_CHANGES gm-1.2.0 "Known and documented"; EM-before-2000 test seen (stats_audit s5) |
| Pod share | 0.30 / 0.45 | 0.45 adopted after design results (protocol_batch0.md B0.2); book level |
| Tranche offsets | 0, 5, 10, 15 trading days | closed here (charter "one week apart") |
Chosen or kept after seeing design results, fixed (not averaged): total vs spot, equal weight in class, trade timing,
market list = 4 pod-level knobs; plus 1 book-level (pod share 0.45). Hindsight count: 4 (+1 book).

## 13. Gating diagnostics
- D1 (charter): gates T09 and T10 markets. A candidate joins only if both averaged shares are under one half, it has
  120 months before 2011 and it is costed at 8 bp; else the breadth item is dropped. PCA on the 61 distinct markets.
  Candidate half cannot run until a locked history exists. T10 needs a D1 extension registered at 3.4.
- D4 (charter): if Trend's mean is negative in the young 5-15% cell and positive beyond 15% (S&P 500 base), this spec
  lists "young, shallow equity fall" as an expected-loss state in section 10; else no such line. Cells under 6 months
  reported only. Reads no sealed month.
- D6 (charter): if the era slopes differ by less than two Newey-West standard errors (2 lags, year-level means),
  "trend return per unit of market move, against the design slope" becomes Trend's breakdown check (section 11); else
  dropped. Reads no sealed month.
- D2, D3 (book items, B9): D3 as written reads sealed months (forward 12-month windows from 2010 month-ends read 2011).
  Proposal for 3.4: end D3's state months at 2009-12 (register D15).
- Proposed, not registered (charter JP2, 3.4): zero-slot shape report: five-state equity table for Trend and Trend
  against the Fung-Hsieh trend factors 1994-2010.

## 14. Overlaps
- Carry inside Trend: confirmed in code (config.py trend spot False; book.py:63-68 strips carry only if spot is True).
  Measured by the reported split of section 10, A2 report.
- Economic trend's risk theme: half of it is the country index's own 12-month excess return (signals.py:215-219),
  exact for 13 of 18 indexes, near for 5 (charter check item Y). Measured at A2 (correlation of the two pods' equity
  positions, reported).
- T12 cross-sectional momentum: one reported line, closed here: per version and class, split the score s into the class
  mean of s and s minus that mean; each part x 0.40 / vol_v / n gives a class-average and a relative position; report
  both returns (B12). BASE still holds a 5% xsmom family (config.py BASE family_w; book.py:104, 12-1 return, rank in
  class); CANDIDATE holds 0. Whether BASE keeps it: 3.4 (register C12).
- Carry in both forms vs Trend directional only (1.3b JP3, C17): closed in section 15.
- Card rules that repeat or oppose Trend (C13): T28, T29, T31 long S&P date rules, T15 stock leg, T34 (card 5 D1 reads
  Trend positions at 75%), T30 shorts after a ramp; T13 and T14 buy bonds when Trend sells them. Measured by the card
  duplicate diagnostics (C1-D2, C4-D2, C5-D1) at B2; one threshold for all cards is set at 3.2 (register C13).

## 15. Open choices
| Choice | Closed as |
|---|---|
| Static or slow-only vol version (charter JP1) | rule: not added. m36 is the slow end in code; slow-only (120 months) is 30% of the hybrid and sets its floor (charter s4, VARIANTS C2); static-at-entry sizing is not built and would be resized anyway by the 36-month block and book scalers, so no static book exists. 3.2 confirms. |
| Total vs spot as a version (JP4) | rule: written blend (section 1); split reported (section 10). |
| Class risk as a version (JP7) | rule: four classes at equal risk stay (charter s4 "Fixed"); any other vector would come from QP09-C21-5's 1989-97 fund shares, a sample-fitted weight. Report by class. 3.2 confirms. |
| Directional only while Carry has both forms (1.3b JP3) | rule: Trend's claim is about each market's own move, class-wide moves included (section 1); the T12 split shows what is relative. |
| Tranche offsets | rule: 0, 5, 10, 15 trading days after month end (section 3). |
| Cap vol for the per-market cap | rule: CANDIDATE hybrid estimate (section 5). |
| Card 5 "no short while the front is above the second contract" (register B18, note for Trend) | rule: not imported. It is a card 5 process rule from 2022-24 quotes; Trend's rules come from the charter. |
| "Loss not seen" flag (P3) | set: event and months named (section 10); not flagged. |
| BASE xsmom 5%, pod share 0.30 vs 0.45 vs equal risk, incumbent for A2 | step 3.4 (register C12, F8, F9). |
| Rule 5 reading for class B | step 3.4. |

## 16. Builder must not change
Sign (long the trailing excess return); the 16-version grid and equal-weight averaging; lookbacks, shapes, cap 2, vol
models and their parameters; design window 1975-01..2010-12 and the eras; no month after 2010-12; the market list
(alternative commodities off; st_us_2y absent); free data sources (Bloomberg only as the registered A1 data swap of the
same series); costs of book.py:46-57 and the double-cost run; tranche offsets.
