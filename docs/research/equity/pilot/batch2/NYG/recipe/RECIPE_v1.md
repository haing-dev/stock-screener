# Recipe: Bill Nygren and Alex Fitch (Oakmark Funds), gate G6

Inputs: CARD.md (label THIN: 2 documents, below the material bar; no held-out document), FIELD_DICTIONARY_v1.0.md,
field_dictionary_v0.1.csv, construction_13F.txt. No return of any kind was seen; no number below is tuned.

Applied at each quarter-end to the eligible set (1,500 largest US stocks, GICS sector known), all inputs as known on
the day (dictionary v1.0 rule 1). Card form = the Oakmark fund (the ~50-name fund); the Select form is a version.

## 0. Shared definitions (used by several lines)

- **E1** = consensus EPS mean, next 12 months (V03 input "EPS mean NTM"), on the same share basis as the price.
- **g_raw** = consensus long-term EPS growth mean (dictionary input "growth mean", as in V14); if missing, E04
  (FY2 EPS mean / FY1 EPS mean - 1).
- **g** = g_raw clipped to [0, 10%] (see P3).
- **r** = max(8%, 7-year Treasury yield on the day) (see P2). The 7-year yield comes from the same source as V13's
  Treasury yield, 7-year tenor (if only the 10-year is loaded, use it and flag the run).
- **V** (value per share, seven-year convention, see P1) =
  sum over t = 1..7 of E1 x (1+g)^(t-1) / (1+r)^t  +  [E1 x (1+g)^6 / r] / (1+r)^7
  (seven years of earnings at g, then a no-growth perpetuity of year-7 earnings at r).
- **PV** = price at the quarter-end / V. E1 <= 0 or missing, or g_raw missing = V missing.

Line format: id | card rule(s) and claim ids | measure | comparison and number | TAG | why this measure stands in.

## 1. BUY (what qualifies)

- **B1** | Rbuy5 (NYG1-C053) | new: rank (1 = largest) inside the eligible set of R01 revenue TTM, R13 net income
  TTM and R33 common equity (latest quarter); pass if the best of the three ranks <= 250 | best rank <= 250 | `quote`
  | his own definition of the Oakmark universe ("250 largest" by sales, net income or shareholders' equity).
- **B2** | Rbuy2 (NYG1-C006, NYG1-C007, NYG1-C009); guard of Ravoid1 (NYG1-C010); one of the three Rbuy1 filters
  (NYG1-C014, NYG1-C048) | new: V10 (dividends per share TTM / price) + g | >= 8% | `quote` (8% = lower end of "eight
  or 9% at a minimum") | "dividend income plus expected per-share value growth"; dividend yield is the income, the
  consensus long-term per-share earnings growth is the only expected per-share growth figure in the dictionary
  (choice of source = convention, card gap 2).

Pass rule (Rbuy1: all filters together): a stock passes when B1, B2 and P4 hold and none of A1-A3 applies. The third
Rbuy1 filter (exceptional, aligned management) is not computable (section 6); A2 covers only its negative side.

## 2. PRICE (when cheap enough)

- **P1** | Rprice1 (NYG1-C002, NYG1-C004, NYG1-C087, NYG2-C002) | new: V as defined in section 0 (consensus NTM EPS
  grown at g for 7 years, discounted at r, plus a no-growth tail) | horizon 7 years | `quote` (seven years) for the
  horizon; the tail and the use of consensus for "his best estimate" are `convention` | value = what an all-cash
  buyer can pay for the next seven years' earnings and still earn an adequate return; consensus is the only
  outside forecast; the no-growth tail credits nothing beyond his stated horizon.
- **P2** | Rprice3 (NYG2-C006, NYG2-C007), Rprice4 (NYG2-C008), "adequate return" (Rprice1) | r = max(8%, 7-year
  Treasury yield) | floor 8% | `convention` (8% = his stated minimum market return, NYG1-C007, read as the "adequate
  return"; the 7-year bond is his stated alternative; no premium is stated, so none is added) | the floor reproduces
  the near-zero-rate floor of 2010-2021; the bond term binds only if the 7-year yield exceeds 8% (it did not in
  2010-2025, so r = 8% in every design quarter).
- **P3** | Rbuy3 (NYG1-C091) used as a bound on growth credit; Ravoid1 | g = g_raw clipped to [0, 10%] | cap 10%,
  floor 0 | `convention` (10% = top of his "something like 8 to 10% a year" for most holdings; floor 0 because
  declining names are excluded by A1) | stops upward-biased consensus long-term growth from valuing growth stocks he
  "can't put into a value framework" (NYG1-C057, example).
- **P4** | Rprice2 (NYG1-C003, NYG1-C005, NYG1-C042) | PV | < 0.70 | `quote` ("something in the 60s cents on the
  dollar"; 0.70 = top of the 60s) | his entry discount, applied to the convention value P1.

Ranges these lines imply (for reading only, r = 8%): PV < 0.70 means forward P/E below about 8.8 at g = 0, 11 at
g = 5% and 13.8 at g = 10%.

## 3. AVOID (exclusions)

- **A1** | Ravoid1 (NYG1-C010, NYG1-C009) | g_raw | < 0 = excluded | `convention` (0 = "declining business value") |
  consensus expecting per-share earnings to shrink is the closest outside sign of "best days in the rearview mirror";
  Altria-type "no growth" (g = 0, NYG1-C008) still passes.
- **A2** | Ravoid2 (NYG1-C012), negative side of Rbuy4 (NYG1-C011) | new: revenue growth over 12 quarters (R01 TTM
  now / R01 TTM 12 quarters earlier - 1) > 0 AND revenue per diluted share growth over the same 12 quarters (R01 TTM
  / R15) <= 0 | both conditions = excluded | `convention` (zero = size grew, per-share did not) | literal reading of
  "don't use a denominator": the business got bigger while each share's part of it did not (issuance or
  share-financed deals).
- **A3** | Rbuy1 / Rprice1 (NYG1-C057 s, Nvidia example) | V missing (E1 <= 0 or missing, or no growth input) |
  missing = excluded | `convention` | a stock that cannot be valued cannot be bought at a discount to value.
- **Industries**: none. The card states no sector or industry exclusion (card section 3) and he holds banks (Bank of
  America, Wells Fargo: NYG2-C024, NYG2-C027). The generic-book exclusions of dictionary X01 (banks, insurers, real
  estate, biotech) do NOT apply to this pod.

## 4. SELL

Held names are not re-screened on BUY each quarter (holding period 5-7 years, Rproc1); they leave only by S1, S2,
delisting or acquisition. S3 trims.

- **S1** | Rsell1 (NYG1-C086, NYG1-C088, NYG1-C042), Rsell2 (NYG1-C089), Rsell3 (NYG1-C093) | PV recomputed at each
  quarter-end with current E1, g, r and price | PV >= 0.90 = sell | `quote` ("selling at 90"; inside "between 85 and
  95%") | his sell target as a share of current value; recomputing every quarter is the machine form of "update the
  value for all new information".
- **S2** | Rsell4 (NYG1-C059, NYG1-C060, NYG1-C045), Rsell5 (NYG1-C063, NYG1-C067), Rsell6 (NYG1-C068, NYG1-C069,
  NYG2-C016), Rsell7 (NYG1-C044, NYG1-C061) | new: dev = (F_now - F_base) / abs(F_base), F = consensus EPS mean for a
  fixed tracked fiscal year (FY1 at the base date; once that year reports, its actual EPS, E03 input), F_base = F at
  entry or at the last re-baseline; skip if F_base <= 0 | dev <= -10% triggers a fresh test: the name stays only if
  it passes the full BUY set today (B1, B2, P4, A1-A3); otherwise sell. After the test (kept or not) and after the
  tracked year reports, re-baseline to the new FY1. dev >= +10%: no action (S1 already uses the new numbers) |
  `quote` (10% = lower end of "10 to 15%") for the trigger; EPS as "fundamentals" and consensus as "the analyst's
  projection" are `convention` | a mistake is a business miss against the forecast, not a price fall; "recommit only
  if it would buy the stock fresh today" (Rsell6) with exit as the default (Rsell7). The 2nd shortfall repeats the
  test; the 3rd (new analyst) has no machine form.
- **S3** | Rsell8 (NYG2-C084), Rsize3 (NYG2-C083) | position weight at the quarter-end | > 4% (2 x the 2% target) =
  trim back to 4% | `quote` ("doubled") | the stated soft ceiling; trimmed cash goes to the ranking queue.

## 5. SIZE

- **Z1** | Rsize1 (NYG2-C003, NYG2-C081) | number of names held | target 50 | `quote` ("just over 50") | his fund's
  name count.
- **Z2** | Rsize2 (NYG2-C082) | entry weight | 2% (= 1/50) | `quote` | typical Oakmark weight. If fewer than 50
  names are held, the empty slots stay in cash (paper); no re-scaling above 2% at entry.

Ranking inside the pass set (brief rule 5; Rprice2 "at 60% ... very very happy" NYG1-C042, Rsell3 "recycle into a
name at about 60%" NYG1-C093, Rsize5 "is it cheaper" NYG1-C054): fill free slots (first build: all 50; later: slots
freed by S1, S2, S3 or exits) with passing names not held, in ascending PV; tie: higher V10 + g. The "diversifier"
half of Rsize5 has no stated measure and is not used.

## 6. Not computable (card rules no dictionary measure can express)

1. Rbuy4 / third filter of Rbuy1, positive side (NYG1-C011, NYG1-C014): "aligned with outside shareholders" has no
   measure; insider ownership (O02) is not his test (A2 covers only "no denominator").
2. Rbuy6 (NYG2-C069, NYG2-C070): "competitively advantaged" reinvestment; a preference, no threshold; incremental
   return (G07) cannot say whether the business is advantaged.
3. Rbuy7 (NYG2-C026): "significant controversy"; no controversy measure (P4 catches only the cheapness it brings).
4. Rbuy8 (NYG2-C075, NYG2-C077): embedded disruption option; no measure.
5. Rprice5 (NYG1-C082): recast of R&D, advertising and acquisition spending; no formula stated.
6. Ravoid3 (NYG2-C033, NYG2-C071): reinvestment "not understood"; judgement.
7. Rsell6, third step (NYG1-C070) and management re-meeting (NYG1-C068): people steps.
8. Rsize5, diversifier half (NYG1-C054): no measure or limit stated.
Process rules Rproc2-Rproc11 (approved list, votes, devil's advocate, reviews, management meetings, accuracy over
conservatism, no market timing, tax lots, team) describe the firm's process, not a stock property: not screenable.

Computable but left out (brief rule 2): Rprice6 (price below cash, B04 >= 1; no threshold stated, "still part of the
process", rare among the 1,500 largest); Rbuy3 as a test (it describes most holdings, used only as the P3 cap);
Rsize4 (~10 new names a year) and Rproc1 (5-7-year holding) are reported as checks, not imposed.

## 7. DECISIVE form (only `quote` and `convention` numbers)

B1 (best rank <= 250), B2 (V10 + g >= 8%), A1 (g_raw < 0 out), A2 (size up, per share not: out), A3 (no value: out),
P1-P4 (seven-year consensus value, r = max(8%, 7y), g clipped [0, 10%], PV < 0.70); SELL S1 (PV >= 0.90), S2
(dev <= -10% -> fresh BUY test), S3 (trim above 4%); SIZE Z1 50 names, Z2 2% each, cash for empty slots; ranking by
ascending PV. Quarterly, quarter-end close.

## 8. FULL form (decisive + `grid` and `revealed-13F` versions)

One-at-a-time versions around the decisive form, each a separate paper book, equal-weight average of all books
(decisive book included), 10 books in all:

| id | line varied | values | TAG | source |
|---|---|---|---|---|
| G1 | B2 bar | 9% | `grid` | other end of "eight or 9%" (NYG1-C007) |
| G2 | P4 entry | 0.60 | `grid` | "at 60% ... very very happy" (NYG1-C005, NYG1-C042) |
| G3 | P2 floor | 9% | `grid` | other end of his market return (NYG1-C007) |
| G4 | g_raw source | E04 only | `grid` | expected-growth source not stated (card gap 2) |
| G5 | S1 target | 0.85 | `grid` | "between 85 and 95%" (NYG1-C088) |
| G6 | S1 target | 0.95 | `grid` | same |
| G7 | S2 trigger | -15% | `grid` | "10 to 15%" (NYG1-C063) |
| G8 | Select form: Z1 20 names, Z2 4%, S3 ceiling 8% | 20 / 4% / 8% | `quote` (numbers), version | NYG2-C082, NYG2-C025 s; B1 kept (no Select universe stated) |
| G9 | S3 ceiling | 7% | `revealed-13F` | 90th percentile of the largest weight (construction_13F.txt); his ceiling is soft |

Checks reported, not imposed (`revealed-13F` and `quote`): median holding in quarters (13F 31; card 5-7 years = 20-28
quarters); names still held after 1 / 3 / 5 years (13F 97 / 79 / 61%); new names per year (card ~10; 13F 7% of
names); effective names (13F 45.5) and top-10 share (13F 36%). The 13F filer is firm-wide (132 names over time, new
positions start at 0.5%, 66% of buys are additions), so its weights describe the firm, not the Oakmark fund.

## 9. Coverage and main risk

Buy rules covered: 2 of 8 fully (Rbuy2, Rbuy5 = 25%); 3 more in part (Rbuy1: two of three filters; Rbuy3: as the
growth cap only; Rbuy4: negative side only via A2) = 5 of 8 touched (62.5%); Rbuy6, Rbuy7, Rbuy8 not at all. Price:
Rprice1-4 in proxy form, Rprice5-6 not. Sell: Rsell1-5, 7, 8 in machine form, Rsell6 in part.

Main risk. His value is his analyst's own seven-year forecast, recast for intangibles, and his best ideas are the
ones where that forecast differs from the crowd's: controversial names (Warner Bros Discovery, Meta, Netflix) where
consensus is wrong in his view. The recipe values every stock on consensus, so by construction it cannot find a gap
between his forecast and the market's; what it finds instead is stocks with low forward P/E for their consensus
growth, a statistical value screen of the kind he says is "not that effective anymore" and replicable by a value
factor fund (NYG1-C101, NYG1-C102). Without the recast it will undervalue R&D- and marketing-heavy companies (his
Netflix, Alphabet, Amgen cases) and favour banks, cyclicals near peak earnings and low-growth high-yield names whose
consensus is high; without a management test it admits capital allocators he would reject (A2 catches only
share-financed growth). The likely result is a book that looks like a cheap-forward-earnings portfolio of large
companies (with no sector control, likely tilted to financials and cyclicals) with the right holding discipline (sell near value, exit on misses), not his portfolio of
contested, analyst-recast situations. Card is THIN (two documents), so any recall shortfall may also reflect rules
he uses but did not state in these two talks.
