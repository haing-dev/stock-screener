# Investor card: Bill Nygren and Alex Fitch (Oakmark Funds)

**File THIN (below the material bar, A13 item 8)**: 2 documents read (NYG1 2025-06-21, NYG2 2022-12-29); the bar needs 3 documents of 5,000+ words. No document held out.

Source: `claims_for_card.json` only (197 claims: 68 rule_status both, 10 third, 119 no). Speaker is Bill Nygren unless marked (Fitch). Tags after an id: **b** = rule_status both, **t** = third, **s** = support only (principle, example, view or not a verified rule). Measure column gives `computable_final` in brackets (yes / proxy / no).

## 1. What he buys and why

He buys a stock only when it sells at a large discount to his estimate of business value, ideally "in the 60s cents on the dollar" (NYG1-C003, NYG1-C005, NYG2-C002). Business value is "the maximum price an all-cash buyer could pay to own the whole business and still earn an adequate return", estimated from what the company can earn over the next seven years discounted back to today (NYG1-C002, NYG1-C004, NYG1-C087), with a roughly seven-year bond as the alternative that sets the discount rate (NYG2-C006, NYG2-C007). Cheapness alone is not enough. Dividend income plus expected per-share value growth must at least match the S&P 500, "eight or 9% at a minimum", so that he avoids value traps "whose best days are in the rearview mirror" (NYG1-C006, NYG1-C007, NYG1-C009, NYG1-C010). Management must be "aligned with outside shareholders in having a goal of maximizing intermediate to long-term per share business value", not just growing in size (NYG1-C011, NYG1-C012, NYG1-C014). He expects to be paid for stepping into controversy (NYG2-C026, NYG2-C042 s) and likes situations with an embedded option where failure only stops the losses (NYG2-C075, NYG2-C077). He holds for about 5 to 7 years (NYG1-C013, NYG1-C090). He sells at 85-95% of value and recycles into names at about 60% (NYG1-C088, NYG1-C093). He treats fundamentals 10-15% off the analyst's forecast as a mistake that should leave the portfolio quickly (NYG1-C060, NYG1-C061, NYG1-C063).

## 2. Rules by part

Format: id | statement | measure [computable] | number and direction as stated | strength | claim ids | dates said.

### Buy

| id | statement | measure | number / direction | strength | claims | dates |
|---|---|---|---|---|---|---|
| Rbuy1 | All three filters must hold together: undervalued, value expected to grow, and an exceptional, aligned management. Every written new idea must show all three. | undervaluation plus management quality; cheapness, value growth, management [proxy / no] | none stated | always | NYG1-C014 t, NYG1-C048 b; s NYG1-C001, NYG1-C015, NYG1-C057 | 2025-06-21 |
| Rbuy2 | Dividend income plus expected per-share value growth must at least match what he expects for the S&P 500. The form does not matter (yield or growth). | dividend yield plus expected per-share value growth [proxy] | "eight or 9% at a minimum" (>= 8-9%) | always (rule) / usually (threshold) | NYG1-C006 b, NYG1-C007 b, NYG1-C009 b; s NYG1-C008 | 2025-06-21 |
| Rbuy3 | Most holdings are expected to grow business value at about 8-10% a year. | business value growth [proxy] | "something like 8 to 10% a year" (between) | usually | NYG1-C091 b; s NYG1-C042 | 2025-06-21 |
| Rbuy4 | Exceptional management means alignment with outside shareholders on maximising intermediate- to long-term per-share business value. | management alignment with per-share value [proxy] | none stated | always | NYG1-C011 b; s NYG1-C017, NYG2-C054, NYG2-C067 | 2025-06-21 |
| Rbuy5 | Oakmark fund universe: a big business among the 250 largest by sales, net income or shareholders' equity (scope: Oakmark fund). | rank by sales, net income or shareholders' equity [yes] | "250 largest" (rank <= 250 on any one of the three) | always | NYG1-C053 b | 2025-06-21 |
| Rbuy6 | Prefers a company reinvesting in its basic business where it is competitively advantaged over one handing capital back. | return on reinvestment / excess return on reinvestment [proxy] | none stated | usually | NYG2-C069 b, NYG2-C070 b; s NYG2-C060, NYG2-C073 | 2022-12-29 |
| Rbuy7 | "There almost has to be significant controversy about that company" to get it cheap enough (scope per the claim note: Select fund). | controversy / discount to value [proxy] | none stated | usually | NYG2-C026 b; s NYG2-C040, NYG2-C042, NYG1-C031 | 2022-12-29 |
| Rbuy8 | Seeks asymmetric set-ups: a disruption option inside a traditional business, with a reasonable chance of success; if it fails, the losses stop and the base earnings come through. | embedded disruption option [proxy] | none stated | usually | NYG2-C075 t, NYG2-C077 b; s NYG2-C065, NYG2-C076, NYG2-C078 | 2022-12-29 |

### Price

| id | statement | measure | number / direction | strength | claims | dates |
|---|---|---|---|---|---|---|
| Rprice1 | Estimate long-term business value and look for large gaps between price and that value. Value = the most an all-cash buyer could pay and still earn an adequate return, from the best estimate of earnings over the next seven years discounted to today. | price to estimated business value; discounted seven-year earnings estimate [proxy] | seven-year horizon; "adequate return" not given as a number | always | NYG1-C002 b, NYG1-C004 b, NYG1-C087 b, NYG2-C002 b, NYG1-C026 t; s NYG2-C055, NYG2-C056, NYG2-C011 | 2025-06-21, 2022-12-29 |
| Rprice2 | Buy at about 60% of estimated value. | price to estimated business value [proxy] | "something in the 60s cents on the dollar" (<= ~0.6x); "at 60% ... very very happy" | usually | NYG1-C003 b, NYG1-C005 b, NYG1-C042 b; s NYG2-C079, NYG1-C096 | 2025-06-21 |
| Rprice3 | Business value is set against alternative investments. One alternative is a long-term bond of about seven years, to match the duration of an equity. | discount rate from about a seven-year bond yield [proxy] | about seven-year bond; no premium stated | always / usually | NYG2-C006 b, NYG2-C007 b; s NYG2-C009, NYG2-C013 | 2022-12-29 |
| Rprice4 | When rates were close to zero, they used a floor that "artificially inflat[ed]" the required discount rate (period 2010-2021). | discount rate floor [no] | floor level none stated | usually | NYG2-C008 b | 2022-12-29 |
| Rprice5 | Recast the income statement and balance sheet (R&D, advertising, sales spend, customer acquisition) to reflect real-world economics, for a growing share of companies. | earnings recast for intangibles [proxy] | none stated | usually | NYG1-C082 b; s NYG1-C078, NYG1-C079, NYG1-C080, NYG1-C081 | 2025-06-21 |
| Rprice6 | "Getting something for free" (price below cash or asset value) is still part of the process. | price to cash or asset value [proxy] | none stated | usually | NYG1-C027 b; s NYG1-C028 | 2025-06-21 |

### Avoid

| id | statement | measure | number / direction | strength | claims | dates |
|---|---|---|---|---|---|---|
| Ravoid1 | No value traps: structurally disadvantaged companies with declining business value (Rbuy2 is the guard). | structurally declining business value [proxy] | none stated | always | NYG1-C010 b, NYG1-C009 b | 2025-06-21 |
| Ravoid2 | Avoid companies whose managers "don't use a denominator" and only try to grow size, not per-share value. | growth in size rather than per-share value [proxy] | none stated | always | NYG1-C012 b; s NYG1-C018 | 2025-06-21 |
| Ravoid3 | Where management reinvests in businesses it does not understand, or the rationale of the investment is not understood, he is interested only if capital comes back to shareholders. | none [no] | none stated | usually | NYG2-C033 b, NYG2-C071 b; s NYG2-C037, NYG2-C032 | 2022-12-29 |

### Sell

| id | statement | measure | number / direction | strength | claims | dates |
|---|---|---|---|---|---|---|
| Rsell1 | Set a sell target at entry, depending on the riskiness of the business and the balance sheet. | price to estimated business value [proxy] | "between 85 and 95%" of current business value (sell at >= 0.85-0.95x); "selling at 90" | always | NYG1-C086 b, NYG1-C088 b, NYG1-C042 b; s NYG1-C097, NYG1-C098 | 2025-06-21 |
| Rsell2 | The analyst updates the value estimate (and so the sell target) for all new information, not only what was known at purchase. | none [no] | none stated | always | NYG1-C089 b; s NYG1-C094, NYG1-C095 | 2025-06-21 |
| Rsell3 | When a stock reaches its target, sell and recycle the capital into a name at about 60% of value. Wider dispersion of performance gives more chances to do this. | price to estimated business value [proxy] | recycle into ~60% of value | always / usually | NYG1-C093 t, NYG2-C005 t; s NYG2-C010, NYG2-C027 | 2025-06-21, 2022-12-29 |
| Rsell4 | A mistake is defined by company fundamentals against the analyst's forecast, not by the stock price, and in either direction. Be "very patient when the stock market isn't acting right and very impatient when the business isn't performing". | fundamentals vs analyst forecast [proxy] | none stated | always | NYG1-C059 b, NYG1-C060 b, NYG1-C045 b | 2025-06-21 |
| Rsell5 | First sign of a mistake = fundamentals deviate 10-15% from the analyst's projection. That triggers an immediate review in front of the stock selection group; any member may then propose removal from the list, and the group votes. | deviation of fundamentals from analyst projection [proxy] | "10 to 15%" (deviation >= 10-15%, either direction) | always | NYG1-C063 b, NYG1-C067 b | 2025-06-21 |
| Rsell6 | Escalation. Second shortfall: an immediate devil's advocate review, and the team meets management again (preferably in their offices) and recommits only if it would buy the stock fresh today. Third shortfall: coverage moves to another analyst. Fitch describes the same process for a name underperforming fundamental estimates. | none [no] | second / third shortfall | usually / always | NYG1-C068 b, NYG1-C069 b, NYG1-C070 b, NYG2-C016 b (Fitch), NYG2-C019 b (Fitch), NYG2-C031 b, NYG2-C018 t (Fitch) | 2025-06-21, 2022-12-29 |
| Rsell7 | Default is that mistakes exit: "if I don't know enough to buy it then I don't know enough for it to stay in the portfolio". Recycle that capital quickly into names more likely to succeed. | none [no] | none stated | always | NYG1-C044 b, NYG1-C061 b, NYG1-C062 b; s NYG1-C058, NYG1-C064, NYG1-C065, NYG1-C066 | 2025-06-21 |
| Rsell8 | After strong performance, start trimming so that the market does not push the position to a very high weight (see Rsize3). | position weight [no] | trim once the weight has roughly doubled from typical | usually | NYG2-C084 b; s NYG2-C083 t | 2022-12-29 |

### Size

| id | statement | measure | number / direction | strength | claims | dates |
|---|---|---|---|---|---|---|
| Rsize1 | Fewer holdings than the average fund: the Oakmark fund holds just over 50 names (a typical fund holds about 100). | number of holdings [no] | "just over 50"; "about half" of ~100 | usually | NYG2-C003 b, NYG2-C081 b; s NYG2-C025 | 2022-12-29 |
| Rsize2 | Typical holding weight: 2% in Oakmark and about 4% in Select. | position weight [no] | 2% (Oakmark); about 4% (Select) | usually | NYG2-C082 b | 2022-12-29 |
| Rsize3 | Once the weight has doubled, the risk/return at the higher price rarely merits a still higher weight. | position weight [no] | about double the typical weight as a soft ceiling | usually | NYG2-C083 t, NYG2-C084 b | 2022-12-29 |
| Rsize4 | New names per year: about 10 a year in Oakmark and about 4 in Select (2022 was unusual: 8 in nine months). | new ideas per year [no] | ~10 (Oakmark); ~4 (Select) | usually | NYG2-C003 b, NYG2-C004 b | 2022-12-29 |
| Rsize5 | At the buy decision, ask whether the name adds to the portfolio: is it cheaper, is it a diversifier? | none [no] | none stated | usually | NYG1-C054 b; s NYG1-C056 | 2025-06-21 |

### Process

| id | statement | measure | number / direction | strength | claims | dates |
|---|---|---|---|---|---|---|
| Rproc1 | Long horizon: the average holding period is 5 to 7 years ("about 5 years" typical). | holding period [no] | "5 to seven years"; "about 5 years" | usually | NYG1-C013 b, NYG1-C090 b; s NYG2-C080 | 2025-06-21 |
| Rproc2 | Approved list. A new idea is challenged at the weekly meeting ("everyone ... trying to present an argument why the analyst might be wrong"). Three investment leaders vote it onto the list. No portfolio may buy a name off the list. The list has about 100 names eligible for the Oakmark fund. | none [no] | three voters; about 100 names | always / usually | NYG1-C049 b, NYG1-C050 b, NYG1-C051 b, NYG1-C052 b | 2025-06-21 |
| Rproc3 | Portfolio entry is decided by a two-out-of-three vote of that group. | none [no] | 2 of 3 | always | NYG1-C055 b | 2025-06-21 |
| Rproc4 | Devil's advocate review for every new idea: someone else spends a couple of days reading the best short reports and presents why not to buy. | none [no] | "a couple days" | always | NYG1-C037 b; s NYG1-C036, NYG1-C041 | 2025-06-21 |
| Rproc5 | Devil's advocate review again for names on the approved list for more than a year. | time on approved list [no] | "more than a year" | always | NYG1-C038 b, NYG1-C040 b; s NYG1-C039 | 2025-06-21 |
| Rproc6 | Analysts review every holding at least once a year, with reviews timed at action points (adding, trimming, a change in the hypothesis). | none [no] | "at least annually" | always / usually | NYG1-C046 b, NYG1-C047 b | 2025-06-21 |
| Rproc7 | Management meetings: get managers off the pitch book. Ask how they judge success or failure, how they motivate people, and which numbers feed the models. | none [no] | none stated | usually | NYG1-C022 t, NYG1-C023 b, NYG1-C024 b; s NYG1-C019, NYG1-C021 | 2025-06-21 |
| Rproc8 | Prize accuracy over conservatism: from purchase to sale, squeeze conservatism out of the numbers and sell on the true best estimate of value. | none [no] | none stated | always | NYG1-C092 b | 2025-06-21 |
| Rproc9 | No market timing ("once the news was out, it was too late to sell"). | none [no] | none stated | always | NYG2-C001 t | 2022-12-29 |
| Rproc10 | Tax management: through the year, keep lowering the tax basis in names that have gone down in price. | none [no] | none stated | always | NYG2-C029 b, NYG2-C028 t | 2022-12-29 |
| Rproc11 | Team organisation: peer ranking of helpfulness is part of pay; hire ethical, hard-working people "smarter than we are" (firm practice, not screenable). | none [no] | none stated | always | NYG1-C071 b, NYG1-C099 b; s NYG1-C104, NYG1-C105 | 2025-06-21 |

## 3. None stated

Every part has at least one verified rule. Within the parts, these are not stated and must come from the 13F or a convention, tagged as such:
- **Buy**: no numeric test for management alignment (Rbuy4), controversy (Rbuy7) or the embedded option (Rbuy8). No size test for the Select fund.
- **Price**: no number for the "adequate return", the equity premium over the seven-year bond, or the near-zero-rate floor (Rprice3, Rprice4). No recasting formula (Rprice5). No price/cash threshold (Rprice6).
- **Avoid**: no measure of structural decline (Ravoid1); no leverage, sector or industry exclusion.
- **Sell**: no mapping from riskiness or balance sheet to a point within 85-95% (Rsell1); "fundamentals" in Rsell5 is not specified (earnings, cash flow, revenue?).
- **Size**: no maximum position, no sector limits, no initial-weight rule beyond "typical 2% / 4%".

## 4. Changes of view and scope

| claims | disagreement | verdict |
|---|---|---|
| NYG1-C100 s (1980s: buying low P/E or low P/B and being patient "was a winning formula") vs NYG1-C101 s, NYG1-C102 s (now replicable at almost no cost with a value factor fund, "not that effective anymore") | Simple value ratios as a method | **Dated change of view**: the later view wins. Simple low P/E and P/B are not his method today. Neither side is a verified rule. |
| NYG2-C007 b (about a seven-year bond as the alternative) vs NYG2-C008 b (floor on the discount rate when rates were near zero, 2010-2021) | Discount-rate basis | **Different scope** (period): both stand. The floor applies only when rates are near zero, and its level is not stated. |
| NYG2-C069 b, NYG2-C070 b (rather they reinvest than return capital) vs NYG2-C071 b (interested only if capital comes back, AT&T case); NYG2-C032, NYG2-C034 s (Meta trimmed for reinvesting with unclear return) | Reinvestment vs payout | **Different scope**: both stand. Reinvestment is preferred where the firm is competitively advantaged; payout is wanted where it reinvests outside its competence or the rationale is unclear (Ravoid3). |
| NYG1-C065 s, NYG1-C066 s (2025: it is "rarely true" that a stock falling more than its value estimate is a better buy; a mistake signals more mistakes), NYG1-C064 s vs NYG2-C017 s, NYG2-C020 s (Fitch, 2022: after Netflix missed subscriber growth two quarters running and fell from $600 to $160, they re-underwrote and "bought more shares near the lows") | Adding after a fundamental shortfall | **Open**. The 2022 add follows Rsell6 (re-underwrite, recommit), so it is not a breach of a stated rule. But the 2025 statement says such adds rarely pay. Neither side is a verified rule, and no claim says whether the add policy changed. |
| NYG1-C045 b (patient on price; mistakes defined by fundamentals, NYG1-C060 b) vs NYG2-C018 t (claim note: "devil's advocate review after a drop") | What triggers a review | **Different scope / resolved**: NYG2-C016 b (Fitch) states the trigger as underperforming "our fundamental estimates", and the Netflix case followed a fundamental miss (NYG2-C017). Both stand. |
| NYG1-C013 b ("5 to seven years") vs NYG1-C090 b, NYG1-C042 b ("about 5 years") | Holding period | **Same view, range**: about 5-7 years. Apple (NYG1-C094) was held 12 years under updated sell targets (Rsell2). |
| NYG1-C003 b (60s cents), NYG1-C005 b (60%) vs NYG1-C096 s (Apple bought at "two-thirds of value") | Entry discount | **Same view**: two-thirds lies inside "the 60s"; 60% is the "very happy" point. |
| NYG1-C007 b (yield + growth >= 8-9%) vs NYG1-C091 b (business value growth 8-10%) and NYG1-C042 b (business grows "the same as the S&P") | Growth bar | **Different measures, consistent**: Rbuy2 is a floor on yield plus growth; Rbuy3 is the typical expected value growth. |
| NYG2-C004 b (Select typically ~4 new names a year; 8 in nine months of 2022) | New-name count | **Period exception** (2022), not a change of rule. |

Open contradictions: **1** (adding after a fundamental shortfall: NYG1-C065/C066 vs NYG2-C017/C020).

## 5. Examples

| claim id | company | fits / fails | rule |
|---|---|---|---|
| NYG1-C008 | Altria (yield ~9%, no growth) | fits | Rbuy2 (via yield) |
| NYG1-C008 | Alphabet (little dividend, faster growth) | fits | Rbuy2 (via growth) |
| NYG1-C028 | National Presto (below cash value; school paper) | fits | Rprice6 |
| NYG1-C057 | Nvidia ("can't put it into a value framework") | fails | Rbuy1 / Rprice1 |
| NYG1-C081 | Amgen (early 1980s; EV / pre-R&D cash flow cheaper than pharma) | fits | Rprice5 |
| NYG1-C079, NYG1-C080 | Cable TV (1980s sector; depreciation and customer acquisition recast) | fits | Rprice5 |
| NYG1-C083, NYG1-C084, NYG1-C085 | Netflix (less than half HBO per subscriber; ~6x annual value increment) | fits | Rprice1, Rprice5 |
| NYG2-C017, NYG2-C018, NYG2-C020 | Netflix 2022 (subscriber misses; devil's advocate; added near lows) | re-underwritten, kept | Rsell6 (see open item, section 4) |
| NYG1-C094, NYG1-C095, NYG1-C096 | Apple (bought ~2009 at two-thirds of value, held 12 years, sell target raised) | fits | Rprice2, Rsell2 |
| NYG2-C024, NYG2-C025 | Bank of America (in Oakmark's ~50, not Select's 20) | fits Oakmark | Rsize1 |
| NYG2-C027 | Bank of America vs Wells Fargo (P/B spread too large for the quality gap; swapped) | switch | Rsell3 |
| NYG2-C030, NYG2-C032, NYG2-C034 | Meta (free cash flow miss; heavy AI / AR spending; position cut until a return is credible) | partly fails | Rsell6, Ravoid3 |
| NYG2-C035, NYG2-C036 | Meta (controversy on the blue app; Instagram worth more than the price) | fits | Rbuy7 |
| NYG2-C041, NYG2-C045, NYG2-C046, NYG2-C048 | Warner Bros Discovery (~4-4.5x earnings power; streaming priced at a negative; every branch above price) | fits | Rbuy7, Rbuy8, Rprice1 |
| NYG2-C037, NYG2-C071 | AT&T (overspent on streaming outside its competence) | fails | Ravoid3 |
| NYG2-C060, NYG2-C061, NYG2-C062, NYG2-C065, NYG2-C067, NYG2-C072, NYG2-C073 | Lithia (reinvests where advantaged; ~5-6x normalised EPS; FCF yield 15-20%; free e-commerce option; CEO incentives) | fits | Rbuy4, Rbuy6, Rbuy8, Rprice1 |
| NYG2-C063, NYG2-C064 | Carvana (not bought; Lithia preferred as profitable in 2008 and diversified) | not bought | no stated rule (resilience is an example only) |
| NYG1-C076 | Under Armour (merchandise left after 2020 riots, read as brand strength) | idea source | none (process anecdote) |

## 6. Gaps (what a screen needs that he does not state)

1. **Business value itself** (Rprice1, Rprice2, Rsell1, Rsell3): it rests on the analyst's seven-year earnings forecast, recast for intangibles, discounted at a rate built from about a seven-year bond plus an "adequate return". No premium, no floor level, no recasting formula and no forecast source are given. A screen needs a convention for value (for example a multiple or a consensus-based DCF), tagged as such.
2. **Expected per-share value growth** (Rbuy2, Rbuy3): its source is not stated (analyst? consensus? past growth?).
3. **Management alignment, controversy, embedded option, structural decline, "understood rationale"** (Rbuy4, Rbuy7, Rbuy8, Ravoid1-3): there is no measurable definition.
4. **Mistake trigger** (Rsell5): "fundamentals" and "what the analyst had projected" are not observable from outside. A proxy (for example reported earnings or cash flow vs consensus at purchase) must be a convention.
5. **Sell-target choice within 85-95%** (Rsell1): there is no mapping from riskiness or balance sheet.
6. **Balance sheet / leverage**: mentioned (NYG1-C001 s, NYG1-C086 b; WBD sub-3x, NYG2-C051 s) but no limit is stated.
7. **Universe**: the 250-largest rule (Rbuy5) has no stated country, measurement date or treatment of financials; nothing is stated for Select.
8. **Sizing**: typical 2% / 4% and the doubling ceiling are given (Rsize2, Rsize3). There is no initial-weight rule by conviction or cheapness, no maximum, and no sector or industry limits.
9. **Holding count and turnover** (Rsize1, Rsize4): stated only as typical figures, with no rule for the 20-name Select subset beyond "20 favorites" (NYG2-C025 s).
10. **Re-buy after a shortfall** is open (section 4).

## Rule counts

buy 8, price 6, avoid 3, sell 8, size 5, process 11 (total 41). Open contradictions: 1.
