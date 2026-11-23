# Agent C notes (step 3.1, five card pods), 2026-11-23

Specs: SPEC_Card1_policy_liquidity.md, SPEC_Card2_regime_debt_cycle.md, SPEC_Card3_relative_value_risk.md,
SPEC_Card4_flows_volatility.md, SPEC_Card5_commodity_balances.md. Helper (mine): tools/check_all_quotes.py (also checks
"words", ID quotes written in the cards' comma style). Nothing registered or run; no market data read.

## (a) Contradictions and gaps between register, notes and code

1. Value holds no commodities in the book. gm/book.py family_positions keeps Value to fx_, bd_, eq_ ("commodity value:
   failed, out"), although signals.value_values computes a commodity 5-year reversal. This settles register D7 / H3, and
   makes card 5's and the register's "Value bets the other way" (T34) wrong for the code (card 5 spec s14).
2. Economic trend, re-checked in gm/signals.py: four themes, no growth (config.py econ_themes; ECON_THEMES). Inflation
   is HEADLINE CPI (OECD CPALTT01 yoy), not core. The monetary theme already holds card 3 R1's idea for currencies
   (local minus US 12-month change of the 2-year yield for US, DE, CA, AU, JP, else lagged 3-month rate; SIGNS FX +1)
   and shorts US equities after a 2-year yield rise (EQ -1), overlapping card 2 R2's trigger, contrary to card 2's text.
   The trade theme (minus log BIS NEER, EQ +1, FI -1) holds card 1 R5's stock leg and opposes its bond version. Growth
   items the cards drop as "held" (falling growth so long bonds; recession so short oil; China reopening; weak growth
   with hot inflation) are not held (register C1 confirmed).
3. Bloomberg switches touch card 5: gm/bloomberg.py ALT_COMMOD includes cm_cocoa, cm_alu, cm_zinc, cm_nickel, cm_lead,
   which enter the panel whenever Bloomberg returns load; with them, card 5 R1's own market rule would admit cocoa and
   LME metals. And carry_values adds Bloomberg curve carry for copper (CURVE_ROOT "HG"). Closed in the card 5 spec: R1's
   markets are those in the registered panel at 3.4 (copper, plus WTI in the crude version, while A1 keeps alternative
   commodities off).
4. Card 2 D1's country list: the Swiss and Swedish rates have no panel 10-year bond or stock index (panel.py BONDS,
   EQUITY); Australia has both but no rate on the card's list. Effective countries: US, JP, DE, GB, CA.
5. Card 1 R5's universe is five currencies (EUR as DE, JPY, GBP, AUD, CAD): the panel has no Swiss, New Zealand,
   Swedish or Norwegian stock index.
6. fx_eur before 1999: panel.fx_usd_value uses DEXUSEU (from 1999) then stooq eurusd; the code does not show that the
   pre-1999 months are the mark. Affects card 1 R5 and card 3 R1 (both say "mark then euro").
7. GS2 start is not on the data sheet (reader's recollection 1976-06). It sets the start of card 1 R2, card 3 R2 and R3,
   card 4 R5 (every version reads GS2).
8. Daily ^GSPC: gm/daily.py reads it (EQ_DAILY), but its first date is not confirmed (register D10). Card 4 spec closes
   the daily excess return as ^GSPC price return plus the panel's monthly carry part spread over trading days, and
   sets the start by a rule.
9. Card 3 R1's foreign 3-month rates (IR3TIB01) are research-only on the data sheet, with no live source; the card's
   splice to LSEG deposit rates before FRED starts makes R1's early history LSEG-dependent (LSEG not registered, D3).
10. Pre-futures panel commodity returns are World Bank monthly average spot (panel flag "spot avg"), which smooths
   returns (TESTING_PROTOCOL's warning); affects card 1 R4-B's basket and card 5 R1's copper P&L.
11. Card 3 C3-D1 still says "Core book" (register A, H4): cannot run before B1/B2 verdicts.
12. Card 4 C4-D1 reads 2011 prices for state months 2010-07 to 2010-12 (register D15); card 4's check did not cut it.
13. Card 3 R1's lag: the card's row gives "1 assumed" for all its rates, the data sheet gives TB3MS lag 0; closed as lag 1
   for all (card 3 spec s3).
14. Card 4 (reader's knowledge, not in the notes): listed S&P index options began in 1983, so R2 and R3 window 2 have no
   option-hedging mechanism in 1975-82; spec adds a reported split only.
15. Register T26 says card 3 R4's start is "confirmed by the digest" (1985) while card 3 says the start is not in its
   pack: no conflict of substance; spec uses the digest date.
16. Register "whether a panel return binds" (T34, A C5-D2): the card's final text binds it; note wins (card 5 spec s15).
17. Choices the notes left open and that I closed (flagged "closed here" for 3.2): first-published read as each month's
   first vintage; episode gap (new episode when the previous on-month is 12 or more months earlier); card 1 D2 and card
   4 D2 combination rules; card 1 R4-B as four equal-risk legs; card 1 R5 median set and price-change trigger; card 3 R2
   semiannual par durations and pair volatility; card 3 "fixed size" as fixed for an on-run; card 4 daily excess return
   and pro-rata roll cost; card 5 WTI as the crude, LSEG c1 as served, run-start real high; no trailing volatility
   rescaling of any rule or pod (a trailing scaler would lever up the on-months of an often-flat rule).

## (b) Items for 3.4 (spec, section)

1. Budget: five card rule layers against WORKFLOW's "at most 4" pods per B batch (register E); all specs s0/s5.
2. C3-D1 "Core book": proposal to read it as the registered systematic pods combined (sign of the incumbent book's net
   position), as card 1's check fixed its D2 (card 3 s13).
3. C4-D1 sealed months: proposal to end state months at 2010-06 (card 4 s13).
4. Date rules R1-R4 without weekly tranches against rule 2 (card 4 s3, s15); placebo design for date rules: proposal to
   move each window to a random start in the same year (R1, R3) or month (R2, R4), same length and sign rule (card 4 s15).
5. One duplicate threshold for all cards (80%, two thirds, 0.80/0.50, 0.80, 75% today; register C13): all specs s13.
6. Pod shares in the shadow book, book caps, netting across cards (register B19), and WORKFLOW 5.1 vs config.py
   CANDIDATE family_w and TESTING_PROTOCOL 45/25/15/15 (register F8): all specs s5.
7. Versions suggested by the checks but not added (brief: versions from notes and register only): card 1 no-tail
   version (s15 #2); card 2 R2 6-month window and 5x multiplier (s15 #1, #8); card 2 R1 long side (s15 #3); card 5
   per-class lag (s15 #1). 3.4 may register them before any run, as new versions.
8. C2-D1 (card 2) floor versions are counted in card 1's grid if the gate opens (+16, +32 with entry; card 1 s6,
   register C18).
9. Rule 5 for class B (card 4 R1, R2, R4: dated pattern, not his mechanism): card 4 s0.
10. Size of the analysts' registered live checkpoint (no note fixes it): all specs s10-s11.
11. LSEG registration: card 3 R1 history (splice) and R4, card 5 R1 prices, card 3 analyst Q2, card 5 analyst scoring
   (card 3 s8, card 5 s8).
12. Card 5 R1 market list fixed at registration (card 5 s3, s15).
13. Series starts and vintage coverage to record from the lock: GS2, TWEXMMTH, daily ^GSPC, IR3TIB01 and LSEG deposit
   rates, LSEG forward EPS, LSEG copper and WTI c1; ALFRED first dates for CPILFESL, M2SL, PCEPILFE, UNRATE (register D12,
   D14): card 1 s7-s8, card 3 s7-s8, card 4 s4, card 5 s4.

## (c) check_ids results (tools/check_ids.py; plus tools/check_all_quotes.py)

| Spec | check_ids | extra quote check |
|---|---|---|
| SPEC_Card1_policy_liquidity.md | ids 17, missing 0, quotes 8: ALL IDS AND QUOTES OK | 16 checked, 0 bad |
| SPEC_Card2_regime_debt_cycle.md | ids 10, missing 0, quotes 4: ALL IDS AND QUOTES OK | 8 checked, 0 bad |
| SPEC_Card3_relative_value_risk.md | ids 14, missing 0, quotes 6: ALL IDS AND QUOTES OK | 12 checked, 0 bad |
| SPEC_Card4_flows_volatility.md | ids 20, missing 0, quotes 5: ALL IDS AND QUOTES OK | 21 checked, 0 bad |
| SPEC_Card5_commodity_balances.md | ids 15, missing 0, quotes 5: ALL IDS AND QUOTES OK | 12 checked, 0 bad |
