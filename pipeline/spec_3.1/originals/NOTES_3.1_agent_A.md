# Agent A notes (step 3.1, existing pods), 2026-11-23

Specs: SPEC_Trend.md, SPEC_Economic_trend.md, SPEC_Carry.md, SPEC_Value.md. Code read: gm/config.py, book.py,
signals.py, panel.py, vol.py, daily.py (header), bloomberg.py, variants.py, protocol.py; metadata only from
tools/bbgq/engine_ref.json (market_months: counts of design months, used to date first return months) and
tools/bbgq/results/gm_bbg_map_v1.txt. No backtest, no market data, no 2011+ result.

## (a) Contradictions and gaps between register, notes and code

1. Value version 2's bond leg has already been seen. protocol_batch1.md V1 (variants.py bond_value_composite) ranked
   the same 7 bonds on the average of the real-yield rank and the 60-month yield rise, i.e. almost exactly the average
   of Value versions 1 and 2 for bonds (rejected, dSR about zero). Register T07 and 1.3b ("No gain is expected") do
   not say the measure was tested. It enters SPEC_Value s12 as an already-seen leg; trial count and hindsight flag: 3.4.
2. Register D7 and H3 settled from book.py: book.py:105 drops the commodity value signal and book.py:106 drops equity
   carry. Value holds no commodities, so card claims that Value bets against card 5 R1 (T34, C15) or holds "oil bought
   cheap" (T93) or a "neglected market" in commodities (T94) are not held (for 3.2 and Agent C).
3. Silent Bloomberg switches are wider than the register says. On the PC with Bloomberg loaded, gm_bbg_map_v1 reports
   the Value composite live for all 18 equity indexes (72 inputs used) and bloomberg.py EQ_INDEX maps eq_eu_stoxx50 to
   "MXEM Index" (MSCI Emerging Markets) and eq_us_ndx, eq_us_r2k to MSCI USA: a code defect. Carry's farthest-contract
   curve carry serves 0 markets today but switches on as tickers load. Both specs register the switches OFF; the engine
   has no flag yet (needs a registered engine change before A1).
4. Live source gap (rule 7): panel.py:368-370 says the OECD 3-month series for GB and the euro area end 2026-01 and are
   carried forward at most 12 months. They feed Carry (FX and bond carry), Economic trend (monetary theme for GB, which
   has no 2-year yield in code) and the excess returns of every GB and euro market. A replacement live source is needed
   before 2027-01. Not in the register.
5. As-of risk: CPI enters Economic trend and Value with a 1-month lag. If the OECD monthly series repeats quarterly
   values (AU, NZ in the design years), the lag reads a quarter before its release. Specs close it with a release-based
   rule, to register as an engine fix (like C1-C4). Unverified: needs a metadata check of the CPI file.
6. Register T01 says "62 ids, 61 distinct". After gm-1.2.2 the panel has 61 ids, all distinct, plus cm_aqr_ew
   (trend only to 2000-12). TESTING_PROTOCOL "62 markets" is to be corrected at 3.4 (gm_CHANGES says so).
7. Free-data coverage (from engine_ref market_months): single commodities start 2000-2004 except WTI (1985), natural gas
   and heating oil (1994), so before 2001 the commodity class of Trend is mostly cm_aqr_ew, Economic trend's commodity
   block is WTI alone until 1994, and Carry's version 2 holds nothing in commodities until a third EIA market has carry.
8. Signal and return sources differ for st_* notes: returns use central-bank yields then stooq (panel.py:503), signals
   use central-bank yields only (signals.py yield_of), so stooq-only months have a return but no carry, value or
   monetary signal. Minor; the builder reports such months.
9. Economic trend's monetary theme splices the 2-year yield onto the lagged 3-month rate (signals.py:214); a 12-month
   change across the splice start mixes two series. Minor; recorded.
10. Strip carry (T10) per unit of face value, as bond carry, puts strips near the bottom of the FI rank (the same
    scale effect already exists between 2-year notes and 30-year bonds; per-duration scaling was rejected as C1). If a
    strip is admitted, version 2 may hold it as a standing relative short. For 3.2.
11. Card 5's "no short while the front is above the second contract" was passed as a note for Trend and Value (register
    B18): it binds nothing in Value (no commodities) and is not imported into Trend (SPEC_Trend s15).
12. Weekly tranches are not built anywhere in gm/ (no tranche code). The specs close the offsets (0, 5, 10, 15 trading
    days); the weekly check still needs daily non-energy commodity data before 2000 (register D9).
13. No register-vs-note disagreement found for T01-T07, T09, T10, T12.
14. tools/check_ids.py silently skips ids with a letter suffix (for example QP08-C17-2b) and quotes broken across a
    line; the specs use neither in checked quotes (all quotes on one line, no suffix ids).

## (b) Items for step 3.4

| # | Item | Spec, section |
|---|---|---|
| 1 | Rule 5 reading for class B (Trend, Value v1, Carry energy) and mixed-leg Carry; Economic trend (C) to Incubator would remove 15% / 30% of the traded book | Trend s0; Econ s0, s5; Carry s0; Value s0 |
| 2 | Pod shares: config.py 30/30/20/15/5 (BASE) and 45/15/25/15/0 (CANDIDATE) against WORKFLOW 5.1 equal risk; BASE's 5% xsmom; incumbent for A2 | all s5; Trend s14 |
| 3 | Registered engine flags before A1: Bloomberg Value composite off, Bloomberg commodity curve carry off, alternative commodity columns off until D1 | Value s3; Carry s3; Trend s4 |
| 4 | Engine fix before A1: release-based lag for quarterly CPI (if the metadata check finds quarterly series) | Econ s3; Value s8 |
| 5 | Live replacement for GB and euro-area 3-month rates after 2026-01 | Econ s8; Carry s8 |
| 6 | Value version 2 bond leg already seen (V1): trial count and hindsight flag | Value s12, s15 |
| 7 | D1 extension to short-rate futures strips (T10): admission cost 8 bp, gross weight 0.25 / 1.9, strip carry formula | Carry s3, s5; Trend s13 |
| 8 | D3 reads sealed months: end its state months at 2009-12 | Trend s13 |
| 9 | Placebo for existing pods (Carry's directional bond leg) | Carry s10, s15 |
| 10 | X2 noise band; D5 power (9 of 12 months overlap) | Value s13; Econ s13 |
| 11 | Zero-slot shape report (five-state table, Fung-Hsieh factors 1994-2010) | Trend s13 |
| 12 | Live bands (W5) for every pod's stop conditions | all s11 |
| 13 | Hindsight knob counts: Trend 4 (+1 book), Economic trend 3 (+1), Carry 3 (+1), Value 3 (+1 seen leg) | all s12 |

For 3.2 to confirm: Trend s15 rules (no static vol version, equal class risk, written blend of carry), Carry s15
(equities out), Value s15 (commodities out), Economic trend s14 code facts against every card "held by Economic trend"
claim, Value s10 loss-event example.

## (c) check_ids results (tools/check_ids.py, final files)

- SPEC_Trend.md: ids cited 10, missing 0, quoted phrases checked 8: ALL IDS AND QUOTES OK
- SPEC_Economic_trend.md: ids cited 8, missing 0, quoted phrases checked 6: ALL IDS AND QUOTES OK
- SPEC_Carry.md: ids cited 7, missing 0, quoted phrases checked 8: ALL IDS AND QUOTES OK
- SPEC_Value.md: ids cited 9, missing 0, quoted phrases checked 7: ALL IDS AND QUOTES OK
