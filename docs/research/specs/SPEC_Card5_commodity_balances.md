# Pod spec: Card 5, commodity balances (Pierre Andurand)

> **Status (2026-11-23): APPROVED WITH CORRECTIONS at step 3.2.** Written at step 3.1 (Opus, agent C); checked by a
> fresh Opus agent (checks/CHECK_3.2_C.md); its 6 corrections to this spec are applied. Claim ids and quotes
> script-checked (ALL OK). Nothing registered or run; open items go to step 3.4 (check section 4, NOTES_3.1_agent_C.md).

Step 3.1, Agent C, 2026-11-23. Nothing here is registered or run. Sources: CARD_1.4_commodity_balances.md (final text,
33 corrections applied) and its check; THESIS_REGISTER_1.5.md rows T34-T36; code read in gm/panel.py, gm/signals.py,
gm/book.py, gm/vol.py, gm/config.py. "Closed here" marks a choice the notes left open. [P] = MT115, identity probable.

## 0. Header

| Item | Value |
|---|---|
| Pod name | Card 5 commodity balances |
| Type | discretionary pod = rule layer (R1 only; R2 held back) + shadow analyst |
| Register rows | T34 R1 Range break where supply is slow, T35 R2 Paper fall in a tight market (held back), T36 analyst layer |
| Source notes | card 5 sections 2 (chains 1-8), 4 (R1, R2), 5, 6 (process), 7, 8, 9, 10 (D1, D2), 13; check sections 2-4 |
| Register status | rule layer in Batch B2, Incubator at best, only if C5-D2 passes and C5-D1 does not call R1 a Trend duplicate; R1's prices are LSEG only (not registered) |
| Dating class | C for R1 and R2 (register column 8; card s9: nothing documented before 2011); n/a for the analyst |
| What rule 5 allows | no holdout verdict; descriptive only; best class Incubator; Core impossible |

## 1. Economic claim

Supply growth against demand growth sets the direction of inventories, and "the price should move in order to keep the
the inventories within kind of uh kind of in range that makes the market function" (MT124-C04-1). Where demand cannot
flex and new supply takes years, the move is large, and range traders "don't really ask themselves what makes that
price right" (MT123-C04-2): they pay when a break carries far. R1 codes only the price side of this (a new high after a
long range) in markets with slow supply.
Evidence (card labels): chain 1 ASSERTED, one recalled case with a number; chain 2 SHOWN for cocoa's arithmetic,
ASSERTED for copper; R1 has no grade word and one live case (cocoa 2024) with no score (register T34); "For copper he
names a fast supply response too" (card s13).

## 2. What is predicted

| Rule | Quantity | Sign | Where largest |
|---|---|---|---|
| R1 | monthly excess return of the triggered market (cm_copper; cm_wti in the crude version) over 24 or 36 months after the last trigger | positive | where supply is slowest; while the real price is still below its earlier real peak |
| Analyst | probabilities, section 3A, 4 and 13 weeks | as stated | n/a |

## 3. Signal

Common (card s4): checked at each month end with data as known then; panel markets as excess returns; equal risk;
opposite positions net; four weekly tranches (charter s4; design runs tranche 0, weekly check 1990-2010); every version
run and averaged. P = the month-end close of the front contract on LSEG commodity futures curves; "a market without an
LSEG curve or a panel return is out" (card s4; this binds, see section 15).

R1 Range break where supply is slow.
1. P(t) = LSEG continuous front contract (c1) month-end close as LSEG serves it (closed here: one series for history and
   live; check JP4). Reported line: P against FRED PCOPPUSDM for copper, to show roll jumps.
2. Trigger month t: P(t) > every earlier month-end P of the series, and at least 120 month-end values exist before t
   (reader's proxy for a break; card s4).
3. Position: long from the trigger month until H months after the last trigger month; H = 24 or 36.
4. Real-ceiling version: the run ends early at the first month u at which P(u) / CPILFESL (lag 1, first published as in
   card 1) exceeds the highest value of P / CPILFESL over all months before the run's first trigger month (closed here:
   "its own earlier high" = the real peak before the break). After such an exit the market stays flat until a new run
   starts with a trigger month whose real price is not above that earlier real high.
5. Markets: copper (cm_copper) always; crude (cm_wti) in the crude version. Closed here: WTI, the panel's crude with the
   longest LSEG curve (1983) and an EIA cross-check; Brent (1988) not added. Code facts: the panel holds no cocoa and no
   base metal but copper (panel.py COMMOD, register D11), so cocoa and the LME metals are out of R1 by the card's own
   market rule. Caveat from the code: gm/bloomberg.py ALT_COMMOD includes cm_cocoa, cm_alu, cm_zinc, cm_nickel, cm_lead,
   which enter the panel whenever Bloomberg returns load (panel.py); the charter's A1 switches them off (register D4).
   Closed here: R1's market list is the slow-class markets in the panel as registered at 3.4 (copper, and WTI in the
   crude version, while A1's rule holds); an alternative commodity joins only if a registered Batch A item (charter D1,
   T09) has put it in the panel before B2 is registered, and 3.4 records the list.

R2 Paper fall in a tight market: HELD BACK, not built (card s4, check item 16). Release condition: a quote of Andurand in
a pack that supports buying a fall in a backwardated market; his action in the source case was "I want to to reduce my
positions" (MT125-C08-7); step 1.5 searched MT115, MT123, MT124, MT125 and found none. If released, its rule text is
card s4 R2 as drafted (crude; front above second and a 10% one-month or 20% three-month fall; gap versions a, b; at most
12 months; 4 versions, 8 with sizing), registered as a new trial, and C5-D1's R2 part then gates it (under 50%: not
registered).

Sizing version (card s6): notional = min(volatility-sized notional, notional at which a 50% adverse move costs one year
of the rule's volatility budget), "be able to take a 50% move" (MT123-C05-7). With unit u = 0.40 (section 5) the cap is
2u of notional, which binds whenever the market's volatility is below 50% a year.

3A. Analyst layer (card s5; W3). Weekly snapshot plus public reports, blind, model id logged; each answer cites its
public source and date; probabilities at 4 and 13 weeks; Brier score against the base rate on LSEG front contracts (WTI,
copper, cocoa) unless stated.
1. Oil stocks against the seasonal norm; WTI higher. 2. Gap between the first and second WTI contract wider. 3. For each
disruption in the news: have exports fallen (yes with a figure, no, unknown); WTI above its pre-event level at 13 weeks.
4. Stated spare capacity and reserve releases; the main producer group announces higher output within 13 weeks.
5. UNRATE against its 12-month low: gap 0.5 or more at 13 weeks (with whether the rise looks large) and WTI lower.
6. Oil moved 9% or more in a day, or 20-day volatility twice its one-year average: half the move reversed (covers R2
while held back). 7. Speculative net length in oil, copper, cocoa against a year ago: the last 13 weeks' price direction
continues. 8. Copper exchange stocks against the start of the year: copper higher. 9. Cocoa inventory to grinding ratio
against his markers 19% and 13%: cocoa higher. 10. Price over CPILFESL as a share of its earlier real peak for oil,
copper, cocoa: higher at 13 weeks.
A view is marked "not understood" when price moves against it by more than one monthly standard deviation with no cause
it can cite; such views are scored apart (card s6). Open forecasts F1-F3 go to the ledger.

## 4. Markets

| Market | Role | Earliest usable design month |
|---|---|---|
| cm_copper (P: LSEG COMEX copper c1; returns: panel) | R1 | P history from 1973 (digest: metals curves from 1973), so the first possible trigger is the 121st month of P, about 1983; returns: cm_copper's panel source, which in the free engine covers only about 89 design months (engine_ref.json market_months, so from about 2003; no World Bank spot, panel.py ALLOW_AVG off): copper runs before then earn nothing unless A1's Bloomberg swap has given cm_copper a GSCI excess-return history before B2 is registered (3.4 records which) |
| cm_wti (P: LSEG CL c1; returns: panel, EIA contracts (cm_wti has 311 design months in engine_ref.json, so from 1985)) | R1 crude version | first possible trigger about 1993 (LSEG WTI from 1983 plus 120 months) |
| cocoa, LME aluminium, zinc, nickel, lead, tin | not traded; C5-D2 reported line only (section 13) | LSEG: London cocoa from 1974; LME via Datastream from 1970 (digest) |
| wheat, corn, soybeans | C5-D2 comparison class only | LSEG grain curves from 1973 (digest) |

## 5. Sizing

1. Volatility: engine hybrid estimate (gm/vol.py, CANDIDATE "hybrid") on the panel return of the market.
2. Position while on = 0.40 / vol per triggered market (engine convention); each triggered market is one unit (closed
   here: markets are triggered separately). Sizing version: notional capped at 2 x 0.40 = 0.80 (section 3).
3. Rule position = mean over versions; pod = R1 (one rule). No trailing rescaling (closed here, as card 1).
4. "no short while the front is above the second contract" (card s6) binds nothing in R1 (long only); passed to Agent A
   as a note for Trend and Value.
5. Pod into the book: WORKFLOW 5.1 vs config.py CANDIDATE family_w (no card pod): shadow only; share, caps, netting
   for 3.4. The card's conflict with volatility sizing (chain 7, register C15) is answered only by the sizing version.

## 6. Version grid

| Knob | Values |
|---|---|
| H | 24 / 36 months |
| Crude | out / in |
| Real-ceiling exit | off / on |
| Versions | 8 |
| With the 50% sizing version | 16 |

Averaged with equal weight. Gates: C5-D2 fail drops R1 unbuilt (all versions); C5-D1 at 75% or more: R1 not
registered. Held back, not counted: R2 (4, 8 with sizing).

## 7. Sample

Design window: from the first month a copper trigger can be evaluated (121st month of LSEG copper P, about 1983; at least
half the versions use copper only) to 2010-12; crude versions add WTI from its 121st month. A run open at 2010-12 is
measured to 2010-12 only. C5-D2 counts breaks up to 2008-12 only (card s10, so that every 24-month outcome ends inside
the design months). Eras 1975-89 (short: about 1983-89) and 1990-2010, reported. Never 2011 or later.

## 8. Data

| Input | History, first date | Live, delay | Licence |
|---|---|---|---|
| LSEG front contracts (COMEX copper, NYMEX WTI; for D2 also cocoa, LME cash, grains) | LSEG Datastream, 1970-83 per market (digest); contract codes fixed at registration | LSEG on the user's PC, not registered as live | LSEG, not registered |
| Panel returns cm_copper, cm_wti | free panel (free engine: copper from about 2003, WTI from 1985; engine_ref.json) | free daily closes, 1 day | free |
| CPILFESL (real-ceiling version) | FRED / ALFRED first-published | FRED, lag 1 | free |
| Analyst: EIA, CFTC, exchange stocks, ICCO, UNRATE, LSEG fronts | live public reports | public / LSEG | mixed |

Rule 7: P has no registered live source, so R1 cannot be Core; it cannot be Core in any case (dating class C).
Pack note: the panel uses no monthly-average spot returns (panel.py ALLOW_AVG off), so TESTING_PROTOCOL's false-trend warning does not apply to these returns;
the copper return source by period is in the panel's SRC record and must be reported with any R1 result.

## 9. Costs

gm/book.py cost_bp: cm_wti 4.0 bp one way, 12 rolls a year; cm_copper 4.0 bp, 5 rolls; charged as in book.run.
Turnover: very low (a run lasts at least 24 months; card horizon "a few months or a few years", MT124-C02-X1). The
double-cost test applies.

## 10. What would prove it wrong

Fixed now, on the design window:
- C5-D2 fails (the slow class does not break further than grains): R1's only thesis, the class filter, fails (card).
- R1's mean excess return over held months is zero or less; or its gain comes only from months in which the 12-month
  Trend versions are long the same market (then it is "Trend with a longer leash", card s13).
- Card s8, in his own terms (for the analyst and the live record): inventories reach his markers and price does not go
  non-linear; or "a bumper crop in West Africa next year" (MT123-C06-1) takes cocoa back down.
- Loss path (P3): R1 loses most when a break reverses fast through supply that answers sooner than he expects (copper
  scrap: "when prices go up you get more scrap Supply", MT123-C09-2) or a large recession ("so not small recessions but
  large recessions", MT124-C08-1); a copper high followed by a fall is in the window (2008). Flag "loss not seen": no.
- Analyst: Brier score no better than the base rate at the registered live checkpoint.

## 11. When it should stop working

Card s8: supply gets faster or cheaper (the 2014 point from gas, [P], claim text); governments clear the market by
mandate, release or cap instead of price; the market is too thin for price to inform ("then the price doesn't mean
anything", MT125-C08-5); long-horizon money arrives and prices deficits early. Live review conditions, reported, not
switches.

## 12. Knobs that were tuned

| Knob | Origin |
|---|---|
| Trigger: new all-time month-end high | reader's proxy (he enters on the balance) |
| 120 months of history | reader (card 2's minimum) |
| Slow class: base metals and cocoa, not grains, not precious metals | quotes on lags (MT124-C10-3, MT123-C08-4, MT123-C07-2); exclusion of precious metals is the reader's |
| H 36 | cocoa's three years (MT123-C07-2); below his metals lag of "at least five years" (MT124-C10-X1) |
| H 24 | reader |
| Crude version | quotes pull both ways: "seven years time" (MT124-C10-4) and "only the u.s has a shorter cycle of probably 12 months" (MT124-C11-1) |
| Real ceiling, CPILFESL deflator | his yardstick; its use as an exit and the deflator are the reader's |
| 50% sizing | quote (MT123-C05-7); "one year of the budget" reader |
| WTI as the crude, c1 as served, run-start real high | closed here |

Chosen after seeing design results: 0. Chosen with sight of post-2010 history: none flagged by the card; the rule rests
on 2022 and 2024 statements.

## 13. Gating diagnostics

Zero slots, no returns of the rule read.
- C5-D2 premise of the class filter (gates R1). Count range breaks (first trigger month after at least 12 months without
  one) up to 2008-12 in the slow class and in wheat, corn and soybeans; measure the share of breaks with P higher 24
  months later. Gate: slow class at least 15 points above grains, with at least 10 breaks in each class; else R1 is
  dropped unbuilt; too few breaks counts as not passed. Slow class closed here: the markets R1 can trade (copper;
  crude reported apart, as the card says), because the gate decides whether R1 is built. Reported line, no gate: the
  same count on LSEG cocoa and the LME cash prices. Likely outcome named by the check: with copper alone the floor of 10
  breaks fails and R1 is dropped (check JP3).
- C5-D1 overlap (gates R1). Share of R1's on-months (closed here: months in which any version holds a position, because trigger months are new all-time highs at which every 12-month Trend version is long by construction) in which the Trend versions with the longest lookback (12 months,
  all their shape and volatility versions) are long the same market by their average sign. 75% or more: R1 is not
  registered. R2 part reported only while R2 is held back. Reported: overlap with card 1 R4-B.
Sealed months: C5-D2 is cut at 2008-12 by the card; C5-D1 reads positions only. None reads 2011.

## 14. Overlaps

Re-checked against the code:
- Trend: long copper or WTI at a new high in most cases (book.trend_signal, positive 1/3/12-month returns), but it exits
  when its returns turn, while R1 holds 24-36 months (C5-D1 measures it).
- Value: signals.value_values computes a commodity 5-year reversal, but book.family_positions keeps Value to fx_, bd_,
  eq_ ("commodity value: failed, out"), so Value holds no commodity in the book. The card's "Value leans against what
  has risen far" therefore does not hold in the code: no Value opposition to R1 (register D7 settled by book.py).
- Carry: carry_values takes EIA F1/F2 slope for cm_wti and, wherever Bloomberg curves load, a Bloomberg curve carry for
  non-energy commodities, copper included (BBG.CURVE_ROOT; register D6). So Carry may hold copper long in backwardation
  during an R1 run; the overlap depends on the Bloomberg switch Agent A must fix.
- Economic trend: commodities get the global (US, DE, JP, CN) inflation, trade, monetary and risk themes (SIGNS CM).
  The card's four duplicates: inflation so long commodities IS held (inflation theme +1); higher rates with dear energy:
  the monetary theme is short commodities after rate rises (CM monetary -1), partly held; a large recession so short oil
  and China reopening are NOT held (no growth theme; config.py econ_themes). 3.2 re-files them (register T106, C1).
- Card 1 R4-B holds all panel commodities long while its inflation state is on: overlap reported in C5-D1.
- Curve carry (Agent B) trades the same curves; R1 uses only the front price, not the spread.

## 15. Open choices

| # | Choice | Closed how |
|---|---|---|
| 1 | Per-class lag version (36 cocoa, 60 metals) (check JP1) | not added: the brief takes versions from the notes and register (R1 = 8); with cocoa out, a 60-month version would be the metals lag; recorded for 3.4 |
| 2 | Crude in the slow class (JP2) | kept as a version (card text); whether it belongs: 3.2 |
| 3 | Which base metals have a curve and a panel return (JP3) | code: copper only while A1 keeps Bloomberg alternative commodities off; the card's rule binds (section 3); C5-D2 on R1's registered markets (section 13); list fixed at 3.4 |
| 4 | Roll convention (JP4) | rule: LSEG c1 as served, with a PCOPPUSDM cross-check line |
| 5 | Economic trend duplicates (JP5) | code facts in section 14; 3.2 re-files |
| 6 | R2 release (JP6) | release condition in section 3 |
| 7 | Ledger rescoring (JP7) | 2.3 |
| 8 | Deflator (JP8) | rule: CPILFESL as the card writes it; not a version (brief: versions from the notes only) |
| - | Register vs note | the register calls "whether a panel return binds" an open choice; the note's final text says a market without a panel return is out, so it binds (note wins) |

## 16. Builder must not change

Sign (long only); the trigger (all-time month-end high after 120 months), H, the real-ceiling rule and the crude
version; markets as fixed at 3.4 (copper, and WTI in the crude version, unless a registered Batch A item has added a slow-class market, section 3); the window and the D2 cut at 2008-12; the grid of section 6 (8 versions, 16 with
sizing), averaged; LSEG c1 for P and panel returns for P&L; engine costs and the double-cost test; R2 stays held back.
