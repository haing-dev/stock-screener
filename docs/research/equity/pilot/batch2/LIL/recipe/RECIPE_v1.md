# Recipe: Li Lu (Himalaya Capital), gate G6

Inputs: CARD.md (THIN: 2 documents, LIL1 2020-04-24 and LIL2 2026-07-24, no held-out document), field_dictionary_v0.1.csv,
FIELD_DICTIONARY_v1.0.md, construction_13F.txt. Claim ids as in the card (`C0nn` = LIL1, `L2-C0nn` = LIL2).
No return or outcome was seen; no number below is tuned.

## 0. Mechanics (apply to every criterion)

- Universe: the 1,500 largest eligible US stocks at the quarter-end, GICS sector known. Sector percentile = rank inside
  the GICS sector among universe members at that quarter-end (higher = better unless stated).
- As-of rules of FIELD_DICTIONARY_v1.0 (first-reported accounts, usable from announcement + 1 day; TTM = four
  consecutive quarters; a ratio with a denominator at or below zero is missing).
- Market value is always the company figure L01c, never per-share numbers (RPr3, C040: "think in market cap"). This is a
  form rule, not a pass/fail criterion.
- Missing measure: a BUY or PRICE measure that is missing = not passed (a pass/fail screen needs the number; the
  reference book's "missing = sector median" does not apply). An AVOID measure that is missing = not excluded.
- No industry is excluded: he names none (card section 3). Note: B1's measure needs a current-asset / current-liability
  split, so banks and insurers usually have B1 missing and fail by construction, not by his rule.

## 1. Criteria

Format: id | card rule(s) and claim ids | measure | comparison and number | TAG | why this measure stands in for his words.

### BUY (what qualifies)

| id | card rule, claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| B1 | RB3 (always), RB1 "good business" leg, RB5; C017, C042, C084, L2-C026, C007, L2-C013 | Q02 Return on capital (Greenblatt): EBIT TTM / (current assets - cash - current liabilities + short-term debt + net fixed assets) | sector percentile >= 0.667 (top third of the GICS sector) | convention | Q02 is his own definition almost word for word: pre-tax, pre-interest earnings over the unleveraged capital the business needs (working capital + fixed assets, goodwill left out). He gives no cut-off ("higher is better"); "a good business" read as clearly better than the sector's typical business = top third. The 50-100% in C084 describes superb businesses he keeps, not an entry filter (card), so it is not used as a threshold. |
| B2 | RB2 (always); C012 | new: lowest month-end split-adjusted close of months t-11..t was set in months t-2..t (the stock made a new 12-month low during the quarter) | true | convention | "Ideas start from the new-low lists, not the new-high lists". The standard new-low list is the 52-week-low list; a quarterly screen reads "on the list" as "made a new 12-month low within the quarter". He states no window or depth (card gap). |

RB4 (strengthening advantage) enters only the ranking rule (section 3), through a proxy; it is not a gate.

### PRICE (when cheap enough): passes if P1 OR P2

| id | card rule, claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| P1 | RPr2 (always), RB1 "cheap" leg; C014, C016, C045, L2-C061 | V06 Book to price (common equity / L01c) | >= 1.0 (price at or below book) | quote | "When a stock is below book value" (C014) is his only stated valuation line; his worked cases are below book (L2-C061: $300m vs $500m book) or below liquid assets (C045). |
| P2 | RPr1 (usually), RB1 "cheap" leg, RB5; C013, C002, L2-C060 | V01 Earnings yield (EBIT TTM / EV) | sector percentile >= 0.8 (cheapest fifth of the GICS sector) | convention | "Cheap is a multi-dimensional concept related to relative value" (L2-C060) and valuation is a fit / no-fit gate (C013) with no number. EBIT/EV matches his EBIT-based view of the business (B1); the cheapest fifth inside the sector is the standard reading of "cheap relative to peers". |

### AVOID (exclusions; none stated by him, taken as conventions from his earnings-quality rule)

| id | card rule, claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| A1 | RPr4 (always); C043, C042, C015, L2-C064 | Q08 Accruals ((net income TTM - CFO TTM) / average total assets) | excluded if in the worst fifth of the sector (highest accruals; reversed percentile < 0.2) | convention | RPr4: break down what the earnings and working capital are made of. Earnings far ahead of cash flow are the computable sign of earnings that do not hold up; worst fifth is the standard cut. |
| A2 | RPr4 (always), supported by L2-C065 | new: operating margin TTM (R07/R01) minus the median of its own TTM values at the last 20 quarter-ends (at least 12 present) | excluded if in the highest fifth of the sector | convention | L2-C065: a low P/E may come from peak-cycle or one-off earnings. A margin far above its own 5-year median is the computable sign of peak earnings. Dictionary S05 uses 10 years; 5 years is used because first-reported accounts start in 2010. |

### SELL

| id | card rule, claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| S1 | RS4 (usually; the later view, card change #1), RS5 dropped; C085, C092, C081, L2-C043 | none (rule of conduct) | never sell or trim a holding because it looks expensive (no valuation exit, no rebalancing down) | convention | "Sit on it once bought"; he replaced "if I don't want to buy at that price, I sell" (C080, former) with holding great businesses. Which holdings are "great and projectable" cannot be computed, so the later view is applied to all holdings. |
| S2 | RS4; C085 | holding age in quarters | broad form only: each stock is held 40 quarters from its entry (10 years), then released | quote | "Project with overwhelming odds next 10 20 years" (C085); the lower end, 10 years, is read as the holding horizon. Flag: C085 states a projection horizon, used here as a holding period. |
| S3 | RS2 (usually); L2-C037 | ranking score (section 3) | investor form: when the book is full, replace the lowest-scoring holding by a pass-set candidate whose score is higher | convention | "Switch when a better target offers a better risk/reward"; no margin is stated, so any higher score counts. |
| S4 | RS4, RS2 | holding age | investor form: no sale (including S3) in the first 4 quarters after entry | revealed-13F | 100% of his positions are still held after 1 year. |
| S5 | RS2, RS4 | switches per year | investor form: at most one S3 replacement per 4 quarters | revealed-13F | New positions are 13% of the book per year (about 0.8 of 6 names); median holding more than 30 quarters; 66% still held after 5 years. |
| S6 | RS3 (sometimes); L2-C038, L2-C040, L2-C044 | V01 Earnings yield, percentile in the whole universe | sell if below the 1st / 2nd / 5th percentile of the universe (plus "off") | grid | "Bubble-like extreme overvaluation" has no multiple and is overridden for great businesses by RS4 (open boundary, card #3); so it is a grid in the full form only. |

### SIZE

| id | card rule, claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| Z1 | RB1 / RB5 (no N stated) | portfolio weights | broad form: equal weight across all held stocks (S2), rebalanced each quarter-end | convention | He states no number of names or weights; the broad form tests the pass set itself. |
| Z2 | RZ3 (no number); C053 | number of names | investor form: N = 6 | revealed-13F | 6 names in his 13F (effective 4.1). C053's "no more than the number on two hands" counts lifetime insights, not holdings (card), so it is not used. |
| Z3 | RZ3; C030, C063 | target weight by rank of the holding's score (section 3) | 38 / 22 / 16 / 11 / 8 / 5 % | revealed-13F | Built to match the 13F: largest 38%, top-5 95%, 6 names; effective names 1/sum(w^2) = 4.2 vs 4.1 revealed. |
| Z4 | RZ3 (usually; bet smaller until the work is done, then add "a lot lot more"); C061, C063 | entry weight | a new position enters at min(6.2%, target); at the next quarter-end it is raised to its Z3 target if it still passes B1 | revealed-13F | New positions start at 6.2% in his 13F; additions are 41% of his buys. Research done cannot be computed, so one quarter stands for "after the work". |
| Z5 | RZ2 (always); L2-C054 | gross exposure of the paper book | sum of weights <= 100%; no borrowing | quote | "No borrowing, so the portfolio can survive a 50% fall": leverage = 0. |
| Z6 | RZ1 (always); C036, C072 | unfilled weight | weight not filled by passing names stays in cash (T-bills) | convention | "Holding cash while waiting is fine; when the chance comes, jump on it." No cash number is stated. |

## 2. Decisive form and full form

**Decisive form (quote and convention numbers only).** Pass set at each quarter-end =
B1 (Q02 top third of sector) AND B2 (new 12-month low in the quarter) AND (P1 V06 >= 1.0 OR P2 V01 cheapest fifth of
sector) AND NOT A1 (accruals worst fifth) AND NOT A2 (margin vs own 5-year median, highest fifth).
Portfolio (broad form): every stock that passed at any quarter-end in the last 40 quarters (S2) and is still listed,
equal weight (Z1), no leverage (Z5), never sold on valuation (S1). Sales otherwise only at delisting or merger (last price).
Criteria used: B1, B2, P1, P2, A1, A2, S1, S2, Z1, Z5, Z6.

**Full form (adds revealed-13F and grid).** Same pass set, with versions averaged at equal weight: the central version
(decisive numbers) plus one-at-a-time variations B1 top half / top fifth (0.5, 0.8); B2 low set within 6 / 12 months;
P2 cheapest third / tenth (0.667, 0.9); S6 at 1 / 2 / 5% = 10 versions. Investor form portfolio: N = 6 (Z2), ranked by
section 3, target weights Z3, entry Z4, S1 no valuation sale, S3 switch with S4 and S5 limits, Z5, Z6; no time exit
(S2 does not apply: 66% of his positions are still held after 5 years).

## 3. Ranking inside the pass set

His order: valuation is a gate, fit or no fit (C013), so cheapness does not rank. Then he prefers the good business
(RB3, C017) whose advantage keeps getting stronger (RB4, C086, C053), "quality yet cheap" (L2-C013).
Score = mean of (a) sector percentile of Q02 and (b) sector percentile of the 3-year change in Q02
(new: Q02 at t minus Q02 12 quarters earlier; missing = 0.5). Ties: higher V06 (larger margin of safety, C002).
Equal weights in the mean: convention. (b) is our proxy for RB4 (return on capital above peers and rising, L2-C026 as
the card notes); it is not his stated measure. The highest scores fill the N = 6 places; the score also drives S3 and Z3.

## 4. Not computable

| card rule | reason |
|---|---|
| RB1, management leg | trust in management is judged in person (RP7); no stand-in (insider ownership, tenure) is stated |
| RB4, core | "advantage getting stronger", "inflection point of a winner-take-all business": no measure; only the ranking proxy (section 3) |
| RB6 | "dynamic creative companies in vibrant economies": no definition; the universe is fixed to the US |
| RS1 | "thesis proven wrong": no stop number; the 20-30% (C062) is the loss already taken |
| RS6 | fund redemptions do not exist in a paper book |
| RZ3, sizing by research done and downside | knowledge and downside judgement cannot be measured; only the 13F entry and add pattern (Z4) |
| RP1 | checklist and "last psychological barrier" |
| RP2 | reading manuals cover to cover; he says no screen is needed |
| RP3 | 5 minutes per page, sums in his head |
| RP6 | reading court documents |
| RP7 | site visits to management and community |
| RP8 | finish the work in a couple of weeks |
| RP9 | wide reading, one insight a year |
| RP10 | analysts' information accurate and complete |
| RP11 | hiring rule |

Computable stand-in exists but not used: RP4 (E05 analyst coverage: he only checks what others look at; "no coverage
is good" is a principle, C019, and nearly every large US company is covered); RP5 (C04 share count change: "needed outside
money" is undefined and his 10-15 year look-back exceeds the 2010+ first-reported data). RS5 is his former rule, replaced
by RS4: not used.

## 5. Coverage and main risk

Buy rules covered: RB2, RB3 and RB5 fully; RB1 two of its three checks (cheap, good business; not management); RB4 only
as a ranking proxy; RB6 not at all. That is 3 of 6 fully (50%), or 4 of 6 (67%) counting the two partial rules as half.

Main risk: the recipe selects his "cheap-stock route" rather than his "insight route". The screen finds US companies
with high return on capital that are below book or cheap within their sector and have just made a 12-month low:
statistical bargains of the kind he says give "ordinary" or "few times" returns (C052, C071; the Timberland and Korean
cases). His book is instead a handful of businesses whose advantage he expects to strengthen for 10-20 years, chosen on
management trust and projectability (RB4, RB6, RS4, RP7), none of which is computable, and some of his named holdings
(BYD, Chinese companies) are outside a US universe. The mechanics add their own bias: B1 is missing (so failed) for
banks and insurers and for businesses whose working capital plus fixed assets is zero or negative, which includes some
of the superb high-return businesses he keeps (C084); and the conjunction of top-third quality, a fresh 12-month low and
below-book or cheapest-fifth value will be empty in many quarters, leaving the paper book mostly in cash. The card is
thin (two documents, none held out), so even the stated rules may be an incomplete picture of how he picks.

## Counts

BUY 2, PRICE 2, AVOID 2, SELL 6, SIZE 6 = 18 criteria (decisive form uses 11). Not computable: 15 card rules
(plus 2 with a stand-in not used, and RS5 dropped as former).
