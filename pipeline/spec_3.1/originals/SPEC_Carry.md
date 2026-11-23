# SPEC: Carry (step 3.1, Agent A, 2026-11-23)

Engine read: gm-1.2.2 / gm-2.0.2-candidate (gm/signals.py carry_values, panel.py, book.py, bloomberg.py), read only.

## 0. Header
- Pod: Carry. Type: existing pod, three legs.
- Register rows: T03 (currency leg), T04 (energy leg), T05 (bond leg); T10 (short-rate futures strips, gated market
  set with a new carry measure, written here). Dropped row: T47 (equity-index carry).
- Source notes: THESIS_1.3_xs s1, s2 rows 3, 4, 11-14, s3 Carry, s5 X1, X2, s10 and THESIS_1.3_xs_check; CHARTER_1.2
  s2 row 11, s3 Carry, s4, s5 D4, s6 and its check; THESIS_1.3_rates s4 and its check (corrections 14-16); THESIS_1.3_method P3.
- Register status: existing book; grid in Batch A2; X1 may change the energy signal (registered with A1); D4 may add
  a stop state; T10 only through a D1 extension (3.4).
- Dating class by leg: currency A for the cross-sectional version only (Lustig and Verdelhan 2007); energy B (Erb and
  Harvey 2006 rule form; de Roon, Nijman and Veld 2000 mechanism; Keynes 1930); bond C (Fama and Bliss 1987 not
  confirmed). Rule 5 then allows: a holdout verdict for the currency cross-sectional part at most; the rest
  descriptive unless 3.4 reads rule 5 otherwise. Whether a pod with mixed legs can be Core: 3.4.

## 1. Economic claim
A forward price is set by people passing on a price risk; whoever takes the risk earns the gap if prices do not move
(reader). By class, as the note states after its check: currencies, a risk premium: low-rate currencies "hold their own in low domestic consumption states" (QP08-C04-5);
the savers who pay are the note's reading. Commodities: "producers selling futures to insure themselves against price falls" (QP08-C05-5),
or, as a rival, storage: "the theory of storage links backwardation to tight inventories" (QP08-C05-8). Bonds: pattern,
no mechanism: "Rates tend to roll down the curve" (QP08-C05-9).
Evidence grade: "grade weak on this pack" (1.3b s3). The one cited cross-class test leans to risk: carry
"is partially explained by recession and volatility risk" (QP08-C05-1).

## 2. What is predicted
- Quantity: next-month excess return of each bond, note, currency (vs USD, rate gap included) and energy future.
- Sign: same as the sign of carry (version 1) and of carry's rank in its class (version 2).
- Largest: when carry gaps are wide and no bad state arrives; losses in bad states are the risk being paid
  (currencies), and in funding breaks (charter row 11, ASSERTED).

## 3. Signal
Code now (signals.py:330-349 carry_values; book.py:106, 131 kind "half"): carry per market at month-end t:
1. Bonds and notes (signals.py BD, 14 ids): (month-end yield of that maturity - local 3-month rate of the previous
   month) / 100 (yield_of: FRED DGS for the US, central-bank files elsewhere; rate: OECD monthly average, euro area for DE).
2. Currencies (13): ((local 3-month rate - US 3-month rate) / 100), lagged 1 month (OECD monthly averages).
3. Energy (cm_wti, cm_natgas, cm_heatoil, cm_gasoline): 12 x (F1 / F2 - 1), EIA NYMEX contracts 1 and 2 at month
   end (panel.py:254-261); positive = backwardation.
4. Equity carry is computed but dropped in book.py:106.
5. Position today: w = 0.5 x rank in class + 0.5 x sign(carry) (book.py:131), rank = cs_rank: ranks demeaned, scaled to
   sum |w| = 1, times the count, only with at least 3 markets (signals.py:388-393); then x 0.40 / vol, equal weight in class.
6. Bloomberg switch (register D6): wherever the Bloomberg workbook loads, carry_values (signals.py:342-348) replaces or
   adds commodity carry ln(F1 / F_far) / years from the farthest contract present, for non-energy markets too.
Registered form:
- Version 1 (directional): w = sign(carry), 0 if 0. Version 2 (cross-asset): w = cs_rank(carry) as in step 5, no
  position when fewer than 3 markets of the class have carry. Each: p = w x 0.40 / vol (CANDIDATE hybrid estimate),
  divided by the count of markets in the class with a position. Pod position = mean of the two, a missing one = 0.
  Closed here: this reproduces today's half-and-half exactly (book.py:131), so A2 tests averaging, not a new rule.
- The Bloomberg switch is OFF: commodity carry is the EIA F1 / F2 measure only, on the four energy markets. Reason: the
  farthest-contract measure is a different measure on new markets, and depends on which tickers loaded (open risk,
  register D16). Allowed at A1: Bloomberg or LSEG contracts 1 and 2 of the same four markets as a data swap of the
  same formula. Switching it off needs a registered engine flag (3.4, with A1).
- X1 (if its gate opens for a market): that market's carry in both versions becomes carry minus the mean, over all
  earlier same-calendar month-ends (at least five; no signal before), of (carry minus its trailing 12-month mean, the
  12 month-ends up to and including that month-end).
- Rebalancing: month-end, traded the first trading day after; tranches as SPEC_Trend section 3 (weekly check only).
- T10 strip market (only if admitted), closed here: market = the first eight quarterly 3-month rate futures expiring
  after the holding month, equal face value; monthly excess return = mean over the eight of -0.25 x (r(t) - r(t-1)) / 100
  for the same contract, r = 100 - settlement price. Carry = the roll down the strip if the curve does not move: each
  contract's rate falls to its nearer neighbour's in three months, gaining 0.25 x (r_i - r_i-1) / 100, i.e.
  (r_i - r_i-1) / 100 a year; averaged over i = 1..8 with r_0 = the local 3-month rate of the previous month, carry =
  (r_8 - r_0) / 800 a year per unit of face value. Scaling: the same per-unit-of-face-value, per-year basis as bond
  carry, ranked in the FI class unchanged (bond carry per unit of duration was tested and rejected, protocol_batch1.md C1).
Signs fixed: long positive carry; long high rank.

## 4. Markets
FI 14 (bd_us_2y, bd_us_5y, bd_us_10y, bd_us_30y, bd_de_10y, bd_gb_10y, bd_jp_10y, bd_ca_10y, bd_au_10y, st_de_2y,
st_gb_5y, st_ca_2y, st_au_2y, st_jp_2y); FX 13 (fx_eur, fx_jpy, fx_gbp, fx_chf, fx_aud, fx_nzd, fx_cad, fx_sek,
fx_nok, fx_mxn, fx_brl, fx_krw, fx_zar); CM 4 (cm_wti, cm_natgas, cm_heatoil, cm_gasoline). First return months as
SPEC_Trend section 4. A market's first position needs its carry (yield and both rates, or EIA contracts 1 and 2: CL
from 1983) and a volatility estimate (12 months); version 2 needs 3 markets in its class (CM: from the month the third
energy market has carry; before it the CM block holds version 1 only). Not in the pod: equities (book.py:106), Brent,
other commodities. Through a gate: T10 strips (D1 extension; eight contracts locked and a registered live source;
today none).

## 5. Sizing
As SPEC_Trend section 5. Pod share: config.py BASE carry 0.20, CANDIDATE 0.25; WORKFLOW 5.1 equal risk: 3.4 decides.
Strip markets, if admitted: counted at 0.25 / 1.9 of face value in the gross cap (2-year equivalent, as variants.py
us_3m_rate); closed here by that engine convention.

## 6. Version grid
| v | Form | Signal |
|---|---|---|
| 1 | directional: sign of carry | section 3 |
| 2 | cross-asset: rank in class | section 3 |
Total 2, averaged, unchanged from the charter and 1.3b. X1 changes a market's signal in both versions, not the count.

## 7. Sample
Design window 1975-01 to 2010-12; markets enter as data start; months before a position are flat; eras 1975-89,
1990-2010; no month after 2010-12. X1's calendar means use design month-ends only.

## 8. Data
| Input | History | Live (delay) | Licence |
|---|---|---|---|
| Bond and note yields | FRED DGS, Bundesbank, BoE, BoC, RBA, MoF files; month end | same, 1 day | free |
| 3-month rates | OECD IR3TIB01 / TB3MS monthly averages | same, 1 month; GB and euro-area series end 2026-01, carried forward at most 12 months (panel.py:368-370) | free |
| EIA contracts 1, 2 | EIA NYMEX daily, from 1983 (CL) | EIA, 1 day | free |
| Strips (T10) | LSEG (Euribor 1994), Bloomberg sterling 1-5; not locked | LSEG only | not registered |
Rule 7: every input of the 31 markets has a free live source: the pod can be Core on rule 7, once a replacement for the
GB and euro OECD rates exists (3.4). Strip markets cannot join a Core pod without a registered live source.

## 9. Costs
book.py:46-57: bonds and notes 1.0 bp one-way, 4 rolls a year; developed currencies 2.0, 4; EM currencies (MXN, BRL,
KRW, ZAR) 8.0, 4; WTI, heating oil, gasoline 4.0, 12; natural gas 6.0, 12. Strip markets: 8 bp (D1 admission cost), 4
rolls. Double-cost test applies. No turnover figure in the notes.

## 10. What would prove it wrong (design window)
- The averaged pod, or a leg, earns zero or less net in both eras.
- Currencies: losses that come without a bad state (the risk story predicts losses in bad states and pay otherwise).
- Commodities: high-carry positions lose on average. ("backwardation is not the norm" (QP08-C05-6) is a stop sign,
  not a falsifier.)
- Bonds: the leg is only a standing long: its return is matched by a position with the same average exposure and no
  timing (placebo, if registered for existing pods at 3.4).
- Profit source: the X2 income/price split, reported by leg for this pod too (income = carry / 12 at the prior month
  end): a Carry leg whose price part is strongly negative and income part positive is paid as carry says; a leg paid
  mostly by price is not the carry mechanism.
- Loss event (P3): "full liquidity break, a dash for cash" (MT083-C05-1); in the window: 1998-08 to 1998-10 and 2008-09 to
  2008-12 (config.py STRESS_WINDOWS). Not flagged.

## 11. When it should stop working (live)
- Rate gaps and curve slopes near zero everywhere (reader, 1.3b).
- A funding break (if D4 opens the line).
- No hedger paying: "backwardation is not the norm" (QP08-C05-6).
- A long rise in yields against a standing long bond leg (1.3b). Bands: W5, numbers at 3.4.

## 12. Knobs that were tuned
| Knob | Value | Origin |
|---|---|---|
| Form | sign and rank, averaged | grid; half-and-half chosen over directional-only and cross-sectional-only after design results (gm_CHANGES trial log 3), now the grid |
| Equities | out | dropped after design results (gm_CHANGES gm-1.1.0, already seen) |
| Bond carry scale | per unit of face value | kept after the per-duration trial (protocol_batch1.md C1) |
| Energy measure | F1 / F2, annualised | engine convention (EIA has 4 contracts) |
| Rates | OECD 3-month, lagged 1 month | engine convention (gm-1.2.0 audit) |
| Markets | 14 + 13 + 4 | EM currency set hand-picked (gm_CHANGES gm-1.2.0 "Known and documented") |
| Strip carry and scale | (r_8 - r_0) / 800, per face value | closed here |
| X1 gate 0.25, five months | 0.25, 5 | 1.3b (fixed before results) |
| Pod share | 0.20 / 0.25 | 0.25 adopted after design results (B0.2); book level |
Chosen or kept after seeing design results, fixed: equities out, bond carry per face value, market list = 3 (+1 book).

## 13. Gating diagnostics
- X1 (1.3b): per energy market, share of carry-signal variance explained by its 12 calendar-month means over design
  month-ends; 0.25 or more -> the seasonal adjustment of section 3 for that market, both versions, registered with A1;
  else no change. Signals only; no sealed month.
- D4 (charter): if Carry loses in both the 1998 and the 2008 windows, "funding break" becomes its stop state (section
  11); else dropped. No sealed month.
- X2 (1.3b): Value's diagnostic; its split by leg is reported here too (section 10). No gate on Carry.
- D1 extension (3.4): admits strip markets.

## 14. Overlaps (re-checked in code)
- Trend holds carry (config.py trend spot False): measured by the split in SPEC_Trend section 10.
- Value is the opposite trade in currencies (1.3b row 14) and differs from bond carry by the short rate minus inflation
  (reader); both in the book: X2 and A2 report.
- T25 card 3 R3 (C8): when Fed funds exceeds the US 2-year yield, bond carry of bd_us_2y (yield minus TB3MS) is likely
  negative, so version 1 is short the US 2-year as R3 is. Card 3 D1 must read Carry's positions (3.2).
- T08 Curve carry and T35 (C9): same energy curves; in backwardation version 1 is long, which is T35's position by
  construction. Curve carry spec (Agent B) states its relation.
- T106, T99 (card 5): "Carry directional (long backwardation)" and the contango short are held only for the four EIA
  energy markets; no other commodity has carry in the book on free data.
- T10, T11 (C10): strip markets and Strip reversion trade the same contracts.
- C17: Carry in both forms, Trend directional only (SPEC_Trend section 15).

## 15. Open choices
| Choice | Closed as |
|---|---|
| Bond leg: pattern or dated source (1.3b JP2) | rule: kept in the pod as a pattern, as the note keeps it; dating C, holdout descriptive. |
| Equities left out on a directional 51% correlation (JP8) | rule: stay out (1.3b "Fixed"); 3.2 confirms. |
| Bloomberg non-energy curve carry (D6, D16) | rule: off (section 3); engine flag registered at 3.4 with A1. |
| Strip carry formula and scaling (1.3a correction 15) | rule in section 3; per face value, as bond carry. |
| Strip cost and gross weight | rule: 8 bp (D1), 0.25 / 1.9 (variants.py). |
| Placebo for existing pods (JP6), mixed-leg dating, pod share | 3.4. |
| GB and euro OECD rates after 2026-01 | 3.4 (live source). |
| Register vs note | none found. |

## 16. Builder must not change
Signs; two versions averaged as section 3; market list (no equities, energy = 4 EIA markets); EIA F1 / F2 measure;
Bloomberg curve carry off; X1 only through its gate; lags; design window; costs; strip formula if admitted.
