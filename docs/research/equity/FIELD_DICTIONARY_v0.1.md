# Field dictionary v0.1 (draft, 2026-11-20)

Plan v0.4 step 2. The list of measures every screen and the tracker will use, so that companies compare like for
like. Draft: version 1.0 (exact formulas with the LSEG field names that test file 2 confirms) is registered before
Batch 0 (`V04_REGISTRATION.md` R7).

- Measures: `field_dictionary_v0.1.csv` (67: valuation 14, profitability 9, stability 5, growth 8, capital use 6,
  balance sheet 6, expectations 5, price 5, size and liquidity 3, ownership 5, classification 1), each with its
  definition, raw inputs and the roster investors whose stated criteria need it.
- Raw items: `field_dictionary_raw_v0.1.csv` (52 account items, each with a first LSEG field name and alternates;
  cited = the name appears in a public source, guess = to be shown by the test file).

Rules that hold for every measure:
1. As known on the day: accounts as first reported (`ReportingState=Orig`), usable from the original announcement
   date plus one trading day; if the date is missing, period end plus 90 days (annual) or 45 days (quarterly).
2. Flows are sums of the last four reported quarters; stocks are the latest reported quarter; averages use the
   balance a year earlier.
3. Ratios with a denominator at or below zero are missing, not negative.
4. Every measure is ranked inside the GICS sector at each month-end (0 to 1); screens state thresholds either as a
   level (the investor's own number) or as a rank; both are versions.
5. A missing measure takes the sector median rank; a stock missing more than half of a pod's measures is not ranked.
6. Banks, insurers and real estate need their own measures (book value, tangible book, deposits, combined ratio);
   they are added with the financials pod (Pilecki), not in v1.0.

Not yet covered, by design: sector data (semiconductor market share, drilling inventory, recurring-revenue
share), event data (spin-offs), moat and management judgements. They belong to the analyst notes.

Test file 2 (`docs/data_requests/lseg_equity_probe2_2026-11-20/LSEG_equity_probe_v2.xlsx`, builder
`build_lseg_equity_probe2.py`, 184 formulas, reader job `tools/bbgq/jobs/lseg_eq_probe_v2.py`) answers:
which field name returns each raw item; quarterly and dated forms across many companies in one formula; the US
company list with companies that died 2010-2025, identifiers, sector, past market value; estimates, returns,
short interest and ownership across companies; how many companies x fields x years one formula carries.
