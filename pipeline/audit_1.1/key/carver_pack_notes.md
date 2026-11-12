# Reduced Carver pack (work_c/pack.json): what is in it, what was dropped

Builder: key_7f3a/tools/build_carver_pack.py (seeded, re-runnable); full listing: key_7f3a/carver_pack_manifest.json.
Source: L0/vault/_data/foundation_packs/U02.json (513,213 bytes; 784 claims, 774 by Carver).

## Size
198,390 bytes (limit 200,000). One claim or post per line.

## Included
- unit id/name/topic; a neutral "about" paragraph explaining the layers (verbatim quote = script-checked; claim text
  and digest = machine-written, digest numbers unchecked); the 19 transcript source ids with approximate dates (taken
  from the synthesis views_timeline; MT002/MT029/MT134/MT155/MT221 partly "not given").
- 415 Carver claims, fields claim_id, speaker, quote, claim, conditions, correction (where present). Quotes are
  byte-identical to the source pack (asserted in the builder):
  - 315 hit at least one of ten topic regexes run over quote + claim + conditions + indicator of ALL 774 Carver claims
    (my own search, not the note's citations; hit counts Q1 51, Q2 86, Q3 34, Q4 14, Q5 51, Q6 11, Q7 19, Q8 25, Q9 26,
    Q10 64; overlapping). The regexes were widened once after reading the dropped list for misses (short-sample,
    risk-target and multiplier terms).
  - 1 more forced because the note cites it for a key statement (MT128-C03-3, silver trade prices; no topic hit).
  - 99 unrelated Carver claims drawn at random (seed 20261112) as filler so the pack does not spoon-feed the topics
    (about a quarter of the claims).
- 21 blog-digest posts that bear on the ten topics: B01 B02 B03 B04 B05 B06 B08 B11 B12 B13 B14 B17 B19 B21 B22 B24 B25
  B26 B27 B29 B31 (complete, unedited).

## Dropped
- The Sonnet-written investor synthesis (all prose: one_paragraph, core_beliefs, mechanisms, playbook, evidence_style,
  views_timeline text, disagreements, internal_tensions, testable_hypotheses, blind_spots, reader_inferences); only
  source ids and dates kept.
- All 10 claims by other speakers (host Niels Kaastrup-Larsen): MT010-C15-3, MT026-C02-3, MT026-C17-1, MT044-C11-2,
  MT106-C05-X1, MT106-C17-2, MT128-C06-1, MT137-C05-1, MT196-C04-2, MT196-C04-7. None is needed for a question about
  Carver's own position.
- 359 Carver claims with no topic hit and not drawn as filler (macro views, crypto, gold, replication, careers, AI,
  allocation advice, etc.).
- Fields mechanism, indicator, time_bound, quote_check from every claim (labels only; all included quotes were
  "exact" or added from maps).
- 10 digest posts that do not bear on the ten topics: B07 (rule performance 2022), B09, B10 (handcrafting follow-ups),
  B15, B16, B18 (skew as a signal), B20 (optimisation/leverage), B23 (absolute vs relative momentum), B28 (kinds of
  overfitting), B30 (very slow mean reversion).
- The U02 note and every other foundation note (not in work_c/).

## Coverage check
Every id the U02 note cites for the ten key statements is in the reduced pack: 38 of 38 claim ids and 17 of 17 post
ids (B01 B02 B03 B04 B05 B06 B11 B13 B17 B21 B22 B24 B25 B26 B27 B29 B31). Nothing had to be left out for size.

## Caveats for scoring
- The re-derivation sees fewer unrelated claims than the note's author did (415 vs 784), and no synthesis prose; it
  cannot be faulted for citing nothing outside the reduced pack. If it cites an id not in the pack, that is an error.
- Topic regexes are keyword-based; a relevant claim phrased without any keyword may be missing. Where the re-derivation
  says "the pack does not show this" and the full U02 pack does show it, check that claim against the manifest before
  scoring it as a re-derivation error.
