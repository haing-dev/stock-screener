# LSEG contract identity: status 2026-11-25 (TESTING_PROTOCOL 7.10 item 3 step 2)

1. L11 (refreshed 2026-11-24; lock v2 94498c88): LSEG returns NO contract dates on this licence. All 12,736
   calendar requests failed: TR.ExpiryDate NULL / "unable to collect", TR.LastTradeDate "access to field(s) denied",
   eight other names "no output". Datastream LTDT invalid. What works: expired contracts' prices (HistoricalPricing
   "CLZ5^9", Datastream "<EDZ5^0>"), and TR.ExpiryDate as a dated series on CLc1 / GCc1 (2005-06).
2. So the calendar is computed from exchange rules (tools/lseg/lseg_rules.py) and checked against LSEG evidence
   (lseg_check_v3, lseg_ident_v1: sample contracts matched by value to the continuous positions).
3. Result on L11 samples (2005 contracts, daily around expiry): the rule last trading day equals the contract's last
   priced day for 16 of 17 roots (WTI one business day earlier: the day after Thanksgiving 2005 counts as a
   non-business day for the 25th rule). Each continuous c1 holds its contract through the last trading day (WTI: the
   rule day = its observed last day).
4. Far positions disagree: exchanges list only part of the cycle far out (WTI consecutive months then June/December;
   gold and grains likewise; Eurodollar and Euribor positions include serial months). Agreement: 100% NG, HO, SB; 92-99%
   C, W, KC, CT, PL; 85% CL; 60-92% metals, ED, FEI with serial variants; LC 50%. Not yet registrable (>= 99% needed).
5. Next: L12 (G:\My Drive\Screener project\LSEG\09_contract_identity\L12_identity_evidence.xlsx, 188 formulas) gives
   TR.ExpiryDate history on c1 / c2 / deepest position for 17 roots, four eras of daily samples per root, serial-month
   samples, two over-life samples per root, and Euribor / short sterling / Euroswiss contracts 3-8 daily. Then: a
   listing-horizon rule per root (fit by value matching, an identity fact, not a performance choice), or, if
   TR.ExpiryDate history works at depth, identity read directly per observation (L13 for the other positions).

## Update 2026-11-25 (L12 read; fits v3, v4)
6. L12 (lock v3 5173fe86): TR.ExpiryDate works as a dated monthly series on c1 and c2 for every HistoricalPricing
   root over the full history (format YYYYMMDD; empty for deeper positions and platinum). So positions 1-2 are
   identified per observation from LSEG itself (CL 318 of 319 months match the rule calendar; LCO 250/250; NG 185/185;
   HO 362/364; GC 368/369 with serial months; KC, W, S 100%).
7. Last trading day by era (ident v3 LT): rules match from ~1995-2000 on; earlier the exchanges used other rules
   (grains +3..+6 business days, cattle -5..-8, natural gas -3..-6). Observed expiries replace the rule wherever a
   contract passed through c1/c2.
8. Listing-rule fit (ident v4, cleaned of chance price matches): NG 100%, GC 100%, KC 100%, HO 99.5% at every depth;
   CL 98.7%, LCO 98.6%, CT 98.4%; HG 96.9%, W 96.0%, S 95.0%, SI 94.5%, C 94.1%, PL 92.1%, LC 88.7%, SB 85.4%, FEI
   87.1%, ED 78.0%. One rule per root cannot reach 99% for most roots (listings changed over time).
9. DECISION (identity method, not a performance choice): use contract-level prices where identity beyond position 2
   is needed (Curve carry legs, strip contracts 1-8). Files L13a (energy, metals: 200 formulas), L13b (grains,
   softs, cattle: 182), L13c (ED, Euribor, SOFR, SONIA quarterly contracts daily: 49) in
   G:\My Drive\Screener project\LSEG\09_contract_identity (builder tools/lseg/build_lseg_l13.py; Datastream
   multi-code form). Short sterling and Euroswiss have no expired-contract codes on LSEG: their strips cannot be
   identified (they hold nothing in Strip reversion unless another source appears). Gasoline before 2006 (HU) is
   not on LSEG.
10. L13a-c were too large for LSEG to load at once (user 2026-11-25) -> replaced by twelve small files L14a-L14l
   (builder tools/lseg/build_lseg_l14.py; <= 360 monthly or 60 daily contract series per file; one delivery year
   per formula). Changes: design deliveries only (to 2012; holdout-year contracts pulled after the freeze); NG, HO,
   GC, KC not pulled (listing rule >= 99.5% at every depth: their legs come from the continuous series). The old
   L13 templates are deleted on the PC by job delete_l13_templates_20261125.
