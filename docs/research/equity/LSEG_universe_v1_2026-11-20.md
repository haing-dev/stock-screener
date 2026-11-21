# LSEG universe file 1: what came back (2026-11-20)

Workbook `LSEG_universe_v1.xlsx` (105 formulas; on the PC in `G:\My Drive\Screener project\LSEG\01_universe`),
refreshed and saved by the user; read with the probe reader (report `tools/bbgq/results/lseg_universe_v1.txt`)
and a join of the list blocks (counts only here; the joined list stays on the PC).

## Company lists
- Datastream dead lists `DEADUS1`-`DEADUS10` (8-10 were guesses and work) and research lists `FAMERA`-`FAMERZ`:
  82,564 codes, 2,550 without details. US common shares (type EQ, major listing): 33,234; of these 17,423 whose
  last exchange is NYSE / Nasdaq / NYSE American, 14,256 whose last exchange is over the counter.
- Main-exchange set alive at each 1 January: 3,882 (2010), 3,740 (2012), 3,889 (2015), 3,846 (2018), 4,105 (2021),
  4,463 (2024). Dead per year about 120-320.
- Check with 11 known dead companies: 4 found on a main exchange (Celgene, Monsanto, Linear, Activision); 4 found
  but listed as over the counter because they traded there after failing (Sears, SVB, Bed Bath & Beyond, First
  Republic); 3 NOT in any list (Twitter, Time Warner, Whole Foods), although their data work by ISIN.

Consequences:
1. The exchange field is the LAST exchange, so failed companies would be dropped. The candidate set must keep
   over-the-counter companies; the monthly price, size and volume rule (R3) then decides when each one is in.
2. The Datastream lists are not complete (3 of 11 missing; all three were taken over at large size). A second,
   independent list is needed: the SEC's quarterly list of 13(f) securities (public, every exchange-listed US
   stock by CUSIP, from 2004; CUSIP converts to ISIN), merged with the Datastream lists, and checked per year
   against CRSP counts on WRDS (a count-only job).

## Retests
| Item | Result |
|---|---|
| Goodwill | `TR.F.GoodwNet` empty for GE and Kraft Heinz too: name still open (intangibles total works) |
| Minority interest | `TR.F.MinIntrEq` works |
| Preferred equity | `TR.F.PrefShHoldEq` works (only for companies that have it) |
| Net debt issuance | `TR.F.DebtLTSTIssuanceRetTotCF` works; debt issued `TR.F.DebtIssuedLTCF` works |
| Trade receivables | `TR.F.TradeAcctTradeNotesRcvblNet` works |
| Interest expense | `TR.F.IntrExpn` works on GE / Kraft Heinz |
| D&A | `TR.F.DeprAmort` sparse; keep `TR.F.DeprDeplAmortCF` |
| Short interest history | Workspace `TR.ShortInterest` with `Frq=M` works from 2010-01 (Apple), twice a month with `Frq=D`. Datastream `SHORTINT` gave no values |
| Ownership | `TR.CategoryOwnershipPct` with `TR.InstrStatTypeValue` gives the percentage by holder category; Datastream `NOSHST`, `NOSHEM`, `NOSHIC`, `NOSHOF` (strategic, employee, investment-company, officer holdings) work monthly from 2009. Other guesses failed |
| Datastream codes, GICS / SIC by year | Failed in this refresh (Datastream session error on single-series blocks) |

Field dictionary: 51 of 52 raw items now have a working name (goodwill open).
