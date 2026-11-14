# The two proposals the charter deferred to this note (verbatim from the foundation notes; their numbers are UNVERIFIED)

## U01-T4
T4. Short-rate futures universe, already in Batch 2 (TESTING_PROTOCOL.md:80-81): the paper raises its prior (fixed
income 0.84, short-rate futures 0.37-0.70, C07-1, C07-2). Rule unchanged; monetary theme with the Exhibit 1 FI sign.
Caution: our synthetic US 3-month market S1 lost 0.015 (protocol_batch1.md:8); costs and a 1990s-only window may
bind. No new slot.

## U05-T5
T5. Spread vol gate as a precondition, and the no-test list (zero slot). If the three built spreads (panel.py:353) are
ever traded, they enter only with his gate: a position is allowed when trailing 3-month spread vol exceeds a fixed
fraction of average leg vol (he gives 2% dormant, 10% tradeable, MT073-C06-4, C07-1; fixed at registration), sized on
current spread vol, zero otherwise; never through the 36-month unit-vol block (book.py:190-193), his constant-risk trap
(MT073-C04-5, C05-1). A one-off look at the three spreads' vol ratio over the design period decides whether to register
them at all. No test, not worth a slot: patient execution and play-forward (U02-T2/T3, U04-T1 cover them; our data say
the fast leg loses with delay); class-specific rules (Carver's pooled evidence, U02 row 12, and his own "signal is a
commodity"); 0DTE conditioning (2012+, holdout era); the 50/50 allocator mix; PCA bond trend with middle factors
overweighted (MT073-C08-2: needs Batch 2 zero curves, a new family not a tweak); single-stock futures, compute curves,
narrative momentum (out of scope); the COT crowding regression (a free monitor, gap_review_crosscheck:41, not a rule);
trend-conditional vol (MT205-C10-3), one extra regressor in U04-T2 at no cost.
