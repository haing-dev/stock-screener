# Fortress screen - the written rules

These are the rules exactly as the website states them (rule text, what is measured, why). Implement them from this
text and the raw data only. Evaluation date: **2026-10-01** (use only facts filed before that date).

Purpose: Recession-proof earnings, stable margins and strong balance sheets. Lower returns than Core; resilience is the point.

| Rule | Name | Rule as written | Why |
| --- | --- | --- | --- |
| F1 | History | at least 9 years of data | A long record, including 2020. |
| F2 | Recent report | at most 1.6 years since the last annual report | Data must be current (latest annual report within ~1.5 years). |
| F3 | Size | at least $500M revenue | Big enough to own; small filers have patchier data. |
| F4 | Held up in 2020 | worst fiscal year ending Mar-2020..Jun-2021 vs prior year: revenue >= -5%, operating income >= -15% | Earnings that hold up in a recession protect the stock. |
| F5 | Held up in 2009 | fiscal years ending Sep-2008..Mar-2010: revenue >= -10%, operating income >= -25%; an operating loss in the window fails; net income is the fallback when revenue/operating income aren't in XBRL; no data = 'check manually' unless the company is younger than the recession (N/A) | The same test for 2008-09; an operating loss in a recession year fails. |
| F6 | Never lost money | at most 0 operating-loss years in 10 | Fortress businesses don't post operating losses. |
| F7 | Stable margins | at most 5% swing in operating margin (std. dev.) | Stable margins over 10 years signal a predictable business. |
| F8 | Decent returns | at least 10% ROIC, 10-year median | Set below Core so asset-heavy toll collectors such as rail and waste qualify. |
| F9 | Leverage | at most 2.0× (net debt / EBITDA) | Survive first: leverage that can't be refinanced breaks companies. |
| F10 | Interest coverage | at least 6.0× (EBIT / interest) | Debt rolls over at today's rates; coverage must hold at them. |
| F11 | Refinancing | debt due within 2 years <= cash + 2 years of FCF | Maturities larger than cash can cause a liquidity crisis. |
| F12 | Cash every year | at most 1 year(s) with negative FCF | Positive free cash flow almost every year. |
| F13 | Inflation test | at least -2% change in margin 2021-23 | Margins that held through 2021-23 inflation show pricing power. |

Classification of a company:
- **PASS**: every rule passes.
- **PASS*** (starred): no rule fails, but at least one couldn't be checked (missing data).
- **FAIL**: at least one rule fails.

Data: `tests/real_samples/*companyfacts_subset.json.gz` - SEC XBRL 'companyfacts' JSON (structure: facts -> taxonomy
(us-gaap, ifrs-full, dei) -> tag -> units -> list of facts with start, end, val, accn, fy, fp, form, filed), already
cut down to the tags a screener might use (10-K/20-F/40-F annual facts and recent 10-Q facts). Files whose name
starts with the same ticker (e.g. aapl26_ and aapl_) are different snapshots of the same company; treat each file
as a separate company. Ignore industry restrictions (treat every file as eligible).
