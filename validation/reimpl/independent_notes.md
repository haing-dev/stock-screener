# Independent re-implementation of the Fortress screen: notes

Inputs used: only `validation/reimpl/fortress_rules.md` and `tests/real_samples/*companyfacts_subset.json.gz`
(38 files). Code: `/tmp/reimpl_agent/fortress.py` (standard library only), sensitivity checks in
`/tmp/reimpl_agent/sens.py`. Output: `validation/reimpl/independent_fortress.csv`.

Result as of 2026-10-01: **PASS 2** (cost, v), **PASS\* 7** (aapl26, aapl, adp, fix, nvs, tsm26, tsm),
**FAIL 29**.

## A. General data handling (applies to every rule)

1. **Point in time.** A fact is used only if `filed < 2026-10-01`. Nothing else is filtered by date.
2. **Annual facts only.** Only facts from forms 10-K, 10-K/A, 20-F, 20-F/A, 40-F, 40-F/A are used for the
   financial rules. The 10-Q facts are ignored. *Ambiguity:* the rules never say whether TTM/quarterly data
   may be used for "latest" values (F3, F9-F11). I used the latest fiscal year only.
3. **What counts as an annual value.** A duration fact counts as a fiscal-year value only if `end - start` is
   340-390 days. That covers 52/53-week years and drops quarters and transition periods that appear inside 10-Ks.
   Balance-sheet (instant) values are read at the fiscal-year end date (±10 days).
4. **Restatements.** For each (tag, period), the value from the **latest filing before the evaluation date**
   wins. So restated and recast comparatives replace the originally reported figures. *Ambiguity:* the text
   doesn't say whether "as first reported" or "as restated" is meant. Restated data makes the YoY comparisons in
   F4/F5 consistent. As-first-reported data is the purer point-in-time choice.
5. **Fiscal years.** The set of fiscal years is the set of distinct end dates of annual revenue / operating
   income / net income / operating-cash-flow facts. A fiscal year is identified by its end date. The fiscal
   `fy`/`fp` fields of the facts are NOT used, because they describe the filing, not the period.
6. **Fiscal-year label** (needed for "2021-23" in F13). I used the Compustat convention: a fiscal year ending in
   January-May belongs to the previous calendar year. Example: TJX's year ending 29 Jan 2022 is fiscal 2021, and
   J&J's 52-week year ending 2 Jan 2022 is fiscal 2021.
7. **Currency.** For each company, the reporting currency is the unit used by most annual revenue/income/cash-flow
   facts: TWD for TSM, BRL for ABEV, EUR for ASML, USD for the others. Ratios are computed in that currency.
   The size test (F3) is converted at fixed approximate rates (EUR 1.10, BRL 0.19, TWD 0.031 USD), because no
   FX source is available offline. *Underspecified:* the rules give no FX source or date.
8. **Taxonomies.** us-gaap and ifrs-full tags are merged into one namespace and handled with the priority lists
   below. `dei` facts count only toward F2 (they show that an annual report was filed).

### Line-item definitions (my choices; none are given in the rules)

| Item | Definition / tag priority |
| --- | --- |
| Revenue | First positive value in the order Revenues, RevenueFromContractWithCustomerExcludingAssessedTax, SalesRevenueNet, RevenueFromContractWithCustomerIncludingAssessedTax, ifrs Revenue, ifrs RevenueFromContractsWithCustomers. A value is skipped if it is less than 50% of the largest revenue-tag value that year. Fallback: SalesRevenueGoodsNet + SalesRevenueServicesNet, then a zero value if that is all there is. |
| Operating income (OI) | OperatingIncomeLoss / ifrs ProfitLossFromOperatingActivities. **Per-year fallback (EBIT proxy):** pre-tax income (IncomeLossFromContinuingOperationsBeforeIncomeTaxes...NoncontrollingInterest, ...MinorityInterestAndIncomeLossFromEquityMethodInvestments, ifrs ProfitLossBeforeTax) + interest expense (0 if untagged). The proxy is used everywhere except F5, where the text prescribes net income instead. |
| Net income | NetIncomeLoss, ProfitLoss, ifrs ProfitLossAttributableToOwnersOfParent |
| Interest expense | InterestExpense, InterestExpenseNonoperating, InterestExpenseDebt, ifrs FinanceCosts. Fallback: InterestPaidNet / InterestPaid (cash interest). |
| D&A | DepreciationDepletionAndAmortization, DepreciationAndAmortization, DepreciationAmortizationAndAccretionNet, Depreciation |
| FCF | Operating cash flow (NetCashProvidedByUsedInOperatingActivities[ContinuingOperations], ifrs CashFlowsFromUsedInOperatingActivities) minus PP&E capex (PaymentsToAcquirePropertyPlantAndEquipment, PaymentsToAcquireProductiveAssets, ...OilAndGasPropertyAndEquipment, ...OtherPropertyPlantAndEquipment, ifrs PurchaseOfPropertyPlantAndEquipment...). Capitalized software, intangibles and acquisitions are excluded. If capex is missing for a year, FCF is unknown for that year (it is not assumed to be zero). |
| Total debt | IFRS: Borrowings, else LongtermBorrowings + current borrowings. US GAAP: DebtLongtermAndShorttermCombinedAmount; else noncurrent LTD (LongTermDebtNoncurrent / LongTermDebtAndCapitalLeaseObligations) + DebtCurrent (or current LTD + ShortTermBorrowings + CommercialPaper); else LongTermDebt + ShortTermBorrowings + CommercialPaper; else the sum of miscellaneous debt tags (NotesPayable, LineOfCredit, SecuredDebt, ...). **If a balance sheet exists but no debt tag does, debt = 0.** Operating leases are excluded. Finance leases are included only where the tag combines them with debt. |
| Cash | CashAndCashEquivalentsAtCarryingValue, ifrs CashAndCashEquivalents, Cash, then CashCashEquivalentsRestrictedCash... |
| Liquid assets | Cash + short-term investments (ShortTermInvestments / MarketableSecuritiesCurrent / AFS debt current / ifrs short-term deposits / CurrentInvestments), or CashCashEquivalentsAndShortTermInvestments if tagged. |
| Equity | Total equity including NCI (StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest, ifrs Equity), else StockholdersEquity |

## B. Rule by rule

**F1 History (>= 9 years of data).** This counts the distinct fiscal years that have an annual revenue, OI,
net income or operating-cash-flow value, including comparatives (a 2009 10-K adds 2007 and 2008). No continuity
is required. *Ambiguous:* "years of data" could mean years of filings, calendar span, consecutive years, or
years with a specific item. It could also mean years of price history, since the "why" says "including 2020".
Files with no financial facts (cni: dei only; xomh: 10-Q only) get 0 years, which is FAIL rather than NO DATA.

**F2 Recent report (<= 1.6 years since last annual report).** This uses the age of the latest *filing date* of an
original 10-K/20-F/40-F (amendments excluded), including dei-only facts. *Ambiguous and outcome-changing:* the
alternative is the age of the latest fiscal *period end* with financial data. That flips three files: tsm26
(filed 0.46y ago, but its 2026 20-F has only a dei fact, so the latest financial period is 1.75y old), tsm
(1.46 vs 1.75) and snow (1.53 vs 1.66). The "why" text ("latest annual report within ~1.5 years") does not
settle whether the 1.6 is a hard limit or 1.5 plus slack. Files with no annual-form fact (xomh) get NO DATA.

**F3 Size (>= $500M revenue).** This uses latest-fiscal-year revenue converted to USD. *Underspecified:* annual
vs TTM, FX source, and which revenue tag. Revenue-tag choice really matters elsewhere (see section C). MTH and
NVS have no revenue tag in the subset, so they get NO DATA. ALLO tags revenue of about 0, so it gets FAIL.

**F4 Held up in 2020.** The window is fiscal years whose end date falls in 2020-03-01..2021-06-30 (calendar
months, no tolerance). Each year is compared with the fiscal year ending 330-400 days earlier. Every year in the
window must pass. This is equivalent to "the worst year", evaluated **separately for revenue and OI**.
- *Ambiguity:* "worst fiscal year" could mean picking one year (the one with the worst revenue or the worst OI)
  and testing both metrics on it. With at most two years in the window, that matters only if the two metrics
  have their worst in different years. That did not happen here.
- If prior OI <= 0, a % change is undefined. I treat a decline from a non-positive base as FAIL and an
  improvement as PASS (snow and allo fail this way).
- The rule gives no fallback. If revenue or OI cannot be computed, the result is NO DATA (mth, nvs: revenue
  missing) unless the other metric already fails. *Underspecified:* F5 has a net-income fallback and F4 does not.
  Was that intentional?
- A company younger than 2020 (alab, sndk) gets NO DATA. The text gives no N/A option here, unlike F5.

**F5 Held up in 2009.** The window is fiscal years ending 2008-09-01..2010-03-31 (no tolerance). Thresholds:
revenue >= -10%, OI >= -25%, and an OI loss in any window year fails.
- **NI fallback:** applied per year. If OI for the year or its prior year is not tagged, net income is used
  with the OI thresholds (-25% and loss = fail). *Underspecified:* the fallback threshold for net income is not
  stated. It is also unclear whether "revenue/operating income aren't in XBRL" means either one missing or both.
  If only revenue is missing, I test only the profit measure.
- **No data versus N/A:** "younger than the recession" can't be read from companyfacts, which contains no
  incorporation or IPO date. My proxy: N/A if the company files **10-Ks** and its first fiscal year in the data
  ends after 2010-03-31. US filers' first XBRL 10-Ks normally carry 2008-09 comparatives, so a later start means
  the company was not public then (alab, allo, sndk, snow, veev). For **20-F/40-F filers** (abev, nvs, tsm),
  IFRS XBRL starts years later regardless of age, so they get NO DATA ("check manually"). This choice alone
  turns tsm/tsm26 from PASS into PASS\*.
- A window year whose prior year is missing (ait: FY Jun-2009 is the first year in XBRL; fix: FY2009 is the
  first) gets NO DATA unless something fails.
- *Edge case:* Costco's year ending 31 Aug 2008 (a 52/53-week year) sits just outside "Sep-2008". With a ±7-day
  tolerance it would be included. That changes Costco's detail but not its result.

**F6 Never lost money (0 operating-loss years in 10).** This uses the 10 most recent fiscal years, counting the
years with OI < 0. Missing years are skipped; a short history is F1's problem. NO DATA only if no OI is
available (rrc, which has neither OI nor a pre-tax income tag in the subset). *Ambiguous:* "in 10" could mean
the last 10 fiscal years or the last 10 years with data. If fewer than 10 are available, is it a pass, or
"couldn't check"?

**F7 Stable margins (std. dev. of operating margin <= 5).** This is the **sample** standard deviation (n-1) of
OI/revenue in **percentage points** over the last 10 fiscal years. At least 3 years are required.
- *Ambiguous:* sample vs population std. jnj flips: 5.01 (sample, FAIL) vs 4.75 (population, PASS).
- "5% swing" could also be read as max-min range, or as std relative to the mean margin (coefficient of
  variation). Those readings would give very different results.
- jnj, adp and dhi have no OperatingIncomeLoss for the last 10 years, so their margins use the EBIT proxy
  (pre-tax + interest). jnj's 5.01 includes litigation and gain items that a reported OI would not, so its
  FAIL depends on the proxy.

**F8 Decent returns (median ROIC >= 10% over 10 years).** ROIC = NOPAT / average invested capital.
- NOPAT = OI x (1 - effective tax rate). The tax rate is income tax / pre-tax income clipped to 0-50%, or 21%
  when pre-tax income is <= 0 or missing.
- Invested capital = total equity + total debt - liquid assets (cash + ST investments), averaged over the
  opening and closing balance sheets (closing only if the opening one is missing).
- Years with invested capital <= 0 are skipped. The median is taken over the last 10 fiscal years with a value,
  and at least 3 are required.
- *Fully underspecified:* the rules give no ROIC formula at all. Choices include pre- vs post-tax, statutory vs
  effective tax, whether to subtract cash, goodwill in or out, average vs ending capital, and how to treat
  negative capital (buyback-heavy firms such as MCO and SPGI give ROIC near 100% or more). The only borderline
  case here is fls (8.5%), with nvs (11.1%) and intc (12.2%) close.

**F9 Leverage (net debt / EBITDA <= 2.0).** Latest fiscal year: (total debt - liquid assets) / (OI + D&A).
- Net cash (net debt <= 0) passes. Net debt > 0 with EBITDA <= 0 fails.
- When D&A is not tagged (all IFRS filers in this subset, msft, veev, and intc's latest year), EBITDA = OI,
  which understates it. A ratio <= 2 is then still a verified pass, but a ratio > 2 is NO DATA rather than
  FAIL (intc).
- *Underspecified:* gross or net cash (cash only, or including marketable securities); leases; latest year or
  TTM; and EBITDA from reported vs adjusted OI. No file flipped between cash-only and cash+STI. Borderline:
  hsy 2.30 and ko 2.37 (FAIL), pool 1.76.
- The "no debt tags means debt = 0" choice matters for mth. Meritage surely has senior notes, but they are not
  under any tag in the subset, so mth passes F9-F11 on an assumption.

**F10 Interest coverage (EBIT / interest >= 6).** Latest fiscal year: OI / interest expense, falling back to
cash interest paid.
- No interest tag at all and debt = 0 gives PASS (inf). Interest expense tagged as 0 gives PASS (mth, where
  homebuilder interest is capitalized). Debt > 0 with no interest figure gives NO DATA.
- Affected NO DATA cases: aapl and aapl26 (Apple stopped tagging InterestExpense after FY2023; this is their
  only open rule), dhi, mco, odfl, tol.
- *Underspecified:* which interest line (gross interest expense vs net, IFRS FinanceCosts, which also includes
  lease and other finance costs, or cash interest). abev is FAIL on FinanceCosts (5.3x) but would pass on cash
  interest paid (26.3x). Also unspecified: whether capitalized interest counts, and what "at today's rates"
  means in the "why". It hints at re-pricing debt at current market rates, which the rule text does not ask for.

**F11 Refinancing (debt due within 2 years <= cash + 2 years of FCF).**
- Debt due = LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths + ...InYearTwo + ShortTermBorrowings
  + CommercialPaper (latest fiscal year).
- Capacity = liquid assets + 2 x latest-year FCF. A negative FCF reduces capacity.
- Without a maturity schedule, I use bounds: PASS if total debt <= capacity; FAIL if current debt alone exceeds
  capacity; otherwise NO DATA (ko, fico, spgi, intc). Also NO DATA when FCF can't be computed (adp: no capex
  tag in the subset).
- *Underspecified:* whether "2 years of FCF" means 2 x latest FCF, 2 x average FCF or a forecast; whether cash
  includes marketable securities; whether revolver capacity counts; and how to treat the maturity schedule
  (which excludes commercial paper and short-term borrowings, so I added them).

**F12 Cash every year (<= 1 negative-FCF year).** This counts negative-FCF years among the last 10 fiscal years
with FCF computable. FAIL as soon as 2 or more are negative. PASS requires at least 3 computable years, else
NO DATA (adp has no capex tag). *Underspecified:* the window (the text gives none; I assumed the 10 years used
by F6/F7), the FCF definition (capex only vs including capitalized software and intangibles), and the treatment
of missing years. veev has only 4 computable years because its capex tag is sparse; it passes on those.

**F13 Inflation test (margin change 2021-23 >= -2%).** Operating margin in fiscal 2023 minus fiscal 2021 (labels
as in A.6), in **percentage points**.
- *Highly ambiguous:* "-2% change in margin" could be percentage points (my reading) or a relative change of the
  margin. Under the relative reading, cost (-0.07pp = -2.2%), dhi (-1.48pp = -7.7%), ko (-1.95pp = -7.3%) and
  lrcx (-0.95pp = -3.1%) would FAIL instead of PASS.
- *Also ambiguous:* which fiscal years count as "2021" and "2023". jnj flips: -6.0pp under the Compustat label
  (FAIL) vs -1.63pp if a year is labelled by the calendar year of its end date (PASS; that mislabels its 52-week
  year ending 3 Jan 2021 as 2021).
- Further open questions: whether the start point is 2021, or 2020/2022 as the inflation start; whether the
  margin is operating, gross or EBITDA; and point-to-point vs average.
- The worst-hit names are spgi (-18.7pp, merger with IHS Markit), mco (-9.6pp), veev (-9.2pp) and asml (-3.5pp).

**Classification.** PASS = all 13 rules PASS (N/A counts as pass). PASS\* = no FAIL, at least one NO DATA.
FAIL = any FAIL. "Check manually" (F5) is treated as NO DATA. *Underspecified:* the rules don't say whether N/A
is neutral or makes the result PASS\*. I treated it as neutral. They also don't say whether some rules are
"defining", so that NO DATA on them would block a pass.

## C. Data quirks found that any implementation must handle (and the rules don't mention)

- **FLS** tags `Revenues` = 0 every year; it must be skipped, or F3/F7/F13 break.
- **AIT** FY2011 `Revenues` = $17.7M (a sub-item) against $2.4B net sales.
- **MA**: `RevenueFromContractWithCustomerExcludingAssessedTax` (2018-21) is gross revenue before rebates
  ($21.8B vs net $15.0B). Taking the largest revenue tag makes F7 FAIL (std 10.5); taking `Revenues` first gives
  PASS (std 2.6). **The revenue-tag order is outcome-changing** and is not specified.
- **TJX** stopped tagging OperatingIncomeLoss after FY2018 and `Revenues` after FY2014. jnj stopped tagging
  OperatingIncomeLoss after 2014, and adp, dhi and rrc never tag it. Without a per-year fallback, F6-F10/F13
  become NO DATA for these names. rrc has no pre-tax income tag either.
- **MTH, NVS** have no revenue tag at all in the subset. **CNI** has only dei facts, and **XOMH** only 10-Q facts.
- **Apple** stopped tagging interest expense after FY2023, so F10 can't be checked for the latest year.
- **tsm26** has a 2026 20-F in the subset with only a dei fact. Its financials therefore end at FY2024 while the
  report itself is recent (see F2).
- Missing debt tags (mth, veev, alab, allo, snow): with debt-free = 0 these pass F9-F11. With "no data", they
  would be PASS\*/NO DATA.

## D. Most important ambiguities (ranked by how often they change a result here)

1. F13 unit (percentage points vs relative %) and the 2021/2023 fiscal-year mapping. These flip cost, dhi, ko,
   lrcx and jnj.
2. Revenue tag choice and the operating-income fallback. These flip ma F7 and drive jnj F7, plus F6-F13 for
   adp, dhi, tjx and rrc.
3. F5 "younger than the recession" for foreign filers whose XBRL starts after 2010. This decides PASS vs PASS\*
   for tsm/tsm26.
4. F2 filed date vs period end. This flips tsm, tsm26 and snow.
5. Interest definition in F10. This flips abev and makes aapl PASS\* rather than PASS.
6. F7 sample vs population std. This flips jnj.
7. ROIC, EBITDA, net debt, "2 years of FCF" and capex definitions are entirely unspecified. Few borderline flips
   occurred here, but a different implementation could easily differ for fls, hsy, ko and pool.
8. NO DATA vs FAIL vs N/A when a component is missing (F4 without revenue, F9 without D&A, F11 without a
   maturity schedule, debt with no tags). These conventions determine most PASS\* outcomes.
