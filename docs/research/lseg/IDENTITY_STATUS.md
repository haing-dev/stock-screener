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
