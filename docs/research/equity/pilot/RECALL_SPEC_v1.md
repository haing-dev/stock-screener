# Recall test spec v1 (gate G8; V04_REGISTRATION A10 item 9 + A13 item 13), 2026-11-27

Written BEFORE any recall number exists. Seal-exempt job 9 `recall` (module tools/equity/wrds/eq_recall.py), runs on
WRDS; prints counts and ratios only (no company, no row, no investor id beyond the masked label). Reads no forward
return; reads prices only up to each quarter-end t (P2, P3 of the recipe).

## Inputs (all on WRDS)
- Conviction purchases: data set `eq_conv_panel` (eq_conv_v2, A6; R2 definition, both versions: (a) new position or
  addition into the five largest weights, (b) new position or addition to >= 1% of the portfolio). A purchase in
  quarter q is evaluated at the quarter-end t BEFORE q.
- Universe at t: the R3 universe (1,500 largest US common stocks by market value, price >= $5, median daily dollar
  volume >= $2m), as eq_ref builds it (CFG of eq_ref), with GICS sector from history (comp.co_hgic), sector known.
- Accounts: Compustat annual (comp.funda, INDL/STD/D/C) known at t: a fiscal year counts only if its datadate is at
  least 90 days before t (stand-in for first-reported: Compustat values are as restated; A8 WRDS-form difference).
  Quarterly items (TTM) from comp.fundq with rdq <= t (or datadate + 45 days when rdq is missing), as eq_ref.
- 10-year US Treasury yield at t: frb.rates_daily (or the nearest WRDS FRB table; constant maturity 10y), last value
  on or before t. If WRDS has no such table the job stops and says so.
- Prices: crsp.msf_v2 month-ends up to t.

## Recipe (Kantesaria v1, decisive form; pilot/recipe/RECIPE_v1.md sections 1-3)
Entry = all of B1-B6 AND P1 AND (P2 OR P3) AND none of A1-A5. Measures exactly as RECIPE_v1 states; "universe
median" = median over the whole eligible universe at t BEFORE the exclusions; a missing measure fails its criterion.
GICS codes for A1-A4 exactly as listed (sector 35; group 4520; industry 151040; sectors 10, 15; sub-industry
30202010; sectors 55, 60; group 4010 incl. 40102010; group 4040; sub-industries 40201050, 40202010, 40204010).
Insurance (group 4030) is excluded by the house rule (A8 2a) in every pod, recipe or not.
(Amended 2026-11-28: the house exclusions, insurance included, do not apply where a registered recipe says so:
pilecki_v1, nygren_v1 and, from 1.1.1, lilu_v1; V04_REGISTRATION A13 items 21-22.)
The full form (B7-B11, P4, A6-A9 versions) is computed and REPORTED only.

## Statistics (A10 item 9)
- Purchases counted: conviction purchases 2010-2025 of the investor (filer 14460) whose stock was in the eligible
  universe at t. Fewer than 20: "not measurable".
- Recall = share of counted purchases that pass the entry at t.
- Base rate = pass rate of the eligible stocks at the same t, same GICS sector and same size third (thirds of market
  value inside sector and t), weighted as the purchases are (each purchase gets the pass rate of its cell).
- Lift = recall / base rate. 90% interval: bootstrap of quarters (2,000 draws, seed 20261127): draw quarters with
  replacement, recompute recall and base rate on the purchases of the drawn quarters.
- Pass (gate): lift >= 2.0 AND interval lower end > 1.25 AND recall >= 25% AND lift above both baselines.
- Baselines: (1) the same recipe on the pooled control investors' purchases (eq_conv_panel group control); (2) the
  reference-book screen (top fifth of the eq_ref book score inside sector at t) on this investor's purchases.
- Per criterion: share of the counted purchases it rejects (no names). Cross table: this recipe on every roster and
  control investor's purchases (lift only, masked labels as in saydo).
- Version: decisive form decides; full-form versions reported (averaged where the recipe says averaged).
- Labels carried into every result: "held-out failed", "recipe covers 7 of 22 buy rules (decisive)".

## One revision round
After the result, the recipe writer sees recall, base rate, lift and the per-criterion rejection shares only (A10
item 9). One revised recipe, every change citing a quote; both results logged.
