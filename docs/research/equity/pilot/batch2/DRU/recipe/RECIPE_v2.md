# Recipe v2: Stanley Druckenmiller (Duquesne Family Office), gate G8 revision round (A10 item 9)

One revision of RECIPE_v1.md after its recall gate FAILED (decisive lift 1.69, 90% [1.27, 2.12], recall 16.5%).
Built from CARD.md v1.1 (labels: thin; held-out test FAILED, DRU2 merged; the 13F shows equity longs only),
FIELD_DICTIONARY_v1.0.md + field_dictionary_v0.1.csv (measures), construction_13F.txt (13F aggregates 2010-2025, no
returns) and RECALL_FEEDBACK.md (recall, base rate, lift, interval, share of purchases each v1 criterion rejects; no
returns, no names). The feedback was used only to find WHERE v1 may misread him; every change below rests on a card
quote. No number is new or tuned: every threshold is the v1 number (`quote` or `convention`) or a `grid` value.

## Change table

| id | v1 | v2 | claim ids | why (one line) |
|---|---|---|---|---|
| C1 | B2 `GR1` >= 0.20 required in branch G (decisive) | B2 removed from the decisive form; kept as a full-form version (F1 b) | DRU5-C015 (b), DRU2-C074 (b), DRU2-C073 (b) | he names ONE rate of a "secular" grower ("a 20 to 30 percent grower") and calls his bias "long-term"; a second, 1-year condition was the writer's addition, not his words |
| C2 | forward growth only in the full form (F1 b-c); Rbuy2 "not computable, not decisive" | new B6: E04 forward EPS growth >= 0.20, accepted in place of B1 (B1 OR B6) | DRU4-C037 (b), DRU5-C030 (b), DRU2-C036 (b), DRU5-C015 (b) | "Do not invest in the present ... Change moves them", 12-24 months ahead: a 20% grower may be one he sees growing 20% over the next 12-24 months, which FY2 over FY1 covers; a trailing-only rate reads "the present" |
| C3 | B5 `IND_EBIT` (industry sum of EBIT TTM) < 0 | B5 `IND_NI` (industry sum of net income TTM, R13) < 0; EBIT sum moved to the full form (F4 b) | DRU2-C075 (b), DRU2-C076 (b) | "buy cyclical industries while they are losing money": in reported accounts "losing money" is a net loss (bottom line); v1's "before financing and one-offs" was the writer's refinement, not in the quote |
| C4 | S1: sell when B1 or B2 fails | S1: sell when the growth condition of branch G (B1 OR B6) fails | DRU4-C049 (b), DRU4-C052 (b), DRU5-C015 (b) | follows C1-C2: "the reason I bought" = the entry condition as now read; cost basis still never an input |
| C5 | ranking ties by `GR3`; F1 / F4 versions as in v1 | ties by the larger of `GR3` and E04; F1 and F4 re-listed so the v1 decisive readings stay as averaged versions | DRU2-C073 (b), DRU2-C075 (b) | consequential on C1-C3: growth bias first (DRU2-C073 "bias toward growth"); the v1 readings stay in the full form, none picked |

Unchanged on purpose (rule 3): B3 (momentum 6-1 > 0, rejects 28%) stays on DRU5-C035 ("when the trends started to go up
that's when I'm supposed to plow in"); B4 (cyclical sectors, rejects 54%) stays on DRU2-C075 / DRU2-C076 ("cyclical
industries"; the rule is about cyclicals, so the 54% of purchases outside them are not branch-C purchases); the
industry-level reading of B5 stays (the quote says "cyclical industries while THEY are losing money", not the company);
no price rule is added (DRU6-C030 n "I'm not really a value investor"; no verified price rule); the threshold 0.20
stays the lower end of "20 to 30 percent" (DRU5-C015). The house exclusions (82 purchases outside the count) stay a
shop rule, not his.

---

Applied at each quarter-end to the eligible US stocks (1,500 largest, GICS sector known). All measures as known on the
day (dictionary v1.0 rules 1-3: first-reported accounts from announcement + 1 day, TTM = last four consecutive quarters,
ratio with denominator <= 0 = missing; consensus = latest mean within 35 days before the quarter-end, as E01). A stock
with a required measure missing does not pass (mechanical, not his); where a criterion accepts either of two measures
(B1 OR B6), a missing measure only fails its own side.
The shop's generic-book exclusions (X01: 4010, 4030, 4040, sector 60, 35201010) are a shop rule, not his; apply them
only if the pilot universe requires it (the card excludes no industry).

Format per criterion: id | card rule(s), claim ids | measure | comparison and number | TAG | why.

The recipe has two entry branches, because the card holds two verified buy styles whose relation is open (card
section 4 item 14): **G = secular growth in an up-trend** (Rbuy3, Rbuy5, read through Rbuy2) and **C = countercyclical**
(Rbuy8). A stock passes if it passes G OR C.

New formulas used (from dictionary inputs):
- `GR3` = (R01 TTM / R01 TTM 12 quarters earlier)^(1/3) - 1 (G01, 3-year form; both TTMs complete)
- `GR1` = R01 TTM / R01 TTM 4 quarters earlier - 1 (G01, 1-year form; full form only)
- E04 = FY2 EPS mean / FY1 EPS mean - 1 (dictionary v0.1; FY1 mean <= 0 = missing, rule 3; both means as known at the
  quarter-end)
- `IND_NI` = sum of R13 net income TTM over eligible universe members in the same GICS industry (6 digits, X01) at the
  quarter-end; members with net income missing left out; at least 3 members with net income present, else missing
- `IND_EBIT` = the same sum on R08 EBIT TTM (full form only)
- `CYC` = GICS sector in {10 Energy, 15 Materials, 20 Industrials, 25 Consumer Discretionary}

## 1. BUY (what qualifies)

| id | card rule, claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| B1 | Rbuy3; DRU5-C015 (b), DRU2-C073 (b), DRU2-C074 (b) | new: `GR3` | >= 0.20 (or B6) | quote (20%) | "a 20 to 30 percent grower" in a "secular" sense: the 3-year rate reads "secular" as sustained (convention for the window); revenue is the plain meaning of "grower" and exists when earnings are negative (convention for the item). Lower bound only: his fitting examples (Nvidia, cloud) grew far above 30%, so 30% is a typical rate, not a cap (cap = grid F2). One rate only: he names one rate and calls his bias long-term ("long-term that's my bias", DRU2-C074), so no second 1-year test [v2, C1] |
| B6 [v2, C2] | Rbuy2 + Rbuy3; DRU4-C037 (b), DRU5-C030 (b), DRU2-C036 (b), DRU5-C015 (b) | E04 (forward EPS growth, FY2 over FY1) | >= 0.20 (or B1) | quote (20%) + convention (measure) | "Do not invest in the present ... Change moves them"; he looks 12 to 24 months ahead (DRU2-C036 12-18, DRU4-C037 / DRU5-C030 18-24): a stock that will grow 20% over that horizon is "a 20 to 30 percent grower" as he invests. The FY2 over FY1 consensus is the standard dated, as-known read of growth 12-24 months out (convention); it is the market's estimate, not his own view (limit, section 10) |
| B3 | Rbuy5; DRU5-C035 (b) | P02 (momentum 6-1) | > 0 | convention | "when the trends started to go up that's when I'm supposed to plow in": a positive recent (6-month) price trend is the standard reading of "trend going up"; the 6-month window reads "started" (recent) rather than a long-established trend |
| B4 | Rbuy8; DRU2-C075 (b), DRU2-C076 (b) | X01, new: `CYC` | sector in {10, 15, 20, 25} | convention | "cyclical industries": the standard capacity-cyclical sectors; they hold his named cases (chemicals 151010, home builders 252010, autos 2510, trucking 203040, shipping 203030, retail 25x) |
| B5 [v2, C3] | Rbuy8; DRU2-C075 (b), DRU2-C076 (b) | new: `IND_NI` | < 0 | convention (0 = "losing money"; a loss = net income below zero, the reported bottom line) | "buy cyclical industries while they are losing money": the industry as a whole, not the company, as he states it; "losing money" in its plain accounting sense is a net loss, so no measure before financing or one-offs is substituted (EBIT = grid F4 b); the 3-member floor keeps a one-company "industry" out (data convention) |

Branch G = (B1 OR B6) AND B3. Branch C = B4 AND B5 (no trend condition in the decisive form: whether a countercyclical
buy waits for the price turn is open, card item 14).

Not used as entry conditions: B2 `GR1` (full form F1 b only, C1); the "slow muted growth" condition of Rbuy3 (a macro
regime he does not define; the growth bias is applied in every period, DRU2-C073 b); Rbuy4, Rbuy6, Rbuy9 (section 9).

## 2. PRICE (when cheap enough)

No criterion. The card has no verified price rule in any document ("I'm not really a value investor", DRU6-C030 n;
multiples appear only as views, card section 3), and construction_13F.txt holds no valuation aggregate. Adding a
valuation screen would put in a rule he does not state. Price count: 0.

## 3. AVOID (exclusions)

| id | card rule, claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| A1 | Ravoid2, Rsize5; DRU6-C033 (b), DRU6-C045 (b) | portfolio weight of one stock | never >= 0.30 (enforced in Z4) | quote (30%) | "never 30 or 40 percent of the fund in an equity" |

Industries he excludes: none stated in the card, so no GICS exclusion is his. Ravoid1 ("do not own something only
because it will fall less") cannot be a filter (it is a motive); it is kept as a design constraint: no criterion of
this recipe selects for low beta, low volatility or defensive sectors, and none may be added.

## 4. SELL

| id | card rule, claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| S1 [v2, C4] | Rsell1; DRU4-C049 (b), DRU4-C052 (b), DRU4-C050 (b); DRU5-C015 (b) | B1, B6 (branch G) | sell at the quarter-end when the growth condition fails (B1 AND B6 both fail), whatever the gain or loss since purchase | convention | "if the reason I bought a stock is no longer the case I don't care what I paid for it": the reason bought = the entry criteria of its branch as read in section 1; cost basis is never an input |
| S2 | Rsell4; DRU4-C042 (b) | P02 (branch G) | sell when P02 <= 0 | convention | "waits for tops", a top = the rate of rise flattens: a non-positive 6-month return is the plainest reading of a rise that has flattened; same window as B3 so a name is not bought and sold on different clocks |
| S3 | Rsell1 + Rbuy8; DRU2-C075 (b), DRU2-C076 (b); Rsell4 DRU4-C042 (b) | quarters held; P02 (branch C) | hold a branch-C name for 12 quarters regardless of price or B5; after that, sell at the first quarter-end with P02 <= 0 | quote (2 or 3 years) + convention (end of window; top rule as S2) | the thesis is "capacity shuts over the next 2 or 3 years": the reason bought lasts that long, so an industry still in loss or a falling price inside the window is not "the reason gone"; after it, he waits for the top |
| S4 | Rsell5; DRU2-C082 (b) | none | short interest, roster ownership (O01, O04) or any crowding measure never trigger a sale | convention | "I don't just sell something because people talk about pain trade" |
| S5 | Rbuy7; DRU4-C046 (b) | none | a stock sold may re-enter at the next quarter-end it passes, at any price; no cooling-off period and no reference to the sale price | convention | "be willing to buy something back higher than he sold it" |

A name that passes both branches is held under branch G rules while it passes G, else under C rules from its first
C entry date.

## 5. SIZE

| id | card rule, claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| Z1 | Rsize1; DRU2-C039 (b), DRU3-C029 (b), DRU4-C054 (b) | target weight of a full position | 15% of the paper portfolio; at most 6 full positions (floor 100 / 15) | quote (15-20%; lower end) | "15-20% of the asset base in a position"; concentrated "fat pitches"; the lower end because the quote does not say it is an equity figure and his equity bets are the smaller ones (Rsize4, Rsize5) |
| Z2 | Rsize6; DRU4-C033 (b), DRU6-C038 (b) | weight of a new entry | one third of Z1 = 5% | quote ("a third of a position") | "start with a meaningful but not Earth shaking position, normally about a third" |
| Z3 | Rsize7; DRU6-C014 (b), DRU6-C038 (b) | P02 at the next quarter-end | a name held from the previous quarter that still passes its branch and has P02 > 0 is raised to 15% | convention | "add when the thesis catches on and momentum turns his way": still passing = thesis holding, positive recent trend = momentum his way (for branch C inside 12 quarters, P02 > 0 is the add signal only; S3 decides the sale) |
| Z4 | Rsize5, Ravoid2; DRU6-C045 (b), DRU6-C033 (b); Rsize1 DRU2-C039 (b) | weight at a quarter-end | trim any name above 20% back to 20%; never let one name reach 30% | quote (20% top of the stated range; 30% "never") | the stated range caps a position at 20%; 30% is the "never" |
| Z5 | Rsize2; DRU3-C030 (b), DRU1-C035 (b), DRU2-C026 (b) | unfilled slots | weight not in stocks is held in cash (T-bills); open slots are never filled with names outside the pass set | convention | "waiting for a fat pitch"; "keep cash for high-conviction bets"; no forced full investment |

Order each quarter-end: (1) apply S1-S3 to holdings; (2) raise eligible holdings to full (Z3); (3) add new entries at 5% (Z2) in
ranking order (section 6) while fewer than 6 names are held; at most 6 names, any mix of 5% and 15% (total stock
weight <= 90%); (4) trim (Z4); (5) rest in cash.

## 6. Ranking inside the pass set (for the paper portfolio of N names)

His stated preference: growth first ("bias toward growth", DRU2-C073 b; "the biggest money I've made in equities have
been in growth stocks", DRU2-C077 n), and size goes to what the trend confirms (Rsize7, DRU6-C014 b); big bets only in
liquid markets (Rsize4, DRU6-C031 b, DRU6-C032 b).

1. Branch G names before branch C names.
2. Inside branch G: P02 descending (trend confirming most strongly); ties by the larger of `GR3` and E04 descending
   (missing side ignored) [v2, C5].
3. Inside branch C: L02 liquidity descending (Rsize4: the larger bet goes where it can be traded); ties by L01c.
4. Holdings that still pass keep their place before any new entry (no swap of a held name for a higher-ranked new one;
   he sells only when the reason is gone, Rsell1).

N: decisive form N <= 6 (Z1). 13F form N <= 15 (section 8).

## 7. DECISIVE FORM (quote and convention numbers only)

Pass = ((B1 `GR3` >= 0.20 OR B6 E04 >= 0.20) AND B3 P02 > 0) OR (B4 sector in {10,15,20,25} AND B5 `IND_NI` < 0).
No price rule. A1 / Z4: weight < 30%, trimmed to 20%. Sell S1-S5 (S1 on B1 OR B6; S3 at 12 quarters). Size Z1-Z5
(entry 5%, full 15%, at most 6 names, rest cash). Ranking section 6.

Criteria per part (decisive): buy 5 (B1, B6, B3, B4, B5), price 0, avoid 1 (A1), sell 5 (S1-S5), size 5 (Z1-Z5).

## 8. FULL FORM (decisive + grid and revealed-13F versions; versions averaged with equal weight, none picked)

| id | replaces | values to average | TAG | source |
|---|---|---|---|---|
| F1 [v2, C1 C2 C5] | branch G growth condition | (a) `GR3` OR E04 >= 0.20 (decisive); (b) `GR3` AND `GR1` >= 0.20 (v1 decisive reading); (c) G02 3-year EPS growth OR E04 >= 0.20; (d) `GR3` alone >= 0.20 | grid | Rbuy3 "which growth not specified" (card section 6); E04 reads Rbuy2 (12-24 months ahead, DRU4-C037 b, DRU2-C036 b); (d) = the trailing-only reading |
| F2 | B1/B6 upper bound | none (decisive); <= 0.30 on the measure that passes (pass only 20-30%) | grid | DRU5-C015 "20 to 30 percent", literal band |
| F3 | B3/S2 trend window | P02 > 0 (decisive); P01 > 0 | grid | Rbuy5 no lookback stated |
| F4 [v2, C3] | B5 loss level | `IND_NI` < 0 (decisive); (b) `IND_EBIT` < 0 (v1 decisive reading); (c) company R08 EBIT TTM < 0 (card proxy "earnings ... from loss") | grid | Rbuy8 gap "company or industry, operating or net" |
| F5 | B4 cyclical set | {10,15,20,25} (decisive); {10,15,20}; {15} (chemicals' sector only) | grid | Rbuy8 "which industries count as cyclical" |
| F6 | branch C trend wait | none (decisive); also require P02 > 0 | grid | card item 14 open |
| F7 | S3 horizon | 12 quarters (decisive); 8 quarters | grid | DRU2-C075 "2 or 3 years" |
| F8 | Z1 full size | 15% (decisive, N <= 6); 20% (N <= 5) | grid | DRU2-C039 "15 to 20%" |
| F9 | Z1-Z4 13F construction | N <= 15 names (effective names 14.7); entry 2.0% (new position starts at 2.0%); full 6.7% (100 / 15); trim at 14% (largest weight) | revealed-13F | construction_13F.txt |
| F10 | holding limit | none (decisive); sell any name after 4 quarters if not re-passing as new (16% of 13F names still held after 1 year; median holding 2 quarters) | revealed-13F | construction_13F.txt |
| F11 | growth-branch holding cap | none (decisive); 16 quarters | grid | Rproc12 "big trends held two to four years" (DRU4-C029 b) |

## 9. Not computable (card rules no dictionary measure can express; not forced)

| card rule | reason |
|---|---|
| Rbuy1 own Treasuries before a bad outcome | not an equity; his own recession forecast |
| Rbuy2 invest on the world 12-24 months ahead | his own forecast of the world is not observable; read only through the consensus growth of the stock (B6), which is the market's estimate, not his [v2: partly used, B6] |
| Rbuy4 long disruptors in tech | no measure of disruptor vs disrupted |
| Rbuy6 enter no later than the second inning | no measure of a thesis's stage |
| Rbuy9 business "much much better" in 3-5 years | judgement; no 3-5 year forecast measure (consensus long-term growth would duplicate B1 / B6) |
| Rbuy10 analyst idea that fits the macro matrix | no measure of the matrix or the idea |
| Rbuy11 Bitcoin or gold under loose policy | not an equity; phases undefined |
| Ravoid1 not for falling less | a motive, not a stock property (kept as design constraint, section 3) |
| Rsell2 sell or add after 2-3 weeks of homework | below the quarterly clock; outcome of private work |
| Rsell3 clean house when unsure | his confidence; no measure |
| Rsize3 spread over five asset buckets | other asset classes; the 13F shows equities only |
| Rsize4 big bets only in liquid markets | beyond the 1,500-largest universe no rule; used only as the branch-C ranking key (section 6) |
| Rsize8 do not pile on in the third to fifth inning | stage of a thesis not measurable |
| Rsize9 hot / cold dial | no definition of hot or cold (card section 6) |
| Rsize10 more cautious when risk/reward is dodgy | no measure |
| Rsize11 no big bet on a small move | needs his expected move |
| Rsize12 size up a hot analyst | analysts not observable |
| Rproc1-Rproc11, Rproc13-Rproc19 (18 rules) | macro, indicator and working-habit rules: not stock properties (Rproc4's leading-industry signal is computable from prices but has no turn definition and no stated link to which stocks to buy) |

Used: Rbuy2 (B6, partly), Rbuy3, Rbuy5, Rbuy7, Rbuy8, Ravoid2, Rsell1, Rsell4, Rsell5, Rsize1, Rsize2, Rsize5, Rsize6,
Rsize7, Rsize4 (ranking only), Rproc12 (grid only).

## 10. Coverage and fitting risk

Coverage of the card's buy rules (decisive form): the entry screen implements 4 of 11 (Rbuy3, Rbuy5, Rbuy8, and
Rbuy2 partly through B6 = 36%; v1: 3 of 11, 27%); with the re-entry rule (Rbuy7, S5) 5 of 11 (45%). The six others
(Rbuy1, Rbuy4, Rbuy6, Rbuy9, Rbuy10, Rbuy11) are macro, non-equity or judgement rules. The full form adds nothing new
to buy coverage.

Risk that v2 fits his purchases rather than his words: all three substantive changes were made after seeing that
branch G rejected 85.5% and branch C 97.8% of his purchases, and all three loosen the screen, so each carries some of
that risk even though each rests on a quote and no number moved. The largest is **C2 (B6, consensus forward growth)**:
the quotes say he invests on the situation 12-24 months out, but they say it is HIS view, and v1 judged consensus to
read it "only partly"; moving it into the decisive form as an OR adds exactly the high-expected-growth names a
momentum-led growth buyer tends to hold, so a recall gain from C2 may reflect that consensus and his purchases chase
the same popular stocks rather than that the recipe now reads his rule. **C1 (dropping the 1-year test)** carries
moderate risk: the quote names one rate and no second test, but "secular" can be read either way, and the v1 reading
stays as F1 b; the change cannot be separated from the fact that B2 rejected 67.9%. **C3 (net income instead of EBIT)**
carries the least: it is the more literal reading of "losing money", the threshold (0) and the industry level are
unchanged, but net income also turns negative on write-downs and interest in sectors that are not in a capacity
squeeze, which could let in industries his chemicals case does not describe; the v1 EBIT reading stays as F4 b. C4 and
C5 are consequential and add no new reading. Because B3, B4, the industry level of B5 and the 0.20 threshold were kept
despite their rejection shares, a v2 recall that still fails should be read as the card's limit (a macro trader's
equity sleeve chosen by theme and timing that no stock screen holds; card labelled thin with a FAILED held-out test),
not as a reason for a further revision.
