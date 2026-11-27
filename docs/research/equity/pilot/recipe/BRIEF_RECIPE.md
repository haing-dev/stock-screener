# Brief: recipe for Dev Kantesaria (gate G6)

Inputs (this folder only): CARD_v1.1.md (his card; label: held-out test FAILED, K174 merged), field_dictionary_v0.1.csv
and FIELD_DICTIONARY_v1.0.md (the measures we can compute for US companies at a quarter-end from first-reported
accounts, prices and consensus), construction_13F.txt (his 13F construction aggregates 2010-2025: number of names,
weights, holding periods; no returns).

Write RECIPE.md: the screen a machine applies at each quarter-end to the eligible US stocks (1,500 largest, GICS
sector known) to say which stocks pass his entry criteria, plus sell and size rules for a paper portfolio.
Five parts: BUY (what qualifies), PRICE (when cheap enough), AVOID (exclusions), SELL, SIZE.
For each criterion, one line: id | card rule(s) and claim ids it implements | measure id from the dictionary (or "new:
<exact formula from dictionary inputs>") | comparison and number | TAG | why this measure stands in for his words.
TAG is one of: `quote` (the number is in a cited claim), `convention` (a standard reading of his words when he gives no
number, e.g. "dominant" = top 2 market share is NOT computable, so say "not computable"), `revealed-13F` (from
construction_13F.txt), `grid` (several values to average, give them). Never tune a number to any outcome; you have none.
Rules:
1. Use only card rules (RB/RP/RA/RS/RZ/RO ids). A card rule that no dictionary measure can express is listed under
   "Not computable" with the reason; do not force it.
2. Prefer few criteria that he states firmly (strength always/usually) over many weak ones.
3. Industries he excludes (by GICS sector or industry) are AVOID criteria with the GICS names.
4. The DECISIVE form of the recipe uses only `quote` and `convention` numbers; list it separately from the full form.
5. Give a ranking rule inside the pass set (his stated order of preference) for the paper portfolio of N names.
6. End with: the share of his card's buy rules the recipe covers, and the main risk that the recipe selects a
   different kind of company than he does (one paragraph).
Work only in this folder. Reply with the criteria count per part and the "Not computable" count.
