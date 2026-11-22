# LSEG measures check on the first stage-B file (2026-11-22)

What was run: `tools/equity/lseg/read_stage_b.py` on `04_accounts/LSEG_accounts_Q2_v1.xlsx` (quarterly first-reported
accounts, companies 851-1700 of the 5,065), then `tools/equity/lseg/lseg_adapter.py`, which feeds the same formulas
as the WRDS engine (`eq_ref.quarterly_table` and `account_measures`; FIELD_DICTIONARY_v1.0 part 1). Levels only; no
return computed.

## Result
- 60,115 company-quarters, 752 of the 850 companies with data, period ends 1982-2026 (80 quarters back from each
  company's latest, so companies that died early reach back further).
- Original announcement date present for 72% of quarters (median 35 days after the period end; 95% within 89 days);
  the rest use the 45-day rule.
- Coverage of the account measures among companies with known accounts at December: about 60% in 2010, 70% in 2015,
  80% in 2020, 90-95% from 2022. Cause: about a third of the 2010 quarter rows carry a period end but no values
  (first-reported values are thinner in early years). The WRDS form (Compustat) fills these years; the comparison
  goes into Batch 0.
- Pooled 2010-2025 levels look sane: ROE median 9.0% (10th / 90th percentile -33% / 31%), accruals median -4.9% of
  assets, Piotroski median 5.6 (distribution centred on 5-6, few 0-1 and 9), earnings yield median 4.8%, book to
  price median 0.39.

## Problems found and what was done
1. Quarterly cash flow from operations (TR.F.NetCashFlowOp, FQ) is one quarter, not year to date. The engine now
   accepts a one-quarter column (eq_ref 1.0.1, registered before any run).
2. **The monthly file's close is split-adjusted to today's basis while shares are as reported** (Apple 2009: close
   x shares = 1/28 of the true market value; Nvidia 1/40). So close x shares and the $5 price floor (R3) would be
   wrong before splits; company market value (TR.CompanyMarketCap) is right. Fix: file 12
   `12_LSEG_monthly_unadjusted_close_v3.xlsx` (close as traded, Adjusted=0, all 5,537 lines, with a check block)
   added to `07_stageB_v3`; until it is loaded, measures use company market value. Dollar volume uses the adjusted
   close with the (adjusted) volume, so the adjustments cancel.
3. The monthly panel repeats some line-months (5,804 groups, 1,095 with differing values): the adapter keeps the row
   with the latest date in the month.
4. Shares in the quarterly accounts are as reported, so the Piotroski share signal needs a split factor; it comes
   from file 12 (unadjusted / adjusted close). Not applied yet.
