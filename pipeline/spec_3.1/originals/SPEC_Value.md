# SPEC: Value (step 3.1, Agent A, 2026-11-23)

Engine read: gm-1.2.2 / gm-2.0.2-candidate (gm/signals.py value_values and equity_dy, book.py, panel.py,
bloomberg.py, variants.py), read only. Nothing run.

## 0. Header
- Pod: Value. Type: existing pod (cross-asset only).
- Register rows: T06 (version 1), T07 (version 2, second anchor). Dropped rows: T46 (directional value), T48
  (half value, half momentum); card items claimed by Value: T70, T93, T94.
- Source notes: THESIS_1.3_xs s1, s2 rows 5-10, 13, 14, s3 Value, s4, s5 X2, s10 and THESIS_1.3_xs_check; CHARTER_1.2
  s3 Value, s4, s6 and its check (table B row B23, table D); THESIS_1.3_method P3.
- Register status: existing book; version 2 enters with the A2 grids; X2 may bar citing the design return for the thesis.
- Dating class: version 1 B (Asness, Liew and Stevens 1997: value across country indexes, measured on book to market,
  no mechanism; Rogoff 1996: slow PPP reversion, a pattern; no source for the bond leg). Version 2 C (measures from
  QP15 2013 and QP08 2015). Rule 5 then allows: no holdout verdict unless 3.4 reads rule 5 to accept B; the pod is
  hindsight-flagged and cannot be Core under the current reading.

## 1. Economic claim
Working reading (the note's, assembled from asserted pieces): investors chase recent winners until flows "eventually push prices away from fundamentals causing reversals or value effects" (QP15-C05-1);
Value leans the other way and is paid as prices come back. The payer is not established, and the authors themselves
find the cross-asset pattern "difficult to reconcile under existing behavioral theories" (QP15-C53-3).
Rivals kept apart: a risk premium (cheap assets lose in bad states; the tested risks show the wrong sign), or an anchor
without a payer (income given up while waiting cancels the gain: "the value premium is perfectly neutralized by the carry" (QP08-C09-1), in a model).
Evidence grade: "Grade: weak" (1.3b s3, after its check; the draft's "moderate pooled" is superseded). The only
per-class figure in a quote is the bond leg's, which fails: "we are only able to produce a Sharpe ratio of 0.18" (QP15-C19-2).

## 2. What is predicted
- Quantity: next-month excess return of cheap against dear markets inside each class (no class-wide position in score units).
- Sign: cheap (high signal) earns more than dear (low signal).
- Largest: after overshoots, when one-way moves end; weakest during "very strong trends which have by definition hurt reversion based value predictors" (QP08-C22-4).

## 3. Signal
Code now (signals.py:317-327 equity_dy, :352-384 value_values; book.py:105 kind "cs", commodities dropped). At
month-end t:
1. Equities (8 markets): trailing 12-month dividend yield. Seven countries: Ken French country market return with
   minus without dividends, summed over 12 months, carried forward at most 12 months (annual file). US: SPY total
   return minus S&P 500 price return, summed over 12 months, clipped to [0, 0.10] (from 1993).
2. Bonds (7 markets, 10 and 30 years): (month-end yield - mean of the CPI year-on-year rate over the last 36 months,
   at least 24, CPI carried forward at most 18 months, lagged 1 month) / 100.
3. Currencies (13): minus the real appreciation over 60 months = -[ln(USD value now / 60 months ago) + sum over 60
   months of (local CPI yoy - US CPI yoy) / 100 / 12, CPI lagged 1 month].
4. Commodities: a 5-year reversal is computed (signals.py:356-358) but book.py:105 drops it: Value holds no
   commodities (register D7 settled from book.py).
5. Bloomberg switch (register D5): wherever Bloomberg loads, the equity measure becomes a rank composite of forward
   E/P, B/P and D/P for all 18 indexes (signals.py:359-372; bloomberg.py:165-183).
6. Position: cs_rank in class (ranks demeaned, sum |w| = 1, times the count; at least 3 markets) x 0.40 / vol, equal
   weight in class.
Registered form, version v at t:
- Version 1: measures 1-3 as coded. Version 2: equities as version 1; bonds: yield(t) - yield(t-60 month-ends), the
  same 7 markets each on its own maturity, higher = cheaper (closed here: the lag fixed at 60 month-ends by 1.3b
  correction 19); currencies: q(t) = ln USD value(t) + cumulative sum of (local CPI yoy - US CPI yoy) / 100 / 12 (CPI
  lagged 1 month, from the first month both exist), signal = -(q(t) - mean of q over all months up to and including
  t), at least 60 months of q (closed here: sign = cheap is a real rate below its own average, long cheap).
- Each version: w = cs_rank(signal, class), p = w x 0.40 / vol (CANDIDATE hybrid estimate), divided by the count of
  markets in the class with a position. Pod position = mean of the two versions, a missing one = 0.
- The Bloomberg composite is OFF: the registered equity measure is the dividend yield. Reason: it is a different
  measure, a Bloomberg-only input cannot run live (rule 7), and its index map gives eq_eu_stoxx50 the MSCI Emerging
  Markets index and eq_us_ndx and eq_us_r2k the MSCI USA index (bloomberg.py EQ_INDEX). Allowed at A1: the same
  12-month dividend yield from Bloomberg or LSEG as a data swap. Switching it off needs a registered engine flag (3.4).
- Rebalancing: month-end; first trading day after; tranches as SPEC_Trend section 3 (weekly check only).
Signs fixed: long cheap, short dear, by rank.

## 4. Markets
EQ 8 (eq_us_spx, eq_gb_ftse, eq_jp_nikkei, eq_au_asx, eq_ca_tsx, eq_hk_hsi, eq_de_dax, eq_fr_cac; the other 10
indexes have no free dividend yield); FI 7 (bd_us_10y, bd_us_30y, bd_de_10y, bd_gb_10y, bd_jp_10y, bd_ca_10y,
bd_au_10y); FX 13 (as SPEC_Carry). First return months as SPEC_Trend section 4. First positions: equities need a
dividend yield (from 1975-12; US 1993-12), a return and a volatility; bonds version 1 need 24 months of CPI and a
yield, version 2 a yield 60 month-ends earlier (bd_gb_10y 1993-12 + 60, bd_au_10y 1995-02 + 60, bd_ca_10y 2001-02 +
60); currencies need 60 months of exchange rates and CPI (fx_eur from 1999-02 + 60). A class with fewer than 3 markets
with a signal holds nothing. No market enters through a gate.

## 5. Sizing
As SPEC_Trend section 5. Pod share 0.15 in BASE and CANDIDATE (config.py); WORKFLOW 5.1 equal risk: 3.4 decides.

## 6. Version grid
| v | Equities | Bonds | Currencies |
|---|---|---|---|
| 1 | 12-month dividend yield | 10y (30y) yield minus 36-month mean CPI inflation | minus 60-month real appreciation |
| 2 | 12-month dividend yield | yield minus yield 60 month-ends earlier | minus deviation of the real rate from its expanding mean (at least 60 months) |
Total 2, averaged (was 1; 1.3b). None opened by a diagnostic.

## 7. Sample
Design window 1975-01 to 2010-12; flat before a class has 3 markets with a signal; eras 1975-89, 1990-2010; no month
after 2010-12. The expanding mean of version 2 uses months up to t only.

## 8. Data
| Input | History | Live (delay) | Licence |
|---|---|---|---|
| Country dividend yields | Ken French international country files (annual update), from 1975 | same; up to 12 months old (weak live source, charter s6) | free |
| US dividend yield | Yahoo SPY and ^GSPC, from 1993 | same, 1 day | free |
| Bond yields | as SPEC_Carry | 1 day | free |
| CPI year-on-year | OECD / FRED CPALTT01, revised | about 1 month | free |
| Exchange rates | Fed H.10, Yahoo, stooq month end | 1 day | free |
Rule 7: every input has a free live source (non-US dividend yield weak), so Value passes rule 7; rule 5, not rule 7,
keeps it from Core. The quarterly-CPI as-of rule of SPEC_Economic_trend section 3 applies to the CPI inputs here too.

## 9. Costs
book.py:46-57: US equities 1.0 bp, 4 rolls; other developed equities 2.0, 4; bonds 1.0, 4; developed currencies 2.0,
4; EM currencies 8.0, 4. Double-cost test applies. No turnover figure in the notes.

## 10. What would prove it wrong (design window)
- The averaged pod earns zero or less net in both eras.
- Paid by income, not by prices coming back (X2): if a leg's price part on its averaged position is zero or below, the
  "prices come back" claim fails for that leg (register entry "paid by income"; its design return may not be cited).
- Value and Trend's relative part lose together (1.3b (iii)): the "contrarian to the chase" reading predicts opposite signs.
- Loss event (P3): a long relative trend in which dear markets keep rising (QP08-C22-4); in the window, for example the
  late-1990s run of US equities (reader, public market history). Not flagged; 3.2 checks the example.

## 11. When it should stop working (live)
- The chase lasts (one-way class factors; QP08-C22-4).
- The anchor moves for good: the dividend yield "can be time-varying and thus not necessarily a measure of value" (QP08-C08-2).
- Funding eases (1.3b row 8: value weak then, pooled, after 1998 only).
- Income given up while waiting exceeds the price gain (1.3b row 14). Bands: W5, numbers at 3.4.

## 12. Knobs that were tuned
| Knob | Value | Origin |
|---|---|---|
| Equity measure | dividend yield | chosen after the 5-year reversal failed on design data (gm_CHANGES gm-1.1.0, already seen) |
| Commodities | out | dropped after design results (book.py:105 "failed", already seen) |
| Bond measure v1 | yield minus 36-month CPI | engine convention since gm-1.0.0 (QP15's alternative, 1.3b pack problem 6) |
| Bond measure v2 | 60-month yield rise | source (QP15-C09-5); ALREADY SEEN inside the V1 bond value composite (protocol_batch1.md V1, variants.py bond_value_composite: average rank of the real yield and the 60-month rise, same 7 bonds) |
| Currency measure v1 | t-60 to t, no skip | kept after the skip-12-month trial (protocol_batch1.md V2) |
| Currency measure v2 | expanding mean, at least 60 months | 1.3b (window "mine"); relative PPP (QP08-C11-3) |
| CPI window 36, carry-forward 18 | 36 / 18 | engine convention |
| At least 3 markets | 3 | engine convention (signals.py:393) |
| Pod share | 0.15 | engine plan (gm-1.0.0), unchanged |
Chosen or kept after seeing design results, fixed: equity measure, commodities out, currency no-skip = 3; plus version
2's bond leg, whose result is already seen through V1. Hindsight count: 3 (+1 seen version leg).

## 13. Gating diagnostics
- X2 (1.3b): per leg and version, monthly excess return split into income (one twelfth of: dividend yield minus
  3-month rate; bond yield minus 3-month rate; rate gap to the dollar; at the prior month-end) and price (the rest;
  bonds include roll-down). Gate on the leg's averaged position over all design months with a position: price part
  zero or below -> "paid by income" entry. Code facts: currency excess return includes the rate gap (panel.py:511);
  bond and equity returns are total returns minus the local rate (panel.py:473, 481). No sealed month. Noise band
  (JP5): 3.4.

## 14. Overlaps (re-checked in code)
- Carry: opposite in currencies; in bonds the real yield and bond carry differ by the short rate minus inflation
  (reader). Equity carry (dividend yield minus rate) is dropped (book.py:106), so the equity dividend yield sits only here.
- Trend: A2 reads version 2 with Trend's old and new grids; Value is judged by what it adds to a book holding Trend.
- Card 2 R1 (T20): Value is cross-asset (cs_rank demeaned in score units), so it holds no class-wide US bond short,
  only relative ones (confirmed, signals.py:388-393).
- Card 5 R1 (T34, C15) and card 4 T93, T94: Value holds NO commodities (book.py:105), so "Value bets the other way" in
  slow-supply commodities and "oil bought cheap" as a Value position are not held. For 3.2.
- Card 1: "in currencies valuation never matters" (MT203-C10-4), against the currency leg (C14): recorded, no change.

## 15. Open choices
| Choice | Closed as |
|---|---|
| Commodities out, currencies in (1.3b JP9) | rule: as the note registers; the asymmetry is recorded; X2 by leg shows whether the currency leg is paid by income. 3.2 confirms. |
| Version 2 bond lag | 60 month-ends (section 3). |
| Version 2 currency sign and window | section 3. |
| Bloomberg composite (D5) | rule: off; registered engine flag at 3.4. |
| Version 2's bond leg already seen through V1 | 3.4 (hindsight flag, trial count). |
| Value next to directional Trend (JP4), X2 noise (JP5), rule 5 (JP7) | A2 report, 3.4. |
| Register vs note | none found. |

## 16. Builder must not change
Cross-asset form only; signs (long cheap); measures and windows of both versions; dividend yield as the equity measure
(Bloomberg composite off); no commodities; 3-market minimum; design window; free data; costs.
